"""Garante que o YAML de limites e a justificativa em docs não se desencontrem."""

import re

from assessor.config import RAIZ, load_risk_limits

DOC = RAIZ / "docs" / "estrategia" / "limites-de-risco.md"


def _resolve(limits: dict, dotted: str) -> bool:
    node = limits
    for part in dotted.split("."):
        if part == "*":
            return isinstance(node, dict) and bool(node)
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    return True


def test_limites_carregam():
    limits = load_risk_limits()
    assert 0 < limits["posicao"]["peso_max_por_acao"] <= limits["posicao"]["peso_max_por_setor"] <= 1
    assert limits["carteira"]["num_acoes_min"] <= limits["carteira"]["num_acoes_max"]
    assert limits["execucao"]["aprovacao_humana_obrigatoria"] is True


def test_toda_chave_citada_na_doc_existe_no_yaml():
    limits = load_risk_limits()
    citadas = re.findall(r"`([a-z_]+\.[a-z_*.]+)`", DOC.read_text(encoding="utf-8"))
    assert citadas, "a doc deveria citar chaves do YAML"
    faltando = [c for c in citadas if not _resolve(limits, c)]
    assert not faltando, f"chaves citadas na doc e ausentes no YAML: {faltando}"


def test_toda_secao_do_yaml_tem_justificativa_na_doc():
    limits = load_risk_limits()
    doc = DOC.read_text(encoding="utf-8")
    sem_justificativa = [secao for secao in limits if f"`{secao}." not in doc]
    assert not sem_justificativa, f"seções do YAML sem justificativa na doc: {sem_justificativa}"
