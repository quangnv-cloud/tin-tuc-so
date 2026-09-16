# Quy trình sản xuất — TIN TỨC SỐ

Runbook thao tác cho MỌI video tin nóng / trending trong ngày. Toàn bộ quy tắc brand/style ở
`BRAND-SYSTEM.md`, 10 cách dựng ở `CONSTRUCTION-STYLES.md`, trình tự routine đầy đủ ở `ROUTINE.md`
— đọc song song, không lặp lại ở đây.

`<EXEC>` = exec URL của Apps Script "TTS News Fetch":
`https://script.google.com/macros/s/AKfycbzDb2gLI8f2KBOMH1R6hgQdNkGoFa5BlEf5SUY8aOYQ5jF_bVK6G5bck8i7pVRopV0FlQ/exec`
`<REPO>` = `quangnv-cloud/tin-tuc-so` (nhánh `master`)

## 0. Trước khi bắt đầu

- Đọc `BRAND-SYSTEM.md` toàn bộ, đặc biệt mục "GSAP / kỹ thuật" (lỗi đã tái diễn nhiều lần).
- Đọc `automation/policy/COMPLIANCE-GATE.md` — **cổng kiểm duyệt chính sách nền tảng bắt buộc**
  (rút gọn từ `automation/policy/youtube-google-policy-engine.md` + `meta-policy-engine.md`).
  GATE A khi chọn tin, GATE B trước render, GATE C + ghi `COMPLIANCE.md` trước khi đăng. RED/ORANGE/
  BLACK → DỪNG, không đăng.
- KHÔNG copy state file (`index.html`, `meta.json`, `compositions/`) từ project cũ — luôn
  `hyperframes init` qua workflow `/hyperframes` rồi build lại nội dung riêng cho tin mới.

## 1. Phát hiện trending → chọn chủ đề & lên kịch bản

1. **Trending**: `GET <EXEC>?category=trend` → từ khoá đang trending ở VN (Google Trends). Mỗi item:
   `id`, `title` (từ khoá), `trafficApprox` ("2000+"), `related` (chuỗi JSON `[{title,url,source,snippet}]`),
   `pubDate`, `hasImage`.
   **Tin nóng nền**: `GET <EXEC>?category=news` → trang chủ VnExpress / Dân Trí / Tuổi Trẻ (bổ sung
   ngữ cảnh + nguồn dự phòng).
2. Chọn **1 chủ đề** vừa đang nóng/trending, vừa QUA GATE A (`automation/policy/COMPLIANCE-GATE.md`
   — bản này siết chặt: loại drama sao, hình sự/khởi tố cá nhân, chính trị/bầu cử, thể thao nước
   ngoài không yếu tố VN). Ưu tiên chủ đề có ở CẢ `trend` VÀ `news`. Nhóm A2 ưu tiên: ra mắt sản
   phẩm/công nghệ, chính sách mới đã ban hành, kết quả thể thao có yếu tố VN, khoa học, tin đời sống
   tích cực, thời tiết/thiên tai đưa trung lập. **Không có chủ đề an toàn → BỎ SUẤT** (ghi log,
   không hạ chuẩn).
3. **Chốt nguồn báo thật** (KHÔNG ghi "Google Trends" là nguồn): dùng `id` của item `category=news`
   đúng chủ đề nếu có; nếu chỉ ở `trend` thì chọn 1 URL báo VN uy tín trong `related`, `source` =
   tên báo đó. Không có URL báo VN nào → chọn chủ đề khác. Chỉ chọn chủ đề `hasImage: true`.
4. Đánh dấu đã dùng: `POST <EXEC>` với `{"id":"<id>","video":"<slug sẽ tạo>"}`. Ghi lại
   `trending_signal` (từ khoá + vị trí + `trafficApprox`) cho COMPLIANCE.md.
5. **Đọc nội dung**: `GET <EXEC>?article=<id>` → `{"ok":true,"source":"...","title":"...","text":"<văn bản>"}`.
   KHÔNG `WebFetch` / `curl` thẳng trang báo (Apps Script tải hộ từ IP Google). Bổ sung từ `related`
   snippets + item `news` cùng chủ đề. `ok:false` + `related` quá mỏng → chọn chủ đề khác. Đối chiếu
   ≥2 nguồn cho claim lớn khi có thể.
6. Viết lại bằng tiếng Việt, văn phong bản tin, gọn, giữ nguyên số liệu/mốc/tên. Nguồn tiếng Anh:
   KHÔNG dịch máy word-by-word, giữ tên riêng + thuật ngữ phổ biến, đóng khung "nghĩa là gì với
   người / thị trường VN" nếu có. TUYỆT ĐỐI không bịa số liệu ngoài nguồn.
7. Nhận cách dựng: `POST <EXEC> {"action":"claim_style","video":"<slug>"}` → `{"ok":true,"index":N,"style":"N-tên"}`.
   Dùng ĐÚNG style đó (`CONSTRUCTION-STYLES.md`). KHÔNG đọc `style-rotation-state.json` để lấy chỉ
   số. Gọi `claim_style` NGAY SAU bước 4, trước khi dựng.
8. Viết `BRIEF.md` + `SCRIPT.md` + `CAPTION.md` trong `videos/<slug>/`.
   - `SCRIPT.md`: MỘT dòng = MỘT act (7 dòng), văn phong tin tức, **KHÔNG viết tắt** (bảng quy đổi
     ở mục "Voiceover" của `BRAND-SYSTEM.md`), act 6 là sự thật đã xảy ra, act 7 là câu hỏi CTA
     kêu gọi bình luận (KHÔNG nhắc tên kênh trong lời đọc).
   - `CAPTION.md`: theo mẫu ở `videos/_reference-astra-openai/CAPTION.md` — dòng đầu 1 emoji + tiêu
     đề IN HOA; 2–3 đoạn ngắn (mỗi đoạn mở 1 emoji 📊 ⚠️ 💬); 1 câu hỏi tranh luận;
     `📌 Nguồn: <tên báo>, <ngày>` (thêm "· dịch" nếu nguồn tiếng Anh); hashtag
     `#TinTucSo #TinNong #TinTrongNgay` + 4–6 hashtag chủ đề. Kèm bản Threads ≤500 ký tự (để dành,
     tuyến này chưa đăng Threads).
9. Ảnh minh hoạ: `GET <EXEC>?image=<id>` → `{"ok":true,"data":"<base64>"}`. Giải mã:
   `curl -s "<EXEC>?image=<id>" | jq -r .data | base64 -d > assets/img/article-hero.jpg`.
   KHÔNG curl thẳng CDN báo. Ảnh trend là thumbnail Google quá nhỏ → dùng `id` của item `news` cùng
   chủ đề. `ok:false` → chọn chủ đề khác `hasImage:true`.

## 2. Giọng đọc (ElevenLabs)

Chi tiết ở mục "Voiceover" của `BRAND-SYSTEM.md`. Tóm tắt: từng dòng script → 1 file mp3
(`line1.mp3`…`line7.mp3`), `model_id: eleven_v3`, `voice_id: RCmOaM1iiIH5xX3QXjIF`, speed ~1.09,
key `ELEVENLABS_API_KEY`. Đo `ffprobe` từng file (input cho timing). Verify phiên âm ngược, soát
riêng lỗi đọc lắp do viết tắt.

## 3. Dựng composition

1. `hyperframes init` qua `/hyperframes` (không copy state cũ).
2. Dựng **7 act** (bảng trong `BRAND-SYSTEM.md`). Hook + Brand Anchor cố định (không thuộc style).
   5 act giữa (What happened / Key facts / Data moment / Context / Impact) dựng theo ẩn dụ hình ảnh
   của style đã claim ở §1.7 — tự thiết kế HTML/CSS/GSAP thật, mô tả style chỉ là định hướng.
   Act 7 CTA theo mẫu `videos/_reference-astra-openai/compositions/frames/07-cta.html` (bố cục — đổi màu sang cam `#FF5A1F`).
3. `data-duration` mỗi frame = độ dài voice thật + đệm ~0.3–0.5s. Rà lại mốc animation nội bộ.
4. Tổng thời lượng **dưới 75s**.
5. Ảnh Hook / Article Image Card dùng file đã tải ở §1.9. Logo dùng `public/logo.png`.

## 4. Nhạc nền & SFX

Chi tiết ở mục "Nhạc nền" của `BRAND-SYSTEM.md` + `videos/_reference-astra-openai/AUDIO-NOTES.md`. Tóm tắt:
Lyria calm (`--density 0.25 --brightness 0.4`, ambient, `--negative-prompt` bắt buộc), retrim +
fade-out, `data-volume` 0.30. Gắn `data-audio-group="voiceover"`, chạy
`node <hyperframes-audio skill dir>/scripts/carve.mjs --comp index.html --strength 0.4`.
**Chạy lại carve sau MỌI thay đổi timing/audio.**

## 5. Lint & QA

```bash
npm run check
```
Fix hết **error** trước khi render. Dùng Studio thumbnail (`preview --background` + endpoint
`.../thumbnail/index.html?t=<giây>&...&v=<cachebust>`) soát từng frame ít nhất 1 mốc, đặc biệt
frame có số liệu dài / nền ảnh + text (contrast WCAG AA).

## 6. Render

**Chuẩn xuất bản cố định — xem BRAND-SYSTEM.md mục "Chuẩn xuất bản video".** Không chạy `npm run
render` trơn (mặc định thấp hơn chuẩn); luôn truyền `--quality high --video-bitrate 10M
--browser-timeout 60`:

```bash
npx hyperframes preview --stop
npx --yes hyperframes@<pinned-version> render --quality high --video-bitrate 10M --browser-timeout 60
```
`ffmpeg` chưa có trên sandbox → `sudo apt-get update && sudo apt-get install -y ffmpeg` (có root).

## 7. Verify file render THẬT (bắt buộc đủ 5 bước)

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 <mp4>   # 1) thời lượng
ffmpeg -i <mp4> -af silencedetect=noise=-40dB:d=0.6 -f null -                          # 2) không có lặng chết giữa video
ffmpeg -i <mp4> -af loudnorm=print_format=summary -f null -                            # 3) loudness -14 LUFS ±1 LU, True Peak ≤ -1.0 dBTP
ffmpeg -y -ss <t> -i <mp4> -frames:v 1 -q:v 2 out.png                                  # 4) trích frame, xem bằng Read
ffmpeg -y -i <mp4> -vn -ac 1 -ar 16000 audio.wav                                       # 5) transcript
python -m whisper audio.wav --model base --language Vietnamese --output_format txt
```
"Input Integrated" ở bước 3 lệch quá ±1 LU so với -14.0 → chạy `loudnorm` 2-pass trước khi giao
file. Ở bước 4, mọi hiệu ứng chớp nhanh (<0.2s, vd smash-cut) cần soát bằng chuỗi frame liên tiếp
(fps=30 qua vài trăm ms quanh mốc), không chỉ 1 ảnh đơn — dễ bị bỏ lỡ nếu chỉ chụp 1 frame ước lượng.

Whisper model host (`openaipublic.azureedge.net`) có thể bị chặn ở sandbox → thay bằng Gemini
multimodal: `POST generativelanguage.googleapis.com/.../models/<model>:generateContent` với
`inline_data` audio/wav. Gọi `GET /v1beta/models` trước để lấy tên model còn dùng được (vd.
`gemini-flash-latest` — tên có timestamp như `gemini-2.5-flash` dễ bị "no longer available").

Chỉ coi "xong" khi cả 5 bước sạch — không báo hoàn thành chỉ dựa `npm run check` / thumbnail.

## 7.5. Thumbnail

```bash
ffmpeg -y -ss 3.5 -i output/<slug>.mp4 -frames:v 1 -q:v 2 output/thumbnail.jpg
```
`t` trong cửa sổ Hook (3–5s), SAU khi toàn bộ animation Hook vào ổn định (đọc timeline
`compositions/frames/01-hook.html`: mốc `tl.fromTo` trễ nhất + `duration` của nó + ~0.3s). Xem lại
bằng Read — xác nhận logo + tên kênh + badge nguồn + tiêu đề + 2 tag đều hiện đủ, rõ, không mờ.

## 8. Commit + push

Commit toàn bộ `videos/<slug>/` (kèm `output/*.mp4` + `output/thumbnail.jpg` — KHÔNG bị
`.gitignore`; `node_modules/` thì bị) lên `<REPO>` nhánh `master`. Thêm 1 dòng vào mảng `log` của
`videos/style-rotation-state.json` (index + style + slug + ngày) cho người đọc theo dõi — con trỏ
thật do `claim_style` quản lý.

## 9. Đăng Facebook + YouTube

Chỉ gọi SAU KHI §8 push xong (FB/YT tải video từ `raw.githubusercontent.com`). Endpoint đã cấu hình
sẵn token — KHÔNG tự tìm / nhập token.

`<mp4>` = `https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/<slug>.mp4`
`<jpg>` = `https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/thumbnail.jpg`

a. **Facebook Reel**:
   `POST <EXEC> {"action":"publish_facebook","video_url":"<mp4>","thumbnail_url":"<jpg>","caption":"<CAPTION.md phần trên dấu --->","video":"<slug>","title":"<tiêu đề tin>"}`
   `thumbnail_url` BẮT BUỘC (nếu không FB tự chọn khung ngẫu nhiên).

b. **YouTube**:
   `POST <EXEC> {"action":"publish_youtube","video_url":"<mp4>","thumbnail_url":"<jpg>","title":"<tiêu đề tin> #Shorts","description":"<CAPTION.md phần trên dấu --->","privacy":"public","video":"<slug>"}`
   Hệ thống tự viết hoa tiêu đề — không tự viết hoa.

Gọi POST bằng client theo được redirect 302 giữ POST (vd `python urllib`) — `curl -L` làm mất
Content-Length (411) hoặc đổi POST→GET. 1 lệnh lỗi → KHÔNG coi cả routine thất bại, ghi rõ.

**IG / Threads**: code có sẵn (`publish_instagram` / `publish_threads`) nhưng tuyến này CHƯA link
tài khoản IG Business / tạo Threads token → **KHÔNG gọi** cho tới khi có chỉ đạo mới.

## 9.5. Chốt thumbnail YouTube

Xem `result.thumbnail` / `result.thumbnail_attempts` trong phản hồi `publish_youtube`. Nếu
`code != 200` (hoặc để chắc), sau khi đăng xong đợi ~90s rồi:
`POST <EXEC> {"action":"yt_set_thumbnail","video_id":"<id YouTube>","thumbnail_url":"<jpg>"}` → `code:200` là xong.
**Lưu ý**: kênh còn mới, quyền custom thumbnail chỉ mở sau ~24h kể từ khi xác minh SĐT. Nếu 403
`youtube.thumbnail`, ghi vào tóm tắt "video đã đăng, thumbnail chưa dính do quyền kênh" — KHÔNG coi
là routine thất bại.

## 10. Tóm tắt cuối

Từ khoá trending đã chọn (+ vị trí/approx_traffic) hoặc "chọn từ category=news + lý do"; tin + nguồn báo thật (+ "đã dịch từ <nguồn>" nếu tiếng Anh), style + index, thời lượng, kết quả verify 4 bước,
đường dẫn repo, kết quả đăng FB (Reel — post id), YouTube (video id/link + trạng thái thumbnail).
Nếu BẤT KỲ bước 1–8 thất bại → DỪNG ở đó, KHÔNG làm 9–9.5, báo lỗi rõ ràng thay vì giao video lỗi
hoặc đăng nhầm nội dung.

## 11. Khi có phản hồi sửa (phiên tương tác)

- Chỉ thị rõ ràng dứt khoát ("bỏ đi", "sửa thành X", "áp dụng cho video sau") → làm luôn.
- Ý kiến chung / câu hỏi mở ("nhịp chậm không?") → trình bày phân tích + đề xuất, chờ xác nhận.
- Phản hồi thường trực cho video sau → ghi ngay vào `BRAND-SYSTEM.md` (brand) hoặc file này (quy
  trình), không chỉ sửa video hiện tại rồi quên.
