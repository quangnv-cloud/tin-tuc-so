# BRIEF — Đội tuyển Việt Nam công bố danh sách dự FIFA ASEAN Cup 2026

Video tin nóng/trending kênh "Tin Tức Số" (khung 19/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kết quả/tin thể thao có yếu tố VN** (đội tuyển quốc gia Việt Nam, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá "danh sách đội tuyển việt nam" (id `9b781ee0a5ab`), `trafficApprox`
  **"1000+"**, vị trí #98/180 trong danh sách, `pubDate` 2026-09-18T23:50:00Z. `related` trỏ 3 báo VN
  uy tín: VnExpress ("Văn Hậu, Văn Lâm không dự FIFA ASEAN Cup 2026"), Tuổi Trẻ ("HLV Kim Sang Sik gọi
  2 cầu thủ Việt kiều Pháp và Anh lên tuyển Việt Nam"), Tạp chí Bóng Đá.
- `GET ?category=news` có bài đúng chủ đề, đầy đủ nhất: **Dân Trí**, id `288df262e098`, "Đội tuyển
  Việt Nam công bố danh sách tham dự FIFA ASEAN Cup 2026" — dùng `id` này cho cả `?article=` và
  `?image=` (ảnh báo chuẩn 2560×1706, không phải thumbnail Google nhỏ của item `trend`).
- **Nguồn thật dùng để dựng**: Báo Dân Trí (KHÔNG ghi "Google Trends" là nguồn).
- Đã POST đánh dấu used cả 2 id: `9b781ee0a5ab` và `288df262e098`, video slug
  `doi-tuyen-viet-nam-cong-bo-danh-sach-asean-cup-2026`.
- `claim_style` → `index: 4`, `style: "5-map-and-geo"` — khớp tự nhiên với bảng đấu có yếu tố địa lý
  rõ (3 đối thủ Đông Nam Á + Nam Á, thi đấu tại Indonesia).
- `trending_signal`: "danh sách đội tuyển việt nam — trafficApprox 1000+, vị trí #98/180 danh sách
  trend hôm nay".

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước)". Đây là tin công
bố danh sách triệu tập đội tuyển quốc gia Việt Nam — hoàn toàn trung lập, không đụng đời tư cầu thủ,
không hình sự/chính trị/cá độ. Lý do vắng mặt của các cầu thủ (chấn thương, trùng lịch Asiad) là thông
tin thể thao thuần tuý, không phải scandal. → **GREEN, APPROVE để dựng**.

(Đã lướt và LOẠI các chủ đề trending khác cùng khung giờ: phần lớn đầu danh sách `trend` là từ khoá
quá chung chung không đủ dữ kiện dựng 7 act ("gia lai", "a", "m", "z", "r", "vn", "game", "nhà", "xe",
"giàu" — BỎ); thể thao nước ngoài thuần giải trí không yếu tố VN (Bundesliga, La Liga Mexico, Serie A,
Premier League — Brentford/Chelsea, Bayern, Monaco, UFC — BỎ); chính trị — "tô lâm" (A1, BỎ NGAY);
hình sự — "bị can", "cướp", "bắt giữ", và trending "xe bán tải" thực chất là vụ án xương người trong
ô tô dưới lòng kênh (A1, BỎ); đời tư nghệ sĩ — "lan hương như cố", "ca sĩ", "the scandal" (A1, BỎ);
xổ số/cờ bạc-kề — "xsmb", "xổ số miền trung/nam" (RED nhóm, BỎ). Đã cân nhắc "vf wild" (VinFast Wild,
A2 ra mắt sản phẩm, trafficApprox 5000+) nhưng ảnh cả từ `trend` lẫn không có `news` item khớp chủ đề
đều chỉ là thumbnail Google ~300×180px, không đạt chuẩn ảnh minh hoạ brand → chọn chủ đề khác có ảnh
báo chuẩn. Danh sách đội tuyển Việt Nam vừa qua GATE A rõ ràng, vừa có ảnh báo chất lượng cao ở
`news`, nên được chọn.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Sáng 18/9/2026, huấn luyện viên Kim Sang Sik công bố danh sách 23 cầu thủ dự FIFA ASEAN Cup 2026.
- 2 tân binh Việt kiều lần đầu được triệu tập: Nguyễn Adou Leygley Minh ("Adou Minh", sinh 1997, gốc
  Việt - Pháp, trung vệ, câu lạc bộ Công An Hà Nội, đã có kinh nghiệm thi đấu V-League) và Williams
  Minh Hoàng (sinh 2007, gốc Việt - Anh, cao 1m90, câu lạc bộ Công An Thành phố Hồ Chí Minh).
- Vắng mặt: thủ môn Văn Lâm, hậu vệ Đoàn Văn Hậu, Nguyễn Văn Vĩ (chấn thương nặng), Đinh Quang Kiệt,
  tiền đạo Nguyễn Trần Việt Cường, Nguyễn Ngọc Mỹ. Quang Kiệt và Ngọc Mỹ đang cùng đội U23 Việt Nam dự
  Asiad (trùng lịch, không phải bị loại vì lý do chuyên môn/kỷ luật).
- Trở lại danh sách: Nguyễn Văn Việt, Lê Ngọc Bảo, Cao Pendant Quang Vinh.
- Huấn luyện viên Kim Sang Sik giữ phần lớn bộ khung vừa giúp đội tuyển Việt Nam vô địch ASEAN Cup
  gần nhất.
- FIFA ASEAN Cup 2026 diễn ra trong các ngày tập trung đội tuyển quốc gia theo lịch FIFA, tháng
  9-10/2026, quy tụ 14 đội tuyển chia 2 hạng đấu. Đội tuyển Việt Nam ở Division 1 (hạng 1), bảng B
  cùng Thái Lan, Philippines và Pakistan.
- Lịch thi đấu bảng B: Việt Nam gặp Philippines ngày 26/9 (19h30, sân Si Jalak Harupat, Bandung,
  Indonesia), gặp Thái Lan ngày 29/9, gặp Pakistan ngày 2/10 — 3 trận trong 7 ngày.
- (Đối chiếu nguồn: Dân Trí — bài chính dùng dựng nội dung; tiêu đề VnExpress "Văn Hậu, Văn Lâm không
  dự FIFA ASEAN Cup 2026" và Tuổi Trẻ "Huấn luyện viên Kim Sang Sik gọi 2 cầu thủ Việt kiều Pháp và
  Anh lên tuyển Việt Nam" trong `related` khớp cùng thông tin.)

## Ảnh (bước 5 ROUTINE.md)

`?image=288df262e098` (id item `news` Dân Trí) → ảnh báo thật 2560×1706px minh hoạ đội tuyển Việt
Nam, có dẫn nguồn. GREEN theo B4 (ảnh og:image bài báo, có dẫn nguồn, không cần disclosure).

## Style dựng: 5-map-and-geo

Ẩn dụ bản đồ khu vực bảng B (Việt Nam, Thái Lan, Philippines, Pakistan) + địa điểm thi đấu tại
Indonesia: What happened (badge nguồn dạng vòng tròn viền cam quanh icon nguồn), Key facts (bản đồ
Đông Nam Á/Nam Á outline mờ phía sau 3 fact, fact liên quan địa lý có icon ghim), Data moment (con số
chính "3 trận / 7 ngày" trong 1 map-pin phóng to, pin drop-in trước khi count-up), Context (bản đồ
với 3 vùng đối thủ highlight tuần tự theo thứ tự thi đấu — Philippines 26/9 → Thái Lan 29/9 → Pakistan
2/10, đường nối ra nhãn ngày), Impact (2 thẻ địa danh trượt vào từ 2 hướng: "giữ nguyên khung vô địch"
/ "tân binh Việt kiều hội nhập", nền bản đồ mờ full-frame).
