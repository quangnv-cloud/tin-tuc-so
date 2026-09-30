#!/usr/bin/env python3
import os, sys, json, urllib.request, mimetypes, uuid

API_KEY = os.environ["ELEVENLABS_API_KEY"]
URL = "https://api.elevenlabs.io/v1/speech-to-text"

base = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(base, "assets", "voice")

for i in range(1, 8):
    path = os.path.join(out_dir, f"line{i}.mp3")
    with open(path, "rb") as f:
        file_data = f.read()

    boundary = uuid.uuid4().hex
    def field(name, value):
        return (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n").encode()

    body = b""
    body += field("model_id", "scribe_v1")
    body += field("timestamps_granularity", "word")
    body += field("language_code", "vi")
    body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"line{i}.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n".encode()
    body += file_data
    body += f"\r\n--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        URL,
        data=body,
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"line{i}: HTTP {e.code} {e.reason}: {e.read().decode('utf-8','ignore')}", file=sys.stderr)
        sys.exit(1)

    out_path = os.path.join(out_dir, f"line{i}.stt.json")
    with open(out_path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    words = [w for w in data.get("words", []) if w.get("type") == "word"]
    print(f"line{i}: {len(words)} words -> {out_path}")
