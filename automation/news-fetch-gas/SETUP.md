# Setup — News Fetch Proxy (Google Apps Script) · Tin Tức Số

Lớp lấy tin + đăng bài cho cloud routine kênh **Tin Tức Số**. Engine dùng lại nguyên bộ đã chạy
production ở "Kinh Tế Số" / "Công Nghệ Số" (`Code.gs`) — khác biệt duy nhất của tuyến này là
**nguồn**: Google Trends VN + trang chủ tin nóng an toàn (VnExpress / Dân Trí / Tuổi Trẻ), thay cho
các RSS công nghệ.

Chi tiết lấy token Facebook / YouTube: `SETUP-FB-YT.md` cùng thư mục.

## ⚠️ Bắt buộc dùng Gmail cá nhân, KHÔNG dùng Google Workspace

Workspace (`@botbanhang.vn`) chặn chia sẻ Apps Script ra ngoài tổ chức → web app "Anyone" vẫn 403.
Deploy bằng **Gmail cá nhân** `minhanhh1108@gmail.com` (cùng tài khoản 2 kênh kia).

## Các bước (làm 1 lần)

1. Đúng tài khoản `minhanhh1108@gmail.com` tại `script.google.com` (kiểm tra avatar góc phải).
2. **Dự án mới** — standalone, không cần tạo Google Sheet trước (`getSheet_()` tự tạo Sheet
   "TTS News Queue" ở lần chạy đầu, lưu ID vào Script Property `SPREADSHEET_ID`).
3. Xoá code mẫu → dán toàn bộ `Code.gs` → `Ctrl+S` → đặt tên **"TTS News Fetch"**.
4. Dropdown hàm → `fetchAndStore` → **Run** → cấp quyền (màn hình "Google chưa xác minh" → Nâng cao
   → Chuyển đến…). Log hiện `fetchAndStore: added N new item(s)`.
   - Kiểm tra Sheet vừa tạo: tab `news_queue` phải có cả dòng `category = trend` (từ khoá Google
     Trends, cột `trafficApprox` + `related` có dữ liệu) và `category = news`.
5. Dropdown → `installHourlyTrigger` → **Run** một lần (lịch chạy `fetchAndStore` mỗi giờ).
6. **Triển khai → Tùy chọn triển khai mới** → Web app · Execute as **Me** · Who has access
   **Anyone** → Deploy → copy **exec URL** (`https://script.google.com/macros/s/…/exec`).
7. Mở exec URL ở tab ẩn danh → thấy `{"items":[...]}`. Thử `?category=trend` và `?category=news`.
   *(Test bằng `curl` từ máy cá nhân VN có thể trả 403 do ISP chặn `script.google.com` — verify từ
   cloud sandbox mới chính xác.)*

## Script Properties cần thêm (Cài đặt dự án → Thuộc tính của tập lệnh)

Người dùng tự nhập token — **theo quy tắc an toàn cố định, Claude Code không được nhập API key/token
vào bất kỳ field cấu hình nào (kể cả Script Properties)** dù người dùng đã cung cấp trực tiếp và
đồng ý; chỉ được *dùng* token để gọi API (vd. verify qua `curl`), không được *nhập* nó vào UI.
`MASTER_SHEET_ID` và `BRAND_SLUG` KHÔNG phải secret — Claude nhập được nếu người dùng yêu cầu.

| Tên | Giá trị | Ai nhập |
|---|---|---|
| `SPREADSHEET_ID` | tự tạo ở bước 4 — không cần nhập tay | (tự động) |
| `FB_PAGE_ACCESS_TOKEN` | System User token của Fanpage Tin Tức Số (không hết hạn), quyền `pages_manage_posts` · `pages_read_engagement` · `pages_show_list` | người dùng |
| `FB_PAGE_ID` | ID Fanpage Tin Tức Số | người dùng |
| `YOUTUBE_CLIENT_ID` | OAuth client (có thể **dùng lại** client "CNS YouTube Publisher" của Công Nghệ Số) | người dùng |
| `YOUTUBE_CLIENT_SECRET` | ↑ | người dùng |
| `YOUTUBE_REFRESH_TOKEN` | refresh token của **kênh YouTube Tin Tức Số** (scope `youtube.upload` + `youtube.readonly`) — phải tạo mới, đăng nhập bằng tài khoản sở hữu kênh Tin Tức Số | người dùng |
| `MASTER_SHEET_ID` | `1isvFaqM9g6F8hFb3Fu5pvMg2Jgj017Nsh6R0OgHsof0` (Sheet analytics master dùng chung) | Claude/người dùng |
| `BRAND_SLUG` | `tin_tuc_so` | Claude/người dùng |

Sau khi thêm đủ → **Triển khai → Quản lý các tùy chọn triển khai → sửa → Phiên bản mới → Deploy**
(giữ nguyên exec URL). Deployment của dự án pin theo version cố định — mọi thay đổi `Code.gs` đều
cần redeploy version mới mới có hiệu lực trên `/exec`.

## Egress allowlist của cloud environment cần có

Routine cloud gọi các host sau (thêm vào Custom allowlist nếu chưa có):

- `script.google.com` — endpoint này (mọi thao tác đọc tin + đăng bài đi qua đây).
- `raw.githubusercontent.com` — Facebook / YouTube tải video + thumbnail đã push.
- `api.elevenlabs.io`, `generativelanguage.googleapis.com` — TTS + verify transcript / Lyria.
- Ảnh bài báo được `serveNewsImage_` tải **server-side từ IP Google** → KHÔNG cần thêm CDN báo vào
  allowlist. `?article=` cũng tải server-side. Từ khoá Trends: ảnh thumbnail ở `*.gstatic.com`
  (Apps Script tải hộ, không cần allowlist phía sandbox).

## Bảo trì

- 1 nguồn đổi đường dẫn RSS (404) → sửa URL trong mảng `FEEDS` ở `Code.gs`, dán lại vào editor,
  Save, **redeploy version mới**. Fetch loop bỏ qua feed lỗi thay vì fail cả run.
- `news_queue` phình dần → dọn thủ công dòng `used=TRUE` cũ > 30 ngày (không bắt buộc).
- `related` (JSON news_item của item Trends) có thể tới vài KB/dòng — bình thường.
- Analytics: sau khi deploy, thêm 1 dòng vào tab `brands` của Sheet master:
  `Tin Tức Số | Tin Tức Số | 📰 | 3 | TRUE` (hoặc chạy lại `setupMaster()` bản đã cập nhật
  `BRANDS_SEED` trong `automation/analytics-master/Code.gs`). `mirrorAnalyticsToMaster_()` tự chạy
  cuối `refreshEngagementMetrics` (trigger 6h sáng) khi có `MASTER_SHEET_ID` + `BRAND_SLUG`.
