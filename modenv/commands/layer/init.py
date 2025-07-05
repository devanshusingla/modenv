def register(parser):
    parser.set_defaults(func=run)

    parser.add_argument(
        "--venv",
        type=str,
        help="Path to the virtual environment to initialize (default: auto-detect from current path)"
    )

    parser.add_argument(
        "--python-version",
        type=str,
        help="Python version string (e.g. 3.11). Required if --venv is passed and current directory is not inside the venv."
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-initialization. Overwrites existing .modenv config and .pth file."
    )

    parser.add_argument(
        "--no-pth",
        action="store_true",
        help="Do not write a .pth file (config-only mode)."
    )

    parser.add_argument(
        "--pth-name",
        type=str,
        default="modenv_layer.pth",
        help="Name of the .pth file to write in site-packages (default: modenv_layer.pth)."
    )

    parser.add_argument(
        "--config-dir",
        type=str,
        help="Override subdirectory name inside .modenv/ (default: pythonX.Y)."
    )

    parser.add_argument(
        "--parents",
        nargs="*",
        type=str,
        default=[],
        help="List of parent layer paths to include during initialization."
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without writing files."
    )

    parser.add_argument(
        "--silent",
        action="store_true",
        help="Suppress non-error output."
    )

def run(args):
    print("Running: layer init")

