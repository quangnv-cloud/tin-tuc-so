#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Lãi suất cho vay giữa các ngân hàng bất ngờ lao dốc, trong khi lãi suất tiết kiệm của người dân vẫn đứng ở mức cao kỷ lục.",
    "Trong tuần từ ngày 7 đến 11 tháng 9, lãi suất liên ngân hàng kỳ hạn qua đêm giảm mạnh, từ 4,6% xuống chỉ còn 1,5% một năm.",
    "Kỳ hạn 1 tuần cũng giảm còn 3%, kỳ hạn 2 tuần còn 3,8%; Ngân hàng Nhà nước hút ròng gần 2.600 tỷ đồng khỏi hệ thống.",
    "Trong khi đó, gửi tiết kiệm từ 10 tỷ đồng, kỳ hạn 13 tháng tại ngân hàng MBV, người dân vẫn được hưởng lãi suất tới 9,46% một năm.",
    "Nhóm ngân hàng quốc doanh niêm yết quanh 6,8%, nhóm cổ phần như ACB, Sacombank từ 7 đến 7,8%, còn mức thực nhận thoả thuận lên tới 9,2%.",
    "Người gửi từ 100 nghìn đồng cũng được cộng thêm lãi suất ưu đãi, còn ngân hàng NCB treo thưởng tổng trị giá tới 65 tỷ đồng để hút thêm tiền gửi.",
    "Lãi suất tiết kiệm cao là tin vui cho người gửi tiền, hay dấu hiệu ngân hàng đang khát vốn? Để lại bình luận quan điểm của bạn.",
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
