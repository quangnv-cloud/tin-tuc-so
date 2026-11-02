import json,os,sys,subprocess
i=int(sys.argv[1]); t=open('SCRIPT.md',encoding='utf-8').read().strip().split('\n')[i-1]
d={"app_id":os.environ["VBEE_APP_ID"],"input_text":t,"voice_code":"hn_male_minhquan_yt-stable","audio_type":"mp3","bitrate":128,"speed_rate":1.09,"response_type":"direct"}
json.dump(d,open(f'/tmp/claude-0/s/line{i}.json','w',encoding='utf-8'),ensure_ascii=False)
r=subprocess.run(['curl','-s','--max-time','90','-X','POST','https://vbee.vn/api/v1/tts','-H','Authorization: Bearer '+os.environ["VBEE_TOKEN"],'-H','Content-Type: application/json; charset=utf-8','--data-binary',f'@/tmp/claude-0/s/line{i}.json'],capture_output=True,text=True).stdout
j=json.loads(r)
if j.get('status')!=1: print(i,'ERR',{k:v for k,v in j.items() if k!='result'}); sys.exit(1)
subprocess.run(['curl','-sL','-o',f'assets/voice/line{i}.mp3',j['result']['audio_link']],check=True)
print(i,'ok')
