# DTO Master — DATA TRAFFIC ORGANIC (nguồn Looker Studio đa kênh)

Một Google Sheet duy nhất gom số liệu organic của mọi tuyến nội dung → Looker Studio hiển thị
tách theo `brand` + tổng `all channels`.

- **File master**: "Bản sao của BBH News Queue"
  `1isvFaqM9g6F8hFb3Fu5pvMg2Jgj017Nsh6R0OgHsof0` — sở hữu bởi `minhanhh1108`.
- Cả 3 Apps Script kênh (Kinh Tế Số + Công Nghệ Số + Tin Tức Số) đều chạy dưới `minhanhh1108` → ghi thẳng được,
  không cần share.

## Cấu trúc

| Tab | Grain | Cột |
|---|---|---|
| `brands` | 1 dòng / tuyến | `brand · label · emoji · order · active` |
| `post_metrics` | 1 dòng / (brand, post_id) — GHI ĐÈ | `brand · platform · video_project · post_type · post_id · permalink · title · posted_at · posted_date · views · likes · reactions · comments · shares · last_checked` |
| `traffic_daily` ⭐ | 1 dòng / (brand, platform, ngày) — THÊM/upsert | `brand · platform · date · posts_published · views_total · views_delta · engagement_total · engagement_delta · followers · followers_delta` |

`brand` = tuyến nội dung (`kinh_te_so`, `cong_nghe_so`, …). `platform` = nền tảng (`facebook`,
`instagram`, `youtube`, `threads`). `*_delta` = chênh so với ngày trước = **traffic organic trong ngày**.

Tab cũ (`engagement_metrics` / `audience_growth` / `posts_log` / `news_queue`) **giữ nguyên** làm
bản chụp lịch sử — `setupMaster()` di trú dữ liệu KTS từ 2 tab đầu sang tab mới.

## Bước 1 — chạy `setupMaster()` (1 lần)

1. Mở file master → **Tiện ích mở rộng → Apps Script**
2. Dán toàn bộ `automation/analytics-master/Code.gs` → **Lưu**
3. Dropdown hàm → `setupMaster` → **Chạy** → cấp quyền
4. Log: tạo 3 tab, seed `brands`, di trú `post_metrics` + `traffic_daily` (KTS)

## Bước 2 — nối từng Apps Script kênh

Với **mỗi** Apps Script kênh (Kinh Tế Số, Công Nghệ Số, Tin Tức Số): **⚙ Cài đặt dự án → Thuộc tính của tập
lệnh**, thêm 2 dòng:

| Tên | Giá trị |
|---|---|
| `MASTER_SHEET_ID` | `1isvFaqM9g6F8hFb3Fu5pvMg2Jgj017Nsh6R0OgHsof0` |
| `BRAND_SLUG` | `cong_nghe_so` / `kinh_te_so` / `tin_tuc_so` |

Code.gs đã có `mirrorAnalyticsToMaster_()` (gọi tự động ở cuối `refreshEngagementMetrics`, chạy 6h
sáng cùng trigger metrics). Không có 2 property này → hàm tự bỏ qua, không lỗi.

**Kinh Tế Số**: `mirrorAnalyticsToMaster_()` + 2 hằng `MASTER_*_HEADERS` cần được copy vào Code.gs
của repo `bot-ban-hang-kinh-doanh` (lấy nguyên khối từ cuối `automation/news-fetch-gas/Code.gs`
tuyến này), rồi thêm dòng `try { mirrorAnalyticsToMaster_(); } catch (e) {...}` sau
`refreshAudienceGrowth_()` trong `refreshEngagementMetrics`, deploy lại. (Phiên khác làm vì đó là
production tuyến cũ.)

## Bước 3 — chạy thử

Ở Apps Script kênh: dropdown → `refreshEngagementMetrics` → **Chạy**. Kiểm tra master:
`post_metrics` có dòng `brand = <slug>`, `traffic_daily` có dòng hôm nay (delta trống ở lần đầu,
có giá trị từ ngày thứ 2).

## Header hàng 1 = tiếng Việt

`setupMaster()` / `relabelHeaders()` đổi hàng 1 mọi tab sang nhãn tiếng Việt (viết hoa chữ cái
đầu câu). Code truy cột theo VỊ TRÍ nên đổi nhãn không ảnh hưởng — chỉ KHÔNG được đổi thứ tự cột.
Nhãn: `post_metrics` = Kênh · Nền tảng · Dự án video · Loại bài đăng · Mã bài đăng · Liên kết ·
Tiêu đề · Thời gian đăng · Ngày đăng · Lượt xem · Lượt thích · Cảm xúc · Bình luận · Lượt chia sẻ ·
Lần kiểm tra cuối. `traffic_daily` = Kênh · Nền tảng · Ngày · Số bài đăng · Tổng lượt xem · Lượt xem
tăng thêm · Tổng tương tác · Tương tác tăng thêm · Người theo dõi · Người theo dõi tăng thêm.
`brands` = Mã kênh · Tên kênh · Biểu tượng · Thứ tự · Đang hoạt động.

## Bước 4 — Looker Studio

### Lấy dữ liệu ở tab nào?

**Dùng CẢ 2, mỗi tab cho một loại biểu đồ** — KHÔNG cần tổng hợp thủ công:

| Biểu đồ / thành phần | Nguồn | Vì sao |
|---|---|---|
| Mọi biểu đồ **THEO NGÀY** (đường xu hướng lượt xem/tương tác, follower theo ngày) | `traffic_daily` | 1 dòng/(kênh, nền tảng, ngày); cột `... tăng thêm` = traffic organic THẬT trong ngày đó |
| Scorecard "traffic trong khoảng ngày đã chọn" | `traffic_daily`, `SUM(Lượt xem tăng thêm)` … | cộng delta theo kỳ |
| Scorecard "tổng số HIỆN TẠI" (tổng lượt xem tích luỹ) | `post_metrics`, `SUM(Lượt xem)` | số mới nhất từng bài |
| Bảng **"Nội dung hiệu quả nhất"** | `post_metrics` | 1 dòng/bài, sort `Lượt xem` giảm dần |
| Donut **follow theo nền tảng** | `traffic_daily`, `Người theo dõi` (dòng ngày mới nhất/nền tảng) | |
| Tra tên kênh + emoji + thứ tự | `brands` (blend theo `Mã kênh` = `Kênh`) | |

**KHÔNG dùng `engagement_metrics` nữa** — nó = `post_metrics` bản cũ 1 kênh, thiếu cột `Kênh`
(brand). Giữ làm lịch sử KTS trước khi có phân tách tuyến.

### Dựng

1. **Tạo báo cáo mới** → nguồn **Google Sheets** → file master → thêm 3 nguồn: `traffic_daily`,
   `post_metrics`, `brands`.
2. `traffic_daily`: `Ngày` kiểu Date; các cột số kiểu Number.
3. **Blend** `traffic_daily` + `brands` theo key `Kênh` = `Mã kênh` → lấy `Tên kênh` + `Thứ tự`.
4. **Trang "All channels"**:
   - Scorecard kỳ 7/28 ngày: `SUM(Lượt xem tăng thêm)`, `SUM(Tương tác tăng thêm)`, `SUM(Người theo dõi tăng thêm)`
   - Đường xu hướng: dimension `Ngày`, metric `Lượt xem tăng thêm`, **breakdown = `Tên kênh`** → mỗi tuyến 1 màu (cả cây, 1 biểu đồ)
   - Bảng: dimension `Tên kênh`, metric `Lượt xem tăng thêm` / `Tương tác tăng thêm` / `Người theo dõi` — sort `Thứ tự`
5. **Filter control** trên `Kênh` → chọn 1 tuyến; để trống = tổng `all_channels`.
6. Muốn mỗi tuyến 1 trang riêng: nhân bản trang, đặt **page-level filter** `Kênh = cong_nghe_so`…
7. "Top bài": nguồn `post_metrics`, dimension `Tiêu đề` + `Tên kênh`, metric `Lượt xem` giảm dần.

### Chuyển dashboard KTS hiện tại

Dashboard "DASHBOARD TRAFFIC ORGANIC" đang chạy trên `engagement_metrics` (KTS-only). Để lên đa kênh:
đổi từng biểu đồ sang `post_metrics` (per-post) hoặc `traffic_daily` (theo ngày) như bảng trên, thêm
`Kênh` vào dimension / filter. **Lưu ý**: biểu đồ "lượt view theo ngày" hiện dùng `Ngày đăng` của
`engagement_metrics` (= view của bài ĐĂNG ngày X) — chuyển sang `traffic_daily` (= view TĂNG ngày X,
chính xác hơn) thì mất lịch sử view-theo-ngày trước ~08/09/2026 (chỉ follower history được di trú).
Cách giữ cả hai: để 1 biểu đồ cũ trên `engagement_metrics` cho lịch sử, thêm 1 biểu đồ mới trên
`traffic_daily` cho số liệu chuẩn từ nay về sau.

## Lưu ý

- **`traffic_daily` chỉ có xu hướng view/tương tác TỪ NGÀY BẮT ĐẦU CHẠY (~08/09/2026)** — không
  backfill được (không có snapshot cũ). Follower history của KTS thì có (di trú từ `audience_growth`).
- `views_delta` có thể âm nếu nền tảng điều chỉnh số, hoặc bài bị xoá → ở Looker lọc `views_delta >= 0`
  nếu muốn "traffic dương" sạch.
- Khi thêm kênh mới: thêm dòng vào `brands` (active TRUE) + set `MASTER_SHEET_ID`/`BRAND_SLUG` ở
  Apps Script kênh đó. Không cần đụng master.
