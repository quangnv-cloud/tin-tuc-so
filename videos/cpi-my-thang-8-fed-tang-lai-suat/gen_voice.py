#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Lạm phát Mỹ tháng 8 vẫn dai dẳng, đẩy khả năng Cục Dự trữ Liên bang Mỹ tăng lãi suất ngay tuần tới lên gần 90%.",
    "Cục Thống kê Lao động Mỹ công bố chỉ số giá tiêu dùng tháng 8 tăng 0,4% so với tháng trước và tăng 3,4% so với cùng kỳ năm ngoái, đúng như dự báo của giới phân tích.",
    "Lạm phát lõi, tức chỉ số đã loại trừ thực phẩm và năng lượng, tăng 0,3% trong tháng và neo ở mức 2,4% tính theo năm, cao hơn kỳ vọng của thị trường.",
    "Ngay sau báo cáo, xác suất Cục Dự trữ Liên bang Mỹ tăng thêm 0,25 điểm phần trăm lãi suất trong tuần tới vọt từ khoảng 70% lên gần 90%.",
    "Giá năng lượng là động lực chính khi giá xăng tăng 3,9% trong tháng, trong khi thị trường lao động Mỹ đón nhận thêm 162 nghìn việc làm mới, vượt xa dự báo và củng cố khả năng Cục Dự trữ Liên bang Mỹ mạnh tay hơn.",
    "Ngay trong phiên sáng 11 tháng 9, chứng khoán Mỹ vẫn tăng điểm nhờ giá dầu hạ nhiệt, chỉ số Dow Jones tăng gần 600 điểm, còn lợi suất trái phiếu chính phủ kỳ hạn 2 năm tăng lên khoảng 4,6 phần trăm.",
    "Nếu Cục Dự trữ Liên bang Mỹ tiếp tục tăng lãi suất trong tuần tới, bạn nghĩ đây là bước đi cần thiết để kiểm soát lạm phát, hay sẽ tạo thêm áp lực lên thị trường tài chính? Để lại bình luận quan điểm của bạn phía dưới nhé.",
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
