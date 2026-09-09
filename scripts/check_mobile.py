"""Concept-only swept envelope verification. No operator, doors or structural certification."""
from pathlib import Path
import math,json
from spatial import SOFA,FIXTURES
D=json.loads((Path(__file__).parent/'design-data.json').read_text())
obs=D['walls']+[f[1:] for f in D['furniture'] if f[0]!='C02']+[list(f[1:]) for f in FIXTURES]+[SOFA['body'],SOFA['chaise']]
obs=[(x+w/2,y+h/2,w/2,h/2) for x,y,w,h in obs]
cache={}
def valid(q):
 if q in cache:return cache[q]
 x,y,a=q;c=abs(math.cos(a*math.pi/12));s=abs(math.sin(a*math.pi/12));cx=math.cos(a*math.pi/12);sy=math.sin(a*math.pi/12);hw=625;hh=300
 ex=hw*c+hh*s;ey=hw*s+hh*c
 ok=x-ex>0 and x+ex<11000 and y-ey>0 and y+ey<9200
 if ok:
  for ox,oy,w,h in obs:
   dx=ox-x;dy=oy-y
   if abs(dx)<ex+w+15 and abs(dy)<ey+h+15 and abs(dx*cx+dy*sy)<hw+w*c+h*s+15 and abs(-dx*sy+dy*cx)<hh+w*s+h*c+15:ok=False;break
 cache[q]=ok;return ok

r=json.loads((Path(__file__).parent/'tv-routes-v6.json').read_text());n=0
for name,p in r.items():
 for q,b in zip(p,p[1:]):
  da=(b[2]-q[2]+6)%12-6
  steps=max(1,math.ceil(max(abs(b[0]-q[0])/10,abs(b[1]-q[1])/10,abs(da)*15)))
  for i in range(steps+1):
   t=i/steps;s=(q[0]+(b[0]-q[0])*t,q[1]+(b[1]-q[1])*t,(q[2]+da*t)%12)
   assert valid(s),(name,s)
   n+=1
print('PASS:',n,'sampled poses, 1250 x 600 mm envelope; 15 mm obstacle margin; concept only')
