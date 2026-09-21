# BRIEF — TP HCM tăng 81 bậc trong bảng xếp hạng thành phố toàn cầu

Video tin nóng/trending kênh "Tin Tức Số" (khung 21/9/2026). Chủ đề chọn từ `category=news` (không
qua Google Trends, xem lý do bên dưới), QUA GATE A nhóm **A2 — tin đời sống/kinh tế đô thị tích cực,
trung lập** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend` (140 item, khung 19-20/9/2026): áp đảo là thể thao nước ngoài thuần giải trí
  không yếu tố VN (Ngoại hạng Anh MU/Arsenal/Liverpool/Man City, Serie A, Bundesliga, La Liga, CONCACAF
  Mexico, UFC), xổ số (`xsmb`/`xsmt`/`xsmn`, RED — cờ bạc/tài chính), từ khoá rác/quá chung chung
  (`24h`, `dân trí`, `vnexpress`, `báo mới`, `google`, `game`, các ký tự đơn lẻ). Có 2 mục có yếu tố cá
  nhân cần loại theo A1: `"phạm nhật vượng"` (đời tư/doanh nhân — không rõ góc trung lập, khả năng dính
  drama/tin đồn cá nhân) và `"tập cận bình"` (chính trị/đối ngoại — BỎ NGAY theo A1). Không còn mục nào
  trong `trend` vừa an toàn vừa đủ dữ kiện dựng 7 act.
- `GET ?category=news` (958 item, trang chủ VnExpress/Dân Trí/Tuổi Trẻ): rà các mục A1 cần loại (hình
  sự "Bắt khẩn cấp 7 đối tượng...", tai nạn cá nhân "Nam sinh lớp 10... tử vong", chính trị/đối ngoại
  "Ông Trump...", "Triều Tiên bắn tên lửa...", "Nga cảnh báo EU...", thể thao nước ngoài thuần giải trí
  Man Utd/Man City/Liverpool/Real Madrid). Chọn **"TP HCM tăng 81 bậc trong bảng xếp hạng thành phố
  toàn cầu"** (VnExpress Thời sự, id `86735e98ade6`, pubDate 2026-09-20T14:18:50Z) — tin đô thị/kinh
  tế tích cực, số liệu phong phú (điểm số, 5 nhóm tiêu chí, so sánh ASEAN/châu Á), không đụng cá nhân/
  chính trị/hình sự, `hasImage: true` với ảnh báo chuẩn (không phải thumbnail Google).
- **Không có ở `trend`** → `trending_signal` để rỗng theo mục 1.g của ROUTINE.md; lý do: khung giờ này
  Google Trends VN bị chi phối hoàn toàn bởi thể thao nước ngoài/xổ số/từ khoá rác, không có mục nào
  đạt A2/A3, nên dùng nguồn dự phòng `category=news` (đúng tinh thần bước 1.b của ROUTINE.md).
- **Nguồn thật dùng để dựng**: Báo VnExpress (Thời sự) — KHÔNG ghi "Google Trends" là nguồn.
- Đã POST đánh dấu used: `{"id":"86735e98ade6","video":"tp-hcm-tang-81-bac-xep-hang-thanh-pho-toan-cau"}`
  → phản hồi `{"ok":true}`.
- `claim_style` → `index: 7`, `style: "8-icon-grid"` — khớp tự nhiên với 5 nhóm tiêu chí (kinh tế /
  nhân lực / chất lượng sống / môi trường / quản trị) trình bày dạng lưới icon.

## GATE A — đánh giá

Nhóm **A2**: "Chính sách/kinh tế trung lập: số liệu tăng trưởng, xếp hạng thành phố... tin đời sống
tích cực". Đây là bảng xếp hạng đô thị độc lập (Oxford Economics, tổ chức nghiên cứu kinh tế Anh, có
phương pháp công khai), không phải xếp hạng do cơ quan VN tự công bố, không liên quan chính trị/nhân
sự/bầu cử. Nội dung là số liệu đo lường (điểm số, thứ hạng, so sánh khu vực) + 1 đạo luật đô thị mới
đã được Quốc hội thông qua (nêu nội dung quy định, không bình luận chính trị) → trung lập, xây dựng,
không gây hại. → **GREEN, APPROVE để dựng**.

(Đã lướt và LOẠI các chủ đề khác cùng khung giờ: thể thao nước ngoài không yếu tố VN — Ngoại hạng Anh,
Serie A, Bundesliga, La Liga, CONCACAF (A1, BỎ); xổ số `xsmb/xsmt/xsmn` — cờ bạc/tài chính (RED, BỎ
NGAY); chính trị/đối ngoại — Trump, Triều Tiên, Nga-EU, Tập Cận Bình, Iran (A1, BỎ NGAY); hình sự/tai
nạn cá nhân — vụ ô tô tông người TPHCM đang điều tra, nam sinh tử vong đuối nước (A1, BỎ NGAY); đời
tư doanh nhân "phạm nhật vượng" (A1, BỎ); bóng chuyền nữ Asiad 20 đã dựng video ngay video liền trước
`bong-chuyen-nu-viet-nam-tu-ket-asiad-20`, dùng lại sẽ trùng chủ đề gần nhất, không chọn.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- TP HCM xếp thứ **205/1.000** đô thị trong Global Cities Index 2026 của Oxford Economics, đạt **62,6
  điểm**; năm 2025 xếp thứ 286 → **tăng 81 bậc**. Nguồn: VnExpress Thời sự.
- 5 nhóm tiêu chí và điểm 2026: kinh tế **58**; nguồn nhân lực **65,7**; chất lượng sống **64,4**; môi
  trường **61,7**; quản trị **49,7**. Nguồn: VnExpress Thời sự.
- So với 2025: cải thiện 3/5 trụ cột — quản trị **tăng 194 bậc**, nguồn nhân lực **tăng 106 bậc**,
  kinh tế **tăng 69 bậc**. 2 trụ cột đi lùi — chất lượng sống **giảm 17 bậc**, môi trường **giảm 100
  bậc**. Nguồn: VnExpress Thời sự.
- Trong ASEAN, TP HCM xếp **thứ 5** sau Singapore (29), Kuala Lumpur (65), Bangkok (122), Jakarta
  (140), Manila (174); ở châu Á đứng sau Seoul (38), Thâm Quyến (93), trên Thượng Hải (216), Delhi
  (268), Mumbai (330). Nguồn: VnExpress Thời sự.
- TP HCM được Oxford Economics đưa vào nhóm **"Cities to Watch"** khu vực châu Á - Thái Bình Dương.
  Nguồn: VnExpress Thời sự.
- Ngày 24/8/2026, Quốc hội thông qua **Luật Phát triển đô thị** (465/474 đại biểu tán thành), hiệu
  lực từ 1/10/2026, đặt trọng tâm phân cấp/phân quyền cho các đô thị lớn. Nguồn: VnExpress Thời sự.
- Sau sáp nhập, TP HCM có hơn **14 triệu dân**, quy mô kinh tế **128 tỷ đô la Mỹ**, GDP bình quân đầu
  người **9.000 đô la Mỹ**; mục tiêu đến **2030** vào nhóm 100 thành phố toàn cầu, đến **2045** vào
  nhóm 100 đô thị chất lượng sống tốt nhất thế giới. Nguồn: VnExpress Thời sự (mục tiêu đã công bố
  chính thức, không phải suy đoán của routine).
- 2 trụ cột tụt hạng (chất lượng sống, môi trường) đang có kế hoạch cải thiện: kiểm soát ô nhiễm/chất
  lượng không khí, di dời nhà ven kênh, chỉnh trang đô thị. Nguồn: VnExpress Thời sự.

Lưu ý biên tập (đã đưa vào script để trung thực với nguồn): bài gốc lưu ý phương pháp luận Oxford
Economics thay đổi qua từng kỳ nên thứ hạng giữa các năm "không hoàn toàn là phép so sánh trực tiếp" —
đã giữ tinh thần này ở act Context, không chốt "tăng 81 bậc" như một con số tuyệt đối duy nhất.

## Ảnh

`assets/img/article-hero.jpg` — ảnh thật từ bài báo VnExpress (`?image=86735e98ade6`), toàn cảnh TP
HCM chụp từ trên cao (flycam), 1200×720 JPEG thật, không qua chỉnh sửa nội dung. Dùng cho Hook +
Article Image Card (B4/B5 — ảnh thật có dẫn nguồn).

## Style dựng (8-icon-grid, index 7)

5 nhóm tiêu chí (kinh tế / nhân lực / chất lượng sống / môi trường / quản trị) trình bày như lưới ô
icon — đúng ẩn dụ "Icon Grid" của style, khớp tự nhiên với cấu trúc dữ liệu gốc (Oxford Economics chấm
điểm theo đúng 5 nhóm này), không phải ép chủ đề vào style. Style dùng gần nhất là 7-timeline-chronology
(video liền trước) → đổi khác, đúng B7.

## 7 act

1. Hook — "TP HCM" to, tag "▲ Tăng 81 bậc" / "⚠ 2 mặt tụt hạng".
2. What happened — hạng 205/1.000 Global Cities Index 2026, tăng từ 286 (2025).
3. Key facts — điểm 62,6; 5 nhóm tiêu chí + điểm số từng nhóm.
4. Data moment — con số **81 bậc** giữa lưới 3 ô (2 ô phụ: quản trị +194, nhân lực +106).
5. Context — lưới 2×3 ô icon 5 tiêu chí (điểm + tăng/giảm bậc từng nhóm), khung dữ liệu chính của style.
6. Impact — 2 ô lớn: xếp hạng ASEAN (thứ 5) + mục tiêu đã công bố "2030 vào top 100 thành phố toàn
   cầu" (sự thật đã công bố, không suy đoán).
7. CTA — tăng hạng thật sự đáng mừng, hay cần nhìn kỹ 2 mặt tụt hạng (chất lượng sống, môi trường)?
