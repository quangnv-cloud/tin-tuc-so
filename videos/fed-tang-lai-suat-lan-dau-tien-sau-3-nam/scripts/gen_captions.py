#!/usr/bin/env python3
"""Generate karaoke caption HTML + GSAP timeline snippets from ElevenLabs STT word timestamps.

Usage: python3 scripts/gen_captions.py <line_number> <prefix> <chunk_size>
Reads assets/stt/line<N>.json, prints HTML div block + GSAP JS block to stdout.
Chunk timing: chunk visible from first word start to last word end + 0.3s pad.
Each word tweens color at its own start time (duration 0.1s).
"""
import json
import sys
import os

def main():
    line_no = sys.argv[1]
    prefix = sys.argv[2]  # short id prefix e.g. "wh" for what-happened
    chunk_size = int(sys.argv[3]) if len(sys.argv) > 3 else 4

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stt_path = os.path.join(base, "assets", "stt", f"line{line_no}.json")
    with open(stt_path, encoding="utf-8") as f:
        data = json.load(f)

    words = [w for w in data["words"] if w["type"] == "word"]
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

    html_lines = []
    js_lines = []
    js_lines.append(f"    tl.set('#{prefix}-c1', {{autoAlpha:0}}, 0);".replace("-c1", ""))  # placeholder removed below
    js_lines = []

    for ci, chunk in enumerate(chunks, start=1):
        cid = f"{prefix}-c{ci}"
        spans = []
        for wi, w in enumerate(chunk, start=1):
            wid = f"{prefix}-c{ci}-w{wi}"
            text = w["text"]
            spans.append(f'<span class="w" id="{wid}">{text}</span>')
        html_lines.append(f'      <div class="kcap-chunk" data-layout-allow-overlap="" id="{cid}">{" ".join(spans)}</div>')

        chunk_start = chunk[0]["start"]
        chunk_end = chunk[-1]["end"] + 0.3
        js_lines.append(f"    tl.set('#{cid}', {{autoAlpha:0}}, 0);")
        js_lines.append(f"    tl.to('#{cid}', {{autoAlpha:1, duration:0.12}}, {chunk_start:.3f});")
        js_lines.append(f"    tl.to('#{cid}', {{autoAlpha:0, duration:0.12}}, {chunk_end:.3f});")
        for wi, w in enumerate(chunk, start=1):
            wid = f"{prefix}-c{ci}-w{wi}"
            js_lines.append(f"    tl.to('#{wid}', {{color:'#FF5A1F', duration:0.1}}, {w['start']:.3f});")

    print("<!-- HTML -->")
    print("\n".join(html_lines))
    print("\n<!-- JS -->")
    print("\n".join(js_lines))
    total_dur = words[-1]["end"] if words else 0
    print(f"\n<!-- total word-span duration: {total_dur:.3f}s -->", file=sys.stderr)


if __name__ == "__main__":
    main()
