# BRIEF — Apple hé lộ iPhone 18 Pro, có thể lên kệ Việt Nam ngày 18/9

Video tin nóng/trending kênh "Tin Tức Số" (khung SÁNG 9/9/2026). Chủ đề phát hiện từ Google Trends VN
("iphone 18"), đối chiếu với tin nóng trang chủ báo lớn, QUA GATE A nhóm **A2 — ra mắt sản phẩm/công
nghệ** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)
- `GET ?category=trend`: từ khoá **"iphone 18"**, id `a2705a0b0cb0`, vị trí #29/93 trong danh sách
  (sắp theo mới nhất trước), `trafficApprox` **"500+"**, `pubDate` 2026-09-08T17:40:00Z.
- Trend item `link`/`related[0]` đã trỏ thẳng bài **VnExpress**: "Chân dung iPhone 18 Pro trước lễ ra
  mắt" — dùng `id` này (`a2705a0b0cb0`) cho `?article=` (server tải bài VnExpress) và cho ảnh dự
  phòng.
- Đối chiếu `GET ?category=news`: có bài cùng chủ đề trên **Dân Trí**, id `6ef106aee66f` — "iPhone 18
  Pro Max có thể lên kệ tại Việt Nam từ sáng 18/9" (dantri.com.vn) — dùng `id` này cho `?image=`
  (ảnh báo chuẩn, không phải thumbnail Google nhỏ của trend). `?article=6ef106aee66f` trả `ok:false`
  (trang không parse được) nên KHÔNG dùng làm nguồn văn bản — chỉ dùng làm nguồn đối chiếu tiêu đề
  (2 nguồn độc lập cùng xác nhận mốc 18/9 tại Việt Nam: chính bài VnExpress cũng có link liên quan
  "iPhone 18 Pro có thể bán tại Việt Nam ngày 18/9" ngay trong nội dung tải về).
- Cả 2 id đã POST đánh dấu `used` (video: `iphone-18-ra-mat-viet-nam`).
- **Nguồn chính thức dùng cho video: VnExpress** (KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là
  công cụ phát hiện chủ đề).
- Ảnh minh hoạ: `?image=6ef106aee66f` (ảnh báo Dân Trí, đã lưu `assets/img/article-hero.jpg`, 540×360,
  JPEG thật — không phải AI tạo, không watermark).

## GATE A
Nhóm **A2 — GREEN**: ra mắt/cập nhật sản phẩm công nghệ (iPhone 18 Pro/Pro Max). Không đụng đời tư,
không hình sự, không chính trị, không thể thao. An toàn để dựng.

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

Nguồn: VnExpress — "'Chân dung' iPhone 18 Pro trước lễ ra mắt", 8/9/2026.
https://vnexpress.net/chan-dung-iphone-18-pro-truoc-le-ra-mat-5117725.html
(Đối chiếu: Dân Trí — "iPhone 18 Pro Max có thể lên kệ tại Việt Nam từ sáng 18/9", 8/9/2026,
https://dantri.com.vn/cong-nghe/iphone-18-pro-max-co-the-len-ke-tai-viet-nam-tu-sang-189-20260908150248598.htm
— dùng để xác nhận mốc "18/9" + góc thị trường Việt Nam.)

- Sự kiện Apple **"Surprise and Shine"** diễn ra **ngày 9/9/2026** tại Apple Park (Mỹ) — Apple dự
  kiến trình làng **iPhone 18 Pro và iPhone 18 Pro Max**, cùng một smartphone gập mới. Bản iPhone 18
  tiêu chuẩn và iPhone Air 2 dự kiến đợi đến nửa đầu năm sau.
- Kích thước màn hình giữ nguyên **6,3 inch (Pro) và 6,9 inch (Pro Max)** như thế hệ trước, nhưng độ
  sáng màn hình được cho là tăng mạnh từ **1.600 nit lên 3.000 nit** (nguồn: Instant Digital, dẫn lại
  qua VnExpress).
- "Bộ não" mới: chip **Apple A20 Pro**, sản xuất trên tiến trình **2 nm** của TSMC (quy trình N2,
  kiến trúc bóng bán dẫn Gate-All-Around) — hiệu năng cao hơn **10–15%**, tiết kiệm điện hơn
  **25–30%** so với thế hệ chip 3 nm.
- Giao diện bộ nhớ chuyển sang **LPDDR5x 96-bit** (rộng hơn 50% so với 64-bit trước) — ước tính hiệu
  năng GPU tăng khoảng **20–30%** (theo Digitimes, dẫn lại qua VnExpress).
- Pin: bản iPhone 18 Pro Max (eSIM) khoảng **5.425 mAh**, cao hơn mức **5.088 mAh** của iPhone 17 Pro
  Max (theo MacWorld, dẫn lại qua VnExpress).
- Giá dự kiến tăng: nhiều hãng nghiên cứu thị trường đưa dự đoán KHÁC NHAU — TrendForce dự báo tăng
  **150–200 đô la Mỹ**; Cnet cho rằng mức tăng **100 đô la Mỹ** khả thi hơn; IDC ước tính **200 đô la
  Mỹ**; nhà phân tích Jeff Pu dự đoán **250–300 đô la Mỹ**. → Video dùng cách nói "khoảng 100 đến 300
  đô la Mỹ tuỳ dự đoán" (KHÔNG chốt 1 số duy nhất vì các nguồn chênh lệch — đây là DỰ ĐOÁN, không phải
  giá chính thức).
- Giá chip nhớ 256 GB đã tăng gần **400%** so với cùng kỳ năm ngoái (đã xảy ra, không phải dự đoán) —
  khiến tổng chi phí nguyên vật liệu một chiếc iPhone Pro bản 256 GB ước tính cao hơn **38%** so với
  trước (theo TrendForce, dẫn lại qua VnExpress).
- iPhone 17 Pro ra mắt năm ngoái có giá khởi điểm **1.099 đô la Mỹ**; iPhone 17 Pro Max **1.199 đô la
  Mỹ**.
- Lịch trình: ra mắt **9/9**, mở đặt hàng từ **12/9**, đến tay người dùng đầu tiên từ **18/9**. Cùng
  mốc này, thông tin từ Dân Trí cho biết iPhone 18 Pro Max **có thể lên kệ tại Việt Nam từ sáng
  18/9** — dùng "có thể" (chưa xác nhận chính thức từ Apple Việt Nam).

## Cấu trúc 7 act (dùng ĐÚNG các số liệu trên, không thêm)
1. **Hook**: "iPhone 18 Pro" TO + badge nguồn VnExpress + ngày 8/9 + 2 tag tương phản: "● Camera & chip
   nâng cấp mạnh" / "● Giá có thể tăng".
2. **What happened**: Apple ra mắt iPhone 18 Pro/Pro Max tại sự kiện "Surprise and Shine" ngày 9/9 tại
   Apple Park.
3. **Key facts**: chip A20 Pro tiến trình 2nm; màn hình sáng hơn (1.600→3.000 nit); RAM LPDDR5x 96-bit
   (GPU +20–30%).
4. **Data moment**: giá có thể tăng thêm khoảng 100–300 đô la Mỹ (tuỳ dự đoán các hãng phân tích).
5. **Context**: lịch trình ra mắt 9/9 → đặt hàng 12/9 → đến tay người dùng 18/9; có thể lên kệ tại
   Việt Nam cùng ngày 18/9.
6. **Impact (sự thật đã xảy ra)**: giá chip nhớ 256GB đã tăng gần 400% trong 1 năm, đẩy chi phí sản
   xuất một chiếc iPhone Pro 256GB cao hơn 38% — lý do giá bán mới dự kiến đắt hơn hẳn thế hệ trước.
7. **CTA**: câu hỏi tranh luận "Giá tăng vẫn đáng nâng cấp, hay chờ đời sau?" + 2 lựa chọn đối lập.

## Style dựng (claim_style)
`POST {"action":"claim_style"}` → `index: 1`, `style: "2-chip-and-leaderboard"`.
Ẩn dụ: chip số liệu viền cam + watermark số khổng lồ mờ phía sau + bảng xếp hạng ngang (dùng cho
Data moment: so các mức tăng giá dự đoán 100 / 150–200 / 200 / 250–300 USD dạng leaderboard ngang,
"khoảng 100–300" là số chính tô cam).

## Voice
ElevenLabs "Khánh Lâm - tin tức, thời sự" (`voice_id RCmOaM1iiIH5xX3QXjIF`), `model_id eleven_v3`,
speed ~1.09. KHÔNG đọc tên kênh "Tin Tức Số" trong lời thoại.

## Ảnh
`assets/img/article-hero.jpg` — ảnh báo Dân Trí (og:image thật, có dẫn nguồn), không AI, không
watermark. Dùng cho Hook + Article Image Card (act 2).
