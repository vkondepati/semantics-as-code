from pathlib import Path

from semantics.validators.validate import validate_path


def test_local_package_dependencies_resolve_references(tmp_path: Path):
    shared = tmp_path / "shared"
    package = tmp_path / "package"
    shared.mkdir()
    package.mkdir()

    (shared / "domain.yaml").write_text(
        """
id: shared-domain
kind: domain
name: Shared Domain
display_name: Shared Domain
description: Shared domain used by another package.
owner: Data Governance
version: 1.0.0
status: active
extensions: {}
""",
        encoding="utf-8",
    )
    (package / "semantics.yaml").write_text(
        """
id: package
kind: semantic_package
name: Package
display_name: Package
description: Package with a local dependency.
owner: Data Governance
version: 1.0.0
spec_version: 1.0.0
dependencies:
  - name: shared
    path: ../shared
extensions: {}
""",
        encoding="utf-8",
    )
    (package / "entity.yaml").write_text(
        """
id: dependent-entity
kind: entity
name: Dependent Entity
display_name: Dependent Entity
description: Entity that references a dependency domain.
business_key: dependent_entity_id
owner: Data Governance
domain: Shared Domain
version: 1.0.0
status: active
classification: Internal
pii: false
quality:
  - dependent_entity_id completeness > 99%
ai_context: Represents a dependency resolution test entity.
extensions: {}
""",
        encoding="utf-8",
    )

    diagnostics, registry = validate_path(package)

    assert diagnostics == []
    assert registry.resolve_kind("Shared Domain", "domain") is not None
