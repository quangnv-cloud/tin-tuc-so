# COMPLIANCE — muc-chuan-tro-cap-nguoi-co-cong-3-012-trieu-tu-1-10
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-30T14:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN (A2 — chính sách mới đã ban hành, nêu nội dung quy định, không bình luận chính trị)
trending_signal: "trợ cấp / vị trí #10 trong 73 từ khoá Google Trends VN / ~1000+; cũng có ở category=news (Tuổi Trẻ, Dân Trí)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài Tuổi Trẻ, có dẫn nguồn 'Ảnh: Tuổi Trẻ'; nhạc nền Google Lyria tự sinh (không lời, lần 2 với prompt beatless); SFX trong repo; giọng AI narrator Vbee 'HN - Minh Quân' (giọng chung, không giả người thật)"
claims_verified:
  - "NĐ 321/2026/NĐ-CP hiệu lực 1/10; mức chuẩn 2.789.000 -> 3.012.000 đ/tháng; mức mới tính từ 1/7 (Tuổi Trẻ + Dân Trí)"
  - "Mức chuẩn là căn cứ trợ cấp/phụ cấp hằng tháng & một lần, điều dưỡng, giáo dục, thăm viếng mộ, xác định danh tính hài cốt liệt sĩ (Tuổi Trẻ)"
  - "+223.000 đ ≈ 8%: tự tính từ hai số liệu của nguồn (3.012.000 − 2.789.000)"
  - "NĐ 335/2026/NĐ-CP hiệu lực 5/10, ban hành 21/8/2026; mức chuẩn trợ giúp xã hội 540.000 đ; tính từ 1/7/2026 (Tuổi Trẻ, Kenh14)"
  - "Khuyết tật nặng người lớn hệ số 1,5 = 810.000 đ (Tuổi Trẻ)"
  - "Thương binh mức hằng tháng cao nhất gần 9,7 triệu (tiêu đề bài liên quan Dân Trí — ghi 'Theo Dân Trí' trên hình)"
  - "Đã bỏ số mức chuẩn trợ giúp xã hội cũ vì hai nguồn mâu thuẫn (500.000 vs 360.000)"
sensitive_flags: ["chính sách an sinh — chỉ nêu nội dung quy định; CTA là câu hỏi quan điểm trung lập"]
vietnam_legal_flags: []
notes: "Thương binh ~9,7 triệu chỉ dựa tiêu đề bài liên quan (chưa đọc toàn văn) nên dùng 'gần' + dẫn nguồn. Whisper-small nghe sai vài từ (nghị/định, hài cốt) nhưng Gemini xác nhận voice đúng script; nghe lại số 335 bằng 4 lượt nhận dạng, 3/4 đọc 'ba trăm ba mươi lăm'. ElevenLabs hết quota (STT/music) — caption dùng faster-whisper, BGM dùng Lyria."
