#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Chỉ 10 phút sau khi mở bán tại Việt Nam, bản iPhone 18 Pro Max màu đỏ Burgundy đã cháy hàng đợt đầu.",
    "Apple mở cổng đặt trước iPhone 18 Pro và 18 Pro Max tại Việt Nam tối 12 tháng 9, nhiều phiên bản hết hàng chỉ sau vài phút.",
    "CellphoneS nhận hơn 10 nghìn đơn trong 15 phút, tăng 40% so với năm ngoái; Hoàng Hà Mobile hơn 9 nghìn đơn chỉ trong 10 phút.",
    "iPhone 18 Pro có giá từ 38,99 triệu đồng, tăng 4 triệu so với 17 Pro; bản Pro Max từ 41,99 triệu đồng.",
    "Thế hệ mới có Dynamic Island nhỏ hơn 25%, lần đầu trang bị camera khẩu độ biến thiên, và thêm 3 màu mới.",
    "Ngay sau đó, Apple khai tử 3 mẫu iPhone cũ, còn tại Việt Nam, Viettel Store ghi nhận gần 60 nghìn lượt quan tâm chỉ sau 2 ngày.",
    "Cháy hàng vì nhu cầu thật, hay vì nguồn cung nhỏ giọt có chủ đích? Để lại bình luận quan điểm của bạn.",
]

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "voice")
os.makedirs(out_dir, exist_ok=True)

for i, text in enumerate(lines, start=1):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "speed": 1.09
        }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
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
