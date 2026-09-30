#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Từ năm hai nghìn không trăm hai mươi bảy, hàng triệu lao động Việt Nam sẽ nghỉ hưu muộn hơn theo đúng lộ trình đã quy định.",
    "Tuổi nghỉ hưu năm hai nghìn không trăm hai mươi bảy tăng thêm ba tháng với lao động nam và bốn tháng với lao động nữ, so với năm trước đó.",
    "Để được hưởng lương hưu, người lao động phải đóng bảo hiểm xã hội bắt buộc từ đủ mười lăm năm trở lên, và đạt đúng độ tuổi quy định.",
    "Cụ thể, lao động nam nghỉ hưu ở tuổi sáu mươi mốt và chín tháng, lao động nữ nghỉ hưu ở tuổi năm mươi bảy và bốn tháng.",
    "Tuổi nghỉ hưu đã tăng dần đều mỗi năm kể từ năm hai nghìn không trăm hai mươi mốt, khi đó nam giới nghỉ hưu ở tuổi sáu mươi và ba tháng; lộ trình sẽ dừng lại khi nam đạt sáu mươi hai tuổi vào năm hai nghìn không trăm hai mươi tám, và nữ đạt sáu mươi tuổi vào năm hai nghìn không trăm ba mươi lăm.",
    "Mức lương hưu hằng tháng cao nhất bằng bảy mươi lăm phần trăm bình quân tiền lương đóng bảo hiểm; lao động nữ đạt mức này sau ba mươi năm đóng, lao động nam sau ba mươi lăm năm đóng.",
    "Lộ trình tăng tuổi nghỉ hưu này là cần thiết để giữ quỹ bảo hiểm xã hội bền vững, hay đang tạo thêm áp lực cho người lao động lớn tuổi? Để lại bình luận nêu quan điểm của bạn.",
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
