# Hướng dẫn kỹ thuật dựng video — TIN TỨC SỐ (Technical Construction Guide)

> **Vai trò của file này**: `BRAND-SYSTEM.md`, `PRODUCTION-WORKFLOW.md`, `CONSTRUCTION-STYLES.md`,
> `ROUTINE.md` nói **CÁI GÌ** phải đúng (màu, act, quy trình, ẩn dụ hình ảnh) ở mức khá cao —
> hex code, tên style, mô tả bằng lời ("mỗi fact là 1 thẻ bo góc"). File này nói **CODE THẬT
> TRÔNG NHƯ THẾ NÀO** — được rút ra bằng cách đọc trực tiếp `index.html` / `compositions/frames/*.html`
> đã render thật của 8 video đã sản xuất (`chung-khoan-viet-nang-hang-ban-rong`,
> `iphone-18-ra-mat-viet-nam`, `v-league-vong-1-ban-thang-tang`, `iphone-duo-man-hinh-gap`,
> `khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`, `gia-xang-dau-tang-hon-1200-dong-lit`,
> `cpi-my-thang-8-fed-tang-lai-suat`, `iphone-18-pro-thay-doi-so-voi-17-pro`) cộng
> `_reference-astra-openai` (template gốc). Đọc 4 file kia TRƯỚC, đọc file này để lấy khung
> HTML/CSS/GSAP copy-paste được. Không lặp lại nội dung 4 file kia trừ khi đang minh hoạ bằng
> code thật cho đúng 1 quy tắc của chúng.
>
> **Không có project mẫu nào khác trong tay bạn** ngoài 4 file brand + file này. Mọi trích dẫn
> code dưới đây là **thật**, lấy nguyên văn từ file đã render — copy, đổi nội dung/placeholder,
> không cần đoán cú pháp.

---

## Mục lục

0. [Quy ước đọc file này](#0-quy-ước-đọc-file-này)
1. [Kiến trúc thư mục dự án](#1-kiến-trúc-thư-mục-dự-án)
2. [`index.html` — composition gốc](#2-indexhtml--composition-gốc)
3. [Hệ thống suy ra timing từ voice thật](#3-hệ-thống-suy-ra-timing-từ-voice-thật)
4. [Act 1 — Hook (cố định)](#4-act-1--hook-cố-định)
5. [Act 7 — CTA (cố định)](#5-act-7--cta-cố-định)
6. [5 act giữa theo từng style dựng (6 style thật + 4 style extrapolate)](#6-5-act-giữa-theo-từng-style-dựng)
7. [Cân bằng dọc — công thức + bằng chứng đo pixel thật](#7-cân-bằng-dọc--công-thức--bằng-chứng-đo-pixel-thật)
8. [Quy tắc GSAP — bug thật + fix thật](#8-quy-tắc-gsap--bug-thật--fix-thật)
9. [Audio pipeline cụ thể](#9-audio-pipeline-cụ-thể)
10. [Khung frame chung copy-paste được](#10-khung-frame-chung-copy-paste-được)
11. [Mâu thuẫn thực tế đã phát hiện (đọc trước khi làm theo mù quáng)](#11-mâu-thuẫn-thực-tế-đã-phát-hiện)

---

## 0. Quy ước đọc file này

- Mọi khối code dưới đây là **trích nguyên văn** (đôi khi rút gọn phần `@font-face` lặp lại 12
  dòng giống hệt nhau ở mọi file — xem mục 1 để có khối `@font-face` đầy đủ copy 1 lần) từ đúng
  slug/act được ghi trong tiêu đề khối. Khi khác với brand docs, phần "Ghi chú" ngay dưới khối nói rõ.
- `{{PLACEHOLDER}}` = phần bạn phải tự điền cho video mới. Mọi chỗ khác giữ nguyên cấu trúc.
- Canvas cố định: **1080×1920px, dọc (portrait)**. Mọi con số px trong file này là theo hệ toạ độ
  đó (top-left gốc `0,0`, `top:` đo từ mép trên).

---

## 1. Kiến trúc thư mục dự án

Cây thư mục đầy đủ (từ `iphone-18-pro-thay-doi-so-voi-17-pro`, dự án mới nhất/đã QC kỹ nhất):

```
videos/<slug>/
├── index.html                    # composition gốc — mount 7 act + Brand Anchor + audio
├── hyperframes.json              # config CLI (registry, paths) — KHÔNG chỉnh tay, sinh bởi `hyperframes init`
├── meta.json                     # {id, name, createdAt} — chỉ vậy, KHÔNG chứa duration/fps
├── package.json                  # 4 script npx hyperframes@<version pinned> <cmd>
├── package-lock.json
├── gen_voice.py                  # script gọi ElevenLabs, sinh line1.mp3..line7.mp3
├── BRIEF.md                      # tóm tắt nguồn tin, số liệu, ảnh
├── SCRIPT.md                     # 7 dòng thoại (1 dòng = 1 act), không viết tắt
├── CAPTION.md                    # caption đăng FB/YouTube
├── COMPLIANCE.md                 # GATE A/B/C, trending_signal, claims_verified, QC log
├── compositions/
│   └── frames/
│       ├── 01-hook.html          # act 1 — CỐ ĐỊNH cấu trúc (mục 4)
│       ├── 02-what.html          # act 2 — style-specific (mục 6)
│       ├── 03-facts.html         # act 3 — style-specific
│       ├── 04-data.html          # act 4 — style-specific, focal number
│       ├── 05-context.html       # act 5 — style-specific
│       ├── 06-impact.html        # act 6 — style-specific
│       └── 07-cta.html           # act 7 — CỐ ĐỊNH cấu trúc (mục 5)
├── assets/
│   ├── fonts/                    # 12 file Montserrat woff2 (6 weight × 2 subset latin/vietnamese)
│   ├── vendor/gsap.min.js        # GSAP vendor LOCAL — từ `npm i gsap`, KHÔNG CDN (xem mục 8)
│   ├── voice/ (hoặc audio/)      # line1.mp3..line7.mp3 — TÊN THƯ MỤC KHÔNG NHẤT QUÁN, xem Ghi chú
│   ├── bgm/
│   │   ├── raw.wav                # (một số project giữ lại) output thô từ lyria-recipe.py
│   │   └── track.mp3              # bản đã retrim/fade, đây mới là file `index.html` trỏ tới
│   ├── sfx/                       # chime.mp3, click-soft.mp3, impact-bass-1.mp3, pop.mp3, whoosh-short.mp3
│   └── img/article-hero.jpg       # ảnh báo thật, tải qua `?image=<id>` (xem PRODUCTION-WORKFLOW.md §1.9)
├── public/logo.png                # logo kênh — copy từ `_reference-astra-openai/public/logo.png`
├── output/
│   ├── <slug>.mp4                 # render cuối — COMMIT, không bị .gitignore
│   └── thumbnail.jpg              # frame trích ở giây 3–5 của Hook
└── node_modules/                  # (có thể xuất hiện, do .gitignore) — không commit
```

**Ghi chú tên thư mục audio (thấy khác nhau giữa các project thật)**:
`chung-khoan-viet-nang-hang-ban-rong`, `cpi-my-thang-8-fed-tang-lai-suat`,
`iphone-18-pro-thay-doi-so-voi-17-pro` dùng `assets/voice/lineN.mp3`; còn
`gia-xang-dau-tang-hon-1200-dong-lit` dùng `assets/audio/lineN.mp3`. Cả hai đều hợp lệ — chỉ
cần `<audio src="...">` trong `index.html` trỏ đúng đường dẫn thật đã dùng. Khuyến nghị: dùng
`assets/voice/` (đa số dự án + template tham chiếu dùng tên này).

### `hyperframes.json` (giống hệt ở mọi project, không chỉnh tay)

```json
{
  "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
  "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry",
  "paths": {
    "blocks": "compositions",
    "components": "compositions/components",
    "assets": "assets"
  },
  "media": {
    "autoProxy": true
  }
}
```

### `meta.json` (tối giản — KHÔNG có duration/fps/dimensions)

```json
{
  "id": "iphone-18-pro-thay-doi-so-voi-17-pro",
  "name": "iphone-18-pro-thay-doi-so-voi-17-pro",
  "createdAt": "2026-09-13T00:35:00.000Z"
}
```

Kích thước canvas (`1080×1920`) và fps sống trong `index.html` (`data-width`/`data-height` trên
`#root`) và trong config render của CLI, không phải ở đây. Đừng thêm field không có trong schema.

### `package.json` — script CLI, luôn pin version

```json
{
  "name": "iphone-18-pro-thay-doi-so-voi-17-pro",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "npx --yes hyperframes@0.8.35 preview",
    "check": "npx --yes hyperframes@0.8.35 check",
    "render": "npx --yes hyperframes@0.8.35 render",
    "publish": "npx --yes hyperframes@0.8.35 publish"
  },
  "dependencies": {
    "gsap": "^3.15.0"
  },
  "devDependencies": {
    "@hyperframes/core": "^0.8.35"
  }
}
```

**Ghi chú version pin thật đã quan sát**: `chung-khoan-viet-nang-hang-ban-rong` pin
`0.8.30`, `iphone-18-pro-thay-doi-so-voi-17-pro` (mới nhất) pin `0.8.35` — version trôi theo
thời gian, đây là bình thường (`hyperframes init` mới stamp version CLI mới nhất tại thời điểm
đó). KHÔNG copy số version từ project cũ sang project mới — để `hyperframes init` tự điền.
`npm run check` / `npm run render` luôn gọi qua `npx --yes hyperframes@<version pinned trong
chính package.json này>`, không phải version global.

### `data-hf-id` — bookkeeping của Studio GUI, KHÔNG bắt buộc khi tự tay/agent viết HTML

Quan sát thật: `cpi-my-thang-8-fed-tang-lai-suat/compositions/frames/*.html` **không có một
`data-hf-id` nào** (0 occurrence ở cả 7 file frame — dự án này được agent viết tay 100%, chưa
từng mở qua Studio GUI để chỉnh sửa trực quan), trong khi `index.html` của CHÍNH dự án đó lại có
29 occurrence (do `hyperframes init` stamp sẵn ở khung root). Ngược lại, các dự án khác (ví dụ
`gia-xang-dau-tang-hon-1200-dong-lit`) có `data-hf-id` rải khắp mọi phần tử ở cả frame lẫn root —
dấu hiệu đã qua ít nhất 1 lần mở/lưu bằng Studio GUI, tool tự stamp id khi đó.

**Kết luận thực dụng**: khi bạn (Claude) tự viết HTML cho frame mới, **không cần tự bịa
`data-hf-id`** — bỏ qua hoàn toàn là hợp lệ và đã có tiền lệ thật (chạy `npm run check` vẫn PASS).
Đừng nhầm nó với `data-hf-id` là attribute bắt buộc của framework.

---

## 2. `index.html` — composition gốc

### 2.1 Bộ khung `<head>` — giống hệt nhau ở MỌI project (kể cả `_reference-astra-openai`)

```html
<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, height=1920">
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      @font-face { font-family: 'Montserrat'; font-weight: 400; src: url('assets/fonts/Montserrat-400-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
      @font-face { font-family: 'Montserrat'; font-weight: 400; src: url('assets/fonts/Montserrat-400-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }
      /* ... lặp lại đúng cặp latin/vietnamese này cho weight 500, 600, 700, 800, 900
             (12 @font-face rules tổng cộng — 6 weight × 2 subset).
             Weight nào KHÔNG dùng trong project thì vẫn có thể khai báo (không bắt buộc dùng hết),
             nhưng weight NÀO dùng trong CSS bên dưới thì BẮT BUỘC phải có cả 2 @font-face
             (latin + vietnamese) — thiếu subset vietnamese → dấu tiếng Việt rơi về font hệ thống. */

      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: #000; }
      #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #0B0E14; font-family: "Montserrat", sans-serif; color: #FFFFFF; }
      .scene { position: absolute; inset: 0; width: 100%; height: 100%; }

      #brand-anchor { position: absolute; inset: 0; z-index: 90; pointer-events: none; opacity: 0; }
      #ba-source { position: absolute; left: 44px; top: 46px; display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px; border-radius: 8px; background: rgba(11,14,20,0.6); border: 1px solid rgba(255,255,255,0.12); backdrop-filter: blur(3px); }
      #ba-source .dot { width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; flex: none; }
      #ba-source span { font-weight: 500; font-size: 21px; letter-spacing: 0.02em; color: rgba(255,255,255,0.9); white-space: nowrap; }
      #ba-brand { position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }
      #ba-brand .mark { width: 44px; height: 44px; flex: none; }
      #ba-brand .mark img { display: block; width: 100%; height: 100%; }
      #ba-brand .word { font-weight: 800; font-size: 24px; letter-spacing: 0.01em; color: #fff; }
    </style>
  </head>
  <body>
```

**Điểm mấu chốt không được bỏ sót**:
- `html, body` cứng `1080px × 1920px`, `overflow: hidden`, nền `#000` — đây là "khung phim", mọi
  thứ tràn ra ngoài đều bị cắt khi render.
- `#root` KHÔNG có `data-composition-id` gắn vào **CSS selector** (chỉ là plain `#root { ... }`).
  Tấm `<div id="root">` thật ở body **có** attribute `data-composition-id="main"` nhưng CSS
  không bao giờ viết `#root[data-composition-id="main"] { ... }` — xem mục 8 vì sao.
- `.scene` — đây là class dùng cho các `<div>` mount từng act (`el-01-hook`, `el-02-what`, …).
  **Lưu ý quan trọng**: kênh này dùng tên class `.scene`, KHÔNG dùng `.clip` (tên class generic
  mà tài liệu HyperFrames core hay nhắc). Cả 8 project + reference đều nhất quán dùng `.scene`
  với đúng CSS full-frame absolute nói trên — đây là quy ước THẬT của kênh, cứ theo nó, không tự
  đổi sang `.clip`. `npm run check` chạy sạch với `.scene`.

### 2.2 `<body>` — thứ tự mount (7 `<div class="scene">` + Brand Anchor + audio) — trích nguyên văn `iphone-18-pro-thay-doi-so-voi-17-pro/index.html`

```html
    <!-- Kênh "Tin Tức Số" — tông cam tin nóng #FF5A1F trên nền #0B0E14.
         data-duration mỗi frame = độ dài voice thật (ffprobe) + đệm ~0.3-0.5s (CTA đệm dài hơn để pulse hoàn tất).
         Tổng video = 57.37s. 7 act: Hook (masthead riêng) → What → Facts → Data → Context → Impact → CTA.
         Style dựng: 4-split-comparison (chia đôi trái/phải, bảng 2 cột 17 Pro/18 Pro, chia đôi trên/dưới ở Impact). -->
    <div data-hf-id="hf-s2fk" id="root" data-composition-id="main" data-start="0" data-duration="57.37" data-width="1080" data-height="1920">

      <div data-hf-id="hf-c9z1" id="el-01-hook" class="scene" data-composition-id="01-hook" data-composition-src="compositions/frames/01-hook.html" data-start="0" data-duration="6.80" data-track-index="1"></div>
      <div data-hf-id="hf-8reo" id="el-02-what" class="scene" data-composition-id="02-what" data-composition-src="compositions/frames/02-what.html" data-start="6.80" data-duration="8.16" data-track-index="1"></div>
      <div data-hf-id="hf-djm6" id="el-03-facts" class="scene" data-composition-id="03-facts" data-composition-src="compositions/frames/03-facts.html" data-start="14.96" data-duration="9.02" data-track-index="1"></div>
      <div data-hf-id="hf-duau" id="el-04-data" class="scene" data-composition-id="04-data" data-composition-src="compositions/frames/04-data.html" data-start="23.98" data-duration="9.02" data-track-index="1"></div>
      <div data-hf-id="hf-ax3e" id="el-05-context" class="scene" data-composition-id="05-context" data-composition-src="compositions/frames/05-context.html" data-start="33.00" data-duration="8.63" data-track-index="1"></div>
      <div data-hf-id="hf-101n" id="el-06-impact" class="scene" data-composition-id="06-impact" data-composition-src="compositions/frames/06-impact.html" data-start="41.63" data-duration="8.24" data-track-index="1"></div>
      <div data-hf-id="hf-ndbo" id="el-07-cta" class="scene" data-composition-id="07-cta" data-composition-src="compositions/frames/07-cta.html" data-start="49.87" data-duration="7.50" data-track-index="1"></div>

      <div data-hf-id="hf-4xka" id="brand-anchor">
        <div data-hf-id="hf-mr34" id="ba-source"><span data-hf-id="hf-9gry" class="dot"></span><span data-hf-id="hf-u83e">Nguồn: VnExpress</span></div>
        <div data-hf-id="hf-218y" id="ba-brand"><span data-hf-id="hf-zeo6" class="mark"><img data-hf-id="hf-rrs2" src="public/logo.png" alt=""></span><span data-hf-id="hf-ottk" class="word">Tin Tức Số</span></div>
      </div>

      <audio data-hf-id="hf-gaf1" id="el-voice-1" src="assets/voice/line1.mp3" data-start="0" data-duration="6.347755" data-track-index="10" data-audio-group="voiceover"></audio>
      <audio data-hf-id="hf-53wm" id="el-voice-2" src="assets/voice/line2.mp3" data-start="6.80" data-duration="7.76" data-track-index="10" data-audio-group="voiceover"></audio>
      <audio data-hf-id="hf-6355" id="el-voice-3" src="assets/voice/line3.mp3" data-start="14.96" data-duration="8.672653" data-track-index="10" data-audio-group="voiceover"></audio>
      <audio data-hf-id="hf-chcn" id="el-voice-4" src="assets/voice/line4.mp3" data-start="23.98" data-duration="8.672653" data-track-index="10" data-audio-group="voiceover"></audio>
      <audio data-hf-id="hf-xae9" id="el-voice-5" src="assets/voice/line5.mp3" data-start="33.00" data-duration="8.280816" data-track-index="10" data-audio-group="voiceover"></audio>
      <audio data-hf-id="hf-xqh8" id="el-voice-6" src="assets/voice/line6.mp3" data-start="41.63" data-duration="7.888980" data-track-index="10" data-audio-group="voiceover"></audio>
      <audio data-hf-id="hf-7rpm" id="el-voice-7" src="assets/voice/line7.mp3" data-start="49.87" data-duration="5.877551" data-track-index="10" data-audio-group="voiceover"></audio>

      <audio data-hf-id="hf-rd28" id="el-sfx-hook" src="assets/sfx/impact-bass-1.mp3" data-start="0.32" data-duration="0.6" data-track-index="30" data-volume="0.35"></audio>
      <audio data-hf-id="hf-zjuv" id="el-sfx-t1" src="assets/sfx/whoosh-short.mp3" data-start="6.70" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio data-hf-id="hf-biaq" id="el-sfx-t2" src="assets/sfx/whoosh-short.mp3" data-start="14.86" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio data-hf-id="hf-wg1y" id="el-sfx-data" src="assets/sfx/pop.mp3" data-start="25.03" data-duration="0.4" data-track-index="30" data-volume="0.3"></audio>
      <audio data-hf-id="hf-n7fg" id="el-sfx-t3" src="assets/sfx/whoosh-short.mp3" data-start="32.90" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio data-hf-id="hf-xgh4" id="el-sfx-warn" src="assets/sfx/impact-bass-1.mp3" data-start="41.53" data-duration="0.6" data-track-index="30" data-volume="0.32"></audio>
      <audio data-hf-id="hf-dqse" id="el-sfx-t4" src="assets/sfx/whoosh-short.mp3" data-start="49.77" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio data-hf-id="hf-jvsk" id="el-sfx-o1" src="assets/sfx/pop.mp3" data-start="50.92" data-duration="0.35" data-track-index="30" data-volume="0.3"></audio>
      <audio data-hf-id="hf-u03g" id="el-sfx-o2" src="assets/sfx/click-soft.mp3" data-start="51.27" data-duration="0.35" data-track-index="30" data-volume="0.32"></audio>
      <audio data-hf-id="hf-jmod" id="el-sfx-cta" src="assets/sfx/chime.mp3" data-start="52.02" data-duration="1.2" data-track-index="30" data-volume="0.32"></audio>

      <audio data-hf-id="hf-r4eg" id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="57.37" data-track-index="20" data-volume="0.30"
             data-fx-carve="{&quot;enabled&quot;:true,&quot;sources&quot;:[&quot;voiceover&quot;],&quot;strength&quot;:0.4}"
             data-fx-chain="{&quot;version&quot;:1,&quot;nodes&quot;:[...4 nodes EQ do carve.mjs sinh...]}"
             data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;fx.n1.gain&quot;,&quot;points&quot;:[...hàng trăm điểm keyframe gain, mỗi ~0.14s một điểm...]}]}"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      tl.set('#brand-anchor', { opacity: 1 }, 6.80);
      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
```

**Đọc kỹ các điểm sau — đây là "hợp đồng" của `index.html`:**

1. **`#root` (composition `main`)** mang `data-start="0"` `data-duration="<tổng thời lượng>"`
   `data-width="1080"` `data-height="1920"` — đây là 4 thuộc tính bắt buộc của root timeline.
2. **7 `<div class="scene">`** — mỗi cái là 1 act, mount qua `data-composition-src` trỏ tới file
   frame tương ứng. `data-start` của act N+1 = `data-start` + `data-duration` của act N (nối đuôi
   nhau khít, không hở, không đè — xem bảng số ở mục 3).
3. **Brand Anchor** (`#brand-anchor`) là **1 khối HTML duy nhất ở root**, KHÔNG lặp lại trong
   từng frame. Nó gồm đúng 2 phần tử con:
   - `#ba-source` (góc **trên-trái**): 1 chấm cam + text `Nguồn: <tên báo>` — style **fixed**,
     không đổi theo act.
   - `#ba-brand` (góc **trên-phải**): logo (`public/logo.png`) + chữ `Tin Tức Số` — style **fixed**.
   - Toàn khối có `opacity: 0` mặc định trong CSS, và **CHỈ 1 dòng GSAP** ở cuối file bật nó lên:
     `tl.set('#brand-anchor', { opacity: 1 }, <data-duration của Hook>)` — tức Brand Anchor **ẩn
     trong suốt Hook**, xuất hiện đúng lúc Hook kết thúc, và **giữ nguyên `opacity:1` tới hết
     video** (không có tween tắt nó ở cuối). Đây chính là dòng "hiện ngay khi Hook kết thúc" mà
     `BRAND-SYSTEM.md` mô tả bằng lời — code thật chỉ là **1 `tl.set(...)`**, không phải
     `fromTo`/animation phức tạp.
4. **Audio voiceover**: mỗi `<audio id="el-voice-N">` có `data-audio-group="voiceover"` — đây
   là attribute mà `carve.mjs` dùng để biết "cái gì là giọng nói cần nhường chỗ". `data-start`
   của voice N **khớp chính xác** với `data-start` của scene N (voice bắt đầu đồng thời với frame
   hiện ra, không lệch).
5. **SFX**: mỗi `<audio>` SFX nằm ở `data-track-index="30"`, `data-volume` 0.3–0.35, cắm đúng vào
   các mốc "pop-in" quan trọng — **không phải mọi lần chuyển act đều có SFX** (chỉ ~1 SFX mỗi
   2 act là đủ, xem mục 9).
6. **BGM**: `<audio id="el-bgm" src="assets/bgm/track.mp3">`, `data-track-index="20"`,
   `data-volume="0.30"` (**KHÔNG BAO GIỜ đổi số 0.30** — đây là brand rule cứng). 3 attribute
   `data-fx-carve` / `data-fx-chain` / `data-automation` là **JSON string tự sinh bởi
   `carve.mjs`** — KHÔNG BAO GIỜ tự tay viết 3 attribute này. `data-automation` có thể dài
   **26.000+ ký tự** (hàng trăm điểm gain theo thời gian, ~1 điểm mỗi ~0.14s) — nếu bạn thấy 1
   dòng cực dài trong `index.html`, đó là carve output bình thường, không phải lỗi.

**Việc DUY NHẤT mà `<script>` cuối `index.html` làm** là khai báo 1 timeline `main` chứa đúng 1
dòng `tl.set(...)` cho Brand Anchor. KHÔNG có logic gì khác ở tầng root — mọi animation thật nằm
trong từng file frame riêng (mục 4–6).

### 2.3 Cross-check thứ 2 dự án — `_reference-astra-openai/index.html` (khác chủ đề, khác màu, CÙNG cấu trúc)

```html
    <!-- Bản THỬ tuyến "Công Nghệ Số" — tông xanh điện #4C8DFF trên nền #0B0E14.
         data-duration mỗi frame = độ dài voice thật (ffprobe) + đệm. Tổng video = 61.98s. -->
    <div data-hf-id="hf-qb3p" id="root" data-composition-id="main" data-start="0" data-duration="61.98" data-width="1080" data-height="1920">
      <div data-hf-id="hf-hzzz" id="el-01-hook" class="scene" data-composition-id="01-hook" data-composition-src="compositions/frames/01-hook.html" data-start="0" data-duration="6.46" data-track-index="1"></div>
      ...
      <div data-hf-id="hf-58ml" id="el-07-cta" class="scene" data-composition-id="07-cta" data-composition-src="compositions/frames/07-cta.html" data-start="54.92" data-duration="7.06" data-track-index="1"></div>

      <div data-hf-id="hf-4xka" id="brand-anchor">
        <div data-hf-id="hf-mr34" id="ba-source"><span data-hf-id="hf-9gry" class="dot"></span><span data-hf-id="hf-v5kj">Nguồn: TechCrunch</span></div>
        <div data-hf-id="hf-218y" id="ba-brand"><span data-hf-id="hf-zeo6" class="mark"><img data-hf-id="hf-8iod" src="public/logo.png" alt=""></span><span data-hf-id="hf-gpa3" class="word">Công Nghệ Số</span></div>
      </div>
      ...
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
      tl.set('#brand-anchor', { opacity: 1 }, 6.46);
      window.__timelines['main'] = tl;
    </script>
```

Duy nhất khác biệt so với 2.2: `#ba-source .dot { background: #4C8DFF; }` (màu xanh của tuyến
"Công Nghệ Số" thay vì `#FF5A1F` cam của "Tin Tức Số"), chữ thương hiệu là "Công Nghệ Số", và mốc
`tl.set(..., 6.46)` khớp `data-duration` của Hook video này (6.46s, khác 6.80s của video kia) —
**mốc bật Brand Anchor LUÔN bằng đúng `data-duration` của act Hook**, không phải số cố định.

---

## 3. Hệ thống suy ra timing từ voice thật

Đây là ví dụ **tái lập được 100%**, lấy từ `gia-xang-dau-tang-hon-1200-dong-lit` — chạy
`ffprobe` thật trên 7 file mp3 gốc, rồi đối chiếu với `data-duration`/`data-start` đã "nướng"
sẵn trong `index.html` của chính project đó.

### 3.1 Đo bằng `ffprobe` (lệnh thật, output thật)

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 assets/audio/line1.mp3
# 6.191020
```

### 3.2 Bảng đối chiếu đầy đủ (7 dòng, số liệu thật — không làm tròn thêm)

| Act | File voice | Độ dài voice thật (ffprobe, s) | Đệm thêm | `data-duration` frame (s) | `data-start` frame (s) |
|---|---|---:|---:|---:|---:|
| 1 Hook | line1.mp3 | 6.191020 | +0.40 | **6.59** | 0 |
| 2 What | line2.mp3 | 4.911020 | +0.40 | **5.31** | 6.59 |
| 3 Facts | line3.mp3 | 14.367347 | +0.40 | **14.77** | 11.90 |
| 4 Data | line4.mp3 | 6.922449 | +0.40 | **7.32** | 26.67 |
| 5 Context | line5.mp3 | 8.751020 | +0.40 | **9.15** | 33.99 |
| 6 Impact | line6.mp3 | 7.967347 | +0.40 | **8.37** | 43.14 |
| 7 CTA | line7.mp3 | 6.426122 | **+2.27** | **8.70** | 51.51 |
| **Tổng** | | | | **60.21s** | (51.51+8.70) |

Nguyên văn `index.html` (2 nhóm attribute khớp nhau tuyệt đối):

```html
<div id="el-01-hook" class="scene" ... data-start="0"     data-duration="6.59"  data-track-index="1"></div>
<div id="el-02-what" class="scene" ... data-start="6.59"  data-duration="5.31"  data-track-index="1"></div>
<div id="el-03-facts" class="scene" ... data-start="11.90" data-duration="14.77" data-track-index="1"></div>
<div id="el-04-data" class="scene" ... data-start="26.67" data-duration="7.32"  data-track-index="1"></div>
<div id="el-05-context" class="scene" ... data-start="33.99" data-duration="9.15"  data-track-index="1"></div>
<div id="el-06-impact" class="scene" ... data-start="43.14" data-duration="8.37"  data-track-index="1"></div>
<div id="el-07-cta" class="scene" ... data-start="51.51" data-duration="8.70"  data-track-index="1"></div>

<audio id="el-voice-1" src="assets/audio/line1.mp3" data-start="0"     data-duration="6.19"  .../>
<audio id="el-voice-2" src="assets/audio/line2.mp3" data-start="6.59"  data-duration="4.91"  .../>
<audio id="el-voice-3" src="assets/audio/line3.mp3" data-start="11.90" data-duration="14.37" .../>
<audio id="el-voice-4" src="assets/audio/line4.mp3" data-start="26.67" data-duration="6.92"  .../>
<audio id="el-voice-5" src="assets/audio/line5.mp3" data-start="33.99" data-duration="8.75"  .../>
<audio id="el-voice-6" src="assets/audio/line6.mp3" data-start="43.14" data-duration="7.97"  .../>
<audio id="el-voice-7" src="assets/audio/line7.mp3" data-start="51.51" data-duration="6.43"  .../>
```

### 3.3 Công thức áp dụng cho video mới

```
frame[i].data-start     = frame[i-1].data-start + frame[i-1].data-duration   (frame[0].data-start = 0)
voice[i].data-start     = frame[i].data-start                                 (đồng bộ tuyệt đối)
voice[i].data-duration  = ffprobe(lineI.mp3)                                  (không làm tròn quá 2 chữ số thập phân)
frame[i].data-duration  = voice[i].data-duration + đệm
  đệm act 1-6  ≈ 0.3 – 0.5s  (ví dụ trên dùng đúng 0.40s cho cả 6 act — chấp nhận 1 số đệm cố định
                              cho cả video, không cần khác nhau mỗi act)
  đệm act 7 (CTA) LỚN HƠN hẳn (ở đây 2.27s) — vì sau khi voice dứt, CTA còn cần thời gian cho
  animation "pulse" nút bấm (`yoyo repeat 3`, xem mục 5) chạy xong + giữ hình 1 nhịp trước khi
  video kết thúc hẳn.
tổng video = frame[cuối].data-start + frame[cuối].data-duration   (phải < 75s theo BRAND-SYSTEM.md)
```

### 3.4 Trường hợp biên đã xảy ra thật — khi tổng gần chạm trần 75s

`iphone-18-ra-mat-viet-nam` (COMPLIANCE.md): tổng 7 dòng voice thật đã dài **74.14s**, sát trần
75s. Quyết định thật: **giảm đệm mỗi frame xuống ~0.1s** (thay vì 0.3–0.5s khuyến nghị) để tổng
không vượt 75s, thay vì cắt bớt nội dung script. Đây là tiền lệ hợp lệ — ưu tiên **trần cứng
75s** hơn khuyến nghị đệm mềm khi 2 cái xung đột.

---

## 4. Act 1 — Hook (cố định)

### 4.1 Hai biến thể layout đã quan sát — biến thể "panel" chiếm đa số (7/8 dự án)

| Biến thể | Dự án dùng | Đặc điểm |
|---|---|---|
| **A — Panel dưới ảnh** (mặc định, khuyến nghị) | `_reference-astra-openai`, `chung-khoan-viet-nang-hang-ban-rong`, `iphone-18-ra-mat-viet-nam`, `v-league-vong-1-ban-thang-tang`, `iphone-duo-man-hinh-gap`, `khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`, `gia-xang-dau-tang-hon-1200-dong-lit` (7/8) | Ảnh chiếm nửa trên (`height` 620–940px tuỳ ảnh), 1 panel nền `#0B0E14` đặc bên dưới chứa toàn bộ masthead/badge/tên/tag — panel **không xuyên qua ảnh**, ranh giới rõ. |
| **B — Chồng trực tiếp lên ảnh + vạch chia dọc** | `iphone-18-pro-thay-doi-so-voi-17-pro` (1/8, style `4-split-comparison`) | Ảnh cao hơn (860px), masthead/badge/tên/tag đặt tuyệt đối chồng lên nửa dưới ảnh (không có panel nền riêng), thêm 1 vạch cam dọc mờ (`.hk-split`) ở mép trái để báo trước ẩn dụ "chia đôi" của style. |

**Khuyến nghị**: dùng biến thể **A (panel)** làm mặc định cho mọi style — đây là biến thể chiếm
đa số và khớp với `_reference-astra-openai` (template được `ROUTINE.md` trích dẫn). Chỉ cân nhắc
biến thể B khi style dựng là `4-split-comparison` và muốn Hook "gợi ý" ẩn dụ chia đôi ngay từ đầu.

### 4.2 Template chuẩn (biến thể A) — annotated, dựng từ `gia-xang-dau-tang-hon-1200-dong-lit/compositions/frames/01-hook.html`

```html
<template>
  <style>
    /* ... 12 @font-face rules — copy nguyên từ mục 2.1, CHỈ các weight thực dùng ở file này
           (400/500/700/800/900) — không bắt buộc chép cả 6 weight nếu không dùng hết ... */

    #root { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: #0B0E14; }

    /* --- KHỐI ẢNH (nửa trên) --- */
    .hk-photo { position: absolute; left: 0; right: 0; top: 0; height: {{PHOTO_HEIGHT_PX}}; overflow: hidden; background: #05070c; }
    .hk-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% {{FOCAL_Y_PERCENT}}%; }
    .hk-scrim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11,14,20,0.10) 0%, rgba(11,14,20,0.30) 55%, rgba(11,14,20,0.99) 100%); }
    /* .hk-orbit / .hk-tint: optional radial glow decor tuỳ style, KHÔNG bắt buộc */

    /* --- PANEL (nửa dưới, nền đặc) --- */
    .hk-panel { position: absolute; left: 0; right: 0; top: {{PANEL_TOP_PX}}; bottom: 0; background: #0B0E14; padding: {{PANEL_PAD_TOP}}px 60px 80px; display: flex; flex-direction: column; align-items: flex-start; }

    .hk-masthead { display: flex; align-items: center; gap: 13px; margin-bottom: 40px; opacity: 0; }
    .hk-logo { width: 52px; height: 52px; flex: none; }
    .hk-logo img { display: block; width: 100%; height: 100%; }
    .hk-mw { font-weight: 800; font-size: 30px; letter-spacing: 0.01em; color: #fff; }

    .hk-badge { display: inline-flex; align-items: center; gap: 12px; padding: 8px 18px 8px 8px; border-radius: 100px; border: 1.5px solid rgba(255,90,31,0.85); background: rgba(255,90,31,0.1); margin-bottom: 56px; opacity: 0; }
    .hk-badge .ring { width: 30px; height: 30px; border-radius: 50%; border: 3px solid #FF5A1F; display: flex; align-items: center; justify-content: center; flex: none; }
    .hk-badge .ring .dot { width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; }
    .hk-badge span.lbl { font-weight: 500; font-size: 21px; letter-spacing: 0.03em; color: #fff; white-space: nowrap; }
    /* biến thể badge đơn giản hơn (không có .ring, chỉ 1 chấm) cũng hợp lệ — xem 01-hook.html của
       iphone-18-pro-thay-doi-so-voi-17-pro: <span class="d"></span> thay vì <span class="ring"><span class="dot"></span></span> */

    .hk-name-wrap { overflow: hidden; }              /* BẮT BUỘC — đây là mask cho hiệu ứng slide-up */
    .hk-name-wrap + .hk-name-wrap { margin-top: 4px; }
    .hk-name { font-weight: 900; font-size: {{NAME_FONT_PX}}; line-height: 1.22; letter-spacing: -0.02em; color: #FF5A1F; white-space: nowrap; }
    /* line-height 1.22, KHÔNG phải 1 — xem mục 8.5, đây là fix thật cho bug dấu tiếng Việt bị cắt */

    .hk-tags { display: flex; flex-direction: column; gap: 28px; margin-top: 130px; }
    .hk-tag { display: flex; align-items: center; font-weight: 800; font-size: 46px; line-height: 1.2; color: #fff; opacity: 0; }
    .hk-tag.warn { color: #FF6B4A; }   /* tag "tiêu cực" dùng đỏ-cam nhạt hơn #FF4438 gốc 1 chút, chấp nhận được */
    .hk-tag .dot { display: inline-block; width: 16px; height: 16px; border-radius: 50%; background: currentColor; margin-right: 18px; flex: none; }
  </style>

  <div id="root" data-composition-id="01-hook" data-width="1080" data-height="1920">
    <div class="hk-photo">
      <img src="assets/img/article-hero.jpg" alt="">
      <div class="hk-scrim"></div>
    </div>

    <div class="hk-panel">
      <div class="hk-masthead">
        <div class="hk-logo"><img src="public/logo.png" alt=""></div>
        <div class="hk-mw">Tin Tức Số</div>
      </div>
      <div class="hk-badge"><span class="ring"><span class="dot"></span></span><span class="lbl">Nguồn: {{TÊN_BÁO}} · {{NGÀY}}</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-name1">{{DÒNG_1_TÊN_CHỦ_THỂ}}</div></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-name2">{{DÒNG_2_TÊN_CHỦ_THỂ}}</div></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>{{TAG_1_TÍCH_CỰC_HOẶC_TRUNG_TÍNH}}</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>{{TAG_2_TIÊU_CỰC_HOẶC_TRANH_CÃI}}</div>
      </div>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });
    tl.fromTo('.hk-photo', { autoAlpha: 0.5, scale: 1.12 }, { autoAlpha: 1, scale: 1, duration: 1.0, ease: 'power2.out' }, 0);
    tl.fromTo('.hk-panel', { y: 48 }, { y: 0, duration: 0.55, ease: 'power3.out' }, 0.1);
    tl.fromTo('.hk-masthead', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.3);
    tl.fromTo('.hk-badge', { autoAlpha: 0, scale: 0.9 }, { autoAlpha: 1, scale: 1, duration: 0.36, ease: 'back.out(1.7)' }, 0.52);
    tl.fromTo('#hk-name1', { yPercent: 118 }, { yPercent: 0, duration: 0.65, ease: 'power4.out' }, 0.8);
    tl.fromTo('#hk-name2', { yPercent: 118 }, { yPercent: 0, duration: 0.65, ease: 'power4.out' }, 0.94);
    tl.fromTo('#hk-t1', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.68);
    tl.fromTo('#hk-t2', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.92);
    window.__timelines['01-hook'] = tl;
  </script>
</template>
```

**Thứ tự reveal timeline (luôn giữ nguyên trình tự này, chỉ đổi số giây tuỳ nhịp voice)**:
ảnh zoom-out nhẹ (`scale 1.12→1`) → panel trượt lên (`y 48→0`) → masthead fade+slide →
badge nguồn "back.out" bounce nhẹ → tên chủ thể 2 dòng slide-up kiểu "text reveal" (`yPercent
118→0`, mask bằng `.hk-name-wrap{overflow:hidden}`) → 2 tag slide-in từ trái, tag sau trễ hơn
tag trước ~0.24s.

**Cái GÌ giống hệt nhau ở MỌI project (kể cả reference)**: cấu trúc DOM
(`.hk-photo > img + .hk-scrim` / `.hk-panel > .hk-masthead + .hk-badge + .hk-name-wrap×N +
.hk-tags`), thứ tự GSAP timeline, `ease` dùng (`power2.out`/`power3.out`/`power4.out`/
`back.out(1.7)`), việc dùng 2 `.hk-name-wrap` xếp chồng khi tên 2 từ dài (1 dòng nếu tên ngắn
— xem `_reference-astra-openai` dùng đúng 1 `.hk-name-wrap` cho "Astra").

**Cái GÌ đổi mỗi video**: nội dung text, `object-position` của ảnh (focal point), chiều cao
`.hk-photo`/`top` của `.hk-panel` (co giãn tuỳ ảnh), font-size `.hk-name` (208px nếu 1 dòng ngắn
như "Astra", 140px nếu 2 dòng như "GIÁ XĂNG"/"DẦU TĂNG"), và **KHÔNG BAO GIỜ** đổi màu — luôn
`#FF5A1F` (name/badge/dot) + `#FF6B4A` hoặc `#FF4438` (tag warn).

---

## 5. Act 7 — CTA (cố định)

CTA là act **giống nhau gần như copy-paste 1:1** giữa mọi project — kể cả `_reference-astra-openai`
(chỉ đổi 3 biến: màu accent, text, chữ ký logo). Đây là phần **ít rủi ro sáng tạo lại từ đầu
nhất** — hãy bám sát template dưới, không tự vẽ layout mới.

### 5.1 Diff giữa `_reference-astra-openai` (gốc) và `gia-xang-dau-tang-hon-1200-dong-lit` (cam hoá)

| | `_reference-astra-openai` | `gia-xang-dau-tang-hon-1200-dong-lit` |
|---|---|---|
| Accent màu | `#4C8DFF` (xanh) | `#FF5A1F` (cam) |
| Icon "lên" (`.t-opt.up .emo`) | vòng tròn viền xanh + mũi tên chéo lên | **giống hệt cấu trúc CSS**, chỉ đổi màu border/border-top/border-right sang `#FF5A1F` |
| Icon "xuống/cảnh báo" (`.t-opt.down .emo`) | tam giác CSS `border-bottom` màu `#FF8A5B` + dấu `!` | tam giác `border-bottom` màu **`#FF4438`** (đúng brand rule — đỏ cảnh báo) + dấu `!` |
| Nút CTA nền | `background: #4C8DFF` | `background: #FF5A1F` |
| Chữ ký cuối | logo + `Công Nghệ Số` | logo + `Tin Tức Số` |
| Emoji | **0** — toàn bộ icon là CSS shape (`border-radius`, `::before`/`::after`, tam giác `border`) | **0** — giữ nguyên nguyên tắc |

### 5.2 Template chuẩn (annotated, dựng từ `gia-xang-dau-tang-hon-1200-dong-lit/compositions/frames/07-cta.html`)

```html
<template>
  <style>
    /* ... @font-face 12 rules như mục 2.1 ... */

    #root { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: #0B0E14; }
    #root::before { content: ""; position: absolute; inset: 0; background: radial-gradient(80% 50% at 50% 34%, rgba(255,90,31,0.16), transparent 60%); }

    .t-wrap { position: absolute; left: 64px; right: 64px; top: {{HEAD_TOP_PX}}; text-align: center; }
    .t-kicker { font-weight: 700; font-size: 26px; letter-spacing: 0.26em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .t-head { margin-top: 30px; font-weight: 900; font-size: {{HEAD_FONT_PX}}; line-height: 1.14; color: #fff; }
    .t-head .ln { overflow: hidden; }              /* mask cho slide-up, giống hk-name-wrap */
    .t-head .ln > span { display: block; }

    .t-opts { display: flex; justify-content: center; align-items: stretch; gap: 20px; margin-top: 60px; }
    .t-opt { flex: 1; max-width: 400px; padding: 34px 22px; border-radius: 18px; border: 2px solid; opacity: 0; }
    .t-opt.up { border-color: rgba(255,90,31,0.75); background: rgba(255,90,31,0.1); }
    .t-opt.down { border-color: rgba(255,68,56,0.75); background: rgba(255,68,56,0.1); }
    .t-opt .emo { width: 44px; height: 44px; margin: 0 auto; position: relative; }
    .t-opt.up .emo { border: 4px solid #FF5A1F; border-radius: 50%; }
    .t-opt.up .emo::after { content: ""; position: absolute; left: 50%; top: 11px; width: 12px; height: 12px; border-top: 4px solid #FF5A1F; border-right: 4px solid #FF5A1F; transform: translateX(-50%) rotate(-45deg); }
    .t-opt.down .emo::before { content: ""; position: absolute; left: 0; bottom: 0; width: 0; height: 0; border-left: 22px solid transparent; border-right: 22px solid transparent; border-bottom: 40px solid #FF4438; }
    .t-opt.down .emo::after { content: "!"; position: absolute; left: 0; right: 0; bottom: -2px; text-align: center; font-weight: 900; font-size: 24px; color: #0B0E14; }
    .t-opt .lab { margin-top: 16px; font-weight: 800; font-size: 32px; line-height: 1.25; color: #fff; }
    .t-vs { display: flex; align-items: center; font-weight: 900; font-size: 34px; color: #6e6463; opacity: 0; }

    .t-cta { display: inline-flex; align-items: center; gap: 18px; margin-top: 64px; padding: 22px 38px; border-radius: 100px; background: #FF5A1F; opacity: 0; }
    .t-cta .ico { width: 40px; height: 40px; flex: none; border-radius: 12px 12px 12px 4px; background: #fff; position: relative; }
    .t-cta .ico::before { content: ""; position: absolute; left: 9px; top: 12px; right: 9px; height: 4px; border-radius: 2px; background: #FF5A1F; box-shadow: 0 9px 0 #FF5A1F; }  /* icon "bong bóng bình luận" — 2 gạch ngang mô phỏng dòng chữ */
    .t-cta span { font-weight: 800; font-size: 34px; letter-spacing: 0.01em; color: #1a0800; }

    .t-sign { position: absolute; left: 0; right: 0; bottom: 220px; display: flex; align-items: center; justify-content: center; gap: 12px; opacity: 0; }
    .t-sign .m { width: 40px; height: 40px; }
    .t-sign .w { font-weight: 800; font-size: 28px; color: rgba(255,255,255,0.85); }
  </style>

  <div id="root" data-composition-id="07-cta" data-width="1080" data-height="1920">
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">{{CÂU_HỎI_DÒNG_1}}</span></div>
        <div class="ln"><span id="t-h2">{{CÂU_HỎI_DÒNG_2}}</span></div>
      </div>

      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">{{LỰA_CHỌN_TÍCH_CỰC}}</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">{{LỰA_CHỌN_TIÊU_CỰC}}</div></div>
      </div>

      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>

    <div class="t-sign" id="t-sign">
      <img class="m" src="public/logo.png" alt="">
      <span class="w">Tin Tức Số</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });
    tl.fromTo('#t-kicker', { autoAlpha: 0, y: -12 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0);
    tl.fromTo('#t-h1', { yPercent: 118 }, { yPercent: 0, duration: 0.55, ease: 'power4.out' }, 0.2);
    tl.fromTo('#t-h2', { yPercent: 118 }, { yPercent: 0, duration: 0.55, ease: 'power4.out' }, 0.36);
    tl.fromTo('#t-o1', { autoAlpha: 0, y: 28, scale: 0.92 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }, 1.05);
    tl.fromTo('#t-vs', { autoAlpha: 0, scale: 0.5 }, { autoAlpha: 1, scale: 1, duration: 0.3, ease: 'back.out(2)' }, 1.3);
    tl.fromTo('#t-o2', { autoAlpha: 0, y: 28, scale: 0.92 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }, 1.4);

    /* --- Nút CTA: MỘT chuỗi 2 tween trên CÙNG phần tử #t-cta.
           Đây là hình mẫu ĐÚNG khi phải chain 2 fromTo() khác nhau lên cùng 1 selector — xem mục 8.3 --- */
    tl.set('#t-cta', { autoAlpha: 0, y: 22, scale: 1 }, 0);
    tl.fromTo('#t-cta', { autoAlpha: 0, y: 22 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out', immediateRender: false }, 2.15);
    tl.fromTo('#t-cta', { scale: 1 }, { scale: 1.04, duration: 0.45, yoyo: true, repeat: 3, ease: 'sine.inOut', immediateRender: false }, 2.75);

    tl.fromTo('#t-sign', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4 }, 2.45);
    window.__timelines['07-cta'] = tl;
  </script>
</template>
```

**Ghi chú quan trọng — biến thể đơn giản hơn cũng tồn tại và vẫn hợp lệ**: 3/4 project khác
(`_reference-astra-openai`, `iphone-18-pro-thay-doi-so-voi-17-pro`) viết ngắn gọn hơn, KHÔNG có
`tl.set(...)` mở đầu và KHÔNG có `immediateRender:false`:

```js
/* biến thể ngắn — vẫn thấy trong _reference-astra-openai và iphone-18-pro-thay-doi-so-voi-17-pro */
tl.fromTo('#t-cta', { autoAlpha: 0, y: 22 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out' }, 2.4);
tl.fromTo('#t-cta', { scale: 1 }, { scale: 1.04, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }, 3.1);
```

**Dùng biến thể `gia-xang-dau-tang-hon-1200-dong-lit` (có `tl.set` + `immediateRender:false`)
làm mặc định** — nó phòng ngừa đúng bug "`fromTo` thứ 2 ghi đè `from`-state của `fromTo` thứ
nhất khi timeline seek ngược" (xem mục 8.3), dù bug đó chưa chắc lộ ra ở mọi trường hợp render
tuyến tính. An toàn hơn không mất gì.

**Icon CSS thay emoji — công thức tái sử dụng được**:
- "Mũi tên lên" = 1 vòng tròn viền (`border-radius:50%`) + `::after` là 1 góc vuông xoay 45°
  dùng `border-top` + `border-right` (tạo hình `⌃`).
- "Cảnh báo" = 1 tam giác CSS thuần (`border-left`/`border-right` trong suốt + `border-bottom`
  màu đặc) + `::after` là ký tự `"!"` căn giữa đè lên đáy tam giác.
- "Bong bóng bình luận" (icon trong nút CTA) = 1 hình vuông bo góc bất đối xứng
  (`border-radius: 12px 12px 12px 4px` — góc dưới-trái nhọn hơn, giả dạng đuôi bong bóng chat) +
  2 gạch ngang trắng ở giữa mô phỏng dòng chữ (`::before` + `box-shadow` tạo gạch thứ 2).

---

## 6. 5 act giữa theo từng style dựng

Nguyên tắc chung quan sát được ở **mọi** act giữa của **mọi** style: mỗi frame có
- 1 `.xx-kicker` (label nhỏ UPPERCASE, `letter-spacing` rộng, màu `#FF5A1F`, fade+slide từ trên
  xuống, luôn animate **đầu tiên**, ~0.35–0.4s),
- 1 tiêu đề/caption chính,
- 1 khối nội dung trung tâm mang ẩn dụ của style (thẻ / chip / vòng tròn / trục / lưới / v.v.),
- optional 1 dòng chú thích/nguồn ở cuối.

GSAP timeline của act giữa **hầu như luôn bắt đầu bằng `const tl = gsap.timeline({ paused: true
});`** rồi liệt kê tuần tự `tl.fromTo(selector, {from}, {to}, <thời điểm tuyệt đối tính bằng
giây kể từ đầu ACT — KHÔNG phải kể từ đầu video>, ...)`, kết thúc bằng
`window.__timelines['0N-tên-act'] = tl;`.

### 6.1 Style `1-card-and-bar` — đã dựng: `chung-khoan-viet-nang-hang-ban-rong`

**Act Key facts** (`03-facts.html`) — "mỗi fact là 1 thẻ bo góc, số thứ tự nhỏ góc trái":

```css
.fc-list { position: absolute; left: 64px; right: 64px; top: 388px; display: flex; flex-direction: column; gap: 40px; }
.fc-card { position: relative; height: 344px; border-radius: 24px; background: #121724; border: 1px solid rgba(255,255,255,0.09); padding: 34px 40px; display: flex; flex-direction: column; justify-content: center; opacity: 0; }
.fc-num { position: absolute; left: 34px; top: 28px; font-weight: 800; font-size: 24px; color: rgba(255,255,255,0.45); letter-spacing: 0.04em; }
.fc-value { font-weight: 900; font-size: 88px; line-height: 1; letter-spacing: -0.01em; color: #FF5A1F; margin-top: 6px; }
.fc-value.warn { color: #FF4438; }
.fc-label { margin-top: 20px; font-weight: 600; font-size: 32px; line-height: 1.3; color: rgba(255,255,255,0.85); }
```

```html
<div class="fc-card" id="fc-c1">
  <div class="fc-num">01</div>
  <div class="fc-value">1.827 điểm</div>
  <div class="fc-label">Mức VN-Index chốt chiều 8/9/2026</div>
</div>
```

```js
tl.fromTo('#fc-c1', { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 0.85);
tl.fromTo('#fc-c2', { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 2.4);
tl.fromTo('#fc-c3', { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 4.0);
```
**Kỹ thuật vertical fill**: 3 thẻ cao 344px, gap 40px → tổng khối `(344×3)+(40×2) = 1112px` bắt
đầu từ `top:388px` → kết thúc ở `top:1500px`. Đây chính là cách "3 card cao + gap rộng" tự động
lấp đầy vùng an toàn mà không cần bất kỳ tính toán căn giữa nào — **cứ đặt `height` đủ lớn cho
từng card rồi cộng dồn `top` khởi điểm + tổng chiều cao + gap, kiểm tra có rơi vào 1400–1680px
không**.

**Act Data moment** (`04-data.html`) — "số chính TO giữa + 2-3 cột dọc so sánh, cột cao nhất tô
cam":

```css
.dm-cols-inner { display: flex; justify-content: space-between; align-items: flex-end; height: 700px; gap: 24px; }
.dm-bar { width: 108px; border-radius: 14px 14px 0 0; background: rgba(255,255,255,0.14); transform-origin: bottom center; transform: scaleY(0); }
.dm-bar.hi { background: #FF5A1F; }
```

```js
const c = { v: 0 };
tl.fromTo(c, { v: 0 }, { v: 90000, duration: 1.3, ease: 'power1.out',
  onUpdate() { numEl.textContent = Math.round(c.v).toLocaleString('vi-VN'); } }, 0.5);
tl.fromTo('#dm-b1', { scaleY: 0 }, { scaleY: 1, duration: 0.5, ease: 'power2.out' }, 2.6);
tl.fromTo('#dm-v1', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, 3.0);
tl.fromTo('#dm-b2', { scaleY: 0 }, { scaleY: 1, duration: 0.5, ease: 'power2.out' }, 3.1);
...
```
**Pattern count-up chuẩn của toàn kênh**: 1 object JS thường `{v: 0}` (KHÔNG phải element DOM),
tween `v` bằng GSAP, `onUpdate` ghi `textContent` bằng `Math.round(...).toLocaleString('vi-VN')`
(dấu chấm phân cách nghìn kiểu Việt). **KHÔNG BAO GIỜ** dùng `innerText`/`innerHTML` trực tiếp
trên số nếu số có HTML con bên trong (unit, sup...) trừ khi build lại cả chuỗi HTML trong
`onUpdate` (xem ví dụ ring-progress mục 6.4 dùng `innerHTML`).
**Cột bar**: `scaleY(0)→scaleY(1)`, `transform-origin: bottom center` — bar "mọc" từ dưới lên,
KHÔNG animate `height`.

### 6.2 Style `2-chip-and-leaderboard` — 2 thế hệ: `iphone-18-ra-mat-viet-nam` (đầu) và `cpi-my-thang-8-fed-tang-lai-suat` (đã cải tiến, dùng làm chuẩn)

**Act Data moment** (`cpi-my-thang-8-fed-tang-lai-suat/04-data.html`) — "leaderboard ngang 2
hàng trước/sau, hàng nổi bật tô cam":

```css
.d-focal { position: absolute; left: 64px; right: 64px; top: 380px; }
.d-num { font-weight: 900; font-size: 250px; line-height: 0.92; letter-spacing: -0.02em; color: #FF5A1F; }
/* LƯU Ý: .d-num KHÔNG có width cố định — số 2 chữ số ("70") hay 3 chữ số đều auto-fit, xem mục 8.4 */

.d-rows { position: absolute; left: 64px; right: 64px; top: 940px; }
.d-row .track { position: relative; height: 26px; border-radius: 13px; background: rgba(255,255,255,0.08); overflow: hidden; }
.d-row .fill { position: absolute; left: 0; top: 0; bottom: 0; width: 0%; border-radius: 13px; background: rgba(255,255,255,0.35); }
.d-row.hi { padding: 34px 36px; border-radius: 20px; background: rgba(255,90,31,0.12); border: 1.5px solid rgba(255,90,31,0.7); }
.d-row.hi .fill { background: #FF5A1F; }

.d-foot { position: absolute; left: 64px; right: 64px; top: 1420px; font-weight: 500; font-size: 26px; color: rgba(255,255,255,0.45); opacity: 0; }
```

```html
<div class="d-focal">
  <div class="d-num"><span id="d-num">70</span>%</div>
  <div class="d-cap" id="d-cap">Xác suất Fed tăng thêm <b>0,25 điểm %</b> lãi suất tuần tới</div>
</div>
<div class="d-rows">
  <div class="d-row" id="d-r1">
    <div class="line"><span class="lab">Trước báo cáo</span><span class="val">~70%</span></div>
    <div class="track"><div class="fill" id="d-fill1"></div></div>
  </div>
  <div class="d-row hi" id="d-r2">
    <div class="line"><span class="lab">Sau báo cáo</span><span class="val">~<span id="d-num2">70</span>%</span></div>
    <div class="track"><div class="fill" id="d-fill2"></div></div>
  </div>
</div>
```

```js
tl.fromTo('#d-r1', { autoAlpha: 0, x: 26 }, { autoAlpha: 1, x: 0, duration: 0.4, ease: 'power2.out' }, 0.45);
tl.fromTo('#d-fill1', { width: '0%' }, { width: '70%', duration: 0.55, ease: 'power2.inOut' }, 0.55);
tl.fromTo('#d-r2', { autoAlpha: 0, x: 26, scale: 0.97 }, { autoAlpha: 1, x: 0, scale: 1, duration: 0.4, ease: 'back.out(1.4)' }, 0.78);
tl.fromTo('#d-fill2', { width: '0%' }, { width: '90%', duration: 0.7, ease: 'power2.inOut' }, 0.88);
tl.fromTo(c, { v: 70 }, { v: 90, duration: 0.8, ease: 'power1.out',
  onUpdate() { const r = Math.round(c.v); numEl.textContent = r; num2El.textContent = r; } }, 0.88);
```
**Kỹ thuật thanh leaderboard**: `width: 0% → width: <N>%` (KHÔNG dùng `scaleX` ở đây, khác với
bar dọc ở style card-and-bar dùng `scaleY` — vì thanh ngang cần padding-left cố định bên trong,
`scaleX` sẽ co cả điểm neo trái). 1 counter object JS dùng chung để cập nhật **2 số khác nhau
cùng lúc** (`numEl` và `num2El`) trong 1 `onUpdate`.

**So sánh với thế hệ đầu `iphone-18-ra-mat-viet-nam`**: cấu trúc tương tự (chip viền cam +
watermark số khổng lồ mờ phía sau ở act Key facts — xem `CONSTRUCTION-STYLES.md` mục Style 1),
nhưng act Data moment thế hệ đầu **chỉ có 1 leaderboard hiện MUỘN** (theo `COMPLIANCE.md` của
`cpi-my-thang-8-fed-tang-lai-suat`, mục 7 dưới đây có chi tiết bug này) — thế hệ 2 sửa bằng cách
đẩy mốc `tl.fromTo(...)` của leaderboard sớm hơn và thêm hẳn 2 hàng so sánh trước/sau thay vì 1
số tĩnh.

### 6.3 Style `4-split-comparison` — 2 thế hệ: `v-league-vong-1-ban-thang-tang` (đầu) và `iphone-18-pro-thay-doi-so-voi-17-pro` (cải tiến, dùng làm chuẩn)

**Act Data moment** (`iphone-18-pro-thay-doi-so-voi-17-pro/04-data.html`) — "2 số cạnh nhau qua
mũi tên, số cũ nhỏ/mờ bên trái, số mới to/cam bên phải":

```css
.dm-vs { position: absolute; left: 0; right: 0; top: 420px; display: flex; align-items: center; justify-content: center; gap: 26px; }
.dm-old { font-weight: 700; font-size: 34px; color: rgba(255,255,255,0.4); opacity: 0; }
.dm-arrow { width: 56px; height: 4px; background: rgba(255,90,31,0.5); position: relative; opacity: 0; }
.dm-arrow::after { content: ""; position: absolute; right: -2px; top: -8px; border-left: 14px solid rgba(255,90,31,0.5); border-top: 10px solid transparent; border-bottom: 10px solid transparent; }
.dm-new-tag { font-weight: 800; font-size: 34px; color: #FF5A1F; opacity: 0; }

.dm-focal { position: absolute; left: 64px; right: 64px; top: 560px; text-align: center; }
.dm-num { font-weight: 900; font-size: 168px; line-height: 1; color: #FF5A1F; letter-spacing: -0.02em; }
.dm-num .small { font-size: 74px; vertical-align: 14px; }   /* dùng cho dấu phẩy thập phân "38,99" */

.dm-rule { position: absolute; left: 64px; right: 64px; top: 1400px; height: 1px; background: rgba(255,255,255,0.12); transform: scaleX(0); }
.dm-card { position: absolute; left: 64px; right: 64px; top: 1466px; display: flex; align-items: center; justify-content: space-between; padding: 40px 36px; border-radius: 16px; background: #121724; border: 1px solid rgba(255,255,255,0.08); opacity: 0; }
```

```js
tl.fromTo('#dm-old', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, 0.35);
tl.fromTo('#dm-arrow', { autoAlpha: 0, scaleX: 0 }, { autoAlpha: 1, scaleX: 1, duration: 0.3, ease: 'power2.out', transformOrigin: 'left' }, 0.55);
tl.fromTo('#dm-newtag', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, 0.8);
tl.fromTo('#dm-num', { autoAlpha: 0, scale: 0.8 }, { autoAlpha: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }, 1.05);
tl.fromTo('#dm-rule', { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: 'power2.out' }, 1.9);
tl.fromTo('#dm-card', { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 2.1);
```
**Kỹ thuật vertical fill của style này**: KHÔNG dùng flex-center, dùng **`top` tuyệt đối cộng
dồn thủ công** — `.dm-vs top:420` → `.dm-focal top:560` → `.dm-rule top:1400` →
`.dm-card top:1466` (card cao ước lượng ~120px với padding 40px → kết thúc quanh 1586–1600px,
đúng dải 1400–1680px yêu cầu).

**Act Impact** (`06-impact.html`) — "chia đôi NGANG (trên/dưới), đổi nhịp so với act 2 (chia dọc
trái/phải)":

```css
.im-top { position: absolute; left: 64px; right: 64px; top: 340px; height: 380px; }
.im-hr { position: absolute; left: 64px; right: 64px; top: 740px; height: 2px; background: rgba(255,255,255,0.12); transform: scaleX(0); }
.im-bot { position: absolute; left: 64px; right: 64px; top: 800px; bottom: 240px; display: flex; flex-direction: column; justify-content: space-between; }
```
```html
<div class="im-top">
  <div class="im-kicker" id="im-k1">Sau ra mắt</div>
  <div class="im-title"><div class="ln"><span id="im-h1">3 mẫu iPhone cũ</span></div><div class="ln"><span id="im-h2">bị khai tử</span></div></div>
  <div class="im-chips">
    <div class="im-chip" id="im-c1"><span class="x"></span><span class="t">iPhone 17 Pro</span></div>
    ...
  </div>
</div>
<div class="im-hr" id="im-hr"></div>
<div class="im-bot">
  <div class="im-kicker" id="im-k2">Tại Việt Nam</div>
  <div class="im-stat" id="im-stat"><span class="num">60.000+</span><span class="unit">lượt quan tâm</span></div>
  <div class="im-desc" id="im-desc">...</div>
</div>
```
Đúng như `CONSTRUCTION-STYLES.md` mô tả — Impact chia NGANG bằng 1 đường kẻ `im-hr` ở giữa
(`scaleX 0→1`), nửa trên và nửa dưới dùng `flex-direction:column; justify-content:space-between`
riêng để tự phân bố đều bên trong khối của nó — đây là 1 lớp flex-fill LỒNG bên trong tổng thể
top-offset tuyệt đối, không mâu thuẫn với nhau.

### 6.4 Style `6-ring-progress` — đã dựng: `iphone-duo-man-hinh-gap`

**Act Data moment** (`04-data.html`) — "số chính giữa 1 vòng radial khổng lồ, vòng vẽ đầy đồng
bộ với count-up":

```css
.dm-ringwrap { position: absolute; left: 50%; top: 540px; width: 700px; height: 700px; transform: translateX(-50%); }
.dm-center { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }
```
```html
<div class="dm-ringwrap">
  <svg class="dm-ring" width="700" height="700" viewBox="0 0 700 700">
    <circle cx="350" cy="350" r="305" fill="none" stroke="rgba(255,255,255,0.09)" stroke-width="29"/>
    <circle id="dm-ring-fg" cx="350" cy="350" r="305" fill="none" stroke="#FF5A1F" stroke-width="29"
            stroke-linecap="round" transform="rotate(-90 350 350)"
            stroke-dasharray="1916.4" stroke-dashoffset="1916.4"/>
  </svg>
  <div class="dm-center">
    <div class="dm-num" id="dm-num"><span id="dm-nums">0</span> triệu</div>
  </div>
</div>
```
```js
tl.fromTo('.dm-ringwrap', { autoAlpha: 0, scale: 0.86 }, { autoAlpha: 1, scale: 1, duration: 0.5, ease: 'power2.out' }, 0.55);
tl.fromTo('#dm-ring-fg', { strokeDashoffset: 1916.4 }, { strokeDashoffset: 0, duration: 1.1, ease: 'power2.out' }, 0.6);
tl.to(counter, {
  val: 104, duration: 1.1, ease: 'power2.out',
  onUpdate: function () { document.getElementById('dm-num').innerHTML = Math.round(counter.val) + ' <span>triệu</span>'; }
}, 0.6);
```
**Kỹ thuật ring reveal — đây CHÍNH LÀ ví dụ thật cho quy tắc "SVG reveal phải có state ẩn mặc
định" của mục 8.2**: `stroke-dasharray="1916.4" stroke-dashoffset="1916.4"` được viết **CỨNG
TRONG HTML** (không phải chỉ dựa vào JS `getTotalLength()` lúc runtime) — `1916.4 ≈ 2π×305`
(chu vi vòng tròn bán kính 305px), tự tính tay và ghi cứng. Vòng **ẩn hoàn toàn** ngay từ đầu vì
`dashoffset == dasharray` (không vẽ nét nào), GSAP chỉ animate `strokeDashoffset` về `0`.

**Vertical fill của ring-progress**: ring 700×700px đặt `top:540` → kết thúc ở `top:1240` —
CHƯA đủ chạm 1400–1680px, nên style này **bắt buộc thêm 1 dòng caption riêng ở `top:1610px`**
(xem `.dm-caption { top: 1610px }` trong code gốc) để tổng khối content thật sự lấp tới gần
1650px — đây chính là kỹ thuật "phóng to / thêm dòng phụ" mà mục 7 sẽ nói kỹ.

**Vòng radial cỡ đã bị sửa 1 lần do vi phạm cân bằng dọc**: xem mục 7.2 (bug thật + fix thật,
620px → 700px).

### 6.5 Style `7-timeline-chronology` — đã dựng: `khong-khi-lanh-ap-thap-nhiet-doi-bien-dong`

**Act Context** (`05-context.html`) — trục dọc với node "nở" theo tuần tự, giá trị tăng dần:

```css
.ct-track { position: absolute; left: 90px; right: 90px; top: 650px; height: 950px; }
.ct-axis { position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: rgba(255,255,255,0.14); }
.ct-axis .fill { position: absolute; left: 0; top: 0; width: 100%; height: 100%; background: #FF5A1F; transform: scaleY(0); transform-origin: top; }
.ct-row { position: absolute; left: 0; right: 0; display: flex; align-items: center; opacity: 0; }
.ct-dot { width: var(--sz, 22px); height: var(--sz, 22px); border-radius: 50%; background: #FF5A1F; margin-left: calc(-1 * var(--sz, 22px) / 2 + 2px); flex: none; }
#ct-r1 { top: 0px; } #ct-r2 { top: 250px; } #ct-r3 { top: 505px; } #ct-r4 { top: 760px; }
```
```js
tl.set('#ct-axis-fill', { scaleY: 0 }, 0);
tl.to('#ct-axis-fill', { scaleY: 0.22, duration: 0.42, ease: 'power2.out' }, 1.6);
tl.fromTo('#ct-dot1', { scale: 0 }, { scale: 1, duration: 0.3, ease: 'back.out(2)' }, 1.7);
tl.fromTo('#ct-r1', { autoAlpha: 0, x: 16 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.76);
tl.to('#ct-axis-fill', { scaleY: 0.48, duration: 0.42, ease: 'power2.out' }, 3.6);
tl.fromTo('#ct-dot2', { scale: 0 }, { scale: 1, duration: 0.3, ease: 'back.out(2)' }, 3.7);
/* ... lặp lại tới scaleY: 1.0 ở mốc cuối cùng ... */
```
**Kỹ thuật trục "vẽ dần"**: 1 thanh nền mờ cố định (`.ct-axis`) + 1 thanh `.fill` chồng lên,
`transform-origin: top; scaleY(0)` ban đầu, mỗi khi 1 node xuất hiện thì tween `scaleY` tới 1 tỉ
lệ lớn hơn (0.22 → 0.48 → 0.74 → 1.0) — mô phỏng trục "mọc dài dần" đúng lúc từng mốc xuất hiện,
KHÔNG phải 1 tween `scaleY(0)→scaleY(1)` chạy hết ngay từ đầu. `--sz` (custom CSS property) đặt
riêng từng dot để dot sau to hơn dot trước (`18px → 34px → 28px → 20px` — kích thước dot tỉ lệ
thuận độ lớn lượng mưa, không phải tăng tuyến tính theo thứ tự).

> **QUAN TRỌNG — mâu thuẫn với văn bản, xem mục 11**: `CONSTRUCTION-STYLES.md` mô tả act Context
> của style này là "**trục thời gian NGANG** đầy đủ 4-5 mốc". Code thật dùng **trục DỌC** (axis
> `width:4px`, các row xếp theo `top` tăng dần). Đây là quyết định thiết kế hợp lý cho canvas dọc
> 1080×1920 (trục ngang thật sẽ rất chật trên khung hẹp 1080px), nhưng là sai lệch thật so với
> văn bản — dùng bản DỌC này làm chuẩn khi dựng lại style `7-timeline-chronology`, không cố ép
> theo mô tả "ngang" trong `CONSTRUCTION-STYLES.md`.

### 6.6 Style `8-icon-grid` — đã dựng: `gia-xang-dau-tang-hon-1200-dong-lit`

**Act Key facts** (`03-facts.html`) — lưới 2×2, icon CSS thật (không phải emoji):

```css
.kf-grid { position: absolute; left: 60px; right: 60px; top: 500px; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 26px; height: 1010px; }
.kf-cell { border-radius: 22px; border: 1.5px solid rgba(255,255,255,0.14); background: rgba(255,255,255,0.04); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; opacity: 0; transform: scale(0.88); }
.kf-cell.hi { border-color: rgba(255,90,31,0.65); background: rgba(255,90,31,0.1); }

.drop { border-radius: 50% 50% 50% 0; transform: rotate(45deg); background: #FF5A1F; }   /* icon "giọt xăng" thuần CSS */
.barrel { border-radius: 12px; border: 5px solid #FF5A1F; background: transparent; }
.barrel::before { content: ""; position: absolute; left: -5px; right: -5px; top: 18px; height: 5px; background: #FF5A1F; }
.barrel::after  { content: ""; position: absolute; left: -5px; right: -5px; top: 34px; height: 5px; background: #FF5A1F; }  /* icon "thùng phuy" — khung + 2 gạch ngang */
```
```js
tl.fromTo('#kf-c1', { autoAlpha: 0, scale: 0.88 }, { autoAlpha: 1, scale: 1, duration: 0.42, ease: 'back.out(1.6)' }, 0.9);
tl.fromTo('#kf-c2', { autoAlpha: 0, scale: 0.88 }, { autoAlpha: 1, scale: 1, duration: 0.42, ease: 'back.out(1.6)' }, 4.5);
tl.fromTo('#kf-c3', { autoAlpha: 0, scale: 0.88 }, { autoAlpha: 1, scale: 1, duration: 0.42, ease: 'back.out(1.6)' }, 8.1);
tl.fromTo('#kf-c4', { autoAlpha: 0, scale: 0.88 }, { autoAlpha: 1, scale: 1, duration: 0.42, ease: 'back.out(1.6)' }, 11.7);
```
**Ghi chú khoảng cách reveal rất rộng (3.6s giữa mỗi ô)**: đây là frame có `data-duration` dài
(14.77s — do voice dòng 3 dài, xem bảng mục 3.2), 4 ô hiện tuần tự trải đều suốt độ dài voice
đọc lần lượt 4 con số, KHÔNG dồn hết trong 1–2 giây đầu. **Bài học**: khoảng cách giữa các mốc
`tl.fromTo` phải khớp nhịp đọc thật của giọng (nếu giọng đọc "xăng E5... xăng E10... dầu diesel…
dầu mazut…" trải trong 14s thì animation cũng phải trải trong 14s, không nén lại).

**Icon CSS shape tái sử dụng**: "giọt nước/giọt xăng" = 1 hình vuông bo 3 góc
(`border-radius: 50% 50% 50% 0`) xoay 45° (biến hình vuông-bo-3-góc thành hình giọt nước đứng);
"thùng phuy" = khung chữ nhật bo góc + 2 gạch ngang `::before`/`::after` mô phỏng vòng đai thùng.

### 6.7 — [EXTRAPOLATED, KHÔNG PHẢI CODE THẬT] Style `3-ticker-tape` — chưa từng dựng

> ⚠️ **Cảnh báo rõ ràng**: không có project nào trong 8 video đã dựng dùng style này (xem
> `videos/style-rotation-state.json` — index 2 chưa từng xuất hiện trong `log`). Toàn bộ code
> dưới đây là **suy diễn** từ (a) mô tả bằng lời trong `CONSTRUCTION-STYLES.md` mục "Style 2 —
> Ticker Tape", và (b) các quy ước kỹ thuật quan sát được xuyên suốt 6 style đã dựng thật ở mục
> 6.1–6.6 (cấu trúc `.xx-kicker`/`.xx-head`, cách count-up, cách reveal SVG, bảng màu). **Trước
> khi dùng, hãy tự dựng và verify bằng Studio thumbnail + render thật** — không copy thẳng và tin
> tưởng tuyệt đối như các mục 6.1–6.6.

**Act Data moment** (suy diễn) — "con số chính giữa 2 vạch kẻ ngang mảnh, phía trên là 1 'mã'
ngắn viết hoa chạy trước khi số count-up":

```css
.dm-code { position: absolute; left: 0; right: 0; top: 480px; text-align: center; font-weight: 700; font-size: 30px; letter-spacing: 0.3em; text-transform: uppercase; color: rgba(255,255,255,0.5); opacity: 0; }
.dm-rule-top, .dm-rule-bot { position: absolute; left: 120px; right: 120px; height: 2px; background: rgba(255,90,31,0.5); transform: scaleX(0); }
.dm-rule-top { top: 600px; } .dm-rule-bot { top: 1080px; }
.dm-num { position: absolute; left: 0; right: 0; top: 660px; text-align: center; font-weight: 900; font-size: 220px; line-height: 1; color: #FF5A1F; }
```
```js
tl.fromTo('.dm-code', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.35 }, 0);
tl.fromTo('.dm-rule-top', { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: 'power2.out' }, 0.3);
tl.fromTo('.dm-rule-bot', { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: 'power2.out' }, 0.4);
tl.fromTo(counter, { v: 0 }, { v: {{TARGET}}, duration: 1.1, ease: 'power1.out', onUpdate() { numEl.textContent = Math.round(counter.v); } }, 0.6);
```

**Act Key facts** (suy diễn) — "mỗi fact hiện dạng dòng terminal, prefix `>`/`+`, reveal
typewriter":

```css
.tk-line { font-family: "Montserrat", monospace; font-weight: 600; font-size: 34px; color: rgba(255,255,255,0.85); opacity: 0; }
.tk-line .prefix { color: #FF5A1F; margin-right: 14px; }
```
```js
/* typewriter thật cần SplitText hoặc cắt chuỗi ký tự thủ công trong onUpdate — KHÔNG có ví dụ
   thật trong 6 style đã dựng cho hiệu ứng này, đây là điểm rủi ro cao nhất khi tự triển khai.
   Cách an toàn hơn (tương đương về cảm giác, chắc chắn chạy đúng): reveal cả dòng bằng
   autoAlpha + x nhỏ, KHÔNG cắt ký tự: */
tl.fromTo('#tk-r1', { autoAlpha: 0, x: -14 }, { autoAlpha: 1, x: 0, duration: 0.3, ease: 'power2.out' }, 0.6);
```
**Vertical fill**: 3-5 dòng terminal cao ~26px + line-height rộng (gap ≥60px giữa các dòng) để
tự nhiên trải xuống — dùng kỹ thuật A (top cộng dồn, mục 7.1) vì đây là danh sách dòng đơn giản
tương tự card-and-bar §6.1, chỉ thay `.fc-card` bằng `.tk-line`.

### 6.8 — [EXTRAPOLATED, KHÔNG PHẢI CODE THẬT] Style `5-map-and-geo` — chưa từng dựng

> ⚠️ Không có project thật dùng style này. Suy diễn từ `CONSTRUCTION-STYLES.md` mục "Style 4 —
> Map & Geo" + quy ước SVG-reveal thật (mục 8.3, dùng nguyên lý giống ring-progress §6.4).

**Act Data moment** (suy diễn) — "con số chính trong 1 map-pin phóng to, pin drop-in trước khi
số count-up":

```css
.dm-pin { position: absolute; left: 50%; top: 500px; width: 240px; height: 300px; transform: translateX(-50%) scale(0); transform-origin: bottom center; }
.dm-pin svg { width: 100%; height: 100%; }
/* pin = 1 hình giọt nước lớn (giống .drop ở mục 6.6 nhưng phóng to) chứa số bên trong */
.dm-pin-body { border-radius: 50% 50% 50% 0; transform: rotate(-45deg); background: #FF5A1F; width: 240px; height: 240px; position: absolute; top: 0; left: 0; }
.dm-pin-inner { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; }
.dm-num { transform: rotate(45deg); font-weight: 900; font-size: 76px; color: #0B0E14; }  /* xoay ngược lại để số đứng thẳng bên trong giọt đã xoay 45deg */
```
```js
tl.fromTo('.dm-pin', { scale: 0 }, { scale: 1, duration: 0.5, ease: 'bounce.out' }, 0.4);  /* "bounce nhẹ" theo mô tả style */
tl.fromTo(counter, { v: 0 }, { v: {{TARGET}}, duration: 1.0, onUpdate() {...} }, 0.9);
```
**Act Context** (suy diễn) — "bản đồ 3-5 vùng highlight tuần tự, đường nối ra nhãn số liệu": dùng
1 SVG `<path>` outline bản đồ (Việt Nam hoặc thế giới tuỳ tin) đặt mờ phía sau (`opacity:0.15`,
`fill:none; stroke:rgba(255,255,255,0.2)`), các vùng highlight là `<circle>`/`<path>` riêng tô
`#FF5A1F` với `opacity:0→1` tuần tự giống pattern `.ct-dot` ở mục 6.5, đường nối dùng
`stroke-dasharray`/`stroke-dashoffset` reveal giống ring-progress (**bắt buộc viết cứng state ẩn
mặc định**, xem mục 8.3 — đây là style RỦI RO CAO nhất về vi phạm quy tắc SVG reveal vì có nhiều
path nhất trong 10 style).

**Nguồn SVG bản đồ**: KHÔNG tự vẽ path bản đồ Việt Nam/thế giới từ đầu bằng tay — dùng
`hyperframes-registry` skill để tìm block bản đồ có sẵn trước (xem hướng dẫn trong skill đó),
hoặc dùng 1 outline SVG bản đồ đơn giản hoá cao (không cần chi tiết địa lý chính xác, chỉ cần
gợi được hình dạng vùng liên quan).

### 6.9 — [EXTRAPOLATED, KHÔNG PHẢI CODE THẬT] Style `9-editorial-clipping` — chưa từng dựng

> ⚠️ Không có project thật dùng style này. Suy diễn từ `CONSTRUCTION-STYLES.md` mục "Style 8 —
> Editorial Clipping" + quy ước bố cục card thật (mục 6.1, `.fc-card`).

**Act Data moment** (suy diễn) — "số chính có dấu ngoặc kép khổng lồ mờ phía sau, gạch chân
tay-vẽ dưới số":

```css
.dm-quote-mark { position: absolute; left: 50%; top: 380px; transform: translateX(-50%); font-family: Georgia, serif; font-weight: 900; font-size: 420px; line-height: 1; color: rgba(255,90,31,0.12); opacity: 0; }
.dm-num { position: absolute; left: 0; right: 0; top: 620px; text-align: center; font-weight: 900; font-size: 200px; color: #FF5A1F; }
.dm-underline { position: absolute; left: 50%; top: 920px; width: 320px; transform: translateX(-50%) scaleX(0); }
/* gạch chân "tay vẽ" = 1 SVG <path> hình sin nhẹ nhàng thay vì đường thẳng, KHÔNG dùng border-bottom thẳng */
```
```js
tl.fromTo('.dm-quote-mark', { autoAlpha: 0, scale: 0.8 }, { autoAlpha: 1, scale: 1, duration: 0.5 }, 0);
tl.fromTo(counter, { v: 0 }, { v: {{TARGET}}, duration: 1.0, onUpdate(){...} }, 0.5);
tl.fromTo('.dm-underline', { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: 'power2.out' }, 1.6);
```
**Act Key facts** (suy diễn) — "3 fact như mẩu giấy xếp chồng lệch, mỗi mẩu xoay góc khác":
```css
.kf-card { position: absolute; width: 780px; border-radius: 4px; background: #121724; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 20px 40px rgba(0,0,0,0.4); padding: 40px; opacity: 0; }
#kf-c1 { top: 480px; left: 60px; transform: rotate(-1.5deg) scale(0.95); }
#kf-c2 { top: 780px; left: 100px; transform: rotate(1deg) scale(0.95); }
#kf-c3 { top: 1080px; left: 70px; transform: rotate(-0.8deg) scale(0.95); }
```
```js
tl.fromTo('#kf-c1', { autoAlpha: 0, y: 40, rotate: 0 }, { autoAlpha: 1, y: 0, rotate: -1.5, duration: 0.5, ease: 'power3.out' }, 0.8);
/* LƯU Ý: rotate ở đây trộn với transform CSS tĩnh (mục 8.7 cảnh báo) — nếu tween bằng GSAP,
   phải để GSAP quản lý toàn bộ transform (rotate+scale) qua object tween, KHÔNG để CSS
   .kf-card có sẵn "transform: rotate(...)" tĩnh rồi GSAP tween "rotate" riêng lẻ đè lên —
   xoá transform tĩnh khỏi CSS, để 100% trong tay GSAP (from {rotate:0, scale:0.9} to
   {rotate:-1.5, scale:0.95}). */
```

### 6.10 — [EXTRAPOLATED, KHÔNG PHẢI CODE THẬT] Style `10-stock-terminal` — chưa từng dựng

> ⚠️ Không có project thật dùng style này. Suy diễn từ `CONSTRUCTION-STYLES.md` mục "Style 9 —
> Stock Terminal" + kỹ thuật bar/count-up thật ở mục 6.1 (card-and-bar) và trục vẽ dần ở mục 6.5
> (timeline-chronology).

**Act Data moment** (suy diễn) — "đường line-chart nhỏ chạy ngang phía sau, vẽ dần trái→phải,
chạm đỉnh đúng lúc số count-up chốt":

```html
<svg class="dm-linechart" viewBox="0 0 800 200" style="position:absolute; left:140px; right:140px; top:520px; opacity:0.5;">
  <path id="dm-line-path" d="M0,160 L100,150 L200,120 L300,130 L400,90 L500,70 L600,40 L700,20 L800,10"
        fill="none" stroke="#FF5A1F" stroke-width="4" stroke-linecap="round"
        stroke-dasharray="1200" stroke-dashoffset="1200" />
  <!-- stroke-dasharray phải >= độ dài path thật (đo bằng path.getTotalLength() lúc dựng, ghi
       cứng số đó vào HTML — KHÔNG chỉ dựa runtime, xem mục 8.3) -->
</svg>
<div class="dm-num" style="position:absolute; left:0; right:0; top:760px; text-align:center;">...</div>
```
```js
tl.fromTo('#dm-line-path', { strokeDashoffset: 1200 }, { strokeDashoffset: 0, duration: 1.3, ease: 'power2.inOut' }, 0.3);
tl.fromTo(counter, { v: 0 }, { v: {{TARGET}}, duration: 1.3, ease: 'power1.out', onUpdate(){...} }, 0.3);  /* CÙNG lúc, CÙNG duration với đường vẽ, để "chạm đỉnh đúng lúc số chốt" */
```
**Act Context** (suy diễn) — "biểu đồ cột đầy đủ 4-6 cột (cam/đỏ), mỗi cột có nhãn số phía
trên": tái dùng nguyên `.dm-bar { transform-origin: bottom center; transform: scaleY(0); }` của
style card-and-bar (§6.1) — chỉ khác: cột nào giá trị âm/giảm thì `background: #FF4438` thay vì
`#FF5A1F` (đúng brand rule "không dùng xanh lá cho tăng" — cả tăng lẫn giảm đều nằm trong palette
cam/đỏ, không thêm màu mới).

---

## 7. Cân bằng dọc — công thức + bằng chứng đo pixel thật

### 7.1 Hai kỹ thuật đã quan sát để lấp khung 1080×1920

| Kỹ thuật | Khi dùng | Ví dụ thật |
|---|---|---|
| **A — Top tuyệt đối cộng dồn thủ công** | Đa số act giữa (facts/data/context/impact) — layout có nhiều khối rời rạc xếp dọc | `chung-khoan`: `.fc-list{top:388px}` + 3 card 344px + gap 40px → hết ở ~1500px. `iphone-18-pro`: `.dm-vs{top:420}` → `.dm-focal{top:560}` → `.dm-rule{top:1400}` → `.dm-card{top:1466}` |
| **B — Flex-center + phóng to element khi nội dung ít** | Hook, CTA, Data-moment 1-số-tĩnh (nội dung tự nhiên ngắn) | Ring-progress: ring **700×700px** (không phải nhỏ hơn) đặt `top:540` + thêm `.dm-caption{top:1610px}` để kéo điểm kết thúc xuống |

**Quy trình quyết định (recipe thực dụng)**:
1. Dựng frame xong bằng logic layout tự nhiên trước (không cố nhồi số `top` để "cho đủ").
2. Tính (hoặc đo bằng Studio thumbnail / trích frame + xem bằng mắt) `top` của điểm THẤP NHẤT
   của phần tử cuối cùng.
3. Nếu điểm đó **< 1400px** → 2 lựa chọn, chọn 1:
   - (a) **Tăng kích thước** phần tử trọng tâm (ring/số/card) — ưu tiên cách này nếu phần tử đó
     là điểm nhấn thị giác chính của act (ví dụ ring-progress 620px→700px, xem 7.2).
   - (b) **Thêm 1 dòng phụ thật sự có nội dung** (caption/footnote/nguồn) ở `top` cao hơn — KHÔNG
     thêm khoảng trắng/div rỗng chỉ để đẩy chiều cao, phải là nội dung thật.
4. Nếu điểm đó **> 1680px** → cắt bớt margin/gap, hoặc rút gọn nội dung phần cuối, tránh tràn
   sát mép an toàn dưới.
5. **Verify bằng đo pixel thật trên file `.mp4` đã render**, KHÔNG chỉ tin "nhìn ảnh thumbnail
   nén thấy có vẻ ổn" — xem bằng chứng 7.3 dưới đây cho thấy nhìn mắt qua ảnh nén từng gây báo
   động giả.

### 7.2 Bug thật + fix thật #1 — ring-progress bị co cụm nửa trên (`iphone-duo-man-hinh-gap`)

Trích nguyên văn `COMPLIANCE.md`:

> Vòng 1 render: phát hiện act 2/3/4/5/6 (What/Facts/Data/Context/Impact) để trống đen quá
> nhiều ở nửa dưới khung (lỗi tái phát đã ghi trong BRAND-SYSTEM.md) — đã sửa: **đôn nội dung/
> vòng radial xuống, phóng to ring ở act Data (620→700px) và Context (260→320px)**, đẩy
> caption/foot xuống gần mốc top:1650-1700, tỉ lệ margin đáy khớp với Hook/CTA tham chiếu; render
> lại vòng 2 xác nhận đã khắc phục qua so sánh frame.

→ Số `700px` đọc thấy trong code hiện tại ở mục 6.4 **chính là kết quả SAU fix này** — nếu bạn
dựng ring-progress mới, bắt đầu luôn từ 700px cho ring chính (act Data), không lặp lại sai lầm
620px.

### 7.3 Bug thật + fix thật #2 — leaderboard hiện quá muộn + đo pixel định lượng thay vì nhìn mắt (`cpi-my-thang-8-fed-tang-lai-suat`)

Trích nguyên văn `COMPLIANCE.md` (rút gọn, giữ số liệu):

> [QA vòng render đầu] ... khi tôi tự trích frame độc lập từ file .mp4 đã render (t=30s, act Data
> moment) phát hiện phần tử cuối cùng của frame chỉ dừng ở **y≈710/1920 (37%)** — vi phạm rõ
> ràng quy tắc 'Cân bằng dọc'... đồng thời act này thiếu hẳn bảng xếp hạng ngang... chỉ có 1 số
> to + 1 đoạn văn. Gửi lại yêu cầu sửa: nguyên nhân là timing GSAP nội bộ của act để lộ trạng
> thái leaderboard quá muộn (chỉ hiện đủ sau ~4.1s trong khi mẫu lấy ở giữa act). Agent sửa lại
> mốc reveal nội bộ (không đổi data-duration/timing tổng), render lại... Sau fix, tôi tự trích
> lại frame tại t=30s bằng ffmpeg độc lập và đo pixel chính xác bằng PIL (không chỉ xem bằng
> mắt) — xác nhận phần tử cuối ... nay dừng ở **y=1455/1920 (75,8%)**, trong khoảng yêu cầu.
>
> [Một nghi vấn đã tự loại trừ] Ở frame CTA, lần xem bằng mắt qua ảnh preview nén khiến tôi nghi
> ngờ chữ ký logo bị cắt ngắn... nhưng đo lại chính xác bằng phân tích pixel (PIL, quét từng
> dòng so màu nền)... cho kết quả nhất quán: phần tử cuối luôn ở **y=1678/1920 (87,4%)** — đúng
> trong khoảng yêu cầu... Kết luận: nghi vấn ban đầu là sai số khi nhìn ảnh preview bị nén/thu
> nhỏ, KHÔNG phải lỗi thật.
>
> Kết quả cuối: 7/7 frame đạt cân bằng dọc (đo pixel: **Hook 1519/79%, What-happened ~1470, Key
> facts 1539/80%, Data moment 1455/76%, Context 1407/73%, Impact ~1425, CTA 1678/87%**).

**Bài học kép rút ra**:
1. **Bug thật**: "cân bằng dọc" không chỉ là vấn đề CSS `top` tĩnh — nó còn là vấn đề **GSAP
   timing**: nếu phần tử ở đáy chỉ "hiện đủ" (opacity 1, đã chạy xong animation) SAU thời điểm
   bạn lấy mẫu QC, bạn sẽ đo nhầm ra "thiếu nội dung/trống nửa dưới" dù CSS layout đã đúng.
   → Khi QC 1 act, lấy mẫu ở gần **cuối** act (không phải giữa act) để chắc chắn mọi tween đã
   chạy xong.
2. **Phương pháp QC đúng**: `ffmpeg` trích PNG từ chính file `.mp4` đã render (không phải xem
   ảnh Studio thumbnail nén), rồi đo bằng thư viện xử lý ảnh (PIL/numpy — quét từng hàng pixel
   so với màu nền `#0B0E14` để tìm hàng pixel cuối cùng có nội dung khác nền). Xem-bằng-mắt qua
   ảnh preview nén **đã từng cho báo động giả** (nghi ngờ chữ ký logo bị cắt, thực tế không).
   Dùng phép đo định lượng làm trọng tài cuối cùng, không dùng cảm quan.

### 7.4 Con số tham chiếu — dải phân bố "chuẩn" trong `_reference-astra-openai`

`BRAND-SYSTEM.md` trích "top ~220px → ~1290px+" — xác nhận bằng cách đọc trực tiếp CSS: file
`03-facts.html` của reference có các `top:` lớn nhất là `4px, 56px, 220px, 560px`; file
`04-data.html` có `18px, 30px, 450px, 880px, 1290px`. Tức là "1290px" là điểm bắt đầu (`top`)
của khối phần tử CUỐI cùng trong file đó, không phải điểm kết thúc — khối đó còn cao thêm vài
trăm px nữa mới chạm dải an toàn 1400–1680px. Khi tính "điểm kết thúc" cho QC, luôn cộng thêm
chiều cao thật của phần tử tại `top` lớn nhất đó, đừng chỉ đọc mỗi con số `top`.

---

## 8. Quy tắc GSAP — bug thật + fix thật

Đối chiếu từng bullet của mục "GSAP / kỹ thuật" trong `BRAND-SYSTEM.md` với bằng chứng thật.

### 8.1 Vendor GSAP local

```html
<script src="assets/vendor/gsap.min.js"></script>
```
Xuất hiện y hệt ở **cả 9 project** (8 video + reference) — không project nào dùng
`<script src="https://cdn.jsdelivr.net/...">`. `assets/vendor/gsap.min.js` được copy từ
`node_modules/gsap/dist/gsap.min.js` sau khi `npm i gsap` (xem `package.json` mục 1 —
`"dependencies": {"gsap": "^3.15.0"}`).

### 8.2 `#root` KHÔNG gắn `data-composition-id` vào CSS selector

Xác nhận ở **mọi** file frame đã đọc: CSS luôn viết `#root { ... }` (selector trơn), trong khi
`<div>` thật ở HTML mang `data-composition-id="01-hook"` (hay tên act khác) như một **thuộc
tính đánh dấu**, KHÔNG BAO GIỜ dùng trong bộ chọn CSS kiểu
`#root[data-composition-id="01-hook"] { ... }`. Không tìm thấy trường hợp vi phạm nào trong 9
project — quy tắc này được tuân thủ tuyệt đối nhất quán, không có "before/after" vì chưa từng
bị phá.

### 8.3 SVG reveal phải có state ẩn mặc định đáng tin — ví dụ thật

Xem mục 6.4 (`iphone-duo-man-hinh-gap/04-data.html`):
```html
<circle id="dm-ring-fg" ... stroke-dasharray="1916.4" stroke-dashoffset="1916.4"/>
```
`dashoffset` bằng đúng `dasharray` được **ghi cứng trong HTML** — vòng tròn ẩn hoàn toàn (0%
nét vẽ) ngay cả TRƯỚC KHI GSAP timeline chạy dòng nào, kể cả nếu JS load chậm hoặc bị lỗi. Đây
chính xác là "state ẩn mặc định đáng tin" mà brand doc yêu cầu — không dựa vào
`el.getTotalLength()` tính runtime (cách đó có độ trễ 1 frame trước khi ẩn được, dễ "lộ tĩnh"
1 khung hình đầu).

### 8.4 `fromTo` "from" khác trạng thái ẩn + fix bằng `tl.set` + `immediateRender:false`

**Before (biến thể ngắn, dùng ở đa số project, KHÔNG sai nhưng có rủi ro)** —
`_reference-astra-openai/07-cta.html`:
```js
tl.fromTo('#t-cta', { autoAlpha: 0, y: 22 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out' }, 2.4);
tl.fromTo('#t-cta', { scale: 1 }, { scale: 1.04, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }, 3.1);
```
**After (fix thật, xuất hiện ở `gia-xang-dau-tang-hon-1200-dong-lit/07-cta.html`, project dựng
sau)**:
```js
tl.set('#t-cta', { autoAlpha: 0, y: 22, scale: 1 }, 0);
tl.fromTo('#t-cta', { autoAlpha: 0, y: 22 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out', immediateRender: false }, 2.15);
tl.fromTo('#t-cta', { scale: 1 }, { scale: 1.04, duration: 0.45, yoyo: true, repeat: 3, ease: 'sine.inOut', immediateRender: false }, 2.75);
```
**Vì sao fix này đúng nguyên tắc trong `BRAND-SYSTEM.md`** ("mọi `gsap.fromTo` có `from` khác
trạng thái ẩn đều nguy hiểm — GSAP hiển thị `from` đó suốt thời gian TRƯỚC `START`"): 2
`fromTo()` liên tiếp trên **cùng 1 phần tử** (`#t-cta`) — theo mặc định GSAP, `immediateRender`
của tween thứ 2 (`scale`) sẽ áp `from: {scale: 1}` NGAY LẬP TỨC lúc timeline dựng xong (tại thời
điểm 0), đè lên `autoAlpha` mà tween thứ nhất đang giữ ở trạng thái ẩn (`0`) trước mốc 2.15s —
nguy cơ phần tử "chớp lộ" ở thời điểm 0 nếu engine áp dụng theo thứ tự khác đi. Fix thêm
`tl.set(...)` ở mốc 0 để CHỦ ĐỘNG khai báo trạng thái ẩn đúng 1 lần, và
`immediateRender: false` trên cả 2 `fromTo` sau đó để chúng **không tự áp `from`-state ngay khi
được thêm vào timeline**, chỉ áp khi playhead thật sự chạm tới mốc thời gian của chúng.
**Khi 1 phần tử cần ≥ 2 tween `fromTo` khác nhau xếp nối tiếp, luôn theo pattern 3 dòng này**
(`tl.set` trạng thái ẩn ở mốc 0, rồi mỗi `fromTo` sau thêm `immediateRender: false`).

### 8.5 Không `width` cố định cho container số auto-fit — quan sát xuyên suốt

Không tìm thấy trường hợp nào set `width` cứng (px) lên `.dm-num`/`.d-num`/`.hk-name`/`.t-head`
— tất cả đều là text ở `display:` mặc định (`block`/`inline`) bên trong 1 container có
`left/right` (co giãn theo nội dung), KHÔNG có `width:` cố định. Ví dụ đối chiếu 2 con số khác độ
dài chữ số hoàn toàn tự nhiên không vỡ layout: `iphone-18-pro-thay-doi-so-voi-17-pro` hiển thị
`38,99` (`font-size:168px`) trong khi `iphone-duo-man-hinh-gap` hiển thị `104` (3 chữ số,
`font-size:112px` — khác font-size vì khác thiết kế, không phải do width ép buộc) — cả hai đều
dùng `.dm-num { font-weight:900; font-size:...; line-height:1; color:#FF5A1F; }` không có
`width`.

### 8.6 Không emoji — icon CSS/SVG thay thế 100%

Xác nhận 0 emoji trong toàn bộ 9 project (kiểm bằng cách đọc code, không phải suy đoán) — mọi
"icon" là CSS shape (`border-radius`, `::before`/`::after`, `border` tam giác — xem thư viện icon
tái dùng ở mục 5.2 và 6.6) hoặc SVG (`<circle>` ở ring-progress). Khi cần 1 icon mới không có
sẵn trong danh sách đã liệt kê, tự vẽ bằng tổ hợp `border-radius` + `border` + `::before`/
`::after`, KHÔNG chèn ký tự emoji Unicode.

### 8.7 `transform` CSS vs GSAP `xPercent`/`yPercent` xung đột — quy ước phòng tránh quan sát được

Không tìm thấy bug thật đã ghi nhận cho quy tắc này trong `COMPLIANCE.md` nào, nhưng quy ước
phòng tránh xuất hiện nhất quán: mọi phần tử được GSAP tween bằng `yPercent` (kiểu text-reveal
`.hk-name`, `.t-head .ln > span`) **không có bất kỳ khai báo `transform:` nào trong CSS** của
chính selector đó — `transform` chỉ xuất hiện trên các phần tử KHÁC được tween bằng
`scale`/`scaleX`/`scaleY` qua GSAP (GSAP tự quản lý toàn bộ thuộc tính `transform` của phần tử đó
từ đầu, không có CSS tĩnh chen vào). **Quy tắc thực dụng**: chọn ĐÚNG MỘT trong hai — hoặc để
GSAP toàn quyền set `transform` (kể cả `x`/`y`/`scale`/`rotate` gộp), hoặc dùng `xPercent`/
`yPercent` không kèm bất kỳ `transform:` CSS tĩnh nào trên cùng phần tử — không bao giờ trộn.

---

## 9. Audio pipeline cụ thể

### 9.1 Voiceover — `gen_voice.py` (xác nhận giống hệt nhau giữa các project, chỉ đổi mảng `lines`)

Đối chiếu `iphone-18-pro-thay-doi-so-voi-17-pro/gen_voice.py` và
`chung-khoan-viet-nang-hang-ban-rong/gen_voice.py` — **100% giống nhau về code**, chỉ khác nội
dung mảng `lines`:

```python
#!/usr/bin/env python3
import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [
    "{{DÒNG_1_HOOK}}",
    "{{DÒNG_2_WHAT_HAPPENED}}",
    "{{DÒNG_3_KEY_FACTS}}",
    "{{DÒNG_4_DATA_MOMENT}}",
    "{{DÒNG_5_CONTEXT}}",
    "{{DÒNG_6_IMPACT}}",
    "{{DÒNG_7_CTA — KHÔNG nhắc tên kênh}}",
]

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "voice")
os.makedirs(out_dir, exist_ok=True)

for i, text in enumerate(lines, start=1):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": { "speed": 1.09 }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={ "xi-api-key": API_KEY, "Content-Type": "application/json", "Accept": "audio/mpeg" },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"line{i}: HTTP {e.code} {e.reason}: {e.read().decode('utf-8', 'ignore')}", file=sys.stderr)
        sys.exit(1)
    out_path = os.path.join(out_dir, f"line{i}.mp3")
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"wrote {out_path} ({len(data)} bytes)")
```

Chạy: `ELEVENLABS_API_KEY=... python3 gen_voice.py`, rồi `ffprobe` từng file (mục 3.1).

**Bug thật đã gặp — ElevenLabs cắt cụt cuối câu** (`gia-xang-dau-tang-hon-1200-dong-lit`,
`COMPLIANCE.md`): dòng cuối (CTA) nghe hụt dù đã tăng đệm frame. Chẩn đoán bằng đo biên độ RMS
300ms cuối file mp3 — biên độ vẫn dao động mạnh (2000–4800) ngay tại điểm cắt thay vì giảm dần
về 0, tức API dừng sinh audio đột ngột giữa câu (không phải do thiếu khung hình đệm). **Fix**:
sinh lại CÙNG text/voice/model/speed 3 lần, so RMS 150ms cuối mỗi bản, chọn bản có biên độ giảm
tự nhiên nhất, cộng thêm fade-out 150ms cuối file cho chắc, cập nhật lại
`data-duration` của đúng `<audio>` đó trong `index.html`, chạy lại `carve.mjs`.
**Bài học**: nếu voice nghe "hụt" ở cuối, đừng vội tăng đệm/duration frame — đo RMS đuôi file mp3
trước, khả năng cao lỗi nằm ở chính file audio gốc.

### 9.2 BGM — Lyria recipe (lệnh CLI thật, đã dùng trong sản xuất thật)

Script: `~/.claude/skills/media-use/audio/scripts/lyria-recipe.py` (cài qua
`npx --yes hyperframes@0.8.30 skills` — xem `ROUTINE.md` bước 0). Flags thật:

```
usage: lyria-recipe.py [-h] --output OUTPUT --duration DURATION
                        [--prompt PROMPT] [--negative-prompt NEGATIVE_PROMPT]
                        [--bpm BPM] [--brightness BRIGHTNESS]
                        [--density DENSITY] [--scale SCALE]
```

Lệnh recipe "calm" chuẩn kênh Tin Tức Số (nguyên văn `AUDIO-NOTES.md` của
`_reference-astra-openai`, chỉ đổi từ "news explainer" cho khớp brand "Tin Tức Số"):

```bash
python lyria-recipe.py --output track-raw.wav --duration <TỔNG_VIDEO + 2-3s đệm cuối> \
  --density 0.25 --brightness 0.4 \
  --prompt "calm ambient news underscore, soft synth pads, sparse, minimal pulse, no drums, instrumental only" \
  --negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming, drums, heavy beat, aggressive percussion, busy rhythm, loud, driving, energetic, buildup, drop"
```

Sau đó: retrim khớp đúng tổng thời lượng thiết kế + fade-in ~1.5s đầu + fade-out ~2–3s cuối, xuất
`assets/bgm/track.mp3` (đây là file `index.html` trỏ tới, `raw.wav` chỉ là bản thô giữ lại tham
khảo — một số project không commit `raw.wav`).

### 9.3 Ducking — `carve.mjs` (lệnh CLI thật)

Script: `~/.claude/skills/hyperframes-audio/scripts/carve.mjs`. Flags thật:

```
carve.mjs --comp <file.html> [--bed <elementId>] [--voice <elementId> ...]
              [--strength 0..1] [--dry-run] [--core <dir>]

  --bed       id của track nhạc bị carve (tự phát hiện nếu bỏ trống)
  --voice     id của 1 track voice cần nhường chỗ; lặp lại được (tự phát hiện nếu bỏ trống)
  --strength  độ mạnh carve, 0..1 (mặc định 0.8)
  --dry-run   báo cáo sẽ ghi gì, không đụng gì
  --core      thư mục resolve @hyperframes/core (mặc định: thư mục của chính file comp)
```

Lệnh chuẩn kênh (nguyên văn `ROUTINE.md` bước 8 / `PRODUCTION-WORKFLOW.md` mục 4):

```bash
node ~/.claude/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --strength 0.4
```

`--strength 0.4` (KHÔNG phải mặc định 0.8) — vì BGM kênh này vốn đã rất nhẹ (`data-volume:0.30`),
carve mạnh hơn sẽ làm nhạc gần như biến mất hoàn toàn dưới giọng, mất luôn cảm giác "có nhạc
nền". `--bed`/`--voice` bỏ trống — công cụ tự nhận diện qua `id="el-bgm"` và
`data-audio-group="voiceover"` đã gắn sẵn trên các thẻ `<audio>`.

**Output của carve.mjs KHÔNG được tự tay viết lại**: nó ghi thẳng 3 attribute
`data-fx-carve` / `data-fx-chain` / `data-automation` (mục 2.2) vào đúng thẻ `<audio id="el-bgm">`
trong `index.html`. **Chạy lại lệnh này SAU MỌI thay đổi timing hoặc audio** (đổi
`data-duration`/`data-start` bất kỳ frame nào, đổi file voice, đổi file BGM) — automation cũ sẽ
lệch nhịp nếu không carve lại.

### 9.4 SFX — cue points thật (từ `iphone-18-pro-thay-doi-so-voi-17-pro/index.html`)

```html
<audio id="el-sfx-hook" src="assets/sfx/impact-bass-1.mp3" data-start="0.32" data-duration="0.6" data-track-index="30" data-volume="0.35"></audio>
<audio id="el-sfx-t1" src="assets/sfx/whoosh-short.mp3" data-start="6.70" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
<audio id="el-sfx-t2" src="assets/sfx/whoosh-short.mp3" data-start="14.86" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
<audio id="el-sfx-data" src="assets/sfx/pop.mp3" data-start="25.03" data-duration="0.4" data-track-index="30" data-volume="0.3"></audio>
<audio id="el-sfx-t3" src="assets/sfx/whoosh-short.mp3" data-start="32.90" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
<audio id="el-sfx-warn" src="assets/sfx/impact-bass-1.mp3" data-start="41.53" data-duration="0.6" data-track-index="30" data-volume="0.32"></audio>
<audio id="el-sfx-t4" src="assets/sfx/whoosh-short.mp3" data-start="49.77" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
<audio id="el-sfx-o1" src="assets/sfx/pop.mp3" data-start="50.92" data-duration="0.35" data-track-index="30" data-volume="0.3"></audio>
<audio id="el-sfx-o2" src="assets/sfx/click-soft.mp3" data-start="51.27" data-duration="0.35" data-track-index="30" data-volume="0.32"></audio>
<audio id="el-sfx-cta" src="assets/sfx/chime.mp3" data-start="52.02" data-duration="1.2" data-track-index="30" data-volume="0.32"></audio>
```

**Mẫu cue chuẩn (9-10 SFX cho 1 video ~57-75s)**:
- `impact-bass-1.mp3` (vol 0.32–0.35) — đúng lúc masthead/tên chủ thể xuất hiện ở Hook (~0.3s
  sau khi video bắt đầu, khớp mốc `hk-name` reveal), và đúng lúc 1 con số/tag "cảnh báo" xuất
  hiện (act Impact/warn).
- `whoosh-short.mp3` (vol 0.3) — mỗi lần **chuyển act** (đặt ở `data-start` ≈ `data-start` của
  act mới trừ ~0.1s) — nhưng **không phải MỌI lần chuyển act** đều có (video 7 act có 4-5
  whoosh, không phải 6).
- `pop.mp3` (vol 0.3) — đúng lúc số liệu chính "chốt" (data moment) và lúc mở 2 lựa chọn CTA.
- `click-soft.mp3` (vol 0.32) — lựa chọn thứ 2 ở CTA (tạo cảm giác "click" 2 lựa chọn liên tiếp
  khác nhịp với pop).
- `chime.mp3` (vol 0.32, duration 1.2s — dài hơn hẳn các SFX khác) — đúng lúc nút CTA
  "Bình luận quan điểm của bạn" xuất hiện, đánh dấu điểm kết.

---

## 10. Khung frame chung copy-paste được

Khung này dùng làm **điểm khởi đầu literal** cho MỌI act giữa (2–6) của MỌI style — đã bọc sẵn
mọi bất biến brand/kỹ thuật bắt buộc. Vùng cần tự thiết kế theo style được đánh dấu rõ
`/* === CUSTOMIZE PER STYLE HERE === */`.

```html
<template>
  <style>
    /* ================================================================
       KHỐI FONT — BẮT BUỘC, KHÔNG ĐƯỢC SỬA. Copy nguyên 12 dòng này
       (6 weight × 2 subset latin/vietnamese) vào MỌI frame mới.
       Chỉ giữ lại các weight thực sự dùng bên dưới nếu muốn file gọn hơn,
       nhưng weight NÀO dùng thì PHẢI có đủ cặp latin + vietnamese.
       ================================================================ */
    @font-face { font-family: 'Montserrat'; font-weight: 400; src: url('assets/fonts/Montserrat-400-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
    @font-face { font-family: 'Montserrat'; font-weight: 400; src: url('assets/fonts/Montserrat-400-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }
    @font-face { font-family: 'Montserrat'; font-weight: 500; src: url('assets/fonts/Montserrat-500-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
    @font-face { font-family: 'Montserrat'; font-weight: 500; src: url('assets/fonts/Montserrat-500-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }
    @font-face { font-family: 'Montserrat'; font-weight: 600; src: url('assets/fonts/Montserrat-600-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
    @font-face { font-family: 'Montserrat'; font-weight: 600; src: url('assets/fonts/Montserrat-600-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }
    @font-face { font-family: 'Montserrat'; font-weight: 700; src: url('assets/fonts/Montserrat-700-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
    @font-face { font-family: 'Montserrat'; font-weight: 700; src: url('assets/fonts/Montserrat-700-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }
    @font-face { font-family: 'Montserrat'; font-weight: 800; src: url('assets/fonts/Montserrat-800-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
    @font-face { font-family: 'Montserrat'; font-weight: 800; src: url('assets/fonts/Montserrat-800-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }
    @font-face { font-family: 'Montserrat'; font-weight: 900; src: url('assets/fonts/Montserrat-900-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
    @font-face { font-family: 'Montserrat'; font-weight: 900; src: url('assets/fonts/Montserrat-900-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }

    /* ================================================================
       ROOT — BẮT BUỘC, KHÔNG ĐƯỢC SỬA (ngoại trừ radial-gradient trang trí tuỳ chọn).
       Selector PHẢI là "#root" trơn — KHÔNG BAO GIỜ "#root[data-composition-id=...]"
       (xem mục 8.2 — gắn attribute selector làm font rơi về Times New Roman khi
       nhiều sub-composition mount lồng nhau).
       ================================================================ */
    #root { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: #0B0E14; }
    /* optional — glow trang trí phía sau, KHÔNG bắt buộc: */
    #root::before { content: ""; position: absolute; inset: 0; background: radial-gradient(70% 40% at 50% {{GLOW_Y}}%, rgba(255,90,31,0.14), transparent 60%); }

    /* === CUSTOMIZE PER STYLE HERE : kicker + tiêu đề — pattern chuẩn, hiếm khi cần đổi === */
    .xx-kicker { position: absolute; left: {{PAD}}px; right: {{PAD}}px; top: {{KICKER_TOP}}px; font-weight: 700; font-size: 26px; letter-spacing: 0.24em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .xx-head   { position: absolute; left: {{PAD}}px; right: {{PAD}}px; top: {{HEAD_TOP}}px; font-weight: 800; font-size: {{HEAD_SIZE}}px; line-height: 1.2; color: #fff; opacity: 0; }

    /* === CUSTOMIZE PER STYLE HERE : khối nội dung trung tâm mang ẩn dụ của style ===
       Ví dụ card-and-bar: .fc-card { border-radius:24px; background:#121724; ... }
       Ví dụ ring-progress: SVG <circle> với stroke-dasharray/dashoffset viết cứng
       Ví dụ split-comparison: 2 cột qua 1 vạch giữa
       — xem mục 6 cho code thật đầy đủ của 6 style đã dựng, mục 6.7-6.10 cho 4 style extrapolate.
       QUY TẮC BẤT BIẾN áp dụng cho khối này bất kể style:
         - accent màu CHỈ #FF5A1F (tích cực/trung tính) hoặc #FF4438 (rủi ro/cảnh báo)
         - KHÔNG width cố định (px) trên container số auto-fit (mục 8.5)
         - Reveal SVG/vẽ-dần phải có state ẩn mặc định trong HTML tĩnh, không chỉ dựa runtime JS (mục 8.3)
         - Icon = CSS shape/SVG, KHÔNG emoji (mục 8.6)
         - KHÔNG set "transform:" CSS tĩnh trên phần tử sẽ bị GSAP tween bằng xPercent/yPercent (mục 8.7)
    */
    .xx-content { position: absolute; left: {{PAD}}px; right: {{PAD}}px; top: {{CONTENT_TOP}}px; /* ...tuỳ style... */ }

    /* === CUSTOMIZE PER STYLE HERE : dòng phụ/caption cuối — dùng để chạm dải an toàn 1400-1680px
       khi khối nội dung tự nhiên kết thúc sớm hơn — xem mục 7 === */
    .xx-caption { position: absolute; left: {{PAD}}px; right: {{PAD}}px; top: {{CAPTION_TOP}}px; /* mục tiêu: 1400-1680px */ font-weight: 500; font-size: 30px; line-height: 1.5; color: rgba(255,255,255,0.65); opacity: 0; }
  </style>

  <div id="root" data-composition-id="{{ACT_ID}}" data-width="1080" data-height="1920">
    <div class="xx-kicker" id="xx-kicker">{{NHÃN_NGẮN_UPPERCASE}}</div>
    <div class="xx-head" id="xx-head">{{TIÊU_ĐỀ_CHÍNH}}</div>

    <div class="xx-content" id="xx-content">
      <!-- === CUSTOMIZE PER STYLE HERE : DOM thật của ẩn dụ style, xem mục 6 === -->
    </div>

    <div class="xx-caption" id="xx-caption">{{DÒNG_PHỤ_NGUỒN_HOẶC_GHI_CHÚ}}</div>
  </div>

  <script>
    /* ================================================================
       KHUNG SCRIPT — BẮT BUỘC. gsap.timeline({paused:true}) + đăng ký
       vào window.__timelines[<data-composition-id>] ở dòng cuối cùng.
       Mọi thời điểm số trong tl.fromTo(...) là GIÂY TÍNH TỪ ĐẦU ACT NÀY,
       không phải từ đầu video.
       ================================================================ */
    const tl = gsap.timeline({ paused: true });

    tl.fromTo('#xx-kicker', { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.36, ease: 'power2.out' }, 0);
    tl.fromTo('#xx-head', { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power2.out' }, 0.18);

    /* === CUSTOMIZE PER STYLE HERE : reveal của .xx-content, trải đều theo nhịp voice thật
       của act này (không dồn hết vào 1-2s đầu nếu act dài) — xem ví dụ mục 6.6 (4 ô cách nhau 3.6s) === */
    tl.fromTo('#xx-content', { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 0.42, ease: 'power3.out' }, 0.7);

    tl.fromTo('#xx-caption', { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, /* {{MỐC_GẦN_CUỐI_ACT}} */);

    window.__timelines['{{ACT_ID}}'] = tl;
  </script>
</template>
```

**Checklist trước khi coi 1 frame mới là "xong"** (áp cho mọi frame dựng từ khung này):
- [ ] `npm run check` sạch 0 error.
- [ ] Không màu nào ngoài `#FF5A1F` / `#0B0E14` / `#121724` / `#FFFFFF` / `#FF4438` (+ độ trong
      suốt `rgba(...)` của chính các màu này).
- [ ] Không emoji.
- [ ] Font chỉ Montserrat, không @font-face nào thiếu subset vietnamese cho weight đang dùng.
- [ ] Không `width:` cố định (px) trên container số/chữ auto-fit.
- [ ] Mọi SVG reveal có state ẩn mặc định viết cứng trong HTML tĩnh.
- [ ] Không có 2 `fromTo` chồng nhau trên cùng 1 selector mà thiếu `tl.set` mở đầu +
      `immediateRender:false` (trừ khi chắc chắn timeline chỉ chạy tuyến tính, không seek ngược).
- [ ] Trích 1 frame gần CUỐI act (không phải giữa act) bằng `ffmpeg`, đo bằng mắt hoặc bằng script
      pixel: phần tử cuối cùng kết thúc trong khoảng `top: 1400–1680px`.
- [ ] `data-duration` của frame = `data-duration` thật của file voice tương ứng (đo bằng
      `ffprobe`) + đệm 0.3–0.5s (riêng CTA đệm dài hơn).

---

## 11. Mâu thuẫn thực tế đã phát hiện

Liệt kê đầy đủ, để con người quyết định có cập nhật văn bản brand hay không:

1. **`CONSTRUCTION-STYLES.md` — Style 6 (`7-timeline-chronology`), act Context**: văn bản mô tả
   "trục thời gian **ngang** đầy đủ 4-5 mốc". Code thật (`khong-khi-lanh-ap-thap-nhiet-doi-bien-dong/
   compositions/frames/05-context.html`) dùng **trục dọc** (`.ct-axis { width: 4px }`, các hàng
   xếp theo `top` tăng dần từ 0 tới 760px). Xem mục 6.5. Đây là quyết định thiết kế hợp lý cho
   canvas dọc 1080px hẹp, nhưng khác hẳn mô tả bằng lời — nên hoặc sửa văn bản, hoặc ghi rõ
   "trục dọc thích ứng canvas dọc" thay vì "ngang".

2. **`hyperframes-core` CLAUDE.md** (tài liệu chung của framework, không phải riêng kênh này) nói
   "Give timed visual elements `class=\"clip\"`. ... lint warns without it." Thực tế **toàn bộ
   9 project của kênh** (kể cả reference) dùng `class="scene"` (tên tự đặt riêng của kênh, với
   CSS full-frame tương đương) cho các `<div>` mount act, KHÔNG dùng `class="clip"` ở đâu cả, và
   `npm run check` vẫn PASS 0 warning theo các log COMPLIANCE.md đã đọc. Không rõ đây là do
   `class` không thực sự bị lint kiểm tra chặt (đúng như CLAUDE.md tự nói: "framework keys
   visibility off `data-start`, not the class"), hay do phiên bản CLI đang pin (`0.8.30`–`0.8.35`)
   chưa bật cảnh báo này. **Khuyến nghị thực dụng**: tiếp tục dùng `class="scene"` để nhất quán
   với toàn bộ code base hiện có của kênh — nhưng nếu `npm run check` tương lai báo warning về
   thiếu class `clip`, đó không phải bug của bạn, là do CLI đổi hành vi.

3. **`BRAND-SYSTEM.md` — độ dài CTA "~5-7s"**: số liệu thật quan sát được trải rộng hơn —
   `chung-khoan-viet-nang-hang-ban-rong` 7.22s (khớp), `_reference-astra-openai` 7.06s (khớp),
   nhưng `gia-xang-dau-tang-hon-1200-dong-lit` **8.70s** và `iphone-18-pro-thay-doi-so-voi-17-pro`
   **7.50s** — CTA của `gia-xang-dau` vượt hẳn mốc trên "~7s". Đây là hệ quả trực tiếp của mục
   3.4/9.1 (đệm CTA phải đủ dài để voice + pulse animation hoàn tất, và 1 lần phải tăng đệm CTA
   thêm ~1.8s để sửa lỗi "đoạn kết bị cụt gấp" theo COMPLIANCE.md) — không phải lỗi, nhưng con số
   "~5-7s" trong văn bản nên đọc là **hướng dẫn khởi điểm**, không phải trần cứng; ưu tiên "voice
   đọc xong + pulse chạy đủ 3 lần + không cắt gấp" hơn là ép đúng khung 5-7s.

4. **`data-hf-id`**: không phải mâu thuẫn với brand docs (docs không nhắc tới nó), nhưng đáng ghi
   chú (mục 1) vì tài liệu framework chung có thể ngầm định nó luôn tồn tại — thực tế nó **hoàn
   toàn tuỳ chọn** với file hand-authored (bằng chứng: `cpi-my-thang-8-fed-tang-lai-suat` có 0
   occurrence trong toàn bộ 7 file frame, vẫn build/render/publish thành công).
