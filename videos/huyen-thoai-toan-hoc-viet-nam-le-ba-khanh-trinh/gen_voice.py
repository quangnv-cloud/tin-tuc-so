#!/usr/bin/env python3
"""Generate per-line ElevenLabs voiceover mp3 files for SCRIPT.md."""
import json
import os
import re
import sys
import urllib.request

VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"  # Khánh Lâm - tin tức, thời sự
MODEL_ID = "eleven_v3"
API_KEY = os.environ["ELEVENLABS_API_KEY"]
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

script_path = sys.argv[1] if len(sys.argv) > 1 else "SCRIPT.md"
out_dir = sys.argv[2] if len(sys.argv) > 2 else "assets/audio"
os.makedirs(out_dir, exist_ok=True)

with open(script_path, encoding="utf-8") as f:
    lines = [ln.strip() for ln in f if ln.strip()]

print(f"{len(lines)} lines found in {script_path}")

for i, line in enumerate(lines, start=1):
    payload = {
        "text": line,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "speed": 1.09,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "xi-api-key": API_KEY,
            "Accept": "audio/mpeg",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        audio = resp.read()
    out_path = os.path.join(out_dir, f"line{i}.mp3")
    with open(out_path, "wb") as f:
        f.write(audio)
    print(f"line{i}.mp3 written ({len(audio)} bytes): {line[:60]}...")
