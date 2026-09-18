# COMPLIANCE — cay-dien-cuc-thinh-giac-than-nao-dau-tien-o-viet-nam

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-18T07:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: ""  # chọn từ category=news, không khớp bất kỳ từ khoá nào trong category=trend
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh phòng mổ thật lấy từ ?image=a644b7e1afcf (Tuổi Trẻ, có dẫn nguồn); nhạc Lyria tự sinh (Google Lyria RealTime, calm ambient); SFX bộ repo _reference-astra-openai/assets/sfx/"
claims_verified: [
  "Bệnh viện Nhi Đồng 1 cấy thành công 2 ca cấy điện cực thính giác thân não đầu tiên tại Việt Nam — đối chiếu ?article=a644b7e1afcf",
  "Bé gái 40 tháng tuổi, Hà Nội, không dây thần kinh ốc tai 2 bên — đối chiếu ?article=a644b7e1afcf",
  "Bé trai 19 tháng tuổi, Đồng Nai, không dây thần kinh ốc tai 2 bên — đối chiếu ?article=a644b7e1afcf",
  "Bộ Y tế cho phép thí điểm kỹ thuật từ tháng 12/2025 — đối chiếu ?article=a644b7e1afcf",
  "Ê-kíp đa chuyên khoa + chuyên gia Cộng hòa Liên bang Đức hướng dẫn trực tiếp — đối chiếu ?article=a644b7e1afcf",
  "Hơn 20 năm chương trình can thiệp thính giác trẻ em tại BV Nhi Đồng 1 — đối chiếu ?article=a644b7e1afcf",
  "Hàng trăm ca cấy ốc tai điện tử đã thực hiện trước đó — đối chiếu ?article=a644b7e1afcf",
  "Sau kích hoạt, cả 2 trẻ nhận biết âm thanh môi trường + phản ứng với âm thanh lớn — đối chiếu ?article=a644b7e1afcf"
]
sensitive_flags: ["Tin y tế/trẻ em — chỉ nêu tuổi + tỉnh/thành, không định danh cá nhân, không hình ảnh bệnh nhi, khung tích cực/thành tựu điều trị"]
vietnam_legal_flags: []
notes: "Chủ đề chọn từ category=news (không qua Google Trends) vì phần lớn trending VN ngày 18/9 dính GATE A A1 (drama nghệ sĩ, thể thao nước ngoài không yếu tố VN); 1 chủ đề A2 hợp lệ trong Trends (giá xăng dầu) bị loại do nguồn related mâu thuẫn tăng/giảm cùng ngày, rủi ro B1 cao hơn phương án tin y tế. Transcript verify: bản đầy đủ (gemini-3.6-flash) khớp SCRIPT.md 100% ngoại trừ 1 chi tiết ASR nghe lệch 'tháng 12/2025' thành '2023' ở lần transcribe cả video — đã tách riêng đoạn 27.16s-34.32s (đúng khung voice dòng 4) và transcribe lại độc lập, kết quả đúng 'tháng 12 năm 2025', khớp SCRIPT.md và khớp ElevenLabs STT word-level gốc (line4.stt.json ghi nhận token '12' start=5.42 và '2025' start=6.28) — xác nhận đây là lỗi nghe của Gemini trên clip dài, không phải lỗi trong voice thật."
```

## GATE A — chi tiết
- Quét ~90 từ khoá đầu `category=trend` (162 item, ngày 18/9/2026): phần lớn là đời tư/scandal nghệ sĩ (trấn thành, ngọc trinh, đàm vĩnh hưng, hoài lâm, ninh dương lan ngọc — A1) và thể thao nước ngoài thuần giải trí không yếu tố VN (Premier League, La Liga, Serie A, MLS — A1/YELLOW→bỏ).
- 1 nhóm A2 hợp lệ trong Trends: "giá xăng"/"giá xăng dầu hôm nay"/"giá dầu hôm nay" (traffic 2000+) — nhưng `related` mâu thuẫn ngay trong ngày (Lao Động: "đồng loạt giảm" vs 24h.com.vn/VietNamNet: "trong nước đồng loạt tăng") → rủi ro B1 (sai số liệu) cao, không chọn.
- Chọn từ `category=news`: id `a644b7e1afcf` (Tuổi Trẻ, 18/9/2026) — "Hai trẻ điếc bẩm sinh phức tạp được mở cánh cửa âm thanh nhờ kỹ thuật đầu tiên ở Việt Nam". Khớp A2 "khoa học" + "tin đời sống tích cực". Không dính bất kỳ mục A1 nào.
- `hasImage: true`, ảnh thật ê-kíp phẫu thuật (không có mặt bệnh nhi, không phản cảm).

## GATE B — chi tiết
- B1: mọi số liệu/tên/mốc trong SCRIPT.md + CAPTION.md truy được về bài gốc (`?article=a644b7e1afcf`), không bịa. Không có claim gây tranh cãi cần "cần theo dõi nguồn chính thức" (đây là công bố chính thức của Giám đốc Sở Y tế TP.HCM, đã có kết quả khách quan đo được).
- B2: không bạo lực/thù ghét/quấy rối/nội dung tình dục; không định danh cá nhân trẻ (chỉ tuổi + tỉnh/thành, đúng như bài gốc).
- B3: không giả danh nền tảng/cơ quan/chuyên gia; không testimonial giả; CTA là câu hỏi quan điểm thật, không engagement bait.
- B4: giọng AI narrator chung = GREEN. Ảnh Hook/Article Image Card = ảnh thật từ `?image=`, có dẫn nguồn = GREEN. Không dùng AI tái dựng cảnh thật nào — mọi minh hoạ số liệu (act Data/Context/Impact) là đồ hoạ CSS/SVG ý niệm (số đếm, sparkline, icon mũi tên), không render người/cảnh giả.
- B5: ảnh chỉ từ `?image=`; nhạc Lyria tự sinh (instrumental, có `--negative-prompt` chặn vocal); SFX từ bộ repo có sẵn; video 100% tự dựng.
- B6: tiêu đề "Cấy điện cực thính giác thân não" = đúng sự kiện, không giật gân. Thumbnail phản ánh đúng nội dung (ảnh phòng mổ + tiêu đề + 2 tag đúng thực tế). Caption không nhồi hashtag (7 hashtag liên quan).
- B7: góc nhìn riêng — trình bày dữ liệu qua ẩn dụ "ticker tape" (mã kỹ thuật ABI, feed kết quả, sparkline nền tảng) khác hẳn bố cục video gần nhất (`the-cong-viettel-hoa-melbourne-victory-cup-c2` dùng style `7-timeline-chronology`). Act 7 CTA đặt đúng câu hỏi tranh luận bám sát tin (bước ngoặt y tế hay còn quá hiếm).
- B8: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện — không cần vietnam_legal_flags.

## GATE C — chi tiết
- Thumbnail + các frame render đã xem qua Read: logo, tên kênh, badge nguồn, tiêu đề, 2 tag đều hiện đủ rõ, không mờ/cắt.
- Cân bằng dọc đo bằng PIL trên frame trích từ file .mp4 đã render thật (không chỉ preview): Hook 1555/1920 (81%), What ~1594 (83%), Facts 1559 (81%), Data 1568 (82%), Context 1519 (79%), Impact 1519 (79%), CTA 1697 (88%, khớp precedent template CTA cố định ~1678-1697 đã validate ở video trước).
- Transcript khớp SCRIPT.md (xem notes) — không câu nào "chế thêm".
- Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

## Verify kỹ thuật (5 bước + cân bằng dọc)
1. Duration: 73.10s (thiết kế 73.08s) — dưới trần 75s.
2. Silencedetect (noise=-40dB, d=0.6): không có khoảng lặng chết giữa video (chỉ có ở đúng đoạn fade-out cuối).
3. Loudnorm: bản render gốc đo được -16.8 LUFS / -1.6 dBTP (lệch quá ±1 LU) → chạy `loudnorm` 2-pass (measured từ pass 1) + `alimiter` giới hạn true peak, tái encode audio (giữ nguyên video `-c:v copy`) → kết quả cuối -14.1/-14.2 LUFS, True Peak -1.4 dBTP — đạt chuẩn -14 LUFS ±1 LU, ≤ -1.0 dBTP.
4. Trích frame tại các mốc quan trọng (t=4, 15.5, 26.5, 33.5, 46.5, 60.3, 71) từ chính file .mp4 đã render, xem bằng Read — đúng nội dung, không phần tử bịa, không lỗi hiển thị.
5. Transcript (Gemini `gemini-3.6-flash` — Whisper host bị chặn ở sandbox) khớp SCRIPT.md, xem notes ở trên cho chi tiết đối chiếu chéo 1 nghi vấn đã tự loại trừ.
4b. Cân bằng dọc: đo bằng PIL (scan pixel khác nền `#0B0E14` trong numpy) trên frame trích từ .mp4 thật — xem GATE C.

`npm run check`: 0 error, 0 warning, 80 info (content_overlap kỹ thuật crossfade caption karaoke 0.12s — chủ đích, có `data-layout-allow-overlap`; container_overflow của `#bg-depth .blob` — chủ đích, blob tràn khung theo đúng công thức depth-bg của BRAND-SYSTEM.md). Contrast: 63/63 text checks pass WCAG AA (đã sửa 1 lần — tăng độ tối `.hk-scrim` ở Hook để chữ caption cam đủ tương phản trên ảnh sáng).
