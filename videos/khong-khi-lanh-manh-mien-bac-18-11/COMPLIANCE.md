# COMPLIANCE — khong-khi-lanh-manh-mien-bac-18-11
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-17T14:25:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — thời tiết / cảnh báo cộng đồng, dẫn nguồn cơ quan khí tượng + Ban Chỉ đạo PTDS quốc gia; không thương vong
trending_signal: "đợt lạnh — vị trí 73/234, 5000+ (related: Lao Động, Tuổi Trẻ, Dân Trí); kèm 'thời tiết miền bắc' 54/234, 2000+ và 'không khí lạnh miền bắc' 94/234, 2000+ (related: Dân Trí, VietNamNet, Lao Động)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không có ảnh AI
copyright_notes: "ảnh og:image qua ?image=, ghi 'Ảnh tư liệu' + nguồn trên hình: VnExpress (Hook/thumbnail), Tuổi Trẻ (act 2); không dùng ảnh Dân Trí (có tranh cổ động chính trị ở nền); nhạc nền Google Lyria tự sinh (không lời — Gemini xác nhận MUSIC_VOCALS: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Không khí lạnh ảnh hưởng từ sáng 18/11, vùng núi Bắc Bộ trước rồi toàn miền Bắc, Bắc Trung Bộ, Trung Trung Bộ — VnExpress, Dân Trí, Tuổi Trẻ"
  - "18–19/11 Bắc Bộ, Thanh Hóa, Nghệ An mưa dông, có nơi mưa lớn — VnExpress, Dân Trí, Tuổi Trẻ"
  - "Hà Nội ảnh hưởng từ trưa 18/11, chuyển rét từ tối — VnExpress, Dân Trí"
  - "Bắc Trung Bộ chuyển rét từ 19/11, Quảng Trị – Huế chuyển lạnh; vùng núi có nơi rét đậm từ đêm 18/11 — VnExpress, Dân Trí, Tuổi Trẻ"
  - "Thấp nhất trung du & vùng núi Bắc Bộ 12–15°C, vùng núi cao dưới 10°C, đồng bằng BB & BTB 15–18°C — cả 3 báo"
  - "Sa Pa (trên 1.500 m) thấp nhất ~8–11°C — VnExpress"
  - "17/11 Tây Bắc Bộ nắng, có nơi trên 32°C — Dân Trí (dự báo ngày 17/11 của TT Dự báo KTTV quốc gia)"
  - "Đêm 19 – ngày 20/11 không khí lạnh tăng cường, ảnh hưởng một số nơi Nam Trung Bộ — VnExpress, Dân Trí"
  - "Vịnh Bắc Bộ từ trưa–chiều 18/11 gió cấp 6–7, giật cấp 8–9, sóng 2–4 m — VnExpress, Tuổi Trẻ"
  - "Tối 16/11 Ban Chỉ đạo Phòng thủ dân sự quốc gia đề nghị 26 tỉnh, thành Bắc Bộ & Trung Bộ chủ động ứng phó; ven biển Quảng Ninh → Lâm Đồng thông báo tàu thuyền; tránh bếp than sưởi trong phòng kín — Tuổi Trẻ, VnExpress"
sensitive_flags: ["thời tiết/cảnh báo cộng đồng — đưa trung lập, chỉ nêu dự báo + khuyến cáo chính thức, không thương vong"]
vietnam_legal_flags: []
notes: "B1: mọi số liệu truy được về ?article= của 3 báo; bỏ nhiệt độ thấp nhất Hà Nội vì 2 nguồn vênh; không nhắc vùng biển đặc khu (tránh chủ đề chủ quyền). Dự báo được gắn nguồn 'Theo Trung tâm Dự báo KTTV quốc gia'. Act 6 là sự thật đã xảy ra (công văn tối 16/11). B7: góc nhìn riêng = gom 3 báo thành timeline diễn biến + bảng xếp hạng nhiệt độ thấp nhất trên thang 0–20°C + đối chiếu '1 ngày trước vẫn trên 32°C'; style 2-chip-and-leaderboard khác video trước (1-card-and-bar). CTA là câu hỏi lựa chọn thật. Verify: 60,7s; silencedetect không có khoảng lặng ≥0,6s; loudness -14,6 LUFS / TP -1,3 dBTP (sau loudnorm 2-pass); frame cân bằng dọc OK (phần tử cuối ~1395–1475px, caption 1490–1600px); smash-cut act 5 soát chuỗi 9 frame; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT 100%. BGM: Google Lyria (không dùng fallback ElevenLabs). Voice: Vbee tài khoản GỐC."
