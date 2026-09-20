# COMPLIANCE — vinfast-vf-wild-ra-mat-gia-860-trieu

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-20T01:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "vf wild" (Google Trends VN, vị trí ~77/184, trafficApprox 5000+, cũng xuất hiện ở category=news)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh sản phẩm chính thức VinFast lấy từ ?image=220e0c3f140f (Dân Trí, 1355x903, không watermark, có dẫn nguồn); nhạc Lyria tự sinh (Google Lyria RealTime, calm ambient, negative-prompt chặn vocal); SFX bộ repo videos/_reference-astra-openai/assets/sfx/"
claims_verified: [
  "VinFast ra mắt VF Wild sáng 19/9/2026, mẫu bán tải đầu tiên của hãng — đối chiếu ?article=220e0c3f140f",
  "Giá 860 triệu đồng (đen/đỏ/trắng), 872 triệu đồng (bạc) — đối chiếu ?article=220e0c3f140f",
  "Đặt cọc sớm 25-30/9/2026 giảm 61 triệu đồng, còn 799 triệu đồng — đối chiếu ?article=220e0c3f140f",
  "Pin LFP 46,4kWh, chạy điện thuần hơn 250km theo chuẩn NEDC — đối chiếu ?article=220e0c3f140f",
  "Động cơ xăng 1,5L chỉ phát điện sạc pin (không dẫn động bánh xe), tổng quãng đường mỗi lần nạp hơn 1.000km — đối chiếu ?article=220e0c3f140f",
  "Công nghệ REEV/EREV, không phụ thuộc hoàn toàn hạ tầng trạm sạc công cộng — đối chiếu ?article=220e0c3f140f",
  "Từng là concept tại CES 2024 (Las Vegas, Mỹ), triết lý thiết kế Fluid Dynamism lấy cảm hứng áo choàng tung bay — đối chiếu ?article=220e0c3f140f",
  "Kích thước 5.376 x 2.069 x 1.873 (mm), trục cơ sở 3.258mm, thùng 1.574 x 1.512 x 509 (mm), tải trọng 750kg — đối chiếu ?article=220e0c3f140f",
  "Cửa thùng mở bằng khí nén, màn hình cảm ứng 10 inch — đối chiếu ?article=220e0c3f140f",
  "Cạnh tranh với Ford Ranger, Toyota Hilux, Mitsubishi Triton, Nissan Navara, Isuzu D-Max — đối chiếu ?article=220e0c3f140f"
]
sensitive_flags: ["Trending keyword đi kèm 'phạm nhật vượng' trong cùng cụm Google Trends nhưng video KHÔNG đề cập/khai thác cá nhân — chỉ nói về sản phẩm VF Wild, xác nhận vẫn thuộc A2"]
vietnam_legal_flags: []
notes: "Phát hiện lúc dựng: ElevenLabs Scribe (STT dùng để lấy timestamp caption karaoke) liên tục nghe nhầm 'VF Wild' thành 'VF 6'/'VF Fly'/'VFY' (thiên kiến mô hình về các tên gọi model VinFast có thật). Đã test chéo bằng Gemini multimodal trên các đoạn audio cô lập ('VinFast VF Wild vừa ra mắt tại Việt Nam') — Gemini nghe đúng 'VF Wild' cả 3 lần thử với các cách viết khác nhau, xác nhận đây là lỗi thiên kiến của Scribe khi transcribe, KHÔNG phải lỗi phát âm của giọng đọc ElevenLabs. Do đó karaoke caption dùng timestamp Scribe nhưng hiển thị đúng text gốc SCRIPT.md (kỹ thuật tương tự merge-group override đã dùng ở video trước cho số liệu bị tách âm). Transcript verify cuối cùng bằng Gemini trên toàn bộ audio thật của video khớp 100% với SCRIPT.md, bao gồm đúng 'VF Wild' ở mọi lần xuất hiện — xác nhận giọng đọc phát âm đúng. Lỗi cân bằng dọc phát hiện ở frame Hook lúc kiểm tra ban đầu (nội dung dồn lên ~1160px, để trống ~40% khung dưới) đã sửa bằng cách đổi hk-panel sang justify-content:center, verify lại bằng frame trích từ file .mp4 đã render lại — nội dung kết thúc tại 1606px, trong dải 1400-1680px yêu cầu."
```

## GATE A — chi tiết
- Từ khoá trending "vf wild" (Google Trends VN, vị trí ~77/184, trafficApprox 5000+), cũng xuất hiện ở `category=news`. Từ khoá liên quan "phạm nhật vượng" xuất hiện trong cùng cụm nhưng câu chuyện thực chất 100% về sản phẩm VinFast VF Wild — video không đề cập cá nhân này.
- Khớp nhóm A2 "ra mắt sản phẩm/xe" — ô tô mới ra mắt chính thức tại VN, giá công bố chính thức, thông số kỹ thuật khách quan từ nguồn báo chính thống (Dân Trí).
- Không dính bất kỳ mục A1 nào: không đời tư/scandal, không hình sự, không chính trị, không thể thao nước ngoài, không tài chính/tiền số, không 18+/cờ bạc, không thuyết âm mưu, không khai thác trẻ em.
- `hasImage: true` — ảnh sản phẩm thật do VinFast/Dân Trí đăng, không watermark, không có người, không vấn đề bản quyền/logo.

## GATE B — chi tiết
- B1: mọi số liệu/tên/mốc trong SCRIPT.md + CAPTION.md truy được về bài gốc `?article=220e0c3f140f` (Dân Trí), không bịa. Điểm nhấn "chỉ ~250km đầu là điện thuần, phần còn lại nhờ máy phát xăng" được trình bày trung thực với vạch đánh dấu 25% trên ring — không đánh đồng cả 1.000km là chạy điện.
- B2: không bạo lực/thù ghét/quấy rối/nội dung tình dục; không nhắm vào cá nhân, chỉ nói về sản phẩm và công nghệ.
- B3: không giả danh VinFast hay bất kỳ hãng/cơ quan nào; kênh "Tin Tức Số" là nguồn tin độc lập; không testimonial giả; CTA là câu hỏi quan điểm thật (REEV có phải bước đi khôn ngoan), không engagement bait.
- B4: giọng AI narrator chung (ElevenLabs "Khánh Lâm") = GREEN, không cần disclosure. Ảnh Hook/Article Image Card = ảnh thật từ `?image=`, có dẫn nguồn = GREEN. Không dùng AI tái dựng cảnh thật nào — mọi minh hoạ số liệu (ring radial, chip đối thủ) là đồ hoạ CSS/SVG ý niệm.
- B5: ảnh chỉ từ `?image=220e0c3f140f`; nhạc Lyria tự sinh (instrumental, `--negative-prompt` chặn vocal); SFX từ bộ repo có sẵn; video 100% tự dựng, không reup.
- B6: tiêu đề "VinFast VF Wild ra mắt: bán tải đầu tiên, giá từ 860 triệu đồng" = đúng sự kiện + số liệu chính, không giật gân. Thumbnail (frame Hook) phản ánh đúng nội dung — logo, tên kênh, badge nguồn, tiêu đề, 2 tag đều hiện rõ. Caption không nhồi hashtag (7 hashtag liên quan).
- B7 (nguyên bản — rủi ro cao nhất): góc nhìn riêng — không chỉ đọc lại tiêu đề báo mà phân tích sâu vào công nghệ REEV và tính trung thực của con số "hơn 1.000km" (chỉ 25% là điện thuần). Ẩn dụ "ring progress" (index 5) khác hẳn style video gần nhất (`cay-dien-cuc-thinh-giac-than-nao-dau-tien-o-viet-nam` dùng `3-ticker-tape`). Act 7 CTA đặt đúng câu hỏi tranh luận bám sát tin (REEV: khôn ngoan hay chưa đủ).
- B8: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện — không cần vietnam_legal_flags.

## GATE C — chi tiết
- Thumbnail + các frame render (đã trích từ file .mp4 đã render thật, xem qua Read): logo, tên kênh, badge nguồn, tiêu đề "VINFAST / VF WILD", 2 tag ("Bán tải đầu tiên" / "Có động cơ xăng") đều hiện đủ, rõ, không mờ/cắt.
- Cân bằng dọc đo bằng PIL (scan pixel khác nền `#0B0E14`) trên frame trích từ .mp4 đã render lại sau khi sửa:
  - Hook (t=3.5s): 1606/1920 (84%) — đã sửa từ lỗi ban đầu (nội dung dừng ở ~1160px, để trống gần 40% khung dưới) bằng cách đổi `.hk-panel` sang `justify-content: center`.
  - What happened (t=16.3s, cuối act): nội dung kết thúc quanh 1570px (đo bằng mắt qua ảnh — `wt-foot` tại top:1530px).
  - Key facts (t=23.9s, cuối reveal): 1467/1920 (76%).
  - Data moment (t=30.7s, cuối reveal): 1501/1920 (78%).
  - Context (t=41.9s, cuối reveal): 1503/1920 (78%).
  - Impact (t=51.9s, cuối reveal): 1497/1920 (78%).
  - CTA (t=63.6s): 1719/1920 (90%) — khớp mẫu CTA cố định của brand (chữ ký logo neo gần đáy, đã validate ở video trước).
  - Tất cả đều trong hoặc vượt dải `top: 1400-1680px` yêu cầu — không còn mảng đen trống nửa dưới khung.
- Transcript (Gemini `gemini-flash-latest`) trên toàn bộ audio thật khớp 100% với SCRIPT.md, không câu nào "chế thêm" khi sinh voice — bao gồm đúng "VF Wild" ở mọi lần xuất hiện.
- Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

## Verify kỹ thuật (5 bước + cân bằng dọc)
1. Duration: 72.40s (thiết kế 72.37s) — dưới trần 75s.
2. Silencedetect (noise=-40dB, d=0.6): không phát hiện khoảng lặng chết nào trong toàn bộ video.
3. Loudnorm: bản render gốc đo được -15.7 LUFS / -1.5 dBTP (lệch quá ±1 LU so với -14.0) → chạy `loudnorm` 2-pass (measured từ pass 1, `linear=true`) + giữ nguyên video (`-c:v copy`), tái encode audio AAC 192kbps → kết quả cuối -14.1 LUFS, True Peak -0.8 dBTP — đạt chuẩn -14 LUFS ±1 LU, ≤ -1.0 dBTP.
4. Trích frame tại các mốc quan trọng (t=3.5, 16.3, 23.9, 30.7, 41.9, 51.9, 63.6) từ chính file .mp4 đã render, xem bằng Read — đúng nội dung, không phần tử bịa, không lỗi hiển thị, không watermark/logo lạ.
5. Transcript (Gemini `gemini-flash-latest` — Whisper host `openaipublic.azureedge.net` không khả dụng trong sandbox) khớp 100% SCRIPT.md.
4b. Cân bằng dọc: đo bằng PIL (numpy, quét pixel khác nền `#0B0E14`) trên frame trích từ .mp4 render thật — xem chi tiết ở GATE C. Phát hiện + sửa 1 lỗi ở Hook (frame duy nhất bị lỗi), verify lại xác nhận đã đạt.

`npm run check`: 0 error, 2 warning (chấp nhận được — `gsap_infinite_repeat` tại root index.html cho hiệu ứng blob/sao trôi nền liên tục, đúng công thức bắt buộc của BRAND-SYSTEM.md mục "Nền có chiều sâu"; `clip_media_fit` lệch ~0.05s giữa data-duration khai báo và độ dài audio thật đo bởi hyperframes — không đáng kể, slot tự co về đúng độ dài media khi render). Layout: 0 error, 0 warning, 80 info sau khi thêm `data-layout-allow-overflow` cho 3 blob nền (tràn khung theo đúng công thức depth-bg của BRAND-SYSTEM.md — chủ đích) và giữ nguyên `data-layout-allow-overlap` sẵn có cho caption karaoke (crossfade 0.12s giữa các chunk — chủ đích). Contrast: 74/74 text checks pass WCAG AA (đã sửa 1 lần — tăng độ tối `.hk-scrim` ở Hook để chữ caption cam đủ tương phản trên ảnh sáng).
