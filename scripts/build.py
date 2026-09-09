"""Rebuild static HTML and vector diagrams. Python 3, standard library only."""
from pathlib import Path
import json,html
from practical_details import render_desktop,desk_section
from fixed_sofa import section as living_section,render as render_sofa
from spatial import additions,VIEWS,ROUTES,view_notes
from mobile_tv import render as render_mobile,section as mobile_section,audit_section,overlay
from skirting_details import render_details,section as skirting_section
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'dist'; A=OUT/'assets'
D=json.loads((ROOT/'scripts/design-data.json').read_text()); C=D['cabinets']; MEDIA=json.loads((ROOT/'scripts/media-meta.json').read_text())
def esc(s): return html.escape(str(s))
def svg_start(w,h,title):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><title>{esc(title)}</title><style>text{{font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;fill:#253630}}.dim{{fill:#68756d;font-size:13px}}</style><rect width="100%" height="100%" fill="#fbfcfa"/>'
def rect(x,y,w,h,fill='#e7e9e2',stroke='#8d9a90',rx=0):return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>'
def txt(x,y,t,size=14,anchor='middle',cls=''):return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{size}" class="{cls}">{esc(t)}</text>'
def line(x,y,a,b,color='#93a097',width=1,dash=''):return f'<path d="M{x:g} {y:g} L{a:g} {b:g}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'
for cid,c in C.items():
 s=min(720/c['w'],610/c['h']);x=90;y=95;w=c['w']*s;h=c['h']*s; height=max(380,h+205)
 out=svg_start(900,height,f'{cid} {c["name"]} 柜体正立面，标注单位毫米')
 out+=txt(55,35,f'{cid}  /  {c["name"]}',18,'start')+txt(55,59,'正立面 · 分区名义尺寸 / 单位 mm',13,'start','dim')
 out+=rect(x,y,w,h,'#ded7c9','#747e72')+line(x,y-20,x+w,y-20)+txt(x+w/2,y-29,str(c['w']),14)
 out+=line(x-24,y,x-24,y+h)+txt(x-35,y+h/2,str(c['h']),13,'end')
 off=0
 for n,b in enumerate(c['bays']):
  bx=x+off*s; bw=b['w']*s
  out+=rect(bx+3,y+3,bw-6,h-6,'#f6f3eb','#9a9d92')
  for i,r in enumerate(b['rows']):
   lo,hi,label=r[:3];top=y+(c['h']-hi)*s;hh=(hi-lo)*s
   out+=rect(bx+5,top,bw-10,hh,'#eef0e9' if i%2==0 else '#f9f8f2','#b5bbae')
   fs=min(14,max(10,(bw-16)/max(len(label),1)))
   out+=txt(bx+bw/2,top+hh/2+4,label,fs)
   if hh>42:out+=txt(bx+bw-8,top+14,str(hi-lo),10,'end','dim')
  for rail in b.get('rail',[]):out+=line(bx+12,y+(c['h']-rail)*s,bx+bw-12,y+(c['h']-rail)*s,'#879c8c',2)
  out+=line(bx,y+h+20,bx+bw,y+h+20)+txt(bx+bw/2,y+h+42,str(b['w']),14)
  off+=b['w']
 out+=txt(90,height-37,f'深度 {c["d"]} mm'+(f' · 柜底离地 {c["off"]} mm' if 'off' in c else ''),14,'start')
 out+=txt(90,height-14,'分区高度含结构占位；板厚、五金、管线与净空须深化，非生产下料图。',12,'start','dim')+'</svg>'
 (A/f'{cid}.svg').write_text(out)
for k,d in D['drawers'].items():
 s=min(730/d['w'],440/d['d']);out=svg_start(900,650,k+' 抽屉俯视净尺寸图')
 out+=txt(60,38,'抽屉俯视 / 内部净尺寸 · mm',18,'start')
 for x,y,w,h,label,_ in d['parts']:
  out+=rect(80+x*s,95+y*s,w*s,h*s,'#eee8dc','#9b9e8f',2)
  out+=txt(80+(x+w/2)*s,95+(y+h/2)*s-5,label,16)+txt(80+(x+w/2)*s,95+(y+h/2)*s+20,f'{w} × {h}',13,cls='dim')
 out+=txt(450,590,f'净宽 {d["w"]} × 净深 {d["d"]} · 分隔板厚 6',16)+txt(450,620,'靠近身体的一侧 ↓',14)+'</svg>'
 (A/f'drawer-{k}.svg').write_text(out)
# Floor plan uses the same millimetre model as the concept book.
for mode in ['layout','life','robot','tv']:
 out=svg_start(1200,1130,'个人安全屋概念平面 / '+mode)
 out+='<g transform="translate(60 90) scale(.098)">'
 def R(x,y,w,h,fill,stroke='#8e998e'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="14"/>'
 def T(x,y,t,size=180,fill='#314337'):return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" style="fill:{fill}">{esc(t)}</text>'
 out+=R(0,0,11000,9200,'#f5f6f0')
 for name,x,y,w,h,fc in D['rooms']:out+=R(x,y,w,h,fc)
 for x,y,w,h in D['walls']:out+=R(x,y,w,h,'#677469','#677469')
 for cid,x,y,w,h in D['furniture']:
  out+=R(x,y,w,h,'#d5cbb6')+T(x+w/2,y+h/2+60,cid,140)
 out+='<defs><marker id="viewarrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#647d92"/></marker></defs>'
 out+=additions(R,T,mode)
 if mode=='tv':out+=overlay(R,T)
 for name,x,y,w,h in [('客厅',2300,8650,0,0),('轻厨房',1900,1500,0,0),('玄关',4820,3100,0,0),('设备间',4600,1000,0,0),('工作室',8030,1120,0,0),('卧室',6750,8550,0,0),('卫浴',9640,5280,0,0)]:out+=T(x,y,name,225)
 out+=T(6050,3460,'1100',130)+T(6050,-360,'入户 ↓',230)+T(5500,-690,'内包络 11000 × 9200 mm',170)
 out+=R(900,9320,3200,430,'#dce6d2')+T(2500,9600,'露台另计',170)
 out+='<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#296b54"/></marker></defs>'
 routes=[]
 if mode=='robot':
  routes=ROUTES['robot']
  out+=f'<circle cx="7100" cy="4130" r="190" fill="#296b54"/>'+T(7330,4540,'R01',170)
  out+=T(8510,3820,'禁入',140,'#a55833')
  out+='<path d="M7200 5580 L9360 5580 L9560 4600" fill="none" stroke="#a16b30" stroke-width="36" stroke-dasharray="85 60"/>'
 elif mode=='life':routes=ROUTES['life']
 for route in routes:out+=f'<polyline points="{" ".join(str(x)+","+str(y) for x,y in route)}" fill="none" stroke="#296b54" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"/>'
 out+='</g>'+txt(60,1098,'概念布局，非实测户型。蓝箭头为视角；L 形为固定沙发占位；路线表示连接，非导航轨迹。',15,'start')+'</svg>'
 (A/f'plan-{mode}-v6.svg').write_text(out)
# Integrated dryer/cord schematic: no split compartment, no hidden live power claim.
out=svg_start(1000,670,'H01 干区挂放概念：吹风机与电线一体归位')
out+=txt(55,45,'H01  /  打开、取用、整体归位',23,'start')
out+=txt(55,76,'干区侧柜内固定挂架 · 示意不按比例',15,'start','dim')
out+=rect(85,140,355,390,'#e2dece','#a4aa9a',4)+rect(105,158,315,350,'#f4f3e9','#a4aa9a',3)
out+=rect(172,213,138,63,'#a9b7ae','#647a6d',20)+rect(214,261,43,123,'#a9b7ae','#647a6d',12)
out+=line(185,310,280,310,'#617c6b',10)
out+='<path d="M236 384 C210 435 365 460 349 390 C335 334 287 398 342 434" fill="none" stroke="#586b60" stroke-width="5" stroke-linecap="round"/>'
out+=rect(337,426,23,30,'#586b60','#586b60',3)
for y,title,body in [(185,'固定的是支架','机身可取下，常用风嘴就近放。'),(288,'机身与线缆共用一个空间','电线松绕归位，不穿过独立隔板。'),(391,'收纳状态断电','取出使用；冷却、干燥后再关门。'),(494,'不硬塞进 150mm 镜柜','位置与净尺寸，按选定机型深化。')]:
 out+=txt(490,y,title,22,'start')+txt(490,y+34,body,16,'start','dim')
out+=txt(55,620,'避开水槽与淋浴溅水范围；插座位置、保护措施与设备要求由专业人员复核。',15,'start','dim')+'</svg>'
(A/'dryer.svg').write_text(out)

render_desktop(svg_start,rect,txt,line,A)
render_details(svg_start,rect,txt,line,A)
render_sofa(svg_start,rect,txt,line,A)
render_mobile(svg_start,rect,txt,line,A,D)

def photo(name,alt,cls='',eager=False):
 name={'living':'living-mobile-v6','study':'study-v2','kitchen':'kitchen-v4','bathroom':'bathroom-v4','bedroom':'bedroom-v6','laundry':'laundry-v6'}.get(name,name)
 from struct import unpack
 # Dimensions are supplied via CSS aspect-ratio; image keeps full intrinsic proportions.
 return f'<a class="photo {cls}" href="assets/{name}.webp" data-lightbox data-caption="{esc(alt)}"><img src="assets/{name}-small.webp" srcset="assets/{name}-small.webp {MEDIA[name+"-small"][0]}w, assets/{name}.webp {MEDIA[name][0]}w" sizes="(max-width: 760px) 100vw, 1200px" alt="{esc(alt)}" width="{MEDIA[name][0]}" height="{MEDIA[name][1]}" loading="{"eager" if eager else "lazy"}" decoding="async" {"fetchpriority=high" if eager else ""}><span class="expand">查看大图 ↗</span></a>'
def diagram(name,alt):
 name=name+'-v6' if name.startswith('plan-') and not name.endswith('-v6') else name
 return f'<a class="diagram" href="assets/{name}.svg" data-lightbox data-caption="{esc(alt)}"><img src="assets/{name}.svg" alt="{esc(alt)}" loading="lazy"><span class="expand">放大图纸 ↗</span></a>'
def facts(rows):return '<dl class="facts">'+''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in rows)+'</dl>'
rooms=[
('living','01','客厅','把时间，留给一部电影。','跟随生活的屏幕、能窝进去的沙发、顺手拿到的水。放松不需要复杂的场景，也不需要填满每一面墙。',[('55 英寸级移动电视','本版以跨房间移动为优先，暂用 55 英寸级屏幕推敲；取消原 98 英寸固定大屏。C02 平时停在图左侧墙，效果图中为右侧；NAS 留在设备间，播放器随柜移动。'),('固定布艺沙发＋长贵妃榻','低靠背、深坐面与同高贵妃榻，随时可以把腿放上来。净躺区目标约 1850 × 1000mm，按 170cm 身高试躺，靠垫承托腰背。'),('清扫有明确边界','电视柜与 T02 边几移开后清扫底部，脚轮区不要求机器人钻入。沙发采用封闭落地底座，机器人沿外轮廓清扫；主要通路与贵妃榻前方保持畅通，边角人工补扫。')],'C02'),
('study','02','工作室','桌面很简单。背后很完整。','桌面只留下正在使用的设备。文件、配件、打印机和网络设备各有位置，工作开始时不用先整理半小时。',[('1800 × 900 mm 工作台','两块显示器同向朝向座位；左侧为 MacBook 立式位，右后为 Mac mini。苹果键盘、鼠标放在桌垫上，主屏与键盘对齐。'),('原装充电，更容易替换','高频快充保留 AC 插座与原装充电器，不把不可升级的固定 USB 当作唯一方案。'),('打印机有自己的使用位置','放在可移出的独立小车上，使用时移到通风位置。进出纸、开盖、换耗材所需空间一起预留。')],'C03'),
('kitchen','03','轻厨房','不爱做饭，也值得好好吃饭。','外卖是日常选择。厨房围绕冷藏、加热、简单夜宵与清洗展开，让一顿饭少几个麻烦的步骤。',[('拆包 → 加热 → 用餐 → 清理','留一块完整的落物台，微波炉附近就能取到餐具，吃完顺路进入洗碗机或垃圾收集区。'),('把空间给高频设备','大冰箱、微波炉、洗碗机，以及满足煎蛋、泡面的简单灶具。制冰、净水与设备散热按机型安排。'),('柜门不能代替散热条件','微波炉开放运行或采用明确支持嵌入的型号；冰箱检修与散热间距不被装饰封板吃掉。')],'C05'),
('bedroom','04','卧室','睡眠，应该足够柔软。','床、软靠背、遮光和安静。能随手放下手机，也能随时结束一天。没有为“主卧应该有”而增加的陈设。',[('1800 × 2000 mm 床垫','作为本方案假设。软硬以实际试睡为准，床架和靠背外廓另计，不把床垫尺寸当作家具总尺寸。'),('降低夜间干扰','网络和存储设备放在独立区域，遮光同时考虑窗帘漏光边缘；床边照明可独立关闭。'),('穿一天、洗一次的衣物循环','常穿、待洗、已洗待归位分开。高频衣物处在容易取到的位置，顶部存放换季用品。')],'C04'),
('bathroom','05','卫浴','开阔，是每天都能感受到的。','洗漱、马桶与浴缸共享开阔空间，仅将淋浴隔开。少一道隔断，少一点拥挤；该隔开的水汽仍然认真处理。',[('1200 × 1200 mm 淋浴区','独立隔水；玻璃、挡水与地面找坡一起设计。效果图的通透感不能替代可靠排水。'),('1600 mm 洗漱台','常用护理品收在镜后，台面留给正在使用的物品。抽屉需绕开排水管，检修口必须能打开。'),('1700 × 800 mm 浴缸外廓','以 170 cm 身高作为本方案参考，舒适度仍要看内腔、靠背角度和跨入高度，选购前试坐。')],'C07'),
('laundry','06','家政区','穿过一次，洗护一次。','独立洗衣机和热泵烘干机，让洗护成为一条短而稳定的流程。机器人有自己的家，但出门不需要你开柜门。',[('脏衣 → 洗烘 → 归位','脏衣篮可移出，洗涤剂就近存放，折衣和暂放区与脏衣区分开，减少反复搬运。'),('洗烘叠放先核对兼容性','使用合适的叠放件；上方滤网、下方排水与电源都能维护，振动和检修不能只靠一张效果图判断。'),('R01 常开通道','基站开口名义宽 800、高 550 mm；前方以 1200 mm 净空为设计目标。按最终基站确认，尤其留意上盖和水箱操作。')],'C08'),
]
roomhtml=''
for image,num,name,title,desc,rows,cid in rooms:
 detail=desk_section(diagram,facts) if image=='study' else living_section(photo,diagram,facts)+mobile_section(photo,diagram,facts) if image=='living' else ''
 view=next(v for v in VIEWS if v[1]==image)
 roomhtml+=f'<article class="room" id="room-{image}"><div class="room-intro"><p class="eyebrow">{num} / {name}</p><h3>{title}</h3><p class="lede">{desc}</p></div>{photo(image,name+"空间概念效果图；尺寸与结构以图纸为准")}<div class="room-bottom"><p class="view-caption"><b>{view[0]}</b> {view[-1]} <a href="#plan">对照平面 ↗</a></p>{facts(rows)}<a class="textlink" href="#cab-{cid}">查看{name}柜体分层 <span>↗</span></a>{detail}</div></article>'
notes={
'C01':('出门与回家的动作，在同一处结束。','每日鞋位与随手放置台靠近入口；背包就近归位。快递开箱工具集中存放，包装及时清走，顶部只放低频用品。'),
'C02':('服务观影，也服务清扫。','柜体本体 1100 × 360 × 550mm，轮组占高目标约 100mm；屏幕支架与底盘另计。左半收遥控器与播放器，右半让给支架、收线和检修；柜体分层图不是承重结构图。'),
'C03':('先按任务分类，再按物品分类。','待处理、近期文件、长期归档分开。数码配件采用浅抽，重要原件上锁；打印机移出使用，不在封闭柜里运行。'),
'C04':('常穿近手，换季上移。','四段各 700 mm：长挂、双层短挂、折叠浅抽、旅行弹性位。挂衣净高、衣架深度和柜门开启需结合实物复核。'),
'C05':('常用的餐具与夜宵，少走一步。','水槽、垃圾桶和洗碗机集中；餐具用浅抽、锅具用深抽。下水、净水和洗碗机管线占位后再核算真实净容量。'),
'C05A':('先选设备，再定最终开口。','冰箱与微波炉分区，保留取放、散热与检修空间。图中尺寸为概念占位，不可作为任何具体型号的安装尺寸。'),
'C06':('接水与泡茶，一次准备好。','水杯、茶具和茶叶就近放置；净水阀门独立检修。右段改为 700mm 名义宽开放位，净宽扣除板厚后核对餐桌与凳子；不再作为满格备品柜。接水台做好接滴与清洁，避免水路经过难以维护的封闭空间。'),
'C07':('让台面留下可以使用的空白。','毛巾和备品在下部，常用护理品在上部。台盆下抽屉绕管；原吹风机抽屉改为洗漱备品，吹风机移到 H01 挂放位。'),
'C07M':('镜后只收纳适合这个深度的物品。','深 150 mm 的镜柜优先存放护理用品；不用它硬塞吹风机。搁板净高、瓶身尺寸和镜门铰链的占位都要检查。'),
'C08':('清洁设备藏起来，使用入口露出来。','洗烘 800＋基站 800＋工具 600 mm 三段。基站地面齐平；柜门、踢脚、管线不可阻挡机器人。实际净宽会扣除板厚。'),
'C09':('运行安静，也能随时检修。','网络与 NAS 分区供电。UPS 优先保网并支持 NAS 安全关机；散热、噪声、线材弯曲和维护净空均需按设备核对。')}
cabhtml=''
for cid,c in C.items():
 a,b=notes[cid]
 cabhtml+=f'<details class="cabinet" id="cab-{cid}"><summary><span class="cab-no">{cid}</span><span><strong>{c["name"]}</strong><small>{c["w"]} × {c["h"]} × {c["d"]} mm</small></span><span class="plus" aria-hidden="true">＋</span></summary><div class="cab-body"><h4>{a}</h4><p>{b}</p>{diagram(cid,c["name"]+"正立面与分层尺寸")}<ul class="bay-list">'+''.join(f'<li><strong>第{i+1}段 · {bay["w"]} mm</strong><span>'+ '、'.join(esc(r[2]) for r in reversed(bay['rows']))+'</span></li>' for i,bay in enumerate(c['bays']))+'</ul></div></details>'
drawerhtml=''
for name,title,copy in [('electronic','数码配件 / 按用途分','短线、充电器、读卡器与长线分开。正在使用的线材留在设备处，抽屉只接纳备用和待取用物品。'),('clothes','贴身衣物 / 一眼找得到','前后两排、三列分格。按个人衣物数量调整，不为追求填满每一格而增加物品。'),('tea','功夫茶具 / 一次取齐','杯、盖碗、茶罐、茶巾分区。按常用茶具实际外廓复核，使用后清洁并干燥，再放回抽屉。')]:
 pic={'electronic':'electronics','clothes':'clothes','tea':'tea'}[name]
 drawerhtml+=f'<article class="drawer"><h3>{title}</h3><p>{copy}</p><div class="drawer-pair">{photo(pic,title+"收纳氛围参考，精确分隔以右侧或下方图纸为准")}{diagram("drawer-"+name,title+"俯视净尺寸")}</div></article>'
body=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#f5f6f2"><title>个人安全屋 SOLO — 把生活安排好，把自己还给自己</title><meta name="description" content="一个人的住宅参考设计。围绕外卖与轻食、睡眠、工作、观影和自动清洁，探索少打理、易归位的空间。包含空间效果图、柜体分层、抽屉尺寸与清扫动线。"><meta property="og:title" content="个人安全屋 SOLO · 把自己还给自己"><meta property="og:description" content="一个围绕独居生活设计的空间：少一些打理，多一些自在。探索空间、收纳和动线。"><meta property="og:type" content="website"><meta property="og:locale" content="zh_CN"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><script src="app.js" defer></script></head><body>
<a class="skip" href="#main">跳到正文</a><header class="site-header"><a class="wordmark" href="#top" aria-label="个人安全屋首页">SOLO<span>个人安全屋</span></a><nav aria-label="主要章节"><a href="#idea">理念</a><a href="#plan">布局</a><a href="#spaces">空间</a><a href="#storage">收纳</a><a href="#skirting">收边</a><a href="#practice">落地</a></nav></header>
<main id="main"><section class="hero" id="top"><div class="hero-copy"><p class="eyebrow">A PRIVATE PLACE TO LIVE</p><h1>把生活安排好。<br><span>把自己还给自己。</span></h1><p>个人安全屋。一个围绕独居生活设计的空间。<br>少一些打理，多一些自在。</p><a class="hero-link" href="#idea">走进安全屋 <span>↓</span></a></div>{photo('living','大落地窗、浅木地板与柔软沙发构成的客厅概念效果图','hero-photo',True)}<div class="hero-foot"><span>SOLO / 独居住宅参考设计</span><span>概念方案 · 持续推敲</span></div></section>
<section class="section manifesto" id="idea"><div class="section-label"><span>01 / 设计理念</span><span>LESS TO MANAGE. MORE TO LIVE.</span></div><div class="manifesto-head"><h2>空间不必填满。<br>生活可以完整。</h2><div><p class="large-copy">一个人的居所，可以从自己的生活出发。</p><p>不必为了低频待客多留一间房，也不必用装饰证明生活的丰盛。睡得好、吃得方便、东西好找、地面好清洁，这些真实发生的事情，才值得优先安排。</p><p>这里的“安全”，是安静、私密、可控和低负担。它不承诺某种防御能力，而是让你回到一个熟悉、清净、无需勉强自己的地方。</p></div></div><div class="principles"><article><span>01</span><h3>少做不想做的事。</h3><p>喜欢外卖，就把加热、饮水与清理安排好。不喜欢打扫，就从布局开始为机器人留路。</p></article><article><span>02</span><h3>让归位比堆放更顺手。</h3><p>物品靠近使用地点，常用的够得着，备用的藏起来。收纳不靠每天重新整理来维持。</p></article><article><span>03</span><h3>把舒适放在前面。</h3><p>一张舒服的床、一个足够深的桌面、一处安心看电影的位置。极简的，是生活负担。</p></article></div><p class="editor-note">这是面向偏爱独居、外卖与低家务负担的一种生活提案。它不代表所有人的选择，也不要求你拥有一样的房子。</p></section>
<section class="plan-section section" id="plan"><div class="section-label"><span>02 / 全屋布局</span><span>EVERYDAY, CONNECTED.</span></div><div class="section-head"><h2>先安排生活，<br>再划分房间。</h2><p>以约 98.4㎡ 室内净地面概念方案为载体。休息与工作分区，家政靠近衣物循环，设备独立安放。重要的不是面积数字，而是每段路为什么存在。</p></div><div class="plan-workspace"><div class="plan-main"><div class="tabs" role="tablist" aria-label="平面图层"><button id="tab-layout" role="tab" aria-controls="plan-panel" aria-selected="true" data-plan="layout">全屋布局</button><button id="tab-life" role="tab" aria-controls="plan-panel" aria-selected="false" tabindex="-1" data-plan="life">生活动线</button><button id="tab-robot" role="tab" aria-controls="plan-panel" aria-selected="false" tabindex="-1" data-plan="robot">机器人清扫</button><button id="tab-tv" role="tab" aria-controls="plan-panel" aria-selected="false" tabindex="-1" data-plan="tv">电视移动</button></div><div id="plan-panel" role="tabpanel" aria-labelledby="tab-layout">{diagram('plan-layout','安全屋概念平面图：客厅、厨房、工作室、卧室、卫浴和设备家政位置')}</div><p id="plan-caption" class="caption" aria-live="polite">布局图 / 柜号与下方收纳图一一对应，点图可放大。</p></div><aside class="plan-notes"><span class="big-number">98.4<small>㎡</small></span><p>概念室内净地面<br>包含柜体占地 · 露台另计</p><div class="rule"></div><h3>生活的三条短路径</h3><ol><li><strong>回家 → 放下 → 放松</strong><span>鞋、包与快递工具在玄关归位，外卖顺路进入加热与用餐区域。</span></li><li><strong>脱衣 → 洗烘 → 衣柜</strong><span>脏衣与干净待归位衣物分开，家政靠近卧室，减少搬运。</span></li><li><strong>基站 → 清扫 → 回充</strong><span>设备和淋浴区不纳入自动清扫；卫浴干区仅在地面干燥、无积水时开放。</span></li></ol><p class="caption">内包络 11.0 × 9.2m，扣除概念内墙约 2.77㎡。不等同于房产证建筑面积，也不表示必须购买这个面积。</p></aside></div><noscript><p>图层切换需要 JavaScript。也可以直接打开 <a href="assets/plan-life-v6.svg">生活动线图</a> 或 <a href="assets/plan-robot-v6.svg">清扫连接图</a>。</p></noscript>{view_notes()}{audit_section()}</section>
<section class="section spaces" id="spaces"><div class="section-label"><span>03 / 空间体验</span><span>A DAY, AT YOUR OWN PACE.</span></div><h2>一天的日常，<br>都有舒服的位置。</h2><p class="section-deck">以下为 AI 生成的概念效果图，表达材质、光线与使用氛围。柜体、家具与开口尺寸以图纸为准；图片不作为施工依据。</p><nav class="room-nav" aria-label="空间目录">{''.join(f'<a href="#room-{r[0]}">{r[2]}</a>' for r in rooms)}</nav>{roomhtml}<div class="quiet-grid"><article>{photo('entry','玄关收纳概念效果图')}<h3>进门，就能放下。</h3><p>鞋、包和钥匙，各有顺路的归位点。入口不承担长期堆积快递的任务。</p><a href="#cab-C01" class="textlink">玄关柜 C01 ↗</a></article><article>{photo('terrace','小露台概念效果图')}<h3>留一个透气的角落。</h3><p>一张舒服的椅子，一处可以放杯的小台面。低频使用的露台，也可以足够简单。</p><p class="caption">室外另计；如用于吸烟，需避免烟气回流或影响邻居，室内通风与过滤不能消除二手烟风险。</p></article><article>{photo('equipment','网络与 NAS 独立设备区概念效果图')}<h3>设备工作，生活安静。</h3><p>网络、8 盘位 NAS 与供电保护集中维护。独立空间仍需处理散热、风道与噪声。</p><a href="#cab-C09" class="textlink">设备架 C09 ↗</a></article></div></section>
<section class="section storage" id="storage"><div class="section-label"><span>04 / 收纳系统</span><span>A PLACE FOR WHAT YOU USE.</span></div><div class="section-head"><h2>收起来之前，<br>先想想怎么拿。</h2><p>让高频动作更短，让低频物品更安静。每一组柜体都说明放什么、怎么分层，以及使用时需要留出的空间。</p></div><div class="storage-principles"><p><b>就近</b>东西跟着使用地点走。</p><p><b>浅放</b>常用小物尽量一眼看全。</p><p><b>留余</b>为未来变化保留弹性。</p></div><div class="storage-gallery">{photo('wardrobe','衣柜内部挂衣、浅抽和被褥收纳概念图')}{photo('files','工作文件与资料归档概念图')}</div><div class="drawing-intro"><h3>柜体图册</h3><p>展开查看内部结构。尺寸顺序为宽 × 高 × 深，单位 mm。所有柜号与布局图对应；其中 C05A 是厨房设备柜，C07M 是镜柜。</p></div><div class="cabinet-list">{cabhtml}</div><div class="drawers"><p class="eyebrow">DRAWER DETAILS / 抽屉的内部</p><h2>打开以后，<br>也不需要翻找。</h2>{drawerhtml}</div><article class="dryer-feature" id="dryer"><p class="eyebrow">H01 / 使用动作的修正</p><h2>吹风机和它的线，<br>本来就是一件东西。</h2><p class="lede">固定的是位置，不是机身。干区侧柜内设置挂架，取下即可使用；机身、线缆和常用风嘴在同一个区域归位。</p>{diagram('dryer','吹风机与电线在同一区域整体归位的干区挂放方案')}<div class="dryer-notes"><p><strong>收纳不增加拆分动作。</strong>电线不经过狭窄的独立隔格，也不拉紧缠绕。柜门不会夹住线材。</p><p><strong>隐藏不等于封死。</strong>使用时取出，归位时断电并等待冷却、干燥。不采用在密闭柜内持续通电的方式。</p><p><strong>按实物深化。</strong>H01 是新增挂放概念，最终位置与净尺寸待机型确定；不沿用原镜柜 150 mm 深度。</p></div></article></section>
{skirting_section(photo,diagram,facts)}
<section class="section systems" id="systems"><div class="section-label"><span>06 / 看不见的体验</span><span>QUIETLY WORKING.</span></div><div class="section-head"><h2>少一点操心，<br>来自多一点预先考虑。</h2><p>智能与设备的价值，是让生活稳定地运转。手动操作、检修路径和故障时的退路，同样属于设计。</p></div><div class="system-grid"><article><span>LIGHT</span><h3>均匀明亮，局部可控。</h3><p>采用多点照明补足工作面与走道，避免只有一盏主灯，也避免为了氛围把全屋做暗。夜间床边与路径照明独立控制。</p></article><article><span>AIR</span><h3>温度、噪声和空气一起考虑。</h3><p>空调送风避开床头与长期坐姿，新风与排风分别解决具体问题。设备间的热与噪声不直接排向卧室。</p></article><article><span>POWER</span><h3>断网之后，基本功能仍能用。</h3><p>灯光、门锁与窗帘保留合适的本地或手动操作。网络 UPS 与 NAS 安全关机分工，备用蜂窝也不承诺外部网络永远可用。</p></article><article><span>WATER</span><h3>用水方便，维护也方便。</h3><p>直饮、制冰、洗烘和机器人水路集中规划。阀门、滤芯、排水与防漏措施保持可达，不藏在拆柜才能处理的位置。</p></article></div><div class="robot-check"><h3>扫地机器人，先给它一条能走的路。</h3>{facts([('通行','门槛、地毯边缘、落地线材与柜门一起检查。路线畅通比隐藏基站更重要。'),('进入','家具最低横撑与裙边决定实际净高。机器人机身高度、直径和越障能力按机型复核。'),('维护','尘袋、清洗盘、污水处理和故障拖出空间都要留。基站上方的柜板不能阻挡维护。'),('边界','不吸液体、热烟灰与危险杂物。淋浴区、露台与设备间不纳入此方案自动清扫。')])}</div></section>
<section class="section practice" id="practice"><div class="section-label"><span>07 / 把原则带回自己的房子</span><span>MAKE IT YOURS.</span></div><h2>不必复制这个户型。<br>可以借走它的思路。</h2><div class="practice-grid"><article><span>01</span><h3>先写一天，再画一间房。</h3><p>记录回家、吃饭、工作、洗衣和睡前的动作。把最常重复、最不愿意做的事圈出来，它们应该优先被设计解决。</p></article><article><span>02</span><h3>先确定常用物，再确定柜子。</h3><p>量衣架、锅具、行李箱和常用设备。整理存量，再决定容量；不是先装满墙的柜，再寻找要放进去的东西。</p></article><article><span>03</span><h3>把预算给每天感受到的地方。</h3><p>床与遮光、静音、洗烘、工作台、洗浴、网络和清洁设备优先。影音和智能配置按使用频率逐步增加。</p></article><article><span>04</span><h3>在施工之前，让假设变成实测。</h3><p>实测墙柱门窗与管井，确认设备型号，复核通道、柜门和检修净空。结构、防水、电气与消防条件由专业人员深化。</p></article></div><details class="method"><summary>关于这份参考设计与资料依据 <span aria-hidden="true">＋</span></summary><div><p>这是面向独居生活的概念住宅研究，不是实际项目的施工图。约 98.4㎡ 室内净地面、1.8m 床垫、170cm 使用者身高与所有柜体尺寸均为本方案条件。尚未确定的设备品牌、型号、价格与工程条件不作确定承诺。</p><p>写实图由 AI 生成；为表达光线、材质和生活氛围，可能与尺寸图存在差异。矢量图由统一尺寸数据绘制，柜体分区名义高度仍需扣除板材、五金和安装占位；抽屉图标注的是内部分隔净尺寸。</p><p>设备要求参考 <a href="https://support.roborock.com/hc/en-us/article_attachments/48931711307801" target="_blank" rel="noopener noreferrer">Roborock 自动上下水版安装说明</a>、<a href="https://support.hp.com/hk-zh/document/c03261414" target="_blank" rel="noopener noreferrer">HP 打印机安装环境说明</a>；室内吸烟相关说明参考 <a href="https://www.epa.gov/indoor-air-quality-iaq/secondhand-tobacco-smoke-and-indoor-air-quality" target="_blank" rel="noopener noreferrer">EPA 室内空气资料</a>。具体安装以购买型号的最新版说明和现场条件为准。</p></div></details></section>
<section class="closing">{photo('bedroom','安静卧室的概念效果图')}<div><p class="eyebrow">YOUR PLACE. YOUR PACE.</p><h2>回到这里，<br>就做自己。</h2><p>一个人的世界。物品有位置，生活有余地。</p><a href="#top" class="textlink">回到开头 ↑</a></div></section></main><footer><a class="wordmark" href="#top">SOLO<span>个人安全屋</span></a><p>独居住宅参考设计 · 概念版 2026.09</p></footer>
<dialog id="lightbox" aria-labelledby="lightbox-caption"><div class="lightbox-toolbar"><p id="lightbox-caption"></p><button id="zoom-toggle" type="button">放大细节</button><a id="lightbox-original" target="_blank" rel="noopener">原图 ↗</a><button id="lightbox-close" aria-label="关闭大图">关闭 ×</button></div><div class="lightbox-stage"><img id="lightbox-image" alt=""></div><p class="lightbox-help">图纸可放大后拖动查看；也可打开原图，使用浏览器双指缩放。</p></dialog></body></html>'''
(OUT/'index.html').write_text(body)
(A/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#253e32"/><path d="M43 19H28c-14 0-14 13 0 13h8c14 0 14 13 0 13H20" fill="none" stroke="#f4f5ec" stroke-width="5"/></svg>')
print('Generated HTML, 11 cabinet diagrams, 3 drawers, 4 plans and integrated dryer diagram.')
