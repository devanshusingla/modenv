from dataclasses import dataclass
from pathlib import Path

@dataclass
class ChildEntry:
    path: Path
    name: str

