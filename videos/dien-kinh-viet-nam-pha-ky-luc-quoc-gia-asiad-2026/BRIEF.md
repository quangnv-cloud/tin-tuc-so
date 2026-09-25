# BRIEF — Điền kinh Việt Nam phá kỷ lục quốc gia, giành HCĐ Asiad 2026

Video tin nóng/trending kênh "Tin Tức Số" (khung 25/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kết quả thể thao có yếu tố VN** (điền kinh Việt Nam tại Asiad 2026, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá `"điền kinh"`, id `84853dd907c6`, `trafficApprox` **"200+"**,
  `pubDate` 2026-09-24T22:20:00Z. `related` trỏ 3 báo VN uy tín cùng chủ đề (VietNamNet, Tuổi Trẻ,
  Lao Động) — đều nói về tổ điền kinh Việt Nam giành HCĐ 4x400m tại Asiad 2026.
- Từ khoá liên quan `"huy chương"`, id `c48e27f2d0e8`, `trafficApprox` **"1000+"**, cùng khung giờ,
  `related` cũng nhắc đến huy chương đồng của điền kinh Việt Nam ngày 24/9 — củng cố đây là chủ đề
  đang trending thật, không chỉ 1 nguồn đơn lẻ.
- `GET ?category=news` có bài đúng chủ đề, đầy đủ chi tiết, ảnh chuẩn báo (không phải thumbnail
  Google nhỏ): **VnExpress Thể thao**, id `3d12d82ae54b`, "Điền kinh Việt Nam phá kỷ lục quốc gia ở
  ASIAD 2026", pubDate 2026-09-24T14:31:40Z → dùng `id` này cho cả `?article=` và `?image=`.
- **Nguồn thật dùng để dựng**: VnExpress Thể thao (KHÔNG ghi "Google Trends" là nguồn).
- Đã POST đánh dấu used: `{"id":"3d12d82ae54b","video":"dien-kinh-viet-nam-pha-ky-luc-quoc-gia-asiad-2026"}`.
- `claim_style` → `index: 4`, `style: "5-map-and-geo"` — khớp tự nhiên vì cuộc đua có yếu tố địa lý
  rõ: tổ chức tại Nhật Bản (chủ nhà Asiad 2026), tranh chấp huy chương giữa nhiều quốc gia châu Á
  (Bahrain, Ấn Độ, Trung Quốc, Nhật Bản, Hàn Quốc, Philippines, UAE), và bảng tổng sắp huy chương
  theo quốc gia.

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước) — tường thuật kết
quả, số liệu." Đây là đoàn thể thao Việt Nam thi đấu tại đại hội thể thao châu Á chính thức (Asiad
2026), thành tích tích cực (huy chương + kỷ lục quốc gia), không đụng đời tư vận động viên, không có
yếu tố hình sự/chính trị/cá độ, không khai thác đau thương. Tường thuật kết quả + số liệu, trung lập,
không giật gân. → **GREEN, APPROVE để dựng**.

(Đã lướt và LOẠI các chủ đề trending khác cùng khung giờ trước khi chọn: phần lớn đầu danh sách
`trend` là bóng đá châu Âu thuần giải trí không yếu tố VN — Nations League (Bồ Đào Nha, Hà Lan, Đức,
Áo, Hy Lạp, Na Uy...), Cristiano Ronaldo, Erling Haaland, Bruno Fernandes (A1, BỎ — thể thao nước
ngoài không yếu tố VN); "trần lưu quang" — tên một lãnh đạo, dính yếu tố chính trị/nhân sự (A1, BỎ);
"lan hương như cố" — nghi liên quan nghệ sĩ, có thể là tin đồn/đời tư (A1, BỎ); "nguyễn đình bắc" —
tin về một cầu thủ bị VFF kỷ luật vì lối chơi bạo lực, liên quan cá nhân + bạo lực sân cỏ, rủi ro B2
(A1-adjacent, BỎ); "phanh xe" — tin tài xế cá nhân bị phạt vì lỗi giao thông, nêu đích danh cá nhân
(BỎ); "xổ số" — không phù hợp brand (BỎ). "điền kinh"/"huy chương" đạt cả 2 tiêu chí: đang trending
+ có báo chính thống đưa tin đầy đủ + ảnh chuẩn, đúng nhóm A2 ưu tiên nhất.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Nội dung: tiếp sức 4x400m hỗn hợp nam nữ, môn điền kinh, Asiad 2026 (Đại hội Thể thao châu Á lần
  thứ 20), thi đấu tại sân vận động Paloma Mizuho, Nhật Bản (chủ nhà Aichi-Nagoya 2026 — xác nhận qua
  banner trong ảnh báo).
- Đội hình Việt Nam (thứ tự chạy): Tạ Ngọc Tưởng, Quách Thị Lan, Lê Ngọc Phúc, Nguyễn Thị Ngọc.
- Đối thủ cùng đợt chạy: Bahrain (đương kim vô địch Á vận hội), Ấn Độ, Nhật Bản, Trung Quốc, Hàn
  Quốc, Philippines, Các Tiểu Vương quốc Ả Rập Thống nhất (UAE).
- Diễn biến: UAE dẫn đầu sau 800m đầu; Lê Ngọc Phúc bứt tốc vươn lên dẫn đầu ở 400m tiếp theo (trao
  gậy sau 2 phút 22 giây 29); Nguyễn Thị Ngọc giữ khoảng cách tốt ở 100m kế nhưng bị vận động viên
  Bahrain (Abdullah Aisha) và Ấn Độ (Vithya Ramraj) vượt qua ở đoạn nước rút cuối.
- Kết quả: Bahrain về nhất, lập kỷ lục Á vận hội mới 3 phút 12 giây 87 (nhanh hơn kỷ lục cũ do chính
  họ lập năm 2023 tới 1 giây 15); Ấn Độ về nhì với 3 phút 14 giây 46; Việt Nam về ba, giành HC đồng
  với 3 phút 14 giây 54 — phá kỷ lục quốc gia cũ 3 phút 15 giây 7 (lập khi giành HCV SEA Games 33 ở
  Thái Lan, đội hình khi đó có Ngọc, Phúc, Tưởng và Nguyễn Thị Hằng thay cho Lan).
- Đây là huy chương đầu tiên của điền kinh Việt Nam tại Asiad 2026. Đoàn điền kinh Việt Nam có 25
  VĐV, tranh 16/50 nội dung, mục tiêu 1 HCV - 1 HCB - 1 HCĐ.
- Bảng tổng sắp huy chương (tính đến thời điểm bài viết): Việt Nam xếp thứ 20 với 1 HCV, 1 HCB, 15
  HCĐ. Trung Quốc dẫn đầu (80-30-20), Nhật Bản thứ nhì (20-34-37), Hàn Quốc thứ ba (10-12-28).
- Các nội dung điền kinh khác cùng ngày: Vũ Thị Ngọc Hà hạng 9 nhảy ba bước nữ (13,13m); Nguyễn Thị
  Oanh hạng 6 (33 phút 34 giây 92) và Lê Thị Tuyết Mai hạng 13 (38 phút 0 giây 87) ở 10.000m nữ —
  KHÔNG đưa vào SCRIPT.md vì act đã đủ 7 dòng, giữ lại làm ngữ cảnh dự phòng nếu cần.
- Đối chiếu chéo: khớp với `related` của trending item "điền kinh" (VietNamNet, Tuổi Trẻ, Lao Động)
  và "huy chương" (24h, Thanh Niên, VietNamNet) — cùng số liệu HCĐ 4x400m ngày 24/9.

## Ảnh (bước 5 ROUTINE.md)

`?image=3d12d82ae54b` trả về ảnh định dạng `webp` (1200×720) — đã convert sang `.jpg` thật bằng
ffmpeg (không đổi nội dung, chỉ đổi container) tại `assets/img/article-hero.jpg`. Ảnh thật: 4 vận
động viên đội tiếp sức (áo đỏ, số 7) cầm cờ Tổ quốc ăn mừng trên sân, nền có banner "Aichi-Nagoya
2026" — ảnh og:image bài báo, có dẫn nguồn, đúng B4 (GREEN, không cần disclosure).

## Style dựng: 5-map-and-geo

Ẩn dụ bản đồ/địa lý xuyên suốt 5 act giữa:
- **What happened**: ảnh + panel chuẩn, badge nguồn đổi thành huy hiệu tròn viền cam bao icon quốc kỳ
  nhỏ, thêm ghim địa danh "Nhật Bản — Aichi-Nagoya 2026" cạnh badge.
- **Key facts**: bản đồ outline châu Á mờ phía sau danh sách 2-3 fact (đội hình + diễn biến), fact có
  yếu tố quốc gia (Bahrain, Ấn Độ, UAE) gắn icon ghim nhỏ.
- **Data moment**: con số 3 phút 14 giây 54 phóng to trong 1 map-pin cách điệu tại vị trí Nhật Bản
  trên bản đồ châu Á, pin drop-in trước khi số count-up.
- **Context**: bản đồ châu Á với 3 vùng/nước highlight tuần tự theo thứ hạng cuộc đua — Bahrain (vàng
  cam đậm nhất), Ấn Độ, Việt Nam — đường nối từ mỗi nước ra nhãn thời gian về đích.
- **Impact**: 2 thẻ địa danh trượt vào từ 2 hướng trên nền bản đồ mờ full-frame — thẻ trái "Việt Nam
  — hạng 20 toàn đoàn (1-1-15)", thẻ phải nhóm dẫn đầu "Trung Quốc — Nhật Bản — Hàn Quốc".

## GATE B — tự kiểm nhanh (chi tiết đầy đủ ở bước riêng trước khi render)

- B1: mọi số liệu/tên/mốc trong SCRIPT + CAPTION đều truy được về `?article=3d12d82ae54b` (xem mục
  claims_verified). Không có số liệu tự nghĩ.
- B2/B3/B5: không bạo lực/thù ghét/doxxing; không giả danh; ảnh từ `?image=` có dẫn nguồn; nhạc Lyria
  tự sinh (bước 8).
- B6: tiêu đề = sự kiện + số liệu (kỷ lục quốc gia, HCĐ), không giật gân.
- B7: góc nhìn riêng — đặt kết quả trong bối cảnh bảng tổng sắp huy chương toàn đoàn (không chỉ đọc
  lại tiêu đề báo), style bản đồ chưa dùng ở video nào trước đó trong kênh.
- B8: không chạm vấn đề pháp lý VN.
