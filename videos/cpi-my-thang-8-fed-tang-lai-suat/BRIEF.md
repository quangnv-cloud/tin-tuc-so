# BRIEF — CPI Mỹ tháng 8 tăng 3,4%, cửa Fed tăng lãi suất vọt lên gần 90%

Video tin nóng/trending kênh "Tin Tức Số" (chạy tự động, khung giờ ngày 12/9/2026). Chủ đề phát
hiện từ Google Trends VN ("cpi mỹ"), đối chiếu tin nóng trang chủ báo lớn, QUA GATE A nhóm
**A2 — kinh tế trung lập, số liệu đã công bố** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"cpi mỹ"**, id `aefa3c383f79`, vị trí **#60/240** trong danh sách
  (sắp mới nhất trước), `trafficApprox` **"200+"**, `pubDate` 2026-09-11T12:50:00Z. `related` của
  item này trỏ 3 bài cùng chủ đề: Dân Trí ("Lạm phát dai dẳng, cửa Fed tăng lãi suất vọt lên 90%"),
  Fili.vn ("Nóng: CPI Mỹ tăng 3,4% trước thềm cuộc họp Fed"), Investing.com Việt Nam ("Giá tiêu
  dùng Mỹ tăng 0,4% trong tháng 8, đúng dự báo").
- `GET ?category=news`: cùng chủ đề có 2 bài liên quan trên báo lớn VN cùng ngày — Dân Trí ("CPI Mỹ
  tháng 8: Con số nào sẽ quyết định nước đi của Fed?", id `02c4923b9045`, bài viết TRƯỚC giờ công
  bố số liệu) và Tuổi Trẻ ("Chứng khoán 11-9: Dự báo VN-Index giằng co, 'nín thở' chờ tin CPI Mỹ tối
  nay", id `854fcfb5bef3`) — xác nhận chủ đề vừa đang trending vừa đã có báo chính thống VN đưa tin
  trước/trong ngày.
- Nguồn chính dùng cho văn bản: `?article=aefa3c383f79` → server tải hộ URL `related[0]` (Dân Trí,
  đường dẫn `dantri.com.vn/.../lam-phat-dai-dang-cua-fed-tang-lai-suat-vot-len-90-...htm`) →
  `ok:true`, text đầy đủ 6.449 ký tự, có số liệu cụ thể + trích phát biểu chuyên gia + tên Chủ tịch
  Fed đương nhiệm (Kevin Warsh) được chính bài báo nêu.
- Đã POST đánh dấu `used` cho id `aefa3c383f79` (video: `cpi-my-thang-8-fed-tang-lai-suat`).
- **Nguồn chính thức dùng cho video: Dân Trí** (KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là
  công cụ phát hiện chủ đề).
- Ảnh minh hoạ: `?image=02c4923b9045` (ảnh báo Dân Trí, chân dung Chủ tịch Fed Kevin Warsh tại một
  sự kiện/điều trần công khai — nhân vật được nêu tên trực tiếp trong bài viết dùng làm nguồn văn
  bản chính, ảnh báo chí thời sự thông thường, không dàn dựng). Đã cân nhắc thay bằng ảnh nhân viên
  văn phòng của Tuổi Trẻ (`?image=854fcfb5bef3`) nhưng chọn ảnh Dân Trí vì gắn trực tiếp với nhân vật
  trung tâm của tin (Chủ tịch Fed) thay vì ảnh minh hoạ chung chung, đồng thời giữ đồng nhất 1 nguồn
  (Dân Trí) cho cả text lẫn ảnh.

## GATE A

Nhóm **A2 — GREEN**: tin kinh tế vĩ mô trung lập (số liệu lạm phát Mỹ đã công bố chính thức bởi Cục
Thống kê Lao động Mỹ), không khuyến nghị đầu tư, không đụng đời tư/hình sự/chính trị VN/thể thao.
Có nhắc tên một quan chức công (Chủ tịch Fed) trong vai trò điều hành chính sách công khai — đây là
phát ngôn/chức vụ công vụ, không phải đời tư/drama cá nhân, nên KHÔNG rơi vào nhóm A1. Không nhắc
chi tiết xung đột địa chính trị (bài gốc có nhắc "căng thẳng Trung Đông" ảnh hưởng giá dầu — theo
đúng tiền lệ của video giá xăng dầu trước, KHÔNG đưa chi tiết này vào SCRIPT để tránh chạm nhóm A1
"đối ngoại/xung đột vũ trang", giữ trọng tâm 100% ở số liệu CPI/lãi suất).

Các chủ đề trending khác đã xét và loại ở Gate A (ghi lại để minh bạch):
- "câu lạc bộ bóng đá bắc ninh", "giải bóng đá vô địch các câu lạc bộ châu âu", "vô địch anh",
  "rennes đấu với marseille", "fiorentina vs", "sevilla – valencia", "west ham đấu với wrexham",
  "chelsea" và các cặp đấu châu Âu khác — thể thao nước ngoài thuần giải trí, không yếu tố VN → bỏ
  theo A1.
- "ngô thanh vân", "lan hương như cố" — đời tư/nghệ sĩ → bỏ theo A1.
- "cảnh sát", "tịch thu" — khả năng liên quan điều tra/an ninh cá nhân, tiêu đề mơ hồ, không đủ
  ngữ cảnh trung lập → bỏ để tránh rủi ro.
- "tổng thống pháp", "harald v của na uy" — chính trị/đối ngoại/nguyên thủ nước ngoài → bỏ theo A1.
- "vietlott" — liên quan xổ số/cờ bạc → bỏ theo A1 (18+/cờ bạc).
- "hit club" — không rõ ngữ cảnh, rủi ro liên quan giải trí người lớn/không xác định được nguồn báo
  chính thống → bỏ.
- "vùng áp thấp" — cùng nhóm chủ đề thời tiết đã dựng trong video khác gần đây
  (`khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`) → bỏ để tránh trùng lặp.
- "bảng xếp hạng v-league" — cùng nhóm bóng đá trong nước đã dựng gần đây
  (`v-league-vong-1-ban-thang-tang`) → bỏ để tránh trùng lặp chủ đề.
- "chính quyền địa phương", "đơn vị hành chính cấp xã", "bộ nội vụ" — liên quan tổ chức bộ máy
  hành chính nhà nước, nhạy cảm gần nhóm chính trị/nhân sự cấp cao → bỏ, chọn chủ đề an toàn hơn.
- "cpi mỹ" / "cpi" — **được chọn** (kinh tế vĩ mô trung lập, GREEN).

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

- Chỉ số giá tiêu dùng (CPI) Mỹ tháng 8 tăng 0,4% so với tháng trước, tăng 3,4% so với cùng kỳ năm
  ngoái, đúng dự báo của giới phân tích — theo số liệu Cục Thống kê Lao động Mỹ (BLS) — Dân Trí.
- CPI lõi (loại trừ thực phẩm, năng lượng) tăng 0,3% theo tháng, cao hơn dự báo 0,1 điểm phần trăm,
  đưa lạm phát lõi cả năm lên 2,4% — Dân Trí.
- Xác suất Fed tăng thêm 0,25 điểm phần trăm lãi suất trong cuộc họp tuần tới vọt từ khoảng 70% lên
  gần 90% ngay sau báo cáo, theo công cụ FedWatch của CME Group (ghi nhận từ CNBC, Wall Street
  Journal) — Dân Trí.
- Giá xăng tăng 3,9% trong tháng (đóng góp hơn 1/3 mức tăng CPI chung); cả năm giá xăng tăng 27,4%,
  dầu sưởi tăng 52%, chỉ số năng lượng nói chung tăng 16,3% — Dân Trí.
- Chi phí nhà ở tăng 0,3%; vé máy bay tăng 2,7% trong tháng (tăng 23,4% so với cùng kỳ); máy tính và
  phụ kiện tăng 3,8% do chi phí chip tăng; cước dịch vụ di động tăng 5,9% — Dân Trí.
- Lãi suất quỹ liên bang hiện ở biên độ 3,5-3,75% — Dân Trí.
- Thị trường lao động Mỹ đón nhận thêm 162.000 việc làm mới trong tháng 8, vượt dự báo — Dân Trí.
- Ngân hàng Trung ương châu Âu (ECB) tăng lãi suất một ngày trước đó, cảnh báo lạm phát còn neo cao
  — Dân Trí.
- Phiên sáng 11/9, chứng khoán Mỹ tăng điểm nhờ giá dầu hạ nhiệt: chỉ số Dow Jones tăng gần 600
  điểm (khoảng 1%); lợi suất trái phiếu chính phủ kỳ hạn 2 năm tăng lên 4,594% — Dân Trí.
- Chủ tịch Fed Kevin Warsh cùng FOMC sẽ quyết định tại cuộc họp chính sách tuần tới (thứ Tư) — Dân
  Trí (đây là lịch họp đã được xác nhận, KHÔNG phải suy đoán quyết định cuối cùng — SCRIPT chỉ nêu
  lịch họp + xác suất thị trường định giá, KHÔNG khẳng định Fed chắc chắn tăng lãi suất).
- Trích phát biểu: ông Chris Zaccarelli (Giám đốc đầu tư, Northlight Asset Management); bà Kathy
  Bostjancic (Kinh tế trưởng, Nationwide) — dùng làm ngữ cảnh BRIEF, KHÔNG đưa trích dẫn trực tiếp
  vào SCRIPT (giữ SCRIPT gọn trong số liệu + sự kiện chính).

## Cấu trúc 7 act (định hướng nội dung, style `2-chip-and-leaderboard`)

1. Hook: CPI Mỹ tháng 8 tăng 3,4%. Tag: "● LẠM PHÁT DAI DẲNG" / "● FED SẮP TĂNG LÃI SUẤT".
2. What happened (ảnh + panel + 2 chip viền cam "Tháng 8/2026" · "So với cùng kỳ"): Cục Thống kê
   Lao động Mỹ công bố CPI tháng 8 tăng 0,4% so với tháng trước, 3,4% so với cùng kỳ năm ngoái.
3. Key facts (watermark số khổng lồ mờ phía sau "2,4%" + 3 fact dọc phía trước): CPI lõi tăng 0,3%
   theo tháng, cao hơn dự báo; lạm phát lõi cả năm neo 2,4%; đúng dự báo ở chỉ số toàn phần.
4. Data moment (bảng xếp hạng ngang xác suất Fed): xác suất tăng lãi suất tuần tới nhảy từ ~70% lên
   gần 90% — hàng "gần 90%" tô cam, count-up.
5. Context (2-3 chip lớn xếp dọc): giá xăng tăng 3,9% trong tháng là động lực chính; thị trường lao
   động thêm 162 nghìn việc làm, vượt dự báo, củng cố khả năng Fed mạnh tay hơn.
6. Impact (sự thật đã xảy ra, watermark số mờ tiếp tục): chứng khoán Mỹ sáng 11/9 vẫn tăng điểm, Dow
   Jones tăng gần 600 điểm, lợi suất trái phiếu 2 năm lên khoảng 4,6%.
7. CTA: tăng lãi suất tuần tới — cần thiết để kiểm soát lạm phát, hay thêm áp lực thị trường? 2 lựa
   chọn đối lập "Cần thiết" / "Thêm áp lực".

## Style claim (đã gọi, KHÔNG gọi lại claim_style)

`POST {"action":"claim_style","video":"cpi-my-thang-8-fed-tang-lai-suat"}` →
`{"ok":true,"index":1,"style":"2-chip-and-leaderboard","claimed_at":"2026-09-12T00:27:36.353Z"}`.
