# COMPLIANCE — gia-xang-giam-6-ky-lien-tiep-26-11
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-26T13:55:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — giá xăng dầu điều hành đã ban hành (liên Bộ Công Thương – Tài chính); nêu nội dung điều chỉnh, không bình luận chính trị
trending_signal: "dự báo giá xăng dầu hôm nay — vị trí 10/267, 5000+; kèm 'xăng' — 65/267, 1000+ (related: 24h, Tuổi Trẻ, Thanh Niên); có ở cả category=news (VnExpress b6396ff338ac, Tuổi Trẻ ca5dc1e76b25, Dân Trí 247ae83fb0f2)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không ảnh AI; biểu đồ/thanh/sparkline là đồ hoạ CSS/SVG
copyright_notes: "ảnh og:image bài VnExpress (Hook), Tuổi Trẻ (act 2), Dân Trí (act 6) qua ?image=, ghi 'Ảnh: VnExpress' / 'Ảnh: Tuổi Trẻ' / 'Ảnh: Dân Trí' trên hình, không chỉnh sửa nội dung ảnh, không xoá watermark; nhạc nền Google Lyria tự sinh (lyria-recipe.py, không lời — Gemini xác nhận VOCALS_IN_MUSIC: no, DRUMS: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Điều chỉnh từ 15h 26/11 bởi liên Bộ Công Thương – Tài chính — VnExpress, Dân Trí, Tuổi Trẻ"
  - "E5 RON 92 18.390 đ (−180); E10 RON 95-III 19.050 đ (−50); diesel 24.960 đ (−1.380); mazut 17.570 đ/kg (−1.100) — VnExpress, Dân Trí (Tuổi Trẻ ghi số lẻ 18.391/19.056/24.965 — chọn số tròn của 2 báo trùng nhau)"
  - "Xăng giảm 6 kỳ liên tiếp trong tháng 11 — VnExpress ('6 kỳ được điều chỉnh giảm'), Dân Trí ('giảm 6 phiên liên tiếp'), Tuổi Trẻ ('lần thứ 6 liên tiếp')"
  - "So với cuối tháng trước: E10 hạ gần 6.700 đ, diesel gần 5.300 đ — VnExpress"
  - "Giá xăng về ngang thời điểm ngay trước khi xảy ra xung đột Trung Đông — VnExpress"
  - "Thành phẩm thế giới bình quân giảm 8–9,3% giữa kỳ 19/11 và 26/11; RON95 −8,6%, diesel −8,1%, mazut −8,9%; lo ngại dư cung — VnExpress (dẫn liên Bộ); Tuổi Trẻ (IEA dự báo dư cung)"
  - "Brent phiên 25/11 +3,5% lên 94,61 USD/thùng — Dân Trí (dẫn Reuters)"
  - "Trích lập quỹ BOG 1.400 đ/lít xăng, 500 đ/lít diesel — VnExpress, Dân Trí"
  - "Thuế TTĐB với xăng 0% đến hết tháng 3/2027 — VnExpress"
  - "Kỳ trước 19/11 (chỉ trên hình) — Dân Trí"
sensitive_flags: ["nhắc 'xung đột ở Trung Đông' chỉ như mốc giá theo đúng câu chữ VnExpress, không bình luận chính trị/đối ngoại", "CTA về quỹ bình ổn: câu hỏi quan điểm chính sách giá, framing trung lập 2 phía"]
vietnam_legal_flags: []
notes: "B1: mọi số liệu truy được về ?article= VnExpress/Dân Trí/Tuổi Trẻ; không số tự tính (thanh tỉ lệ dùng đúng tỉ lệ các số nguồn: 180/50/1.380 và 6.700/5.300). Đường line-chart mờ sau số 6.700 ở act 4 và sparkline act 6 là texture trang trí không nhãn/không giá trị (theo mô tả style 10-stock-terminal). B6: tiêu đề = sự kiện + số liệu, không giật tít. B7: góc nhìn riêng = đặt cạnh nhau thế giới −8–9,3% / xăng trong nước chỉ −50–180 đ / trích lập lại quỹ BOG 1.400 đ (không khẳng định nhân quả), thanh tỉ lệ mức giảm từng mặt hàng, cột so sánh giá thành phẩm vs cú bật Brent; style 10-stock-terminal khác video trước (9-editorial-clipping). Verify: 70,0s (1080×1920, 30fps, h264 render --quality high --video-bitrate 10M, AAC 192k); silencedetect chỉ có 0,61s lặng ở cuối (69,38→70,0s — đuôi fade, không phải giữa video); loudness -14,4 LUFS / TP -1,3 dBTP (loudnorm 2-pass + limiter, gốc -20,4); frame cuối reveal mỗi act: Hook ~1460, What ~1420, Facts ~1420, Data ~1440, Context ~1430, Impact ~1440, CTA chữ ký ~1500 (+ caption karaoke ~1520–1600); smash-cut act 4 soát chuỗi 12 frame; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu, GARBLED: none ('diesel' đọc 'đi-ê-zen' đúng cách đọc tiếng Việt). Thumbnail t=3,5s (Hook vào xong ~2,7s): đủ logo + tên kênh + badge nguồn + tiêu đề + 2 tag. Voice: Vbee tài khoản GỐC. BGM: Google Lyria (không cần fallback ElevenLabs). Bản đăng FB/YT: output/gia-xang-giam-6-ky-lien-tiep-26-11-fb.mp4 (nén ~1 Mbps, cùng nội dung, 9,1 MB). Đăng: Facebook Reel post 122130041343451654 (video 2345199256322228, thumbnail code 200); YouTube uiWF5k665zc (gọi 1 lần, không timeout, ~149s; thumbnail tùy chỉnh 403 youtube.thumbnail — quyền kênh chưa mở, thử lại yt_set_thumbnail sau 90s vẫn 403)."
