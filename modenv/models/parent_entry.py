from dataclasses import dataclass
from pathlib import Path

@dataclass
class ParentEntry:
    path: Path
    name: str

