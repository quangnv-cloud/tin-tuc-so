# COMPLIANCE — sua-nghi-dinh-168-vuot-den-do-lan-dau
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-19T14:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): YELLOW   # đề xuất chính sách giao thông (chưa ban hành) — dựng được với framing "đề xuất, chưa có hiệu lực"; không chính trị, không cá nhân, không hình sự
trending_signal: "cục cảnh sát giao thông — vị trí 59/232, 5000+ (related: Lao Động, Tuổi Trẻ, VnExpress); kèm 'nghị định 168/2024/nđ–cp' 65/232, 2000+ và 'đèn giao thông' 20/232, 1000+"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không có ảnh AI
copyright_notes: "ảnh og:image qua ?image=, ghi 'Ảnh tư liệu' + nguồn trên hình: VnExpress (Hook/thumbnail + nền mờ act 2), Tuổi Trẻ (act 2, mặt người đã được báo làm mờ), Dân Trí (act 5, ảnh camera giám sát); nhạc nền Google Lyria tự sinh (không lời — Gemini xác nhận MUSIC_VOCALS: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Chiều 19/11 Cục CSGT (Bộ Công an) đưa định hướng, chuẩn bị nghị định mới thay thế NĐ 168/2024 — Tuổi Trẻ, Dân Trí, VnExpress"
  - "Đèn vàng, xe đi qua vạch dừng: đề xuất không xử phạt — cả 3 báo"
  - "Đèn đỏ, vượt vạch nhưng dừng lại, không cản trở: lần 1 cảnh cáo, lần 2 phạt tiền + trừ điểm, lần 3 lũy kế có thể gấp 3 — cả 3 báo"
  - "Đèn đỏ, vượt vạch và đi tiếp: lần 1 phạt tiền + trừ điểm, lần 2 có thể gấp 2, lần 3 có thể gấp 3 — cả 3 báo"
  - "Tính lũy kế theo thời hiệu, dựa trên dữ liệu camera/hệ thống giám sát — cả 3 báo"
  - "Cảnh cáo vẫn là quyết định xử phạt; CSDL định danh điện tử, GPLX, đăng ký xe đã liên thông — Tuổi Trẻ"
  - "Đây là định hướng nghiên cứu, đề xuất chính sách, chưa có hiệu lực — Tuổi Trẻ, VnExpress"
  - "NĐ 168 hiện hành: ô tô 18–20 triệu đồng, xe máy 4–6 triệu đồng, trừ 4 điểm GPLX — VnExpress"
sensitive_flags: ["đề xuất chính sách giao thông chưa ban hành — nêu rõ 'đề xuất, chưa có hiệu lực' trên hình (chip ĐỀ XUẤT ở Hook, stamp act 5), lời đọc và caption"]
vietnam_legal_flags: ["thông tin pháp luật: tránh hiểu nhầm là quy định đã có hiệu lực — đã gắn nhãn đề xuất ở Hook/act 5/caption, mức phạt hiện hành dẫn đúng NĐ 168/2024 theo VnExpress; không bịa số điều luật"]
notes: "B1: mọi số liệu truy được về ?article= của VnExpress/Tuổi Trẻ/Dân Trí. Act 6 là sự thật đang áp dụng (mức phạt NĐ 168 hiện hành). B6: tiêu đề có chip ĐỀ XUẤT + 'có thể'. B7: góc nhìn riêng = thang chế tài 3 nhóm hành vi × số lần vi phạm, đặt cạnh mức phạt hiện hành; style 3-ticker-tape khác video trước (2-chip-and-leaderboard). CTA là câu hỏi lựa chọn thật. Verify: 67,9s (1080×1920, 30fps); silencedetect không có khoảng lặng ≥0,6s; loudness -14,5 LUFS / TP -1,2 dBTP (sau loudnorm 2-pass); frame cân bằng dọc OK (phần tử cuối ~1340–1440px, caption 1500–1600px); smash-cut act 5 soát chuỗi 10 frame; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT 100%. BGM: Google Lyria (không dùng fallback ElevenLabs). Voice: Vbee tài khoản GỐC."
