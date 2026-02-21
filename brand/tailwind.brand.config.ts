/**
 * Live Vibe Coding Club — Tailwind CSS Brand Config
 *
 * Tailwind CSS v4 (@theme directive) と v3 (tailwind.config) の両方で使用可能。
 *
 * v4での使用方法:
 *   global.cssの @theme ディレクティブにトークンをコピーして適用。
 *
 * v3での使用方法:
 *   tailwind.config.ts の theme.extend にこの設定をスプレッドする。
 */

// ============================================================
// Design Tokens
// ============================================================

export const colors = {
  // --- Primary: Vibe Violet ---
  primary: {
    50: "#F5F3FF",
    100: "#EDE9FE",
    200: "#DDD6FE",
    300: "#C4B5FD",
    400: "#A78BFA",
    500: "#8B5CF6",
    600: "#7C3AED",
    700: "#6D28D9",
    800: "#5B21B6",
    900: "#4C1D95",
    950: "#2E1065",
    DEFAULT: "#8B5CF6",
  },

  // --- Secondary: Cyber Cyan ---
  secondary: {
    50: "#ECFEFF",
    100: "#CFFAFE",
    200: "#A5F3FC",
    300: "#67E8F9",
    400: "#22D3EE",
    500: "#06B6D4",
    600: "#0891B2",
    700: "#0E7490",
    800: "#155E75",
    900: "#164E63",
    950: "#083344",
    DEFAULT: "#06B6D4",
  },

  // --- Accent: Live Pink ---
  accent: {
    50: "#FDF2F8",
    100: "#FCE7F3",
    200: "#FBCFE8",
    300: "#F9A8D4",
    400: "#F472B6",
    500: "#EC4899",
    600: "#DB2777",
    700: "#BE185D",
    800: "#9D174D",
    900: "#831843",
    950: "#500724",
    DEFAULT: "#EC4899",
  },

  // --- Neutral: Void ---
  neutral: {
    50: "#F8F8FC",
    100: "#EDEDF3",
    200: "#D4D4DE",
    300: "#A1A1B5",
    400: "#71718A",
    500: "#4A4A63",
    600: "#33334A",
    700: "#1E1E32",
    800: "#12121F",
    900: "#0A0A14",
    950: "#050507",
  },

  // --- Semantic ---
  success: "#10B981",
  danger: "#EF4444",

  // --- Legacy aliases (既存サイト互換) ---
  bg: "#050507",
  text: "#FFFFFF",
  muted: "rgba(255, 255, 255, 0.5)",
  "gradient-start": "#8B5CF6",
  "gradient-mid": "#06B6D4",
  "gradient-end": "#EC4899",
} as const;

export const fontFamily = {
  display: ["Outfit", "ui-sans-serif", "system-ui", "-apple-system", "sans-serif"],
  body: ["Outfit", "ui-sans-serif", "system-ui", "-apple-system", "sans-serif"],
  mono: ["JetBrains Mono", "ui-monospace", "Cascadia Code", "Fira Code", "monospace"],
  jp: ["Noto Sans JP", "Hiragino Sans", "Hiragino Kaku Gothic ProN", "sans-serif"],
} as const;

export const fontSize = {
  xs: ["0.75rem", { lineHeight: "1.5", letterSpacing: "0.02em" }],
  sm: ["0.875rem", { lineHeight: "1.5", letterSpacing: "0.01em" }],
  base: ["1rem", { lineHeight: "1.6", letterSpacing: "0" }],
  lg: ["1.125rem", { lineHeight: "1.6", letterSpacing: "-0.01em" }],
  xl: ["1.25rem", { lineHeight: "1.4", letterSpacing: "-0.01em" }],
  "2xl": ["1.5rem", { lineHeight: "1.3", letterSpacing: "-0.02em" }],
  "3xl": ["1.875rem", { lineHeight: "1.2", letterSpacing: "-0.02em" }],
  "4xl": ["2.25rem", { lineHeight: "1.1", letterSpacing: "-0.03em" }],
  "5xl": ["3rem", { lineHeight: "1.0", letterSpacing: "-0.04em" }],
  "6xl": ["4rem", { lineHeight: "1.0", letterSpacing: "-0.05em" }],
  "7xl": ["5rem", { lineHeight: "0.95", letterSpacing: "-0.05em" }],
} as const;

export const backgroundImage = {
  "vibe-gradient": "linear-gradient(to right, #8B5CF6, #06B6D4, #EC4899)",
  "vibe-gradient-vertical": "linear-gradient(to bottom, #8B5CF6, #06B6D4, #EC4899)",
  "subtle-glow": "radial-gradient(ellipse at center, rgba(139,92,246,0.15), transparent 70%)",
} as const;

export const dropShadow = {
  glow: "0 0 30px rgba(139, 92, 246, 0.4)",
  "glow-cyan": "0 0 30px rgba(6, 182, 212, 0.4)",
  "glow-pink": "0 0 30px rgba(236, 72, 153, 0.4)",
} as const;

export const animation = {
  float: "float 6s ease-in-out infinite",
  "float-fade": "fade-in 1s ease-out backwards, float 6s ease-in-out 1s infinite",
  gradient: "gradient-shift 8s ease infinite",
  "fade-in": "fade-in 1s ease-out backwards",
} as const;

export const keyframes = {
  float: {
    "0%, 100%": { transform: "translateY(0)" },
    "50%": { transform: "translateY(-10px)" },
  },
  "gradient-shift": {
    "0%, 100%": { backgroundPosition: "0% 50%" },
    "50%": { backgroundPosition: "100% 50%" },
  },
  "fade-in": {
    from: { opacity: "0", transform: "translateY(20px)" },
    to: { opacity: "1", transform: "translateY(0)" },
  },
} as const;

export const borderRadius = {
  brand: "9999px",
} as const;

// ============================================================
// Tailwind v3 Config Export
// ============================================================

export default {
  theme: {
    extend: {
      colors,
      fontFamily,
      fontSize,
      backgroundImage,
      dropShadow,
      animation,
      keyframes,
      borderRadius,
    },
  },
} as const;

// ============================================================
// Tailwind v4 @theme Reference (copy into global.css)
// ============================================================
/*
@theme {
  --color-primary-50: #F5F3FF;
  --color-primary-100: #EDE9FE;
  --color-primary-200: #DDD6FE;
  --color-primary-300: #C4B5FD;
  --color-primary-400: #A78BFA;
  --color-primary-500: #8B5CF6;
  --color-primary-600: #7C3AED;
  --color-primary-700: #6D28D9;
  --color-primary-800: #5B21B6;
  --color-primary-900: #4C1D95;
  --color-primary-950: #2E1065;

  --color-secondary-50: #ECFEFF;
  --color-secondary-100: #CFFAFE;
  --color-secondary-200: #A5F3FC;
  --color-secondary-300: #67E8F9;
  --color-secondary-400: #22D3EE;
  --color-secondary-500: #06B6D4;
  --color-secondary-600: #0891B2;
  --color-secondary-700: #0E7490;
  --color-secondary-800: #155E75;
  --color-secondary-900: #164E63;
  --color-secondary-950: #083344;

  --color-accent: #EC4899;

  --color-neutral-50: #F8F8FC;
  --color-neutral-100: #EDEDF3;
  --color-neutral-200: #D4D4DE;
  --color-neutral-300: #A1A1B5;
  --color-neutral-400: #71718A;
  --color-neutral-500: #4A4A63;
  --color-neutral-600: #33334A;
  --color-neutral-700: #1E1E32;
  --color-neutral-800: #12121F;
  --color-neutral-900: #0A0A14;
  --color-neutral-950: #050507;

  --color-bg: #050507;
  --color-text: #FFFFFF;
  --color-muted: rgba(255, 255, 255, 0.5);
  --color-success: #10B981;
  --color-danger: #EF4444;

  --color-gradient-start: #8B5CF6;
  --color-gradient-mid: #06B6D4;
  --color-gradient-end: #EC4899;

  --font-family-display: 'Outfit', sans-serif;
  --font-family-body: 'Outfit', sans-serif;
  --font-family-mono: 'JetBrains Mono', monospace;
  --font-family-jp: 'Noto Sans JP', sans-serif;
}
*/
