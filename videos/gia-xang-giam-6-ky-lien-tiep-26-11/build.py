#!/usr/bin/env python3
"""Build index.html + 7 frames for gia-xang-giam-6-ky-lien-tiep-26-11 (style 10-stock-terminal).
Timing comes from real Vbee voice durations (ffprobe) + ElevenLabs STT word timestamps."""
import json, subprocess, html

PAD = 0.45      # tail pad per frame
LEAD = 0.10     # voice starts 0.1s into each frame
FONT_W = [400, 500, 600, 700, 800, 900]
LAT = "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
VIE = "U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB"
FONTS = "\n".join(
    f"@font-face{{font-family:'Montserrat';font-weight:{w};src:url('assets/fonts/Montserrat-{w}-{s}.woff2') format('woff2');unicode-range:{r};}}"
    for w in FONT_W for s, r in (("latin", LAT), ("vietnamese", VIE)))


def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).decode())


VD = [dur(f'assets/voice/line{i}.mp3') for i in range(1, 8)]
STT = []
for i in range(1, 8):
    d = json.load(open(f'assets/voice/stt{i}.json'))
    STT.append([w for w in d['words'] if w.get('type') == 'word'])
FD = [round(LEAD + VD[i] + PAD, 2) for i in range(7)]
FS = [0.0]
for i in range(6):
    FS.append(round(FS[-1] + FD[i], 2))
TOTAL = round(FS[-1] + FD[-1], 2)


def wt(line, idx):
    """frame-local time of word idx in voice line (1-based line)"""
    return round(LEAD + STT[line - 1][idx]['start'], 2)


def find(line, text, nth=0):
    hits = [k for k, w in enumerate(STT[line - 1]) if w['text'].strip('.,?').lower() == text.lower()]
    return wt(line, hits[nth])


COMMON = """
#root { position:absolute; inset:0; width:100%; height:100%; overflow:hidden; font-family:"Montserrat",sans-serif; color:#fff; background:transparent; font-variant-numeric:tabular-nums; }
#content { position:absolute; inset:0; transform-origin:50% 45%; }
.kick { position:absolute; left:64px; top:300px; display:flex; align-items:center; gap:14px; font-weight:700; font-size:26px; letter-spacing:0.22em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.kick .blink { width:12px; height:12px; border-radius:50%; background:#FF5A1F; box-shadow:0 0 14px rgba(255,90,31,0.9); }
.kick .code { padding:4px 10px; border:1.5px solid rgba(255,90,31,0.7); border-radius:6px; font-size:20px; letter-spacing:0.12em; }
.credit { position:absolute; right:14px; bottom:12px; padding:5px 10px; border-radius:6px; background:rgba(11,14,20,0.78); font-weight:500; font-size:18px; color:rgba(255,255,255,0.9); }
.card { position:absolute; background:#121724; border:1.5px solid rgba(255,255,255,0.12); border-radius:18px; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.card.hot { border-color:rgba(255,90,31,0.85); }
.card.warn { border-color:rgba(255,68,56,0.85); }
.tri-d { display:inline-block; width:0; height:0; border-left:13px solid transparent; border-right:13px solid transparent; border-top:20px solid #FF5A1F; vertical-align:middle; }
.tri-u { display:inline-block; width:0; height:0; border-left:13px solid transparent; border-right:13px solid transparent; border-bottom:20px solid #FF4438; vertical-align:middle; }
.grid-bg { position:absolute; inset:0; opacity:0.5; background-image:linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px); background-size:60px 60px; }
.cutflash { position:absolute; inset:0; z-index:6; pointer-events:none; opacity:0; background:linear-gradient(180deg, rgba(255,90,31,0.4), rgba(255,68,56,0.18)); }
"""


def frame(fid, css, body, js):
    return f"""<template>
  <style>
{FONTS}
{COMMON}
{css}
  </style>
  <div id="root" data-composition-id="{fid}" data-width="1080" data-height="1920">
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}
    window.__timelines['{fid}'] = tl;
  </script>
</template>
"""


def smash(T):
    return f"""    tl.fromTo('#cutflash',{{opacity:0}},{{opacity:0.55,duration:0.05,ease:'none'}},{T});
    tl.to('#cutflash',{{opacity:0,duration:0.16,ease:'power1.in'}},{T + 0.05:.2f});
    tl.fromTo('#content',{{scale:1}},{{scale:0.986,duration:0.06,ease:'power1.out'}},{T});
    tl.to('#content',{{scale:1,duration:0.14,ease:'power2.out'}},{T + 0.061:.3f});
"""


frames = {}
sfx = []   # (src, abs_start, dur, vol)

# ---------------- 01 HOOK (fixed brand layout) ----------------
d = FD[0]
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:880px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:40% 50%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:760px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:28px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:132px; line-height:1.04; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.hk-name.o { color:#FF5A1F; }
.hk-sub { margin-top:20px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:28px; margin-top:42px; }
.hk-tag { font-weight:800; font-size:48px; line-height:1; color:#FF5A1F; opacity:0; white-space:nowrap; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: VnExpress</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress · 26/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Giá xăng</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">giảm 6 kỳ</div></div>
      <div class="hk-sub" id="hk-sub">Từ 15h ngày 26/11 · <b>liên tiếp trong tháng 11</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Diesel −1.380 đ/lít</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Xăng chỉ −50 đến −180 đ</div>
      </div>
    </div>
""", f"""
    tl.fromTo('.hk-photo',{{autoAlpha:0,scale:1.1}},{{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'}},0);
    tl.fromTo('.hk-panel',{{autoAlpha:0,y:48}},{{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'}},0.05);
    tl.fromTo('.hk-masthead',{{autoAlpha:0,y:14}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},0.22);
    tl.fromTo('.hk-badge',{{autoAlpha:0,scale:0.9}},{{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'}},0.42);
    tl.fromTo('#hk-n1',{{yPercent:118}},{{yPercent:0,duration:0.6,ease:'power4.out'}},0.6);
    tl.fromTo('#hk-n2',{{yPercent:118}},{{yPercent:0,duration:0.6,ease:'power4.out'}},0.85);
    tl.fromTo('#hk-sub',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},1.4);
    tl.fromTo('#hk-t1',{{autoAlpha:0,x:-18}},{{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'}},2.0);
    tl.fromTo('#hk-t2',{{autoAlpha:0,x:-18}},{{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'}},2.3);
    tl.to('.hk-photo img',{{scale:1.06,duration:{d},ease:'none'}},0);
""")
sfx += [('impact-bass-1.mp3', 0.60, 0.6, 0.35), ('pop.mp3', 2.0, 0.4, 0.3)]

# ---------------- 02 WHAT HAPPENED ----------------
d = FD[1]
tick_items = [("E5 RON 92", "18.390", "180"), ("E10 RON 95-III", "19.050", "50"), ("DIESEL 0,05S", "24.960", "1.380"), ("MAZUT", "17.570", "1.100")]
tick_html = "".join(f'<span class="ti"><span class="tn">{n}</span><span class="tp">{p}</span><span class="tri-d"></span><span class="td">{dd}</span></span>' for n, p, dd in tick_items * 3)
frames['02-what'] = frame('02-what', """
.w-img { position:absolute; left:64px; right:64px; top:360px; height:560px; border-radius:18px; overflow:hidden; box-shadow:0 0 40px rgba(255,90,31,0.14); border:1.5px solid rgba(255,255,255,0.12); opacity:0; }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 40%; }
.tape { position:absolute; left:0; right:0; top:960px; height:76px; border-top:2px solid #FF5A1F; border-bottom:2px solid #FF5A1F; background:rgba(255,90,31,0.07); overflow:hidden; opacity:0; }
.tape .live { position:absolute; left:0; top:0; bottom:0; width:150px; z-index:2; display:flex; align-items:center; gap:10px; padding-left:24px; background:#0B0E14; font-weight:800; font-size:22px; letter-spacing:0.16em; color:#FF5A1F; }
.tape .live i { width:11px; height:11px; border-radius:50%; background:#FF5A1F; }
.tape .rw { position:absolute; left:0px; right:0; top:0; bottom:0; overflow:hidden; }
.tape .row { position:absolute; left:0; top:0; bottom:0; display:flex; align-items:center; white-space:nowrap; }
.ti { display:inline-flex; align-items:center; gap:12px; margin-right:54px; font-size:28px; }
.ti .tn { font-weight:600; color:rgba(255,255,255,0.7); letter-spacing:0.04em; }
.ti .tp { font-weight:800; color:#fff; }
.ti .td { font-weight:700; color:#FF5A1F; }
.w-head { position:absolute; left:64px; right:64px; top:1080px; font-weight:800; font-size:58px; line-height:1.15; }
.w-head .ln { overflow:hidden; padding-bottom:4px; } .w-head .ln > span { display:block; }
.w-head b { color:#FF5A1F; font-weight:900; }
.w-sub { position:absolute; left:64px; right:64px; top:1300px; font-weight:600; font-size:34px; line-height:1.3; color:rgba(255,255,255,0.85); opacity:0; }
.w-chips { position:absolute; left:64px; top:1380px; display:flex; gap:18px; }
.chip { display:inline-flex; align-items:center; gap:10px; padding:12px 22px; border-radius:10px; border:1.5px solid rgba(255,90,31,0.8); font-weight:700; font-size:28px; opacity:0; }
.chip.g { border-color:rgba(255,255,255,0.25); color:rgba(255,255,255,0.85); }
""", f"""
    <div class="grid-bg"></div>
    <div id="content">
      <div class="kick" id="w-k"><span class="blink"></span>Điều chỉnh giá <span class="code">15:00 · 26/11</span></div>
      <div class="w-img" id="w-img"><img src="assets/img/tt.jpg" alt=""><div class="credit">Ảnh: Tuổi Trẻ</div></div>
      <div class="tape" id="w-tape"><div class="rw"><div class="row" id="w-row">{tick_html}</div></div></div>
      <div class="w-head">
        <div class="ln"><span id="w-h1">Liên Bộ Công Thương –</span></div>
        <div class="ln"><span id="w-h2">Tài chính <b>hạ giá bán lẻ</b></span></div>
        <div class="ln"><span id="w-h3">xăng dầu</span></div>
      </div>
      <div class="w-sub" id="w-sub">Theo đà giảm của giá thành phẩm thế giới</div>
      <div class="w-chips"><div class="chip" id="w-c1"><span class="tri-d"></span>Kỳ giảm thứ 6 với xăng</div><div class="chip g" id="w-c2">Kỳ trước: 19/11</div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#w-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
    tl.to('#w-k .blink',{{keyframes:[{{opacity:0.2,duration:0.4}},{{opacity:1,duration:0.4}},{{opacity:0.2,duration:0.4}},{{opacity:1,duration:0.4}},{{opacity:0.2,duration:0.4}},{{opacity:1,duration:0.4}}]}},0.5);
    tl.fromTo('#w-img',{{autoAlpha:0,y:40,scale:0.97}},{{autoAlpha:1,y:0,scale:1,duration:0.6,ease:'power3.out'}},0.15);
    tl.to('#w-img img',{{scale:1.07,duration:{d},ease:'none'}},0);
    tl.fromTo('#w-tape',{{autoAlpha:0,scaleX:0.6}},{{autoAlpha:1,scaleX:1,duration:0.45,ease:'power3.out'}},0.55);
    tl.fromTo('#w-row',{{x:0}},{{x:-1500,duration:{d},ease:'none'}},0);
    tl.fromTo('#w-h1',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(2,'Liên')});
    tl.fromTo('#w-h2',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(2,'chính')});
    tl.fromTo('#w-h3',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(2,'xăng')});
    tl.fromTo('#w-sub',{{autoAlpha:0,y:14}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},{find(2,'theo')});
    tl.fromTo('#w-c1',{{autoAlpha:0,y:14}},{{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'}},{find(2,'thế')});
    tl.fromTo('#w-c2',{{autoAlpha:0,y:14}},{{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'}},{find(2,'thế') + 0.3:.2f});
""")
sfx += [('whoosh-short.mp3', FS[1] - 0.1, 0.5, 0.3), ('pop.mp3', FS[1] + find(2, 'thế'), 0.4, 0.28)]

# ---------------- 03 KEY FACTS ----------------
d = FD[2]
rows = [("01", "Xăng E5 RON 92", "18.390", "180", 180, find(3, 'E5')),
        ("02", "Xăng E10 RON 95-III", "19.050", "50", 50, find(3, 'E10')),
        ("03", "Dầu diesel 0,05S", "24.960", "1.380", 1380, find(3, 'Dầu'))]
row_html, row_js = "", ""
for k, (no, name, price, delta, dv, t) in enumerate(rows):
    top = 380 + k * 336
    hot = ' hot' if k == 2 else ''
    w = max(2.5, dv / 1380 * 100)
    row_html += f"""
      <div class="card f-row{hot}" id="f-r{k}" style="top:{top}px;">
        <div class="f-no">{no}</div>
        <div class="f-candle"><div class="wick"></div><div class="body" id="f-cb{k}" style="height:{40 + dv / 1380 * 120:.0f}px"></div></div>
        <div class="f-name">{name}</div>
        <div class="f-price"><span id="f-p{k}">{price}</span><small>đ/lít</small></div>
        <div class="f-delta"><span class="tri-d"></span>{delta} đ</div>
        <div class="f-bar"><div class="f-fill" id="f-f{k}" style="width:{w:.1f}%"></div></div>
        <div class="f-cap">Mức giảm kỳ này (so với diesel)</div>
      </div>"""
    row_js += f"""    tl.fromTo('#f-r{k}',{{autoAlpha:0,x:60}},{{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'}},{t - 0.1:.2f});
    tl.fromTo('#f-cb{k}',{{scaleY:0}},{{scaleY:1,duration:0.5,ease:'power2.out'}},{t + 0.2:.2f});
    tl.fromTo('#f-f{k}',{{scaleX:0}},{{scaleX:1,duration:0.7,ease:'power2.out'}},{t + 0.35:.2f});
"""
    sfx.append(('pop.mp3', FS[2] + t - 0.1, 0.4, 0.26))
frames['03-facts'] = frame('03-facts', """
.f-row { left:64px; right:64px; height:300px; opacity:0; }
.f-no { position:absolute; left:30px; top:30px; font-weight:700; font-size:22px; letter-spacing:0.14em; color:rgba(255,255,255,0.45); }
.f-candle { position:absolute; left:40px; top:78px; width:26px; height:170px; }
.f-candle .wick { position:absolute; left:12px; top:0; width:2px; height:170px; background:rgba(255,90,31,0.45); }
.f-candle .body { position:absolute; left:0; top:10px; width:26px; border-radius:3px; background:#FF5A1F; transform-origin:top center; }
.f-name { position:absolute; left:110px; top:28px; font-weight:600; font-size:32px; color:rgba(255,255,255,0.78); }
.f-price { position:absolute; left:106px; top:72px; font-weight:900; font-size:104px; line-height:1; letter-spacing:-0.02em; }
.f-price small { margin-left:12px; font-weight:600; font-size:28px; letter-spacing:0; color:rgba(255,255,255,0.6); }
.f-delta { position:absolute; right:34px; top:96px; display:flex; align-items:center; gap:12px; padding:12px 20px; border-radius:10px; background:rgba(255,90,31,0.14); border:1.5px solid rgba(255,90,31,0.7); font-weight:800; font-size:40px; color:#FF5A1F; }
.f-bar { position:absolute; left:110px; right:34px; top:220px; height:14px; border-radius:7px; background:rgba(255,255,255,0.08); overflow:hidden; }
.f-fill { height:100%; border-radius:7px; background:linear-gradient(90deg,#FF5A1F,#FF4438); transform-origin:left center; }
.f-cap { position:absolute; left:110px; top:246px; font-weight:500; font-size:20px; color:rgba(255,255,255,0.5); }
.f-foot { position:absolute; left:64px; right:64px; top:1400px; display:flex; align-items:center; gap:14px; font-weight:600; font-size:30px; color:rgba(255,255,255,0.75); opacity:0; }
.f-foot b { color:#fff; font-weight:800; }
""", f"""
    <div class="grid-bg"></div>
    <div id="content">
      <div class="kick" id="f-k"><span class="blink"></span>Bảng giá mới <span class="code">VNĐ/LÍT</span></div>
{row_html}
      <div class="f-foot" id="f-foot"><span class="tri-d"></span>Mazut: <b>17.570 đ/kg</b> (−1.100 đ)</div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#f-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
{row_js}{smash(rows[2][5] - 0.12)}
    tl.fromTo('#f-foot',{{autoAlpha:0,y:14}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},{find(3,'hai'):.2f});
""")
sfx += [('whoosh-short.mp3', FS[2] - 0.1, 0.5, 0.3), ('click-soft.mp3', FS[2] + rows[2][5] - 0.12, 0.3, 0.4)]

# ---------------- 04 DATA MOMENT ----------------
d = FD[3]
t_num = find(4, 'gần', 0)
t_dsl = find(4, 'dầu')
t_mark = find(4, 'Giá')
frames['04-data'] = frame('04-data', """
.d-lab { position:absolute; left:64px; right:64px; top:370px; font-weight:700; font-size:42px; color:rgba(255,255,255,0.85); opacity:0; }
.d-lab b { color:#fff; font-weight:900; }
.d-chart { position:absolute; left:40px; top:430px; width:1000px; height:330px; }
.d-chart path { fill:none; stroke:rgba(255,90,31,0.45); stroke-width:5; stroke-linecap:round; stroke-linejoin:round; }
.d-chart .area { fill:url(#dg); stroke:none; opacity:0; }
.d-num { position:absolute; left:64px; right:64px; top:470px; display:flex; align-items:baseline; gap:18px; opacity:0; }
.d-num .pre { font-weight:800; font-size:56px; color:rgba(255,255,255,0.85); }
.d-num .n { font-weight:900; font-size:220px; line-height:1; letter-spacing:-0.04em; color:#FF5A1F; text-shadow:0 0 40px rgba(255,90,31,0.35); }
.d-num .u { font-weight:700; font-size:44px; color:rgba(255,255,255,0.75); }
.d-bars { position:absolute; left:64px; right:64px; top:830px; }
.d-b { position:relative; height:150px; margin-bottom:34px; opacity:0; }
.d-b .nm { font-weight:700; font-size:32px; color:rgba(255,255,255,0.85); }
.d-b .trk { position:absolute; left:0; right:0; top:52px; height:60px; border-radius:10px; background:rgba(255,255,255,0.06); }
.d-b .fill { position:absolute; left:0; top:52px; height:60px; border-radius:10px; background:linear-gradient(90deg,#FF5A1F,#FF4438); transform-origin:left center; box-shadow:0 0 30px rgba(255,90,31,0.25); }
.d-b .val { position:absolute; right:18px; top:58px; font-weight:900; font-size:40px; color:#fff; z-index:2; }
.d-b.sec .fill { background:rgba(255,90,31,0.55); }
.d-mark { left:64px; right:64px; top:1210px; height:230px; opacity:0; }
.d-mark .tg { position:absolute; left:34px; top:28px; font-weight:700; font-size:22px; letter-spacing:0.18em; color:#FF5A1F; }
.d-mark .tx { position:absolute; left:34px; right:34px; top:70px; font-weight:800; font-size:44px; line-height:1.22; }
.d-mark .tx b { color:#FF5A1F; font-weight:900; }
""", f"""
    <div class="grid-bg"></div>
    <div id="content">
      <div class="kick" id="d-k"><span class="blink"></span>Cộng dồn <span class="code">SO VỚI CUỐI THÁNG 10</span></div>
      <svg class="d-chart" viewBox="0 0 1000 330"><defs><linearGradient id="dg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF5A1F" stop-opacity="0.18"/><stop offset="1" stop-color="#FF5A1F" stop-opacity="0"/></linearGradient></defs>
        <path class="area" id="d-area" d="M0,40 L170,70 L330,120 L500,170 L670,215 L830,262 L1000,290 L1000,330 L0,330 Z"/>
        <path id="d-line" pathLength="1" d="M0,40 L170,70 L330,120 L500,170 L670,215 L830,262 L1000,290" style="stroke-dasharray:1;stroke-dashoffset:1"/>
      </svg>
      <div class="d-lab" id="d-lab">Mỗi lít <b>xăng E10</b> rẻ hơn</div>
      <div class="d-num" id="d-num"><span class="pre">gần</span><span class="n" id="d-n">0</span><span class="u">đ</span></div>
      <div class="d-bars">
        <div class="d-b" id="d-b1"><div class="nm">Xăng E10</div><div class="trk"></div><div class="fill" id="d-f1" style="width:100%"></div><div class="val">gần 6.700 đ</div></div>
        <div class="d-b sec" id="d-b2"><div class="nm">Dầu diesel</div><div class="trk"></div><div class="fill" id="d-f2" style="width:{5300/6700*100:.1f}%"></div><div class="val">gần 5.300 đ</div></div>
      </div>
      <div class="card hot d-mark" id="d-mark"><div class="tg">MỐC GIÁ XĂNG</div><div class="tx">Về ngang thời điểm <b>ngay trước khi xảy ra xung đột ở Trung Đông</b></div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#d-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#d-lab',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{find(4,'mỗi') - 0.1:.2f});
    tl.to('#d-line',{{strokeDashoffset:0,duration:1.4,ease:'power1.inOut'}},{find(4,'mỗi'):.2f});
    tl.fromTo('#d-area',{{opacity:0}},{{opacity:1,duration:0.6}},{find(4,'mỗi') + 0.9:.2f});
    tl.fromTo('#d-num',{{autoAlpha:0,scale:0.9}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(1.6)'}},{t_num - 0.2:.2f});
    const c = {{v:0}}; const numEl = document.querySelector('#d-n');
    tl.fromTo(c,{{v:0}},{{v:6700,duration:1.1,ease:'power2.out',onUpdate(){{ numEl.textContent = Math.round(c.v/10)*10 >= 1000 ? (Math.round(c.v/10)*10).toLocaleString('de-DE') : String(Math.round(c.v/10)*10); }}}},{t_num - 0.2:.2f});
    tl.fromTo('#d-b1',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{t_num + 0.7:.2f});
    tl.fromTo('#d-f1',{{scaleX:0}},{{scaleX:1,duration:0.8,ease:'power2.out'}},{t_num + 0.8:.2f});
    tl.fromTo('#d-b2',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{t_dsl - 0.1:.2f});
    tl.fromTo('#d-f2',{{scaleX:0}},{{scaleX:1,duration:0.8,ease:'power2.out'}},{t_dsl:.2f});
{smash(t_mark - 0.1)}
    tl.fromTo('#d-mark',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},{t_mark - 0.05:.2f});
""")
sfx += [('whoosh-short.mp3', FS[3] - 0.1, 0.5, 0.3), ('impact-bass-1.mp3', FS[3] + t_num + 0.9, 0.6, 0.32),
        ('click-soft.mp3', FS[3] + t_mark - 0.1, 0.3, 0.4)]

# ---------------- 05 CONTEXT (bar chart) ----------------
d = FD[4]
BASE = 780
SC = 40  # px per %
cols = [("Xăng RON 95", -8.6, "−8,6%", 140), ("Dầu diesel", -8.1, "−8,1%", 345), ("Mazut", -8.9, "−8,9%", 550)]
t_cols = find(5, 'giảm') - 0.2
t_brent = find(5, 'Brent') - 0.15
col_html, col_js = "", ""
for k, (nm, v, lab, x) in enumerate(cols):
    h = abs(v) * SC
    col_html += f"""
      <div class="c-col" id="c-c{k}" style="left:{x}px;top:{BASE}px;height:{h:.0f}px"></div>
      <div class="c-val" id="c-v{k}" style="left:{x - 30}px;top:{BASE + h + 14:.0f}px">{lab}</div>
      <div class="c-nm" id="c-n{k}" style="left:{x - 30}px;top:{BASE - 62}px">{nm}</div>"""
    col_js += f"""    tl.fromTo('#c-c{k}',{{scaleY:0}},{{scaleY:1,duration:0.7,ease:'power2.out'}},{t_cols + k * 0.25:.2f});
    tl.fromTo(['#c-v{k}','#c-n{k}'],{{autoAlpha:0}},{{autoAlpha:1,duration:0.3}},{t_cols + k * 0.25 + 0.4:.2f});
"""
bh = 3.5 * SC * 1.6
frames['05-context'] = frame('05-context', f"""
.c-head {{ position:absolute; left:64px; right:64px; top:360px; font-weight:800; font-size:52px; line-height:1.18; }}
.c-head .ln {{ overflow:hidden; padding-bottom:4px; }} .c-head .ln > span {{ display:block; }}
.c-head b {{ color:#FF5A1F; font-weight:900; }}
.c-sub {{ position:absolute; left:64px; top:500px; font-weight:600; font-size:30px; color:rgba(255,255,255,0.7); opacity:0; }}
.c-axis {{ position:absolute; left:64px; right:64px; top:{BASE}px; height:3px; background:rgba(255,255,255,0.4); transform-origin:left center; }}
.c-col {{ position:absolute; width:150px; border-radius:0 0 10px 10px; background:linear-gradient(180deg,#FF5A1F,rgba(255,90,31,0.55)); transform-origin:top center; box-shadow:0 0 30px rgba(255,90,31,0.2); }}
.c-val {{ position:absolute; width:210px; text-align:center; font-weight:900; font-size:44px; color:#FF5A1F; opacity:0; }}
.c-nm {{ position:absolute; width:210px; text-align:center; font-weight:700; font-size:26px; color:rgba(255,255,255,0.8); opacity:0; }}
.c-div {{ position:absolute; left:760px; top:560px; width:0; height:760px; border-left:2px dashed rgba(255,255,255,0.25); opacity:0; }}
.c-bcol {{ position:absolute; left:820px; top:{BASE - bh:.0f}px; width:150px; height:{bh:.0f}px; border-radius:10px 10px 0 0; background:linear-gradient(0deg,rgba(255,68,56,0.55),#FF4438); transform-origin:bottom center; box-shadow:0 0 30px rgba(255,68,56,0.25); }}
.c-bval {{ position:absolute; left:790px; width:210px; top:{BASE - bh - 64:.0f}px; text-align:center; font-weight:900; font-size:44px; color:#FF4438; opacity:0; display:flex; align-items:center; justify-content:center; gap:8px; }}
.c-bnm {{ position:absolute; left:790px; width:210px; top:{BASE + 18}px; text-align:center; font-weight:700; font-size:26px; line-height:1.3; color:rgba(255,255,255,0.8); opacity:0; }}
.c-bprice {{ left:600px; right:64px; top:1262px; height:170px; opacity:0; }}
.c-bprice .tg {{ position:absolute; left:28px; top:22px; font-weight:700; font-size:20px; letter-spacing:0.16em; color:#FF4438; }}
.c-bprice .v {{ position:absolute; left:28px; top:58px; font-weight:900; font-size:56px; color:#fff; }}
.c-bprice .v small {{ font-weight:600; font-size:24px; color:rgba(255,255,255,0.65); margin-left:8px; }}
.c-note {{ position:absolute; left:64px; width:500px; top:1272px; font-weight:600; font-size:26px; line-height:1.35; color:rgba(255,255,255,0.65); opacity:0; }}
.c-note b {{ color:#fff; }}
""", f"""
    <div class="grid-bg"></div>
    <div id="content">
      <div class="kick" id="c-k"><span class="blink"></span>Giá thế giới <span class="code">GIỮA 2 KỲ ĐIỀU HÀNH</span></div>
      <div class="c-head">
        <div class="ln"><span id="c-h1">Thành phẩm thế giới</span></div>
        <div class="ln"><span id="c-h2">bình quân <b>giảm 8–9,3%</b></span></div>
      </div>
      <div class="c-sub" id="c-sub">Do lo ngại dư cung</div>
      <div class="c-axis" id="c-axis"></div>
{col_html}
      <div class="c-div" id="c-div"></div>
      <div class="c-bcol" id="c-bcol"></div>
      <div class="c-bval" id="c-bval"><span class="tri-u"></span>+3,5%</div>
      <div class="c-bnm" id="c-bnm">Dầu Brent<br>phiên 25/11</div>
      <div class="c-note" id="c-note">Bình quân giá thành phẩm giữa kỳ <b>19/11</b> và <b>26/11</b>, theo liên Bộ Công Thương – Tài chính</div>
      <div class="card warn c-bprice" id="c-bp"><div class="tg">BRENT · 25/11</div><div class="v">94,61<small>USD/thùng</small></div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#c-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#c-h1',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(5,'giá'):.2f});
    tl.fromTo('#c-h2',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(5,'bình'):.2f});
    tl.fromTo('#c-axis',{{scaleX:0}},{{scaleX:1,duration:0.6,ease:'power2.out'}},{find(5,'bình'):.2f});
{col_js}    tl.fromTo('#c-sub',{{autoAlpha:0,y:10}},{{autoAlpha:1,y:0,duration:0.4}},{find(5,'lo'):.2f});
    tl.fromTo('#c-note',{{autoAlpha:0,y:10}},{{autoAlpha:1,y:0,duration:0.4}},{find(5,'cung') + 0.2:.2f});
{smash(t_brent)}
    tl.fromTo('#c-div',{{autoAlpha:0}},{{autoAlpha:1,duration:0.3}},{t_brent:.2f});
    tl.fromTo('#c-bnm',{{autoAlpha:0}},{{autoAlpha:1,duration:0.3}},{t_brent + 0.05:.2f});
    tl.fromTo('#c-bcol',{{scaleY:0}},{{scaleY:1,duration:0.7,ease:'power2.out'}},{find(5,'bật') - 0.1:.2f});
    tl.fromTo('#c-bval',{{autoAlpha:0,y:10}},{{autoAlpha:1,y:0,duration:0.35}},{find(5,'bật') + 0.4:.2f});
    tl.fromTo('#c-bp',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{find(5,'lên') - 0.05:.2f});
""")
sfx += [('whoosh-short.mp3', FS[4] - 0.1, 0.5, 0.3), ('click-soft.mp3', FS[4] + t_brent, 0.3, 0.4),
        ('pop.mp3', FS[4] + find(5, 'lên'), 0.4, 0.26)]

# ---------------- 06 IMPACT ----------------
d = FD[5]
t_tax = find(6, 'Thuế')
spark = "M0,60 L60,48 L120,66 L180,40 L240,52 L300,30 L360,44 L420,24"
frames['06-impact'] = frame('06-impact', """
.i-img { position:absolute; left:64px; right:64px; top:360px; height:330px; border-radius:18px; overflow:hidden; border:1.5px solid rgba(255,255,255,0.12); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.i-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:40% 45%; }
.i-row { left:64px; right:64px; height:200px; opacity:0; }
.i-row .nm { position:absolute; left:34px; top:28px; font-weight:700; font-size:30px; color:rgba(255,255,255,0.82); }
.i-row .nm small { display:block; margin-top:6px; font-weight:600; font-size:22px; letter-spacing:0.12em; color:#FF5A1F; }
.i-row svg { position:absolute; left:34px; top:110px; width:420px; height:80px; }
.i-row svg path { fill:none; stroke:rgba(255,90,31,0.75); stroke-width:4; stroke-linecap:round; stroke-linejoin:round; }
.i-row .v { position:absolute; right:34px; top:62px; font-weight:900; font-size:84px; line-height:1; color:#FF5A1F; opacity:0; }
.i-row .v small { font-weight:700; font-size:28px; color:rgba(255,255,255,0.7); margin-left:8px; }
.i-tax { left:64px; right:64px; top:1220px; height:220px; opacity:0; }
.i-tax .nm { position:absolute; left:34px; top:30px; font-weight:700; font-size:30px; line-height:1.3; color:rgba(255,255,255,0.85); width:520px; }
.i-tax .nm small { display:block; margin-top:10px; font-weight:600; font-size:26px; color:rgba(255,255,255,0.6); }
.i-tax .v { position:absolute; right:40px; top:36px; font-weight:900; font-size:140px; line-height:1; color:#FF5A1F; }
""", f"""
    <div class="grid-bg"></div>
    <div id="content">
      <div class="kick" id="i-k"><span class="blink"></span>Kỳ này <span class="code">QUỸ BÌNH ỔN · THUẾ</span></div>
      <div class="i-img" id="i-img"><img src="assets/img/dt2.jpg" alt=""><div class="credit">Ảnh: Dân Trí</div></div>
      <div class="card i-row" id="i-r1" style="top:730px"><div class="nm">Trích lập quỹ bình ổn<small>XĂNG</small></div><svg viewBox="0 0 420 80"><path id="i-s1" pathLength="1" d="{spark}" style="stroke-dasharray:1;stroke-dashoffset:1"/></svg><div class="v" id="i-v1">1.400<small>đ/lít</small></div></div>
      <div class="card i-row" id="i-r2" style="top:965px"><div class="nm">Trích lập quỹ bình ổn<small>DẦU DIESEL</small></div><svg viewBox="0 0 420 80"><path id="i-s2" pathLength="1" d="{spark}" style="stroke-dasharray:1;stroke-dashoffset:1"/></svg><div class="v" id="i-v2">500<small>đ/lít</small></div></div>
      <div class="card hot i-tax" id="i-tax"><div class="nm">Thuế tiêu thụ đặc biệt với xăng<small>Giữ đến hết tháng 3/2027</small></div><div class="v">0%</div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#i-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#i-img',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'}},0.1);
    tl.to('#i-img img',{{scale:1.06,duration:{d},ease:'none'}},0);
    tl.fromTo('#i-r1',{{autoAlpha:0,x:50}},{{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'}},{find(6,'trích') - 0.1:.2f});
    tl.to('#i-s1',{{strokeDashoffset:0,duration:1.0,ease:'power1.inOut'}},{find(6,'trích') + 0.2:.2f});
    tl.fromTo('#i-v1',{{autoAlpha:0,scale:0.8}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(1.8)'}},{find(6,'1.400'):.2f});
    tl.fromTo('#i-r2',{{autoAlpha:0,x:50}},{{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'}},{find(6,'và') - 0.2:.2f});
    tl.to('#i-s2',{{strokeDashoffset:0,duration:0.7,ease:'power1.inOut'}},{find(6,'và') - 0.1:.2f});
    tl.fromTo('#i-v2',{{autoAlpha:0,scale:0.8}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(1.8)'}},{find(6,'500'):.2f});
{smash(t_tax - 0.1)}
    tl.fromTo('#i-tax',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},{t_tax - 0.05:.2f});
""")
sfx += [('whoosh-short.mp3', FS[5] - 0.1, 0.5, 0.3), ('pop.mp3', FS[5] + find(6, '1.400'), 0.4, 0.26),
        ('click-soft.mp3', FS[5] + t_tax - 0.1, 0.3, 0.4)]

# ---------------- 07 CTA (fixed brand layout) ----------------
d = FD[6]
t_q = find(7, 'Theo')
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:330px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-ctx { display:inline-flex; align-items:center; gap:12px; margin-top:26px; padding:10px 20px; border-radius:10px; border:1.5px solid rgba(255,255,255,0.18); font-weight:600; font-size:24px; color:rgba(255,255,255,0.8); opacity:0; }
.t-ctx .rc { width:20px; height:20px; border-radius:50%; border:3px solid #FF5A1F; }
.t-head { margin-top:34px; font-weight:900; font-size:64px; line-height:1.14; color:#fff; }
.t-head .ln { overflow:hidden; } .t-head .ln > span { display:block; }
.t-head .o { color:#FF5A1F; } .t-head .r { color:#FF4438; }
.t-opts { display:flex; justify-content:center; align-items:stretch; gap:20px; margin-top:70px; }
.t-opt { flex:1; max-width:400px; padding:46px 24px; border-radius:18px; border:2px solid; opacity:0; }
.t-opt.up { border-color:rgba(255,90,31,0.8); background:rgba(255,90,31,0.10); }
.t-opt.down { border-color:rgba(255,68,56,0.8); background:rgba(255,68,56,0.10); }
.t-opt .emo { width:48px; height:48px; margin:0 auto; position:relative; }
.t-opt.up .emo { border:4px solid #FF5A1F; border-radius:50%; }
.t-opt.up .emo::after { content:""; position:absolute; left:50%; top:13px; width:12px; height:12px; border-top:4px solid #FF5A1F; border-right:4px solid #FF5A1F; transform:translateX(-50%) rotate(-45deg); }
.t-opt.down .emo::before { content:""; position:absolute; left:0; bottom:0; width:0; height:0; border-left:24px solid transparent; border-right:24px solid transparent; border-bottom:44px solid #FF4438; }
.t-opt.down .emo::after { content:"!"; position:absolute; left:0; right:0; bottom:-2px; text-align:center; font-weight:900; font-size:26px; color:#0B0E14; }
.t-opt .lab { margin-top:18px; font-weight:800; font-size:34px; line-height:1.2; color:#fff; }
.t-vs { display:flex; align-items:center; font-weight:900; font-size:34px; color:rgba(255,255,255,0.35); opacity:0; }
.t-cta { display:inline-flex; align-items:center; gap:18px; margin-top:76px; padding:24px 40px; border-radius:100px; background:#FF5A1F; opacity:0; }
.t-cta .ico { width:40px; height:40px; flex:none; border-radius:12px 12px 12px 4px; background:#fff; position:relative; }
.t-cta .ico::before { content:""; position:absolute; left:9px; top:12px; right:9px; height:4px; border-radius:2px; background:#FF5A1F; box-shadow:0 9px 0 #FF5A1F; }
.t-cta span { font-weight:800; font-size:36px; letter-spacing:0.01em; color:#0B0E14; }
.t-sign { position:absolute; left:0; right:0; top:1450px; display:flex; align-items:center; justify-content:center; gap:14px; opacity:0; }
.t-sign .m { width:48px; height:48px; }
.t-sign .w { font-weight:800; font-size:32px; color:rgba(255,255,255,0.9); }
""", """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Giá xăng dầu · 6 kỳ giảm liên tiếp</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Xăng chỉ giảm nhẹ:</span></div>
        <div class="ln"><span id="t-h2" class="o">giảm sâu hơn ngay</span></div>
        <div class="ln"><span id="t-h3">hay <span class="r">trích quỹ dự phòng</span>?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Giảm sâu hơn ngay</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Trích quỹ dự phòng biến động</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>
""", f"""
    tl.fromTo('#t-kicker',{{autoAlpha:0,y:-12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},0);
    tl.fromTo('#t-ctx',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},0.15);
    tl.fromTo('#t-h1',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.3);
    tl.fromTo('#t-h2',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(7,'nên') - 0.1:.2f});
    tl.fromTo('#t-h3',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(7,'hay') - 0.05:.2f});
    tl.fromTo('#t-o1',{{autoAlpha:0,y:28,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'}},{find(7,'sâu') - 0.1:.2f});
    tl.fromTo('#t-vs',{{autoAlpha:0,scale:0.5}},{{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'}},{find(7,'hay'):.2f});
    tl.fromTo('#t-o2',{{autoAlpha:0,y:28,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'}},{find(7,'quỹ') - 0.05:.2f});
    tl.fromTo('#t-cta',{{autoAlpha:0,y:22}},{{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'}},{find(7,'Hãy') - 0.1:.2f});
    tl.to('#t-cta',{{keyframes:[{{scale:1.04,duration:0.45,ease:'sine.inOut'}},{{scale:1,duration:0.45,ease:'sine.inOut'}},{{scale:1.04,duration:0.45,ease:'sine.inOut'}},{{scale:1,duration:0.45,ease:'sine.inOut'}}]}},{find(7,'Hãy') + 0.4:.2f});
    tl.fromTo('#t-sign',{{autoAlpha:0}},{{autoAlpha:1,duration:0.4}},{find(7,'Hãy') + 0.2:.2f});
""")
sfx += [('whoosh-short.mp3', FS[6] - 0.1, 0.5, 0.3), ('chime.mp3', FS[6] + find(7, 'Hãy'), 1.0, 0.3)]

# ---------------- captions (karaoke) ----------------
FIX = {('7', 'sang'): 'xăng'}
caps_html, caps_js = [], []
cid = 0
for li in range(7):
    words = STT[li]
    base = FS[li] + LEAD
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        txt = ' '.join(x['text'] for x in cur)
        end_punct = w['text'][-1] in '.,?:'
        if len(cur) >= 6 or len(txt) > 26 or (end_punct and len(cur) >= 3):
            chunks.append(cur); cur = []
    if cur:
        if chunks and len(cur) <= 2:
            chunks[-1] += cur
        else:
            chunks.append(cur)
    for ci, ch in enumerate(chunks):
        st = base + ch[0]['start']
        en = base + ch[-1]['end'] + 0.3
        if ci + 1 < len(chunks):
            en = min(en, base + chunks[ci + 1][0]['start'] - 0.02)
        spans = []
        for wi, w in enumerate(ch):
            t = FIX.get((str(li + 1), w['text']), w['text'])
            spans.append(f'<span class="w" id="w{cid}_{wi}">{html.escape(t)}</span>')
            caps_js.append(f"tl.to('#w{cid}_{wi}',{{color:'#FF5A1F',duration:0.1,ease:'none'}},{base + w['start']:.2f});")
        caps_html.append(f'<div class="cap" id="cap{cid}">{" ".join(spans)}</div>')
        caps_js.insert(len(caps_js) - len(ch), f"tl.set('#cap{cid}',{{autoAlpha:1}},{st:.2f});tl.set('#cap{cid}',{{autoAlpha:0}},{en:.2f});")
        cid += 1

# ---------------- stars (seeded PRNG, deterministic) ----------------
def mulberry32(seed):
    def r():
        nonlocal seed
        seed = (seed + 0x6D2B79F5) & 0xFFFFFFFF
        t = seed
        t = ((t ^ (t >> 15)) * (1 | t)) & 0xFFFFFFFF
        t = (t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF) ^ t) & 0xFFFFFFFF
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return r
rnd = mulberry32(20261126)
stars = "".join(f'<circle cx="{rnd()*1080:.0f}" cy="{rnd()*1920:.0f}" r="{1.5 + rnd()*1.5:.1f}" fill="#fff" opacity="{0.15 + rnd()*0.25:.2f}"/>' for _ in range(40))

scenes = "\n".join(
    f'<div id="el-{fid}" class="scene clip" data-composition-id="{fid}" data-composition-src="compositions/frames/{fid}.html" data-start="{FS[i]}" data-duration="{FD[i]}" data-track-index="1"></div>'
    for i, fid in enumerate(frames))
voices = "\n".join(
    f'<audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{FS[i] + LEAD:.2f}" data-duration="{VD[i]:.3f}" data-track-index="10" data-audio-group="voiceover"></audio>'
    for i in range(7))
sfx_html = "\n".join(
    f'<audio id="el-sfx-{k}" src="assets/sfx/{s}" data-start="{max(0, st):.2f}" data-duration="{dd}" data-track-index="{32 if s[:5] == "click" else 30 + k % 2}" data-volume="{v}"></audio>'
    for k, (s, st, dd, v) in enumerate(sfx))
try:
    bgm_attrs = open('.bgm_attrs').read().strip()
except FileNotFoundError:
    bgm_attrs = ''

index = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920">
<script src="assets/vendor/gsap.min.js"></script>
<style>
{FONTS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000; }}
#root {{ position:relative; width:1080px; height:1920px; overflow:hidden; background:#0B0E14; font-family:"Montserrat",sans-serif; color:#fff; }}
.scene {{ position:absolute; inset:0; width:100%; height:100%; z-index:2; }}
#bg-depth {{ position:absolute; inset:0; overflow:hidden; z-index:0; }}
#bg-depth .blob {{ position:absolute; border-radius:50%; filter:blur(60px); }}
#bg-stars {{ position:absolute; inset:0; width:100%; height:100%; }}
#brand-anchor {{ position:absolute; inset:0; z-index:90; pointer-events:none; opacity:0; }}
#ba-source {{ position:absolute; left:44px; top:46px; display:inline-flex; align-items:center; gap:10px; padding:9px 16px; border-radius:8px; background:rgba(11,14,20,0.6); border:1px solid rgba(255,255,255,0.12); }}
#ba-source .dot {{ width:7px; height:7px; border-radius:50%; background:#FF5A1F; }}
#ba-source span {{ font-weight:500; font-size:21px; letter-spacing:0.02em; color:rgba(255,255,255,0.9); white-space:nowrap; }}
#ba-brand {{ position:absolute; right:40px; top:40px; display:inline-flex; align-items:center; gap:11px; }}
#ba-brand .mark {{ width:44px; height:44px; flex:none; }} #ba-brand .mark img {{ display:block; width:100%; height:100%; }}
#ba-brand .word {{ font-weight:800; font-size:24px; color:#fff; }}
#caps {{ position:absolute; left:80px; right:180px; top:1520px; height:110px; z-index:85; pointer-events:none; }}
.cap {{ position:absolute; left:0; right:0; top:0; text-align:center; font-weight:800; font-size:42px; line-height:1.2; color:rgba(255,255,255,0.92); text-shadow:0 2px 12px rgba(0,0,0,0.9), 0 0 4px rgba(0,0,0,0.9); opacity:0; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
<div id="bg-depth">
  <div class="blob" style="width:640px;height:640px;background:radial-gradient(circle,rgba(255,90,31,0.20),transparent 70%);top:-120px;left:-160px;"></div>
  <div class="blob" style="width:560px;height:560px;background:radial-gradient(circle,rgba(255,68,56,0.16),transparent 70%);top:900px;right:-200px;"></div>
  <div class="blob" style="width:520px;height:520px;background:radial-gradient(circle,rgba(255,90,31,0.12),transparent 70%);bottom:-180px;left:200px;"></div>
  <svg id="bg-stars" viewBox="0 0 1080 1920">{stars}</svg>
</div>
{scenes}
<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
<div id="caps">
{chr(10).join(caps_html)}
</div>
{voices}
{sfx_html}
<audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30" {bgm_attrs}></audio>
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.set('#brand-anchor',{{opacity:1}},{FD[0]});
tl.to('.blob',{{x:'+=40',y:'-=30',duration:18,ease:'sine.inOut',repeat:3,yoyo:true,stagger:3}},0);
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:{int(TOTAL // 4)},yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{chr(10).join(caps_js)}
window.__timelines['main'] = tl;
</script>
</body>
</html>
"""

for fid, s in frames.items():
    open(f'compositions/frames/{fid}.html', 'w', encoding='utf-8').write(s)
open('index.html', 'w', encoding='utf-8').write(index)
print('frames', FD, 'starts', FS, 'TOTAL', TOTAL)
