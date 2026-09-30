# BRIEF — Mưa lớn diện rộng Bắc Bộ - Nghệ An, cảnh báo lũ và sạt lở

Video tin nóng/trending kênh "Tin Tức Số". Chủ đề phát hiện từ Google Trends VN
("dự báo thời tiết hà nội"), đối chiếu với tin nóng trang chủ báo lớn, QUA GATE A nhóm **A2 — thời
tiết/thiên tai đưa trung lập, khuyến cáo an toàn** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"dự báo thời tiết hà nội"**, id `935867005e9e`, vị trí **#1/201**
  trong danh sách (sắp mới nhất trước), `trafficApprox` **"5000+"**, `pubDate` 2026-09-14T23:30:00Z.
  `related` của chính item này trỏ tới 3 bài: Lao Động "Dự báo thời tiết 10 ngày tới", Tuổi Trẻ
  "Thời tiết hôm nay 15-9: Bắc Bộ đến Nghệ An mưa rất to", VnExpress "Mưa lớn dịch chuyển ra Bắc Bộ,
  Bắc Trung Bộ" — đúng chủ đề, không cần suy diễn.
- `GET ?category=news`: có bài đúng chủ đề từ Tuổi Trẻ (id `8d2b6ee83739`, "Thời tiết hôm nay 15-9:
  Bắc Bộ đến Nghệ An mưa rất to", trùng khớp với `related` của item trending) — xác nhận đây vừa
  đang trending vừa đã có báo chính thống đưa tin cùng thời điểm.
- Đối chiếu nguồn thứ 2: **Dân Trí**, id `00b155749ce3` — "Hà Nội mưa rất to, miền Bắc nhiều nơi
  nguy cơ ngập lụt" — cùng trích dẫn Trung tâm Dự báo khí tượng thuỷ văn quốc gia, số liệu khớp với
  Tuổi Trẻ (100-250mm có nơi trên 400mm; 200-400mm cục bộ trên 500mm; nguy cơ lũ trên các sông Bắc Bộ,
  Thanh Hoá, Nghệ An lên báo động 1-2).
- Đã POST đánh dấu `used` cho id `935867005e9e` (video: `mua-lon-bac-bo-den-nghe-an`).
- **Nguồn chính thức dùng cho video: Tuổi Trẻ** (id `8d2b6ee83739`) — KHÔNG ghi "Google Trends" là
  nguồn, Trends chỉ là công cụ phát hiện chủ đề.
- Ảnh minh hoạ: `?image=8d2b6ee83739` — ảnh báo Tuổi Trẻ, người đi xe máy mặc áo mưa giữa trời mưa
  lớn, ảnh thật/tài liệu báo chí, có dẫn nguồn, không watermark ngoài của báo gốc, 1200x749, `ok:true`.

## GATE A

Nhóm **A2 — GREEN**: thời tiết/cảnh báo cộng đồng, đưa mức thông tin dự báo + khuyến cáo an toàn,
dẫn nguồn cơ quan chức năng (Trung tâm Dự báo khí tượng thuỷ văn quốc gia), KHÔNG khai thác thương
vong (video chỉ nêu dự báo/cảnh báo nguy cơ ngập lụt, sạt lở — chưa có số liệu thiệt hại người/tài
sản cụ thể nào được đưa vào script). Không đụng đời tư, không hình sự, không chính trị, không thể
thao — an toàn để dựng.

Các chủ đề trending khác đã xét và loại ở GATE A (ghi lại để minh bạch, quét top ~100/201 item mới
nhất trong `category=trend` ngày 2026-09-14/15):
- "trương mỹ lan" (traffic 1000-2000+) — cáo buộc hình sự/đang xét xử một cá nhân → bỏ theo A1.
- Hàng loạt trận đấu bóng đá nước ngoài thuần giải trí không yếu tố VN: "leeds – newcastle",
  "inter milan", "villarreal đấu với betis", "brest vs psg", "man utd đấu với man city",
  "levante đấu với barcelona", "câu lạc bộ bóng đá al nassr", "bảng xếp hạng ngoại hạng anh"… → bỏ
  theo A1 (thể thao nước ngoài, không VĐV/đội tuyển VN).
- "xổ số miền bắc/trung/nam" (traffic 200000-500000+, cao nhất danh sách) — kết quả xổ số, nhạy cảm
  cờ bạc/không mang giá trị tin tức xây dựng → bỏ.
- "binance exchange" / "binance buy crypto" / "bitcoin" — tài chính tiền số, rủi ro nhóm "kèo"/đầu cơ
  theo GATE A → bỏ theo A1.
- "hoài linh", "dakota johnson", "kwon eun-bi", "nhã phương", "trấn thành", "jisoo" — đời tư/tin giải
  trí cá nhân nghệ sĩ, không phải sự kiện nghề nghiệp trung lập rõ ràng → bỏ theo A1.
- "tô lâm" — chính trị/nhân sự cấp cao → bỏ theo A1.
- "vụ khủng bố ngày 11 9" — bạo lực nghiêm trọng/nhạy cảm lịch sử → bỏ theo A1.
- "ukraina", "houthis", "niger" — xung đột vũ trang/đối ngoại → bỏ theo A1.
- "đội tuyển bóng đá nữ quốc gia việt nam", "u-23 việt nam" (traffic thấp hơn, chưa có bài
  `category=news` xác nhận kết quả cụ thể cùng thời điểm) — cân nhắc nhưng chủ đề thời tiết có
  traffic cao hơn, mới hơn (pubDate gần nhất trong toàn bộ danh sách) và đã có ≥2 nguồn báo chính
  thống khớp số liệu → ưu tiên thời tiết cho suất này.
- "samsung galaxy z fold8", "ios 27" — traffic rất thấp (100-200+), chưa đủ tín hiệu trending mạnh so
  với chủ đề thời tiết (5000+ và xuất hiện ở cả trend lẫn news).

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

- Hôm nay 15/9 đến ngày mai 16/9, đồng bằng Bắc Bộ, Bắc Ninh, phía nam Phú Thọ, Thanh Hoá mưa to đến
  rất to, lượng mưa 100-250mm, có nơi trên 400mm — Tuổi Trẻ + Dân Trí (khớp 2 nguồn).
- Hưng Yên, Ninh Bình, phía nam Phú Thọ và Thanh Hoá lượng mưa 200-400mm, có nơi trên 500mm — Tuổi
  Trẻ + Dân Trí (khớp 2 nguồn, dùng mốc "trên 500mm" theo cách nói chung của cả hai thay vì số lẻ
  550mm chỉ 1 nguồn nêu).
- Lạng Sơn, bắc Phú Thọ, phía nam Thái Nguyên/Tuyên Quang/Sơn La/Lào Cai và Nghệ An mưa vừa đến to,
  có nơi rất to, lượng mưa 80-170mm, có nơi trên 300mm — Tuổi Trẻ.
- Cảnh báo nguy cơ mưa cường độ lớn trên 100mm/3 giờ; trong mưa dông có khả năng lốc, sét, mưa đá,
  gió giật mạnh — Tuổi Trẻ.
- Trên các sông ở Bắc Bộ, Thanh Hoá, Nghệ An khả năng xuất hiện một đợt lũ: đỉnh lũ sông Bôi (Phú
  Thọ), sông Hoàng Long (Ninh Bình), thượng lưu sông Bưởi, sông Mã, sông Chu (Thanh Hoá) khả năng
  lên mức báo động 1 đến báo động 2, có sông vượt báo động 2; thượng lưu sông Cả (Nghệ An) khả năng
  lên trên báo động 1 — Tuổi Trẻ + Dân Trí (khớp 2 nguồn).
- Nguy cơ cao ngập lụt tại vùng trũng thấp ven sông và khu đô thị, sạt lở đất trên sườn dốc các tỉnh
  Phú Thọ, Ninh Bình, Thanh Hoá, Nghệ An — Tuổi Trẻ + Dân Trí.
- Nguyên nhân: hoàn lưu sau áp thấp nhiệt đới kết hợp dải hội tụ nhiệt đới — Tuổi Trẻ.
- Riêng Hà Nội, lượng mưa dự báo phổ biến 100-250mm, phía Nam thành phố có nơi trên 250mm — Dân Trí.
- Nam Bộ, TP.HCM cùng thời điểm: mưa có xu hướng giảm, ban ngày nắng nhiều hơn — Tuổi Trẻ (dùng để
  đối lập ngắn, không phải trọng tâm video).

## Cấu trúc 7 act (định hướng nội dung, style `10-stock-terminal` — tái diễn giải thành "bảng dữ liệu
mưa lũ" thay vì benchmark công nghệ: cột lượng mưa theo vùng, sparkline mức nước sông)

1. Hook: "MƯA LỚN DIỆN RỘNG BẮC BỘ - NGHỆ AN" + tag "● MƯA TO NHẤT 500MM" / "● CẢNH BÁO LŨ, SẠT LỞ".
2. What happened: ảnh người đi xe máy giữa mưa lớn (article-hero.jpg) + 1-2 câu: Trung tâm Dự báo
   khí tượng thuỷ văn quốc gia cảnh báo Bắc Bộ đến Nghệ An mưa to đến rất to trong 2 ngày 15-16/9.
3. Key facts (mỗi fact 1 cột mini lượng mưa theo vùng): đồng bằng Bắc Bộ/Thanh Hoá 100-250mm (trên
   400mm); Hưng Yên/Ninh Bình 200-400mm (trên 500mm); Lạng Sơn/Sơn La/Lào Cai/Nghệ An 80-170mm (trên
   300mm).
4. Data moment: con số chính "trên 500mm" (lượng mưa cao nhất dự báo, Hưng Yên - Ninh Bình) với
   line-chart nhỏ chạy phía sau, chạm đỉnh khi số chốt.
5. Context (biểu đồ cột mức báo động sông): sông Bôi, Hoàng Long, Bưởi, Mã, Chu lên báo động 1-2 (có
   sông vượt báo động 2); sông Cả (Nghệ An) trên báo động 1.
6. Impact (sự thật đã xảy ra — cảnh báo đã ban hành): cơ quan khí tượng đã cảnh báo nguy cơ cao ngập
   lụt đô thị, sạt lở đất tại Phú Thọ, Ninh Bình, Thanh Hoá, Nghệ An, kèm nguy cơ lốc, sét, mưa đá,
   gió giật mạnh trong mưa dông.
7. CTA: nhà bạn có đang ở vùng mưa lớn này không? 2 lựa chọn đối lập "MƯA TO, VẪN ỔN" (mũi tên lên
   cam) / "NGUY CƠ NGẬP LŨ" (tam giác cảnh báo đỏ) + pill "Bình luận quan điểm của bạn".

## Style claim (đã gọi, KHÔNG gọi lại claim_style)

`POST {"action":"claim_style","video":"mua-lon-bac-bo-den-nghe-an"}` →
`{"ok":true,"index":9,"style":"10-stock-terminal","claimed_at":"2026-09-15T00:25:43.290Z"}`.
