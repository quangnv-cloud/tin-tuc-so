#!/usr/bin/env python3
"""Build karaoke caption chunk timing (chunks of 4 words) per line, using
ElevenLabs STT word timestamps for timing but ORIGINAL SCRIPT.md text for
display (STT sometimes mis-transcribes numbers spoken as words, e.g. "860"
-> "tam tram sau muoi", or collapses "VF Wild" -> "VFY"/"VF Fly" -- confirmed
via a separate Gemini multimodal cross-check that the TTS audio itself says
"VF Wild" correctly; this is an ElevenLabs Scribe language-model bias toward
known VinFast model codes like "VF 6"/"VF 8", not a TTS pronunciation defect).
Output: assets/voice/lineN.captions.json

MERGES[line] = list of (orig_lo, orig_hi, stt_lo, stt_hi) inclusive-index
segments where the ORIGINAL word span [orig_lo, orig_hi] corresponds to the
STT word span [stt_lo, stt_hi] as a whole (their combined [start,end] is
split evenly across the original words in that span). Any words between
consecutive covered segments (or before the first / after the last) are
assumed to align 1:1 in order.
"""
import json, os

base = os.path.dirname(os.path.abspath(__file__))
lines = open(os.path.join(base, "SCRIPT.md"), encoding="utf-8").read().strip().split("\n")

MERGES = {
    2: [(28, 28, 28, 31)],                     # "860" <- "tam tram sau muoi"
    3: [(4, 4, 4, 7),                          # "860" <- "tam tram sau muoi"
        (22, 22, 25, 27),                      # "61" <- "sau muoi mot"
        (31, 31, 36, 40)],                     # "799" <- "bay tram chin muoi chin"
    4: [(0, 1, 0, 0),                          # "VF Wild" <- "VFY" (collapse)
        (7, 7, 6, 9),                          # "250" <- "hai tram nam muoi"
        (32, 32, 34, 35)],                     # "1.000" <- "mot nghin"
    5: [(0, 1, 0, 0)],                         # "VF Wild" <- "VFY" (collapse)
}


def align(orig_words, stt_words, merges):
    timed = []
    oi = 0
    si = 0
    merges = sorted(merges, key=lambda m: m[0])
    mi = 0
    while oi < len(orig_words):
        if mi < len(merges) and merges[mi][0] == oi:
            olo, ohi, slo, shi = merges[mi]
            mi += 1
            start = stt_words[slo]["start"]
            end = stt_words[shi]["end"]
            n = ohi - olo + 1
            step = (end - start) / n
            for k in range(n):
                timed.append({
                    "text": orig_words[olo + k],
                    "start": round(start + step * k, 3),
                    "end": round(start + step * (k + 1), 3),
                })
            oi = ohi + 1
            si = shi + 1
        else:
            tok = stt_words[si]
            timed.append({"text": orig_words[oi], "start": tok["start"], "end": tok["end"]})
            oi += 1
            si += 1
    assert si == len(stt_words), f"leftover stt words: consumed {si} of {len(stt_words)}"
    return timed


for i, line in enumerate(lines, start=1):
    orig_words = line.split()
    stt_path = os.path.join(base, "assets", "voice", f"line{i}.stt.json")
    d = json.load(open(stt_path, encoding="utf-8"))
    stt_words = [w for w in d["words"] if w.get("type") == "word"]

    timed = align(orig_words, stt_words, MERGES.get(i, []))
    assert len(timed) == len(orig_words), f"line{i}: {len(timed)} vs {len(orig_words)}"

    CHUNK = 4
    chunks = [timed[k:k + CHUNK] for k in range(0, len(timed), CHUNK)]

    out_chunks = []
    for ci, chunk in enumerate(chunks):
        fadein = chunk[0]["start"]
        if ci + 1 < len(chunks):
            fadeout = chunks[ci + 1][0]["start"]
        else:
            fadeout = round(chunk[-1]["end"] + 0.35, 3)
        out_chunks.append({
            "words": [{"text": w["text"], "start": w["start"]} for w in chunk],
            "fadein": round(fadein, 3),
            "fadeout": round(fadeout, 3),
        })

    out_path = os.path.join(base, "assets", "voice", f"line{i}.captions.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_chunks, f, ensure_ascii=False, indent=2)
    print(f"line{i}: {len(out_chunks)} chunks -> {out_path}")
