#!/usr/bin/env python3
"""Generate compositions + index.html for the-cong-viettel-bi-loai-acl-two-hoa-melbourne (style 9-editorial-clipping).

Timing is derived from real voice durations (ffprobe) + ElevenLabs STT word timestamps (karaoke captions).
"""
import json, os, re, difflib, sys, subprocess

P = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.chdir(P)

VOFF = 0.10
VDUR = [float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                        f'assets/voice/line{i+1}.mp3']).decode().strip()) for i in range(7)]
PAD = [0.45, 0.4, 0.4, 0.45, 0.45, 0.45, 1.7]
DURS = [round(v + VOFF + p, 2) for v, p in zip(VDUR, PAD)]
STARTS = [0.0]
for d in DURS[:-1]:
    STARTS.append(round(STARTS[-1] + d, 2))
TOTAL = round(STARTS[-1] + DURS[-1], 2)


def T(x):  # voice-relative -> frame-local
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
.credit { position:absolute; right:14px; bottom:12px; padding:5px 10px; border-radius:6px; background:rgba(11,14,20,0.78); font-weight:500; font-size:18px; color:rgba(255,255,255,0.9); }
.ttl { position:absolute; left:64px; right:64px; font-weight:800; font-size:60px; line-height:1.14; letter-spacing:-0.01em; }
.ttl .ln { overflow:hidden; padding-bottom:4px; } .ttl .ln > span { display:block; }
.ttl b { color:#FF5A1F; font-weight:900; } .ttl b.r { color:#FF4438; }
/* editorial clipping: paper scraps (white paper / dark card), torn bottom edge, soft shadow */
.clip-p { position:absolute; opacity:0; box-shadow:0 24px 50px rgba(0,0,0,0.55), 0 0 40px rgba(255,90,31,0.14); }
.paper { background:#FFFFFF; color:#0B0E14; }
.dark { background:#121724; border:1.5px solid rgba(255,255,255,0.14); color:#fff; }
.dark.hot { border-color:rgba(255,90,31,0.8); } .dark.warn { border-color:rgba(255,68,56,0.8); }
.torn { clip-path:polygon(0 0,100% 0,100% 92%,96% 97%,91% 93%,86% 99%,80% 94%,74% 98%,68% 93%,62% 99%,56% 94%,50% 98%,44% 93%,38% 99%,32% 94%,26% 98%,20% 93%,14% 99%,8% 94%,3% 98%,0 94%); }
.tape { position:absolute; top:-18px; left:50%; width:150px; height:38px; margin-left:-75px; background:rgba(255,90,31,0.55); transform:rotate(-3deg); }
.src { font-weight:600; font-size:20px; letter-spacing:0.12em; text-transform:uppercase; }
.paper .src { color:rgba(11,14,20,0.66); } .dark .src { color:rgba(255,255,255,0.68); }
.qmark { position:absolute; color:rgba(255,90,31,0.18); font-family:Georgia, "Times New Roman", serif; font-weight:900; line-height:1; opacity:0; }
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


def drop(sel, t, rot, dur=0.55):
    """Clipping 'dropped' onto desk: hidden -> visible with final rotation (GSAP owns the whole transform)."""
    return (f"    tl.fromTo('{sel}',{{autoAlpha:0,y:60,rotation:{round(rot * 2.5, 2)},scale:0.9}},"
            f"{{autoAlpha:1,y:0,rotation:{rot},scale:1,duration:{dur},ease:'power3.out'}},{t});\n")


def head_js(prefix, t0=0.05):
    return (f"    tl.fromTo('#{prefix}-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},{t0});\n"
            f"    tl.fromTo('#{prefix}-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{round(t0 + 0.07, 2)});\n"
            f"    tl.fromTo('#{prefix}-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{round(t0 + 0.21, 2)});\n")


def smash(prefix, cut):
    return (f"    tl.fromTo('#{prefix}-flash',{{opacity:0}},{{opacity:0.55,duration:0.05,ease:'none'}},{cut});\n"
            f"    tl.to('#{prefix}-flash',{{opacity:0,duration:0.16,ease:'power1.in'}},{round(cut + 0.05, 2)});\n"
            f"    tl.fromTo('#{prefix}-content',{{scale:1}},{{scale:0.986,duration:0.06,ease:'power1.out'}},{cut});\n"
            f"    tl.to('#{prefix}-content',{{scale:1,duration:0.14,ease:'power2.out'}},{round(cut + 0.061, 3)});\n")


frames = {}

# ---------------- 01 HOOK (fixed brand layout) ----------------
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:880px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:42% 40%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0.0) 40%, rgba(11,14,20,0.99) 100%); }
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
    <div class="hk-photo"><img src="assets/img/vne.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: VnExpress</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: VnExpress, Tuổi Trẻ · 25/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Thể Công</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">dừng bước</div></div>
      <div class="hk-sub" id="hk-sub">Hòa Melbourne Victory 0-0 · <b>Cúp C2 châu Á</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>2 điểm sau 5 lượt</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>12 trận không thắng</div>
      </div>
    </div>""", """
    tl.fromTo('.hk-photo',{autoAlpha:0,scale:1.1},{autoAlpha:1,scale:1,duration:0.9,ease:'power2.out'},0);
    tl.fromTo('.hk-panel',{autoAlpha:0,y:48},{autoAlpha:1,y:0,duration:0.55,ease:'power3.out'},0.05);
    tl.fromTo('.hk-masthead',{autoAlpha:0,y:14},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.22);
    tl.fromTo('.hk-badge',{autoAlpha:0,scale:0.9},{autoAlpha:1,scale:1,duration:0.36,ease:'back.out(1.7)'},0.42);
    tl.fromTo('#hk-n1',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.6);
    tl.fromTo('#hk-n2',{yPercent:118},{yPercent:0,duration:0.6,ease:'power4.out'},0.85);
    tl.fromTo('#hk-sub',{autoAlpha:0,y:16},{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'},1.4);
    tl.fromTo('#hk-t1',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.0);
    tl.fromTo('#hk-t2',{autoAlpha:0,x:-18},{autoAlpha:1,x:0,duration:0.36,ease:'power2.out'},2.3);
    tl.to('.hk-photo img',{scale:1.06,duration:%s,ease:'none'},0);""" % DURS[0])

# ---------------- 02 WHAT HAPPENED (ảnh như mẩu báo cắt dán + panel có ngoặc kép lớn) ----------------
D2 = DURS[1]
frames['02-what'] = frame('02-what', """
.w-head { position:absolute; left:64px; top:190px; display:flex; align-items:center; gap:18px; }
.w-kick { opacity:0; }
.w-badge { padding:7px 16px; border-radius:30px; border:2px solid #FF5A1F; font-weight:800; font-size:24px; color:#fff; background:rgba(255,90,31,0.15); opacity:0; }
.w-photo { left:70px; width:940px; top:280px; padding:16px 16px 60px; background:#FFFFFF; }
.w-photo .im { position:relative; width:100%; height:600px; overflow:hidden; }
.w-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 30%; }
.w-photo .cap2 { position:absolute; left:20px; bottom:16px; font-weight:600; font-size:22px; color:rgba(11,14,20,0.7); }
.w-panel { position:absolute; left:64px; right:64px; top:1040px; }
.w-q { left:-20px; top:-70px; font-size:420px; }
.w-ttl { position:relative; font-weight:800; font-size:58px; line-height:1.16; letter-spacing:-0.01em; }
.w-ttl .ln { overflow:hidden; padding-bottom:4px; } .w-ttl .ln > span { display:block; }
.w-ttl b { color:#FF5A1F; font-weight:900; }
.w-strip { position:relative; display:flex; gap:16px; margin-top:56px; }
.w-chip { padding:20px 24px; border-radius:6px; background:#121724; border:1.5px solid rgba(255,90,31,0.7); font-weight:700; font-size:28px; line-height:1.25; color:#fff; opacity:0; }
.w-chip.r { border-color:rgba(255,68,56,0.8); }
.w-chip i { display:block; font-style:normal; font-weight:600; font-size:20px; letter-spacing:0.12em; text-transform:uppercase; color:rgba(255,255,255,0.55); margin-bottom:6px; }
""", """
    <div class="w-head"><div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div><div class="w-badge" id="w-badge">Chiều 25/11</div></div>
    <div data-layout-allow-overlap class="clip-p w-photo" id="w-photo"><div class="im"><img src="assets/img/tt.jpg" alt=""></div><div class="cap2">Thể Công Viettel làm khách tại Australia · Ảnh: Tuổi Trẻ</div><div class="tape"></div></div>
    <div class="w-panel">
      <div class="qmark w-q" id="w-q">&ldquo;</div>
      <div class="w-ttl"><div class="ln"><span id="w-h1">Hòa Melbourne Victory <b>0-0</b>,</span></div><div class="ln"><span id="w-h2">dù cần <b>thắng</b> để còn hy vọng</span></div></div>
      <div class="w-strip">
        <div class="w-chip" id="w-c1"><i>Lượt 5 · Bảng E</i>AFC Champions League Two</div>
        <div class="w-chip r" id="w-c2"><i>Sân khách</i>Kardinia Park, Australia</div>
      </div>
    </div>""", f"""
    tl.fromTo('#w-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#w-badge',{{autoAlpha:0,scale:0.7}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(2)'}},0.3);
{drop('#w-photo', 0.2, -1.5, 0.65)}    tl.fromTo('#w-photo img',{{scale:1.12}},{{scale:1.0,duration:{D2},ease:'none'}},0.2);
    tl.fromTo('#w-q',{{autoAlpha:0,scale:0.8}},{{autoAlpha:1,scale:1,duration:0.5,ease:'power2.out'}},{T(1.2)});
    tl.fromTo('#w-h1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{T(3.0)});
    tl.fromTo('#w-h2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{T(5.4)});
    tl.fromTo('#w-c1',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(1.3)});
    tl.fromTo('#w-c2',{{autoAlpha:0,y:24}},{{autoAlpha:1,y:0,duration:0.45,ease:'power3.out'}},{T(1.8)});""")

# ---------------- 03 KEY FACTS (3 mẩu giấy xếp chồng lệch) ----------------
frames['03-facts'] = frame('03-facts', """
.f-kick { position:absolute; left:64px; top:190px; opacity:0; }
.f-ttl { top:240px; }
.f-card { width:860px; padding:40px 48px 54px; }
.f-card .v { font-weight:900; font-size:96px; line-height:1; letter-spacing:-0.02em; }
.f-card .l { margin-top:16px; font-weight:700; font-size:36px; line-height:1.25; }
.paper .v { color:#FF5A1F; } .paper .v.r { color:#FF4438; }
.dark .v { color:#FF4438; }
.paper .l { color:#0B0E14; } .dark .l { color:#fff; }
.f-card .src { margin-top:18px; }
""", """
    <div class="kick f-kick" id="f-kick">Những con số chính</div>
    <div class="ttl f-ttl"><div class="ln"><span id="f-t1">Cuối bảng E,</span></div><div class="ln"><span id="f-t2"><b class="r">hết cửa đi tiếp</b></span></div></div>
    <div data-layout-allow-overlap class="clip-p paper torn f-card" id="f-c1" style="left:70px; top:430px;"><div class="v">2 điểm</div><div class="l">sau 5 lượt trận — xếp cuối bảng E</div><div class="src">Tuổi Trẻ · 25/11</div></div>
    <div data-layout-allow-overlap class="clip-p dark warn f-card" id="f-c2" style="left:150px; top:790px;"><div class="v" style="font-size:80px">Loại sớm 1 vòng</div><div class="l">Còn 1 lượt, đã hết cơ hội đi tiếp</div><div class="src">VnExpress · 25/11</div></div>
    <div data-layout-allow-overlap class="clip-p paper torn f-card" id="f-c3" style="left:90px; top:1150px;"><div class="v r">12 trận</div><div class="l">không thắng liên tiếp trên mọi đấu trường</div><div class="src">VnExpress, Tuổi Trẻ</div></div>""",
    head_js('f') + drop('#f-c1', T(1.5), -1.8) + drop('#f-c2', T(3.1), 1.2) + drop('#f-c3', T(5.1), -0.9))

# ---------------- 04 DATA MOMENT (số khổng lồ + ngoặc kép mờ + gạch chân tay vẽ) ----------------
tally = "".join(f'<div class="d-m" id="d-m{i}"><i><span></span></i></div>' for i in range(12))
tally_js = "".join(f"    tl.fromTo('#d-m{i} span',{{scaleX:0}},{{scaleX:1,duration:0.14,ease:'power2.out'}},{round(T(0.2) + 0.08 * i, 2)});\n"
                   f"    tl.fromTo('#d-m{i}',{{autoAlpha:0}},{{autoAlpha:1,duration:0.1}},{round(T(0.15) + 0.08 * i, 2)});\n" for i in range(12))
frames['04-data'] = frame('04-data', """
.d-kick { position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }
.d-q { left:50%; top:250px; margin-left:-230px; font-size:640px; }
.d-num { position:absolute; left:0; right:0; top:360px; text-align:center; font-weight:900; font-size:420px; line-height:1; letter-spacing:-0.04em; color:#FF4438; }
.d-ul { position:absolute; left:50%; top:800px; width:520px; height:60px; margin-left:-260px; }
.d-ul path { fill:none; stroke:#FF5A1F; stroke-width:12; stroke-linecap:round; }
.d-lab { position:absolute; left:64px; right:64px; top:900px; text-align:center; font-weight:800; font-size:54px; line-height:1.2; opacity:0; }
.d-tally { position:absolute; left:110px; right:110px; top:1070px; display:grid; grid-template-columns:repeat(12, 1fr); gap:12px; }
.d-m { height:80px; border-radius:6px; background:#121724; border:1.5px solid rgba(255,255,255,0.16); position:relative; opacity:0; }
.d-m i { position:absolute; inset:0; display:block; transform:rotate(-55deg); }
.d-m span { position:absolute; left:8%; right:8%; top:50%; height:6px; margin-top:-3px; background:#FF4438; border-radius:3px; transform:scaleX(0); transform-origin:center; }
.d-last { left:110px; width:860px; top:1240px; padding:34px 44px 50px; }
.d-last .k { font-weight:700; font-size:22px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(11,14,20,0.6); }
.d-last .v { margin-top:10px; font-weight:900; font-size:54px; line-height:1.1; color:#0B0E14; }
.d-last .v b { color:#FF5A1F; }
.d-last .s { margin-top:10px; font-weight:600; font-size:28px; color:rgba(11,14,20,0.75); }
""", f"""
    <div class="kick d-kick" id="d-kick">Chuỗi không thắng</div>
    <div class="qmark d-q" id="d-q">&ldquo;</div>
    <div class="d-num" id="d-num">0</div>
    <svg class="d-ul" viewBox="0 0 520 60"><path id="d-ulp" d="M8 38 C 90 18, 160 52, 250 32 S 420 14, 512 30" stroke-dasharray="560" stroke-dashoffset="560"/></svg>
    <div class="d-lab" id="d-lab">trận liên tiếp không thắng</div>
    <div class="d-tally">{tally}</div>
    <div data-layout-allow-overlap class="clip-p paper torn d-last" id="d-last"><div class="k">Lần thắng gần nhất · 4/9</div><div class="v">Thể Công <b>2-0</b> Đồng Nai</div><div class="s">Vòng 1 giải vô địch quốc gia (V-League)</div></div>""", f"""
    tl.fromTo('#d-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#d-q',{{autoAlpha:0,scale:0.8}},{{autoAlpha:1,scale:1,duration:0.5,ease:'power2.out'}},0.05);
    const c = {{ v: 0 }};
    const numEl = document.querySelector('#d-num');
    tl.fromTo(c,{{v:0}},{{v:12,duration:1.0,ease:'power1.out',onUpdate(){{ numEl.textContent = Math.round(c.v); }}}},{T(0.05)});
{tally_js}    tl.fromTo('#d-ulp',{{strokeDashoffset:560}},{{strokeDashoffset:0,duration:0.5,ease:'power2.out'}},{T(1.15)});
    tl.fromTo('#d-lab',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},{T(0.9)});
{drop('#d-last', T(1.8), -1.2)}""")

# ---------------- 05 CONTEXT (pull-quote blocks kiểu clipping + biểu đồ tỉ lệ) ----------------
shots = "".join(f'<span class="x-dot{" on" if i < 3 else ""}" id="x-s{i}"></span>' for i in range(14))
shots_js = "".join(f"    tl.fromTo('#x-s{i}',{{autoAlpha:0,scale:0}},{{autoAlpha:1,scale:1,duration:0.2,ease:'back.out(2)'}},{round(T(1.6) + 0.05 * i, 2)});\n" for i in range(14))
frames['05-context'] = frame('05-context', """
.x-kick { position:absolute; left:64px; top:190px; opacity:0; }
.x-ttl { top:240px; }
.x-blk { left:64px; width:952px; padding:34px 44px 44px; }
.x-blk .k { font-weight:700; font-size:22px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.x-blk .big { margin-top:10px; font-weight:900; font-size:52px; line-height:1.1; }
.x-blk .big b { color:#FF5A1F; } .x-blk .big b.r { color:#FF4438; }
.x-shots { display:flex; gap:14px; margin-top:24px; }
.x-dot { width:46px; height:46px; border-radius:50%; border:3px solid rgba(255,255,255,0.35); opacity:0; }
.x-dot.on { background:#FF5A1F; border-color:#FF5A1F; }
.x-bars { margin-top:22px; display:flex; flex-direction:column; gap:18px; }
.x-row { display:flex; align-items:center; gap:20px; }
.x-row .n { width:230px; flex:none; font-weight:700; font-size:28px; color:#fff; }
.x-row .bar { height:44px; border-radius:6px; transform-origin:left center; transform:scaleX(0); }
.x-row .val { font-weight:900; font-size:44px; }
.x-note { margin-top:20px; font-weight:600; font-size:26px; color:rgba(255,255,255,0.75); }
.x-leg { left:120px; width:840px; top:1220px; padding:30px 44px 46px; }
.x-leg .k { font-weight:700; font-size:22px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(11,14,20,0.6); }
.x-leg .v { margin-top:8px; font-weight:900; font-size:56px; line-height:1.1; color:#0B0E14; }
.x-leg .v b { color:#FF5A1F; }
#x-content { position:absolute; inset:0; }
""", f"""
    <div id="x-content">
    <div class="kick x-kick" id="x-kick">Thế trận</div>
    <div class="ttl x-ttl"><div class="ln"><span id="x-t1">Sút nhiều,</span></div><div class="ln"><span id="x-t2"><b>trúng đích ít</b></span></div></div>
    <div data-layout-allow-overlap class="clip-p dark hot x-blk" id="x-b1" style="top:430px;"><div class="k">Thể Công Viettel</div><div class="big"><b>14</b> cú sút · chỉ <b>3</b> trúng đích</div><div class="x-shots">{shots}</div></div>
    <div data-layout-allow-overlap class="clip-p dark warn x-blk" id="x-b2" style="top:770px;"><div class="k">Sút trúng khung thành</div>
      <div class="x-bars">
        <div class="x-row"><div class="n">Thể Công</div><div class="bar" id="x-bar1" style="width:300px; background:#FF5A1F;"></div><div class="val" id="x-v1" style="color:#FF5A1F;">3</div></div>
        <div class="x-row"><div class="n">Melbourne</div><div class="bar" id="x-bar2" style="width:500px; background:#FF4438;"></div><div class="val" id="x-v2" style="color:#FF4438;">5</div></div>
      </div>
      <div class="x-note">Thủ môn Caruso Minh Khang nhiều lần cứu thua</div></div>
    <div data-layout-allow-overlap class="clip-p paper torn x-leg" id="x-leg"><div class="k">Lượt đi · sân Hàng Đẫy</div><div class="v">Hai đội hòa <b>1-1</b></div><div class="tape"></div></div>
    </div>
    <div class="cutflash" id="x-flash"></div>""", head_js('x') + drop('#x-b1', T(0.7), -0.8) + shots_js + drop('#x-b2', T(3.3), 0.9) + f"""
    tl.fromTo('#x-bar1',{{scaleX:0}},{{scaleX:1,duration:0.5,ease:'power2.out'}},{T(3.6)});
    tl.fromTo('#x-v1',{{autoAlpha:0}},{{autoAlpha:1,duration:0.25}},{T(3.9)});
    tl.fromTo('#x-bar2',{{scaleX:0}},{{scaleX:1,duration:0.6,ease:'power2.out'}},{T(3.9)});
    tl.fromTo('#x-v2',{{autoAlpha:0}},{{autoAlpha:1,duration:0.25}},{T(4.3)});
""" + drop('#x-leg', T(5.4), -1.4))

# ---------------- 06 IMPACT (2 mẩu báo chồng lên nhau + smash-cut tại "Trong khi đó") ----------------
CUT = T(3.6)
frames['06-impact'] = frame('06-impact', """
.i-kick { position:absolute; left:64px; top:190px; opacity:0; }
.i-ttl { top:240px; }
.i-a { left:64px; width:900px; top:420px; padding:40px 48px 64px; }
.i-b { left:116px; width:900px; top:830px; padding:40px 48px 50px; }
.i-a .k, .i-b .k { display:block; margin-bottom:6px; font-weight:700; font-size:22px; letter-spacing:0.16em; text-transform:uppercase; }
.i-a .k { color:rgba(255,255,255,0.6); } .i-b .k { color:rgba(11,14,20,0.6); }
.i-a .v { margin-top:20px; font-weight:900; font-size:70px; line-height:1.18; color:#FF4438; }
.i-a .l { margin-top:14px; font-weight:700; font-size:36px; line-height:1.25; color:#fff; }
.i-a .s { margin-top:14px; font-weight:600; font-size:26px; color:rgba(255,255,255,0.7); }
.i-b .v { margin-top:20px; font-weight:900; font-size:64px; line-height:1.18; color:#0B0E14; }
.i-b .v b { color:#FF5A1F; }
.i-b .l { margin-top:14px; font-weight:700; font-size:34px; line-height:1.25; color:#0B0E14; }
.i-b .src { margin-top:16px; }
.i-next { position:absolute; left:64px; right:64px; top:1350px; display:flex; align-items:center; gap:16px; padding:18px 24px; border-radius:8px; border:1.5px dashed rgba(255,255,255,0.3); font-weight:700; font-size:28px; color:rgba(255,255,255,0.85); opacity:0; }
.i-next .d { width:12px; height:12px; border-radius:50%; background:#FF5A1F; flex:none; }
#i-content { position:absolute; inset:0; }
""", """
    <div id="i-content">
    <div class="kick i-kick" id="i-kick">Tác động</div>
    <div class="ttl i-ttl"><div class="ln"><span id="i-t1">Hai đại diện,</span></div><div class="ln"><span id="i-t2"><b>hai ngả đường</b></span></div></div>
    <div data-layout-allow-overlap class="clip-p dark warn i-a" id="i-a"><div class="k">Thể Công Viettel · Cúp C2</div><div class="v">Lần thứ 2 liên tiếp</div><div class="l">không vượt qua vòng bảng Cup châu Á</div><div class="s">Lần trước: AFC Champions League 2021</div></div>
    <div data-layout-allow-overlap class="clip-p paper torn i-b" id="i-b"><div class="k">Công an Hà Nội · Cúp C1 · 24/11</div><div class="v">Thắng Vissel Kobe <b>3-1</b></div><div class="l"><b style="color:#FF5A1F">7 điểm</b>, vẫn cạnh tranh suất đi tiếp</div><div class="src">VnExpress · AFC Champions League Elite</div><div class="tape"></div></div>
    <div class="i-next" id="i-next"><span class="d"></span>Trận cuối của Thể Công ở giải: tiếp Persib Bandung ngày 2/12</div>
    </div>
    <div class="cutflash" id="i-flash"></div>""", head_js('i') + drop('#i-a', T(0.3), -1.6) + drop('#i-b', round(CUT + 0.25, 2), 1.3) + f"""
    tl.fromTo('#i-next',{{autoAlpha:0,y:20}},{{autoAlpha:1,y:0,duration:0.45,ease:'power2.out'}},{T(7.0)});
""" + smash('i', CUT))

# ---------------- 07 CTA (fixed brand layout) ----------------
frames['07-cta'] = frame('07-cta', """
.t-wrap { position:absolute; left:64px; right:64px; top:300px; text-align:center; }
.t-kicker { font-weight:700; font-size:26px; letter-spacing:0.26em; text-transform:uppercase; color:#FF5A1F; opacity:0; }
.t-ctx { display:inline-flex; align-items:center; gap:12px; margin-top:26px; padding:10px 20px; border-radius:10px; border:1.5px solid rgba(255,255,255,0.18); font-weight:600; font-size:24px; color:rgba(255,255,255,0.8); opacity:0; }
.t-ctx .rc { width:20px; height:20px; border-radius:50%; border:3px solid #FF5A1F; }
.t-head { margin-top:34px; font-weight:900; font-size:66px; line-height:1.14; color:#fff; }
.t-head .ln { overflow:hidden; } .t-head .ln > span { display:block; }
.t-head .o { color:#FF5A1F; } .t-head .r { color:#FF4438; }
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
.t-sign { position:absolute; left:0; right:0; top:1440px; display:flex; align-items:center; justify-content:center; gap:14px; opacity:0; }
.t-sign .m { width:48px; height:48px; }
.t-sign .w { font-weight:800; font-size:32px; color:rgba(255,255,255,0.9); }
""", """
    <div class="t-wrap">
      <div class="t-kicker" id="t-kicker">Góc nhìn của bạn</div>
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Thể Công Viettel · 12 trận không thắng</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">12 trận không thắng:</span></div>
        <div class="ln"><span id="t-h2" class="o">chỉ là chững lại</span></div>
        <div class="ln"><span id="t-h3">hay <span class="r">báo động thật sự</span>?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Chỉ là giai đoạn chững lại</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Hồi chuông báo động thật sự</div></div>
      </div>
      <div class="t-cta" id="t-cta"><span class="ico"></span><span>Bình luận quan điểm của bạn</span></div>
    </div>
    <div class="t-sign" id="t-sign"><img class="m" src="public/logo.png" alt=""><span class="w">Tin Tức Số</span></div>""", """
    tl.fromTo('#t-kicker',{autoAlpha:0,y:-12},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0);
    tl.fromTo('#t-ctx',{autoAlpha:0,y:-10},{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'},0.15);
    tl.fromTo('#t-h1',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},0.3);
    tl.fromTo('#t-h2',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},%(h2)s);
    tl.fromTo('#t-h3',{yPercent:118},{yPercent:0,duration:0.55,ease:'power4.out'},%(h3)s);
    tl.fromTo('#t-o1',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},%(o1)s);
    tl.fromTo('#t-vs',{autoAlpha:0,scale:0.5},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2)'},%(vs)s);
    tl.fromTo('#t-o2',{autoAlpha:0,y:28,scale:0.92},{autoAlpha:1,y:0,scale:1,duration:0.42,ease:'back.out(1.5)'},%(o2)s);
    tl.fromTo('#t-cta',{autoAlpha:0,y:22},{autoAlpha:1,y:0,duration:0.44,ease:'power3.out'},%(cta)s);
    tl.to('#t-cta',{keyframes:[{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'},{scale:1.04,duration:0.5,ease:'sine.inOut'},{scale:1,duration:0.5,ease:'sine.inOut'}]},%(pulse)s);
    tl.fromTo('#t-sign',{autoAlpha:0},{autoAlpha:1,duration:0.4},%(sign)s);""" % dict(
    h2=T(1.1), h3=T(2.3), o1=T(1.5), vs=T(2.4), o2=T(2.7), cta=T(4.8), pulse=round(T(4.8) + 0.5, 2), sign=T(5.2)))

SFX = [
    ("hook", "impact-bass-1", 0.6, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("f2", "click-soft", STARTS[2] + T(3.1), 0.35, 0.3),
    ("f3", "click-soft", STARTS[2] + T(5.1), 0.35, 0.3),
    ("big", "impact-bass-1", STARTS[3] + T(0.9), 0.6, 0.3),
    ("dl", "pop", STARTS[3] + T(1.8), 0.4, 0.24),
    ("xb2", "click-soft", STARTS[4] + T(3.3), 0.35, 0.3),
    ("xleg", "pop", STARTS[4] + T(5.4), 0.4, 0.22),
    ("icut", "click-soft", STARTS[5] + CUT, 0.35, 0.32),
    ("o1", "pop", STARTS[6] + T(1.5), 0.35, 0.3),
    ("o2", "pop", STARTS[6] + T(2.7), 0.35, 0.3),
    ("cta", "chime", STARTS[6] + T(4.8), 1.2, 0.32),
]
TRK = {a: (31 if a in ("big", "hook", "f3", "icut", "o2", "xleg") else 30) for a, *_ in SFX}
SOURCE_TEXT = "Nguồn: VnExpress, Tuổi Trẻ"
SEED = 20261125
# caption display text (numerals as they appear on screen); timing aligned to STT words
CAP_LINES = [
    "Hòa không bàn thắng trên đất Úc, Thể Công Viettel chính thức dừng bước ngay từ vòng bảng Cúp C2 châu Á.",
    "Chiều 25 tháng 11, ở lượt trận thứ năm bảng E, đội bóng áo lính hòa Melbourne Victory với tỷ số 0-0, dù cần một chiến thắng để nuôi hy vọng đi tiếp.",
    "Sau năm lượt trận, Thể Công Viettel chỉ có hai điểm, đứng cuối bảng E và bị loại sớm một vòng. Trận hòa cũng nâng chuỗi không thắng trên mọi đấu trường lên 12 trận.",
    "12 trận liên tiếp không biết thắng. Lần gần nhất đội bóng áo lính giành ba điểm là ngày 4 tháng 9, khi thắng Đồng Nai 2-0 ngay vòng đấu mở màn giải vô địch quốc gia.",
    "Trong trận này, Thể Công Viettel tung ra 14 cú sút nhưng chỉ ba lần trúng đích, còn Melbourne có năm cú sút trúng khung thành. Ở lượt đi trên sân Hàng Đẫy, hai đội hòa 1-1.",
    "Đây là lần thứ hai liên tiếp Thể Công Viettel không vượt qua vòng bảng một giải cúp châu Á. Trong khi đó, Công an Hà Nội vừa thắng Vissel Kobe 3-1, có bảy điểm và vẫn cạnh tranh suất đi tiếp ở Cúp C1.",
    "12 trận không thắng: chỉ là giai đoạn chững lại, hay hồi chuông báo động thật sự cho đội bóng áo lính? Hãy để lại bình luận quan điểm của bạn.",
]

os.makedirs('compositions/frames', exist_ok=True)
for k, v in frames.items():
    open(f'compositions/frames/{k}.html', 'w', encoding='utf-8').write(v)


# ---------------- captions (karaoke) ----------------
def norm(t):
    return re.sub(r'[^\w]', '', t.lower())


caps = []
for i, line in enumerate(CAP_LINES):
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


rand = mulberry32(SEED)
stars = "".join(f'<circle cx="{int(rand()*1080)}" cy="{int(rand()*1920)}" r="{1.5+rand()*1.5:.1f}" fill="#fff" opacity="{0.15+rand()*0.25:.2f}" />' for _ in range(40))

clips = ""
names = ['01-hook', '02-what', '03-facts', '04-data', '05-context', '06-impact', '07-cta']
for n, s, d in zip(names, STARTS, DURS):
    clips += f'<div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{s}" data-duration="{d}" data-track-index="1"></div>\n'

voices = ""
for i in range(7):
    voices += f'<audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{STARTS[i]+VOFF:.2f}" data-duration="{VDUR[i]:.3f}" data-track-index="10" data-audio-group="voiceover"></audio>\n'

sfx = "".join(f'<audio id="el-sfx-{a}" src="assets/sfx/{f}.mp3" data-start="{s:.2f}" data-duration="{d}" data-track-index="{TRK[a]}" data-volume="{v}"></audio>\n' for a, f, s, d, v in SFX)

# carve output (fx attrs) is preserved across regenerations via .bgm_attrs
bgm_attr = open('.bgm_attrs').read().strip() if os.path.exists('.bgm_attrs') else ""
blob_rep = max(1, int(TOTAL // 18))
star_rep = max(1, int(TOTAL // 4))

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
{clips}<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>{SOURCE_TEXT}</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
<div id="caps">
{cap_html}</div>
{voices}<audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.30"{(' ' + bgm_attr) if bgm_attr else ''}></audio>
{sfx}</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.set('#brand-anchor',{{opacity:1}},{STARTS[1]});
tl.to('.blob',{{x:'+=40',y:'-=30',duration:18,ease:'sine.inOut',repeat:{blob_rep},yoyo:true,stagger:3}},0);
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:{star_rep},yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{cap_js}window.__timelines['main'] = tl;
</script>
</body>
</html>
"""
open('index.html', 'w', encoding='utf-8').write(index)
print('starts', STARTS, 'durs', DURS, 'total', TOTAL, 'caps', len(caps))
