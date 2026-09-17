#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Cục Dự trữ Liên bang Mỹ bất ngờ tăng lãi suất lần đầu tiên sau ba năm, bất chấp phản ứng giận dữ từ Tổng thống Trump.",
    "Ngày 16 tháng 9, Cục Dự trữ Liên bang Mỹ tăng lãi suất thêm 0,25 điểm phần trăm, lên 3,75 đến 4%, lần đầu tiên kể từ năm 2023.",
    "Chủ tịch Kevin Warsh giải thích lạm phát Mỹ đã quá cao trong thời gian quá dài, và Ủy ban Thị trường Mở Liên bang nhất trí thông qua quyết định.",
    "Mức lãi suất mới là 3,75 đến 4%, trong khi chỉ số giá tiêu dùng tháng 8 vẫn ở 3,4%, cao hơn mục tiêu dài hạn 2% của Cục Dự trữ Liên bang.",
    "Cục Dự trữ Liên bang cũng nâng dự báo lạm phát chi tiêu tiêu dùng cá nhân lên 3,7%, tăng trưởng kinh tế lên 2,3%, và 12 trên 18 nhà hoạch định chính sách dự báo cần thêm một đợt tăng lãi suất nữa trước cuối năm.",
    "Sáng 17 tháng 9, Ngân hàng Nhà nước nâng tỷ giá trung tâm lên 25.632 đồng một đô la Mỹ, cao nhất từ trước đến nay, còn giá vàng SJC giảm 700.000 đồng mỗi lượng, xuống 142,8 đến 145,8 triệu đồng một lượng.",
    "Lãi suất tăng để kiềm chế lạm phát: bạn thấy đây là bước đi cần thiết, hay chỉ khiến người vay tiền thêm gánh nặng? Để lại bình luận nêu quan điểm của bạn.",
]

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "audio")
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
