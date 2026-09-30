# COMPLIANCE — tuoi-nghi-huu-2027-thay-doi

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-16T07:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "bảo hiểm xã hội" (Google Trends VN, id d08ce802734d, vị trí #1/142 trong danh sách
  category=trend lúc chạy routine, trafficApprox "2000+", pubDate 2026-09-16T05:20:00.000Z)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero (assets/img/article-hero.jpg) là ảnh báo chí thật lấy qua
  ?image=0e2bfb2595f7 (Dân Trí, bài 'Đóng bảo hiểm xã hội tự nguyện 17 năm, xin hưởng lương hưu sớm
  được không?'), gốc 1280x853 jpg, không chỉnh sửa nội dung ảnh, cảnh cán bộ bảo hiểm xã hội tư vấn
  người dân — minh hoạ đúng chủ đề tổng quát, không gắn với số liệu cụ thể nào trong video nên không
  gây hiểu sai. Nguồn hiển thị trên video (Brand Anchor + Hook badge + CAPTION) = 'Dân Trí' (khớp
  nguồn ảnh, tránh lệch nguồn hiển thị). Nhạc nền sinh qua Google Lyria (lyria-recipe.py, calm
  ambient, negative-prompt loại vocal/drum), đã xác minh 100% không lời bằng Gemini multimodal
  (gemini-flash-lite-latest) trước khi dùng — độ dài gốc bị giới hạn ~62-64s do timeout API, đã nối
  dài an toàn bằng kỹ thuật crossfade-loop (ffmpeg acrossfade, đoạn lặp lấy từ chính bản nhạc, không
  lấy từ nguồn khác) để đạt đủ 67.76s + fade-out. SFX từ bộ có sẵn trong repo
  (videos/_reference-astra-openai/assets/sfx, không đổi tốc độ/pitch). Giọng đọc ElevenLabs 'Khánh
  Lâm' (RCmOaM1iiIH5xX3QXjIF, eleven_v3) — AI narrator chung, không giả giọng người thật cụ thể."
claims_verified:
  - "Từ năm 2027, tuổi nghỉ hưu điều chỉnh theo lộ trình Bộ luật Lao động 2019: lao động nam tăng
    thêm 3 tháng, lao động nữ tăng thêm 4 tháng so với năm 2026 — Thanh Niên (?article=d08ce802734d,
    related[0]) + xác nhận độc lập bởi Dân Trí (0e2bfb2595f7, mục 'Tuổi nghỉ hưu của người lao động
    năm 2027 thay đổi ra sao?')"
  - "Năm 2027: lao động nam nghỉ hưu khi đủ 61 tuổi 9 tháng; lao động nữ nghỉ hưu khi đủ 57 tuổi 4
    tháng — Thanh Niên"
  - "Lộ trình tăng dần dừng lại khi nam đạt 62 tuổi (năm 2028), nữ đạt 60 tuổi (năm 2035) — Thanh Niên"
  - "Điều kiện hưởng lương hưu (Luật Bảo hiểm xã hội 2024, hiệu lực 1/7/2025): đủ tuổi nghỉ hưu +
    đóng bảo hiểm xã hội bắt buộc từ đủ 15 năm trở lên — Thanh Niên; xác nhận độc lập bởi Dân Trí
    (trích Điều 98 Luật Bảo hiểm xã hội, Khoản 2 Điều 169 Bộ luật Lao động, Nghị định 159/2025/NĐ-CP)"
  - "Người làm nghề nặng nhọc/độc hại/nguy hiểm hoặc làm việc ở vùng có điều kiện kinh tế - xã hội
    đặc biệt khó khăn: nghỉ hưu sớm hơn tối đa 5 năm — Thanh Niên"
  - "Người khai thác than trong hầm lò, đủ 15 năm làm nghề: nghỉ hưu sớm hơn tối đa 10 năm — Thanh Niên"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chính sách lao động/bảo hiểm xã hội đã ban hành theo lộ trình có sẵn (Bộ luật Lao động 2019,
  Luật Bảo hiểm xã hội 2024) — KHÔNG phải đề xuất/tranh cãi mới, KHÔNG đụng cá nhân/chính trị. Loại
  bỏ khỏi video chi tiết 'Bộ Nội vụ đề xuất tăng tuổi nghỉ hưu công chức lên 70' (chỉ là đề xuất tham
  khảo kinh nghiệm nước ngoài, chưa ban hành) để tránh nhầm giữa đề xuất và quy định đã có hiệu lực
  (đúng B1). Đối chiếu độc lập 2 nguồn (Thanh Niên chủ đạo + Dân Trí xác nhận số liệu và trích dẫn
  điều luật cụ thể) cho mọi claim chính — không số liệu nào routine tự nghĩ ra.
  Góc nhìn riêng (B7): tổng hợp 3 lớp thông tin từ luật (mốc tuổi cụ thể theo giới tính, điều kiện số
  năm đóng bảo hiểm xã hội, các trường hợp ngoại lệ nghỉ hưu sớm theo nghề/vùng) thành 1 bức tranh đầy
  đủ hơn từng bài hỏi-đáp đơn lẻ trên báo; mỗi act giữa bám đúng số liệu của dòng thoại riêng act đó
  (không lặp/lấn số liệu act khác). Style dựng 5-map-and-geo (index 4, claim_style) — CHƯA từng dùng ở
  8 video trước (khác hẳn style 1-card-and-bar của video liền trước mien-bac-mua-lon-ngap-ha-noi) —
  diễn giải ẩn dụ bản đồ qua phạm vi áp dụng toàn quốc (Hook/What happened), 'hành trình' 2 điều kiện
  tới lương hưu trên trục dọc kiểu waypoint (Context), và bản đồ mờ + 2 thẻ trượt vào cho ngoại lệ
  nghỉ hưu sớm theo nghề/vùng (Impact) — KHÔNG bịa thêm tên tỉnh/vùng cụ thể không có trong nguồn.
  Bug thật phát hiện + đã sửa trong QC: (1) số '62' trong map-pin ở act Data moment ban đầu render
  cực nhỏ, méo hướng do quên counter-rotate phần tử con ngược chiều rotate(-45deg) của pin — đã thêm
  transform:rotate(45deg) cho .dm-pin-inner; xác nhận lại bằng thumbnail Studio thấy số hiện đúng cỡ
  156px, đứng thẳng, đọc rõ. (2) span số đếm #dm-num dùng id nhưng CSS chỉ định nghĩa qua class
  .dm-num (thiếu class= trên phần tử) khiến style không áp dụng — đã thêm class=\"dm-num\" vào span.
  (3) bản đồ SVG nền mờ ở act Key facts và act Impact bị 2 card đặc che gần hết, chỉ lộ 1 mảnh tam
  giác nâu kỳ lạ ở khe hở giữa 2 card — gây rối mắt, không đọc được là bản đồ — đã bỏ hẳn lớp bản đồ ở
  2 act này (giữ pin icon trên mỗi card + radial glow trang trí thay thế), ẩn dụ Map & Geo vẫn được
  giữ đủ qua Hook/What/Data/Context/Impact.
  Vertical-balance QC: đo bằng script PIL/numpy quét hàng pixel cuối cùng khác nền #0B0E14 trên 8
  frame trích từ file .mp4 đã render (không chỉ xem ảnh preview nén) — Hook 1428px (74%), What
  1479px (77%), Key facts 1499px (78%), Data moment 1494px (78%), Context 1442px (75%), Impact
  1474px (77%) — đều trong dải 1400-1680px yêu cầu; CTA 1757px (91%, chữ ký logo gần đáy, đúng thiết
  kế cố định của act CTA, khớp tiền lệ 87% của video trước).
  Verify 5 bước (mục 7 PRODUCTION-WORKFLOW.md): (1) ffprobe duration 67.766667s khớp thiết kế 67.76s;
  (2) silencedetect noise=-40dB:d=0.6 không phát hiện khoảng lặng chết nào trong toàn video; (3)
  loudnorm — bản render gốc đo được -15.3 LUFS integrated / -1.4 dBTP (lệch quá ±1 LU so với -14.0) →
  đã chạy loudnorm 2-pass (measured_I=-15.3, measured_TP=-1.4, measured_LRA=2.6, target I=-14,
  TP=-1.5 để chừa dư địa cho AAC re-encode) trên file render gốc, tái đo độc lập bằng ffmpeg loudnorm
  lần 2 xác nhận Input Integrated -14.4 LUFS / True Peak -1.4 dBTP — đạt cả 2 chuẩn; (4) trích 8 frame
  ở nhiều mốc mỗi act, xem bằng Read — đúng thiết kế, phát hiện + sửa 3 bug ở trên trước khi chốt; (5)
  transcript qua Gemini multimodal (gemini-flash-lite-latest) khớp 100% với SCRIPT.md, không câu nào
  bịa thêm, không đọc tên kênh 'Tin Tức Số' trong lời thoại, các năm (2027/2019/2028/2035) được viết
  đầy đủ bằng chữ trong SCRIPT.md nên đọc chuẩn không lắp/ê a. Thumbnail (output/thumbnail.jpg, trích
  t=3.5s) xem lại bằng Read — logo, tên kênh, badge nguồn, tiêu đề, 2 tag đều hiện đủ rõ, không mờ."
```
