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
  trong nước (A2) và tránh chạm nhóm A1 'xung đột vũ trang/đối ngoại'.

  [Vòng review với người dùng sau bản render đầu] Người dùng phản hồi 2 lỗi trên bản render đầu
  (58.44s): (1) dấu thanh của tiêu đề Hook ('GIÁ XĂNG'/'DẦU TĂNG', Montserrat 900/140px) bị cắt phần
  trên do `line-height:1` quá chật bên trong wrapper `overflow:hidden` dùng cho hiệu ứng slide-up —
  sửa `line-height` lên 1.22 cho `.hk-name`, xác nhận lại bằng Studio thumbnail: dấu hiện đầy đủ,
  không cắt. (2) đoạn kết bị cụt gấp — pad sau voice line 7 chỉ 0.4s trước khi cắt cứng — tăng
  `data-duration` act CTA từ 6.93s lên 8.70s (thêm ~1.8s), tổng video từ 58.44s lên 60.21s; sinh lại
  BGM Lyria (preset/negative-prompt giữ nguyên) đủ độ dài mới, retrim + fade-out 2.5s cuối tại
  57.71-60.21s, chạy lại `carve.mjs --strength 0.4` sau khi đổi timing/audio theo đúng quy định.
  `npm run check` PASS lại sau cả 2 fix (0 lỗi lint/runtime/layout/motion, contrast 45/45 AA).
  Render lại bản cuối (60.23s) và verify lại đầy đủ 4 bước: (1) ffprobe duration 60.23s khớp thiết
  kế 60.21s; (2) silencedetect noise=-35dB/d=0.6 — không phát hiện khoảng lặng chết; (3) trích frame
  Hook (t=3.5s) xác nhận dấu không còn bị cắt, frame gần cuối (t=59.5s) xác nhận CTA giữ ổn định,
  không cắt gấp; (4) transcript (Gemini gemini-flash-latest) khớp SCRIPT.md, không câu nào 'chế
  thêm' — nội dung audio không đổi so với bản đầu, chỉ kéo dài phần giữ hình tĩnh cuối act CTA.
  Xuất lại thumbnail từ bản render cuối (t=3.5s, dấu hiển thị đầy đủ).

  LẦN CHẠY TEST — KHÔNG đăng Facebook/YouTube (bước 14-16 bị bỏ qua có chủ đích theo yêu cầu)."
```
