# COMPLIANCE — gio-mua-dong-bac-ret-bac-mua-lon-trung-24-11
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-24T13:44:29Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — thời tiết / cảnh báo cộng đồng; đưa mức thông tin + khuyến cáo, dẫn Trung tâm Dự báo KTTV quốc gia và Ban Chỉ đạo Phòng thủ dân sự quốc gia; không nêu thương vong; không nhắc vùng biển/quần đảo nhạy cảm (chỉ "vịnh Bắc Bộ" trong caption)
trending_signal: "gió mùa đông bắc — vị trí 31/238, 100000+ (related: Dân Trí 'Miền Bắc rét diện rộng, miền Trung mưa to'; Tiền Phong 'Dự báo thời tiết Hà Nội ngày 25/11: Rét nhất đợt này…'; VnExpress 'Miền Trung có thể mưa trên 750 mm trong 7 ngày tới'); có ở cả category=news (Dân Trí 0859ab5e5fb7, Tuổi Trẻ 154a0ad5b390, e018b080646f)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không ảnh AI; icon/lưới ô/thang nhiệt độ là đồ hoạ CSS
copyright_notes: "ảnh og:image bài Dân Trí qua ?image= (cầu Long Biên trời âm u), ghi 'Ảnh: Dân Trí' trên hình, không chỉnh sửa nội dung ảnh, giữ nguyên watermark báo; nhạc nền Google Lyria tự sinh (không lời — Gemini xác nhận VOCALS_IN_MUSIC: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Không khí lạnh ảnh hưởng Đông Bắc Bộ gần sáng/sáng 24/11, sau đó Tây Bắc Bộ, Bắc Trung Bộ, Trung Trung Bộ — Dân Trí (?article= 0859ab5e5fb7), Tuổi Trẻ (154a0ad5b390)"
  - "Bắc Bộ, Bắc Trung Bộ chuyển rét; vùng núi Bắc Bộ có nơi rét đậm — Dân Trí, Tuổi Trẻ"
  - "Nhiệt độ thấp nhất Bắc Bộ 14–17°C, vùng núi 11–14°C, núi cao có nơi dưới 10°C; Bắc Trung Bộ 15–18°C — Dân Trí, Tuổi Trẻ (trùng khớp)"
  - "Trung Bộ có thể có 2 đợt mưa lớn 24–30/11; đợt 1 đến hết đêm 25/11, Huế → phía Đông Quảng Ngãi 80–180 mm, cục bộ trên 250 mm — Dân Trí; Tuổi Trẻ (80–180 mm, >250 mm)"
  - "Đợt 2 từ 27–30/11, mưa lớn diện rộng — Dân Trí"
  - "Lũ sông Bồ, Hương (Huế), Trà Khúc, Vệ (Quảng Ngãi) có thể lên báo động 2–3 — Dân Trí"
  - "Nguy cơ lũ quét, sạt lở đất vùng núi Quảng Trị → Khánh Hòa — Dân Trí"
  - "Nam Bộ ngày nắng; TP.HCM cao nhất 32–34°C — Tuổi Trẻ (e018b080646f)"
  - "Vịnh Bắc Bộ gió đông bắc cấp 6–7, giật cấp 8, sóng 2–4 m (chỉ trong caption) — Tuổi Trẻ"
  - "Chiều 23/11 Ban Chỉ đạo Phòng thủ dân sự quốc gia đề nghị các tỉnh, TP ven biển Quảng Ninh → Lâm Đồng hướng dẫn tàu thuyền chủ động phòng tránh; rà soát, sơ tán dân vùng nguy cơ cao ngập sâu, lũ quét, sạt lở — Tuổi Trẻ"
sensitive_flags: ["thiên tai/thời tiết — đưa mức thông tin + khuyến cáo, không khai thác thương vong; dự báo dùng 'có thể'", "đã loại số nhiệt độ Hà Nội do 2 nguồn lệch mốc ngày"]
vietnam_legal_flags: []
notes: "B1: không số liệu nào ngoài nguồn; thang nhiệt độ act 4 vẽ dải 'núi cao' mờ dần sang trái + nhãn 'dưới 10°' (không ngụ ý cận dưới — đã sửa trước render). Act 6 là sự thật đã xảy ra (công văn chiều 23/11). B6: tiêu đề = sự kiện + số liệu, không giật tít. B7: góc nhìn riêng = 'một đợt gió mùa, ba kiểu thời tiết' (Bắc rét / Trung mưa lũ / Nam nắng) + lưới dashboard 2×3 mức báo động từng sông; style 8-icon-grid khác video trước (7-timeline-chronology); CTA hỏi cảnh báo đã đủ sớm chưa. Verify: 72,0s (1080×1920, 30fps, h264 ~4,4 Mbps, AAC 192k); silencedetect không có khoảng lặng ≥0,6s; loudness -14,5 LUFS / TP -1,2 dBTP (loudnorm 2-pass + limiter, gốc -20,4); frame cuối reveal mỗi act soát bằng Read — phần tử cuối kết thúc ~1440–1450px, caption karaoke ~1530px; smash-cut act 5 soát chuỗi 9 frame; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu, GARBLED: none. Thumbnail t=4,9s (sau khi Hook vào xong ở ~3,0s; caption 'hai đợt mưa lớn,'). Voice: Vbee tài khoản GỐC. BGM: Google Lyria (lyria-realtime-exp). Bản đăng FB/YT: output/gio-mua-dong-bac-ret-bac-mua-lon-trung-24-11-fb.mp4 (nén 1080×1920 ~0,9 Mbps, cùng nội dung, 8,9 MB). Đăng: Facebook Reel post 122129610471451654 (video 1502109438472713, thumbnail code 200); YouTube ySSuZAm9JPU (tiêu đề rút gọn còn 89 ký tự vì bản đầy đủ 102 ký tự vượt giới hạn 100; list_yt_content xác nhận không trùng; thumbnail tùy chỉnh 403 youtube.thumbnail — quyền kênh chưa mở)."
