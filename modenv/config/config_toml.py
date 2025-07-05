from datetime import datetime
from pathlib import Path
from .base import TomlConfigBase

class ConfigToml(TomlConfigBase):
    def __init__(self, path: Path):
        super().__init__(path)
        self.data = {
            "modenv": {
                "version": 1,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "python_version": None,
                "site_packages": None,
            }
        }

    def set_metadata(self, python_version: str, site_packages: Path):
        self.data["modenv"]["python_version"] = python_version
        self.data["modenv"]["site_packages"] = str(site_packages.resolve())

    def get_site_packages(self) -> Path:
        return Path(self.data["modenv"]["site_packages"])

    def get_python_version(self) -> str:
        return self.data["modenv"]["python_version"]

