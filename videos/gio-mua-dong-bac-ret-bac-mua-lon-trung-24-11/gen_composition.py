#!/usr/bin/env python3
"""Generate compositions + index.html for gio-mua-dong-bac-ret-bac-mua-lon-trung-24-11 (style 8-icon-grid)."""
import json, os, re, difflib, sys, subprocess

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


def T(x):  # voice-relative -> frame-local
    return round(x + VOFF, 2)


FONTS = ""
for w in (400, 500, 600, 700, 800, 900):
    FONTS += ("@font-face{font-family:'Montserrat';font-weight:%d;src:url('assets/fonts/Montserrat-%d-latin.woff2') format('woff2');"
              "unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}\n" % (w, w))
    FONTS += ("@font-face{font-family:'Montserrat';font-weight:%d;src:url('assets/fonts/Montserrat-%d-vietnamese.woff2') format('woff2');"
              "unicode-range:U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB;}\n" % (w, w))

# Icon set: pure CSS shapes (no emoji). Each icon is a 1x box scaled via --s (px).
BASE_CSS = """
#root { position:absolute; inset:0; width:100%; height:100%; overflow:hidden; font-family:"Montserrat",sans-serif; color:#fff; background:transparent; }
.kick { font-weight:700; font-size:26px; letter-spacing:0.22em; text-transform:uppercase; color:#FF5A1F; }
.num { font-variant-numeric: tabular-nums; }
.credit { position:absolute; right:14px; bottom:12px; padding:5px 10px; border-radius:6px; background:rgba(11,14,20,0.78); font-weight:500; font-size:18px; color:rgba(255,255,255,0.9); }
.ttl { position:absolute; left:64px; right:64px; font-weight:800; font-size:60px; line-height:1.14; letter-spacing:-0.01em; }
.ttl .ln { overflow:hidden; } .ttl .ln > span { display:block; }
.ttl b { color:#FF5A1F; font-weight:900; } .ttl b.r { color:#FF4438; }
.cell { position:absolute; border-radius:22px; background:rgba(18,23,36,0.94); border:1.5px solid rgba(255,255,255,0.12); box-shadow:0 0 40px rgba(255,90,31,0.14); opacity:0; }
.cell.hot { border-color:rgba(255,90,31,0.75); }
.cell.warn { border-color:rgba(255,68,56,0.75); }
.ib { position:relative; flex:none; width:var(--s); height:var(--s); }
/* thermometer */
.ic-therm::before { content:""; position:absolute; left:38%; top:4%; width:24%; height:66%; border-radius:999px; border:calc(var(--s)*0.06) solid #FF5A1F; box-sizing:border-box; }
.ic-therm::after { content:""; position:absolute; left:26%; bottom:2%; width:48%; height:48%; border-radius:50%; background:#FF5A1F; }
/* rain drop */
.ic-drop::before { content:""; position:absolute; left:20%; top:22%; width:60%; height:60%; background:#FF5A1F; border-radius:0 50% 50% 50%; transform:rotate(45deg); }
.ic-drop.r::before { background:#FF4438; }
/* sun */
.ic-sun::before { content:""; position:absolute; left:26%; top:26%; width:48%; height:48%; border-radius:50%; background:#FF5A1F; }
.ic-sun::after { content:""; position:absolute; inset:4%; border-radius:50%; border:calc(var(--s)*0.07) dashed #FF5A1F; box-sizing:border-box; }
/* wind: three rounded strokes */
.ic-wind::before, .ic-wind::after, .ic-wind i { content:""; position:absolute; left:8%; height:calc(var(--s)*0.09); border-radius:999px; background:#FF5A1F; }
.ic-wind::before { top:22%; width:70%; } .ic-wind i { top:45%; width:86%; display:block; } .ic-wind::after { top:68%; width:52%; }
/* spread: dot with expanding rings */
.ic-spread::before { content:""; position:absolute; left:38%; top:38%; width:24%; height:24%; border-radius:50%; background:#FF5A1F; }
.ic-spread::after { content:""; position:absolute; inset:6%; border-radius:50%; border:calc(var(--s)*0.06) solid rgba(255,90,31,0.6); box-sizing:border-box; box-shadow:inset 0 0 0 calc(var(--s)*0.14) rgba(11,14,20,0.0), 0 0 0 0 transparent; }
.ic-spread i { position:absolute; inset:22%; border-radius:50%; border:calc(var(--s)*0.06) solid #FF5A1F; box-sizing:border-box; display:block; }
/* river waves */
.ic-wave i { position:absolute; left:6%; right:6%; height:28%; border-top:calc(var(--s)*0.08) solid #FF5A1F; border-radius:50% 50% 0 0 / 100% 100% 0 0; display:block; }
.ic-wave i:nth-child(1) { top:18%; } .ic-wave i:nth-child(2) { top:44%; } .ic-wave i:nth-child(3) { top:70%; opacity:0.6; }
.ic-wave.r i { border-top-color:#FF4438; }
/* warning triangle */
.ic-warn::before { content:""; position:absolute; left:8%; bottom:10%; width:0; height:0; border-left:calc(var(--s)*0.42) solid transparent; border-right:calc(var(--s)*0.42) solid transparent; border-bottom:calc(var(--s)*0.74) solid #FF4438; }
.ic-warn::after { content:"!"; position:absolute; left:0; right:0; bottom:9%; text-align:center; font-weight:900; font-size:calc(var(--s)*0.46); line-height:1; color:#0B0E14; }
/* calendar */
.ic-cal::before { content:""; position:absolute; left:10%; top:18%; width:80%; height:72%; border-radius:12%; border:calc(var(--s)*0.07) solid #FF5A1F; box-sizing:border-box; }
.ic-cal::after { content:""; position:absolute; left:10%; top:18%; width:80%; height:22%; border-radius:12% 12% 0 0; background:#FF5A1F; }
/* boat */
.ic-boat::before { content:""; position:absolute; left:6%; bottom:16%; width:52%; height:0; border-top:calc(var(--s)*0.22) solid #FF5A1F; border-left:calc(var(--s)*0.12) solid transparent; border-right:calc(var(--s)*0.12) solid transparent; }
.ic-boat::after { content:""; position:absolute; left:42%; top:8%; width:0; height:0; border-bottom:calc(var(--s)*0.5) solid rgba(255,90,31,0.75); border-right:calc(var(--s)*0.34) solid transparent; }
.ic-boat i { position:absolute; left:38%; top:8%; width:calc(var(--s)*0.05); height:62%; background:#FF5A1F; display:block; }
/* house */
.ic-house::before { content:""; position:absolute; left:4%; top:6%; width:0; height:0; border-left:calc(var(--s)*0.46) solid transparent; border-right:calc(var(--s)*0.46) solid transparent; border-bottom:calc(var(--s)*0.40) solid #FF5A1F; }
.ic-house::after { content:""; position:absolute; left:20%; top:46%; width:60%; height:48%; background:#FF5A1F; border-radius:0 0 6% 6%; }
.ic-house i { position:absolute; left:42%; top:66%; width:16%; height:28%; background:#0B0E14; z-index:1; display:block; }
.cutflash { position:absolute; inset:0; z-index:6; pointer-events:none; opacity:0; background:linear-gradient(180deg, rgba(255,90,31,0.4), rgba(255,68,56,0.18)); }
"""


def icon(kind, size, extra=""):
    inner = {"wind": "<i></i>", "spread": "<i></i>", "wave": "<i></i><i></i><i></i>", "boat": "<i></i>", "house": "<i></i>"}.get(kind, "")
    return f'<span class="ib ic-{kind}{(" " + extra) if extra else ""}" style="--s:{size}px">{inner}</span>'


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


def pop(sel, t, dy=30, dur=0.45):
    return f"    tl.fromTo('{sel}',{{autoAlpha:0,y:{dy},scale:0.96}},{{autoAlpha:1,y:0,scale:1,duration:{dur},ease:'power3.out'}},{t});\n"


def head_js(prefix, t0=0.05):
    return (f"    tl.fromTo('#{prefix}-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},{t0});\n"
            f"    tl.fromTo('#{prefix}-t1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{round(t0 + 0.07, 2)});\n"
            f"    tl.fromTo('#{prefix}-t2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},{round(t0 + 0.21, 2)});\n")


frames = {}

# ---------------- 01 HOOK (fixed brand layout) ----------------
frames['01-hook'] = frame('01-hook', """
.hk-photo { position:absolute; left:0; right:0; top:0; height:900px; overflow:hidden; background:#05070c; }
.hk-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:46% 50%; }
.hk-scrim { position:absolute; inset:0; background:linear-gradient(180deg, rgba(11,14,20,0.25) 0%, rgba(11,14,20,0.0) 40%, rgba(11,14,20,0.99) 100%); }
.hk-panel { position:absolute; left:0; right:0; top:770px; padding:30px 64px 0; display:flex; flex-direction:column; align-items:flex-start; }
.hk-masthead { display:flex; align-items:center; gap:14px; margin-bottom:28px; opacity:0; }
.hk-logo { width:60px; height:60px; flex:none; } .hk-logo img { display:block; width:100%; height:100%; }
.hk-mw { font-weight:800; font-size:34px; color:#fff; }
.hk-badge { display:inline-flex; align-items:center; gap:10px; padding:11px 19px; border-radius:9px; border:1.5px solid rgba(255,90,31,0.85); background:rgba(255,90,31,0.12); margin-bottom:30px; opacity:0; }
.hk-badge .d { width:8px; height:8px; border-radius:50%; background:#FF5A1F; flex:none; }
.hk-badge span { font-weight:500; font-size:24px; letter-spacing:0.03em; color:#fff; white-space:nowrap; }
.hk-name-wrap { overflow:hidden; padding-bottom:6px; }
.hk-name { font-weight:900; font-size:128px; line-height:1.02; letter-spacing:-0.02em; color:#fff; white-space:nowrap; }
.hk-name.o { color:#FF5A1F; }
.hk-sub { margin-top:24px; font-weight:700; font-size:36px; line-height:1.3; color:rgba(255,255,255,0.92); opacity:0; }
.hk-sub b { color:#FF5A1F; font-weight:800; }
.hk-tags { display:flex; flex-direction:column; gap:30px; margin-top:50px; }
.hk-tag { font-weight:800; font-size:48px; line-height:1; color:#FF5A1F; opacity:0; white-space:nowrap; }
.hk-tag.warn { color:#FF4438; }
.hk-tag .dot { display:inline-block; width:13px; height:13px; border-radius:50%; background:currentColor; margin:0 16px 8px 0; vertical-align:middle; }
""", """
    <div class="hk-photo"><img src="assets/img/article-hero.jpg" alt=""><div class="hk-scrim"></div><div class="credit">Ảnh: Dân Trí</div></div>
    <div class="hk-panel">
      <div class="hk-masthead"><div class="hk-logo"><img src="public/logo.png" alt=""></div><div class="hk-mw">Tin Tức Số</div></div>
      <div class="hk-badge"><span class="d"></span><span>Nguồn: Dân Trí, Tuổi Trẻ · 23/11/2026</span></div>
      <div class="hk-name-wrap"><div class="hk-name" id="hk-n1">Gió mùa</div></div>
      <div class="hk-name-wrap"><div class="hk-name o" id="hk-n2">đông bắc</div></div>
      <div class="hk-sub" id="hk-sub">Từ sáng 24/11 · Bắc rét · <b>Trung mưa lớn</b></div>
      <div class="hk-tags">
        <div class="hk-tag" id="hk-t1"><span class="dot"></span>Núi cao dưới 10°C</div>
        <div class="hk-tag warn" id="hk-t2"><span class="dot"></span>Mưa có nơi trên 250 mm</div>
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

# ---------------- 02 WHAT HAPPENED (ảnh + panel + 2 ô vuông icon) ----------------
D2 = DURS[1]
frames['02-what'] = frame('02-what', """
.w-head { position:absolute; left:64px; top:190px; display:flex; align-items:center; gap:18px; }
.w-kick { opacity:0; }
.w-badge { padding:7px 16px; border-radius:30px; border:2px solid #FF5A1F; font-weight:800; font-size:24px; color:#fff; background:rgba(255,90,31,0.15); opacity:0; }
.w-ttl { top:240px; }
.w-img { position:absolute; left:64px; right:64px; top:420px; height:540px; border-radius:22px; overflow:hidden; opacity:0; box-shadow:0 0 40px rgba(255,90,31,0.14); }
.w-img img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 55%; }
.w-sq { top:1000px; width:466px; height:450px; padding:40px 36px; display:flex; flex-direction:column; align-items:flex-start; }
.w-sq .k { margin-top:auto; font-weight:700; font-size:22px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.w-sq .v { margin-top:12px; font-weight:900; font-size:46px; line-height:1.12; color:#fff; }
.w-sq .v b { color:#FF5A1F; }
.w-step { position:absolute; left:64px; top:40px; font-weight:900; font-size:30px; color:rgba(255,255,255,0.25); }
""", f"""
    <div class="w-head"><div class="kick w-kick" id="w-kick">Chuyện gì xảy ra</div><div class="w-badge" id="w-badge">Sáng 24/11</div></div>
    <div class="ttl w-ttl"><div class="ln"><span id="w-h1">Không khí lạnh</span></div><div class="ln"><span id="w-h2"><b>tràn xuống</b> miền Bắc</span></div></div>
    <div class="w-img" id="w-img"><img src="assets/img/article-hero.jpg" alt=""><div class="credit">Ảnh: Dân Trí</div></div>
    <div class="cell hot w-sq" id="w-s1" style="left:64px">{icon('wind', 110)}<div class="k">Ảnh hưởng trước</div><div class="v"><b>Đông Bắc Bộ</b></div></div>
    <div class="cell w-sq" id="w-s2" style="left:550px">{icon('spread', 110)}<div class="k">Sau đó lan ra</div><div class="v">Tây Bắc Bộ, Bắc Trung Bộ, <b>Trung Trung Bộ</b></div></div>""", f"""
    tl.fromTo('#w-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.05);
    tl.fromTo('#w-badge',{{autoAlpha:0,scale:0.7}},{{autoAlpha:1,scale:1,duration:0.4,ease:'back.out(2)'}},0.3);
    tl.fromTo('#w-h1',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.15);
    tl.fromTo('#w-h2',{{yPercent:115}},{{yPercent:0,duration:0.55,ease:'power4.out'}},0.3);
    tl.fromTo('#w-img',{{autoAlpha:0,y:40}},{{autoAlpha:1,y:0,duration:0.6,ease:'power3.out'}},0.35);
    tl.fromTo('#w-img img',{{scale:1.14}},{{scale:1.0,duration:{D2},ease:'none'}},0.35);
{pop('#w-s1', T(2.9))}{pop('#w-s2', T(4.1))}""")

# ---------------- 03 KEY FACTS (3 ô 3x1, mỗi ô 1 icon đại diện) ----------------
REG = [
    ("therm", "", "Bắc Bộ · Bắc Trung Bộ", "Chuyển <b>rét</b>", "Vùng núi có nơi rét đậm", "hot", T(0.0)),
    ("drop", "", "Trung Bộ", "Có thể <b>2 đợt mưa lớn</b>", "Từ 24 đến 30/11", "hot", T(3.15)),
    ("sun", "", "Nam Bộ", "Ngày <b>nắng</b>", "TP.HCM cao nhất 32–34°C", "", T(7.15)),
]
f_html, f_js = "", ""
for i, (ic, ex, k, v, s, cls, t) in enumerate(REG):
    top = 450 + i * 340
    f_html += (f'    <div class="cell {cls} f-row" id="f-c{i}" style="top:{top}px"><div class="f-ic">{icon(ic, 120, ex)}</div>'
               f'<div class="f-tx"><div class="k">{k}</div><div class="v">{v}</div><div class="s">{s}</div></div></div>\n')
    f_js += pop(f'#f-c{i}', t)
frames['03-facts'] = frame('03-facts', """
.f-kick { position:absolute; left:64px; top:190px; opacity:0; }
.f-ttl { top:240px; }
.f-row { left:64px; right:64px; height:310px; padding:0 44px; display:flex; align-items:center; gap:40px; }
.f-ic { width:180px; height:180px; flex:none; border-radius:24px; background:rgba(255,90,31,0.10); border:1.5px solid rgba(255,90,31,0.35); display:flex; align-items:center; justify-content:center; }
.f-tx .k { font-weight:700; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.f-tx .v { margin-top:12px; font-weight:800; font-size:52px; line-height:1.12; color:#fff; }
.f-tx .v b { color:#FF5A1F; font-weight:900; }
.f-tx .s { margin-top:12px; font-weight:600; font-size:30px; color:rgba(255,255,255,0.72); }
""", f"""
    <div class="kick f-kick" id="f-kick">Một đợt gió mùa</div>
    <div class="ttl f-ttl"><div class="ln"><span id="f-t1">Ba miền,</span></div><div class="ln"><span id="f-t2"><b>ba kiểu thời tiết</b></span></div></div>
{f_html}""", head_js('f') + f_js)

# ---------------- 04 DATA MOMENT (ô lớn giữa lưới 3 ô + thang nhiệt độ tỉ lệ thật) ----------------
# scale 8..20 °C mapped to 0..100%
def pct(c):
    return round((c - 8) / 12 * 100, 2)

RANGES = [("Núi cao", 8, 10, "linear-gradient(90deg, rgba(255,68,56,0), #FF4438)", T(4.8)), ("Vùng núi", 11, 14, "#FF5A1F", T(2.5)),
          ("Bắc Bộ", 14, 17, "rgba(255,90,31,0.7)", T(1.3)), ("Bắc Trung Bộ", 15, 18, "rgba(255,90,31,0.45)", T(5.7))]
r_html, r_js = "", ""
for i, (lab, a, b, col, t) in enumerate(RANGES):
    top = 70 + i * 54
    r_html += (f'<div class="d-rl" style="top:{top}px">{lab}</div>'
               f'<div class="d-rb" id="d-rb{i}" style="top:{top}px;left:calc(210px + (100% - 250px) * {pct(a)/100});width:calc((100% - 250px) * {(pct(b)-pct(a))/100});background:{col}"></div>'
               f'<div class="d-rv" id="d-rv{i}" style="top:{top}px;left:calc(222px + (100% - 250px) * {pct(b)/100})">{("dưới " + str(b)) if i == 0 else (str(a) + "–" + str(b))}°</div>\n')
    r_js += f"    tl.to('#d-rb{i}',{{scaleX:1,duration:0.6,ease:'power2.out'}},{t});\n"
    r_js += f"    tl.fromTo('#d-rv{i}',{{autoAlpha:0}},{{autoAlpha:1,duration:0.3}},{round(t + 0.45, 2)});\n"
ticks = "".join(f'<div class="d-tk" style="left:calc(210px + (100% - 250px) * {pct(c)/100})">{c}°</div>' for c in (8, 10, 12, 14, 16, 18, 20))
frames['04-data'] = frame('04-data', f"""
.d-kick {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
.d-glow {{ position:absolute; left:290px; top:300px; width:500px; height:700px; border-radius:50%; background:radial-gradient(circle, rgba(255,68,56,0.22), transparent 70%); opacity:0; }}
.d-side {{ top:440px; width:240px; height:520px; padding:36px 22px; display:flex; flex-direction:column; align-items:center; text-align:center; }}
.d-side .v {{ margin-top:auto; font-weight:900; font-size:50px; line-height:1.05; color:rgba(255,255,255,0.85); white-space:nowrap; }}
.d-side .v small {{ display:block; font-size:32px; }}
.d-side .k {{ margin-top:14px; font-weight:700; font-size:24px; line-height:1.25; color:rgba(255,255,255,0.6); }}
.d-main {{ left:324px; top:360px; width:432px; height:680px; padding:44px 20px; display:flex; flex-direction:column; align-items:center; text-align:center; border-width:2.5px; }}
.d-main .pre {{ margin-top:30px; font-weight:800; font-size:44px; color:#fff; }}
.d-main .n {{ font-weight:900; font-size:176px; line-height:1; letter-spacing:-0.04em; color:#FF4438; white-space:nowrap; }}
.d-main .n sup {{ font-size:70px; vertical-align:top; position:relative; top:18px; letter-spacing:0; }}
.d-main .k {{ margin-top:auto; font-weight:800; font-size:34px; color:#fff; }}
.d-main .k2 {{ margin-top:8px; font-weight:600; font-size:24px; color:rgba(255,255,255,0.6); }}
.d-scale {{ left:64px; right:64px; top:1090px; height:360px; }}
.d-scale .t {{ position:absolute; left:40px; top:26px; font-weight:700; font-size:22px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }}
.d-rl {{ position:absolute; left:40px; height:40px; line-height:40px; font-weight:700; font-size:24px; color:#fff; white-space:nowrap; }}
.d-rb {{ position:absolute; height:34px; margin-top:3px; border-radius:10px; transform-origin:0% 50%; transform:scaleX(0); }}
.d-rv {{ position:absolute; height:40px; line-height:40px; font-weight:800; font-size:22px; color:#fff; white-space:nowrap; opacity:0; }}
.d-axis {{ position:absolute; left:210px; right:40px; top:296px; height:2px; background:rgba(255,255,255,0.25); }}
.d-tk {{ position:absolute; top:306px; width:60px; margin-left:-30px; text-align:center; font-weight:700; font-size:20px; color:rgba(255,255,255,0.55); }}
""", f"""
    <div class="kick d-kick" id="d-kick">Nhiệt độ thấp nhất</div>
    <div class="d-glow" id="d-glow"></div>
    <div class="cell d-side" id="d-l" style="left:64px">{icon('therm', 90)}<div class="v num">14–17<small>°C</small></div><div class="k">Bắc Bộ phổ biến</div></div>
    <div class="cell warn d-main" id="d-m">{icon('therm', 120)}<div class="pre">Dưới</div><div class="n num"><span id="d-n">17</span><sup>°C</sup></div><div class="k">Vùng núi cao</div><div class="k2">có nơi</div></div>
    <div class="cell d-side" id="d-r" style="left:776px">{icon('therm', 90)}<div class="v num">15–18<small>°C</small></div><div class="k">Bắc Trung Bộ phổ biến</div></div>
    <div class="cell d-scale" id="d-sc"><div class="t">Thang nhiệt độ thấp nhất</div>
{r_html}<div class="d-axis"></div>{ticks}</div>""", f"""
    tl.fromTo('#d-kick',{{autoAlpha:0,y:-10}},{{autoAlpha:1,y:0,duration:0.35,ease:'power2.out'}},0.0);
{pop('#d-sc', 0.25)}{pop('#d-l', T(1.2))}{r_js}{pop('#d-m', T(3.9), 40, 0.5)}    tl.fromTo('#d-glow',{{autoAlpha:0}},{{autoAlpha:1,duration:0.8}},{T(4.0)});
    const cn = {{ v: 17 }}; const cnE = document.getElementById('d-n');
    tl.fromTo(cn,{{v:17}},{{v:10,duration:0.9,ease:'power2.out',onUpdate(){{ cnE.textContent = Math.round(cn.v); }}}},{T(4.2)});
{pop('#d-r', T(5.6))}""")

# ---------------- 05 CONTEXT (lưới 2x3 dashboard, smash-cut khi chuyển mưa -> lũ) ----------------
CELLS = [
    ("drop", "", "Đợt 1 · đến hết 25/11", "80–180 mm", "Huế → phía Đông Quảng Ngãi", "hot", T(2.4)),
    ("drop", "r", "Có nơi", "trên 250 mm", "Mưa cục bộ", "warn", T(5.5)),
    ("wave", "", "Sông Bồ, sông Hương", "Báo động 2–3", "Huế · có thể lên", "hot", T(7.3)),
    ("wave", "", "Sông Trà Khúc, sông Vệ", "Báo động 2–3", "Quảng Ngãi · có thể lên", "hot", T(8.7)),
    ("cal", "", "Đợt 2", "27–30/11", "Mưa lớn diện rộng", "", T(11.8)),
    ("warn", "", "Nguy cơ", "Lũ quét, sạt lở", "Vùng núi Quảng Trị → Khánh Hòa", "warn", T(13.3)),
]
x_html, x_js = "", ""
for i, (ic, ex, k, v, s, cls, t) in enumerate(CELLS):
    col, row = i % 2, i // 2
    x_html += (f'    <div class="cell {cls} x-cell" id="x-c{i}" style="left:{64 + col * 486}px;top:{450 + row * 340}px">'
               f'{icon(ic, 76, ex)}<div class="k">{k}</div><div class="v{" r" if cls == "warn" else ""}">{v}</div><div class="s">{s}</div></div>\n')
    x_js += pop(f'#x-c{i}', t, 24, 0.4)
CUT = T(7.25)
frames['05-context'] = frame('05-context', """
.x-kick { position:absolute; left:64px; top:190px; opacity:0; }
.x-ttl { top:240px; }
.x-cell { width:466px; height:320px; padding:32px 32px; display:flex; flex-direction:column; align-items:flex-start; }
.x-cell .k { margin-top:auto; font-weight:700; font-size:22px; letter-spacing:0.1em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.x-cell .v { margin-top:8px; font-weight:900; font-size:52px; line-height:1.08; color:#FF5A1F; white-space:nowrap; }
.x-cell .v.r { color:#FF4438; }
.x-cell .s { margin-top:8px; font-weight:600; font-size:24px; line-height:1.25; color:rgba(255,255,255,0.75); }
#x-content { position:absolute; inset:0; }
""", f"""
    <div id="x-content">
    <div class="kick x-kick" id="x-kick">Mưa lớn miền Trung</div>
    <div class="ttl x-ttl"><div class="ln"><span id="x-t1">Hai đợt mưa,</span></div><div class="ln"><span id="x-t2"><b>lũ có thể lên cao</b></span></div></div>
{x_html}    </div>
    <div class="cutflash" id="x-flash"></div>""", head_js('x') + x_js + f"""
    tl.fromTo('#x-flash',{{opacity:0}},{{opacity:0.55,duration:0.05,ease:'none'}},{CUT});
    tl.to('#x-flash',{{opacity:0,duration:0.16,ease:'power1.in'}},{round(CUT + 0.05, 2)});
    tl.fromTo('#x-content',{{scale:1}},{{scale:0.986,duration:0.06,ease:'power1.out'}},{CUT});
    tl.to('#x-content',{{scale:1,duration:0.14,ease:'power2.out'}},{round(CUT + 0.061, 3)});
""")

# ---------------- 06 IMPACT (2 ô lớn cạnh nhau, icon lớn phía trên tiêu đề) ----------------
frames['06-impact'] = frame('06-impact', """
.i-kick { position:absolute; left:64px; top:190px; opacity:0; }
.i-ttl { top:240px; }
.i-chip { position:absolute; left:64px; right:64px; top:430px; height:96px; padding:0 30px; display:flex; align-items:center; gap:18px; border-radius:18px; border:1.5px solid rgba(255,90,31,0.6); background:rgba(255,90,31,0.10); opacity:0; }
.i-chip .d { width:14px; height:14px; border-radius:50%; background:#FF5A1F; flex:none; }
.i-chip span { font-weight:800; font-size:30px; color:#fff; }
.i-blk { top:560px; width:466px; height:890px; padding:44px 34px; display:flex; flex-direction:column; align-items:flex-start; }
.i-blk .icw { width:150px; height:150px; border-radius:26px; background:rgba(255,90,31,0.10); border:1.5px solid rgba(255,90,31,0.35); display:flex; align-items:center; justify-content:center; }
.i-blk .k { margin-top:34px; font-weight:700; font-size:24px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.6); }
.i-blk .h { margin-top:14px; font-weight:800; font-size:46px; line-height:1.15; color:#fff; }
.i-blk .h b { color:#FF5A1F; }
.i-pills { margin-top:auto; display:flex; flex-direction:column; gap:14px; width:100%; }
.i-pill { padding:16px 22px; border-radius:14px; border:2px solid rgba(255,90,31,0.7); background:rgba(255,90,31,0.10); font-weight:800; font-size:30px; line-height:1.2; color:#fff; opacity:0; }
.i-pill.r { border-color:rgba(255,68,56,0.75); background:rgba(255,68,56,0.10); }
""", f"""
    <div class="kick i-kick" id="i-kick">Đã triển khai</div>
    <div class="ttl i-ttl"><div class="ln"><span id="i-t1">Chiều 23/11:</span></div><div class="ln"><span id="i-t2"><b>yêu cầu ứng phó</b></span></div></div>
    <div class="i-chip" id="i-chip"><span class="d"></span><span>Ban Chỉ đạo Phòng thủ dân sự quốc gia</span></div>
    <div class="cell hot i-blk" id="i-b1" style="left:64px"><div class="icw">{icon('boat', 110)}</div><div class="k">Tàu thuyền</div><div class="h">Hướng dẫn <b>chủ động phòng tránh</b></div>
      <div class="i-pills"><div class="i-pill" id="i-p0">Ven biển<br>Quảng Ninh → Lâm Đồng</div></div></div>
    <div class="cell warn i-blk" id="i-b2" style="left:550px"><div class="icw">{icon('house', 110)}</div><div class="k">Người dân</div><div class="h">Rà soát, <b>sơ tán</b> vùng nguy cơ cao</div>
      <div class="i-pills"><div class="i-pill r" id="i-p1">Ngập sâu</div><div class="i-pill r" id="i-p2">Lũ quét</div><div class="i-pill r" id="i-p3">Sạt lở đất</div></div></div>""",
    head_js('i') + f"""    tl.fromTo('#i-chip',{{autoAlpha:0,y:16}},{{autoAlpha:1,y:0,duration:0.4,ease:'power2.out'}},{T(1.3)});
{pop('#i-b1', T(3.0))}    tl.fromTo('#i-p0',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.35,ease:'power2.out'}},{T(4.3)});
{pop('#i-b2', T(6.8))}    tl.fromTo('#i-p1',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.3,ease:'power2.out'}},{T(9.2)});
    tl.fromTo('#i-p2',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.3,ease:'power2.out'}},{T(9.8)});
    tl.fromTo('#i-p3',{{autoAlpha:0,x:-20}},{{autoAlpha:1,x:0,duration:0.3,ease:'power2.out'}},{T(10.4)});
""")

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
      <div class="t-ctx" id="t-ctx"><span class="rc"></span>Gió mùa đông bắc · cảnh báo từ chiều 23/11</div>
      <div class="t-head">
        <div class="ln"><span id="t-h1">Cảnh báo thời tiết:</span></div>
        <div class="ln"><span id="t-h2" class="o">đủ sớm để chủ động</span></div>
        <div class="ln"><span id="t-h3">hay vẫn bị động?</span></div>
      </div>
      <div class="t-opts">
        <div class="t-opt up" id="t-o1"><div class="emo"></div><div class="lab">Đủ sớm, kịp chủ động</div></div>
        <div class="t-vs" id="t-vs">VS</div>
        <div class="t-opt down" id="t-o2"><div class="emo"></div><div class="lab">Người dân vẫn bị động</div></div>
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
    o1=T(5.1), vs=T(6.0), o2=T(6.4), cta=T(7.6), pulse=round(T(7.6) + 0.5, 2), sign=T(8.0)))

SFX = [
    ("hook", "impact-bass-1", 0.6, 0.6, 0.35),
    ("t1", "whoosh-short", STARTS[1] - 0.1, 0.5, 0.3),
    ("t2", "whoosh-short", STARTS[2] - 0.1, 0.5, 0.3),
    ("t3", "whoosh-short", STARTS[3] - 0.1, 0.5, 0.3),
    ("t4", "whoosh-short", STARTS[4] - 0.1, 0.5, 0.3),
    ("t5", "whoosh-short", STARTS[5] - 0.1, 0.5, 0.3),
    ("t6", "whoosh-short", STARTS[6] - 0.1, 0.5, 0.3),
    ("ws2", "pop", STARTS[1] + T(4.1), 0.4, 0.22),
    ("f2", "click-soft", STARTS[2] + T(3.15), 0.35, 0.3),
    ("f3", "click-soft", STARTS[2] + T(7.15), 0.35, 0.3),
    ("big", "impact-bass-1", STARTS[3] + T(3.9), 0.6, 0.3),
    ("x250", "pop", STARTS[4] + T(5.5), 0.4, 0.24),
    ("xcut", "click-soft", STARTS[4] + CUT, 0.35, 0.32),
    ("x2", "pop", STARTS[4] + T(11.8), 0.4, 0.22),
    ("i2", "click-soft", STARTS[5] + T(6.8), 0.35, 0.3),
    ("o1", "pop", STARTS[6] + T(5.1), 0.35, 0.3),
    ("o2", "pop", STARTS[6] + T(6.4), 0.35, 0.3),
    ("cta", "chime", STARTS[6] + T(7.6), 1.2, 0.32),
]
TRK = {a: (31 if a in ("big", "hook", "f3", "xcut", "i2", "o2") else 30) for a, *_ in SFX}
SOURCE_TEXT = "Nguồn: Dân Trí, Tuổi Trẻ"
SEED = 20261124
DISPLAY = {"mi-li-mét,": "mm,", "mi-li-mét.": "mm."}

exec(open('gen_tail.py', encoding='utf-8').read())
