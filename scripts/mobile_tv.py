"""Mobile media concept, dimensions and explicit render/plan correspondence."""
import json
from pathlib import Path

def section(photo,diagram,facts):
 return '<div class="practical-detail mobile-feature" id="mobile-tv"><p class="eyebrow">C02 / 屏幕跟着生活走</p><h4>墙面留白。电视，推到需要的地方。</h4><p class="detail-lede">客厅看电影，吃饭时继续看，睡前推到床尾。以跨房间移动为优先，本版暂按 55 英寸级屏幕设计；这是对原 98 英寸方案的明确调整，成品型号尚未选定。</p>'+diagram('plan-tv-v6','移动电视路径：同一台 C02 的三个停放位与转向占位，非三台电视')+'<p class="caption">实线为客厅至卧室的移动中心线，虚线为用餐方向；细框表示整机不同方向的占位。先移开 T02 边几、收好 T01 餐桌，移动结束再布置用餐。机器人暂停作业。不是自动驾驶路线。</p>'+facts([
 ('电视墙做减法','保留连续同色哑光墙面、既定低踢脚防护与低位电源；不做大理石背景、格栅或固定长柜。插座藏在停靠柜后，但可从侧边触及；电视推走后不留下空洞或安装板。'),
 ('柜架是一件完整设备','目标柜体宽 1100、深 550、本体高 360mm；轮组占高约 100mm。电视通过匹配 VESA 的支架连接承重底盘，不能只把电视原脚座搁在普通带轮柜上。支架、轮组、连接件、重心和防倾覆由成品厂家共同确认。'),
 ('轻的跟着走，重的留在原位','NAS 与网络设备继续放在 C09。小型播放器随柜，短 HDMI 在柜内归位，通过无线网络读取内容；高码率视频先验证各停放点实际网络表现。移动前关机拔掉外部电源并收线，停稳锁轮后再接电。'),
 ('三处停放各有边界','客厅常驻靠西墙；用餐位临时放在厨房空地、面向 T01；卧室临时停在床尾，保留床侧进出。床尾柜会占用该段过道，睡前看完优先移回客厅。两处临时位就近预留插座，不把电线横拉过通道。')])+photo('tv-rear-v6','C02 后部打开检修的结构意向：支架贯通、通风播放器层与断电收线；非观看状态')+'<p class="caption">后视图为检修展示，屏幕临时转向；常态朝向以客厅主图和平面为准。图示是外观与结构意向，未指定量产产品，也未完成承载认证。</p>'+diagram('tv-details-v6','移动电视与边几尺寸：整机包络、柜体结构与过门方向')+facts([
 ('过门要算整机','用 1250 × 600mm 平面包络进行概念转向检查，包含屏幕外伸及柜架余量。图中客厅连接开口扩大到 2220mm，卧室入口名义 1320mm；门套、门扇、把手和操作者站位仍需复核，不能据此保证实房可通过。'),
 ('T02 是可移动边几','台面目标 450 × 350mm、高 550mm，圆角硬质面，四脚轮带驻停。放在沙发近端扶手外侧，水杯不置于软垫；移动前拿下杯子。底座不强塞进落地沙发下方，转移电视时先把边几让开。'),
 ('保留 98 英寸的另一种取舍','若最终仍以 98 英寸观影为第一优先，应回到客厅常驻大屏方案，重新验证大型柜架；不能沿用本版 55 英寸包络和移动路线。以三星 98 QN90D 为例，机身约 2185 × 1249mm、无底座约 61.4kg。')])+'<p class="caption">尺寸依据示例：<a href="https://www.samsung.com/au/tvs/qled-tv/qn90d-98-inch-neo-qled-4k-smart-tv-qa98qn90dawxxy/" target="_blank" rel="noopener">三星 98 QN90D 官方规格</a>。<a href="https://media.ergotron.com/reserved/resources/05-087-orig.pdf" target="_blank" rel="noopener">Ergotron 移动媒体车资料</a>用于说明专业承重、线缆管理与锁轮产品类别，不代表图示定制柜或本项目已选型号。</p></div>'

def audit_section():
 rows=[('V01 客厅','平面西侧 C02、东侧沙发、南侧露台','主图朝南拍摄，画面左沙发、右电视；固定长柜已取消，T02 带轮边几已补入。'),('V02 工作室','北侧 C03、东侧窗下工作台','两屏同向；MacBook、Mac mini、键鼠和桌垫保留。桌面细部单独看尺寸图。'),('V03 轻厨房','西侧操作台、北侧设备与饮水柜','主图保持左操作台、正面冰箱与 C06；主图为餐桌收起、电视不在用餐位的状态。'),('V04 卧室','西侧衣柜、北向床头、东侧外窗','删除旧图左侧多余门洞；入口在镜头外。图为安静睡眠状态，床尾电视只在移动图中临时出现。'),('V05 卫浴','左淋浴、正面单盆镜柜、右马桶与浴缸','主设备关系已核对。淋浴挡水和镜柜分缝由结构图深化，不从透视量尺寸。'),('V06 家政','C08 北至南：洗烘、基站、工具','改为正立面局部图，删除旧图不成立的客厅远景。')]
 return '<details class="method"><summary>本版图纸与效果图核对记录 <span>＋</span></summary><div><p>本版统一到 V6。三种使用状态共用一台移动电视；效果图表达材质，平面标注家具外廓，不能把透视画面当作尺寸图。</p><div class="audit-scroll"><table class="audit-table"><thead><tr><th>视角</th><th>平面基准</th><th>核对与修正</th></tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div><p>门洞调整仅针对尚未购房的概念平面，不表示现有建筑可以拆墙。家具尺寸、墙体性质、净开口与操作者空间须在选房和实测阶段确认。</p></div></details>'

def overlay(R,T):
 data=json.loads((Path(__file__).parent/'tv-routes-v6.json').read_text());out=''
 for k,color in [('bedroom','#466c98'),('dining','#a17742')]:
  p=data[k];points=' '.join(f'{x},{y}' for x,y,a in p)
  out+=f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="25" stroke-dasharray="{90 if k=="dining" else 0}"/>'
  for x,y,a in p[::max(1,len(p)//8)]:
   out+=f'<rect x="{x-625}" y="{y-300}" width="1250" height="600" transform="rotate({a*15} {x} {y})" fill="none" stroke="{color}" stroke-width="12" opacity=".6"/>'
 for x,y,a,label in [(500,6000,90,'客厅常驻'),(2700,2800,90,'用餐临时'),(9250,8850,0,'床尾临时')]:
  out+=f'<g transform="translate({x} {y}) rotate({a})"><rect x="-550" y="-275" width="1100" height="550" fill="#d1def0" stroke="#466c98" stroke-width="22"/><path d="M-625 -290H625" stroke="#263e59" stroke-width="36"/></g>'
  out+=T(x,9180 if label=='床尾临时' else 1800 if label=='用餐临时' else y-760,label,140)
 out+=R(1100,1950,650,450,'#e2d2b8')+T(1425,2230,'T01 用餐',120)
 return out

def render(svg_start,rect,txt,line,A,D):
 out=svg_start(1120,810,'C02 移动电视柜架与 T02 边几概念尺寸，非制造图')
 out+=txt(45,45,'移动的是整套设备，不只是一块屏幕。',25,'start')+txt(45,78,'C02 / 正立面与平面包络 · T02 / 移动边几 · 单位 mm',15,'start','dim')
 # Front, scaled .30; screen 1250 x 710 placeholder, center1050.
 out+=rect(65,130,375,213,'#2c3539','#172124',3)+rect(243,343,18,51,'#a4aaa9')+rect(87.5,394,330,108,'#e4e3de','#7f8785',3)
 out+=line(252,394,252,502)+txt(170,443,'播放器 / 遥控器',14)+txt(335,443,'支架 / 收线',14)
 for x in [104,385]:out+=rect(x,507,20,23,'#6e7977','#596563',6)
 out+=line(87,558,418,558)+txt(252,585,'柜宽 1100 / 本体高 360',16)
 out+=txt(252,617,'轮组占高目标 100 · 屏幕中心约 1050',14,cls='dim')
 out+=rect(590,160,375,180,'#eef3f7','#547491',3)+rect(612.5,167.5,330,165,'#d4dbdf','#547491')
 out+=txt(777,214,'整机校核包络',18)+txt(777,245,'1250 × 600',20)+txt(777,279,'柜体 1100 × 550',15)+txt(777,370,'屏幕外伸、底盘与脚轮一起计入',14,cls='dim')
 out+=rect(615,465,135,12,'#d7dad8','#758781',6)+rect(650,477,8,135,'#c7cfcb')+rect(710,477,8,135,'#c7cfcb')+rect(615,612,135,9,'#c7cfcb')
 for x in [625,730]:out+=rect(x,621,15,16,'#758781','#758781',5)
 out+=txt(790,492,'T02 / 圆角硬质台面',18,'start')+txt(790,527,'450 × 350 · 高 550',16,'start')+txt(790,562,'四轮驻停 · 不承坐人',15,'start','dim')+txt(790,595,'转移电视前先让开',15,'start','dim')
 out+=txt(45,710,'过门方向：屏幕长边沿行进方向时，需检查的是整机深度与转弯扫过的范围。',16,'start')
 out+=txt(45,745,'支架连接到底盘，柜壳只负责收纳与外观。承载、稳定性与 VESA 匹配须由成品厂家确认。',15,'start','dim')
 out+=txt(45,779,'尺寸为选型目标；55 英寸仅是屏幕级别，具体外廓、重量与轮组会改变移动条件。',15,'start','dim')+'</svg>'
 (A/'tv-details-v6.svg').write_text(out)
