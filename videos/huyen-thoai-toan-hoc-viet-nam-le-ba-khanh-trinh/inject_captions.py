#!/usr/bin/env python3
"""Replace <!--CAPTIONS_HTML_N--> and /*CAPTIONS_JS_N*/ placeholders in each
frame file with the exact generated snippet content (avoids hand-transcription
errors)."""
import os

base = os.path.dirname(os.path.abspath(__file__))
frame_files = {
    1: "01-hook.html",
    2: "02-what.html",
    3: "03-facts.html",
    4: "04-data.html",
    5: "05-context.html",
    6: "06-impact.html",
    7: "07-cta.html",
}

for i, fname in frame_files.items():
    fpath = os.path.join(base, "compositions", "frames", fname)
    if not os.path.exists(fpath):
        print(f"skip {fname} (not created yet)")
        continue
    html_snip = open(os.path.join(base, ".captions-build", f"line{i}.html.txt"), encoding="utf-8").read().rstrip("\n")
    js_snip = open(os.path.join(base, ".captions-build", f"line{i}.js.txt"), encoding="utf-8").read().rstrip("\n")

    content = open(fpath, encoding="utf-8").read()
    html_marker = f"<!--CAPTIONS_HTML_{i}-->"
    js_marker = f"/*CAPTIONS_JS_{i}*/"
    if html_marker not in content:
        print(f"WARN {fname}: html marker not found")
    if js_marker not in content:
        print(f"WARN {fname}: js marker not found")
    content = content.replace(html_marker, html_snip)
    content = content.replace(js_marker, js_snip)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{fname}: injected {html_marker} and {js_marker}")
