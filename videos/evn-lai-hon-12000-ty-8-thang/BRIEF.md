# BRIEF — EVN lãi hơn 12.200 tỷ đồng trong 8 tháng, xoá sạch lỗ luỹ kế (2026)

Video tin nóng/trending kênh "Tin Tức Số" (khung 18/9/2026). Chủ đề phát hiện từ Google Trends VN,
QUA GATE A nhóm **A2 — kinh tế trung lập** (doanh nghiệp nhà nước công bố số liệu tài chính định kỳ), GREEN.

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá "tập đoàn điện lực việt nam" (id `8505bab4f7a6`), `trafficApprox`
  "200+", `pubDate` 2026-09-17T22:00:00Z. `related` trỏ 3 báo VN uy tín cùng chủ đề: Tuổi Trẻ,
  VnExpress, VnEconomy.
- `GET ?category=news` có bài đầy đủ nhất đúng chủ đề: **Tuổi Trẻ**, id `d4ba160e0146`, "EVN lãi hơn
  12.000 tỉ đồng trong 8 tháng, sắp tới giá điện có giảm?" — dùng `id` này cho cả `?article=` và
  `?image=` (đúng chủ đề, đủ số liệu, ảnh báo chuẩn 1200×750px).
- Đối chiếu nguồn thứ 2: **Dân Trí**, id `18306b4e1b14`, "EVN lãi 8.631 tỷ đồng nửa đầu năm, vì sao
  giá vốn tăng mạnh?" — cung cấp số liệu quý 2 / công ty mẹ để đối chiếu đà tăng trưởng.
- Nguồn thật dùng để dựng: Báo Tuổi Trẻ (chính) + Báo Dân Trí (đối chiếu). KHÔNG ghi "Google Trends"
  là nguồn.
- Đã POST đánh dấu used: `{"id":"8505bab4f7a6","video":"evn-lai-hon-12000-ty-8-thang"}` → `{"ok":true}`.
- `claim_style` → `{"ok":true,"index":1,"style":"2-chip-and-leaderboard"}`.
- `trending_signal`: "tập đoàn điện lực việt nam — trafficApprox 200+, xuất hiện đồng thời ở trend
  và news (3 báo Tuổi Trẻ/VnExpress/VnEconomy cùng đưa tin trong ngày 17/9)".

## GATE A — đánh giá

Nhóm **A2**: "Kinh tế trung lập: số liệu tăng trưởng, doanh nghiệp mở rộng/đầu tư, thị trường lao
động". Đây là công bố tài chính định kỳ của một tập đoàn nhà nước tại cuộc họp với Phó Thủ tướng
Thường trực, số liệu do chính EVN công bố — không phải suy đoán/tin đồn. Không đụng cá nhân, không
drama, không chính trị bầu cử/nhân sự cấp cao. Bài gốc có câu hỏi mở "giá điện có giảm?" nhưng cả bài
gốc lẫn video đều KHÔNG khẳng định chắc chắn sẽ giảm, chỉ nêu EVN đã báo cáo phương án giá theo đúng
cơ chế Nghị định 72/278 (sự thật đã xảy ra) — câu hỏi "giảm hay không" chỉ đặt ở act CTA dưới dạng mời
tranh luận, không chốt như sự thật (đúng B1). → **GREEN, APPROVE để dựng.**

(Đã lướt và LOẠI các chủ đề trending khác trong danh sách hôm nay trước khi chọn chủ đề này: phần lớn
danh sách là bóng đá châu Âu không yếu tố VN — La Liga, Europa League, EFL Cup, Man City, Barcelona,
Sunderland, Juventus... (A1, BỎ); các trận U-23 châu Á không có Việt Nam — Philippines, Hồng Kông,
Iran, Thái Lan, UAE (A1, BỎ vì không yếu tố VN — riêng tin "U23 Việt Nam đấu Philippines" ở
`category=news` mới chỉ là "dự đoán tỉ số"/lịch thi đấu, TRẬN CHƯA DIỄN RA, chưa có kết quả thật để
tường thuật nên không dùng được); chính trị — "tô lâm" (A1, BỎ NGAY); đời tư nghệ sĩ — "ninh dương lan
ngọc", "hoài lâm", "ca sĩ", "khánh my" (A1, BỎ); tai nạn/thảm kịch cá nhân — "vụ nổ" (tủ lạnh phát nổ 4
người tử vong), "xe cứu thương" (tai nạn cao tốc 4 người bị thương) (A1, BỎ); "nghệ sĩ nhân dân" —
tin buồn NSND qua đời, cân nhắc loại vì gần nhóm tưởng niệm cá nhân, rủi ro không cần thiết (BỎ); chủ
đề thời tiết "vùng áp thấp"/"áp thấp nhiệt đới" ban đầu có vẻ là A2 nhưng khi đọc `?article=` xác nhận
đây là áp thấp LPA 09d ngoài khơi Philippines theo dự báo PAGASA, di chuyển hướng Nhật Bản, **KHÔNG
ảnh hưởng Việt Nam** — loại bỏ vì gắn với khán giả VN sẽ sai sự thật; mưa lũ ngập lụt miền Bắc đang
diễn ra thật (nhiều bài `news`) nhưng đã là chủ đề video `mien-bac-mua-lon-ngap-ha-noi` (15/9) và có
rủi ro B2 nếu nhấn vào số liệu thương vong — cân nhắc kỹ, quyết định BỎ lượt này, ưu tiên chủ đề an
toàn hơn; "bảo hiểm y tế" gắn với gian lận/truy tố (BỎ, tránh nhóm hình sự); "đèn giao thông" gắn với
1 vụ tai nạn cụ thể (BỎ); "thuế", "chung cư", "nhiệm kỳ" quá chung chung không đủ dữ kiện dựng 7 act
(BỎ); xổ số các miền chỉ là kết quả định kỳ, không có giá trị biên tập (BỎ). Chủ đề EVN vừa có ở
`trend` vừa có nhiều bài ở `news` từ các báo độc lập, số liệu rõ ràng, kinh tế trung lập, an toàn nhất
trong danh sách hôm nay.)

## Nội dung xác nhận từ nguồn (claims_verified — dùng cho COMPLIANCE.md)

- Toàn Tập đoàn Điện lực Việt Nam, 8 tháng đầu năm 2026: doanh thu 482.042 tỷ đồng (70% kế hoạch
  năm); lợi nhuận ước đạt 12.215 tỷ đồng (103% kế hoạch); nộp ngân sách nhà nước khoảng 17.160 tỷ
  đồng (65% kế hoạch) — theo Tuổi Trẻ, dẫn báo cáo của Chủ tịch EVN Đặng Hoàng An tại cuộc họp do Phó
  Thủ tướng Thường trực Phạm Gia Túc chủ trì.
- Đến 30/6/2026, EVN xử lý hết số lỗ luỹ kế tích tụ từ các năm khó khăn 2022-2023 — theo Tuổi Trẻ.
- Mục tiêu cả năm 2026: lợi nhuận trên 13.500 tỷ đồng, nộp ngân sách trên 26.300 tỷ đồng — theo Tuổi
  Trẻ.
- EVN đã báo cáo Bộ Công Thương phương án giá bán lẻ điện bình quân năm 2026 theo cơ chế Nghị định 72
  (đã sửa đổi, bổ sung bởi Nghị định 278/2026, ban hành 9/7/2026) — theo Tuổi Trẻ. Đây là bước thủ tục
  định kỳ, KHÔNG phải cam kết giảm giá điện — video KHÔNG khẳng định giá điện sẽ giảm hay tăng.
- Đối chiếu Dân Trí: công ty mẹ EVN lãi 8.631 tỷ đồng trong 6 tháng đầu năm (tăng 26,2% so với cùng
  kỳ); riêng quý 2 lợi nhuận gộp giảm 74,6% còn 3.154 tỷ đồng (biên lợi nhuận gộp co lại 1,9%) do giá
  vốn tăng nhanh hơn doanh thu (cao điểm mùa nắng nóng); chi phí tài chính giảm hơn 72% (từ 6.643 tỷ
  xuống 1.835 tỷ đồng, chủ yếu do lỗ tỷ giá chưa thực hiện giảm mạnh) — nguồn tự nhận định "lợi nhuận
  chịu tác động trái chiều", dùng làm cơ sở cho khung "bù đắp" trong video. Đây là số liệu công ty mẹ
  (phạm vi hẹp hơn "toàn tập đoàn" 8 tháng ở trên) — SCRIPT.md ghi rõ "công ty mẹ" khi dùng số liệu
  này để không gây nhầm lẫn phạm vi (đúng B1).

## Ảnh (bước 5 ROUTINE.md)

`?image=d4ba160e0146` (id item `news` Tuổi Trẻ) → ảnh báo thật 1200×750px, có dẫn nguồn, không chỉnh
sửa nội dung. GREEN theo B4.

## Style dựng: 2-chip-and-leaderboard (index 1)

- **What happened**: ảnh + panel, 2 chip số liệu viền cam ("8 tháng đầu năm 2026" · "Đã xoá sạch lỗ
  luỹ kế").
- **Key facts**: watermark số "12.215" mờ phía sau, 3 fact xếp dọc (doanh thu 482.042 tỷ · lợi nhuận
  12.215 tỷ (103% kế hoạch) · nộp ngân sách 17.160 tỷ).
- **Data moment**: bảng xếp hạng ngang 3 hàng thể hiện đà tăng lợi nhuận qua các mốc (công ty mẹ 6
  tháng 8.631 tỷ → toàn tập đoàn 8 tháng 12.215 tỷ → mục tiêu cả năm trên 13.500 tỷ), hàng "8 tháng"
  (mốc chính, đã xảy ra) tô cam, thanh chạy count-up.
- **Context**: 2 chip lớn xếp dọc — quý 2 lợi nhuận gộp co lại còn 1,9% biên lãi gộp (rủi ro, tô đỏ)
  / chi phí tài chính giảm hơn 72% bù đắp (điểm tích cực, tô cam).
- **Impact**: 2 chip tác động — đã xoá sạch lỗ luỹ kế + đã báo cáo phương án giá điện 2026 theo đúng
  lộ trình Nghị định 72/278 (sự thật đã xảy ra, KHÔNG suy đoán giá tăng/giảm).
- **CTA**: câu hỏi tranh luận "khoản lãi nên ưu tiên giảm giá điện hay đầu tư lưới điện?" + 2 lựa
  chọn đối lập + pill "Bình luận quan điểm của bạn".
