from modenv.commands.layer import init, unlink, list
from modenv.commands.layer.parent import add, remove


def register_layer(subparsers):
    layer_parser = subparsers.add_parser("layer", help="Manage .venv layers")
    layer_sub = layer_parser.add_subparsers(dest="layer_command", required=True)

    # layer init
    init_parser = layer_sub.add_parser("init", help="Initialize .venv layer")
    init.register(init_parser)

    # layer unlink
    unlink_parser = layer_sub.add_parser("unlink", help="Unlink this layer")
    unlink.register(unlink_parser)

    # layer list
    list_parser = layer_sub.add_parser("list", help="List parent layers")
    list.register(list_parser)

    # layer parent
    parent_parser = layer_sub.add_parser("parent", help="Manage parent layers")
    parent_sub = parent_parser.add_subparsers(dest="parent_command", required=True)

    add_parser = parent_sub.add_parser("add", help="Add parent layer")
    add.register(add_parser)

    remove_parser = parent_sub.add_parser("remove", help="Remove parent layer")
    remove.register(remove_parser)

