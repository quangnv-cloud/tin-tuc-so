# COMPLIANCE — mua-lon-bac-bo-den-nghe-an

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-15T00:55:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "dự báo thời tiết hà nội (Google Trends VN, vị trí #1/201 trong danh sách category=trend
  sắp mới nhất trước, id 935867005e9e, trafficApprox 5000+, pubDate 2026-09-14T23:30:00Z); related của
  chính item trỏ thẳng tới bài Tuổi Trẻ 'Thời tiết hôm nay 15-9: Bắc Bộ đến Nghệ An mưa rất to' — trùng
  khớp với item category=news id 8d2b6ee83739 cùng chủ đề, cùng thời điểm — xác nhận vừa đang trending
  vừa đã có báo chính thống đưa tin."
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh Hook/Article Image Card lấy từ ?image=8d2b6ee83739 (og:image bài Tuổi Trẻ, ảnh
  thật người dân đi xe máy trong mưa, có dẫn nguồn Tuổi Trẻ ở Brand Anchor + badge Hook, không
  watermark ngoài của báo gốc); nhạc nền sinh riêng bằng Google Lyria (lyria-recipe.py, recipe calm,
  density 0.25 / brightness 0.4, negative-prompt loại vocal/nhịp mạnh), retrim 57.46s + fade in/out,
  carve.mjs strength 0.4 duck dưới voice; SFX từ bộ palette chung của kênh
  (impact-bass-1/whoosh-short/pop/click-soft/chime); giọng đọc ElevenLabs eleven_v3, voice Khánh Lâm.
claims_verified:
  - "Từ 15/9 đến 16/9, đồng bằng Bắc Bộ, Bắc Ninh, Phú Thọ, Thanh Hoá mưa to đến rất to, lượng mưa
    100-250mm, có nơi trên 400mm — Tuổi Trẻ (?article=8d2b6ee83739) + Dân Trí (?article=00b155749ce3),
    số liệu khớp 2 nguồn."
  - "Hưng Yên, Ninh Bình lượng mưa 200-400mm, có nơi trên 500mm (mức cao nhất đợt này) — Tuổi Trẻ +
    Dân Trí, khớp 2 nguồn (dùng mốc chung 'trên 500mm' thay vì số lẻ 550mm chỉ 1 nguồn nêu)."
  - "Lạng Sơn, bắc Phú Thọ, nam Thái Nguyên/Tuyên Quang/Sơn La/Lào Cai, Nghệ An mưa vừa đến to, có nơi
    rất to, lượng mưa 80-170mm, có nơi trên 300mm — Tuổi Trẻ."
  - "Đỉnh lũ sông Bôi (Phú Thọ), sông Hoàng Long (Ninh Bình), thượng lưu sông Bưởi/Mã/Chu (Thanh Hoá)
    khả năng lên báo động 1-2, có sông vượt báo động 2 (không nêu tên sông cụ thể vượt vì nguồn không
    xác định rõ — tránh bịa); thượng lưu sông Cả (Nghệ An) khả năng vượt báo động 1 — Tuổi Trẻ + Dân Trí."
  - "Nguy cơ cao ngập lụt vùng trũng thấp ven sông, khu đô thị, sạt lở đất sườn dốc tại Phú Thọ, Ninh
    Bình, Thanh Hoá, Nghệ An — Tuổi Trẻ + Dân Trí."
  - "Cảnh báo mưa cường độ lớn trên 100mm/3 giờ, dông kèm nguy cơ lốc, sét, mưa đá, gió giật mạnh —
    Tuổi Trẻ."
  - "Nguyên nhân: hoàn lưu sau áp thấp nhiệt đới kết hợp dải hội tụ nhiệt đới — Tuổi Trẻ."
sensitive_flags: ["Thiên tai/thời tiết — đưa mức thông tin dự báo + khuyến cáo an toàn, dẫn nguồn cơ
  quan khí tượng quốc gia, không khai thác thương vong/thiệt hại cụ thể nào (video không dùng bất kỳ
  số liệu thiệt hại người/tài sản nào, chỉ nêu dự báo và cảnh báo nguy cơ)."]
vietnam_legal_flags: []
notes: "Verify 4 bước: (1) ffprobe duration 57.466667s khớp thiết kế 57.46s. (2) ffmpeg silencedetect
  -35dB/0.6s: không phát hiện khoảng lặng chết. (3) Trích 7 frame từ file .mp4 đã render (t=3.5/10/22/
  30/38/45/53s) — xem bằng Read, đúng bố cục/màu/cân bằng dọc, không phần tử bịa. (4) Transcript: Gemini
  API (generativelanguage.googleapis.com) trả lỗi 429 quota exceeded liên tục (đã thử model
  gemini-flash-latest theo đúng GET /v1beta/models, retry có backoff) — chuyển sang Whisper (host
  openaipublic.azureedge.net không bị chặn ở sandbox này) model small, language Vietnamese. Transcript
  khớp SCRIPT.md cả 7 dòng, chỉ lệch âm gần giống do chất lượng ASR tiếng Việt của Whisper (vd 'Nghệ An'
  nghe thành 'Lệ An', 'diện rộng' thành 'diện rộng'/'diện dọc' tuỳ lần chạy) — không có câu nào sai cấu
  trúc/nghĩa, không phát hiện lỗi đọc lắp/đánh vần do viết tắt lọt vào SCRIPT.md. Whisper có hallucinate
  thêm 1 câu 'Hãy subscribe cho kênh Ghiền Mì Gõ...' ở mốc 57.44-61.44s — mốc này VƯỢT QUÁ độ dài file
  audio.wav thực tế (57.47s), tự chứng minh đây là ảo giác ASR khi gặp đoạn chỉ còn nhạc nền (BGM) sau
  khi voice7 đã dứt lúc ~53.7s, không phải nội dung thật trong video (kênh không tồn tại tên đó, và
  SCRIPT.md/CAPTION.md tuyệt đối không nhắc tên kênh nào khác lẫn không có lời kêu gọi subscribe).
  Thumbnail (t=3.5s, trong cửa sổ Hook, sau khi animation ổn định ở ~2.24s): logo + tên kênh + badge
  nguồn + tiêu đề + 2 tag tương phản đều hiện đủ, rõ, không mờ/cắt."
```
