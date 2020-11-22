"""tekswift cli (command line interface)."""
import argparse
import collections
import yaml
from tekswift import dataloader


def transform_country_data(country_data):
    """Return a new flattened representation of the swiftcode_data."""
    new_data = []
    for key, value in country_data.items():
        new_transform = collections.defaultdict()
        new_transform["swiftcode"] = key
        new_transform.update(value)
        new_data.append(new_transform)
    return new_data


def swift_lookup(args: argparse.Namespace):
    """Lookup the given SWIFTCODE in the database."""
    info = dataloader.lookup_swiftcode(args.swiftcode)
    print(yaml.dump(info))
    return


def country_lookup(args: argparse.Namespace):
    """Return details of all banks for the given country code."""
    country_data = dataloader.load_country_data(args.country_code)
    print(yaml.dump(transform_country_data(country_data)))
    return


def usage(args, **kwargs):
    """Handle Main repodoc Entrypoint without subcommands."""
    if args.bash_completion:
        import shtab

        print(shtab.complete(args.parser, shell="bash"))
        return
    if args.zsh_completion:
        import shtab

        print(shtab.complete(args.parser, shell="zsh"))
        return


def get_main_parser():
    """Return main argparse.ArgumentParser."""
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=usage)
    parser.add_argument(
        "-bc",
        "--bash-completion",
        help="Print Bash Completion Script.",
        action="store_true",
        dest="bash_completion",
    )
    parser.add_argument(
        "-zc",
        "--zsh-completion",
        help="Print ZSH Completion Script.",
        action="store_true",
        dest="zsh_completion",
    )
    subparsers = parser.add_subparsers(title="subcommands")
    lookup_sp = subparsers.add_parser(
        "lookup",
        aliases=["l", "lk", "get"],
        help=swift_lookup.__doc__,
    )
    lookup_sp.set_defaults(func=swift_lookup)
    lookup_sp.add_argument(
        "swiftcode", help="SWIFTCODE [8 or 11 alphanumeric].")
    country_sp = subparsers.add_parser(
        "country",
        aliases=["cn"],
        help=country_lookup.__doc__,
    )
    country_sp.set_defaults(func=country_lookup)
    country_sp.add_argument(
        "country_code", help="ISO-2 or ISO-3 Country Code.")
    return parser


def main():
    """Run main cli entry point."""
    parser = get_main_parser()
    args = parser.parse_args()
    args.func(args)
    return
