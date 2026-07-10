import { defineConfig } from "astro/config";
export default defineConfig({
  site: "https://vkondepati.github.io",
  base: "/semantics-as-code/",
  output: "static",
  vite: {
    server: {
      fs: {
        allow: [".."]
      }
    }
  }
});
