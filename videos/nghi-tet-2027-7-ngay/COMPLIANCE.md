# COMPLIANCE — nghi-tet-2027-7-ngay

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-03T13:55:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "tết nguyên đán — #8 trong list category=trend, trafficApprox 200+; có cả ở category=news (VnExpress id 49074ba45bf3, Tuổi Trẻ id 50de5d996e79, Dân Trí id 4f25b19eed6b / 4c23b1659ca1)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (đồ hoạ lịch tháng 2/2027), có dẫn nguồn trong card + badge, không chỉnh sửa/cắt watermark; nhạc nền Google Lyria tự sinh (instrumental) — KHÔNG dùng ElevenLabs Music fallback; giọng đọc Vbee 'HN - Minh Quân' (narrator chung); SFX bộ repo; logo + font Montserrat là tài sản kênh."
claims_verified:
  - "Ngày 2/10/2026 Văn phòng Chính phủ: Phó thủ tướng Phạm Thị Thanh Trà đồng ý phương án nghỉ lễ, Tết 2026–2027 do Bộ Nội vụ trình — ?article=49074ba45bf3 (VnExpress), khớp Tuổi Trẻ + Dân Trí."
  - "Tết Đinh Mùi nghỉ 28 tháng chạp → hết mùng 5 tháng giêng (4/2–10/2/2027), đi làm lại mùng 6 (11/2/2027) — VnExpress, Tuổi Trẻ."
  - "7 ngày = 5 ngày nghỉ theo quy định (2 trước Tết + 3 sau Tết) + 2 ngày cuối tuần — Tuổi Trẻ (?article=50de5d996e79)."
  - "Doanh nghiệp: người sử dụng lao động quyết định, không thấp hơn luật định; 3 phương án 1+4 (5/2–11/2), 2+3 (4/2–10/2), 3+2 (3/2–9/2/2027) — VnExpress."
  - "Quốc khánh 2027: nghỉ thêm 3/9, cộng cuối tuần = 4 ngày, 2/9–5/9/2027 — VnExpress, Tuổi Trẻ."
  - "2027 có 6 kỳ nghỉ chính thức, 22 ngày nghỉ tính cả cuối tuần liền kề — Dân Trí (?article=4c23b1659ca1)."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chính sách mới đã ban hành (A2), nêu nội dung quy định, không bình luận chính trị. Ảnh infographic gốc có chú thích 'nghỉ bù' cho mùng 4–5; video không diễn giải thêm cách bù ngày ngoài số liệu bài báo. ElevenLabs STT/Music hết quota (401) → mốc từ caption lấy bằng whisper cục bộ + phân bổ theo âm tiết; BGM dùng Lyria nên không ảnh hưởng. Voice kiểm bằng Gemini (gemini-flash-latest) khớp SCRIPT; dòng 3 phiên âm 'ngày mùng 10' có thể là sai số nhận dạng của bên phiên âm."
```

## Chi tiết
- GATE A: từ khoá khác đã loại: xổ số/Vietlott (cờ bạc), thể thao nước ngoài (Thái Lan–Philippines, Hàn Quốc–Venezuela, Nations League…), đời tư/drama (Đặng Lê Nguyên Vũ, Nana, Ronaldo), hình sự (Trương Mỹ Lan, vụ án), nhân sự quân đội cấp cao (Hồ Quang Tuấn — chính trị/nhân sự), Việt Nam–Pakistan (đã làm video riêng hôm 2/10).
- GATE B: B1 mọi số liệu truy được về VnExpress/Tuổi Trẻ/Dân Trí; B2–B3 không vi phạm, CTA là câu hỏi quan điểm thật; B4 ảnh thật có dẫn nguồn, không AI; B5 hợp lệ; B6 tiêu đề = sự kiện/số liệu; B7 góc riêng (tách 7 ngày = 5 + 2, 3 phương án doanh nghiệp, đặt Tết cạnh Quốc khánh trong 22 ngày); B8 không flag.
- GATE C: đã xem thumbnail + frame 8 mốc; transcript khớp SCRIPT.
- Kỹ thuật: 1080×1920, 30fps, 53.2s, h264 + AAC 192k; loudnorm 2-pass: -14.5 LUFS, True Peak -1.1 dBTP; silencedetect 0 khoảng lặng chết; style 6-ring-progress (claim_style index 5).

**decision: APPROVE**
