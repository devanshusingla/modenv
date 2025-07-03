import argparse
from stacked_venv.commands.stack import stack_venv
from stacked_venv.commands.list import list_stacked_packages

def main():
    parser = argparse.ArgumentParser(description="Layer Python virtual environments using .pth files")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # stack
    subparsers.add_parser("stack", help="Stack parent/user packages into current venv")

    # list
    subparsers.add_parser("list", help="List all packages visible in current stacked venv")

    args = parser.parse_args()

    if args.command == "stack":
        stack_venv()
    elif args.command == "list":
        list_stacked_packages()

