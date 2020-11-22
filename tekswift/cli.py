"""tekswift cli (command line interface)."""
import argparse
import yaml
from tekswift import dataloader


def swift_lookup(args: argparse.Namespace):
    """Lookup the given SWIFTCODE in the database."""
    info = dataloader.lookup_swiftcode(args.swiftcode)
    print(yaml.dump(info))
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
    return parser


def main():
    """Run main cli entry point."""
    parser = get_main_parser()
    args = parser.parse_args()
    args.func(args)
    return
