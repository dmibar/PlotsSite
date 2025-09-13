# -*- coding: utf-8 -*-
# Генерит docs/index.html из содержимого docs/img/*
import os, html

IMG_DIR = "docs/img"
OUT = "docs/index.html"

cards = []
if os.path.isdir(IMG_DIR):
    for name in sorted(os.listdir(IMG_DIR)):
        if name.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".webp")):
            safe = html.escape(name)
            cards.append(f"""
    <div class="card">
      <a href="img/{safe}" target="_blank">
        <img src="img/{safe}" alt="{safe}" loading="lazy">
      </a>
      <div class="cap">{safe}</div>
    </div>""")

html_out = f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Our Team Plots</title>
<style>
/* ===== Dark theme + centered ===== */
body {{
  font-family: system-ui, -apple-system, Segoe UI, Arial, sans-serif;
  margin: 0;
  padding: 40px;
  background: #000;   /* чёрный фон */
  color: #fff;        /* белый текст */
  text-align: center; /* выравнивание текста */
}}
h1 {{
  margin: 0 0 24px;
  font-size: 2em;
}}
.grid {{
  display: grid;
  justify-content: center;                  /* центрируем сетку */
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;                           /* центрируем блок */
}}
.card {{
  background: #111;                         /* тёмные карточки */
  border: 1px solid #333;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 1px 4px rgba(255,255,255,0.08);
}}
.card img {{
  width: 100%;
  height: auto;
  display: block;
  border-radius: 6px;
  background: #222;
}}
.cap {{
  margin-top: 8px;
  color: #aaa;
  font-size: .95em;
  word-break: break-word;
}}
.empty {{ color: #888; }}
</style></head><body>
<h1>Our Team Plots</h1>
<div class="grid">
{''.join(cards)}
</div>
{"<p class='empty'>В папке <code>docs/img</code> нет изображений.</p>" if not cards else ""}
</body></html>"""

os.makedirs("docs", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_out)
print("✓ Wrote", OUT)
