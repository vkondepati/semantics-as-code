# Specification

Semantics as Code definitions are YAML files with a required `kind` field. Version 0.1 supports domains, entities, metrics, glossary terms, relationships, and quality expectations.

## Common Fields

| Field | Required | Description |
| --- | --- | --- |
| `id` | Yes | Stable identifier for references and generated artifacts. |
| `kind` | Yes | Object type such as `entity` or `metric`. |
| `name` | Yes | Human-readable semantic name. |
| `display_name` | Yes | Label for documentation and generated outputs. |
| `description` | Most objects | Business description. |
| `owner` | Yes | Accountable business or data owner. |
| `steward` | Recommended | Day-to-day steward or governance owner. |
| `domain` | Recommended | Business domain reference. |
| `version` | Yes | Definition version. |
| `status` | Recommended | `draft`, `active`, `deprecated`, or `retired`. |
| `classification` | Optional | `Public`, `Internal`, `Confidential`, or `Restricted`. |
| `extensions` | Optional | Namespaced vendor or organization metadata. |

## Extension Model

Use `extensions` for fields that are not part of the portable core.

```yaml
extensions:
  databricks:
    catalog: main
  openmetadata:
    glossary: Enterprise Glossary
```

Generators may ignore unknown extension namespaces.
