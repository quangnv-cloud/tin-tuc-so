# COMPLIANCE — ap-thap-nhiet-doi-hinh-thanh-bien-dong

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-12T07:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "áp thấp nhiệt đới" (Google Trends VN, id 9589ce7db488, vị trí #2/234 trong danh
  sách, trafficApprox "100000+", pubDate 2026-09-12T05:10:00Z)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card lấy từ ?image=8aa455295473 (bản đồ dự báo đường đi áp
  thấp nhiệt đới, og:image gốc của VnExpress, đồ hoạ dự báo chính thức không phải ảnh dàn dựng cảnh
  thật/người thật, có dẫn nguồn, không watermark ngoài); nhạc nền sinh bằng Google Lyria
  (lyria-recipe.py, preset calm, density 0.25/brightness 0.4, negative-prompt loại bỏ giọng hát/lời),
  100% không lời, thuộc quyền dự án, data-volume 0.30, carve --strength 0.4; SFX từ thư viện repo
  (_reference-astra-openai/assets/sfx); giọng đọc ElevenLabs 'Khánh Lâm - tin tức, thời sự'
  (voice_id RCmOaM1iiIH5xX3QXjIF, model eleven_v3, speed 1.09)."
claims_verified:
  - "Sáng sớm 12/9, vùng áp thấp cách đặc khu Hoàng Sa 150km về phía tây nam mạnh lên thành áp thấp nhiệt đới, gió cấp 6 giật cấp 8, di chuyển hướng tây bắc tốc độ ~10km/h — VnExpress (?article=8aa455295473) + Dân Trí (?article=31ee0089da77, khớp 2 nguồn)"
  - "Dự báo 4h 13/9: áp thấp trên vùng biển Huế - Đà Nẵng; 4h 14/9: vùng biển ven bờ Hà Tĩnh - Huế, sau đó suy yếu dần thành vùng áp thấp — VnExpress + Dân Trí"
  - "Mưa lớn ngày 13/9 có thể vượt 300mm cục bộ tại khu vực từ Nam Nghệ An đến Đà Nẵng — VnExpress"
  - "Vùng biển phía tây Hoàng Sa và Hà Tĩnh - Quảng Ngãi gió cấp 6 giật cấp 8, sóng cao 2-4m, biển động — VnExpress + Dân Trí"
  - "Ban Chỉ đạo Phòng thủ dân sự quốc gia đã đề nghị các địa phương theo dõi mưa lũ, chủ động di dời dân nguy cơ cao, kiểm tra an toàn hồ chứa/đê điều — VnExpress"
  - "Bão Saudel (cuối 8, đầu 9) không gây thiệt hại cho Việt Nam; bão Narra không đổ bộ nhưng hoàn lưu và rãnh áp thấp gây mưa lớn, giông sét, thiệt hại về người và tài sản — VnExpress"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề thời tiết/thiên tai trung lập (A2), thuần dự báo + khuyến cáo an toàn từ cơ quan chức
  năng, KHÔNG khai thác thương vong cụ thể (không có nạn nhân cá nhân nào được nêu, chỉ nhắc lại
  câu tổng quát 'thiệt hại về người và tài sản' của bão Narra đã qua, đúng nguyên văn nguồn báo, không
  thêm chi tiết). Khác biệt với video đã đăng trước đó cùng chủ đề thời tiết
  (`khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`, đăng 10/9): video cũ là dự báo một vùng áp thấp CÓ
  THỂ hình thành (80%/30-40% xác suất); video này là diễn biến MỚI — áp thấp ĐÃ CHÍNH THỨC hình
  thành sáng 12/9 với vị trí/cấp gió/hướng đi cụ thể, và có góc so sánh riêng với 2 cơn bão gần đây
  (Saudel/Narra) không có trong video cũ — đạt B7 (nguyên bản, không đọc lại tiêu đề báo).

  Style dựng: 3-ticker-tape (index 2, claim_style trả về lúc 2026-09-12T06:28:11.885Z) — dải 'LIVE'
  + dòng feed kiểu terminal (prefix >/+) + mã ngắn 'ATNĐ' trước số liệu + sparkline so sánh 2 cơn bão
  vẽ draw-in. Khác hẳn bố cục style `7-timeline-chronology` đã dùng ở video thời tiết trước.

  Verify 4 bước (PRODUCTION-WORKFLOW.md mục 7) trên file render thật
  output/ap-thap-nhiet-doi-hinh-thanh-bien-dong.mp4:
  (1) ffprobe duration = 68.53s — khớp thiết kế (7 frame data-duration cộng lại 68.51s), dưới mốc 75s.
  (2) ffmpeg silencedetect noise=-35dB:d=0.6 — không phát hiện khoảng lặng chết nào giữa video.
  (3) Trích frame tại t=2s (Hook) và t=67s (CTA) bằng ffmpeg từ chính file .mp4 đã render, xem bằng
  Read — khớp 100% với bản xem trước qua Studio thumbnail: logo + tên kênh + badge nguồn + tiêu đề +
  2 tag hiện đầy đủ, rõ, không mờ/cắt; CTA hiển thị đủ 2 lựa chọn đối lập + pill bình luận + chữ ký.
  (4) Transcript qua Gemini multimodal (gemini-flash-latest, inline_data audio/wav, language tiếng
  Việt) khớp SCRIPT.md gần như nguyên văn — chỉ 1 lỗi phiên âm gần giống chấp nhận được ('Narra' nghe
  thành 'Narda', âm gần giống, không sai cấu trúc/nghĩa câu) — không có câu nào bị 'chế thêm'.

  QC cân bằng dọc (BRAND-SYSTEM.md): đã tự hỏi với mỗi frame 'nửa dưới có trống đen không?' qua ảnh
  Studio thumbnail lẫn frame trích từ file render thật. Phần tử cuối mỗi frame kết thúc trong khoảng
  ước tính 68-88% chiều cao khung (Hook ~79%, What-happened ~79%, Key facts ~76%, Data moment ~80%,
  Context ~80%, Impact ~79%, CTA ~88% chữ ký) — nhất quán với dải phân bố đã chấp nhận ở các video
  trước, không có khoảng trống đen bất thường ở nửa dưới.

  Lint (npm run check): 0 error / 0 warning ở Lint, Runtime, Layout, Motion; Contrast 42/42 text
  checks pass WCAG AA (đã sửa 1 lỗi contrast ban đầu ở caption ảnh trong act What-happened bằng cách
  đổi nền caption sang nền tối đặc thay vì gradient phụ thuộc màu ảnh bên dưới)."
```
