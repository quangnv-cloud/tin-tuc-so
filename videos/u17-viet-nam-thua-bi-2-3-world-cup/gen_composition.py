#!/usr/bin/env python3
"""Generate compositions + index.html for u17-viet-nam-thua-bi-2-3-world-cup (style 5-map-and-geo)."""
import json, os, re, difflib, sys, subprocess

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
SMASH4 = 5.16  # voice-local "Dù trước đó" in act 4

GEO = json.load(open('assets/img/geo-countries.json'))  # projected paths, viewBox 0 0 1080 570


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
.card { border-radius:20px; background:rgba(18,23,36,0.94); border:1px solid rgba(255,255,255,0.10); box-shadow:0 0 40px rgba(255,90,31,0.14); }
.pin { display:inline-block; position:relative; width:30px; height:30px; flex:none; border-radius:50% 50% 50% 0; transform:rotate(-45deg); background:#FF5A1F; }
.pin::after { content:""; position:absolute; left:9px; top:9px; width:12px; height:12px; border-radius:50%; background:#0B0E14; }
.pin.w { background:rgba(255,255,255,0.85); }
.mapbg { position:absolute; opacity:0.0; pointer-events:none; }
.mapbg img { display:block; width:100%; height:100%; }
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
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:30% 30%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0.0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:750px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:30px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:118px; line-height:1.02; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.hk-name.o { color:#FF5A1F; font-size:104px; }
.hk-sub { margin-top:28px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:32px; margin-top:68px; }
.hk-tag { font-weight:800; font-size:48px; line-height:1; color:#FF5A1F; opacity:0; white-space:nowrap; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: VnExpress</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress · 21/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">U17 Việt Nam</div></div>
      <div class="hk-name-wrap"><div class="hk-name o num" id="hk-n2">thua Bỉ 2–3</div></div>
      <div class="hk-sub" id="hk-sub">trận ra quân <b>U17 World Cup 2026</b> tại Qatar</div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>2 bàn thắng lịch sử</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Thua sát nút á quân châu Âu</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.6);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.85);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.5);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.6);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.85);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (ảnh + ghim địa danh + thẻ thông tin) ----------------
D2 = DURS[1]
frames['02-what'] = frame('02-what', """
.w-kick { position:absolute; left:64px; top:190px; opacity:0; }
.w-ttl { top:240px; }
.w-img { position:absolute; left:64px; right:64px; top:430px; height:600px; border-radius:20px; overflow:hidden; opacity:0; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 40%; }
.w-geo { position:absolute; left:30px; top:30px; display:flex; align-items:center; gap:16px; padding:14px 22px 14px 18px; border-radius:14px; background:rgba(11,14,20,0.82); border:1.5px solid rgba(255,90,31,0.8); opacity:0; }
.w-geo .pin { width:34px; height:34px; } .w-geo .pin::after { left:11px; top:11px; }
.w-geo .t { font-weight:800; font-size:30px; color:#fff; line-height:1.1; }
.w-geo .t small { display:block; font-weight:600; font-size:20px; letter-spacing:0.14em; text-transform:uppercase; color:#FF5A1F; margin-bottom:4px; }
.w-ring { position:absolute; left:47px; top:47px; width:28px; height:28px; border-radius:50%; border:3px solid #FF5A1F; opacity:0; }
.w-info { position:absolute; left:64px; right:64px; top:1070px; padding:14px 34px; }
.w-row { display:flex; align-items:center; gap:22px; height:88px; border-bottom:1px solid rgba(255,255,255,0.09); opacity:0; }
.w-row:last-child { border-bottom:none; }
.w-row .k { width:250px; font-weight:700; font-size:24px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.w-row .v { flex:1; font-weight:800; font-size:34px; color:#fff; white-space:nowrap; }
.w-row .v b { color:#FF5A1F; font-weight:900; }
""", """
    <div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div>
    <div class="ttl w-ttl"><div class="ln"><span id="w-h1">Ra quân <b>bảng G</b>, gặp ngay</span></div><div class="ln"><span id="w-h2">á quân châu Âu</span></div></div>
    <div class="w-img" id="w-img"><img src="assets/img/tuoitre.jpg" alt=""><div class="credit">Ảnh: Tuổi Trẻ</div>
      <div class="w-geo" id="w-geo"><span class="pin"></span><div class="t"><small>Địa điểm</small>Học viện Aspire · Qatar</div></div>
    </div>
    <div class="card w-info" id="w-info">
      <div class="w-row" id="w-r1"><div class="k">Thời gian</div><div class="v">Tối <b>20/11/2026</b></div></div>
      <div class="w-row" id="w-r2"><div class="k">Huấn luyện viên</div><div class="v">Cristiano Roland</div></div>
      <div class="w-row" id="w-r3"><div class="k">Đối thủ</div><div class="v">U17 Bỉ · <b>á quân châu Âu</b></div></div>
      <div class="w-row" id="w-r4"><div class="k">Giải đấu</div><div class="v">U17 World Cup · <b>lượt 1</b></div></div>
    </div>""", """
    tl.fromTo('#w-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#w-h1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.15);
    tl.fromTo('#w-h2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.3);
    tl.fromTo('#w-img',{autoAlpha:0,y:40},{autoAlpha:1,y:0,duration:0.6,ease:'power3.out'},0.35);
    tl.fromTo('#w-img img',{scale:1.14},{scale:1.0,duration:%(d)s,ease:'none'},0.35);
    tl.fromTo('#w-geo',{autoAlpha:0,y:-30},{autoAlpha:1,y:0,duration:0.5,ease:'bounce.out'},%(geo)s);
    tl.fromTo('#w-info',{autoAlpha:0},{autoAlpha:1,duration:0.3},%(r1)s);
    tl.fromTo('#w-r1',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r1)s);
    tl.fromTo('#w-r2',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r2)s);
    tl.fromTo('#w-r3',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r3)s);
    tl.fromTo('#w-r4',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r4)s);""" % dict(
    d=D2, geo=T(1.4), r1=T(0.3), r2=T(2.6), r3=T(4.4), r4=T(5.6)))

# ---------------- 03 KEY FACTS (diễn biến 5 bàn, bản đồ mờ phía sau, ghim đội) ----------------
GOALS = [
    ("4'", "VN", "Lê Sỹ Bách", "đánh gót mở tỷ số", T(0.1)),
    ("39'", "BỈ", "Moorthamer", "gỡ hoà 1–1", T(4.2)),
    ("42'", "BỈ", "Achahbar", "vượt lên 2–1", T(4.98)),
    ("60'", "BỈ", "Philips", "nâng lên 3–1", T(5.62)),
    ("84'", "VN", "Chu Ngọc Nguyễn Lực", "sút thẳng từ phạt góc", T(6.56)),
]
g_html, g_js = "", ""
for i, (m, team, who, what, t) in enumerate(GOALS):
    vn = team == "VN"
    g_html += (f'<div class="card f-g{" vn" if vn else ""}" id="f-g{i}"><div class="m num">{m}</div>'
               f'<div class="tm"><span class="pin{"" if vn else " w"}"></span><span>{"Việt Nam" if vn else "Bỉ"}</span></div>'
               f'<div class="who">{who}<small>{what}</small></div></div>\n')
    g_js += f"    tl.fromTo('#f-g{i}',{{autoAlpha:0,x:{-60 if vn else 60}}},{{autoAlpha:1,x:0,duration:0.42,ease:'power3.out'}},{t});\n"
frames['03-facts'] = frame('03-facts', """
.f-map { left:-760px; top:300px; width:2700px; height:1425px; }
.f-kick { position:absolute; left:64px; top:190px; opacity:0; }
.f-ttl { top:240px; }
.f-list { position:absolute; left:64px; right:64px; top:440px; display:flex; flex-direction:column; gap:16px; }
.f-g { position:relative; display:flex; align-items:center; gap:24px; height:132px; padding:0 28px; opacity:0; }
.f-g.vn { border-color:rgba(255,90,31,0.75); background:rgba(255,90,31,0.10); }
.f-g .m { width:120px; font-weight:900; font-size:56px; color:rgba(255,255,255,0.85); }
.f-g.vn .m { color:#FF5A1F; }
.f-g .tm { display:flex; align-items:center; gap:12px; width:190px; font-weight:700; font-size:26px; color:rgba(255,255,255,0.75); }
.f-g .pin { width:24px; height:24px; } .f-g .pin::after { left:7px; top:7px; width:10px; height:10px; }
.f-g .who { flex:1; font-weight:800; font-size:34px; line-height:1.15; color:#fff; }
.f-g .who small { display:block; margin-top:4px; font-weight:600; font-size:24px; color:rgba(255,255,255,0.65); }
.f-score { position:absolute; left:64px; right:64px; top:1240px; height:170px; display:flex; align-items:center; justify-content:center; gap:36px; opacity:0; }
.f-score .lab { font-weight:700; font-size:24px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.f-score .s { font-weight:900; font-size:84px; color:#fff; white-space:nowrap; }
.f-score .s .o { color:#FF5A1F; }
.f-score .t { font-weight:800; font-size:34px; color:#fff; }
""", f"""
    <div class="mapbg f-map" id="f-map"><img src="assets/img/world.svg" alt=""></div>
    <div class="kick f-kick" id="f-kick">Diễn biến</div>
    <div class="ttl f-ttl"><div class="ln"><span id="f-t1"><b>5 bàn thắng</b> trong 90 phút</span></div></div>
    <div class="f-list">
{g_html}    </div>
    <div class="card f-score" id="f-score"><div class="lab">Chung cuộc</div><div class="t">Việt Nam</div><div class="s num"><span class="o">2</span> – 3</div><div class="t">Bỉ</div></div>""", f"""
    tl.fromTo('#f-map',{{autoAlpha:0}},{{autoAlpha:0.9,duration:0.8,ease:'power1.out'}},0);
    tl.fromTo('#f-map',{{x:0}},{{x:-60,duration:{DURS[2]},ease:'none'}},0);
    tl.fromTo('#f-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#f-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
{g_js}    tl.fromTo('#f-score',{{autoAlpha:0,scale:0.9}},{{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.6)'}},{T(8.3)});""")

# ---------------- 04 DATA MOMENT (map-pin khổng lồ chứa số 2 + các kỳ World Cup trước) ----------------
frames['04-data'] = frame('04-data', """
.d-map { left:-1150px; top:240px; width:2700px; height:1425px; }
.d-kick { position:absolute; left:64px; top:190px; opacity:0; }
.d-ttl { top:240px; }
.d-pinwrap { position:absolute; left:50%; top:420px; width:400px; height:520px; margin-left:-200px; opacity:0; }
.d-pin { position:absolute; left:40px; top:0; width:320px; height:320px; border-radius:50% 50% 50% 0; transform:rotate(-45deg); background:linear-gradient(135deg,#FF5A1F,#FF4438); box-shadow:0 0 60px rgba(255,90,31,0.45); }
.d-pin-in { position:absolute; left:80px; top:40px; width:240px; height:240px; border-radius:50%; background:#0B0E14; display:flex; align-items:center; justify-content:center; }
.d-pin-in .n { font-weight:900; font-size:170px; line-height:1; color:#FF5A1F; }
.d-shadow { position:absolute; left:120px; top:470px; width:160px; height:30px; border-radius:50%; background:rgba(255,90,31,0.35); filter:blur(8px); transform-origin:center; }
.d-cap { position:absolute; left:64px; right:64px; top:950px; text-align:center; font-weight:800; font-size:38px; color:#fff; opacity:0; }
.d-cap b { color:#FF5A1F; }
.d-rows { position:absolute; left:64px; right:64px; top:1050px; display:flex; flex-direction:column; gap:16px; }
.d-r { display:flex; align-items:center; gap:22px; height:112px; padding:0 30px; opacity:0; }
.d-r .pin { width:26px; height:26px; } .d-r .pin::after { left:8px; top:8px; width:10px; height:10px; }
.d-r .k { flex:1; font-weight:800; font-size:34px; color:#fff; }
.d-r .k small { font-weight:600; font-size:26px; color:rgba(255,255,255,0.6); margin-left:12px; }
.d-r .v { font-weight:800; font-size:32px; color:rgba(255,255,255,0.55); white-space:nowrap; }
.d-r.hot { border-color:rgba(255,90,31,0.8); background:rgba(255,90,31,0.12); }
.d-r.hot .v { color:#FF5A1F; font-weight:900; font-size:40px; }
""", """
    <div class="mapbg d-map" id="d-map"><img src="assets/img/world.svg" alt=""></div>
    <div class="cutflash" id="cutflash"></div>
    <div id="content" style="position:absolute;inset:0;">
    <div class="kick d-kick" id="d-kick">Cột mốc</div>
    <div class="ttl d-ttl"><div class="ln"><span id="d-t1">Bàn thắng <b>đầu tiên</b> tại một</span></div><div class="ln"><span id="d-t2">World Cup 11 người</span></div></div>
    <div class="d-pinwrap" id="d-pinwrap"><div class="d-shadow" id="d-shadow"></div><div class="d-pin"></div><div class="d-pin-in"><span class="n num" id="d-n">0</span></div></div>
    <div class="d-cap" id="d-cap">bàn thắng của <b>Việt Nam</b> ở World Cup 11 người</div>
    <div class="d-rows">
      <div class="card d-r" id="d-r1"><span class="pin w"></span><div class="k">U20 nam<small>2017</small></div><div class="v">chưa ghi bàn</div></div>
      <div class="card d-r" id="d-r2"><span class="pin w"></span><div class="k">Tuyển nữ<small>2023</small></div><div class="v">chưa ghi bàn</div></div>
      <div class="card d-r hot" id="d-r3"><span class="pin"></span><div class="k">U17 nam<small>2026</small></div><div class="v num">2 bàn</div></div>
    </div>
    </div>""", """
    tl.fromTo('#d-map',{autoAlpha:0},{autoAlpha:0.9,duration:0.8,ease:'power1.out'},0);
    tl.fromTo('#d-map',{scale:1},{scale:1.08,duration:%(dur)s,ease:'none'},0);
    tl.fromTo('#d-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#d-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.12);
    tl.fromTo('#d-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.26);
    tl.fromTo('#d-pinwrap',{autoAlpha:0,y:-260},{autoAlpha:1,y:0,duration:0.75,ease:'bounce.out'},%(pin)s);
    tl.fromTo('#d-shadow',{scaleX:0.3},{scaleX:1,duration:0.75,ease:'bounce.out'},%(pin)s);
    tl.fromTo('#d-n',{textContent:0},{textContent:2,duration:0.6,ease:'none',snap:{textContent:1}},%(cnt)s);
    tl.fromTo('#d-cap',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},%(cap)s);
    tl.fromTo('#cutflash',{opacity:0},{opacity:0.55,duration:0.05,ease:'none'},%(sm)s);
    tl.to('#cutflash',{opacity:0,duration:0.16,ease:'power1.in'},%(sm2)s);
    tl.fromTo('#content',{scale:1},{scale:0.986,duration:0.06,ease:'power1.out'},%(sm)s);
    tl.to('#content',{scale:1,duration:0.14,ease:'power2.out'},%(sm3)s);
    tl.fromTo('#d-r1',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r1)s);
    tl.fromTo('#d-r2',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r2)s);
    tl.fromTo('#d-r3',{autoAlpha:0,y:24,scale:0.95},{autoAlpha:1,y:0,scale:1,duration:0.45,ease:'back.out(1.6)'},%(r3)s);""" % dict(
    dur=DURS[3], pin=T(1.0), cnt=T(1.6), cap=T(2.3), sm=T(SMASH4), sm2=round(T(SMASH4) + 0.05, 2), sm3=round(T(SMASH4) + 0.061, 2),
    r1=T(6.5), r2=T(8.7), r3=T(9.6)))

# ---------------- 05 CONTEXT (bản đồ thế giới, 4 nước bảng G tô cam tuần tự + bảng xếp hạng) ----------------
C = {k: v for k, v in GEO.items()}
# label boxes in map coords (x,y of label anchor) -> placed in HTML over the 1080x570 map at top 330
LAB = {"ML": (330, 330, "Mali"), "BE": (340, 70, "Bỉ"), "VN": (975, 215, "Việt Nam"), "NZ": (840, 500, "New Zealand")}
paths = "".join(f'<path id="c-{k}" d="{C[k]["d"]}" fill="#FF5A1F" fill-opacity="0" stroke="#FF5A1F" stroke-width="1.5" stroke-opacity="0"/>' for k in ("VN", "BE", "ML", "NZ") if C[k]["d"])
dots = ""
lines = ""
for k, (lx, ly, name) in LAB.items():
    cx, cy = C[k]["c"]
    dots += f'<circle id="dot-{k}" cx="{cx}" cy="{cy}" r="7" fill="#FF5A1F" opacity="0"/>'
    lines += f'<line id="ln-{k}" x1="{cx}" y1="{cy}" x2="{lx}" y2="{ly}" stroke="#FF5A1F" stroke-width="2" opacity="0"/>'
qx, qy = C["QA"]["c"]
labels = "".join(f'<div class="x-lab" id="lab-{k}" style="left:{lx}px;top:{330 + ly}px">{name}</div>' for k, (lx, ly, name) in LAB.items())
STAND = [("ML", "Mali", 3, "+3"), ("BE", "Bỉ", 3, "+1"), ("VN", "Việt Nam", 0, "−1"), ("NZ", "New Zealand", 0, "−3")]
rows = ""
for i, (k, n, p, gd) in enumerate(STAND):
    rows += (f'<div class="x-row{" vn" if k == "VN" else ""}{" q" if i < 2 else ""}" id="x-r{i}"><div class="pos num">{i+1}</div>'
             f'<div class="nm">{n}</div><div class="gd num">{gd}</div><div class="pt num">{p}</div></div>\n')
frames['05-context'] = frame('05-context', """
.x-kick { position:absolute; left:64px; top:190px; opacity:0; }
.x-ttl { top:240px; font-size:56px; }
.x-map { position:absolute; left:0; top:330px; width:1080px; height:570px; opacity:0; }
.x-map img, .x-map svg { position:absolute; inset:0; width:100%; height:100%; }
.x-lab { position:absolute; transform:translate(-50%,-50%); padding:8px 16px; border-radius:10px; background:rgba(11,14,20,0.9); border:1.5px solid #FF5A1F; font-weight:800; font-size:26px; color:#fff; white-space:nowrap; opacity:0; z-index:3; }
.x-host { position:absolute; display:flex; align-items:center; gap:10px; transform:translate(-14px,-44px); opacity:0; z-index:3; }
.x-host .pin { width:30px; height:30px; }
.x-host span { padding:6px 12px; border-radius:8px; background:rgba(255,255,255,0.92); font-weight:800; font-size:22px; color:#0B0E14; white-space:nowrap; }
.x-tbl { position:absolute; left:64px; right:64px; top:930px; padding:18px 30px 14px; opacity:0; }
.x-hd { display:flex; align-items:center; height:50px; font-weight:700; font-size:22px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.55); border-bottom:1px solid rgba(255,255,255,0.12); }
.x-hd .a { flex:1; } .x-hd .b { width:150px; text-align:right; } .x-hd .c { width:110px; text-align:right; }
.x-row { display:flex; align-items:center; height:86px; border-bottom:1px solid rgba(255,255,255,0.08); opacity:0; }
.x-row:last-child { border-bottom:none; }
.x-row .pos { width:60px; font-weight:900; font-size:32px; color:rgba(255,255,255,0.5); }
.x-row .nm { flex:1; font-weight:800; font-size:36px; color:#fff; }
.x-row .gd { width:150px; text-align:right; font-weight:700; font-size:32px; color:rgba(255,255,255,0.75); }
.x-row .pt { width:110px; text-align:right; font-weight:900; font-size:40px; color:#fff; }
.x-row.q .pos { color:#FF5A1F; }
.x-row.vn { background:rgba(255,90,31,0.14); border-radius:12px; margin:0 -16px; padding:0 16px; }
.x-row.vn .nm, .x-row.vn .pt { color:#FF5A1F; }
.x-rule { position:absolute; left:64px; right:64px; top:1404px; display:flex; align-items:center; gap:16px; padding:18px 26px; border-radius:14px; border:1.5px solid rgba(255,90,31,0.8); background:rgba(255,90,31,0.10); opacity:0; }
.x-rule .k { font-weight:800; font-size:22px; letter-spacing:0.14em; text-transform:uppercase; color:#FF5A1F; white-space:nowrap; }
.x-rule .v { font-weight:700; font-size:28px; color:#fff; white-space:nowrap; }
""", f"""
    <div class="kick x-kick" id="x-kick">Bảng G sau lượt 1</div>
    <div class="ttl x-ttl"><div class="ln"><span id="x-t1">Bốn châu lục, <b>một bảng đấu</b></span></div></div>
    <div class="x-map" id="x-map"><img src="assets/img/world.svg" alt="">
      <svg viewBox="0 0 1080 570">{paths}{lines}{dots}</svg>
    </div>
    <div class="x-host" id="x-host" style="left:{qx}px;top:{330 + qy}px"><span class="pin w"></span><span>Qatar · chủ nhà</span></div>
    {labels}
    <div class="card x-tbl" id="x-tbl"><div class="x-hd"><div class="a">Đội</div><div class="b">Hiệu số</div><div class="c">Điểm</div></div>
{rows}    </div>
    <div class="x-rule" id="x-rule"><div class="k">Đi tiếp</div><div class="v">2 đội đầu bảng + 8 đội thứ ba tốt nhất</div></div>""",
f"""
    tl.fromTo('#x-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#x-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.12);
    tl.fromTo('#x-map',{{autoAlpha:0,scale:1.06}},{{autoAlpha:1,scale:1,duration:0.8,ease:'power2.out'}},0.1);
    tl.fromTo('#x-host',{{autoAlpha:0,y:-40}},{{autoAlpha:1,y:0,duration:0.5,ease:'bounce.out'}},0.5);
    tl.fromTo('#x-tbl',{{autoAlpha:0,y:30}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(0.5)});
""" + "".join(
    f"    tl.to('#c-{k}',{{attr:{{'fill-opacity':0.75,'stroke-opacity':1}},duration:0.5,ease:'power2.out'}},{t});\n"
    f"    tl.fromTo('#dot-{k}',{{opacity:0}},{{opacity:1,duration:0.3}},{t});\n"
    f"    tl.fromTo('#ln-{k}',{{opacity:0}},{{opacity:0.9,duration:0.3}},{t});\n"
    f"    tl.fromTo('#lab-{k}',{{autoAlpha:0,scale:0.8}},{{autoAlpha:1,scale:1,duration:0.35,ease:'back.out(1.8)'}},{round(t + 0.1, 2)});\n"
    for k, t in (("ML", T(0.84)), ("NZ", T(1.2)), ("BE", T(2.8)), ("VN", T(3.78)))) +
"".join(f"    tl.fromTo('#x-r{i}',{{autoAlpha:0,x:-24}},{{autoAlpha:1,x:0,duration:0.38,ease:'power3.out'}},{t});\n"
        for i, t in enumerate((T(2.4), T(2.8), T(3.78), T(4.2)))) +
f"    tl.fromTo('#x-rule',{{autoAlpha:0,y:20}},{{autoAlpha:1,y:0,duration:0.42,ease:'power3.out'}},{T(5.64)});")

# ---------------- 06 IMPACT (2 thẻ địa danh trượt từ 2 phía + trích dẫn HLV, nền bản đồ mờ) ----------------
frames['06-impact'] = frame('06-impact', """
.i-map { left:-300px; top:560px; width:1700px; height:897px; }
.i-kick { position:absolute; left:64px; top:190px; opacity:0; }
.i-ttl { top:240px; }
.i-card { position:absolute; left:64px; right:64px; height:300px; padding:34px 38px; opacity:0; }
.i-c1 { top:440px; } .i-c2 { top:770px; }
.i-card .hd { display:flex; align-items:center; gap:16px; }
.i-card .hd .pin { width:32px; height:32px; } .i-card .hd .pin::after { left:10px; top:10px; }
.i-card .hd .org { font-weight:900; font-size:44px; color:#fff; }
.i-card .hd .reg { margin-left:auto; padding:6px 14px; border-radius:8px; border:1.5px solid rgba(255,90,31,0.7); font-weight:700; font-size:20px; letter-spacing:0.14em; text-transform:uppercase; color:#FF5A1F; }
.i-card .q { margin-top:26px; font-weight:700; font-size:38px; line-height:1.3; color:rgba(255,255,255,0.92); }
.i-card .q b { color:#FF5A1F; font-weight:800; }
.i-quote { position:absolute; left:64px; right:64px; top:1100px; height:330px; padding:40px 44px; border-radius:20px; background:linear-gradient(135deg, rgba(255,90,31,0.22), rgba(255,68,56,0.10)); border:2px solid #FF5A1F; box-shadow:0 0 40px rgba(255,90,31,0.18); opacity:0; overflow:hidden; }
.i-quote .mk { position:absolute; right:30px; top:-60px; font-weight:900; font-size:300px; line-height:1; color:rgba(255,90,31,0.18); }
.i-quote .t { position:relative; font-weight:900; font-size:50px; line-height:1.2; color:#fff; }
.i-quote .by { position:relative; margin-top:26px; font-weight:700; font-size:26px; letter-spacing:0.06em; color:rgba(255,255,255,0.75); }
.i-quote .by b { color:#FF5A1F; }
""", """
    <div class="mapbg i-map" id="i-map"><img src="assets/img/world.svg" alt=""></div>
    <div class="kick i-kick" id="i-kick">Sau trận đấu</div>
    <div class="ttl i-ttl"><div class="ln"><span id="i-t1">Hai siêu phẩm được</span></div><div class="ln"><span id="i-t2"><b>FIFA và AFC</b> khen ngợi</span></div></div>
    <div class="card i-card i-c1" id="i-c1"><div class="hd"><span class="pin"></span><span class="org">FIFA</span><span class="reg">Toàn cầu</span></div><div class="q">Pha đánh gót <b>“đậm chất Zlatan”</b> của Lê Sỹ Bách ở phút thứ 4</div></div>
    <div class="card i-card i-c2" id="i-c2"><div class="hd"><span class="pin"></span><span class="org">AFC</span><span class="reg">Châu Á</span></div><div class="q">“Dù thất bại nhưng đây là <b>trận đấu đáng khen</b> của U17 Việt Nam”</div></div>
    <div class="i-quote" id="i-quote"><div class="mk">”</div><div class="t">“Đội tuyển xứng đáng với mọi lời khen dù thất bại”</div><div class="by">HLV <b>Cristiano Roland</b> · theo VnExpress</div></div>""", """
    tl.fromTo('#i-map',{autoAlpha:0},{autoAlpha:0.8,duration:0.8,ease:'power1.out'},0);
    tl.fromTo('#i-map',{x:0},{x:-50,duration:%(d)s,ease:'none'},0);
    tl.fromTo('#i-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.05);
    tl.fromTo('#i-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.12);
    tl.fromTo('#i-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.26);
    tl.fromTo('#i-c1',{autoAlpha:0,x:-140},{autoAlpha:1,x:0,duration:0.55,ease:'power3.out'},%(a)s);
    tl.fromTo('#i-c2',{autoAlpha:0,x:140},{autoAlpha:1,x:0,duration:0.55,ease:'power3.out'},%(b)s);
    tl.fromTo('#i-quote',{autoAlpha:0,y:40,scale:0.96},{autoAlpha:1,y:0,scale:1,duration:0.55,ease:'back.out(1.4)'},%(c)s);""" % dict(
    d=DURS[5], a=T(0.78), b=T(1.32), c=T(3.56)))

# ---------------- 07 CTA (fixed brand layout) ----------------
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:330px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-ctx { display:inline-flex; align-items:center; gap:12px; margin-top:26px; padding:10px 20px; border-radius:10px; border:1.5px solid rgba(255,255,255,0.18); font-weight:600; font-size:24px; color:rgba(255,255,255,0.8); opacity:0; }
.t-ctx .pin { width:22px; height:22px; } .t-ctx .pin::after { left:6px; top:6px; width:10px; height:10px; }
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
      <div class="t-ctx" id="t-ctx"><span class="pin"></span>Lượt 2 · 23/11 · gặp New Zealand</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">U17 Việt Nam sẽ</span></div>
        <div class="ln"><span id="t-h2" class="o">giành 3 điểm</span></div>
        <div class="ln"><span id="t-h3">hay thể lực vẫn là nỗi lo?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Đủ sức thắng New Zealand</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Thể lực vẫn là nỗi lo</div></div>
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
    o1=T(4.0), vs=T(4.6), o2=T(5.0), cta=T(6.8), pulse=round(T(6.8) + 0.6, 2), sign=T(7.1)))

os.makedirs('compositions/frames', exist_ok=True)
for k, v in frames.items():
    open(f'compositions/frames/{k}.html', 'w', encoding='utf-8').write(v)

# ---------------- captions (karaoke) ----------------
def norm(t):
    return re.sub(r'[^\w]', '', t.lower())

slines = open('SCRIPT.md', encoding='utf-8').read().strip().split('\n')
caps = []
for i, line in enumerate(slines):
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

rand = mulberry32(20261121)
stars = "".join(f'<circle cx="{int(rand()*1080)}" cy="{int(rand()*1920)}" r="{1.5+rand()*1.5:.1f}" fill="#fff" opacity="{0.15+rand()*0.25:.2f}" />' for _ in range(40))

clips = ""
names = ['01-hook', '02-what', '03-facts', '04-data', '05-context', '06-impact', '07-cta']
for n, s, d in zip(names, STARTS, DURS):
    clips += f'<div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{s}" data-duration="{d}" data-track-index="1"></div>\n'

voices = ""
for i in range(7):
    voices += f'<audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{STARTS[i]+VOFF:.2f}" data-duration="{VDUR[i]:.3f}" data-track-index="10" data-audio-group="voiceover"></audio>\n'

SFX = [
    ("hook", "impact-bass-1", 0.6, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("geo", "pop", STARTS[1] + T(1.4), 0.4, 0.24),
    ("g5", "pop", STARTS[2] + T(6.56), 0.4, 0.26),
    ("pin", "impact-bass-1", STARTS[3] + T(1.0) + 0.3, 0.6, 0.3),
    ("cut4", "click-soft", STARTS[3] + T(SMASH4), 0.35, 0.32),
    ("vn5", "pop", STARTS[4] + T(3.78), 0.4, 0.26),
    ("q6", "pop", STARTS[5] + T(3.56), 0.4, 0.24),
    ("o1", "pop", STARTS[6] + T(4.0), 0.35, 0.3),
    ("o2", "pop", STARTS[6] + T(5.0), 0.35, 0.3),
    ("cta", "chime", STARTS[6] + T(6.8), 1.2, 0.32),
]
TRK = {a: (31 if a in ("pin", "hook", "cut4") else 30) for a, *_ in SFX}
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
#caps {{ position:absolute; left:80px; right:180px; top:1505px; height:110px; z-index:85; pointer-events:none; }}
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
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:17,yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{cap_js}window.__timelines['main'] = tl;
</script>
</body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(index)
print('starts', STARTS, 'durs', DURS, 'total', TOTAL, 'caps', len(caps))
