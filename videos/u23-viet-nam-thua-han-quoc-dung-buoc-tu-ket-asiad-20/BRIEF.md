# BRIEF — U23 Việt Nam thua đậm U23 Hàn Quốc, dừng bước tứ kết Asiad 20

## Nguồn

- Chính: Báo Dân Trí — "U23 Việt Nam thua đậm U23 Hàn Quốc, dừng bước tại tứ kết Asiad 20"
  (id `e526da9fa822`, đăng 25/9/2026, `category=news`).
- Đối chiếu: Báo Tuổi Trẻ — "Tứ kết Asiad 20 không có VAR, U23 Việt Nam mất bàn thắng oan uổng?"
  (id `6b930128dac0`, `category=news`) — dùng để bổ sung góc nhìn tình huống bàn thắng bị từ chối
  (phút 35, Quang Vinh sút dội cột, Văn Thuận đá bồi nhưng việt vị, trận không có công nghệ hỗ trợ
  trọng tài bằng video nên quyết định giữ nguyên).
- Phát hiện: **Google Trends VN** — từ khoá "u-23 hàn quốc đấu với u-23 việt nam", `trafficApprox`
  100.000+ (mục trending cao nhất trong danh sách kiểm lúc chọn, 26/9/2026). Có ở CẢ `trend` VÀ
  `news` → ưu tiên theo ROUTINE.md bước 1c.
- Ảnh: og:image bài Dân Trí (`?image=e526da9fa822`), ảnh thật trận đấu, có dẫn nguồn, không watermark.

## GATE A

Nhóm **A2 — kết quả thể thao có yếu tố Việt Nam** (đội tuyển U23 Việt Nam tại Asiad 20) → **GREEN**.
Không dính đời tư/drama cá nhân, không chính trị, không cáo buộc hình sự. Có nhắc tên cầu thủ/HLV
nhưng chỉ trong khuôn khổ tường thuật chuyên môn trận đấu đã diễn ra công khai — không phải phê bình
cá nhân ngoài sân cỏ. Tình huống trọng tài Uzbekistan từ chối bàn thắng là phê bình **quyết định/ hệ
thống trọng tài** (không có công nghệ hỗ trợ), không phải công kích cá nhân trọng tài.

## Tóm tắt sự kiện (theo bài gốc)

- Tối 25/9/2026, U23 Việt Nam thua 0-4 trước U23 Hàn Quốc ở tứ kết bóng đá nam Asiad 20, sân vận động
  Paloma Mizuho (Nhật Bản), chính thức dừng bước tại giải.
- Bàn thắng: phút 15 Lee Young Jun đánh đầu mở tỷ số 1-0 (từ đường tạt của Lee Hyun Ju); phút 76 Kim
  Ji Soo nâng tỷ số 2-0; phút 81 Lee Young Jun ghi bàn thứ hai (cú đúp), nâng 3-0; phút 88 Lee Young
  Jun hoàn tất hat-trick (bàn thắng cá nhân thứ ba) từ đường chuyền của Eom Ji Sung, ấn định 4-0.
- Cơ hội đáng chú ý nhất của U23 Việt Nam: phút 35, Quang Vinh sút xa dội cột dọc, Văn Thuận đá bồi
  tung lưới nhưng bàn thắng không được công nhận vì lỗi việt vị — trận đấu không có công nghệ hỗ trợ
  trọng tài bằng video nên quyết định trên sân được giữ nguyên (theo Tuổi Trẻ, tình huống được đánh
  giá là "nhạy cảm" qua hình ảnh quay chậm truyền hình).
- Hiệp 2, U23 Việt Nam cho rằng một cầu thủ Hàn Quốc để bóng chạm tay trong vòng cấm nhưng trọng tài
  không cho hưởng phạt đền.
- U23 Hàn Quốc mang đội hình có 9 cầu thủ đang thi đấu ở châu Âu cùng 3 cầu thủ quá tuổi (23+), và là
  đội đang bảo vệ ngôi vô địch sau khi thắng 3 kỳ Asiad liên tiếp gần nhất (2014, 2019, 2023).
- HLV Đinh Hồng Vinh: "Chúng tôi đã thể hiện được bản lĩnh trước Hàn Quốc."

## Góc nhìn riêng (B7)

Video không chỉ đọc lại tỷ số 0-4 mà dùng cấu trúc **icon grid** (style đã claim) để tách 2 lớp dữ
kiện độc lập: (1) diễn biến 4 bàn thắng — nhấn vào việc một mình Lee Young Jun ghi 3/4 bàn thắng
(hat-trick) làm Data moment, thay vì chỉ nêu tỷ số chung; (2) bối cảnh vì sao Hàn Quốc áp đảo — lưới
4 ô dữ liệu (cầu thủ chơi ở châu Âu, tuổi vượt hạn mức, thành tích 3 kỳ Asiad liên tiếp, kết quả vòng
bảng) mô phỏng "bảng dữ liệu đối thủ" thay vì chỉ tường thuật cảm tính. Câu hỏi CTA đặt đúng góc tranh
cãi thật của trận đấu (đẳng cấp chênh lệch hay bàn thắng bị từ chối là bước ngoặt), không phải bait
chung chung.

## Cách dựng (claim_style)

`POST claim_style` → `index: 7`, `style: "8-icon-grid"`. Ẩn dụ: lưới ô icon số liệu — 3 ô ngang cho
Key facts, 1 ô lớn giữa lưới 3 ô cho Data moment (hat-trick Lee Young Jun), lưới 2×2 ô cho Context
(sức mạnh U23 Hàn Quốc), lưới 2 ô lớn cho Impact.

## Act 6 (Impact) — sự thật đã xảy ra

U23 Việt Nam dừng bước tại tứ kết Asiad 20; U23 Hàn Quốc tiến vào bán kết, tiếp tục hành trình bảo vệ
ngôi vô địch — cả hai đều là kết quả đã xảy ra theo bài gốc, không suy đoán tương lai.

## Act 7 (CTA)

Câu hỏi tranh luận: trận thua 0-4 — vấn đề đẳng cấp hay bàn thắng bị từ chối (không có công nghệ hỗ
trợ trọng tài) là bước ngoặt? 2 lựa chọn đối lập: "Đẳng cấp vượt trội" / "Bước ngoặt là bàn thắng bị
từ chối". Không nhắc tên kênh trong lời đọc.

## Trending signal (đưa vào COMPLIANCE.md)

`"u-23 hàn quốc đấu với u-23 việt nam" — Google Trends VN, trafficApprox 100.000+, mục trending cao
nhất trong danh sách category=trend lúc chọn (26/9/2026)`.
