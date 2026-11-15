import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    lib: {
      entry: fileURLToPath(new URL('./scripts/market-charts.js', import.meta.url)),
      formats: ['es'],
      fileName: () => 'market-charts.bundle.js',
    },
    outDir: fileURLToPath(new URL('./assets/js', import.meta.url)),
    emptyOutDir: false,
    rollupOptions: {
      output: {
        banner: '/*! TradingView Lightweight Charts v5.0.9, Copyright (c) 2025 TradingView, Inc. (Apache-2.0); Lucide Contributors (ISC); fancy-canvas (MIT). See MARKET-CHARTS-NOTICE.txt. */',
      },
    },
  },
});
