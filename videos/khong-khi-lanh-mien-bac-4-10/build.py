#!/usr/bin/env python3
"""Sinh index.html + compositions/frames/*.html cho video khong-khi-lanh-mien-bac-4-10.
Timing lấy từ độ dài voice thật (ffprobe) + đệm. Chạy lại sau mọi thay đổi voice."""
import json, subprocess, re, os, random, html

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
W = [l.strip() for l in open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')]
assert len(W) == 7


def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).decode())


VD = [dur(f'assets/voice/line{i}.mp3') for i in range(1, 8)]
PAD = [0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.9]
FD = [round(v + p, 2) for v, p in zip(VD, PAD)]
ST = []
t = 0.0
for d in FD:
    ST.append(round(t, 2))
    t += d
TOTAL = round(t, 2)
print('frames', FD, 'starts', ST, 'total', TOTAL)

FONTS = ''.join(
    f"@font-face {{ font-family: 'Montserrat'; font-weight: {w}; src: url('assets/fonts/Montserrat-{w}-{s}.woff2') format('woff2'); unicode-range: {r}; }}\n"
    for w in (400, 500, 600, 700, 800, 900)
    for s, r in (('latin', 'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD'),
                 ('vietnamese', 'U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB'))
)

BASE = """
    #root { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: transparent; }
    .card { background: #121724; border: 1.5px solid rgba(255,255,255,0.10); border-radius: 22px; box-shadow: 0 0 40px rgba(255,90,31,0.14); }
    .kick { font-weight: 700; font-size: 26px; letter-spacing: 0.24em; text-transform: uppercase; color: #FF5A1F; }
    .hot { color: #FF4438; } .or { color: #FF5A1F; }
"""


def tpl(cid, css, body, js):
    return f"""<template>
  <style>
{FONTS}{BASE}{css}
  </style>

  <div id="root" data-composition-id="{cid}" data-width="1080" data-height="1920">
{body}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}
    window.__timelines['{cid}'] = tl;
  </script>
</template>
"""


# ---------------------------------------------------------------- 01 HOOK
hook_css = """
    #root { background: #0B0E14; }
    .hk-photo { position: absolute; left: 0; right: 0; top: 0; height: 900px; overflow: hidden; background: #05070c; }
    .hk-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 48% 40%; }
    .hk-scrim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11,14,20,0.10) 0%, rgba(11,14,20,0.22) 52%, rgba(11,14,20,0.99) 100%); }
    .hk-tint { position: absolute; inset: 0; background: radial-gradient(120% 70% at 78% 20%, rgba(255,90,31,0.16), transparent 58%); mix-blend-mode: screen; }
    .hk-panel { position: absolute; left: 0; right: 0; top: 858px; bottom: 0; background: #0B0E14; padding: 62px 60px 0; display: flex; flex-direction: column; align-items: flex-start; }
    .hk-masthead { display: flex; align-items: center; gap: 14px; margin-bottom: 26px; opacity: 0; }
    .hk-logo { width: 56px; height: 56px; flex: none; } .hk-logo img { display: block; width: 100%; height: 100%; }
    .hk-mw { font-weight: 800; font-size: 32px; letter-spacing: 0.01em; color: #fff; }
    .hk-badge { display: inline-flex; align-items: center; gap: 10px; padding: 11px 20px; border-radius: 9px; border: 1.5px solid rgba(255,90,31,0.85); background: rgba(255,90,31,0.12); margin-bottom: 34px; opacity: 0; }
    .hk-badge .d { width: 9px; height: 9px; border-radius: 50%; background: #FF5A1F; flex: none; }
    .hk-badge span { font-weight: 500; font-size: 23px; letter-spacing: 0.03em; color: #fff; white-space: nowrap; }
    .hk-wrap { overflow: hidden; padding-bottom: 6px; }
    .hk-l1 { font-weight: 900; font-size: 168px; line-height: 1.02; letter-spacing: -0.02em; color: #fff; white-space: nowrap; }
    .hk-l2 { font-weight: 900; font-size: 168px; line-height: 1.02; letter-spacing: -0.02em; color: #FF5A1F; white-space: nowrap; }
    .hk-sub { margin-top: 20px; font-weight: 700; font-size: 44px; line-height: 1.2; color: rgba(255,255,255,0.92); opacity: 0; }
    .hk-tags { display: flex; gap: 18px; margin-top: 38px; }
    .hk-tag { font-weight: 800; font-size: 40px; line-height: 1; color: #fff; opacity: 0; white-space: nowrap; }
    .hk-tag.warn { color: #FF4438; }
    .hk-tag .dot { display: inline-block; width: 11px; height: 11px; border-radius: 50%; background: currentColor; margin: 0 12px 7px 0; vertical-align: middle; }
"""
hook_body = """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="hk-tint"></div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress · 3/10/2026</span></div>
      <div class="hk-wrap"><div class="hk-l1" id="hk-a">Không khí</div></div>
      <div class="hk-wrap"><div class="hk-l2" id="hk-b">lạnh về</div></div>
      <div class="hk-sub" id="hk-sub">Tràn xuống miền Bắc từ đêm 4/10</div>
      <div class="hk-tags">
        <div class="hk-tag warn" id="hk-t1"><span class="dot"></span>Nóng tới 38,4°C</div>
        <div class="hk-tag" id="hk-t2"><span class="dot"></span>Lạnh từ đêm 4/10</div>
      </div>
    </div>
"""
hook_js = """
    tl.fromTo('.hk-photo', { autoAlpha: 0.5, scale: 1.1 }, { autoAlpha: 1, scale: 1, duration: 0.95, ease: 'power2.out' }, 0);
    tl.fromTo('.hk-panel', { y: 48 }, { y: 0, duration: 0.55, ease: 'power3.out' }, 0.08);
    tl.fromTo('.hk-masthead', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.25);
    tl.fromTo('.hk-badge', { autoAlpha: 0, scale: 0.9 }, { autoAlpha: 1, scale: 1, duration: 0.36, ease: 'back.out(1.7)' }, 0.42);
    tl.fromTo('#hk-a', { yPercent: 118 }, { yPercent: 0, duration: 0.6, ease: 'power4.out' }, 0.62);
    tl.fromTo('#hk-b', { yPercent: 118 }, { yPercent: 0, duration: 0.6, ease: 'power4.out' }, 0.8);
    tl.fromTo('#hk-sub', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 1.25);
    tl.fromTo('#hk-t1', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.6);
    tl.fromTo('#hk-t2', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.85);
"""

# ---------------------------------------------------------------- 02 WHAT (split dọc: ảnh | panel)
what_css = """
    .w-photo { position: absolute; left: 40px; top: 330px; width: 440px; height: 1080px; border-radius: 22px; overflow: hidden; box-shadow: 0 0 40px rgba(255,90,31,0.18); opacity: 0; }
    .w-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 47% 50%; }
    .w-photo .cap { position: absolute; left: 0; right: 0; bottom: 0; padding: 70px 22px 22px; background: linear-gradient(180deg, transparent, rgba(11,14,20,0.92)); font-weight: 600; font-size: 21px; color: rgba(255,255,255,0.85); }
    .w-div { position: absolute; left: 508px; top: 330px; width: 3px; height: 1080px; background: linear-gradient(180deg, #FF5A1F, rgba(255,90,31,0.15)); transform-origin: top; }
    .w-panel { position: absolute; left: 540px; top: 330px; width: 500px; height: 1080px; display: flex; flex-direction: column; }
    .w-kick { opacity: 0; font-size: 22px; }
    .w-head { margin-top: 22px; font-weight: 900; font-size: 60px; line-height: 1.12; opacity: 0; }
    .w-steps { margin-top: 44px; display: flex; flex-direction: column; gap: 22px; flex: 1; }
    .w-step { padding: 26px 26px; opacity: 0; flex: 1; display: flex; flex-direction: column; justify-content: center; }
    .w-step .when { font-weight: 800; font-size: 26px; letter-spacing: 0.12em; text-transform: uppercase; color: #FF5A1F; }
    .w-step .what { margin-top: 10px; font-weight: 800; font-size: 42px; line-height: 1.15; }
    .w-note { margin-top: 20px; font-weight: 600; font-size: 22px; color: rgba(255,255,255,0.62); opacity: 0; }
"""
what_body = """
    <div class="w-photo" id="w-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="cap">Ảnh: VnExpress</div></div>
    <div class="w-div" id="w-div"></div>
    <div class="w-panel">
      <div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div>
      <div class="w-head" id="w-head">Không khí lạnh <span class="or">đổ xuống</span> miền Bắc</div>
      <div class="w-steps">
        <div class="card w-step" id="w-s1"><div class="when">Khoảng đêm 4/10</div><div class="what">Tới <span class="or">Đông Bắc Bộ</span></div></div>
        <div class="card w-step" id="w-s2"><div class="when">Sau đó</div><div class="what">Lan ra <span class="or">toàn Bắc Bộ</span></div></div>
        <div class="card w-step" id="w-s3"><div class="when">Và cả</div><div class="what"><span class="or">Bắc Trung Bộ</span> chuyển lạnh</div></div>
      </div>
      <div class="w-note" id="w-note">Theo Trung tâm Dự báo Khí tượng Thủy văn quốc gia</div>
    </div>
"""
what_js = """
    tl.fromTo('#w-photo', { autoAlpha: 0, x: -50 }, { autoAlpha: 1, x: 0, duration: 0.6, ease: 'power3.out' }, 0.1);
    tl.fromTo('#w-div', { scaleY: 0, autoAlpha: 0 }, { scaleY: 1, autoAlpha: 1, duration: 0.7, ease: 'power2.inOut' }, 0.2);
    tl.fromTo('#w-kick', { autoAlpha: 0, y: -12 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.45);
    tl.fromTo('#w-head', { autoAlpha: 0, x: 40 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 0.6);
    tl.fromTo('#w-s1', { autoAlpha: 0, x: 60 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 2.4);
    tl.fromTo('#w-s2', { autoAlpha: 0, x: 60 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 3.6);
    tl.fromTo('#w-s3', { autoAlpha: 0, x: 60 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 4.9);
    tl.fromTo('#w-note', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.5 }, 6.0);
    tl.fromTo('#w-photo img', { scale: 1.0 }, { scale: 1.06, duration: 7.5, ease: 'none' }, 0.1);
"""

# ---------------------------------------------------------------- 03 FACTS (mỗi fact 1 hàng chia đôi)
facts_css = """
    .f-head { position: absolute; left: 60px; right: 60px; top: 312px; display: flex; justify-content: space-between; align-items: baseline; opacity: 0; }
    .f-head .kick { font-size: 24px; }
    .f-rows { position: absolute; left: 40px; right: 40px; top: 380px; display: flex; flex-direction: column; gap: 22px; }
    .f-row { position: relative; height: 230px; display: flex; align-items: center; opacity: 0; }
    .f-row::after { content: ""; position: absolute; left: 300px; top: 28px; bottom: 28px; width: 2px; background: rgba(255,255,255,0.14); }
    .f-lab { width: 300px; padding: 0 34px; font-weight: 600; font-size: 31px; line-height: 1.25; color: rgba(255,255,255,0.62); }
    .f-val { flex: 1; padding: 0 36px; text-align: right; font-weight: 900; font-size: 92px; line-height: 1; white-space: nowrap; }
    .f-val.sm { font-size: 38px; line-height: 1.3; padding: 0 28px; }
    .f-val.md { font-size: 56px; }
    .f-val small { font-size: 0.5em; font-weight: 800; }
"""
facts_body = """
    <div class="f-head" id="f-head"><div class="kick">Tuần nóng qua đi</div><div class="kick" style="color:rgba(255,255,255,0.5)">Số liệu</div></div>
    <div class="f-rows">
      <div class="card f-row" id="f-r1"><div class="f-lab">Hà Nội, cao nhất</div><div class="f-val hot" id="f-v1">38,4<small>°C</small></div></div>
      <div class="card f-row" id="f-r2"><div class="f-lab">Trên 37°C</div><div class="f-val sm">Sơn La · Phú Thọ · Cao Bằng<br><span class="hot">Hải Phòng · Hưng Yên · Ninh Bình</span></div></div>
      <div class="card f-row" id="f-r3"><div class="f-lab">Một tuần qua</div><div class="f-val md">Nắng nóng <span class="hot">kéo dài</span></div></div>
      <div class="card f-row" id="f-r4"><div class="f-lab">Không khí lạnh đến</div><div class="f-val md or">Từ đêm 4/10</div></div>
    </div>
"""
facts_js = """
    tl.fromTo('#f-head', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4 }, 0.1);
    tl.fromTo('#f-r1', { autoAlpha: 0, x: -70 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 0.3);
    tl.fromTo('#f-r2', { autoAlpha: 0, x: 70 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 2.9);
    tl.fromTo('#f-r3', { autoAlpha: 0, x: -70 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 5.7);
    tl.fromTo('#f-r4', { autoAlpha: 0, x: 70 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 7.2);
"""

# ---------------------------------------------------------------- 04 DATA (2 số cạnh nhau qua vạch)
data_css = """
    .d-kick { position: absolute; left: 0; right: 0; top: 330px; text-align: center; opacity: 0; font-size: 26px; }
    .d-title { position: absolute; left: 60px; right: 60px; top: 388px; text-align: center; font-weight: 800; font-size: 44px; line-height: 1.2; color: rgba(255,255,255,0.9); opacity: 0; }
    .d-split { position: absolute; left: 40px; right: 40px; top: 520px; height: 560px; display: flex; align-items: stretch; }
    .d-side { flex: 1; padding: 40px 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0; }
    .d-side .when { font-weight: 700; font-size: 26px; letter-spacing: 0.1em; text-transform: uppercase; }
    .d-side .num { margin-top: 26px; font-weight: 900; font-size: 92px; line-height: 1; white-space: nowrap; letter-spacing: -0.02em; }
    .d-side .num small { font-size: 0.42em; font-weight: 800; letter-spacing: 0; }
    .d-side .sub { margin-top: 18px; font-weight: 600; font-size: 26px; color: rgba(255,255,255,0.6); }
    .d-left { margin-right: 0; } .d-left .when { color: rgba(255,255,255,0.55); } .d-left .num { color: rgba(255,255,255,0.45); }
    .d-right .when { color: #FF5A1F; } .d-right .num { color: #FF5A1F; }
    .d-mid { width: 4px; align-self: stretch; background: linear-gradient(180deg, transparent, #FF5A1F 18%, #FF5A1F 82%, transparent); position: relative; transform-origin: center; opacity: 0; }
    .d-mid::after { content: "→"; position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); width: 76px; height: 76px; border-radius: 50%; background: #0B0E14; border: 3px solid #FF5A1F; font-weight: 900; font-size: 40px; line-height: 70px; text-align: center; color: #FF5A1F; }
    .d-drop { position: absolute; left: 140px; right: 140px; top: 1140px; height: 230px; border-radius: 26px; border: 2.5px solid rgba(255,90,31,0.85); background: linear-gradient(180deg, rgba(255,90,31,0.16), rgba(255,68,56,0.08)); display: flex; align-items: center; justify-content: center; gap: 28px; opacity: 0; box-shadow: 0 0 50px rgba(255,90,31,0.18); }
    .d-drop .arr { width: 0; height: 0; border-left: 34px solid transparent; border-right: 34px solid transparent; border-top: 58px solid #FF5A1F; }
    .d-drop .big { font-weight: 900; font-size: 104px; line-height: 1; color: #fff; white-space: nowrap; }
    .d-drop .big small { font-size: 0.45em; font-weight: 800; color: rgba(255,255,255,0.85); margin-left: 8px; }
    .d-src { position: absolute; left: 0; right: 0; top: 1396px; text-align: center; font-weight: 600; font-size: 22px; color: rgba(255,255,255,0.55); opacity: 0; }
"""
data_body = """
    <div class="kick d-kick" id="d-kick">Dự báo cho Hà Nội</div>
    <div class="d-title" id="d-title">Nhiệt độ cao nhất sẽ hạ nhiệt</div>
    <div class="d-split">
      <div class="d-side d-left" id="d-l"><div class="when">Ngày 2 và 3/10</div><div class="num">26–35<small>°C</small></div><div class="sub">Dao động</div></div>
      <div class="d-mid" id="d-m"></div>
      <div class="d-side d-right" id="d-r"><div class="when">Chủ nhật</div><div class="num">23–30<small>°C</small></div><div class="sub">Dao động</div></div>
    </div>
    <div class="d-drop" id="d-drop"><div class="arr"></div><div class="big">Giảm 5<small>độ</small></div></div>
    <div class="d-src" id="d-src">Nguồn: AccuWeather, qua VnExpress</div>
"""
data_js = """
    tl.fromTo('#d-kick', { autoAlpha: 0, y: -12 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.1);
    tl.fromTo('#d-title', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'power2.out' }, 0.3);
    tl.fromTo('#d-m', { autoAlpha: 0, scaleY: 0 }, { autoAlpha: 1, scaleY: 1, duration: 0.6, ease: 'power2.inOut' }, 2.2);
    tl.fromTo('#d-l', { autoAlpha: 0, x: -50 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 2.7);
    tl.fromTo('#d-r', { autoAlpha: 0, x: 50 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 5.2);
    tl.fromTo('#d-drop', { autoAlpha: 0, scale: 0.85 }, { autoAlpha: 1, scale: 1, duration: 0.55, ease: 'back.out(1.6)' }, 7.0);
    tl.to('#d-drop', { scale: 1.03, duration: 0.5, yoyo: true, repeat: 1, ease: 'sine.inOut' }, 7.7);
    tl.fromTo('#d-src', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.5 }, 7.9);
"""

# ---------------------------------------------------------------- 05 CONTEXT (bảng 2 cột đối xứng)
ctx_css = """
    .c-sec { position: absolute; left: 60px; right: 60px; text-align: center; opacity: 0; font-size: 24px; }
    .c-grid { position: absolute; left: 40px; right: 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .c-cell { padding: 30px 26px; text-align: center; opacity: 0; display: flex; flex-direction: column; justify-content: center; }
    .c-cell .reg { font-weight: 800; font-size: 28px; letter-spacing: 0.04em; color: rgba(255,255,255,0.6); }
    .c-cell .val { margin-top: 14px; font-weight: 900; font-size: 56px; line-height: 1.12; }
    .c-cell .val.big { font-size: 104px; line-height: 1; }
    .c-cell .val small { font-size: 0.45em; font-weight: 800; }
    .c-cell .hint { margin-top: 12px; font-weight: 600; font-size: 24px; color: rgba(255,255,255,0.58); }
    #c-sec1 { top: 312px; } #c-g1 { top: 372px; height: 330px; }
    #c-sec2 { top: 770px; } #c-g2 { top: 830px; height: 400px; }
    #c-foot { position: absolute; left: 60px; right: 60px; top: 1262px; text-align: center; font-weight: 600; font-size: 26px; line-height: 1.35; color: rgba(255,255,255,0.7); opacity: 0; }
"""
ctx_body = """
    <div class="kick c-sec" id="c-sec1">Mưa giông đi kèm — theo vùng</div>
    <div class="c-grid" id="c-g1">
      <div class="card c-cell" id="c-a1"><div class="reg">Bắc Bộ</div><div class="val or">4/10 → sáng 5/10</div><div class="hint">Mưa, mưa vừa và dông</div></div>
      <div class="card c-cell" id="c-a2"><div class="reg">Thanh Hóa – Huế</div><div class="val or">Đêm 4 → 6/10</div><div class="hint">Mưa vừa và dông</div></div>
    </div>
    <div class="kick c-sec" id="c-sec2">Nhiệt độ thấp nhất</div>
    <div class="c-grid" id="c-g2">
      <div class="card c-cell" id="c-b1"><div class="reg">Bắc Bộ và Thanh Hóa</div><div class="val big">19–22<small>°C</small></div><div class="hint">Phổ biến</div></div>
      <div class="card c-cell" id="c-b2"><div class="reg">Vùng núi cao</div><div class="val big or">14–17<small>°C</small></div><div class="hint">Phổ biến</div></div>
    </div>
    <div id="c-foot">Hà Nội: trời chuyển lạnh từ gần sáng 5/10, kèm mưa giông cục bộ</div>
"""
ctx_js = """
    tl.fromTo('#c-sec1', { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.1);
    tl.fromTo('#c-a1', { autoAlpha: 0, x: -80 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 0.45);
    tl.fromTo('#c-a2', { autoAlpha: 0, x: 80 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 0.6);
    tl.fromTo('#c-sec2', { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 6.4);
    tl.fromTo('#c-b1', { autoAlpha: 0, x: -80 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 6.8);
    tl.fromTo('#c-b2', { autoAlpha: 0, x: 80 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 8.6);
    tl.fromTo('#c-foot', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.5 }, 10.2);
"""

# ---------------------------------------------------------------- 06 IMPACT (chia đôi NGANG trên/dưới)
imp_css = """
    .i-half { position: absolute; left: 40px; right: 40px; padding: 34px 36px; opacity: 0; }
    #i-top { top: 330px; height: 520px; display: flex; gap: 30px; align-items: center; }
    #i-bot { top: 930px; height: 500px; }
    .i-tag { font-weight: 700; font-size: 24px; letter-spacing: 0.22em; text-transform: uppercase; color: #FF5A1F; }
    .i-ico { flex: none; width: 150px; height: 130px; position: relative; }
    .i-ico::before { content: ""; position: absolute; left: 0; bottom: 0; width: 0; height: 0; border-left: 75px solid transparent; border-right: 75px solid transparent; border-bottom: 130px solid #FF4438; }
    .i-ico::after { content: "!"; position: absolute; left: 0; right: 0; bottom: 6px; text-align: center; font-weight: 900; font-size: 74px; line-height: 1; color: #0B0E14; }
    .i-txt h3 { margin-top: 14px; font-weight: 900; font-size: 54px; line-height: 1.12; }
    .i-txt p { margin-top: 18px; font-weight: 600; font-size: 33px; line-height: 1.3; color: rgba(255,255,255,0.78); }
    .i-sep { position: absolute; left: 40px; right: 40px; top: 880px; height: 3px; background: linear-gradient(90deg, transparent, #FF5A1F, transparent); transform-origin: center; }
    .i-stats { display: flex; gap: 16px; margin-top: 30px; }
    .i-stat { flex: 1; padding: 30px 12px; border-radius: 18px; background: rgba(255,90,31,0.10); border: 1.5px solid rgba(255,90,31,0.55); text-align: center; opacity: 0; }
    .i-stat .n { font-weight: 900; font-size: 64px; line-height: 1; color: #FF5A1F; white-space: nowrap; }
    .i-stat .n small { font-size: 0.45em; font-weight: 800; }
    .i-stat .l { margin-top: 12px; font-weight: 700; font-size: 25px; line-height: 1.25; color: rgba(255,255,255,0.85); }
    .i-bot-h { margin-top: 14px; font-weight: 900; font-size: 54px; line-height: 1.12; }
    .i-bot-p { margin-top: 16px; font-weight: 600; font-size: 31px; color: rgba(255,255,255,0.72); }
"""
imp_body = """
    <div class="card i-half" id="i-top">
      <div class="i-ico" id="i-ico"></div>
      <div class="i-txt"><div class="i-tag">Trên đất liền</div><h3>Đề phòng lốc, sét, mưa đá, gió giật mạnh</h3><p>Mưa lớn cục bộ có thể gây lũ quét, sạt lở đất, ngập úng vùng trũng thấp</p></div>
    </div>
    <div class="i-sep" id="i-sep"></div>
    <div class="card i-half" id="i-bot">
      <div class="i-tag">Trên vịnh Bắc Bộ</div>
      <div class="i-bot-h">Gió đông bắc <span class="or">mạnh lên</span></div>
      <div class="i-stats">
        <div class="i-stat" id="i-s1"><div class="n">6–7</div><div class="l">Gió<br>cấp</div></div>
        <div class="i-stat" id="i-s2"><div class="n">8–9</div><div class="l">Giật<br>cấp</div></div>
        <div class="i-stat" id="i-s3"><div class="n">2–3<small>m</small></div><div class="l">Sóng<br>cao</div></div>
      </div>
      <div class="i-bot-p">Ảnh hưởng đến tàu thuyền và hoạt động trên biển</div>
    </div>
"""
imp_js = """
    tl.fromTo('#i-top', { autoAlpha: 0, y: -50 }, { autoAlpha: 1, y: 0, duration: 0.55, ease: 'power3.out' }, 0.15);
    tl.fromTo('#i-ico', { scale: 0.6 }, { scale: 1, duration: 0.5, ease: 'back.out(2)' }, 0.5);
    tl.fromTo('#i-sep', { scaleX: 0, autoAlpha: 0 }, { scaleX: 1, autoAlpha: 1, duration: 0.6, ease: 'power2.inOut' }, 5.2);
    tl.fromTo('#i-bot', { autoAlpha: 0, y: 50 }, { autoAlpha: 1, y: 0, duration: 0.55, ease: 'power3.out' }, 5.6);
    tl.fromTo('#i-s1', { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'back.out(1.5)' }, 7.0);
    tl.fromTo('#i-s2', { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'back.out(1.5)' }, 8.3);
    tl.fromTo('#i-s3', { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'back.out(1.5)' }, 9.6);
"""

# ---------------------------------------------------------------- 07 CTA
cta_css = """
    #root::before { content: ""; position: absolute; inset: 0; background: radial-gradient(80% 50% at 50% 40%, rgba(255,90,31,0.16), transparent 60%); }
    .t-wrap { position: absolute; left: 64px; right: 64px; top: 372px; text-align: center; }
    .t-kicker { font-weight: 700; font-size: 28px; letter-spacing: 0.26em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .t-head { margin-top: 34px; font-weight: 900; font-size: 104px; line-height: 1.1; color: #fff; }
    .t-head .ln { overflow: hidden; padding-bottom: 6px; } .t-head .ln > span { display: block; }
    .t-opts { display: flex; justify-content: center; align-items: stretch; gap: 20px; margin-top: 72px; }
    .t-opt { flex: 1; max-width: 420px; padding: 40px 24px; border-radius: 20px; border: 2px solid; opacity: 0; }
    .t-opt.up { border-color: rgba(255,90,31,0.8); background: rgba(255,90,31,0.12); }
    .t-opt.down { border-color: rgba(255,68,56,0.8); background: rgba(255,68,56,0.12); }
    .t-opt .emo { width: 52px; height: 52px; margin: 0 auto; position: relative; }
    .t-opt.up .emo { border: 4px solid #FF5A1F; border-radius: 50%; }
    .t-opt.up .emo::after { content: ""; position: absolute; left: 50%; top: 15px; width: 14px; height: 14px; border-top: 4px solid #FF5A1F; border-right: 4px solid #FF5A1F; transform: translateX(-50%) rotate(-45deg); }
    .t-opt.down .emo::before { content: ""; position: absolute; left: 0; bottom: 0; width: 0; height: 0; border-left: 26px solid transparent; border-right: 26px solid transparent; border-bottom: 46px solid #FF4438; }
    .t-opt.down .emo::after { content: "!"; position: absolute; left: 0; right: 0; bottom: -2px; text-align: center; font-weight: 900; font-size: 28px; color: #0B0E14; }
    .t-opt .lab { margin-top: 20px; font-weight: 800; font-size: 38px; line-height: 1.2; color: #fff; }
    .t-vs { display: flex; align-items: center; font-weight: 900; font-size: 36px; color: rgba(255,255,255,0.4); opacity: 0; }
    .t-cta { display: inline-flex; align-items: center; gap: 18px; margin-top: 76px; padding: 26px 42px; border-radius: 100px; background: #FF5A1F; opacity: 0; }
    .t-cta .ico { width: 44px; height: 44px; flex: none; border-radius: 13px 13px 13px 4px; background: #fff; position: relative; }
    .t-cta .ico::before { content: ""; position: absolute; left: 10px; top: 13px; right: 10px; height: 4px; border-radius: 2px; background: #FF5A1F; box-shadow: 0 10px 0 #FF5A1F; }
    .t-cta span { font-weight: 800; font-size: 40px; letter-spacing: 0.01em; color: #0B0E14; }
    .t-sign { position: absolute; left: 0; right: 0; top: 1330px; display: flex; align-items: center; justify-content: center; gap: 14px; opacity: 0; }
    .t-sign .m { width: 46px; height: 46px; } .t-sign .w { font-weight: 800; font-size: 32px; color: rgba(255,255,255,0.88); }
"""
cta_body = """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Lạnh về: dễ chịu</span></div>
        <div class="ln"><span id="t-h2">hay đáng lo?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Dễ chịu đáng mong</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Điều đáng lo</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>
"""
cta_js = """
    tl.fromTo('#t-kicker', { autoAlpha: 0, y: -12 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0);
    tl.fromTo('#t-h1', { yPercent: 118 }, { yPercent: 0, duration: 0.55, ease: 'power4.out' }, 0.2);
    tl.fromTo('#t-h2', { yPercent: 118 }, { yPercent: 0, duration: 0.55, ease: 'power4.out' }, 0.36);
    tl.fromTo('#t-o1', { autoAlpha: 0, y: 28, scale: 0.92 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }, 3.4);
    tl.fromTo('#t-vs', { autoAlpha: 0, scale: 0.5 }, { autoAlpha: 1, scale: 1, duration: 0.3, ease: 'back.out(2)' }, 3.65);
    tl.fromTo('#t-o2', { autoAlpha: 0, y: 28, scale: 0.92 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }, 3.75);
    tl.fromTo('#t-cta', { autoAlpha: 0, y: 22 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out' }, 5.3);
    tl.to('#t-cta', { scale: 1.04, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }, 5.9);
    tl.fromTo('#t-sign', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4 }, 5.6);
"""

FR = [('01-hook', hook_css, hook_body, hook_js), ('02-what', what_css, what_body, what_js),
      ('03-facts', facts_css, facts_body, facts_js), ('04-data', data_css, data_body, data_js),
      ('05-context', ctx_css, ctx_body, ctx_js), ('06-impact', imp_css, imp_body, imp_js),
      ('07-cta', cta_css, cta_body, cta_js)]
os.makedirs('compositions/frames', exist_ok=True)
for cid, css, body, js in FR:
    open(f'compositions/frames/{cid}.html', 'w', encoding='utf-8').write(tpl(cid, css, body, js))

# ---------------------------------------------------------------- karaoke caption data
def load_words(i):
    return json.load(open(f'assets/voice/tr{i}.json', encoding='utf-8'))


def script_words(line):
    return line.split()


def map_times(sw, ww):
    """gán thời gian cho từng từ script dựa trên timeline whisper (tỉ lệ theo số ký tự tích luỹ)."""
    wl = [max(1, len(re.sub(r'\W', '', x['text']))) for x in ww]
    cum = [0]
    for l in wl:
        cum.append(cum[-1] + l)
    tot = cum[-1]
    sl = [max(1, len(re.sub(r'\W', '', x))) for x in sw]
    scum = [0]
    for l in sl:
        scum.append(scum[-1] + l)
    stot = scum[-1]

    def tat(f):  # f 0..1 -> time
        c = f * tot
        for k in range(len(ww)):
            if cum[k] <= c <= cum[k + 1]:
                a, b = ww[k]['start'], ww[k]['end']
                return a + (b - a) * ((c - cum[k]) / max(1, wl[k]))
        return ww[-1]['end']
    out = []
    for k in range(len(sw)):
        out.append((tat(scum[k] / stot), tat(scum[k + 1] / stot)))
    return out


caps = []  # (chunk_html, start_abs, end_abs, top)
for i, line in enumerate(W, start=1):
    sw = script_words(line)
    ww = load_words(i)
    tm = map_times(sw, ww)
    # chunk 3-6 từ, ngắt ở dấu câu
    chunks, cur = [], []
    for k, w in enumerate(sw):
        cur.append(k)
        punct = w[-1] in ',.;:?!'
        if len(cur) >= 6 or (punct and len(cur) >= 3) or k == len(sw) - 1:
            chunks.append(cur)
            cur = []
    # gộp chunk cuối quá ngắn
    if len(chunks) > 1 and len(chunks[-1]) < 3:
        chunks[-2] += chunks[-1]
        chunks.pop()
    for c in chunks:
        st0 = ST[i - 1] + tm[c[0]][0]
        en0 = ST[i - 1] + tm[c[-1]][1]
        spans = ''.join(f'<span class="w" data-s="{ST[i-1]+tm[k][0]:.3f}">{html.escape(sw[k])}</span> ' for k in c)
        caps.append((spans.strip(), st0, en0, 740 if i == 1 else 1492))

# ---------------------------------------------------------------- index.html
rng = random.Random(20261003)
stars = ''.join(
    f'<circle cx="{rng.randint(10,1070)}" cy="{rng.randint(10,1910)}" r="{rng.choice([1.5,2,2.5,3])}" opacity="{rng.choice([0.15,0.2,0.28,0.35,0.4])}"/>'
    for _ in range(40))

scene_names = ['01-hook', '02-what', '03-facts', '04-data', '05-context', '06-impact', '07-cta']
scenes = '\n'.join(
    f'      <div id="el-{n}" class="scene" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{ST[k]}" data-duration="{FD[k]}" data-track-index="1"></div>'
    for k, n in enumerate(scene_names))
voices = '\n'.join(
    f'      <audio id="el-voice-{k+1}" src="assets/voice/line{k+1}.mp3" data-start="{ST[k]}" data-duration="{VD[k]:.2f}" data-track-index="10" data-audio-group="voiceover"></audio>'
    for k in range(7))
BGMDUR = TOTAL
sfx = [
    ('hook', 'impact-bass-1', 0.3, 0.6, 0.35), ('t1', 'whoosh-short', ST[1] - 0.1, 0.5, 0.3), ('t2', 'whoosh-short', ST[2] - 0.1, 0.5, 0.3),
    ('t3', 'whoosh-short', ST[3] - 0.1, 0.5, 0.3), ('data', 'pop', ST[3] + 5.2, 0.4, 0.3), ('drop', 'impact-bass-1', ST[3] + 7.0, 0.6, 0.3),
    ('t4', 'whoosh-short', ST[4] - 0.1, 0.5, 0.3), ('t5', 'whoosh-short', ST[5] - 0.1, 0.5, 0.3), ('sep', 'click-soft', ST[5] + 5.6, 0.35, 0.32),
    ('t6', 'whoosh-short', ST[6] - 0.1, 0.5, 0.3), ('o1', 'pop', ST[6] + 3.4, 0.35, 0.3), ('o2', 'click-soft', ST[6] + 3.75, 0.35, 0.32),
    ('cta', 'chime', ST[6] + 5.3, 1.2, 0.32)]
sfx_html = '\n'.join(
    f'      <audio id="el-sfx-{n}" src="assets/sfx/{f}.mp3" data-start="{s:.2f}" data-duration="{d}" data-track-index="{30+k}" data-volume="{v}"></audio>'
    for k, (n, f, s, d, v) in enumerate(sfx))

cap_html = '\n'.join(
    f'      <div class="cap-chunk" id="cc{k}" style="top:{top}px">{sp}</div>' for k, (sp, a, b, top) in enumerate(caps))
cap_js = []
for k, (sp, a, b, top) in enumerate(caps):
    nxt = caps[k + 1][1] if k + 1 < len(caps) else 1e9
    end = min(b + 0.3, nxt - 0.02)
    cap_js.append(f"tl.set('#cc{k}', {{ opacity: 1 }}, {a:.3f}); tl.set('#cc{k}', {{ opacity: 0 }}, {end:.3f});")
cap_js.append("""document.querySelectorAll('.cap-chunk .w').forEach(function (w) { tl.to(w, { color: '#FF5A1F', duration: 0.1, ease: 'none' }, parseFloat(w.getAttribute('data-s'))); });""")

index = f"""<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, height=1920">
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
{FONTS}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #0B0E14; font-family: "Montserrat", sans-serif; color: #FFFFFF; }}
      .scene {{ position: absolute; inset: 0; width: 100%; height: 100%; z-index: 5; }}

      #bg-depth {{ position: absolute; inset: 0; overflow: hidden; z-index: 0; }}
      #bg-depth .blob {{ position: absolute; border-radius: 50%; filter: blur(60px); }}
      #bg-depth .blob-1 {{ width: 640px; height: 640px; background: radial-gradient(circle, rgba(255,90,31,0.20), transparent 70%); top: -120px; left: -160px; }}
      #bg-depth .blob-2 {{ width: 560px; height: 560px; background: radial-gradient(circle, rgba(255,68,56,0.16), transparent 70%); top: 900px; right: -200px; }}
      #bg-depth .blob-3 {{ width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,90,31,0.12), transparent 70%); bottom: -180px; left: 200px; }}
      #bg-stars {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
      #bg-stars circle {{ fill: #fff; }}

      #brand-anchor {{ position: absolute; inset: 0; z-index: 90; pointer-events: none; opacity: 0; }}
      #ba-source {{ position: absolute; left: 44px; top: 46px; display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px; border-radius: 8px; background: rgba(11,14,20,0.6); border: 1px solid rgba(255,255,255,0.12); }}
      #ba-source .dot {{ width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; flex: none; }}
      #ba-source span {{ font-weight: 500; font-size: 21px; letter-spacing: 0.02em; color: rgba(255,255,255,0.9); white-space: nowrap; }}
      #ba-brand {{ position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }}
      #ba-brand .mark {{ width: 44px; height: 44px; flex: none; }}
      #ba-brand .mark img {{ display: block; width: 100%; height: 100%; }}
      #ba-brand .word {{ font-weight: 800; font-size: 24px; letter-spacing: 0.01em; color: #fff; }}

      #captions {{ position: absolute; inset: 0; z-index: 80; pointer-events: none; }}
      .cap-chunk {{ position: absolute; left: 70px; right: 190px; text-align: center; opacity: 0; font-weight: 800; font-size: 50px; line-height: 1.2; text-shadow: 0 2px 14px rgba(0,0,0,0.85), 0 0 4px rgba(0,0,0,0.9); }}
      .cap-chunk .w {{ color: rgba(255,255,255,0.88); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="bg-depth">
        <div class="blob blob-1" data-layout-allow-overflow></div><div class="blob blob-2" data-layout-allow-overflow></div><div class="blob blob-3" data-layout-allow-overflow></div>
        <svg id="bg-stars" viewBox="0 0 1080 1920">{stars}</svg>
      </div>

{scenes}

      <div id="brand-anchor">
        <div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress</span></div>
        <div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div>
      </div>

      <div id="captions">
{cap_html}
      </div>

{voices}

      <audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{BGMDUR}" data-track-index="20" data-volume="0.3"></audio>

{sfx_html}
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.set('#brand-anchor', {{ opacity: 1 }}, {ST[1]});
      tl.to('.blob', {{ x: '+=40', y: '-=30', duration: 18, ease: 'sine.inOut', repeat: 3, yoyo: true, stagger: 3 }}, 0);
      tl.to('#bg-stars circle', {{ opacity: '+=0.25', duration: 4, ease: 'sine.inOut', repeat: 17, yoyo: true, stagger: {{ each: 0.15, from: 'random' }} }}, 0);
      {chr(10).join('      ' + x for x in cap_js).strip()}
      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(index)
json.dump({'total': TOTAL, 'starts': ST, 'durs': FD}, open('/tmp/w/timing.json', 'w'))
print('ok')
