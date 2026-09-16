# COMPLIANCE — u23-viet-nam-hoa-1-1-kuwait-o-asiad-2026

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-16T01:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "u-23 việt nam đấu với đội tuyển bóng đá u-23 quốc gia kuwait" (Google Trends VN, trafficApprox 10000+, id 263fc4864192) + "u23 việt nam" (trafficApprox 5000+, id a8ddf8f7cbba) — cả hai đều xuất hiện gần đỉnh danh sách `?category=trend` lúc chọn tin. Bài dựng dùng nguồn/ảnh từ item `category=news` cùng chủ đề (VnExpress Thể thao, id d3e2d4edfcba).
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài báo VnExpress Thể thao (HLV Đinh Hồng Vinh họp báo Aichi-Nagoya 2026), có dẫn nguồn, không chỉnh sửa nội dung; nhạc nền sinh bằng Google Lyria (lyria-recipe.py, không lời); SFX từ bộ SFX repo (_reference-astra-openai/assets/sfx); giọng đọc ElevenLabs 'Khánh Lâm' (AI narrator chung, không giả giọng người thật)."
claims_verified:
  - "Kết quả trận đấu: U23 Việt Nam 1-1 U23 Kuwait, bảng C bóng đá nam Asiad 20, sân CS Asset Minato (Nagoya, Nhật Bản), chiều 15/9/2026 — đối chiếu ?article=d3e2d4edfcba (VnExpress Thể thao)"
  - "Bàn thắng: phút 78 Omar Almatar (Kuwait); phút 80 Nguyễn Ngọc Mỹ gỡ hòa (Việt Nam) — đối chiếu ?article=d3e2d4edfcba"
  - "Thống kê: kiểm soát bóng 63%-37%; dứt điểm 27 (trúng 6) - 10 (trúng 5); phạt góc 8-4; 4 lần bóng dội cột dọc/xà ngang — đối chiếu ?article=d3e2d4edfcba"
  - "Phát biểu HLV Đinh Hồng Vinh 'Thật tiếc vì không thắng được Kuwait, dù chúng tôi có rất nhiều cơ hội' — trích nguyên văn ?article=d3e2d4edfcba"
  - "Bảng C sau lượt 1: Việt Nam và Kuwait cùng 1 điểm, xếp sau Uzbekistan (thắng Philippines 5-1); lượt 2 ngày 18/9 Việt Nam gặp Philippines; lần gần nhất (bán kết SEA Games 33) Việt Nam thắng Philippines 2-0 — đối chiếu ?article=d3e2d4edfcba"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề A2 (kết quả thể thao có yếu tố VN — đội tuyển U23 Việt Nam tại đại hội thể thao châu Á), không đụng đời tư/hình sự/chính trị. Góc nhìn riêng (B7): phân tích nghịch lý 'áp đảo 27 cú dứt điểm nhưng chỉ hòa', không chỉ đọc lại tiêu đề báo. Style dựng 4-split-comparison (index 3, claim_style) — khác style video liền trước (1-card-and-bar, mien-bac-mua-lon-ngap-ha-noi). Verify 4 bước: (1) ffprobe duration 69.47s khớp thiết kế 69.44s; (2) silencedetect chỉ có khoảng lặng hợp lý ở đoạn kết (68.76-69.48s, sau khi voice+nhạc đã fade out), không có khoảng lặng chết giữa video; (3) trích 8 frame gần cuối mỗi act, đo pixel định lượng (PIL) xác nhận nội dung kết thúc trong dải an toàn 1400-1699px (78-88% chiều cao khung) ở mọi act, xem bằng mắt xác nhận không lỗi hiển thị/tràn chữ, dấu tiếng Việt hiển thị đúng; (4) transcript (Gemini multimodal, model gemini-flash-latest bị quota free-tier chặn → dùng gemini-flash-lite-latest) khớp SCRIPT.md từng câu, không có câu 'chế thêm', chỉ lệch nhẹ phiên âm tên riêng nước ngoài ('Omar Almatar' → nghe thành 'Oma Al-Mata', lỗi STT chấp nhận được theo ROUTINE.md, không phải lỗi giọng đọc)."
