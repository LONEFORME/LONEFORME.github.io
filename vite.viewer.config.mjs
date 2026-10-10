import { fileURLToPath } from "node:url";
import { defineConfig } from "vite";

export default defineConfig({
  build: {
    lib: {
      entry: fileURLToPath(new URL("./scripts/three-viewer-deps.js", import.meta.url)),
      formats: ["es"],
      fileName: () => "three-viewer-deps.bundle.js"
    },
    outDir: fileURLToPath(new URL("./assets/js", import.meta.url)),
    emptyOutDir: false
  }
});
