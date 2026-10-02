# COMPLIANCE — khong-khi-lanh-mien-bac-giam-10-do
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-02T00:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # thời tiết / cảnh báo cộng đồng (A2), đưa mức thông tin + khuyến cáo, dẫn cơ quan khí tượng
trending_signal: "đợt lạnh — Google Trends VN, vị trí #6 trong list category=trend, 500+; đồng thời có ở category=news (Dân Trí)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí (qua ?image=, có dẫn nguồn, không chỉnh sửa); giọng đọc Vbee TTS (AI narrator chung); nhạc nền Google Lyria tự sinh (không lời); SFX bộ trong repo"
claims_verified:
  - "Không khí lạnh cường độ khá mạnh tràn xuống miền Bắc đêm 4 và rạng sáng 5/10 — bài Dân Trí 1/10/2026"
  - "Bắc Bộ mưa vừa, nơi mưa to, dông từ chiều tối 4/10 đến trưa 5/10; phía đông Bắc Bộ ảnh hưởng rõ nhất — Dân Trí"
  - "Nhiệt độ miền Bắc giảm 8-10°C — Dân Trí"
  - "Hà Nội 2/10 cao nhất 32-34°C; 4/10 cao nhất ~27°C — Dân Trí; AccuWeather 4-5/10 cao nhất 28-29°C — Dân Trí (trích AccuWeather)"
  - "5-6/10 miền Bắc đêm và sáng lạnh, vùng núi rét; Thanh Hóa - Quảng Trị mưa rào dông đêm 4-6/10 — Dân Trí"
  - "Tháng 10 nhiệt độ TB cả nước cao hơn TBNN 0,5-1,5°C; khuyến cáo đề phòng tố, lốc, mưa đá, gió giật — Dân Trí"
sensitive_flags: ["thời tiết nguy hiểm — chỉ nêu mức thông tin + khuyến cáo, không khai thác thiệt hại"]
vietnam_legal_flags: []
notes: "B7: góc riêng = đặt mức giảm 8-10°C cạnh số liệu Hà Nội cụ thể (đối chiếu AccuWeather) và bối cảnh cả tháng 10 vẫn ấm hơn trung bình. Số liệu 1 nguồn chính (Dân Trí, dẫn Trung tâm Dự báo KTTV QG). Karaoke caption dùng timing ước lượng (ElevenLabs STT hết quota). Loudness -14.5 LUFS sau loudnorm 2-pass."
