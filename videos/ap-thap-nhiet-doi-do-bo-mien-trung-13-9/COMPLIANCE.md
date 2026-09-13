# COMPLIANCE — ap-thap-nhiet-doi-do-bo-mien-trung-13-9

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-13T07:03:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "dự báo áp thấp nhiệt đới — vị trí #4/-- trong danh sách Google Trends VN lúc phát hiện (id 6263156ab6f7), trafficApprox 1000+, pubDate 2026-09-13T04:20:00Z. Chủ đề xuất hiện ở CẢ category=trend ('dự báo áp thấp nhiệt đới') VÀ category=news (nhiều bài đưa tin áp thấp nhiệt đới cùng ngày trên cả VnExpress/Tuổi Trẻ/Dân Trí). Nhóm A2 (thời tiết/thiên tai/cảnh báo cộng đồng, đưa mức thông tin + khuyến cáo an toàn, dẫn nguồn cơ quan chức năng, KHÔNG khai thác thương vong) → GREEN, không dính A1 (không có thông tin thương vong cá nhân trong nguồn, chỉ thiệt hại vật chất do cơ quan chức năng công bố)."
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh bài VnExpress (id ffdf62b4a88d, ?image= endpoint, chuyển webp gốc sang jpg), có dẫn nguồn 'Nguồn: VnExpress · 13/9/2026' trong Brand Anchor/Hook badge — không chỉnh sửa nội dung ảnh, không tái dựng cảnh thật bằng AI. 5 act giữa (What/Facts/Data/Context/Impact) dùng đồ hoạ ring-progress/biểu tượng tự vẽ (HTML/CSS/SVG), không phải ảnh AI mô phỏng người/sự kiện thật. Nhạc nền do Lyria tự sinh (instrumental, không lời), đã áp `data-fx-carve` (carve theo voiceover, strength 0.4) + EQ/automation retrim theo đúng tổng thời lượng thật (68.21s), data-volume 0.30. SFX từ thư viện repo (chime/click-soft/impact-bass-1/pop/whoosh-short), không đổi tốc độ/pitch để né Content ID. Giọng đọc ElevenLabs 'Khánh Lâm' — AI narrator chung, không giả giọng người thật cụ thể, không cần disclosure."
claims_verified:
  - "Tâm áp thấp nhiệt đới 7h ngày 13/9 trên vùng biển Quảng Trị - Huế, cách Huế khoảng 100km — đối chiếu ?article=ffdf62b4a88d (VnExpress) và ?article=fe29aaeaeb17 (Tuổi Trẻ, mốc 4h sáng cùng ngày, chênh lệch nhỏ do khác mốc giờ đã ghi rõ trong BRIEF)"
  - "Sức gió mạnh nhất 49 km/h, cấp 6, giật cấp 8; di chuyển hướng tây tây bắc, tốc độ 10-15 km/h — đối chiếu ?article=ffdf62b4a88d"
  - "Duy trì cường độ trên đất liền Hà Tĩnh và phía bắc Quảng Trị đến sáng 14/9 rồi mới suy yếu — đối chiếu ?article=ffdf62b4a88d"
  - "Mưa Hà Tĩnh đến Huế phổ biến 100-200mm, cục bộ có nơi trên 350mm (mức cơ quan khí tượng xếp diện mưa rất to); Thanh Hóa - Nghệ An 40-70mm, cục bộ trên 150mm — đối chiếu ?article=ffdf62b4a88d"
  - "Nguy cơ lũ sông Ngàn Sâu, Ngàn Phố (Hà Tĩnh) lên báo động 2-3 — đối chiếu ?article=ffdf62b4a88d"
  - "Đến 6h ngày 13/9 (theo Cục Quản lý đê điều và Phòng, chống thiên tai): Quảng Trị có 10 điểm đường/cầu tràn ngập chia cắt cục bộ; Đà Nẵng sơ tán 101 hộ dân nguy cơ sạt lở; Huế có 2 điểm sạt lở trên quốc lộ 49 khoảng 150 m3 đất đá — đối chiếu ?article=ffdf62b4a88d. Đây là số liệu ĐÃ XẢY RA (Act 6 Impact), không phải suy đoán tương lai."
sensitive_flags: []
vietnam_legal_flags:
  - "Tin thời tiết/thiên tai — chỉ tường thuật số liệu dự báo (Trung tâm Dự báo KTTV quốc gia) và thiệt hại/ứng phó đã công bố (Cục Quản lý đê điều và PCTT), không suy đoán vượt nguồn, không đưa số liệu thương vong cá nhân, không bịa cấp độ rủi ro thiên tai. Không thuộc diện quảng cáo có điều kiện."
notes: |
  Nội dung sản xuất bởi routine tự động "Tin Tức Số". Chủ đề trùng cả category=trend ("dự báo áp
  thấp nhiệt đới") và category=news (VnExpress/Tuổi Trẻ/Dân Trí cùng đưa); nguồn thật chốt là
  VnExpress (id ffdf62b4a88d, KHÔNG ghi "Google Trends" là nguồn), đối chiếu chéo Tuổi Trẻ
  (fe29aaeaeb17). Style đã claim qua Apps Script: index 5 = "6-ring-progress". Góc nhìn riêng (B7):
  tổng hợp toàn bộ dữ liệu thành "bảng đo mức độ ảnh hưởng" theo khu vực (gió — mưa — lũ — thiệt hại
  đã ghi nhận) bằng vòng radial thay vì chỉ đọc lại tiêu đề báo; khác cách dựng với 2 video gần nhất
  cùng chủ đề thời tiết (index 6 "7-timeline-chronology", ngày 10/9) và video gần nhất nói chung
  (index 3 "4-split-comparison", ngày 13/9).

  Verify kỹ thuật (4 bước, đều đạt) trên bản render CUỐI CÙNG (sau khi sửa layout, xem mục "Vấn đề
  phát hiện và đã sửa" bên dưới):
  1) ffprobe duration = 68.233s (thiết kế 68.21s, dưới 75s) — khớp.
  2) ffmpeg silencedetect noise=-35dB:d=0.6 — CHỈ có 1 khoảng lặng tại 67.359s→68.224s (đúng đoạn
     fade-out cuối act CTA sau khi voice + nhạc kết thúc), KHÔNG có khoảng lặng chết giữa video.
  3) Trích frame tại t=3, 5.5, 10, 14, 20, 25, 32, 35, 40, 45, 47, 52, 56.5, 62, 65, 67 (trải đều cả
     7 act) — xem bằng Read: brand đúng (#FF5A1F/#0B0E14, logo Tin Tức Số góc trên-phải, "Nguồn:
     VnExpress · 13/9/2026" góc trên-trái/badge Hook), ring-progress tô đúng màu cam/đỏ theo đúng
     Style 6, không phần tử bịa, không emoji trong composition. Act 7 CTA dùng đúng mẫu
     `_reference-astra-openai/07-cta.html` (đổi màu cam) theo đúng quy định.
  4) Transcript (Gemini multimodal, model `gemini-flash-lite-latest` → trả về `gemini-3.5-flash-lite`
     — Whisper cài được nhưng model host bị chặn/hỏng checksum qua proxy sandbox) khớp SCRIPT.md sát
     nghĩa từng câu (số liệu Gemini normalize thành chữ số "49 km/h" thay vì đọc-lại "bốn mươi chín"
     chỉ là cách hiển thị transcript, giọng đọc gốc vẫn đọc đúng số như trong SCRIPT.md), không có
     câu nào bị "chế thêm", không lỗi đọc lắp do viết tắt (SCRIPT.md không dùng viết tắt).

  Vấn đề phát hiện và đã sửa (bước verify 4 bước, mục 3 — cân bằng dọc):
  - Bản render ĐẦU TIÊN (trước phiên này) có lỗi bố cục: 3/7 act (02-what, 04-data, 05-context) đặt
    dòng chú thích/caption cuối act ở vị trí `top` cố định quá thấp (1560px/1610px/1620px trên canvas
    1920px), tạo khoảng đen chết ~350-430px giữa nội dung chính và caption — vi phạm quy tắc "cân
    bằng dọc, không trống đen nửa dưới". Đã sửa tối thiểu: đưa `top` của `.wh-sub` (02-what),
    `.dm-caption` (04-data), `.cx-foot` (05-context) lên sát dưới khối nội dung chính (1200px/1310px/
    1260px) — chỉ đổi vị trí caption, không đổi nội dung/số liệu/timing giọng đọc. Re-render lại toàn
    bộ, verify lại đủ 4 bước trên bản mới — đạt. 4 act còn lại (01-hook, 03-facts, 06-impact,
    07-cta) đã cân bằng tốt ngay từ đầu, không cần sửa.
  - Lưu ý vận hành: trong lúc sửa, phát hiện một tiến trình render nền còn sót lại từ phiên trước
    (container được resume) đã ghi đè 3 file composition trên về nội dung gốc (chưa sửa) ngay sau khi
    sửa lần 1 — đã phát hiện qua re-đọc file, chờ tiến trình đó kết thúc hẳn (không còn process
    hyperframes/chrome-headless/npm run render nào chạy), áp lại đúng 3 chỉnh sửa, render lại lần 2,
    và xác nhận lại toàn bộ (checksum + trích frame) trước khi coi là bản cuối cùng.

  npm run check (sau khi sửa): 0 errors/0 warnings (Lint), 1 warning Runtime không liên quan
  (el-voice-2: data-duration 10.37s vs audio thật 10.32s, lệch 0.05s không đáng kể, không ảnh hưởng
  nội dung/hình ảnh), Layout 0 issues/9 samples, Motion 0/0, Contrast 37/37 WCAG AA pass.

  Thumbnail (`output/thumbnail.jpg`, trích tại t=3.5s trong cửa sổ Hook, sau khi toàn bộ animation
  Hook đã ổn định lúc ~2.28s): xem bằng Read — logo + tên kênh "Tin Tức Số", badge nguồn "Nguồn:
  VnExpress · 13/9/2026", tiêu đề "Áp thấp nhiệt đới / áp sát miền Trung", và 2 tag tương phản "Gió
  giật cấp 8" (trắng) + "Mưa lớn diện rộng" (cam/đỏ) đều hiện rõ, sắc nét, không mờ, không chồng lấp.
