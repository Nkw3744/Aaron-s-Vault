from pathlib import Path
import re,subprocess,json,math
root=Path('/home/aaron/projects/thermo-past-exam-resource')
files=['test1.tex','test2.tex','test3.tex','test4.tex','test2025.tex','endyear-stretch.tex']
expected=[4,4,4,4,3,3]
r={'chapters':{},'errors':[]}
alltext=''
for fn,n in zip(files,expected):
 t=(root/'chapters'/fn).read_text(); alltext+=t
 q=t.count('Rewritten question.')
 a=t.count('\\textbf{Assumptions.}')
 s=len(re.findall(r'\\textbf\{System (?:and boundary|type / boundary)\.\}',t))
 r['chapters'][fn]={'questions':q,'assumptions':a,'systems':s,'open_math':t.count('\\['),'close_math':t.count('\\]')}
 if (q,a,s)!=(n,n,n): r['errors'].append(f'coverage {fn}: {(q,a,s)} expected {n}')
 if t.count('\\[')!=t.count('\\]'): r['errors'].append('display imbalance '+fn)
 if re.search(r'TODO|PLACEHOLDER|not recoverable|source-limited|see source table',t,re.I): r['errors'].append('placeholder language '+fn)
refs=re.findall(r'\\questionfigure\{([^}]+)\}',alltext)
missing=[x for x in refs if not (root/'question-images'/x).exists()]
r['figures']={'references':len(refs),'files':len(list((root/'question-images').glob('*.png'))),'missing':missing}
if missing or len(refs)!=14:r['errors'].append('figure coverage')
pdf=root/'build/Thermodynamics-Past-Exam-Booklet-Weeks-1-6.pdf'
info=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
r['pdf']={'pages':int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1)),'a4':'595.28 x 841.89' in info,'encrypted':'Encrypted:       no' in info,'bytes':pdf.stat().st_size}
if r['pdf']['pages']!=30 or not r['pdf']['a4']:r['errors'].append('pdf metadata')
# Independent arithmetic regressions for representative numeric questions.
calc={}
v1=.001073+.25*(.60582-.001073); V1=2*v1; W=500*(2*V1-V1); u1=561.11+.25*1982.1; x3=(2*v1-.001093)/(.37483-.001093); u3=639.54+x3*1921.2; Q=W+2*(u3-u1)
calc['test4_q2']=[V1,W,Q]
calc['test3_q3_current']=1008.56e3/(230*360)
calc['test3_q4_net']=1500*(.0362-.0181)+(1500*.0181-652.9*.0362)/(1-1.2)
calc['2025_q1']=[10*3*(75-25),10*3*(75-25)/20,10*3*(80-75)]
calc['endyear_p10_cop']=(5.30-1.23-.45)/1.23
checks=[abs(V1-.30452)<5e-4,abs(W-152.26)<.3,abs(Q-2437.6)<3,abs(calc['test3_q3_current']-12.18)<.02,abs(calc['test3_q4_net']-9.6)<.2,all(abs(a-b)<.2 for a,b in zip(calc['2025_q1'],[1500,75,150])),abs(calc['endyear_p10_cop']-2.94)<.02]
r['arithmetic']={'values':calc,'passed':all(checks)}
if not all(checks):r['errors'].append('arithmetic regression')
r['status']='PASS' if not r['errors'] else 'FAIL'
(root/'verification/verification-report.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='PASS' else 1)
