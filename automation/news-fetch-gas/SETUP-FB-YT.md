# Setup Apps Script — đăng tự động Facebook + YouTube cho "Tin Tức Số"

Code đã viết xong ở `automation/news-fetch-gas/Code.gs` (~2470 dòng — dùng lại toàn bộ engine
đã chạy production ở kênh "Kinh Tế Số" / "Công Nghệ Số": có sẵn `publish_facebook`, `publish_facebook_photo`,
`publish_youtube`; IG/Threads cũng có sẵn trong code, để đó dùng sau, không cần cấu hình bây giờ).

Việc còn lại = tạo project + deploy + lấy token/ID điền vào Script Properties.

---

## PHẦN A — Tạo & deploy Apps Script (Claude làm cùng anh qua trình duyệt được)

1. Đăng nhập **đúng Gmail cá nhân mới** của kênh Tin Tức Số trên Chrome (KHÔNG Workspace).
2. `script.google.com` → **Dự án mới**.
3. Xoá code mẫu → dán toàn bộ `Code.gs` → Ctrl+S, đặt tên "TTS News Fetch".
4. Dropdown hàm → chọn `fetchAndStore` → **Run** → cấp quyền (Authorize, chấp nhận màn hình
   "Google chưa xác minh" → Nâng cao → Chuyển đến...) → log hiện `added N new item(s)`.
5. Dropdown → `installHourlyTrigger` → **Run** một lần.
6. **Triển khai → Tùy chọn triển khai mới** → Web app · Execute as: **Me** · Who has access:
   **Anyone** → Deploy → copy **exec URL** (`https://script.google.com/macros/s/.../exec`).
7. Mở exec URL trên tab ẩn danh → phải thấy `{"items":[...]}`.

## PHẦN B — Token Facebook (anh tự làm, Claude không được nhập token vào UI)

**Mục tiêu**: 1 Page Access Token dạng **System User** (không hết hạn) + Page ID.

1. `business.facebook.com` → **Cài đặt doanh nghiệp** (Business Settings).
2. **Người dùng → Người dùng hệ thống** → Thêm → tạo 1 System User, vai trò **Quản trị viên**.
3. **Tài khoản → Trang** → chọn Fanpage Tin Tức Số → **Thêm người** → chọn System User vừa tạo
   → bật **Quản lý Trang** (toàn quyền).
4. **Tài khoản → Ứng dụng** → chọn (hoặc tạo mới tại `developers.facebook.com`) 1 app → gán
   System User vào app với quyền **Quản lý ứng dụng**.
5. Quay lại **Người dùng hệ thống** → chọn System User → **Tạo mã thông báo mới (Generate token)**
   → chọn app ở bước 4 → tick 3 quyền: `pages_manage_posts`, `pages_read_engagement`,
   `pages_show_list` → **Tạo mã**. Copy token này (dạng `EAAG...`, rất dài, **không hết hạn**).
   *(Nếu định dùng Instagram sau này thì tick thêm `instagram_basic`, `instagram_content_publish`
   ngay bây giờ luôn cho đỡ làm lại.)*
6. **Page ID**: vào Fanpage → Giới thiệu/Cài đặt, hoặc gửi Claude token ở trên để verify + lấy ID
   qua `GET graph.facebook.com/v20.0/me/accounts` (Claude chỉ *dùng* token để gọi API kiểm tra,
   không nhập vào đâu).

→ Trong Apps Script: **Cài đặt dự án** (bánh răng) → **Thuộc tính của tập lệnh** → thêm:
| Tên | Giá trị |
|---|---|
| `FB_PAGE_ACCESS_TOKEN` | token System User ở bước B5 |
| `FB_PAGE_ID` | Page ID ở bước B6 |

## PHẦN C — Token YouTube (anh tự làm)

**Có thể dùng lại Client ID + Secret của app "CNS YouTube Publisher"** (Cloud project của Công Nghệ Số) — chỉ cần tạo **refresh token mới** đăng nhập bằng tài khoản Google sở hữu **kênh YouTube Tin Tức Số**. Nếu vậy, bỏ qua bước C1–C4, bắt đầu từ C5 với Client ID/Secret cũ.

**Mục tiêu**: OAuth Client ID + Secret + Refresh token (scope upload + readonly).

1. `console.cloud.google.com` — đăng nhập bằng **tài khoản Google sở hữu kênh YouTube Tin Tức Số**.
2. Tạo 1 project mới (hoặc dùng sẵn) → **APIs & Services → Library** → bật **YouTube Data API v3**.
3. **OAuth consent screen** → User type: **External** → điền tên app, email → **Test users**: thêm
   chính email của anh → Scopes: thêm `.../auth/youtube.upload` và `.../auth/youtube.readonly`.
4. **Credentials → Create credentials → OAuth client ID** → Application type: **Web application** →
   **Authorized redirect URIs**: thêm `https://developers.google.com/oauthplayground` → Create.
   Copy **Client ID** + **Client Secret**.
5. `developers.google.com/oauthplayground` → bánh răng góc phải → tick **Use your own OAuth
   credentials** → dán Client ID + Secret.
6. Bên trái, ô "Input your own scopes" → dán:
   `https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.readonly`
   → **Authorize APIs** → đăng nhập bằng tài khoản kênh YouTube → **Allow**.
7. **Step 2 → Exchange authorization code for tokens** → copy **Refresh token** (dạng `1//...`).

→ Trong Apps Script Script Properties thêm:
| Tên | Giá trị |
|---|---|
| `YOUTUBE_CLIENT_ID` | bước C4 |
| `YOUTUBE_CLIENT_SECRET` | bước C4 |
| `YOUTUBE_REFRESH_TOKEN` | bước C7 |

**Lưu ý** (bài học từ kênh cũ): khi sửa/thêm 1 property, các property khác dễ bị xoá nếu bấm nhầm
"−" cạnh dòng — kiểm tra lại đủ các dòng sau khi lưu (FB x2, YouTube x3, MASTER_SHEET_ID, BRAND_SLUG).

## PHẦN D — Sau khi có đủ property (FB x2 + YouTube x3 + MASTER_SHEET_ID + BRAND_SLUG=tin_tuc_so)

1. **Triển khai → Quản lý các tùy chọn triển khai** → sửa (pencil) → Phiên bản: **Phiên bản mới**
   → Deploy (giữ nguyên exec URL).
2. Test đăng thật (Claude chạy giúp qua `curl`, cần 1 URL mp4 + jpg công khai — vd. push video
   1 video test lên GitHub repo, hoặc host tạm):
   - Facebook Reel: `POST <exec> {"action":"publish_facebook","video_url":"<mp4>","caption":"...","thumbnail_url":"<jpg>","video":"test-tts","title":"..."}`
   - YouTube: `POST <exec> {"action":"publish_youtube","video_url":"<mp4>","title":"... #Shorts","description":"...","privacy":"public","thumbnail_url":"<jpg>","video":"test-tts"}`
3. Kiểm tra bài lên đúng Fanpage + kênh YouTube.

---

**Claude giúp được**: Phần A (tạo/dán/deploy/verify), Phần D (test đăng qua curl).
**Anh tự làm**: Phần B, C (đăng nhập tài khoản + OAuth consent + nhập token vào Script Properties —
Claude không được nhập token vào UI theo quy tắc an toàn).
