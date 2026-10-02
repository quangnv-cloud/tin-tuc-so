#!/usr/bin/env python3
"""Generates compositions/frames/*.html + index.html for this video (style 0: Card & Bar)."""
import json, os, html, re
base = os.path.dirname(os.path.abspath(__file__))
caps = json.load(open(os.path.join(base, "assets/voice/captions.json"), encoding="utf-8"))
DUR = [4.75, 8.15, 7.30, 8.75, 9.20, 10.70, 7.20]
STARTS = []
t = 0.0
for d in DUR: STARTS.append(round(t, 2)); t += d
TOTAL = round(t, 2)

FONTS = "\n".join(
  f"    @font-face {{ font-family: 'Montserrat'; font-weight: {w}; src: url('assets/fonts/Montserrat-{w}-{sub}.woff2') format('woff2'); unicode-range: {ur}; }}"
  for w in (500, 600, 700, 800, 900)
  for sub, ur in (("latin", "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"),
                  ("vietnamese", "U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB")))

BASE_CSS = """
    #root { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: transparent; }
    .kcap-band { position: absolute; left: 90px; right: 90px; top: 128px; text-align: center; z-index: 12; pointer-events: none; }
    .kcap-chunk { position: absolute; left: 0; right: 0; top: 0; font-weight: 700; font-size: 32px; line-height: 1.35; opacity: 0; visibility: hidden; }
    .kcap-chunk .w { color: rgba(255,255,255,0.88); text-shadow: 0 2px 14px rgba(0,0,0,0.9), 0 1px 3px rgba(0,0,0,0.95); margin: 0 3px; }
"""

def cap_html_js(n, prefix):
    h, j = [], []
    for ci, ch in enumerate(caps[str(n)], 1):
        cid = f"{prefix}-{ci}"
        spans = " ".join(f'<span class="w" id="{cid}-w{wi}">{html.escape(w["text"])}</span>' for wi, w in enumerate(ch["words"], 1))
        h.append(f'      <div class="kcap-chunk" data-layout-allow-overlap="" id="{cid}">{spans}</div>')
        j.append(f"    tl.set('#{cid}', {{autoAlpha:0}}, 0);")
        j.append(f"    tl.to('#{cid}', {{autoAlpha:1, duration:0.12}}, {ch['fadein']});")
        j.append(f"    tl.to('#{cid}', {{autoAlpha:0, duration:0.12}}, {ch['fadeout']});")
        for wi, w in enumerate(ch["words"], 1):
            j.append(f"    tl.to('#{cid}-w{wi}', {{color:'#FF5A1F', duration:0.1}}, {w['start']});")
    return "\n".join(h), "\n".join(j)

def frame(n, name, css, body, js):
    ch, cj = cap_html_js(n, f"c{n}")
    out = f"""<template>
  <style>
{FONTS}
{BASE_CSS}
{css}
  </style>

  <div id="root" data-composition-id="{name}" data-width="1080" data-height="1920">
    <div class="kcap-band">
{ch}
    </div>
{body}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}

{cj}

    window.__timelines['{name}'] = tl;
  </script>
</template>
"""
    open(os.path.join(base, "compositions/frames", f"{name}.html"), "w", encoding="utf-8").write(out)

# ---------------------------------------------------------------- 01 HOOK
frame(1, "01-hook", """
    #root { background: #0B0E14; }
    .hk-photo { position: absolute; left: 0; right: 0; top: 0; height: 860px; overflow: hidden; background: #05070c; }
    .hk-photo img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 55%; }
    .hk-scrim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(11,14,20,0.35) 0%, rgba(11,14,20,0.25) 40%, #0B0E14 100%); }
    .hk-tint { position: absolute; inset: 0; background: radial-gradient(120% 70% at 80% 18%, rgba(255,90,31,0.16), transparent 58%); mix-blend-mode: screen; }
    .hk-masthead { position: absolute; left: 64px; top: 900px; display: flex; align-items: center; gap: 14px; opacity: 0; }
    .hk-logo { width: 56px; height: 56px; flex: none; }
    .hk-logo img { display: block; width: 100%; height: 100%; }
    .hk-mw { font-weight: 800; font-size: 32px; letter-spacing: 0.01em; color: #fff; }
    .hk-badge { position: absolute; left: 64px; top: 990px; display: inline-flex; align-items: center; gap: 10px; padding: 12px 20px; border-radius: 9px; border: 1.5px solid rgba(255,90,31,0.85); background: rgba(255,90,31,0.12); opacity: 0; }
    .hk-badge .d { width: 8px; height: 8px; border-radius: 50%; background: #FF5A1F; flex: none; }
    .hk-badge span { font-weight: 500; font-size: 23px; letter-spacing: 0.03em; color: #fff; white-space: nowrap; }
    .hk-title-wrap { position: absolute; left: 64px; right: 64px; top: 1092px; }
    .hk-title { font-weight: 900; font-size: 84px; line-height: 1.14; letter-spacing: -0.02em; color: #FF5A1F; white-space: nowrap; }
    .hk-title .row { overflow: hidden; }
    .hk-title .row > span { display: block; }
    .hk-title .row.w { color: #fff; }
    .hk-tags { position: absolute; left: 64px; right: 64px; top: 1430px; display: flex; flex-direction: column; gap: 24px; }
    .hk-tag { display: inline-flex; align-items: center; width: fit-content; font-weight: 800; font-size: 40px; line-height: 1; color: #fff; opacity: 0; }
    .hk-tag .dot { display: inline-block; width: 17px; height: 17px; border-radius: 50%; background: #FF5A1F; margin-right: 18px; flex: none; }
    .hk-tag.warn .dot { background: #FF4438; }
""", """
    <div class="hk-photo">
      <img src="assets/img/article-hero.jpg" alt="">
      <div class="hk-scrim"></div>
      <div class="hk-tint"></div>
    </div>
    <div class="hk-masthead" id="hk-mh">
      <div class="hk-logo"><img src="public/logo.png" alt=""></div>
      <div class="hk-mw">Tin Tức Số</div>
    </div>
    <div class="hk-badge" id="hk-badge"><span class="d"></span><span>Dân Trí &middot; 1/10/2026</span></div>
    <div class="hk-title-wrap">
      <div class="hk-title">
        <div class="row"><span id="hk-t1">Không khí lạnh</span></div>
        <div class="row w"><span id="hk-t2">tràn về miền Bắc</span></div>
      </div>
    </div>
    <div class="hk-tags">
      <div class="hk-tag" id="hk-g1"><span class="dot"></span>GIẢM TỚI 10&deg;C</div>
      <div class="hk-tag warn" id="hk-g2"><span class="dot"></span>MƯA DÔNG, GIÓ GIẬT</div>
    </div>
""", """
    tl.fromTo('.hk-photo', { autoAlpha: 0.5, scale: 1.1 }, { autoAlpha: 1, scale: 1, duration: 0.95, ease: 'power2.out' }, 0);
    tl.fromTo('#hk-mh', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.35);
    tl.fromTo('#hk-badge', { autoAlpha: 0, scale: 0.9 }, { autoAlpha: 1, scale: 1, duration: 0.36, ease: 'back.out(1.7)' }, 0.6);
    tl.fromTo('#hk-t1', { yPercent: 118 }, { yPercent: 0, duration: 0.6, ease: 'power4.out' }, 0.95);
    tl.fromTo('#hk-t2', { yPercent: 118 }, { yPercent: 0, duration: 0.6, ease: 'power4.out' }, 1.12);
    tl.fromTo('#hk-g1', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 1.85);
    tl.fromTo('#hk-g2', { autoAlpha: 0, x: -18 }, { autoAlpha: 1, x: 0, duration: 0.36, ease: 'power2.out' }, 2.1);
""")

# ---------------------------------------------------------------- 02 WHAT (card + panel)
frame(2, "02-what", """
    .wh-wrap { position: absolute; left: 60px; right: 60px; top: 300px; }
    .wh-card { position: relative; border-radius: 24px; overflow: hidden; background: #121724; box-shadow: 0 0 40px rgba(255,90,31,0.14); opacity: 0; }
    .wh-card img { display: block; width: 100%; height: 600px; object-fit: cover; object-position: 50% 55%; }
    .wh-card .fr { position: absolute; inset: 0; border-radius: 24px; border: 1px solid rgba(255,255,255,0.08); }
    .wh-panel { margin-top: 28px; padding: 40px 40px 44px; border-radius: 24px; background: #121724; border: 1px solid rgba(255,255,255,0.07); box-shadow: 0 0 40px rgba(255,90,31,0.10); opacity: 0; }
    .wh-kicker { font-weight: 700; font-size: 26px; letter-spacing: 0.22em; text-transform: uppercase; color: #FF5A1F; }
    .wh-head { margin-top: 22px; font-weight: 800; font-size: 54px; line-height: 1.28; color: #fff; }
    .wh-head .ln { overflow: hidden; }
    .wh-head .ln > span { display: block; opacity: 0; }
    .wh-head .hi { color: #FF5A1F; }
    .wh-sub { margin-top: 26px; font-weight: 500; font-size: 34px; line-height: 1.45; color: rgba(255,255,255,0.74); opacity: 0; }
""", """
    <div class="wh-wrap">
      <div class="wh-card" id="wh-card"><img src="assets/img/article-hero.jpg" alt=""><div class="fr"></div></div>
      <div class="wh-panel" id="wh-panel">
        <div class="wh-kicker">Chuyện gì xảy ra</div>
        <div class="wh-head">
          <div class="ln"><span id="wh-h1">Không khí lạnh <span class="hi">khá mạnh</span></span></div>
          <div class="ln"><span id="wh-h2">tràn xuống miền Bắc</span></div>
          <div class="ln"><span id="wh-h3">đêm 4 &ndash; rạng sáng <span class="hi">5/10</span></span></div>
        </div>
        <div class="wh-sub" id="wh-sub">Kéo theo mưa dông, theo Trung tâm Dự báo khí tượng thủy văn quốc gia.</div>
      </div>
    </div>
""", """
    tl.fromTo('#wh-card', { autoAlpha: 0, y: 30, scale: 0.97 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.55, ease: 'power3.out' }, 0);
    tl.fromTo('#wh-panel', { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 0.4);
    tl.fromTo('#wh-h1', { yPercent: 118 }, { yPercent: 0, autoAlpha: 1, duration: 0.5, ease: 'power4.out' }, 0.9);
    tl.fromTo('#wh-h2', { yPercent: 118 }, { yPercent: 0, autoAlpha: 1, duration: 0.5, ease: 'power4.out' }, 1.05);
    tl.fromTo('#wh-h3', { yPercent: 118 }, { yPercent: 0, autoAlpha: 1, duration: 0.5, ease: 'power4.out' }, 1.2);
    tl.fromTo('#wh-sub', { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power2.out' }, 1.7);
""")

# ---------------------------------------------------------------- 03 FACTS (numbered cards)
frame(3, "03-facts", """
    .fc-wrap { position: absolute; left: 64px; right: 64px; top: 300px; display: flex; flex-direction: column; gap: 36px; }
    .fc { position: relative; height: 360px; padding: 44px 44px 40px 132px; border-radius: 26px; background: #121724; border: 1px solid rgba(255,255,255,0.07); box-shadow: 0 0 40px rgba(255,90,31,0.10); opacity: 0; display: flex; flex-direction: column; justify-content: center; }
    .fc .no { position: absolute; left: 36px; top: 40px; font-weight: 900; font-size: 56px; line-height: 1; color: #FF5A1F; }
    .fc .lb { font-weight: 700; font-size: 26px; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(255,255,255,0.55); }
    .fc .vl { margin-top: 18px; font-weight: 800; font-size: 54px; line-height: 1.22; color: #fff; }
    .fc .vl .hi { color: #FF5A1F; }
    .fc.warn .no { color: #FF4438; }
    .fc.warn .vl .hi { color: #FF4438; }
""", """
    <div class="fc-wrap">
      <div class="fc" id="fc1"><div class="no">01</div><div class="lb">Thời điểm</div><div class="vl">Từ <span class="hi">chiều tối 4/10</span> đến <span class="hi">trưa 5/10</span></div></div>
      <div class="fc" id="fc2"><div class="no">02</div><div class="lb">Thời tiết Bắc Bộ</div><div class="vl">Mưa vừa, nơi <span class="hi">mưa to</span> và dông</div></div>
      <div class="fc warn" id="fc3"><div class="no">03</div><div class="lb">Chịu ảnh hưởng rõ rệt nhất</div><div class="vl">Khu vực <span class="hi">phía đông</span> Bắc Bộ</div></div>
    </div>
""", """
    tl.fromTo('#fc1', { autoAlpha: 0, x: -60 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 0.15);
    tl.fromTo('#fc2', { autoAlpha: 0, x: -60 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 1.9);
    tl.fromTo('#fc3', { autoAlpha: 0, x: -60 }, { autoAlpha: 1, x: 0, duration: 0.5, ease: 'power3.out' }, 4.1);
""")

# ---------------------------------------------------------------- 04 DATA (big number + bars)
BAR_MAX = 470
def bh(v): return round(BAR_MAX * v / 34)
frame(4, "04-data", f"""
    .dm-wrap {{ position: absolute; left: 0; right: 0; top: 290px; padding: 0 64px; text-align: center; }}
    .dm-kicker {{ font-weight: 700; font-size: 26px; letter-spacing: 0.22em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }}
    .dm-num {{ margin-top: 20px; height: 250px; font-weight: 900; font-size: 236px; line-height: 250px; letter-spacing: -0.03em; color: #FF5A1F; white-space: nowrap; opacity: 0; background: linear-gradient(180deg, #FF5A1F 30%, #FF4438 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }}
    .dm-lbl {{ margin-top: 10px; font-weight: 700; font-size: 38px; color: #fff; opacity: 0; }}
    .dm-chart-t {{ margin-top: 62px; font-weight: 700; font-size: 26px; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.55); opacity: 0; }}
    .dm-bars {{ position: relative; margin: 0 auto; width: 880px; height: 650px; }}
    .dm-base {{ position: absolute; left: 0; right: 0; top: 540px; height: 2px; background: rgba(255,255,255,0.22); }}
    .bar {{ position: absolute; width: 230px; bottom: 110px; height: 0; border-radius: 16px 16px 0 0; }}
    .bar .v {{ position: absolute; left: 0; right: 0; top: -66px; font-weight: 900; font-size: 46px; line-height: 1; opacity: 0; }}
    .bar .d {{ position: absolute; left: -30px; right: -30px; top: calc(100% + 18px); font-weight: 700; font-size: 25px; line-height: 1.3; color: rgba(255,255,255,0.8); opacity: 0; }}
    .b1 {{ left: 20px; background: linear-gradient(180deg, #FF5A1F, rgba(255,90,31,0.55)); box-shadow: 0 0 40px rgba(255,90,31,0.25); }}
    .b1 .v {{ color: #FF5A1F; }}
    .b2 {{ left: 325px; background: linear-gradient(180deg, #ffffff, rgba(255,255,255,0.45)); }}
    .b2 .v {{ color: #fff; }}
    .b3 {{ left: 630px; background: linear-gradient(180deg, rgba(255,255,255,0.35), rgba(255,255,255,0.12)); border: 1.5px dashed rgba(255,255,255,0.4); }}
    .b3 .v {{ color: rgba(255,255,255,0.8); }}
    .dm-foot {{ margin-top: 16px; font-weight: 500; font-size: 24px; color: rgba(255,255,255,0.5); opacity: 0; }}
""", f"""
    <div class="dm-wrap">
      <div class="dm-kicker" id="dm-kicker">Nhiệt độ miền Bắc dự báo giảm</div>
      <div class="dm-num" id="dm-num">8&ndash;10&deg;C</div>
      <div class="dm-lbl" id="dm-lbl">trong đợt không khí lạnh này</div>
      <div class="dm-chart-t" id="dm-ct">Hà Nội &middot; nhiệt độ cao nhất dự báo</div>
      <div class="dm-bars">
        <div class="dm-base"></div>
        <div class="bar b1" id="bar1" data-h="{bh(34)}"><div class="v" id="bv1">32&ndash;34&deg;C</div><div class="d" id="bd1">Ngày 2/10</div></div>
        <div class="bar b2" id="bar2" data-h="{bh(27)}"><div class="v" id="bv2">~27&deg;C</div><div class="d" id="bd2">Ngày 4/10</div></div>
        <div class="bar b3" id="bar3" data-h="{bh(29)}"><div class="v" id="bv3">28&ndash;29&deg;C</div><div class="d" id="bd3">AccuWeather<br>4&ndash;5/10</div></div>
      </div>
      <div class="dm-foot" id="dm-foot">Chiều cao cột theo mốc cao nhất của khoảng dự báo</div>
    </div>
""", """
    tl.fromTo('#dm-kicker', { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.36, ease: 'power2.out' }, 0);
    tl.fromTo('#dm-num', { autoAlpha: 0, scale: 0.7 }, { autoAlpha: 1, scale: 1, duration: 0.55, ease: 'back.out(1.7)' }, 0.25);
    tl.fromTo('#dm-lbl', { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0.7);
    tl.fromTo('#dm-ct', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4, ease: 'power2.out' }, 3.1);
    [['bar1', 'bv1', 'bd1', 3.8], ['bar2', 'bv2', 'bd2', 5.6], ['bar3', 'bv3', 'bd3', 6.9]].forEach(function (b) {
      var h = parseFloat(document.getElementById(b[0]).getAttribute('data-h'));
      tl.fromTo('#' + b[0], { height: 0 }, { height: h, duration: 0.8, ease: 'power3.out' }, b[3]);
      tl.fromTo('#' + b[1], { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, b[3] + 0.5);
      tl.fromTo('#' + b[2], { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4, ease: 'power2.out' }, b[3] + 0.2);
    });
    tl.fromTo('#dm-foot', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.45, ease: 'power2.out' }, 7.6);
""")

# ---------------------------------------------------------------- 05 CONTEXT (spec table)
frame(5, "05-context", """
    .cx-wrap { position: absolute; left: 64px; right: 64px; top: 300px; }
    .cx-kicker { font-weight: 700; font-size: 26px; letter-spacing: 0.22em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .cx-title { margin-top: 18px; font-weight: 800; font-size: 50px; line-height: 1.2; color: #fff; opacity: 0; }
    .cx-table { margin-top: 56px; border-radius: 26px; background: #121724; border: 1px solid rgba(255,255,255,0.07); box-shadow: 0 0 40px rgba(255,90,31,0.10); overflow: hidden; opacity: 0; }
    .cx-row { position: relative; height: 320px; padding: 0 44px; display: flex; flex-direction: column; justify-content: center; opacity: 0; }
    .cx-row + .cx-row { border-top: 1.5px solid rgba(255,255,255,0.1); }
    .cx-row .lb { font-weight: 700; font-size: 26px; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.55); }
    .cx-row .vl { margin-top: 14px; font-weight: 800; font-size: 50px; line-height: 1.2; color: #fff; }
    .cx-row .vl .hi { color: #FF5A1F; }
    .cx-row.warn .vl .hi { color: #FF4438; }
    .cx-row .tick { position: absolute; right: 44px; top: 50%; width: 14px; height: 14px; margin-top: -7px; border-radius: 50%; background: #FF5A1F; }
    .cx-row.warn .tick { background: #FF4438; }
""", """
    <div class="cx-wrap">
      <div class="cx-kicker" id="cx-kicker">Bối cảnh</div>
      <div class="cx-title" id="cx-title">Diễn biến những ngày tiếp theo</div>
      <div class="cx-table" id="cx-table">
        <div class="cx-row" id="cx1"><div class="lb">5&ndash;6/10 &middot; Miền Bắc</div><div class="vl">Đêm và sáng <span class="hi">trời lạnh</span></div><span class="tick"></span></div>
        <div class="cx-row" id="cx2"><div class="lb">5&ndash;6/10 &middot; Vùng núi</div><div class="vl">Đêm và sáng <span class="hi">trời rét</span></div><span class="tick"></span></div>
        <div class="cx-row warn" id="cx3"><div class="lb">Đêm 4 &ndash; 6/10 &middot; Thanh Hóa &ndash; Quảng Trị</div><div class="vl">Mưa rào, dông, nơi <span class="hi">mưa to</span></div><span class="tick"></span></div>
      </div>
    </div>
""", """
    tl.fromTo('#cx-kicker', { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.36, ease: 'power2.out' }, 0);
    tl.fromTo('#cx-title', { autoAlpha: 0, y: 12 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'power2.out' }, 0.2);
    tl.fromTo('#cx-table', { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 0.5);
    tl.fromTo('#cx1', { autoAlpha: 0, x: -40 }, { autoAlpha: 1, x: 0, duration: 0.45, ease: 'power3.out' }, 1.0);
    tl.fromTo('#cx2', { autoAlpha: 0, x: -40 }, { autoAlpha: 1, x: 0, duration: 0.45, ease: 'power3.out' }, 2.6);
    tl.fromTo('#cx3', { autoAlpha: 0, x: -40 }, { autoAlpha: 1, x: 0, duration: 0.45, ease: 'power3.out' }, 4.9);
""")

# ---------------------------------------------------------------- 06 IMPACT (2 big cards)
frame(6, "06-impact", """
    .im-wrap { position: absolute; left: 64px; right: 64px; top: 300px; }
    .im-kicker { font-weight: 700; font-size: 26px; letter-spacing: 0.22em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .im-cards { margin-top: 30px; display: flex; gap: 24px; }
    .im-card { flex: 1; height: 1090px; padding: 48px 34px; border-radius: 28px; background: #121724; border: 1.5px solid; opacity: 0; display: flex; flex-direction: column; }
    .im-card.ok { border-color: rgba(255,90,31,0.55); box-shadow: 0 0 40px rgba(255,90,31,0.14); }
    .im-card.risk { border-color: rgba(255,68,56,0.6); box-shadow: 0 0 40px rgba(255,68,56,0.14); }
    .ico-up { width: 96px; height: 96px; border: 7px solid #FF5A1F; border-radius: 50%; position: relative; flex: none; }
    .ico-up::after { content: ""; position: absolute; left: 50%; top: 28px; width: 28px; height: 28px; border-top: 7px solid #FF5A1F; border-right: 7px solid #FF5A1F; transform: translateX(-50%) rotate(-45deg); }
    .ico-warn { width: 0; height: 0; border-left: 52px solid transparent; border-right: 52px solid transparent; border-bottom: 92px solid #FF4438; position: relative; flex: none; margin: 0; }
    .ico-warn::after { content: "!"; position: absolute; left: -52px; width: 104px; top: 26px; text-align: center; font-weight: 900; font-size: 54px; line-height: 1; color: #0B0E14; }
    .im-t { margin-top: 36px; font-weight: 800; font-size: 40px; line-height: 1.22; color: #fff; }
    .im-n { margin-top: 30px; font-weight: 900; font-size: 74px; line-height: 1.05; letter-spacing: -0.02em; color: #FF5A1F; white-space: nowrap; }
    .im-d { margin-top: 20px; font-weight: 500; font-size: 32px; line-height: 1.4; color: rgba(255,255,255,0.74); }
    .im-list { margin-top: 36px; display: flex; flex-direction: column; gap: 28px; }
    .im-li { display: flex; align-items: center; gap: 16px; font-weight: 800; font-size: 44px; line-height: 1.1; color: #fff; opacity: 0; }
    .im-li i { display: block; width: 16px; height: 16px; border-radius: 50%; background: #FF4438; flex: none; }
""", """
    <div class="im-wrap">
      <div class="im-kicker" id="im-kicker">Ý nghĩa với người dân</div>
      <div class="im-cards">
        <div class="im-card ok" id="im1">
          <div class="ico-up"></div>
          <div class="im-t">Cả tháng 10 vẫn ấm hơn mức thường</div>
          <div class="im-n">0,5&ndash;1,5&deg;C</div>
          <div class="im-d">Nhiệt độ trung bình cả nước cao hơn trung bình nhiều năm</div>
        </div>
        <div class="im-card risk" id="im2">
          <div class="ico-warn"></div>
          <div class="im-t">Cần đề phòng khi lạnh tràn về</div>
          <div class="im-list">
            <div class="im-li" id="il1"><i></i>Tố</div>
            <div class="im-li" id="il2"><i></i>Lốc</div>
            <div class="im-li" id="il3"><i></i>Mưa đá</div>
            <div class="im-li" id="il4"><i></i>Gió giật mạnh</div>
          </div>
        </div>
      </div>
    </div>
""", """
    tl.fromTo('#im-kicker', { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.36, ease: 'power2.out' }, 0);
    tl.fromTo('#im1', { autoAlpha: 0, x: -50 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 0.3);
    tl.fromTo('#im2', { autoAlpha: 0, x: 50 }, { autoAlpha: 1, x: 0, duration: 0.55, ease: 'power3.out' }, 5.6);
    ['il1', 'il2', 'il3', 'il4'].forEach(function (id, k) {
      tl.fromTo('#' + id, { autoAlpha: 0, x: 20 }, { autoAlpha: 1, x: 0, duration: 0.35, ease: 'power2.out' }, 8.0 + k * 0.45);
    });
""")

# ---------------------------------------------------------------- 07 CTA
frame(7, "07-cta", """
    #root::before { content: ""; position: absolute; inset: 0; background: radial-gradient(80% 50% at 50% 34%, rgba(255,90,31,0.16), transparent 60%); }
    .t-wrap { position: absolute; left: 64px; right: 64px; top: 380px; text-align: center; }
    .t-kicker { font-weight: 700; font-size: 28px; letter-spacing: 0.26em; text-transform: uppercase; color: #FF5A1F; opacity: 0; }
    .t-head { margin-top: 34px; font-weight: 900; font-size: 84px; line-height: 1.16; color: #fff; }
    .t-head .ln { overflow: hidden; }
    .t-head .ln > span { display: block; }
    .t-opts { display: flex; justify-content: center; align-items: stretch; gap: 20px; margin-top: 80px; }
    .t-opt { flex: 1; max-width: 420px; padding: 44px 24px; border-radius: 20px; border: 2px solid; opacity: 0; }
    .t-opt.up { border-color: rgba(255,90,31,0.7); background: rgba(255,90,31,0.1); }
    .t-opt.down { border-color: rgba(255,68,56,0.7); background: rgba(255,68,56,0.1); }
    .t-opt .emo { width: 56px; height: 56px; margin: 0 auto; position: relative; }
    .t-opt.up .emo { border: 5px solid #FF5A1F; border-radius: 50%; }
    .t-opt.up .emo::after { content: ""; position: absolute; left: 50%; top: 14px; width: 15px; height: 15px; border-top: 5px solid #FF5A1F; border-right: 5px solid #FF5A1F; transform: translateX(-50%) rotate(-45deg); }
    .t-opt.down .emo::before { content: ""; position: absolute; left: 0; bottom: 0; width: 0; height: 0; border-left: 28px solid transparent; border-right: 28px solid transparent; border-bottom: 50px solid #FF4438; }
    .t-opt.down .emo::after { content: "!"; position: absolute; left: 0; right: 0; bottom: -2px; text-align: center; font-weight: 900; font-size: 30px; color: #0B0E14; }
    .t-opt .lab { margin-top: 22px; font-weight: 800; font-size: 36px; line-height: 1.25; color: #fff; }
    .t-vs { display: flex; align-items: center; font-weight: 900; font-size: 36px; color: rgba(255,255,255,0.35); opacity: 0; }
    .t-cta { display: inline-flex; align-items: center; gap: 18px; margin-top: 84px; padding: 26px 44px; border-radius: 100px; background: #FF5A1F; opacity: 0; }
    .t-cta .ico { width: 44px; height: 44px; flex: none; border-radius: 12px 12px 12px 4px; background: #fff; position: relative; }
    .t-cta .ico::before { content: ""; position: absolute; left: 10px; top: 13px; right: 10px; height: 4px; border-radius: 2px; background: #FF5A1F; box-shadow: 0 10px 0 #FF5A1F; }
    .t-cta span { font-weight: 800; font-size: 36px; letter-spacing: 0.01em; color: #1a0700; }
    .t-sign { position: absolute; left: 0; right: 0; top: 1500px; display: flex; align-items: center; justify-content: center; gap: 12px; opacity: 0; }
    .t-sign .m { width: 44px; height: 44px; }
    .t-sign .w { font-weight: 800; font-size: 30px; color: rgba(255,255,255,0.85); }
""", """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-head">
        <div class="ln" data-layout-allow-overflow=""><span id="t-h1">Sẵn sàng đón lạnh</span></div>
        <div class="ln" data-layout-allow-overflow=""><span id="t-h2">hay còn muốn nắng?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Đã chuẩn bị đón lạnh</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Chưa kịp thích nghi</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>
""", """
    tl.fromTo('#t-kicker', { autoAlpha: 0, y: -12 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 0);
    tl.fromTo('#t-h1', { yPercent: 118 }, { yPercent: 0, duration: 0.55, ease: 'power4.out' }, 0.2);
    tl.fromTo('#t-h2', { yPercent: 118 }, { yPercent: 0, duration: 0.55, ease: 'power4.out' }, 0.36);
    tl.fromTo('#t-o1', { autoAlpha: 0, y: 28, scale: 0.92 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }, 1.1);
    tl.fromTo('#t-vs', { autoAlpha: 0, scale: 0.5 }, { autoAlpha: 1, scale: 1, duration: 0.3, ease: 'back.out(2)' }, 1.35);
    tl.fromTo('#t-o2', { autoAlpha: 0, y: 28, scale: 0.92 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.42, ease: 'back.out(1.5)' }, 1.45);
    tl.fromTo('#t-cta', { autoAlpha: 0, y: 22 }, { autoAlpha: 1, y: 0, duration: 0.44, ease: 'power3.out' }, 3.4);
    tl.fromTo('#t-cta', { scale: 1 }, { scale: 1.04, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }, 4.0);
    tl.fromTo('#t-sign', { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4 }, 3.7);
""")

# ---------------------------------------------------------------- INDEX
names = ["01-hook","02-what","03-facts","04-data","05-context","06-impact","07-cta"]
scenes = "\n".join(
  f'      <div id="el-{n}" class="scene" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{STARTS[i]}" data-duration="{DUR[i]}" data-track-index="1"></div>'
  for i, n in enumerate(names))
voice_d = [4.32, 7.752, 6.912, 8.352, 8.784, 10.32, 6.336]
voices = "\n".join(
  f'      <audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{STARTS[i]}" data-duration="{voice_d[i]}" data-track-index="10" data-audio-group="voiceover"></audio>'
  for i in range(7))
S = STARTS
sfx = [
  ("hook","impact-bass-1",0.9,0.6,0.35),("t1","whoosh-short",S[1]-0.1,0.5,0.3),("t2","whoosh-short",S[2]-0.1,0.5,0.3),
  ("data","pop",S[3]+0.35,0.4,0.3),("bar","pop",S[3]+3.9,0.4,0.28),("t3","whoosh-short",S[4]-0.1,0.5,0.3),
  ("warn","impact-bass-1",S[5]+5.6,0.6,0.3),("t4","whoosh-short",S[6]-0.1,0.5,0.3),("o1","pop",S[6]+1.15,0.35,0.3),
  ("o2","click-soft",S[6]+1.5,0.35,0.32),("cta","chime",S[6]+3.4,1.2,0.32)]
sfx_html = "\n".join(f'      <audio id="el-sfx-{n}" src="assets/sfx/{f}.mp3" data-start="{round(s,2)}" data-duration="{d}" data-track-index="30" data-volume="{v}"></audio>' for n,f,s,d,v in sfx)

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
      .scene {{ position: absolute; inset: 0; width: 100%; height: 100%; }}

      /* --- Depth background (mounted once, behind every scene) --- */
      #bg-depth {{ position: absolute; inset: 0; overflow: hidden; z-index: 0; }}
      #bg-depth .blob {{ position: absolute; border-radius: 50%; filter: blur(60px); }}
      #bg-depth .blob-1 {{ width: 640px; height: 640px; background: radial-gradient(circle, rgba(255,90,31,0.20), transparent 70%); top: -120px; left: -160px; }}
      #bg-depth .blob-2 {{ width: 560px; height: 560px; background: radial-gradient(circle, rgba(255,68,56,0.16), transparent 70%); top: 900px; right: -200px; }}
      #bg-depth .blob-3 {{ width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,90,31,0.12), transparent 70%); bottom: -180px; left: 200px; }}
      #bg-stars circle {{ fill: #fff; }}
      .scene {{ z-index: 2; }}

      #brand-anchor {{ position: absolute; inset: 0; z-index: 90; pointer-events: none; opacity: 0; }}
      #ba-source {{ position: absolute; left: 44px; top: 46px; display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px; border-radius: 8px; background: rgba(11,14,20,0.6); border: 1px solid rgba(255,255,255,0.12); backdrop-filter: blur(3px); }}
      #ba-source .dot {{ width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; flex: none; }}
      #ba-source span {{ font-weight: 500; font-size: 21px; letter-spacing: 0.02em; color: rgba(255,255,255,0.9); white-space: nowrap; }}
      #ba-brand {{ position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }}
      #ba-brand .mark {{ width: 44px; height: 44px; flex: none; }}
      #ba-brand .mark img {{ display: block; width: 100%; height: 100%; }}
      #ba-brand .word {{ font-weight: 800; font-size: 24px; letter-spacing: 0.01em; color: #fff; }}
    </style>
  </head>
  <body>
    <!-- Kênh "Tin Tức Số" — cam #FF5A1F trên nền #0B0E14. Style dựng: 1-card-and-bar (claim_style index 0).
         data-duration mỗi frame = voice thật (ffprobe) + đệm. Tổng video = {TOTAL}s. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">

      <div id="bg-depth" data-layout-allow-overflow="">
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
        <div class="blob blob-3"></div>
        <svg id="bg-stars" viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:100%;height:100%;"></svg>
      </div>

{scenes}

      <div id="brand-anchor">
        <div id="ba-source"><span class="dot"></span><span>Nguồn: Dân Trí</span></div>
        <div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div>
      </div>

{voices}

{sfx_html}

      <audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"></audio>
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
      var rand = mulberry32(20261002);
      var starsSvg = document.getElementById('bg-stars');
      var starFrag = document.createDocumentFragment();
      var starEls = [];
      for (var i = 0; i < 40; i++) {{
        var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        c.setAttribute('cx', (rand() * 1080).toFixed(1));
        c.setAttribute('cy', (rand() * 1920).toFixed(1));
        c.setAttribute('r', (1.5 + rand() * 1.5).toFixed(2));
        c.setAttribute('opacity', (0.15 + rand() * 0.25).toFixed(2));
        starFrag.appendChild(c);
        starEls.push(c);
      }}
      starsSvg.appendChild(starFrag);

      const tl = gsap.timeline({{ paused: true }});
      tl.to('.blob', {{ x: '+=40', y: '-=30', duration: 18, ease: 'sine.inOut', repeat: -1, yoyo: true, stagger: 3 }}, 0);
      tl.to(starEls, {{ opacity: '+=0.25', duration: 4, ease: 'sine.inOut', repeat: -1, yoyo: true, stagger: {{ each: 0.15, from: 'random' }} }}, 0);
      tl.set('#brand-anchor', {{ opacity: 1 }}, {STARTS[1]});
      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
"""
open(os.path.join(base, "index.html"), "w", encoding="utf-8").write(index)
print("total", TOTAL, STARTS)
