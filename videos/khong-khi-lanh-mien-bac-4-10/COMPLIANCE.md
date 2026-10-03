# COMPLIANCE — khong-khi-lanh-mien-bac-4-10
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-03T00:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN (thời tiết / cảnh báo cộng đồng, đưa trung lập, dẫn nguồn cơ quan khí tượng)
trending_signal: "gió mùa đông bắc / vị trí #3 (index 2) trong list trend / 200+; đồng thời có ở category=news (VnExpress, Dân Trí, Tuổi Trẻ)"
GATE B (content):   GREEN (B1 số liệu truy được về ?article=; B4 ảnh og:image VnExpress có dẫn nguồn, không ảnh AI; B6 tiêu đề trung lập; B7 góc nhìn chia đôi nóng↔lạnh, đất liền↔biển)
GATE C (final):     PASS (thumbnail + 7 frame render đúng; transcript Gemini khớp SCRIPT; caption = CAPTION.md)

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress, có dẫn nguồn; giọng AI narrator chung (Vbee Minh Quân); nhạc Lyria tự sinh (không dùng ElevenLabs Music fallback); SFX trong repo"
claims_verified: ["Hà Nội có ngày 38,4°C; Sơn La, Phú Thọ, Cao Bằng, Hải Phòng, Hưng Yên, Ninh Bình trên 37°C (VnExpress)", "Lạnh đến Đông Bắc Bộ khoảng đêm 4/10 rồi Bắc Bộ + Bắc Trung Bộ (VnExpress, Dân Trí)", "Thấp nhất 19-22°C, núi cao 14-17°C (VnExpress, Dân Trí)", "AccuWeather qua VnExpress: HN 26-35°C ngày 2-3/10, Chủ nhật giảm 5 độ còn 23-30°C", "Mưa giông Bắc Bộ 4 đến sáng 5/10; Thanh Hóa-Huế đêm 4 đến 6/10 (Dân Trí)", "Gió đông bắc vịnh Bắc Bộ cấp 6-7 giật 8-9, sóng 2-3 m (VnExpress)"]
sensitive_flags: ["thiên tai/thời tiết — chỉ nêu khuyến cáo của cơ quan khí tượng, không khai thác thương vong"]
vietnam_legal_flags: []
notes: "Karaoke caption dùng mốc từ Whisper cục bộ (ElevenLabs STT hết quota). Loudness sau loudnorm -14.5 LUFS / -1.3 dBTP. Chưa đăng FB/YouTube: xem tóm tắt (ràng buộc nhánh push)."
