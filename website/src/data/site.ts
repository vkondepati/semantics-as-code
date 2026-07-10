export const repo = "https://github.com/vkondepati/semantics-as-code";
export const siteUrl = "https://vkondepati.github.io/semantics-as-code/";
export const version = "1.0.0";

export const nav = [
  { label: "Home", href: "/" },
  { label: "Get Started", href: "/getting-started/" },
  { label: "Concepts", href: "/concepts/" },
  { label: "Specification", href: "/specification/" },
  { label: "Starter Kit", href: "/starter-kit/" },
  { label: "Examples", href: "/examples/" },
  { label: "Generators", href: "/generators/" },
  { label: "Enterprise Blueprint", href: "/enterprise-blueprint/" },
  { label: "Roadmap", href: "/roadmap/" }
];

export const objectKinds = [
  "semantic-package",
  "domain",
  "entity",
  "metric",
  "glossary-term",
  "relationship",
  "quality-expectation",
  "semantic-object"
];

export const modelCards = [
  ["Domains", "Business areas such as Finance, Sales, Supply Chain, or Loyalty."],
  ["Entities", "Canonical business concepts such as Customer, Order, Product, Supplier, Store, or Region."],
  ["Metrics", "Governed calculations with formula, grain, filters, dimensions, ownership, and quality context."],
  ["Glossary Terms", "Shared definitions, synonyms, related objects, and stewardship metadata."],
  ["Relationships", "Connections between entities and semantic objects for reasoning and diagrams."],
  ["Quality Expectations", "Business-level quality rules attached to entities and metrics."],
  ["Governance Metadata", "Owners, stewards, lifecycle status, classification, PII flags, and tags."],
  ["AI Context", "Plain-language guidance that helps AI systems interpret semantic definitions correctly."]
];

export const generatorTargets = [
  { target: "markdown", output: "index.md, domains.md, entities.md, metrics.md", use: "Readable project documentation." },
  { target: "html", output: "index.html", use: "Standalone generated documentation." },
  { target: "mermaid", output: "semantic-graph.mmd", use: "Entity relationship diagrams." },
  { target: "dbt", output: "semantic_models.yml", use: "dbt Semantic Layer-oriented scaffolding." },
  { target: "openmetadata", output: "openmetadata.json", use: "OpenMetadata-oriented import payloads." },
  { target: "ai-context", output: "ai-context.json, ai-context.md", use: "AI and retrieval context files." },
  { target: "knowledge-graph", output: "knowledge-graph.jsonld, knowledge-graph.ttl", use: "Graph-ready semantic relationships." },
  { target: "databricks", output: "databricks_metric_views.yml", use: "Databricks metric view scaffolding." },
  { target: "snowflake", output: "snowflake_semantic_model.yml", use: "Snowflake semantic model scaffolding." },
  { target: "fabric", output: "fabric_semantic_model.yml", use: "Microsoft Fabric semantic model scaffolding." },
  { target: "bigquery", output: "bigquery_dataform_semantics.yml", use: "BigQuery/Dataform semantic scaffolding." },
  { target: "openmetadata-adapter", output: "openmetadata.json", use: "Vendor adapter output for OpenMetadata." },
  { target: "apache-metadata", output: "apache_metadata_mappings.yml", use: "Apache Iceberg, Polaris, and Gravitino mappings." }
];

export const commands = [
  'pip install -e ".[dev]"',
  "semantics validate examples/supply-chain",
  "semantics lint examples/supply-chain",
  "semantics generate examples/supply-chain --target html --output dist/html",
  "semantics generate examples/supply-chain --target mermaid --output dist/diagrams",
  "semantics generate examples/supply-chain --target databricks --output dist/databricks",
  "semantics diff --base examples/supply-chain --head examples/retail",
  "python -m pytest"
];

export const comparison = [
  ["Business glossary", "Yes", "Partial", "Partial", "No", "Partial", "Yes"],
  ["Git-first authoring", "Yes", "Partial", "Yes", "Partial", "Partial", "Yes"],
  ["Runtime execution", "No", "Catalog platform", "Metric runtime", "Platform feature", "Interchange", "BI runtime"],
  ["Vendor neutrality", "Yes", "Broad but platformed", "Partial", "No", "Yes", "No"],
  ["Starter templates", "Yes", "Limited", "Limited", "No", "No", "Limited"],
  ["Multi-platform generation", "Yes", "No", "No", "No", "Interchange-focused", "No"]
];

export const lifecycle = [
  "Author YAML",
  "Review in Git",
  "Validate and lint",
  "Diff semantic changes",
  "Generate artifacts",
  "Deploy to platforms",
  "Observe and govern"
];
