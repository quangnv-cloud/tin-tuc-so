# COMPLIANCE — gia-vang-sjc-giam-57-trieu-tu-dinh
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-20T14:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — kinh tế trung lập: giá vàng/bạc niêm yết, số liệu đã công bố; không khuyến nghị đầu tư, không dự báo giá
trending_signal: "giá vàng hôm nay — vị trí 64/203, 10000+ (related: Lao Động, Dân Trí, VnExpress); kèm 'giá bạc hôm nay' 47/203, 1000+ và 'giá vàng thế giới' 74/203, 1000+; có ở cả category=news (Dân Trí 'Giá vàng, bạc đồng loạt lao dốc mạnh')"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không có ảnh AI
copyright_notes: "ảnh og:image qua ?image=, ghi nguồn trên hình: Dân Trí (Hook/thumbnail), VnExpress (act 2), Tuổi Trẻ (act 5) — không cắt/xoá watermark; ảnh minh hoạ kiểu stock/AI của bài Dân Trí 'Bốc hơi 1.000 tỷ USD' KHÔNG dùng; nhạc nền Google Lyria tự sinh (không lời — Gemini xác nhận MUSIC_VOCALS: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Vàng miếng SJC kết phiên 20/11: 129,2–134,2 triệu đ/lượng — Dân Trí, VnExpress, Tuổi Trẻ"
  - "Giảm 5 triệu chiều mua, 3 triệu chiều bán trong phiên — Dân Trí (kết phiên; VnExpress buổi sáng ghi 4/2 → dùng số kết phiên)"
  - "Chênh lệch mua–bán vàng miếng 3 → 5 triệu; nhẫn trơn SJC 128–134, chênh 6 triệu — Dân Trí, VnExpress, Tuổi Trẻ"
  - "Bạc thỏi giảm gần 3 triệu đ/kg — Dân Trí"
  - "Đỉnh lịch sử 191,3 triệu (bán ra) cuối tháng 1; giảm hơn 57 triệu, gần 30% — Dân Trí; VnExpress 'gần 57 triệu, gần 30%'; Tuổi Trẻ 57,8 / 30,1%"
  - "Người mua ở đỉnh lỗ hơn 62 triệu/lượng (191,3 − 129,2) — Dân Trí"
  - "Vàng thế giới có lúc 3.534 USD/ounce, thấp nhất hơn 1 năm — Dân Trí, VnExpress"
  - "USD gần mức cao nhất 19 tháng; FedWatch 99,3% Fed tăng lãi suất tháng 12 — Dân Trí (Tuổi Trẻ: 100%)"
  - "Quy đổi ~112,4 triệu/lượng, chênh trong nước gần 22 triệu — Dân Trí (nguồn khác 23–24,4 → dùng số nguồn chính)"
  - "Doanh nghiệp giảm giá mua vào để phòng ngừa rủi ro — Tuổi Trẻ"
sensitive_flags: ["giá tài sản/kim loại quý — chỉ tường thuật số liệu, KHÔNG khuyến nghị mua/bán, KHÔNG dự báo giá; CTA hỏi quan điểm về chênh lệch mua–bán, không hỏi 'có nên mua'"]
vietnam_legal_flags: []
notes: "B1: mọi số liệu truy được về ?article= Dân Trí (092523f50f41) + VnExpress (c75032de5075) + Tuổi Trẻ (c42de3b8f02c). Act 6 là sự thật đã xảy ra (lỗ tính theo giá niêm yết). B6: tiêu đề = sự kiện + số liệu, không giật gân. B7: góc nhìn riêng = tách 2 chiều mua vào/bán ra cho thấy người bán lại chịu thiệt kép (giá giảm + chênh lệch nới rộng) và đối chiếu trong nước ↔ thế giới; style 4-split-comparison khác video trước (3-ticker-tape). Verify: 70,9s (1080×1920, 30fps, h264 ~8,6 Mbps, AAC 192k); silencedetect không có khoảng lặng ≥0,6s; loudness -14,5 LUFS / TP -1,0 dBTP (sau loudnorm 2-pass); frame cuối reveal mỗi act soát bằng Read — phần tử cuối kết thúc ~1390–1460px, caption karaoke 1500–1600px; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu. Voice: Vbee tài khoản GỐC. BGM: Google Lyria."
