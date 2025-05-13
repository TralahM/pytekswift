"""tekswift package.

Defines:
    build_path,
    countrycode_from_swiftcode,
    load_country_data,
    isvalid_swiftcode,
    InvalidCountryCode,
    InvalidSwiftCode,
"""

# import
from .dataloader import (
    InvalidCountryCode,
    InvalidSwiftCode,
    build_path,
    countrycode_from_swiftcode,
    isvalid_swiftcode,
    load_country_data,
    lookup_swiftcode,
)
from .utils import bin_to_swifts


__all__ = [
    "InvalidCountryCode",
    "InvalidSwiftCode",
    "build_path",
    "countrycode_from_swiftcode",
    "isvalid_swiftcode",
    "load_country_data",
    "lookup_swiftcode",
    "bin_to_swifts",
]

__version__ = "0.1.6"

__author__ = "Tralah M Brian <https://github.com/TralahM>"
