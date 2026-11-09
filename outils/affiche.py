# -*- coding: utf-8 -*-
"""Affiche A4/A3 portrait avec QR code.  Usage : python outils/affiche.py [URL]
L'URL par défaut est PROVISOIRE : ne rien imprimer avant d'avoir relancé le script avec la vraie adresse du site."""
import os, sys, segno, io
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = sys.argv[1] if len(sys.argv) > 1 else "https://perroquet-vert-honfleur.fr/"
OUT = os.path.join(ROOT, "affiches"); os.makedirs(OUT, exist_ok=True)
VERT = (63, 160, 90); VERT_F = (36, 118, 66); OR = (201, 162, 78); CREME = (248, 244, 232); NOIR = (20, 22, 20)

def font(name, size, wght):
    f = ImageFont.truetype(os.path.join(ROOT, "outils", "polices", name), size)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f

def centre(d, y, txt, f, fill, W, spacing=0):
    if spacing:
        w = sum(d.textlength(c, font=f) + spacing for c in txt) - spacing
        x = (W - w) / 2
        for c in txt:
            d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + spacing
    else:
        w = d.textlength(txt, font=f); d.text(((W - w) / 2, y), txt, font=f, fill=fill)

def make(W, H, name):
    u = W / 2480  # échelle par rapport à l'A4 à 300 ppp
    S = lambda v: int(v * u)
    im = Image.new("RGB", (W, H), CREME); d = ImageDraw.Draw(im)
    # photo en haut
    ph = Image.open(os.path.join(ROOT, "img", "petit-dejeuner.jpg")).convert("RGB")
    ph_h = S(1000); r = max(W / ph.width, ph_h / ph.height)
    ph = ph.resize((int(ph.width * r), int(ph.height * r)), Image.LANCZOS)
    ox = (ph.width - W) // 2; oy = int((ph.height - ph_h) * 0.5)
    im.paste(ph.crop((ox, oy, ox + W, oy + ph_h)), (0, 0))
    # courbe crème sous la photo
    d.ellipse((-S(900), ph_h - S(160), W + S(900), ph_h + S(900)), fill=CREME)
    # logo (pastille verte)
    lg = Image.open(os.path.join(ROOT, "img", "logo.png")).convert("RGBA")
    cd = S(480); cx, cy = W // 2, ph_h - S(40)
    d.ellipse((cx - cd // 2 - S(18), cy - cd // 2 - S(18), cx + cd // 2 + S(18), cy + cd // 2 + S(18)), fill=CREME)
    d.ellipse((cx - cd // 2, cy - cd // 2, cx + cd // 2, cy + cd // 2), fill=NOIR, outline=OR, width=S(10))
    lw = int(cd * 0.74); lh = int(lw * lg.height / lg.width)
    lg = lg.resize((lw, lh), Image.LANCZOS); im.paste(lg, (cx - lw // 2, cy - lh // 2), lg)
    # titre
    y = cy + cd // 2 + S(50)
    centre(d, y, "Le Perroquet Vert", font("corm.ttf", S(220), 600), VERT_F, W)
    y += S(270)
    centre(d, y, "BAR · BRUNCH · BILLARD · QUAI SAINTE-CATHERINE", font("jost.ttf", S(48), 400), (110, 108, 98), W, spacing=S(9))
    y += S(110)
    centre(d, y, "Un bon moment au Perroquet Vert ?", font("corm-i.ttf", S(120), 500), NOIR, W)
    y += S(170)
    centre(d, y, "Votre avis aide d'autres voyageurs à nous trouver.", font("jost.ttf", S(52), 300), (110, 108, 98), W)
    # QR
    q = segno.make(URL, error="h", micro=False)
    buf = io.BytesIO(); q.save(buf, kind="png", scale=1, border=0, dark=VERT_F, light=(255, 255, 255)); buf.seek(0)
    qi = Image.open(buf).convert("RGB"); qs = S(700)
    qi = qi.resize((qs, qs), Image.NEAREST)
    y += S(110); pad = S(60)
    d.rounded_rectangle((W // 2 - qs // 2 - pad, y, W // 2 + qs // 2 + pad, y + qs + 2 * pad), radius=S(60), fill=(255, 255, 255), outline=OR, width=S(10))
    im.paste(qi, (W // 2 - qs // 2, y + pad))
    y += qs + 2 * pad + S(70)
    centre(d, y, "SCANNEZ AVEC VOTRE TÉLÉPHONE", font("jost.ttf", S(50), 500), VERT_F, W, spacing=S(8))
    # bandeau bas
    by = H - S(330)
    d.rectangle((0, by, W, H), fill=VERT_F)
    d.ellipse((-S(600), by - S(120), W + S(600), by + S(120)), fill=VERT_F)
    centre(d, by + S(60), "52 quai Sainte-Catherine · 14600 Honfleur", font("jost.ttf", S(58), 400), (245, 240, 220), W, spacing=S(3))
    centre(d, by + S(150), URL.replace("https://", "").rstrip("/"), font("jost.ttf", S(78), 500), (255, 226, 140), W)
    centre(d, by + S(255), "02 31 89 14 19", font("jost.ttf", S(48), 300), (225, 235, 215), W)
    im.save(os.path.join(OUT, name + ".png"))
    im.save(os.path.join(OUT, name + ".pdf"), resolution=300)

make(2480, 3508, "affiche-perroquet-vert-A4-portrait")
make(3508, 4961, "affiche-perroquet-vert-A3-portrait")
print("ok", URL)
