# COMPLIANCE — tphcm-mua-trai-mua-cong-ngan-trieu-10000-ty
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-28T14:25:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — thời tiết / hạ tầng chống ngập; đưa mức thông tin, dẫn Đài KTTV Nam Bộ, không thương vong, không chính trị
trending_signal: "dự báo thời tiết tphcm — vị trí 13/209, 100000+ (related: VietNamNet, Lao Động, 24h); kèm 'dự báo thời tiết tphcm hôm nay' — 15/209, 200+ (related: VnExpress, Tuổi Trẻ, Thanh Niên); có ở cả category=news (VnExpress 1904ba2b19c2, 80db2b7b0acf; Tuổi Trẻ 69b03cf5cc53, 4567f09a1bb4; Dân Trí 81b48f556b9b, d321c59e86ac)"
GATE B (content):   YELLOW-fixed   # B1: sửa 2 câu trước render — lượng mưa >100 mm ghi rõ là DỰ BÁO; nước dâng chân cầu Phú Mỹ ghi rõ là đợt triều 25/11 (sinh lại voice dòng 2 và 6)
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không ảnh AI; bảng xếp hạng/chip/thẻ là đồ hoạ CSS
copyright_notes: "ảnh og:image bài VnExpress (Hook), Tuổi Trẻ (act 2), Dân Trí (act 5) qua ?image=, ghi 'Ảnh: VnExpress' / 'Ảnh: Tuổi Trẻ' / 'Ảnh: Dân Trí' trên hình, không chỉnh sửa nội dung ảnh, không xoá watermark; nhạc nền Google Lyria tự sinh (lyria-recipe.py, recipe calm, không lời — Gemini xác nhận VOCALS: no, RHYTHMIC_DRIVE: low); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Đài KTTV Nam Bộ dự báo mưa dông 27–29/11, có nơi có thể >100 mm; rãnh áp thấp + nhiễu động gió đông — VnExpress 80db2b7b0acf, Tuổi Trẻ 69b03cf5cc53"
  - "Chiều 28/11 chủ đầu tư đóng các cống chủ động chống ngập; Trần Xuân Soạn (thường ngập nhất trước đây) không ngập do triều, nước mưa đọng nhưng rút nhanh — Tuổi Trẻ 69b03cf5cc53 (đối chiếu Tuổi Trẻ 4567f09a1bb4 về tối 27/11)"
  - "6 cống lớn (Bến Nghé, Tân Thuận, Phú Xuân, Mương Chuối, Cây Khô, Phú Định) + 2 cống nhỏ — VnExpress 1904ba2b19c2; Dân Trí 81b48f556b9b"
  - "~570 km², hơn 1/4 diện tích TP HCM trước sáp nhập, ~6,5 triệu người hưởng lợi — VnExpress 1904ba2b19c2, Dân Trí 81b48f556b9b"
  - "3 trạm bơm Bến Nghé, Tân Thuận, Phú Định ~120 m³/s — VnExpress 1904ba2b19c2, Dân Trí 81b48f556b9b"
  - "25/11 vận hành liên hoàn; đỉnh triều Phú An 1,65 m vượt BĐ III 5 cm; Nhà Bè 1,66 m; đỉnh lịch sử Phú An 1,78 m (11/2025) — VnExpress 1904ba2b19c2"
  - "Dự báo đỉnh triều tối 27/11 Phú An 1,58 m — VnExpress 80db2b7b0acf"
  - "Chênh lệch mực nước hai phía cống 1–2,05 m (vận hành thử 25/11, theo Sở NN&MT) — VnExpress 1904ba2b19c2"
  - "Đỉnh triều Phú An, Nhà Bè tăng trung bình 31–38 cm giai đoạn 2000–2025 — VnExpress 1904ba2b19c2 (dẫn Đài KTTV Nam Bộ)"
  - "Khởi công 2016, ban đầu dự kiến xong sau 2 năm — VnExpress 1904ba2b19c2; dừng 3 lần, kéo dài 5 năm (theo chủ đầu tư) — Dân Trí 81b48f556b9b"
  - "Đợt triều 25/11 một số tuyến dưới chân cầu Phú Mỹ vẫn bị nước dâng, vùng bảo vệ chưa khép kín, đoạn hở ngoài phạm vi dự án; Sở NN&MT đề xuất thêm 19 công trình — VnExpress 1904ba2b19c2"
sensitive_flags: ["Dự án BT có tranh luận về tiến độ — không đưa phần chủ đầu tư quy trách nhiệm cho đơn vị tư vấn; không đưa 'cam kết hết ngập' như sự thật; nêu cả mặt hiệu quả lẫn mặt chưa khép kín", "Lượng mưa là dự báo — ghi rõ 'dự báo / có thể'"]
vietnam_legal_flags: []
notes: "B6: tiêu đề = sự kiện (mưa trái mùa trùng triều cường) + chủ thể (cống ngăn triều 10.000 tỷ), không giật tít. B7: góc nhìn riêng = nối tin thời tiết đang trending với phép thử thực tế của công trình: bảng xếp hạng đỉnh triều (kỷ lục 2025 / 25/11 / dự báo 27/11, thanh tỉ lệ theo số thật), con số chênh lệch hai phía cống, bối cảnh 25 năm triều dâng, đặt cạnh nhau mặt 'đã khô' và 'chưa khép kín'; style 2-chip-and-leaderboard khác video trước (1-card-and-bar). Verify: 70,3s (1080×1920, 30fps, h264 render --quality high --video-bitrate 10M, AAC 192k); silencedetect -40dB/0,6s: không có khoảng lặng; loudness -14,5 LUFS / TP -1,2 dBTP (loudnorm 2-pass + limiter, gốc -20,5); frame cuối reveal mỗi act: Hook ~1430, What ~1410, Facts ~1490, Data ~1510, Context ~1455, Impact ~1425, CTA chữ ký ~1475 (+ caption karaoke ~1540–1600); smash-cut act 4 soát chuỗi 9 frame liên tiếp; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu, MISMATCHES: none, GARBLED: none. Lần render 1 phát hiện chip act 2 tràn mép phải → sửa, render lại; BGM Lyria lần 1 bị Gemini đánh giá 'rhythmic drive medium / ticking pulse' → sinh lại Lyria cùng recipe calm (negative thêm percussion), bản dùng: drive low. Thumbnail t=3,5s (Hook vào xong ~2,7s): đủ logo + tên kênh + badge nguồn + tiêu đề + 2 tag. Voice: Vbee tài khoản GỐC. BGM: Google Lyria (không cần fallback ElevenLabs). Bản đăng FB/YT: output/tphcm-mua-trai-mua-cong-ngan-trieu-10000-ty-fb.mp4 (nén ~0,9 Mbps, cùng nội dung, 8,7 MB)."
