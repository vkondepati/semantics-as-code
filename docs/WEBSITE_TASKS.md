# Website Implementation Tasks

## Objective

Build a complete public documentation and education website for Semantics as Code under `website/`, deployable to GitHub Pages at:

```text
https://vkondepati.github.io/semantics-as-code/
```

The site should explain the project to business and technology leaders, teach architects and engineers how to use it, present Semantics as Code as a vendor-neutral open proposal and reference implementation, and provide direct access to documentation, examples, templates, CLI commands, schemas, and generated artifacts.

## Guardrails

- [x] Do not reimplement, replace, rename, or restructure the existing Python package or CLI.
- [x] Use existing repository docs, schemas, examples, generators, tests, and commands as source of truth.
- [x] Do not advertise capabilities that are not implemented.
- [x] Use Astro, TypeScript, static site generation, and minimal client-side JavaScript.
- [x] Configure Astro for the GitHub Pages base path `/semantics-as-code/`.
- [x] Keep the website isolated under `website/`.
- [x] Do not create a `CNAME` unless a custom domain is explicitly provided.

## Phase 1: Discovery and Source-of-Truth Audit

- [x] Inspect the current repository structure.
- [x] Inventory implemented CLI commands.
- [x] Inventory implemented generator targets.
- [x] Inventory supported schema object kinds from `schemas/`.
- [x] Inventory templates from `templates/`.
- [x] Inventory examples from `examples/`.
- [x] Inventory documentation from `docs/`.
- [x] Inventory roadmap/task status from `docs/TASKS.md`.
- [x] Inspect GitHub Actions workflows.
- [x] Inspect the V.E.N.K.A.T. Framework website implementation, layout, typography, navigation, spacing, gradients, cards, diagrams, responsiveness, and visual language.
- [x] Record style observations without copying content or branding directly.

Acceptance checks:

- [x] A source-of-truth feature inventory exists for the website content.
- [x] Every advertised generator and adapter maps to an actual implementation.
- [x] Every command shown on the website has been verified against the repository.

## Phase 2: Website Project Setup

- [x] Create `website/`.
- [x] Initialize Astro with TypeScript.
- [x] Configure static site generation.
- [x] Configure `astro.config.mjs` with `site` and `base` for GitHub Pages.
- [x] Add `website/package.json`.
- [x] Add `website/README.md`.
- [x] Add `npm run dev`.
- [x] Add `npm run build`.
- [x] Add `npm run preview`.
- [x] Add TypeScript configuration.
- [x] Add shared CSS structure.
- [x] Add public assets folder.

Acceptance checks:

- [x] `cd website && npm install` succeeds.
- [x] `npm run dev` starts local development.
- [x] `npm run build` produces a static build.
- [x] Built links work under `/semantics-as-code/`.

## Phase 3: Brand and Visual System

- [x] Create a distinct Semantics as Code visual identity.
- [x] Create a CSS or SVG site logo.
- [x] Create favicon assets.
- [x] Create social preview image.
- [x] Define color tokens for dark navy, near-black, blue, cyan, violet, teal, and light content sections.
- [x] Define typography scale.
- [x] Define spacing scale.
- [x] Define card, table, code block, callout, and diagram styles.
- [x] Define light and dark themes.
- [x] Add visible focus states.
- [x] Add reduced-motion support.

Acceptance checks:

- [x] Site feels related to the reference style but has its own identity.
- [x] Color contrast is accessible.
- [x] Logo and favicon render correctly.
- [x] Social preview metadata points to a valid image.

## Phase 4: Information Architecture and Data Files

- [x] Create centralized navigation data.
- [x] Create feature data.
- [x] Create adapters/generators data from actual implementation.
- [x] Create roadmap data from actual task status.
- [x] Create comparison matrix data.
- [x] Create CLI command data.
- [x] Create supported object type data from schemas.
- [x] Create GitHub source link helpers.

Acceptance checks:

- [x] Navigation is not duplicated across pages.
- [x] Generator and adapter lists are data-driven.
- [x] Object type pages derive from schema metadata where practical.

## Phase 5: Reusable Components

- [x] `Header`
- [x] `Footer`
- [x] `Hero`
- [x] `SectionHeading`
- [x] `FeatureCard`
- [x] `CodeBlock`
- [x] `CodeTabs`
- [x] `ArchitectureDiagram`
- [x] `ComparisonTable`
- [x] `WorkflowSteps`
- [x] `Callout`
- [x] `VersionBadge`
- [x] `Breadcrumbs`
- [x] `DocumentationSidebar`
- [x] `ThemeToggle`
- [x] `GitHubButton`
- [x] `RoadmapTimeline`
- [x] `BackToTop`
- [x] `CopyButton`
- [x] `SearchBox`

Acceptance checks:

- [x] Components are reusable and typed.
- [x] Interactive components work with keyboard navigation.
- [x] Copy buttons work for command and YAML blocks.
- [x] Mobile navigation is fully responsive.

## Phase 6: Core Layout and SEO

- [x] Create base layout.
- [x] Add page title metadata.
- [x] Add meta descriptions.
- [x] Add canonical URLs.
- [x] Add Open Graph metadata.
- [x] Add Twitter/X card metadata.
- [x] Add structured data where useful.
- [x] Add `robots.txt`.
- [x] Add sitemap generation.
- [x] Use semantic HTML landmarks.
- [x] Add descriptive alt text for visual assets.

Acceptance checks:

- [x] Every route has a meaningful title and description.
- [x] Sitemap includes all public pages.
- [x] Metadata uses the GitHub Pages URL.
- [x] No root-relative asset links break under the base path.

## Phase 7: Home Page

- [x] Build dark enterprise-style hero.
- [x] Add headline: `Semantics as Code`.
- [x] Add tagline: `Define once. Govern everywhere.`
- [x] Add supporting message.
- [x] Add `Get Started`, `Explore Specification`, and `View on GitHub` actions.
- [x] Add current version badge from package/version source.
- [x] Add problem section.
- [x] Add solution pipeline section.
- [x] Add â€œWhat can be modeledâ€ cards.
- [x] Add starter-kit section.
- [x] Add vendor-neutral section.
- [x] Add quick-start commands with copy buttons.
- [x] Add tabbed YAML examples from real repository files.
- [x] Add architecture diagram.
- [x] Add comparison table.
- [x] Add final call-to-action section.

Acceptance checks:

- [x] Homepage claims match implemented features.
- [x] Example YAML is pulled from or matches real examples.
- [x] Comparison section is careful, vendor-neutral, and non-inflammatory.

## Phase 8: Getting Started Page

- [x] Add prerequisites.
- [x] Add cloning instructions.
- [x] Add Python setup instructions.
- [x] Add development dependency installation.
- [x] Add validation command.
- [x] Add lint command.
- [x] Add Markdown generation command.
- [x] Add HTML generation command.
- [x] Add Mermaid generation command.
- [x] Add vendor output commands.
- [x] Add semantic diff command.
- [x] Add test command.
- [x] Show expected folder structures and outputs.

Acceptance checks:

- [x] All commands match actual implementation.
- [x] Output paths match actual generator behavior.

## Phase 9: Concepts Page

- [x] Explain enterprise semantics.
- [x] Explain semantics versus metadata.
- [x] Explain semantics versus a semantic layer.
- [x] Explain semantics versus ontology.
- [x] Explain semantics versus business glossary.
- [x] Explain entities.
- [x] Explain metrics.
- [x] Explain domains.
- [x] Explain relationships.
- [x] Explain business keys.
- [x] Explain quality expectations.
- [x] Explain governance metadata.
- [x] Explain AI context.
- [x] Explain knowledge graph mappings.

Acceptance checks:

- [x] Explanations are simple, visual, and enterprise-focused.
- [x] No claims imply Semantics as Code is a runtime platform.

## Phase 10: Specification Browser

- [x] Discover supported object types from `schemas/`.
- [x] For each object type, document purpose.
- [x] For each object type, list required properties.
- [x] For each object type, list optional properties.
- [x] For each object type, show field descriptions.
- [x] For each object type, show validation rules.
- [x] For each object type, show complete YAML examples.
- [x] Link to source schema files on GitHub.

Acceptance checks:

- [x] Supported object types are not hardcoded only from the prompt.
- [x] Schema docs match the current JSON Schema files.
- [x] All examples validate.

## Phase 11: Starter Kit Page

- [x] Explain enterprise adoption blueprint.
- [x] Step 1: Select a business domain.
- [x] Step 2: Identify canonical entities.
- [x] Step 3: Define business keys.
- [x] Step 4: Define relationships.
- [x] Step 5: Define metrics and dimensions.
- [x] Step 6: Add owners and stewards.
- [x] Step 7: Add quality expectations.
- [x] Step 8: Add AI context and synonyms.
- [x] Step 9: Validate through CI/CD.
- [x] Step 10: Generate vendor-specific artifacts.
- [x] Link to templates.
- [x] Link to examples.

Acceptance checks:

- [x] Links point to actual repository files.
- [x] Blueprint is practical for enterprise teams.

## Phase 12: Examples Page

- [x] Browse actual repository examples.
- [x] Include supply-chain example.
- [x] Include retail example if present.
- [x] Show domain overview.
- [x] Show entities.
- [x] Show metrics.
- [x] Show relationships.
- [x] Show quality expectations.
- [x] Show generated architecture diagram.
- [x] Show selected YAML.
- [x] Show CLI generation commands.
- [x] Link to source files.

Acceptance checks:

- [x] Example content is derived from repository files where practical.
- [x] No example page references missing examples.

## Phase 13: Generators and Adapters Page

- [x] List implemented output targets only.
- [x] For each target, explain what is generated.
- [x] For each target, show output file names.
- [x] For each target, show example command.
- [x] For each target, explain intended use.
- [x] For each target, show implementation status.
- [x] For each target, document limitations where known.

Acceptance checks:

- [x] Planned adapters are not labeled completed.
- [x] Target names match CLI targets.

## Phase 14: Enterprise Blueprint Page

- [x] Explain Git-based semantic lifecycle.
- [x] Cover authoring.
- [x] Cover review.
- [x] Cover approval.
- [x] Cover validation.
- [x] Cover deployment.
- [x] Cover artifact generation.
- [x] Cover versioning.
- [x] Cover semantic diff.
- [x] Cover rollback.
- [x] Cover governance ownership.
- [x] Cover platform integration.
- [x] Include recommended enterprise repository structure.
- [x] Include Dev, Test, Production promotion guidance.

Acceptance checks:

- [x] Blueprint is vendor-neutral.
- [x] Lifecycle diagram is clear and responsive.

## Phase 15: Vendor Neutrality Page

- [x] Explain why vendor neutrality matters.
- [x] Explain why semantics should not be trapped inside a BI tool.
- [x] Explain one source model producing multiple artifacts.
- [x] Explain how vendors can implement adapters.
- [x] Explain how the project complements existing standards and platforms.
- [x] Add vendor adapter architecture diagram.

Acceptance checks:

- [x] Positioning remains complementary, not adversarial.
- [x] No unsupported claims about vendor compatibility.

## Phase 16: Documentation Hub

- [x] Render existing Markdown documentation from `docs/`.
- [x] Avoid duplicating docs unnecessarily.
- [x] Generate documentation navigation.
- [x] Add syntax-highlighted examples.
- [x] Add previous/next navigation.
- [x] Add table of contents.
- [x] Support deep links.
- [x] Add documentation search.

Acceptance checks:

- [x] Existing docs render correctly.
- [x] Deep links work under GitHub Pages base path.

## Phase 17: Roadmap Page

- [x] Read actual roadmap/task status from repository.
- [x] Separate completed items.
- [x] Separate in-progress items.
- [x] Separate planned items.
- [x] Separate future ideas.
- [x] Present roadmap visually.

Acceptance checks:

- [x] Completed status matches actual implementation.
- [x] Future items are not presented as implemented.

## Phase 18: Contribute Page

- [x] Explain how to report issues.
- [x] Explain how to propose specification changes.
- [x] Explain how to contribute templates.
- [x] Explain how to add generators.
- [x] Explain how to add vendor adapters.
- [x] Explain how to run tests.
- [x] Add pull request guidance.
- [x] Link to `CONTRIBUTING.md`.
- [x] Link to `CODE_OF_CONDUCT.md`.

Acceptance checks:

- [x] Existing contribution files are reused.
- [x] No existing contribution files are overwritten.

## Phase 19: Interactions and Accessibility

- [x] Add copy-to-clipboard buttons.
- [x] Add YAML code tabs.
- [x] Add expandable architecture explanations.
- [x] Add searchable documentation.
- [x] Add light/dark theme toggle.
- [x] Add mobile navigation.
- [x] Add active navigation highlighting.
- [x] Add subtle workflow animation.
- [x] Add reusable callouts.
- [x] Add back-to-top control.
- [x] Verify keyboard navigation.
- [x] Verify visible focus indicators.
- [x] Verify reduced-motion behavior.
- [x] Verify semantic headings.
- [x] Verify ARIA labels where needed.

Acceptance checks:

- [x] Site is usable without a mouse.
- [x] Site remains readable with reduced motion enabled.
- [x] Interactive components have accessible labels.

## Phase 20: GitHub Pages Deployment

- [x] Add `.github/workflows/deploy-website.yml`.
- [x] Checkout repository.
- [x] Install Node.js.
- [x] Install website dependencies.
- [x] Build Astro site.
- [x] Upload Pages artifact.
- [x] Deploy to GitHub Pages.
- [x] Document GitHub Pages repository settings.
- [x] Document optional future custom domain configuration.

Acceptance checks:

- [x] Workflow YAML is valid.
- [x] Site builds with GitHub Pages base path.
- [x] Deployment target is `https://vkondepati.github.io/semantics-as-code/`.

## Phase 21: Root Repository Integration

- [x] Update root `README.md` with website local development commands.
- [x] Add link to website documentation.
- [x] Keep Python package commands intact.
- [x] Keep existing CI workflow intact.
- [x] Do not commit generated `dist/` output.

Acceptance checks:

- [x] Root README includes:
  - `cd website`
  - `npm install`
  - `npm run dev`
  - `npm run build`
  - `npm run preview`

## Phase 22: Validation and Testing

- [x] Run `cd website && npm install`.
- [x] Run `npm run build`.
- [x] Run `npm run preview` where practical.
- [x] Verify all routes.
- [x] Verify internal links.
- [x] Verify GitHub Pages base-path behavior.
- [x] Verify mobile navigation.
- [x] Verify light and dark themes.
- [x] Verify code-copy buttons.
- [x] Verify no Python tests are broken.
- [x] Run `python -m pytest`.
- [x] Validate GitHub Actions YAML structure.

Acceptance checks:

- [x] Website build succeeds.
- [x] Existing Python test suite still passes.
- [x] No broken internal links are known.
- [x] No unsupported claims remain in content.

## Phase 23: Final Handoff

- [x] Provide concise implementation summary.
- [x] List files added.
- [x] List files modified.
- [x] Provide local development commands.
- [x] Provide production build commands.
- [x] Provide exact GitHub Pages enablement steps.
- [x] Note any limitations or follow-up work.

## Suggested GitHub Topics

Add these repository topics in GitHub for discoverability:

- `semantic-layer`
- `semantics`
- `semantics-as-code`
- `data-governance`
- `metadata`
- `yaml`
- `enterprise-architecture`
- `data-modeling`
- `knowledge-graph`
- `agentic-ai`
- `llm`
- `business-glossary`
- `unity-catalog`
- `databricks`
- `snowflake`
- `microsoft-fabric`
- `dbt`
- `openmetadata`
- `data-engineering`
- `ai`
