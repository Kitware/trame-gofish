import json
from pathlib import Path

ALPHABET = json.loads(Path(__file__).with_name("alphabet.json").read_text())
SEAFOOD = json.loads(Path(__file__).with_name("seafood.json").read_text())

__all__ = [
    "ALPHABET",
    "SEAFOOD",
]
