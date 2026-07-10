from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from semantics.core.errors import Diagnostic
from semantics.core.registry import Registry, SemanticObject


DEFAULT_RULES = {
    "SAC-LINT-001": "error",
    "SAC-LINT-002": "error",
    "SAC-LINT-003": "warning",
    "SAC-LINT-004": "warning",
    "SAC-LINT-005": "warning",
    "SAC-LINT-006": "warning",
}


def lint_registry(registry: Registry, config: Optional[Dict[str, str]] = None) -> List[Diagnostic]:
    rule_config = DEFAULT_RULES | (config or {})
    diagnostics: List[Diagnostic] = []
    for obj in registry.all():
        diagnostics.extend(_apply_config(_lint_description(obj), rule_config))
        diagnostics.extend(_apply_config(_lint_owner(obj), rule_config))
        diagnostics.extend(_apply_config(_lint_steward(obj), rule_config))
        diagnostics.extend(_apply_config(_lint_quality(obj), rule_config))
        diagnostics.extend(_apply_config(_lint_ai_context(obj), rule_config))
        diagnostics.extend(_apply_config(_lint_name_casing(obj), rule_config))
    return diagnostics


def load_lint_config(path: Path, explicit_config: Optional[Path] = None) -> Dict[str, str]:
    config_path = explicit_config or _find_manifest(path)
    if not config_path or not config_path.exists():
        return {}

    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    lint_rules = data.get("lint", {}).get("rules", {})
    if not isinstance(lint_rules, dict):
        return {}
    config = {}
    for rule_id, severity in lint_rules.items():
        normalized = _normalize_severity(severity)
        if normalized in {"off", "warning", "error"}:
            config[str(rule_id)] = normalized
    return config


def _find_manifest(path: Path) -> Optional[Path]:
    root = path.parent if path.is_file() else path
    for name in ("semantics.yaml", "semantics.yml"):
        candidate = root / name
        if candidate.exists():
            return candidate
    return None


def _apply_config(diagnostics: List[Diagnostic], config: Dict[str, str]) -> List[Diagnostic]:
    configured = []
    for diagnostic in diagnostics:
        severity = config.get(diagnostic.rule_id, diagnostic.severity)
        if severity == "off":
            continue
        diagnostic.severity = severity
        configured.append(diagnostic)
    return configured


def _normalize_severity(value: Any) -> str:
    if value is False:
        return "off"
    return str(value).lower()


def _lint_description(obj: SemanticObject) -> List[Diagnostic]:
    if obj.kind == "semantic_package":
        return []
    description = obj.data.get("description") or obj.data.get("definition")
    if not isinstance(description, str) or len(description.strip()) < 12:
        return [
            Diagnostic(
                severity="error",
                rule_id="SAC-LINT-001",
                path=obj.path,
                object_id=obj.id,
                message="Description must be meaningful and at least 12 characters.",
            )
        ]
    return []


def _lint_owner(obj: SemanticObject) -> List[Diagnostic]:
    if obj.kind == "semantic_package":
        return []
    if not obj.data.get("owner") and obj.kind != "relationship":
        return [
            Diagnostic(
                severity="error",
                rule_id="SAC-LINT-002",
                path=obj.path,
                object_id=obj.id,
                message="Owner must be present.",
            )
        ]
    return []


def _lint_steward(obj: SemanticObject) -> List[Diagnostic]:
    if obj.kind in {"entity", "metric", "glossary_term"} and not obj.data.get("steward"):
        return [
            Diagnostic(
                severity="warning",
                rule_id="SAC-LINT-003",
                path=obj.path,
                object_id=obj.id,
                message="Steward is recommended for governed semantic objects.",
            )
        ]
    return []


def _lint_quality(obj: SemanticObject) -> List[Diagnostic]:
    if obj.kind in {"entity", "metric"} and not obj.data.get("quality"):
        return [
            Diagnostic(
                severity="warning",
                rule_id="SAC-LINT-004",
                path=obj.path,
                object_id=obj.id,
                message="Quality expectations are recommended for entities and metrics.",
            )
        ]
    return []


def _lint_ai_context(obj: SemanticObject) -> List[Diagnostic]:
    if obj.kind in {"entity", "metric"} and not obj.data.get("ai_context"):
        return [
            Diagnostic(
                severity="warning",
                rule_id="SAC-LINT-005",
                path=obj.path,
                object_id=obj.id,
                message="AI context is recommended for entities and metrics.",
            )
        ]
    return []


def _lint_name_casing(obj: SemanticObject) -> List[Diagnostic]:
    if obj.kind == "semantic_package":
        return []
    name = obj.data.get("name")
    if isinstance(name, str) and ("_" in name or name[:1].islower()):
        return [
            Diagnostic(
                severity="warning",
                rule_id="SAC-LINT-006",
                path=obj.path,
                object_id=obj.id,
                message="Name should use display-style casing without underscores.",
            )
        ]
    return []
