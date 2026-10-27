"""Loads the advisor's YAML configuration."""

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
RISK_LIMITS_PATH = CONFIG_DIR / "risk_limits.yaml"
ADVISOR_PATH = CONFIG_DIR / "advisor.yaml"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_risk_limits(path: Path = RISK_LIMITS_PATH) -> dict[str, Any]:
    return _load(path)


def load_advisor_settings(path: Path = ADVISOR_PATH) -> dict[str, Any]:
    return _load(path)
