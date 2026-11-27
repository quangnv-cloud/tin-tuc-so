# COMPLIANCE — ca-phe-tuoi-rot-con-15000-dong-kg
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-27T13:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN   # A2 — kinh tế/nông sản trung lập (giá cà phê đầu vụ), không khuyến nghị đầu tư/mua bán
trending_signal: "giá cà phê robusta — vị trí 30/246, 2000+; kèm 'gia lai' — 43/246, 2000+ và 'giá cà phê hôm nay' — 54/246, 1000+ (related: VnExpress, Dân Trí, Lao Động); có ở cả category=news (VnExpress 29286309528a, Dân Trí 879d208696c7)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false        # giọng AI narrator chung (Vbee HN - Minh Quân); không ảnh AI; cột/thẻ/icon là đồ hoạ CSS
copyright_notes: "ảnh og:image bài VnExpress (Hook) và Dân Trí (act 2) qua ?image=, ghi 'Ảnh: VnExpress' / 'Ảnh: Dân Trí' trên hình, không chỉnh sửa nội dung ảnh, không xoá watermark; nhạc nền Google Lyria tự sinh (lyria-recipe.py, không lời — Gemini xác nhận VOCALS_IN_MUSIC: no, DRUMS: no); SFX bộ repo; video 100% tự dựng"
claims_verified:
  - "Cà phê tươi ~15.000 đ/kg, giảm 40% so với cùng kỳ (khảo sát Quảng Ngãi) — VnExpress; Dân Trí ghi ~16.000 đ/kg ở Đắk Lắk (trên hình ghi 15.000–16.000)"
  - "Nông hộ mất 25–30% doanh thu dù được mùa — VnExpress"
  - "Cà phê nhân mất giá liên tục từ đầu tháng 11; khảo sát Quảng Ngãi, Đắk Lắk, Lâm Đồng, Gia Lai — VnExpress"
  - "Ngày 25/11 cà phê nhân 69.500–70.000 đ/kg — VnExpress; Dân Trí (Đắk Lắk 70.000, Lâm Đồng 69.500)"
  - "−16.000 đ (−17%) so với tháng trước; ~−40.000 đ (−36%) so với cùng kỳ — VnExpress"
  - "Cà phê tươi giảm 200–500 đ/kg mỗi ngày — VnExpress (lời nông dân, video ghi 'theo nông dân')"
  - "Robusta London giảm 12 phiên liên tiếp; kỳ hạn 1/2027 phiên 24/11 2.813 USD/tấn — VnExpress"
  - "Robusta thấp nhất 3 năm — VnExpress dẫn Reuters"
  - "Vicofa ước sản lượng niên vụ 2026–2027 ~2,2 triệu tấn, tăng hơn 5% — VnExpress"
  - "Việt Nam ~18% nguồn cung toàn cầu — VnExpress, Dân Trí"
  - "Cao điểm thu hoạch giữa tháng 11 đến hết tháng 12 — VnExpress, Dân Trí"
  - "Xuất khẩu tháng 10: 114.000 tấn, +61%; lũy kế 10 tháng 1,57 triệu tấn, +18,8% — Dân Trí"
sensitive_flags: ["CTA bán ngay hay trữ chờ giá: câu hỏi quan điểm, framing 2 phía, không khuyến nghị giao dịch"]
vietnam_legal_flags: []
notes: "B1: mọi số liệu truy được về ?article= VnExpress/Dân Trí; chiều cao cột act 4 theo đúng tỉ lệ suy từ −36%/−17% của nguồn, không gắn nhãn giá tuyệt đối tự tính. Không nêu tên/thu nhập cá nhân nông hộ trong bài gốc. B6: tiêu đề = sự kiện + số liệu, không giật tít. B7: góc nhìn riêng 'được mùa, mất giá' — đặt cạnh nhau sản lượng/xuất khẩu tăng với giá giảm 17%/36%, cột so sánh 3 mốc, bảng nguyên nhân thị trường; style 1-card-and-bar khác video trước (10-stock-terminal). Verify: 63,7s (1080×1920, 30fps, h264 render --quality high --video-bitrate 10M, AAC 192k); silencedetect không có khoảng lặng ≥0,6s; loudness -14,6 LUFS / TP -1,3 dBTP (loudnorm 2-pass + limiter, gốc -20,4); frame cuối reveal mỗi act: Hook ~1436, What ~1468, Facts ~1448 (đã sửa từ ~1380 + số bị xuống dòng, render lại), Data ~1430, Context ~1450, Impact ~1450, CTA chữ ký ~1500 (+ caption karaoke ~1520–1600); smash-cut act 5 tại 'Hiệp hội'; transcript Gemini (gemini-3-flash-preview) khớp SCRIPT.md từng câu, GARBLED: none ('London' nghe thành 'Luân Đôn' — cách phiên âm, chấp nhận). Thumbnail t=3,5s (Hook vào xong ~2,7s): đủ logo + tên kênh + badge nguồn + tiêu đề + 2 tag. Voice: Vbee tài khoản GỐC. BGM: Google Lyria (không cần fallback ElevenLabs). Bản đăng FB/YT: output/ca-phe-tuoi-rot-con-15000-dong-kg-fb.mp4 (nén ~0,9 Mbps, cùng nội dung, 7,4 MB — bản gốc 37MB từng làm Apps Script Out of memory). Đăng: Facebook Reel post 122130212439451654 (video 1821305075794716, thumbnail code 200); YouTube A8oCFKZ-fx8 (gọi 1 lần, không timeout, ~150s; thumbnail tùy chỉnh 403 youtube.thumbnail — quyền kênh chưa mở, thử yt_set_thumbnail sau 90s vẫn 403)."
