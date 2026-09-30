#!/usr/bin/env python3
"""Build karaoke caption chunk timing (chunks of 4 words) per line, using
ElevenLabs STT word timestamps for timing but ORIGINAL SCRIPT.md text for
display (STT sometimes mis-transcribes or normalizes spoken numbers, e.g.
"mười hai" -> "12"). Output: assets/voice/lineN.captions.json
"""
import json, os

base = os.path.dirname(os.path.abspath(__file__))
lines = open(os.path.join(base, "SCRIPT.md"), encoding="utf-8").read().strip().split("\n")

# Manual alignment overrides go here if STT word count mismatches SCRIPT.md
# for a given line (e.g. STT collapses/expands spoken digits into numerals).
# "merge_groups": (lo, hi, stt_idx) -- orig words lo..hi <- ONE stt token at stt_idx
#   (STT collapsed several spoken words into one, e.g. numeral).
# "split_groups": (orig_idx, stt_lo, stt_hi) -- ONE orig word <- stt tokens stt_lo..stt_hi
#   (STT expanded one written numeral into several spoken words, e.g. "23" -> "hai","mươi","ba").
OVERRIDES = {
    2: {
        "split_groups": [
            (16, 16, 18),   # orig idx 16 ("23") <- stt idx 16..18 ("hai","mươi","ba")
        ]
    }
}

for i, line in enumerate(lines, start=1):
    orig_words = line.split()
    stt_path = os.path.join(base, "assets", "voice", f"line{i}.stt.json")
    d = json.load(open(stt_path, encoding="utf-8"))
    stt_words = [w for w in d["words"] if w.get("type") == "word"]

    timed = []  # list of {text, start, end}
    if i in OVERRIDES:
        merge_map = {(lo, hi): stt_idx for lo, hi, stt_idx in OVERRIDES[i].get("merge_groups", [])}
        split_map = {orig_idx: (stt_lo, stt_hi) for orig_idx, stt_lo, stt_hi in OVERRIDES[i].get("split_groups", [])}
        oi = 0
        si = 0
        while oi < len(orig_words):
            matched_merge = None
            for (lo, hi), stt_idx in merge_map.items():
                if oi == lo:
                    matched_merge = (lo, hi, stt_idx)
                    break
            if matched_merge:
                lo, hi, stt_idx = matched_merge
                tok = stt_words[stt_idx]
                span = tok["end"] - tok["start"]
                n = hi - lo + 1
                step = span / n
                for k in range(n):
                    timed.append({
                        "text": orig_words[lo + k],
                        "start": round(tok["start"] + step * k, 3),
                        "end": round(tok["start"] + step * (k + 1), 3),
                    })
                oi = hi + 1
                si = stt_idx + 1
            elif oi in split_map:
                stt_lo, stt_hi = split_map[oi]
                timed.append({
                    "text": orig_words[oi],
                    "start": stt_words[stt_lo]["start"],
                    "end": stt_words[stt_hi]["end"],
                })
                oi += 1
                si = stt_hi + 1
            else:
                tok = stt_words[si]
                timed.append({"text": orig_words[oi], "start": tok["start"], "end": tok["end"]})
                oi += 1
                si += 1
    else:
        assert len(orig_words) == len(stt_words), f"line{i}: word count mismatch {len(orig_words)} vs {len(stt_words)}"
        for ow, sw in zip(orig_words, stt_words):
            timed.append({"text": ow, "start": sw["start"], "end": sw["end"]})

    # Chunk into groups of 4 words
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
