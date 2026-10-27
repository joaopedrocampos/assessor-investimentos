"""Keeps the risk-limits YAML and its rationale doc from drifting apart."""

import re

from advisor.config import ROOT, load_advisor_settings, load_risk_limits

RATIONALE_DOC = ROOT / "docs" / "strategy" / "risk-limits.md"
KEY_PATTERN = re.compile(r"`([a-z_]+\.[a-z_*.]+)`")


def _key_exists(limits: dict, dotted: str) -> bool:
    node = limits
    for part in dotted.split("."):
        if part == "*":
            return isinstance(node, dict) and bool(node)
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    return True


def test_risk_limits_are_coherent():
    limits = load_risk_limits()
    position = limits["position"]
    portfolio = limits["portfolio"]
    assert 0 < position["max_weight_per_stock"] <= position["max_weight_per_sector"] <= 1
    assert portfolio["min_stocks"] <= portfolio["max_stocks"]
    assert portfolio["fixed_income_reserve_min"] <= portfolio["fixed_income_reserve_max"]
    assert limits["execution"]["human_approval_required"] is True


def test_every_key_cited_in_rationale_exists_in_yaml():
    limits = load_risk_limits()
    cited = KEY_PATTERN.findall(RATIONALE_DOC.read_text(encoding="utf-8"))
    assert cited, "the rationale doc should cite YAML keys"
    missing = [key for key in cited if not _key_exists(limits, key)]
    assert not missing, f"keys cited in the doc but missing from the YAML: {missing}"


def test_every_yaml_section_has_a_rationale():
    limits = load_risk_limits()
    doc = RATIONALE_DOC.read_text(encoding="utf-8")
    undocumented = [section for section in limits if f"`{section}." not in doc]
    assert not undocumented, f"YAML sections with no rationale in the doc: {undocumented}"


def test_report_language_is_supported():
    assert load_advisor_settings()["reports"]["language"] in {"en", "pt-BR"}
