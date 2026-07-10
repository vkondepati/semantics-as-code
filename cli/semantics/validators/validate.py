from pathlib import Path
from typing import Any, Dict, List

import json
from jsonschema import Draft202012Validator

from semantics.core.errors import Diagnostic
from semantics.core.registry import (
    Registry,
    SemanticObject,
    SUPPORTED_KINDS,
    discover_yaml_files,
    load_yaml_file,
)

SCHEMA_DIR = Path(__file__).resolve().parents[3] / "schemas"


def validate_path(path: Path) -> tuple[List[Diagnostic], Registry]:
    diagnostics: List[Diagnostic] = []
    registry = Registry()
    files = discover_yaml_files(path)

    if not files:
        diagnostics.append(
            Diagnostic(
                severity="error",
                rule_id="SAC-FILE-002",
                path=path,
                message="No YAML files found.",
                suggestion="Point the command at a semantic package or YAML file.",
            )
        )
        return diagnostics, registry

    schema_cache: Dict[str, Draft202012Validator] = {}
    pending: List[SemanticObject] = []

    for file_path in files:
        data, error = load_yaml_file(file_path)
        if error:
            diagnostics.append(error)
            continue
        assert data is not None

        kind = data.get("kind")
        if kind not in SUPPORTED_KINDS:
            diagnostics.append(
                Diagnostic(
                    severity="error",
                    rule_id="SAC-SCHEMA-001",
                    path=file_path,
                    message=f'Unsupported or missing kind "{kind}".',
                    suggestion=f"Use one of: {', '.join(sorted(SUPPORTED_KINDS))}.",
                )
            )
            continue

        validator = schema_cache.get(kind)
        if validator is None:
            validator = load_schema_validator(kind)
            schema_cache[kind] = validator

        for error_item in sorted(validator.iter_errors(data), key=lambda err: list(err.path)):
            location = ".".join(str(part) for part in error_item.path)
            suffix = f" at {location}" if location else ""
            diagnostics.append(
                Diagnostic(
                    severity="error",
                    rule_id="SAC-SCHEMA-002",
                    path=file_path,
                    object_id=data.get("id"),
                    message=f"{error_item.message}{suffix}.",
                )
            )

        if any(d.path == file_path and d.rule_id.startswith("SAC-SCHEMA") for d in diagnostics):
            continue

        semantic_object = SemanticObject(
            id=str(data["id"]),
            kind=str(kind),
            name=str(data.get("name", data["id"])),
            path=file_path,
            data=data,
        )
        pending.append(semantic_object)
        duplicate = registry.add(semantic_object)
        if duplicate:
            diagnostics.append(duplicate)

    if not any(d.severity == "error" for d in diagnostics):
        diagnostics.extend(validate_references(registry))

    return diagnostics, registry


def load_schema_validator(kind: str) -> Draft202012Validator:
    schema_path = SCHEMA_DIR / f"{kind.replace('_', '-')}.schema.json"
    with schema_path.open("r", encoding="utf-8") as handle:
        schema = json.load(handle)
    return Draft202012Validator(schema)


def validate_references(registry: Registry) -> List[Diagnostic]:
    diagnostics: List[Diagnostic] = []

    for obj in registry.all():
        if obj.kind == "semantic_package":
            continue

        domain = obj.data.get("domain")
        if domain and not _resolve_kind(registry, domain, "domain"):
            diagnostics.append(_missing_ref(obj, "SAC-REF-001", "domain", domain))

        if obj.kind == "entity":
            for reference in obj.data.get("relationships", []):
                if not registry.resolve(reference):
                    diagnostics.append(_missing_ref(obj, "SAC-REF-002", "relationship target", reference))
            for reference in obj.data.get("quality", []):
                if isinstance(reference, str) and reference.startswith("@") and not registry.resolve(reference[1:]):
                    diagnostics.append(_missing_ref(obj, "SAC-REF-003", "quality expectation", reference))

        if obj.kind == "metric":
            grain = obj.data.get("grain")
            if grain and not registry.resolve(grain):
                diagnostics.append(_missing_ref(obj, "SAC-REF-004", "metric grain", grain))
            for reference in obj.data.get("dimensions", []):
                if not registry.resolve(reference):
                    diagnostics.append(_missing_ref(obj, "SAC-REF-005", "metric dimension", reference))
            for reference in obj.data.get("glossary_terms", []):
                if not _resolve_kind(registry, reference, "glossary_term"):
                    diagnostics.append(_missing_ref(obj, "SAC-REF-006", "glossary term", reference))

        if obj.kind == "relationship":
            for field in ("from", "to"):
                reference = obj.data.get(field)
                if reference and not registry.resolve(reference):
                    diagnostics.append(_missing_ref(obj, "SAC-REF-007", f"relationship {field}", reference))

        if obj.kind == "quality_expectation":
            target = obj.data.get("target")
            if target and not registry.resolve(target):
                diagnostics.append(_missing_ref(obj, "SAC-REF-008", "quality target", target))

    return diagnostics


def _resolve_kind(registry: Registry, reference: Any, kind: str):
    return registry.resolve_kind(reference, kind)


def _missing_ref(obj: SemanticObject, rule_id: str, label: str, reference: Any) -> Diagnostic:
    return Diagnostic(
        severity="error",
        rule_id=rule_id,
        path=obj.path,
        object_id=obj.id,
        message=f'Missing {label} reference "{reference}".',
        suggestion="Add the referenced semantic object or update the reference.",
    )
