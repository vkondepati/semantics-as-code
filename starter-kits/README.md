# Semantics as Code Starter Kits

These starter kits provide a practical path from business meaning to platform implementation and production operations.

## Available kits

- `minimal/` — a small proof of concept with one domain, two entities, one metric, one relationship, and one quality rule.
- `enterprise/` — an operating-model blueprint with environments, mappings, governance, security, privacy, tests, and CI/CD.
- `supply-chain/` — a connected reference model for Customer, Product, Order, Warehouse, Inventory, and Shipment.

## Recommended workflow

1. Copy the closest starter kit into a new repository or project folder.
2. Replace sample business definitions with approved enterprise terms.
3. Keep business definitions vendor neutral.
4. Map canonical attributes to Databricks, Snowflake, or other physical platforms.
5. Configure Dev, Test, and Production mappings.
6. Validate and lint all semantic objects.
7. Review changes through pull requests.
8. Generate documentation and platform artifacts.
9. Promote approved releases through environments.
10. Monitor reconciliation, drift, performance, and review dates.

## Quick start

```bash
pip install -e ".[dev]"
semantics validate starter-kits/supply-chain
semantics lint starter-kits/supply-chain
semantics generate starter-kits/supply-chain --target html --output dist/html
semantics generate starter-kits/supply-chain --target mermaid --output dist/diagrams
semantics generate starter-kits/supply-chain --target databricks --output dist/databricks
```

## Design rule

Business semantics are authored. Platform artifacts are generated.
