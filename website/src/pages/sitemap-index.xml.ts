import { docs } from "@lib/repo";
import { nav } from "@data/site";

export async function GET() {
  const base = "https://vkondepati.github.io/semantics-as-code";
  const docUrls = docs().map((page) => `${base}/docs/${page.slug}/`);
  const navUrls = nav.map((item) => `${base}${item.href}`);
  const extra = [
    `${base}/docs/`,
    `${base}/vendor-neutrality/`,
    `${base}/contribute/`
  ];
  const urls = Array.from(new Set([...navUrls, ...extra, ...docUrls]));
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls
      .map((url) => `  <url><loc>${url}</loc></url>`)
      .join("\n")}\n</urlset>\n`,
    { headers: { "Content-Type": "application/xml" } }
  );
}
