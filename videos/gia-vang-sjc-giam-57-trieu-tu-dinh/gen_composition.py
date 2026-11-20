#!/usr/bin/env python3
"""Generate compositions + index.html for gia-vang-sjc-giam-57-trieu-tu-dinh (style 4-split-comparison)."""
import json, os, re, difflib, sys, subprocess

P = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.chdir(P)

VOFF = 0.10
VDUR = [float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                        f'assets/voice/line{i+1}.mp3']).decode().strip()) for i in range(7)]
PAD = [0.4, 0.4, 0.4, 0.45, 0.45, 0.45, 1.3]
DURS = [round(v + VOFF + p, 2) for v, p in zip(VDUR, PAD)]
STARTS = [0.0]
for d in DURS[:-1]:
    STARTS.append(round(STARTS[-1] + d, 2))
TOTAL = round(STARTS[-1] + DURS[-1], 2)
SMASH5 = 13.65  # voice-local "Quy đổi" in act 5


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
.cutflash { position:absolute; inset:0; z-index:6; pointer-events:none; opacity:0; background:linear-gradient(180deg, rgba(255,90,31,0.4), rgba(255,68,56,0.18)); }
.ttl { position:absolute; left:64px; right:64px; font-weight:800; font-size:60px; line-height:1.14; letter-spacing:-0.01em; }
.ttl .ln { overflow:hidden; } .ttl .ln > span { display:block; }
.ttl b { color:#FF5A1F; font-weight:900; } .ttl b.r { color:#FF4438; }
.vline { position:absolute; width:3px; background:#FF5A1F; transform-origin:top center; box-shadow:0 0 18px rgba(255,90,31,0.55); }
.card { border-radius:20px; background:rgba(18,23,36,0.94); border:1px solid rgba(255,255,255,0.10); box-shadow:0 0 40px rgba(255,90,31,0.14); }
.tri-d { display:inline-block; width:0; height:0; border-left:13px solid transparent; border-right:13px solid transparent; border-top:20px solid #FF4438; vertical-align:middle; margin-right:12px; }
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
.hk-photo { position:absolute; left:0; right:0; top:0; height:900px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:62% 40%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0.0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:720px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:30px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:130px; line-height:1.02; letter-spacing:-0.02em; color:#fff; }
.hk-name.o { color:#FF5A1F; font-size:96px; }
.hk-sub { margin-top:30px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:30px; margin-top:56px; }
.hk-tag { font-weight:800; font-size:50px; line-height:1; color:#FF5A1F; opacity:0; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: Dân Trí</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: Dân Trí · 20/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Vàng SJC</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">mất hơn 57 triệu</div></div>
      <div class="hk-sub" id="hk-sub">so với đỉnh lịch sử, mỗi lượng còn <b>134,2 triệu</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Thấp nhất hơn 1 năm</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Chênh mua – bán 5 triệu</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.7);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.92);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.4);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.0);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.3);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (split dọc: ảnh trái | panel phải + hàng chia đôi) ----------------
D2 = DURS[1]
frames['02-what'] = frame('02-what', """
.w-kick { position:absolute; left:64px; top:190px; opacity:0; }
.w-ttl { top:240px; }
.w-split { position:absolute; left:64px; right:64px; top:420px; height:560px; }
.w-img { position:absolute; left:0; top:0; width:462px; height:560px; border-radius:20px 0 0 20px; overflow:hidden; opacity:0; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 50%; }
.w-vl { left:475px; top:0; height:560px; }
.w-pan { position:absolute; left:490px; right:0; top:0; height:560px; border-radius:0 20px 20px 0; padding:44px 34px; display:flex; flex-direction:column; justify-content:center; opacity:0; }
.w-pan .l { font-weight:700; font-size:24px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.w-pan .p { margin-top:22px; font-weight:900; font-size:62px; line-height:1.05; color:#fff; }
.w-pan .p span { display:block; }
.w-pan .p .o { color:#FF5A1F; }
.w-pan .u { margin-top:18px; font-weight:600; font-size:25px; line-height:1.35; color:rgba(255,255,255,0.75); }
.w-rows { position:absolute; left:64px; right:64px; top:1030px; display:flex; flex-direction:column; gap:18px; }
.w-row { position:relative; display:flex; align-items:center; height:122px; border-radius:16px; padding:0 30px; overflow:hidden; opacity:0; }
.w-row .k { width:430px; font-weight:700; font-size:32px; color:rgba(255,255,255,0.78); }
.w-row .sep { position:absolute; left:470px; top:24px; bottom:24px; width:2px; background:rgba(255,90,31,0.6); }
.w-row .v { flex:1; text-align:right; font-weight:900; font-size:50px; color:#FF4438; white-space:nowrap; }
.w-row .v small { font-size:28px; font-weight:700; color:rgba(255,255,255,0.75); margin-left:8px; }
""", """
    <div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div>
    <div class="ttl w-ttl"><div class="ln"><span id="w-h1">SJC hạ giá <b>cả hai chiều</b></span></div><div class="ln"><span id="w-h2">trong phiên 20/11</span></div></div>
    <div class="w-split">
      <div class="w-img" id="w-img"><img src="assets/img/vnexpress.jpg" alt=""><div class="credit">Ảnh: VnExpress</div></div>
      <div class="vline w-vl" id="w-vl"></div>
      <div class="card w-pan" id="w-pan"><div class="l">Vàng miếng SJC</div><div class="p num"><span>129,2 –</span><span class="o">134,2</span></div><div class="u">triệu đồng/lượng<br>mua vào – bán ra</div></div>
    </div>
    <div class="w-rows">
      <div class="card w-row" id="w-r1"><div class="k">Giá mua vào</div><div class="sep"></div><div class="v num"><span class="tri-d"></span>5 triệu</div></div>
      <div class="card w-row" id="w-r2"><div class="k">Giá bán ra</div><div class="sep"></div><div class="v num"><span class="tri-d"></span>3 triệu</div></div>
      <div class="card w-row" id="w-r3"><div class="k">Bạc thỏi</div><div class="sep"></div><div class="v num"><span class="tri-d"></span>gần 3 triệu<small>/kg</small></div></div>
    </div>""", """
    tl.fromTo('#w-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#w-h1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.15);
    tl.fromTo('#w-h2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.3);
    tl.fromTo('#w-vl',{scaleY:0},{scaleY:1,duration:0.6,ease:'power3.inOut'},0.45);
    tl.fromTo('#w-img',{autoAlpha:0,x:-60},{autoAlpha:1,x:0,duration:0.6,ease:'power3.out'},0.6);
    tl.fromTo('#w-img img',{scale:1.14},{scale:1.0,duration:%(d)s,ease:'none'},0.6);
    tl.fromTo('#w-pan',{autoAlpha:0,x:60},{autoAlpha:1,x:0,duration:0.6,ease:'power3.out'},0.75);
    tl.fromTo('#w-r1',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r1)s);
    tl.fromTo('#w-r2',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r2)s);
    tl.fromTo('#w-r3',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r3)s);""" % dict(
    d=D2, r1=T(2.7), r2=T(4.2), r3=T(9.0)))

# ---------------- 03 KEY FACTS (2 nửa mua/bán + thanh chênh lệch tỉ lệ) ----------------
frames['03-facts'] = frame('03-facts', """
.f-kick { position:absolute; left:64px; top:190px; opacity:0; }
.f-ttl { top:240px; }
.f-pair { position:absolute; left:64px; right:64px; top:430px; height:250px; }
.f-half { position:absolute; top:430px; width:452px; height:250px; padding:34px 30px; opacity:0; }
.f-half.l { left:64px; border-color:rgba(255,68,56,0.7); background:rgba(255,68,56,0.10); }
.f-half.r { right:64px; }
.f-half .k { font-weight:700; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.65); }
.f-half .v { margin-top:18px; font-weight:900; font-size:78px; line-height:1; white-space:nowrap; }
.f-half.l .v { color:#FF4438; } .f-half.r .v { color:#fff; }
.f-half .s { margin-top:14px; font-weight:600; font-size:25px; color:rgba(255,255,255,0.7); }
.f-vl { left:475px; top:430px; height:250px; }
.f-gl { position:absolute; left:64px; right:64px; top:740px; font-weight:800; font-size:30px; letter-spacing:0.12em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.f-bars { position:absolute; left:64px; right:64px; top:800px; display:flex; flex-direction:column; gap:26px; }
.f-b { position:relative; height:180px; padding:26px 30px; opacity:0; }
.f-b .k { display:flex; justify-content:space-between; align-items:baseline; font-weight:700; font-size:30px; color:rgba(255,255,255,0.82); }
.f-b .k b { font-weight:900; font-size:52px; color:#fff; }
.f-b.hot .k b { color:#FF5A1F; } .f-b.max .k b { color:#FF4438; }
.f-b .trk { position:absolute; left:30px; right:30px; bottom:30px; height:26px; border-radius:13px; background:rgba(255,255,255,0.07); overflow:hidden; }
.f-b .fill { position:absolute; left:0; top:0; bottom:0; border-radius:13px; background:rgba(255,255,255,0.45); transform-origin:left center; }
.f-b.hot .fill { background:linear-gradient(90deg,#FF5A1F,#FF7A45); }
.f-b.max .fill { background:linear-gradient(90deg,#FF5A1F,#FF4438); }
""", """
    <div class="kick f-kick" id="f-kick">Điểm đáng chú ý</div>
    <div class="ttl f-ttl"><div class="ln"><span id="f-t1">Giá mua vào <b class="r">giảm mạnh hơn</b></span></div><div class="ln"><span id="f-t2">giá bán ra</span></div></div>
    <div class="card f-half l" id="f-hl"><div class="k">Mua vào</div><div class="v num">−5 triệu</div><div class="s">doanh nghiệp mua từ người dân</div></div>
    <div class="vline f-vl" id="f-vl"></div>
    <div class="card f-half r" id="f-hr"><div class="k">Bán ra</div><div class="v num">−3 triệu</div><div class="s">doanh nghiệp bán cho người dân</div></div>
    <div class="f-gl" id="f-gl">Chênh lệch mua – bán (triệu đồng/lượng)</div>
    <div class="f-bars">
      <div class="card f-b" id="f-b1"><div class="k"><span>Vàng miếng · phiên trước</span><b class="num">3</b></div><div class="trk"><div class="fill" id="f-f1" style="width:50%"></div></div></div>
      <div class="card f-b hot" id="f-b2"><div class="k"><span>Vàng miếng · 20/11</span><b class="num">5</b></div><div class="trk"><div class="fill" id="f-f2" style="width:83.3%"></div></div></div>
      <div class="card f-b max" id="f-b3"><div class="k"><span>Nhẫn trơn SJC · 20/11</span><b class="num">6</b></div><div class="trk"><div class="fill" id="f-f3" style="width:100%"></div></div></div>
    </div>""", """
    tl.fromTo('#f-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#f-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.15);
    tl.fromTo('#f-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.3);
    tl.fromTo('#f-vl',{scaleY:0},{scaleY:1,duration:0.5,ease:'power3.inOut'},%(a)s);
    tl.fromTo('#f-hl',{autoAlpha:0,x:-50},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},%(b)s);
    tl.fromTo('#f-hr',{autoAlpha:0,x:50},{autoAlpha:1,x:0,duration:0.5,ease:'power3.out'},%(c)s);
    tl.fromTo('#f-gl',{autoAlpha:0,y:10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},%(g)s);
    tl.fromTo('#f-b1',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(d)s);
    tl.fromTo('#f-f1',{scaleX:0},{scaleX:1,duration:0.6,ease:'power2.out'},%(d)s);
    tl.fromTo('#f-b2',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(e)s);
    tl.fromTo('#f-f2',{scaleX:0},{scaleX:1,duration:0.6,ease:'power2.out'},%(e)s);
    tl.fromTo('#f-b3',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(f)s);
    tl.fromTo('#f-f3',{scaleX:0},{scaleX:1,duration:0.6,ease:'power2.out'},%(f)s);""" % dict(
    a=T(0.6), b=T(0.8), c=T(1.7), g=T(2.6), d=T(4.0), e=T(4.5), f=T(6.6)))

# ---------------- 04 DATA MOMENT (191,3 → 134,2 + cột tỉ lệ) ----------------
BAR_MAX = 520
H_NOW = round(BAR_MAX * 134.2 / 191.3)
frames['04-data'] = frame('04-data', """
.d-kick { position:absolute; left:64px; top:190px; opacity:0; }
.d-ttl { top:240px; }
.d-pair { position:absolute; left:64px; right:64px; top:420px; height:250px; }
.d-n { position:absolute; top:0; width:420px; text-align:center; opacity:0; }
.d-n.l { left:0; } .d-n.r { right:0; }
.d-n .v { font-weight:900; font-size:132px; line-height:1; letter-spacing:-0.02em; white-space:nowrap; }
.d-n.l .v { color:rgba(255,255,255,0.45); } .d-n.r .v { color:#FF5A1F; }
.d-n .s { margin-top:18px; font-weight:700; font-size:26px; letter-spacing:0.1em; text-transform:uppercase; color:rgba(255,255,255,0.7); }
.d-mid { position:absolute; left:50%%; top:20px; width:112px; height:112px; margin-left:-56px; border-radius:50%%; border:3px solid #FF5A1F; opacity:0; }
.d-mid::before { content:""; position:absolute; left:26px; top:53px; width:48px; height:5px; background:#FF5A1F; border-radius:3px; }
.d-mid::after { content:""; position:absolute; left:56px; top:39px; width:0; height:0; border-top:17px solid transparent; border-bottom:17px solid transparent; border-left:26px solid #FF5A1F; }
.d-unit { position:absolute; left:0; right:0; top:200px; text-align:center; font-weight:600; font-size:26px; color:rgba(255,255,255,0.6); opacity:0; }
.d-chart { position:absolute; left:64px; right:64px; top:720px; height:%(bm)dpx; }
.d-base { position:absolute; left:0; right:0; bottom:0; height:2px; background:rgba(255,255,255,0.25); }
.d-col { position:absolute; bottom:0; width:300px; transform-origin:bottom center; border-radius:14px 14px 0 0; }
.d-col.a { left:90px; height:%(bm)dpx; background:linear-gradient(180deg, rgba(255,255,255,0.32), rgba(255,255,255,0.12)); }
.d-col.b { right:90px; height:%(hn)dpx; background:linear-gradient(180deg,#FF5A1F,#c8430f); box-shadow:0 0 40px rgba(255,90,31,0.25); }
.d-gap { position:absolute; right:90px; width:300px; top:0; height:%(gap)dpx; border:3px dashed #FF4438; border-bottom:none; border-radius:14px 14px 0 0; background:rgba(255,68,56,0.08); opacity:0; }
.d-gap span { position:absolute; left:0; right:0; top:50%%; transform:translateY(-50%%); text-align:center; font-weight:900; font-size:44px; color:#FF4438; }
.d-res { position:absolute; left:64px; right:64px; top:1290px; display:flex; justify-content:center; align-items:baseline; gap:28px; opacity:0; }
.d-res .a { font-weight:900; font-size:96px; line-height:1; color:#FF4438; }
.d-res .b { font-weight:800; font-size:52px; color:#fff; }
""" % dict(bm=BAR_MAX, hn=H_NOW, gap=BAR_MAX - H_NOW), """
    <div class="kick d-kick" id="d-kick">Vàng miếng SJC · bán ra</div>
    <div class="ttl d-ttl"><div class="ln"><span id="d-t1">Từ đỉnh lịch sử</span></div><div class="ln"><span id="d-t2">đến <b>hôm nay</b></span></div></div>
    <div class="d-pair">
      <div class="d-n l" id="d-nl"><div class="v num">191,3</div><div class="s">Đỉnh · cuối tháng 1</div></div>
      <div class="d-mid" id="d-mid"></div>
      <div class="d-n r" id="d-nr"><div class="v num">134,2</div><div class="s">Kết phiên 20/11</div></div>
      <div class="d-unit" id="d-unit">triệu đồng/lượng</div>
    </div>
    <div class="d-chart">
      <div class="d-col a" id="d-ca"></div>
      <div class="d-col b" id="d-cb"></div>
      <div class="d-gap" id="d-gap"><span class="num">−57</span></div>
      <div class="d-base"></div>
    </div>
    <div class="d-res" id="d-res"><span class="a num">−57 triệu</span><span class="b num">gần 30%</span></div>""", """
    tl.fromTo('#d-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#d-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.12);
    tl.fromTo('#d-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.26);
    tl.fromTo('#d-nl',{autoAlpha:0,y:30},{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'},%(a)s);
    tl.fromTo('#d-unit',{autoAlpha:0},{autoAlpha:1,duration:0.4},%(a)s);
    tl.fromTo('#d-ca',{scaleY:0},{scaleY:1,duration:0.8,ease:'power2.out'},%(a)s);
    tl.fromTo('#d-mid',{autoAlpha:0,scale:0.4},{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(2)'},%(m)s);
    tl.to('#d-mid',{keyframes:[{scale:1.12,duration:0.25},{scale:1,duration:0.25},{scale:1.12,duration:0.25},{scale:1,duration:0.25}]},%(m2)s);
    tl.fromTo('#d-nr',{autoAlpha:0,y:30},{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'},%(b)s);
    tl.fromTo('#d-cb',{scaleY:0},{scaleY:1,duration:0.8,ease:'power2.out'},%(b)s);
    tl.fromTo('#d-gap',{autoAlpha:0},{autoAlpha:1,duration:0.4,ease:'power2.out'},%(c)s);
    tl.fromTo('#d-res',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.7)'},%(e)s);""" % dict(
    a=T(0.6), m=T(2.9), m2=T(3.3), b=T(3.3), c=T(4.3), e=T(5.4)))

# ---------------- 05 CONTEXT (bảng đối xứng Trong nước | Thế giới + smash-cut) ----------------
frames['05-context'] = frame('05-context', """
#content { position:absolute; inset:0; transform-origin:50% 50%; }
.c-kick { position:absolute; left:64px; top:190px; opacity:0; }
.c-ttl { top:240px; }
.c-band { position:absolute; left:64px; right:64px; top:400px; height:250px; border-radius:20px; overflow:hidden; opacity:0; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.c-band img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 45%; }
.c-head { position:absolute; left:64px; right:64px; top:690px; height:60px; }
.c-head div { position:absolute; top:0; width:440px; text-align:center; font-weight:800; font-size:28px; letter-spacing:0.16em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.c-head .l { left:0; } .c-head .r { right:0; }
.c-vl { left:539px; top:690px; height:770px; }
.c-row { position:absolute; left:64px; right:64px; height:150px; }
.c-cell { position:absolute; top:0; width:440px; height:150px; padding:22px 24px; text-align:center; opacity:0; }
.c-cell.l { left:0; } .c-cell.r { right:0; }
.c-cell .v { font-weight:900; font-size:52px; line-height:1.05; color:#fff; white-space:nowrap; }
.c-cell .v.o { color:#FF5A1F; } .c-cell .v.r { color:#FF4438; }
.c-cell .s { margin-top:12px; font-weight:600; font-size:23px; color:rgba(255,255,255,0.7); }
.c-r1 { top:760px; } .c-r2 { top:930px; } .c-r3 { top:1100px; }
.c-gap { position:absolute; left:50%; top:1290px; transform:translateX(-50%); padding:26px 46px; border-radius:100px; background:#FF4438; white-space:nowrap; font-weight:900; font-size:44px; color:#fff; opacity:0; box-shadow:0 0 40px rgba(255,68,56,0.35); }
""", """
    <div id="content">
    <div class="kick c-kick" id="c-kick">Bối cảnh</div>
    <div class="ttl c-ttl"><div class="ln"><span id="c-t1">Áp lực đến từ</span></div><div class="ln"><span id="c-t2"><b>thị trường thế giới</b></span></div></div>
    <div class="c-band" id="c-band"><img src="assets/img/tuoitre.jpg" alt=""><div class="credit">Ảnh: Tuổi Trẻ</div></div>
    <div class="c-head"><div class="l" id="c-hl">Trong nước</div><div class="r" id="c-hr">Thế giới</div></div>
    <div class="vline c-vl" id="c-vl"></div>
    <div class="c-row c-r1">
      <div class="card c-cell l" id="c-1l"><div class="v r num">−5 triệu</div><div class="s">SJC mua vào · phiên 20/11</div></div>
      <div class="card c-cell r" id="c-1r"><div class="v o num">3.534 USD</div><div class="s">/ounce · thấp nhất hơn 1 năm</div></div>
    </div>
    <div class="c-row c-r2">
      <div class="card c-cell l" id="c-2l"><div class="v num">Chênh 5 triệu</div><div class="s">mua – bán vàng miếng SJC</div></div>
      <div class="card c-cell r" id="c-2r"><div class="v o num">99,3%</div><div class="s">đặt cược Fed tăng lãi suất T12</div></div>
    </div>
    <div class="c-row c-r3">
      <div class="card c-cell l" id="c-3l"><div class="v num">134,2</div><div class="s">triệu đồng/lượng · SJC bán ra</div></div>
      <div class="card c-cell r" id="c-3r"><div class="v o num">≈ 112,4</div><div class="s">triệu đồng/lượng quy đổi</div></div>
    </div>
    <div class="c-gap num" id="c-gap">Chênh gần 22 triệu/lượng</div>
    </div>
    <div class="cutflash" id="cutflash"></div>""", """
    tl.fromTo('#c-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#c-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.12);
    tl.fromTo('#c-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.26);
    tl.fromTo('#c-band',{autoAlpha:0,y:30},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.5);
    tl.fromTo('#c-band img',{scale:1.15},{scale:1.0,duration:%(d)s,ease:'none'},0.5);
    tl.fromTo('#c-hl',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(h)s);
    tl.fromTo('#c-hr',{autoAlpha:0,x:30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(h)s);
    tl.fromTo('#c-vl',{scaleY:0},{scaleY:1,duration:0.7,ease:'power3.inOut'},%(h)s);
    tl.fromTo('#c-1l',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'},%(r1)s);
    tl.fromTo('#c-1r',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'},%(r1)s);
    tl.fromTo('#c-2l',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'},%(r2)s);
    tl.fromTo('#c-2r',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'},%(r2b)s);
    tl.fromTo('#cutflash',{opacity:0},{opacity:0.55,duration:0.05,ease:'none'},%(sm)s);
    tl.to('#cutflash',{opacity:0,duration:0.16,ease:'power1.in'},%(sm2)s);
    tl.fromTo('#content',{scale:1},{scale:0.986,duration:0.06,ease:'power1.out'},%(sm)s);
    tl.to('#content',{scale:1,duration:0.14,ease:'power2.out'},%(sm3)s);
    tl.fromTo('#c-3l',{autoAlpha:0,x:-40},{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'},%(r3)s);
    tl.fromTo('#c-3r',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.45,ease:'power3.out'},%(r3b)s);
    tl.fromTo('#c-gap',{autoAlpha:0,scale:0.85},{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.8)'},%(g)s);""" % dict(
    d=DURS[4], h=T(1.6), r1=T(2.9), r2=T(6.5), r2b=T(9.3), sm=T(SMASH5), sm2=round(T(SMASH5) + 0.05, 2), sm3=round(T(SMASH5) + 0.061, 2),
    r3=T(13.75), r3b=T(14.9), g=T(17.2)))

# ---------------- 06 IMPACT (chia đôi NGANG: mua ở đỉnh / bán lại hôm nay) ----------------
frames['06-impact'] = frame('06-impact', """
.i-kick { position:absolute; left:64px; top:190px; opacity:0; color:#FF4438; }
.i-ttl { top:240px; }
.i-top, .i-bot { position:absolute; left:64px; right:64px; height:260px; padding:36px 40px; display:flex; justify-content:space-between; align-items:center; opacity:0; }
.i-top { top:420px; }
.i-bot { top:930px; }
.i-top .k, .i-bot .k { font-weight:700; font-size:30px; line-height:1.35; color:rgba(255,255,255,0.8); }
.i-top .k b, .i-bot .k b { display:block; font-weight:800; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:#FF5A1F; margin-bottom:8px; }
.i-top .v, .i-bot .v { text-align:right; font-weight:900; font-size:86px; line-height:1; white-space:nowrap; }
.i-top .v small, .i-bot .v small { display:block; margin-top:8px; font-size:24px; font-weight:600; color:rgba(255,255,255,0.65); }
.i-hl { position:absolute; left:64px; right:64px; top:705px; height:2px; background:linear-gradient(90deg, transparent, #FF4438 15%, #FF4438 85%, transparent); transform-origin:center; }
.i-res { position:absolute; left:0; right:0; top:742px; text-align:center; opacity:0; }
.i-res .a { display:inline-block; padding:22px 44px; border-radius:100px; background:rgba(255,68,56,0.14); border:3px solid #FF4438; font-weight:900; font-size:58px; color:#FF4438; white-space:nowrap; }
.i-why { position:absolute; left:64px; right:64px; top:1240px; display:flex; gap:20px; align-items:center; justify-content:center; }
.i-chip { padding:24px 30px; border-radius:16px; border:2px solid rgba(255,90,31,0.8); background:rgba(255,90,31,0.10); font-weight:800; font-size:34px; color:#fff; white-space:nowrap; opacity:0; }
.i-plus { font-weight:900; font-size:52px; color:#FF5A1F; opacity:0; }
.i-note { position:absolute; left:64px; right:64px; top:1390px; text-align:center; font-weight:600; font-size:24px; color:rgba(255,255,255,0.6); opacity:0; }
""", """
    <div class="kick i-kick" id="i-kick">Tác động</div>
    <div class="ttl i-ttl"><div class="ln"><span id="i-t1">Người mua ở vùng đỉnh</span></div><div class="ln"><span id="i-t2"><b class="r">lỗ nặng nếu bán lại</b></span></div></div>
    <div class="card i-top" id="i-top"><div class="k"><b>Mua ở đỉnh</b>giá bán ra<br>cuối tháng 1</div><div class="v num">191,3<small>triệu đồng/lượng</small></div></div>
    <div class="i-hl" id="i-hl"></div>
    <div class="i-res" id="i-res"><span class="a num">Lỗ hơn 62 triệu/lượng</span></div>
    <div class="card i-bot" id="i-bot"><div class="k"><b>Bán lại hôm nay</b>giá mua vào<br>kết phiên 20/11</div><div class="v num" style="color:#FF5A1F">129,2<small>triệu đồng/lượng</small></div></div>
    <div class="i-why"><div class="i-chip" id="i-c1">Giá giảm</div><div class="i-plus" id="i-p">+</div><div class="i-chip" id="i-c2">Chênh lệch mua – bán</div></div>
    <div class="i-note" id="i-note">Theo Dân Trí, kết phiên 20/11/2026</div>""", """
    tl.fromTo('#i-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#i-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.12);
    tl.fromTo('#i-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.26);
    tl.fromTo('#i-top',{autoAlpha:0,y:-40},{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'},%(a)s);
    tl.fromTo('#i-hl',{scaleX:0},{scaleX:1,duration:0.5,ease:'power3.inOut'},%(b)s);
    tl.fromTo('#i-res',{autoAlpha:0,scale:0.85},{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.8)'},%(b)s);
    tl.fromTo('#i-bot',{autoAlpha:0,y:40},{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'},%(c)s);
    tl.fromTo('#i-c1',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(d)s);
    tl.fromTo('#i-p',{autoAlpha:0,scale:0.5},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'},%(e)s);
    tl.fromTo('#i-c2',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(f)s);
    tl.fromTo('#i-note',{autoAlpha:0},{autoAlpha:1,duration:0.4},%(f)s);""" % dict(
    a=T(0.4), b=T(2.0), c=T(3.5), d=T(4.6), e=T(5.1), f=T(5.4)))

# ---------------- 07 CTA (fixed brand layout) ----------------
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:360px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-head { margin-top:30px; font-weight:900; font-size:66px; line-height:1.12; color:#fff; }
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
.t-opt .lab { margin-top:18px; font-weight:800; font-size:34px; line-height:1.2; color:#fff; }
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
        <div class="ln"><span id="t-h1">Nới chênh lệch mua – bán:</span></div>
        <div class="ln"><span id="t-h2" class="o">hợp lý hay người mua</span></div>
        <div class="ln"><span id="t-h3" class="o">chịu thiệt?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Hợp lý, để phòng rủi ro</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Người mua chịu thiệt</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>""", """
    tl.fromTo('#t-kicker',{autoAlpha:0,y:-12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0);
    tl.fromTo('#t-h1',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.2);
    tl.fromTo('#t-h2',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.36);
    tl.fromTo('#t-h3',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.5);
    tl.fromTo('#t-o1',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},2.7);
    tl.fromTo('#t-vs',{autoAlpha:0,scale:0.5},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'},3.4);
    tl.fromTo('#t-o2',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},3.7);
    tl.fromTo('#t-cta',{autoAlpha:0,y:22},{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'},5.0);
    tl.to('#t-cta',{keyframes:[{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'},{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'}]},5.6);
    tl.fromTo('#t-sign',{autoAlpha:0},{autoAlpha:1,duration:0.4},5.3);""")

os.makedirs('compositions/frames', exist_ok=True)
for k, v in frames.items():
    open(f'compositions/frames/{k}.html', 'w', encoding='utf-8').write(v)

# ---------------- captions (karaoke) ----------------
def norm(t):
    return re.sub(r'[^\w]', '', t.lower())

lines = open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')
caps = []
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
    chunk, chunks = [], []
    for w in timed:
        chunk.append(w)
        if len(chunk) >= 5 or (len(chunk) >= 3 and re.search(r'[,.?!:]$', w[0])):
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

cap_html, cap_js = "", ""
for ci, (st, en, c) in enumerate(caps):
    spans = " ".join(f'<span class="w" id="w{ci}_{k}">{w[0]}</span>' for k, w in enumerate(c))
    cap_html += f'<div class="cap" id="cap{ci}">{spans}</div>\n'
    cap_js += f"tl.set('#cap{ci}',{{autoAlpha:1}},{st:.2f});tl.set('#cap{ci}',{{autoAlpha:0}},{en:.2f});\n"
    for k, w in enumerate(c):
        cap_js += f"tl.to('#w{ci}_{k}',{{color:'#FF5A1F',duration:0.1,ease:'none'}},{w[1]:.2f});\n"


def mulberry32(seed):
    def r():
        nonlocal seed
        seed = (seed + 0x6D2B79F5) & 0xFFFFFFFF
        t = seed
        t = ((t ^ (t >> 15)) * (1 | t)) & 0xFFFFFFFF
        t = (t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return r

rand = mulberry32(20261120)
stars = "".join(f'<circle cx="{int(rand()*1080)}" cy="{int(rand()*1920)}" r="{1.5+rand()*1.5:.1f}" fill="#fff" opacity="{0.15+rand()*0.25:.2f}" />' for _ in range(42))

clips = ""
names = ['01-hook', '02-what', '03-facts', '04-data', '05-context', '06-impact', '07-cta']
for n, s, d in zip(names, STARTS, DURS):
    clips += f'<div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{s}" data-duration="{d}" data-track-index="1"></div>\n'

voices = ""
for i in range(7):
    voices += f'<audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{STARTS[i]+VOFF:.2f}" data-duration="{VDUR[i]:.3f}" data-track-index="10" data-audio-group="voiceover"></audio>\n'

SFX = [
    ("hook", "impact-bass-1", 0.7, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("w1", "pop", STARTS[1] + T(2.7), 0.4, 0.24),
    ("f3", "pop", STARTS[2] + T(6.6), 0.4, 0.26),
    ("dn", "impact-bass-1", STARTS[3] + T(5.4), 0.6, 0.3),
    ("cut5", "click-soft", STARTS[4] + T(SMASH5), 0.35, 0.32),
    ("gap5", "pop", STARTS[4] + T(17.2), 0.4, 0.26),
    ("res6", "impact-bass-1", STARTS[5] + T(2.0), 0.6, 0.28),
    ("o1", "pop", STARTS[6] + 2.7, 0.35, 0.3),
    ("o2", "pop", STARTS[6] + 3.7, 0.35, 0.3),
    ("cta", "chime", STARTS[6] + 5.0, 1.2, 0.32),
]
TRK = {a: (31 if a in ("dn", "hook", "cut5", "res6") else 30) for a, *_ in SFX}
sfx = "".join(f'<audio id="el-sfx-{a}" src="assets/sfx/{f}.mp3" data-start="{s:.2f}" data-duration="{d}" data-track-index="{TRK[a]}" data-volume="{v}"></audio>\n' for a, f, s, d, v in SFX)

bgm_attr = open('.bgm_attrs').read().strip() if os.path.exists('.bgm_attrs') else ""

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
#caps {{ position:absolute; left:80px; right:180px; top:1500px; height:110px; z-index:85; pointer-events:none; }}
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
{clips}<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: Dân Trí, VnExpress, Tuổi Trẻ</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
<div id="caps">
{cap_html}</div>
{voices}<audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"{(' ' + bgm_attr) if bgm_attr else ''}></audio>
{sfx}</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.set('#brand-anchor',{{opacity:1}},{STARTS[1]});
tl.to('.blob',{{x:'+=40',y:'-=30',duration:18,ease:'sine.inOut',repeat:3,yoyo:true,stagger:3}},0);
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:17,yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{cap_js}window.__timelines['main'] = tl;
</script>
</body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(index)
print('starts', STARTS, 'durs', DURS, 'total', TOTAL, 'caps', len(caps))
