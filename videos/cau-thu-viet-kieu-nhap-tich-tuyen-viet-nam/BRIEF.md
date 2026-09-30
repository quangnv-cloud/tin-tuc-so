# BRIEF — Tuyển Việt Nam có thêm trung vệ Việt kiều nhập tịch

Video tin nóng/trending kênh "Tin Tức Số", chủ đề phát hiện từ Google Trends VN ("nhập tịch"), đối
chiếu tin nóng trang chủ 2 báo lớn, QUA GATE A nhóm **A2 — kết quả/diễn biến thể thao có yếu tố VN +
tin đời sống tích cực** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"nhập tịch"**, id `593c48302761`, `trafficApprox` **"200+"**,
  `pubDate` 2026-09-11T01:10:00Z. `related` của chính item này trỏ 3 bài cùng chủ đề: Thanh Niên,
  Tạp chí Bóng đá (bongdaplus.vn), Thể Thao 247 — đều xác nhận: trung vệ Kyle Colonna (tên Việt
  Lương Chí Khải) nhập quốc tịch Việt Nam thành công.
- `GET ?category=news`: có ít nhất 2 bài cùng chủ đề từ 2 báo lớn khác nhau — Tuổi Trẻ (id
  `c5c83174bb69`, "Tuyển Việt Nam sắp có trung vệ Việt kiều Mỹ cao gần 1m90") và Dân Trí (id
  `1479b8f6963b`, "Sao Việt kiều cao 1,88m nhập tịch thành công, sẵn sàng lên tuyển Việt Nam") — xác
  nhận đây vừa đang trending vừa đã có báo chính thống đưa tin, số liệu khớp nhau giữa 2 nguồn.
- Nguồn chính dùng cho văn bản + ảnh: **Tuổi Trẻ**, id `c5c83174bb69` (`?article=` trả `ok:true`,
  text đầy đủ, có trích dẫn công bố từ Văn phòng Chủ tịch nước).
- Nguồn đối chiếu thứ 2: **Dân Trí**, id `1479b8f6963b` — số liệu khớp gần như 100% với Tuổi Trẻ,
  có thêm dữ liệu chuyên môn (thông số thu hồi bóng, tranh chấp, không chiến).
- Đã POST đánh dấu `used` cho id `c5c83174bb69` (video: `cau-thu-viet-kieu-nhap-tich-tuyen-viet-nam`).
- **Nguồn chính thức dùng cho video: Tuổi Trẻ** (KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là
  công cụ phát hiện chủ đề).
- Ảnh minh hoạ: `?image=c5c83174bb69` — ảnh thật từ Tuổi Trẻ (CLB Thể Công - Viettel ăn mừng bàn
  thắng), có dẫn nguồn, không watermark ngoài của báo gốc, độ phân giải 1200×750 đủ dùng.

## GATE A

Nhóm **A2 — GREEN**: kết quả/diễn biến thể thao có yếu tố Việt Nam (cầu thủ nhập tịch phục vụ đội
tuyển quốc gia) + tin đời sống tích cực (một cá nhân đạt nguyện vọng trở thành công dân Việt Nam,
không dính scandal/tranh cãi cá nhân). Đây là tin chuyên môn thể thao trung lập, không đụng đời tư/
hình sự/chính trị.

Các chủ đề trending khác đã xét và loại ở Gate A (ghi lại để minh bạch):
- "mỹ tâm", "trường giang", "hari won", "nhật kim anh", "hồ ngọc hà", "phú quang" — đời tư/nghệ sĩ →
  bỏ theo A1.
- "xung đột", "iran", "putin", "ukraina", "tên lửa đạn đạo", "tô lâm", "chính phủ", "quân sự" —
  chính trị/đối ngoại/xung đột vũ trang → bỏ theo A1.
- "charlie kirk" — nhân vật chính trị Mỹ, drama/tranh cãi → bỏ theo A1.
- "rửa tiền", "công an xã", "công an thành phố đồng nai", "cục cảnh sát giao thông" — khả năng liên
  quan điều tra/hình sự cá nhân → bỏ theo A1.
- Hàng loạt từ khoá bóng đá nước ngoài thuần giải trí không yếu tố VN (Man Utd, Barca, PSG, Arsenal,
  Bayern, Chelsea, Liverpool, Napoli, AS Roma, Fenerbahçe, giải MLS Mỹ…) → bỏ theo A1.
- "giá xăng" / "giá xăng dầu" — đã dựng video cùng chủ đề gần đây (`gia-xang-dau-tang-hon-1200-dong-lit`,
  10/9) → bỏ để tránh trùng lặp, ưu tiên chủ đề mới hơn.
- "áp thấp nhiệt đới" / "bão hôm nay" / các mục dự báo thời tiết — đã dựng video cùng nhóm chủ đề gần
  đây (`khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`, 10/9) → bỏ để tránh trùng lặp.
- "iphone duo" — đã dựng video cùng chủ đề gần đây (`iphone-duo-man-hinh-gap`, 10/9) → bỏ để tránh
  trùng lặp.
- "sức khỏe và đời sống", "văn khấn mùng 1", "lịch âm", "xổ số miền nam"… — traffic cao nhưng nội
  dung không đủ chất tin tức thời sự (nội dung tra cứu/tâm linh định kỳ) → bỏ.

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

- Trung vệ Việt kiều Mỹ Colonna Nino Kyle (CLB Thể Công - Viettel) chính thức có quốc tịch Việt Nam,
  quyết định công bố trên Trang thông tin điện tử Văn phòng Chủ tịch nước — Tuổi Trẻ.
- Nhập quốc tịch ngày 29/8, tên gọi Việt Nam: **Lương Chí Khải** — Tuổi Trẻ, Dân Trí.
- Sinh năm 1999 tại Mỹ, bố người Mỹ, mẹ người Việt — Tuổi Trẻ, Dân Trí.
- Chiều cao: Tuổi Trẻ ghi "gần 1m90"; Dân Trí ghi "1,88m" — video dùng cách nói an toàn "gần 1,9 mét"
  (khớp cả 2 nguồn, không chốt số lẻ gây chênh).
- Giúp HLV Kim Sang Sik có thêm lựa chọn nơi hàng thủ cho đội tuyển Việt Nam, hướng tới **FIFA ASEAN
  Cup 2026** — Tuổi Trẻ, Dân Trí.
- Sang Việt Nam từ tháng 8/2024, khoác áo Hà Nội FC mùa 2024-2025, chuyển sang CLB Thể Công - Viettel
  từ mùa 2025-2026 — Tuổi Trẻ, Dân Trí.
- Mùa 2025-2026: ghi 1 bàn trong 24 trận đá chính ở V-League — Tuổi Trẻ.
- Mùa 2026-2027 (mới đá 2 vòng): đã ghi 1 bàn ngay trận ra quân, CLB Thể Công - Viettel thắng chủ nhà
  Thành phố Đồng Nai 2-0 — Tuổi Trẻ.
- Thông số chuyên môn mùa trước: trung bình 10,8 lần thu hồi bóng/trận, 6,5 lần tranh chấp thành
  công, 2,4 lần không chiến thắng lợi mỗi trận; có tên trong đội hình tiêu biểu V-League mùa trước —
  Dân Trí.
- Bối cảnh: các trung vệ kỳ cựu Duy Mạnh, Bùi Tiến Dũng đang chấn thương; Khổng Minh Gia Bảo chơi
  chưa thuyết phục ở ASEAN Cup 2026 — Tuổi Trẻ.
- Trước Lương Chí Khải, hàng thủ tuyển Việt Nam đã có trung vệ Việt kiều Adou Minh (gốc Pháp, CLB
  Công An Hà Nội) nhập tịch — Tuổi Trẻ.
- Trưởng thành từ bóng đá học đường Mỹ: khoác áo Đại học San Diego State 2018-2022 (69 trận, 2 năm
  đội trưởng, vào top 14 đội xuất sắc nhất toàn quốc 2022), sau đó ký hợp đồng chuyên nghiệp với
  New Mexico United (Giải hạng nhất Mỹ) — Tuổi Trẻ.

## Cấu trúc 7 act (định hướng nội dung, style `1-card-and-bar`)

1. Hook: Tuyển Việt Nam có thêm trung vệ nhập tịch — Lương Chí Khải (Kyle Colonna). Tag: "● NHẬP
   TỊCH THÀNH CÔNG" / "● HƯỚNG ASEAN CUP".
2. What happened: trung vệ Việt kiều Mỹ của CLB Thể Công - Viettel chính thức có quốc tịch Việt Nam
   ngày 29/8, tên gọi Lương Chí Khải, mở thêm lựa chọn cho HLV Kim Sang Sik.
3. Key facts (3 thẻ bo góc, số thứ tự): sinh năm 1999 tại Mỹ, bố Mỹ mẹ Việt · cao gần 1,9 mét, chơi
   trung vệ · sang Việt Nam từ tháng 8/2024, hiện khoác áo Thể Công - Viettel.
4. Data moment (số chính giữa + cột phụ so sánh): 1 bàn thắng trong trận ra quân mùa 2026-2027 (Thể
   Công - Viettel thắng Thành phố Đồng Nai 2-0); cột phụ: 10,8 lần thu hồi bóng/trận, 6,5 lần tranh
   chấp thành công mùa trước.
5. Context (bảng thông số / dòng so sánh): từng là đội trưởng Đại học San Diego State (Mỹ), sau đó
   khoác áo Hà Nội FC rồi Thể Công - Viettel; là trung vệ Việt kiều thứ 2 nhập tịch sau Adou Minh.
6. Impact (sự thật đã xảy ra): tuyển Việt Nam có thêm lựa chọn chất lượng nơi hàng thủ trong bối cảnh
   Duy Mạnh, Bùi Tiến Dũng chấn thương, hướng tới FIFA ASEAN Cup 2026.
7. CTA: cầu thủ Việt kiều nhập tịch — tiếp sức hay tranh suất của cầu thủ nội? 2 lựa chọn đối lập
   "Tiếp sức đội tuyển" / "Tranh suất cầu thủ nội".

## Style claim (đã gọi, KHÔNG gọi lại claim_style)

`POST {"action":"claim_style","video":"cau-thu-viet-kieu-nhap-tich-tuyen-viet-nam"}` →
`{"ok":true,"index":0,"style":"1-card-and-bar","claimed_at":"2026-09-11T06:28:00.212Z"}`.
