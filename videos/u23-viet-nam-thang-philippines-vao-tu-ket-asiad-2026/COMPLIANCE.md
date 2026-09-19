# COMPLIANCE — u23-viet-nam-thang-philippines-vao-tu-ket-asiad-2026
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-19T01:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "đội tuyển bóng đá u-23 quốc gia philippines đấu với u-23 việt nam — trafficApprox 20000+ (vị trí #78/162 danh sách trend Google Trends VN, 2026-09-19)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image báo Dân Trí (id 035eb7329b35), có dẫn nguồn, không chỉnh sửa nội dung; nhạc nền sinh bằng Google Lyria (tự sinh, không lời, không sample từ nguồn khác); SFX từ bộ SFX chung của repo (_reference-astra-openai/assets/sfx)."
claims_verified:
  - "U23 Việt Nam thắng U23 Philippines 2-0 — đối chiếu Dân Trí (bài chính, id 035eb7329b35) + VnExpress ('Việt Nam hạ Philippines, sáng cửa vào tứ kết ASIAD 2026')"
  - "Bàn thắng: Thanh Nhàn phút 74, Lê Phát phút 87 — theo tường thuật diễn biến của Dân Trí"
  - "Kiểm soát bóng 73% trong hiệp một — theo Dân Trí"
  - "Huấn luyện viên trưởng: Đinh Hồng Vinh — theo Dân Trí"
  - "Địa điểm: Nagoya, Nhật Bản; vòng bảng C, Á vận hội (Asiad) lần thứ 20 — theo Dân Trí"
  - "U23 Uzbekistan thắng U23 Kuwait cùng ngày, tạo thêm lợi thế cho U23 Việt Nam ở bảng C — theo tiêu đề bài liên quan trên Dân Trí (category=news), dùng làm bối cảnh, không trích số liệu trận đó vì không có trong bài đã tải"
  - "Kết quả giúp U23 Việt Nam rộng cửa giành vé vào tứ kết Asiad 20 — theo tiêu đề chính bài Dân Trí"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề A2 (kết quả thể thao có yếu tố VN — đội tuyển U23 quốc gia). Không đụng đời tư cầu thủ, không yếu tố hình sự/chính trị/cá độ. Style dựng: 4-split-comparison (claim_style index 3), thiết kế mới hoàn toàn (không copy-paste HTML/CSS từ video split-comparison trước đó — iphone-18-pro-thay-doi-so-voi-17-pro / u23-viet-nam-hoa-1-1-kuwait). Kỹ thuật hình ảnh nâng cao đầy đủ: depth background (blob + stars, seed 20260919), glow brand-color trên card/divider, caption karaoke đồng bộ giọng đọc (ElevenLabs STT scribe_v1, word-level timestamps), cân bằng dọc verify bằng frame thật ở cuối animation-reveal mỗi act. Audio: BGM Lyria calm (density 0.25, brightness 0.4, negative-prompt đầy đủ), carve.mjs strength 0.4, loudnorm 2-pass đưa về -14.1 LUFS / -1.3 dBTP (lệch ban đầu -15.6 LUFS đã được sửa). Verify 5 bước: (1) duration 61.9s đúng thiết kế; (2) silencedetect — không khoảng lặng chết giữa video (chỉ có ở đuôi fade-out cuối, đã cắt bỏ ở bản audio cuối); (3) loudnorm — đạt -14.1 LUFS / True Peak -1.3 dBTP; (4) trích frame tại cuối animation-reveal mỗi act — phần tử cuối cùng đều kết thúc trong khoảng top 1400-1680px, không trống đen; (5) transcript qua Gemini multimodal (gemini-flash-latest, Whisper host bị chặn) khớp hoàn toàn SCRIPT.md, không câu nào bị chế thêm khi sinh voice."
