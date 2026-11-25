#!/usr/bin/env python3
"""Vbee TTS per line: write UTF-8 JSON file, POST with curl --data-binary, download audio_link immediately."""
import json, os, subprocess, sys
lines = open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')
which = [int(x) for x in sys.argv[1:]] or list(range(1, 8))
os.makedirs('assets/voice', exist_ok=True)
for n in which:
    body = {"app_id": os.environ['VBEE_APP_ID'], "input_text": lines[n-1], "voice_code": "hn_male_minhquan_yt-stable",
            "audio_type": "mp3", "bitrate": 128, "speed_rate": 1.09, "response_type": "direct"}
    jf = f'assets/voice/line{n}.json'
    with open(jf, 'w', encoding='utf-8') as f:
        json.dump(body, f, ensure_ascii=False)
    out = subprocess.run(['curl', '-s', '--max-time', '90', '-X', 'POST', 'https://vbee.vn/api/v1/tts',
                          '-H', 'Authorization: Bearer ' + os.environ['VBEE_TOKEN'],
                          '-H', 'Content-Type: application/json; charset=utf-8', '--data-binary', '@' + jf],
                         capture_output=True, text=True).stdout
    os.remove(jf)  # do not keep credentials on disk
    try:
        r = json.loads(out)
    except Exception:
        print(n, 'BAD RESPONSE', out[:300]); sys.exit(1)
    if r.get('status') != 1:
        print(n, 'ERROR', json.dumps({k: v for k, v in r.items() if k != 'app_id'}, ensure_ascii=False)[:500]); sys.exit(1)
    link = r['result']['audio_link']
    subprocess.run(['curl', '-sL', '-o', f'assets/voice/line{n}.mp3', link], check=True)
    d = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'assets/voice/line{n}.mp3']).decode().strip()
    print(n, 'ok', d, flush=True)
