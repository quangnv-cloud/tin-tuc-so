# COMPLIANCE — ho-chua-quang-ngai-can-nuoc-el-nino
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-07T20:50:00+07:00
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN  (A2 — thiên tai/thời tiết/cảnh báo cộng đồng + tài nguyên nước, đưa mức thông tin, dẫn nguồn báo chính thống, không khai thác thương vong)
trending_signal: "sạt lở / vị trí 43 trong list trend (220 mục) / 1000+; 'bão áp thấp nhiệt đới' vị trí 48 / 1000+ — cùng chủ đề thời tiết miền Trung; tin cụ thể chọn từ category=news (Tuổi Trẻ, id 8b39188b576e) vì góc hồ chứa không có từ khoá trend riêng"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Tuổi Trẻ (hồ chứa), có dẫn nguồn 'Ảnh: Tuổi Trẻ'; nhạc nền Google Lyria tự sinh (không lời); giọng AI narrator chung Vbee 'HN - Minh Quân' (tài khoản GỐC); SFX trong repo"
claims_verified:
  - "24 hồ chứa thủy lợi Quảng Ngãi tích 25–57% dung tích thiết kế — Tuổi Trẻ 7/11 (?article=8b39188b576e)"
  - "Liệt Sơn hơn 25%, An Thọ 34%, Núi Ngang gần 35% — Dân Trí (?article=451a8cf16cc3)"
  - "Đắk Đrinh dừng phát điện từ 1/11; Nước Trong, Núi Ngang từ 3/11, dự kiến phát điện lại 5/12; mục tiêu Đắk Đrinh cao trình 410 m cuối tháng 12 — Dân Trí (451a8cf16cc3)"
  - "Mưa 9–11/11 có nơi tới 500 mm, ven biển/đồng bằng 300–500 mm; công văn 7/11 của UBND tỉnh; cảnh báo ngập lụt, lũ quét, sạt lở — Tuổi Trẻ (8b39188b576e)"
  - "El Nino 2026 rất mạnh (tương đương hoặc cao hơn 2015–2016, 2019–2020); sông Vu Gia 12 tháng qua thấp hơn 66%; dự báo 10/2026–9/2027 thấp hơn 60–75% — Dân Trí (?article=525edc343245), dẫn Cục KTTV / Đài KTTV Trung bộ"
sensitive_flags: ["thiên tai/cảnh báo cộng đồng — chỉ thông tin + cần theo dõi bản tin chính thức, không khai thác thương vong"]
vietnam_legal_flags: []
notes: |
  - B7: cùng ngày-liền-trước kênh đã đăng 'mien-trung-mua-lon-8-11' (lượng mưa dự báo). Video này đi góc khác (hồ chứa thiếu nước do El Nino, mức tích nước từng hồ, thủy điện dừng phát điện, đối trọng tích nước vs an toàn hạ du), dữ liệu riêng, style khác (3-ticker-tape vs 1-chip-and-leaderboard).
  - Số liệu 'hồ Nước Trong 58%' (Dân Trí) lệch nhẹ so với dải 25–57% (Tuổi Trẻ) → video chỉ dùng dải của Tuổi Trẻ và 3 hồ cụ thể của Dân Trí.
  - Phiên âm ngược nghe 'Liệt Sơn' thành 'Liên Sơn' (2 lần, 2 biến thể câu) — nghi nhiễu của công cụ STT, hiển thị chữ trên hình là 'Liệt Sơn' đúng nguồn; không sửa được thêm bằng TTS.
  - Id ?article=abde3060b39f (Dân Trí, miền Trung mưa 8/11) đã POST đánh dấu 'used' nhầm lúc đầu rồi đổi sang chủ đề này (id 8b39188b576e) vì trùng chủ đề video hôm trước.
  - Render dùng wrapper pgrep cục bộ để tránh việc CLI hyperframes tự kill tiến trình hệ thống của sandbox; không ảnh hưởng chất lượng.
