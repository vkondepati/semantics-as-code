from pathlib import Path

import yaml

from semantics.core.diff import diff_paths


def test_diff_paths_detects_changed_objects(tmp_path: Path):
    base = tmp_path / "base"
    head = tmp_path / "head"
    base.mkdir()
    head.mkdir()
    obj = {
        "id": "test-domain",
        "kind": "domain",
        "name": "Test Domain",
        "display_name": "Test Domain",
        "description": "A test semantic domain.",
        "owner": "Data Governance",
        "version": "0.2.0",
        "status": "active",
        "extensions": {},
    }
    (base / "domain.yaml").write_text(yaml.safe_dump(obj), encoding="utf-8")
    obj["description"] = "A changed test semantic domain."
    (head / "domain.yaml").write_text(yaml.safe_dump(obj), encoding="utf-8")

    result = diff_paths(base, head)

    assert result.diagnostics == []
    assert result.changed == ["domain:test-domain"]
