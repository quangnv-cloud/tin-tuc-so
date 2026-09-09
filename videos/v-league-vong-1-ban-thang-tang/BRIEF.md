# BRIEF — Vòng 1 V-League 2026-2027: bàn thắng tăng vọt, Việt kiều trẻ tỏa sáng

Video tin nóng/trending kênh "Tin Tức Số" (khung CHIỀU 9/9/2026). Chủ đề phát hiện từ Google Trends VN
("giải bóng đá vô địch quốc gia việt nam"), QUA GATE A nhóm **A2 — kết quả thể thao có yếu tố VN**
(giải trong nước, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"giải bóng đá vô địch quốc gia việt nam"**, id `d3353fbbf7ab`,
  vị trí #74/112 trong danh sách (sắp mới nhất trước), `trafficApprox` **"200+"**, `pubDate`
  2026-09-08T12:10:00Z.
- `related[0]` trỏ bài **Báo Thanh Niên** — nội dung khớp: "V-League sẽ còn bùng nổ" — dùng `id` này
  cho `?article=` (server tải bài Thanh Niên).
- Đối chiếu thêm 2 `related` khác cùng chủ đề (không có text đầy đủ, chỉ tiêu đề — dùng làm ngữ cảnh
  bổ sung, không trích số liệu từ đây): "Bảng xếp hạng V-League 2026/2027 mới nhất: Xuất hiện điều
  hiếm thấy" (VOV.VN), "Khép lại vòng 1 V.League 2025/26: Chủ nhà chiếm ưu thế?" (VTV.vn).
- `category=news` không có bài đúng chủ đề "vòng 1 V-League 2026-2027" (chỉ có tin khác về CLB
  Becamex TP.HCM muốn lên hạng) — không dùng làm nguồn nội dung, chỉ dùng ảnh minh hoạ chung V-League
  (xem mục Ảnh).

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước) — tường thuật kết
quả, số liệu." Đây là giải quốc nội (V-League/giải bóng đá vô địch quốc gia Việt Nam), không phải
thể thao nước ngoài thuần giải trí. Không đụng đời tư cầu thủ, không có yếu tố hình sự/chính trị.
→ **GREEN, APPROVE để dựng**.

(Đã cân nhắc và LOẠI 2 chủ đề khác trước khi chọn chủ đề này:
1. "sầu riêng" (xuất khẩu tăng 47%, id `9b08d8381a97`) — nội dung QUA GATE A (A2) nhưng ảnh trend chỉ
   284×177px (thumbnail Google quá nhỏ/mờ) và không có item `category=news` cùng chủ đề đúng góc xuất
   khẩu để lấy ảnh chuẩn (chỉ có bài giá nông sản cà phê/sầu riêng ngày, ảnh og:image lại là ảnh cà
   phê — sai chủ đề, không dùng được) → bỏ vì không có ảnh dùng được (mục 1e ROUTINE.md), đã POST
   đánh dấu used.
2. "khu liên hợp thể thao" (Bộ Quốc phòng quản lý khu liên hợp thể thao quốc gia Mỹ Đình từ 1/10, id
   `587bc422ea88`) — có ảnh chuẩn tốt (VnExpress, 1200×720) nhưng chủ đề chạm tổ chức quản lý nhà
   nước / Bộ Quốc phòng → xếp vào vùng xám gần nhóm A1 "chính trị/nhân sự-tổ chức nhà nước", GATE A
   bản tuyến này siết chặt "không đụng kể cả tin tích cực" với nhóm chính trị/đối ngoại/tổ chức nhà
   nước cấp cao → chủ động bỏ dù đã đạt yêu cầu ảnh, ưu tiên an toàn chính sách hơn. Chưa POST đánh
   dấu used cho id này vì chưa từng chọn chính thức.)

## Nguồn & nội dung (bước 2 ROUTINE.md)

Nguồn chính: **Báo Thanh Niên** (qua `?article=d3353fbbf7ab`). Số liệu:

- Vòng 1 giải bóng đá vô địch quốc gia Việt Nam mùa 2026-2027: **7 trận, tổng 23 bàn thắng**, nhiều
  hơn 3 bàn so với vòng mở màn mùa trước (tức mùa trước vòng 1 có 20 bàn).
  Trung bình hơn 3 bàn/trận — "một con số ấn tượng cho vòng đấu đầu tiên" (nguyên văn báo Thanh Niên).
- Kết quả đáng chú ý: Nam Định thắng Hoàng Anh Gia Lai 4-0; Ninh Bình thắng Hải Phòng 4-1; Thanh Hóa
  thắng Đà Nẵng 3-2.
- Tân binh chơi tốt ngay vòng 1: Ezequiel Santos (Nam Định), Saliou Guindo (Thanh Hóa), dàn cầu thủ
  mới của Thể Công Viettel.
- Trọng tài/VAR: không có tình huống tranh cãi đáng kể xuyên suốt vòng 1.
- Cầu thủ nội nổi bật: Tiến Linh (đánh đầu ghi bàn vào lưới Hà Nội), Williams Minh Hoàng, Xuân Son
  (ghi 1 bàn), Đình Bắc, Quang Vinh, Đoàn Văn Hậu, thủ môn Patrik Lê Giang.
- Việt kiều trẻ tỏa sáng: Trần Thành Trung (Ninh Bình), Tran Lenn Minh Quang (Công an TP.HCM), Tyler
  James Thai Crawford (Nam Định) — theo báo, đây là "nguồn lực" cho lứa U.23 Việt Nam.
- HLV Kim Sang-sik đang tìm nhân tố mới cho đội tuyển Việt Nam, hướng tới giải bóng đá vô địch Đông
  Nam Á (FIFA ASEAN Cup) sắp tới — nêu là bối cảnh có thật (giải đấu sắp diễn ra), KHÔNG suy đoán kết
  quả tương lai của đội tuyển.

TUYỆT ĐỐI không bịa thêm cầu thủ/kết quả ngoài danh sách trên. Không dùng "ngược dòng" hay các tính
từ diễn giải không có trong nguồn cho các trận đấu.

## Ảnh minh hoạ (bước 5 ROUTINE.md)

- `?image=d3353fbbf7ab` (item trend) trả ảnh 263×191px — thumbnail Google quá nhỏ, không dùng.
- Không có item `category=news` đúng chủ đề "vòng 1 V-League" để lấy ảnh chuẩn khớp 100%. Dùng ảnh
  **og:image từ Báo Tuổi Trẻ** (`?image=bad08b6d7743`, bài "CLB Becamex TP.HCM xuất quân, quyết trở
  lại V-League", 1200×750px) — ảnh chụp thật một pha bóng V-League (có logo giải VPF trên biển quảng
  cáo sân), dùng làm ảnh minh hoạ KHÔNG khí V-League nói chung cho Hook/Article Image Card — KHÔNG chú
  thích là ảnh của trận đấu/cầu thủ cụ thể nào được nêu trong script (tránh gây hiểu sai theo B6).
  Badge "Nguồn" trên video vẫn ghi tên nguồn nội dung chính (Thanh Niên); ảnh dẫn nguồn phụ Tuổi Trẻ
  ghi trong `copyright_notes` của COMPLIANCE.md (tương tự tiền lệ video `iphone-18-ra-mat-viet-nam`
  dùng ảnh Dân Trí trong khi badge nguồn là VnExpress).

## Cách dựng (style)

`claim_style` → index 3, **"4-split-comparison"**. Ẩn dụ: mùa trước ↔ mùa này (bàn thắng 20 ↔ 23),
đội thắng ↔ đội thua trong các trận đáng chú ý, cầu thủ nội ↔ Việt kiều.

## 7 act

1. Hook — masthead + badge nguồn "Thanh Niên" + ngày 9/9/2026 + tên chủ thể to "Vòng 1 V-League bùng
   nổ bàn thắng" + 2 tag tương phản: "● Bàn thắng tăng vọt" / "● Trọng tài không tranh cãi".
2. What happened — vòng 1 mùa 2026-2027 khép lại với 23 bàn thắng sau 7 trận.
3. Key facts — 3 kết quả đáng chú ý (Nam Định 4-0 HAGL, Ninh Bình 4-1 Hải Phòng, Thanh Hóa 3-2 Đà
   Nẵng).
4. Data moment (split trước/nay) — 20 bàn (vòng 1 mùa trước) ↔ 23 bàn (vòng 1 mùa này), +3 bàn,
   trung bình hơn 3 bàn/trận.
5. Context (split nội ↔ Việt kiều) — tân binh + cầu thủ nội nổi bật ↔ Việt kiều trẻ tỏa sáng.
6. Impact (sự thật đã xảy ra) — HLV Kim Sang-sik có thêm lựa chọn nhân sự chất lượng cho đội tuyển
   Việt Nam trước thềm giải bóng đá vô địch Đông Nam Á.
7. CTA — câu hỏi tranh luận: cả mùa sẽ hấp dẫn hay chỉ là hưng phấn đầu mùa?
