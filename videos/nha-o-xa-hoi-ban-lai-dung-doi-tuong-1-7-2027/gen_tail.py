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
{clips}<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>{SOURCE_TEXT}</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
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
