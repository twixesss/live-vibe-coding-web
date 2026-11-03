// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// Unicorn Studio (background effect) is loaded from jsDelivr with SRI (see src/pages/index.astro).
// It fetches its scene JSON from storage.googleapis.com and textures from assets.unicorn.studio.
const UNICORN_SCRIPT = 'https://cdn.jsdelivr.net/gh/hiunicornstudio/unicornstudio.js@v2.0.2/dist/unicornStudio.umd.js';

export default defineConfig({
  site: 'https://vibec.uk',
  output: 'static',
  trailingSlash: 'ignore',
  // Markdown is not used; disabling Shiki avoids its inline styles (incompatible with CSP) and the build warning.
  markdown: {
    syntaxHighlight: false,
  },
  security: {
    // Emits a <meta http-equiv="content-security-policy"> with hashes for inline scripts/styles.
    // GitHub Pages cannot set response headers, so frame-ancestors etc. are not available here.
    csp: {
      directives: [
        "default-src 'self'",
        "img-src 'self' data: blob: https://assets.unicorn.studio https://storage.googleapis.com",
        "font-src https://fonts.gstatic.com",
        "connect-src 'self' https://storage.googleapis.com https://assets.unicorn.studio",
        "object-src 'none'",
        "base-uri 'self'",
        "form-action 'none'",
        'upgrade-insecure-requests',
      ],
      scriptDirective: {
        resources: ["'self'", UNICORN_SCRIPT],
      },
      styleDirective: {
        resources: ["'self'", 'https://fonts.googleapis.com'],
      },
    },
  },
  vite: {
    plugins: [tailwindcss()]
  }
});
