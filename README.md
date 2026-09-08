# Tin Tức Số

Kênh tin nóng / trending trong ngày, tự động — tiếng Việt, khán giả VN. Mỗi ngày phát hiện chủ đề
đang được quan tâm nhất từ **Google Trends VN** (RSS chính thức), lọc rất chặt qua cổng chính sách
(GATE A — loại drama sao, hình sự/khởi tố cá nhân, chính trị/bầu cử, thể thao nước ngoài), chọn
chủ đề an toàn, đối chiếu với báo lớn VN (VnExpress, Dân Trí, Tuổi Trẻ), tự dựng video (HyperFrames,
7 act + CTA) rồi tự đăng theo lịch (3 khung giờ/ngày) lên Facebook Fanpage và YouTube.

Kế thừa khung motion-graphics của tuyến "Công Nghệ Số" — đổi màu nhận diện sang **cam tin nóng
`#FF5A1F`**, mô-típ **quả địa cầu + vành quỹ đạo** (theo logo). Tuyến nội dung độc lập hoàn toàn với
các tuyến khác — Gmail riêng, Apps Script riêng, token riêng, repo riêng.

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `automation/news-fetch-gas/` | `Code.gs` — Apps Script proxy: Google Trends VN + trang chủ tin nóng VN, chống trùng, phục vụ ảnh (`?image=`) + văn bản bài (`?article=`), và các endpoint đăng bài (`publish_facebook`, `publish_youtube`, …). `SETUP.md` + `SETUP-FB-YT.md` — deploy + lấy token. |
| `automation/policy/` | `COMPLIANCE-GATE.md` (GATE A/B/C — bản tuyến này đã siết chặt) + 2 policy engine đầy đủ. |
| `automation/analytics-master/` | Ghi số liệu organic về Google Sheet master đa kênh (`mirrorAnalyticsToMaster_`). |
| `videos/BRAND-SYSTEM.md` · `PRODUCTION-WORKFLOW.md` · `CONSTRUCTION-STYLES.md` · `ROUTINE.md` | Toàn bộ quy tắc thương hiệu + quy trình + 10 cách dựng xoay vòng + checklist routine. |
| `videos/_reference-astra-openai/` | Project HyperFrames tham chiếu (kế thừa từ Công Nghệ Số) — dùng cho bố cục / nhịp / kỹ thuật, KHÔNG tham chiếu màu (xanh cũ) hay chủ đề. |
| `docs/` | Trang chủ + Chính sách quyền riêng tư (GitHub Pages) — dùng cho màn hình xác nhận OAuth của app YouTube. |

## Bảo mật

Token / API key **không bao giờ** nằm trong repo này. Tất cả đọc từ **Script Properties** của dự án
Apps Script (`FB_PAGE_ACCESS_TOKEN`, `FB_PAGE_ID`, `YOUTUBE_CLIENT_ID`, `YOUTUBE_CLIENT_SECRET`,
`YOUTUBE_REFRESH_TOKEN`, `SPREADSHEET_ID`, `MASTER_SHEET_ID`, `BRAND_SLUG=tin_tuc_so`, …).
