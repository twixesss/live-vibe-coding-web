"""
Live Vibe Coding Club — Brand Board PDF Generator
A3 横向き (420mm x 297mm) のビジュアルブランドボードを生成する。
"""

import urllib.request
from pathlib import Path

from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ============================================================
# Font Download & Registration
# ============================================================

FONT_DIR = Path(__file__).parent / "fonts"
FONT_DIR.mkdir(exist_ok=True)

FONTS = {
    "Outfit-Regular": "https://cdn.jsdelivr.net/fontsource/fonts/outfit@latest/latin-400-normal.ttf",
    "Outfit-Black": "https://cdn.jsdelivr.net/fontsource/fonts/outfit@latest/latin-900-normal.ttf",
    "JetBrainsMono-Regular": "https://cdn.jsdelivr.net/fontsource/fonts/jetbrains-mono@latest/latin-400-normal.ttf",
}


def download_fonts():
    for name, url in FONTS.items():
        path = FONT_DIR / f"{name}.ttf"
        if not path.exists():
            print(f"Downloading {name}...")
            try:
                urllib.request.urlretrieve(url, path)
            except Exception as e:
                print(f"  Warning: Could not download {name}: {e}")


def register_fonts():
    for name in FONTS:
        path = FONT_DIR / f"{name}.ttf"
        if path.exists():
            try:
                pdfmetrics.registerFont(TTFont(name, str(path)))
            except Exception as e:
                print(f"  Warning: Could not register {name}: {e}")


# ============================================================
# Color Definitions
# ============================================================

C = {
    "bg": HexColor("#050507"),
    "text": HexColor("#F8F8FC"),
    "muted": HexColor("#71718A"),
    "card": HexColor("#1E1E32"),
    "card_border": HexColor("#33334A"),
    "p50": HexColor("#F5F3FF"),  "p100": HexColor("#EDE9FE"),
    "p200": HexColor("#DDD6FE"), "p300": HexColor("#C4B5FD"),
    "p400": HexColor("#A78BFA"), "p500": HexColor("#8B5CF6"),
    "p600": HexColor("#7C3AED"), "p700": HexColor("#6D28D9"),
    "p800": HexColor("#5B21B6"), "p900": HexColor("#4C1D95"),
    "p950": HexColor("#2E1065"),
    "s50": HexColor("#ECFEFF"),  "s100": HexColor("#CFFAFE"),
    "s200": HexColor("#A5F3FC"), "s300": HexColor("#67E8F9"),
    "s400": HexColor("#22D3EE"), "s500": HexColor("#06B6D4"),
    "s600": HexColor("#0891B2"), "s700": HexColor("#0E7490"),
    "s800": HexColor("#155E75"), "s900": HexColor("#164E63"),
    "s950": HexColor("#083344"),
    "accent": HexColor("#EC4899"),
    "success": HexColor("#10B981"),
    "danger": HexColor("#EF4444"),
}

# ============================================================
# Helpers
# ============================================================

def f(name, fallback="Helvetica"):
    try:
        pdfmetrics.getFont(name)
        return name
    except KeyError:
        return fallback

F_REG = lambda: f("Outfit-Regular")
F_BLK = lambda: f("Outfit-Black")
F_MONO = lambda: f("JetBrainsMono-Regular", "Courier")


def draw_gradient_rect(cv, x, y, w, h, colors_list, steps=120):
    strip_w = w / steps
    for i in range(steps):
        t = i / (steps - 1)
        if t < 0.5:
            t2 = t * 2
            r = colors_list[0].red + (colors_list[1].red - colors_list[0].red) * t2
            g = colors_list[0].green + (colors_list[1].green - colors_list[0].green) * t2
            b = colors_list[0].blue + (colors_list[1].blue - colors_list[0].blue) * t2
        else:
            t2 = (t - 0.5) * 2
            r = colors_list[1].red + (colors_list[2].red - colors_list[1].red) * t2
            g = colors_list[1].green + (colors_list[2].green - colors_list[1].green) * t2
            b = colors_list[1].blue + (colors_list[2].blue - colors_list[1].blue) * t2
        cv.setFillColor(Color(r, g, b))
        cv.rect(x + i * strip_w, y, strip_w + 0.5, h, fill=1, stroke=0)


def draw_rounded_rect(cv, x, y, w, h, r, fill_color):
    cv.saveState()
    cv.setFillColor(fill_color)
    p = cv.beginPath()
    p.roundRect(x, y, w, h, r)
    cv.drawPath(p, fill=1, stroke=0)
    cv.restoreState()


def draw_swatch_row(cv, x, y, swatches, swatch_w, swatch_h, gap):
    """Draw a row of color swatches with labels below."""
    for i, (label, hex_str, color) in enumerate(swatches):
        sx = x + i * (swatch_w + gap)
        draw_rounded_rect(cv, sx, y, swatch_w, swatch_h, 2.5 * mm, color)
        cv.setFillColor(C["text"])
        cv.setFont(F_REG(), 6.5)
        cv.drawString(sx + 1, y - 10, label)
        cv.setFillColor(C["muted"])
        cv.setFont(F_MONO(), 5.5)
        cv.drawString(sx + 1, y - 18, hex_str)


def section_title(cv, x, y, text):
    cv.setFillColor(C["p500"])
    cv.setFont(F_BLK(), 11)
    cv.drawString(x, y, text)


# ============================================================
# Main
# ============================================================

def generate_brand_board():
    download_fonts()
    register_fonts()

    output_path = Path(__file__).parent / "brand-board.pdf"
    page_w, page_h = landscape(A3)
    cv = canvas.Canvas(str(output_path), pagesize=landscape(A3))

    M = 15 * mm  # margin
    CW = page_w - 2 * M  # content width
    LEFT_W = CW * 0.54  # left column width
    RIGHT_X = M + CW * 0.58  # right column x
    RIGHT_W = CW * 0.42  # right column width

    # ── Background ──
    cv.setFillColor(C["bg"])
    cv.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    # ── Header gradient bar ──
    top = page_h - M
    draw_gradient_rect(cv, M, top - 2.5 * mm, CW, 2.5 * mm,
                       [C["p500"], C["s500"], C["accent"]])

    # ── Title ──
    cv.setFillColor(C["text"])
    cv.setFont(F_BLK(), 30)
    cv.drawString(M, top - 28 * mm, "LIVE VIBE CODING CLUB")

    cv.setFillColor(C["muted"])
    cv.setFont(F_REG(), 11)
    cv.drawString(M, top - 36 * mm, "Brand Design System v1.0")

    cv.setFont(F_REG(), 9)
    cv.drawRightString(page_w - M, top - 28 * mm, "vibec.uk")
    cv.drawRightString(page_w - M, top - 36 * mm, "2026-02-16")

    # ================================================================
    # LEFT COLUMN
    # ================================================================
    ly = top - 46 * mm  # left column start y

    # ── Brand Essence ──
    section_title(cv, M, ly, "BRAND ESSENCE")
    cv.setFillColor(C["text"])
    cv.setFont(F_BLK(), 20)
    cv.drawString(M, ly - 20, "AI to tomo ni, code de asobe.")
    cv.setFillColor(C["muted"])
    cv.setFont(F_REG(), 9)
    cv.drawString(M, ly - 34, "Personality:  Cutting-Edge  /  Creative  /  Open")

    # ── Color Palette ──
    palette_y = ly - 52 * mm
    section_title(cv, M, palette_y, "COLOR PALETTE")

    SW = 16 * mm  # swatch width
    SH = 16 * mm  # swatch height
    SG = 2.2 * mm  # gap

    # Primary
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 8)
    cv.drawString(M, palette_y - 14, "Primary — Vibe Violet")

    primary = [
        ("50", "#F5F3FF", C["p50"]),   ("100", "#EDE9FE", C["p100"]),
        ("200", "#DDD6FE", C["p200"]), ("300", "#C4B5FD", C["p300"]),
        ("400", "#A78BFA", C["p400"]), ("500", "#8B5CF6", C["p500"]),
        ("600", "#7C3AED", C["p600"]), ("700", "#6D28D9", C["p700"]),
        ("800", "#5B21B6", C["p800"]), ("900", "#4C1D95", C["p900"]),
        ("950", "#2E1065", C["p950"]),
    ]
    draw_swatch_row(cv, M, palette_y - 38 * mm, primary, SW, SH, SG)

    # Secondary
    sec_y = palette_y - 60 * mm
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 8)
    cv.drawString(M, sec_y, "Secondary — Cyber Cyan")

    secondary = [
        ("50", "#ECFEFF", C["s50"]),   ("100", "#CFFAFE", C["s100"]),
        ("200", "#A5F3FC", C["s200"]), ("300", "#67E8F9", C["s300"]),
        ("400", "#22D3EE", C["s400"]), ("500", "#06B6D4", C["s500"]),
        ("600", "#0891B2", C["s600"]), ("700", "#0E7490", C["s700"]),
        ("800", "#155E75", C["s800"]), ("900", "#164E63", C["s900"]),
        ("950", "#083344", C["s950"]),
    ]
    draw_swatch_row(cv, M, sec_y - 24 * mm, secondary, SW, SH, SG)

    # Accent & Semantic
    acc_y = sec_y - 48 * mm
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 8)
    cv.drawString(M, acc_y, "Accent & Semantic")

    accent_colors = [
        ("Accent", "#EC4899", C["accent"]),
        ("Success", "#10B981", C["success"]),
        ("Danger", "#EF4444", C["danger"]),
    ]
    draw_swatch_row(cv, M, acc_y - 24 * mm, accent_colors, SW, SH, SG)

    # Vibe Gradient
    grad_x = M + 4 * (SW + SG)
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 8)
    cv.drawString(grad_x, acc_y, "Vibe Gradient")

    grad_w = M + LEFT_W - grad_x
    draw_gradient_rect(cv, grad_x, acc_y - 24 * mm, grad_w, SH,
                       [C["p500"], C["s500"], C["accent"]])
    cv.setFillColor(C["muted"])
    cv.setFont(F_MONO(), 6)
    cv.drawString(grad_x, acc_y - 24 * mm - 10, "#8B5CF6 -> #06B6D4 -> #EC4899")

    # ================================================================
    # RIGHT COLUMN
    # ================================================================
    ry = top - 46 * mm

    # ── Typography ──
    section_title(cv, RIGHT_X, ry, "TYPOGRAPHY")

    # Display
    cv.setFillColor(C["muted"])
    cv.setFont(F_REG(), 8)
    cv.drawString(RIGHT_X, ry - 16, "Display / Body — Outfit")

    cv.setFillColor(C["text"])
    cv.setFont(F_BLK(), 38)
    cv.drawString(RIGHT_X, ry - 50, "Aa Bb Cc")

    cv.setFont(F_REG(), 16)
    cv.drawString(RIGHT_X, ry - 70, "ABCDEFGHIJKLM  abcdefghijklm")

    cv.setFillColor(C["muted"])
    cv.setFont(F_REG(), 10)
    cv.drawString(RIGHT_X, ry - 86, "Regular 400  |  Black 900")

    # Mono
    cv.setFillColor(C["muted"])
    cv.setFont(F_REG(), 8)
    cv.drawString(RIGHT_X, ry - 106, "Mono — JetBrains Mono")

    code_box_w = RIGHT_W - 5 * mm
    draw_rounded_rect(cv, RIGHT_X, ry - 140, code_box_w, 28, 3 * mm, C["card"])
    cv.setFillColor(C["s400"])
    cv.setFont(F_MONO(), 13)
    cv.drawString(RIGHT_X + 10, ry - 131, "const vibe = await ai.code();")

    # Japanese
    cv.setFillColor(C["muted"])
    cv.setFont(F_REG(), 8)
    cv.drawString(RIGHT_X, ry - 158, "Japanese — Noto Sans JP")
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 14)
    cv.drawString(RIGHT_X, ry - 176, "Noto Sans JP  Regular 400 / Bold 700 / Black 900")

    # ── Tone & Manner ──
    tone_y = ry - 205
    section_title(cv, RIGHT_X, tone_y, "TONE & MANNER")

    # DO column
    do_x = RIGHT_X
    cv.setFillColor(C["success"])
    cv.setFont(F_BLK(), 9)
    cv.drawString(do_x, tone_y - 18, "DO")

    dos = [
        "Active voice, action-oriented",
        "Name specific tools (Claude, Cursor...)",
        "Casual-polite Japanese",
        "Short punchy phrases",
        "Show real examples & outcomes",
    ]
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 7.5)
    for i, item in enumerate(dos):
        cv.drawString(do_x + 2 * mm, tone_y - 30 - i * 12, f"- {item}")

    # DON'T column
    dont_x = RIGHT_X + RIGHT_W * 0.52
    cv.setFillColor(C["danger"])
    cv.setFont(F_BLK(), 9)
    cv.drawString(dont_x, tone_y - 18, "DON'T")

    donts = [
        "Overly formal language",
        "AI threat narratives",
        "Exclusive / elitist phrasing",
        "Vague superlatives",
        "Long paragraphs (max 3 sentences)",
    ]
    cv.setFillColor(C["text"])
    cv.setFont(F_REG(), 7.5)
    for i, item in enumerate(donts):
        cv.drawString(dont_x + 2 * mm, tone_y - 30 - i * 12, f"- {item}")

    # ================================================================
    # BOTTOM: Logo Concepts
    # ================================================================
    logo_y = 28 * mm
    draw_gradient_rect(cv, M, logo_y + 12, CW, 1.5, [C["p500"], C["s500"], C["accent"]])

    section_title(cv, M, logo_y + 18, "LOGO CONCEPTS")

    concepts = [
        ("1. Wave Pulse", "Audio wave + real-time pulse motif"),
        ("2. Code Orbit", "<> brackets forming orbital paths"),
        ("3. Spark Node", "Neural network node, glowing spark"),
    ]
    col_w = CW / 3
    for i, (name, desc) in enumerate(concepts):
        cx = M + i * col_w
        cv.setFillColor(C["text"])
        cv.setFont(F_BLK(), 9)
        cv.drawString(cx, logo_y - 2, name)
        cv.setFillColor(C["muted"])
        cv.setFont(F_REG(), 8)
        cv.drawString(cx, logo_y - 14, desc)

    # ── Footer gradient bar ──
    draw_gradient_rect(cv, M, 8 * mm, CW, 1.5 * mm,
                       [C["p500"], C["s500"], C["accent"]])

    cv.save()
    print(f"Brand board generated: {output_path}")


if __name__ == "__main__":
    generate_brand_board()
