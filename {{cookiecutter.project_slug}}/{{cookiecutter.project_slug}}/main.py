import argparse
import sys
from typing import Optional
from typing import Sequence

import {{cookiecutter.project_slug}}.constants as C
from {{cookiecutter.project_slug}}.commands.hello import hello

def add_filter_option(
    parser: argparse.ArgumentParser, choices=None, default=None
) -> None:
    """ Add the filter command to a parser. """
    parser.add_argument(
        "-f",
        "--filter",
        choices=choices,
        default=default,
        help="Filter the data for a specific attribute.",
    )


def add_output_option(parser: argparse.ArgumentParser) -> None:
    """ Add the output command to a parser. """
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        default="json",
        choices=["json", "text", "raw"],
        help="Specifies the output type. (json, text, raw)",
    )


def add_color_option(parser: argparse.ArgumentParser) -> None:
    """ Add the color command to a parser. """
    parser.add_argument(
        "-c",
        "--color",
        nargs="?",
        default="off",
        choices=["on", "off"],
        help="Color output. (on or off)",
    )

def main(argv: Optional[Sequence[str]] = None) -> int:
    """ Driver """
    argv = argv if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-V", "--version", action='version', version=f'%(prog)s {C.VERSION}')
    add_color_option(parser)
    add_output_option(parser)

    subparser = parser.add_subparsers(dest='command')

    # add hello command
    hello_parser = subparser.add_parser('hello', help='Run hello.')
    add_filter_option(hello_parser)

    # add help command
    help = subparser.add_parser("help", help="Show help for a specific command.")
    help.add_argument("help_cmd", nargs="?", help="Command to show help for.")

    if len(argv) == 0:
        argv = ['hello']
    
    args = parser.parse_args(argv)

    if args.command == "help" and args.help_cmd:
        parser.parse_args([args.help_cmd, "--help"])
    elif args.command == "help":
        parser.parse_args(["--help"])

    if args.command == 'hello':
        return hello()

if __name__ == "__main__":
    exit(main())
