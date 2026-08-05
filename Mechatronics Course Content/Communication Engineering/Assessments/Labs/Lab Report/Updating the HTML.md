# Updating the Communication Engineering Report

The editable master is [[Communication Engineering Lab Report - Draft]]. The standalone browser version is [[Communication Engineering Lab Report - Draft.html]].

## Normal update process

1. Edit the Markdown master in place. New sections, paragraphs, figures, and corrections can be patched independently; the report does not need to be rewritten from scratch.
2. Store new figures in `figures/` and add them to the Markdown using relative image paths.
3. Regenerate the HTML with the renderer stored in this folder.
4. Verify headings, mathematics, figure captions, links, checkboxes, and print layout before sharing a revised copy.

The HTML embeds all current figures, so it remains a single portable file. Direct HTML edits are possible, but the Markdown source should normally remain authoritative because regenerating the report would overwrite direct changes to the exported HTML.

## Build command

```bash
/home/aaron/projects/enel700-lab-report/.venv/bin/python \
  "build_html.py" \
  "Communication Engineering Lab Report - Draft.md" \
  "Communication Engineering Lab Report - Draft.html"
```

Run that command from this report folder. The Python environment itself stays outside Obsidian to avoid syncing unnecessary package files.

Supporting build files: [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Report/build_html.py|HTML renderer]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Report/requirements.txt|Python requirements]]
