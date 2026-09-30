# COMPLIANCE — lai-suat-lien-ngan-hang-giam-manh-tiet-kiem-van-cao
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-14T00:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "lãi suất ngân hàng — Google Trends VN, id 97393d8d4f95, trafficApprox 100+, pubDate 2026-09-12T19:50Z; corroborated bởi 2 bài category=news cùng chủ đề trong ngày (Dân Trí, Tuổi Trẻ). Chọn id c981b8d9ee14 (Dân Trí) làm nguồn chính cho ?article=/?image= vì ảnh của item trend gốc chỉ là thumbnail Google 259×194 (không đạt chuẩn brand), trong khi item news có ảnh báo chí thật 5000×3333."
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh hero (assets/img/article-hero.jpg) là ảnh báo chí thật lấy qua ?image=c981b8d9ee14 (Dân Trí, minh hoạ giao dịch ngân hàng), ghi nguồn trong Brand Anchor + Hook badge + CAPTION; không chỉnh sửa nội dung ảnh. Nhạc nền sinh qua Google Lyria (lyria-recipe.py, calm ambient, --density 0.25 --brightness 0.4, --negative-prompt loại vocal), đã xác minh bằng Gemini multimodal (gemini-flash-latest) là 100% không lời trước khi dùng. SFX từ bộ có sẵn trong repo (videos/_reference-astra-openai/assets/sfx, không đổi tốc độ/pitch). Giọng đọc ElevenLabs 'Khánh Lâm' (RCmOaM1iiIH5xX3QXjIF, eleven_v3) — AI narrator chung, không giả giọng người thật cụ thể. Icon trong composition là CSS shapes tự vẽ (không dùng ảnh/emoji)."
claims_verified:
  - "Lãi suất liên ngân hàng kỳ hạn qua đêm giảm còn 1,5%/năm (giảm 3,1 điểm % so với 4/9), giảm liên tục 4,6% → 3,5% → 2,5% → 1,5% từ 4/9 đến 9/9, duy trì tới hết tuần 7-11/9 — Dân Trí (c981b8d9ee14), theo số liệu Vira (Hội Nghiên cứu thị trường liên ngân hàng Việt Nam)"
  - "Kỳ hạn 1 tuần giảm 2,15 điểm % còn 3%/năm; kỳ hạn 2 tuần giảm 2,7 điểm % còn 3,8%/năm; kỳ hạn 1 tháng giảm 0,8 điểm % còn 5,5%/năm — Dân Trí (c981b8d9ee14)"
  - "Ngân hàng Nhà nước chào thầu 11.000 tỷ đồng qua kênh cầm cố (lãi suất 4,5%/năm), hơn 6.005 tỷ đồng trúng thầu, hơn 8.583 tỷ đồng đáo hạn → hút ròng gần 2.600 tỷ đồng khỏi hệ thống — Dân Trí (c981b8d9ee14)"
  - "Lãi suất huy động nhóm quốc doanh: 4,75%/năm (3 tháng), 6,6%/năm (6-9 tháng), 6,8%/năm (12 tháng) — Dân Trí (c981b8d9ee14)"
  - "Nhóm cổ phần niêm yết: ACB dẫn đầu 7,6-7,8%/năm (6-12 tháng); Sacombank, LPBank, Bac A Bank, SaigonBank, MBV cũng niêm yết từ 7%/năm — Dân Trí (c981b8d9ee14)"
  - "Mức thực nhận thoả thuận (không phải niêm yết công khai) tại LPBank, SHB, HDBank, MSB, MB, MBV, Vikki: 8,5-9,2%/năm kỳ hạn 6-12 tháng — Dân Trí (c981b8d9ee14)"
  - "MBV: gửi từ 10 tỷ đồng kỳ hạn 13 tháng lãi suất 9,46%/năm (kỳ hạn 12 tháng: 9,4%/năm) — xác nhận chéo ở Dân Trí (c981b8d9ee14, 6677fc7221d0) và Tuổi Trẻ (c6ac5c8a4fb7)"
  - "Vikki Bank đã chạm 9,4%/năm (từ cuối tháng 7 là 9,2%/năm) — Dân Trí (6677fc7221d0), Tuổi Trẻ (c6ac5c8a4fb7)"
  - "Cake by VPBank niêm yết 7,2-7,4%/năm, cộng thêm 2 điểm % ưu đãi tháng 9 cho khách gửi tiết kiệm lần đầu (từ 100.000 đồng) → tối đa 9,4%/năm kỳ hạn 12 tháng — Dân Trí (6677fc7221d0)"
  - "NCB triển khai chương trình NCB Signature Savings, tổng giá trị giải thưởng tới 65 tỷ đồng (gửi từ 2 tỷ đồng, kỳ hạn ≥6 tháng, đến hết 25/9), giải thưởng hằng tuần là căn hộ cao cấp 3 phòng ngủ (Blanca City TPHCM / Charmora City Khánh Hoà) — Tuổi Trẻ (c6ac5c8a4fb7)"
sensitive_flags: ["Tin tài chính — thuần số liệu lãi suất công khai từ báo chí, KHÔNG khuyến nghị đầu tư / gửi tiền ở ngân hàng cụ thể nào, không phải quảng cáo"]
vietnam_legal_flags: []
notes: "Tin kinh tế trung lập (A2), số liệu thị trường tiền tệ do đơn vị nghiên cứu độc lập (Vira) công bố qua báo chí chính thống. Góc nhìn riêng (B7): tổng hợp + đối chiếu 3 bài báo (2 Dân Trí + 1 Tuổi Trẻ) thành 1 nghịch lý duy nhất (liên ngân hàng rẻ ↔ tiết kiệm dân cư đắt) + tự dựng bảng so sánh 3 nhóm ngân hàng (không có sẵn nguyên bản trong 1 bài báo nào) — không chỉ đọc lại tiêu đề báo. Style dựng 8-icon-grid (index 7, claim_style), khác với style video liền trước (4-split-comparison) — thoả B7 chống trùng bố cục. Vertical-balance QC: xem thumbnail Studio + frame render tại nhiều mốc mỗi act (giữa và cuối khung); phát hiện 1 lỗi tràn chữ (số '9,46%' tràn viền thẻ ở Data moment) và đã sửa (giảm cỡ chữ 126px→100px, mở rộng thẻ giữa 440px→460px) trước khi render — xác nhận lại bằng frame thật sau render, không còn tràn viền. Không có mảng đen bất thường ở nửa dưới khung tại trạng thái ổn định (cuối) của mỗi act. Verify 4 bước (mục 7 PRODUCTION-WORKFLOW.md): (1) ffprobe duration 64.47s khớp thiết kế 64.45s; (2) silencedetect chỉ phát hiện khoảng lặng ở đuôi video (63.75s→hết, đúng fade-out BGM 2.5s sau khi voice line 7 kết thúc), không có khoảng lặng chết giữa video; (3) trích 7 frame ở các mốc quan trọng từ file render thật, xem bằng Read — đúng thiết kế, không phần tử bịa/lộ tĩnh, khớp ảnh preview Studio; (4) transcript qua Gemini (gemini-flash-latest, Whisper host bị chặn ở sandbox) khớp 100% với SCRIPT.md, không có câu bịa thêm, không đọc tên kênh."
