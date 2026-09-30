import json, os, sys, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"

lines = [l.strip() for l in open("SCRIPT.md", encoding="utf-8") if l.strip()]
assert len(lines) == 7, f"expected 7 lines, got {len(lines)}"

for i, text in enumerate(lines, start=1):
    payload = {
        "text": text,
        "model_id": "eleven_v3",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "speed": 1.09}
    }
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"xi-api-key": API_KEY, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print("ERROR line", i, e.code, e.read().decode())
        sys.exit(1)
    out = f"assets/audio/voice/line{i}.mp3"
    with open(out, "wb") as f:
        f.write(data)
    print("wrote", out, len(data), "bytes")
