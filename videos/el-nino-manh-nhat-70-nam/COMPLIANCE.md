# COMPLIANCE — el-nino-manh-nhat-70-nam
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-09T06:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN (khoa học / thời tiết — cảnh báo khí hậu của Tổ chức Khí tượng Thế giới, đưa trung lập)
trending_signal: "el niño / vị trí #57-58 trong category=trend / 200+"; đối chiếu item news Tuổi Trẻ id 12250492f2c9 ("El Nino có thể mạnh nhất hơn 70 năm, đỉnh điểm vào tháng 12")
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài Tuổi Trẻ (đất nứt nẻ), có dẫn nguồn 'Ảnh: Tuổi Trẻ'; giọng AI narrator chung (Vbee hn_male_minhquan_yt-stable); nhạc Google Lyria tự sinh; SFX trong repo"
claims_verified: [WMO cảnh báo ngày 8/10, El Nino mạnh lên nhanh, có thể thành một trong những đợt mạnh nhất kể từ 1950, đạt đỉnh cuối 2026 (Tuổi Trẻ); nguy cơ nắng nóng, hạn hán, lũ lụt toàn cầu (Tuổi Trẻ); Tổng thư ký Celeste Saulo: hiện tượng đã hình thành rõ rệt, gần 100% khả năng tiếp diễn đến 2/2027 (Tuổi Trẻ); chênh lệch nhiệt độ mặt nước biển vùng xích đạo trung tâm và Đông Thái Bình Dương: hơn 1,6°C (tháng 6), 2,5°C (tháng 8), dự báo khoảng 3,7°C quý cuối năm, kỷ lục trước 2,6°C (2015-2016) (Tuổi Trẻ); đợt El Nino trước góp phần khiến 2024 là năm nóng nhất lịch sử quan trắc, ~1,55°C trên tiền công nghiệp 1850-1900 (Tuổi Trẻ); dự báo từ tháng 11 ĐBSCL, Tây Nguyên, Đông Nam Bộ có khả năng hạn hán, xâm nhập mặn diện rộng (Tuổi Trẻ, nêu rõ là dự báo); Trung Mỹ hạn hán kéo dài, mất mùa, vật nuôi chết hàng loạt (Tuổi Trẻ). Chỉ đối chiếu 1 bài báo gốc (Tuổi Trẻ, dẫn WMO) + headline related của trend (France 24, WMO, Vietnam.vn) cùng nội dung]
sensitive_flags: ["dự báo thiên tai khí hậu — nêu rõ nguồn WMO và 'dự báo', kèm 'cần theo dõi thông báo của cơ quan khí tượng' trong caption"]
vietnam_legal_flags: []
notes: "Style 4-split-comparison (claim_style index 3). BGM thực tế: Google Lyria (không cần fallback). Voice: Vbee 1.09, lời đọc sinh qua file JSON UTF-8. Karaoke caption: ElevenLabs STT hết quota nên timing từng từ ước lượng từ whisper local (neo theo từ khớp) + nội suy. Transcript whisper local khớp SCRIPT (khác biệt chỉ do nhận dạng: 'Celeste Saulo' -> 'Senator Solo', 'năng nóng', 'tháng mười một' nghe thành 'tháng 10, một'; Gemini bị 429 nên không dùng được). Loudness sau loudnorm 2-pass -14.5 LUFS / -2.5 dBTP. Ảnh hero độ phân giải thấp (1200x751) nhưng đủ rõ."
