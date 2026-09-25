# BRIEF — Việt Nam lần đầu giành huy chương canoeing ở ASIAD

## Nguồn

- Chính: VnExpress Thể thao — "Việt Nam lần đầu giành huy chương canoeing ở ASIAD" (id `e5ac0b604684`,
  đăng 25/9/2026 04:52 UTC, `category=news`).
- Phát hiện qua Google Trends VN: từ khoá **"huy chương"** (`category=trend`, id `c48e27f2d0e8`,
  `trafficApprox` "1000+", vị trí thứ 10 trong danh sách trending lúc kiểm 25/9/2026 ~06:25 UTC),
  `related` trỏ tới 3 bài báo VN uy tín cùng chủ đề bảng huy chương ASIAD (24h, Thanh Niên, VietNamNet).
  Chủ đề xuất hiện ở CẢ `trend` VÀ `news` → ưu tiên theo ROUTINE.md bước 1c. Dùng `id` của item
  `category=news` (VnExpress) cho `?article=`/`?image=` vì có ảnh báo chuẩn + bài viết chi tiết hơn.
- Không cần đối chiếu nguồn thứ 2 cho số liệu chính (thời gian về đích, thứ hạng đoàn) — bài VnExpress
  nêu đầy đủ, không phải claim gây tranh cãi.
- Ảnh: og:image bài VnExpress (`?image=e5ac0b604684`), ảnh thật (VĐV thi đấu), có dẫn nguồn, không
  watermark. Gốc là webp (converted sang jpg bằng ffmpeg, không đổi nội dung ảnh).

## GATE A

Nhóm **A2 — kết quả thể thao có yếu tố VN** → **GREEN**. Tin về đoàn Thể thao Việt Nam tại ASIAD 2026,
không dính đời tư/drama, không chính trị, không cá nhân bị nêu tên theo hướng tiêu cực — thuần thành
tích thể thao, tích cực, mang tính lịch sử (huy chương đầu tiên của canoeing Việt Nam ở đấu trường này).

## Tóm tắt sự kiện (theo bài gốc)

- Sáng 25/9/2026, Nguyễn Thị Hương và Diệp Thị Hương cán đích thứ ba ở chung kết kayak đôi nữ 500m môn
  canoeing tại hồ Miyoshi, thời gian 1 phút 57 giây 255 — giành HC đồng đầu tiên trong lịch sử của Đoàn
  Thể thao Việt Nam ở môn canoeing tại ASIAD.
- HC vàng thuộc về Trung Quốc (Sun Mengya, Ma Yanan), thời gian 1 phút 54 giây 700. HC bạc thuộc về
  Uzbekistan, thời gian 1 phút 56 giây 419.
- Khoảng cách với đội vô địch: 2,555 giây. Khoảng cách với đội hạng nhì (Uzbekistan): chỉ 0,836 giây.
- Việt Nam dự canoeing ở ASIAD từ năm 2006 (Doha, Qatar), tiếp tục góp mặt các kỳ 2010, 2018, 2023,
  nhưng đều KHÔNG có huy chương nào ở môn này cho tới kỳ 2026.
- Nguyễn Thị Hương (25 tuổi) và Diệp Thị Hương (23 tuổi) từng giành HC vàng SEA Games 33, tiếp tục đứng
  chung thuyền ở ASIAD 2026.
- Tính đến 11h40 sáng 25/9 giờ Hà Nội, Đoàn Thể thao Việt Nam có tổng cộng 1 HC vàng, 1 HC bạc, 16 HC
  đồng, đứng thứ 20 trên bảng tổng sắp huy chương ASIAD 2026.

## Góc nhìn riêng (B7)

Video không chỉ thuật lại "có huy chương" mà dùng ẩn dụ **vòng tiến trình (ring progress)** — style đã
claim — để làm nổi bật 2 lớp dữ liệu: (1) khoảng cách rất sát với đội hạng nhì (chỉ 0,836 giây) trình
bày như một vòng tiến trình gần đầy, nhấn mạnh "chỉ cách một chút nữa là bạc"; và (2) chuỗi 4 kỳ ASIAD
liên tiếp (2006-2023) không có huy chương canoeing nào, đối lập với kỳ 2026 — dùng chuỗi vòng tròn nhỏ
xếp ngang để trực quan hoá "lần đầu tiên sau nhiều năm". Câu hỏi CTA đặt vấn đề thật: khoảnh khắc này là
bước ngoặt đầu tư cho canoeing hay chỉ là một cột mốc đơn lẻ.

## Cách dựng (claim_style)

`POST claim_style` → `index: 5`, `style: "6-ring-progress"`. Ẩn dụ: vòng radial cho What happened
(badge nguồn dạng vòng tròn viền cam), Key facts (mini-radial ~80px mỗi fact), Data moment (vòng radial
khổng lồ quanh con số 0,836 giây — khoảng cách với HC bạc), Context (4-5 vòng radial nhỏ xếp hàng ngang
biểu diễn các kỳ ASIAD 2006/2010/2018/2023/2026, chỉ vòng cuối tô đầy cam), Impact (2 vòng radial lớn:
tổng huy chương đoàn + vị trí bảng tổng sắp).

## Act 6 (Impact) — sự thật đã xảy ra

Số liệu tổng huy chương (1 vàng, 1 bạc, 16 đồng) và vị trí thứ 20 bảng tổng sắp tính đến 11h40 sáng
25/9/2026 là số liệu đã xảy ra theo bài gốc (thời điểm chốt bài báo), không suy đoán tương lai.

## Act 7 (CTA)

Câu hỏi tranh luận: huy chương đồng canoeing đầu tiên sau 4 kỳ ASIAD không có huy chương là bước ngoặt
đáng đầu tư, hay chỉ là một cột mốc đơn lẻ cần thời gian chứng minh? 2 lựa chọn đối lập: "Bước ngoặt
đáng đầu tư" / "Cần thời gian chứng minh". Không nhắc tên kênh trong lời đọc.

## Trending signal (đưa vào COMPLIANCE.md)

`"huy chương" — Google Trends VN, category=trend, vị trí #10 trong danh sách lúc kiểm, trafficApprox
"1000+", cùng chủ đề với bài category=news đã chọn (đối chiếu qua related URLs: 24h.com.vn, Thanh
Niên, VietNamNet đều đưa bảng huy chương ASIAD ngày 24-25/9/2026).`
