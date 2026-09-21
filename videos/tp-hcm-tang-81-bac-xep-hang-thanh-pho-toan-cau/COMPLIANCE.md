# COMPLIANCE — tp-hcm-tang-81-bac-xep-hang-thanh-pho-toan-cau

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-21T01:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: ""  # chọn từ category=news — xem lý do trong BRIEF.md (khung giờ 21/9/2026, Google Trends VN bị chi phối hoàn toàn bởi thể thao nước ngoài/xổ số/từ khoá rác, không có mục nào đạt A2/A3)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài báo VnExpress Thời sự (assets/img/article-hero.jpg, id 86735e98ade6), flycam TP HCM, có dẫn nguồn trong Hook + Article Image Card; không chỉnh sửa nội dung ảnh; nhạc nền sinh bằng Google Lyria (lyria-recipe.py, calm/instrumental, negative-prompt loại vocal); SFX từ bộ repo chung (assets/sfx); logo public/logo.png và font Montserrat (self-hosted) là tài sản thương hiệu kênh."
claims_verified:
  - "TP HCM xếp hạng 205/1.000 đô thị trong Global Cities Index 2026 của Oxford Economics, đạt 62,6 điểm; năm 2025 xếp thứ 286 → tăng 81 bậc — đối chiếu VnExpress Thời sự (?article=86735e98ade6)."
  - "5 nhóm tiêu chí và điểm 2026: kinh tế 58; nguồn nhân lực 65,7; chất lượng sống 64,4; môi trường 61,7; quản trị 49,7 — nguồn VnExpress Thời sự."
  - "3/5 trụ cột cải thiện: quản trị +194 bậc, nguồn nhân lực +106 bậc, kinh tế +69 bậc; 2 trụ cột đi lùi: chất lượng sống -17 bậc, môi trường -100 bậc — nguồn VnExpress Thời sự."
  - "Trong ASEAN, TP HCM xếp thứ 5 sau Singapore (29), Kuala Lumpur (65), Bangkok (122), Jakarta (140), Manila (174) — nguồn VnExpress Thời sự (nguyên văn từ bài báo, không suy diễn thêm)."
  - "TP HCM được Oxford Economics đưa vào nhóm 'Cities to Watch' khu vực châu Á - Thái Bình Dương — nguồn VnExpress Thời sự."
  - "Mục tiêu công bố chính thức: đến 2030 vào nhóm 100 thành phố toàn cầu; đến 2045 vào nhóm 100 đô thị chất lượng sống tốt nhất thế giới — nguồn VnExpress Thời sự (mục tiêu đã công bố, không phải suy đoán của routine)."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Video tin đô thị/kinh tế tích cực, trung lập (A2), không đụng cá nhân/chính trị/hình sự. Toàn bộ số liệu (điểm số, thứ hạng, delta từng trụ cột, so sánh ASEAN/châu Á, mục tiêu 2030/2045) truy được về bài báo VnExpress Thời sự dùng làm nguồn chính; không có con số nào routine tự nghĩ ra."
```

## Chi tiết kiểm tra

### GATE A — chọn chủ đề
`category=trend` (140 mục, khung 19-20/9/2026) bị chi phối hoàn toàn bởi thể thao nước ngoài thuần
giải trí (Ngoại hạng Anh, Serie A, Bundesliga, La Liga, CONCACAF), xổ số (`xsmb/xsmt/xsmn` — RED, cờ
bạc/tài chính), và từ khoá rác/quá chung chung. Hai mục có yếu tố cá nhân/chính trị bị loại theo A1:
`"phạm nhật vượng"` (đời tư doanh nhân) và `"tập cận bình"` (chính trị/đối ngoại). Không còn mục nào
trong `trend` đạt A2/A3.

Chuyển sang `category=news` (958 mục): loại các mục A1 (hình sự "Bắt khẩn cấp 7 đối tượng...", tai
nạn cá nhân "Nam sinh lớp 10... tử vong", chính trị/đối ngoại Trump/Triều Tiên/Nga-EU, thể thao nước
ngoài thuần giải trí Man Utd/Man City/Liverpool/Real Madrid). Bóng chuyền nữ Asiad 20 đã dựng video
liền trước (`bong-chuyen-nu-viet-nam-tu-ket-asiad-20`), không chọn lại để tránh trùng chủ đề gần nhất.
Chọn **"TP HCM tăng 81 bậc trong bảng xếp hạng thành phố toàn cầu"** (VnExpress Thời sự, id
`86735e98ade6`) — nhóm **A2: "chính sách/kinh tế trung lập: số liệu tăng trưởng, xếp hạng thành phố...
tin đời sống tích cực"**. Bảng xếp hạng độc lập (Oxford Economics, tổ chức nghiên cứu kinh tế Anh),
không liên quan chính trị/nhân sự/bầu cử; nội dung là số liệu đo lường + 1 đạo luật đô thị đã được
Quốc hội thông qua (nêu nội dung quy định, không bình luận chính trị). → **GREEN**.

`trending_signal` để rỗng theo đúng tinh thần mục 1.g ROUTINE.md (chọn từ `category=news`, không qua
Google Trends) — lý do đầy đủ đã ghi trong `BRIEF.md`.

### GATE B — nội dung (SCRIPT.md + CAPTION.md + ảnh, trước render)
- **B1 Sự thật & nguồn**: mọi số liệu (205, 286, 81 bậc, 62,6 điểm, điểm+delta từng nhóm tiêu chí,
  xếp hạng ASEAN, "Cities to Watch", mục tiêu 2030) đều truy được về bài VnExpress Thời sự dùng làm
  nguồn chính. Giữ nguyên lưu ý phương pháp luận của Oxford Economics (thứ hạng giữa các năm "không
  hoàn toàn so sánh trực tiếp") ở act Context, không chốt "tăng 81 bậc" như con số tuyệt đối duy nhất
  — đúng tinh thần "phân biệt cáo buộc/dự đoán vs sự thật" áp dụng cho số liệu có điều kiện.
- **B2 An toàn cộng đồng**: không bạo lực/thù ghét/quấy rối/doxxing/nội dung 18+. Nội dung thuần đô
  thị/kinh tế, không công kích cá nhân/tổ chức.
- **B3 Chính hãng**: kênh không mạo nhận là VnExpress hay Oxford Economics; badge "Nguồn: VnExpress"
  đúng thực tế. Không testimonial/dashboard giả, không engagement bait — CTA là câu hỏi quan điểm thật
  bám sát 2 mặt của tin (tăng hạng thật sự vs cần nhìn 2 mặt tụt hạng).
- **B4 AI/synthetic media**: giọng ElevenLabs "Khánh Lâm" (narrator chung, không giả giọng người
  thật) = GREEN, không cần disclosure. Ảnh Hook + Article Image Card dùng ảnh thật flycam từ bài báo
  (`?image=86735e98ade6`), có dẫn nguồn, không chỉnh sửa nội dung = GREEN. Không có cảnh AI tái dựng
  người/sự kiện thật như ảnh chụp — mọi đồ hoạ khác (icon-grid, biểu đồ cột, thẻ số liệu) là minh hoạ
  ý niệm rõ ràng.
- **B5 Bản quyền**: ảnh chỉ từ `?image=` (không watermark), nhạc Lyria tự sinh (instrumental, có
  negative-prompt loại vocal), SFX từ bộ repo chung, video 100% tự dựng.
- **B6 Tiêu đề/thumbnail**: tiêu đề "TP HCM tăng 81 bậc trong bảng xếp hạng thành phố toàn cầu" = sự
  kiện + số liệu, không giật gân. Thumbnail (Hook, t=3.5s) đã xem lại — logo/tên kênh/badge nguồn/tiêu
  đề "TP.HCM"/2 tag tương phản đều hiện đủ, rõ, không mờ/cắt.
- **B7 Nguyên bản**: góc nhìn riêng — data moment tách "81 bậc" tổng với 2 trụ cột đóng góp chính
  (quản trị +194, nhân lực +106) làm điểm nhấn (thay vì chỉ đọc lại tiêu đề báo); act Context dùng
  lưới icon 5 tiêu chí kiểu dashboard cho góc nhìn "2 chiều" (3 tăng — 2 giảm) mà tiêu đề báo gốc
  không nhấn mạnh; act Impact đối chiếu xếp hạng ASEAN + mục tiêu 2030 đã công bố. Style dựng
  (8-icon-grid, index 7) khác style video liền trước (7-timeline-chronology). CTA đặt câu hỏi tranh
  luận thật ("bước tiến thực chất hay chỉ là con số").
- **B8 Pháp lý VN**: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện —
  không flag.
→ **GREEN**.

### GATE C — kiểm tra cuối (sau render, trước đăng)
- Đã xem lại `output/thumbnail.jpg` + 7 frame trích từ video thật render (cuối animation-reveal của
  từng act: hook t=4.0s, what-happened t=18.5s, key-facts t=26.5s, data-moment t=36.5s, context
  t=51.5s, impact t=64.5s, cta t=73.5s) bằng Read (multimodal): đúng B6, không phần tử bịa, không lỗi
  hiển thị, cân bằng dọc đạt — nội dung mỗi act (bao gồm caption karaoke) lấp gần hết khung, không có
  mảng đen trống lớn ở nửa dưới sau khi mở rộng lưới icon-grid (act Key facts thêm ô "Cities to Watch",
  act Context tăng padding/kích cỡ icon cho 5 ô) và sau khi sửa vị trí caption/chữ ký logo ở act CTA
  (di chuyển caption lên top:1330px để không đè lên chữ ký "Tin Tức Số").
- Transcript: đối chiếu SCRIPT.md với STT gốc từng dòng (ElevenLabs scribe_v1, không lẫn nhạc nền) —
  khớp đủ 7 dòng, không câu nào "chế thêm"; số liệu đọc đúng dạng chữ (viết tắt "205"→"hai trăm linh
  năm", "2026" đọc đúng, không lẫn sang "2024"). Đối chiếu chéo bằng Gemini multimodal
  (`gemini-flash-latest`) trên file voice line1.mp3 riêng lẻ để loại trừ nghi vấn từ "TP" xuất hiện
  trong bản ghi scribe_v1 (xác nhận audio thật đọc đầy đủ "Thành phố Hồ Chí Minh", "TP" chỉ là cách
  scribe_v1 tự chuẩn hoá chữ viết, không phải lỗi phát âm viết tắt).
- Caption dùng để đăng = `CAPTION.md` đã qua GATE B, không sửa tay thêm claim mới.
- Verify kỹ thuật (chạy trực tiếp trên file render thật, không chỉ tin báo cáo dựng video):
  - `ffprobe` duration: **74.568s** (khớp thiết kế `data-duration=74.43` + làm tròn render + xử lý
    audio).
  - `ffmpeg silencedetect -40dB/0.6s`: không phát hiện khoảng lặng chết nào giữa video.
  - `ffmpeg`/`ebur128` loudness: **-14.1 LUFS** integrated, **True Peak -1.3 dBTP** (đạt chuẩn -14
    LUFS ±1 LU, TP ≤ -1.0 dBTP — đã qua loudnorm 2-pass + `alimiter` do bản render gốc đo được -15.4
    LUFS / -0.8 dBTP, lệch quá ngưỡng).
  - 1080×1920, h264/30fps, AAC 192kbps/48kHz→96kHz stereo — đúng chuẩn xuất bản cố định.

**decision: APPROVE — đủ điều kiện đăng Facebook Reel + YouTube Shorts.**
