# BRIEF — Giá xăng dầu đồng loạt tăng mạnh, có loại tăng hơn 1.200 đồng/lít

Video tin nóng/trending kênh "Tin Tức Số" (LẦN CHẠY TEST — kiểm tra chất lượng pipeline trên
environment/team mới, KHÔNG phải lần chạy sản xuất thật; dừng lại sau bước 13, KHÔNG đăng
Facebook/YouTube). Chủ đề phát hiện từ Google Trends VN ("giá xăng dầu"), đối chiếu tin nóng trang
chủ báo lớn, QUA GATE A nhóm **A2 — chính sách/quy định mới đã ban hành (giá xăng)** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"giá xăng dầu"**, id `87f1ccd3ac31`, vị trí **#1/197** trong danh
  sách chưa dùng (sắp mới nhất trước), `trafficApprox` **"200+"**, `pubDate` 2026-09-10T08:30:00Z.
  `related` của chính item này trỏ tới 3 bài cùng chủ đề: Dân Trí, Lao Động, Tuổi Trẻ.
- `GET ?category=news`: có ít nhất 2 bài cùng chủ đề từ 2 báo lớn khác nhau (Tuổi Trẻ, VnExpress),
  cùng trích số liệu từ thông báo chính thức của Bộ Công Thương — xác nhận đây vừa đang trending vừa
  đã có báo chính thống đưa tin, số liệu khớp nhau (chênh lệch làm tròn vài đồng) giữa 2 nguồn độc lập.
- Nguồn chính dùng cho văn bản + ảnh: **Tuổi Trẻ**, id `eb4b27f442ec` — "Giá xăng dầu tăng mạnh, xăng
  sinh học tăng cao nhất thêm hơn 1.200 đồng/lít" (`?article=` trả `ok:true`, text đầy đủ, số liệu cụ thể).
- Nguồn đối chiếu thứ 2: **VnExpress**, id `9ec4abd03d41` — "Giá xăng, dầu cùng tăng" — số liệu khớp
  gần như 100% với Tuổi Trẻ (chênh lệch làm tròn 4-10 đồng), có thêm dữ liệu so sánh giá khu vực.
- Đã POST đánh dấu `used` cho id `eb4b27f442ec` (video: `gia-xang-dau-tang-hon-1200-dong-lit`).
- **Nguồn chính thức dùng cho video: Tuổi Trẻ** (KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là
  công cụ phát hiện chủ đề).
- Ảnh minh hoạ: `?image=eb4b27f442ec` (ảnh báo Tuổi Trẻ từ CDN báo, có dẫn nguồn, không watermark
  ngoài của báo gốc).

## GATE A

Nhóm **A2 — GREEN**: chính sách/quy định giá đã ban hành chính thức (Bộ Công Thương thông báo điều
chỉnh giá xăng dầu), số liệu kinh tế trung lập, không đụng đời tư/hình sự/chính trị/thể thao. Nguyên
nhân giá thế giới biến động được nêu ở mức khái quát ("đà biến động thị trường năng lượng thế giới")
theo đúng cách VnExpress đóng khung — KHÔNG nêu chi tiết xung đột vũ trang cụ thể (dù bài gốc có nhắc
căng thẳng Mỹ-Iran) để tránh chạm nhóm A1 "xung đột vũ trang/đối ngoại", giữ trọng tâm video 100% ở
chủ đề giá xăng dầu trong nước.

Các chủ đề trending khác đã xét và loại ở Gate A (ghi lại để minh bạch):
- "hari won" — đời tư/nghệ sĩ → bỏ theo A1.
- "quân sự", "ukraina" — đối ngoại/xung đột vũ trang → bỏ theo A1.
- "giám đốc" — traffic thấp, tiêu đề mơ hồ, rủi ro là tin nhân sự/cá nhân cụ thể → bỏ để tránh rủi ro.
- "công an thành phố đồng nai" — khả năng liên quan điều tra/an ninh cá nhân, không có ảnh → bỏ.
- "casemiro", "thứ hạng của chicago fire gặp inter miami" — thể thao nước ngoài thuần giải trí, không
  yếu tố VN → bỏ theo A1.
- "dự báo thời tiết hà nội" / "dự báo thời tiết tphcm hôm nay" — cùng nhóm chủ đề thời tiết đã dựng
  trong video khác cùng ngày (`khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`) → bỏ để tránh trùng lặp.

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

- Bộ Công Thương thông báo điều chỉnh giá xăng dầu, áp dụng từ 15h ngày 10-9-2026 — Tuổi Trẻ + VnExpress.
- Xăng E5 RON92: 23.744 đồng/lít, tăng 1.258 đồng/lít so với kỳ trước — Tuổi Trẻ (VnExpress: 23.740
  đồng/lít, tăng 1.260 đồng — chênh lệch làm tròn không đáng kể).
- Xăng E10 RON95-III: 24.239 đồng/lít, tăng 965 đồng/lít — Tuổi Trẻ (VnExpress: 24.230 đồng, tăng 960
  đồng).
- Dầu diesel 0.05S: 28.485 đồng/lít, tăng 742 đồng/lít — Tuổi Trẻ (VnExpress: 28.480 đồng).
- Dầu mazut 180CST 3.5S: 18.157 đồng/kg, tăng 516 đồng/kg — Tuổi Trẻ (VnExpress: 18.150 đồng).
- Nguyên nhân: xu hướng chung là tăng mạnh do biến động thị trường xăng dầu/năng lượng thế giới —
  Tuổi Trẻ ("chịu ảnh hưởng của nhiều yếu tố... xu hướng chung là tăng mạnh"), VnExpress ("theo đà
  biến động của thị trường năng lượng thế giới").
- Liên bộ Công Thương - Tài chính dừng trích lập quỹ bình ổn giá xăng dầu về 0 đồng với tất cả mặt
  hàng, riêng xăng sinh học được chi sử dụng quỹ bình ổn 500 đồng/lít — Tuổi Trẻ.
- Đây là kỳ tăng giá liên tiếp sau đà tăng ở kỳ điều hành trước — Tuổi Trẻ.
- So sánh khu vực (VnExpress): sau điều chỉnh, giá xăng Việt Nam vẫn thấp hơn Campuchia/Thái Lan
  (khoảng 28.330-30.000 đồng/lít), Trung Quốc (hơn 32.870 đồng/lít), Lào (tới 48.210 đồng/lít).

## Cấu trúc 7 act (định hướng nội dung, style `8-icon-grid`)

1. Hook: Giá xăng dầu đồng loạt tăng mạnh, hiệu lực từ 15h. Tag: "● TĂNG ĐỒNG LOẠT" / "● HIỆU LỰC TỪ 15H".
2. What happened: Bộ Công Thương thông báo điều chỉnh giá xăng dầu, áp dụng từ 15h ngày 10/9.
3. Key facts (lưới icon 1×4 hoặc 2×2 — mỗi ô 1 loại xăng dầu): E5 23.744đ/lít · E10 24.239đ/lít ·
   diesel 28.485đ/lít · mazut 18.157đ/kg.
4. Data moment (ô lớn giữa lưới 3 ô, 2 ô phụ 2 bên chứa số bổ trợ E10/diesel): mức tăng mạnh nhất —
   xăng E5 tăng 1.258 đồng/lít.
5. Context (lưới icon so sánh khu vực): giá xăng VN vẫn thấp hơn Campuchia/Thái Lan, Trung Quốc, Lào;
   nguyên nhân đà biến động thị trường năng lượng thế giới.
6. Impact (sự thật đã xảy ra): liên bộ dừng trích lập quỹ bình ổn về 0 đồng (trừ xăng sinh học 500đ/lít
   được chi); đây là kỳ tăng liên tiếp sau đợt tăng kỳ trước.
7. CTA: mức tăng giá xăng ảnh hưởng chi tiêu của bạn thế nào? 2 lựa chọn đối lập "Vẫn ổn" / "Áp lực
   chi tiêu".

## Style claim (đã gọi, KHÔNG gọi lại claim_style)

`POST {"action":"claim_style","video":"gia-xang-dau-tang-hon-1200-dong-lit"}` →
`{"ok":true,"index":7,"style":"8-icon-grid","claimed_at":"2026-09-10T09:45:21.335Z"}`.
