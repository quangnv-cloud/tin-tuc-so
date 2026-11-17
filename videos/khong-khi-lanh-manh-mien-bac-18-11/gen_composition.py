#!/usr/bin/env python3
"""Generate compositions + index.html for khong-khi-lanh-manh-mien-bac-18-11 (style 2-chip-and-leaderboard)."""
import json, os, re, difflib, sys

P = sys.argv[1]
os.chdir(P)

STARTS = [0, 5.6, 13.5, 22.35, 31.05, 42.15, 51.75]
DURS = [5.6, 7.9, 8.85, 8.7, 11.1, 9.6, 8.9]
TOTAL = round(STARTS[-1] + DURS[-1], 2)
VOFF = 0.10
SMASH5 = 3.76 + VOFF  # local time in act 5 where "Đêm 19" starts

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
.credit { position:absolute; right:14px; bottom:12px; padding:5px 10px; border-radius:6px; background:rgba(11,14,20,0.75); font-weight:500; font-size:18px; color:rgba(255,255,255,0.88); }
.chip { display:inline-flex; align-items:center; gap:12px; padding:14px 24px; border-radius:14px; border:2px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.10); box-shadow:0 0 40px rgba(255,90,31,0.14); }
.chip.warn { border-color:rgba(255,68,56,0.9); background:rgba(255,68,56,0.10); box-shadow:0 0 40px rgba(255,68,56,0.14); }
.cutflash { position:absolute; inset:0; z-index:6; pointer-events:none; opacity:0; background:linear-gradient(180deg, rgba(255,90,31,0.4), rgba(255,68,56,0.18)); }
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

frames = {}

# ---------------- 01 HOOK (fixed brand layout) ----------------
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:960px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:58% 40%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.30) 0%, rgba(11,14,20,0.0) 38%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:800px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:30px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:106px; line-height:1.04; letter-spacing:-0.02em; color:#fff; }
.hk-name.o { color:#FF5A1F; font-size:90px; }
.hk-sub { margin-top:24px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:22px; margin-top:38px; }
.hk-tag { font-weight:800; font-size:44px; line-height:1; color:#FF5A1F; opacity:0; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh tư liệu: VnExpress</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress · 17/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Không khí lạnh</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">tràn về miền Bắc</div></div>
      <div class="hk-sub" id="hk-sub">Từ sáng <b>18/11</b> · vùng núi cao <b>dưới 10°C</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Rét đậm vùng núi</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Mưa dông, gió giật cấp 8–9</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.62);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.84);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.4);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.0);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.3);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (style 1: ảnh + panel + 2 chip) ----------------
frames['02-what'] = frame('02-what', """
.w-kick { position:absolute; left:64px; top:250px; opacity:0; }
.w-card { position:absolute; left:64px; right:64px; top:304px; height:600px; border-radius:22px; overflow:hidden; box-shadow:0 0 40px rgba(255,90,31,0.14); border:1px solid rgba(255,255,255,0.10); opacity:0; }
.w-card img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 50%; }
.w-head { position:absolute; left:64px; right:64px; top:940px; font-weight:800; font-size:54px; line-height:1.16; letter-spacing:-0.01em; }
.w-head .ln { overflow:hidden; } .w-head .ln > span { display:block; }
.w-head b { color:#FF5A1F; font-weight:900; }
.w-chips { position:absolute; left:64px; right:64px; top:1136px; display:flex; gap:18px; }
.w-chips .chip { opacity:0; font-weight:800; font-size:30px; }
.w-chips .chip small { font-weight:600; font-size:22px; color:rgba(255,255,255,0.75); letter-spacing:0.06em; text-transform:uppercase; }
.w-flow { position:absolute; left:64px; right:64px; top:1252px; }
.w-flow .lab { font-weight:600; font-size:22px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.6); margin-bottom:16px; opacity:0; }
.w-steps { display:flex; align-items:stretch; gap:0; }
.w-step { flex:1; position:relative; padding:24px 10px 22px; text-align:center; border-radius:12px; background:#121724; border:1px solid rgba(255,255,255,0.10); opacity:0; }
.w-step .n { font-weight:900; font-size:24px; color:#FF5A1F; }
.w-step .t { margin-top:6px; font-weight:700; font-size:25px; line-height:1.2; color:#fff; }
.w-step.first { border-color:rgba(255,90,31,0.9); background:rgba(255,90,31,0.12); }
.w-arr { width:34px; flex:none; position:relative; opacity:0; }
.w-arr::before { content:""; position:absolute; left:8px; top:50%; width:14px; height:14px; border-top:4px solid #FF5A1F; border-right:4px solid #FF5A1F; transform:translateY(-50%) rotate(45deg); }
""", """
    <div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div>
    <div class="w-card" id="w-card"><img src="assets/img/tuoitre.jpg" alt=""><div class="credit">Ảnh tư liệu: Tuổi Trẻ</div></div>
    <div class="w-head">
      <div class="ln"><span id="w-h1">Khối không khí lạnh <b>mạnh</b></span></div>
      <div class="ln"><span id="w-h2">đang di chuyển xuống phía nam</span></div>
    </div>
    <div class="w-chips">
      <div class="chip" id="w-c1"><small>Bắt đầu</small><span class="num">Sáng 18/11</span></div>
      <div class="chip" id="w-c2"><small>Theo</small><span>TT Dự báo KTTV quốc gia</span></div>
    </div>
    <div class="w-flow">
      <div class="lab" id="w-lab">Phạm vi lan dần</div>
      <div class="w-steps">
        <div class="w-step first" id="w-s1"><div class="n">1</div><div class="t">Vùng núi Bắc Bộ</div></div>
        <div class="w-arr" id="w-a1"></div>
        <div class="w-step" id="w-s2"><div class="n">2</div><div class="t">Toàn miền Bắc</div></div>
        <div class="w-arr" id="w-a2"></div>
        <div class="w-step" id="w-s3"><div class="n">3</div><div class="t">Bắc Trung Bộ</div></div>
        <div class="w-arr" id="w-a3"></div>
        <div class="w-step" id="w-s4"><div class="n">4</div><div class="t">Trung Trung Bộ</div></div>
      </div>
    </div>""", """
    tl.fromTo('#w-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#w-card',{autoAlpha:0,scale:0.96},{autoAlpha:1,scale:1,duration:0.6,ease:'power3.out'},0.15);
    tl.fromTo('#w-card img',{scale:1.12},{scale:1.0,duration:7.5,ease:'none'},0.15);
    tl.fromTo('#w-h1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.5);
    tl.fromTo('#w-h2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.68);
    tl.fromTo('#w-c1',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'},1.2);
    tl.fromTo('#w-c2',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'},1.4);
    tl.fromTo('#w-lab',{autoAlpha:0},{autoAlpha:1,duration:0.3},2.9);
    tl.fromTo('#w-s1',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},3.4);
    tl.fromTo('#w-a1',{autoAlpha:0,x:-8},{autoAlpha:1,x:0,duration:0.25},4.4);
    tl.fromTo('#w-s2',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},4.55);
    tl.fromTo('#w-a2',{autoAlpha:0,x:-8},{autoAlpha:1,x:0,duration:0.25},5.85);
    tl.fromTo('#w-s3',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},5.95);
    tl.fromTo('#w-a3',{autoAlpha:0,x:-8},{autoAlpha:1,x:0,duration:0.25},6.5);
    tl.fromTo('#w-s4',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},6.6);""")

# ---------------- 03 KEY FACTS (watermark số khổng lồ + 3 fact xếp dọc) ----------------
frames['03-facts'] = frame('03-facts', """
.f-wm { position:absolute; left:-40px; right:-40px; top:900px; text-align:center; font-weight:900; font-size:420px; line-height:1; letter-spacing:-0.04em; color:rgba(255,90,31,0.07); opacity:0; }
.f-kick { position:absolute; left:64px; top:270px; opacity:0; }
.f-title { position:absolute; left:64px; right:64px; top:318px; font-weight:800; font-size:58px; line-height:1.15; }
.f-title .ln { overflow:hidden; } .f-title .ln > span { display:block; }
.f-list { position:absolute; left:64px; right:64px; top:470px; display:flex; flex-direction:column; gap:36px; }
.f-row { display:flex; gap:28px; align-items:center; min-height:262px; padding:36px 34px; border-radius:20px; background:rgba(18,23,36,0.92); border:1px solid rgba(255,255,255,0.10); border-left:6px solid #FF5A1F; opacity:0; }
.f-row.warn { border-left-color:#FF4438; }
.f-when { flex:none; width:290px; }
.f-when .t { font-weight:900; font-size:48px; white-space:nowrap; line-height:1.05; color:#FF5A1F; }
.f-row.warn .f-when .t { color:#FF4438; }
.f-when .s { margin-top:8px; font-weight:600; font-size:21px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.55); }
.f-what { font-weight:700; font-size:40px; line-height:1.3; color:#fff; }
.f-what .sub { display:block; margin-top:10px; font-weight:500; font-size:30px; color:rgba(255,255,255,0.72); }
""", """
    <div class="f-wm num" id="f-wm">18/11</div>
    <div class="kick f-kick" id="f-kick">Diễn biến chính</div>
    <div class="f-title"><div class="ln"><span id="f-t1">Mưa dông trước, rét sau</span></div></div>
    <div class="f-list">
      <div class="f-row warn" id="f-r1"><div class="f-when"><div class="t num">18–19/11</div><div class="s">Mưa dông</div></div>
        <div class="f-what">Bắc Bộ, Thanh Hóa, Nghệ An<span class="sub">Có mưa dông, có nơi mưa lớn</span></div></div>
      <div class="f-row" id="f-r2"><div class="f-when"><div class="t num">Trưa 18/11</div><div class="s">Hà Nội</div></div>
        <div class="f-what">Không khí lạnh ảnh hưởng Thủ đô<span class="sub">Chuyển rét từ tối 18/11</span></div></div>
      <div class="f-row" id="f-r3"><div class="f-when"><div class="t num">Từ 19/11</div><div class="s">Miền Trung</div></div>
        <div class="f-what">Bắc Trung Bộ chuyển rét<span class="sub">Quảng Trị – Huế chuyển lạnh</span></div></div>
      <div class="chip" id="f-note" style="align-self:flex-start;opacity:0;font-weight:800;font-size:32px;">Vùng núi Bắc Bộ có nơi rét đậm từ đêm 18/11</div>
    </div>""", """
    tl.fromTo('#f-wm',{autoAlpha:0,scale:1.08},{autoAlpha:1,scale:1,duration:1.2,ease:'power2.out'},0);
    tl.to('#f-wm',{y:-30,duration:8.5,ease:'none'},0);
    tl.fromTo('#f-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#f-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.25);
    tl.fromTo('#f-r1',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},0.5);
    tl.fromTo('#f-r2',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},5.0);
    tl.fromTo('#f-r3',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},7.0);
    tl.fromTo('#f-note',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.6)'},7.6);""")

# ---------------- 04 DATA MOMENT (số focal + bảng xếp hạng nhiệt độ) ----------------
# scale 0..20 °C mapped to track width
ROWS = [
    ("r1", "Sa Pa (Lào Cai)", "điểm cao trên 1.500 m", 8, 11, "8–11°C", True),
    ("r2", "Trung du & vùng núi Bắc Bộ", "phổ biến", 12, 15, "12–15°C", False),
    ("r3", "Đồng bằng Bắc Bộ & Bắc Trung Bộ", "phổ biến", 15, 18, "15–18°C", False),
]
rows_html = ""
for rid, name, sub, lo, hi, lab, hl in ROWS:
    left = lo / 20 * 100
    width = (hi - lo) / 20 * 100
    rows_html += f"""      <div class="d-row{' hl' if hl else ''}" id="d-{rid}">
        <div class="d-top"><div class="d-name">{name}<span>{sub}</span></div><div class="d-val num">{lab}</div></div>
        <div class="d-track"><div class="d-fill" id="d-{rid}-f" style="left:{left:.1f}%;width:{width:.1f}%;"></div></div>
      </div>
"""
frames['04-data'] = frame('04-data', """
.d-kick { position:absolute; left:64px; right:64px; top:270px; text-align:center; opacity:0; }
.d-focal { position:absolute; left:64px; right:64px; top:320px; text-align:center; }
.d-big { font-weight:900; font-size:230px; line-height:1.12; letter-spacing:-0.04em; color:#FF5A1F; opacity:0; }
.d-big small { font-size:120px; letter-spacing:0; }
.d-cap { margin-top:18px; font-weight:700; font-size:40px; color:#fff; opacity:0; }
.d-board { position:absolute; left:64px; right:64px; top:740px; padding:40px 36px 34px; border-radius:22px; background:rgba(18,23,36,0.92); border:1px solid rgba(255,255,255,0.10); box-shadow:0 0 40px rgba(255,90,31,0.12); opacity:0; }
.d-bh { display:flex; justify-content:space-between; font-weight:600; font-size:22px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.55); margin-bottom:22px; }
.d-row { padding:26px 0 30px; border-top:1px solid rgba(255,255,255,0.08); opacity:0; }
.d-top { display:flex; justify-content:space-between; align-items:flex-end; gap:20px; }
.d-name { font-weight:700; font-size:35px; line-height:1.2; color:#fff; }
.d-name span { display:block; margin-top:4px; font-weight:500; font-size:22px; color:rgba(255,255,255,0.6); }
.d-val { flex:none; font-weight:900; font-size:58px; color:#fff; }
.d-row.hl .d-val { color:#FF5A1F; }
.d-track { position:relative; margin-top:20px; height:24px; border-radius:12px; background:rgba(255,255,255,0.08); }
.d-fill { position:absolute; top:0; bottom:0; border-radius:9px; background:rgba(255,255,255,0.55); transform-origin:left center; }
.d-row.hl .d-fill { background:linear-gradient(90deg,#FF4438,#FF5A1F); }
.d-axis { position:relative; height:36px; margin-top:10px; font-weight:600; font-size:24px; color:rgba(255,255,255,0.5); opacity:0; }
.d-axis span { position:absolute; top:4px; transform:translateX(-50%); }
""", f"""
    <div class="kick d-kick" id="d-kick">Nhiệt độ thấp nhất dự báo</div>
    <div class="d-focal">
      <div class="d-big num" id="d-big"><small>&lt;</small>10<small>°C</small></div>
      <div class="d-cap" id="d-cap">Vùng núi cao có nơi</div>
    </div>
    <div class="d-board" id="d-board">
      <div class="d-bh"><span>Khu vực</span><span>Thấp nhất</span></div>
{rows_html}      <div class="d-axis num" id="d-axis"><span style="left:0%;transform:none">0°C</span><span style="left:25%">5</span><span style="left:50%">10</span><span style="left:75%">15</span><span style="left:100%;transform:translateX(-100%)">20°C</span></div>
    </div>""", """
    tl.fromTo('#d-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#d-big',{autoAlpha:0,scale:0.7},{autoAlpha:1,scale:1,duration:0.6,ease:'back.out(1.6)'},0.2);
    tl.fromTo('#d-cap',{autoAlpha:0,y:12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.55);
    tl.fromTo('#d-board',{autoAlpha:0,y:40},{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'},0.9);
    tl.fromTo('#d-axis',{autoAlpha:0},{autoAlpha:1,duration:0.4},1.1);
    tl.fromTo('#d-r2',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},1.4);
    tl.fromTo('#d-r2-f',{scaleX:0},{scaleX:1,duration:0.8,ease:'power2.out'},1.55);
    tl.fromTo('#d-r3',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},3.55);
    tl.fromTo('#d-r3-f',{scaleX:0},{scaleX:1,duration:0.8,ease:'power2.out'},3.7);
    tl.fromTo('#d-r1',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},6.0);
    tl.fromTo('#d-r1-f',{scaleX:0},{scaleX:1,duration:0.8,ease:'power2.out'},6.15);
    tl.fromTo('#d-r1',{backgroundColor:'rgba(255,90,31,0)'},{backgroundColor:'rgba(255,90,31,0.10)',duration:0.5},6.6);""")

# ---------------- 05 CONTEXT (chip lớn xếp dọc + smash-cut) ----------------
frames['05-context'] = frame('05-context', f"""
.c-kick {{ position:absolute; left:64px; top:270px; opacity:0; }}
.c-head {{ position:absolute; left:64px; right:64px; top:318px; font-weight:800; font-size:60px; line-height:1.15; }}
.c-head .ln {{ overflow:hidden; }} .c-head .ln > span {{ display:block; }}
.c-head b {{ color:#FF5A1F; font-weight:900; }}
#c-content {{ position:absolute; inset:0; }}
.c-list {{ position:absolute; left:64px; right:64px; top:470px; display:flex; flex-direction:column; gap:36px; }}
.c-chip {{ display:flex; flex-direction:column; align-items:flex-start; justify-content:center; min-height:290px; padding:36px 38px; border-radius:20px; border:2px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.08); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }}
.c-chip.warn {{ border-color:rgba(255,68,56,0.9); background:rgba(255,68,56,0.08); box-shadow:0 0 40px rgba(255,68,56,0.14); }}
.c-chip .tg {{ font-weight:700; font-size:25px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.65); }}
.c-chip .v {{ margin-top:12px; font-weight:900; font-size:78px; line-height:1.05; color:#FF5A1F; }}
.c-chip.warn .v {{ color:#FF4438; }}
.c-chip .d {{ margin-top:12px; font-weight:600; font-size:35px; line-height:1.3; color:#fff; }}
""", """
    <div id="c-content">
    <div class="kick c-kick" id="c-kick">Bối cảnh</div>
    <div class="c-head"><div class="ln"><span id="c-h1">Từ nắng nóng sang <b>rét</b></span></div></div>
    <div class="c-list">
      <div class="c-chip" id="c-1"><div class="tg">Ngày 17/11 · Tây Bắc Bộ</div><div class="v num">Trên 32°C</div><div class="d">Trời vẫn nắng, có nơi trên 32°C</div></div>
      <div class="c-chip" id="c-2"><div class="tg">Đêm 19 – ngày 20/11</div><div class="v">Tăng cường</div><div class="d">Ảnh hưởng tới một số nơi ở Nam Trung Bộ</div></div>
      <div class="c-chip warn" id="c-3"><div class="tg">Vịnh Bắc Bộ · từ trưa 18/11</div><div class="v num">Giật cấp 8–9</div><div class="d">Gió cấp 6–7, sóng cao 2–4 m</div></div>
    </div>
    </div>
    <div class="cutflash" id="c-flash"></div>""", f"""
    tl.fromTo('#c-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.1);
    tl.fromTo('#c-h1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.25);
    tl.fromTo('#c-1',{{autoAlpha:0,y:30,scale:0.96}},{{autoAlpha:1,y:0,scale:1,duration:0.5,ease:'back.out(1.4)'}},1.3);
    tl.fromTo('#c-flash',{{opacity:0}},{{opacity:0.55,duration:0.05,ease:'none'}},{SMASH5 - 0.1:.2f});
    tl.to('#c-flash',{{opacity:0,duration:0.16,ease:'power1.in'}},{SMASH5 - 0.05:.2f});
    tl.fromTo('#c-content',{{scale:1}},{{scale:0.986,duration:0.06,ease:'power1.out'}},{SMASH5 - 0.1:.2f});
    tl.to('#c-content',{{scale:1,duration:0.14,ease:'power2.out'}},{SMASH5 - 0.039:.3f});
    tl.fromTo('#c-2',{{autoAlpha:0,y:30,scale:0.96}},{{autoAlpha:1,y:0,scale:1,duration:0.5,ease:'back.out(1.4)'}},{SMASH5:.2f});
    tl.fromTo('#c-3',{{autoAlpha:0,y:30,scale:0.96}},{{autoAlpha:1,y:0,scale:1,duration:0.5,ease:'back.out(1.4)'}},{7.1 + VOFF:.2f});""")

# ---------------- 06 IMPACT (watermark số + 2 chip tác động) ----------------
frames['06-impact'] = frame('06-impact', """
.i-wm { position:absolute; left:0; right:0; top:820px; text-align:center; font-weight:900; font-size:560px; line-height:1; letter-spacing:-0.05em; color:rgba(255,90,31,0.07); opacity:0; }
.i-kick { position:absolute; left:64px; top:270px; opacity:0; }
.i-org { position:absolute; left:64px; right:64px; top:318px; font-weight:700; font-size:34px; line-height:1.3; color:rgba(255,255,255,0.85); opacity:0; }
.i-big { position:absolute; left:64px; right:64px; top:400px; }
.i-big .n { font-weight:900; font-size:170px; line-height:1; letter-spacing:-0.03em; color:#FF5A1F; opacity:0; }
.i-big .n small { font-size:72px; letter-spacing:0; color:#fff; }
.i-big .s { margin-top:12px; font-weight:700; font-size:38px; line-height:1.3; color:#fff; opacity:0; }
.i-big .s span { color:rgba(255,255,255,0.65); font-weight:600; font-size:28px; display:block; margin-top:6px; }
.i-list { position:absolute; left:64px; right:64px; top:900px; display:flex; flex-direction:column; gap:36px; }
.i-chip { display:flex; gap:30px; align-items:center; min-height:250px; padding:36px 36px; border-radius:20px; border:2px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.08); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.i-chip.warn { border-color:rgba(255,68,56,0.9); background:rgba(255,68,56,0.08); box-shadow:0 0 40px rgba(255,68,56,0.14); }
.i-ico { flex:none; width:70px; height:70px; border-radius:50%; border:4px solid #FF5A1F; position:relative; }
.i-ico.ship::before { content:""; position:absolute; left:14px; right:14px; bottom:18px; height:14px; border-radius:0 0 12px 12px; background:#FF5A1F; }
.i-ico.ship::after { content:""; position:absolute; left:31px; top:14px; width:4px; height:22px; background:#FF5A1F; }
.i-ico.warn { border:none; }
.i-ico.warn::before { content:""; position:absolute; left:2px; top:4px; width:0; height:0; border-left:33px solid transparent; border-right:33px solid transparent; border-bottom:60px solid #FF4438; }
.i-ico.warn::after { content:"!"; position:absolute; left:0; right:0; top:22px; text-align:center; font-weight:900; font-size:34px; color:#0B0E14; }
.i-t { font-weight:800; font-size:40px; line-height:1.25; color:#fff; }
.i-t span { display:block; margin-top:10px; font-weight:500; font-size:30px; color:rgba(255,255,255,0.75); }
""", """
    <div class="i-wm num" id="i-wm">26</div>
    <div class="kick i-kick" id="i-kick">Đã có chỉ đạo ứng phó</div>
    <div class="i-org" id="i-org">Ban Chỉ đạo Phòng thủ dân sự quốc gia · tối 16/11</div>
    <div class="i-big">
      <div class="n num" id="i-n"><span id="i-cnt">26</span> <small>tỉnh, thành</small></div>
      <div class="s" id="i-s">Bắc Bộ và Trung Bộ được đề nghị chủ động ứng phó<span>Mưa lớn, rét, gió mạnh trên biển</span></div>
    </div>
    <div class="i-list">
      <div class="i-chip" id="i-c1"><div class="i-ico ship"></div><div class="i-t">Ven biển Quảng Ninh → Lâm Đồng<span>Thông báo tàu thuyền chủ động phòng tránh gió mạnh</span></div></div>
      <div class="i-chip warn" id="i-c2"><div class="i-ico warn"></div><div class="i-t">Không dùng bếp than sưởi ấm trong phòng kín<span>Phòng nguy cơ ngộ độc khí khi trời rét</span></div></div>
    </div>""", """
    tl.fromTo('#i-wm',{autoAlpha:0,scale:1.08},{autoAlpha:1,scale:1,duration:1.2,ease:'power2.out'},0);
    tl.to('#i-wm',{y:-30,duration:9.4,ease:'none'},0);
    tl.fromTo('#i-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#i-org',{autoAlpha:0,y:10},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},1.2);
    tl.fromTo('#i-n',{autoAlpha:0,scale:0.8},{autoAlpha:1,scale:1,duration:0.5,ease:'back.out(1.6)'},3.3);
    tl.fromTo('#i-s',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},4.2);
    tl.fromTo('#i-c1',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},5.4);
    tl.fromTo('#i-c2',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},6.8);""")

# ---------------- 07 CTA (fixed brand layout, orange) ----------------
frames['07-cta'] = frame('07-cta', """
#root::before { content:""; position:absolute; inset:0; background:radial-gradient(80% 50% at 50% 40%, rgba(255,90,31,0.14), transparent 60%); }
.t-wrap { position:absolute; left:64px; right:64px; top:420px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-head { margin-top:30px; font-weight:900; font-size:80px; line-height:1.1; color:#fff; }
.t-head .ln { overflow:hidden; } .t-head .ln > span { display:block; }
.t-head .o { color:#FF5A1F; }
.t-opts { display:flex; justify-content:center; align-items:stretch; gap:20px; margin-top:80px; }
.t-opt { flex:1; max-width:400px; padding:50px 24px; border-radius:18px; border:2px solid; opacity:0; }
.t-opt.up { border-color:rgba(255,90,31,0.8); background:rgba(255,90,31,0.10); }
.t-opt.down { border-color:rgba(255,68,56,0.8); background:rgba(255,68,56,0.10); }
.t-opt .emo { width:48px; height:48px; margin:0 auto; position:relative; }
.t-opt.up .emo { border:4px solid #FF5A1F; border-radius:50%; }
.t-opt.up .emo::after { content:""; position:absolute; left:50%; top:13px; width:12px; height:12px; border-top:4px solid #FF5A1F; border-right:4px solid #FF5A1F; transform:translateX(-50%) rotate(-45deg); }
.t-opt.down .emo::before { content:""; position:absolute; left:0; bottom:0; width:0; height:0; border-left:24px solid transparent; border-right:24px solid transparent; border-bottom:44px solid #FF4438; }
.t-opt.down .emo::after { content:"!"; position:absolute; left:0; right:0; bottom:-2px; text-align:center; font-weight:900; font-size:26px; color:#0B0E14; }
.t-opt .lab { margin-top:18px; font-weight:800; font-size:36px; line-height:1.2; color:#fff; }
.t-vs { display:flex; align-items:center; font-weight:900; font-size:34px; color:rgba(255,255,255,0.35); opacity:0; }
.t-cta { display:inline-flex; align-items:center; gap:18px; margin-top:90px; padding:24px 40px; border-radius:100px; background:#FF5A1F; opacity:0; }
.t-cta .ico { width:40px; height:40px; flex:none; border-radius:12px 12px 12px 4px; background:#fff; position:relative; }
.t-cta .ico::before { content:""; position:absolute; left:9px; top:12px; right:9px; height:4px; border-radius:2px; background:#FF5A1F; box-shadow:0 9px 0 #FF5A1F; }
.t-cta span { font-weight:800; font-size:36px; letter-spacing:0.01em; color:#0B0E14; }
.t-sign { position:absolute; left:0; right:0; top:1410px; display:flex; align-items:center; justify-content:center; gap:14px; opacity:0; }
.t-sign .m { width:48px; height:48px; }
.t-sign .w { font-weight:800; font-size:32px; color:rgba(255,255,255,0.9); }
""", """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Miền Bắc sắp rét:</span></div>
        <div class="ln"><span id="t-h2" class="o">háo hức hay lo ngại?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Háo hức đón gió lạnh</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Lo sức khỏe, đi lại</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>""", """
    tl.fromTo('#t-kicker',{autoAlpha:0,y:-12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0);
    tl.fromTo('#t-h1',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.2);
    tl.fromTo('#t-h2',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.36);
    tl.fromTo('#t-o1',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},1.3);
    tl.fromTo('#t-vs',{autoAlpha:0,scale:0.5},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'},2.4);
    tl.fromTo('#t-o2',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},2.6);
    tl.fromTo('#t-cta',{autoAlpha:0,y:22},{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'},4.8);
    tl.to('#t-cta',{keyframes:[{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'},{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'}]},5.4);
    tl.fromTo('#t-sign',{autoAlpha:0},{autoAlpha:1,duration:0.4},5.2);""")

os.makedirs('compositions/frames', exist_ok=True)
for k, v in frames.items():
    open(f'compositions/frames/{k}.html', 'w', encoding='utf-8').write(v)

# ---------------- captions ----------------
def norm(t):
    return re.sub(r'[^\w]', '', t.lower())

lines = open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')
caps = []  # (start, end, [(text, t)])
for i, line in enumerate(lines):
    ow = line.split()
    d = json.load(open(f'assets/voice/stt{i+1}.json', encoding='utf-8'))
    sw = [w for w in d['words'] if w.get('type') == 'word']
    off = STARTS[i] + VOFF
    sm = difflib.SequenceMatcher(a=[norm(x) for x in ow], b=[norm(x['text']) for x in sw], autojunk=False)
    times = [None] * len(ow)
    ends = [None] * len(ow)
    for tag, a0, a1, b0, b1 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(a1 - a0):
                times[a0 + k] = sw[b0 + k]['start']; ends[a0 + k] = sw[b0 + k]['end']
        elif a1 > a0:
            if b1 > b0:
                s, e = sw[b0]['start'], sw[b1 - 1]['end']
            else:
                s = sw[b0 - 1]['end'] if b0 > 0 else 0.0
                e = sw[b0]['start'] if b0 < len(sw) else s + 0.3
            step = (e - s) / (a1 - a0)
            for k in range(a1 - a0):
                times[a0 + k] = s + step * k; ends[a0 + k] = s + step * (k + 1)
    timed = [(ow[k], off + times[k], off + ends[k]) for k in range(len(ow))]
    # chunk: 3-5 words, break after punctuation
    chunk = []
    chunks = []
    for w in timed:
        chunk.append(w)
        if len(chunk) >= 5 or (len(chunk) >= 3 and re.search(r'[,.?!]$', w[0])):
            chunks.append(chunk); chunk = []
    if chunk:
        if len(chunk) < 2 and chunks:
            chunks[-1].extend(chunk)
        else:
            chunks.append(chunk)
    for ci, c in enumerate(chunks):
        st = c[0][1]
        en = chunks[ci + 1][0][1] - 0.02 if ci + 1 < len(chunks) else c[-1][2] + 0.3
        caps.append((st, en, c))

cap_html = ""
cap_js = ""
for ci, (st, en, c) in enumerate(caps):
    spans = " ".join(f'<span class="w" id="w{ci}_{k}">{w[0]}</span>' for k, w in enumerate(c))
    cap_html += f'<div class="cap" id="cap{ci}">{spans}</div>\n'
    cap_js += f"tl.set('#cap{ci}',{{autoAlpha:1}},{st:.2f});tl.set('#cap{ci}',{{autoAlpha:0}},{en:.2f});\n"
    for k, w in enumerate(c):
        cap_js += f"tl.to('#w{ci}_{k}',{{color:'#FF5A1F',duration:0.1,ease:'none'}},{w[1]:.2f});\n"

# stars (deterministic PRNG)
def mulberry32(seed):
    def r():
        nonlocal seed
        seed = (seed + 0x6D2B79F5) & 0xFFFFFFFF
        t = seed
        t = ((t ^ (t >> 15)) * (1 | t)) & 0xFFFFFFFF
        t = (t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return r
rand = mulberry32(20261117)
stars = "".join(f'<circle cx="{int(rand()*1080)}" cy="{int(rand()*1920)}" r="{1.5+rand()*1.5:.1f}" fill="#fff" opacity="{0.15+rand()*0.25:.2f}" />' for _ in range(40))

clips = ""
names = ['01-hook', '02-what', '03-facts', '04-data', '05-context', '06-impact', '07-cta']
for n, s, d in zip(names, STARTS, DURS):
    clips += f'<div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{s}" data-duration="{d}" data-track-index="1"></div>\n'

import subprocess
voices = ""
for i in range(7):
    dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'assets/voice/line{i+1}.mp3']).decode().strip())
    voices += f'<audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{STARTS[i]+VOFF:.2f}" data-duration="{dur:.3f}" data-track-index="10" data-audio-group="voiceover"></audio>\n'

SFX = [
    ("hook", "impact-bass-1", 0.65, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("chips", "pop", STARTS[1] + 1.2, 0.4, 0.26),
    ("num", "impact-bass-1", STARTS[3] + 0.2, 0.6, 0.3),
    ("sapa", "pop", STARTS[3] + 6.0, 0.4, 0.26),
    ("cut5", "click-soft", STARTS[4] + SMASH5 - 0.1, 0.35, 0.32),
    ("n26", "pop", STARTS[5] + 3.3, 0.4, 0.26),
    ("o1", "pop", STARTS[6] + 1.3, 0.35, 0.3),
    ("o2", "pop", STARTS[6] + 2.6, 0.35, 0.3),
    ("cta", "chime", STARTS[6] + 4.8, 1.2, 0.32),
]
TRK = {a: (31 if a in ("num", "hook", "cut5") else 30) for a, *_ in SFX}
sfx = "".join(f'<audio id="el-sfx-{a}" src="assets/sfx/{f}.mp3" data-start="{s:.2f}" data-duration="{d}" data-track-index="{TRK[a]}" data-volume="{v}"></audio>\n' for a, f, s, d, v in SFX)

bgm_attr = ""
if os.path.exists('.bgm_attrs'):
    bgm_attr = open('.bgm_attrs').read().strip()

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
#caps {{ position:absolute; left:80px; right:180px; top:1490px; height:110px; z-index:85; pointer-events:none; }}
.cap {{ position:absolute; left:0; right:0; top:0; text-align:center; font-weight:800; font-size:42px; line-height:1.2; color:rgba(255,255,255,0.92); text-shadow:0 2px 12px rgba(0,0,0,0.9); opacity:0; }}
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
{clips}<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress, Dân Trí, Tuổi Trẻ</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
<div id="caps">
{cap_html}</div>
{voices}<audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"{(' ' + bgm_attr) if bgm_attr else ''}></audio>
{sfx}</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.set('#brand-anchor',{{opacity:1}},{STARTS[1]});
tl.to('.blob',{{x:'+=40',y:'-=30',duration:18,ease:'sine.inOut',repeat:3,yoyo:true,stagger:3}},0);
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:15,yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{cap_js}window.__timelines['main'] = tl;
</script>
</body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(index)
print('total', TOTAL, 'caps', len(caps))
