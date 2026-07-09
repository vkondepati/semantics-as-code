from pathlib import Path

from semantics.core.registry import Registry, SemanticObject, discover_yaml_files, normalize_ref


def test_normalize_ref_handles_spaces_and_case():
    assert normalize_ref("Inventory Item") == "inventory-item"


def test_registry_resolves_by_id_name_and_display_name(tmp_path: Path):
    obj = SemanticObject(
        id="inventory-item",
        kind="entity",
        name="Inventory Item",
        path=tmp_path / "inventory-item.yaml",
        data={"id": "inventory-item", "name": "Inventory Item", "display_name": "Inventory Item"},
    )
    registry = Registry()

    assert registry.add(obj) is None
    assert registry.resolve("inventory-item") == obj
    assert registry.resolve("Inventory Item") == obj


def test_discover_yaml_files_ignores_non_yaml_files(tmp_path: Path):
    yaml_file = tmp_path / "entity.yaml"
    text_file = tmp_path / "notes.txt"
    yaml_file.write_text("kind: domain\n", encoding="utf-8")
    text_file.write_text("ignore", encoding="utf-8")

    assert discover_yaml_files(tmp_path) == [yaml_file]
