#!/usr/bin/env python3
"""Generate compositions + index.html for nha-o-xa-hoi-ban-lai-dung-doi-tuong-1-7-2027 (style 6-ring-progress)."""
import json, os, re, difflib, sys, subprocess, math

P = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.chdir(P)

VOFF = 0.10
VDUR = [float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                        f'assets/voice/line{i+1}.mp3']).decode().strip()) for i in range(7)]
PAD = [0.45, 0.4, 0.4, 0.45, 0.45, 0.45, 1.3]
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
.ring { position:relative; flex:none; }
.ring svg { position:absolute; inset:0; width:100%; height:100%; overflow:visible; }
.ring .in { position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
"""


def ring(rid, size, stroke, color, track='rgba(255,255,255,0.10)', ticks=0, inner=''):
    """SVG radial: track + arc (hidden via dashoffset=C) + optional segment ticks. Returns (html, C)."""
    r = (size - stroke) / 2
    c = size / 2
    C = round(2 * math.pi * r, 2)
    tk = ''
    for k in range(ticks):
        a = -math.pi / 2 + 2 * math.pi * k / ticks
        x1, y1 = c + (r - stroke) * math.cos(a), c + (r - stroke) * math.sin(a)
        x2, y2 = c + (r + stroke) * math.cos(a), c + (r + stroke) * math.sin(a)
        tk += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#0B0E14" stroke-width="{max(4, stroke // 4)}"/>'
    html = (f'<div class="ring" id="{rid}" style="width:{size}px;height:{size}px">'
            f'<svg viewBox="0 0 {size} {size}"><circle cx="{c}" cy="{c}" r="{r}" fill="none" stroke="{track}" stroke-width="{stroke}"/>'
            f'<circle class="arc" cx="{c}" cy="{c}" r="{r}" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="butt" '
            f'stroke-dasharray="{C}" stroke-dashoffset="{C}" transform="rotate(-90 {c} {c})"/>{tk}</svg>'
            f'<div class="in">{inner}</div></div>')
    return html, C


def ring_js(rid, C, pct, t, dur=0.9, ease='power2.out'):
    return f"    tl.fromTo('#{rid} .arc',{{strokeDashoffset:{C}}},{{strokeDashoffset:{round(C * (1 - pct), 2)},duration:{dur},ease:'{ease}'}},{t});\n"


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


frames = {}

# ---------------- 01 HOOK (fixed brand layout) ----------------
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:900px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 40%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0.0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:760px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:30px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:118px; line-height:1.02; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.hk-name.o { color:#FF5A1F; font-size:88px; }
.hk-sub { margin-top:26px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:30px; margin-top:56px; }
.hk-tag { font-weight:800; font-size:48px; line-height:1; color:#FF5A1F; opacity:0; white-space:nowrap; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: Dân Trí</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: Dân Trí · 21/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Nhà ở xã hội</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">hết bán lại tự do</div></div>
      <div class="hk-sub" id="hk-sub">Luật Nhà ở (sửa đổi) vừa được <b>Quốc hội thông qua</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Hiệu lực từ 1/7/2027</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Chỉ bán đúng đối tượng</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.6);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.85);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.5);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.4);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.7);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (ảnh + badge nguồn dạng vòng + 3 ô số + vòng 96%) ----------------
D2 = DURS[1]
r96, C96 = ring('w-r96', 150, 14, '#FF5A1F', inner='<div style="font-weight:900;font-size:40px;color:#fff" class="num"><span id="w-96n">0</span>%</div>')
frames['02-what'] = frame('02-what', """
.w-kick { position:absolute; left:64px; top:190px; opacity:0; }
.w-ttl { top:240px; }
.w-img { position:absolute; left:64px; right:64px; top:430px; height:560px; border-radius:20px; overflow:hidden; opacity:0; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 35%; }
.w-src { position:absolute; left:26px; top:26px; display:flex; align-items:center; gap:14px; padding:10px 20px 10px 10px; border-radius:60px; background:rgba(11,14,20,0.82); opacity:0; }
.w-src .rc { width:62px; height:62px; border-radius:50%; border:3px solid #FF5A1F; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:22px; color:#FF5A1F; }
.w-src .t { font-weight:700; font-size:26px; color:#fff; }
.w-src .t small { display:block; font-weight:600; font-size:18px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.w-tiles { position:absolute; left:64px; right:64px; top:1030px; display:flex; gap:20px; }
.w-tile { flex:1; height:200px; padding:28px 24px; opacity:0; display:flex; flex-direction:column; justify-content:center; }
.w-tile .v { font-weight:900; font-size:64px; line-height:1; color:#FF5A1F; white-space:nowrap; }
.w-tile .v.s { font-size:46px; }
.w-tile .k { margin-top:14px; font-weight:700; font-size:22px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.65); }
.w-vote { position:absolute; left:64px; right:64px; top:1260px; height:210px; display:flex; align-items:center; gap:34px; padding:0 34px; opacity:0; }
.w-vote .t { font-weight:800; font-size:38px; line-height:1.2; color:#fff; }
.w-vote .t b { color:#FF5A1F; }
.w-vote .t small { display:block; margin-top:8px; font-weight:600; font-size:22px; color:rgba(255,255,255,0.6); }
""", f"""
    <div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div>
    <div class="ttl w-ttl"><div class="ln"><span id="w-h1">Quốc hội thông qua</span></div><div class="ln"><span id="w-h2"><b>Luật Nhà ở</b> sửa đổi</span></div></div>
    <div class="w-img" id="w-img"><img src="assets/img/tuoitre.jpg" alt=""><div class="credit">Ảnh: Tuổi Trẻ</div>
      <div class="w-src" id="w-src"><div class="rc">21/11</div><div class="t"><small>Biểu quyết</small>Sáng 21/11/2026</div></div>
    </div>
    <div class="w-tiles">
      <div class="card w-tile" id="w-t1"><div class="v num">13</div><div class="k">Chương</div></div>
      <div class="card w-tile" id="w-t2"><div class="v num">129</div><div class="k">Điều</div></div>
      <div class="card w-tile" id="w-t3"><div class="v s num">1/7/2027</div><div class="k">Hiệu lực</div></div>
    </div>
    <div class="card w-vote" id="w-vote">{r96}<div class="t">Hơn <b>96%</b> đại biểu tham gia biểu quyết tán thành<small>Theo VnExpress</small></div></div>""", f"""
    tl.fromTo('#w-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#w-h1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.15);
    tl.fromTo('#w-h2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.3);
    tl.fromTo('#w-img',{{autoAlpha:0,y:40}},{{autoAlpha:1,y:0,duration:0.6,ease:'power3.out'}},0.35);
    tl.fromTo('#w-img img',{{scale:1.14}},{{scale:1.0,duration:{D2},ease:'none'}},0.35);
    tl.fromTo('#w-src',{{autoAlpha:0,x:-30}},{{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'}},{T(0.4)});
    tl.fromTo('#w-vote',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(3.2)});
{ring_js('w-r96', C96, 0.96, T(3.4), 1.2)}    const c96 = {{ v: 0 }}; const n96 = document.getElementById('w-96n');
    tl.fromTo(c96,{{v:0}},{{v:96,duration:1.2,ease:'power2.out',onUpdate(){{ n96.textContent = Math.round(c96.v); }}}},{T(3.4)});
    tl.fromTo('#w-t1',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'}},{T(7.0)});
    tl.fromTo('#w-t2',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'}},{T(8.0)});
    tl.fromTo('#w-t3',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'}},{T(8.5)});""")

# ---------------- 03 KEY FACTS (3 fact + mini radial) ----------------
FACTS = [
    ('f-r1', 1.0, '#FF5A1F', '<div class="rv">5</div><div class="ru">năm</div>', 'Mốc tính', 'Từ ngày <b>trả đủ tiền</b> mua, thuê mua nhà', T(0.0)),
    ('f-r2', 1.0, '#FF5A1F', '<div class="rv">2</div><div class="ru">bên mua</div>', 'Chỉ được bán lại cho', '<b>Chủ đầu tư</b> hoặc <b>người thuộc diện</b> được mua nhà ở xã hội', T(1.9)),
    ('f-r3', 1.0, '#FF4438', '<div class="rv">≤</div><div class="ru">giá gốc</div>', 'Giá bán tối đa', 'Bằng giá trong <b class="r">hợp đồng ban đầu</b> với chủ đầu tư', T(5.4)),
]
f_html, f_js = "", ""
for i, (rid, pct, col, inner, k, v, t) in enumerate(FACTS):
    rh, C = ring(rid, 150, 14, col, inner=inner)
    f_html += f'<div class="card f-row" id="f-row{i}">{rh}<div class="tx"><div class="k">{k}</div><div class="v">{v}</div></div></div>\n'
    f_js += f"    tl.fromTo('#f-row{i}',{{autoAlpha:0,x:-50}},{{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'}},{t});\n"
    f_js += ring_js(rid, C, pct, round(t + 0.15, 2), 0.8)
frames['03-facts'] = frame('03-facts', """
.f-kick { position:absolute; left:64px; top:190px; opacity:0; }
.f-ttl { top:240px; }
.f-list { position:absolute; left:64px; right:64px; top:450px; display:flex; flex-direction:column; gap:30px; }
.f-row { display:flex; align-items:center; gap:36px; height:300px; padding:0 40px; opacity:0; }
.f-row .rv { font-weight:900; font-size:52px; line-height:1; color:#fff; }
.f-row .ru { margin-top:4px; font-weight:700; font-size:18px; letter-spacing:0.06em; color:rgba(255,255,255,0.7); }
.f-row .tx { flex:1; }
.f-row .k { font-weight:700; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.f-row .v { margin-top:12px; font-weight:800; font-size:40px; line-height:1.22; color:#fff; }
.f-row .v b { color:#FF5A1F; font-weight:900; } .f-row .v b.r { color:#FF4438; }
""", f"""
    <div class="kick f-kick" id="f-kick">5 năm đầu</div>
    <div class="ttl f-ttl"><div class="ln"><span id="f-t1">Chỉ bán lại</span></div><div class="ln"><span id="f-t2"><b>đúng đối tượng</b>, đúng giá</span></div></div>
    <div class="f-list">
{f_html}    </div>""", f"""
    tl.fromTo('#f-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#f-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#f-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.26);
{f_js}""")

# ---------------- 04 DATA MOMENT (vòng radial khổng lồ 5 năm + 3 điều kiện sau mốc) ----------------
big, CB = ring('d-big', 600, 40, '#FF5A1F', ticks=5,
               inner='<div class="d-num num"><span id="d-n">0</span></div><div class="d-unit">năm</div>')
CONDS = [("Giá bán", "Thỏa thuận <b>theo thị trường</b>", T(0.9)),
         ("Người mua", "Vẫn phải <b>thuộc diện được mua</b>", T(2.8)),
         ("Căn nhà", "Đã được <b>cấp giấy chứng nhận</b>", T(5.2))]
c_html, c_js = "", ""
for i, (k, v, t) in enumerate(CONDS):
    c_html += f'<div class="card d-c" id="d-c{i}"><span class="ck"></span><div class="k">{k}</div><div class="v">{v}</div></div>\n'
    c_js += f"    tl.fromTo('#d-c{i}',{{autoAlpha:0,y:26}},{{autoAlpha:1,y:0,duration:0.42,ease:'power3.out'}},{t});\n"
frames['04-data'] = frame('04-data', """
.d-kick { position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }
.d-wrap { position:absolute; left:240px; top:270px; width:600px; height:600px; opacity:0; }
.d-wrap .ring { width:600px; height:600px; }
.d-num { font-weight:900; font-size:260px; line-height:0.9; color:#fff; }
.d-unit { margin-top:6px; font-weight:800; font-size:44px; letter-spacing:0.08em; color:#FF5A1F; }
.d-glow { position:absolute; left:290px; top:320px; width:500px; height:500px; border-radius:50%; background:radial-gradient(circle, rgba(255,90,31,0.22), transparent 70%); opacity:0; }
.d-sub { position:absolute; left:64px; right:64px; top:930px; text-align:center; font-weight:800; font-size:40px; color:#fff; opacity:0; }
.d-sub b { color:#FF5A1F; }
.d-list { position:absolute; left:64px; right:64px; top:1020px; display:flex; flex-direction:column; gap:20px; }
.d-c { position:relative; display:flex; align-items:center; gap:24px; height:128px; padding:0 34px; opacity:0; }
.d-c .ck { width:44px; height:44px; flex:none; border-radius:50%; border:4px solid #FF5A1F; position:relative; }
.d-c .ck::after { content:""; position:absolute; left:12px; top:6px; width:10px; height:18px; border-right:4px solid #FF5A1F; border-bottom:4px solid #FF5A1F; transform:rotate(45deg); }
.d-c .k { width:210px; font-weight:700; font-size:24px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.d-c .v { flex:1; font-weight:800; font-size:36px; line-height:1.2; color:#fff; }
.d-c .v b { color:#FF5A1F; font-weight:900; }
""", f"""
    <div class="kick d-kick" id="d-kick">Mốc khóa chuyển nhượng</div>
    <div class="d-glow" id="d-glow"></div>
    <div class="d-wrap" id="d-wrap">{big}</div>
    <div class="d-sub" id="d-sub">Sau mốc <b>5 năm</b>, được bán khi:</div>
    <div class="d-list">
{c_html}    </div>""", f"""
    tl.fromTo('#d-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.0);
    tl.fromTo('#d-wrap',{{autoAlpha:0,scale:0.85}},{{autoAlpha:1,scale:1,duration:0.5,ease:'back.out(1.5)'}},0.05);
    tl.fromTo('#d-glow',{{autoAlpha:0}},{{autoAlpha:1,duration:0.8}},0.3);
{ring_js('d-big', CB, 1.0, 0.2, 1.3, 'power1.inOut')}    const cn = {{ v: 0 }}; const nEl = document.getElementById('d-n');
    tl.fromTo(cn,{{v:0}},{{v:5,duration:1.3,ease:'power1.inOut',onUpdate(){{ nEl.textContent = Math.round(cn.v); }}}},0.2);
    tl.fromTo('#d-sub',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{T(0.6)});
{c_js}""")

# ---------------- 05 CONTEXT (3 vòng vừa + bảng so sánh trước/sau) ----------------
RINGS5 = [
    ('x-r1', 1.0, 'rgba(255,255,255,0.55)', 0, '<div class="rv">Tự do</div>', 'Hiện nay<br>sau 5 năm', T(0.0)),
    ('x-r2', 1.0, '#FF5A1F', 8, '<div class="rv">8</div><div class="ru">nhóm</div>', 'Đối tượng<br>được mua', T(2.3)),
    ('x-r3', 1.0, '#FF5A1F', 0, '<div class="rv">1</div><div class="ru">căn</div>', 'Mỗi cá nhân,<br>hộ gia đình', T(4.3)),
]
x_html, x_js = "", ""
for i, (rid, pct, col, ticks, inner, lab, t) in enumerate(RINGS5):
    rh, C = ring(rid, 250, 20, col, ticks=ticks, inner=inner)
    x_html += f'<div class="x-col" id="x-col{i}">{rh}<div class="lab">{lab}</div></div>\n'
    x_js += f"    tl.fromTo('#x-col{i}',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'}},{t});\n"
    x_js += ring_js(rid, C, pct, round(t + 0.1, 2), 0.8)
ROWS5 = [("Hiện nay · sau 5 năm", '<s>Bán cho bất kỳ ai</s>', T(0.6)),
         ("Từ 1/7/2027 · sau 5 năm", 'Chỉ bán cho <b>người thuộc diện được mua</b>', T(2.3)),
         ("Mỗi cá nhân, hộ gia đình", 'Chỉ mua hoặc thuê mua <b>1 căn</b>', T(4.6))]
rw_html, rw_js = "", ""
for i, (k, v, t) in enumerate(ROWS5):
    rw_html += f'<div class="x-row" id="x-row{i}"><div class="k">{k}</div><div class="v">{v}</div></div>\n'
    rw_js += f"    tl.fromTo('#x-row{i}',{{autoAlpha:0,x:-30}},{{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'}},{t});\n"
frames['05-context'] = frame('05-context', """
.x-kick { position:absolute; left:64px; top:190px; opacity:0; }
.x-ttl { top:240px; }
.x-rings { position:absolute; left:64px; right:64px; top:440px; display:flex; justify-content:space-between; }
.x-col { width:290px; display:flex; flex-direction:column; align-items:center; opacity:0; }
.x-col .rv { font-weight:900; font-size:64px; line-height:1; color:#fff; }
.x-col .ru { margin-top:4px; font-weight:700; font-size:22px; color:rgba(255,255,255,0.7); }
#x-col0 .rv { font-size:46px; color:rgba(255,255,255,0.8); }
.x-col .lab { margin-top:22px; text-align:center; font-weight:700; font-size:26px; line-height:1.3; color:rgba(255,255,255,0.8); }
.x-card { position:absolute; left:64px; right:64px; top:880px; height:580px; padding:20px 40px; opacity:0; display:flex; flex-direction:column; justify-content:center; }
.x-row { padding:26px 0; border-bottom:1px solid rgba(255,255,255,0.09); opacity:0; }
.x-row:last-child { border-bottom:none; }
.x-row .k { font-weight:700; font-size:24px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.55); }
.x-row .v { margin-top:10px; font-weight:800; font-size:42px; line-height:1.2; color:#fff; }
.x-row .v b { color:#FF5A1F; font-weight:900; }
.x-row .v s { color:#FF4438; text-decoration-thickness:4px; }
""", f"""
    <div class="kick x-kick" id="x-kick">Trước và sau</div>
    <div class="ttl x-ttl"><div class="ln"><span id="x-t1">Khác gì so với</span></div><div class="ln"><span id="x-t2"><b>hiện nay?</b></span></div></div>
    <div class="x-rings">
{x_html}    </div>
    <div class="card x-card" id="x-card">
{rw_html}    </div>""", f"""
    tl.fromTo('#x-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#x-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#x-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.26);
    tl.fromTo('#x-card',{{autoAlpha:0}},{{autoAlpha:1,duration:0.35}},{T(0.5)});
{x_js}{rw_js}""")

# ---------------- 06 IMPACT (2 vòng lớn cạnh nhau + thẻ chi tiết) ----------------
rL, CL = ring('i-rl', 440, 34, '#FF4438', inner='<div class="rv r">Vô hiệu</div>')
rR, CR = ring('i-rr', 440, 34, '#FF5A1F', inner='<div class="rv">Dân sự</div>')
frames['06-impact'] = frame('06-impact', """
.i-kick { position:absolute; left:64px; top:190px; opacity:0; }
.i-ttl { top:240px; }
.i-cols { position:absolute; left:64px; right:64px; top:450px; display:flex; gap:24px; }
.i-col { flex:1; display:flex; flex-direction:column; align-items:center; }
.i-ring { opacity:0; }
.i-ring .rv { font-weight:900; font-size:66px; color:#FF5A1F; } .i-ring .rv.r { color:#FF4438; }
.i-card { margin-top:34px; width:100%; height:500px; padding:36px 30px; opacity:0; }
.i-card.w { border-color:rgba(255,68,56,0.6); box-shadow:0 0 40px rgba(255,68,56,0.14); }
.i-card .k { font-weight:700; font-size:22px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.55); }
.i-card .h { margin-top:16px; font-weight:800; font-size:44px; line-height:1.22; color:#fff; }
.i-card .h b { color:#FF5A1F; } .i-card.w .h b { color:#FF4438; }
.i-card .d { margin-top:24px; padding-top:22px; border-top:1px solid rgba(255,255,255,0.1); font-weight:600; font-size:33px; line-height:1.4; color:rgba(255,255,255,0.8); opacity:0; }
""", f"""
    <div class="kick i-kick" id="i-kick">Điều luật quy định</div>
    <div class="ttl i-ttl"><div class="ln"><span id="i-t1">Bán sai thì sao,</span></div><div class="ln"><span id="i-t2"><b>căn đã bán</b> thì sao?</span></div></div>
    <div class="i-cols">
      <div class="i-col"><div class="i-ring" id="i-wl">{rL}</div>
        <div class="card i-card w" id="i-cl"><div class="k">Bán sai đối tượng</div><div class="h">Hợp đồng <b>vô hiệu</b></div><div class="d" id="i-dl">Phải bàn giao lại nhà; không bàn giao thì UBND cấp tỉnh cưỡng chế thu hồi</div></div></div>
      <div class="i-col"><div class="i-ring" id="i-wr">{rR}</div>
        <div class="card i-card" id="i-cr"><div class="k">Đã bán lại đúng quy định</div><div class="h">Trước <b>1/7/2027</b></div><div class="d" id="i-dr">Vẫn giao dịch theo pháp luật dân sự, không chịu hạn chế mới</div></div></div>
    </div>""", f"""
    tl.fromTo('#i-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#i-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#i-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.26);
    tl.fromTo('#i-wl',{{autoAlpha:0,scale:0.85}},{{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.5)'}},{T(0.1)});
{ring_js('i-rl', CL, 1.0, T(0.25), 1.0)}    tl.fromTo('#i-cl',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(0.7)});
    tl.fromTo('#i-dl',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{T(2.2)});
    tl.fromTo('#i-wr',{{autoAlpha:0,scale:0.85}},{{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.5)'}},{T(3.8)});
{ring_js('i-rr', CR, 1.0, T(3.95), 1.0)}    tl.fromTo('#i-cr',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(4.4)});
    tl.fromTo('#i-dr',{{autoAlpha:0,y:12}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{T(8.0)});""")

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
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Luật Nhà ở (sửa đổi) · hiệu lực 1/7/2027</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Siết bán lại nhà ở xã hội:</span></div>
        <div class="ln"><span id="t-h2" class="o">giữ đúng an sinh</span></div>
        <div class="ln"><span id="t-h3">hay làm khó người mua?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Giữ đúng mục tiêu an sinh</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Người mua khó xoay xở hơn</div></div>
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
    o1=T(1.4), vs=T(2.4), o2=T(2.8), cta=T(4.6), pulse=round(T(4.6) + 0.6, 2), sign=T(5.0)))

SFX = [
    ("hook", "impact-bass-1", 0.6, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("v96", "pop", STARTS[1] + T(3.2), 0.4, 0.24),
    ("f3", "click-soft", STARTS[2] + T(5.4), 0.35, 0.3),
    ("big", "impact-bass-1", STARTS[3] + 1.5, 0.6, 0.3),
    ("x3", "pop", STARTS[4] + T(4.3), 0.4, 0.24),
    ("i1", "click-soft", STARTS[5] + T(0.1), 0.35, 0.3),
    ("i2", "pop", STARTS[5] + T(3.8), 0.4, 0.24),
    ("o1", "pop", STARTS[6] + T(1.4), 0.35, 0.3),
    ("o2", "pop", STARTS[6] + T(2.8), 0.35, 0.3),
    ("cta", "chime", STARTS[6] + T(4.6), 1.2, 0.32),
]
TRK = {a: (31 if a in ("big", "hook", "f3", "i1") else 30) for a, *_ in SFX}
SOURCE_TEXT = "Nguồn: Dân Trí, VnExpress, Tuổi Trẻ"
SEED = 20261122

exec(open('gen_tail.py', encoding='utf-8').read())
