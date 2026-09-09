#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Việt Nam sắp được nâng hạng thị trường chứng khoán, nhưng khối ngoại vẫn đang bán ròng hàng chục nghìn tỷ đồng.",
    "Tổ chức xếp hạng thị trường FTSE Russell sẽ chính thức nâng hạng chứng khoán Việt Nam, từ thị trường cận biên lên thị trường mới nổi thứ cấp, có hiệu lực từ ngày hai mươi mốt tháng chín.",
    "Chiều ngày tám tháng chín, chỉ số VN-Index giao dịch quanh 1.827 điểm, tăng hơn 5 điểm, phục hồi sau phiên giảm bất ngờ 31 điểm hồi đầu tuần.",
    "Nhưng tính từ đầu năm đến nay, nhà đầu tư nước ngoài đã bán ròng hơn 90 nghìn tỷ đồng trên sàn Thành phố Hồ Chí Minh, bất chấp tin vui nâng hạng.",
    "Việc nâng hạng được áp dụng theo 4 giai đoạn, kéo dài đến tháng 9 năm sau, và đợt đầu tiên chỉ tính khoảng 10% tỷ trọng đầy đủ, nên dòng vốn mới sẽ vào từng bước chứ không ồ ạt.",
    "Giới phân tích tài chính nhận định, nâng hạng là điều kiện cần nhưng chưa đủ để dòng vốn ngoại quay lại, bởi quyết định của họ còn phụ thuộc tỷ giá, lãi suất toàn cầu và lợi nhuận doanh nghiệp Việt Nam.",
    "Theo bạn, nâng hạng thị trường có thực sự kéo dòng vốn ngoại trở lại Việt Nam, hay chỉ là kỳ vọng ngắn hạn? Để lại bình luận quan điểm của bạn phía dưới nhé.",
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
