# Builds the four pages: wraps each body in _src/ with the shared header and footer, and fills in the
# support email. Run from the repo root: python3 tools/build.py
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "topsol.org@gmail.com"  # the support address shown on every page
pages = {
  "index.html": ("", "Quilo: AI Chatbot Assistant", "Ask anything, snap a photo, summarize a PDF or create an image. Quilo picks the right AI for every question.", "home"),
  "support/index.html": ("../", "Support · Quilo", "Get help with Quilo: subscriptions, restoring purchases, privacy and contact.", "support"),
  "privacy/index.html": ("../", "Privacy Policy · Quilo", "How Quilo handles your data.", "privacy"),
  "terms/index.html": ("../", "Terms of Use · Quilo", "The terms for using Quilo and Quilo Pro.", "terms"),
}
def nav(p, cur):
    def a(href, label, key, cls=""):
        cur_attr = ' aria-current="page"' if key == cur else ""
        c = f' class="{cls}"' if cls else ""
        return f'<li{c}><a href="{p}{href}"{cur_attr}>{label}</a></li>'
    return f'''<header class="nav"><div class="wrap">
  <a class="brand" href="{p or './'}"><img src="{p}assets/apple-touch-icon.png" alt="" width="32" height="32">Quilo</a>
  <ul>{a("support/", "Support", "support")}{a("privacy/", "Privacy", "privacy")}{a("terms/", "Terms", "terms", "hide-sm")}</ul>
</div></header>'''
def footer(p):
    return f'''<footer><div class="wrap">
  <span>© 2026 Quilo. Published by TOPSOL Innovative Solutions.</span>
  <nav><a href="{p or './'}">Home</a><a href="{p}support/">Support</a><a href="{p}privacy/">Privacy Policy</a><a href="{p}terms/">Terms of Use</a><a href="mailto:{{{{EMAIL}}}}">Contact</a></nav>
</div></footer>'''
for path, (p, title, desc, key) in pages.items():
    body = (root / "_src" / path.replace("/index.html", ".html")).read_text()
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://sohaibiii.github.io/quilo-site/assets/icon-512.png">
<meta name="apple-itunes-app" content="app-id=6834858853">
<link rel="icon" href="{p}assets/favicon.png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}assets/site.css">
</head>
<body>
{nav(p, key)}
{body}
{footer(p)}
</body>
</html>
'''
    html = html.replace("{{EMAIL}}", EMAIL)
    out = root / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
print("built", len(pages))
