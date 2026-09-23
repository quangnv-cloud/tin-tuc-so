#!/usr/bin/env python3
"""Render HTML + GSAP snippets for karaoke captions per line, ready to paste
into each frame file. Prefix per act: 01c, 02c, 03c, 04c, 05c, 06c, 07c."""
import json, os, html

base = os.path.dirname(os.path.abspath(__file__))
prefixes = {1: "h1c", 2: "h2c", 3: "h3c", 4: "h4c", 5: "h5c", 6: "h6c", 7: "h7c"}

for i in range(1, 8):
    chunks = json.load(open(os.path.join(base, "assets", "voice", f"line{i}.captions.json"), encoding="utf-8"))
    prefix = prefixes[i]
    html_lines = []
    js_lines = []
    for ci, chunk in enumerate(chunks, start=1):
        cid = f"{prefix}-{ci}"
        word_spans = []
        for wi, w in enumerate(chunk["words"], start=1):
            wid = f"{cid}-w{wi}"
            word_spans.append(f'<span class="w" id="{wid}">{html.escape(w["text"])}</span>')
        html_lines.append(f'      <div class="kcap-chunk" data-layout-allow-overlap="" id="{cid}">{" ".join(word_spans)}</div>')
        js_lines.append(f"    tl.set('#{cid}', {{autoAlpha:0}}, 0);")
        js_lines.append(f"    tl.to('#{cid}', {{autoAlpha:1, duration:0.12}}, {chunk['fadein']});")
        js_lines.append(f"    tl.to('#{cid}', {{autoAlpha:0, duration:0.12}}, {chunk['fadeout']});")
        for wi, w in enumerate(chunk["words"], start=1):
            wid = f"{cid}-w{wi}"
            js_lines.append(f"    tl.to('#{wid}', {{color:'#FF5A1F', duration:0.1}}, {w['start']});")

    out_dir = os.path.join(base, ".captions-build")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"line{i}.html.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines) + "\n")
    with open(os.path.join(out_dir, f"line{i}.js.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(js_lines) + "\n")
    print(f"line{i}: {len(chunks)} chunks rendered")
