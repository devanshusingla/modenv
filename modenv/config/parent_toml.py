class ParentsToml(TomlConfigBase):
    def __init__(self, path: Path):
        super().__init__(path)
        self.data = {"parents": {}}

    def add_parent(self, path: Path, name: str, priority: int):
        key = str(priority)
        self.data["parents"][key] = {
            "path": str(path.resolve()),
            "name": name
        }

    def remove_by_name(self, name: str):
        self.data["parents"] = {
            k: v for k, v in self.data["parents"].items()
            if v["name"] != name
        }

    def find_by_name(self, name: str) -> tuple[int, ParentEntry] | None:
        for prio, entry in self.get_all():
            if entry.name == name:
                return prio, entry
        return None


    def get_all(self) -> list[tuple[int, ParentEntry]]:
        return sorted(
            [(int(p), ParentEntry(Path(info["path"]), info["name"]))
             for p, info in self.data["parents"].items()],
            key=lambda x: x[0]
        )

