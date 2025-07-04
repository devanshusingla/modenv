import sys
from modenv.parser.base import get_main_parser


def main():
    parser = get_main_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

