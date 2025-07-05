from pathlib import Path
import tomllib
import tomli_w

class TomlConfigBase:
    def __init__(self, path: Path):
        self.path = path
        self.data = {}

    def load(self):
        if self.path.exists():
            with self.path.open("rb") as f:
                self.data = tomllib.load(f)

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("wb") as f:
            tomli_w.dump(self.data, f)

