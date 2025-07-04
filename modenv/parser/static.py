def register_static(subparsers):
    subparsers.add_parser("graph", help="Visualize environment graph")
    subparsers.add_parser("inspect", help="Show current .venv resolution")

