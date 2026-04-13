import yaml
from pathlib import Path

def load(file_name: str) -> dict:
    """Load a YAML file from the project root data folder."""
    path = Path(__file__).parent.parent / "data" / file_name
    with open(path, "r") as f:
        return yaml.safe_load(f)