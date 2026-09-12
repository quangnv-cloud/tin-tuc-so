#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Một áp thấp nhiệt đới vừa hình thành trên Biển Đông, sức gió mạnh cấp 6, giật cấp 8, đang hướng vào miền Trung.",
    "Sáng sớm 12 tháng 9, Trung tâm Dự báo khí tượng thuỷ văn quốc gia ghi nhận vùng áp thấp cách đặc khu Hoàng Sa 150 ki-lô-mét về phía tây nam đã mạnh lên thành áp thấp nhiệt đới, di chuyển theo hướng tây bắc với tốc độ khoảng 10 ki-lô-mét mỗi giờ.",
    "Dự báo đến 4 giờ ngày 13 tháng 9, áp thấp nhiệt đới di chuyển tới vùng biển Huế, Đà Nẵng; đến 4 giờ ngày 14 tháng 9 áp thấp tới vùng biển ven bờ từ Hà Tĩnh đến Huế, sau đó suy yếu dần thành một vùng áp thấp.",
    "Ngày 13 tháng 9, mưa lớn có thể vượt 300 milimét tại khu vực từ nam Nghệ An đến Đà Nẵng.",
    "Trước đó, bão Saudel không gây thiệt hại cho Việt Nam, nhưng bão Narra dù không đổ bộ vẫn khiến hoàn lưu và rãnh áp thấp gây mưa lớn, giông sét, thiệt hại về người và tài sản.",
    "Ban Chỉ đạo Phòng thủ dân sự quốc gia đã yêu cầu các địa phương ven biển miền Trung theo dõi sát diễn biến mưa lũ, chủ động di dời người dân ở khu vực nguy cơ cao, và kiểm tra an toàn hồ chứa, đê điều.",
    "Trước đợt áp thấp nhiệt đới và mưa lớn diện rộng này, bạn đã chủ động chuẩn bị ứng phó chưa, hay vẫn đang chờ theo dõi thêm?",
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
