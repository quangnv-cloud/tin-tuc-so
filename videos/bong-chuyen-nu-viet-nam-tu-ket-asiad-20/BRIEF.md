# BRIEF — Bóng chuyền nữ Việt Nam thua Hàn Quốc, gặp Trung Quốc ở tứ kết Asiad 20 (2026)

Video tin nóng/trending kênh "Tin Tức Số" (khung 20/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kết quả thể thao có yếu tố VN** (đội tuyển bóng chuyền nữ Việt Nam, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"bóng chuyền nữ"** (id `c52cc3de20af`), `trafficApprox` **"2000+"**,
  `related` trỏ 3 báo VN uy tín cùng chủ đề: VnExpress ("Việt Nam gặp Trung Quốc ở tứ kết bóng chuyền
  nữ ASIAD 2026"), VietNamNet ("Trực tiếp bóng chuyền nữ Việt Nam 0-2 Hàn Quốc"), Dân Trí ("Thua Hàn
  Quốc, tuyển bóng chuyền nữ Việt Nam gặp Trung Quốc ở tứ kết Asiad") — cùng đưa 1 sự kiện.
- `GET ?category=news` có bài đúng chủ đề, đủ số liệu, ảnh báo chuẩn: **VnExpress Thể thao**, id
  `a9fb3290cdc9`, "Việt Nam gặp Trung Quốc ở tứ kết bóng chuyền nữ ASIAD 2026" (`pubDate`
  2026-09-18T09:56:16Z ≈ 16h56 giờ VN) — dùng `id` này cho cả `?article=` và `?image=` (đúng chủ đề,
  đủ chi tiết, ảnh báo chuẩn không phải thumbnail Google).
- **Nguồn thật dùng để dựng**: Báo VnExpress (Thể thao) — KHÔNG ghi "Google Trends" là nguồn.
- Đã POST đánh dấu used: `{"id":"a9fb3290cdc9","video":"bong-chuyen-nu-viet-nam-tu-ket-asiad-20"}`.
- `claim_style` → `index: 6`, `style: "7-timeline-chronology"` — khớp tự nhiên với diễn biến trận đấu
  theo set (set 1 → set 2 → set 3 kịch tính → set 4) và hành trình đối đầu Hàn Quốc 2023 → 2026.
- `trending_signal`: "bóng chuyền nữ — trafficApprox 2000+ (xuất hiện ở cả trend và news cùng ngày)".

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước)". Đội tuyển bóng
chuyền nữ Việt Nam thi đấu tại Á vận hội (Asiad) 20 — giải đấu thể thao châu lục có đoàn Việt Nam
tham dự chính thức, không phải "thể thao nước ngoài thuần giải trí". Tường thuật kết quả + diễn biến
trận đấu bằng số liệu (tỷ số set, đội hình, lịch sử đối đầu), trung lập, không khai thác đời tư vận
động viên, không có yếu tố hình sự/chính trị/cá độ.
→ **GREEN, APPROVE để dựng**.

(Đã lướt và LOẠI các chủ đề trending khác cùng khung giờ trước khi chọn chủ đề này: phần lớn đầu danh
sách `trend` là thể thao nước ngoài thuần giải trí không yếu tố VN — UFC, Serie A, Ngoại hạng Anh
Arsenal/Newcastle/Everton/Tottenham/Chelsea, Bundesliga Bayern, Ligue 1 Monaco, La Liga Espanyol,
CONCACAF/Liga MX Mexico (A1, BỎ); chính trị cấp cao — "tô lâm" (A1, BỎ NGAY); hình sự — "bị can",
"cướp", "bắt giữ" (A1, BỎ NGAY); từ khoá quá chung chung/rác không đủ dữ kiện xây 7 act — "xsmb",
"xsmt", "xsmn" (xổ số — tài chính/cờ bạc, RED, BỎ), "dân trí", "vnexpress", "tin tuc 24h", "24h",
"báo mới", "google", "flashscore", các ký tự đơn lẻ "a"/"o"/"m"/"z"/"r" (nhiễu Trends, BỎ). Bóng chuyền
nữ Việt Nam là chủ đề thể thao có yếu tố VN rõ ràng, xuất hiện ở cả `trend` (2000+) và `news` (nhiều
báo lớn cùng đưa), trận tứ kết diễn ra đúng hôm nay 20/9 — tính thời sự cao nhất trong các lựa chọn
an toàn.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Trận đấu: Việt Nam – Hàn Quốc, lượt cuối vòng bảng D môn bóng chuyền nữ Asiad 20, chiều 18/9/2026.
  Kết quả: Việt Nam thua 1 set thắng – 3 set thua (set 1: thua 19-25; set 2: thua 21-25; set 3:
  thắng kịch tính 28-26 sau khi bỏ lỡ 5 set-point liên tiếp, thành công ở lần thứ 6 nhờ Phạm Quỳnh
  Hương phát bóng ăn điểm trực tiếp; set 4: thua 18-25). Nguồn: VnExpress Thể thao.
- Vì thua, Việt Nam xếp nhì bảng D (Hàn Quốc nhất bảng); đội nhì bảng D phải gặp Trung Quốc — đội
  đang giữ huy chương vàng 2 kỳ Á vận hội liên tiếp gần nhất — ở tứ kết. Trận tứ kết diễn ra ngày
  20/9/2026 (hôm nay), sau 1 ngày nghỉ. Nếu thua, đội tuyển tiếp tục thi đấu vòng phân hạng 5-8.
  Nguồn: VnExpress Thể thao.
- Đội hình chính HLV Nguyễn Tuấn Kiệt sử dụng: đội trưởng Trần Thị Thanh Thúy, cùng Võ Thị Kim Thoa,
  Trần Thị Bích Thủy, Lê Như Anh, và bộ đôi tuổi teen Bùi Thị Ánh Thảo, Phạm Quỳnh Hương. Nguồn:
  VnExpress Thể thao.
- Lịch sử đối đầu: năm 2023 (Asiad 19 và giải vô địch châu Á), Việt Nam từng thắng Hàn Quốc 2 lần ở
  vòng bảng; nhưng 2 trận gần nhất trước ngày 18/9/2026, Việt Nam đều thua Hàn Quốc. Nguồn: VnExpress
  Thể thao.
- Đối chiếu chéo: VietNamNet ("Trực tiếp bóng chuyền nữ Việt Nam 0-2 Hàn Quốc") và Dân Trí ("Thua Hàn
  Quốc, tuyển bóng chuyền nữ Việt Nam gặp Trung Quốc ở tứ kết Asiad") cùng xác nhận kết quả thua và
  đối thủ tứ kết là Trung Quốc — khớp với bài VnExpress dùng làm nguồn chính.

## Ảnh

`assets/img/article-hero.jpg` — ảnh thật từ bài báo VnExpress (`?image=a9fb3290cdc9`), cầu thủ đội
tuyển bóng chuyền nữ Việt Nam áo trắng có quốc kỳ, 1200×720, đã convert từ webp sang jpg thật (Pillow).
Không qua chỉnh sửa nội dung. Dùng cho Hook + Article Image Card (B4/B5 — ảnh thật có dẫn nguồn).

## Style dựng (7-timeline-chronology, index 6)

Trục thời gian dọc xuyên suốt: lịch sử đối đầu 2023 → 2 trận thua gần nhất → 4 set trận đấu 18/9 →
tứ kết hôm nay 20/9 gặp Trung Quốc. Đúng ẩn dụ "timeline" của style — không phải chọn ép, khớp tự
nhiên với dữ kiện.

## 7 act

1. Hook — đội tuyển bóng chuyền nữ Việt Nam, tag "Thua kịch tính" / "Tứ kết hôm nay".
2. What happened — thua ngược Hàn Quốc, nhì bảng D, gặp Trung Quốc tứ kết.
3. Key facts — HLV + đội hình chính.
4. Data moment — set 3 kịch tính, cứu 5 cơ hội kết thúc set.
5. Context — timeline đối đầu Hàn Quốc 2023 → nay + diễn biến 4 set.
6. Impact — nhánh đấu khó hơn, gặp đương kim vô địch 2 kỳ Trung Quốc ngay tứ kết.
7. CTA — tạo bất ngờ hay dừng bước trước Trung Quốc?
