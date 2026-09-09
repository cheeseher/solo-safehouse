"""Powered fabric sofa concept states and common footprint dimensions."""
from spatial import SOFA
STATES=[('closed','01 / 收起坐姿','脚托收回，靠背竖起。进出、坐下与起身，都在这个状态完成。'),('legs','02 / 抬腿放松','脚托展开、抬起，腿部获得支撑；靠背保持较直，适合看电影。'),('recline','03 / 后仰躺卧','靠背后仰、脚托继续伸展，让背、腰与双腿都能放松。')]
def section(photo,diagram,facts):
 cards=''.join(f'<figure data-sofa-frame="{i}">{photo("sofa-"+key,title+"；V01 同视角 AI 动作概念图")}<figcaption><strong>{title}</strong><p>{copy}</p></figcaption></figure>' for i,(key,title,copy) in enumerate(STATES))
 buttons=''.join(f'<button type="button" data-sofa-state="{i}" aria-pressed="{str(i==0).lower()}" aria-controls="sofa-frames">{title}</button>' for i,(_,title,_) in enumerate(STATES))
 return '<div class="practical-detail" id="sofa-demo"><p class="eyebrow">S01 / 坐下来，再慢慢躺下</p><h4>布艺的柔软，伸展开的自在。</h4><p class="detail-lede">选用宽座布艺电动伸展沙发，以可分别调节脚托与靠背的型号为选型方向。示意图演示靠近镜头的座位，另一个座位保持收起；它不需要另拼一块脚凳。</p><div class="sofa-controls" hidden>'+buttons+'<button id="sofa-play" type="button" aria-pressed="false">演示伸缩 ↔</button></div><div id="sofa-frames" class="sofa-frames">'+cards+'</div><p id="sofa-status" class="caption" aria-live="polite">三张同视角效果图展示收起、抬腿与后仰。动作演示采用状态切换，不是实拍视频或机械仿真。</p>'+diagram('sofa-envelope','S01 电动布艺沙发收起、展开占位及保留通路')+facts([
 ('能躺，先核对有效支撑','以 170cm 身高试躺，连续支撑长度目标约 1850mm、单座有效宽目标约 1050mm。让头颈、腰和脚跟有支撑；不把总深度当作可躺长度，也不默认任何型号都能放平到 180°。'),
 ('展开以后，路还在','收起占位目标约 2600 × 1050mm；最大活动区暂按 2800 × 2150mm 预留，包含侧向余量和后仰范围。平面保留一条约 1000mm 主要通路，选定型号后用完整运动包络重新核对。'),
 ('机构区域，不交给机器人','沙发底部与活动扫掠区设为机器人禁入，电源沿墙固定、避开活动件。清扫前收起并按说明书断电；需要移动时按厂家要求操作，不用加高脚来改装电动机构。')])+'<p class="caption">操作前确认脚托周围没有桌脚、线材或其他障碍；起身先收脚托。电动家具动作与维护原则参考 <a href="https://content.la-z-boy.com/productassets/productmanuals/93000536_POWER_RECLINE_OI.pdf" target="_blank" rel="noopener noreferrer">电动躺椅／沙发使用说明</a>，实际以购买型号为准。</p></div><div class="practical-detail"><p class="eyebrow">T01 / 把吃饭和躺卧都安排好</p><h4>需要台面时，把硬质餐桌移过来。</h4>'+facts([
 ('侧边放杯，不挡脚托','石质小边几放在沙发端部外侧，只放水杯、手机与遥控器。它不进入脚托前方。'),
 ('坐直吃饭，用完停回','约 650 × 400mm 的轻便硬质餐桌，优先在厨房使用。移到沙发前时沙发完全收起；吃完先清空餐具，再将桌子停回 C06 右段开放位，然后才能展开脚托。'),
 ('底座不伸进机构','餐桌独立落地，不再使用底座插入电动沙发下的方案。C06 停放位同步改为开放结构，按真实桌腿、桌高和凳子核对取放。')])+'</div>'

def render(svg_start,rect,txt,line,A):
 out=svg_start(1100,810,'S01 俯视：电动沙发最大活动区与通道；单位 mm')
 out+=txt(45,42,'S01 / 展开以后，仍然走得过去',24,'start')+txt(45,76,'与全屋平面同向 · 图左电视，图右沙发 · 概念预留，单位 mm',15,'start','dim')
 s=.13;ox=80;oy=145
 def r(x,y,w,h,c):return rect(ox+x*s,oy+(y-4400)*s,w*s,h*s,c,'#8f9b88',3)
 out+=r(0,4400,5400,4100,'#f2f3eb')+r(0,5180,400,2400,'#d2c7b6')
 out+=r(*SOFA['passage'],'#d5e7d3')
 x,y,w,h=SOFA['envelope'];out+=f'<rect x="{ox+x*s}" y="{oy+(y-4400)*s}" width="{w*s}" height="{h*s}" fill="#ddc29e" fill-opacity=".25" stroke="#a16b30" stroke-width="2" stroke-dasharray="7 5"/>'
 out+=r(*SOFA['closed'],'#bbc9b6')+r(4080,5140,200,2320,'#91a58e')
 out+=txt(ox+1300*s,oy+2100*s,'主要通路',17)+txt(ox+1300*s,oy+2350*s,'1000',17)
 out+=txt(ox+3825*s,oy+1700*s,'收起占位',17)+txt(ox+3825*s,oy+1950*s,'2600 × 1050',15)
 out+=txt(ox+3625*s,oy+3200*s,'← 脚托伸展',15)
 out+=line(ox+2550*s,oy+3500*s,ox+4700*s,oy+3500*s)+txt(ox+3625*s,oy+3750*s,'活动深度预留 2150',15)
 for i,(a,b) in enumerate([('脚托 + 靠背','最大范围按型号复核。'),('后仰与墙面','不能按收起状态贴墙摆。'),('机器人禁入','整块活动区排除清扫。'),('餐桌停放','回到厨房 C06 右段。')]):
  out+=txt(825,185+i*112,a,19,'start')+txt(825,218+i*112,b,14,'start','dim')
 out+=txt(45,727,'虚线范围 2800 × 2150 为选型预留，不是某款沙发的实测尺寸；单座动作也按完整活动区避让。',15,'start','dim')
 out+=txt(45,765,'净躺长目标 1850、单座净宽目标 1050；试躺后再定型号，机构下方不承诺机器人可进入。',15,'start','dim')+'</svg>'
 (A/'sofa-envelope.svg').write_text(out)
