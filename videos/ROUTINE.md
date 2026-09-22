# ROUTINE — trình tự bắt buộc cho cloud routine "Tin Tức Số"

File này là checklist thao tác mà routine cloud (chạy 3 khung giờ/ngày) phải làm ĐÚNG THỨ TỰ.
Quy tắc brand/style đầy đủ ở `BRAND-SYSTEM.md` / `PRODUCTION-WORKFLOW.md` / `CONSTRUCTION-STYLES.md`
(đọc 3 file đó TRƯỚC). Khung motion tham chiếu (kế thừa từ Công Nghệ Số, KHÔNG tham chiếu màu/chủ đề):
`videos/_reference-astra-openai/`.

Điểm KHÁC các tuyến cũ: **bước 1 phát hiện chủ đề đang trending từ Google Trends VN** rồi mới chọn
tin, và **GATE A siết chặt hơn** (loại drama sao / hình sự / chính trị / thể thao nước ngoài).

---

Bạn đang tự động sản xuất 1 video tin nóng / trending trong ngày cho kênh "Tin Tức Số", chạy không giám sát theo lịch. Đọc kỹ 3 file sau TRƯỚC KHI làm bất cứ điều gì — đây là toàn bộ quy tắc bắt buộc, không được bỏ qua hay tự suy đoán thay thế:
  - videos/BRAND-SYSTEM.md
  - videos/PRODUCTION-WORKFLOW.md
  - videos/CONSTRUCTION-STYLES.md
  - automation/policy/COMPLIANCE-GATE.md  (GATE A/B/C — bản tuyến này đã siết chặt)

`<EXEC>` = https://script.google.com/macros/s/AKfycbzDb2gLI8f2KBOMH1R6hgQdNkGoFa5BlEf5SUY8aOYQ5jF_bVK6G5bck8i7pVRopV0FlQ/exec
`<REPO>` = quangnv-cloud/tin-tuc-so (nhánh master)

Thực hiện đúng trình tự trong videos/PRODUCTION-WORKFLOW.md, cụ thể:

0. (1 lần, đầu run) Sandbox cloud KHÔNG có sẵn `lyria-recipe.py` (BGM) và `carve.mjs` (audio ducking) — chạy `cd /tmp && npx --yes hyperframes@0.8.30 skills` để cài bộ skill chính chủ chứa 2 script này (`~/.claude/skills/media-use/audio/scripts/lyria-recipe.py` và `~/.claude/skills/hyperframes-audio/scripts/carve.mjs`). Cũng `pip install --quiet google-genai` cho lyria-recipe.py. KHÔNG tự viết script thay thế, KHÔNG bỏ bước BGM/carve.

1. **Phát hiện chủ đề trending + chọn tin** (bước riêng của tuyến này):
   a. GET `<EXEC>?category=trend` → danh sách từ khoá đang trending ở VN (Google Trends). Mỗi item:
      `title` = từ khoá, `trafficApprox` (vd "2000+"), `related` = **chuỗi JSON** mảng ~3 bài báo
      `[{title,url,source,snippet}]`, `hasImage`, `pubDate`. Danh sách đã sắp mới nhất trước.
   b. GET `<EXEC>?category=news` → tin nóng từ trang chủ báo lớn VN (VnExpress / Dân Trí / Tuổi Trẻ)
      — dùng để (i) BỔ SUNG ngữ cảnh cho một từ khoá trending, (ii) làm NGUỒN DỰ PHÒNG khi mọi chủ
      đề trending đều bị GATE A loại.
   c. **Chọn 1 chủ đề** vừa đang nóng/trending, vừa QUA GATE A (đọc `automation/policy/COMPLIANCE-GATE.md`
      mục GATE A — bản này siết chặt). Ưu tiên chủ đề xuất hiện ở CẢ `trend` VÀ `news` (đang trending
      + đã có báo chính thống đưa tin). Ưu tiên nhóm A2: ra mắt sản phẩm/công nghệ, chính sách mới đã
      ban hành, kết quả thể thao có yếu tố VN, khoa học, tin đời sống tích cực, thời tiết/thiên tai
      đưa trung lập.
   d. **Chốt nguồn tin thật**: KHÔNG ghi "Google Trends" là nguồn — Trends chỉ là công cụ phát hiện.
      - Nếu có 1 item `category=news` đúng chủ đề → dùng `id` của item đó cho `?article=` / `?image=`,
        `source` = tên báo đó.
      - Nếu chỉ có ở `trend` → chọn 1 URL trong `related` từ **báo VN uy tín** (VnExpress, Tuổi Trẻ,
        Dân Trí, Thanh Niên, VietnamNet, Lao Động, VTV, Znews…); `source` = tên báo của URL đó. Dùng
        `id` của item `trend` cho `?article=` (server sẽ tải URL `related[0]`) và `?image=`.
      - `related` cho các từ khoá quốc tế thường trỏ báo nước ngoài / trang cá cược → nếu không có
        URL báo VN nào và `news` cũng không có → chủ đề này KHÔNG dùng được, chọn chủ đề khác.
   e. Chỉ chọn chủ đề có ảnh dùng được: item phải `hasImage: true`. Với item `trend`, ảnh mặc định là
      thumbnail nhỏ của Google — nếu có item `news` cùng chủ đề với ảnh báo chuẩn thì ưu tiên lấy ảnh
      từ `id` của item `news` đó (bước 5).
   f. Sau khi chọn: POST `<EXEC>` với `{"id":"<id đã chọn>","video":"<slug sẽ tạo>"}` để đánh dấu đã dùng.
   g. **Ghi lại `trending_signal`** (từ khoá + vị trí trong list + `trafficApprox`) để đưa vào COMPLIANCE.md.
      Nếu chọn từ `category=news` (không qua Trends) thì `trending_signal` = "" và nêu lý do trong tóm tắt.

**GATE A — sàng lọc chính sách lúc chọn chủ đề** (bắt buộc, `automation/policy/COMPLIANCE-GATE.md` mục GATE A). BỎ CHỦ ĐỀ (chọn chủ đề khác; POST đánh dấu used chủ đề vừa bỏ nếu đã POST) nếu thuộc nhóm A1: đời tư/drama/tin đồn người nổi tiếng, cáo buộc hình sự/khởi tố/bắt giữ cá nhân, tai nạn/án mạng khai thác chi tiết, chính trị/bầu cử/nhân sự cấp cao/đối ngoại/chủ quyền, thể thao nước ngoài thuần giải trí không yếu tố VN, y tế "thuốc thần", tài chính/tiền số "cam kết lãi"/"kèo", deepfake là nội dung chính, 18+/cờ bạc/chất kích thích, thuyết âm mưu/tin giả đã bị bác, và mọi nội dung BLACK (khai thác trẻ em/bạo lực nghiêm trọng/lừa đảo/phishing/thù ghét). **Nếu không còn chủ đề nào đạt A2/A3 trong khung giờ này → BỎ SUẤT**: kết thúc routine bằng tóm tắt "skip slot — không có chủ đề trending an toàn", KHÔNG hạ chuẩn để lấp suất, KHÔNG làm tiếp bước 2+.

2. Đọc nội dung tin: GET `<EXEC>?article=<id đã chọn>` → JSON `{"ok":true,"source":"...","title":"...","text":"<văn bản bài báo>"}`. TUYỆT ĐỐI KHÔNG WebFetch / curl thẳng trang báo (domain tin không nằm trong egress allowlist của sandbox — Apps Script tải hộ từ IP Google). Bổ sung ngữ cảnh từ trường `related` (snippet + tên báo) của item trending và từ các item `category=news` cùng chủ đề. Nếu `?article=` trả `{"ok":false}` (trang JS-render không parse được) VÀ `related` snippets quá mỏng để dựng đủ 7 act → quay lại bước 1 chọn chủ đề khác (POST đánh dấu used chủ đề cũ trước).
   - Viết lại bằng tiếng Việt theo văn phong bản tin, gọn, giữ nguyên số liệu/mốc/tên. Nếu nguồn chính là báo tiếng Anh: KHÔNG dịch máy word-by-word, giữ tên riêng + thuật ngữ phổ biến, đóng khung "điều này nghĩa là gì với người / thị trường VN" nếu có góc đó. TUYỆT ĐỐI không bịa số liệu ngoài nguồn.
   - **Đối chiếu tối thiểu 2 nguồn** cho claim lớn khi có thể (item `news` + 1 URL trong `related`). Chênh lệch số liệu giữa các nguồn → chọn con số của báo chính thống hơn, hoặc nói "khoảng".

3. Nhận "cách dựng" (construction style): POST `<EXEC>` với `{"action":"claim_style","video":"<slug>"}` → trả `{"ok":true,"index":N,"style":"N-tên"}`. Dùng ĐÚNG style đó (chi tiết ở videos/CONSTRUCTION-STYLES.md). KHÔNG đọc videos/style-rotation-state.json để lấy chỉ số. Gọi claim_style NGAY SAU bước 1 (đã POST đánh dấu used), trước khi dựng.

4. Viết BRIEF.md + SCRIPT.md + CAPTION.md trong videos/<slug>/. Khởi tạo project qua hyperframes CLI (KHÔNG copy state file từ project cũ).
   - SCRIPT.md: MỘT dòng = MỘT act (7 dòng, act 7 là CTA), văn phong tin tức. TUYỆT ĐỐI KHÔNG viết tắt — viết đầy đủ đúng cách đọc thành tiếng vì ElevenLabs đọc verbatim: "AI" → "trí tuệ nhân tạo" (hoặc "ây-ai" nếu ngữ cảnh cần, nhất quán trong 1 video), "AGI" → "trí tuệ nhân tạo tổng quát", "API" → "ây-pi-ai", "CEO" → "giám đốc điều hành", "USD" → "đô la Mỹ", "GB"/"TB" → "gi-ga-bai"/"tê-ra-bai" (bảng đầy đủ ở mục "Voiceover" của videos/BRAND-SYSTEM.md). Tên riêng đọc nguyên được thì giữ. Số lớn viết theo cách người Việt đọc ("4.000 tỷ" → "4 nghìn tỷ").
   - QUAN TRỌNG: lời voice act 7 (CTA) kêu gọi để lại bình luận / nêu quan điểm nhưng KHÔNG được nhắc tên kênh ("Tin Tức Số"). Tên kênh chỉ xuất hiện bằng hình.
   - BRIEF.md và text hiển thị trên video vẫn được viết tắt bình thường — ràng buộc không-viết-tắt CHỈ áp cho SCRIPT.md.
   - CAPTION.md: theo đúng mẫu videos/_reference-astra-openai/CAPTION.md — dòng đầu 1 emoji + tiêu đề IN HOA nêu sự kiện/số liệu chính; 1 dòng trống; 2-3 đoạn ngắn nêu số liệu / bối cảnh / các mặt của vấn đề (mỗi đoạn mở 1 emoji như 📊 ⚠️ 💬); 1 câu hỏi tranh luận mời bình luận; 1 dòng trống; "📌 Nguồn: <tên báo>, <ngày>" (thêm " · dịch" nếu nguồn tiếng Anh); 1 dòng trống; hashtag gồm **#TinTucSo #TinNong #TinTrongNgay** + 4-6 hashtag liên quan chủ đề. Kèm 1 bản rút gọn ≤500 ký tự (mục "Bản rút gọn cho Threads") để dành — tuyến này CHƯA đăng Threads. TUYỆT ĐỐI không bịa số liệu ngoài BRIEF.md/SCRIPT.md.

5. Ảnh minh hoạ bài báo (bắt buộc theo brand — Hook + Article Image Card + thumbnail): GET `<EXEC>?image=<id tin>` → trả JSON `{"ok":true,"mime":"image/jpeg","filename":"...","data":"<base64>"}`. Giải mã ra file: `curl -s "<EXEC>?image=<id>" | jq -r .data | base64 -d > assets/img/article-hero.jpg`. KHÔNG curl thẳng CDN báo. Nếu ảnh trả về là thumbnail Google quá nhỏ / mờ (item `trend`) → dùng `id` của một item `category=news` cùng chủ đề để lấy ảnh báo chuẩn. Nếu `{"ok":false}` → quay lại bước 1 chọn chủ đề khác có ảnh dùng được.

**GATE B — kiểm duyệt nội dung trước render** (bắt buộc, `automation/policy/COMPLIANCE-GATE.md` mục GATE B). Trên SCRIPT.md + CAPTION.md + ảnh vừa tải, kiểm: (B1) mọi số liệu / mốc / tên / phát ngôn TRUY ĐƯỢC về `?article=`, `related`, hoặc item `news` — KHÔNG con số nào tự nghĩ; phân biệt cáo buộc/dự đoán vs sự thật; nguồn tiếng Anh dịch đúng nghĩa không thêm kết luận. (B2) không bạo lực / thù ghét / quấy rối / doxxing / nội dung tình dục hoặc liên quan trẻ em; phê bình hành vi-sản phẩm-chính sách không phải con người; tin thiên tai/tai nạn KHÔNG khai thác đau thương / không giật tít thương vong. (B3) KHÔNG giả danh nền tảng / hãng / cơ quan / chuyên gia (kênh là nguồn tin độc lập); không testimonial-doanh-thu-dashboard giả; không engagement bait; không lừa đảo / link độc. (B4 — AI media) giọng AI narrator chung = OK không cần disclosure; ảnh og:image bài báo có dẫn nguồn = OK; ảnh AI minh hoạ ý niệm (bản đồ/sơ đồ/biểu tượng) = OK; ❌ TUYỆT ĐỐI KHÔNG dùng AI tái dựng cảnh thật / người thật như-ảnh-chụp, hiện trường giả, phát ngôn giả, bằng chứng giả — nếu cần hình một sự kiện thật mà không có ảnh thật thì dùng đồ hoạ ý niệm rõ ràng (ngoại lệ bất khả kháng: thêm chữ "Hình ảnh minh hoạ do AI tạo" + khai AI trong YouTube Studio). (B5) ảnh chỉ từ `?image=` / AI tự tạo / stock có quyền — không watermark; nhạc tự sinh (Lyria, hoặc ElevenLabs Music khi Lyria lỗi/hết quota — xem bước 8); SFX repo; không né Content ID; video 100% tự dựng không reup. (B6) tiêu đề = sự kiện/số liệu + tò mò hợp lý, KHÔNG "SỐC!!!"/"CHẤN ĐỘNG"/"100% CHẮC CHẮN"; thumbnail phản ánh đúng nội dung; caption không nhồi/không hashtag lạ. (B7 — nguyên bản, rủi ro cao nhất) video có ≥1 góc nhìn / phân tích / cách trình bày dữ liệu riêng — KHÔNG chỉ đọc lại tiêu đề báo; không trùng bố cục video gần nhất. (B8) flag pháp lý VN nếu chạm an ninh mạng / thông tin sai / dữ liệu cá nhân / quảng cáo có điều kiện — KHÔNG bịa số điều luật. Vi phạm B mà không sửa được → DỪNG, không dựng tiếp.

6. Sinh giọng đọc ElevenLabs — model_id eleven_v3 (KHÔNG eleven_multilingual_v2 — không hỗ trợ tiếng Việt), voice_id RCmOaM1iiIH5xX3QXjIF ("Khánh Lâm - tin tức, thời sự"), voice_settings.speed ~1.09, key từ biến môi trường ELEVENLABS_API_KEY. Tạo TỪNG DÒNG script 1 file mp3 riêng (line1.mp3 … line7.mp3), không gộp. Đo ffprobe từng file (input cho timing frame).

7. Dựng composition 7 act (Hook → What happened → Key facts → Data moment → Context → Impact → CTA) theo đúng định hướng ẩn dụ hình ảnh của style đã claim ở bước 3. Hook + Brand Anchor (logo + tên kênh "Tin Tức Số" góc trên-phải, "Nguồn:" góc trên-trái) + act 7 CTA giữ cố định theo brand, không thuộc style. Màu nhận diện = cam `#FF5A1F` (KHÔNG dùng xanh của video tham chiếu), cảnh báo/rủi ro = đỏ `#FF4438`. Act 6 (Impact) nội dung là sự thật/số liệu đã xảy ra — KHÔNG suy đoán tương lai. Act 7 CTA: câu hỏi tranh luận của tin + 2 lựa chọn đối lập (icon bằng CSS shape, KHÔNG emoji) + pill "Bình luận quan điểm của bạn" + chữ ký logo (tham chiếu videos/_reference-astra-openai/compositions/frames/07-cta.html cho bố cục, đổi màu sang cam). Ảnh Hook/Article Image Card dùng file đã tải ở bước 5. Logo dùng videos/<slug>/public/logo.png (copy từ videos/_reference-astra-openai/public/logo.png). data-duration mỗi frame = độ dài voice thật (bước 6) + đệm ~0.3-0.5s. Tổng thời lượng dưới 75 giây. VENDOR GSAP LOCAL (assets/vendor/gsap.min.js từ npm i gsap) — KHÔNG dùng <script src="cdn.jsdelivr.net/...">, CDN đó bị chặn ở sandbox. KHÔNG emoji trong composition (thiếu font khi render).
   ⚠️ CÂN BẰNG DỌC (bắt buộc — lỗi đã tái phát 2 lần ở tuyến gốc): nội dung MỖI frame phải LẤP ĐẦY khung 1080×1920, KHÔNG dồn hết lên 55-65% trên rồi để trống đen nửa dưới. Phần tử cuối của frame kết thúc quanh top: 1400-1680px, không dừng ở ~1000px. Frame ít nội dung → căn giữa dọc HOẶC phóng to element. Bám dải phân bố dọc của videos/_reference-astra-openai/compositions/frames/ (top ~220 → ~1290px+). Xem mục "Cân bằng dọc" trong BRAND-SYSTEM.md. Khi soát thumbnail/frame ở bước 10, với MỖI frame tự hỏi "nửa dưới có trống đen không?" — có thì sửa trước khi render.

8. BGM: Google Lyria (lyria-recipe.py, key GEMINI_API_KEY) — recipe CALM: --density 0.25 --brightness 0.4, prompt kiểu "calm ambient news underscore, soft synth pads, sparse, minimal pulse, no drums, instrumental only", LUÔN kèm --negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming". BGM ambient NHẸ, ít nhịp — KHÔNG dùng prompt "driving/fast-paced".
   **[Bắt buộc — 2026-09-22] Fallback sang ElevenLabs Music khi Lyria lỗi/hết quota**: nếu lyria-recipe.py trả lỗi (bất kỳ mã nào — 429/quota=0, 5xx, timeout...) dù đã thử đủ 3 model (lyria-3.5, lyria-3-pro-preview, lyria-3-pro), KHÔNG dừng routine — chuyển sang ElevenLabs Music (cùng domain/key ElevenLabs đã dùng ở bước 6, không cần cấu hình gì thêm):
   ```bash
   curl -sS -X POST https://api.elevenlabs.io/v1/music \
     -H "xi-api-key: $ELEVENLABS_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "calm ambient news underscore, soft synth pads, sparse, minimal pulse, no drums, instrumental only, no vocals, no lyrics, no singing, no choir, no rap",
       "music_length_ms": <tổng thời lượng video tính bằng ms + đệm>,
       "force_instrumental": true,
       "model_id": "music_v2_5",
       "output_format": "mp3_44100_128"
     }' \
     -o assets/bgm/track-raw.mp3 -w 'HTTP:%{http_code}\n'
   ```
   `force_instrumental: true` đảm bảo không lời chắc chắn hơn negative-prompt. Chỉ dừng routine (không giao video thiếu nhạc) nếu CẢ Lyria VÀ ElevenLabs Music đều lỗi. Ghi rõ nguồn BGM thực tế đã dùng (Lyria hay ElevenLabs Music fallback) vào tóm tắt cuối và COMPLIANCE.md.
   Retrim khớp tổng thời lượng + fade-out 2-3s cuối. data-volume track BGM = 0.30. SFX mật độ vừa phải. Gắn data-audio-group="voiceover" cho mọi <audio> giọng, rồi chạy `node <hyperframes-audio skill dir>/scripts/carve.mjs --comp index.html --strength 0.4`. Chạy lại carve sau MỌI thay đổi timing/audio.

9. npm run check — fix hết error trước khi render.

10. Trước khi render: kiểm tra ffmpeg -version, nếu chưa có thì `sudo apt-get update && sudo apt-get install -y ffmpeg` (sandbox có quyền root). Render bằng npm run render. Verify đầy đủ 4 bước theo mục 7 của videos/PRODUCTION-WORKFLOW.md: (1) ffprobe duration đúng thiết kế; (2) ffmpeg silencedetect — không có khoảng lặng chết giữa video; (3) trích frame tại các mốc quan trọng, xem bằng Read; (4) transcript so với SCRIPT.md — nếu Whisper model host bị chặn thì dùng Gemini multimodal (generativelanguage.googleapis.com, gọi GET /v1beta/models trước để lấy tên model còn dùng được, vd gemini-flash-latest). Soát riêng lỗi đọc lắp / đánh vần do viết tắt lọt vào SCRIPT.md — nếu có, sửa dòng đó thành dạng viết đầy đủ rồi sinh lại đúng file voice đó. Nếu render/verify thất bại hoàn toàn dù đã thử cài đặt, DỪNG LẠI, ghi rõ lý do.

11. Xuất thumbnail: `ffmpeg -y -ss 3.5 -i output/<slug>.mp4 -frames:v 1 -q:v 2 output/thumbnail.jpg` (t trong cửa sổ Hook 3-5s, sau khi toàn bộ animation Hook vào ổn định — đọc timeline compositions/frames/01-hook.html để tính chính xác). Xem lại bằng Read — xác nhận logo + tên kênh + badge nguồn + tiêu đề + 2 tag tương phản đều hiện đủ, rõ, không mờ/cắt.

**GATE C — kiểm tra cuối + ghi COMPLIANCE.md** (bắt buộc, `automation/policy/COMPLIANCE-GATE.md` mục GATE C + OUTPUT). Xem lại thumbnail + 3-4 frame render (đúng B6, không phần tử bịa); transcript khớp SCRIPT (không câu nào "chế thêm" khi sinh voice); caption đăng = CAPTION.md đã qua GATE B. Ghi `videos/<slug>/COMPLIANCE.md` theo mẫu OUTPUT trong COMPLIANCE-GATE.md (policy_version, kết quả GATE A/B/C, **trending_signal**, decision, risk_level, ai_disclosure_required, copyright_notes, claims_verified, sensitive_flags, vietnam_legal_flags). **Nếu decision != APPROVE hoặc risk_level ∈ {ORANGE, RED, BLACK} → DỪNG routine ở đây, KHÔNG đăng, ghi lý do vào tóm tắt cuối.**

12. Thêm 1 dòng vào mảng "log" của videos/style-rotation-state.json (index + style + slug + ngày + từ khoá trending) cho người đọc theo dõi — KHÔNG cần sửa last_used_index (con trỏ thật do claim_style / Apps Script quản lý).

13. Commit + push toàn bộ videos/<slug>/ (kèm output/<slug>.mp4 + output/thumbnail.jpg + COMPLIANCE.md — thư mục output KHÔNG bị .gitignore; node_modules/ thì bị) lên <REPO> nhánh master. Chỉ tới đây nếu GATE C = APPROVE.

14. Đăng Facebook Fanpage — POST `<EXEC>` (endpoint đã cấu hình sẵn token Facebook — KHÔNG cần và KHÔNG được tự tìm/nhập token nào khác):
   `{"action":"publish_facebook","video_url":"https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/<slug>.mp4","thumbnail_url":"https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/thumbnail.jpg","caption":"<CAPTION.md, phần TRÊN dấu --->","video":"<slug>","title":"<tiêu đề tin>"}` — đăng video lên Reels của Trang. thumbnail_url BẮT BUỘC.
   Chỉ gọi SAU KHI bước 13 push xong (Facebook tải video/ảnh từ raw.githubusercontent.com). Gọi POST bằng client theo được redirect 302 giữ nguyên POST (vd python urllib) — curl -L làm mất Content-Length (lỗi 411) hoặc đổi POST→GET. Lệnh tự ghi log vào Google Sheet. Nếu thất bại, KHÔNG coi cả routine là thất bại — ghi rõ lỗi vào tóm tắt, phần sản xuất video vẫn hoàn tất nếu bước 10-13 ok.

15. Đăng kênh YouTube — POST `<EXEC>` (đã cấu hình sẵn OAuth2 refresh token YouTube — KHÔNG tự tìm/nhập credential):
   `{"action":"publish_youtube","video_url":"https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/<slug>.mp4","thumbnail_url":"https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/thumbnail.jpg","title":"<tiêu đề tin> #Shorts","description":"<CAPTION.md, phần TRÊN dấu --->","privacy":"public","video":"<slug>"}`
   Hệ thống tự viết hoa toàn bộ tiêu đề trước khi đăng — không cần tự viết hoa. Chỉ gọi SAU KHI bước 13 push xong. Nếu lệnh thất bại toàn bộ, hoặc chỉ phần thumbnail báo lỗi 403 youtube.thumbnail (quyền custom thumbnail của kênh mới chỉ mở sau ~24h kể từ khi xác minh SĐT), KHÔNG coi cả routine là thất bại — video vẫn đăng thành công dù thiếu thumbnail tùy chỉnh; ghi rõ trạng thái vào tóm tắt.
   TUYẾN NÀY CHƯA đăng Instagram / Threads — KHÔNG gọi publish_instagram / publish_threads.

   ⚠️ **QUY TẮC BẮT BUỘC chống đăng trùng (sự cố thật đã xảy ra 11/9/2026 — 1 video lên YouTube 2 lần)**:
   upload video lên YouTube qua `<EXEC>` thường mất 1.5-3 phút; ở nhiều lần gọi, kết nối HTTP phía client
   bị timeout/`RemoteDisconnected` DÙ video đã upload thành công ở phía server (Apps Script vẫn chạy xong
   `videos.insert`, chỉ là response không kịp trả về trước khi client bỏ cuộc). Nếu KHÔNG kiểm tra trước
   khi gọi lại, việc "thử lại vì tưởng lỗi" sẽ tạo ra 2 video thật trên kênh (đã xảy ra: video A đăng lúc
   T, request timeout ở T+2p, agent gọi lại ngay và tạo video B ở T+2p30 — cả 2 đều public, agent chỉ biết
   về video B).
   **Do đó**: nếu `publish_youtube` báo lỗi kiểu timeout/connection-drop/`RemoteDisconnected` (KHÔNG phải
   lỗi JSON rõ ràng như 401/403 từ chính API) → **TUYỆT ĐỐI KHÔNG gọi lại `publish_youtube` ngay** — trước
   tiên gọi `{"action":"list_yt_content","limit":5}` (read-only, không đăng/xoá gì) để xem 5 video mới nhất
   trên kênh có video nào title trùng + thời gian đăng (`publishedAt`) nằm trong vài phút gần đây không.
   Nếu ĐÃ THẤY video đó → dùng `video_id` đó cho bước 16, KHÔNG gọi `publish_youtube` lần 2. Chỉ gọi lại
   `publish_youtube` nếu `list_yt_content` xác nhận thật sự chưa có video nào khớp.

16. Chốt thumbnail YouTube: xem result.thumbnail (và result.thumbnail_attempts) trong phản hồi publish_youtube. Nếu code != 200 (hoặc để chắc chắn), SAU khi đăng xong đợi ~90s rồi gọi POST `<EXEC>` `{"action":"yt_set_thumbnail","video_id":"<id YouTube>","thumbnail_url":"https://raw.githubusercontent.com/quangnv-cloud/tin-tuc-so/master/videos/<slug>/output/thumbnail.jpg"}`. code:200 là xong. Nếu vẫn 403 youtube.thumbnail → ghi "chưa dính do quyền kênh chưa mở", không coi là lỗi routine.

17. Kết thúc bằng 1 bản tóm tắt ngắn: **từ khoá trending đã chọn + vị trí/approx_traffic** (hoặc "chọn từ category=news, lý do …"), tin + nguồn báo thật (+ "đã dịch từ <nguồn>" nếu tiếng Anh), style + index từ claim_style, thời lượng video, **kết quả GATE A/B/C (risk_level + decision)**, kết quả verify 4 bước, đường dẫn file trong repo, kết quả đăng Facebook (Reel — thành công/lỗi + post id), kết quả đăng YouTube (thành công/lỗi + video id/link + trạng thái thumbnail). Nếu là **skip slot** (GATE A không có chủ đề an toàn) → chỉ cần nêu rõ đã skip + liệt kê vài từ khoá trending đã xét và lý do loại. Nếu BẤT KỲ bước 1-13 thất bại — HOẶC **GATE A/B/C không PASS/APPROVE** — DỪNG LẠI ở đó, KHÔNG thực hiện bước 14-16, không hạ thấp tiêu chuẩn brand / không bỏ bước verify / **không "nới" cổng chính sách** — báo lỗi rõ ràng trong tóm tắt thay vì giao 1 video lỗi hoặc đăng nội dung vi phạm.
