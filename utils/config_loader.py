import yaml
from pathlib import Path

def load_config():
    """Load configuration from YAML file."""
    config_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)