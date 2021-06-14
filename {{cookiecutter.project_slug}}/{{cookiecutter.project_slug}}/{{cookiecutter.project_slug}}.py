import argparse
import sys
from typing import Optional
from typing import Sequence

from {{cookiecutter.project_slug}} import constants as C
from {{cookiecutter.project_slug}}.commands.hello import hello


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-V", "--version", action='version', version=f'%(prog)s {C.VERSION}')
    
    subparsers = parser.add_subparsers(dest='command')
    hello_parser = subparsers.add_parser('hello', help='Run hello.')

    if len(argv) == 0:
        argv = ['hello']
    
    args = parser.parse_args(argv)

    if args.command == 'hello':
        return hello()

if __name__ == "__main__":
    exit(main())
