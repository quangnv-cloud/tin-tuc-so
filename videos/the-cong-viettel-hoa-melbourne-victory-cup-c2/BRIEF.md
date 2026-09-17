# BRIEF — Thể Công Viettel hòa 1-1 Melbourne Victory ở Cúp C2 châu Á (2026)

Video tin nóng/trending kênh "Tin Tức Số" (khung 17/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kết quả thể thao có yếu tố VN** (câu lạc bộ Việt Nam Thể Công Viettel, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: cụm từ khoá "thể công gặp melbourne victory" / "thể công đấu với melbourne
  victory" xuất hiện với `trafficApprox` cao nhất danh sách hôm nay: **"10000+"** (id `57cf0e75bf04`
  và `4b453214b99f`, cùng nội dung, khác thời điểm fetch), `pubDate` 2026-09-16T14:20:00Z. `related`
  của cả 2 item trỏ báo VN uy tín: 24h.com.vn, Lao Động, Thể Thao 247, VietNamNet, Tuổi Trẻ.
- `GET ?category=news` có bài tổng kết trận đấu đầy đủ nhất: **Dân Trí**, id `11f07e3d785d`,
  "Thể Công Viettel chia điểm với đội bóng Australia tại Cúp C2 châu Á" — dùng `id` này cho cả
  `?article=` và `?image=` (đúng chủ đề, đủ số liệu, ảnh báo chuẩn).
- **Nguồn thật dùng để dựng**: Báo Dân Trí (KHÔNG ghi "Google Trends" là nguồn).
- Đã POST đánh dấu used: `{"id":"11f07e3d785d","video":"the-cong-viettel-hoa-melbourne-victory-cup-c2"}`.
- `claim_style` → `index: 6`, `style: "7-timeline-chronology"` — khớp tự nhiên với diễn biến trận đấu
  theo mốc thời gian (phút 46 → 58 → 62).
- `trending_signal`: "thể công gặp melbourne victory — trafficApprox 10000+ (đỉnh danh sách trend hôm nay)".

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước)". Thể Công Viettel
là câu lạc bộ Việt Nam thi đấu tại Cúp C2 châu Á (AFC Champions League Two) — giải cấp câu lạc bộ châu
lục, không phải "thể thao nước ngoài thuần giải trí". Không đụng đời tư cầu thủ, không có yếu tố hình
sự/chính trị/cá độ. Tường thuật kết quả + diễn biến trận đấu, trung lập, không giật gân.
→ **GREEN, APPROVE để dựng**.

(Đã lướt và LOẠI các chủ đề trending khác cùng khung giờ trước khi chọn chủ đề này: phần lớn đầu danh
sách `trend` là thể thao nước ngoài thuần giải trí không yếu tố VN — La Liga, Premier League, EFL
Cup, Europa League, AFC Champions League Elite của Al Ain/Al-Nassr, U-23 các đội Nhật Bản/Hàn Quốc/
Iran/Thái Lan không có VN (A1, BỎ); chính trị — "tô lâm" (A1, BỎ NGAY); đời tư nghệ sĩ — "trấn thành",
"mạc văn khoa", "doãn quốc đam", "ninh dương lan ngọc" (A1, BỎ); từ khoá quá chung chung không đủ dữ
kiện xây 7 act — "tiết kiệm", "phần mềm", "thuế", "chung cư", "nhiệm kỳ" (BỎ). Thể Công Viettel là chủ
đề thể thao có yếu tố VN rõ ràng, trafficApprox cao nhất, vừa có ở `trend` vừa có bài tổng kết đầy đủ
ở `news` với ảnh báo chuẩn.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Trận đấu: Thể Công Viettel (Việt Nam) – Melbourne Victory (Úc), lượt trận thứ nhất vòng bảng, khu
  vực phía Đông, Cúp C2 châu Á (AFC Champions League Two) 2026-2027, sân Hàng Đẫy (Hà Nội), tối
  16/9/2026.
- Kết quả: hòa 1-1.
- Diễn biến: phút 46, Lucas Ribamar (Thể Công Viettel) sút vào lưới nhưng bị từ chối bàn thắng do
  trước đó bóng chạm tay cầu thủ Thể Công Viettel. Phút 58, Clarismario (Melbourne Victory) đi bóng
  qua hậu vệ, sút vào góc xa trước thủ môn Văn Việt, Melbourne Victory dẫn 1-0. Phút 62, hậu vệ cánh
  trái Phan Tuấn Tài tạt bóng chân phải, hậu vệ Melbourne Victory phá bóng không tốt, Lucas Ribamar
  đánh đầu ghi bàn gỡ hòa 1-1 (tỷ số chung cuộc).
  (Đối chiếu 2 nguồn: Dân Trí — bài chính dùng dựng nội dung; VietNamNet "Kết quả bóng đá Thể Công
  Viettel 1-1 Melbourne Victory" — cùng khớp tỷ số và mốc trận đấu.)
- Bảng xếp hạng: kết quả hòa giúp Thể Công Viettel tạm xếp thứ hai bảng E, sau Persib Bandung
  (Indonesia). Cùng ngày, Persib Bandung thắng FC Seoul (Hàn Quốc) 1-0, tại Seoul.
- Bối cảnh: Thể Công Viettel vừa thắng CLB Đồng Nai 2-0 ở trận mở màn V-League 2026-2027 (trận có
  hai thẻ đỏ). CLB Công An Hà Nội (đại diện Việt Nam khác) thua 1-4 trước Gamba Osaka (Nhật Bản) ở
  Cúp C1 châu Á (AFC Champions League Elite), ngày 15/9 tại Osaka — dùng làm bối cảnh, KHÔNG phải nội
  dung chính.
- HLV Popov (Thể Công Viettel) — theo tiêu đề bài trên Tuổi Trẻ (trong `related`): "Hòa được Melbourne
  là thành công" — dùng như trích dẫn tinh thần chung, KHÔNG trích nguyên văn phát ngôn đầy đủ vì
  không có trong bài đã tải (`?article=`).

## Ảnh (bước 5 ROUTINE.md)

`?image=11f07e3d785d` (id item `news` Dân Trí) → ảnh báo thật, minh hoạ trận đấu Thể Công Viettel –
Melbourne Victory, có dẫn nguồn. GREEN theo B4 (ảnh og:image bài báo, có dẫn nguồn, không cần
disclosure).

## Style dựng: 7-timeline-chronology

Trục thời gian dọc xuyên các mốc trận đấu: What happened (badge mốc trận đấu cạnh kicker), Key facts
(3 fact xếp dọc theo trục đứng bên trái, node tròn nở khi fact xuất hiện), Data moment (node lớn tại
phút 62 — bàn gỡ hòa, trục vẽ dần rồi dừng khi số chốt), Context (trục đầy đủ các mốc phút 46 → 58 →
62 theo chiều dọc), Impact (2 node cuối trục phóng to thành khối bảng xếp hạng bảng E).
