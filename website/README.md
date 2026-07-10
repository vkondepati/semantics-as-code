# Semantics as Code Website

Astro documentation and education website for the Semantics as Code project.

## Local Development

```bash
cd website
npm install
npm run dev
```

## Production Build

```bash
cd website
npm run build
npm run preview
```

The site is configured for GitHub Pages at:

```text
https://vkondepati.github.io/semantics-as-code/
```

Astro is configured with `base: "/semantics-as-code"` so links and assets work under the repository subpath.

## GitHub Pages

To enable deployment:

1. Open the repository settings in GitHub.
2. Go to **Pages**.
3. Set **Source** to **GitHub Actions**.
4. Push to `main`.
5. The `deploy-website.yml` workflow will build and publish the site.

No `CNAME` is included. Add one later only if a custom domain is provided.
