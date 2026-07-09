# Examples

The `examples/` directory contains complete semantic packages.

## Supply Chain

`examples/supply-chain` includes:

- Five business domains.
- Eight entities.
- Six metrics.
- Six glossary terms.
- Six explicit relationships.
- Three quality expectations.

Run:

```bash
semantics validate examples/supply-chain
semantics lint examples/supply-chain
semantics generate examples/supply-chain --target markdown --output dist/docs
```
