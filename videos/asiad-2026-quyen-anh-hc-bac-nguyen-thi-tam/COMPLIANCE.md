# COMPLIANCE — asiad-2026-quyen-anh-hc-bac-nguyen-thi-tam

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-02T06:55:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "nguyễn thị tâm — #3 trong list, trafficApprox 500+; 'huy chương' — #4, 10000+ (Google Trends VN); có cả ở category=news (VnExpress Thể thao, id 16168a1f879f)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài báo VnExpress Thể thao (assets/img/article-hero.jpg, id 16168a1f879f), có dẫn nguồn trong card + badge, không chỉnh sửa nội dung; nhạc nền Google Lyria tự sinh (instrumental, negative-prompt loại vocal) — KHÔNG dùng ElevenLabs Music fallback; giọng đọc Vbee 'HN - Minh Quân' (narrator chung); SFX bộ repo; logo + font Montserrat là tài sản kênh."
claims_verified:
  - "Sáng 2/10/2026, Nguyễn Thị Tâm thua Wu Yu 0-5 ở chung kết hạng 51 kg nữ ASIAD, nhà thi đấu Nishio, Aichi → HC bạc, thành tích tốt nhất lịch sử quyền Anh VN tại ASIAD — ?article=16168a1f879f (VnExpress), khớp related VietNamNet/Tuổi Trẻ/Znews."
  - "Wu Yu: số 1 thế giới hạng 51 kg, HCV Olympic Paris 2024 (hạng 50 kg), vô địch châu Á 2026 và World Boxing Cup — VnExpress."
  - "Đường vào chung kết: 5-0 Nepal, 4-1 Đài Loan, 5-0 Hàn Quốc (tứ kết), 5-0 Alua Balkibekova (Kazakhstan, ĐKVĐ thế giới, bán kết) — VnExpress."
  - "Tâm là võ sĩ VN đầu tiên (nam lẫn nữ) vào chung kết quyền Anh một kỳ ASIAD; 32 tuổi, quê Thái Bình — VnExpress."
  - "HC đồng Jakarta 2018; HC bạc thế giới 2023; đứt dây chằng chéo trước gối trái ở SEA Games 32 (2023), gần 2 năm điều trị; vô địch quốc gia 2025 — VnExpress."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tường thuật kết quả thể thao có yếu tố VN (A2). Không đời tư/hình sự/chính trị. Số trọng tài chấm trong bảng Data = suy từ tỷ số 5-0/4-1/0-5 của bài gốc. ElevenLabs STT hết quota → dùng whisper cục bộ (hyperframes transcribe) để lấy mốc từ cho caption và kiểm tra giọng đọc."
```

## Chi tiết
- GATE A: chủ đề thể thao có VĐV Việt Nam tại ASIAD, trending + có báo chính thống → GREEN. Các từ khoá khác đã loại: drama/hình sự ("vụ án", "đảng việt tân", "trương mỹ lan"), thể thao nước ngoài ("Bruno Fernandes", "Haaland", "Denmark vs Portugal", "Nhật Bản đấu Ecuador"), xổ số, chính trị.
- GATE B: B1 mọi số liệu truy được về bài VnExpress; B2–B3 không vi phạm, CTA là câu hỏi quan điểm thật; B4 ảnh thật có dẫn nguồn, đồ hoạ là ý niệm; B5 ảnh/nhạc/SFX hợp lệ; B6 tiêu đề = sự kiện, không giật gân; B7 góc nhìn riêng (bảng số trọng tài từng trận, 3 mốc hành trình trở lại); B8 không flag.
- GATE C: đã xem thumbnail + frame của cả 7 act; không phần tử bịa. Transcript từng dòng voice (whisper small, vi) khớp SCRIPT, chỉ lệch do nhận dạng. Caption đăng = CAPTION.md.
- Kỹ thuật: 1080×1920, 30fps, 59.5s, h264 + AAC 192k; loudnorm 2-pass: -14.5 LUFS, True Peak -1.0 dBTP; silencedetect 0 khoảng lặng chết.

**decision: APPROVE**
