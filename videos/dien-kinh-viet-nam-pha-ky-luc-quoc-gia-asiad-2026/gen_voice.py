#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Điền kinh Việt Nam vừa giành huy chương đồng đầu tiên tại đại hội thể thao châu Á Asiad 2026, đồng thời phá kỷ lục quốc gia ở nội dung tiếp sức 4 nhân 400 mét hỗn hợp nam nữ.",
    "Tại sân vận động Paloma Mizuho ở Nhật Bản, tổ tiếp sức của Việt Nam gồm Tạ Ngọc Tưởng, Quách Thị Lan, Lê Ngọc Phúc và Nguyễn Thị Ngọc về đích ở vị trí thứ ba, trong cuộc đua có Bahrain, Ấn Độ, Trung Quốc, Nhật Bản, Hàn Quốc, Philippines và Các Tiểu Vương quốc Ả Rập Thống nhất.",
    "Sau 800 mét đầu do đội Các Tiểu Vương quốc Ả Rập Thống nhất dẫn đầu, Lê Ngọc Phúc bứt tốc vươn lên dẫn đầu trước khi trao gậy cho Nguyễn Thị Ngọc, nhưng vận động viên Bahrain và Ấn Độ đã vượt lên ở 100 mét cuối.",
    "Việt Nam về đích với thời gian 3 phút 14 giây 54, phá kỷ lục quốc gia cũ 3 phút 15 giây 7 từng lập tại giải thể thao Đông Nam Á lần thứ 33 ở Thái Lan.",
    "Đội vô địch Bahrain lập kỷ lục Á vận hội mới 3 phút 12 giây 87, đội về nhì Ấn Độ đạt 3 phút 14 giây 46, cuộc đua diễn ra ngay trên đất Nhật Bản, quốc gia chủ nhà Asiad 2026.",
    "Đây là huy chương điền kinh đầu tiên của Việt Nam tại kỳ đại hội này, giúp đoàn thể thao Việt Nam xếp thứ 20 toàn đoàn với 1 huy chương vàng, 1 huy chương bạc và 15 huy chương đồng, trong khi Trung Quốc dẫn đầu bảng tổng sắp, tiếp theo là Nhật Bản và Hàn Quốc.",
    "Phá kỷ lục quốc gia nhưng vẫn chỉ về thứ ba, bạn thấy đây là một bước tiến đáng tự hào của điền kinh Việt Nam, hay khoảng cách với nhóm đầu châu Á vẫn còn quá xa?",
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
