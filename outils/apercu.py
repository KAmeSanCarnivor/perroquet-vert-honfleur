# -*- coding: utf-8 -*-
"""Prépare le dossier _apercu/ pour le partage (aperçu privé à montrer au commerçant)."""
import os, re, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); A = os.path.join(R, "_apercu")
shutil.rmtree(A, ignore_errors=True); os.makedirs(A)
for f in ("style.css", "site.js"): shutil.copy(os.path.join(R, f), A)
shutil.copytree(os.path.join(R, "img"), os.path.join(A, "img"))
L = ["fr", "en", "nl", "de", "es", "ko"]
def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8", newline="\n").write(s)
def sub(s):  # pages dans un sous-dossier : chemins vers la racine et liens de langue explicites
    s = re.sub(r'(src|href)="(img/|style\.css|site\.js|mentions-legales\.html)', r'\1="../\2', s)
    s = re.sub(r'href="\.\./(en|nl|de|es|ko)/"', r'href="../\1/index.html"', s)
    s = s.replace('href="./"', 'href="../fr/index.html"')
    return s
fr = rd(os.path.join(R, "index.html"))
# pages en/nl/de/es/ko : liens vers fr et entre langues
for l in L[1:]:
    s = rd(os.path.join(R, l, "index.html"))
    s = re.sub(r'href="\.\./"', 'href="../fr/index.html"', s)
    s = re.sub(r'href="\.\./(en|nl|de|es|ko)/"', r'href="../\1/index.html"', s)
    wr(os.path.join(A, l, "index.html"), s)
# fr en sous-dossier (plein document) pour les liens depuis les autres langues
s = fr
s = re.sub(r'(src|href)="(img/|style\.css|site\.js|mentions-legales\.html)', r'\1="../\2', s)
s = re.sub(r'href="(en|nl|de|es|ko)/"', r'href="../\1/index.html"', s)
s = s.replace('href="./"', 'href="index.html"')
wr(os.path.join(A, "fr", "index.html"), s)
# page principale : fragment (le gabarit de publication fournit doctype/head)
m = re.search(r"<title>.*?</title>", fr, re.S)
body = re.search(r"<body>(.*)</body>", fr, re.S).group(1)
links = "".join(re.findall(r'<link [^>]*(?:preconnect|stylesheet|googleapis)[^>]*>\n?', fr))
body = re.sub(r'href="(en|nl|de|es|ko)/"', r'href="\1/index.html"', body).replace('href="./"', 'href="#haut"')
frag = "<title>Le Perroquet Vert</title>\n" + links + body
wr(os.path.join(A, "perroquet.html"), frag)
shutil.copy(os.path.join(R, "mentions-legales.html"), os.path.join(A, "mentions-legales.html"))
ml = rd(os.path.join(A, "mentions-legales.html")).replace('href="./"', 'href="perroquet.html"')
wr(os.path.join(A, "mentions-legales.html"), ml)
print("ok")
