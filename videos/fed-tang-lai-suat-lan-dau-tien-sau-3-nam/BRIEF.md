# BRIEF — Fed tăng lãi suất lần đầu tiên sau 3 năm, tỷ giá và vàng Việt Nam phản ứng ngay

Video tin nóng/trending kênh "Tin Tức Số" (chạy tự động, khung giờ ngày 17/9/2026, suất thứ 2
trong ngày). Chủ đề phát hiện từ Google Trends VN ("fed tăng lãi suất"), đối chiếu tin nóng trang
chủ báo lớn, QUA GATE A nhóm **A2 — kinh tế trung lập, số liệu đã công bố** (GREEN).

## Phát hiện trending (bước 1 ROUTINE.md)

- `GET ?category=trend`: từ khoá **"fed tăng lãi suất"**, id `3b9cf8a878a7`, vị trí **#85/161**
  trong danh sách (0-index 84), `trafficApprox` **"200+"**, `pubDate` 2026-09-16T06:20:00Z.
- `GET ?category=news`: chủ đề đang phủ dày trang chủ báo lớn VN sáng 17/9 — ít nhất 7 bài cùng chủ
  đề (VnExpress Kinh doanh, Dân Trí, Tuổi Trẻ) xác nhận vừa trending vừa đã có báo chính thống đưa
  tin. Dùng bài `category=news` đúng chủ đề cho `?article=`/`?image=` theo đúng thứ tự ưu tiên của
  PRODUCTION-WORKFLOW.md §1.3.
- Nguồn chính dùng cho văn bản: `?article=a96b798ba5ec` → Tuổi Trẻ, "Fed tăng lãi suất lần đầu tiên
  sau 3 năm, chuyện gì tiếp theo?" → `ok:true`, text 9.374 ký tự, đầy đủ số liệu + trích lời Chủ tịch
  Fed.
- Đã POST đánh dấu `used` cho id `a96b798ba5ec` (video: `fed-tang-lai-suat-lan-dau-tien-sau-3-nam`).
- **Nguồn chính thức dùng cho video: Tuổi Trẻ.**
- Ảnh minh hoạ: `?image=a96b798ba5ec` (ảnh báo Tuổi Trẻ đi kèm bài, ảnh báo chí thời sự thông
  thường, không dàn dựng).
- Đối chiếu chéo với 2 nguồn VN bổ sung để lấy số liệu tác động trong nước (Act "Impact"):
  - Dân Trí, "Giá vàng SJC giảm nhanh sau động thái của Fed" (`?article=6c3b46f56032`).
  - VnExpress Kinh doanh, "Tỷ giá trung tâm tiếp tục lập đỉnh" (`?article=f592159d5c19`).

## Nội dung cốt lõi (đối chiếu ≥2 nguồn cho claim lớn)

- Ngày 16/9/2026, Cục Dự trữ Liên bang Mỹ (Fed) tăng lãi suất tham chiếu thêm 0,25 điểm phần trăm,
  lên mức **3,75–4%** — lần đầu tiên kể từ 2023 (bất chấp phản đối của Tổng thống Trump).
  Ủy ban FOMC quyết định nhất trí.
- Lý do: Chủ tịch Fed Kevin Warsh nói lạm phát Mỹ "quá cao trong thời gian quá dài". CPI tháng 8 là
  3,4% (đã công bố 11/9), cao hơn mục tiêu dài hạn 2% của Fed.
- Dự báo cập nhật (SEP) của Fed: PCE cuối năm 3,7% (+0,1đ so với dự báo trước); GDP cuối năm 2,3%
  (+0,1đ). Ít nhất 12/18 nhà hoạch định chính sách cho rằng cần thêm ít nhất 1 đợt tăng nữa trước
  cuối năm — nêu rõ đây là DỰ BÁO của chính Fed, không phải khẳng định chắc chắn của routine.
- Ông Trump phản ứng giận dữ, gọi đây là "đợt tăng lãi suất chống Trump" — nêu là phát ngôn được báo
  dẫn trực tiếp, không phải diễn giải của routine.
- **Tác động tại Việt Nam (đã xảy ra, không suy đoán)**:
  - Ngân hàng Nhà nước ngày 17/9 nâng tỷ giá trung tâm lên **25.632 đồng/USD** (+6 đồng so với hôm
    trước) — mức cao nhất từ trước đến nay; giá USD tại các ngân hàng thương mại cũng nhích lên.
  - Giá vàng miếng SJC sáng 17/9 giảm 700.000 đồng/lượng, còn **142,8–145,8 triệu đồng/lượng** (mua
    – bán) theo đà giảm chung của giá vàng thế giới sau quyết định của Fed.

## GATE A

Nhóm **A2 — GREEN**: tin kinh tế vĩ mô trung lập (quyết định chính sách tiền tệ đã công bố chính
thức bởi Fed, số liệu tỷ giá/vàng đã công bố bởi Ngân hàng Nhà nước/thị trường), không khuyến nghị
đầu tư, không đụng đời tư/hình sự/chính trị VN/thể thao. Có nhắc phát ngôn của quan chức công (Chủ
tịch Fed, Tổng thống Mỹ) trong vai trò điều hành/phản ứng chính sách công khai, được báo chính thống
dẫn trực tiếp — không phải đời tư/drama cá nhân nên KHÔNG rơi vào nhóm A1 "chính trị/bầu cử/nhân sự
cấp cao" (đây là chính sách tiền tệ Mỹ, không phải chính trị/bầu cử/nhân sự VN). Không đưa khuyến
nghị đầu tư/mua bán vàng-USD-chứng khoán cho khán giả — chỉ tường thuật số liệu đã xảy ra.

## GATE B — kiểm tra trước render (đã chạy trên SCRIPT.md + CAPTION.md + BRIEF.md ở trên)

Mọi số liệu (0,25 điểm phần trăm, 3,75–4%, CPI 3,4%, mục tiêu 2%, PCE dự báo 3,7%, GDP dự báo 2,3%,
12/18 nhà hoạch định chính sách, tỷ giá trung tâm 25.632đ/USD +6đ, giá vàng SJC giảm 700.000đ còn
142,8–145,8 triệu đồng/lượng) đều truy được về 1 trong 3 bài `?article=` đã đối chiếu ở trên. Đã gỡ
1 con số "mức lãi suất trước đó 3,5–3,75%" suy luận số học nhưng KHÔNG có nguyên văn trong nguồn —
thay bằng so sánh với mục tiêu 2% + CPI 3,4% (đều có nguyên văn). Không khuyến nghị đầu tư/mua bán.
Không đời tư/hình sự/thù ghét/nội dung 18+. Ảnh dùng ảnh báo thật (`?image=`), không AI tái dựng
người/cảnh thật. CTA là câu hỏi quan điểm thật, không engagement bait. → **GATE B: GREEN**.

## Cách dựng (construction style)

`POST {"action":"claim_style"}` → `{"ok":true,"index":0,"style":"1-card-and-bar"}`. Dùng đúng style
**Card & Bar** (`CONSTRUCTION-STYLES.md`) cho 5 act giữa.

**Lưu ý minh bạch**: trước lệnh claim_style thật, một lệnh POST thăm dò cú pháp gọi nhầm với slug giả
`test-probe-ignore` đã vô tình tiêu tốn 1 lượt xoay vòng thật (trả về `index:9,
style:"10-stock-terminal"`, ghi nhận trên Apps Script với video giả đó). Đây là tác dụng phụ ngoài ý
muốn lên con trỏ xoay vòng dùng chung — không ảnh hưởng tới nội dung/chất lượng video này, ghi lại
để minh bạch và tránh lặp lại (không gọi POST có hiệu ứng phụ với dữ liệu giả nữa).

## Cấu trúc 7 act (định hướng — chi tiết ở SCRIPT.md)

1. Hook: "Fed tăng lãi suất" + tag "● Lần đầu sau 3 năm" / "● Ông Trump giận dữ".
2. What happened: Fed tăng 0,25 điểm phần trăm lên 3,75–4%, ngày 16/9, FOMC nhất trí.
3. Key facts: ai (Fed/Chủ tịch Kevin Warsh) — vì sao (lạm phát quá cao quá lâu) — khi nào (16/9).
4. Data moment: con số chính 3,75–4% (lãi suất mới) + so sánh với mục tiêu lạm phát dài hạn 2% và
   CPI tháng 8 thực tế 3,4% — KHÔNG dùng con số "mức lãi suất trước đó" vì không có trong nguồn đã
   đối chiếu (chỉ nguồn nói "tăng thêm 0,25 điểm phần trăm", không nêu rõ mức khởi điểm bằng số).
5. Context: bảng thông số (CPI 3,4% · PCE dự báo 3,7% · GDP dự báo 2,3% · dự báo thêm 1 đợt tăng).
6. Impact (sự thật đã xảy ra tại VN): tỷ giá trung tâm 25.632đ/USD (cao nhất từ trước đến nay) +
   giá vàng SJC giảm 700.000đ/lượng còn 142,8–145,8 triệu đồng/lượng.
7. CTA: câu hỏi tranh luận "tăng lãi suất kiềm lạm phát cần thiết, hay thêm gánh nặng vay tiền?"
