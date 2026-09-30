# COMPLIANCE — nang-nong-mien-bac-chuyen-lanh-30-9
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-30T00:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN  (A2 — thời tiết / cảnh báo cộng đồng, đưa trung lập, dẫn nguồn cơ quan chức năng)
trending_signal: "dự báo thời tiết hôm nay / vị trí #2 trong list category=trend / trafficApprox 500+ (cùng chủ đề có mặt ở category=news: Tuổi Trẻ, Dân Trí)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero og:image Dân Trí (?image=8350a53cc292), có dẫn nguồn 'Ảnh: Dân Trí' + badge nguồn; không chỉnh sửa nội dung ảnh. Giọng đọc AI narrator chung (Vbee HN - Minh Quân), không giả người thật. Nhạc nền Google Lyria tự sinh (không lời; transcript toàn bộ audio chỉ có lời script, không có vocal lạ). SFX từ repo. Video 100% tự dựng, không reup."
claims_verified:
  - "30/9: trung du & đồng bằng Bắc Bộ, Thanh Hóa–Đà Nẵng, phía đông Quảng Ngãi nắng nóng, cao nhất 35–36°C, có nơi trên 36°C — Tuổi Trẻ ?article=d1e401b62c81 (nguồn 24h ghi 'có nơi trên 37°C' → dùng số thận trọng hơn)"
  - "Hà Nội thấp nhất 27–29°C, cao nhất 35–37°C — Tuổi Trẻ"
  - "TP.HCM 32–34°C, mưa rào chiều tối — Tuổi Trẻ"
  - "Độ ẩm thấp nhất phổ biến 45–50% ở vùng nắng nóng; nhiệt độ cảm nhận chênh 1–3°C — 24h ?article=7648e97d4e84 + Tuổi Trẻ"
  - "Đêm 30/9 không khí lạnh yếu ảnh hưởng Bắc Bộ; từ 1/10 giảm ~2–3°C, nắng nóng chấm dứt; Trung Bộ nóng thêm ~2 ngày; 4–5/10 CÓ KHẢ NĂNG lạnh mạnh hơn (đóng khung là dự báo) — 24h (trích Trung tâm Dự báo KTTV Quốc gia)"
  - "Cảnh báo rủi ro thiên tai do nắng nóng cấp 1; nguy cơ cháy nổ khu dân cư; mất nước khi ở ngoài nắng lâu — 24h"
  - "ĐBSCL: triều cường, trạm hạ nguồn báo động 2–3, có nơi báo động 3; nguy cơ ngập vùng trũng thấp, sạt lở bờ bao — Tuổi Trẻ"
  - "Tiêu đề Dân Trí 'nắng nóng gay gắt đến trên 37°C' — chỉ dùng để xác nhận chủ đề/ảnh, không lấy số liệu"
sensitive_flags: ["thiên tai/thời tiết — đưa mức thông tin + khuyến cáo, không khai thác thương vong", "dự báo 4–5/10 nêu rõ là 'có khả năng'"]
vietnam_legal_flags: []
notes: "Voice Vbee 7/7 dòng; transcript Gemini khớp SCRIPT (ratio 1.00 cả 7 act, không lỗi đọc lắp/viết tắt). Caption karaoke tính thời điểm từ độ dài file voice + silencedetect vì ElevenLabs STT hết quota (0 credits). BGM: Lyria (không cần fallback ElevenLabs Music). Góc nhìn riêng (B7): bản đồ hoá mốc kết thúc nóng theo vùng + biểu đồ khoảng nhiệt Hà Nội vs TP.HCM. Loudness sau loudnorm -14.6 LUFS, TP -1.2 dBTP. Chủ đề thời tiết gần với video 'khong-khi-lanh-ap-thap-nhiet-doi-bien-dong' nhưng khác góc (nắng nóng 30/9 → mốc lạnh 1/10, 4–5/10) và khác style."
