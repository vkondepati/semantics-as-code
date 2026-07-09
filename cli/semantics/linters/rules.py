from typing import List

from semantics.core.errors import Diagnostic
from semantics.core.registry import Registry, SemanticObject


def lint_registry(registry: Registry) -> List[Diagnostic]:
    diagnostics: List[Diagnostic] = []
    for obj in registry.all():
        diagnostics.extend(_lint_description(obj))
        diagnostics.extend(_lint_owner(obj))
        diagnostics.extend(_lint_steward(obj))
        diagnostics.extend(_lint_quality(obj))
        diagnostics.extend(_lint_ai_context(obj))
        diagnostics.extend(_lint_name_casing(obj))
    return diagnostics


def _lint_description(obj: SemanticObject) -> List[Diagnostic]:
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
