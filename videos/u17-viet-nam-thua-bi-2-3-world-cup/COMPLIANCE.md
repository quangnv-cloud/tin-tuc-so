# COMPLIANCE — u17-viet-nam-thua-bi-2-3-world-cup
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-21T13:48:58Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — kết quả thể thao có yếu tố VN (đội tuyển U17 quốc gia tại U17 World Cup 2026); tường thuật kết quả, số liệu, phát ngôn chính thức
trending_signal: "u-17 bỉ đấu với đội tuyển bóng đá u-17 quốc gia việt nam — vị trí 134/220, 20000+ (related: 24h, VnExpress, Lao Động); kèm 'vietnam vs belgium' 110/220 & 112/220, 200+; có ở cả category=news (VnExpress 'HLV Roland: U17 Việt Nam xứng đáng với mọi lời khen dù thua Bỉ' + hơn 25 bài Dân Trí/Tuổi Trẻ)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không có ảnh AI; bản đồ là đồ hoạ vector từ dữ liệu Natural Earth
copyright_notes: "ảnh og:image qua ?image=, ghi nguồn trên hình: VnExpress (Hook/thumbnail — HLV Roland), Tuổi Trẻ (act 2 — pha tranh bóng); không cắt/xoá watermark; bản đồ vector world-atlas/Natural Earth (public domain); nhạc nền Google Lyria tự sinh (không lời — Gemini xác nhận MUSIC_VOCALS: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Việt Nam thua Bỉ 2-3, lượt 1 bảng G U17 World Cup 2026, tối 20/11, Học viện Aspire (Qatar) — VnExpress, Dân Trí, Tuổi Trẻ"
  - "Bỉ là đương kim á quân châu Âu; HLV Cristiano Roland — VnExpress, Dân Trí"
  - "Bàn thắng: 4' Lê Sỹ Bách (đánh gót), 39' Moorthamer, 42' Achahbar, 60' Philips, 84' Chu Ngọc Nguyễn Lực (trực tiếp từ phạt góc) — VnExpress, Dân Trí, Tuổi Trẻ"
  - "Bàn thắng đầu tiên của VN ở World Cup 11 người, dù từng dự U20 nam 2017 và ĐTQG nữ 2023 — VnExpress"
  - "Mali thắng New Zealand 3-0; BXH Mali 3đ +3, Bỉ 3đ +1, VN 0đ −1, NZ 0đ −3 — Tuổi Trẻ, Dân Trí, VnExpress"
  - "Thể thức: 2 đội đầu bảng + 8/12 đội thứ ba tốt nhất đi tiếp — Dân Trí, Tuổi Trẻ"
  - "FIFA: pha đánh gót 'đậm chất Zlatan'; AFC: 'Dù thất bại nhưng đây là trận đấu đáng khen của U17 Việt Nam' — Dân Trí (93fcfc4c0114)"
  - "HLV Roland: 'Đội tuyển xứng đáng với mọi lời khen dù thất bại' — VnExpress; thừa nhận thể lực là vấn đề khó khăn — Dân Trí"
  - "Lượt 2 gặp New Zealand 22h30 ngày 23/11 — VnExpress, Dân Trí, Tuổi Trẻ"
sensitive_flags: ["cầu thủ U17 (vị thành niên) — chỉ nêu tên + hành động thi đấu như báo chí chính thống đã đưa, không thông tin cá nhân", "không bình luận các tình huống VFS/trọng tài tranh cãi", "không nội dung cá cược"]
vietnam_legal_flags: []
notes: "B1: mọi số liệu truy được về ?article= VnExpress (e9e1f2b63be1) + Dân Trí (58a7724a3a9a, ee9887f524ab, 93fcfc4c0114, 589d6170d321, c104ec52fddf) + Tuổi Trẻ (8d1bf90b1a28). Act 6 là sự thật đã xảy ra (lời khen của FIFA/AFC/HLV sau trận). B6: tiêu đề = kết quả + cột mốc, 'lịch sử' theo đúng cách VnExpress/Dân Trí mô tả. B7: góc nhìn riêng = cột mốc bàn thắng đầu tiên ở World Cup 11 người (so với U20 nam 2017, tuyển nữ 2023), diễn biến 5 bàn theo phút, bản đồ 4 châu lục bảng G + thể thức đi tiếp; style 5-map-and-geo khác video trước (4-split-comparison). Verify: 61,1s (1080×1920, 30fps, h264 ~7,9 Mbps, AAC 192k); silencedetect không có khoảng lặng ≥0,6s; loudness -14,5 LUFS / TP -1,3 dBTP (sau loudnorm 2-pass); frame cuối reveal mỗi act soát bằng Read — phần tử cuối kết thúc ~1400–1475px, caption karaoke 1505–1615px; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu. Voice: Vbee tài khoản GỐC. BGM: Google Lyria. Bản đăng FB/YT: output/u17-viet-nam-thua-bi-2-3-world-cup-fb.mp4 (nén 1080×1920 ~1 Mbps, cùng nội dung) vì Apps Script tải cả file vào bộ nhớ."
