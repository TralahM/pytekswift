"""tekswift cli (command line interface)."""
import argparse
import yaml
from tekswift import dataloader
from tekswift.utils import transform_country_data, bin_to_swifts


def bin2swift_lookup(args: argparse.Namespace):
    """Return the Swift codes for the matching issuer."""
    swifts, bin_data, pmap = bin_to_swifts(args.bin_code, args.threshold)
    bin_data["swift_data"] = swifts
    print(yaml.dump(bin_data))
    if args.verbose:
        # [print(f"{k}: {b}") for k, b in pmap.items()]
        print(pmap)
    # print(yaml.dump(swifts))
    return


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
    bin_sp = subparsers.add_parser(
        "bin",
        aliases=["bn"],
        help=bin2swift_lookup.__doc__,
    )
    bin_sp.set_defaults(func=bin2swift_lookup)
    bin_sp.add_argument(
        "-p",
        "--probability-threshold",
        action="store",
        default=0.8,
        dest="threshold",
        help="threshold to use as a filter bettween [0,1].",
        type=float,
    )
    bin_sp.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        dest="verbose",
        help="be verbose.",
    )
    bin_sp.add_argument("bin_code", help="Bank Indetification Code.")
    return parser


def main():
    """Run main cli entry point."""
    parser = get_main_parser()
    args = parser.parse_args()
    args.func(args)
    return
