#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Đội tuyển Việt Nam bất ngờ vắng hàng loạt trụ cột quen thuộc trong danh sách chuẩn bị cho FIFA ASEAN Cup, nhưng lại chào đón hai gương mặt Việt kiều lần đầu được gọi tên.",
    "Sáng 18 tháng 9, huấn luyện viên Kim Sang Sik chính thức công bố danh sách 23 cầu thủ tham dự FIFA ASEAN Cup, giữ phần lớn bộ khung vừa vô địch giải đấu này.",
    "Hai tân binh là Adou Minh, trung vệ Việt kiều Pháp của câu lạc bộ Công An Hà Nội, và Williams Minh Hoàng, hậu vệ Việt kiều Anh cao một mét chín mươi của câu lạc bộ Công An Thành phố Hồ Chí Minh.",
    "Đội tuyển Việt Nam sẽ đá 3 trận trong vòng 7 ngày, gặp Philippines, Thái Lan và Pakistan ở bảng B, hạng đấu cao nhất giải.",
    "Lịch thi đấu lần lượt là gặp Philippines ngày 26 tháng 9 tại Indonesia, Thái Lan ngày 29 tháng 9, và Pakistan ngày 2 tháng 10, ngay sau chức vô địch ASEAN Cup gần nhất của đội tuyển Việt Nam.",
    "Việc vắng những gương mặt quen thuộc như thủ môn Văn Lâm, hậu vệ Đoàn Văn Hậu, cùng vài cầu thủ khác đang dự Á vận hội hoặc dính chấn thương, không ngăn huấn luyện viên Kim Sang Sik giữ ổn định lối chơi, đồng thời mở cửa cho lứa cầu thủ Việt kiều hội nhập đội tuyển quốc gia.",
    "Bạn nghĩ sao về việc đội tuyển Việt Nam tăng cường cầu thủ Việt kiều: đây là bước đi cần thiết để nâng tầm đội tuyển, hay nên ưu tiên đào tạo cầu thủ nội binh? Để lại bình luận quan điểm của bạn phía dưới nhé.",
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
