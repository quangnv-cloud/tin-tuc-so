# COMPLIANCE — gia-xang-dau-tang-hon-1200-dong-lit

**LƯU Ý: LẦN CHẠY TEST** — kiểm tra chất lượng pipeline trên environment/team mới, KHÔNG phải lần
sản xuất thật. Routine dừng lại sau bước 13 theo yêu cầu; KHÔNG thực hiện bước 14-16 (publish
Facebook/YouTube). Toàn bộ nội dung dưới đây vẫn được thực hiện đầy đủ, không hạ chuẩn.

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-10T10:09:01Z
platforms: [facebook_reel, youtube_shorts]  # dự kiến — CHƯA đăng trong lần chạy test này

GATE A (topic pick): GREEN
trending_signal: "giá xăng dầu" (Google Trends VN, id 87f1ccd3ac31, vị trí #1/197 trong danh sách
  chưa dùng, trafficApprox "200+", pubDate 2026-09-10T08:30:00Z)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card lấy từ ?image=eb4b27f442ec (CDN báo Tuổi Trẻ, ảnh báo
  gốc có dẫn nguồn, không watermark ngoài, không chỉnh sửa nội dung); nhạc nền sinh bằng Google
  Lyria (lyria-recipe.py, preset calm, density 0.25/brightness 0.4, negative-prompt loại bỏ giọng
  hát/lời), 100% không lời, thuộc quyền dự án; SFX từ thư viện repo (_reference-astra-openai/assets/sfx);
  giọng đọc ElevenLabs 'Khánh Lâm - tin tức, thời sự' (voice_id RCmOaM1iiIH5xX3QXjIF, model eleven_v3)."
claims_verified:
  - "Bộ Công Thương thông báo điều chỉnh giá xăng dầu, áp dụng từ 15h ngày 10-9-2026 — Tuổi Trẻ (?article=eb4b27f442ec) + VnExpress (?article=9ec4abd03d41)"
  - "Xăng E5 RON92: 23.744 đồng/lít, tăng 1.258 đồng/lít — Tuổi Trẻ (VnExpress: 23.740đ/+1.260đ, chênh làm tròn không đáng kể)"
  - "Xăng E10 RON95-III: 24.239 đồng/lít, tăng 965 đồng/lít — Tuổi Trẻ (VnExpress: 24.230đ/+960đ)"
  - "Dầu diesel 0.05S: 28.485 đồng/lít, tăng 742 đồng/lít — Tuổi Trẻ (VnExpress: 28.480đ)"
  - "Dầu mazut 180CST 3.5S: 18.157 đồng/kg, tăng 516 đồng/kg — Tuổi Trẻ (VnExpress: 18.150đ)"
  - "Nguyên nhân: đà biến động thị trường xăng dầu/năng lượng thế giới — Tuổi Trẻ + VnExpress"
  - "Liên bộ Công Thương - Tài chính dừng trích lập quỹ bình ổn giá về 0 đồng, riêng xăng sinh học được chi 500 đồng/lít — Tuổi Trẻ"
  - "Đây là kỳ tăng giá liên tiếp sau đợt tăng của kỳ điều hành trước — Tuổi Trẻ"
  - "So sánh khu vực: Campuchia & Thái Lan ~28.330-30.000đ/lít, Trung Quốc hơn 32.870đ/lít, Lào tới 48.210đ/lít — VnExpress"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Nguyên nhân giá dầu thế giới được viết ở mức khái quát ('đà biến động thị trường năng lượng
  thế giới', theo đúng cách VnExpress đóng khung) — KHÔNG nêu chi tiết xung đột vũ trang cụ thể dù bài
  gốc Tuổi Trẻ/VnExpress có nhắc căng thẳng Mỹ-Iran, để giữ trọng tâm video 100% ở chủ đề giá xăng dầu
  trong nước (A2) và tránh chạm nhóm A1 'xung đột vũ trang/đối ngoại'. Verify 4 bước: (1) ffprobe
  duration 58.47s khớp thiết kế 58.44s; (2) silencedetect noise=-35dB/d=0.6 — không phát hiện khoảng
  lặng chết; (3) 9 frame trích xuất khớp thiết kế, không phần tử bịa, cân bằng dọc đạt (nội dung kết
  thúc trong khoảng top 1400-1680px mọi frame, đã sửa 2 lỗi bố cục ở act Impact và CTA trước khi
  render cuối); (4) transcript (Gemini gemini-flash-latest, do Whisper host có thể bị chặn ở sandbox)
  khớp SCRIPT.md, không câu nào 'chế thêm'. LẦN CHẠY TEST — KHÔNG đăng Facebook/YouTube (bước 14-16 bị bỏ qua có chủ đích theo yêu cầu)."
```
