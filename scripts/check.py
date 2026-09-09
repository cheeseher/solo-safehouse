"""Bounded validation of site assets, anchors, dimensions and private content."""
from pathlib import Path
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
import json
P=Path(__file__).resolve().parents[1];root=P/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.tags=[]
 def handle_starttag(self,t,a):self.tags.append((t,dict(a)))
s=Page();s.feed((root/'index.html').read_text());ids=[a['id'] for _,a in s.tags if 'id'in a]
assert len(ids)==len(set(ids)), 'Duplicate anchors'
for t,a in s.tags:
 for key in ('src','href'):
  v=a.get(key,'')
  if not v or v.startswith(('http:','https:')):continue
  assert v[1:] in ids if v.startswith('#') else (root/v).is_file(),v
 if t=='img':assert a.get('alt') or a.get('id')=='lightbox-image'
 if t=='script':assert not a.get('src','').startswith('http')
for f in (root/'assets').glob('*.svg'):ET.parse(f)
D=json.loads((P/'scripts/design-data.json').read_text())
for key,c in D['cabinets'].items():
 assert sum(b['w'] for b in c['bays'])==c['w'],key
 for b in c['bays']:
  for r in b['rows']:assert 0<=r[0]<r[1]<=c['h']
for d in D['drawers'].values():
 for i,(x,y,w,h,*_) in enumerate(d['parts']):
  assert x>=0 and y>=0 and x+w<=d['w'] and y+h<=d['d']
  for X,Y,W,H,*_ in d['parts'][i+1:]:assert x+w<=X or X+W<=x or y+h<=Y or Y+H<=y
assert sum(t=='h1' for t,_ in s.tags)==1
assert all('chatgpt.com/share' not in f.read_text() for f in root.rglob('*') if f.suffix in {'.html','.js','.css','.svg'})
print('PASS: local links, unique anchors, image alt text, SVG XML, cabinet widths, drawer bounds/non-overlap, no original private chat link.')
print('Static payload:',round(sum(f.stat().st_size for f in root.rglob('*') if f.is_file())/1e6,2),'MB')
