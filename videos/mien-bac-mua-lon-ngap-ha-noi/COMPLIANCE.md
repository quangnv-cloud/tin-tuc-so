# COMPLIANCE — mien-bac-mua-lon-ngap-ha-noi
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-15T06:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "vùng áp thấp — Google Trends VN, trafficApprox 100000+, id ceaca093eb53, pubDate 2026-09-14T10:50:00.000Z (từ khoá liên quan 'áp thấp nhiệt đới mới nhất', id 04f4f7c38d61, cùng trafficApprox 100000+)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero (assets/img/article-hero.jpg) là ảnh báo chí thật lấy qua ?image=2007f5267935 (VnExpress Thời sự, 'Miền Bắc và Trung mưa lớn đến ngày 16/9'), gốc webp 1200x720 convert sang jpg không chỉnh sửa nội dung, ghi nguồn trong Brand Anchor + Hook badge + CAPTION. Nhạc nền sinh qua Google Lyria (lyria-recipe.py, calm ambient, negative-prompt loại vocal), đã xác minh bằng Gemini multimodal (gemini-flash-latest) là 100% không lời trước khi dùng. SFX từ bộ có sẵn trong repo (videos/_reference-astra-openai/assets/sfx, không đổi tốc độ/pitch). Giọng đọc ElevenLabs 'Khánh Lâm' (RCmOaM1iiIH5xX3QXjIF, eleven_v3) — AI narrator chung, không giả giọng người thật cụ thể."
claims_verified:
  - "Mưa lớn diện rộng Bắc Bộ/Bắc Trung Bộ do hậu áp thấp nhiệt đới kết hợp không khí lạnh, dự báo duy trì đến 16/9, có thể chấm dứt 19/9 — VnExpress (2007f5267935)"
  - "Miền Trung (Hà Tĩnh–Quảng Ngãi) mưa 150-400mm, Quảng Trị/Huế 400-600mm; điểm cực đoan Tà Long (Quảng Trị) 844mm, Đỉnh Bạch Mã (Huế) 1.309mm — VnExpress"
  - "Nội thành Hà Nội (số liệu Công ty TNHH MTV Thoát nước Hà Nội, 22h 14/9-6h 15/9): Yên Sở 270,4mm (cao nhất), Hai Bà Trưng 219,2mm, Triều Khúc - Thanh Liệt 175,5mm — Tuổi Trẻ (3ceea23a7b90)"
  - "Các tuyến ngập/ùn tắc Hà Nội: Đàm Quang Trung, Cổ Linh, Vĩnh Hưng, QL6 đoạn Yên Nghĩa, Đại lộ Thăng Long hầm 4/5/6/9+6; cầu Vĩnh Tuy ùn tắc — Tuổi Trẻ"
  - "Mực nước sông: Bôi (Phú Thọ) 12,47m dưới BĐ3 0,53m; Âm (Thanh Hoá) 48,76m trên BĐ1 0,26m; Chu (Cửa Đạt) 28,13m trên BĐ1 0,13m; dự báo 15-16/9 sông Bôi có thể vượt BĐ3, sông Hoàng Long lên BĐ2-3 — VnExpress"
  - "Thiệt hại tính đến 6h 15/9: sập 1 nhà, hư hỏng 10 nhà, ngập 591 nhà tại Quảng Trị (nước đã rút); 712 hộ sơ tán đã về nhà an toàn; hơn 1.000ha lúa/hoa màu hư hại (Quảng Trị 353ha, Đà Nẵng 581ha, Quảng Ngãi 63ha, Thanh Hoá 3ha); 6 tuyến quốc lộ/tỉnh lộ ngập; 44 điểm sạt lở — VnExpress"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin thời tiết/thiên tai diện rộng (A2), framing trung lập bằng số liệu khí tượng-thuỷ văn-hạ tầng, có tín hiệu tích cực có thật (712 hộ đã về nhà an toàn), KHÔNG nêu tên/khai thác nạn nhân cá nhân, KHÔNG số liệu thương vong (không có trong 2 nguồn chính dùng). Đối chiếu 2 nguồn độc lập (VnExpress + Tuổi Trẻ) cho các claim số liệu chính. Góc nhìn riêng (B7): tổng hợp 3 lớp dữ liệu (mưa theo phường nội thành Hà Nội + mưa cực đoan miền Trung + mực nước sông so báo động) thành 1 bức tranh đầy đủ hơn từng bài báo đơn lẻ, đặt câu hỏi tranh luận thực tế 'thời tiết cực đoan hay hạ tầng thoát nước' — không chỉ đọc lại tiêu đề báo. Style dựng 1-card-and-bar (index 0, claim_style) khác hẳn style 4-split-comparison của video liền trước (iphone-18-pro-thay-doi-so-voi-17-pro).
Vertical-balance QC: trích 7 frame bằng ffmpeg gần cuối mỗi act (t=6.9/14.8/26.3/37.1/47.4/57.7/65.5s) từ file .mp4 đã render, xem bằng Read — Hook/What/Facts/Data/Context đều có phần tử cuối rơi trong dải ước lượng ~1400-1500px (không trống đen nửa dưới). Act Impact vòng 1 phát hiện khoảng trống lớn giữa 2 card và dòng chú thích rời (kết thúc nội dung sớm, tạo mảng đen giữa khung) — đã sửa: gộp thành 3 card đồng nhất (591 nhà / 712 hộ / hơn 1.000ha hoa màu) thay vì 2 card + caption rời, render lại, xác nhận khung lấp đều tới ~1425px, không còn khoảng trống bất thường.
Verify 4 bước (mục 7 PRODUCTION-WORKFLOW.md): (1) ffprobe duration 66.87s khớp thiết kế 66.84s; (2) silencedetect chỉ phát hiện khoảng lặng ở đuôi video (65.88s-hết, đúng fade-out BGM sau khi voice CTA + pulse animation kết thúc), không có khoảng lặng chết giữa video; (3) trích 7 frame ở các mốc cuối mỗi act, xem bằng Read — đúng thiết kế, không phần tử bịa, không lộ tĩnh; (4) transcript qua Gemini (gemini-flash-lite-latest, gemini-flash-latest bị giới hạn quota tạm thời) khớp SCRIPT.md, không câu nào bịa thêm, không đọc tên kênh trong lời thoại. BGM đã xác minh 100% không lời qua Gemini multimodal trước khi dùng."
