# BRIEF — Áp thấp trên Biển Đông có thể thành bão số 6, không khí lạnh đầu mùa tràn về

Video tin nóng/trending kênh "Tin Tức Số" (khung CHIỀU 10/9/2026). Chủ đề phát hiện từ Google Trends VN
("thời tiết áp thấp nhiệt đới"), đối chiếu với tin nóng trang chủ báo lớn, QUA GATE A nhóm **A2 — thời
tiết/thiên tai đưa trung lập, khuyến cáo an toàn** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"thời tiết áp thấp nhiệt đới"**, id `922fae8ff9c1`, vị trí **#17/196**
  trong danh sách (sắp mới nhất trước), `trafficApprox` **"5000+"**, `pubDate` 2026-09-10T00:50:00Z.
  `related` của chính item này đã trỏ thẳng tới bài Dân Trí "Không khí lạnh tràn về miền Bắc, Biển Đông
  có thể sắp đón bão" — đúng chủ đề, không cần suy diễn.
- `GET ?category=news`: có ít nhất 2 bài cùng chủ đề, từ 2 báo lớn khác nhau, cùng trích dẫn Trung tâm
  Dự báo khí tượng thuỷ văn quốc gia với **cùng một bộ số liệu** (xác suất 80% / 30-40%, lượng mưa từng
  vùng) — xác nhận đây vừa đang trending vừa đã có báo chính thống đưa tin, số liệu khớp nhau giữa
  2 nguồn độc lập.
- Nguồn chính dùng cho văn bản + ảnh: **Dân Trí**, id `e71179c125db` — "Không khí lạnh tràn về miền Bắc,
  Biển Đông có thể sắp đón bão" (`?article=` trả `ok:true`, text đầy đủ, có số liệu cụ thể).
- Nguồn đối chiếu thứ 2: **Tuổi Trẻ**, id `c856322eaecf` — "Biển Đông có thể xuất hiện bão số 6 trong
  1-2 ngày tới" — cùng trích dẫn Trung tâm Dự báo khí tượng thuỷ văn quốc gia, **số liệu trùng khớp
  100%** với bài Dân Trí (xác suất 80%/30-40%, lượng mưa 60-120mm/cục bộ >180mm ở Tây Nguyên-Nam Bộ,
  40-100mm/cục bộ >150mm ở Thanh Hoá-Huế, 15-30mm/cục bộ >80mm ở duyên hải Nam Trung Bộ, mốc 12-17/9).
- Đã POST đánh dấu `used` cho id `e71179c125db` (video: `khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`).
- **Nguồn chính thức dùng cho video: Dân Trí** (KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là
  công cụ phát hiện chủ đề).
- Ảnh minh hoạ: `?image=e71179c125db` (ảnh báo Dân Trí, ảnh thật/đồ hoạ dự báo, có dẫn nguồn, không
  watermark ngoài của báo gốc; ~1MB, jpeg, xác nhận `ok:true`).

## GATE A

Nhóm **A2 — GREEN**: thời tiết / cảnh báo cộng đồng, đưa mức thông tin dự báo + khuyến cáo an toàn,
dẫn nguồn cơ quan chức năng (Trung tâm Dự báo khí tượng thuỷ văn quốc gia), KHÔNG khai thác thương
vong (chưa có thiệt hại xảy ra, đây thuần tuý là bản tin dự báo/cảnh báo trước). Không đụng đời tư,
không hình sự, không chính trị, không thể thao — an toàn để dựng.

Các chủ đề trending khác đã xét và loại ở Gate A (ghi lại để minh bạch):
- "giám đốc" (Vingroup miễn nhiệm 1 Phó Tổng giám đốc, báo nước ngoài đặt câu hỏi "vì sao rời ban lãnh
  đạo") — cận A1 đời tư/drama nhân sự, có khung "vì sao" mời suy đoán cá nhân → bỏ.
- "bệnh viện e" (Bộ Y tế xác minh vụ tố "kẹp tiền" để được xạ trị nhanh) — cáo buộc/điều tra đang diễn
  ra, có thể liên quan cá nhân cụ thể, routine không đủ năng lực verify → bỏ theo A1.
- "phú quang" (vợ cố nhạc sĩ nhận tài sản thừa kế, con riêng được hưởng gì) — đời tư gia đình người nổi
  tiếng đã mất → bỏ theo A1.
- "casemiro", "lionel messi", "chicago fire đấu inter miami", các trận vòng bảng Champions League… —
  thể thao nước ngoài thuần giải trí, không yếu tố VN → bỏ theo A1.
- "ukraina" — xung đột vũ trang/đối ngoại → bỏ theo A1.
- "iphone 16 pro max" / "airpod 5" — cùng sự kiện Apple đã dựng 2 video liên tiếp (`iphone-18-ra-mat-
  viet-nam`, `iphone-duo-man-hinh-gap`) trong 2 ngày gần nhất; traffic thấp (100+), không có góc mới →
  bỏ để tránh trùng lặp nội dung (B7).

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

- Sáng/chiều 9/9, Trung tâm Dự báo khí tượng thuỷ văn quốc gia ghi nhận một vùng áp thấp hình thành
  trên dải hội tụ nhiệt đới, ở khu vực giữa Biển Đông — Dân Trí + Tuổi Trẻ.
- Trong 1-2 ngày tới, vùng áp thấp có khả năng cao (xác suất khoảng 80%) mạnh lên thành áp thấp nhiệt
  đới; không loại trừ khả năng (xác suất khoảng 30-40%) mạnh lên thành bão — nếu thành bão sẽ là **bão
  số 6** trên Biển Đông trong năm nay — Dân Trí + Tuổi Trẻ (số liệu trùng khớp 2 nguồn).
- Không khí lạnh đầu mùa: gần sáng 10/9 ảnh hưởng vùng núi Bắc Bộ, trưa/chiều 10/9 ảnh hưởng trung du,
  đồng bằng Bắc Bộ và Bắc Trung Bộ; đêm 10 và ngày 11/9 tiếp tục tăng cường — Dân Trí.
- Đây là đợt không khí lạnh đầu tiên trong năm, đến sớm hơn trung bình nhiều năm khoảng 3-5 ngày
  (trung bình nhiều năm rơi vào 12/9-4/10; sớm nhất từng ghi nhận là 16/8/2003) — Dân Trí.
- Nhiệt độ thấp nhất đợt này: Bắc Bộ và Bắc Trung Bộ phổ biến 21-24 độ C, vùng núi cao Bắc Bộ có nơi
  dưới 19 độ C — Dân Trí.
- Đêm 9 đến ngày 10/9, Bắc Bộ có mưa rào và dông rải rác 10-30mm, cục bộ trên 70mm; Hà Nội tiếp tục
  mưa, chuyển mát từ 10/9 — Dân Trí.
- Kịch bản áp thấp nhiệt đới/bão kết hợp không khí lạnh + gió mùa Tây Nam mạnh, từ 10-11/9: Tây Nguyên
  và Nam Bộ mưa vừa-to, dông, 60-120mm, cục bộ trên 180mm; khu vực Thanh Hoá-Huế mưa vừa-to 40-100mm,
  cục bộ trên 150mm; duyên hải Nam Trung Bộ mưa 15-30mm, cục bộ trên 80mm — Dân Trí + Tuổi Trẻ (khớp
  2 nguồn).
- Từ 12-17/9, dưới tác động dải hội tụ nhiệt đới qua miền Trung, các tỉnh Trung Bộ khả năng cao tiếp
  tục mưa vừa-to diện rộng, kèm nguy cơ cao lốc, sét, lũ quét, sạt lở đất, ngập úng cục bộ — Dân Trí +
  Tuổi Trẻ.

## Cấu trúc 7 act (định hướng nội dung, style `7-timeline-chronology`)

1. Hook: Áp thấp Biển Đông có thể thành bão số 6 + không khí lạnh đầu mùa. Tag: "CÓ THỂ THÀNH BÃO SỐ 6"
   / "KHÔNG KHÍ LẠNH ĐẦU MÙA".
2. What happened: 9/9, cơ quan khí tượng ghi nhận vùng áp thấp hình thành giữa Biển Đông.
3. Key facts (trục dọc 3 mốc): 80% khả năng thành áp thấp nhiệt đới; 30-40% khả năng thành bão; không
   khí lạnh đến sớm 3-5 ngày so với trung bình nhiều năm.
4. Data moment (node lớn trên trục ngang): nhiệt độ thấp nhất — dưới 19 độ C ở vùng núi cao Bắc Bộ.
5. Context (trục ngang đầy đủ mốc theo vùng): mưa cục bộ trên 180mm (Tây Nguyên/Nam Bộ), trên 150mm
   (Thanh Hoá-Huế), trên 80mm (duyên hải Nam Trung Bộ), khung 10-11/9.
6. Impact (sự thật đã xảy ra — cảnh báo đã được ban hành): cơ quan khí tượng đã cảnh báo nguy cơ cao
   lốc, sét, lũ quét, sạt lở đất tại Trung Bộ, từ 12-17/9.
7. CTA: bạn đã chuẩn bị gì ứng phó với đợt thời tiết chuyển mùa bất thường này chưa?

## Style claim (đã gọi, KHÔNG gọi lại claim_style)

`POST {"action":"claim_style","video":"khong-khi-lanh-ap-thap-nhiet-doi-bien-dong"}` →
`{"ok":true,"index":6,"style":"7-timeline-chronology","claimed_at":"2026-09-10T06:28:26.788Z"}`.
