# modenv spec

Import/export modenv configuration to/from a TOML spec file.

## export
Generate a TOML spec for the current layer (paths, parents, etc.)

## apply
Apply a TOML spec to the current layer.

### Flags:
- `--force`: Overwrite any conflicting data
- `--dry-run`: Preview the import without applying it
