#!/usr/bin/env python3
"""Build karaoke caption chunk timing (chunks of 4 words) per line, using
ElevenLabs STT word timestamps for timing but ORIGINAL SCRIPT.md text for
display (STT sometimes mis-transcribes or normalizes spoken numbers)."""
import json, os

base = os.path.dirname(os.path.abspath(__file__))
lines = open(os.path.join(base, "SCRIPT.md"), encoding="utf-8").read().strip().split("\n")

# Manual alignment: numbers written as digits in SCRIPT.md ("32", "171", "19", "5", "40")
# get spelled out by ElevenLabs STT as multiple word tokens ("ba mươi hai", "một trăm
# bảy mươi mốt", ...). Map: orig_word_index (0-based) -> number of STT tokens it
# consumes (0 = no dedicated token, reuse previous timed word's timestamps -- used for
# "Luân Đôn" -> STT token "London"). Verified by inspecting assets/voice/lineN.stt.json
# against SCRIPT.md word counts.
MERGE = {
    3: {19: 0, 24: 2, 26: 2},          # "Đôn"<-reuse "Luân"/"London"; "40"<-2; "40,"<-2
    4: {1: 3, 17: 5, 25: 2},           # "32"<-3; "171"<-5; "19"<-2
}

for i, line in enumerate(lines, start=1):
    orig_words = line.split()
    stt_path = os.path.join(base, "assets", "voice", f"line{i}.stt.json")
    d = json.load(open(stt_path, encoding="utf-8"))
    stt_words = [w for w in d["words"] if w.get("type") == "word"]

    timed = []
    merge_map = MERGE.get(i, {})
    if merge_map:
        si = 0
        prev_entry = None
        for oi, ow in enumerate(orig_words):
            span = merge_map.get(oi, 1)
            if span == 0:
                entry = {"text": ow, "start": prev_entry["start"], "end": prev_entry["end"]}
                timed.append(entry)
                continue
            toks = stt_words[si:si + span]
            entry = {"text": ow, "start": toks[0]["start"], "end": toks[-1]["end"]}
            timed.append(entry)
            prev_entry = entry
            si += span
        if si != len(stt_words):
            print(f"line{i}: WARNING merge consumed {si} stt tokens, have {len(stt_words)}")
    elif len(orig_words) == len(stt_words):
        for ow, sw in zip(orig_words, stt_words):
            timed.append({"text": ow, "start": sw["start"], "end": sw["end"]})
    else:
        print(f"line{i}: MISMATCH orig={len(orig_words)} stt={len(stt_words)} -- NEEDS MANUAL ALIGNMENT")
        print("orig:", orig_words)
        print("stt:", [w["text"] for w in stt_words])
        # fallback: distribute evenly across stt total span (rough) -- will flag for review
        if stt_words:
            total_start = stt_words[0]["start"]
            total_end = stt_words[-1]["end"]
            span = total_end - total_start
            n = len(orig_words)
            for k, ow in enumerate(orig_words):
                timed.append({
                    "text": ow,
                    "start": round(total_start + span * k / n, 3),
                    "end": round(total_start + span * (k + 1) / n, 3),
                })

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
