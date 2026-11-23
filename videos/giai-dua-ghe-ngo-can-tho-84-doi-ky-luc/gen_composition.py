#!/usr/bin/env python3
"""Generate compositions + index.html for giai-dua-ghe-ngo-can-tho-84-doi-ky-luc (style 7-timeline-chronology)."""
import json, os, re, difflib, sys, subprocess, math

P = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.chdir(P)

VOFF = 0.10
VDUR = [float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                        f'assets/voice/line{i+1}.mp3']).decode().strip()) for i in range(7)]
PAD = [0.45, 0.4, 0.4, 0.45, 0.45, 0.45, 1.4]
DURS = [round(v + VOFF + p, 2) for v, p in zip(VDUR, PAD)]
STARTS = [0.0]
for d in DURS[:-1]:
    STARTS.append(round(STARTS[-1] + d, 2))
TOTAL = round(STARTS[-1] + DURS[-1], 2)


def T(x):  # voice-relative local time -> frame-local time
    return round(x + VOFF, 2)


FONTS = ""
for w in (400, 500, 600, 700, 800, 900):
    FONTS += ("@font-face{font-family:'Montserrat';font-weight:%d;src:url('assets/fonts/Montserrat-%d-latin.woff2') format('woff2');"
              "unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}\n" % (w, w))
    FONTS += ("@font-face{font-family:'Montserrat';font-weight:%d;src:url('assets/fonts/Montserrat-%d-vietnamese.woff2') format('woff2');"
              "unicode-range:U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;}\n" % (w, w))

BASE_CSS = """
#root { position:absolute; inset:0; width:100%; height:100%; overflow:hidden; font-family:"Montserrat",sans-serif; color:#fff; background:transparent; }
.kick { font-weight:700; font-size:26px; letter-spacing:0.22em; text-transform:uppercase; color:#FF5A1F; }
.num { font-variant-numeric: tabular-nums; }
.credit { position:absolute; right:14px; bottom:12px; padding:5px 10px; border-radius:6px; background:rgba(11,14,20,0.78); font-weight:500; font-size:18px; color:rgba(255,255,255,0.9); }
.ttl { position:absolute; left:64px; right:64px; font-weight:800; font-size:60px; line-height:1.14; letter-spacing:-0.01em; }
.ttl .ln { overflow:hidden; } .ttl .ln > span { display:block; }
.ttl b { color:#FF5A1F; font-weight:900; } .ttl b.r { color:#FF4438; }
.card { border-radius:20px; background:rgba(18,23,36,0.94); border:1px solid rgba(255,255,255,0.10); box-shadow:0 0 40px rgba(255,90,31,0.14); }
.axis-v { position:absolute; width:4px; border-radius:2px; background:linear-gradient(180deg,#FF5A1F,rgba(255,90,31,0.25)); transform-origin:50% 0%; transform:scaleY(0); }
.axis-h { position:absolute; height:4px; border-radius:2px; background:linear-gradient(90deg,rgba(255,90,31,0.25),#FF5A1F); transform-origin:0% 50%; transform:scaleX(0); }
.node { position:absolute; border-radius:50%; background:#0B0E14; border:5px solid #FF5A1F; box-shadow:0 0 24px rgba(255,90,31,0.45); transform:scale(0); }
.node::after { content:""; position:absolute; inset:7px; border-radius:50%; background:#FF5A1F; }
"""


def frame(cid, css, body, js):
    return f"""<template>
  <style>
{FONTS}{BASE_CSS}{css}
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


def count_js(var, el_id, to, t, dur=1.0, fmt='Math.round(o.v)'):
    return (f"    const {var} = {{ v: 0 }}; const {var}E = document.getElementById('{el_id}');\n"
            f"    tl.fromTo({var},{{v:0}},{{v:{to},duration:{dur},ease:'power2.out',onUpdate(){{ const o={var}; {var}E.textContent = {fmt}; }}}},{t});\n")


frames = {}

# ---------------- 01 HOOK (fixed brand layout) ----------------
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:920px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:55% 30%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0.0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:780px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:30px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:122px; line-height:1.02; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.hk-name.o { color:#FF5A1F; font-size:92px; }
.hk-sub { margin-top:24px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:30px; margin-top:52px; }
.hk-tag { font-weight:800; font-size:48px; line-height:1; color:#FF5A1F; opacity:0; white-space:nowrap; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: Tuổi Trẻ</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: Tuổi Trẻ, VTV · 23/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Đua ghe Ngo</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">Cần Thơ 2026</div></div>
      <div class="hk-sub" id="hk-sub">Lễ hội Oóc Om Bóc · <b>khởi tranh 23/11</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>84 đội · kỷ lục</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Gần 6.900 VĐV</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.6);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.85);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.5);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.3);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.65);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (ảnh + panel + badge mốc thời gian + thanh 4 ngày lễ hội) ----------------
D2 = DURS[1]
DAYS = [("21/11", "Khai mạc", T(3.86)), ("22/11", "", T(4.1)), ("23/11", "Khởi tranh", T(4.35)), ("24/11", "Chung kết", T(4.66))]
day_html, day_js = "", ""
for i, (d, lab, t) in enumerate(DAYS):
    x = 40 + i * 290
    day_html += (f'<div class="w-dn node" id="w-dn{i}" style="left:{x - 20}px;top:96px;width:44px;height:44px"></div>'
                 f'<div class="w-dl" id="w-dl{i}" style="left:{x - 80}px"><div class="d">{d}</div><div class="l">{lab}</div></div>\n')
    day_js += f"    tl.to('#w-dn{i}',{{scale:1,duration:0.35,ease:'back.out(2.2)'}},{t});\n"
    day_js += f"    tl.fromTo('#w-dl{i}',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},{t});\n"
frames['02-what'] = frame('02-what', """
.w-head { position:absolute; left:64px; top:190px; display:flex; align-items:center; gap:18px; }
.w-kick { opacity:0; }
.w-badge { padding:7px 16px; border-radius:30px; border:2px solid #FF5A1F; font-weight:800; font-size:24px; color:#fff; background:rgba(255,90,31,0.15); opacity:0; }
.w-ttl { top:240px; }
.w-img { position:absolute; left:64px; right:64px; top:420px; height:560px; border-radius:20px; overflow:hidden; opacity:0; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:55% 30%; }
.w-days { position:absolute; left:64px; right:64px; top:1020px; height:270px; opacity:0; }
.w-days .k { position:absolute; left:40px; top:30px; font-weight:700; font-size:22px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.w-days .axis-h { left:40px; width:870px; top:116px; }
.w-dl { position:absolute; top:160px; width:160px; text-align:center; opacity:0; }
.w-dl .d { font-weight:900; font-size:36px; color:#fff; }
.w-dl .l { margin-top:6px; font-weight:700; font-size:21px; color:#FF5A1F; min-height:26px; }
.w-chip { position:absolute; left:64px; right:64px; top:1320px; height:130px; display:flex; align-items:center; gap:24px; padding:0 36px; opacity:0; }
.w-chip .ic { width:52px; height:52px; flex:none; border-radius:50%; border:4px solid #FF5A1F; position:relative; }
.w-chip .ic::after { content:""; position:absolute; left:50%; top:50%; width:16px; height:16px; margin:-8px 0 0 -8px; border-radius:50%; background:#FF5A1F; }
.w-chip .t { font-weight:800; font-size:36px; line-height:1.2; color:#fff; }
.w-chip .t b { color:#FF5A1F; }
""", f"""
    <div class="w-head"><div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div><div class="w-badge" id="w-badge">21–24/11</div></div>
    <div class="ttl w-ttl"><div class="ln"><span id="w-h1">Lễ hội Oóc Om Bóc</span></div><div class="ln"><span id="w-h2"><b>Đua ghe Ngo</b> 2026</span></div></div>
    <div class="w-img" id="w-img"><img src="assets/img/article-hero.jpg" alt=""><div class="credit">Ảnh: Tuổi Trẻ</div></div>
    <div class="card w-days" id="w-days"><div class="k">4 ngày lễ hội</div><div class="axis-h" id="w-ax"></div>
{day_html}    </div>
    <div class="card w-chip" id="w-chip"><span class="ic"></span><div class="t">Gắn với <b>Ngày Văn hóa Việt Nam</b> 24/11</div></div>""", f"""
    tl.fromTo('#w-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#w-badge',{{autoAlpha:0,scale:0.7}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(2)'}},0.3);
    tl.fromTo('#w-h1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.15);
    tl.fromTo('#w-h2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.3);
    tl.fromTo('#w-img',{{autoAlpha:0,y:40}},{{autoAlpha:1,y:0,duration:0.6,ease:'power3.out'}},0.35);
    tl.fromTo('#w-img img',{{scale:1.14}},{{scale:1.0,duration:{D2},ease:'none'}},0.35);
    tl.fromTo('#w-days',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(2.9)});
    tl.to('#w-ax',{{scaleX:1,duration:1.0,ease:'power1.inOut'}},{T(3.8)});
{day_js}    tl.fromTo('#w-chip',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(5.7)});""")

# ---------------- 03 KEY FACTS (trục dọc 3 mốc, node nở khi fact xuất hiện) ----------------
FACTS = [
    ("21/11", "Tối 21/11", "Khai mạc <b>lễ hội</b>", "Công viên 30/4, phường Phú Lợi", T(0.06)),
    ("23/11", "Ngày 23/11", "<b>Vòng bảng</b> giải đua", "Sông Maspéro, phường Sóc Trăng", T(2.42)),
    ("24/11", "Ngày 24/11", "Vòng loại đến <b>chung kết</b>", "Cả nội dung nam và nữ", T(6.48)),
]
f_html, f_js = "", ""
for i, (_, k, v, s, t) in enumerate(FACTS):
    top = 450 + i * 340
    f_html += (f'<div class="node" id="f-n{i}" style="left:100px;top:{top + 100}px;width:56px;height:56px"></div>'
               f'<div class="card f-card" id="f-c{i}" style="top:{top}px"><div class="k">{k}</div><div class="v">{v}</div><div class="s">{s}</div></div>\n')
    f_js += f"    tl.to('#f-n{i}',{{scale:1,duration:0.4,ease:'back.out(2.4)'}},{t});\n"
    f_js += f"    tl.fromTo('#f-c{i}',{{autoAlpha:0,x:50}},{{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'}},{round(t + 0.08, 2)});\n"
frames['03-facts'] = frame('03-facts', """
.f-kick { position:absolute; left:64px; top:190px; opacity:0; }
.f-ttl { top:240px; }
.f-ax { left:126px; top:470px; height:1000px; }
.f-card { position:absolute; left:200px; right:64px; height:290px; padding:34px 40px; opacity:0; display:flex; flex-direction:column; justify-content:center; }
.f-card .k { font-weight:700; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:#FF5A1F; }
.f-card .v { margin-top:14px; font-weight:800; font-size:44px; line-height:1.2; color:#fff; }
.f-card .v b { color:#FF5A1F; font-weight:900; }
.f-card .s { margin-top:14px; font-weight:600; font-size:28px; color:rgba(255,255,255,0.65); }
""", f"""
    <div class="kick f-kick" id="f-kick">Lịch trình</div>
    <div class="ttl f-ttl"><div class="ln"><span id="f-t1">Ba mốc của</span></div><div class="ln"><span id="f-t2"><b>mùa giải 2026</b></span></div></div>
    <div class="axis-v f-ax" id="f-ax"></div>
{f_html}""", f"""
    tl.fromTo('#f-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#f-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#f-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.26);
    tl.to('#f-ax',{{scaleY:1,duration:{T(6.6)},ease:'none'}},0.1);
{f_js}""")

# ---------------- 04 DATA MOMENT (trục ngang vẽ dần, dừng ở node 84; cột nam/nữ tỉ lệ thật) ----------------
frames['04-data'] = frame('04-data', """
.d-kick { position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }
.d-glow { position:absolute; left:240px; top:250px; width:600px; height:520px; border-radius:50%; background:radial-gradient(circle, rgba(255,90,31,0.24), transparent 70%); opacity:0; }
.d-big { position:absolute; left:0; right:0; top:300px; text-align:center; opacity:0; }
.d-big .n { font-weight:900; font-size:290px; line-height:1.0; color:#fff; letter-spacing:-0.03em; }
.d-big .u { margin-top:28px; font-weight:800; font-size:46px; letter-spacing:0.06em; color:#FF5A1F; }
.d-ax { left:64px; width:476px; top:780px; }
.d-ax2 { left:540px; width:476px; top:780px; background:linear-gradient(90deg,#FF5A1F,rgba(255,90,31,0.1)); }
.d-node { left:508px; top:750px; width:64px; height:64px; }
.d-tag { position:absolute; left:0; right:0; top:840px; text-align:center; font-weight:700; font-size:26px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); opacity:0; }
.d-bars { position:absolute; left:64px; right:64px; top:910px; height:300px; padding:34px 40px; opacity:0; display:flex; flex-direction:column; justify-content:center; gap:34px; }
.d-row { display:flex; align-items:center; gap:22px; }
.d-row .k { width:150px; font-weight:800; font-size:34px; color:#fff; }
.d-row .tr { flex:1; height:56px; border-radius:12px; background:rgba(255,255,255,0.06); position:relative; overflow:hidden; }
.d-row .b { position:absolute; left:0; top:0; bottom:0; border-radius:12px; transform-origin:0% 50%; transform:scaleX(0); }
.d-row .v { width:120px; text-align:right; font-weight:900; font-size:52px; color:#FF5A1F; }
.d-ath { position:absolute; left:64px; right:64px; top:1240px; height:210px; padding:0 40px; display:flex; align-items:center; gap:30px; opacity:0; }
.d-ath .n { font-weight:900; font-size:84px; color:#FF5A1F; white-space:nowrap; }
.d-ath .t { font-weight:800; font-size:34px; line-height:1.25; color:#fff; }
.d-ath .t small { display:block; margin-top:6px; font-weight:600; font-size:26px; color:rgba(255,255,255,0.65); }
""", f"""
    <div class="kick d-kick" id="d-kick">Quy mô kỷ lục</div>
    <div class="d-glow" id="d-glow"></div>
    <div class="d-big" id="d-big"><div class="n num" id="d-n">0</div><div class="u">đội ghe nam, nữ</div></div>
    <div class="axis-h d-ax" id="d-ax"></div><div class="axis-h d-ax2" id="d-ax2"></div>
    <div class="node d-node" id="d-node"></div>
    <div class="d-tag" id="d-tag">Đông nhất từ trước đến nay</div>
    <div class="card d-bars" id="d-bars">
      <div class="d-row"><div class="k">Nam</div><div class="tr"><div class="b" id="d-b1" style="width:{67/84*100:.1f}%;background:linear-gradient(90deg,#FF5A1F,#FF7A45)"></div></div><div class="v num" id="d-v1">0</div></div>
      <div class="d-row"><div class="k">Nữ</div><div class="tr"><div class="b" id="d-b2" style="width:{17/84*100:.1f}%;background:linear-gradient(90deg,#FF4438,#FF5A1F)"></div></div><div class="v num" id="d-v2">0</div></div>
    </div>
    <div class="card d-ath" id="d-ath"><div class="n">~6.900</div><div class="t">vận động viên<small>Từ TP Cần Thơ và tỉnh Cà Mau</small></div></div>""", f"""
    tl.fromTo('#d-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.0);
    tl.to('#d-ax',{{scaleX:1,duration:0.7,ease:'power2.inOut'}},0.05);
    tl.to('#d-node',{{scale:1,duration:0.4,ease:'back.out(2.4)'}},{T(0.6)});
    tl.fromTo('#d-big',{{autoAlpha:0,scale:0.85}},{{autoAlpha:1,scale:1,duration:0.5,ease:'back.out(1.5)'}},{T(0.4)});
    tl.fromTo('#d-glow',{{autoAlpha:0}},{{autoAlpha:1,duration:0.8}},{T(0.5)});
{count_js('cn', 'd-n', 84, T(0.4), 1.0)}    tl.to('#d-ax2',{{scaleX:1,duration:0.6,ease:'power2.out'}},{T(1.0)});
    tl.fromTo('#d-tag',{{autoAlpha:0}},{{autoAlpha:1,duration:0.4}},{T(1.1)});
    tl.fromTo('#d-bars',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(1.4)});
    tl.to('#d-b1',{{scaleX:1,duration:0.8,ease:'power2.out'}},{T(1.6)});
{count_js('c1', 'd-v1', 67, T(1.6), 0.8)}    tl.to('#d-b2',{{scaleX:1,duration:0.6,ease:'power2.out'}},{T(2.7)});
{count_js('c2', 'd-v2', 17, T(2.7), 0.6)}    tl.fromTo('#d-ath',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(3.7)});""")

# ---------------- 05 CONTEXT (2 trục dọc song song: đường đi của đội nam / nữ qua vòng bảng) ----------------
LANES = [
    ("Nam", [("67", "đội", T(0.7)), ("1.200 m", "4 lượt đua", T(1.62)), ("32", "đội vào loại trực tiếp", T(3.34))]),
    ("Nữ", [("17", "đội", T(5.06)), ("1.000 m", "vòng bảng", T(5.66)), ("8", "đội vào tứ kết", T(6.56))]),
]
x_html, x_js = "", ""
for li, (name, steps) in enumerate(LANES):
    left = 64 + li * 488
    x_html += f'<div class="x-lane" style="left:{left}px"><div class="x-name" id="x-name{li}">{name}</div><div class="axis-v x-ax" id="x-ax{li}"></div>\n'
    x_js += f"    tl.fromTo('#x-name{li}',{{autoAlpha:0,y:-12}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},{round(steps[0][2] - 0.2, 2)});\n"
    x_js += f"    tl.to('#x-ax{li}',{{scaleY:1,duration:{round(steps[2][2] - steps[0][2] + 0.3, 2)},ease:'none'}},{steps[0][2]});\n"
    for si, (v, lab, t) in enumerate(steps):
        top = 120 + si * 370
        big = ' last' if si == 2 else ''
        x_html += (f'  <div class="node" id="x-n{li}{si}" style="left:8px;top:{top + 30}px;width:{50 + si * 8}px;height:{50 + si * 8}px"></div>'
                   f'<div class="x-step{big}" id="x-s{li}{si}" style="top:{top}px"><div class="v">{v}</div><div class="l">{lab}</div></div>\n')
        x_js += f"    tl.to('#x-n{li}{si}',{{scale:1,duration:0.35,ease:'back.out(2.4)'}},{t});\n"
        x_js += f"    tl.fromTo('#x-s{li}{si}',{{autoAlpha:0,x:30}},{{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'}},{round(t + 0.05, 2)});\n"
    x_html += '</div>\n'
frames['05-context'] = frame('05-context', """
.x-kick { position:absolute; left:64px; top:190px; opacity:0; }
.x-ttl { top:240px; }
.x-lanes { position:absolute; left:0; right:0; top:430px; height:1060px; }
.x-lane { position:absolute; top:0; width:464px; height:1060px; }
.x-name { position:absolute; left:0; top:0; padding:8px 22px; border-radius:30px; background:#FF5A1F; font-weight:800; font-size:30px; color:#0B0E14; opacity:0; }
.x-ax { left:32px; top:130px; height:850px; }
.x-step { position:absolute; left:100px; right:10px; opacity:0; }
.x-step .v { font-weight:900; font-size:72px; line-height:1; color:#fff; white-space:nowrap; }
.x-step .l { margin-top:10px; font-weight:700; font-size:28px; line-height:1.25; color:rgba(255,255,255,0.7); }
.x-step.last .v { color:#FF5A1F; font-size:96px; }
.x-step.last .l { color:#fff; }
""", f"""
    <div class="kick x-kick" id="x-kick">Thể thức vòng bảng</div>
    <div class="ttl x-ttl"><div class="ln"><span id="x-t1">Từ 84 đội,</span></div><div class="ln"><span id="x-t2">ai <b>đi tiếp</b>?</span></div></div>
    <div class="x-lanes">
{x_html}    </div>""", f"""
    tl.fromTo('#x-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#x-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#x-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.26);
{x_js}""")

# ---------------- 06 IMPACT (trục ngang 2025 → 2026, 2 node cuối phóng to thành 2 khối) ----------------
frames['06-impact'] = frame('06-impact', """
.i-kick { position:absolute; left:64px; top:190px; opacity:0; }
.i-ttl { top:240px; }
.i-ax { left:64px; top:500px; width:952px; }
.i-y { position:absolute; top:405px; font-weight:900; font-size:40px; color:rgba(255,255,255,0.5); opacity:0; }
.i-y.now { color:#FF5A1F; }
.i-n1 { left:150px; top:476px; width:52px; height:52px; border-color:rgba(255,255,255,0.5); }
.i-n2 { left:850px; top:470px; width:64px; height:64px; }
.i-delta { position:absolute; left:0; right:0; top:550px; text-align:center; opacity:0; }
.i-delta .a { display:inline-flex; align-items:center; gap:26px; font-weight:900; font-size:110px; color:#fff; }
.i-delta .a .from { color:rgba(255,255,255,0.45); }
.i-delta .a .arr { width:70px; height:6px; background:#FF5A1F; position:relative; }
.i-delta .a .arr::after { content:""; position:absolute; right:-4px; top:-12px; border-left:22px solid #FF5A1F; border-top:15px solid transparent; border-bottom:15px solid transparent; }
.i-delta .a .to { color:#FF5A1F; }
.i-delta .s { margin-top:6px; font-weight:700; font-size:30px; color:rgba(255,255,255,0.75); }
.i-delta .s b { color:#FF5A1F; }
.i-axv { left:538px; top:770px; height:120px; }
.i-blocks { position:absolute; left:64px; right:64px; top:900px; display:flex; gap:24px; }
.i-blk { flex:1; height:550px; padding:40px 34px; opacity:0; display:flex; flex-direction:column; }
.i-blk .k { font-weight:700; font-size:22px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.55); }
.i-blk .h { margin-top:18px; font-weight:800; font-size:44px; line-height:1.2; color:#fff; }
.i-blk .h b { color:#FF5A1F; }
.i-pills { margin-top:auto; display:flex; flex-direction:column; gap:14px; }
.i-pill { padding:14px 22px; border-radius:14px; border:2px solid rgba(255,90,31,0.7); background:rgba(255,90,31,0.10); font-weight:800; font-size:32px; color:#fff; opacity:0; }
.i-tv { margin-top:auto; display:flex; align-items:center; gap:20px; opacity:0; }
.i-tv .scr { width:96px; height:66px; flex:none; border-radius:10px; border:5px solid #FF5A1F; position:relative; }
.i-tv .scr::after { content:""; position:absolute; left:36px; top:14px; border-left:22px solid #FF5A1F; border-top:13px solid transparent; border-bottom:13px solid transparent; }
.i-tv .t { font-weight:800; font-size:32px; line-height:1.25; color:#fff; }
.i-tv .t small { display:block; font-weight:600; font-size:24px; color:rgba(255,255,255,0.65); }
""", f"""
    <div class="kick i-kick" id="i-kick">Điểm mới năm nay</div>
    <div class="ttl i-ttl"><div class="ln"><span id="i-t1">Đường đua nữ</span></div><div class="ln"><span id="i-t2"><b>rộng mở hơn</b></span></div></div>
    <div class="axis-h i-ax" id="i-ax"></div>
    <div class="i-y" id="i-y1" style="left:120px">2025</div><div class="i-y now" id="i-y2" style="left:825px">2026</div>
    <div class="node i-n1" id="i-n1"></div><div class="node i-n2" id="i-n2"></div>
    <div class="i-delta" id="i-delta"><div class="a"><span class="from num">8</span><span class="arr"></span><span class="to num">17</span></div><div class="s">đội nữ · <b>tăng thêm 9 đội</b></div></div>
    <div class="axis-v i-axv" id="i-axv"></div>
    <div class="i-blocks">
      <div class="card i-blk" id="i-b1"><div class="k">Ngày hội chung</div><div class="h">Của đồng bào <b>các dân tộc</b></div>
        <div class="i-pills"><div class="i-pill" id="i-p1">Kinh</div><div class="i-pill" id="i-p2">Khmer</div><div class="i-pill" id="i-p3">Hoa</div></div></div>
      <div class="card i-blk" id="i-b2"><div class="k">Phủ sóng</div><div class="h">Truyền hình <b style="white-space:nowrap">trực tiếp</b></div>
        <div class="i-tv" id="i-tv"><span class="scr"></span><div class="t">VTV5 · VTV6<br>VTV9 · VTV10<small>và ứng dụng VTVGo</small></div></div></div>
    </div>""", f"""
    tl.fromTo('#i-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#i-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#i-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.26);
    tl.to('#i-n1',{{scale:1,duration:0.35,ease:'back.out(2.4)'}},{T(0.4)});
    tl.fromTo('#i-y1',{{autoAlpha:0}},{{autoAlpha:1,duration:0.3}},{T(0.4)});
    tl.to('#i-ax',{{scaleX:1,duration:1.4,ease:'power1.inOut'}},{T(0.5)});
    tl.to('#i-n2',{{scale:1,duration:0.4,ease:'back.out(2.4)'}},{T(1.8)});
    tl.fromTo('#i-y2',{{autoAlpha:0}},{{autoAlpha:1,duration:0.3}},{T(1.8)});
    tl.fromTo('#i-delta',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.45,ease:'back.out(1.6)'}},{T(2.1)});
    tl.to('#i-axv',{{scaleY:1,duration:0.4,ease:'power2.out'}},{T(3.2)});
    tl.fromTo('#i-b1',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(3.3)});
    tl.fromTo('#i-p1',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.3,ease:'power2.out'}},{T(5.1)});
    tl.fromTo('#i-p2',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.3,ease:'power2.out'}},{T(5.5)});
    tl.fromTo('#i-p3',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.3,ease:'power2.out'}},{T(6.15)});
    tl.fromTo('#i-b2',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(6.8)});
    tl.fromTo('#i-tv',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{T(7.5)});""")

# ---------------- 07 CTA (fixed brand layout) ----------------
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:330px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-ctx { display:inline-flex; align-items:center; gap:12px; margin-top:26px; padding:10px 20px; border-radius:10px; border:1.5px solid rgba(255,255,255,0.18); font-weight:600; font-size:24px; color:rgba(255,255,255,0.8); opacity:0; }
.t-ctx .rc { width:20px; height:20px; border-radius:50%; border:3px solid #FF5A1F; }
.t-head { margin-top:34px; font-weight:900; font-size:64px; line-height:1.14; color:#fff; }
.t-head .ln { overflow:hidden; } .t-head .ln > span { display:block; }
.t-head .o { color:#FF5A1F; }
.t-opts { display:flex; justify-content:center; align-items:stretch; gap:20px; margin-top:76px; }
.t-opt { flex:1; max-width:400px; padding:50px 24px; border-radius:18px; border:2px solid; opacity:0; }
.t-opt.up { border-color:rgba(255,90,31,0.8); background:rgba(255,90,31,0.10); }
.t-opt.down { border-color:rgba(255,68,56,0.8); background:rgba(255,68,56,0.10); }
.t-opt .emo { width:48px; height:48px; margin:0 auto; position:relative; }
.t-opt.up .emo { border:4px solid #FF5A1F; border-radius:50%; }
.t-opt.up .emo::after { content:""; position:absolute; left:50%; top:13px; width:12px; height:12px; border-top:4px solid #FF5A1F; border-right:4px solid #FF5A1F; transform:translateX(-50%) rotate(-45deg); }
.t-opt.down .emo::before { content:""; position:absolute; left:0; bottom:0; width:0; height:0; border-left:24px solid transparent; border-right:24px solid transparent; border-bottom:44px solid #FF4438; }
.t-opt.down .emo::after { content:"!"; position:absolute; left:0; right:0; bottom:-2px; text-align:center; font-weight:900; font-size:26px; color:#0B0E14; }
.t-opt .lab { margin-top:18px; font-weight:800; font-size:34px; line-height:1.2; color:#fff; }
.t-vs { display:flex; align-items:center; font-weight:900; font-size:34px; color:rgba(255,255,255,0.35); opacity:0; }
.t-cta { display:inline-flex; align-items:center; gap:18px; margin-top:80px; padding:24px 40px; border-radius:100px; background:#FF5A1F; opacity:0; }
.t-cta .ico { width:40px; height:40px; flex:none; border-radius:12px 12px 12px 4px; background:#fff; position:relative; }
.t-cta .ico::before { content:""; position:absolute; left:9px; top:12px; right:9px; height:4px; border-radius:2px; background:#FF5A1F; box-shadow:0 9px 0 #FF5A1F; }
.t-cta span { font-weight:800; font-size:36px; letter-spacing:0.01em; color:#0B0E14; }
.t-sign { position:absolute; left:0; right:0; top:1420px; display:flex; align-items:center; justify-content:center; gap:14px; opacity:0; }
.t-sign .m { width:48px; height:48px; }
.t-sign .w { font-weight:800; font-size:32px; color:rgba(255,255,255,0.9); }
""", """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Đua ghe Ngo Cần Thơ 2026 · 84 đội</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Đua ghe Ngo kỷ lục:</span></div>
        <div class="ln"><span id="t-h2" class="o">cơ hội quảng bá văn hóa</span></div>
        <div class="ln"><span id="t-h3">hay lo thương mại hóa?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Quảng bá văn hóa, hút du khách</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Lễ hội dễ bị thương mại hóa</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>""", """
    tl.fromTo('#t-kicker',{autoAlpha:0,y:-12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0);
    tl.fromTo('#t-ctx',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.15);
    tl.fromTo('#t-h1',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.3);
    tl.fromTo('#t-h2',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.46);
    tl.fromTo('#t-h3',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.62);
    tl.fromTo('#t-o1',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},%(o1)s);
    tl.fromTo('#t-vs',{autoAlpha:0,scale:0.5},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'},%(vs)s);
    tl.fromTo('#t-o2',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},%(o2)s);
    tl.fromTo('#t-cta',{autoAlpha:0,y:22},{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'},%(cta)s);
    tl.to('#t-cta',{keyframes:[{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'},{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'}]},%(pulse)s);
    tl.fromTo('#t-sign',{autoAlpha:0},{autoAlpha:1,duration:0.4},%(sign)s);""" % dict(
    o1=T(1.8), vs=T(2.9), o2=T(3.3), cta=T(5.4), pulse=round(T(5.4) + 0.5, 2), sign=T(5.8)))

SFX = [
    ("hook", "impact-bass-1", 0.6, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("days", "pop", STARTS[1] + T(3.86), 0.4, 0.22),
    ("f2", "click-soft", STARTS[2] + T(2.42), 0.35, 0.3),
    ("f3", "click-soft", STARTS[2] + T(6.48), 0.35, 0.3),
    ("big", "impact-bass-1", STARTS[3] + T(0.6), 0.6, 0.3),
    ("x32", "pop", STARTS[4] + T(3.34), 0.4, 0.24),
    ("x8", "pop", STARTS[4] + T(6.56), 0.4, 0.24),
    ("i1", "click-soft", STARTS[5] + T(2.1), 0.35, 0.3),
    ("o1", "pop", STARTS[6] + T(1.8), 0.35, 0.3),
    ("o2", "pop", STARTS[6] + T(3.3), 0.35, 0.3),
    ("cta", "chime", STARTS[6] + T(5.4), 1.2, 0.32),
]
TRK = {a: (31 if a in ("big", "hook", "f3", "i1", "x8") else 30) for a, *_ in SFX}
SOURCE_TEXT = "Nguồn: Tuổi Trẻ, VTV"
SEED = 20261123
DISPLAY = {"Ma-xpê-rô.": "Maspéro."}

exec(open('gen_tail.py', encoding='utf-8').read())
