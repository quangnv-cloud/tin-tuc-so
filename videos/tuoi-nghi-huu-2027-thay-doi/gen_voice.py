#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Từ năm hai nghìn không trăm hai mươi bảy, tuổi nghỉ hưu của người lao động Việt Nam tiếp tục tăng theo lộ trình đã được quy định từ nhiều năm trước.",
    "Theo lộ trình của bộ luật Lao động năm hai nghìn không trăm mười chín, tuổi nghỉ hưu năm hai nghìn không trăm hai mươi bảy tăng thêm ba tháng với lao động nam và bốn tháng với lao động nữ so với năm trước đó.",
    "Cụ thể, lao động nam nghỉ hưu khi đủ sáu mươi mốt tuổi chín tháng, còn lao động nữ nghỉ hưu khi đủ năm mươi bảy tuổi bốn tháng.",
    "Lộ trình tăng dần này sẽ dừng lại khi tuổi nghỉ hưu của lao động nam đạt sáu mươi hai tuổi, còn của lao động nữ đạt sáu mươi tuổi.",
    "Để được hưởng lương hưu, người lao động cần đóng bảo hiểm xã hội bắt buộc từ đủ mười lăm năm trở lên và đủ tuổi nghỉ hưu theo quy định.",
    "Người làm nghề nặng nhọc, độc hại hoặc làm việc ở vùng có điều kiện kinh tế xã hội đặc biệt khó khăn được nghỉ hưu sớm hơn tối đa năm năm, riêng người khai thác than trong hầm lò đủ mười lăm năm làm nghề được nghỉ hưu sớm hơn tối đa mười năm.",
    "Tuổi nghỉ hưu tiếp tục tăng theo lộ trình đã định, bạn thấy đây là điều chỉnh cần thiết để đảm bảo quỹ bảo hiểm xã hội, hay sẽ tạo thêm áp lực cho người lao động? Để lại bình luận quan điểm của bạn phía dưới nhé.",
]

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "voice")
os.makedirs(out_dir, exist_ok=True)

for i, text in enumerate(lines, start=1):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": { "speed": 1.09 }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={ "xi-api-key": API_KEY, "Content-Type": "application/json", "Accept": "audio/mpeg" },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"line{i}: HTTP {e.code} {e.reason}: {e.read().decode('utf-8', 'ignore')}", file=sys.stderr)
        sys.exit(1)
    out_path = os.path.join(out_dir, f"line{i}.mp3")
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"wrote {out_path} ({len(data)} bytes)")
