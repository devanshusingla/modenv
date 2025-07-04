from modenv.commands.spec import export, apply


def register_spec(subparsers):
    spec_parser = subparsers.add_parser("spec", help="Import/export environment spec")
    spec_sub = spec_parser.add_subparsers(dest="spec_command", required=True)

    export_parser = spec_sub.add_parser("export", help="Export spec")
    export.register(export_parser)

    apply_parser = spec_sub.add_parser("apply", help="Apply spec")
    apply.register(apply_parser)

