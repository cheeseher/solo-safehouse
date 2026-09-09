"""Surface-mounted skirting details and a usable-length chaise layout."""
def render_details(svg_start,rect,txt,line,A):
 out=svg_start(1120,810,'B01 同墙色明装踢脚线：木地板墙脚剖面概念')
 out+=txt(45,42,'B01 / 不开槽，也能把墙脚保护好',24,'start')+txt(45,76,'剖面原理图 · 示例 H60 / 外凸 P15 / 伸缩缝 G10，单位 mm',15,'start','dim')
 # Wall and floor are separate systems. The hollow profile is fastened to wall only.
 out+=rect(90,125,210,570,'#d7ddd5','#8f9b8d')+rect(290,125,10,495,'#f7f8f1','#adb5a8')
 out+=rect(90,700,505,45,'#c4cabe','#8f9b8d')+rect(360,620,235,75,'#d8c9aa','#a9987a')
 out+=txt(188,175,'墙体 / 找平基层',16)+txt(466,665,'木地板',18)+txt(466,729,'垫层 / 基层',15)
 out+=rect(301,290,8,280,'#b2c5ad','#71866c')
 # Adhesive and rear attachment are schematic, not a prescribed extrusion section.
 out+=line(309,300,381,300,'#a7b6a0',3)+line(309,560,381,560,'#a7b6a0',3)
 out+=rect(381,262,9,349,'#fafbf5','#8d9c87')+rect(309,260,81,10,'#fafbf5','#8d9c87')
 out+=line(90,620,360,620,'#8e9a88',1,'4 4')
 out+=line(420,260,420,620)+line(411,260,429,260)+line(411,620,429,620)+txt(442,454,'H = 60',15,'start')
 out+=line(300,220,390,220)+line(300,214,300,226)+line(390,214,390,226)+txt(345,207,'P = 15',15)
 out+=line(300,680,360,680)+txt(330,674,'G10',13)
 for y,title,copy in [(160,'01  同色的成品表面','低矮、平直、哑光；不做装饰凹槽。'),(273,'02  型材固定在墙上','胶或配套卡扣按厂家系统安装。'),(386,'03  留足遮盖量','示例 15 − 10 = 5mm，不是通用尺寸。'),(499,'04  地板仍能伸缩','不把型材压死、钉死在浮铺地板上。'),(612,'05  拖地接触的是收边','有防潮要求时按地板厂家做弹性封边。')]:
  out+=txt(650,y,title,21,'start')+txt(650,y+36,copy,16,'start','dim')
 out+=txt(45,782,'截面仅表达构造关系，不是订货截面。P 必须覆盖实际 G、安装偏差与遮盖余量；高度并非防水等级。',14,'start','dim')+'</svg>'
 (A/'skirting-section.svg').write_text(out)
 out=svg_start(1120,560,'B02 阴角、阳角、门套端头的踢脚线收口示意')
 out+=txt(45,42,'B02 / 好看的收边，结束处也要完整',24,'start')+txt(45,75,'平面收口原理 · 不按比例，采用选定型材的配套节点',15,'start','dim')
 for n,(x,title) in enumerate([(45,'阴角 / 内转角'),(415,'阳角 / 外转角'),(785,'门套 / 结束处')]):
  out+=txt(x,127,title,20,'start')
  if n==0:
   out+=rect(x+20,165,260,35,'#d6ddd2')+rect(x+20,200,35,165,'#d6ddd2')
   out+=rect(x+56,201,224,15,'#f8faf2')+rect(x+56,216,15,148,'#f8faf2')+line(x+56,201,x+71,216,'#73806e',1.5)
  elif n==1:
   out+=rect(x+20,165,180,150,'#d6ddd2')+rect(x+20,316,194,15,'#f8faf2')+rect(x+201,165,15,150,'#f8faf2')+line(x+200,315,x+215,330,'#73806e',1.5)
  else:
   out+=rect(x+5,205,240,35,'#d6ddd2')+rect(x+5,241,178,15,'#f8faf2')+rect(x+184,238,8,21,'#e1e7db')+rect(x+196,188,49,82,'#f3f6ec')
   out+=txt(x+144,305,'配套端帽',14)+line(x+152,287,x+188,260)
  for j,t in enumerate([['贴合墙角，不留积灰洞。','拼缝或配套内角件，颜色一致。'],['斜切去毛刺或使用配套外角件。','避免尖锐金属边外露。'],['端头闭合，衔接门套。','与门扇开启及地面收口一起核对。']][n]):out+=txt(x,409+j*32,t,16,'start','dim')
 out+=txt(45,513,'先做一段样板：直线＋转角＋门套端头。白天与夜间看色差，用湿拖布轻擦后再确认整屋施工。',15,'start','dim')+'</svg>'
 (A/'skirting-corners.svg').write_text(out)

def section(photo,diagram,facts):
 return '''<section class="section skirting" id="skirting"><div class="section-label"><span>05 / 墙脚与收边</span><span>LESS VISIBLE. STILL PROTECTED.</span></div><div class="section-head"><h2>墙脚安静，<br>拖地省心。</h2><p>不想要厚重的传统踢脚线，也不想为隐藏做法开槽、找平和反复补漆。这个方案保留必要的墙脚保护，用低矮、同墙色的平直明装款降低存在感。</p></div>'''+photo('skirting','同墙色、低矮明装踢脚线的 AI 近景效果图；型材截面与尺寸以结构示意及实物为准')+'''<div class="practical-detail"><p class="eyebrow">B01 / 本方案的参考方向</p><h3>约 60mm 高，颜色接近墙面。</h3><p class="detail-lede">先找现货哑光铝合金平直款，看样板、看配套转角和端帽。固定在完成的墙面上，省去隐藏式收边的开槽和墙面重做工序。预算紧时也可比较成品防潮平直款；材料、配件与人工一起报价，不默认金属一定最便宜。</p>'''+facts([
 ('少一点存在感','降低高度、接近墙色、简化外形，比一味追求“极薄”更可靠。选成品涂层，现场打样看色差与擦洗表现，不把普通墙漆直接当作金属面漆。'),
 ('保留实际保护','拖布和机器人沿墙清洁时，先接触易擦拭的收边表面。它能减少墙脚直接受污，但不等于全墙防水，也不免除转角和上沿的擦拭。'),
 ('先确定地面，再定截面','木地板、SPC 或其他浮铺地材可能需要周边伸缩空间。踢脚线的覆盖宽度按具体地板要求选择，不为了藏线感把地板顶死在墙上。')])+'''</div><div class="drawer"><h3>厚度不能只看外观。</h3><p>这张剖面用“缝宽 10mm、外凸 15mm”说明遮盖关系，数字只是示例。实际缝宽、墙面偏差和伸缩量由地板系统确定；太薄盖不住时，应换足够覆盖的截面。</p>'''+diagram('skirting-section','明装踢脚线墙地剖面：固定在墙、覆盖伸缩缝、保留地板活动能力')+'''</div><div class="drawer"><h3>转角与门套，先做出来看。</h3><p>不要等整屋装完才发现端头裸露、门套错台或胶缝过宽。用同批材料做一段完整样板，包含直线、一个转角和一处门套结束点。</p>'''+diagram('skirting-corners','踢脚线内角、外角与门套端头的收口原理')+'''</div><div class="practical-detail"><h3>把钱花在需要的工序上。</h3>'''+facts([
 ('墙脚先平整、干燥','基层松动、起砂或不平，薄型收边容易显缝。先处理局部基层，再按型材厂家的胶粘或卡扣方式固定；不预先指定所有墙都能直接粘。'),
 ('伸缩缝不硬填','不把踢脚线钉在或压死在浮铺地板上。防水型地材若要求背衬泡沫与弹性封边，按该系统完整做；不能用硬胶或水泥填死伸缩空间。'),
 ('清洁范围说清楚','普通房间按地面材料要求微湿清洁，积水及时处理。卫生间淋浴等长期湿区另做墙地防水与收口，不能靠这条踢脚线解决。')])+'''<p class="caption">订货清单同时问清：型材、内外角件、端帽、胶或卡扣、基层处理与安装人工。不要只比较单根材料价格。</p></div><details class="method"><summary>材料与结构参考依据 <span aria-hidden="true">＋</span></summary><div><p><a href="https://asp-profiles.com/products/p-3-60" target="_blank" rel="noopener noreferrer">ASP 的明装铝合金踢脚线</a>说明了完成墙面安装及墙脚保护用途；<a href="https://www.progressprofiles.com/en/skirting-boards" target="_blank" rel="noopener noreferrer">Progress Profiles</a>提供多种高度与固定方式的成品收边。这里借鉴构造原则，不指定进口品牌或其价格。</p><p><a href="https://int.quick-step.com/en/laminate/installation" target="_blank" rel="noopener noreferrer">Quick-Step 地板安装资料</a>提供分材料安装指导。地板伸缩、防潮封边、清洁方法必须以购买产品的最新版要求为准。本页剖面是概念关系图，不是可直接加工的型材图。</p></div></details></section>'''
