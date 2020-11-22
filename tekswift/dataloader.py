#!/usr/bin/env python
"""PyTekSwift.DataLoader.

DESCRIPTION OF dataloader MODULE:

Utility functions to read from the swift database files, lookup swiftcodes,
and lookup by countries.
"""

from yaml import load  # ,dump
import os

try:
    from yaml import CLoader as Loader  # CDumper as Dumper
except ImportError:
    from yaml import Loader  # , Dumper

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class InvalidCountryCode(Exception):
    """Exception Class for Invalid alpha_2,alpha_3 country codes."""

    pass


class InvalidSwiftCode(Exception):
    """InvalidSwiftCode Exception."""

    pass


def build_path(countrycode: str) -> str:
    """Build Path to YAML File."""
    countrycode = countrycode.lower()
    if not len(countrycode) >= 2:
        raise InvalidCountryCode("CountryCode Too Short <2")
    path = os.path.join(CURRENT_DIR, f"data/{countrycode[:2]}.yml")
    if not os.path.exists(path):
        raise InvalidCountryCode
    return path


def load_country_data(countrycode):
    """Return a Python Object from the loaded yaml countrycode data file."""
    path = build_path(countrycode)
    with open(path, "r") as fl:
        document = load(fl, Loader=Loader)
    return document


def isvalid_swiftcode(code):
    """Is swiftcode valid, 8 chars or 11 chars?."""
    if len(code) == 8 or len(code) == 11:
        return True
    else:
        return False


def countrycode_from_swiftcode(swiftcode: str):
    """Swift Code Structure.

    The previous edition is ISO 9362:2009 (dated 2009-10-01).
    The SWIFT code is 8 or 11 characters, made up of:

    4 letters: institution code or bank code.
    2 letters: ISO 3166-1 alpha-2 country code (exceptionally, SWIFT has assigned the code XK to Republic of Kosovo, which does not have an ISO 3166-1 country code)
    2 letters or digits: location code
        if the second character is "0", then it is typically a test BIC as opposed to a BIC used on the live network.
        if the second character is "1", then it denotes a passive participant in the SWIFT network
        if the second character is "2", then it typically indicates a reverse billing BIC, where the recipient pays for the message as opposed to the more usual mode whereby the sender pays for the message.
    3 letters or digits: branch code, optional ('XXX' for primary office)

    Where an eight digit code is given, it may be assumed that it refers to the primary office.

    """
    if not isvalid_swiftcode(swiftcode):
        raise InvalidSwiftCode(f"Invalid Swift Code {swiftcode}")
    return f"{swiftcode[4:6]}"


def lookup_swiftcode(swiftcode: str):
    """Get Details of provided swiftcode or None."""
    data = load_country_data(countrycode_from_swiftcode(swiftcode))
    swiftkey = swiftcode.upper()
    return data.get(swiftkey)
