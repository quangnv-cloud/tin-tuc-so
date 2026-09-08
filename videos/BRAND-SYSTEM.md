# TIN TỨC SỐ — Hệ thống thương hiệu & sản xuất video tin nóng trong ngày

Nguồn tham chiếu chung cho MỌI video tin nóng / trending của kênh. Không lặp lại toàn văn trong từng
`BRIEF.md`, chỉ trích phần liên quan. Đọc song song với `PRODUCTION-WORKFLOW.md` (quy trình thao
tác), `CONSTRUCTION-STYLES.md` (10 cách dựng xoay vòng) và `ROUTINE.md` (12 bước routine + bước phát
hiện trending riêng của tuyến này).

Tuyến này **tách hoàn toàn** khỏi các tuyến khác (Gmail, Apps Script, repo, token riêng) nhưng
**kế thừa toàn bộ ngữ pháp motion-graphics** của khung "Công Nghệ Số" — chỉ đổi màu nhận diện sang
**cam tin nóng**, đổi mô-típ nhận diện sang **quả địa cầu + vành quỹ đạo** (theo logo), đổi chủ đề
sang tin nóng trong ngày, và thêm **một bước phát hiện chủ đề trending từ Google Trends VN** trước
khi chọn tin.

## Định vị & tính cách thương hiệu

Bản tin nóng trong ngày: nhanh, gọn, dữ-liệu-hoá, TỈNH TÁO — không giật gân. Bám chủ đề khán giả VN
đang thực sự quan tâm (Google Trends), nhưng lọc rất chặt: chỉ làm tin có thể trình bày trung lập,
xây dựng, không gây hại. Đưa tin + đặt câu hỏi để khán giả tranh luận — KHÔNG hype, KHÔNG câu view
bằng drama, KHÔNG sai sự thật. Tin là trung tâm.

**Tuyến này KHÔNG làm**: drama/đời tư người nổi tiếng, hình sự / khởi tố / điều tra cá nhân, chính
trị / bầu cử / nhân sự cấp cao, thể thao nước ngoài thuần giải trí, nội dung 18+, thuyết âm mưu.
Xem GATE A trong `automation/policy/COMPLIANCE-GATE.md` (bản tuyến này đã siết chặt thêm).

## Bảng màu (cố định — không tự thêm màu)

| Vai trò | Hex |
| --- | --- |
| Primary — cam tin nóng | `#FF5A1F` |
| Nền gần đen | `#0B0E14` |
| Card tối | `#121724` |
| Chữ trắng | `#FFFFFF` |
| Cảnh báo / rủi ro — đỏ | `#FF4438` |

Không dùng: xanh dương, xanh lá, tím, neon, rainbow gradient. Cam `#FF5A1F` là màu nhận diện (khớp
vành quỹ đạo trong logo); đỏ `#FF4438` CHỈ cho tín hiệu cảnh báo / mặt "mối lo" / gạch xoá / nhấn
tương phản, không rải khắp khung. Cho phép chuyển sắc cam→đỏ-cam trong 1 phần tử lớn (masthead,
số liệu focal) để khớp gradient logo — không dùng như nền toàn khung.

## Thứ bậc thị giác (bắt buộc mọi frame)

```
TEXT (quan trọng nhất — số liệu, tên chủ thể, kết luận)
  ↓
MOTION GRAPHIC (giải thích / nhấn mạnh, phục vụ text)
  ↓
ẢNH BÀI BÁO (bằng chứng / context — không bao giờ là yếu tố lớn nhất)
```

- **Primary text**: số liệu / tên mô hình, công ty / từ khoá / kết luận. Montserrat 700–900, contrast cao.
- **Secondary text**: giải thích, nhỏ hơn, Montserrat 500–600.
- **Supporting text**: nguồn / ngày / chú thích, nhỏ nhất.
- **Keyword highlight**: trong 1 câu, chỉ số liệu / tên riêng nổi bật bằng `#FF5A1F` (hoặc `#FF4438`
  nếu là điểm tiêu cực / rủi ro) — không để cả câu cùng visual weight.
- Màu chữ: trắng trên nền tối / ảnh tối; cam `#FF5A1F` để highlight; đỏ `#FF4438` để highlight điểm rủi ro; chữ tối
  `#0B0E14` trên card sáng (hiếm dùng).

## Typography

**Font chuẩn duy nhất: Montserrat** cho MỌI vai trò (headline / body / nhãn chrome viết hoa
tracked). Weight cần: 400/500/600/700/800/900, self-host 2 subset latin + vietnamese mỗi weight
(`@font-face` + `unicode-range`). Khi tải qua Google Fonts `css2` bằng `curl`, dùng User-Agent
trình duyệt CŨ (Chrome ~55) để Google trả từng file weight riêng, không phải 1 variable font.

## Chữ hoa / thường

Viết hoa chữ cái đầu câu + danh từ riêng theo chính tả tiếng Việt. KHÔNG lowercase cả câu, KHÔNG
UPPERCASE cả câu dài. Ngoại lệ: nhãn nhỏ kiểu chrome (kicker, badge — "RA MẮT", "TRANH CÃI", "TÁC
ĐỘNG") giữ UPPERCASE tracked. **Bẫy kỹ thuật**: nếu style cha có `text-transform`, nó đè lên chữ đã
gõ trong HTML — kiểm tra và gỡ.

## Fixed Elements — Brand Anchor (0 → hết video)

- **Logo Tin Tức Số** (`public/logo.png` — quả địa cầu + vành quỹ đạo cam, đã tách nền) + chữ **"Tin Tức Số"** —
  góc **trên-phải**. Fixed vị trí / cỡ / margin. Không animation liên tục, không che nội dung.
- **Nguồn** ("Nguồn: <tên nguồn>" hoặc "Nguồn: <tên nguồn quốc tế> · dịch") — góc **trên-trái**.
  Fixed typography. Không tự tạo / đổi tên nguồn.

Hai anchor này dựng ở tầng root/`index.html`, hiện ngay khi Hook kết thúc — KHÔNG lặp lại độc lập
trong từng frame. Frame Hook (0 → ~6s) tự mang masthead (logo + tên kênh) + badge nguồn + ngày
trong panel riêng của nó.

## Cân bằng dọc — nội dung phải LẤP ĐẦY khung 1080×1920 (bắt buộc, lỗi đã tái phát)

**KHÔNG được dồn toàn bộ nội dung lên 55–65% phía trên rồi để trống đen 1/3–1/2 khung dưới.**
Đây là lỗi người dùng đã phản hồi 2 lần (video Astra + video routine đầu tiên `ai-agent-vuot-rao`).
Khi dựng MỖI frame của 5 act giữa + act CTA:

- **Vùng an toàn nội dung**: từ ~`top: 300px` (ngay dưới Brand Anchor) tới ~`top: 1720px`. Phần tử
  cuối cùng của frame (card / bar / dòng / quote / pill) phải KẾT THÚC trong khoảng
  `top: 1400px → 1680px` — KHÔNG dừng ở ~1000px.
- **Frame ít nội dung** (Hook chỉ có tên chủ thể + 2 tag; CTA; Data moment 1 số): căn khối nội dung
  **giữa dọc** trong vùng an toàn (`#root` là flex `align-items:center; justify-content:center` với
  padding trên/dưới ~màn hình, HOẶC dịch khối xuống bằng `top` lớn hơn), HOẶC phóng to element
  (font lớn hơn, card cao hơn, spacing rộng hơn) để chiếm hết chiều cao — đừng để nó co cụm ở trên.
- **Hook**: ảnh chiếm ~nửa trên; panel (masthead + badge + tên chủ thể + 2 tag) đặt sao cho tag
  cuối kết thúc quanh `top: 1500–1650px`, không phải ~1100px. Nếu panel ngắn, giãn khoảng cách
  masthead → badge → tiêu đề → tag, hoặc tăng cỡ tiêu đề chủ thể.
- **Tham chiếu cụ thể**: các frame trong `videos/_reference-astra-openai/compositions/frames/` — phần tử trải
  từ `top: ~220px` tới `top: ~1290px`+ (xem `03-facts`, `04-data`, `05-context`). Dùng làm chuẩn
  bố cục dọc, KHÔNG copy-paste nhưng bám cùng dải phân bố.
- **QC bắt buộc**: khi soát Studio thumbnail / frame render (bước verify), với MỖI frame tự hỏi
  "nửa dưới khung có trống đen không?" — nếu có, sửa lại bố cục dọc trước khi render/đăng.

## Cấu trúc 7 act

Giới hạn tổng: **dưới 75 giây** (nhỉnh hơn tuyến kinh doanh vì có act CTA). Không mốc cứng khác —
độ dài thật khớp kịch bản, không kéo khung để lấp giờ.

| Act | Nội dung |
| --- | --- |
| 1. Hook | Masthead (logo + "Tin Tức Số") + badge nguồn + ngày + tên chủ thể TO + **2 tag tương phản ngắn** (vd "● Mạnh nhất  ● Tranh cãi nhất"). Hiểu được ngay khi tắt tiếng. |
| 2. What happened | Chuyển từ hook sang nội dung tin thật (ảnh bài báo trong card + 1–2 câu chốt chuyện gì xảy ra). |
| 3. Key facts | Ai / cái gì / khi nào — kinetic typography, lower third, data card. |
| 4. Data moment | Con số / benchmark / mốc quan trọng nhất thành focal point — NUMBER > GRAPHIC. |
| 5. Context | Vì sao / nền tảng — timeline, so sánh, trích dẫn, sơ đồ. |
| 6. Impact | Ý nghĩa với người dùng / ngành / thị trường VN. **Act cuối phải là SỰ THẬT đã xảy ra** — không suy đoán "liệu... có... không". |
| 7. CTA | Đặt lại câu hỏi tranh luận của tin ("bước tiến hay mối lo?") + 2 lựa chọn đối lập (icon CSS: mũi tên lên cam / tam giác cảnh báo đỏ) + pill **"Bình luận quan điểm của bạn"** + chữ ký logo. ~5–7s. |

**Khớp khung hình với giọng đọc thật**: `data-duration` mỗi frame = độ dài file voice thật của
dòng đó (`ffprobe`) + đệm ~0.3–0.5s. KHÔNG copy khung giờ từ video trước (để lại khoảng lặng chết
2s+, nhịp phim chậm). Khi rút ngắn khung, co giãn TOÀN BỘ mốc animation nội bộ frame đó.

**Mỗi video một cách dựng khác nhau**: giữ brand (màu, font, 7 act, image-first, sentence case,
anchor) nhưng bố cục / motion cụ thể của 5 act giữa đổi theo style xoay vòng (`CONSTRUCTION-STYLES.md`)
— không copy-paste HTML/CSS 1 frame từ video trước rồi đổi chữ.

## Voiceover

**Giọng chuẩn kênh: ElevenLabs "Khánh Lâm - tin tức, thời sự"** (`voice_id: RCmOaM1iiIH5xX3QXjIF`),
**`model_id: eleven_v3`** — KHÔNG dùng `eleven_multilingual_v2` (không hỗ trợ tiếng Việt dù tên
"Multilingual"). `voice_settings.speed` ~1.09. Tạo TỪNG DÒNG script 1 file mp3 riêng, khớp
`data-start` frame tương ứng — không gộp cả kịch bản 1 lần gọi API.

**[BẮT BUỘC] KHÔNG đọc tên kênh trong lời thoại** — TTS đọc "Tin Tức Số" sai nhịp / lạc giọng. Tên
kênh chỉ xuất hiện bằng HÌNH (masthead Hook + Brand Anchor + chữ ký act CTA). Lời CTA kêu gọi bình
luận nhưng KHÔNG nhắc tên kênh.

**[BẮT BUỘC] KHÔNG viết tắt trong `SCRIPT.md`** (TTS đọc verbatim). Quy đổi khi soạn:
- `AI` → `trí tuệ nhân tạo` (hoặc `ây-ai` nếu ngữ cảnh cần đọc như tên gọi — nhất quán trong 1 video)
- `AGI` → `trí tuệ nhân tạo tổng quát`; `API` → `ây-pi-ai`; `CEO` → `giám đốc điều hành`;
  `IPO` → `phát hành cổ phiếu lần đầu`
- `USD` → `đô la Mỹ`; `%` giữ nguyên; `km` → `ki-lô-mét`; `GB`/`TB` → `gi-ga-bai`/`tê-ra-bai`
- Tên riêng / mã đọc nguyên được thì giữ (`OpenAI`, `Nvidia`, `Gemini`, `ChatGPT`, `iPhone`) —
  chỉ ép viết đầy đủ khi nghe thử thấy TTS đọc sai.
- Số lớn viết theo cách người Việt đọc: `4.000 tỷ` → `4 nghìn tỷ` cho chắc.

**Text hiển thị trên video vẫn được viết tắt biên tập** ("GPT-5", "8 tỷ USD" hợp lệ về hình) —
ràng buộc này CHỈ áp cho `SCRIPT.md`.

Verify bằng phiên âm ngược (Whisper/Gemini, ép `language=Vietnamese`) so với script gốc — nhầm âm
gần giống ("lấn"→"lớn") chấp nhận được; câu sai cấu trúc/nghĩa hoàn toàn là dấu hiệu giọng đọc sai
ngôn ngữ. Soát riêng lỗi đọc lắp / đánh vần do viết tắt lọt vào `SCRIPT.md`.

Gắn `data-audio-group="voiceover"` cho mọi `<audio>` giọng, rồi chạy `carve.mjs --comp index.html`
để duck BGM dưới giọng.

## Nhạc nền (BGM)

**[Quy tắc thương hiệu cố định]** BGM ambient NHẸ, ít nhịp, gần như không tiết tấu — người dùng
đã phản hồi bản đầu "quá nhiều nhịp, lấn giọng khi xem". KHÔNG dùng prompt "driving / fast-paced"
như tuyến kinh doanh.

- Sinh qua Google Lyria (`lyria-recipe.py`, key `GEMINI_API_KEY`), **LUÔN** kèm
  `--negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming"` — BGM 100% không lời.
- Recipe calm: `--density 0.25 --brightness 0.4`, prompt kiểu
  `"calm ambient tech-news underscore, soft synth pads, sparse, minimal pulse, no drums, instrumental only"`.
- `data-volume` track BGM = **0.30**. carve `--strength 0.4`.
- Retrim khớp tổng thời lượng video + fade-out 2–3s cuối. Nghe/soi waveform để chắc không dính vocal.
- Công thức đầy đủ: `videos/_reference-astra-openai/AUDIO-NOTES.md`.

## SFX

Đặt cue tại điểm pop-in text/card quan trọng + điểm chuyển cảnh chính (không phải MỌI lần chuyển
cảnh). Palette tham chiếu: `videos/_reference-astra-openai/assets/sfx/` (chime / click-soft / impact-bass /
pop / whoosh-short). Mật độ vừa phải — đây là bản tin, không phải trailer.

## GSAP / kỹ thuật (bài học bắt buộc áp dụng)

- **Vendor GSAP local**: `assets/vendor/gsap.min.js` (từ `npm i gsap`), KHÔNG `<script src="cdn.jsdelivr.net/...">`
  — CDN đó bị chặn ở egress sandbox cloud.
- Dùng `#root { ... }` trơn cho style gốc frame, KHÔNG `#root[data-composition-id="..."]` (font
  rơi về Times New Roman im lặng khi nhiều sub-composition mount lồng nhau).
- Reveal SVG (đường nối, vòng tròn, node) phải có state ẩn mặc định đáng tin (`opacity: 0` CSS
  hoặc `scale: 0` trong tween khởi tạo) — KHÔNG chỉ dựa `stroke-dasharray`/`getTotalLength()`.
- Mọi `gsap.fromTo(el, {from...}, {to...}, START)` có `from` KHÁC trạng thái ẩn (opacity 0 / scale 0)
  đều NGUY HIỂM — GSAP hiển thị `from` đó suốt thời gian TRƯỚC `START` → phần tử "hiệu ứng" lộ tĩnh
  từ đầu clip. Dùng MỘT tween với `keyframes: [...]` cho chuyển động nhiều giai đoạn, KHÔNG tween
  `duration: 0.001` để "chốt tức thời".
- KHÔNG `width` cố định (px) cho container chứa số/chữ auto-fit — số 3 chữ số của video sau sẽ
  tràn layout đặt cho số 2 chữ số của video trước. Để auto-width, hoặc verify bằng ảnh render thật.
- KHÔNG dùng emoji trong composition (không có font emoji khi render → thiếu ký tự). Icon = CSS
  shapes / SVG.
- CSS `transform` + GSAP `xPercent`/`yPercent` trên cùng phần tử xung đột — chọn 1.
- **Debug nhanh**: khi `hyperframes preview --background` chạy, endpoint
  `http://localhost:<port>/api/projects/<id>/thumbnail/index.html?t=<giây>&format=png&output=source&v=<cachebust>`
  trả PNG render thật. Luôn đổi `v=` mỗi lần gọi (cache server-side).

## Cổng kiểm duyệt chính sách nền tảng (bắt buộc)

Trước khi xuất bản MỌI video: chạy `automation/policy/COMPLIANCE-GATE.md` (GATE A lúc chọn tin,
GATE B trước render, GATE C + ghi `videos/<slug>/COMPLIANCE.md` trước khi đăng). Nội dung phải tuân
thủ chính sách YouTube/Google + Meta (Facebook/Instagram/Threads) — bản đầy đủ ở
`automation/policy/`. RED / ORANGE / BLACK → DỪNG, không đăng. Điểm rủi ro cao nhất của kênh tự
động: "inauthentic / mass-produced" (mỗi video phải có góc nhìn riêng, không chỉ đọc lại tiêu đề
báo) và AI synthetic media (KHÔNG tái dựng cảnh thật/người thật như ảnh chụp).

## Final QC Checklist

Brand (đúng `#FF5A1F` / `#0B0E14`, logo + tên kênh góc trên-phải, nguồn góc trên-trái) · **Cân
bằng dọc (nội dung lấp đầy khung, KHÔNG trống đen nửa dưới — xem mục "Cân bằng dọc")** · Text
(headline dễ đọc, số liệu nổi bật, keyword highlight đúng màu, không nhồi chữ) · Motion (sinh động
không lấn text, không effect thừa, không phần tử lộ tĩnh) · Image (ảnh thật trong card, không che
nội dung) · Audio (BGM nhẹ không lấn giọng, không vocal, VO không đọc tên kênh) · Act 7 CTA (câu
hỏi bám đúng góc tranh luận của tin, pill bình luận rõ) · Editorial (tin là trung tâm, không bịa
số liệu / nguồn, act cuối nội dung là sự thật).

## Nguyên tắc cốt lõi

**TEXT kể chuyện. MOTION giải thích. IMAGE chứng minh. BRAND nhận diện. CTA mời tranh luận.**
Cảm giác cần đạt: "một bản tin nóng hiện đại thiết kế bằng ngôn ngữ motion graphics" — không
phải "một clip câu view giật gân".

Video mẫu tham chiếu ĐẦY ĐỦ khung motion (kế thừa từ Công Nghệ Số): `videos/_reference-astra-openai/`
— tham chiếu bố cục / nhịp / kỹ thuật, KHÔNG tham chiếu màu (video đó dùng xanh cũ) và KHÔNG tham
chiếu chủ đề.
