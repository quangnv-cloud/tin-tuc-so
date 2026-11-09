import json, re, subprocess, os
def durations(i):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'assets/voice/line{i}.mp3']).decode().strip())
def silences(i):
    out=subprocess.run(['ffmpeg','-hide_banner','-i',f'assets/voice/line{i}.mp3','-af','silencedetect=noise=-33dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)]
    du=[float(x) for x in re.findall(r'silence_duration: ([\d.]+)',out)]
    return list(zip(st,du))
def align_line(text,i):
    words=text.split()
    D=durations(i); sil=silences(i)
    # speech span: trailing silence start
    lead=0.0
    end=D
    internal=[]
    for s,d in sil:
        if s<0.05: lead=d; continue
        if s+d>=D-0.05: end=s; continue
        internal.append((s,s+d))
    wts=[len(re.sub(r'\W','',w))+2.0 for w in words]
    tot=sum(wts)
    # predicted timeline with fixed pause allowance after punctuation
    punct=[k for k,w in enumerate(words[:-1]) if re.search(r'[,.:?]$',w)]
    PAUSE=0.28
    span=end-lead-PAUSE*len(punct)
    t=lead; pred=[]
    for k,w in enumerate(words):
        a=t; b=t+span*wts[k]/tot; pred.append([a,b]); t=b
        if k in punct: t+=PAUSE
    # anchors: punctuation boundary -> nearest unused silence
    anchors=[(lead,lead)]
    used=set()
    for k in punct:
        pend=pred[k][1]
        best=None
        for j,(s,e) in enumerate(internal):
            if j in used: continue
            if abs((s+e)/2-(pend+PAUSE/2))<0.7:
                if best is None or abs((s+e)/2-(pend+PAUSE/2))<abs((internal[best][0]+internal[best][1])/2-(pend+PAUSE/2)): best=j
        if best is not None:
            used.add(best); anchors.append((pend,internal[best][0]))
            anchors.append((pred[k+1][0],internal[best][1]))
    anchors.append((pred[-1][1],end))
    anchors.sort()
    # monotonic dedupe
    A=[]
    for p,a in anchors:
        if A and (p<=A[-1][0] or a<=A[-1][1]): continue
        A.append((p,a))
    def mp(x):
        for (p0,a0),(p1,a1) in zip(A,A[1:]):
            if p0<=x<=p1: return a0+(a1-a0)*(x-p0)/(p1-p0) if p1>p0 else a0
        return A[-1][1] if x>A[-1][0] else A[0][1]
    return [{'w':w,'s':round(mp(pred[k][0]),3),'e':round(mp(pred[k][1]),3)} for k,w in enumerate(words)], D
if __name__=='__main__':
    lines=open('SCRIPT.md',encoding='utf-8').read().strip().split('\n')
    for i,l in enumerate(lines,1):
        ws,D=align_line(l,i)
        print(i,D,' '.join(f"{w['w']}@{w['s']}" for w in ws[:12]),'...')
