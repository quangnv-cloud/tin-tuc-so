# BRIEF — U23 Việt Nam thắng U23 Philippines 2-0, rộng cửa vào tứ kết Asiad 20 (2026)

Video tin nóng/trending kênh "Tin Tức Số" (khung 19/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kết quả thể thao có yếu tố VN** (đội tuyển U23 Việt Nam, GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: cụm từ khoá "đội tuyển bóng đá u-23 quốc gia philippines đấu với u-23 việt
  nam" (id `a6d6a6019385`), `trafficApprox`: **"20000+"** (vị trí #78/162 trong danh sách, đã sắp
  mới nhất trước), `pubDate` 2026-09-18T06:10:00Z. `related` trỏ báo VN uy tín: Lao Động, Báo Lào
  Cai điện tử, VnExpress — cả 3 đều tường thuật trực tiếp trận đấu.
- `GET ?category=news` có bài tổng kết trận đấu đầy đủ nhất, đã có kết quả chung cuộc: **Dân Trí**,
  id `035eb7329b35`, "U23 Việt Nam thắng U23 Philippines, rộng cửa vào tứ kết Asiad 20" — dùng `id`
  này cho cả `?article=` và `?image=` (đúng chủ đề, đủ số liệu, ảnh báo chuẩn, có tỷ số cuối cùng —
  item `trend` chỉ dừng ở tỷ số 0-0 hiệp một do fetch giữa trận).
- **Nguồn thật dùng để dựng**: Báo Dân Trí (KHÔNG ghi "Google Trends" là nguồn).
- Đã POST đánh dấu used: `{"id":"035eb7329b35","video":"u23-viet-nam-thang-philippines-vao-tu-ket-asiad-2026"}`.
- `claim_style` → `index: 3`, `style: "4-split-comparison"` — khớp tự nhiên với thế đối đầu 2 đội
  (Việt Nam ↔ Philippines).
- `trending_signal`: "đội tuyển bóng đá u-23 quốc gia philippines đấu với u-23 việt nam — trafficApprox 20000+ (vị trí #78/162 danh sách trend)".

## GATE A — đánh giá

Nhóm **A2**: "Kết quả thể thao có yếu tố VN (đội tuyển VN, VĐV VN, giải trong nước)". Đây là đội
tuyển U23 quốc gia Việt Nam thi đấu tại Asiad 20 (Á vận hội) — giải đấu cấp châu lục có yếu tố VN rõ
ràng, không phải "thể thao nước ngoài thuần giải trí". Không đụng đời tư cầu thủ, không có yếu tố
hình sự/chính trị/cá độ. Tường thuật kết quả + diễn biến trận đấu, trung lập, không giật gân.
→ **GREEN, APPROVE để dựng**.

(Đã lướt và LOẠI các chủ đề trending khác cùng khung giờ trước khi chọn chủ đề này: phần lớn đầu danh
sách `trend` là thể thao nước ngoài thuần giải trí không yếu tố VN — Premier League (Brentford,
Chelsea), Bundesliga (Bayern, Union Berlin), Ligue 1 (Monaco, Lens), Serie A (Monza, Sassuolo) (A1,
BỎ); chính trị — "tô lâm" (A1, BỎ NGAY); an ninh/hình sự cá nhân — "cướp", "bắt giữ", "siết cổ", "học
viện an ninh nhân dân" (A1, BỎ); đời tư nghệ sĩ — "trấn thành", "ngọc trinh", "đàm vĩnh hưng", "the
scandal" (A1, BỎ); từ khoá quá chung chung không đủ dữ kiện xây 7 act — "xe", "an ninh", "y tế",
"điện thoại", "doanh nghiệp", "sinh viên" (BỎ); xổ số/cá cược — "xsmb", "xổ số miền trung/nam" (RED,
BỎ NGAY). U23 Việt Nam – Philippines là chủ đề thể thao có yếu tố VN rõ ràng, trafficApprox cao nhất
trong nhóm A2 hôm nay, vừa có ở `trend` vừa có bài tổng kết đầy đủ ở `news` với ảnh báo chuẩn và kết
quả chung cuộc đã ngã ngũ.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Trận đấu: U23 Việt Nam – U23 Philippines, vòng bảng (bảng C) môn bóng đá nam Asiad 20 (Á vận hội
  lần thứ 20), sân CS Asset Minato, Nagoya (Nhật Bản), chiều 18/9/2026. HLV trưởng U23 Việt Nam:
  Đinh Hồng Vinh.
- Kết quả: U23 Việt Nam thắng U23 Philippines **2-0**.
- Diễn biến: hiệp một U23 Việt Nam kiểm soát bóng 73% nhưng chưa ghi bàn (Minh Phúc, Ngọc Mỹ có cơ
  hội nhưng chưa thành bàn); hiệp hai, phút 74 Thanh Nhàn dứt điểm mở tỷ số từ đường chuyền dài của
  Đức Anh; phút 87 Lê Phát đánh đầu bồi nhân đôi cách biệt, ấn định thắng lợi 2-0.
  (Đối chiếu 2 nguồn: Dân Trí — bài chính dùng dựng nội dung, có tường thuật diễn biến chi tiết theo
  phút; VnExpress "Việt Nam hạ Philippines, sáng cửa vào tứ kết ASIAD 2026" cùng khớp tỷ số 2-0 và
  kết quả trận đấu.)
- Bối cảnh/ý nghĩa: chiến thắng giúp U23 Việt Nam tạm xếp nhì bảng C và rộng cửa giành vé vào tứ kết
  Asiad 20; cùng ngày U23 Uzbekistan thắng U23 Kuwait, trao thêm cơ hội cho U23 Việt Nam đi tiếp
  (theo tiêu đề bài liên quan trên Dân Trí trong `category=news`, dùng làm bối cảnh, KHÔNG phải nội
  dung chính, không trích số liệu trận đó vì không có trong bài đã tải).

## Ảnh (bước 5 ROUTINE.md)

`?image=035eb7329b35` (id item `news` Dân Trí) → ảnh báo thật, hai cầu thủ U23 Việt Nam (áo số 3 và
22) ăn mừng trên sân, có dẫn nguồn. GREEN theo B4 (ảnh og:image bài báo, có dẫn nguồn, không cần
disclosure).

## Style dựng: 4-split-comparison

Chia khung theo thế đối đầu Việt Nam ↔ Philippines xuyên suốt 5 act giữa: What happened (chia dọc
ảnh trái/panel phải, vạch cam giữa), Key facts (mỗi fact 1 hàng chia đôi nhãn trái/giá trị phải),
Data moment (tỷ số 2-0 hai bên vạch "–" ở giữa, số Philippines mờ/nhỏ bên trái, số Việt Nam lớn/cam
bên phải, vạch giữa pulse), Context (bảng 2 cột đối xứng ghi kiểm soát bóng / bảng xếp hạng bảng C),
Impact (chia đôi NGANG — trên: rộng cửa tứ kết; dưới: lợi thế từ kết quả Uzbekistan-Kuwait).
