#!/usr/bin/env python3
"""Build index.html + 7 frames for tphcm-mua-trai-mua-cong-ngan-trieu-10000-ty (style 2-chip-and-leaderboard).
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
PADS = [PAD] * 6 + [1.1]   # CTA: let the pill pulse finish + smooth ending
FD = [round(LEAD + VD[i] + PADS[i], 2) for i in range(7)]
FS = [0.0]
for i in range(6):
    FS.append(round(FS[-1] + FD[i], 2))
TOTAL = round(FS[-1] + FD[-1], 2)


def wt(line, idx):
    return round(LEAD + STT[line - 1][idx]['start'], 2)


def find(line, text, nth=0):
    hits = [k for k, w in enumerate(STT[line - 1]) if w['text'].strip('.,?:').lower() == text.lower()]
    if len(hits) <= nth:
        raise SystemExit(f'word not found: line {line} {text!r} #{nth}')
    return wt(line, hits[nth])


COMMON = """
#root { position:absolute; inset:0; width:100%; height:100%; overflow:hidden; font-family:"Montserrat",sans-serif; color:#fff; background:transparent; font-variant-numeric:tabular-nums; }
#content { position:absolute; inset:0; transform-origin:50% 45%; }
.kick { position:absolute; left:64px; top:300px; display:flex; align-items:center; gap:14px; font-weight:700; font-size:26px; letter-spacing:0.22em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.kick .bar { width:36px; height:4px; border-radius:2px; background:#FF5A1F; }
.credit { position:absolute; right:14px; bottom:12px; padding:5px 10px; border-radius:6px; background:rgba(11,14,20,0.78); font-weight:500; font-size:18px; color:rgba(255,255,255,0.9); }
.chip { display:inline-flex; align-items:center; gap:12px; padding:16px 26px; border-radius:14px; border:2px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.08); font-weight:800; font-size:34px; color:#fff; box-shadow:0 0 30px rgba(255,90,31,0.12); opacity:0; white-space:nowrap; }
.chip b { color:#FF5A1F; font-weight:900; }
.chip.warn { border-color:rgba(255,68,56,0.85); background:rgba(255,68,56,0.08); box-shadow:0 0 30px rgba(255,68,56,0.12); }
.chip.warn b { color:#FF4438; }
.wm { position:absolute; left:0; right:0; text-align:center; font-weight:900; line-height:1; letter-spacing:-0.05em; color:rgba(255,90,31,0.07); opacity:0; white-space:nowrap; }
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
    return f"""    tl.fromTo('#cutflash',{{opacity:0}},{{opacity:0.55,duration:0.05,ease:'none'}},{T:.2f});
    tl.to('#cutflash',{{opacity:0,duration:0.16,ease:'power1.in'}},{T + 0.05:.2f});
    tl.fromTo('#content',{{scale:1}},{{scale:0.986,duration:0.06,ease:'power1.out'}},{T:.2f});
    tl.to('#content',{{scale:1,duration:0.14,ease:'power2.out'}},{T + 0.061:.3f});
"""


frames = {}
sfx = []   # (src, abs_start, dur, vol)

# ---------------- 01 HOOK (fixed brand layout) ----------------
d = FD[0]
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:880px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 40%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.3) 0%, rgba(11,14,20,0) 38%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:740px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:26px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:100px; line-height:1.04; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.hk-name.o { font-size:150px; color:#FF5A1F; }
.hk-sub { margin-top:18px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:26px; margin-top:40px; }
.hk-tag { font-weight:800; font-size:46px; line-height:1; color:#FF5A1F; opacity:0; white-space:nowrap; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: VnExpress</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress · 28/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Cống ngăn triều</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">10.000 tỷ</div></div>
      <div class="hk-sub" id="hk-sub">Mưa trái mùa giữa mùa khô · <b>trùng triều cường</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Rốn ngập nay khô ráo</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Vùng bảo vệ chưa khép kín</div>
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

# ---------------- 02 WHAT HAPPENED (image + panel + 2 chips) ----------------
d = FD[1]
frames['02-what'] = frame('02-what', """
.w-img { position:absolute; left:64px; right:64px; top:360px; height:600px; border-radius:20px; overflow:hidden; box-shadow:0 0 40px rgba(255,90,31,0.14); border:1.5px solid rgba(255,255,255,0.12); opacity:0; }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 45%; }
.w-head { position:absolute; left:64px; right:64px; top:1010px; font-weight:800; font-size:60px; line-height:1.14; }
.w-head .ln { overflow:hidden; padding-bottom:4px; } .w-head .ln > span { display:block; }
.w-head b { color:#FF5A1F; font-weight:900; }
.w-sub { position:absolute; left:64px; right:64px; top:1262px; font-weight:600; font-size:30px; line-height:1.3; color:rgba(255,255,255,0.72); opacity:0; }
.w-chips { position:absolute; left:64px; right:64px; top:1340px; display:flex; gap:20px; }
""", """
    <div id="content">
      <div class="kick" id="w-k"><span class="bar"></span>Mưa trái mùa · Nam Bộ</div>
      <div class="w-img" id="w-img"><img src="assets/img/tt.jpg" alt=""><div class="credit">Ảnh: Tuổi Trẻ</div></div>
      <div class="w-head" data-layout-allow-overlap>
        <div class="ln"><span id="w-h1">Mưa dông giữa mùa khô,</span></div>
        <div class="ln"><span id="w-h2">chủ đầu tư <b>đóng cống</b></span></div>
        <div class="ln"><span id="w-h3">chủ động chống ngập</span></div>
      </div>
      <div class="w-sub" id="w-sub" data-layout-allow-overlap>Dự báo: Đài KTTV Nam Bộ · đóng cống chiều 28/11</div>
      <div class="w-chips"><div class="chip" id="w-c1"><b>27 – 29/11</b>đợt mưa dông</div><div class="chip" id="w-c2">Dự báo <b>&gt;100 mm</b></div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#w-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.05);
    tl.fromTo('#w-img',{{autoAlpha:0,y:40,scale:0.97}},{{autoAlpha:1,y:0,scale:1,duration:0.6,ease:'power3.out'}},0.12);
    tl.to('#w-img img',{{scale:1.07,duration:{d},ease:'none'}},0);
    tl.fromTo('#w-h1',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(2,'đợt') - 0.1:.2f});
    tl.fromTo('#w-sub',{{autoAlpha:0,y:14}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},{find(2,'Đài'):.2f});
    tl.fromTo('#w-c1',{{autoAlpha:0,y:16,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.6)'}},{find(2,'27') - 0.1:.2f});
    tl.fromTo('#w-c2',{{autoAlpha:0,y:16,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.6)'}},{find(2,'trên') - 0.05:.2f});
{smash(find(2, 'Chiều') - 0.1)}
    tl.fromTo('#w-h2',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(2,'chủ'):.2f});
    tl.fromTo('#w-h3',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(2,'chủ', 1) - 0.1:.2f});
""")
sfx += [('whoosh-short.mp3', FS[1] - 0.1, 0.5, 0.3), ('pop.mp3', FS[1] + find(2, '27') - 0.1, 0.4, 0.28),
        ('pop.mp3', FS[1] + find(2, 'trên') - 0.05, 0.4, 0.24), ('click-soft.mp3', FS[1] + find(2, 'Chiều') - 0.1, 0.3, 0.4)]

# ---------------- 03 KEY FACTS (watermark giant number + 3 stacked facts) ----------------
d = FD[2]
facts = [
    ("01", "6 cống lớn <span class='p'>+</span> 2 cống nhỏ", "Bến Nghé, Tân Thuận, Phú Xuân, Mương Chuối, Cây Khô, Phú Định", find(3, 'sáu')),
    ("02", "~570 km<sup>2</sup>", "Vùng kiểm soát ngập do triều · khoảng 6,5 triệu người hưởng lợi", find(3, 'khoảng')),
    ("03", "3 trạm bơm · ~120 m<sup>3</sup>/s", "Tổng công suất tại các cống Bến Nghé, Tân Thuận, Phú Định", find(3, 'ba')),
]
f_html, f_js = "", ""
for k, (no, big, sub, t) in enumerate(facts):
    top = 380 + k * 336
    hot = ' hot' if k == 1 else ''
    f_html += f"""
      <div class="f-card{hot}" id="f-r{k}" style="top:{top}px;"><div class="f-no">{no}</div><div class="f-big">{big}</div><div class="f-sub">{sub}</div></div>"""
    f_js += f"    tl.fromTo('#f-r{k}',{{autoAlpha:0,x:70}},{{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'}},{t - 0.12:.2f});\n"
    sfx.append(('pop.mp3', FS[2] + t - 0.12, 0.4, 0.26))
frames['03-facts'] = frame('03-facts', """
.f-card { position:absolute; left:64px; right:64px; height:304px; border-radius:20px; background:rgba(18,23,36,0.92); border:1.5px solid rgba(255,255,255,0.12); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.f-card.hot { border:2px solid rgba(255,90,31,0.85); }
.f-no { position:absolute; left:34px; top:30px; padding:6px 14px; border-radius:8px; border:1.5px solid rgba(255,90,31,0.8); font-weight:800; font-size:22px; letter-spacing:0.1em; color:#FF5A1F; }
.f-big { position:absolute; left:34px; right:34px; top:92px; font-weight:900; font-size:68px; line-height:1.05; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.f-card.hot .f-big { color:#FF5A1F; font-size:96px; top:84px; }
.f-big .p { color:#FF5A1F; } .f-big sup { font-size:0.5em; vertical-align:0.8em; }
.f-sub { position:absolute; left:34px; right:34px; top:206px; font-weight:600; font-size:28px; line-height:1.3; color:rgba(255,255,255,0.72); }
.f-foot { position:absolute; left:64px; top:1418px; }
""", f"""
    <div class="wm" id="f-wm" style="top:640px;font-size:560px;">570</div>
    <div id="content">
      <div class="kick" id="f-k"><span class="bar"></span>Quy mô hệ thống</div>
{f_html}
      <div class="f-foot"><div class="chip" id="f-foot">Hơn <b>1/4</b> diện tích TP HCM trước sáp nhập</div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#f-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#f-wm',{{autoAlpha:0,scale:0.92}},{{autoAlpha:1,scale:1,duration:1.2,ease:'power2.out'}},0.1);
    tl.to('#f-wm',{{y:-40,duration:{d},ease:'none'}},0);
{f_js}{smash(facts[2][3] - 0.14)}
    tl.fromTo('#f-foot',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.45,ease:'back.out(1.5)'}},{find(3,'triệu') - 0.1:.2f});
""")
sfx += [('whoosh-short.mp3', FS[2] - 0.1, 0.5, 0.3), ('click-soft.mp3', FS[2] + facts[2][3] - 0.14, 0.3, 0.4)]

# ---------------- 04 DATA MOMENT (leaderboard of tide peaks) ----------------
d = FD[3]
t_big = find(4, '1,65') - 0.15
rows = [  # label, sub, value, display, cls
    ("Phú An", "Đỉnh lịch sử · 11/2025", 1.78, "1,78 m", "dim"),
    ("Nhà Bè", "Chiều 25/11/2026", 1.66, "1,66 m", ""),
    ("Phú An", "25/11 · vượt báo động III 5 cm", 1.65, "1,65 m", "hot"),
    ("Phú An", "Dự báo tối 27/11/2026", 1.58, "1,58 m", "dim"),
]
r_html, r_js = "", ""
for k, (nm, sub, v, disp, cls) in enumerate(rows):
    top = 690 + k * 140
    w = v / 1.78 * 100
    r_html += f"""
      <div class="lb-row {cls}" id="lb-r{k}" style="top:{top}px;"><div class="lb-rank">{k + 1}</div><div class="lb-nm">{nm}<small>{sub}</small></div><div class="lb-trk"><div class="lb-fill" id="lb-f{k}" style="width:{w:.1f}%"></div></div><div class="lb-v">{disp}</div></div>"""
    ts = t_big + 0.7 + k * 0.22
    r_js += f"""    tl.fromTo('#lb-r{k}',{{autoAlpha:0,x:-40}},{{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'}},{ts:.2f});
    tl.fromTo('#lb-f{k}',{{scaleX:0}},{{scaleX:1,duration:0.8,ease:'power2.out'}},{ts + 0.15:.2f});
"""
t_gap = find(4, 'nhưng') - 0.1
frames['04-data'] = frame('04-data', """
.d-lab { position:absolute; left:64px; right:64px; top:350px; font-weight:700; font-size:36px; color:rgba(255,255,255,0.82); opacity:0; }
.d-lab b { color:#fff; font-weight:900; }
.d-num { position:absolute; left:64px; top:436px; display:flex; align-items:baseline; gap:16px; opacity:0; }
.d-num .n { font-weight:900; font-size:210px; line-height:1; letter-spacing:-0.04em; color:#FF5A1F; text-shadow:0 0 40px rgba(255,90,31,0.35); }
.d-num .u { font-weight:800; font-size:72px; color:rgba(255,255,255,0.85); }
.lb-row { position:absolute; left:64px; right:64px; height:120px; border-radius:16px; background:rgba(18,23,36,0.9); border:1.5px solid rgba(255,255,255,0.1); opacity:0; }
.lb-row.hot { border:2px solid rgba(255,90,31,0.9); background:rgba(255,90,31,0.10); box-shadow:0 0 40px rgba(255,90,31,0.18); }
.lb-rank { position:absolute; left:24px; top:36px; width:48px; height:48px; border-radius:50%; border:2px solid rgba(255,255,255,0.3); text-align:center; line-height:44px; font-weight:800; font-size:24px; color:#fff; }
.lb-row.hot .lb-rank { border-color:#FF5A1F; background:#FF5A1F; color:#0B0E14; }
.lb-nm { position:absolute; left:94px; top:18px; width:330px; font-weight:800; font-size:34px; color:#fff; }
.lb-nm small { display:block; margin-top:6px; font-weight:600; font-size:19px; line-height:1.25; color:rgba(255,255,255,0.78); }
.lb-row.hot .lb-nm small { color:#FF5A1F; }
.lb-trk { position:absolute; left:440px; right:200px; top:46px; height:28px; border-radius:14px; background:rgba(255,255,255,0.07); overflow:hidden; }
.lb-fill { height:100%; border-radius:14px; background:rgba(255,255,255,0.35); transform-origin:left center; }
.lb-row.hot .lb-fill { background:linear-gradient(90deg,#FF5A1F,#FF4438); }
.lb-row.dim .lb-fill { background:rgba(255,255,255,0.22); }
.lb-v { position:absolute; right:26px; top:34px; font-weight:900; font-size:44px; color:#fff; }
.lb-row.hot .lb-v { color:#FF5A1F; }
.lb-cap { position:absolute; left:64px; right:64px; top:1258px; font-weight:500; font-size:22px; color:rgba(255,255,255,0.7); opacity:0; }
.d-gap { position:absolute; left:64px; right:64px; top:1310px; height:200px; border-radius:20px; border:2px solid rgba(255,68,56,0.85); background:rgba(255,68,56,0.08); box-shadow:0 0 40px rgba(255,68,56,0.14); opacity:0; }
.d-gap .tg { position:absolute; left:34px; top:28px; font-weight:700; font-size:22px; letter-spacing:0.16em; color:#FF4438; }
.d-gap .tx { position:absolute; left:34px; top:70px; width:430px; font-weight:800; font-size:36px; line-height:1.2; color:#fff; }
.d-gap .v { position:absolute; right:34px; top:56px; font-weight:900; font-size:86px; line-height:1; color:#FF4438; }
.d-gap .v small { font-size:44px; margin-left:6px; }
""", f"""
    <div id="content">
      <div class="kick" id="d-k"><span class="bar"></span>Bảng đỉnh triều · sông Sài Gòn</div>
      <div class="d-lab" id="d-lab">Đỉnh triều <b>Phú An</b> · ngày đầu vận hành liên hoàn</div>
      <div class="d-num" id="d-num"><span class="n" id="d-n">0,00</span><span class="u">m</span></div>
{r_html}
      <div class="lb-cap" id="lb-cap">Thanh tỉ lệ theo mực nước thực đo / dự báo · Đài KTTV Nam Bộ</div>
      <div class="d-gap" id="d-gap"><div class="tg">CHÊNH LỆCH HAI PHÍA CỐNG</div><div class="tx">Cống giữ nước sông lớn ngoài vùng bảo vệ</div><div class="v">1–2,05<small>m</small></div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#d-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#d-lab',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{find(4,'ngày') - 0.1:.2f});
    tl.fromTo('#d-num',{{autoAlpha:0,scale:0.9}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(1.6)'}},{t_big - 0.5:.2f});
    const c = {{v:0}}; const numEl = document.querySelector('#d-n');
    tl.fromTo(c,{{v:0}},{{v:1.65,duration:1.0,ease:'power2.out',onUpdate(){{ numEl.textContent = c.v.toFixed(2).replace('.', ','); }}}},{t_big - 0.5:.2f});
{r_js}    tl.fromTo('#lb-cap',{{autoAlpha:0}},{{autoAlpha:1,duration:0.4}},{t_big + 1.6:.2f});
{smash(t_gap)}
    tl.fromTo('#d-gap',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'}},{t_gap + 0.05:.2f});
""")
sfx += [('whoosh-short.mp3', FS[3] - 0.1, 0.5, 0.3), ('impact-bass-1.mp3', FS[3] + t_big + 0.5, 0.6, 0.32),
        ('click-soft.mp3', FS[3] + t_gap, 0.3, 0.4)]

# ---------------- 05 CONTEXT (aerial banner + 3 big chips stacked) ----------------
d = FD[4]
cchips = [
    ("+31–38 cm", "Đỉnh triều Phú An, Nhà Bè tăng trung bình", "Giai đoạn 2000–2025 · Đài KTTV Nam Bộ", "", find(5, 'tăng') - 0.1),
    ("2016", "Khởi công dự án ngăn triều", "Ban đầu dự kiến xong sau 2 năm", "", find(5, 'khởi') - 0.1),
    ("3 lần dừng", "Kéo dài 5 năm tạm ngưng", "Theo chủ đầu tư Trung Nam Group", "warn", find(5, 'dừng') - 0.1),
]
c_html, c_js = "", ""
for k, (big, t1, t2, cls, t) in enumerate(cchips):
    top = 700 + k * 262
    c_html += f"""
      <div class="cc {cls}" id="cc{k}" style="top:{top}px;"><div class="cc-big">{big}</div><div class="cc-tx">{t1}<small>{t2}</small></div></div>"""
    c_js += f"    tl.fromTo('#cc{k}',{{autoAlpha:0,x:-60}},{{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'}},{t:.2f});\n"
    sfx.append(('pop.mp3', FS[4] + t, 0.4, 0.25))
frames['05-context'] = frame('05-context', """
.c-img { position:absolute; left:64px; right:64px; top:360px; height:300px; border-radius:20px; overflow:hidden; border:1.5px solid rgba(255,255,255,0.12); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.c-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 50%; }
.cc { position:absolute; left:64px; right:64px; height:232px; border-radius:20px; border:2px solid rgba(255,90,31,0.85); background:rgba(18,23,36,0.92); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.cc.warn { border-color:rgba(255,68,56,0.85); box-shadow:0 0 40px rgba(255,68,56,0.14); }
.cc-big { position:absolute; left:34px; top:0; bottom:0; display:flex; align-items:center; font-weight:900; font-size:66px; letter-spacing:-0.03em; color:#FF5A1F; white-space:nowrap; }
.cc.warn .cc-big { color:#FF4438; font-size:62px; }
.cc-tx { position:absolute; left:440px; right:30px; top:50%; transform:translateY(-50%); font-weight:800; font-size:32px; line-height:1.2; color:#fff; }
.cc-tx small { display:block; margin-top:10px; font-weight:600; font-size:22px; line-height:1.3; color:rgba(255,255,255,0.6); }
""", f"""
    <div id="content">
      <div class="kick" id="c-k"><span class="bar"></span>Bối cảnh · 25 năm triều cường</div>
      <div class="c-img" id="c-img"><img src="assets/img/dt.jpg" alt=""><div class="credit">Ảnh: Dân Trí</div></div>
{c_html}
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#c-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#c-img',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'}},0.1);
    tl.to('#c-img img',{{scale:1.08,duration:{d},ease:'none'}},0);
{c_js}{smash(find(5, 'Còn') - 0.1)}
""")
sfx += [('whoosh-short.mp3', FS[4] - 0.1, 0.5, 0.3), ('click-soft.mp3', FS[4] + find(5, 'Còn') - 0.1, 0.3, 0.4)]

# ---------------- 06 IMPACT (2 big chips + watermark) ----------------
d = FD[5]
t_but = find(6, 'Tuy') - 0.1
frames['06-impact'] = frame('06-impact', """
.ic { position:absolute; left:64px; right:64px; height:420px; border-radius:22px; border:2px solid rgba(255,90,31,0.9); background:rgba(18,23,36,0.92); box-shadow:0 0 40px rgba(255,90,31,0.16); opacity:0; }
.ic.warn { border-color:rgba(255,68,56,0.9); box-shadow:0 0 40px rgba(255,68,56,0.16); }
.ic .tg { position:absolute; left:40px; top:36px; display:flex; align-items:center; gap:12px; font-weight:700; font-size:24px; letter-spacing:0.16em; color:#FF5A1F; }
.ic.warn .tg { color:#FF4438; }
.ic .pin { width:22px; height:22px; border-radius:50% 50% 50% 0; transform:rotate(-45deg); background:currentColor; }
.ic .ti { position:absolute; left:40px; right:40px; top:96px; font-weight:900; font-size:66px; line-height:1.08; color:#fff; }
.ic .ti b { color:#FF5A1F; } .ic.warn .ti b { color:#FF4438; }
.ic .sb { position:absolute; left:40px; right:40px; top:268px; font-weight:600; font-size:28px; line-height:1.35; color:rgba(255,255,255,0.72); }
.ic .ok { position:absolute; right:40px; top:28px; width:52px; height:52px; border-radius:50%; border:4px solid #FF5A1F; }
.ic .ok::after { content:""; position:absolute; left:14px; top:6px; width:12px; height:22px; border-right:5px solid #FF5A1F; border-bottom:5px solid #FF5A1F; transform:rotate(45deg); }
.ic .wr { position:absolute; right:40px; top:28px; width:0; height:0; border-left:28px solid transparent; border-right:28px solid transparent; border-bottom:50px solid #FF4438; }
.ic .wr::after { content:"!"; position:absolute; left:-10px; top:14px; width:20px; text-align:center; font-weight:900; font-size:30px; color:#0B0E14; }
.i-note { position:absolute; left:64px; top:1360px; }
""", f"""
    <div class="wm" id="i-wm" style="top:900px;font-size:300px;">28/11</div>
    <div id="content">
      <div class="kick" id="i-k"><span class="bar"></span>Ghi nhận thực tế</div>
      <div class="ic" id="ic1" style="top:380px;"><div class="tg"><span class="pin"></span>Trần Xuân Soạn · chiều 28/11</div><div class="ok"></div><div class="ti">Không còn <b>ngập do triều</b></div><div class="sb">Nơi trước đây thường ngập nhất; nước mưa có đọng nhưng rút nhanh (Tuổi Trẻ)</div></div>
      <div class="ic warn" id="ic2" style="top:840px;"><div class="tg"><span class="pin"></span>Chân cầu Phú Mỹ · đợt triều 25/11</div><div class="wr"></div><div class="ti">Vẫn bị <b>nước dâng</b></div><div class="sb">Vùng bảo vệ chưa khép kín, đoạn hở nằm ngoài phạm vi dự án (VnExpress)</div></div>
      <div class="i-note"><div class="chip" id="i-note">Sở NN&amp;MT đề xuất thêm <b>19 công trình</b></div></div>
    </div>
    <div class="cutflash" id="cutflash"></div>
""", f"""
    tl.fromTo('#i-k',{{autoAlpha:0,x:-16}},{{autoAlpha:1,x:0,duration:0.4,ease:'power2.out'}},0.02);
    tl.fromTo('#i-wm',{{autoAlpha:0,scale:0.92}},{{autoAlpha:1,scale:1,duration:1.2,ease:'power2.out'}},0.1);
    tl.to('#i-wm',{{y:-40,duration:{d},ease:'none'}},0);
    tl.fromTo('#ic1',{{autoAlpha:0,x:-70}},{{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'}},{find(6,'đường') - 0.15:.2f});
{smash(t_but)}
    tl.fromTo('#ic2',{{autoAlpha:0,x:70}},{{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'}},{t_but + 0.05:.2f});
    tl.fromTo('#i-note',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.45,ease:'back.out(1.5)'}},{find(6,'vùng') - 0.05:.2f});
""")
sfx += [('whoosh-short.mp3', FS[5] - 0.1, 0.5, 0.3), ('pop.mp3', FS[5] + find(6, 'đường') - 0.15, 0.4, 0.26),
        ('click-soft.mp3', FS[5] + t_but, 0.3, 0.4)]

# ---------------- 07 CTA (fixed brand layout) ----------------
d = FD[6]
t_hay = find(7, 'Hãy')
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:330px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-ctx { display:inline-flex; align-items:center; gap:12px; margin-top:26px; padding:10px 20px; border-radius:10px; border:1.5px solid rgba(255,255,255,0.18); font-weight:600; font-size:24px; color:rgba(255,255,255,0.8); opacity:0; }
.t-ctx .rc { width:20px; height:20px; border-radius:50%; border:3px solid #FF5A1F; }
.t-head { margin-top:34px; font-weight:900; font-size:66px; line-height:1.14; color:#fff; }
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
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Cống ngăn triều 10.000 tỷ · TP HCM</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Cống 10.000 tỷ:</span></div>
        <div class="ln"><span id="t-h2" class="o">lời giải chống ngập</span></div>
        <div class="ln"><span id="t-h3">hay <span class="r">mới là bước đầu</span>?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Đã là lời giải chống ngập</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Mới chỉ là bước đầu</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>
""", f"""
    tl.fromTo('#t-kicker',{{autoAlpha:0,y:-12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},0);
    tl.fromTo('#t-ctx',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},0.15);
    tl.fromTo('#t-h1',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.3);
    tl.fromTo('#t-h2',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(7,'lời') - 0.1:.2f});
    tl.fromTo('#t-o1',{{autoAlpha:0,y:28,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'}},{find(7,'chống') - 0.05:.2f});
    tl.fromTo('#t-h3',{{yPercent:118}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{find(7,'hay') - 0.05:.2f});
    tl.fromTo('#t-vs',{{autoAlpha:0,scale:0.5}},{{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'}},{find(7,'hay'):.2f});
    tl.fromTo('#t-o2',{{autoAlpha:0,y:28,scale:0.92}},{{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'}},{find(7,'bước') - 0.05:.2f});
    tl.fromTo('#t-cta',{{autoAlpha:0,y:22}},{{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'}},{t_hay - 0.1:.2f});
    tl.to('#t-cta',{{keyframes:[{{scale:1.04,duration:0.45,ease:'sine.inOut'}},{{scale:1,duration:0.45,ease:'sine.inOut'}},{{scale:1.04,duration:0.45,ease:'sine.inOut'}},{{scale:1,duration:0.45,ease:'sine.inOut'}}]}},{t_hay + 0.4:.2f});
    tl.fromTo('#t-sign',{{autoAlpha:0}},{{autoAlpha:1,duration:0.4}},{t_hay + 0.2:.2f});
""")
sfx += [('whoosh-short.mp3', FS[6] - 0.1, 0.5, 0.3), ('chime.mp3', FS[6] + t_hay, 1.0, 0.3)]

# ---------------- captions (karaoke) ----------------
FIX = {('1', 'thành'): 'Thành', ('1', 'phố'): 'phố', ('2', 'milimet.'): 'mm.', ('3', 'kilomet'): 'km²', ('5', 'centimet.'): 'cm.'}
SKIP_NEXT = {('3', 'vuông')}   # merged into "km²"
caps_html, caps_js = [], []
cid = 0
for li in range(7):
    words = [w for w in STT[li] if (str(li + 1), w['text']) not in SKIP_NEXT]
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
        en = min(en, FS[li] + FD[li] - 0.02) if li < 6 else en
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


rnd = mulberry32(20261128)
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
#caps {{ position:absolute; left:80px; right:180px; top:1540px; height:110px; z-index:85; pointer-events:none; }}
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
<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress, Tuổi Trẻ</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
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
