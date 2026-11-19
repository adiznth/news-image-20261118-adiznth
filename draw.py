#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news summary image (1024x1024 PNG).

One front page: a masthead naming the day, then six illustrated story
panels covering the day's biggest stories across regions and fields.
Every panel is drawn from scratch with Pillow vector shapes -- no photos,
no downloaded assets -- so the program is fully self-contained and runs
with no network. Run:  python3 draw.py  (writes entry.png next to it).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 244, 238)          # paper
INK = (18, 24, 38)            # near-black
NAVY = (15, 42, 74)
RED = (178, 34, 34)
BLUE = (24, 90, 160)
TEAL = (14, 110, 110)
GOLD = (176, 124, 20)
GREEN = (34, 110, 60)
GREY = (90, 96, 108)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w, size=19):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font(fnt, size)) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- masthead -------------------------------------------------------------
d.rectangle([0, 0, W, 118], fill=NAVY)
center(d, W // 2, 12, "THE WORLD IN ONE DAY", font(SANS_B, 26),
       (212, 175, 105))
center(d, W // 2, 44, "WEDNESDAY  18  NOVEMBER  2026",
       font(SERIF, 44), (255, 255, 255))
d.line([40, 108, W - 40, 108], fill=(212, 175, 105), width=2)

# ---- lead headline --------------------------------------------------------
center(d, W // 2, 130, "XI MEETS PUTIN IN SHENZHEN",
       font(SERIF, 40), INK)
center(d, W // 2, 178,
       "Leaders talk Ukraine and Iran before Thursday's three-way summit with Trump",
       font(SERIF_R, 21), GREY)
d.line([60, 212, W - 60, 212], fill=INK, width=2)

# ---- story panels ---------------------------------------------------------
PANELS = [
    ("SUMMIT IN SHENZHEN", RED,
     "Xi and Putin meet at APEC, one day before three-way talks with Trump.",
     "globe"),
    ("GULF FLARE-UP", BLUE,
     "Iran drones hit US bases in Kuwait and Bahrain; US jets strike Qeshm Island.",
     "ship"),
    ("KERCH BRIDGE HIT", TEAL,
     "Ukraine strikes the bridge for a second day; part of the road span collapses.",
     "bridge"),
    ("SENATE FLIPS BLUE", NAVY,
     "Peltola wins Alaska; Democrats take a 56-44 Senate majority.",
     "ballot"),
    ("NVIDIA'S RECORD QUARTER", GREEN,
     "Revenue doubles to $115.8bn; board rules out a Huang return.",
     "chip"),
    ("CYCLONE AKVAN", GOLD,
     "Severe storm strengthens in the Bay of Bengal, bearing down on Andhra Pradesh.",
     "storm"),
]

PX, PY, PW, PH = 28, 232, 300, 236
GAPX, GAPY = 24, 20


def draw_globe(box, color):
    x0, y0, x1, y1 = box
    cx, cy, r = (x0 + x1) // 2, (y0 + y1) // 2, 40
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(210, 228, 244),
              outline=color, width=5)
    d.ellipse([cx - 16, cy - r, cx + 16, cy + r], outline=color, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=3)
    d.ellipse([cx - 40, cy - 44, cx - 22, cy - 26], fill=RED)
    d.ellipse([cx + 22, cy - 44, cx + 40, cy - 26], fill=GOLD)


def draw_ship(box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    d.polygon([(x0 + 30, cy + 8), (x1 - 30, cy + 8), (x1 - 58, cy + 34),
               (x0 + 58, cy + 34)], fill=color)
    d.rectangle([cx - 30, cy - 20, cx + 30, cy + 8], fill=(70, 70, 80))
    d.rectangle([cx - 5, cy - 36, cx + 5, cy - 20], fill=(70, 70, 80))
    d.polygon([(cx + 5, cy - 36), (cx + 34, cy - 26), (cx + 5, cy - 18)],
              fill=RED)
    for wx in (x0 + 44, x0 + 112, x0 + 180):
        d.arc([wx, cy + 38, wx + 42, cy + 56], 0, 180, fill=color, width=4)


def draw_bridge(box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    d.line([x0 + 16, cy + 40, x1 - 16, cy + 40], fill=color, width=6)
    d.line([cx - 88, cy + 40, cx - 88, cy - 34], fill=color, width=6)
    d.line([cx + 88, cy + 40, cx + 88, cy - 34], fill=color, width=6)
    d.line([cx - 88, cy - 34, cx + 88, cy - 34], fill=color, width=5)
    d.line([cx - 88, cy - 34, cx - 36, cy + 40], fill=color, width=3)
    d.line([cx + 88, cy - 34, cx + 36, cy + 40], fill=color, width=3)
    d.line([cx - 88, cy - 34, cx + 36, cy + 40], fill=color, width=3)
    d.line([cx + 88, cy - 34, cx - 36, cy + 40], fill=color, width=3)
    d.line([cx - 12, cy + 40, cx + 12, cy + 40], fill=RED, width=10)
    d.ellipse([cx - 24, cy - 56, cx - 6, cy - 38], fill=RED)
    d.ellipse([cx + 6, cy - 56, cx + 24, cy - 38], fill=RED)


def draw_ballot(box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    d.rounded_rectangle([cx - 56, cy - 22, cx + 56, cy + 46], radius=8,
                        fill=color)
    d.rectangle([cx - 30, cy - 34, cx + 30, cy - 22], fill=(255, 255, 255),
                outline=color, width=3)
    d.line([cx - 38, cy + 2, cx - 14, cy + 26], fill=(255, 255, 255), width=7)
    d.line([cx - 14, cy + 26, cx + 42, cy - 20], fill=(255, 255, 255), width=7)


def draw_chip(box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    for i in range(-2, 3):
        d.line([cx + i * 22, cy - 56, cx + i * 22, cy - 34], fill=color, width=5)
        d.line([cx + i * 22, cy + 34, cx + i * 22, cy + 56], fill=color, width=5)
        d.line([cx - 56, cy + i * 22, cx - 34, cy + i * 22], fill=color, width=5)
        d.line([cx + 34, cy + i * 22, cx + 56, cy + i * 22], fill=color, width=5)
    d.rounded_rectangle([cx - 34, cy - 34, cx + 34, cy + 34], radius=10,
                        fill=color)
    d.rounded_rectangle([cx - 20, cy - 20, cx + 20, cy + 20], radius=6,
                        fill=(255, 255, 255))
    d.text((cx - 14, cy - 15), "$", font=font(SANS_B, 28), fill=color)


def draw_storm(box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    for k in range(4):
        r0 = 12 + k * 11
        d.arc([cx - r0, cy - r0, cx + r0, cy + r0],
              start=40 + k * 55, end=300 + k * 55, fill=color, width=6)
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED)
    d.line([x0 + 24, cy + 48, x1 - 24, cy + 48], fill=color, width=4)


DRAW = {"globe": draw_globe, "ship": draw_ship, "bridge": draw_bridge,
        "ballot": draw_ballot, "chip": draw_chip, "storm": draw_storm}

for i, (title, color, caption, kind) in enumerate(PANELS):
    col, row = i % 3, i // 3
    x = PX + col * (PW + GAPX)
    y = PY + row * (PH + GAPY)
    d.rounded_rectangle([x, y, x + PW, y + PH], radius=10,
                        outline=(200, 196, 188), width=2, fill=(255, 255, 255))
    d.rectangle([x, y, x + PW, y + 8], fill=color)
    DRAW[kind]((x + 8, y + 12, x + PW - 8, y + 112), color)
    size = 24
    while size > 18 and d.textlength(title, font=font(SANS_B, size)) > PW - 24:
        size -= 1
    center(d, x + PW // 2, y + 120, title, font(SANS_B, size), INK)
    lines = wrap(d, caption, SANS, PW - 28, size=18)
    ly = y + 150
    for ln in lines[:3]:
        center(d, x + PW // 2, ly, ln, font(SANS, 18), (52, 58, 70))
        ly += 23

# ---- footer -----------------------------------------------------------------
fy = PY + 2 * PH + GAPY + 12
d.line([40, fy, W - 40, fy], fill=INK, width=2)
center(d, W // 2, fy + 10,
       "Sources: AP  ·  Reuters  ·  AFP  ·  Al Jazeera  —  reported on 18 November 2026",
       font(SANS, 18), GREY)
center(d, W // 2, fy + 36, "The world in one day  ·  18 November 2026",
       font(SERIF_R, 18), GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
