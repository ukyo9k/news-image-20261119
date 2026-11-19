#!/usr/bin/env python3
"""Draw the front page for Thursday 19 November 2026.

Everything here is drawn from scratch with Pillow: no photos, no network,
no copied artwork. The news items were gathered by the author from wire
and newspaper reports of 18-19 November 2026 and are listed in README.md.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 28

PAPER = (247, 243, 233)
INK = (24, 24, 26)
NAVY = (18, 38, 63)
NAVY_SOFT = (31, 58, 88)
RED = (178, 38, 30)
GOLD = (201, 162, 39)
TEAL = (15, 118, 110)
CARD = (255, 255, 255)
CARD_LINE = (205, 198, 184)
MUTED = (92, 88, 80)
SUNSET_TOP = (255, 138, 76)
SUNSET_MID = (232, 84, 96)
SUNSET_LOW = (94, 52, 110)
SEA = (24, 64, 96)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def load(size, bold=False, serif=False):
    name = "DejaVuSerif-Bold.ttf" if serif else (
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = load(52, serif=True)
F_DATE = load(21, bold=True)
F_TAG = load(13, bold=True)
F_HERO_HEAD = load(34, bold=True)
F_HERO_DECK = load(17)
F_CARD_KICK = load(12, bold=True)
F_CARD_HEAD = load(19, bold=True)
F_CARD_DECK = load(14)
F_TILE_KICK = load(11, bold=True)
F_TILE_HEAD = load(16, bold=True)
F_TILE_DECK = load(13)
F_ALSO_HEAD = load(14, bold=True)
F_ALSO = load(14)
F_FOOT = load(12)


def wrap(draw, text, font, width):
    """Greedy word wrap using real pixel widths."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, font, width, fill, leading=None, max_lines=None):
    """Draw wrapped text; return the y just below the last line."""
    x, y = xy
    leading = leading or int(font.size * 1.28)
    lines = wrap(draw, text, font, width)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, fill=RED, width=3):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def card(draw, box, fill=CARD, outline=CARD_LINE):
    draw.rounded_rectangle(box, radius=10, fill=fill, outline=outline, width=1)


# ---------------------------------------------------------------- icons

def draw_controller(draw, cx, cy, s, fill):
    """A simple game controller silhouette."""
    w, h = int(1.5 * s), int(0.85 * s)
    x0, y0 = cx - w // 2, cy - h // 2
    draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=h // 3, fill=fill)
    draw.ellipse([x0 - s // 6, y0 + h // 2, x0 + s // 6, y0 + h], fill=fill)
    draw.ellipse([x0 + w - s // 6, y0 + h // 2, x0 + w + s // 6, y0 + h],
                 fill=fill)
    draw.line([x0 + w // 4 - 6, cy, x0 + w // 4 + 6, cy], fill=PAPER, width=3)
    draw.line([x0 + w // 4, cy - 6, x0 + w // 4, cy + 6], fill=PAPER, width=3)
    for dx, dy in ((8, -8), (-8, -8), (8, 8), (-8, 8)):
        draw.ellipse([cx + w // 4 + dx - 3, cy + dy - 3,
                      cx + w // 4 + dx + 3, cy + dy + 3], fill=GOLD)


def draw_palm(draw, x, y, s, fill):
    draw.line([x, y, x, y - s], fill=fill, width=4)
    for ang in (-70, -35, 0, 35, 70):
        r = math.radians(ang)
        ex = x + int(math.sin(r) * s * 0.55)
        ey = y - s - int(math.cos(r) * s * 0.28)
        draw.line([x, y - s, ex, ey], fill=fill, width=3)


def draw_flags(draw, x, y, s):
    """Three flag poles with three different pennants."""
    cols = [RED, GOLD, TEAL]
    for i, c in enumerate(cols):
        px = x + i * (s + 14)
        draw.line([px, y, px, y - s], fill=INK, width=3)
        draw.polygon([(px, y - s), (px + s, y - s + 9), (px, y - s + 18)],
                     fill=c)


def draw_scales(draw, cx, cy, s, fill):
    draw.line([cx, cy - s, cx, cy + s], fill=fill, width=4)
    draw.line([cx - s, cy - s + 8, cx + s, cy - s + 8], fill=fill, width=4)
    for sx in (-s, s):
        draw.line([cx + sx, cy - s + 8, cx + sx, cy - s + 22], fill=fill,
                  width=2)
        draw.polygon([(cx + sx - 12, cy - s + 22), (cx + sx + 12, cy - s + 22),
                      (cx + sx, cy - s + 34)], outline=fill, width=2)
    draw.line([cx - s - 6, cy + s, cx + s + 6, cy + s], fill=fill, width=4)


def draw_rocket(draw, cx, cy, s, fill):
    draw.ellipse([cx - s // 2, cy - s, cx + s // 2, cy + s // 2], fill=fill)
    draw.polygon([(cx - s // 2, cy), (cx - s, cy + s // 2),
                  (cx - s // 2, cy + s // 4)], fill=fill)
    draw.polygon([(cx + s // 2, cy), (cx + s, cy + s // 2),
                  (cx + s // 2, cy + s // 4)], fill=fill)
    draw.ellipse([cx - 6, cy - s + 12, cx + 6, cy - s + 24], fill=PAPER)
    draw.polygon([(cx - 8, cy + s // 2), (cx + 8, cy + s // 2),
                  (cx, cy + s)], fill=GOLD)


def draw_bars(draw, x, y, w, h, fill):
    vals = [0.45, 0.62, 0.55, 0.8, 1.0]
    bw = w // (len(vals) * 2)
    for i, v in enumerate(vals):
        bx = x + i * 2 * bw
        bh = int(h * v)
        draw.rectangle([bx, y + h - bh, bx + bw, y + h], fill=fill)


def draw_spiral(draw, cx, cy, r, fill):
    pts = []
    for t in range(0, 540, 6):
        rad = math.radians(t)
        rr = r * t / 540.0
        pts.append((cx + rr * math.cos(rad), cy + rr * math.sin(rad)))
    draw.line(pts, fill=fill, width=3, joint="curve")


# ---------------------------------------------------------------- sections

def masthead(draw):
    draw.rectangle([0, 0, W, 116], fill=NAVY)
    draw.rectangle([0, 116, W, 122], fill=RED)
    draw.text((MARGIN, 18), "THE WORLD IN ONE DAY",
              font=F_TITLE, fill=PAPER)
    draw.text((MARGIN, 82), "THURSDAY  19  NOVEMBER  2026",
              font=F_DATE, fill=GOLD)
    tag = "ONE DAY  ·  ONE IMAGE  ·  19 NOV 2026"
    tw = draw.textlength(tag, font=F_TAG)
    draw.text((W - MARGIN - tw, 88), tag, font=F_TAG, fill=(190, 200, 215))


def hero(draw):
    x0, y0, x1, y1 = MARGIN, 134, W - MARGIN, 360
    card(draw, [x0, y0, x1, y1])
    # Sunset art panel on the left.
    ax0, ay0, ax1, ay1 = x0 + 10, y0 + 10, 428, y1 - 10
    for i, band in enumerate((SUNSET_TOP, SUNSET_MID, SUNSET_LOW, SEA)):
        top = ay0 + (ay1 - ay0) * i // 4
        bot = ay0 + (ay1 - ay0) * (i + 1) // 4
        draw.rectangle([ax0, top, ax1, bot], fill=band)
    draw.ellipse([ax0 + 150, ay0 + 26, ax0 + 226, ay0 + 102],
                 fill=(255, 214, 130))
    # Skyline silhouettes.
    base = ay1 - 46
    for bx, bw, bh in ((0, 46, 66), (52, 34, 96), (92, 58, 54), (156, 30, 84),
                       (192, 52, 62), (250, 36, 100), (292, 44, 58),
                       (342, 30, 78)):
        draw.rectangle([ax0 + bx, base - bh, ax0 + bx + bw, base],
                       fill=(30, 22, 46))
    draw.rectangle([ax0, base, ax1, ay1], fill=(16, 28, 52))
    draw_palm(draw, ax0 + 40, base + 4, 52, (16, 28, 52))
    draw_palm(draw, ax1 - 42, base + 4, 44, (16, 28, 52))
    draw.text((ax0 + 14, ay0 + 118), "VICE CITY", font=load(30, bold=True),
              fill=(255, 214, 130))
    draw_controller(draw, ax0 + (ax1 - ax0) // 2, ay1 - 22, 34, PAPER)
    # Text on the right.
    tx = 452
    draw.text((tx, y0 + 16), "CULTURE  ·  GAMES", font=F_CARD_KICK, fill=RED)
    y = para(draw, (tx, y0 + 42), "VICE CITY OPENS AT LAST",
             F_HERO_HEAD, x1 - tx - 18, INK, max_lines=2)
    y = para(draw, (tx, y + 8),
             "Grand Theft Auto VI unlocks at midnight local time around "
             "the world, starting in New Zealand \u2014 13 years after GTA V.",
             F_HERO_DECK, x1 - tx - 18, INK, max_lines=3)
    y = para(draw, (tx, y + 8),
             "Pre-orders near $1.5bn for about 16m copies; early reviews "
             "put it at 99 on Metacritic.",
             F_HERO_DECK, x1 - tx - 18, MUTED, max_lines=2)
    draw.text((tx, y1 - 34), "ROCKSTAR GAMES  ·  PS5 & XBOX SERIES X|S  ·  $79.99",
              font=F_TAG, fill=NAVY_SOFT)


def top_three(draw):
    y0, y1 = 372, 540
    cols = [MARGIN, 358, 688]
    cw = 308
    items = [
        ("DIPLOMACY", "Three presidents, one table",
         "Xi, Trump and Putin meet in Shenzhen on the APEC sidelines "
         "\u2014 a first trilateral.", "flags"),
        ("JUSTICE", "The Hague rules on the Rohingya",
         "The World Court rules today in The Gambia\u2019s genocide case "
         "against Myanmar.", "scales"),
        ("SPACE", "A light-day from home",
         "Voyager 1, launched in 1977, has crossed one light-day from "
         "Earth \u2014 16bn miles. NASA briefs the world today.", "rocket"),
    ]
    for (x, (kick, head, deck, icon)) in zip(cols, items):
        card(draw, [x, y0, x + cw, y1])
        draw.text((x + 16, y0 + 12), kick, font=F_CARD_KICK, fill=RED)
        iy = y0 + 34
        if icon == "flags":
            draw_flags(draw, x + 18, iy + 30, 26)
        elif icon == "scales":
            draw_scales(draw, x + 52, iy + 18, 22, NAVY_SOFT)
        else:
            draw_rocket(draw, x + 52, iy + 18, 22, NAVY_SOFT)
            for sx, sy in ((x + 96, iy + 8), (x + 116, iy + 34),
                           (x + 84, iy + 44)):
                draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=GOLD)
        y = para(draw, (x + 16, iy + 44), head, F_CARD_HEAD, cw - 32, INK,
                 max_lines=2)
        para(draw, (x + 16, y + 4), deck, F_CARD_DECK, cw - 32, MUTED,
             max_lines=3)


def grid(draw):
    rows = [(552, 664), (672, 784)]
    cols = [MARGIN, 358, 688]
    cw = 308
    tiles = [
        ("MARKETS", "Anthropic\u2019s $81bn debut",
         "Anthropic\u2019s IPO prices at $83 a share \u2014 the biggest "
         "ever. Trading starts today.", "bars"),
        ("EUROPE", "\u20ac45bn more for Kyiv",
         "EU proposes a \u20ac45bn loan for Ukraine, repaid only after "
         "Russia pays reparations.", None),
        ("MIDDLE EAST", "Canberra sanctions settlers",
         "Australia blacklists three people and four groups over West "
         "Bank settlements.", None),
        ("GAZA", "Tanks cross the Yellow Line",
         "Israeli armour enters Hamas-held central Gaza \u2014 first "
         "ground op since the truce.", None),
        ("WEATHER", "Cyclone Akvan bears down",
         "India\u2019s east coast braces for Friday landfall; red alerts "
         "for heavy rain.", "spiral"),
        ("WASHINGTON", "Jeffries one step from the gavel",
         "Democrats nominate Jeffries for Speaker, 251\u201311. The full "
         "House votes on 3 January.", None),
    ]
    for idx, (kick, head, deck, icon) in enumerate(tiles):
        x = cols[idx % 3]
        ry0, ry1 = rows[idx // 3]
        card(draw, [x, ry0, x + cw, ry1])
        draw.text((x + 14, ry0 + 10), kick, font=F_TILE_KICK, fill=RED)
        if icon == "bars":
            draw_bars(draw, x + cw - 66, ry0 + 12, 52, 26, TEAL)
        elif icon == "spiral":
            draw_spiral(draw, x + cw - 34, ry0 + 26, 16, TEAL)
        y = para(draw, (x + 14, ry0 + 32), head, F_TILE_HEAD, cw - 28, INK,
                 max_lines=2)
        para(draw, (x + 14, y + 3), deck, F_TILE_DECK, cw - 28, MUTED,
             max_lines=2)


def also_on(draw):
    y0 = 800
    draw.text((MARGIN, y0), "ALSO ON THIS DAY", font=F_ALSO_HEAD, fill=NAVY)
    rule(draw, MARGIN + 168, W - MARGIN, y0 + 9, fill=CARD_LINE, width=2)
    left = [
        "Peltola wins Alaska\u2019s Senate seat; Democrats lead 56\u201344.",
        "India and Japan hold 2+2 defence talks in Tokyo.",
        "Ukraine says relay drones helped hit the Kerch bridge.",
        "LPG tanker that sank off Bulgaria \u2018was hit by projectiles\u2019.",
    ]
    right = [
        "Migrant boat capsizes off Senegal; at least one dead.",
        "Somalia accuses the UAE of building secret bases on its soil.",
        "Haaland sends Norway into the Nations League quarters.",
        "Deutsche Bank handled $582m in Epstein-linked payments (FT).",
    ]
    y = y0 + 26
    for row in range(4):
        for col, items in ((MARGIN, left), (524, right)):
            draw.text((col, y), "\u2022", font=F_ALSO, fill=RED)
            para(draw, (col + 16, y), items[row], F_ALSO, 452, INK,
                 max_lines=1)
        y += 26


def footer(draw):
    y = 956
    rule(draw, MARGIN, W - MARGIN, y, fill=CARD_LINE, width=2)
    draw.text((MARGIN, y + 10),
              "Sources: Reuters \u00b7 AP \u00b7 BBC \u00b7 NASA / JPL \u00b7 Human Rights Watch \u00b7 NPR \u00b7 CNN \u00b7 The Hindu \u00b7 IMD \u00b7 Le Monde",
              font=F_FOOT, fill=MUTED)
    draw.text((MARGIN, y + 30),
              "Events of Thursday 19 November 2026, as reported 18\u201319 November 2026  \u00b7  make.fun news-image-20261119",
              font=F_FOOT, fill=MUTED)


def build(path="entry.png"):
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    hero(draw)
    top_three(draw)
    grid(draw)
    also_on(draw)
    footer(draw)
    img.save(path, optimize=True)
    return path


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    build(out)
    print("wrote", out)
