import json,re,os
S='/tmp/claude-0/-workspace-tin-tuc-so/acb9e5a5-8f21-5cfa-ae75-184377287922/scratchpad'
fonts=open('/tmp/claude-0/fonts.css',encoding='utf-8').read()
common=open('src/common.css',encoding='utf-8').read()
names=['01-hook','02-what','03-facts','04-data','05-context','06-impact','07-cta']
voice=[8.448,11.112,8.904,6.936,11.688,13.032,7.128]
pad=[0.4,0.4,0.4,0.4,0.4,0.4,0.8]
D=[round(v+p,2) for v,p in zip(voice,pad)]
St=[0]
for d in D[:-1]: St.append(round(St[-1]+d,2))
TOTAL=round(St[-1]+D[-1],2)
for n in names:
    css,html,js=open(f'src/{n}.html',encoding='utf-8').read().split('\n@@\n')
    out=f"""<template>
  <style>
{fonts}
{common}
{css}
  </style>

  <div id="root" data-composition-id="{n}" data-width="1080" data-height="1920">
{html}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}
    window.__timelines['{n}'] = tl;
  </script>
</template>
"""
    open(f'compositions/frames/{n}.html','w',encoding='utf-8').write(out)
# captions
caps=[]  # (chunk words [(text,start,end)])
for i in range(7):
    d=json.load(open(f'{S}/stt{i+1}.json'))
    ws=[(x['text'],x['start']+St[i],x['end']+St[i]) for x in d['words'] if x['type']=='word']
    cur=[]
    for w in ws:
        cur.append(w)
        if len(cur)>=4 or re.search(r'[,.:?]$',w[0]) and len(cur)>=2:
            caps.append(cur); cur=[]
    if cur:
        if len(cur)==1 and caps: caps[-1].extend(cur)
        else: caps.append(cur)
capdata=[]
for k,c in enumerate(caps):
    end=c[-1][2]+0.3
    if k+1<len(caps): end=min(end,caps[k+1][0][1]-0.02)
    capdata.append({'s':round(c[0][1],2),'e':round(end,2),'w':[[t,round(a,2)] for t,a,b in c]})
json.dump(capdata,open('src/caps.json','w',encoding='utf-8'),ensure_ascii=False)
scenes=''.join(f'      <div id="el-{n}" class="scene clip" data-composition-id="{n}" data-composition-src="compositions/frames/{n}.html" data-start="{St[i]}" data-duration="{D[i]}" data-track-index="1"></div>\n' for i,n in enumerate(names))
voices=''.join(f'      <audio id="el-voice-{i+1}" src="assets/voice/line{i+1}.mp3" data-start="{St[i]}" data-duration="{voice[i]}" data-track-index="10" data-audio-group="voiceover"></audio>\n' for i in range(7))
sfx=[('hook','impact-bass-1',0.32,0.6,0.35),('t1','whoosh-short',St[1]-0.1,0.5,0.3),('t2','whoosh-short',St[2]-0.1,0.5,0.3),('t3','whoosh-short',St[3]-0.1,0.5,0.3),('data','pop',St[3]+1.65,0.4,0.3),('t4','whoosh-short',St[4]-0.1,0.5,0.3),('n1','click-soft',St[4]+3.5,0.35,0.28),('n2','click-soft',St[4]+4.5,0.35,0.28),('n3','click-soft',St[4]+5.6,0.35,0.28),('n4','click-soft',St[4]+6.3,0.35,0.28),('cut','pop',St[4]+8.6,0.4,0.3),('t5','whoosh-short',St[5]-0.1,0.5,0.3),('warn','impact-bass-1',St[5]+9.3,0.6,0.3),('t6','whoosh-short',St[6]-0.1,0.5,0.3),('o1','pop',St[6]+2.0,0.35,0.3),('o2','click-soft',St[6]+3.4,0.35,0.3),('cta','chime',St[6]+5.3,1.2,0.3)]
sfxh=''.join(f'      <audio id="el-sfx-{a}" src="assets/sfx/{b}.mp3" data-start="{round(c,2)}" data-duration="{d}" data-track-index="30" data-volume="{e}"></audio>\n' for a,b,c,d,e in sfx)
html=f"""<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, height=1920">
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
{fonts}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #0B0E14; font-family: "Montserrat", sans-serif; color: #FFFFFF; }}
      .scene {{ position: absolute; inset: 0; width: 100%; height: 100%; z-index: 2; }}
      #bg-depth {{ position: absolute; inset: 0; overflow: hidden; z-index: 0; }}
      #bg-depth .blob {{ position: absolute; border-radius: 50%; filter: blur(60px); }}
      #bg-stars {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
      #brand-anchor {{ position: absolute; inset: 0; z-index: 90; pointer-events: none; opacity: 0; }}
      #ba-source {{ position: absolute; left: 44px; top: 46px; display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px; border-radius: 8px; background: rgba(11,14,20,0.6); border: 1px solid rgba(255,255,255,0.12); }}
      #ba-source .dot {{ width: 7px; height: 7px; border-radius: 50%; background: #FF5A1F; }}
      #ba-source span {{ font-weight: 500; font-size: 21px; letter-spacing: 0.02em; color: rgba(255,255,255,0.9); white-space: nowrap; }}
      #ba-brand {{ position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }}
      #ba-brand .mark {{ width: 44px; height: 44px; flex: none; }} #ba-brand .mark img {{ display: block; width: 100%; height: 100%; }}
      #ba-brand .word {{ font-weight: 800; font-size: 24px; letter-spacing: 0.01em; color: #fff; }}
      #captions {{ position: absolute; left: 50px; width: 980px; top: 1490px; height: 110px; z-index: 80; pointer-events: none; }}
      .cap-chunk {{ position: absolute; left: 0; right: 0; top: 0; display: block; opacity: 0; text-align: center; font-weight: 800; font-size: 56px; line-height: 1.15; white-space: nowrap; text-shadow: 0 3px 18px rgba(0,0,0,0.85); }}
      .cap-chunk .w {{ color: rgba(255,255,255,0.92); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="bg-depth">
        <div class="blob" style="width:640px;height:640px;background:radial-gradient(circle, rgba(255,90,31,0.20), transparent 70%);top:-120px;left:-160px;"></div>
        <div class="blob" style="width:560px;height:560px;background:radial-gradient(circle, rgba(255,68,56,0.16), transparent 70%);top:900px;right:-200px;"></div>
        <div class="blob" style="width:520px;height:520px;background:radial-gradient(circle, rgba(255,90,31,0.12), transparent 70%);bottom:-180px;left:200px;"></div>
        <svg id="bg-stars" viewBox="0 0 1080 1920"></svg>
      </div>

{scenes}
      <div id="brand-anchor">
        <div id="ba-source"><span class="dot"></span><span>Nguồn: Dân Trí</span></div>
        <div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Tin Tức Số</span></div>
      </div>
      <div id="captions" data-layout-allow-overflow></div>

{voices}
      <audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="0.3"></audio>

{sfxh}    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      function mulberry32(seed) {{ return function () {{ seed |= 0; seed = (seed + 0x6D2B79F5) | 0; var t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }}; }}
      var rand = mulberry32(20261101);
      var svg = document.getElementById('bg-stars');
      for (var i = 0; i < 40; i++) {{
        var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        c.setAttribute('cx', (rand() * 1080).toFixed(1)); c.setAttribute('cy', (rand() * 1920).toFixed(1));
        c.setAttribute('r', (1.5 + rand() * 1.5).toFixed(1)); c.setAttribute('fill', '#fff'); c.setAttribute('opacity', (0.15 + rand() * 0.25).toFixed(2));
        svg.appendChild(c);
      }}
      tl.to('.blob', {{ x: '+=40', y: '-=30', duration: 18, ease: 'sine.inOut', repeat: 3, yoyo: true, stagger: 3 }}, 0);
      tl.to('#bg-stars circle', {{ opacity: '+=0.25', duration: 4, ease: 'sine.inOut', repeat: 17, yoyo: true, stagger: {{ each: 0.15, from: 'random' }} }}, 0);
      tl.set('#brand-anchor', {{ opacity: 1 }}, {St[1]});
      var CAPS = {json.dumps(capdata,ensure_ascii=False)};
      var host = document.getElementById('captions');
      CAPS.forEach(function (c, k) {{
        var el = document.createElement('div'); el.className = 'cap-chunk'; el.id = 'cap' + k;
        c.w.forEach(function (w, j) {{ var s = document.createElement('span'); s.className = 'w'; s.textContent = w[0] + (j < c.w.length - 1 ? ' ' : ''); el.appendChild(s); }});
        host.appendChild(el);
        tl.set(el, {{ opacity: 1 }}, c.s); tl.set(el, {{ opacity: 0 }}, c.e);
        c.w.forEach(function (w, j) {{ tl.to(el.children[j], {{ color: '#FF5A1F', duration: 0.1, ease: 'none' }}, w[1]); }});
      }});
      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
"""
open('index.html','w',encoding='utf-8').write(html)
print(D,St,TOTAL,len(capdata))
