#!/usr/bin/env python3
"""Karaoke caption timing per line. ElevenLabs STT quota was exhausted, so word timing is
estimated: distribute SCRIPT.md words over the VOICED portion of each line (ffmpeg silencedetect),
weighted by syllable count (digit tokens ~2.2). Display text = original SCRIPT.md words."""
import json, os, re, subprocess, html
base = os.path.dirname(os.path.abspath(__file__))
lines = [l for l in open(os.path.join(base, "SCRIPT.md"), encoding="utf-8").read().split("\n") if l.strip()]
CHUNK = 4
out = {}
for i, line in enumerate(lines, 1):
    p = os.path.join(base, "assets/voice", f"line{i}.mp3")
    dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
    log = subprocess.run(["ffmpeg","-i",p,"-af","silencedetect=noise=-38dB:d=0.12","-f","null","-"],capture_output=True,text=True).stderr
    sil = []
    st = None
    for m in re.finditer(r"silence_(start|end): ([\d.]+)", log):
        if m.group(1) == "start": st = float(m.group(2))
        elif st is not None: sil.append((st, float(m.group(2)))); st = None
    if st is not None: sil.append((st, dur))
    voiced, cur = [], 0.0
    for s, e in sil:
        if s - cur > 0.03: voiced.append((cur, s))
        cur = e
    if dur - cur > 0.03: voiced.append((cur, dur))
    total_v = sum(e - s for s, e in voiced)
    words = line.split()
    w = [2.2 if re.search(r"\d", x) else 1.0 for x in words]
    # punctuation-trailing words get slightly longer
    w = [x * (1.25 if re.search(r"[,.;?]$", words[k]) else 1.0) for k, x in enumerate(w)]
    tw = sum(w)
    def to_abs(u):  # position in voiced-time -> absolute time
        for s, e in voiced:
            if u <= e - s + 1e-9: return s + u
            u -= (e - s)
        return voiced[-1][1]
    acc, timed = 0.0, []
    for k, x in enumerate(words):
        a = to_abs(acc / tw * total_v); acc += w[k]; b = to_abs(acc / tw * total_v)
        timed.append({"text": x, "start": round(a, 3), "end": round(b, 3)})
    # chunk by CHUNK words but prefer breaking after punctuation
    chunks, buf = [], []
    for t in timed:
        buf.append(t)
        if len(buf) >= CHUNK or (len(buf) >= 3 and re.search(r"[,.;?]$", t["text"])):
            chunks.append(buf); buf = []
    if buf:
        if chunks and len(buf) < 2: chunks[-1] += buf
        else: chunks.append(buf)
    res = []
    for ci, ch in enumerate(chunks):
        fin = ch[0]["start"]
        fout = chunks[ci+1][0]["start"] if ci+1 < len(chunks) else round(ch[-1]["end"] + 0.3, 3)
        res.append({"words": [{"text": x["text"], "start": x["start"]} for x in ch], "fadein": fin, "fadeout": fout})
    out[i] = res
json.dump(out, open(os.path.join(base, "assets/voice/captions.json"), "w"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in out.items()})
