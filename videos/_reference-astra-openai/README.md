# _reference-astra-openai — project HyperFrames THAM CHIẾU (không phải video của kênh này)

Đây là video mẫu "OpenAI ra mắt Astra" dựng cho tuyến **Công Nghệ Số** (kế thừa khung), giữ lại ở
đây làm **tham chiếu kỹ thuật** cho routine Tin Tức Số.

**Dùng để tham chiếu:**
- Cấu trúc 7 act + act CTA, cách chia `compositions/frames/*.html`, `hyperframes.json`, `meta.json`.
- Nhịp / `data-duration` khớp voice, dải phân bố dọc (top ~220 → ~1290px+) — xem BRAND-SYSTEM.md mục "Cân bằng dọc".
- Kỹ thuật GSAP local, `#root {}` trơn, reveal SVG, không emoji, carve/BGM.
- `assets/fonts/` (Montserrat 400–900, 2 subset), `assets/sfx/`, `assets/vendor/gsap.min.js` — copy dùng lại.
- `public/logo.png` — ĐÃ thay bằng logo Tin Tức Số (quả địa cầu + vành quỹ đạo cam). Copy sang `videos/<slug>/public/logo.png`.
- `CAPTION.md` — MẪU CẤU TRÚC caption (emoji + tiêu đề IN HOA, đoạn ngắn, câu hỏi, 📌 Nguồn, hashtag).

**KHÔNG tham chiếu:**
- Màu: video này dùng xanh `#4C8DFF` của Công Nghệ Số. Tin Tức Số dùng **cam `#FF5A1F`** + đỏ `#FF4438`.
- Chủ đề / tên kênh / hashtag (`#CongNgheSo`) / masthead "Công Nghệ Số".
- KHÔNG copy-paste HTML/CSS 1 frame rồi đổi chữ — mỗi video tự dựng theo style đã claim.
