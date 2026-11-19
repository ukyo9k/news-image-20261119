#!/usr/bin/env python3
"""Render the front-page poster for Thursday 19 November 2026 world news.

Draws entry.png (1024x1024) with PIL + DejaVu fonts only. Every story was
verified against sources opened on 19 Nov 2026 (Reuters, CNN, NASA/JPL,
Polygon, People, Metacritic, ISPR, Financial Times). Run: python3 build_poster.py
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (18, 28, 54)
RED = (178, 24, 24)
GOLD = (176, 141, 44)
GREY = (88, 90, 96)
LIGHT = (255, 255, 255)
TEAL = (24, 96, 104)
SUNSET_TOP = (255, 158, 92)
SUNSET_MID = (232, 92, 110)
SUNSET_BOT = (84, 48, 120)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for w in text.split():
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, font, color, max_w, leading, max_lines=None):
    lines = wrap(d, text, font, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=font, fill=color)
        y += leading
    return y


def rule(d, y, width=2, color=INK):
    d.line([24, y, W - 24, y], fill=color, width=width)


def kicker(d, x, y, text, color=RED, size=13):
    d.text((x, y), text, font=fnt(SANS_B, size), fill=color)
    return y + size + 5


def draw_skyline(d, x, y, w, h):
    """Drawn sunset skyline over Leonida for the hero panel."""
    # gradient sky
    for i in range(h):
        t = i / h
        if t < 0.5:
            u = t / 0.5
            c = tuple(int(SUNSET_TOP[j] + (SUNSET_MID[j] - SUNSET_TOP[j]) * u)
                      for j in range(3))
        else:
            u = (t - 0.5) / 0.5
            c = tuple(int(SUNSET_MID[j] + (SUNSET_BOT[j] - SUNSET_MID[j]) * u)
                      for j in range(3))
        d.line([x, y + i, x + w, y + i], fill=c)
    # sun
    sx, sy, sr = x + w - 78, y + 52, 30
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(255, 214, 120))
    # sea strip
    sea_y = y + h - 46
    d.rectangle([x, sea_y, x + w, y + h], fill=(38, 74, 110))
    d.line([x, sea_y, x + w, sea_y], fill=(255, 214, 120), width=2)
    # buildings (dark silhouettes)
    import random
    rng = random.Random(1911)
    bx = x + 6
    while bx < x + w - 20:
        bw = rng.randint(22, 44)
        bh = rng.randint(50, 118)
        by = sea_y - bh
        d.rectangle([bx, by, bx + bw, sea_y], fill=(30, 22, 58))
        # lit windows
        for wy in range(by + 8, sea_y - 6, 12):
            for wx in range(bx + 5, bx + bw - 4, 10):
                if rng.random() < 0.45:
                    d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 214, 120))
        bx += bw + 4
    # palm silhouettes
    for px, py, s in [(x + 34, sea_y - 8, 1.0), (x + w - 46, sea_y - 6, 0.85)]:
        d.line([px, py, px + 4 * s, py - 34 * s], fill=(22, 18, 44), width=3)
        for ang in (-70, -35, 0, 35, 70):
            rad = math.radians(ang - 90)
            ex = px + 4 * s + 18 * s * math.cos(rad)
            ey = py - 34 * s + 18 * s * math.sin(rad)
            d.line([px + 4 * s, py - 34 * s, ex, ey], fill=(22, 18, 44), width=3)
    d.text((x + 10, y + 8), "LEONIDA — VICE CITY", font=fnt(SANS_B, 13),
           fill=LIGHT)
    d.text((x + w - 10, y + h - 24), "DRAWN, NOT A PHOTO",
           font=fnt(SANS, 10), fill=(220, 220, 220), anchor="ra")


def icon_tile(d, x, y, kind):
    """44x44 navy tile with a gold line icon."""
    d.rectangle([x, y, x + 44, y + 44], fill=INK)
    g = GOLD
    if kind == "summit":  # three flags / three heads
        for i, fx in enumerate((x + 9, x + 19, x + 29)):
            d.line([fx, y + 12, fx, y + 36], fill=g, width=2)
            d.polygon([(fx, y + 12), (fx + 9, y + 16), (fx, y + 20)], fill=g)
    elif kind == "court":  # scales of justice
        d.line([x + 22, y + 10, x + 22, y + 36], fill=g, width=2)
        d.line([x + 10, y + 14, x + 34, y + 14], fill=g, width=2)
        d.arc([x + 8, y + 14, x + 16, y + 26], 0, 180, fill=g, width=2)
        d.arc([x + 28, y + 14, x + 36, y + 26], 0, 180, fill=g, width=2)
        d.line([x + 12, y + 36, x + 32, y + 36], fill=g, width=2)
    else:  # rocket / probe
        d.polygon([(x + 22, y + 8), (x + 30, y + 24), (x + 26, y + 34),
                   (x + 18, y + 34), (x + 14, y + 24)], outline=g, width=2)
        d.ellipse([x + 19, y + 16, x + 25, y + 22], fill=g)
        d.line([x + 22, y + 34, x + 22, y + 40], fill=g, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 90], fill=INK)
    d.rectangle([0, 90, W, 96], fill=RED)
    d.text((24, 12), "THE WORLD TODAY", font=fnt(SERIF_B, 46), fill=LIGHT)
    d.text((24, 64), "22 STORIES  ·  6 CONTINENTS  ·  ALL VERIFIED",
           font=fnt(SANS_B, 14), fill=(198, 203, 214))
    d.text((W - 24, 10), "THURSDAY", font=fnt(SANS_B, 26), fill=GOLD, anchor="ra")
    d.text((W - 24, 42), "19 NOVEMBER 2026", font=fnt(SANS_B, 22), fill=LIGHT,
           anchor="ra")
    d.text((W - 24, 70), "FRONT PAGE — ONE DAY IN ONE IMAGE",
           font=fnt(SANS, 12), fill=(198, 203, 214), anchor="ra")

    # ---------- hero: GTA VI ----------
    hx, hy, hw = 24, 110, 600
    kicker(d, hx, hy, "CULTURE  —  THE BIGGEST LAUNCH OF THE DECADE", size=15)
    d.text((hx, hy + 26), "VICE CITY", font=fnt(SERIF_B, 54), fill=INK)
    d.text((hx, hy + 84), "CALLS AGAIN", font=fnt(SERIF_B, 54), fill=INK)
    y = para(d, hx, hy + 148,
             "Grand Theft Auto VI opens at midnight worldwide after a "
             "13-year wait — a 99 on Metacritic, the highest-rated game "
             "ever, tying Ocarina of Time.",
             fnt(SANS, 18), INK, hw, 23, max_lines=3)
    d.text((hx, y + 6), "Gamers in New Zealand and Australia were first in; "
           "IGN gave it 10/10.", font=fnt(SANS, 13), fill=GREY)
    draw_skyline(d, 648, 110, 352, 216)
    d.text((648, 334), "Rockstar's Leonida, drawn from the game's own "
           "sunset palette.", font=fnt(SANS, 11), fill=GREY)

    rule(d, 366)

    # ---------- top 3 ----------
    top3 = [
        ("DIPLOMACY — SHENZHEN", "summit",
         "THREE LEADERS, ONE TABLE",
         "Trump, Xi and Putin meet in Shenzhen today — a first-ever "
         "trilateral, with nuclear arms control on the agenda and a "
         "Trump–Putin one-on-one beside it."),
        ("JUSTICE — THE HAGUE", "court",
         "WORLD COURT RULES ON MYANMAR",
         "The ICJ delivers its genocide verdict on the Rohingya today — "
         "seven years on, the court has never before found a state guilty "
         "of genocide."),
        ("SPACE — VOYAGER 1", "probe",
         "ONE LIGHT-DAY FROM HOME",
         "NASA confirms Voyager 1 crossed the mark at 05:16 EST on "
         "Wednesday — 16.1 billion miles out, a signal now takes a full "
         "day to arrive."),
    ]
    col_w = 320
    for i, (kick, icon, head, deck) in enumerate(top3):
        x = 24 + i * (col_w + 8)
        y = 380
        icon_tile(d, x, y, icon)
        d.text((x + 54, y + 2), kick, font=fnt(SANS_B, 12), fill=RED)
        d.text((x + 54, y + 20), "19 NOV", font=fnt(SANS_B, 12), fill=GREY)
        y = para(d, x, y + 52, head, fnt(SANS_B, 20), INK, col_w, 23,
                 max_lines=2)
        para(d, x, y + 4, deck, fnt(SANS, 14), (40, 40, 40), col_w, 17,
             max_lines=4)

    rule(d, 528)

    # ---------- grid 2x3 ----------
    grid = [
        ("EUROPE — UKRAINE AID",
         "Brussels proposes €45bn Kyiv loan",
         "Covers two-thirds of Ukraine's €70bn 2027 gap; Kyiv repays only "
         "once Russia pays reparations."),
        ("USA — SPY AGENCY DOWN",
         "NSA's classified network still out",
         "NSANet has been down since Tuesday; the Georgia hub serving "
         "Middle East intel is hit. No cyberattack, officials say."),
        ("LATIN AMERICA — CARACAS",
         "Hegseth signs Venezuela defence pact",
         "First Pentagon chief's visit since Maduro's January ouster; joint "
         "training and intel sharing agreed."),
        ("ASIA — ARMS RACE",
         "Pakistan test-fires Fatah-3 missile",
         "Supersonic cruise missile launched on Wednesday — the third new "
         "Fatah-series test in six weeks."),
        ("OCEANIA — SANCTIONS",
         "Australia sanctions settler leaders",
         "Three Israelis and four groups hit over West Bank expansion, a "
         "day after Britain sanctioned builders."),
        ("BLACK SEA — SHIPPING",
         "Tanker hit by four projectiles",
         "LPG carrier Gas Husky sank off Bulgaria; all 19 crew rescued. "
         "A second ship was lost in 24 hours."),
    ]
    gw, gh = 320, 104
    for i, (kick, head, deck) in enumerate(grid):
        col, row = i % 3, i // 3
        x = 24 + col * (gw + 8)
        y = 542 + row * (gh + 6)
        d.text((x, y), kick, font=fnt(SANS_B, 12), fill=RED)
        y = para(d, x, y + 18, head, fnt(SANS_B, 18), INK, gw, 21,
                 max_lines=2)
        para(d, x, y + 2, deck, fnt(SANS, 13), (40, 40, 40), gw, 16,
             max_lines=2)

    rule(d, 764)

    # ---------- also list ----------
    d.text((24, 776), "ALSO ON THURSDAY 19 NOVEMBER",
           font=fnt(SANS_B, 17), fill=INK)
    d.line([24, 800, W - 24, 800], fill=RED, width=2)
    also = [
        ("GAZA", "Israeli tanks cross the Yellow Line in central Gaza."),
        ("SOMALIA", "President accuses UAE of secret bases, arming rivals."),
        ("IRAQ", "Six French ISIL members jailed for life; 16 convicted."),
        ("CANADA", "Carney recalibrates China ties, seeks US deal."),
        ("EPSTEIN FILES", "Deutsche Bank handled $582m in Epstein deals."),
        ("CALIFORNIA", "Atmospheric river brings floods and heavy rain."),
        ("INDIA–JAPAN", "Defence ties review as ministers arrive in Tokyo."),
        ("US VISAS", "Tougher green-card rules proposed; hiring slows."),
        ("LIBYA", "Cocaine and millions of pills seized in the east."),
        ("GULF", "Saudi Arabia: danger has passed in three cities."),
        ("CYBER", "Senators: AI-enabled threats outpacing defences."),
        ("CRICKET", "Duckett's 133 puts England on top in 3rd ODI."),
    ]
    col_w2 = 480
    for i, (kick, text) in enumerate(also):
        col, row = i % 2, i // 2
        x = 24 + col * (col_w2 + 16)
        y = 812 + row * 28
        d.text((x, y), kick + " — ", font=fnt(SANS_B, 14), fill=RED)
        kw = d.textlength(kick + " — ", font=fnt(SANS_B, 14))
        para(d, x + kw, y, text, fnt(SANS, 14), (30, 30, 30),
             col_w2 - kw, 17, max_lines=1)
        if kw + d.textlength(text, font=fnt(SANS, 14)) > col_w2:
            print("OVERLONG also item:", kick, "excess",
                  round(kw + d.textlength(text, font=fnt(SANS, 14)) - col_w2),
                  "px")

    # ---------- footer ----------
    rule(d, 986)
    d.text((24, 994), "Sources: Reuters · CNN · NASA/JPL · Polygon · People · "
           "Metacritic · ISPR · Financial Times — verified 19 Nov 2026.",
           font=fnt(SANS, 12), fill=GREY)
    d.text((W - 24, 994), "make.fun", font=fnt(SANS_B, 12), fill=GREY,
           anchor="ra")

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
