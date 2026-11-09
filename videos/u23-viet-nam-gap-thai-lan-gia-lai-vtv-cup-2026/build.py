#!/usr/bin/env python3
"""Sinh index.html + compositions/frames/*.html (style 3 split-comparison) từ SCRIPT.md + assets/voice/*.mp3."""
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from align import align_line

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)
LINES = open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')
assert len(LINES) == 7
PAD, CTA_PAD = 0.4, 0.85
ALIGN, VOICE = {}, {}
for i, l in enumerate(LINES, 1):
    ALIGN[i], VOICE[i] = align_line(l, i)
DUR = {i: round(VOICE[i] + (CTA_PAD if i == 7 else PAD), 3) for i in range(1, 8)}
START, t = {}, 0.0
for i in range(1, 8):
    START[i] = round(t, 3)
    t += DUR[i]
TOTAL = round(t, 3)
DISPLAY = {'U': 'U'}


def norm(w):
    return re.sub(r'[^\w\-]', '', w.lower())


def wt(line, phrase, nth=1):
    toks = [norm(x) for x in phrase.split()]
    ws = [norm(x['w']) for x in ALIGN[line]]
    c = 0
    for k in range(len(ws) - len(toks) + 1):
        if ws[k:k + len(toks)] == toks:
            c += 1
            if c == nth:
                return ALIGN[line][k]['s']
    raise KeyError(f'{line}:{phrase}')


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
    .card { position: absolute; background: #121724; border: 1.5px solid rgba(255,255,255,0.14); border-radius: 14px; box-shadow: 0 18px 40px rgba(0,0,0,0.55), 0 0 40px rgba(255,90,31,0.12); opacity: 0; }
    .lab { font-weight: 800; font-size: 24px; letter-spacing: 0.16em; text-transform: uppercase; color: #FF5A1F; }
    .lab.d { color: rgba(255,255,255,0.6); } .lab.r { color: #FF4438; }
    em { font-style: normal; color: #FF5A1F; }
"""
SFX = []


def sfx(line, tt, kind='click'):
    SFX.append((round(START[line] + tt, 3), kind))


def caps(line, prefix):
    ws = ALIGN[line]
    chunks, cur = [], []
    for w in ws:
        cur.append(w)
        txt = ' '.join(x['w'] for x in cur)
        if (re.search(r'[,.:?]$', w['w']) and len(cur) >= 2) or len(cur) >= 5 or len(txt) >= 24:
            chunks.append(cur); cur = []
    if cur:
        if chunks and len(cur) == 1:
            chunks[-1].extend(cur)
        else:
            chunks.append(cur)
    html, js = [], []
    for ci, ch in enumerate(chunks, 1):
        cid = f'{prefix}{ci}'
        spans = ''.join(f'<span class="w" id="{cid}-w{k}">{x["w"]}</span>' for k, x in enumerate(ch, 1))
        html.append(f'      <div class="cap-chunk" id="{cid}">{spans}</div>')
        t0 = ch[0]['s']
        t_off = chunks[ci][0]['s'] if ci < len(chunks) else min(ch[-1]['e'] + 0.3, DUR[line] - 0.05)
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


def rev(sel, tt, y=24, dur=0.45, x=0, ease='power3.out'):
    return f"    tl.fromTo('{sel}', {{ autoAlpha: 0, y: {y}, x: {x} }}, {{ autoAlpha: 1, y: 0, x: 0, duration: {dur}, ease: '{ease}' }}, {tt:.3f});"


# ---------------- 1 HOOK ----------------
def f1():
    css = """
    .hk-photo { position: absolute; left: 0; right: 0; top: 0; height: 800px; overflow: hidden; background: #05070c; }
    .hk-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 42% 30%; }
    .hk-scrim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11,14,20,0.08) 0%, rgba(11,14,20,0.30) 58%, rgba(11,14,20,0.99) 100%); }
    .hk-panel { position: absolute; left: 0; right: 0; top: 800px; bottom: 0; padding: 36px 60px 0; display: flex; flex-direction: column; align-items: flex-start; }
    .hk-masthead { display: flex; align-items: center; gap: 13px; margin-bottom: 30px; opacity: 0; }
    .hk-logo { width: 56px; height: 56px; flex: none; } .hk-logo img { display: block; width: 100%; height: 100%; }
    .hk-mw { font-weight: 800; font-size: 32px; color: #fff; }
    .hk-badge { display: inline-flex; align-items: center; gap: 12px; padding: 8px 18px 8px 8px; border-radius: 100px; border: 1.5px solid rgba(255,90,31,0.85); background: rgba(255,90,31,0.1); margin-bottom: 30px; opacity: 0; }
    .hk-badge .ring { width: 30px; height: 30px; border-radius: 50%; border: 3px solid #FF5A1F; display: flex; align-items: center; justify-content: center; flex: none; }
    .hk-badge .ring .dot { width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; }
    .hk-badge span.lbl { font-weight: 500; font-size: 22px; color: #fff; white-space: nowrap; }
    .hk-name-wrap { overflow: hidden; }
    .hk-name { font-weight: 900; font-size: 104px; line-height: 1.17; letter-spacing: -0.02em; white-space: nowrap; }
    .hk-name.a { color: #fff; } .hk-name.b { color: #FF5A1F; }
    .hk-sub { margin-top: 20px; font-weight: 500; font-size: 30px; color: rgba(255,255,255,0.75); opacity: 0; }
    .hk-tags { display: flex; flex-direction: column; gap: 18px; margin-top: 34px; }
    .hk-tag { display: flex; align-items: center; font-weight: 800; font-size: 44px; line-height: 1.2; opacity: 0; }
    .hk-tag.warn { color: #FF4438; } .hk-tag.hot { color: #FF5A1F; }
    .hk-tag .dot { display: inline-block; width: 16px; height: 16px; border-radius: 50%; background: currentColor; margin-right: 18px; flex: none; }
    """
    body = """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="ring"><span class="dot"></span></span><span class="lbl">Nguồn: Dân Trí · 9/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name a" id="hk-name1">U23 VIỆT NAM</div></div>
      <div class="hk-name-wrap"><div class="hk-name b" id="hk-name2">U23 THÁI LAN</div></div>
      <div class="hk-sub" id="hk-sub">Mở màn giải tứ hùng Gia Lai · tối 10/11</div>
      <div class="hk-tags">
        <div class="hk-tag hot" id="hk-t1"><span class="dot"></span>Hai đội, hai mục tiêu</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Việt Nam vắng hai cầu thủ</div>
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
    SFX.append((round(0.9, 3), 'impact'))
    return frame('01-hook', 1, css, body, anim, 'ac')


# ---------------- 2 WHAT (chia dọc: trái ảnh | phải panel) ----------------
def f2():
    css = """
    .s-wrap { position: absolute; left: 0; right: 0; top: 330px; height: 1090px; }
    .s-photo { position: absolute; left: 0; top: 0; width: 470px; height: 1090px; overflow: hidden; opacity: 0; }
    .s-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 41% 50%; }
    .s-photo .credit { position: absolute; left: 14px; bottom: 14px; padding: 6px 14px; background: rgba(11,14,20,0.85); font-weight: 600; font-size: 20px; color: #fff; }
    .s-bar { position: absolute; left: 470px; top: 0; width: 5px; height: 1090px; background: #FF5A1F; transform-origin: top; box-shadow: 0 0 24px rgba(255,90,31,0.6); }
    .s-panel { position: absolute; left: 475px; top: 0; width: 605px; height: 1090px; background: #121724; padding: 46px 40px 0 44px; }
    .s-head .ln { overflow: hidden; } .s-head .ln > span { display: block; font-weight: 900; font-size: 64px; line-height: 1.16; }
    .s-head { margin-top: 34px; }
    .s-rows { margin-top: 50px; }
    .s-row { padding: 26px 0 24px; border-top: 1.5px solid rgba(255,255,255,0.14); opacity: 0; }
    .s-row:last-child { border-bottom: 1.5px solid rgba(255,255,255,0.14); }
    .s-row .k { font-weight: 800; font-size: 21px; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.55); margin-bottom: 8px; }
    .s-row .v { font-weight: 800; font-size: 38px; line-height: 1.2; color: #fff; }
    """
    body = """
    <div class="s-wrap">
      <div class="s-photo" id="s-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="credit">Ảnh: Dân Trí</div></div>
      <div class="s-bar" id="s-bar"></div>
      <div class="s-panel" id="s-panel">
        <div class="kick" id="s-kick"><i></i><b>Chuyện gì xảy ra</b></div>
        <div class="s-head">
          <div class="ln"><span id="s-h1">Mở màn giải</span></div>
          <div class="ln"><span id="s-h2">tứ hùng</span></div>
          <div class="ln"><span id="s-h3" style="color:#FF5A1F">Gia Lai 2026</span></div>
        </div>
        <div class="s-rows">
          <div class="s-row" id="s-r1"><div class="k">Trận đầu</div><div class="v">Việt Nam <em>vs</em> Thái Lan · tối 10/11</div></div>
          <div class="s-row" id="s-r2"><div class="k">Bốn đội dự giải</div><div class="v">Việt Nam · Thái Lan · Qatar · Singapore</div></div>
          <div class="s-row" id="s-r3"><div class="k">Danh sách Việt Nam</div><div class="v"><em>26</em> cầu thủ trong nước</div></div>
        </div>
      </div>
    </div>"""
    t1, t2, t3 = wt(2, 'Giải có bốn'), wt(2, 'Huấn luyện'), wt(2, 'hai mươi sáu')
    anim = f"""
    tl.fromTo('#s-photo', {{ autoAlpha: 0, x: -90 }}, {{ autoAlpha: 1, x: 0, duration: 0.7, ease: 'power3.out' }}, 0.05);
    tl.fromTo('#s-panel', {{ x: 120 }}, {{ x: 0, duration: 0.7, ease: 'power3.out' }}, 0.05);
    tl.fromTo('#s-bar', {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.7, ease: 'power2.inOut' }}, 0.1);
    tl.fromTo('#s-kick', {{ autoAlpha: 0, x: -20 }}, {{ autoAlpha: 1, x: 0, duration: 0.4 }}, 0.5);
    tl.fromTo('#s-h1', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.55, ease: 'power4.out' }}, 0.65);
    tl.fromTo('#s-h2', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.55, ease: 'power4.out' }}, 0.78);
    tl.fromTo('#s-h3', {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.55, ease: 'power4.out' }}, 0.91);
{rev('#s-r1', 0.3 + 1.0, 20, 0.4, 40)}
{rev('#s-r2', t1, 20, 0.4, 40)}
{rev('#s-r3', t3 - 0.2, 20, 0.4, 40)}
    tl.to('#s-photo img', {{ scale: 1.06, duration: 9, ease: 'sine.inOut' }}, 0.8);"""
    for tt, k in [(0.1, 'whoosh'), (1.3, 'click'), (t1, 'click'), (t3 - 0.2, 'pop')]:
        sfx(2, tt, k)
    return frame('02-what', 2, css, body, anim, 'bc')


# ---------------- 3 KEY FACTS (hàng chia đôi nhãn | giá trị) ----------------
def f3():
    css = """
    .k-rows { position: absolute; left: 60px; right: 60px; top: 330px; }
    .k-row { position: relative; display: flex; align-items: center; height: 262px; border-top: 1.5px solid rgba(255,255,255,0.14); opacity: 0; }
    .k-row:last-child { border-bottom: 1.5px solid rgba(255,255,255,0.14); }
    .k-row .l { width: 330px; flex: none; font-weight: 800; font-size: 26px; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(255,255,255,0.55); line-height: 1.35; }
    .k-row .div { width: 4px; height: 150px; background: #FF5A1F; margin: 0 40px 0 0; flex: none; transform-origin: center; }
    .k-row.warn .div { background: #FF4438; }
    .k-row .v { flex: 1; font-weight: 900; font-size: 48px; line-height: 1.2; text-align: right; }
    .k-row .v small { display: block; margin-top: 10px; font-weight: 600; font-size: 28px; color: rgba(255,255,255,0.7); }
    .k-row.warn .v b { color: #FF4438; } .k-row .v b { font-weight: 900; color: #FF5A1F; }
    """
    body = """
    <div class="k-rows">
      <div class="k-row warn" id="k1"><div class="l">Việt Nam<br>vắng mặt</div><div class="div"></div><div class="v"><b>Trần Thành Trung</b><br><b>Nguyễn Trọng Tuấn</b></div></div>
      <div class="k-row" id="k2"><div class="l">Cách xử lý</div><div class="div"></div><div class="v">Triệu tập gấp<small>người thay thế</small></div></div>
      <div class="k-row" id="k3"><div class="l">Thái Lan<br>mang theo</div><div class="div"></div><div class="v"><b>Nhiều cầu thủ trẻ</b><small>pha trộn gương mặt giàu kinh nghiệm</small></div></div>
      <div class="k-row warn" id="k4"><div class="l">HLV Thái Lan<br>có mặt</div><div class="div"></div><div class="v">Tối <b>9/11</b><small>tại Pleiku, do lịch bay</small></div></div>
    </div>"""
    t = dict(k1=wt(3, 'Thành Trung'), k2=wt(3, 'triệu tập gấp'), k3=wt(3, 'Phía Thái'), k4=wt(3, 'Pleiku') - 0.9)
    anim = ''.join(f"{rev('#' + k, v - 0.15, 24, 0.45, 50)}\n    tl.fromTo('#{k} .div', {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.4, ease: 'power2.out' }}, {v:.3f});\n" for k, v in t.items())
    for k, kind in zip(t, ['pop', 'click', 'click', 'pop']):
        sfx(3, t[k] - 0.1, kind)
    sfx(3, 0.05, 'whoosh')
    return frame('03-facts', 3, css, body, anim, 'cc')


# ---------------- 4 DATA (2 số cạnh nhau qua vạch vs) ----------------
def f4():
    css = """
    .d-kick { position: absolute; left: 60px; top: 330px; }
    .d-l { position: absolute; left: 40px; top: 520px; width: 300px; text-align: center; opacity: 0; }
    .d-l .n { font-weight: 900; font-size: 280px; line-height: 0.9; height: 260px; color: rgba(255,255,255,0.4); }
    .d-l .t { font-weight: 800; font-size: 32px; color: rgba(255,255,255,0.7); margin-top: 40px; }
    .d-vs { position: absolute; left: 340px; top: 470px; width: 80px; height: 480px; opacity: 0; }
    .d-vs i { position: absolute; left: 38px; top: 0; width: 4px; height: 480px; background: #FF5A1F; box-shadow: 0 0 22px rgba(255,90,31,0.7); }
    .d-vs b { position: absolute; left: 0; top: 200px; width: 80px; text-align: center; font-weight: 900; font-size: 34px; color: #fff; background: #0B0E14; padding: 8px 0; letter-spacing: 0.06em; }
    .d-r { position: absolute; left: 420px; top: 440px; width: 640px; text-align: center; opacity: 0; }
    .d-r .n { font-weight: 900; font-size: 420px; line-height: 0.9; height: 400px; letter-spacing: -0.04em; color: #FF5A1F; text-shadow: 0 0 60px rgba(255,90,31,0.35); }
    .d-r .t { font-weight: 800; font-size: 40px; color: #fff; margin-top: 40px; }
    .d-card { left: 60px; right: 60px; top: 1050px; height: 360px; padding: 30px 36px 0; }
    .d-card .t1 { font-weight: 800; font-size: 32px; margin-bottom: 26px; }
    .d-dots { display: flex; flex-wrap: wrap; gap: 14px 14px; }
    .d-dots i { display: block; width: 58px; height: 58px; border-radius: 50%; background: #FF5A1F; opacity: 0; }
    """
    dots = ''.join(f'<i></i>' for _ in range(26))
    body = f"""
    <div class="kick d-kick" id="d-kick"><i></i><b>Con số của trận mở màn</b></div>
    <div class="d-l" id="d-l"><div class="n" id="d-ln">4</div><div class="t">đội dự giải</div></div>
    <div class="d-vs" id="d-vs"><i></i><b>vs</b></div>
    <div class="d-r" id="d-r"><div class="n" id="d-rn">26</div><div class="t">cầu thủ Việt Nam</div></div>
    <div class="card d-card" id="d-card"><div class="t1">Tất cả đến từ <em>các câu lạc bộ trong nước</em></div><div class="d-dots" id="d-dots">{dots}</div></div>"""
    t_n, t_all = wt(4, 'Hai mươi sáu'), wt(4, 'Tất cả')
    anim = f"""
    tl.fromTo('#d-kick', {{ autoAlpha: 0, x: -20 }}, {{ autoAlpha: 1, x: 0, duration: 0.4 }}, 0.2);
    tl.fromTo('#d-l', {{ autoAlpha: 0, x: -60 }}, {{ autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }}, 0.3);
    tl.fromTo('#d-vs', {{ autoAlpha: 0, scaleY: 0 }}, {{ autoAlpha: 1, scaleY: 1, duration: 0.5, ease: 'power2.out' }}, 0.6);
    tl.fromTo('#d-r', {{ autoAlpha: 0, x: 60, scale: 0.9 }}, {{ autoAlpha: 1, x: 0, scale: 1, duration: 0.6, ease: 'back.out(1.5)' }}, {max(t_n - 0.1, 0.9):.3f});
    tl.to('#d-vs i', {{ opacity: 0.4, duration: 0.3, yoyo: true, repeat: 1 }}, {max(t_n - 0.1, 0.9) + 0.3:.3f});
    tl.fromTo('#d-card', {{ autoAlpha: 0, y: 40 }}, {{ autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }}, {t_all - 0.3:.3f});
    tl.fromTo('#d-dots i', {{ autoAlpha: 0, scale: 0.2 }}, {{ autoAlpha: 1, scale: 1, duration: 0.25, ease: 'back.out(2)', stagger: 0.045 }}, {t_all:.3f});"""
    for tt, k in [(0.3, 'whoosh'), (max(t_n - 0.1, 0.9), 'impact'), (t_all, 'pop')]:
        sfx(4, tt, k)
    return frame('04-data', 4, css, body, anim, 'dc')


# ---------------- 5 CONTEXT (bảng 2 cột đối xứng) ----------------
def f5():
    css = """
    .c-head { position: absolute; left: 0; right: 0; top: 330px; display: flex; }
    .c-head div { flex: 1; text-align: center; font-weight: 900; font-size: 44px; padding-bottom: 18px; border-bottom: 5px solid; opacity: 0; }
    .c-head .a { color: #FF5A1F; border-color: #FF5A1F; margin-left: 60px; margin-right: 8px; }
    .c-head .b { color: #fff; border-color: #fff; margin-right: 60px; margin-left: 8px; }
    .c-vline { position: absolute; left: 539px; top: 340px; width: 2px; height: 1070px; background: rgba(255,255,255,0.22); transform-origin: top; }
    .c-row { position: absolute; left: 0; right: 0; height: 300px; }
    .c-lab { position: absolute; left: 0; right: 0; top: 0; text-align: center; opacity: 0; }
    .c-lab span { display: inline-block; padding: 8px 20px; background: #0B0E14; font-weight: 800; font-size: 22px; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.6); position: relative; z-index: 2; }
    .c-cell { position: absolute; top: 60px; width: 450px; height: 220px; padding: 0 20px; display: flex; align-items: center; justify-content: center; text-align: center; font-weight: 800; font-size: 40px; line-height: 1.2; border-radius: 14px; background: #121724; border: 1.5px solid rgba(255,255,255,0.14); opacity: 0; }
    .c-cell.a { left: 60px; border-color: rgba(255,90,31,0.7); } .c-cell.a em { color: #FF5A1F; }
    .c-cell.b { right: 60px; }
    """
    rows = [(1, 'Giải này là', 'Dịp <em>tích lũy kinh nghiệm</em>', 'Bước chuẩn bị <em style="color:#fff;text-decoration:underline;text-decoration-color:#FF5A1F">đầu tiên</em>'),
            (2, 'Hướng tới', 'Năm <em>2027</em>: VCK U23 châu Á', 'Vòng loại <em style="color:#fff">U23 châu Á</em>'),
            (3, 'Xa hơn', '<em>Olympic</em>', 'Nhiều cầu thủ trẻ')]
    rh = ''
    for i, lab, a, b in rows:
        top = 400 + (i - 1) * 345
        rh += f'<div class="c-row" style="top:{top}px"><div class="c-lab" id="cl{i}"><span>{lab}</span></div><div class="c-cell a" id="ca{i}"><div>{a}</div></div><div class="c-cell b" id="cb{i}"><div>{b}</div></div></div>\n'
    body = f"""
    <div class="c-head"><div class="a" id="c-ha">VIỆT NAM</div><div class="b" id="c-hb">THÁI LAN</div></div>
    <div class="c-vline" id="c-vl" data-layout-allow-overlap=""></div>
    {rh}"""
    tHai = wt(5, 'Hai đội')
    tA = [wt(5, 'Việt Nam hướng') - 0.3, wt(5, 'hướng') , wt(5, 'Olympic') - 0.4]
    tB = [wt(5, 'coi') , wt(5, 'vòng loại'), wt(5, 'Olympic') + 0.9]
    anim = f"""
    tl.fromTo('#c-vl', {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.8, ease: 'power2.inOut' }}, 0.1);
    tl.fromTo('#c-ha', {{ autoAlpha: 0, x: -50 }}, {{ autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }}, 0.25);
    tl.fromTo('#c-hb', {{ autoAlpha: 0, x: 50 }}, {{ autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }}, 0.25);
"""
    for i in (1, 2, 3):
        ta, tb = tA[i - 1], tB[i - 1]
        ta = max(ta, 0.7 + (i - 1) * 0.4); tb = max(tb, ta + 0.35)
        anim += f"""    tl.fromTo('#cl{i}', {{ autoAlpha: 0 }}, {{ autoAlpha: 1, duration: 0.35 }}, {ta - 0.1:.3f});
    tl.fromTo('#ca{i}', {{ autoAlpha: 0, x: -140 }}, {{ autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }}, {ta:.3f});
    tl.fromTo('#cb{i}', {{ autoAlpha: 0, x: 140 }}, {{ autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }}, {tb:.3f});
"""
        sfx(5, ta, 'click'); sfx(5, tb, 'click')
    sfx(5, 0.1, 'whoosh')
    return frame('05-context', 5, css, body, anim, 'ec')


# ---------------- 6 IMPACT (chia đôi NGANG) ----------------
def f6():
    css = """
    .i-half { position: absolute; left: 60px; right: 60px; height: 520px; padding: 40px 44px 0; opacity: 0; }
    .i-top { top: 330px; border-left: 9px solid #FF5A1F; }
    .i-bot { top: 900px; }
    .i-h { font-weight: 900; font-size: 74px; line-height: 1.14; margin-top: 26px; }
    .i-s { margin-top: 26px; font-weight: 600; font-size: 34px; line-height: 1.3; color: rgba(255,255,255,0.78); }
    .i-div { position: absolute; left: 60px; width: 960px; top: 868px; height: 5px; background: #FF5A1F; transform-origin: left; box-shadow: 0 0 22px rgba(255,90,31,0.7); }
    .i-q { position: absolute; right: 50px; top: 340px; font-weight: 900; font-size: 360px; line-height: 1; color: #FF5A1F; opacity: 0; }
    """
    body = """
    <div class="i-q" id="i-q" data-layout-allow-overlap="">”</div>
    <div class="card i-half i-top" id="i-top"><div class="lab">Báo chí Thái Lan</div><div class="i-h" id="i-h1">Không quá kỳ vọng <em>thắng Việt Nam</em></div><div class="i-s">Lý do: đội nhà không có nhiều thời gian chuẩn bị</div></div>
    <div class="i-div" id="i-div"></div>
    <div class="card i-half i-bot" id="i-bot"><div class="lab">Lượt cuối của Việt Nam</div><div class="i-h">Gặp <em>U23 Qatar</em></div><div class="i-s">Giải tứ hùng Gia Lai 2026: Việt Nam, Thái Lan, Qatar, Singapore</div></div>"""
    t1, t2, t3 = wt(6, 'Báo chí'), wt(6, 'vì đội'), wt(6, 'lượt cuối') + 0.6
    anim = f"""
    tl.fromTo('#i-top', {{ autoAlpha: 0, y: -60 }}, {{ autoAlpha: 1, y: 0, duration: 0.6, ease: 'power3.out' }}, {max(t1, 0.1):.3f});
    tl.fromTo('#i-q', {{ autoAlpha: 0, scale: 0.8 }}, {{ autoAlpha: 0.14, scale: 1, duration: 0.8 }}, {max(t1, 0.1) + 0.3:.3f});
    tl.fromTo('#i-div', {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.6, ease: 'power2.inOut' }}, {t2 - 0.2:.3f});
    tl.fromTo('#i-bot', {{ autoAlpha: 0, y: 60 }}, {{ autoAlpha: 1, y: 0, duration: 0.6, ease: 'power3.out' }}, {t3 - 0.6:.3f});"""
    for tt, k in [(max(t1, 0.1), 'whoosh'), (t2, 'click'), (t3 - 0.6, 'pop')]:
        sfx(6, tt, k)
    return frame('06-impact', 6, css, body, anim, 'fc')


# ---------------- 7 CTA ----------------
def f7():
    css = """
    .z-q { position: absolute; left: 60px; right: 60px; top: 330px; text-align: center; }
    .z-q .big { font-weight: 900; font-size: 84px; line-height: 1.15; margin-top: 26px; }
    .z-q .kick { justify-content: center; }
    .z-opts { position: absolute; left: 60px; right: 60px; top: 770px; display: flex; gap: 24px; }
    .z-opt { flex: 1; height: 360px; border-radius: 18px; background: #121724; border: 2.5px solid rgba(255,255,255,0.2); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px; opacity: 0; }
    .z-opt.a { border-color: #FF5A1F; box-shadow: 0 0 40px rgba(255,90,31,0.25); }
    .z-opt .nm { font-weight: 900; font-size: 56px; text-align: center; line-height: 1.15; }
    .ico-up { width: 0; height: 0; border-left: 46px solid transparent; border-right: 46px solid transparent; border-bottom: 80px solid #FF5A1F; }
    .ico-ring { width: 84px; height: 84px; border-radius: 50%; border: 12px solid #fff; }
    .z-vs { position: absolute; left: 50%; top: 910px; margin-left: -38px; width: 76px; height: 76px; border-radius: 50%; background: #0B0E14; border: 2.5px solid #fff; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 28px; z-index: 3; opacity: 0; }
    .z-pill { position: absolute; left: 90px; right: 90px; top: 1210px; height: 112px; border-radius: 60px; background: #FF5A1F; color: #0B0E14; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 40px; opacity: 0; }
    .z-sig { position: absolute; left: 0; right: 0; top: 1360px; display: flex; align-items: center; justify-content: center; gap: 16px; opacity: 0; }
    .z-sig img { width: 64px; height: 64px; } .z-sig span { font-weight: 800; font-size: 36px; }
    """
    body = """
    <div class="z-q"><div class="kick" id="z-kick"><i></i><b>Bạn nghĩ sao?</b></div><div class="big" id="z-big">Trận mở màn:<br>bạn nghiêng về <em>đội nào</em>?</div></div>
    <div class="z-opts"><div class="z-opt a" id="z-a"><div class="ico-up"></div><div class="nm">Đội trẻ<br>Việt Nam</div></div><div class="z-opt" id="z-b"><div class="ico-ring"></div><div class="nm">Đội trẻ<br>Thái Lan</div></div></div>
    <div class="z-vs" id="z-vs">VS</div>
    <div class="z-pill" id="z-pill">Bình luận quan điểm của bạn</div>
    <div class="z-sig" id="z-sig"><img src="public/logo.png" alt=""><span>Tin Tức Số</span></div>"""
    tq, tn = wt(7, 'Hai mục'), wt(7, 'bạn nghiêng')
    anim = f"""
    tl.fromTo('#z-kick', {{ autoAlpha: 0 }}, {{ autoAlpha: 1, duration: 0.4 }}, 0.1);
    tl.fromTo('#z-big', {{ autoAlpha: 0, y: 30 }}, {{ autoAlpha: 1, y: 0, duration: 0.6, ease: 'power3.out' }}, 0.25);
    tl.fromTo('#z-a', {{ autoAlpha: 0, x: -80 }}, {{ autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }}, {tn:.3f});
    tl.fromTo('#z-b', {{ autoAlpha: 0, x: 80 }}, {{ autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }}, {tn:.3f});
    tl.fromTo('#z-vs', {{ autoAlpha: 0, scale: 0.4 }}, {{ autoAlpha: 1, scale: 1, duration: 0.4, ease: 'back.out(2)' }}, {tn + 0.35:.3f});
    tl.fromTo('#z-pill', {{ autoAlpha: 0, y: 30 }}, {{ autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }}, {wt(7, 'Hãy') - 0.1:.3f});
    tl.to('#z-pill', {{ scale: 1.04, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }}, {wt(7, 'Hãy') + 0.5:.3f});
    tl.fromTo('#z-sig', {{ autoAlpha: 0 }}, {{ autoAlpha: 1, duration: 0.5 }}, {DUR[7] - 2.2:.3f});"""
    for tt, k in [(0.1, 'whoosh'), (tn, 'pop'), (tn + 0.35, 'pop'), (DUR[7] - 2.2, 'chime')]:
        sfx(7, tt, k)
    return frame('07-cta', 7, css, body, anim, 'gc')


FR = [('01-hook', f1), ('02-what', f2), ('03-facts', f3), ('04-data', f4), ('05-context', f5), ('06-impact', f6), ('07-cta', f7)]
for name, fn in FR:
    open(f'compositions/frames/{name}.html', 'w', encoding='utf-8').write(fn())

SFXFILE = {'impact': ('impact-bass-1.mp3', 0.35), 'whoosh': ('whoosh-short.mp3', 0.3), 'click': ('click-soft.mp3', 0.32), 'pop': ('pop.mp3', 0.3), 'chime': ('chime.mp3', 0.3)}
scenes = '\n'.join(f'      <div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{START[i]}" data-duration="{DUR[i]}" data-track-index="1"></div>' for i, (n, _) in enumerate(FR, 1))
voices = '\n'.join(f'      <audio id="el-voice-{i}" src="assets/voice/line{i}.mp3" data-start="{START[i]}" data-duration="{round(VOICE[i],3)}" data-track-index="10" data-audio-group="voiceover"></audio>' for i in range(1, 8))
sfxs = '\n'.join(f'      <audio id="el-sfx-{k}" src="assets/sfx/{SFXFILE[kind][0]}" data-start="{tt:.3f}" data-duration="0.5" data-track-index="{30 + k % 4}" data-volume="{SFXFILE[kind][1]}"></audio>' for k, (tt, kind) in enumerate(sorted(SFX), 1))
idx = f"""<!DOCTYPE html>
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
      #ba-source span {{ font-weight: 500; font-size: 21px; color: rgba(255,255,255,0.9); white-space: nowrap; }}
      #ba-brand {{ position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }}
      #ba-brand .mark {{ width: 44px; height: 44px; flex: none; }} #ba-brand .mark img {{ display: block; width: 100%; height: 100%; }}
      #ba-brand .word {{ font-weight: 800; font-size: 24px; color: #fff; }}
    </style>
  </head>
  <body>
    <!-- Tin Tức Số — cam #FF5A1F / #0B0E14. Style 3: 4-split-comparison. Tổng {TOTAL}s. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="bg-depth" data-layout-allow-overflow="">
        <div class="blob blob-1"></div><div class="blob blob-2"></div><div class="blob blob-3"></div>
        <svg id="bg-stars" viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:100%;height:100%;"></svg>
      </div>
{scenes}
      <div id="brand-anchor">
        <div id="ba-source"><span class="dot"></span><span>Nguồn: Dân Trí</span></div>
        <div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div>
      </div>
{voices}
{sfxs}
      <audio id="el-bgm" src="assets/bgm/bgm-final.wav" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"></audio>
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
      var rand = mulberry32(20261109);
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
      tl.to('.blob', {{ x: '+=40', y: '-=30', duration: 18, ease: 'sine.inOut', repeat: 3, yoyo: true, stagger: 3 }}, 0);
      tl.to(starEls, {{ opacity: '+=0.25', duration: 4, ease: 'sine.inOut', repeat: 13, yoyo: true, stagger: {{ each: 0.15, from: 'random' }} }}, 0);
      tl.set('#brand-anchor', {{ opacity: 1 }}, {START[2]});
      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(idx)
print('TOTAL', TOTAL, START)
