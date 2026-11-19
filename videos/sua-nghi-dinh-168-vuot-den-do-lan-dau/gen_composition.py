#!/usr/bin/env python3
"""Generate compositions + index.html for sua-nghi-dinh-168-vuot-den-do-lan-dau (style 3-ticker-tape)."""
import json, os, re, difflib, sys, subprocess

P = sys.argv[1] if len(sys.argv) > 1 else '.'
os.chdir(P)

VOFF = 0.10
VDUR = [float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                        f'assets/voice/line{i+1}.mp3']).decode().strip()) for i in range(7)]
PAD = [0.4, 0.4, 0.4, 0.45, 0.45, 0.45, 1.25]
DURS = [round(v + VOFF + p, 2) for v, p in zip(VDUR, PAD)]
STARTS = [0.0]
for d in DURS[:-1]:
    STARTS.append(round(STARTS[-1] + d, 2))
TOTAL = round(STARTS[-1] + DURS[-1], 2)
SMASH5 = 9.4 + VOFF  # local time act 5: "Cục Cảnh sát giao thông nhấn mạnh"

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
.cutflash { position:absolute; inset:0; z-index:6; pointer-events:none; opacity:0; background:linear-gradient(180deg, rgba(255,90,31,0.4), rgba(255,68,56,0.18)); }
.tape { position:absolute; left:0; right:0; height:86px; border-top:3px solid #FF5A1F; border-bottom:3px solid #FF5A1F; background:rgba(11,14,20,0.92); overflow:visible; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.tape .live { position:absolute; left:40px; top:-55px; height:52px; z-index:2; display:flex; align-items:center; gap:12px; padding:0 22px; border-radius:8px 8px 0 0; background:#FF5A1F; font-weight:900; font-size:28px; letter-spacing:0.14em; color:#0B0E14; }
.tape .live .bl { width:14px; height:14px; border-radius:50%; background:#0B0E14; }
.tape .rail { position:absolute; left:0; right:0; top:0; bottom:0; overflow:hidden; }
.tape .run { position:absolute; left:0; top:0; bottom:0; display:flex; align-items:center; white-space:nowrap; font-weight:700; font-size:32px; color:#fff; }
.tape .run i { font-style:normal; color:#FF5A1F; margin:0 26px; }
.term { position:absolute; left:56px; right:56px; border-radius:22px; background:rgba(18,23,36,0.94); border:1px solid rgba(255,255,255,0.10); box-shadow:0 0 40px rgba(255,90,31,0.14); overflow:hidden; }
.term .bar { height:58px; display:flex; align-items:center; gap:12px; padding:0 26px; border-bottom:1px solid rgba(255,255,255,0.08); background:rgba(255,255,255,0.03); }
.term .bar .d { width:14px; height:14px; border-radius:50%; background:rgba(255,255,255,0.18); }
.term .bar .d.o { background:#FF5A1F; }
.term .bar .t { margin-left:12px; font-weight:600; font-size:21px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.55); }
.tl { position:relative; white-space:nowrap; clip-path:inset(0 100% 0 0); }
.tl .p { color:#FF5A1F; font-weight:900; margin-right:18px; }
.tl.w .p { color:#FF4438; }
.cursor { display:inline-block; width:18px; height:40px; margin-left:8px; vertical-align:-6px; background:#FF5A1F; }
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


def T(x):  # voice-relative local time -> frame-local time
    return round(x + VOFF, 2)


frames = {}

# ---------------- 01 HOOK (fixed brand layout) ----------------
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:940px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:42% 50%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.30) 0%, rgba(11,14,20,0.0) 38%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:760px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-row { display:flex; gap:14px; align-items:center; margin-bottom:30px; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-prop { padding:11px 18px; border-radius:9px; background:#FF5A1F; font-weight:900; font-size:23px; letter-spacing:0.16em; color:#0B0E14; opacity:0; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:112px; line-height:1.04; letter-spacing:-0.02em; color:#fff; }
.hk-name.o { color:#FF5A1F; font-size:84px; }
.hk-sub { margin-top:24px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:24px; margin-top:40px; }
.hk-tag { font-weight:800; font-size:46px; line-height:1; color:#FF5A1F; opacity:0; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh tư liệu: VnExpress</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-row"><div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress · 19/11/2026</span></div><div class="hk-prop" id="hk-prop">ĐỀ XUẤT</div></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Vượt đèn vàng</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">có thể không bị phạt</div></div>
      <div class="hk-sub" id="hk-sub">Cục CSGT nghiên cứu sửa <b>Nghị định 168</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Lần đầu: chỉ cảnh cáo</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Tái phạm: có thể gấp 3</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-prop',{autoAlpha:0,scale:0.8},{autoAlpha:1,scale:1,duration:0.32,ease:'back.out(2)'},0.55);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.7);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.92);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.4);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.0);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.3);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (ticker: ảnh nền mờ + dải LIVE + feed) ----------------
D2 = DURS[1]
frames['02-what'] = frame('02-what', """
.w-bg { position:absolute; inset:0; overflow:hidden; opacity:0; }
.w-bg img { position:absolute; inset:-40px; width:calc(100% + 80px); height:calc(100% + 80px); object-fit:cover; filter:blur(26px) brightness(0.32) saturate(0.8); }
.w-kick { position:absolute; left:64px; top:250px; opacity:0; }
.w-head { position:absolute; left:64px; right:64px; top:300px; font-weight:800; font-size:62px; line-height:1.14; letter-spacing:-0.01em; }
.w-head .ln { overflow:hidden; } .w-head .ln > span { display:block; }
.w-head b { color:#FF5A1F; font-weight:900; }
.w-card { position:absolute; left:64px; right:64px; top:520px; height:440px; border-radius:22px; overflow:hidden; box-shadow:0 0 40px rgba(255,90,31,0.14); border:1px solid rgba(255,255,255,0.12); opacity:0; }
.w-card img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 45%; }
.w-tape { top:1040px; opacity:0; }
.w-feed { position:absolute; left:64px; right:64px; top:1150px; display:flex; flex-direction:column; gap:0; }
.w-row { display:flex; align-items:baseline; gap:22px; padding:18px 0; border-bottom:1px solid rgba(255,255,255,0.12); opacity:0; }
.w-row .k { flex:none; width:215px; white-space:nowrap; font-weight:800; font-size:25px; letter-spacing:0.08em; text-transform:uppercase; color:#FF5A1F; }
.w-row .v { font-weight:700; font-size:31px; line-height:1.25; color:#fff; }
""", """
    <div class="w-bg" id="w-bg"><img src="assets/img/article-hero.jpg" alt=""></div>
    <div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div>
    <div class="w-head">
      <div class="ln"><span id="w-h1">Cục CSGT tính <b>đổi cách phạt</b></span></div>
      <div class="ln"><span id="w-h2">lỗi đèn tín hiệu</span></div>
    </div>
    <div class="w-card" id="w-card"><img src="assets/img/tuoitre2.jpg" alt=""><div class="credit">Ảnh tư liệu: Tuổi Trẻ</div></div>
    <div class="tape w-tape" id="w-tape"><div class="live"><span class="bl" id="w-bl"></span>LIVE</div>
      <div class="rail"><div class="run" id="w-run">VnExpress<i>/</i>Lần đầu vượt đèn vàng hoặc rẽ phải khi đèn đỏ có thể không bị phạt tiền<i>/</i>Tuổi Trẻ<i>/</i>Tái phạm vượt đèn đỏ có thể bị phạt tiền gấp 3 lần<i>/</i>Dân Trí</div></div></div>
    <div class="w-feed">
      <div class="w-row" id="w-r1"><div class="k num">Chiều 19/11</div><div class="v">Cục CSGT (Bộ Công an) đưa ra định hướng</div></div>
      <div class="w-row" id="w-r2"><div class="k">Mục tiêu</div><div class="v">Nghị định mới thay thế Nghị định 168/2024</div></div>
      <div class="w-row" id="w-r3"><div class="k">Phạm vi</div><div class="v">Xử phạt vi phạm giao thông đường bộ</div></div>
    </div>""", """
    tl.fromTo('#w-bg',{autoAlpha:0},{autoAlpha:1,duration:0.6},0);
    tl.fromTo('#w-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#w-h1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.25);
    tl.fromTo('#w-h2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.42);
    tl.fromTo('#w-card',{autoAlpha:0,scale:0.96},{autoAlpha:1,scale:1,duration:0.6,ease:'power3.out'},0.6);
    tl.fromTo('#w-card img',{scale:1.12},{scale:1.0,duration:%(d)s,ease:'none'},0.6);
    tl.fromTo('#w-tape',{autoAlpha:0,y:30},{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'},0.9);
    tl.fromTo('#w-run',{x:40},{x:-2600,duration:%(d)s,ease:'none'},0.9);
    tl.to('#w-bl',{keyframes:[%(blink)s]},1.0);
    tl.fromTo('#w-r1',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r1)s);
    tl.fromTo('#w-r2',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r2)s);
    tl.fromTo('#w-r3',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r3)s);""" % dict(
    d=D2, r1=T(1.2), r2=T(4.4), r3=T(8.0),
    blink=",".join(["{opacity:0.15,duration:0.45},{opacity:1,duration:0.45}"] * 10)))

# ---------------- 03 KEY FACTS (dòng terminal typewriter) ----------------
D3 = DURS[2]
frames['03-facts'] = frame('03-facts', """
.f-kick { position:absolute; left:64px; top:250px; opacity:0; }
.f-title { position:absolute; left:64px; right:64px; top:300px; font-weight:800; font-size:60px; line-height:1.14; }
.f-title .ln { overflow:hidden; } .f-title .ln > span { display:block; }
.f-title b { color:#FF5A1F; }
.f-term { top:480px; height:970px; opacity:0; }
.f-body { padding:40px 40px; display:flex; flex-direction:column; gap:32px; }
.f-sec { font-weight:900; font-size:46px; line-height:1.2; }
.f-sec .lamp { display:inline-block; width:30px; height:30px; border-radius:50%; margin-right:18px; vertical-align:-2px; }
.f-sec .lamp.y { background:#FF5A1F; box-shadow:0 0 22px rgba(255,90,31,0.7); }
.f-sec .lamp.r { background:#FF4438; box-shadow:0 0 22px rgba(255,68,56,0.7); }
.f-cond { font-weight:600; font-size:35px; line-height:1.3; color:rgba(255,255,255,0.82); white-space:normal; }
.f-res { display:flex; align-items:center; justify-content:space-between; padding:28px 28px; border-radius:14px; background:rgba(255,90,31,0.10); border:2px solid rgba(255,90,31,0.8); opacity:0; }
.f-res.w { background:rgba(255,68,56,0.10); border-color:rgba(255,68,56,0.85); }
.f-res .l { font-weight:700; font-size:28px; letter-spacing:0.08em; text-transform:uppercase; color:rgba(255,255,255,0.7); }
.f-res .r { font-weight:900; font-size:42px; color:#FF5A1F; }
.f-res.w .r { color:#FF4438; }
.f-sep { height:1px; background:rgba(255,255,255,0.12); margin:8px 0; }
""", """
    <div class="kick f-kick" id="f-kick">Đề xuất chia theo mức độ</div>
    <div class="f-title"><div class="ln"><span id="f-t1">Lỗi đèn tín hiệu: <b>không còn</b></span></div><div class="ln"><span id="f-t2">một mức phạt cứng</span></div></div>
    <div class="term f-term" id="f-term">
      <div class="bar"><span class="d o"></span><span class="d"></span><span class="d"></span><span class="t">de-xuat / den-tin-hieu</span></div>
      <div class="f-body">
        <div class="tl f-sec" id="f-l1"><span class="p">&gt;</span><span class="lamp y"></span>Đèn vàng</div>
        <div class="tl f-cond" id="f-l2"><span class="p">+</span>Xe đã đi qua vạch dừng</div>
        <div class="f-res" id="f-r1"><span class="l">Đề xuất</span><span class="r">Không xử phạt</span></div>
        <div class="f-sep"></div>
        <div class="tl f-sec w" id="f-l3"><span class="p">&gt;</span><span class="lamp r"></span>Đèn đỏ</div>
        <div class="tl f-cond" id="f-l4"><span class="p">+</span>Vượt vạch nhưng đứng lại, không cản trở</div>
        <div class="f-res" id="f-r2"><span class="l num">Lần 1</span><span class="r">Cảnh cáo</span></div>
        <div class="f-res w" id="f-r3"><span class="l num">Lần 2</span><span class="r">Phạt tiền + trừ điểm<span class="cursor" id="f-cur"></span></span></div>
      </div>
    </div>""", """
    tl.fromTo('#f-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#f-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.25);
    tl.fromTo('#f-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.42);
    tl.fromTo('#f-term',{autoAlpha:0,y:40},{autoAlpha:1,y:0,duration:0.5,ease:'power3.out'},0.7);
    tl.fromTo('#f-l1',{clipPath:'inset(0 100%% 0 0)'},{clipPath:'inset(0 0%% 0 0)',duration:0.5,ease:'steps(12)'},%(a)s);
    tl.fromTo('#f-l2',{clipPath:'inset(0 100%% 0 0)'},{clipPath:'inset(0 0%% 0 0)',duration:0.8,ease:'steps(24)'},%(b)s);
    tl.fromTo('#f-r1',{autoAlpha:0,x:-24},{autoAlpha:1,x:0,duration:0.4,ease:'back.out(1.6)'},%(c)s);
    tl.fromTo('#f-l3',{clipPath:'inset(0 100%% 0 0)'},{clipPath:'inset(0 0%% 0 0)',duration:0.5,ease:'steps(12)'},%(d)s);
    tl.fromTo('#f-l4',{clipPath:'inset(0 100%% 0 0)'},{clipPath:'inset(0 0%% 0 0)',duration:1.2,ease:'steps(36)'},%(e)s);
    tl.fromTo('#f-r2',{autoAlpha:0,x:-24},{autoAlpha:1,x:0,duration:0.4,ease:'back.out(1.6)'},%(f)s);
    tl.fromTo('#f-r3',{autoAlpha:0,x:-24},{autoAlpha:1,x:0,duration:0.4,ease:'back.out(1.6)'},%(g)s);
    tl.to('#f-cur',{keyframes:[%(blink)s]},%(g)s);""" % dict(
    a=T(2.3), b=T(3.0), c=T(4.4), d=T(5.5), e=T(6.2), f=T(8.6), g=T(9.8),
    blink=",".join(["{opacity:0,duration:0.3},{opacity:1,duration:0.3}"] * 3)))

# ---------------- 04 DATA MOMENT (mã ngắn + số ×3 giữa 2 vạch + thang tái phạm) ----------------
frames['04-data'] = frame('04-data', """
.d-kick { position:absolute; left:64px; top:250px; opacity:0; color:#FF4438; }
.d-title { position:absolute; left:64px; right:64px; top:300px; font-weight:800; font-size:60px; line-height:1.14; }
.d-title .ln { overflow:hidden; } .d-title .ln > span { display:block; }
.d-title b { color:#FF4438; }
.d-zone { position:absolute; left:64px; right:64px; top:490px; height:550px; }
.d-rule { position:absolute; left:0; right:0; height:3px; background:linear-gradient(90deg, transparent, #FF5A1F 20%, #FF4438 80%, transparent); transform-origin:center; }
.d-rule.a { top:0; } .d-rule.b { bottom:0; }
.d-code { position:absolute; left:0; right:0; top:34px; text-align:center; font-weight:900; font-size:30px; letter-spacing:0.5em; color:rgba(255,255,255,0.6); }
.d-num { position:absolute; left:0; right:0; top:70px; text-align:center; font-weight:900; font-size:300px; line-height:1; letter-spacing:-0.03em; color:#FF5A1F; }
#d-n3 { color:#FF4438; }
.d-numwrap { position:absolute; left:0; right:0; top:70px; height:380px; }
.d-num .x { font-size:190px; margin-right:12px; }
.d-cap { position:absolute; left:0; right:0; bottom:28px; text-align:center; font-weight:700; font-size:32px; color:rgba(255,255,255,0.82); opacity:0; }
.d-steps { position:absolute; left:64px; right:64px; top:1080px; display:flex; flex-direction:column; gap:22px; }
.d-st { display:flex; align-items:center; gap:24px; padding:32px 30px; border-radius:14px; background:rgba(18,23,36,0.92); border:1px solid rgba(255,255,255,0.10); border-left:6px solid #FF4438; opacity:0; }
.d-st .k { flex:none; width:150px; font-weight:900; font-size:32px; color:#FF4438; }
.d-st .v { font-weight:700; font-size:36px; color:#fff; }
.d-st .v b { color:#FF5A1F; }
""", """
    <div class="kick d-kick" id="d-kick">Vượt đèn đỏ rồi đi tiếp</div>
    <div class="d-title"><div class="ln"><span id="d-t1">Phạt ngay từ lần đầu,</span></div><div class="ln"><span id="d-t2"><b>tái phạm tính lũy kế</b></span></div></div>
    <div class="d-zone">
      <div class="d-rule a" id="d-ra"></div>
      <div class="d-code" id="d-code">TÁI PHẠM</div>
      <div class="d-numwrap"><div class="d-num num" id="d-n1"><span class="x">×</span>1</div></div>
      <div class="d-numwrap"><div class="d-num num" id="d-n2" style="opacity:0"><span class="x">×</span>2</div></div>
      <div class="d-numwrap"><div class="d-num num" id="d-n3" style="opacity:0"><span class="x">×</span>3</div></div>
      <div class="d-cap" id="d-cap">Mức phạt tiền lũy kế có thể tới</div>
      <div class="d-rule b" id="d-rb"></div>
    </div>
    <div class="d-steps">
      <div class="d-st" id="d-s1"><div class="k num">Lần 1</div><div class="v">Phạt tiền + trừ điểm GPLX</div></div>
      <div class="d-st" id="d-s2"><div class="k num">Lần 2</div><div class="v">Phạt tiền có thể <b>gấp 2</b> + trừ điểm</div></div>
      <div class="d-st" id="d-s3"><div class="k num">Lần 3</div><div class="v">Phạt tiền có thể <b>gấp 3</b> + trừ điểm</div></div>
    </div>""", """
    tl.fromTo('#d-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#d-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.2);
    tl.fromTo('#d-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.38);
    tl.fromTo('#d-ra',{scaleX:0},{scaleX:1,duration:0.6,ease:'power3.out'},0.5);
    tl.fromTo('#d-rb',{scaleX:0},{scaleX:1,duration:0.6,ease:'power3.out'},0.6);
    tl.fromTo('#d-code',{autoAlpha:0,scale:1.3},{autoAlpha:1,scale:1,duration:0.6,ease:'power2.out'},0.7);
    tl.fromTo('#d-n1',{autoAlpha:0,scale:0.6},{autoAlpha:1,scale:1,duration:0.45,ease:'back.out(1.6)'},%(s1)s);
    tl.fromTo('#d-s1',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(s1)s);
    tl.to('#d-n1',{autoAlpha:0,yPercent:-30,duration:0.25,ease:'power2.in'},%(s2)s);
    tl.fromTo('#d-n2',{autoAlpha:0,yPercent:30},{autoAlpha:1,yPercent:0,duration:0.35,ease:'power3.out'},%(s2b)s);
    tl.fromTo('#d-s2',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(s2)s);
    tl.to('#d-n2',{autoAlpha:0,yPercent:-30,duration:0.25,ease:'power2.in'},%(s3)s);
    tl.fromTo('#d-n3',{autoAlpha:0,yPercent:30},{autoAlpha:1,yPercent:0,duration:0.4,ease:'back.out(2)'},%(s3b)s);
    tl.fromTo('#d-s3',{autoAlpha:0,x:-30},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(s3)s);
    tl.fromTo('#d-cap',{autoAlpha:0,y:12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},%(cap)s);""" % dict(
    s1=T(1.6), s2=T(5.3), s2b=T(5.5), s3=T(6.8), s3b=T(7.0), cap=T(7.3)))

# ---------------- 05 CONTEXT (ảnh camera + dòng so sánh có sparkline + smash-cut) ----------------
def spark(seed, n=14):
    # deterministic zig-zag path across 920x70
    pts = []
    s = seed
    for i in range(n):
        s = (s * 1103515245 + 12345) & 0x7fffffff
        pts.append((round(i * 920 / (n - 1)), 12 + (s % 50)))
    return "M" + " L".join(f"{x},{y}" for x, y in pts)

frames['05-context'] = frame('05-context', """
.c-kick { position:absolute; left:64px; top:250px; opacity:0; }
.c-title { position:absolute; left:64px; right:64px; top:300px; font-weight:800; font-size:58px; line-height:1.14; }
.c-title .ln { overflow:hidden; } .c-title .ln > span { display:block; }
.c-title b { color:#FF5A1F; }
.c-card { position:absolute; left:64px; right:64px; top:470px; height:400px; border-radius:22px; overflow:hidden; box-shadow:0 0 40px rgba(255,90,31,0.14); border:1px solid rgba(255,255,255,0.12); opacity:0; }
.c-card img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 55%; }
.c-rows { position:absolute; left:64px; right:64px; top:900px; display:flex; flex-direction:column; }
.c-row { position:relative; padding:22px 0 22px; border-bottom:1px solid rgba(255,255,255,0.12); opacity:0; }
.c-row svg { position:absolute; left:0; top:8px; width:952px; height:80px; overflow:visible; }
.c-row svg path { fill:none; stroke:rgba(255,90,31,0.35); stroke-width:3; }
.c-row .k { position:relative; font-weight:800; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:#FF5A1F; }
.c-row .v { position:relative; margin-top:6px; font-weight:700; font-size:34px; line-height:1.25; color:#fff; }
.c-stamp { position:absolute; left:64px; right:64px; top:1300px; padding:26px 30px; border-radius:16px; border:3px solid #FF4438; background:rgba(255,68,56,0.12); display:flex; align-items:center; gap:24px; opacity:0; }
.c-stamp .tri { flex:none; width:0; height:0; border-left:28px solid transparent; border-right:28px solid transparent; border-bottom:50px solid #FF4438; position:relative; }
.c-stamp .tri::after { content:"!"; position:absolute; left:-10px; top:12px; width:20px; text-align:center; font-weight:900; font-size:28px; color:#0B0E14; }
.c-stamp .t { font-weight:900; font-size:40px; line-height:1.15; color:#fff; }
.c-stamp .t b { color:#FF4438; }
""", """
    <div class="kick c-kick" id="c-kick">Cách theo dõi tái phạm</div>
    <div class="c-title" id="c-content"><div class="ln"><span id="c-t1">Mỗi lần vi phạm đều <b>được ghi lại</b></span></div></div>
    <div class="c-card" id="c-card"><img src="assets/img/dantri.jpg" alt=""><div class="credit">Ảnh tư liệu: Dân Trí</div></div>
    <div class="c-rows">
      <div class="c-row" id="c-r1"><svg viewBox="0 0 952 80"><path id="c-p1" d="%(p1)s"/></svg><div class="k">Lũy kế</div><div class="v">Tính theo thời hiệu, dựa trên dữ liệu camera</div></div>
      <div class="c-row" id="c-r2"><svg viewBox="0 0 952 80"><path id="c-p2" d="%(p2)s"/></svg><div class="k">Cảnh cáo</div><div class="v">Vẫn là một quyết định xử phạt</div></div>
      <div class="c-row" id="c-r3"><svg viewBox="0 0 952 80"><path id="c-p3" d="%(p3)s"/></svg><div class="k">Liên thông dữ liệu</div><div class="v">Định danh điện tử · GPLX · đăng ký xe</div></div>
    </div>
    <div class="c-stamp" id="c-stamp"><div class="tri"></div><div class="t">Mới là <b>đề xuất</b>, chưa có hiệu lực</div></div>
    <div class="cutflash" id="cutflash"></div>""" % dict(p1=spark(7), p2=spark(42), p3=spark(1999)), """
    tl.fromTo('#c-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#c-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.25);
    tl.fromTo('#c-card',{autoAlpha:0,scale:0.96},{autoAlpha:1,scale:1,duration:0.6,ease:'power3.out'},0.4);
    tl.fromTo('#c-card img',{scale:1.1},{scale:1.0,duration:%(d)s,ease:'none'},0.4);
    tl.fromTo('#c-r1',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r1)s);
    tl.fromTo('#c-p1',{strokeDasharray:1400,strokeDashoffset:1400},{strokeDashoffset:0,duration:1.4,ease:'power1.inOut'},%(r1)s);
    tl.fromTo('#c-r2',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r2)s);
    tl.fromTo('#c-p2',{strokeDasharray:1400,strokeDashoffset:1400},{strokeDashoffset:0,duration:1.4,ease:'power1.inOut'},%(r2)s);
    tl.fromTo('#c-r3',{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.4,ease:'power3.out'},%(r3)s);
    tl.fromTo('#c-p3',{strokeDasharray:1400,strokeDashoffset:1400},{strokeDashoffset:0,duration:1.4,ease:'power1.inOut'},%(r3)s);
    tl.fromTo('#cutflash',{opacity:0},{opacity:0.55,duration:0.05,ease:'none'},%(sm)s);
    tl.to('#cutflash',{opacity:0,duration:0.16,ease:'power1.in'},%(sm2)s);
    tl.fromTo('#c-stamp',{autoAlpha:0,scale:1.15},{autoAlpha:1,scale:1,duration:0.35,ease:'back.out(2)'},%(st)s);""" % dict(
    d=DURS[4], r1=T(0.0), r2=T(3.2), r3=T(5.1), sm=SMASH5, sm2=round(SMASH5 + 0.05, 2), st=round(SMASH5 + 0.12, 2)))

# ---------------- 06 IMPACT (dòng feed: nhãn trái + số phải + tam giác) ----------------
frames['06-impact'] = frame('06-impact', """
.i-kick { position:absolute; left:64px; top:250px; opacity:0; }
.i-title { position:absolute; left:64px; right:64px; top:300px; font-weight:800; font-size:60px; line-height:1.14; }
.i-title .ln { overflow:hidden; } .i-title .ln > span { display:block; }
.i-title b { color:#FF5A1F; }
.i-tape { top:540px; opacity:0; }
.i-feed { position:absolute; left:64px; right:64px; top:670px; display:flex; flex-direction:column; }
.i-row { display:flex; align-items:center; justify-content:space-between; gap:20px; min-height:222px; border-bottom:1px solid rgba(255,255,255,0.14); opacity:0; }
.i-row .l .k { font-weight:900; font-size:46px; color:#fff; }
.i-row .l .s { margin-top:6px; font-weight:600; font-size:24px; letter-spacing:0.1em; text-transform:uppercase; color:rgba(255,255,255,0.55); }
.i-row .r { display:flex; align-items:center; gap:22px; }
.i-row .r .v { font-weight:900; font-size:66px; letter-spacing:-0.01em; color:#FF4438; white-space:nowrap; }
.i-row .r .v small { font-size:32px; font-weight:800; margin-left:8px; }
.i-row .tri { width:0; height:0; border-left:18px solid transparent; border-right:18px solid transparent; border-bottom:30px solid #FF4438; }
.i-note { position:absolute; left:64px; right:64px; top:1340px; font-weight:600; font-size:28px; line-height:1.4; color:rgba(255,255,255,0.7); opacity:0; }
.i-note b { color:#FF5A1F; font-weight:800; }
""", """
    <div class="kick i-kick" id="i-kick">Mức phạt đang áp dụng</div>
    <div class="i-title"><div class="ln"><span id="i-t1">Hiện nay theo</span></div><div class="ln"><span id="i-t2"><b>Nghị định 168/2024</b></span></div></div>
    <div class="tape i-tape" id="i-tape"><div class="live">HIỆN HÀNH</div><div class="rail"><div class="run" id="i-run">Vượt đèn đỏ<i>/</i>Vượt đèn vàng khi chưa qua vạch dừng<i>/</i>Không chấp hành hiệu lệnh đèn tín hiệu</div></div></div>
    <div class="i-feed">
      <div class="i-row" id="i-r1"><div class="l"><div class="k">Ô tô</div><div class="s">Phạt tiền</div></div><div class="r"><span class="v num">18–20<small>triệu đồng</small></span><span class="tri"></span></div></div>
      <div class="i-row" id="i-r2"><div class="l"><div class="k">Xe máy</div><div class="s">Phạt tiền</div></div><div class="r"><span class="v num">4–6<small>triệu đồng</small></span><span class="tri"></span></div></div>
      <div class="i-row" id="i-r3"><div class="l"><div class="k">Cả hai</div><div class="s">Giấy phép lái xe</div></div><div class="r"><span class="v num">−4<small>điểm</small></span><span class="tri"></span></div></div>
    </div>
    <div class="i-note" id="i-note">Áp dụng ngay từ lần vi phạm đầu tiên — đề xuất mới muốn <b>phân hóa</b> theo mức độ và số lần.</div>""", """
    tl.fromTo('#i-kick',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'},0.1);
    tl.fromTo('#i-t1',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.2);
    tl.fromTo('#i-t2',{yPercent:115},{yPercent:0,duration:0.55,ease:'power4.out'},0.36);
    tl.fromTo('#i-tape',{autoAlpha:0,y:30},{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'},0.6);
    tl.fromTo('#i-run',{x:20},{x:-1400,duration:%(d)s,ease:'none'},0.6);
    tl.fromTo('#i-r1',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r1)s);
    tl.fromTo('#i-r2',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r2)s);
    tl.fromTo('#i-r3',{autoAlpha:0,x:40},{autoAlpha:1,x:0,duration:0.4,ease:'power3.out'},%(r3)s);
    tl.fromTo('#i-note',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},%(nt)s);""" % dict(
    d=DURS[5], r1=T(1.6), r2=T(4.2), r3=T(5.6), nt=T(6.4)))

# ---------------- 07 CTA (fixed brand layout) ----------------
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:380px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-head { margin-top:30px; font-weight:900; font-size:68px; line-height:1.1; color:#fff; }
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
        <div class="ln"><span id="t-h1">Cảnh cáo lần đầu:</span></div>
        <div class="ln"><span id="t-h2" class="o">nhân văn hay dễ lơ là?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Nhân văn, hợp lý</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Lo nhiều người lơ là</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>""", """
    tl.fromTo('#t-kicker',{autoAlpha:0,y:-12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0);
    tl.fromTo('#t-h1',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.2);
    tl.fromTo('#t-h2',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.36);
    tl.fromTo('#t-o1',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},1.9);
    tl.fromTo('#t-vs',{autoAlpha:0,scale:0.5},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'},3.0);
    tl.fromTo('#t-o2',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},3.2);
    tl.fromTo('#t-cta',{autoAlpha:0,y:22},{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'},4.8);
    tl.to('#t-cta',{keyframes:[{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'},{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'}]},5.4);
    tl.fromTo('#t-sign',{autoAlpha:0},{autoAlpha:1,duration:0.4},5.2);""")

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

rand = mulberry32(20261119)
stars = "".join(f'<circle cx="{int(rand()*1080)}" cy="{int(rand()*1920)}" r="{1.5+rand()*1.5:.1f}" fill="#fff" opacity="{0.15+rand()*0.25:.2f}" />' for _ in range(40))

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
    ("tape", "click-soft", STARTS[1] + 0.9, 0.35, 0.26),
    ("f1", "pop", STARTS[2] + T(4.4), 0.4, 0.26),
    ("f2", "pop", STARTS[2] + T(8.6), 0.4, 0.26),
    ("n3", "impact-bass-1", STARTS[3] + T(7.0), 0.6, 0.3),
    ("cut5", "click-soft", STARTS[4] + SMASH5, 0.35, 0.32),
    ("o1", "pop", STARTS[6] + 1.9, 0.35, 0.3),
    ("o2", "pop", STARTS[6] + 3.2, 0.35, 0.3),
    ("cta", "chime", STARTS[6] + 4.8, 1.2, 0.32),
]
TRK = {a: (31 if a in ("n3", "hook", "cut5") else 30) for a, *_ in SFX}
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
{clips}<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: VnExpress, Tuổi Trẻ, Dân Trí</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
<div id="caps">
{cap_html}</div>
{voices}<audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"{(' ' + bgm_attr) if bgm_attr else ''}></audio>
{sfx}</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.set('#brand-anchor',{{opacity:1}},{STARTS[1]});
tl.to('.blob',{{x:'+=40',y:'-=30',duration:18,ease:'sine.inOut',repeat:3,yoyo:true,stagger:3}},0);
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:16,yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{cap_js}window.__timelines['main'] = tl;
</script>
</body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(index)
print('starts', STARTS, 'durs', DURS, 'total', TOTAL, 'caps', len(caps))
