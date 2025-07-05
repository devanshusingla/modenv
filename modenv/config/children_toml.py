from pathlib import Path
from modenv.config.base import TomlConfigBase
from modenv.models.child_entry import ChildEntry

class ChildrenToml(TomlConfigBase):
    def __init__(self, path: Path):
        super().__init__(path)
        self.data = {"children": []}

    def add_child(self, path: Path, name: str):
        resolved = str(path.resolve())
        if not any(c["path"] == resolved for c in self.data["children"]):
            self.data["children"].append({
                "name": name,
                "path": resolved
            })

    def remove_by_name(self, name: str):
        self.data["children"] = [
            c for c in self.data["children"] if c["name"] != name
        ]

    def get_all(self) -> list[ChildEntry]:
        return [ChildEntry(Path(c["path"]), c["name"]) for c in self.data["children"]]

    def find_by_name(self, name: str) -> ChildEntry | None:
        for c in self.get_all():
            if c.name == name:
                return c
        return None

