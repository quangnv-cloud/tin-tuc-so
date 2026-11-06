# COMPLIANCE — mien-trung-mua-lon-8-11
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-06T20:45:00+07:00
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN  (A2 — thời tiết/cảnh báo cộng đồng, đưa mức thông tin + khuyến cáo, dẫn cơ quan chức năng, không khai thác thương vong)
trending_signal: "thời tiết / vị trí 43 trong list trend (204 mục) / 50000+; 'ban chỉ đạo phòng thủ dân sự quốc gia' vị trí 118 / 50000+; cùng chủ đề có ở category=news (VnExpress, Tuổi Trẻ)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (giữ nguyên dấu nguồn, có dẫn nguồn 'Ảnh: VnExpress'), là ảnh ngập lụt minh hoạ của bài; giọng AI narrator Vbee (chung, không giả người thật); nhạc nền Lyria tự sinh (không lời); SFX trong repo"
claims_verified:
  - "mưa lớn diện rộng đêm 8–11/11, nam Nghệ An–Đà Nẵng và đông Quảng Ngãi–Đắk Lắk, có nơi >700 mm — VnExpress (?article=52223b9d580a), đối chiếu Tuổi Trẻ (?article=48e07d98e89a)"
  - "GĐ1 đêm 8–đêm 9/11 nam Nghệ An–bắc Quảng Trị 100–200 mm, cục bộ >300; GĐ2 9–đêm 11/11 Huế, Đà Nẵng, đông Quảng Ngãi 250–450, cục bộ >700; nam Quảng Trị, đông Gia Lai–Đắk Lắk 150–300, nơi >400 — VnExpress + Tuổi Trẻ"
  - "cảnh báo >100 mm/3 giờ, ngập úng, lũ quét, sạt lở; Ban Chỉ đạo Phòng thủ dân sự quốc gia yêu cầu theo dõi bản tin, rà soát sơ tán, điều tiết hồ chứa — VnExpress"
  - "nguyên nhân: không khí lạnh mạnh nhất từ đầu mùa đông 2026-2027, nhiễu động gió đông trên cao — Tuổi Trẻ"
sensitive_flags: ["thiên tai/thời tiết — framing trung lập, dẫn nguồn cơ quan khí tượng; đây là dự báo, không chốt như sự đã xảy ra; nên theo dõi bản tin chính thức"]
vietnam_legal_flags: []
notes: "B7: góc riêng = tách 2 giai đoạn + bảng xếp hạng lượng mưa cục bộ theo 3 vùng. Act 6 là cảnh báo/chỉ đạo đã ban hành. Vbee: tài khoản GỐC. Verify: 1080x1920/30fps, 63,9s, không khoảng lặng, loudnorm 2-pass -14,5 LUFS / TP -1,3 dBTP, phiên âm khớp SCRIPT (dùng ElevenLabs STT vì Gemini timeout). BGM nguồn: Lyria. Ảnh hero là ảnh ngập lụt minh hoạ của VnExpress, không phải hiện trường của đợt mưa sắp tới."
