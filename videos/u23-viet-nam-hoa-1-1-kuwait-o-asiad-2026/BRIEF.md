# BRIEF — U23 Việt Nam hòa 1-1 Kuwait ở trận ra quân Asiad 20 (2026)

Video tin nóng/trending kênh "Tin Tức Số" (khung 16/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kết quả thể thao có yếu tố VN** (đội tuyển U23 Việt Nam, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: 2 từ khoá cùng chủ đề xuất hiện gần đỉnh danh sách (mới nhất trước):
  - `"u-23 việt nam đấu với đội tuyển bóng đá u-23 quốc gia kuwait"`, id `263fc4864192`,
    `trafficApprox` **"10000+"**, `pubDate` 2026-09-15T09:40:00Z.
  - `"u23 việt nam"`, id `a8ddf8f7cbba`, `trafficApprox` **"5000+"**, `pubDate` 2026-09-15T08:00:00Z.
  - `related` của cả 2 item đều trỏ báo VN uy tín (VnExpress, VietnamNet, Vietnam+, 24h, Thể Thao 247).
- `GET ?category=news` có nhiều bài đúng chủ đề, đầy đủ chi tiết trận đấu SAU khi trận kết thúc
  (khác với `trend`/`related` — vốn chỉ có bài "trước trận"/"trực tiếp"). Chọn bài tổng kết trận đấu
  đầy đủ số liệu nhất: **VnExpress Thể thao**, id `d3e2d4edfcba`,
  "HLV U23 Việt Nam tiếc nuối vì không thắng Kuwait ở ASIAD 2026", pubDate 2026-09-15T13:17:40Z.
  → dùng `id` này cho cả `?article=` và `?image=` (đúng chủ đề, đủ số liệu, ảnh chuẩn 1200×720,
  không phải thumbnail Google).
- **Nguồn thật dùng để dựng**: VnExpress Thể thao (KHÔNG ghi "Google Trends" là nguồn).
- Đã POST đánh dấu used: `{"id":"d3e2d4edfcba","video":"u23-viet-nam-hoa-1-1-kuwait-o-asiad-2026"}`.
- `claim_style` → `index: 3`, `style: "4-split-comparison"` (khớp tự nhiên với ẩn dụ so sánh
  2 đội Việt Nam / Kuwait).

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước) — tường thuật kết
quả, số liệu." Đây là đội tuyển U23 Việt Nam thi đấu tại đại hội thể thao châu Á (Asiad 20/Asian
Games), không phải thể thao nước ngoài thuần giải trí. Không đụng đời tư cầu thủ, không có yếu tố
hình sự/chính trị/cá độ. Tường thuật kết quả + số liệu trận đấu, trung lập, không giật gân.
→ **GREEN, APPROVE để dựng**.

(Đã lướt qua và LOẠI các chủ đề trending khác cùng khung giờ trước khi chọn chủ đề này — phần lớn
đầu danh sách `trend` là: thể thao nước ngoài thuần giải trí không yếu tố VN — La Liga, Premier
League, AFC Champions League Elche/Real Madrid, Liverpool/Spurs, Al Ain/Al-Nassr… (A1, BỎ); đời tư/
tên nghệ sĩ — Trấn Thành, Mạc Văn Khoa, Doãn Quốc Đam, Mai Tài Phến, "công lý" nghi là nghệ sĩ Công
Lý (A1, BỎ); từ khoá quá chung chung không đủ dữ kiện xây 7 act — "tiết kiệm", "phần mềm", "ngân
hàng", "sinh viên" (BỎ). U23 Việt Nam là chủ đề trending cao nhất (10000+) vừa QUA GATE A2 vừa có đủ
nguồn báo chính thống + ảnh chuẩn.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Trận đấu: U23 Việt Nam – U23 Kuwait, bảng C môn bóng đá nam Asiad 20 (Đại hội Thể thao châu Á),
  sân CS Asset Minato, Nagoya, Nhật Bản, chiều/tối 15/9/2026.
- Kết quả: hòa 1-1.
- Bàn thắng: phút 78, Omar Almatar (Kuwait) đánh đầu mở tỷ số; phút 80, Nguyễn Ngọc Mỹ đánh đầu gỡ
  hòa cho Việt Nam.
- Thống kê trận đấu: Việt Nam kiểm soát bóng 63%; dứt điểm 27 lần (trúng đích 6) so với 10 lần
  (trúng đích 5) của Kuwait; phạt góc 8 so với 4.
- Việt Nam 4 lần dứt điểm dội cột dọc/xà ngang trong trận (lần cuối: Lê Văn Thuận, cuối trận).
- HLV Đinh Hồng Vinh: "Thật tiếc vì không thắng được Kuwait, dù chúng tôi có rất nhiều cơ hội."; đội
  mới tập trung từ 12/9, mưa lớn trong trận ảnh hưởng cảm giác bóng.
- Đội hình có 13 cầu thủ lứa U21 (từng giành HC đồng U23 châu Á 2026 tháng 1 tại Arab Saudi), vắng
  một số trụ cột: Nguyễn Đình Bắc, Trần Trung Kiên, Nguyễn Hiểu Minh, Nguyễn Nhật Minh, Khuất Văn
  Khang, Nguyễn Thái Sơn.
- Bảng C sau lượt 1: Uzbekistan thắng Philippines 5-1, đứng đầu bảng; Việt Nam và Kuwait cùng 1 điểm.
- Lượt 2 (18/9/2026): Việt Nam gặp Philippines (lần gần nhất 2 đội gặp nhau ở bán kết SEA Games 33,
  Việt Nam thắng 2-0).
- Thể thức: bóng đá nam Asiad 20 có 15 đội chia 4 bảng, đấu vòng tròn 1 lượt, chọn 4 đội nhất + 4
  đội nhì vào tứ kết.

## Ảnh (bước 5 ROUTINE.md)

`?image=d3e2d4edfcba` trả về ảnh định dạng `webp` (1200×720) — đã convert sang `.jpg` thật bằng
ffmpeg (không đổi nội dung, chỉ đổi container/encoding) tại `assets/img/article-hero.jpg`. Ảnh: HLV
Đinh Hồng Vinh trả lời họp báo tại Aichi-Nagoya 2026, có banner sự kiện + bảng tên "ĐINH HỒNG VINH"
phía trước — ảnh thật, có thể dùng làm Article Image Card / Hook theo B4 (ảnh og:image bài báo, có
dẫn nguồn, GREEN, không cần disclosure).

## Style dựng: 4-split-comparison

Chia đôi khung Việt Nam ↔ Kuwait xuyên suốt: What happened (ảnh trái/panel phải), Key facts (nhãn
trái/giá trị phải), Data moment (số Kuwait mờ/nhỏ bên trái "vs" số Việt Nam lớn/cam bên phải: 27 cú
dứt điểm), Context (bảng 2 cột đối xứng thống kê Việt Nam/Kuwait), Impact (chia đôi NGANG: bảng xếp
hạng bảng C / lịch lượt 2).
