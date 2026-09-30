# COMPLIANCE — doi-tuyen-viet-nam-cong-bo-danh-sach-asean-cup-2026

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-19T07:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "danh sách đội tuyển việt nam — trafficApprox 1000+, vị trí #98/180 danh sách trend hôm nay (Google Trends VN)"
GATE B (content):   GREEN-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Báo Dân Trí (id news 288df262e098, 2560x1706, có dẫn nguồn Nguồn: Dân Trí trên brand anchor); nhạc nền Lyria tự sinh qua Google Lyria RealTime (calm ambient, không lời, negative-prompt vocals/lyrics/singing/choir/rap/spoken-word/humming); SFX từ bộ palette repo videos/_reference-astra-openai/assets/sfx/; composition 100% tự dựng (HTML/CSS/GSAP), không reup/cắt ghép video kênh khác."
claims_verified:
  - "Sáng 18/9, huấn luyện viên Kim Sang Sik công bố danh sách 23 cầu thủ dự FIFA ASEAN Cup — khớp ?article=288df262e098 (Dân Trí)"
  - "2 tân binh Việt kiều lần đầu triệu tập: Adou Minh (Nguyễn Adou Leygley Minh, trung vệ, Việt kiều Pháp, câu lạc bộ Công An Hà Nội, đã có kinh nghiệm V-League) và Williams Minh Hoàng (hậu vệ, Việt kiều Anh, cao 1m90, câu lạc bộ Công An TP.HCM) — khớp ?article="
  - "Vắng: thủ môn Văn Lâm, hậu vệ Đoàn Văn Hậu, Nguyễn Văn Vĩ (chấn thương), Đinh Quang Kiệt, Nguyễn Trần Việt Cường, Nguyễn Ngọc Mỹ; Quang Kiệt/Ngọc Mỹ đang dự Asiad cùng U23 — khớp ?article=, KHÔNG gán lý do chấn thương/Asiad cho Văn Lâm/Văn Hậu (nguồn không nêu lý do 2 người này, đã sửa ở bước GATE B1)"
  - "Bảng B, Division 1, đối thủ Thái Lan/Philippines/Pakistan — khớp ?article="
  - "Lịch: Philippines 26/9 (19h30, sân Si Jalak Harupat, Bandung, Indonesia), Thái Lan 29/9, Pakistan 2/10 — khớp ?article="
  - "Đối chiếu 2 nguồn: tiêu đề VnExpress 'Văn Hậu, Văn Lâm không dự FIFA ASEAN Cup 2026' + Tuổi Trẻ 'Huấn luyện viên Kim Sang Sik gọi 2 cầu thủ Việt kiều Pháp và Anh lên tuyển Việt Nam' trong related của item trend — khớp nội dung chính"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề thể thao thuần tuý đội tuyển quốc gia (A2), không đụng đời tư/hình sự/chính trị. Style dựng 5-map-and-geo (claim_style index 4) diễn giải qua ẩn dụ bảng đấu khu vực (đối thủ + lịch thi đấu + xuất xứ 2 tân binh) — khác biệt rõ với 2 video gần nhất (7-timeline-chronology, 3-ticker-tape), đạt B7 nguyên bản."
```

## GATE A — chi tiết

Nhóm **A2 — kết quả/tin thể thao có yếu tố VN** (đội tuyển quốc gia Việt Nam). Tin công bố danh sách
triệu tập, hoàn toàn trung lập: không đời tư, không hình sự, không chính trị. Lý do vắng mặt nêu trong
nguồn (chấn thương Văn Vĩ, trùng lịch Asiad của Quang Kiệt/Ngọc Mỹ) là thông tin thể thao thuần tuý,
không phải scandal. → GREEN, APPROVE để dựng. Chi tiết các chủ đề trending khác đã lướt qua và loại ở
GATE A: xem `BRIEF.md` mục "GATE A — đánh giá".

## GATE B — chi tiết theo checklist COMPLIANCE-GATE.md

- **B1 (sự thật & nguồn)**: mọi số liệu/tên/mốc thời gian trong SCRIPT.md + CAPTION.md truy được về
  `?article=288df262e098`. Phát hiện 1 lỗi khi soát lần đầu — script gán nhầm lý do "chấn thương và
  trùng lịch Á vận hội" cho cả Văn Lâm lẫn Đoàn Văn Hậu trong khi nguồn chỉ nêu lý do cho Văn Vĩ/Quang
  Kiệt/Ngọc Mỹ — đã sửa lại SCRIPT.md dòng 6 và CAPTION.md trước khi sinh giọng đọc, không còn gán lý
  do không có nguồn. Không có claim tranh cãi cần khung "cần theo dõi nguồn chính thức".
- **B2 (an toàn cộng đồng)**: không bạo lực/thù ghét/quấy rối/doxxing/nội dung tình dục. Nêu cầu thủ
  vắng mặt theo đúng lý do thể thao trung lập trong nguồn, không suy diễn tiêu cực.
- **B3 (chính hãng & liêm chính)**: kênh không mạo nhận VFF/FIFA/báo chí; không testimonial giả; CTA
  là câu hỏi quan điểm thật, không engagement bait; không link/lừa đảo trong caption.
- **B4 (AI/synthetic media)**: giọng ElevenLabs "Khánh Lâm" = GREEN không cần disclosure. Ảnh Hook +
  Article Image Card dùng ảnh thật từ `?image=288df262e098` (og:image Dân Trí, có dẫn nguồn) = GREEN.
  Đồ hoạ minh hoạ (globe/orbit outline, map-pin, thẻ dữ liệu) hoàn toàn là biểu tượng/sơ đồ trừu tượng,
  KHÔNG tái dựng cảnh thật/người thật như ảnh chụp = GREEN, không cần disclosure.
- **B5 (bản quyền)**: ảnh có dẫn nguồn; nhạc Lyria tự sinh; SFX repo; video tự dựng 100%.
- **B6 (tiêu đề/thumbnail)**: tiêu đề "Đội tuyển Việt Nam chốt danh sách 23 cầu thủ dự FIFA ASEAN Cup"
  = sự kiện + số liệu, không giật gân. Thumbnail (frame Hook, t=3.5s) hiện đủ rõ logo, tên kênh, badge
  nguồn, tiêu đề, 2 tag tương phản — đã xem lại bằng Read, không mờ/cắt. Caption không nhồi hashtag
  (3 brand + 4 chủ đề).
- **B7 (nguyên bản)**: góc nhìn riêng — khung "bảng đấu khu vực" (đối thủ theo địa lý + lịch thi đấu
  dồn dập 3 trận/7 ngày) thay vì chỉ đọc lại tiêu đề báo; style 5-map-and-geo chưa dùng ở 2 video gần
  nhất. Act 7 CTA đặt đúng câu hỏi tranh luận bám tin (tăng cường Việt kiều).
- **B8 (pháp lý VN)**: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện.

## GATE C — chi tiết

- Xem lại thumbnail + 8 frame render thật (t=4s, 8s, 13s, 17.5s, 27.5s, 35.5s, 47.5s, 58s, 59.3s, 68s,
  72s — bao gồm mốc cuối animation-reveal mỗi act giữa và mốc smash-cut act Impact): đúng B6, không
  phần tử bịa, không lộ lỗi render, cân bằng dọc đạt (phần tử cuối mỗi act kết thúc trong khoảng
  top 1350-1510px, không trống đen nửa dưới).
- Transcript (Gemini `gemini-flash-latest`, whisper host bị chặn nên dùng fallback) khớp hoàn toàn
  SCRIPT.md — không câu nào "chế thêm" khi sinh giọng đọc. Sai khác duy nhất là cách phiên âm số/tên
  riêng của máy STT (không phải lỗi đọc: "Kim Sang-sik" thay vì "Kim Sang Sik", "1,90 m" thay vì "một
  mét chín mươi") — chấp nhận được theo hướng dẫn "nhầm âm gần giống chấp nhận được".
- Caption dùng để đăng = CAPTION.md đã qua GATE B (đã sửa B1, đã cắt bản Threads về 487 ký tự).

**Verify 5 bước file render thật**: (1) duration 74.63s/74.70s < 75s ✓; (2) silencedetect noise=-40dB
d=0.6 → không phát hiện khoảng lặng chết ✓; (3) loudnorm — bản render gốc đo được -16.5 LUFS, ngoài
ngưỡng ±1 LU so với -14.0 → đã chạy `loudnorm` 2-pass (measured_I=-16.5, measured_TP=-1.6,
measured_LRA=2.5, measured_thresh=-26.6) → kết quả cuối **-14.0 LUFS, True Peak -1.0 dBTP** ✓ đúng
chuẩn; (4) trích 8 frame ở mốc quan trọng + mốc cuối reveal mỗi act, xem bằng Read — đạt; (5) transcript
Gemini khớp SCRIPT.md — đạt.

**Quyết định**: decision = APPROVE, risk_level = GREEN → đủ điều kiện commit + push + đăng Facebook/YouTube.
