# COMPLIANCE — the-cong-viettel-bi-loai-acl-two-hoa-melbourne
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-25T14:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — kết quả thể thao có yếu tố VN (CLB Thể Công Viettel tại AFC Champions League Two); tường thuật kết quả + số liệu, không bình luận cá nhân HLV/cầu thủ, không nhắc chuyện nhân sự
trending_signal: "thứ hạng của melbourne victory gặp thể công — vị trí 19/266, 20000+; kèm 'melbourne victory đấu với thể công' — 28/266, 5000+ (related: 24h, VietNamNet, VnExpress 'Thể Công bị loại sớm ở Cup châu Á', VOV, Tuổi Trẻ); có ở cả category=news (VnExpress d2916fa4a909, Tuổi Trẻ 519749cdc0fc)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không ảnh AI; mẩu báo/thanh/tally là đồ hoạ CSS/SVG
copyright_notes: "ảnh og:image bài VnExpress (Hook) và Tuổi Trẻ (act 2) qua ?image=, ghi 'Ảnh: VnExpress' / 'Ảnh: Tuổi Trẻ' trên hình, không chỉnh sửa nội dung ảnh; nhạc nền Google Lyria tự sinh (lyria-realtime-exp, không lời — Gemini xác nhận VOCALS_IN_MUSIC: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Hòa Melbourne Victory 0-0, lượt 5 bảng E AFC Champions League Two, chiều 25/11 — VnExpress, Tuổi Trẻ, VietNamNet"
  - "Sân Kardinia Park, Australia — VnExpress"
  - "Sau 5 lượt: 2 điểm, cuối bảng E, bị loại sớm 1 vòng — Tuổi Trẻ ('chia tay giải châu Á sớm 1 vòng đấu'), 24h; VnExpress 'hết cơ hội đi tiếp'"
  - "Chuỗi không thắng mọi đấu trường 12 trận — VnExpress, Tuổi Trẻ"
  - "Lần thắng gần nhất: 2-0 Đồng Nai, vòng 1 V-League, 4/9 — VnExpress"
  - "14 cú sút, 3 trúng đích; Melbourne 5 lần trúng đích; thủ môn Caruso Minh Khang cứu thua — Tuổi Trẻ (thủ môn: cả VietNamNet, VnExpress)"
  - "Lượt đi hòa 1-1 trên sân Hàng Đẫy — VnExpress, Tuổi Trẻ, VietNamNet"
  - "Lần thứ 2 liên tiếp không qua vòng bảng 1 Cup châu Á, trước đó ACL 2021 — VnExpress"
  - "Công an Hà Nội thắng Vissel Kobe 3-1 ngày 24/11, 7 điểm, còn cạnh tranh suất đi tiếp ở ACL Elite — VnExpress"
  - "Trận cuối: tiếp Persib Bandung 2/12 (chỉ trên hình) — VnExpress"
sensitive_flags: ["thể thao — kết quả không tích cực của CLB VN: chỉ nêu số liệu, không bình luận cá nhân, CTA hỏi về phong độ đội bóng"]
vietnam_legal_flags: []
notes: "B1: mọi số liệu truy được về ?article= VnExpress/Tuổi Trẻ + related; không số tự tính. B6: tiêu đề = sự kiện + số liệu, không giật tít. B7: góc nhìn riêng = đặt trận hòa vào chuỗi 12 trận không thắng + hiệu suất dứt điểm (14 sút/3 trúng đích, thanh tỉ lệ 3 vs 5 trúng khung) + đối chiếu Công an Hà Nội ở Cúp C1; style 9-editorial-clipping (mẩu báo cắt dán có ghi nguồn) khác video trước (8-icon-grid). Verify: 57,2s (1080×1920, 30fps, h264 render --quality high --video-bitrate 10M, AAC 192k); silencedetect không có khoảng lặng ≥0,6s; loudness -14,5 LUFS / TP -1,2 dBTP (loudnorm 2-pass + limiter, gốc -20,3); frame cuối reveal mỗi act đo pixel: Hook 1478, What 1346 (+ caption karaoke ~1570), Facts 1485, Data 1466, Context 1396, Impact 1455, CTA 1474; smash-cut act 6 soát chuỗi 12 frame; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu, GARBLED: none. Sửa trước khi giao: dòng 4 ban đầu 'hai - không ở vòng một' bị Gemini nghe thành 'vòng 11' → viết lại 'ngay vòng đấu mở màn', sinh lại line4, dựng lại timing/carve, render lại. BGM: Lyria thử 3 lần — 2 bản đầu có trống/nhịp rõ (không đạt brand) → bản cuối bpm 60, density 0.1, năng lượng thấp. Thumbnail t=3,5s (Hook vào xong ~2,7s). Voice: Vbee tài khoản GỐC. Bản đăng FB/YT: output/the-cong-viettel-bi-loai-acl-two-hoa-melbourne-fb.mp4 (nén 1080×1920 ~0,9 Mbps, cùng nội dung, 6,9 MB — bản gốc 37 MB từng làm Apps Script Out of memory). Đăng: Facebook Reel post 122129818869451654 (video 3069970423346718, thumbnail code 200); YouTube mnAD-xf_Z-o (gọi 1 lần, không timeout; thumbnail tùy chỉnh 403 youtube.thumbnail — quyền kênh chưa mở, thử lại yt_set_thumbnail sau 90s vẫn 403)."
