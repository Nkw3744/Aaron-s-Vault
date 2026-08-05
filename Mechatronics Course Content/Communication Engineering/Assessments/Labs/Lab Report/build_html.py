#!/usr/bin/env python3
"""Render the editable ENEL700 Markdown draft as a standalone HTML file."""

from __future__ import annotations

import argparse
import base64
import html
import io
import mimetypes
import re
from datetime import date
from pathlib import Path

import markdown
from PIL import Image


CSS = r"""
:root {
  --ink: #172033;
  --muted: #667085;
  --navy: #102a43;
  --blue: #2563eb;
  --cyan: #0ea5e9;
  --paper: #ffffff;
  --surface: #f5f7fb;
  --line: #d9e1ec;
  --draft-bg: #fff7df;
  --draft-line: #e4ae32;
  --code: #eff4fb;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--surface);
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.68;
}
.hero {
  color: white;
  background: linear-gradient(125deg, #0b1f33 0%, #123f66 58%, #176b87 100%);
  padding: 3.2rem max(1.5rem, calc((100vw - 1180px)/2));
  border-bottom: 5px solid #3dd5f3;
}
.hero .eyebrow {
  margin: 0 0 .55rem;
  color: #8fe8f8;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  font-size: .78rem;
}
.hero h1 { margin: 0; max-width: 900px; color: white; font-size: clamp(2rem, 5vw, 3.4rem); line-height: 1.08; }
.hero p { max-width: 780px; margin: 1rem 0 0; color: #d9edf5; }
.badges { display: flex; flex-wrap: wrap; gap: .6rem; margin-top: 1.25rem; }
.badge { padding: .35rem .65rem; border: 1px solid rgba(255,255,255,.25); border-radius: 999px; background: rgba(255,255,255,.10); font-size: .82rem; font-weight: 700; }
.layout { display: grid; grid-template-columns: 270px minmax(0, 860px); gap: 2rem; max-width: 1180px; margin: 2rem auto 4rem; padding: 0 1.25rem; align-items: start; }
nav {
  position: sticky; top: 1rem; max-height: calc(100vh - 2rem); overflow: auto;
  background: var(--paper); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1rem 1.1rem;
  box-shadow: 0 8px 26px rgba(17, 42, 67, .06);
}
nav strong { display: block; color: var(--navy); margin-bottom: .55rem; }
nav ul { list-style: none; margin: 0; padding-left: 0; }
nav ul ul { padding-left: .8rem; border-left: 1px solid var(--line); }
nav li { margin: .35rem 0; }
nav a { color: #3d5168; text-decoration: none; font-size: .9rem; }
nav a:hover { color: var(--blue); }
article {
  background: var(--paper); border: 1px solid var(--line); border-radius: 16px;
  padding: clamp(1.35rem, 4vw, 3.4rem); box-shadow: 0 14px 40px rgba(17, 42, 67, .07);
}
article > h1:first-child { display: none; }
h1, h2, h3, h4 { color: var(--navy); line-height: 1.25; scroll-margin-top: 1rem; }
h2 { margin-top: 2.8rem; padding-bottom: .45rem; border-bottom: 2px solid #dbe8f3; font-size: 1.65rem; }
h3 { margin-top: 2rem; color: #174f75; }
h4 { color: #25627f; }
p { margin: .85rem 0; }
a { color: var(--blue); }
blockquote {
  margin: 1.25rem 0; padding: 1rem 1.15rem; border-left: 5px solid var(--draft-line);
  background: var(--draft-bg); border-radius: 0 10px 10px 0; color: #5f470e;
}
blockquote p { margin: .3rem 0; }
code { background: var(--code); border-radius: 5px; padding: .12rem .35rem; font-size: .92em; }
pre { overflow: auto; background: #101c2b; color: #e6edf5; padding: 1rem; border-radius: 10px; }
pre code { background: transparent; padding: 0; }
ul, ol { padding-left: 1.35rem; }
li { margin: .35rem 0; }
.task { list-style: none; margin-left: -1.2rem; }
.task input { margin-right: .5rem; accent-color: var(--blue); }
table { width: 100%; border-collapse: collapse; margin: 1.2rem 0; font-size: .94rem; }
th { background: #eaf2f8; color: var(--navy); text-align: left; }
th, td { border: 1px solid var(--line); padding: .65rem .7rem; vertical-align: top; }
figure { margin: 1.65rem 0 2rem; padding: .75rem; border: 1px solid var(--line); border-radius: 12px; background: #fbfcfe; }
figure img { display: block; width: 100%; height: auto; border-radius: 7px; }
figcaption { margin: .65rem .25rem .15rem; color: var(--muted); font-size: .9rem; text-align: center; }
details { margin: 1.5rem 0; border: 1px solid var(--line); border-radius: 12px; background: #fbfcfe; overflow: hidden; }
summary { cursor: pointer; padding: .9rem 1rem; color: var(--navy); background: #eaf2f8; font-weight: 700; }
details[open] > summary { border-bottom: 1px solid var(--line); }
details > :not(summary) { margin-left: 1rem; margin-right: 1rem; }
details > h2 { margin-top: 1.6rem; }
hr { border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }
.footer { max-width: 1180px; margin: -2rem auto 3rem; padding: 0 1.25rem; color: var(--muted); font-size: .85rem; text-align: right; }
@media (max-width: 880px) {
  .layout { grid-template-columns: 1fr; }
  nav { position: static; max-height: none; }
  article { border-radius: 12px; }
}
@media print {
  body { background: white; font-size: 10.5pt; }
  .hero { padding: 1.2cm 1.5cm; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .hero h1 { font-size: 24pt; }
  .layout { display: block; max-width: none; margin: 0; padding: 0; }
  nav { display: none; }
  article { border: 0; box-shadow: none; padding: 1.2cm 1.5cm; }
  h2, h3, figure, table { break-inside: avoid; }
  figure { page-break-inside: avoid; }
  details { border: 0; overflow: visible; }
  details > summary { display: none; }
  details:not([open]) > *:not(summary) { display: block; }
  a { color: inherit; text-decoration: none; }
  .footer { display: none; }
}
"""


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def replace_wikilinks(text: str) -> str:
    # Standalone HTML cannot resolve Obsidian links; retain readable labels.
    return re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"**\2**", text)


def prepare_markdown(text: str) -> tuple[str, dict[str, str]]:
    """Protect TeX delimiters from Markdown and simplify Obsidian callouts."""
    text = re.sub(
        r"^> \[![^\]]+\]\s*(.+)$",
        r"> **\1**",
        text,
        flags=re.MULTILINE,
    )
    protected: dict[str, str] = {}

    def hold_display(match: re.Match[str]) -> str:
        token = f"MATHDISPLAYTOKEN{len(protected)}X"
        protected[token] = f'<div class="math-display">\\[{match.group(1).strip()}\\]</div>'
        return token

    def hold_inline(match: re.Match[str]) -> str:
        token = f"MATHINLINETOKEN{len(protected)}X"
        protected[token] = f'<span class="math-inline">\\({match.group(1).strip()}\\)</span>'
        return token

    text = re.sub(r"\\\[(.*?)\\\]", hold_display, text, flags=re.DOTALL)
    text = re.sub(r"\\\((.*?)\\\)", hold_inline, text, flags=re.DOTALL)
    return text, protected


def embed_figures(rendered: str, source_dir: Path) -> str:
    pattern = re.compile(r'<p><img alt="([^"]*)" src="([^"]+)"\s*/?></p>')

    def repl(match: re.Match[str]) -> str:
        alt, src = match.group(1), match.group(2)
        path = (source_dir / src).resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Missing figure: {path}")
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        raw = path.read_bytes()
        # Keep the Markdown linked to the original in-class evidence, but avoid
        # turning large phone photographs into an unnecessarily huge HTML file.
        if mime in {"image/jpeg", "image/png", "image/webp"} and len(raw) > 1_000_000:
            with Image.open(io.BytesIO(raw)) as image:
                image.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
                if image.mode != "RGB":
                    background = Image.new("RGB", image.size, "white")
                    if "A" in image.getbands():
                        background.paste(image, mask=image.getchannel("A"))
                    else:
                        background.paste(image)
                    image = background
                compressed = io.BytesIO()
                image.save(compressed, format="JPEG", quality=88, optimize=True)
                raw = compressed.getvalue()
                mime = "image/jpeg"
        data = base64.b64encode(raw).decode("ascii")
        return (
            f'<figure><img src="data:{mime};base64,{data}" alt="{html.escape(alt)}">'
            f'<figcaption>{html.escape(alt)}</figcaption></figure>'
        )

    return pattern.sub(repl, rendered)


def build(source: Path, output: Path) -> None:
    text = replace_wikilinks(strip_frontmatter(source.read_text(encoding="utf-8")))
    text, protected_math = prepare_markdown(text)
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists"], output_format="html5")
    body = md.convert(text)
    for token, replacement in protected_math.items():
        body = body.replace(token, replacement)
    def task_item(match: re.Match[str]) -> str:
        checked = " checked" if match.group(1).lower() == "x" else ""
        return (
            f'<li class="task"><input type="checkbox" disabled{checked}>'
            f'{match.group(2)}</li>'
        )

    body = re.sub(
        r"<li>\[([ xX])\]\s*(.*?)</li>",
        task_item,
        body,
        flags=re.DOTALL,
    )
    body = embed_figures(body, source.parent)
    toc = md.toc or "<p>No headings found.</p>"

    generated_on = date.today().strftime("%d %B %Y")
    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ENEL700 Communication Engineering Laboratory Report — Draft</title>
<style>{CSS}</style>
<script>
window.MathJax = {{tex: {{inlineMath: [['\\\\(','\\\\)']], displayMath: [['\\\\[','\\\\]']]}}}};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
<header class="hero">
  <p class="eyebrow">ENEL700 · Working report</p>
  <h1>Communication Engineering Laboratory Report</h1>
  <p>A running candidate report built first from the group’s in-class files and Aaron’s weekly account, with later analysis kept clearly separate.</p>
  <div class="badges"><span class="badge">Working draft</span><span class="badge">In-class evidence first</span><span class="badge">Lab 4 + Lab 5 drafted</span><span class="badge">Three-lab selection pending</span></div>
</header>
<div class="layout">
  <nav><strong>Contents</strong>{toc}</nav>
  <article>{body}</article>
</div>
<div class="footer">Generated from the editable Markdown source · {generated_on}</div>
</body>
</html>"""
    output.write_text(document, encoding="utf-8")
    print(f"WROTE {output}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
