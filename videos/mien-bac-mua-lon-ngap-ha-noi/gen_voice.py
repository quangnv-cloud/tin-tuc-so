#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Mưa lớn dồn dập khiến Hà Nội ngập nhiều tuyến phố ngay trong đêm, có nơi lượng mưa vượt 270 milimét chỉ trong một ngày.",
    "Hậu áp thấp nhiệt đới kết hợp không khí lạnh gây mưa lớn diện rộng từ miền Trung ra Bắc Bộ, dự báo còn kéo dài đến ngày 16 tháng 9.",
    "Tại nội thành Hà Nội, Yên Sở ghi nhận mưa lớn nhất với 270,4 milimét, trong khi một số điểm ở Quảng Trị và Huế mưa vượt 800, thậm chí hơn 1.300 milimét.",
    "Riêng từ 10 giờ tối đến 6 giờ sáng, nhiều phường nội thành đã mưa trên 150 milimét, dẫn đầu là Yên Sở, tiếp theo là Hai Bà Trưng với 219,2 milimét.",
    "Mưa lớn dự báo còn tiếp diễn đến 16 tháng 9 rồi giảm dần, trong khi mực nước nhiều sông ở Bắc Bộ và Thanh Hoá đang lên nhanh, có sông áp sát mức báo động 3.",
    "Mưa lũ đã làm ngập 591 nhà tại Quảng Trị và hư hại hơn 1.000 héc-ta lúa, hoa màu; 712 hộ dân từng sơ tán nay đã trở về nhà an toàn.",
    "Ngập lụt đô thị sau mưa lớn kỷ lục: do thời tiết cực đoan, hay do hạ tầng thoát nước quá tải? Để lại bình luận quan điểm của bạn.",
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
