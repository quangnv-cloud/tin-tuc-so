import json,re,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def ff(w,sub,rng): return f"@font-face{{font-family:'Montserrat';font-weight:{w};src:url('assets/fonts/Montserrat-{w}-{sub}.woff2') format('woff2');unicode-range:{rng};}}"
LAT="U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
VI="U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB"
FONTS="\n".join(ff(w,s,r) for w in (400,500,600,700,800,900) for s,r in (("latin",LAT),("vietnamese",VI)))
names=["01-hook","02-what","03-facts","04-data","05-context","06-impact","07-cta"]
for n in names:
    open(f"compositions/frames/{n}.html","w").write(open(f"compositions/src/{n}.html").read().replace("/*FONTS*/",FONTS))
vd=[5.280,7.968,10.680,8.472,10.128,10.104,6.600]
pad=[0.40,0.40,0.40,0.40,0.40,0.40,2.00]
dur=[round(v+p,2) for v,p in zip(vd,pad)]
st=[0.0]
for d in dur[:-1]: st.append(round(st[-1]+d,2))
total=round(st[-1]+dur[-1],2)
# stars
seed=20261111
def mulberry():
    global seed
    seed=(seed+0x6D2B79F5)&0xffffffff; t=seed
    t=((t^(t>>15))*(1|t))&0xffffffff
    t=(t+(((t^(t>>7))*(61|t))&0xffffffff))&0xffffffff ^ t
    return ((t^(t>>14))&0xffffffff)/4294967296
stars="".join(f'<circle cx="{int(mulberry()*1080)}" cy="{int(mulberry()*1920)}" r="{1.5+mulberry()*1.5:.1f}" fill="#fff" opacity="{0.15+mulberry()*0.25:.2f}"/>' for _ in range(40))
# captions
caps=[];js=[]
ci=0
for i in range(7):
    w=[x for x in json.load(open(f"assets/voice/stt{i+1}.json"))['words'] if x['type']=='word']
    chunks=[];cur=[]
    for x in w:
        cur.append(x)
        end_punct=x['text'][-1] in ',.?!'
        if len(cur)>=5 or (end_punct and len(cur)>=3): chunks.append(cur);cur=[]
    if cur:
        if len(cur)<=2 and chunks: chunks[-1]+=cur
        else: chunks.append(cur)
    for k,c in enumerate(chunks):
        s0=st[i]+c[0]['start']; e=st[i]+c[-1]['end']+0.3
        if k+1<len(chunks): e=min(e, st[i]+chunks[k+1][0]['start']-0.02)
        spans=" ".join(f'<span class="w" id="w{ci}_{j}">{x["text"]}</span>' for j,x in enumerate(c))
        caps.append(f'<div class="cap" id="cap{ci}">{spans}</div>')
        js.append(f"tl.set('#cap{ci}',{{autoAlpha:1}},{s0:.2f});tl.set('#cap{ci}',{{autoAlpha:0}},{e:.2f});")
        for j,x in enumerate(c): js.append(f"tl.to('#w{ci}_{j}',{{color:'#FF5A1F',duration:0.1,ease:'none'}},{st[i]+x['start']:.2f});")
        ci+=1
scenes="\n".join(f'<div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{st[k]}" data-duration="{dur[k]}" data-track-index="1"></div>' for k,n in enumerate(names))
voices="\n".join(f'<audio id="el-voice-{k+1}" src="assets/voice/line{k+1}.mp3" data-start="{st[k]}" data-duration="{vd[k]:.2f}" data-track-index="10" data-audio-group="voiceover"></audio>' for k in range(7))
sfx=[("hook","impact-bass-1",0.3,0.6,0.35)]+[(f"t{k}","whoosh-short",st[k]-0.1,0.5,0.3) for k in range(1,7)]+[
 ("srcring","click-soft",st[1]+0.6,0.35,0.3),("cut3","click-soft",st[2]+3.25,0.35,0.32),("ring4","pop",st[3]+1.4,0.4,0.3),("num4","impact-bass-1",st[3]+5.2,0.6,0.28),
 ("s2ctx","pop",st[4]+2.4,0.4,0.3),("p88","pop",st[4]+7.4,0.4,0.28),("r6a","pop",st[5]+2.4,0.4,0.28),("r6b","pop",st[5]+4.8,0.4,0.28),
 ("o1","pop",st[6]+1.3,0.35,0.3),("o2","click-soft",st[6]+2.7,0.35,0.32),("cta","chime",st[6]+4.75,1.2,0.32)]
sfxh="\n".join(f'<audio id="el-sfx-{a}" src="assets/sfx/{b}.mp3" data-start="{c:.2f}" data-duration="{d}" data-track-index="30" data-volume="{v}"></audio>' for a,b,c,d,v in sfx)
html=f'''<!DOCTYPE html>
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
#caps {{ position:absolute; left:80px; right:180px; top:1515px; height:90px; z-index:85; pointer-events:none; }}
.cap {{ position:absolute; left:0; right:0; top:0; text-align:center; font-weight:800; font-size:42px; line-height:1.2; color:rgba(255,255,255,0.92); text-shadow:0 2px 12px rgba(0,0,0,0.85); opacity:0; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
<div id="bg-depth">
  <div class="blob" style="width:640px;height:640px;background:radial-gradient(circle,rgba(255,90,31,0.20),transparent 70%);top:-120px;left:-160px;"></div>
  <div class="blob" style="width:560px;height:560px;background:radial-gradient(circle,rgba(255,68,56,0.16),transparent 70%);top:900px;right:-200px;"></div>
  <div class="blob" style="width:520px;height:520px;background:radial-gradient(circle,rgba(255,90,31,0.12),transparent 70%);bottom:-180px;left:200px;"></div>
  <svg id="bg-stars" viewBox="0 0 1080 1920">{stars}</svg>
</div>
{scenes}
<div id="brand-anchor"><div id="ba-source"><span class="dot"></span><span>Nguồn: Tuổi Trẻ</span></div><div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div></div>
<div id="caps">{chr(10).join(caps)}</div>
{voices}
<audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{total}" data-track-index="20" data-volume="0.3"></audio>
{sfxh}
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.set('#brand-anchor',{{opacity:1}},{st[1]});
tl.to('.blob',{{x:'+=40',y:'-=30',duration:18,ease:'sine.inOut',repeat:3,yoyo:true,stagger:3}},0);
tl.to('#bg-stars circle',{{opacity:'+=0.25',duration:4,ease:'sine.inOut',repeat:15,yoyo:true,stagger:{{each:0.15,from:'random'}}}},0);
{chr(10).join(js)}
window.__timelines['main'] = tl;
</script>
</body>
</html>
'''
open("index.html","w").write(html)
print("starts",st,"durs",dur,"total",total,"caps",ci)
