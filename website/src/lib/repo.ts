import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { marked } from "marked";
import YAML from "yaml";

export const root = path.resolve(process.cwd(), "..");

export function readText(relativePath: string): string {
  return fs.readFileSync(path.join(root, relativePath), "utf-8");
}

export function readJson<T = any>(relativePath: string): T {
  return JSON.parse(readText(relativePath));
}

export function readYaml<T = any>(relativePath: string): T {
  return YAML.parse(readText(relativePath));
}

export function listFiles(relativeDir: string, extension?: string): string[] {
  const dir = path.join(root, relativeDir);
  if (!fs.existsSync(dir)) return [];
  const files: string[] = [];
  function walk(current: string) {
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      const full = path.join(current, entry.name);
      if (entry.isDirectory()) walk(full);
      if (entry.isFile() && (!extension || entry.name.endsWith(extension))) {
        files.push(path.relative(root, full).replaceAll("\\", "/"));
      }
    }
  }
  walk(dir);
  return files.sort();
}

export function schemaSummaries() {
  return listFiles("schemas", ".json").map((file) => {
    const schema = readJson(file);
    const required = schema.required ?? [];
    const properties = Object.keys(schema.properties ?? {});
    const optional = properties.filter((property) => !required.includes(property));
    const kind = file.replace("schemas/", "").replace(".schema.json", "");
    const templatePath = `templates/${kind}.yaml`;
    const example = fs.existsSync(path.join(root, templatePath)) ? readText(templatePath) : "";
    return {
      kind,
      file,
      title: schema.title ?? kind,
      required,
      optional,
      properties,
      example
    };
  });
}

export function examplePackage(name: "supply-chain" | "retail") {
  const base = `examples/${name}`;
  const files = listFiles(base, ".yaml");
  const objects = files.map((file) => ({ file, data: readYaml(file) }));
  return {
    name,
    readme: readText(`${base}/README.md`),
    files,
    domains: objects.filter((object) => object.data.kind === "domain"),
    entities: objects.filter((object) => object.data.kind === "entity"),
    metrics: objects.filter((object) => object.data.kind === "metric"),
    relationships: objects.filter((object) => object.data.kind === "relationship"),
    quality: objects.filter((object) => object.data.kind === "quality_expectation"),
    glossary: objects.filter((object) => object.data.kind === "glossary_term"),
    selectedYaml: files.slice(0, 5).map((file) => ({ file, text: readText(file) }))
  };
}

export function docs() {
  return listFiles("docs", ".md")
    .filter((file) => file !== "docs/WEBSITE_TASKS.md")
    .map((file) => {
      const raw = readText(file);
      const parsed = matter(raw);
      const title = raw.match(/^#\s+(.+)$/m)?.[1] ?? file.replace("docs/", "").replace(".md", "");
      return {
        file,
        slug: file.replace("docs/", "").replace(".md", "").toLowerCase(),
        title,
        html: marked.parse(parsed.content)
      };
    });
}

export function roadmap() {
  const tasks = readText("docs/TASKS.md").split(/\r?\n/);
  return tasks
    .filter((line) => line.startsWith("- ["))
    .map((line) => ({
      done: line.startsWith("- [x]"),
      text: line.replace(/^- \[[x ]\]\s*/, "")
    }));
}
