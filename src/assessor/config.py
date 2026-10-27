"""Carrega os limites de risco de config/risk_limits.yaml."""

from pathlib import Path
from typing import Any

import yaml

RAIZ = Path(__file__).resolve().parents[2]
RISK_LIMITS_PATH = RAIZ / "config" / "risk_limits.yaml"


def load_risk_limits(path: Path = RISK_LIMITS_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)
