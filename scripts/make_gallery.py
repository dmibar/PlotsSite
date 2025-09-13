# -*- coding: utf-8 -*-
import os, html

IMG_DIR = "docs/img"
OUT = "docs/index.html"

cards = []
if os.path.isdir(IMG_DIR):
    for name in sorted(os.listdir(IMG_DIR)):
        if name.lower().endswith((".png", ".jpg", ".jpeg", ".svg")):
            safe = html.escape(name)
            cards.append(f"""
    <div class="card">
      <a href="img/{safe}" target="_blank"><img src="img/{safe}" alt="{safe}" loading="lazy"></a>
      <div class="cap">{safe}</div>
    </div>""")

html_out = f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Галерея графиков</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Arial,sans-serif;margin:20px;background:#fafafa}}
h1{{margin:0 0 16px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
.card{{background:#fff;border:1px solid #e5e5e5;border-radius:10px;padding:10px;box-shadow:0 1px 2px rgba(0,0,0,.04)}}
.card img{{width:100%;height:auto;display:block;border-radius:6px;background:#f5f5f5}}
.cap{{margin-top:8px;color:#555;font-size:.9em;word-break:break-word}}
.empty{{color:#666}}
</style></head><body>
<h1>Галерея графиков</h1>
<div class="grid">
{''.join(cards)}
</div>
{"<p class='empty'>В папке <code>docs/img</code> нет изображений.</p>" if not cards else ""}
</body></html>"""

os.makedirs("docs", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_out)
print("✓ Wrote", OUT)
