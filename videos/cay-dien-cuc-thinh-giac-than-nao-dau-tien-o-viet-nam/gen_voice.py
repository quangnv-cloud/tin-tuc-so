#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "Lần đầu tiên tại Việt Nam, hai trẻ điếc bẩm sinh nghe được âm thanh nhờ một kỹ thuật y khoa chưa từng được thực hiện trong nước.",
    "Bệnh viện Nhi Đồng 1 tại Thành phố Hồ Chí Minh vừa cấy thành công điện cực thính giác thân não cho hai bệnh nhi, mở ra cơ hội nghe cho những trẻ điếc bẩm sinh phức tạp nhất.",
    "Bệnh nhi đầu tiên là một bé gái bốn mươi tháng tuổi ở Hà Nội, bệnh nhi thứ hai là một bé trai mười chín tháng tuổi ở Đồng Nai, cả hai đều không có dây thần kinh ốc tai ở hai bên tai.",
    "Đây là hai ca đầu tiên tại Việt Nam áp dụng kỹ thuật này, sau khi Bộ Y tế cho phép thí điểm từ tháng mười hai năm hai nghìn hai mươi lăm.",
    "Ca phẫu thuật được thực hiện bởi một kíp đa chuyên khoa của bệnh viện, dưới sự hướng dẫn trực tiếp của các chuyên gia đến từ Cộng hòa Liên bang Đức, dựa trên nền tảng hơn hai mươi năm phát triển chương trình can thiệp thính giác cho trẻ em tại đây.",
    "Sau khi thiết bị được kích hoạt, cả hai trẻ đã bắt đầu nhận biết âm thanh từ môi trường xung quanh và phản ứng rõ ràng với những âm thanh lớn, mở thêm lựa chọn cho những ca mà trước đây gia đình phải ra nước ngoài với chi phí rất lớn.",
    "Kỹ thuật này được xem là một bước ngoặt của y tế Việt Nam, nhưng hiện mới chỉ có hai trẻ được hưởng lợi. Hãy để lại bình luận, theo bạn đây là tín hiệu đáng mừng hay vẫn còn quá hiếm để nhiều gia đình có thể tiếp cận?",
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
