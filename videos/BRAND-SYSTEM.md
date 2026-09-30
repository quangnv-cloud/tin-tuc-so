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
| 7. CTA | Đặt lại câu hỏi tranh luận của tin ("bước tiến hay mối lo?") + 2 lựa chọn đối lập (icon CSS: mũi tên lên cam / tam giác cảnh báo đỏ) + pill **"Bình luận quan điểm của bạn"** + chữ ký logo. ~5–7s là khởi điểm, KHÔNG phải trần cứng — thực tế đã tới ~8,7s khi cần đủ chỗ cho voice CTA đọc hết + pulse animation chạy đủ vòng + không cắt gấp đoạn kết. Ưu tiên "voice đọc trọn + nhịp animation đủ + kết thúc mượt" hơn ép đúng khung 5–7s. |

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

## Kỹ thuật hình ảnh nâng cao (BẮT BUỘC — mọi video, từ video tiếp theo trở đi)

**[Thêm 2026-09-16]** Đúc kết từ video mẫu `mau-tin-tuc-so-nang-cap` (phiên 2026-09-15/16, đạt
~95/100 theo chuẩn quốc tế) — trước đây các kỹ thuật này chỉ tồn tại trong 1 video mẫu dựng tay,
CHƯA từng ghi thành quy tắc nên video routine hàng ngày không áp dụng, vẫn trông "phong cách cũ"
(nền phẳng, không glow, không caption, trống đen nửa dưới khung — xác nhận qua frame thật ngày
16/9 của 2 video `tuoi-nghi-huu-2027-thay-doi` và Công Nghệ Số `ai-tuyen-dung-han-quoc`). Từ giờ
BẮT BUỘC, không phải tùy chọn.

### 1. Nền có chiều sâu (depth background) — mount 1 lần ở root `index.html`, phía sau mọi scene

2-3 blob mờ trôi rất chậm + hạt sao tĩnh nhấp nháy nhẹ — KHÔNG phải "particle explosion":

```html
<div id="bg-depth" style="position:absolute;inset:0;overflow:hidden;z-index:0;">
  <div class="blob" style="position:absolute;width:640px;height:640px;border-radius:50%;
    background:radial-gradient(circle, rgba(255,90,31,0.20), transparent 70%);
    filter:blur(60px); top:-120px; left:-160px;"></div>
  <div class="blob" style="position:absolute;width:560px;height:560px;border-radius:50%;
    background:radial-gradient(circle, rgba(255,68,56,0.16), transparent 70%);
    filter:blur(60px); top:900px; right:-200px;"></div>
  <div class="blob" style="position:absolute;width:520px;height:520px;border-radius:50%;
    background:radial-gradient(circle, rgba(255,90,31,0.12), transparent 70%);
    filter:blur(60px); bottom:-180px; left:200px;"></div>
  <svg id="bg-stars" viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:100%;height:100%;">
    <!-- 35-45 <circle r="1.5..3" fill="#fff" opacity="0.15..0.4">, toạ độ sinh bằng PRNG seed
         cố định bên dưới — KHÔNG dùng Math.random()/Date.now() (vi phạm deterministic render) -->
  </svg>
</div>
```

```js
function mulberry32(seed) { // đổi seed mỗi video để bố cục hạt khác nhau
  return function () {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
    var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
var rand = mulberry32(20260916); // rand() sinh cx/cy 35-45 particle trong 0..1080 / 0..1920

// repeat:-1 CHỈ an toàn ở index.html gốc (có data-duration riêng), KHÔNG trong sub-composition
// thiếu data-duration (gây lỗi lint gsap_infinite_repeat).
tl.to(".blob", { x: "+=40", y: "-=30", duration: 18, ease: "sine.inOut", repeat: -1, yoyo: true, stagger: 3 }, 0);
tl.to("#bg-stars circle", { opacity: "+=0.25", duration: 4, ease: "sine.inOut", repeat: -1, yoyo: true, stagger: { each: 0.15, from: "random" } }, 0);
```

### 2. Glow accent bằng chính màu brand (không đổi hue theo từng cảnh)

```css
.evidence-card, .article-image-wrap {
  box-shadow: 0 0 40px rgba(255, 90, 31, 0.14);
}
```

### 3. Caption karaoke đồng bộ giọng đọc (BẮT BUỘC cho mọi video từ giờ)

1. Sau khi có voice từng dòng, gọi ElevenLabs STT lấy timestamp từng TỪ: `POST
   https://api.elevenlabs.io/v1/speech-to-text` với `model_id=scribe_v1`,
   `timestamps_granularity=word`, file = từng `lineN.mp3`.
2. Cộng `data-start` của dòng đó vào timestamp cục bộ → timestamp TUYỆT ĐỐI theo composition.
3. Gom từ thành chunk 3-6 từ (đủ ngắn vừa 1 dòng ở độ rộng safe-zone), mỗi chunk là 1 `.cap-chunk`,
   hiện từ lúc từ đầu chunk bắt đầu tới khi từ cuối kết thúc + ~0.3s đệm.
4. Mỗi từ là 1 `<span class="w">`, mặc định trắng/mờ, tween sang màu brand (`#FF5A1F`) ĐÚNG lúc từ
   đó được đọc (`duration` ~0.08-0.12s, ease đơn giản).
5. Vị trí: trong safe-zone (xem mục "Chuẩn xuất bản video" bên dưới — tránh ~11-17% đáy khung).
6. Không giọng đọc ở đoạn nào = không caption đoạn đó.

### 4. Smash-cut nội bộ cho act dài (>10s) — chỉ khi có điểm chuyển nội dung thật

```css
.cutflash { position: absolute; inset: 0; z-index: 6; pointer-events: none; opacity: 0;
  background: linear-gradient(180deg, rgba(255,90,31,0.4), rgba(255,68,56,0.18)); }
```
```js
tl.fromTo("#cutflash", { opacity: 0 }, { opacity: 0.55, duration: 0.05, ease: "none" }, T);
tl.to("#cutflash", { opacity: 0, duration: 0.16, ease: "power1.in" }, T + 0.05);
tl.fromTo("#content", { scale: 1 }, { scale: 0.986, duration: 0.06, ease: "power1.out" }, T);
tl.to("#content", { scale: 1, duration: 0.14, ease: "power2.out" }, T + 0.061);
```
Kèm 1 SFX click riêng đúng lúc `T`.

### 5. Bằng chứng thật đa dạng — không lặp lại 1 ảnh cho nhiều cảnh

Tìm qua nhiều nguồn tin độc lập nếu cần; đa dạng loại (ảnh hiện trường, văn bản/tài liệu, biểu đồ)
qua các act khác nhau thay vì dùng đi dùng lại 1 ảnh.

### 6. Biểu đồ tỉ lệ động thay thẻ số tĩnh khi có ≥2 số liệu để so sánh

`scaleY` từ 0, `transform-origin: bottom`, chiều cao tỉ lệ đúng số liệu thật — trực quan hơn 2 thẻ
số đặt cạnh nhau.

### 7. Cân bằng dọc — GATE đo được (bổ sung cho mục "Cân bằng dọc" ở trên)

Mục "Cân bằng dọc" phía trên đã có quy tắc nhưng lỗi vẫn tái diễn vì chỉ dựa "tự hỏi mình" lúc soát
Studio. Từ giờ **BẮT BUỘC** ở bước Verify (`PRODUCTION-WORKFLOW.md` §7): trích 1 frame thật ở CUỐI
animation-reveal của MỖI act giữa (không chỉ đầu act) bằng `ffmpeg -ss <t> ... out.png` rồi xem
bằng Read tool — xác nhận phần tử cuối cùng kết thúc trong `top: 1400-1680px`. Nếu dừng sớm hơn
~1000px, PHẢI thêm phần tử bổ sung trước khi coi là xong, không chỉ ghi chú "cân nhắc sau".

## Chuẩn xuất bản video (CỐ ĐỊNH — dùng chung cho MỌI kênh: BOT BÁN HÀNG, Công Nghệ Số, Tin Tức Số,
Kinh Tế Số, Retify — không đổi theo từng video)

Một tỉ lệ khung hình + một mức chất lượng duy nhất, vì FB Reels/TikTok/YouTube Shorts đều dùng
chung 9:16 — không tối ưu riêng theo nền tảng.

- **Tỉ lệ khung hình / độ phân giải**: 9:16 dọc, cố định **1080×1920** (`data-width`/`data-height`
  trên `#root`). Không hạ xuống 720×1280.
- **Frame rate**: 30fps.
- **Lệnh render bắt buộc** (KHÔNG chạy `npm run render` trơn — mặc định của hyperframes thấp hơn
  chuẩn này):
  ```bash
  npx hyperframes preview --stop
  npx --yes hyperframes@<pinned-version> render --quality high --video-bitrate 10M --browser-timeout 60
  ```
- **Audio**: AAC 192kbps. Target loudness **-14 LUFS integrated**, True Peak ≤ **-1.0 dBTP** (đúng
  chuẩn normalize của FB/TikTok/YouTube). Lệch quá ±1 LU → `loudnorm` 2-pass trước khi giao file.
- **Vùng an toàn UI nền tảng (safe zone)** — caption/anchor/badge/CTA không đặt trong:
  - ~11–17% đáy khung hình (thanh mô tả + nút tương tác TikTok/Reels/Shorts đè lên)
  - ~150–200px cạnh phải (cột icon like/comment/share/follow)
- **Bản phái sinh** (không bắt buộc, chỉ khi cần đăng chéo nền tảng ngang/vuông): tái khung từ bản
  1080×1920 gốc bằng kỹ thuật nền blur, không dựng canvas khác trong composition:
  ```bash
  ffmpeg -i <goc.mp4> -filter_complex \
    "[0:v]split=2[bg][fg];[bg]scale=W:H:force_original_aspect_ratio=increase,crop=W:H,gblur=sigma=20[bgb]; \
     [fg]scale=W:H:force_original_aspect_ratio=decrease[fgs];[bgb][fgs]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]" \
    -map "[v]" -map 0:a -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k <ra.mp4>
  ```
  (1:1 → W=H=1080; 16:9 → W=1920, H=1080)

## Final QC Checklist

Brand (đúng `#FF5A1F` / `#0B0E14`, logo + tên kênh góc trên-phải, nguồn góc trên-trái) · **Cân
bằng dọc (nội dung lấp đầy khung, KHÔNG trống đen nửa dưới — xem mục "Cân bằng dọc")** · Text
(headline dễ đọc, số liệu nổi bật, keyword highlight đúng màu, không nhồi chữ) · Motion (sinh động
không lấn text, không effect thừa, không phần tử lộ tĩnh) · Image (ảnh thật trong card, không che
nội dung) · Audio (BGM nhẹ không lấn giọng, không vocal, VO không đọc tên kênh) · Act 7 CTA (câu
hỏi bám đúng góc tranh luận của tin, pill bình luận rõ) · Editorial (tin là trung tâm, không bịa
số liệu / nguồn, act cuối nội dung là sự thật) · **Xuất bản** (đúng 1080×1920/30fps, render bằng
`--quality high --video-bitrate 10M`, loudness -14 LUFS ±1 LU, không caption/anchor lấn safe zone
đáy/phải) · **Hình ảnh nâng cao** (nền có chiều sâu, glow brand-color, caption karaoke đồng bộ
giọng đọc, cân bằng dọc đã verify bằng frame thật — xem mục "Kỹ thuật hình ảnh nâng cao").

## Nguyên tắc cốt lõi

**TEXT kể chuyện. MOTION giải thích. IMAGE chứng minh. BRAND nhận diện. CTA mời tranh luận.**
Cảm giác cần đạt: "một bản tin nóng hiện đại thiết kế bằng ngôn ngữ motion graphics" — không
phải "một clip câu view giật gân".

Video mẫu tham chiếu ĐẦY ĐỦ khung motion (kế thừa từ Công Nghệ Số): `videos/_reference-astra-openai/`
— tham chiếu bố cục / nhịp / kỹ thuật, KHÔNG tham chiếu màu (video đó dùng xanh cũ) và KHÔNG tham
chiếu chủ đề.
