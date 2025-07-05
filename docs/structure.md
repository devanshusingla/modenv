# .modenv Directory Structure

Each virtual environment that is initialized with `modenv layer init` will have a `.modenv/` folder created at the root of the virtual environment (alongside `pyvenv.cfg`).

## Folder Layout

```
.venv/
├── pyvenv.cfg
├── bin/
├── lib/
│   └── python3.X/site-packages/
├── .modenv/
│   ├── python3.11/
│   │   ├── config.toml
│   │   ├── parents.toml
│   │   ├── children.toml
│   │   └── modenv_layer.pth
```

## Python Version Handling

- The subdirectory inside `.modenv/` is named `pythonX.Y`, derived from the Python version tag.
- This allows a single `.venv/` to support multiple interpreters (e.g. Python 3.10 and 3.11), keeping each metadata config isolated.
- All file operations reference the correct subfolder based on the active Python or the one provided via `--python-version`.
