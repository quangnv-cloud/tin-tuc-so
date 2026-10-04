#!/usr/bin/env python3
"""Sinh compositions/frames/*.html + index.html từ SCRIPT.md + assets/voice/*.mp3.
Chạy: python3 build.py   (căn timing theo voice thật; chạy lại sau mỗi thay đổi voice)."""
import re, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from align import align_line, durations

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)
LINES = open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')
assert len(LINES) == 7
PAD = 0.4
CTA_PAD = 0.85
SLUG = os.path.basename(BASE)

ALIGN, VOICE = {}, {}
for i, l in enumerate(LINES, 1):
    ALIGN[i], VOICE[i] = align_line(l, i)
DUR = {i: round(VOICE[i] + (CTA_PAD if i == 7 else PAD), 3) for i in range(1, 8)}
START = {}
t = 0.0
for i in range(1, 8):
    START[i] = round(t, 3)
    t += DUR[i]
TOTAL = round(t, 3)

DISPLAY = {'Phi-pha': 'FIFA', 'A-xê-an': 'ASEAN'}


def norm(w):
    return re.sub(r'[^\w\-]', '', w.lower())


def wt(line, phrase, nth=1):
    """Thời điểm (giây, cục bộ trong frame) từ đầu của cụm `phrase` ở lần xuất hiện thứ nth."""
    toks = [norm(x) for x in phrase.split()]
    ws = [norm(x['w']) for x in ALIGN[line]]
    c = 0
    for k in range(len(ws) - len(toks) + 1):
        if ws[k:k + len(toks)] == toks:
            c += 1
            if c == nth:
                return ALIGN[line][k]['s']
    raise KeyError(f'{line}:{phrase}')


# ---------- CSS / HTML chung ----------
REF = open('../_reference-astra-openai/compositions/frames/01-hook.html', encoding='utf-8').read()
FONTS = '\n'.join(re.findall(r"@font-face[^\n]*", REF))
COMMON_CSS = FONTS + """
    #root { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: transparent; }
    .cap-wrap { position: absolute; left: 60px; right: 90px; top: 1490px; height: 100px; z-index: 40; pointer-events: none; }
    .cap-chunk { position: absolute; inset: 0; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; column-gap: 14px; row-gap: 4px; opacity: 0; visibility: hidden; font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 46px; line-height: 1.18; text-align: center; text-shadow: 0 2px 14px rgba(0,0,0,0.85), 0 0 3px rgba(0,0,0,0.9); }
    .cap-chunk .w { color: rgba(255,255,255,0.58); }
    .kick { display: flex; align-items: center; gap: 16px; opacity: 0; }
    .kick i { display: block; width: 44px; height: 5px; border-radius: 3px; background: #FF5A1F; }
    .kick b { font-weight: 800; font-size: 26px; letter-spacing: 0.24em; text-transform: uppercase; color: #FF5A1F; }
    .kick.r i { background: #FF4438; } .kick.r b { color: #FF4438; }
    .paper { position: absolute; background: #121724; border: 1.5px solid rgba(255,255,255,0.14); border-radius: 14px; box-shadow: 0 18px 40px rgba(0,0,0,0.55), 0 0 40px rgba(255,90,31,0.10); opacity: 0; }
    .paper.hot { border-left: 9px solid #FF5A1F; }
    .paper.warn { border-left: 9px solid #FF4438; box-shadow: 0 18px 40px rgba(0,0,0,0.55), 0 0 40px rgba(255,68,56,0.12); }
    .tape { position: absolute; width: 150px; height: 40px; background: rgba(255,90,31,0.55); top: -20px; left: 50%; margin-left: -75px; transform: rotate(-2deg); }
    .lab { font-weight: 800; font-size: 24px; letter-spacing: 0.16em; text-transform: uppercase; color: #FF5A1F; }
    .lab.r { color: #FF4438; } .lab.d { color: rgba(255,255,255,0.6); }
"""


def caps(line, prefix):
    """HTML + JS karaoke cho 1 dòng voice (thời gian cục bộ trong frame)."""
    ws = ALIGN[line]
    chunks, cur = [], []
    for w in ws:
        cur.append(w)
        txt = ' '.join(DISPLAY.get(x['w'], x['w']) for x in cur)
        if re.search(r'[,.:?]$', w['w']) and len(cur) >= 2 or len(cur) >= 5 or len(txt) >= 24:
            chunks.append(cur); cur = []
    if cur:
        if chunks and len(cur) == 1:
            chunks[-1].extend(cur)
        else:
            chunks.append(cur)
    html, js = [], []
    for ci, ch in enumerate(chunks, 1):
        cid = f'{prefix}{ci}'
        spans = ''.join(f'<span class="w" id="{cid}-w{k}">{DISPLAY.get(x["w"], x["w"])}</span>' for k, x in enumerate(ch, 1))
        html.append(f'      <div class="cap-chunk" id="{cid}">{spans}</div>')
        t0 = ch[0]['s']
        t_off = chunks[ci][0]['s'] + 0.05 if ci < len(chunks) else min(ch[-1]['e'] + 0.3, DUR[line] - 0.05)
        js.append(f"    tl.set('#{cid}', {{ autoAlpha: 1 }}, {t0:.3f});")
        for k, x in enumerate(ch, 1):
            js.append(f"    tl.to('#{cid}-w{k}', {{ color: '#FF5A1F', duration: 0.1, ease: 'none' }}, {x['s']:.3f});")
        js.append(f"    tl.set('#{cid}', {{ autoAlpha: 0 }}, {t_off:.3f});")
    return '\n'.join(html), '\n'.join(js)


def frame(fid, line, css, body, anim, prefix):
    chtml, cjs = caps(line, prefix)
    return f"""<template>
  <style>
{COMMON_CSS}
{css}
  </style>

  <div id="root" data-composition-id="{fid}" data-width="1080" data-height="1920">
{body}
    <div class="cap-wrap">
{chtml}
    </div>
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
{anim}
{cjs}
    window.__timelines['{fid}'] = tl;
  </script>
</template>
"""


SFX = []  # (thời điểm tuyệt đối, tệp, âm lượng)


def sfx(line, t, kind='pop'):
    SFX.append((round(START[line] + t, 3), kind))


def reveal(sel, t, y=24, dur=0.45, ease='power3.out', rot=None, extra=''):
    if rot is None:
        return f"    tl.fromTo('{sel}', {{ autoAlpha: 0, y: {y} }}, {{ autoAlpha: 1, y: 0, duration: {dur}, ease: '{ease}' {extra}}}, {t:.3f});"
    r0, r1 = rot
    return f"    tl.fromTo('{sel}', {{ autoAlpha: 0, y: {y}, rotation: {r0} }}, {{ autoAlpha: 1, y: 0, rotation: {r1}, duration: {dur}, ease: '{ease}' }}, {t:.3f});"


# ======================= FRAME 1 — HOOK =======================
def f1():
    css = """
    .hk-photo { position: absolute; left: 0; right: 0; top: 0; height: 760px; overflow: hidden; background: #05070c; }
    .hk-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; }
    .hk-scrim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11,14,20,0.08) 0%, rgba(11,14,20,0.30) 58%, rgba(11,14,20,0.99) 100%); }
    .hk-panel { position: absolute; left: 0; right: 0; top: 760px; bottom: 0; padding: 40px 60px 0; display: flex; flex-direction: column; align-items: flex-start; }
    .hk-masthead { display: flex; align-items: center; gap: 13px; margin-bottom: 28px; opacity: 0; }
    .hk-logo { width: 52px; height: 52px; flex: none; } .hk-logo img { display: block; width: 100%; height: 100%; }
    .hk-mw { font-weight: 800; font-size: 30px; color: #fff; }
    .hk-badge { display: inline-flex; align-items: center; gap: 12px; padding: 8px 18px 8px 8px; border-radius: 100px; border: 1.5px solid rgba(255,90,31,0.85); background: rgba(255,90,31,0.1); margin-bottom: 26px; opacity: 0; }
    .hk-badge .ring { width: 30px; height: 30px; border-radius: 50%; border: 3px solid #FF5A1F; display: flex; align-items: center; justify-content: center; flex: none; }
    .hk-badge .ring .dot { width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; }
    .hk-badge span.lbl { font-weight: 500; font-size: 21px; letter-spacing: 0.03em; color: #fff; white-space: nowrap; }
    .hk-name-wrap { overflow: hidden; }
    .hk-name { font-weight: 900; font-size: 128px; line-height: 1.17; letter-spacing: -0.02em; white-space: nowrap; }
    .hk-name.a { color: #fff; } .hk-name.b { color: #FF5A1F; }
    .hk-sub { margin-top: 18px; font-weight: 500; font-size: 30px; color: rgba(255,255,255,0.72); opacity: 0; }
    .hk-tags { display: flex; flex-direction: column; gap: 16px; margin-top: 30px; }
    .hk-tag { display: flex; align-items: center; font-weight: 800; font-size: 42px; line-height: 1.2; opacity: 0; }
    .hk-tag.warn { color: #FF4438; } .hk-tag.hot { color: #FF5A1F; }
    .hk-tag .dot { display: inline-block; width: 16px; height: 16px; border-radius: 50%; background: currentColor; margin-right: 18px; flex: none; }
    """
    body = """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="ring"><span class="dot"></span></span><span class="lbl">Nguồn: VnExpress · 4/10/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name a" id="hk-name1">VIỆT NAM</div></div>
      <div class="hk-name-wrap"><div class="hk-name b" id="hk-name2">MALAYSIA</div></div>
      <div class="hk-sub" id="hk-sub">Tranh hạng ba FIFA ASEAN Cup 2026 · 16h ngày 5/10</div>
      <div class="hk-tags">
        <div class="hk-tag hot" id="hk-t1"><span class="dot"></span>Malaysia 12 năm chưa thắng</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Hai đội đều thiếu quân</div>
      </div>
    </div>"""
    anim = """
    tl.fromTo('.hk-photo', { autoAlpha: 0.5, scale: 1.12 }, { autoAlpha: 1, scale: 1, duration: 1.0, ease: 'power2.out' }, 0);
    tl.fromTo('.hk-panel', { y: 48 }, { y: 0, duration: 0.55, ease: 'power3.out' }, 0.1);
    tl.fromTo('.hk-masthead', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.3);
    tl.fromTo('.hk-badge', { autoAlpha: 0, scale: 0.9 }, { autoAlpha: 1, scale: 1, duration: 0.36, ease: 'back.out(1.7)' }, 0.52);
    tl.fromTo('#hk-name1', { yPercent: 118 }, { yPercent: 0, duration: 0.65, ease: 'power4.out' }, 0.8);
    tl.fromTo('#hk-name2', { yPercent: 118 }, { yPercent: 0, duration: 0.65, ease: 'power4.out' }, 0.94);
    tl.fromTo('#hk-sub', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4 }, 1.5);
    tl.fromTo('#hk-t1', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.8);
    tl.fromTo('#hk-t2', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 2.1);"""
    SFX.append((round(START[1] + 0.9, 3), 'impact'))
    return frame('01-hook', 1, css, body, anim, 'ac')


# ======================= FRAME 2 — WHAT HAPPENED =======================
def f2():
    css = """
    .w-photo { position: absolute; left: 90px; top: 330px; width: 900px; height: 540px; padding: 8px; background: #fff; box-shadow: 0 22px 50px rgba(0,0,0,0.6), 0 0 44px rgba(255,90,31,0.18); opacity: 0; }
    .w-photo img { display: block; width: 100%; height: 100%; object-fit: cover; }
    .w-photo .credit { position: absolute; right: 8px; bottom: 8px; padding: 6px 14px; background: rgba(11,14,20,0.85); font-weight: 600; font-size: 20px; color: #fff; letter-spacing: 0.04em; }
    .w-qmark { position: absolute; left: 50px; top: 830px; font-weight: 900; font-size: 420px; line-height: 1; color: #FF5A1F; opacity: 0; }
    .w-kick { position: absolute; left: 60px; top: 930px; }
    .w-head { position: absolute; left: 60px; right: 60px; top: 990px; }
    .w-head .ln { overflow: hidden; } .w-head .ln > span { display: block; font-weight: 900; font-size: 78px; line-height: 1.16; }
    .w-head .o { color: #FF5A1F; }
    .w-rows { position: absolute; left: 60px; right: 60px; top: 1190px; }
    .w-row { display: flex; align-items: center; justify-content: space-between; height: 84px; border-top: 1.5px solid rgba(255,255,255,0.14); opacity: 0; }
    .w-row:last-child { border-bottom: 1.5px solid rgba(255,255,255,0.14); }
    .w-row .k { font-weight: 800; font-size: 22px; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.55); }
    .w-row .v { font-weight: 800; font-size: 38px; color: #fff; text-align: right; }
    .w-row .v em { font-style: normal; color: #FF5A1F; }
    """
    body = """
    <div class="w-qmark" id="w-q" data-layout-allow-overlap="">“</div>
    <div class="w-photo" id="w-photo"><div class="tape"></div><img src="assets/img/article-hero.jpg" alt=""><div class="credit">Ảnh: VnExpress</div></div>
    <div class="kick w-kick" id="w-kick"><i></i><b>Chuyện gì xảy ra</b></div>
    <div class="w-head">
      <div class="ln"><span id="w-h1">Trận tranh hạng ba</span></div>
      <div class="ln"><span id="w-h2" class="o">FIFA ASEAN Cup 2026</span></div>
    </div>
    <div class="w-rows">
      <div class="w-row" id="w-r1"><span class="k">Giờ đấu</span><span class="v">16h · <em>thứ Hai 5/10</em></span></div>
      <div class="w-row" id="w-r2"><span class="k">Sân</span><span class="v">Gelora Bung Karno · Jakarta</span></div>
      <div class="w-row" id="w-r3"><span class="k">Bảng A</span><span class="v">Malaysia <em>7 điểm</em> · ghi 9 bàn</span></div>
    </div>"""
    t_time = wt(2, 'lúc mười sáu')
    t_san = wt(2, 'sân')
    t_my = wt(2, 'Malaysia')
    anim = f"""
    tl.fromTo('#w-photo', {{ autoAlpha: 0, y: 70, rotation: -5 }}, {{ autoAlpha: 1, y: 0, rotation: -1.6, duration: 0.7, ease: 'power3.out' }}, 0.05);
    tl.fromTo('#w-q', {{ autoAlpha: 0, scale: 0.8 }}, {{ autoAlpha: 0.13, scale: 1, duration: 0.8, ease: 'power2.out' }}, 0.4);
    tl.fromTo('#w-kick', {{ autoAlpha: 0, x: -20 }}, {{ autoAlpha: 1, x: 0, duration: 0.4, ease: 'power2.out' }}, 0.5);
    tl.fromTo('#w-h1', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.6, ease: 'power4.out' }}, 0.65);
    tl.fromTo('#w-h2', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.6, ease: 'power4.out' }}, 0.8);
{reveal('#w-r1', t_time, 20, 0.4)}
{reveal('#w-r2', t_san, 20, 0.4)}
{reveal('#w-r3', t_my, 20, 0.4)}
    tl.to('#w-photo', {{ rotation: -0.9, scale: 1.015, duration: 8, ease: 'sine.inOut' }}, 0.8);"""
    for t, k in [(0.1, 'whoosh'), (t_time, 'click'), (t_san, 'click'), (t_my, 'pop')]:
        sfx(2, t, k)
    return frame('02-what', 2, css, body, anim, 'bc')


# ======================= FRAME 3 — KEY FACTS =======================
def f3():
    css = """
    .p1 { left: 60px; top: 320px; width: 960px; height: 470px; padding: 34px 40px 0 44px; }
    .p2 { left: 60px; top: 840px; width: 960px; height: 600px; padding: 34px 40px 0 44px; }
    .f-lab { display: flex; align-items: center; justify-content: space-between; }
    .f-chips { display: flex; gap: 16px; margin-top: 26px; }
    .f-chip { flex: 1; padding: 22px 12px 20px; border-radius: 14px; border: 2px solid rgba(255,255,255,0.18); text-align: center; background: rgba(255,255,255,0.03); opacity: 0; }
    .f-chip.hot { border-color: rgba(255,90,31,0.85); background: rgba(255,90,31,0.1); }
    .f-chip.warn { border-color: rgba(255,68,56,0.85); background: rgba(255,68,56,0.1); }
    .f-chip .sc { font-weight: 900; font-size: 74px; line-height: 1; color: #fff; }
    .f-chip.hot .sc { color: #FF5A1F; } .f-chip.warn .sc { color: #FF4438; }
    .f-chip .op { margin-top: 12px; font-weight: 700; font-size: 26px; color: rgba(255,255,255,0.8); }
    .f-foot { margin-top: 28px; display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 34px; opacity: 0; }
    .f-foot em { font-style: normal; color: #FF5A1F; }
    .f-foot .sh { width: 30px; height: 34px; background: #FF5A1F; clip-path: polygon(0 0, 100% 0, 100% 62%, 50% 100%, 0 62%); flex: none; }
    .f-streak { margin-top: 30px; opacity: 0; }
    .f-streak .tx { font-weight: 800; font-size: 34px; margin-bottom: 18px; }
    .f-streak .tx em { font-style: normal; color: #FF4438; }
    .f-ticks { display: flex; gap: 6px; }
    .f-ticks i { display: block; flex: 1; height: 54px; border-radius: 4px; background: #FF5A1F; opacity: 0; }
    .f-ticks i.x { background: #FF4438; }
    .f-ticks-cap { margin-top: 12px; display: flex; justify-content: space-between; font-weight: 600; font-size: 21px; color: rgba(255,255,255,0.6); }
    """
    ticks = ''.join(f'<i id="tk{k}"></i>' if k < 27 else '<i class="x" id="tk27"></i>' for k in range(1, 28))
    body = f"""
    <div class="paper hot p1" id="p1"><div class="tape"></div>
      <div class="f-lab"><span class="lab">Malaysia · bảng A</span><span class="lab d">Chung kết: lỡ hẹn</span></div>
      <div class="f-chips">
        <div class="f-chip hot" id="c1"><div class="sc">3–0</div><div class="op">Bangladesh</div></div>
        <div class="f-chip" id="c2"><div class="sc">0–0</div><div class="op">Indonesia</div></div>
        <div class="f-chip hot" id="c3"><div class="sc">6–0</div><div class="op">Singapore</div></div>
      </div>
      <div class="f-foot" id="f1foot"><span class="sh"></span><span><em>7 điểm</em> · chưa thủng lưới</span></div>
    </div>
    <div class="paper warn p2" id="p2"><div class="tape"></div>
      <div class="f-lab"><span class="lab r">Việt Nam · bảng B</span><span class="lab d">Vòng bảng</span></div>
      <div class="f-chips">
        <div class="f-chip warn" id="c4"><div class="sc">0–2</div><div class="op">Thái Lan</div></div>
        <div class="f-chip hot" id="c5"><div class="sc">4–2</div><div class="op">Pakistan</div></div>
      </div>
      <div class="f-streak" id="f-streak">
        <div class="tx"><em>27 trận</em> bất bại bị ngắt</div>
        <div class="f-ticks">{ticks}</div>
        <div class="f-ticks-cap"><span>Chuỗi bất bại</span><span>Thua Thái Lan 0–2</span></div>
      </div>
    </div>"""
    t = {k: wt(3, v) for k, v in dict(c1='Bangladesh', c2='Indonesia', c3='Singapore', foot='chưa thủng', vn='Việt Nam', c4='Thái Lan', st='chấm dứt', c5='Pakistan').items()}
    anim = f"""
{reveal('#p1', 0.15, 50, 0.6, rot=(-4, -1.2))}
{reveal('#c1', t['c1'], 18, 0.35)}
{reveal('#c2', t['c2'], 18, 0.35)}
{reveal('#c3', t['c3'], 18, 0.35)}
{reveal('#f1foot', t['foot'], 14, 0.35)}
{reveal('#p2', t['vn'] - 0.1, 60, 0.6, rot=(4, 1.0))}
{reveal('#c4', t['c4'], 18, 0.35)}
{reveal('#f-streak', t['st'] - 0.5, 14, 0.3)}
    tl.fromTo('#p2 .f-ticks i', {{ autoAlpha: 0, scaleY: 0.2 }}, {{ autoAlpha: 1, scaleY: 1, duration: 0.28, ease: 'back.out(2)', stagger: 0.03 }}, {t['st'] - 0.4:.3f});
    tl.to('#tk27', {{ backgroundColor: '#FF4438', duration: 0.01 }}, {t['st'] + 0.7:.3f});
{reveal('#c5', t['c5'], 18, 0.35)}"""
    for key, k in [('c1', 'click'), ('c2', 'click'), ('c3', 'click'), ('c4', 'pop'), ('st', 'impact'), ('c5', 'click')]:
        sfx(3, t[key], k)
    sfx(3, 0.05, 'whoosh')
    return frame('03-facts', 3, css, body, anim, 'cc')


# ======================= FRAME 4 — DATA =======================
def f4():
    css = """
    .d-kick { position: absolute; left: 60px; top: 330px; }
    .d-sub { position: absolute; left: 60px; right: 60px; top: 392px; font-weight: 700; font-size: 38px; color: rgba(255,255,255,0.85); opacity: 0; }
    .d-qmark { position: absolute; left: 20px; top: 360px; font-weight: 900; font-size: 760px; line-height: 1; color: #FF5A1F; opacity: 0; }
    .d-num { position: absolute; left: 0; right: 0; top: 440px; text-align: center; font-weight: 900; font-size: 560px; line-height: 1; letter-spacing: -0.04em; color: #FF5A1F; opacity: 0; text-shadow: 0 0 60px rgba(255,90,31,0.35); }
    .d-ul { position: absolute; left: 150px; top: 960px; width: 780px; height: 40px; opacity: 0; }
    .d-unit { position: absolute; left: 0; right: 0; top: 1000px; text-align: center; font-weight: 900; font-size: 96px; letter-spacing: 0.3em; color: #fff; opacity: 0; padding-left: 0.3em; }
    .d-stub { position: absolute; left: 60px; right: 60px; top: 1150px; height: 110px; display: flex; align-items: center; justify-content: space-between; padding: 0 34px; opacity: 0; }
    .d-stub .l { font-weight: 800; font-size: 26px; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.6); }
    .d-stub .r { font-weight: 900; font-size: 44px; color: #fff; } .d-stub .r em { font-style: normal; color: #FF5A1F; }
    .d-tally { position: absolute; left: 60px; right: 60px; top: 1290px; height: 190px; padding: 26px 34px 0; opacity: 0; }
    .d-tally .t1 { font-weight: 800; font-size: 28px; color: #fff; margin-bottom: 18px; } .d-tally .t1 em { font-style: normal; color: #FF5A1F; }
    .d-sq { display: flex; gap: 12px; }
    .d-sq i { display: block; flex: 1; height: 76px; border-radius: 10px; background: #FF5A1F; opacity: 0; }
    .d-sq i.draw { background: transparent; border: 4px solid rgba(255,255,255,0.85); }
    """
    sq = ''.join(f'<i id="sq{k}"></i>' for k in range(1, 10)) + '<i class="draw" id="sq10"></i>'
    body = f"""
    <div class="kick d-kick" id="d-kick"><i></i><b>Lần gần nhất Malaysia thắng Việt Nam</b></div>
    <div class="d-qmark" id="d-q" data-layout-allow-overlap="">”</div>
    <div class="d-num" id="d-num" data-layout-allow-overlap="">12</div>
    <svg class="d-ul" id="d-ul" viewBox="0 0 780 40"><path id="d-ulp" d="M6 26 C 120 6, 240 34, 380 16 S 640 8, 774 22" fill="none" stroke="#FF5A1F" stroke-width="8" stroke-linecap="round" stroke-dasharray="800" stroke-dashoffset="800"/></svg>
    <div class="d-unit" id="d-unit">NĂM</div>
    <div class="paper hot d-stub" id="d-stub"><span class="l">Mỹ Đình · 2014</span><span class="r">Malaysia <em>4–2</em> Việt Nam</span></div>
    <div class="paper d-tally" id="d-tally"><div class="t1">Từ đó đến nay: <em>9 thua</em> · 1 hòa</div><div class="d-sq">{sq}</div></div>"""
    t_n = 0.25
    t_stub = wt(4, 'bốn hai')
    t_tal = wt(4, 'Từ đó')
    t_thua = wt(4, 'thua')
    t_hoa = wt(4, 'hòa')
    anim = f"""
    tl.fromTo('#d-kick', {{ autoAlpha: 0, x: -20 }}, {{ autoAlpha: 1, x: 0, duration: 0.4, ease: 'power2.out' }}, 0.05);
    tl.fromTo('#d-q', {{ autoAlpha: 0, scale: 0.85 }}, {{ autoAlpha: 0.08, scale: 1, duration: 0.9, ease: 'power2.out' }}, 0.1);
    tl.fromTo('#d-num', {{ autoAlpha: 0, scale: 0.88 }}, {{ autoAlpha: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }}, {t_n});
    const cnt = {{ v: 0 }};
    tl.to(cnt, {{ v: 12, duration: 0.75, ease: 'power2.out', onUpdate: function () {{ document.getElementById('d-num').textContent = Math.round(cnt.v); }} }}, {t_n});
    tl.fromTo('#d-ul', {{ autoAlpha: 0 }}, {{ autoAlpha: 1, duration: 0.05 }}, {t_n + 0.7:.3f});
    tl.to('#d-ulp', {{ strokeDashoffset: 0, duration: 0.6, ease: 'power2.inOut' }}, {t_n + 0.7:.3f});
    tl.fromTo('#d-unit', {{ autoAlpha: 0, y: 24 }}, {{ autoAlpha: 1, y: 0, duration: 0.45, ease: 'power3.out' }}, {t_n + 0.95:.3f});
{reveal('#d-stub', t_stub - 0.1, 30, 0.45)}
{reveal('#d-tally', t_tal - 0.1, 30, 0.45)}
    tl.fromTo('#d-tally .d-sq i:not(.draw)', {{ autoAlpha: 0, scale: 0.4 }}, {{ autoAlpha: 1, scale: 1, duration: 0.25, ease: 'back.out(2)', stagger: {{ each: {(t_hoa - t_thua - 0.2) / 9:.3f}, from: 'start' }} }}, {t_thua:.3f});
    tl.fromTo('#sq10', {{ autoAlpha: 0, scale: 0.4 }}, {{ autoAlpha: 1, scale: 1, duration: 0.3, ease: 'back.out(2)' }}, {t_hoa:.3f});"""
    for t, k in [(0.1, 'whoosh'), (t_n + 0.05, 'impact'), (t_stub, 'click'), (t_tal, 'click'), (t_hoa, 'pop')]:
        sfx(4, t, k)
    return frame('04-data', 4, css, body, anim, 'dc')


# ======================= FRAME 5 — CONTEXT =======================
def f5():
    css = """
    .q1 { left: 70px; top: 320px; width: 940px; height: 330px; padding: 26px 40px; display: flex; align-items: center; gap: 36px; }
    .q1 .big { font-weight: 900; font-size: 196px; line-height: 1; color: #FF5A1F; letter-spacing: -0.04em; white-space: nowrap; }
    .q1 .tx { font-weight: 700; font-size: 34px; line-height: 1.3; color: #fff; }
    .q1 .tx b { display: block; margin-bottom: 8px; font-weight: 800; font-size: 22px; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.6); }
    .q2 { left: 60px; top: 690px; width: 930px; height: 330px; padding: 30px 44px 0 48px; }
    .q2 .who { display: flex; align-items: center; gap: 14px; }
    .q2 .stat { margin-top: 26px; font-weight: 900; font-size: 56px; line-height: 1.18; }
    .q2 .stat em { font-style: normal; color: #FF5A1F; }
    .q2 .src { margin-top: 20px; font-weight: 600; font-size: 24px; color: rgba(255,255,255,0.6); }
    .q3 { left: 80px; top: 1060px; width: 930px; height: 390px; padding: 30px 44px 0 52px; }
    .q3 .qm { position: absolute; left: 24px; top: -40px; font-weight: 900; font-size: 300px; line-height: 1; color: #FF5A1F; opacity: 0.22; }
    .q3 .who { position: relative; display: flex; align-items: center; gap: 14px; }
    .q3 .qt { position: relative; margin-top: 22px; font-weight: 800; font-size: 50px; line-height: 1.22; }
    .q3 .qt em { font-style: normal; color: #FF5A1F; }
    .q3 .src { position: relative; margin-top: 18px; font-weight: 600; font-size: 24px; color: rgba(255,255,255,0.6); }
    """
    body = """
    <div class="paper hot q1" id="q1"><div class="tape"></div>
      <div class="big">4–0</div>
      <div class="tx"><b>Lần gặp trước</b>Việt Nam thắng Malaysia tổng tỷ số hai lượt bán kết ASEAN Cup 2026</div>
    </div>
    <div class="paper warn q2" id="q2">
      <div class="who"><span class="lab r">HLV Kim Sang-sik thừa nhận</span></div>
      <div class="stat">Lần này đối thủ có lực lượng <em>tốt hơn, mạnh hơn rất nhiều</em></div>
      <div class="src">Chú ý đặc biệt tới tiền đạo Bergson da Silva</div>
    </div>
    <div class="paper hot q3" id="q3"><div class="tape"></div><div class="qm" data-layout-allow-overlap="">“</div>
      <div class="who"><span class="lab">HLV Tan Cheng Hoe · Malaysia</span></div>
      <div class="qt">Tôi rất muốn <em>đánh bại Việt Nam</em>. Chúng tôi đã không thắng họ hơn 10 năm qua.</div>
      <div class="src">Nguồn: VnExpress</div>
    </div>"""
    t_b = wt(5, 'Huấn luyện viên', 1)
    t_c = wt(5, 'huấn luyện viên', 2)
    anim = f"""
{reveal('#q1', 0.2, 50, 0.55, rot=(-3, -1.0))}
{reveal('#q2', t_b - 0.1, 50, 0.55, rot=(3, 0.8))}
{reveal('#q3', t_c - 0.1, 50, 0.55, rot=(-3, -1.3))}"""
    for t, k in [(0.1, 'whoosh'), (0.25, 'impact'), (t_b, 'click'), (t_c, 'click')]:
        sfx(5, t, k)
    return frame('05-context', 5, css, body, anim, 'ec')


# ======================= FRAME 6 — IMPACT =======================
def f6():
    css = """
    .i1 { left: 60px; top: 320px; width: 900px; height: 330px; padding: 30px 40px 0 46px; }
    .i2 { left: 120px; top: 640px; width: 900px; height: 280px; padding: 28px 40px 0 46px; z-index: 2; }
    .i-row { display: flex; align-items: center; gap: 18px; margin-top: 20px; font-weight: 800; font-size: 40px; line-height: 1.15; opacity: 0; }
    .i-row .d { width: 16px; height: 16px; border-radius: 50%; background: #FF4438; flex: none; }
    .i-row.o .d { background: #FF5A1F; }
    .i-row small { display: block; margin-top: 4px; font-weight: 600; font-size: 24px; color: rgba(255,255,255,0.65); }
    .i3 { left: 60px; top: 980px; width: 960px; height: 480px; padding: 28px 40px 0 44px; z-index: 1; }
    .h-plot { position: absolute; left: 44px; right: 40px; top: 96px; height: 380px; }
    .h-grid { position: absolute; left: 0; right: 0; border-top: 1.5px dashed rgba(255,255,255,0.25); }
    .h-grid span { position: absolute; right: 0; top: -30px; font-weight: 600; font-size: 21px; color: rgba(255,255,255,0.6); }
    .h-bars { position: absolute; left: 0; right: 120px; bottom: 36px; height: 300px; display: flex; align-items: flex-end; justify-content: space-between; gap: 22px; }
    .h-bar { position: relative; flex: 1; border-radius: 10px 10px 0 0; background: rgba(255,255,255,0.78); transform-origin: bottom; opacity: 0; }
    .h-bar.o { background: #FF5A1F; box-shadow: 0 0 28px rgba(255,90,31,0.45); }
    .h-bar .v { position: absolute; left: 0; right: 0; top: -40px; text-align: center; font-weight: 900; font-size: 32px; color: #fff; }
    .h-bar.o .v { color: #FF5A1F; }
    .h-names { position: absolute; left: 0; right: 120px; bottom: 0; height: 36px; display: flex; justify-content: space-between; gap: 22px; }
    .h-names span { flex: 1; text-align: center; font-weight: 700; font-size: 17px; line-height: 1.1; color: rgba(255,255,255,0.75); }
    """
    # chiều cao thanh: (h - 1.70) / 0.20 * 300
    def hb(h):
        return round((h - 1.70) / 0.20 * 280 + 20)
    body = f"""
    <div class="paper warn i1" id="i1"><div class="tape"></div>
      <span class="lab r">Việt Nam thiếu quân</span>
      <div class="i-row" id="i1a"><span class="d"></span><span>Hoàng Hên<small>không kịp hồi phục</small></span></div>
      <div class="i-row" id="i1b"><span class="d"></span><span>Việt Anh<small>chấn thương cơ đùi sau</small></span></div>
    </div>
    <div class="paper hot i2" id="i2">
      <span class="lab">Malaysia cũng vắng</span>
      <div class="i-row o" id="i2a"><span class="d"></span><span>Dion Cools<small>đội trưởng</small></span></div>
      <div class="i-row o" id="i2b"><span class="d"></span><span>Faisal Halim</span></div>
    </div>
    <div class="paper i3" id="i3">
      <div class="f-lab" style="display:flex;justify-content:space-between"><span class="lab">Chiều cao (tính từ mốc 1m70)</span><span class="lab d">Dân Trí</span></div>
      <div class="h-plot">
        <div class="h-grid" style="top:{380 - 36 - round(0.10 / 0.20 * 280 + 20) + 0}px"><span>1m80</span></div>
        <div class="h-grid" style="top:{380 - 36 - round(0.20 / 0.20 * 280 + 20) + 0}px"><span>1m90</span></div>
        <div class="h-bars">
          <div class="h-bar o" id="hb1" style="height:{hb(1.85)}px"><div class="v">1m85</div></div>
          <div class="h-bar" id="hb2" style="height:{hb(1.86)}px"><div class="v">1m86</div></div>
          <div class="h-bar" id="hb3" style="height:{hb(1.83)}px"><div class="v">1m83</div></div>
          <div class="h-bar" id="hb4" style="height:{hb(1.80)}px"><div class="v">1m80</div></div>
        </div>
        <div class="h-names"><span>Việt Anh<br>(hậu vệ VN)</span><span>Tierney<br>(Malaysia)</span><span>Paulo Josue<br>(Malaysia)</span><span>Bergson<br>(Malaysia)</span></div>
      </div>
    </div>"""
    t = {k: wt(6, v) for k, v in dict(a='Hoàng', b='Việt Anh', mal='Malaysia', ch='cao một mét').items()}
    t_b2 = wt(6, 'Dion')
    t_b3 = wt(6, 'Faisal')
    anim = f"""
{reveal('#i1', 0.15, 50, 0.55, rot=(-3, -1.0))}
{reveal('#i1a', t['a'], 14, 0.35)}
{reveal('#i1b', wt(6, 'Việt Anh', 1) + 0.0, 14, 0.35)}
{reveal('#i3', t['ch'] - 0.9, 50, 0.55, rot=(2, 0.4))}
    tl.fromTo('.h-bar', {{ autoAlpha: 0, scaleY: 0 }}, {{ autoAlpha: 1, scaleY: 1, duration: 0.5, ease: 'back.out(1.3)', stagger: 0.12 }}, {t['ch'] - 0.2:.3f});
{reveal('#i2', t['mal'] - 0.1, 50, 0.55, rot=(3, 1.0))}
{reveal('#i2a', t_b2, 14, 0.35)}
{reveal('#i2b', t_b3, 14, 0.35)}"""
    for tt, k in [(0.1, 'whoosh'), (t['a'], 'click'), (wt(6, 'Việt Anh', 1), 'click'), (t['ch'] - 0.2, 'pop'), (t['mal'], 'click'), (t_b2, 'click'), (t_b3, 'click')]:
        sfx(6, tt, k)
    return frame('06-impact', 6, css, body, anim, 'fc')


# ======================= FRAME 7 — CTA =======================
def f7():
    css = """
    .ct-wrap { position: absolute; left: 60px; right: 60px; top: 390px; text-align: center; }
    .ct-kick { font-weight: 800; font-size: 26px; letter-spacing: 0.26em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .ct-head { margin-top: 28px; font-weight: 900; font-size: 88px; line-height: 1.12; color: #fff; }
    .ct-head .ln { overflow: hidden; } .ct-head .ln > span { display: block; }
    .ct-head em { font-style: normal; color: #FF5A1F; }
    .ct-opts { display: flex; justify-content: center; align-items: stretch; gap: 18px; margin-top: 80px; }
    .ct-opt { flex: 1; max-width: 420px; padding: 58px 22px; border-radius: 22px; border: 2.5px solid; opacity: 0; }
    .ct-opt.up { border-color: rgba(255,90,31,0.85); background: rgba(255,90,31,0.1); }
    .ct-opt.down { border-color: rgba(255,68,56,0.85); background: rgba(255,68,56,0.1); }
    .ct-opt .emo { width: 72px; height: 72px; transform: scale(1.25); margin: 0 auto; position: relative; }
    .ct-opt.up .emo::before { content: ""; position: absolute; left: 50%; top: 0; width: 0; height: 0; border-left: 28px solid transparent; border-right: 28px solid transparent; border-bottom: 30px solid #FF5A1F; transform: translateX(-50%); }
    .ct-opt.up .emo::after { content: ""; position: absolute; left: 50%; top: 30px; width: 22px; height: 26px; background: #FF5A1F; transform: translateX(-50%); }
    .ct-opt.down .emo::before { content: ""; position: absolute; left: 0; bottom: 0; width: 0; height: 0; border-left: 28px solid transparent; border-right: 28px solid transparent; border-bottom: 50px solid #FF4438; }
    .ct-opt.down .emo::after { content: "!"; position: absolute; left: 0; right: 0; bottom: -2px; text-align: center; font-weight: 900; font-size: 30px; color: #0B0E14; }
    .ct-opt .lab2 { margin-top: 30px; font-weight: 800; font-size: 40px; line-height: 1.2; color: #fff; }
    .ct-vs { display: flex; align-items: center; font-weight: 900; font-size: 34px; color: rgba(255,255,255,0.4); opacity: 0; }
    .ct-cta { display: inline-flex; align-items: center; gap: 18px; margin-top: 90px; padding: 28px 46px; border-radius: 100px; background: #FF5A1F; opacity: 0; }
    .ct-cta .ico { width: 42px; height: 42px; flex: none; border-radius: 12px 12px 12px 4px; background: #fff; position: relative; }
    .ct-cta .ico::before { content: ""; position: absolute; left: 10px; top: 13px; right: 10px; height: 4px; border-radius: 2px; background: #FF5A1F; box-shadow: 0 9px 0 #FF5A1F; }
    .ct-cta span { font-weight: 800; font-size: 36px; color: #0B0E14; }
    .ct-sign { position: absolute; left: 0; right: 0; top: 1400px; display: flex; align-items: center; justify-content: center; gap: 12px; opacity: 0; }
    .ct-sign .m { width: 44px; height: 44px; }
    .ct-sign .w2 { font-weight: 800; font-size: 30px; color: rgba(255,255,255,0.88); }
    """
    body = """
    <div class="ct-wrap">
      <div class="ct-kick" id="ct-kick">Góc nhìn của bạn</div>
      <div class="ct-head">
        <div class="ln"><span id="ct-h1">12 năm chưa thắng:</span></div>
        <div class="ln"><span id="ct-h2"><em>giữ mạch thắng</em> hay phá dớp?</span></div>
      </div>
      <div class="ct-opts">
        <div class="ct-opt up" id="ct-o1"><div class="emo"></div><div class="lab2">Việt Nam giữ vững mạch thắng</div></div>
        <div class="ct-vs" id="ct-vs">VS</div>
        <div class="ct-opt down" id="ct-o2"><div class="emo"></div><div class="lab2">Malaysia phá dớp</div></div>
      </div>
      <div class="ct-cta" id="ct-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="ct-sign" id="ct-sign"><img class="m" src="public/logo.png" alt=""><span class="w2">Tin Tức Số</span></div>"""
    t_o1 = wt(7, 'bạn nghiêng')
    t_vs = wt(7, 'hay')
    t_o2 = wt(7, 'Malaysia')
    t_cta = wt(7, 'Hãy')
    anim = f"""
    tl.fromTo('#ct-kick', {{ autoAlpha: 0, y: -12 }}, {{ autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }}, 0);
    tl.fromTo('#ct-h1', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.55, ease: 'power4.out' }}, 0.2);
    tl.fromTo('#ct-h2', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.55, ease: 'power4.out' }}, 0.36);
    tl.fromTo('#ct-o1', {{ autoAlpha: 0, y: 28, scale: 0.92 }}, {{ autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }}, {t_o1:.3f});
    tl.fromTo('#ct-vs', {{ autoAlpha: 0, scale: 0.5 }}, {{ autoAlpha: 1, scale: 1, duration: 0.3, ease: 'back.out(2)' }}, {t_vs:.3f});
    tl.fromTo('#ct-o2', {{ autoAlpha: 0, y: 28, scale: 0.92 }}, {{ autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }}, {t_o2:.3f});
    tl.fromTo('#ct-cta', {{ autoAlpha: 0, y: 22 }}, {{ autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out' }}, {t_cta:.3f});
    tl.fromTo('#ct-cta', {{ scale: 1 }}, {{ scale: 1.04, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }}, {t_cta + 0.5:.3f});
    tl.fromTo('#ct-sign', {{ autoAlpha: 0 }}, {{ autoAlpha: 1, duration: 0.4 }}, {t_cta + 0.3:.3f});"""
    for t, k in [(0.1, 'whoosh'), (t_o1, 'pop'), (t_o2, 'pop'), (t_cta + 0.05, 'chime')]:
        sfx(7, t, k)
    return frame('07-cta', 7, css, body, anim, 'gc')


FRAMES = [
    ('01-hook', f1), ('02-what', f2), ('03-facts', f3), ('04-data', f4),
    ('05-context', f5), ('06-impact', f6), ('07-cta', f7),
]
os.makedirs('compositions/frames', exist_ok=True)
for fid, fn in FRAMES:
    open(f'compositions/frames/{fid}.html', 'w', encoding='utf-8').write(fn())

# ---------- index.html ----------
SFX_FILE = {'pop': ('pop.mp3', 0.5, 0.30), 'click': ('click-soft.mp3', 0.37, 0.32), 'whoosh': ('whoosh-short.mp3', 0.5, 0.30),
            'impact': ('impact-bass-1.mp3', 0.5, 0.35), 'chime': ('chime.mp3', 0.5, 0.30)}
sfx_html = []
for n, (t0, kind) in enumerate(sorted(SFX), 1):
    f, d, v = SFX_FILE[kind]
    sfx_html.append(f'      <audio id="el-sfx-{n}" src="assets/sfx/{f}" data-start="{max(t0, 0):.3f}" data-duration="{d}" data-track-index="{30 + n % 4}" data-volume="{v}"></audio>')
scene_html = '\n'.join(
    f'      <div id="el-{fid}" class="scene clip" data-composition-id="{fid}" data-composition-src="compositions/frames/{fid}.html" data-start="{START[i]}" data-duration="{DUR[i]}" data-track-index="1"></div>'
    for i, (fid, _) in enumerate(FRAMES, 1))
voice_html = '\n'.join(
    f'      <audio id="el-voice-{i}" src="assets/voice/line{i}.mp3" data-start="{START[i]}" data-duration="{round(VOICE[i], 3)}" data-track-index="10" data-audio-group="voiceover"></audio>'
    for i in range(1, 8))
bgm_exists = os.path.exists('assets/bgm/bgm-final.wav')
bgm_html = (f'      <audio id="el-bgm" src="assets/bgm/bgm-final.wav" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"></audio>'
            if bgm_exists else '')
INDEX = f"""<!DOCTYPE html>
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
      .scene {{ position: absolute; inset: 0; width: 100%; height: 100%; }}

      #bg-depth {{ position: absolute; inset: 0; overflow: hidden; z-index: 0; }}
      #bg-depth .blob {{ position: absolute; border-radius: 50%; filter: blur(60px); }}
      #bg-depth .blob-1 {{ width: 640px; height: 640px; background: radial-gradient(circle, rgba(255,90,31,0.20), transparent 70%); top: -120px; left: -160px; }}
      #bg-depth .blob-2 {{ width: 560px; height: 560px; background: radial-gradient(circle, rgba(255,68,56,0.16), transparent 70%); top: 900px; right: -200px; }}
      #bg-depth .blob-3 {{ width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,90,31,0.12), transparent 70%); bottom: -180px; left: 200px; }}
      #bg-stars circle {{ fill: #fff; }}

      #brand-anchor {{ position: absolute; inset: 0; z-index: 90; pointer-events: none; opacity: 0; }}
      #ba-source {{ position: absolute; left: 44px; top: 46px; display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px; border-radius: 8px; background: rgba(11,14,20,0.6); border: 1px solid rgba(255,255,255,0.12); }}
      #ba-source .dot {{ width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; flex: none; }}
      #ba-source span {{ font-weight: 500; font-size: 21px; letter-spacing: 0.02em; color: rgba(255,255,255,0.9); white-space: nowrap; }}
      #ba-brand {{ position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }}
      #ba-brand .mark {{ width: 44px; height: 44px; flex: none; }}
      #ba-brand .mark img {{ display: block; width: 100%; height: 100%; }}
      #ba-brand .word {{ font-weight: 800; font-size: 24px; letter-spacing: 0.01em; color: #fff; }}
    </style>
  </head>
  <body>
    <!-- Kênh "Tin Tức Số" — cam #FF5A1F trên #0B0E14. Style dựng: 9-editorial-clipping (index 8).
         data-duration mỗi frame = độ dài voice thật + đệm 0.4s (CTA +0.85s). Tổng = {TOTAL}s. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">

      <div id="bg-depth" data-layout-allow-overflow="">
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
        <div class="blob blob-3"></div>
        <svg id="bg-stars" viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:100%;height:100%;"></svg>
      </div>

{scene_html}

      <div id="brand-anchor">
        <div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress</span></div>
        <div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div>
      </div>

{voice_html}

{chr(10).join(sfx_html)}

{bgm_html}
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};

      function mulberry32(seed) {{
        return function () {{
          seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
          var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
          t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
          return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
        }};
      }}
      var rand = mulberry32(20261004133);
      var starsSvg = document.getElementById('bg-stars');
      var starEls = [];
      for (var i = 0; i < 40; i++) {{
        var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        c.setAttribute('cx', (rand() * 1080).toFixed(1));
        c.setAttribute('cy', (rand() * 1920).toFixed(1));
        c.setAttribute('r', (1.5 + rand() * 1.5).toFixed(2));
        c.setAttribute('opacity', (0.15 + rand() * 0.25).toFixed(2));
        starsSvg.appendChild(c);
        starEls.push(c);
      }}

      const tl = gsap.timeline({{ paused: true }});
      tl.to('.blob', {{ x: '+=40', y: '-=30', duration: 18, ease: 'sine.inOut', repeat: -1, yoyo: true, stagger: 3 }}, 0);
      tl.to(starEls, {{ opacity: '+=0.25', duration: 4, ease: 'sine.inOut', repeat: -1, yoyo: true, stagger: {{ each: 0.15, from: 'random' }} }}, 0);
      tl.set('#brand-anchor', {{ opacity: 1 }}, {DUR[1]});
      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(INDEX)
json.dump({'START': START, 'DUR': DUR, 'TOTAL': TOTAL}, open('/tmp/vb/timing.json', 'w'))
print('TOTAL', TOTAL, 'START', START, 'sfx', len(SFX))
