# Vendor Adapters

Vendor adapters transform the semantic registry into platform-oriented artifacts. They use the same generator command surface as other outputs.

## Adapter API

Adapters implement `VendorAdapter`:

```python
class VendorAdapter:
    name: str

    def generate(self, registry, output_path):
        ...
```

## Built-In Adapters

| Target | Output |
| --- | --- |
| `databricks` | `databricks_metric_views.yml` |
| `snowflake` | `snowflake_semantic_model.yml` |
| `fabric` | `fabric_semantic_model.yml` |
| `bigquery` | `bigquery_dataform_semantics.yml` |
| `openmetadata-adapter` | `openmetadata.json` |
| `apache-metadata` | `apache_metadata_mappings.yml` |

## Usage

```bash
semantics generate examples/supply-chain --target databricks --output dist/databricks
semantics generate examples/supply-chain --target snowflake --output dist/snowflake
semantics generate examples/supply-chain --target apache-metadata --output dist/apache
```
