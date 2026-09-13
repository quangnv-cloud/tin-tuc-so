# COMPLIANCE — ap-thap-nhiet-doi-do-bo-mien-trung-13-9

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-13T06:52:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "dự báo áp thấp nhiệt đới — vị trí #4 trong danh sách trending, trafficApprox 1000+, pubDate 2026-09-13T04:20:00Z. Chủ đề xuất hiện ở CẢ category=trend (từ khoá 'dự báo áp thấp nhiệt đới', id 6263156ab6f7) VÀ category=news (nhiều bài đưa tin áp thấp nhiệt đới cùng ngày trên VnExpress/Tuổi Trẻ/Dân Trí) — ưu tiên theo mục 1.c ROUTINE.md."
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh bài báo VnExpress (id ffdf62b4a88d, ?image= endpoint), có dẫn nguồn 'Nguồn: VnExpress' trong Brand Anchor + badge Hook — không chỉnh sửa nội dung ảnh (chỉ chuyển định dạng webp gốc sang jpg thật, không thêm/bớt yếu tố). Nhạc nền do Google Lyria tự sinh qua lyria-recipe.py (instrumental, không lời, --negative-prompt loại vocals/lyrics/singing/... đã áp dụng), retrim đúng tổng thời lượng thật (68.21s) + fade-in 1.5s/fade-out 3s. SFX từ thư viện repo (chime/click-soft/impact-bass-1/pop/whoosh-short), không đổi tốc độ/pitch để né Content ID. Giọng đọc ElevenLabs 'Khánh Lâm - tin tức, thời sự' (voice_id RCmOaM1iiIH5xX3QXjIF, model eleven_v3) — AI narrator chung của kênh, không giả giọng người thật cụ thể, không cần disclosure. Không dùng asset nào khác ngoài repo/API đã cấu hình."
claims_verified:
  - "Lúc 7h ngày 13/9, tâm áp thấp nhiệt đới trên vùng biển Quảng Trị - Huế, cách Huế khoảng 100km về phía bắc đông bắc, cách Quảng Trị khoảng 170km về phía đông đông nam — đối chiếu ?article=ffdf62b4a88d (VnExpress) và ?article=fe29aaeaeb17 (Tuổi Trẻ, mốc 4h sáng cùng ngày, chênh lệch nhỏ do khác mốc giờ, đã ghi 'khoảng')"
  - "Sức gió mạnh nhất 49 km/h, cấp 6, giật cấp 8; di chuyển hướng tây tây bắc, tốc độ 10-15 km/h — đối chiếu ?article=ffdf62b4a88d"
  - "Giữ nguyên cường độ trên đất liền Hà Tĩnh và phía bắc Quảng Trị đến 7h ngày 14/9 rồi suy yếu thành vùng áp thấp ở Trung Lào — đối chiếu ?article=ffdf62b4a88d"
  - "Mưa Hà Tĩnh đến Huế phổ biến 100-200mm, cục bộ có nơi trên 350mm, mức cơ quan khí tượng xếp vào diện mưa rất to — đối chiếu ?article=ffdf62b4a88d"
  - "Thanh Hóa, Nghệ An mưa 40-70mm, cục bộ trên 150mm; nguy cơ lũ sông Ngàn Sâu, Ngàn Phố lên báo động 2-3 — đối chiếu ?article=ffdf62b4a88d"
  - "Đến 6h ngày 13/9 (Cục Quản lý đê điều và Phòng, chống thiên tai): Quảng Trị có 10 điểm đường/cầu/ngầm tràn bị ngập, chia cắt cục bộ; Đà Nẵng sơ tán 101 hộ có nguy cơ sạt lở; Huế có 2 vị trí trên quốc lộ 49 sạt lở khoảng 150 m3 đất đá — đối chiếu ?article=ffdf62b4a88d"
sensitive_flags:
  - "Thời tiết/thiên tai (nhóm A2) — chỉ đưa mức thông tin dự báo + khuyến cáo/thiệt hại vật chất (ngập đường, sạt lở, sơ tán phòng ngừa) đã được cơ quan chức năng công bố; KHÔNG có số liệu thương vong cá nhân trong nguồn, KHÔNG khai thác đau thương, không giật tít."
vietnam_legal_flags: []
notes: |
  Nội dung sản xuất tiếp nối từ 1 phiên trước đã hoàn tất GATE A (chọn chủ đề + claim style qua Apps
  Script API, index 5 = "6-ring-progress") và soạn BRIEF.md/SCRIPT.md/CAPTION.md/ảnh bài báo. Phiên
  này thực hiện các bước 5-13 của ROUTINE.md: khởi tạo project qua `hyperframes init` (không copy
  state cũ), sinh giọng đọc, dựng 7 act, BGM + carve, lint, render, verify, thumbnail, GATE B/C,
  COMPLIANCE.md, cập nhật style-rotation-state.json, commit.

  Góc nhìn riêng (B7): thay vì chỉ đọc lại tiêu đề báo, video tổng hợp toàn bộ dữ liệu khí tượng
  (gió, mưa, báo động lũ, thiệt hại) thành "bảng đo mức độ" bằng vòng radial (ẩn dụ trung tâm của
  style 6-ring-progress) — mỗi mức độ (cấp gió Beaufort, ngưỡng mưa rất to, báo động lũ 1-2-3, số
  điểm ngập/hộ sơ tán) được trực quan hoá bằng 1 vòng tròn riêng, giúp người xem hình dung nhanh mức
  độ nghiêm trọng theo từng khu vực thay vì chỉ nghe số liệu rời rạc.

  Act 6 (Impact) chỉ dùng 2 con số ĐÃ XẢY RA thật (10 điểm ngập tại Quảng Trị; 101 hộ dân Đà Nẵng đã
  sơ tán), không suy đoán tương lai — đúng yêu cầu brand.

  Verify kỹ thuật (4 bước, đều đạt):
  1) ffprobe duration = 68.233333s (thiết kế 68.21s, dưới trần 75s) — khớp.
  2) ffmpeg silencedetect noise=-35dB:d=0.6 — CHỈ có 1 khoảng lặng tại 67.36s→68.22s (đúng đoạn
     fade-out cuối act CTA sau khi voice + nhạc kết thúc), KHÔNG có khoảng lặng chết giữa video.
  3) Trích frame gần CUỐI mỗi act bằng ffmpeg (t=5.9/16.6/28.0/36.3/47.9/57.5/63.3/67.5s tương ứng
     Hook/What/Facts/Data/Context/Impact/CTA-giữa/CTA-cuối) rồi đo bằng PIL/numpy (hàng pixel cuối
     cùng khác màu nền #0B0E14): Hook 1697px (88,4%), What 1651px (86,0%), Facts 1603px (83,5%),
     Data 1648px (85,8%), Context 1656px (86,2%), CTA 1699px (88,5%) — toàn bộ đạt/vượt dải an toàn
     1400-1680px yêu cầu, không trống đen nửa dưới khung ở bất kỳ act nào. Act Impact xem bằng mắt
     (radial-gradient nền khiến phép đo tự động không đáng tin ở act này) xác nhận nội dung (2 vòng
     radial 10/101 + dòng chú thích Huế) lấp gần hết nửa dưới khung, không có khoảng trống bất
     thường. Cả 7 frame đều đúng brand (#FF5A1F/#0B0E14/#FF4438, logo + "Tin Tức Số" góc trên-phải,
     "Nguồn: VnExpress" góc trên-trái), không phần tử bịa, không emoji trong composition, ẩn dụ vòng
     radial nhất quán xuyên suốt 5 act giữa đúng style đã claim.
  4) Transcript (Gemini multimodal, model gemini-flash-latest — thử cài Whisper cục bộ bị timeout
     nên chuyển sang Gemini theo đúng phương án dự phòng của ROUTINE.md) khớp SCRIPT.md từng câu,
     từng số liệu (100km, 49km/h cấp 6 giật cấp 8, 10-15km/h, 350mm, 40-70mm/150mm, báo động 2-3,
     10 điểm ngập, 101 hộ sơ tán) — không có câu nào bị "chế thêm", không lỗi đọc lắp/đánh vần do
     viết tắt lọt vào SCRIPT.md (SCRIPT.md đã viết đầy đủ số theo cách đọc tiếng Việt ngay từ đầu).

  npm run check: 0 errors, 1 warning benign (clip_media_fit trên el-voice-2: chênh lệch ~0,05s giữa
  data-duration khai báo và độ dài PCM thực của mp3 do đệm encoder — không ảnh hưởng render/verify).
  Layout 0 issues/9 samples, Motion 0 errors/0 warnings, Contrast 37/37 WCAG AA pass.

  Thumbnail: trích tại t=3,5s (trong cửa sổ Hook 3-5s, sau khi mốc tween trễ nhất của Hook — tag2
  "Mưa lớn diện rộng" tại 1,92s+0,36s=2,28s — đã ổn định). Xem lại bằng Read: logo + "Tin Tức Số"
  góc trên-phải, badge "Nguồn: VnExpress · 13/9/2026", tiêu đề "Áp thấp nhiệt đới áp sát miền Trung"
  và 2 tag tương phản "Gió giật cấp 8" / "Mưa lớn diện rộng" đều hiện đủ, rõ nét, không cắt/mờ.

  Deviation theo chỉ đạo phiên này (ghi lại để minh bạch, KHÔNG phải lỗi quy trình): routine gốc ở
  bước 13-15 yêu cầu push lên nhánh `master` của <REPO> rồi đăng Facebook Reel + YouTube Shorts từ
  URL raw.githubusercontent.com của nhánh đó. Phiên làm việc này vận hành dưới chính sách git bắt
  buộc chỉ được commit/push vào nhánh `claude/wizardly-shannon-x2qmib`, KHÔNG được push `master` hay
  mở PR nếu không có con người chỉ định rõ ràng. Do đó: đã commit + push đầy đủ toàn bộ sản phẩm
  (BRIEF/SCRIPT/CAPTION/COMPLIANCE, assets, compositions, index.html, output/*.mp4,
  output/thumbnail.jpg) lên nhánh `claude/wizardly-shannon-x2qmib`; KHÔNG push `master`; KHÔNG gọi
  publish_facebook / publish_youtube (các endpoint đó cần video đã live trên URL raw.githubusercontent
  của nhánh master, chưa hội đủ điều kiện); KHÔNG mở pull request. Việc đăng Facebook/YouTube được
  giữ lại chờ con người cấp phép push master một cách tường minh.
