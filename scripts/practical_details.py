"""Dimensioned desk layout and copy shared by the practical-living revision."""
DESK={
 'width':1800,'depth':900,
 'items':[
  {'id':'laptop','name':'MacBook 立式位','x':25,'y':105,'w':100,'d':280,'color':'#e3e7e4'},
  {'id':'secondary','name':'副屏 / 含底座占位','x':150,'y':100,'w':610,'d':280,'color':'#d8dfd9'},
  {'id':'primary','name':'主屏 / 含底座占位','x':790,'y':100,'w':610,'d':280,'color':'#d8dfd9'},
  {'id':'mini','name':'Mac mini 预留','x':1530,'y':105,'w':220,'d':220,'color':'#e3e7e4'},
  {'id':'mat','name':'桌垫 800 × 400','x':700,'y':440,'w':800,'d':400,'color':'#dedfd4'},
  {'id':'keyboard','name':'苹果键盘','x':885,'y':565,'w':420,'d':130,'color':'#fafbf7'},
  {'id':'mouse','name':'苹果鼠标','x':1350,'y':570,'w':80,'d':130,'color':'#fafbf7'},
 ]}
def render_desktop(svg_start,rect,txt,line,A):
 s=.54;ox=70;oy=150
 out=svg_start(1120,875,'1800 × 900mm 桌面俯视布置；双屏同向、MacBook、Mac mini、苹果键鼠与桌垫')
 out+=txt(55,42,'D10 / 一个人的完整工作台',24,'start')+txt(55,77,'俯视占位 · 单位 mm · 屏幕均朝向下方的同一座位',16,'start','dim')
 out+=rect(ox,oy,1800*s,900*s,'#e6ddcb','#859285',4)
 out+=line(ox,oy-30,ox+1800*s,oy-30)+txt(ox+900*s,oy-42,'1800',15)
 out+=line(ox-23,oy,ox-23,oy+900*s)+txt(ox-30,oy+450*s,'900',15,'end')
 out+=rect(ox+170*s,oy+20*s,1400*s,45*s,'#cbd5c8','#889b88',3)
 out+=txt(ox+870*s,oy+43*s+5,'后沿可检修理线区',13)
 for i in DESK['items']:
  x=ox+i['x']*s;y=oy+i['y']*s;w=i['w']*s;h=i['d']*s
  out+=rect(x,y,w,h,i['color'],'#81917e',4)
  if i['id']=='laptop':
   out+=txt(x+w/2,y+h/2-12,'MacBook',11)+txt(x+w/2,y+h/2+9,'立式位',12)
  elif i['id']=='mini':
   out+=txt(x+w/2,y+h/2-3,'Mac mini',14)+txt(x+w/2,y+h/2+20,'预留位',13)
  elif i['id']=='mat':out+=txt(x+w/2,y+h-15,i['name'],16)
  elif i['id']=='mouse':out+=txt(x+w/2,y+h+21,'鼠标',14)
  else:
   out+=txt(x+w/2,y+h/2+4,i['name'],16)
  if i['id'] in ['primary','secondary']:
   out+=line(x+8,y+30,x+w-8,y+30,'#45634e',5)
   out+=txt(x+w/2,y+h-15,'屏幕正面 ↓',15)
 for x in [75,455,1095,1620]:out+=line(ox+x*s,oy+100*s,ox+x*s,oy+65*s,'#6a8470',2,'4 3')
 # Sitting centre lines up with primary screen and keyboard centre.
 cx=ox+1095*s;front=oy+900*s
 out+=line(cx,oy+385*s,cx,oy+430*s,'#2f6a4d',2,'5 4')+line(cx,front+5,cx,front+35,'#2f6a4d',2)
 out+=txt(cx,front+62,'座位中心 / 对齐主屏与键盘',18)
 out+=txt(55,757,'显示器先以两块 27 英寸级别占位；具体外廓、底座或支架需按实物复核。',16,'start','dim')
 out+=txt(55,790,'MacBook 默认合盖停放；需要打开使用时，移出立式位，不在夹持状态强行开盖。',16,'start','dim')
 out+=txt(55,823,'各设备矩形为布置预留，不是产品标称尺寸。桌垫下方不压电源或发热设备。',16,'start','dim')
 out+='</svg>';(A/'desk-layout.svg').write_text(out)

def desk_section(diagram,facts):
 return '<div class="practical-detail" id="desk-details"><p class="eyebrow">D10 / 桌面布置与使用</p><h4>两台电脑，共用一个清楚的工作位置。</h4><p class="detail-lede">以 Mac mini 作为常驻主机，MacBook 放在左侧立式位，便于带走。两块显示器都朝向座位；主屏和键盘对齐，副屏略向内转，不需要扭着身体工作。</p>'+diagram('desk-layout','桌面俯视图：双屏同向、左侧 MacBook、右后 Mac mini、桌垫与苹果键鼠')+facts([
 ('桌面不是设备堆放区','桌垫按 800 × 400 mm 预留，苹果键盘与鼠标放在其上，鼠标右侧保留活动范围；前沿不放充电器和杂物。'),
 ('两台电脑，不假定自动切换','日常先让 Mac mini 驱动双屏。MacBook 接入时，按实际机型与显示器接口安排换线或兼容的切换设备；键鼠连接也单独确认。'),
 ('线藏起来，也能取出来','供电和视频线沿后沿进入可打开的线槽，留合理余量。Mac mini 保持通风、接口可达；桌下不悬挂线团，不挤占膝腿空间。')])+'<p class="caption">双屏数量、分辨率、刷新率和合盖外接条件取决于实际 Mac 型号与连接方式，选型前核对 <a href="https://support.apple.com/en-us/102555" target="_blank" rel="noopener noreferrer">Apple 外接显示器说明</a>。当前图示为桌面占位方案，不默认任何一根扩展坞线都能实现双屏和键鼠切换。</p></div>'
