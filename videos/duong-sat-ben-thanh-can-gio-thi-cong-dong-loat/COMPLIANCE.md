# COMPLIANCE — duong-sat-ben-thanh-can-gio-thi-cong-dong-loat
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-30T13:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "đường sắt cao tốc — Google Trends VN, vị trí 26 trong list, 2000+; có báo chính thống ở category=news (VnExpress, Tuổi Trẻ, Dân Trí). Id đánh dấu used: ce44145976d7 (Tuổi Trẻ); nguồn chính dùng: VnExpress 9aad701f74cf"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (bãi đúc dầm), có dẫn nguồn 'Nguồn: VnExpress' trong video; đã loại ảnh Dân Trí vì có watermark; nhạc nền Google Lyria tự sinh, không lời (không dùng fallback ElevenLabs Music); SFX từ repo; giọng đọc AI narrator chung (Vbee Minh Quân), không giả giọng người thật"
claims_verified:
  - "30/10/2026 VinSpeed + liên danh tổng thầu phát lệnh thi công đồng loạt — VnExpress, Tuổi Trẻ, Dân Trí"
  - "Tuyến ~54 km, qua 9 xã/phường, đường đôi, điện khí hoá, tối đa 350 km/h — VnExpress"
  - "Vốn ~102.430 tỷ đồng, chưa gồm gần 12.800 tỷ đồng giải phóng mặt bằng do ngân sách thành phố — VnExpress"
  - "Cao điểm 10.000 công nhân/kỹ sư — VnExpress, Tuổi Trẻ, Dân Trí"
  - "3 bãi đúc dầm; ~1.300 dầm hộp trong ~15 tháng; 1-2 nhịp/ngày/bãi — VnExpress, Dân Trí; phiến dầm đầu tiên 750 tấn — Dân Trí"
  - "Ga Bến Thành ~566 m, hố móng sâu 34 m; hầm hơn 2 km tại cảng Sài Gòn, máy đào hầm đường kính 13 m — VnExpress"
  - "Động thổ 12/2025; hoàn thành thi công quý IV/2028; vận hành 2029 (theo kế hoạch VinSpeed công bố) — VnExpress"
  - "1 trong 8 tuyến đường sắt đô thị, mục tiêu 255 km metro vào 2030 — Tuổi Trẻ"
  - "Phép tính hiển thị 3 bãi x 1-2 nhịp = 3-6 nhịp/ngày là số học thuần từ số liệu trên"
sensitive_flags: ["dự án hạ tầng do tư nhân đầu tư — chỉ nêu số liệu/kế hoạch công bố, không bình luận chính trị; không nêu tên lãnh đạo"]
vietnam_legal_flags: []
notes: "Voice Vbee tài khoản GỐC (biến VBEE_*_TAM không có trong môi trường; tài khoản gốc hoạt động bình thường, không lỗi 1051). BGM Lyria (cần cài google-genai cho python 3.11). Transcript ElevenLabs STT khớp SCRIPT, lệch nhẹ ở phiên âm 'Sáng'/'Phiến'/tên VinSpeed. Sơ đồ tuyến là minh hoạ đồ hoạ ý niệm, có chú thích không theo tỷ lệ, không phải bản đồ thật. Loudnorm 2-pass: -14.6 LUFS, TP -1.3 dBTP. Render 1080x1920/30fps, 70.2s. Góc riêng: sơ đồ hành trình các điểm thi công + bài toán 1.300 dầm/15 tháng quy ra 3-6 nhịp/ngày. Đẩy lên nhánh claude/kind-tesla-bftbc3 theo chỉ định phiên."
