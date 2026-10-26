# COMPLIANCE — bac-ai-thuy-dien-tich-nang

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-26T14:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: ""   # chọn từ category=news (Dân Trí id 988e49bebde3), không qua Google Trends: các từ khoá trending đầu danh sách (xổ số, án mạng/drama, thể thao nước ngoài, ảnh nhà riêng tỷ phú) bị GATE A loại hoặc chỉ có nguồn nước ngoài/thứ cấp; tin hạ tầng năng lượng này có 2 báo chính thống (Dân Trí, Tuổi Trẻ) trong ngày.
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí (?image=988e49bebde3), có dẫn nguồn 'Nguồn: Dân Trí' + 'Ảnh: Dân Trí', không chỉnh sửa; nhạc Lyria tự sinh (không lời); SFX thư viện repo; giọng đọc AI narrator chung Vbee 'HN - Minh Quân' (tài khoản GỐC — biến TAM không có trong môi trường)"
claims_verified:
  - "Ký hợp đồng thiết bị cơ điện Bác Ái chiều 26/10, EVN + liên danh Voith Hydro Shanghai – Powerchina Zhongnan, hơn 4.462 tỷ đồng, đấu thầu quốc tế rộng rãi, 51 tháng — ?article=988e49bebde3 + ?article=eed7ea3ca01b (Tuổi Trẻ)"
  - "4 tổ máy, 1.200MW, tổng mức đầu tư hơn 21.100 tỷ đồng (Dân Trí ghi 21.101), dự án thủy điện tích năng đầu tiên của Việt Nam — cả 2 bài"
  - "Lộ trình tổ máy 12/2029, 4/2030, 8/2030, 12/2030, hoàn thành 5/2031 — cả 2 bài"
  - "Cơ chế bơm tích nước giờ thấp điểm/phát điện giờ cao điểm, điều tần, bù công suất phản kháng, 'cục pin khổng lồ' — Dân Trí"
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  Style claim_style: index 0 = 1-card-and-bar. B7: giải thích cơ chế + so sánh gói thiết bị/tổng mức đầu tư + lộ trình.
  Tiêu đề Tuổi Trẻ có cụm "lớn nhất Đông Nam Á" — KHÔNG dùng vì chỉ có ở tiêu đề, chưa đối chiếu.
  Ảnh Dân Trí là ảnh minh hoạ công trình thủy điện (không khẳng định là công trình Bác Ái).
  Verify: ffprobe 61.17s 1080x1920 30fps; silencedetect không có khoảng lặng chết; loudness -14.9 LUFS, TP -1.6 dBTP
  (loudnorm 2-pass, mẫu gốc -21.2); transcript (ElevenLabs STT, vì Whisper bị chặn) khớp SCRIPT, riêng tên nhà thầu
  nước ngoài được lược khỏi lời đọc (TTS đọc sai) nhưng vẫn hiện bằng chữ; frame cuối mỗi act kết thúc ~top 1380-1490px;
  npm run check 0 error, contrast 69/69 AA.
