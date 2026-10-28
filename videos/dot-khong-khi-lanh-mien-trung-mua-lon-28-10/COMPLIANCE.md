# COMPLIANCE — dot-khong-khi-lanh-mien-trung-mua-lon-28-10
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-28T14:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "đợt lạnh — Google Trends VN, vị trí 70 trong list, 1000+ (item trend e88e08911a2a); đối chiếu thêm item category=news Dân trí 7812afe161cb"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân trí (người đi xe máy trong mưa), có dẫn nguồn trong video; nhạc nền Google Lyria tự sinh, không lời (không dùng fallback ElevenLabs Music); SFX từ repo; giọng đọc AI narrator chung (Vbee Minh Quân), không giả giọng người thật"
claims_verified:
  - "Mưa to đến rất to từ Hà Tĩnh đến Đà Nẵng, từ tối 27/10 đến hết 29/10, do không khí lạnh kết hợp nhiễu động gió Đông trên cao — Dân trí (dự báo viên Phạm Thị Phương Chi, Trung tâm Dự báo khí tượng thủy văn quốc gia); VietNamNet"
  - "Tối 27 → 28/10 phổ biến 40–70 mm, có nơi trên 100 mm trong 3 giờ; đêm 28 → 29/10 phổ biến 20–50 mm — VietNamNet"
  - "Tổng 3 ngày phổ biến khoảng 60–120 mm (Dân trí ghi 60–130 mm, nêu 'khoảng'), cục bộ trên 250 mm — Dân trí + VietNamNet"
  - "Hà Nội 28/10: thấp nhất 23–25°C, cao nhất 31–33°C; Bắc Bộ chịu không khí lạnh yếu, mưa rào và dông — Dân trí, VietNamNet"
  - "1–2/11 miền Bắc CÓ THỂ đón không khí lạnh mạnh hơn (dự báo, nói rõ 'có thể') — VietNamNet (ông Nguyễn Đức Hòa)"
  - "Khuyến cáo lốc, sét, mưa đá, gió giật; ngập úng vùng trũng, lũ quét sông suối nhỏ, sạt lở đất sườn dốc — VietNamNet"
sensitive_flags: ["thời tiết/thiên tai — đưa mức thông tin và khuyến cáo, không khai thác thương vong"]
vietnam_legal_flags: []
notes: "Voice Vbee tài khoản GỐC (biến TẠM không có trong môi trường; tài khoản gốc hoạt động bình thường). BGM Lyria. Style 3-ticker-tape (claim_style index 2). Transcript (ElevenLabs STT) khớp SCRIPT, chỉ lệch phiên âm ('se lạnh' → 'xe lạnh'). Loudnorm 2-pass + alimiter: -14.7 LUFS, TP -1.3 dBTP. Render 1080x1920/30fps, 63.4s. Góc riêng: từ khoá trending là 'đợt lạnh' nhưng tác động đáng chú ý là mưa lớn ở Hà Tĩnh–Đà Nẵng; đối chiếu Bắc se lạnh vs Trung mưa trên 250 mm cùng một khối không khí lạnh."
