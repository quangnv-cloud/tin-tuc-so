#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Áp thấp nhiệt đới đang áp sát miền Trung, gây gió giật cấp tám và mưa lớn diện rộng từ Hà Tĩnh đến Huế.",
    "Sáng nay, tâm áp thấp nhiệt đới nằm trên vùng biển Quảng Trị, Huế, cách thành phố Huế khoảng một trăm ki lô mét, sức gió mạnh nhất bốn mươi chín ki lô mét trên giờ, tức cấp sáu, giật cấp tám.",
    "Áp thấp di chuyển theo hướng tây tây bắc với tốc độ mười đến mười lăm ki lô mét trên giờ, dự kiến giữ nguyên cường độ trên đất liền Hà Tĩnh và phía bắc Quảng Trị đến sáng mai rồi mới suy yếu.",
    "Mưa lớn có thể vượt ba trăm năm mươi mi li mét cục bộ ở khu vực từ Hà Tĩnh đến Huế, mức cơ quan khí tượng xếp vào diện mưa rất to.",
    "Thanh Hóa và Nghệ An cũng ghi nhận mưa bốn mươi đến bảy mươi mi li mét, cục bộ trên một trăm năm mươi mi li mét, kéo theo nguy cơ lũ trên sông Ngàn Sâu và Ngàn Phố lên mức báo động hai đến báo động ba.",
    "Tính đến sáu giờ sáng nay, Quảng Trị đã có mười điểm đường và cầu tràn bị ngập, chia cắt cục bộ, còn Đà Nẵng sơ tán một trăm lẻ một hộ dân khỏi khu vực có nguy cơ sạt lở.",
    "Bạn đánh giá thế nào về công tác ứng phó áp thấp nhiệt đới lần này, đã đủ chủ động hay cần cảnh báo sớm hơn? Để lại bình luận quan điểm của bạn phía dưới nhé.",
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
