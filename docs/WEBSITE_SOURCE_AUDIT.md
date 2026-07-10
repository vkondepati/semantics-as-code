# Website Source Audit

## Reference Style Notes

The V.E.N.K.A.T. Framework reference site is a static enterprise architecture website with:

- Sticky white navigation and compact link density.
- Dark navy first-viewport hero.
- Strong type hierarchy with large hero text and restrained section headings.
- White and lightly tinted content bands.
- 8px card radii, thin borders, and subtle shadows.
- Enterprise architecture diagrams and grid-based card sections.
- Minimal JavaScript.
- Professional, practitioner-oriented language.

The Semantics as Code website uses these implementation cues while creating a distinct identity around connected semantic nodes, YAML/code brackets, graph-oriented diagrams, teal/cyan/blue/violet accents, and project-specific content.

## Repository Source of Truth

Website content is derived from:

- `pyproject.toml` for current project version.
- `schemas/` for supported object types.
- `templates/` for YAML templates.
- `examples/supply-chain/` and `examples/retail/` for example packages.
- `docs/` for documentation hub content.
- `docs/TASKS.md` for roadmap status.
- `cli/semantics/generators/registry.py` for implemented generator and adapter targets.
- `README.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` for project and contribution guidance.

## Verified Commands

- `npm install`
- `npm run build`
- `python -m pytest`

The website build generated 22 static routes.
