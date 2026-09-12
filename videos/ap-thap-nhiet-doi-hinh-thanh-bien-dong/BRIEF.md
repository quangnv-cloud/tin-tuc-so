# BRIEF — Áp thấp nhiệt đới hình thành trên Biển Đông, mưa có thể vượt 300mm

Video tin nóng/trending kênh "Tin Tức Số". Chủ đề phát hiện từ Google Trends VN
("áp thấp nhiệt đới"), đối chiếu với tin nóng trang chủ báo lớn, QUA GATE A nhóm **A2 — thời
tiết/thiên tai đưa trung lập, khuyến cáo an toàn** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"áp thấp nhiệt đới"**, id `9589ce7db488`, vị trí **#2/234**
  trong danh sách (sắp mới nhất trước), `trafficApprox` **"100000+"**, `pubDate`
  2026-09-12T05:10:00Z. `related[0]` của chính item này trỏ thẳng tới bài VnExpress
  "Áp thấp nhiệt đới hình thành trên Biển Đông" — đúng chủ đề, không cần suy diễn.
- `GET ?category=news`: có ít nhất 4 bài cùng chủ đề trong ngày 12/9 từ VnExpress, Dân Trí, Tuổi Trẻ
  — cùng trích dẫn Trung tâm Dự báo khí tượng thuỷ văn quốc gia với **cùng một bộ số liệu** (vị trí
  cách Hoàng Sa 150km, cấp gió, hướng di chuyển) — xác nhận vừa đang trending vừa đã có báo chính
  thống đưa tin, số liệu khớp nhau giữa các nguồn độc lập.
- Nguồn chính dùng cho văn bản + ảnh: **VnExpress Thời sự**, id `8aa455295473` — "Áp thấp nhiệt đới
  hình thành trên Biển Đông" (`?article=` trả `ok:true`, text đầy đủ, số liệu cụ thể; URL khớp
  100% với `related[0]` của item trending).
- Nguồn đối chiếu thứ 2: **Dân Trí**, id `31ee0089da77` — "Áp thấp nhiệt đới vừa hình thành, có thể
  gây mưa lớn trên cả nước" — cùng trích dẫn Trung tâm Dự báo khí tượng thuỷ văn quốc gia, **số liệu
  trùng khớp** với bài VnExpress (vị trí cách Hoàng Sa 150km về tây nam, cấp 6 giật cấp 8, hướng tây
  bắc tốc độ ~10km/h, mốc thời gian 4h 13/9 và 4h 14/9, vùng gió mạnh/sóng lớn trên biển).
- Đã POST đánh dấu `used` cho id `9589ce7db488` (video: `ap-thap-nhiet-doi-hinh-thanh-bien-dong`).
- **Nguồn chính thức dùng cho video: VnExpress** (KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là
  công cụ phát hiện chủ đề).
- Ảnh minh hoạ: `?image=8aa455295473` (ảnh báo VnExpress, có dẫn nguồn, không watermark ngoài của
  báo gốc).

## GATE A

Nhóm **A2 — GREEN**: thời tiết / cảnh báo cộng đồng, đưa mức thông tin dự báo + khuyến cáo an toàn,
dẫn nguồn cơ quan chức năng (Trung tâm Dự báo khí tượng thuỷ văn quốc gia, Ban Chỉ đạo Phòng thủ dân
sự quốc gia), KHÔNG khai thác thương vong (chưa ghi nhận thiệt hại về người trong bài gốc — thuần
tuý là bản tin dự báo/cảnh báo trước, cùng nhắc lại 2 cơn bão trước đó — Saudel không gây thiệt hại,
Narra có gây thiệt hại nhưng đã xảy ra và được báo chí đưa tin công khai, không phải chi tiết nạn
nhân cụ thể). Không đụng đời tư, không hình sự, không chính trị, không thể thao — an toàn để dựng.
**Khác biệt với video đã đăng trước đó** (`khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`, 10/9): video
cũ là DỰ BÁO một vùng áp thấp CÓ THỂ hình thành (80%/30-40% xác suất) kèm không khí lạnh; video này
là bản tin MỚI, áp thấp ĐÃ CHÍNH THỨC hình thành sáng 12/9 với vị trí/cấp gió/hướng đi cụ thể — một
diễn biến thời sự mới, không phải nội dung lặp lại (B7).

Các chủ đề trending khác đã xét và loại ở Gate A (ghi lại để minh bạch):
- "lưu diệc phi", "hari won", "phương mỹ chi" (không có ảnh), "lê phương", "doãn quốc đam" — đời tư/
  showbiz nghệ sĩ → bỏ theo A1.
- "twitch", "lck" — nền tảng/giải đấu game quốc tế, không yếu tố VN rõ ràng, không thuộc nhóm A2 ưu
  tiên → bỏ.
- "tijuana đấu với querétaro", "ben shelton", "câu lạc bộ bóng đá inter miami", "giải bóng đá vô địch
  các câu lạc bộ châu âu", "necaxa đấu với puebla" — thể thao nước ngoài thuần giải trí, không yếu tố
  VN → bỏ theo A1.
- "dầu" (đường ống dẫn dầu Ả-rập Xê-út bị tấn công, Biển Đỏ chao đảo) — liên quan tấn công hạ tầng/
  xung đột khu vực Trung Đông → bỏ theo A1 (xung đột vũ trang/đối ngoại).
- "vietlott" — xổ số, cận nhóm nhạy cảm cờ bạc → bỏ, tránh rủi ro.
- "phạm nhật quân anh" — tên riêng cá nhân chưa rõ ngữ cảnh, rủi ro đời tư → bỏ, ưu tiên chủ đề an
  toàn hơn đã có (áp thấp nhiệt đới, traffic cao nhất danh sách).
- "câu lạc bộ bóng đá thép xanh nam định" (CLB Nam Định thua đậm, 2 thẻ đỏ, ngoại binh giẫm vào bụng
  đối thủ) — có yếu tố VN (V-League) nhưng xoay quanh tiểu tiết hành vi bạo lực trên sân/tranh cãi
  trọng tài, rủi ro khó giữ trung lập bằng tin thời tiết an toàn hơn cùng traffic cao hơn nhiều lần
  (100000+ so với 10000+) → ưu tiên áp thấp nhiệt đới.
- "học sinh" (khan hiếm sách giáo khoa) — có thể dựng (A3, nêu tên NXB Giáo dục) nhưng traffic thấp
  hơn nhiều so với áp thấp nhiệt đới → không chọn kỳ này.

## Nguồn & số liệu xác nhận (TUYỆT ĐỐI KHÔNG bịa thêm ngoài danh sách này)

- Sáng sớm 12/9, vùng áp thấp cách đặc khu Hoàng Sa khoảng 150km về phía tây nam đã mạnh lên thành
  áp thấp nhiệt đới, sức gió mạnh nhất 49km/h (cấp 6), giật cấp 8, di chuyển hướng tây bắc, tốc độ
  khoảng 10km/h — VnExpress + Dân Trí (khớp 2 nguồn).
- Dự báo: đến 4h ngày 13/9, áp thấp trên vùng biển Huế - Đà Nẵng (cách Đà Nẵng khoảng 120km về phía
  đông đông bắc), cường độ vẫn cấp 6 giật cấp 8. Đến 4h ngày 14/9, áp thấp trên vùng biển ven bờ từ
  Hà Tĩnh đến Huế, đổi hướng tây tây bắc, sau đó suy yếu dần thành một vùng áp thấp trong 48-72 giờ
  tiếp theo — VnExpress + Dân Trí.
- Mưa: ngày và đêm 13/9, mưa lớn từ phía nam Nghệ An đến Đà Nẵng phổ biến 80-180mm, **cục bộ trên
  300mm**; khu vực Hà Tĩnh đến bắc Quảng Trị 40-80mm cục bộ trên 150mm; nam Quảng Trị đến Quảng Ngãi
  80-150mm cục bộ trên 250mm — VnExpress.
- Trên biển: vùng biển phía tây Hoàng Sa và từ Hà Tĩnh đến Quảng Ngãi có gió mạnh cấp 6, giật cấp 8,
  sóng cao 2-4m, biển động; tàu thuyền trong vùng nguy hiểm có khả năng chịu tác động giông, lốc, gió
  mạnh, sóng lớn — VnExpress + Dân Trí.
- Ban Chỉ đạo Phòng thủ dân sự quốc gia đã đề nghị các địa phương theo dõi chặt diễn biến mưa lớn,
  lũ, ngập lụt, lũ quét, sạt lở đất để cảnh báo người dân; chủ động di dời người ở khu vực nguy cơ
  đến nơi an toàn; kiểm tra an toàn hồ chứa, công trình đang thi công, các tuyến đê xung yếu — VnExpress.
- So sánh với 2 cơn bão gần đây: bão Saudel (cuối 8, đầu 9) không gây thiệt hại cho Việt Nam; bão
  Narra không đổ bộ nhưng hoàn lưu và rãnh áp thấp đã gây mưa lớn, giông sét, gây thiệt hại về người
  và vật chất — VnExpress.

## Cấu trúc 7 act (định hướng nội dung, style `3-ticker-tape`)

1. Hook: Áp thấp nhiệt đới hình thành trên Biển Đông. Tag: "CẤP 6, GIẬT CẤP 8" / "MƯA LỚN MIỀN TRUNG".
2. What happened: sáng sớm 12/9, vùng áp thấp cách Hoàng Sa 150km mạnh lên thành áp thấp nhiệt đới,
   di chuyển hướng tây bắc 10km/h.
3. Key facts (dòng feed kiểu terminal): (1) 4h 13/9 → vùng biển Huế - Đà Nẵng; (2) 4h 14/9 → vùng
   biển ven bờ Hà Tĩnh - Huế; (3) sau 48-72 giờ suy yếu dần thành vùng áp thấp.
4. Data moment (số chính giữa 2 vạch, mã ngắn "ATNĐ" phía trên): mưa cục bộ có thể vượt 300mm tại
   khu vực Nam Nghệ An - Đà Nẵng ngày 13/9.
5. Context (sparkline so sánh): nhắc bão Saudel (không thiệt hại) và bão Narra (không đổ bộ nhưng
   vẫn gây thiệt hại) — cho thấy áp thấp/bão dù không đổ bộ trực tiếp vẫn có thể gây hậu quả.
6. Impact (sự thật đã xảy ra — chỉ đạo đã ban hành): Ban Chỉ đạo Phòng thủ dân sự quốc gia đã yêu
   cầu các địa phương ven biển miền Trung rà soát di dời dân nguy cơ cao, kiểm tra hồ chứa/đê điều.
7. CTA: trước đợt áp thấp nhiệt đới và mưa lớn diện rộng này, bạn đã chủ động ứng phó chưa hay vẫn
   đang chờ theo dõi thêm?

## Style claim (đã gọi, KHÔNG gọi lại claim_style)

`POST {"action":"claim_style","video":"ap-thap-nhiet-doi-hinh-thanh-bien-dong"}` →
`{"ok":true,"index":2,"style":"3-ticker-tape","claimed_at":"2026-09-12T06:28:11.885Z"}`.
