#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "U23 Việt Nam vừa có trận ra quân đầy tiếc nuối tại đại hội thể thao châu Á Asiad 20, khi chỉ cầm hòa một đều trước U23 Kuwait dù chơi lấn lướt gần trọn trận đấu.",
    "Trên đất Nhật Bản, U23 Việt Nam hòa U23 Kuwait một đều ở trận ra quân bảng C môn bóng đá nam Asiad 20, diễn ra chiều 15 tháng 9.",
    "Kuwait bất ngờ vượt lên nhờ pha đánh đầu của Omar Almatar ở phút 78, nhưng chỉ 2 phút sau, Nguyễn Ngọc Mỹ đánh đầu gỡ hòa cho Việt Nam.",
    "Việt Nam dứt điểm tới 27 lần trong trận, vượt trội hoàn toàn so với 10 lần của Kuwait, nhưng cả trận chỉ ghi được đúng 1 bàn thắng.",
    "Ngoài dứt điểm áp đảo, Việt Nam còn kiểm soát bóng tới 63%, có 8 quả phạt góc so với 4 của Kuwait, và tới 4 lần dứt điểm dội cột dọc, xà ngang trong trận.",
    "Sau lượt đấu đầu tiên bảng C, Việt Nam và Kuwait cùng có 1 điểm, xếp sau Uzbekistan, đội vừa thắng đậm Philippines 5 bàn 1; U23 Việt Nam sẽ gặp Philippines ở lượt 2 vào ngày 18 tháng 9.",
    "Dứt điểm 27 lần mà chỉ ghi được 1 bàn, bạn nghĩ U23 Việt Nam đang thiếu may mắn, hay đây thực sự là vấn đề về khả năng dứt điểm?",
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
