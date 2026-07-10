from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import yaml

from semantics.core.errors import Diagnostic


SUPPORTED_KINDS = {
    "semantic_package",
    "domain",
    "entity",
    "metric",
    "glossary_term",
    "relationship",
    "quality_expectation",
}


@dataclass
class SemanticObject:
    id: str
    kind: str
    name: str
    path: Path
    data: Dict[str, Any]


class Registry:
    def __init__(self) -> None:
        self.objects: Dict[str, SemanticObject] = {}
        self.aliases: Dict[str, str] = {}

    def add(self, semantic_object: SemanticObject) -> Optional[Diagnostic]:
        normalized_id = normalize_ref(semantic_object.id)
        if normalized_id in self.objects:
            existing = self.objects[normalized_id]
            return Diagnostic(
                severity="error",
                rule_id="SAC-REG-001",
                path=semantic_object.path,
                object_id=semantic_object.id,
                message=f'Duplicate semantic object id "{semantic_object.id}".',
                suggestion=f"First definition was found in {existing.path}.",
            )

        self.objects[normalized_id] = semantic_object
        self.aliases[normalized_id] = normalized_id
        self.aliases[normalize_ref(semantic_object.name)] = normalized_id
        display_name = semantic_object.data.get("display_name")
        if display_name:
            self.aliases[normalize_ref(display_name)] = normalized_id
        return None

    def resolve(self, reference: Any) -> Optional[SemanticObject]:
        if not isinstance(reference, str):
            return None
        object_id = self.aliases.get(normalize_ref(reference))
        if not object_id:
            return None
        return self.objects.get(object_id)

    def resolve_kind(self, reference: Any, kind: str) -> Optional[SemanticObject]:
        if not isinstance(reference, str):
            return None
        normalized = normalize_ref(reference)
        for obj in self.objects.values():
            if obj.kind != kind:
                continue
            aliases = {
                normalize_ref(obj.id),
                normalize_ref(obj.name),
                normalize_ref(str(obj.data.get("display_name", ""))),
            }
            if normalized in aliases:
                return obj
        return None

    def by_kind(self, kind: str) -> List[SemanticObject]:
        return sorted(
            [obj for obj in self.objects.values() if obj.kind == kind],
            key=lambda obj: obj.name.lower(),
        )

    def all(self) -> Iterable[SemanticObject]:
        return sorted(self.objects.values(), key=lambda obj: (obj.kind, obj.name.lower()))

    def package(self) -> Optional[SemanticObject]:
        packages = self.by_kind("semantic_package")
        return packages[0] if packages else None


def normalize_ref(value: str) -> str:
    return value.strip().lower().replace("_", "-").replace(" ", "-")


def discover_yaml_files(path: Path) -> List[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() in {".yaml", ".yml"} else []
    if not path.exists():
        return []
    ignored_parts = {".git", ".venv", "__pycache__", "dist", "build"}
    files = []
    for candidate in path.rglob("*"):
        if candidate.is_file() and candidate.suffix.lower() in {".yaml", ".yml"}:
            if not any(part in ignored_parts for part in candidate.parts):
                files.append(candidate)
    return sorted(files)


def load_yaml_file(path: Path) -> tuple[Optional[Dict[str, Any]], Optional[Diagnostic]]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        return None, Diagnostic(
            severity="error",
            rule_id="SAC-YAML-001",
            path=path,
            message=f"Invalid YAML: {exc}",
        )
    except OSError as exc:
        return None, Diagnostic(
            severity="error",
            rule_id="SAC-FILE-001",
            path=path,
            message=f"Could not read file: {exc}",
        )

    if data is None:
        return None, Diagnostic(
            severity="error",
            rule_id="SAC-YAML-002",
            path=path,
            message="YAML file is empty.",
        )
    if not isinstance(data, dict):
        return None, Diagnostic(
            severity="error",
            rule_id="SAC-YAML-003",
            path=path,
            message="YAML file must contain a mapping object.",
        )
    return data, None
