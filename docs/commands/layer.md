# modenv layer

Manage a virtual environment as a layer.

## init
Initialize a layer in the current or specified virtual environment.

### Flags:
- `--venv PATH`: Target .venv directory (default: autodetect)
- `--python-version VERSION`: Python version to use if not running from within the venv
- `--force`: Overwrite existing config if present
- `--dry-run`: Show what would be done without modifying anything
- `--silent`: Suppress output
- `--no-pth`: Don't write the `.pth` file
- `--pth-name NAME`: Custom .pth file name (default: `modenv_layer.pth`)
- `--config-dir DIR`: Override `.modenv/pythonX.Y/` subdir
- `--parents PATHS`: Parent site-packages to link (space-separated)

## parent add
Link a parent environment to the current layer.

### Flags:
- `--name`: Human-readable name of the parent
- `--priority`: Insertion priority (lower = higher precedence)

## parent remove
Remove a parent by name.

### Flags:
- `--name`: Name of the parent to remove
