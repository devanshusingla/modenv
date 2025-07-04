import argparse

from modenv.parser.layer import register_layer
from modenv.parser.doctor import register_doctor
from modenv.parser.spec import register_spec
from modenv.parser.static import register_static


def get_main_parser():
    parser = argparse.ArgumentParser(
        prog="modenv", description="Manage layered Python virtual environments."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    register_layer(subparsers)
    register_doctor(subparsers)
    register_spec(subparsers)
    register_static(subparsers)

    return parser

