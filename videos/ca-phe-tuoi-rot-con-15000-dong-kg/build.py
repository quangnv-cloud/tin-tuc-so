#!/usr/bin/env python3
"""Build index.html + 7 frames for ca-phe-tuoi-rot-con-15000-dong-kg (style 1-card-and-bar).
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
FD[6] = round(FD[6] + 1.0, 2)  # CTA: voice + pulse + smooth end
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
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 50%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:760px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:28px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:124px; line-height:1.04; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
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
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Cà phê tươi</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">15.000 đ/kg</div></div>
      <div class="hk-sub" id="hk-sub">Chỉ còn khoảng · <b>giảm 40% so với cùng kỳ</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Được mùa: sản lượng +5%</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Mất giá: cà phê nhân −36%</div>
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


# ======================= STYLE 1-card-and-bar : 5 middle acts =======================
CB = """
.cb-kick { position:absolute; left:64px; top:300px; display:flex; align-items:center; gap:14px; font-weight:700; font-size:26px; letter-spacing:0.22em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.cb-kick .bar { width:36px; height:6px; border-radius:3px; background:#FF5A1F; }
.num { position:absolute; left:26px; top:22px; font-weight:800; font-size:22px; letter-spacing:0.1em; color:rgba(255,90,31,0.9); }
.hl { color:#FF5A1F; } .hr { color:#FF4438; }
.note { font-weight:500; font-size:22px; color:rgba(255,255,255,0.55); }
"""

# ---------------- 02 WHAT HAPPENED ----------------
d = FD[1]
t_prov = [find(2, 'Quảng'), find(2, 'Đắk'), find(2, 'Lâm'), find(2, 'Gia')]
t_loss = find(2, 'Nhiều')
frames['02-what'] = frame('02-what', CB + """
.w-img { position:absolute; left:64px; right:64px; top:370px; height:520px; border-radius:22px; overflow:hidden; border:1.5px solid rgba(255,255,255,0.14); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 60%; }
.w-panel { position:absolute; left:64px; right:64px; top:930px; }
.w-head { font-weight:900; font-size:64px; line-height:1.1; color:#fff; opacity:0; }
.w-sub { margin-top:16px; font-weight:600; font-size:31px; line-height:1.35; color:rgba(255,255,255,0.86); opacity:0; }
.w-provs { display:flex; flex-wrap:wrap; gap:14px; margin-top:28px; }
.w-prov { display:inline-flex; align-items:center; gap:10px; padding:12px 20px; border-radius:12px; background:#121724; border:1.5px solid rgba(255,90,31,0.6); font-weight:700; font-size:28px; color:#fff; opacity:0; }
.w-prov .pin { width:14px; height:14px; border-radius:50% 50% 50% 0; transform:rotate(-45deg); background:#FF5A1F; }
.w-loss { position:absolute; left:64px; right:64px; top:1320px; height:150px; display:flex; align-items:center; gap:26px; padding:0 34px; opacity:0; }
.w-loss .big { font-weight:900; font-size:72px; color:#FF4438; white-space:nowrap; }
.w-loss .txt { font-weight:700; font-size:30px; line-height:1.3; color:#fff; }
""", """
    <div id="content">
    <div class="cb-kick" id="w-kick"><span class="bar"></span>Chuyện gì xảy ra</div>
    <div class="w-img" id="w-img"><img src="assets/img/dt.jpg" alt=""><div class="credit">Ảnh: Dân Trí</div></div>
    <div class="w-panel">
      <div class="w-head" id="w-head">Được mùa, <span class="hr">mất giá</span></div>
      <div class="w-sub" id="w-sub">Cà phê nhân mất giá liên tục từ đầu tháng 11, kéo giá cà phê tươi đi xuống</div>
      <div class="w-provs">
        <div class="w-prov" id="w-p0"><span class="pin"></span>Quảng Ngãi</div>
        <div class="w-prov" id="w-p1"><span class="pin"></span>Đắk Lắk</div>
        <div class="w-prov" id="w-p2"><span class="pin"></span>Lâm Đồng</div>
        <div class="w-prov" id="w-p3"><span class="pin"></span>Gia Lai</div>
      </div>
    </div>
    <div class="card warn w-loss" id="w-loss"><div class="big">−25–30%</div><div class="txt">doanh thu của nhiều nông hộ dù sản lượng tăng</div></div>
    </div>
""", f"""
    tl.fromTo('#w-kick',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
    tl.fromTo('#w-img',{{autoAlpha:0,y:40,scale:0.97}},{{autoAlpha:1,y:0,scale:1,duration:0.6,ease:'power3.out'}},0.1);
    tl.to('#w-img img',{{scale:1.07,duration:{d},ease:'none'}},0);
    tl.fromTo('#w-head',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},0.35);
    tl.fromTo('#w-sub',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},{find(2,'cho'):.2f});
""" + "".join(f"    tl.fromTo('#w-p{k}',{{autoAlpha:0,y:14,scale:0.9}},{{autoAlpha:1,y:0,scale:1,duration:0.32,ease:'back.out(1.8)'}},{t_prov[k] - 0.05:.2f});\n" for k in range(4)) + f"""
    tl.fromTo('#w-loss',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{t_loss:.2f});
""")
sfx += [('whoosh-short.mp3', FS[1] - 0.05, 0.5, 0.25), ('pop.mp3', FS[1] + t_loss, 0.4, 0.3)]

# ---------------- 03 KEY FACTS ----------------
d = FD[2]
facts = [
    ('01', '25/11 · cà phê nhân', '69.500–70.000', 'đ/kg', 'Quảng Ngãi, Đắk Lắk, Lâm Đồng, Gia Lai', find(3, 'cà')),
    ('02', 'Cà phê tươi', '15.000–16.000', 'đ/kg', 'VnExpress · Dân Trí', find(3, 'Theo')),
    ('03', 'Mức giảm mỗi ngày (theo nông dân)', '200–500', 'đ/kg', 'giá cà phê tươi', find(3, '200')),
]
fact_html = "".join(f"""
      <div class="card f-card{' hot' if k == 0 else ''}" id="f{k}" style="top:{390 + k * 365}px;">
        <div class="num">{n}</div>
        <div class="f-lab">{lab}</div>
        <div class="f-val"><span class="v">{v}</span><span class="u">{u}</span></div>
        <div class="note f-note">{nt}</div>
      </div>""" for k, (n, lab, v, u, nt, _) in enumerate(facts))
frames['03-facts'] = frame('03-facts', CB + """
.f-card { left:64px; right:64px; height:330px; padding:66px 40px 0; overflow:hidden; opacity:0; }
.f-lab { font-weight:600; font-size:32px; color:rgba(255,255,255,0.8); }
.f-val { margin-top:12px; display:flex; align-items:baseline; gap:16px; }
.f-val .v { white-space:nowrap; font-weight:900; font-size:88px; line-height:1; color:#fff; letter-spacing:-0.01em; }
.f-card.hot .f-val .v { color:#FF5A1F; }
.f-val .u { font-weight:700; font-size:40px; color:rgba(255,255,255,0.75); }
.f-note { margin-top:16px; }
.f-card::after { content:""; position:absolute; left:0; top:0; bottom:0; width:6px; background:#FF5A1F; }
""", f"""
    <div id="content">
    <div class="cb-kick" id="f-kick"><span class="bar"></span>Các con số chính</div>{fact_html}
    </div>
""", f"""
    tl.fromTo('#f-kick',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
""" + "".join(f"    tl.fromTo('#f{k}',{{autoAlpha:0,x:-60,clipPath:'inset(0 100% 0 0)'}},{{autoAlpha:1,x:0,clipPath:'inset(0 0% 0 0)',duration:0.55,ease:'power3.out'}},{max(0.2, facts[k][5] - 0.25):.2f});\n" for k in range(3)))
sfx += [('click-soft.mp3', FS[2] + max(0.2, facts[k][5] - 0.25), 0.3, 0.3) for k in range(3)]

# ---------------- 04 DATA MOMENT ----------------
d = FD[3]
t17 = find(4, '17%')
t36 = find(4, '36%')
# bar heights proportional to source ratios: now = 0.64 x year-ago (−36%), now = 0.83 x month-ago (−17%)
H = 560
h_year, h_now = H, round(H * 0.64)
h_month = round(h_now / 0.83)
bars = [('Cùng kỳ 2025', h_year, '', 'b-old'), ('Tháng trước', h_month, '−17%', 'b-old'), ('25/11/2026', h_now, '69.500–70.000 đ', 'b-now')]
bar_html = "".join(f"""
        <div class="b-col"><div class="b-tag" id="bt{k}">{tag}</div><div class="b-bar {cls}" id="bb{k}" style="height:{hh}px"></div><div class="b-lab">{lab}</div></div>""" for k, (lab, hh, tag, cls) in enumerate(bars))
frames['04-data'] = frame('04-data', CB + """
.d-main { position:absolute; left:0; right:0; top:360px; text-align:center; }
.d-big { font-weight:900; font-size:220px; line-height:1; color:#FF4438; letter-spacing:-0.03em; opacity:0; }
.d-cap { margin-top:10px; font-weight:700; font-size:34px; color:#fff; opacity:0; }
.d-cap2 { margin-top:10px; font-weight:600; font-size:28px; color:rgba(255,255,255,0.7); opacity:0; }
.d-chart { position:absolute; left:100px; right:100px; top:760px; height:640px; display:flex; align-items:flex-end; justify-content:space-between; border-bottom:2px solid rgba(255,255,255,0.25); }
.b-col { width:240px; display:flex; flex-direction:column; align-items:center; position:relative; }
.b-bar { width:170px; border-radius:14px 14px 0 0; transform-origin:50% 100%; transform:scaleY(0); }
.b-old { background:linear-gradient(180deg, rgba(255,255,255,0.34), rgba(255,255,255,0.12)); }
.b-now { background:linear-gradient(180deg, #FF5A1F, #FF4438); box-shadow:0 0 40px rgba(255,90,31,0.3); }
.b-tag { margin-bottom:14px; font-weight:800; font-size:28px; color:#fff; white-space:nowrap; opacity:0; min-height:34px; }
.b-lab { position:absolute; top:100%; margin-top:16px; font-weight:700; font-size:26px; color:rgba(255,255,255,0.8); white-space:nowrap; }
""", f"""
    <div id="content">
    <div class="cb-kick" id="d-kick"><span class="bar"></span>Giá cà phê nhân</div>
    <div class="d-main">
      <div class="d-big" id="d-big">−<span id="d-n">0</span>%</div>
      <div class="d-cap" id="d-cap">so với cùng kỳ năm ngoái · <span class="hr">khoảng −40.000 đ/kg</span></div>
      <div class="d-cap2" id="d-cap2">So với tháng trước: <span class="hl">−16.000 đ/kg (−17%)</span></div>
    </div>
    <div class="d-chart">{bar_html}
    </div>
    </div>
""", f"""
    tl.fromTo('#d-kick',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
    tl.to('#bb0',{{scaleY:1,duration:0.7,ease:'power3.out'}},0.2);
    tl.to('#bb1',{{scaleY:1,duration:0.7,ease:'power3.out'}},0.45);
    tl.fromTo('#d-cap2',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{find(4,'16.000') - 0.1:.2f});
    tl.fromTo('#bt1',{{autoAlpha:0,y:10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},{t17 - 0.05:.2f});
    tl.to('#bb2',{{scaleY:1,duration:0.8,ease:'power3.out'}},{find(4,'ngoái') - 0.4:.2f});
    tl.fromTo('#bt2',{{autoAlpha:0,y:10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},{find(4,'ngoái') + 0.3:.2f});
    tl.fromTo('#d-big',{{autoAlpha:0,scale:0.8}},{{autoAlpha:1,scale:1,duration:0.5,ease:'back.out(1.6)'}},{find(4,'40.000') - 0.2:.2f});
    tl.fromTo('#d-cap',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{find(4,'40.000'):.2f});
    var cnt = {{v:0}};
    tl.to(cnt,{{v:36,duration:{round(t36 - find(4,'40.000') + 0.4, 2)},ease:'power2.out',onUpdate:function(){{ document.querySelector('#d-n').textContent = Math.round(cnt.v); }}}},{find(4,'40.000') - 0.2:.2f});
""")
sfx += [('click-soft.mp3', FS[3] + t17, 0.3, 0.3), ('impact-bass-1.mp3', FS[3] + find(4, '40.000') - 0.2, 0.6, 0.3)]

# ---------------- 05 CONTEXT (table) ----------------
d = FD[4]
T = round(find(5, 'Hiệp') - 0.12, 2)
rows = [
    ('Robusta sàn London', 'giảm 12 phiên liên tiếp', find(5, '12') - 0.1, 'hr'),
    ('Theo Reuters', 'thấp nhất trong 3 năm', find(5, 'Reuters'), 'hr'),
    ('Kỳ hạn 1/2027 · phiên 24/11', '2.813 USD/tấn', find(5, 'năm') + 0.1, ''),
    ('Sản lượng niên vụ 2026–2027', '~2,2 triệu tấn', find(5, '2,2') - 0.1, 'hl'),
    ('So với vụ trước', 'tăng hơn 5%', find(5, 'tăng') - 0.05, 'hl'),
]
row_html = "".join(f"""
        <div class="c-row" id="cr{k}"><div class="c-l">{l}</div><div class="c-v {cls}">{v}</div></div>""" for k, (l, v, _, cls) in enumerate(rows))
frames['05-context'] = frame('05-context', CB + """
.c-head { position:absolute; left:64px; right:64px; top:370px; font-weight:900; font-size:58px; line-height:1.12; color:#fff; opacity:0; }
.c-table { position:absolute; left:64px; right:64px; top:560px; padding:12px 36px; }
.c-row { display:flex; justify-content:space-between; align-items:center; gap:20px; padding:30px 0; border-bottom:1.5px solid rgba(255,255,255,0.12); opacity:0; }
.c-row:last-child { border-bottom:none; }
.c-l { font-weight:600; font-size:28px; color:rgba(255,255,255,0.72); }
.c-v { font-weight:800; font-size:36px; color:#fff; text-align:right; white-space:nowrap; }
.c-tag { position:absolute; left:64px; top:310px; }
.c-sec { position:absolute; left:64px; right:64px; top:1300px; height:150px; display:flex; align-items:center; gap:24px; padding:0 34px; opacity:0; }
.c-sec .cal { width:58px; height:58px; flex:none; border:4px solid #FF5A1F; border-radius:10px; position:relative; }
.c-sec .cal::before { content:""; position:absolute; left:-4px; right:-4px; top:-4px; height:16px; background:#FF5A1F; border-radius:8px 8px 0 0; }
.c-sec .txt { font-weight:700; font-size:30px; line-height:1.3; color:#fff; }
""", f"""
    <div id="content">
    <div class="cb-kick" id="c-kick"><span class="bar"></span>Vì sao giá giảm</div>
    <div class="c-head" id="c-head">Thế giới giảm, <span class="hl">nguồn cung</span> tăng</div>
    <div class="card c-table">{row_html}
    </div>
    <div class="card hot c-sec" id="c-sec"><div class="cal"></div><div class="txt">Cao điểm thu hoạch: giữa tháng 11 đến hết tháng 12</div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#c-kick',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
    tl.fromTo('#c-head',{{autoAlpha:0,y:20}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},0.2);
    tl.fromTo('.c-table',{{autoAlpha:0}},{{autoAlpha:1,duration:0.4}},0.3);
""" + "".join(f"    tl.fromTo('#cr{k}',{{autoAlpha:0,x:40}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},{max(0.4, rows[k][2]):.2f});\n" for k in range(len(rows))) + smash(T) + f"""
    tl.fromTo('#c-sec',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{find(5,'tấn'):.2f});
""")
sfx += [('click-soft.mp3', FS[4] + T, 0.3, 0.35), ('pop.mp3', FS[4] + find(5, 'tấn'), 0.4, 0.25)]

# ---------------- 06 IMPACT ----------------
d = FD[5]
frames['06-impact'] = frame('06-impact', CB + """
.i-head { position:absolute; left:64px; right:64px; top:370px; font-weight:900; font-size:56px; line-height:1.14; color:#fff; opacity:0; }
.i-cards { position:absolute; left:64px; right:64px; top:560px; height:560px; display:flex; gap:24px; }
.i-card { position:relative; flex:1; padding:44px 30px; opacity:0; }
.i-ico { width:76px; height:76px; position:relative; margin-bottom:30px; }
.i-ico.globe { border:5px solid #FF5A1F; border-radius:50%; }
.i-ico.globe::before { content:""; position:absolute; left:18px; right:18px; top:-5px; bottom:-5px; border:4px solid #FF5A1F; border-radius:50%; }
.i-ico.globe::after { content:""; position:absolute; left:-5px; right:-5px; top:30px; height:5px; background:#FF5A1F; }
.i-ico.ship::before { content:""; position:absolute; left:0; right:0; bottom:6px; height:30px; background:#FF5A1F; clip-path:polygon(0 0,100% 0,85% 100%,15% 100%); }
.i-ico.ship::after { content:""; position:absolute; left:22px; width:32px; bottom:40px; height:28px; border:5px solid #FF5A1F; border-radius:4px; }
.i-big { font-weight:900; font-size:96px; line-height:1; color:#FF5A1F; letter-spacing:-0.02em; }
.i-big.s { font-size:78px; }
.i-lab { margin-top:20px; font-weight:700; font-size:30px; line-height:1.3; color:#fff; }
.i-sub { margin-top:14px; }
.i-wide { position:absolute; left:64px; right:64px; top:1160px; height:290px; padding:40px 36px; opacity:0; }
.i-wide .lab { font-weight:600; font-size:28px; color:rgba(255,255,255,0.75); }
.i-wide .row { margin-top:16px; display:flex; align-items:baseline; gap:22px; }
.i-wide .v { font-weight:900; font-size:76px; color:#fff; }
.i-wide .g { font-weight:800; font-size:44px; color:#FF5A1F; }
""", """
    <div id="content">
    <div class="cb-kick" id="i-kick"><span class="bar"></span>Vị thế Việt Nam</div>
    <div class="i-head" id="i-head">Nguồn cung Việt Nam <span class="hl">dồi dào</span></div>
    <div class="i-cards">
      <div class="card hot i-card" id="i-c1"><div class="i-ico globe"></div><div class="i-big">~18%</div><div class="i-lab">nguồn cung cà phê toàn cầu</div><div class="note i-sub">VnExpress · Dân Trí</div></div>
      <div class="card i-card" id="i-c2"><div class="i-ico ship"></div><div class="i-big s">114.000 tấn</div><div class="i-lab">xuất khẩu tháng 10 · <span class="hl">+61%</span> so với cùng kỳ</div><div class="note i-sub">Dân Trí</div></div>
    </div>
    <div class="card i-wide" id="i-wide"><div class="lab">Lũy kế 10 tháng xuất khẩu</div><div class="row"><span class="v">1,57 triệu tấn</span><span class="g">+18,8%</span></div><div class="note" style="margin-top:12px">Dân Trí</div></div>
    </div>
""", f"""
    tl.fromTo('#i-kick',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
    tl.fromTo('#i-head',{{autoAlpha:0,y:20}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},0.15);
    tl.fromTo('#i-c1',{{autoAlpha:0,y:50}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},{find(6,'18%') - 0.25:.2f});
    tl.fromTo('#i-c2',{{autoAlpha:0,y:50}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},{find(6,'114.000') - 0.3:.2f});
    tl.fromTo('#i-wide',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},{find(6,'61%') + 0.2:.2f});
""")
sfx += [('whoosh-short.mp3', FS[5] - 0.05, 0.5, 0.22), ('pop.mp3', FS[5] + find(6, '18%') - 0.25, 0.4, 0.28), ('pop.mp3', FS[5] + find(6, '114.000') - 0.3, 0.4, 0.28)]

# ---------------- 07 CTA (fixed brand layout) ----------------
d = FD[6]
t_q = find(7, 'theo')
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:330px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-ctx { display:inline-flex; align-items:center; gap:12px; margin-top:26px; padding:10px 20px; border-radius:10px; border:1.5px solid rgba(255,255,255,0.18); font-weight:600; font-size:24px; color:rgba(255,255,255,0.8); opacity:0; }
.t-ctx .rc { width:20px; height:20px; border-radius:50%; border:3px solid #FF5A1F; }
.t-head { margin-top:34px; font-weight:900; font-size:64px; line-height:1.14; color:#fff; }
.t-head .ln { overflow:hidden; } .t-head .ln > span { display:block; }
.t-head .o { color:#FF5A1F; } .t-head .r { color:#FF4438; }
.t-opts { display:flex; justify-content:center; align-items:stretch; gap:20px; margin-top:110px; }
.t-opt { flex:1; max-width:400px; padding:56px 24px; border-radius:18px; border:2px solid; opacity:0; }
.t-opt.up { border-color:rgba(255,90,31,0.8); background:rgba(255,90,31,0.10); }
.t-opt.down { border-color:rgba(255,68,56,0.8); background:rgba(255,68,56,0.10); }
.t-opt .emo { width:48px; height:48px; margin:0 auto; position:relative; }
.t-opt.up .emo { border:4px solid #FF5A1F; border-radius:50%; }
.t-opt.up .emo::after { content:""; position:absolute; left:50%; top:13px; width:12px; height:12px; border-top:4px solid #FF5A1F; border-right:4px solid #FF5A1F; transform:translateX(-50%) rotate(-45deg); }
.t-opt.down .emo::before { content:""; position:absolute; left:0; bottom:0; width:0; height:0; border-left:24px solid transparent; border-right:24px solid transparent; border-bottom:44px solid #FF4438; }
.t-opt.down .emo::after { content:"!"; position:absolute; left:0; right:0; bottom:-2px; text-align:center; font-weight:900; font-size:26px; color:#0B0E14; }
.t-opt .lab { margin-top:18px; font-weight:800; font-size:34px; line-height:1.2; color:#fff; }
.t-vs { display:flex; align-items:center; font-weight:900; font-size:34px; color:rgba(255,255,255,0.35); opacity:0; }
.t-cta { display:inline-flex; align-items:center; gap:18px; margin-top:120px; padding:28px 46px; border-radius:100px; background:#FF5A1F; opacity:0; }
.t-cta .ico { width:40px; height:40px; flex:none; border-radius:12px 12px 12px 4px; background:#fff; position:relative; }
.t-cta .ico::before { content:""; position:absolute; left:9px; top:12px; right:9px; height:4px; border-radius:2px; background:#FF5A1F; box-shadow:0 9px 0 #FF5A1F; }
.t-cta span { font-weight:800; font-size:36px; letter-spacing:0.01em; color:#0B0E14; }
.t-sign { position:absolute; left:0; right:0; top:1460px; display:flex; align-items:center; justify-content:center; gap:14px; opacity:0; }
.t-sign .m { width:48px; height:48px; }
.t-sign .w { font-weight:800; font-size:32px; color:rgba(255,255,255,0.9); }
""", """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Giá cà phê · vụ thu hoạch 2026–2027</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Giá đầu vụ giảm sâu:</span></div>
        <div class="ln"><span id="t-h2" class="o">bán ngay thu hồi vốn</span></div>
        <div class="ln"><span id="t-h3">hay <span class="r">trữ chờ giá</span>?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Bán ngay, thu hồi vốn</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Phơi khô, trữ chờ giá phục hồi</div></div>
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
    tl.fromTo('#t-o1',{{autoAlpha:0,y:28,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'}},{find(7,'bán') - 0.1:.2f});
    tl.fromTo('#t-vs',{{autoAlpha:0,scale:0.5}},{{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'}},{find(7,'hay'):.2f});
    tl.fromTo('#t-o2',{{autoAlpha:0,y:28,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'}},{find(7,'phơi') - 0.05:.2f});
    tl.fromTo('#t-cta',{{autoAlpha:0,y:22}},{{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'}},{find(7,'Hãy') - 0.1:.2f});
    tl.to('#t-cta',{{keyframes:[{{scale:1.04,duration:0.45,ease:'sine.inOut'}},{{scale:1,duration:0.45,ease:'sine.inOut'}},{{scale:1.04,duration:0.45,ease:'sine.inOut'}},{{scale:1,duration:0.45,ease:'sine.inOut'}}]}},{find(7,'Hãy') + 0.4:.2f});
    tl.fromTo('#t-sign',{{autoAlpha:0}},{{autoAlpha:1,duration:0.4}},{find(7,'Hãy') + 0.2:.2f});
""")
sfx += [('whoosh-short.mp3', FS[6] - 0.1, 0.5, 0.3), ('chime.mp3', FS[6] + find(7, 'Hãy'), 1.0, 0.3)]

# ---------------- captions (karaoke) ----------------
FIX = {}
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
rnd = mulberry32(20261127)
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
<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress · Dân Trí</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
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
