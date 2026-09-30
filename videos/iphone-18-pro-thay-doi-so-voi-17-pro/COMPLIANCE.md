# COMPLIANCE — iphone-18-pro-thay-doi-so-voi-17-pro
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-13T01:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "18 pro max — Google Trends VN, trafficApprox 2000+, id 7232c7c92fa3, pubDate 2026-09-12T18:50:00Z"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero (assets/img/article-hero.jpg) là ảnh báo chí thật lấy qua ?image=f37036fa2745 (VnExpress Khoa học, 'iPhone 18 Pro Max cháy hàng đợt đầu tại Việt Nam sau 10 phút'), ghi nguồn trong Brand Anchor + Hook badge + CAPTION; không chỉnh sửa nội dung ảnh. Nhạc nền sinh qua Google Lyria (lyria-recipe.py, calm ambient, negative-prompt loại vocal), đã xác minh bằng Gemini multimodal là 100% không lời trước khi dùng. SFX từ bộ có sẵn trong repo (videos/_reference-astra-openai/assets/sfx, không đổi tốc độ/pitch). Giọng đọc ElevenLabs 'Khánh Lâm' (RCmOaM1iiIH5xX3QXjIF, eleven_v3) — AI narrator chung, không giả giọng người thật cụ thể."
claims_verified:
  - "Apple mở cổng đặt trước iPhone 18 Pro/18 Pro Max tại VN từ 19h 12/9/2026 — VnExpress (f37036fa2745), Dân Trí (69343d2db87b)"
  - "iPhone 18 Pro Max màu Đỏ Burgundy cháy hàng đợt đầu ~10 phút sau mở bán, giao hàng lùi sang 2-3 tuần — VnExpress, Dân Trí"
  - "CellphoneS: hơn 10.000 đơn đặt cọc/15 phút, +40% so với năm ngoái — VnExpress"
  - "Hoàng Hà Mobile: hơn 9.000 đơn/10 phút, dự kiến 18.000 đơn/24h — VnExpress"
  - "Viettel Store: gần 60.000 lượt quan tâm sau 2 ngày; màu Đỏ Burgundy ~70% nhu cầu bản Pro Max — VnExpress, Dân Trí"
  - "Giá VN: iPhone 18 Pro từ 38,99 triệu đồng (256GB), +4 triệu so với giá niêm yết ra mắt của 17 Pro; 18 Pro Max từ 41,99 triệu đồng — VnExpress"
  - "Dynamic Island nhỏ hơn 25%; camera lần đầu có khẩu độ biến thiên + cảm biến Fusion 48MP; chip A20 Pro (2nm); modem C2 hỗ trợ AI, -15% năng lượng — VnExpress, xác nhận chéo Dân Trí (Dynamic Island + khẩu độ biến thiên)"
  - "4 màu, 3 màu mới bên cạnh màu bạc quen thuộc — VnExpress (f37036fa2745 liệt kê đủ 4 màu; 7c73af0cf4d3 xác nhận '3 màu mới bên cạnh màu bạc')"
  - "Apple khai tử iPhone 17 Pro, 17 Pro Max, 16 Plus ngay sau ra mắt bộ đôi mới — VnExpress (trích trực tiếp trong bài nguồn)"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin ra mắt sản phẩm công nghệ tiêu dùng (A2), framing trung lập, không khuyến nghị mua hàng, không đầu cơ. Góc nhìn riêng: tổng hợp số liệu đặt hàng của 3 đại lý khác nhau + so sánh kỹ thuật 2 cột 17 Pro/18 Pro + câu hỏi tranh luận về động cơ cháy hàng, không chỉ đọc lại tiêu đề báo — thoả B7. Vertical-balance QC: đo bằng phân tích pixel (numpy, ngưỡng khác nền #0B0E14) cho cả 7 frame — hàng nội dung cuối cùng nằm trong khoảng top 1601-1697px (mục tiêu 1400-1680px), không có mảng đen nửa dưới khung. Verify 4 bước (mục 7 PRODUCTION-WORKFLOW.md): (1) ffprobe duration 57.40s khớp thiết kế 57.37s; (2) silencedetect chỉ phát hiện khoảng lặng ở đuôi video (55.84s→hết, đúng như fade-out BGM 2.5s sau khi voice line 7 kết thúc), không có khoảng lặng chết giữa video; (3) trích 8 frame ở các mốc quan trọng, xem bằng Read — đúng thiết kế, không phần tử bịa/lộ tĩnh; (4) transcript qua Gemini (gemini-flash-latest, model host Whisper openaipublic.azureedge.net bị chặn ở sandbox) khớp 100% với SCRIPT.md, không có câu bịa thêm, không đọc tên kênh."
