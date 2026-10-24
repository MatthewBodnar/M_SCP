from pathlib import Path
from html import escape
import textwrap,math,json
OUT=Path('dist/diagrams');OUT.mkdir(parents=True,exist_ok=True)
G='#163e36';M='#bce6d0';O='#efb88f';B='#d9e6f0';BG='#f6f8f3';S='#66766e'
captions={}
def svg(id,title,desc,draw):
 global parts
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 460" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8Z" fill="{G}"/></marker></defs><rect width="960" height="460" rx="16" fill="{BG}"/>']
 txt(36,42,title,25,weight='700');draw();parts.append('</svg>');(OUT/(id+'.svg')).write_text(''.join(parts));captions[id]={'title':title,'description':desc}
def txt(x,y,s,size=18,color=G,anchor='start',weight='400'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(str(s))}</text>')
def line(x1,y1,x2,y2,arrow=False,color=G,dash=False):
 parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2.5" '+('marker-end="url(#a)" ' if arrow else '')+('stroke-dasharray="7 6" ' if dash else '')+'/>')
def box(x,y,w,h,title,sub='',color=M):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}"/>');ls=textwrap.wrap(title,max(8,int(w/11)))
 for i,s in enumerate(ls):txt(x+w/2,y+30+i*23,s,20,anchor='middle',weight='700')
 for i,s in enumerate(textwrap.wrap(sub,max(10,int(w/9)))):txt(x+w/2,y+40+len(ls)*21+i*20,s,16,anchor='middle')
def chain(labels,subs=None):
 n=len(labels);w=(850-(n-1)*28)/n
 for i,l in enumerate(labels):
  x=55+i*(w+28);box(x,160,w,145,l,(subs or ['']*n)[i],M if i%2==0 else B)
  if i<n-1:line(x+w+4,232,x+w+23,232,True)
def grid(labels,xlab,ylab,subs=None):
 for i,t in enumerate(labels):
  c=i%2;r=i//2;box(145+c*345,90+r*135,325,120,t,(subs or ['']*4)[i],[M,B,O,'#e6e9d5'][i])
 line(120,365,855,365,True);line(120,365,120,80,True);txt(500,411,xlab,19,anchor='middle');txt(150,385,'Low',15);txt(812,385,'High',15);txt(23,95,'High',15);txt(29,350,'Low',15);txt(22,232,ylab,17)
def plotbase(ylabel,xlabel):
 line(90,365,880,365,True);line(90,365,90,90,True);txt(92,78,ylabel,17);txt(480,420,xlabel,17,anchor='middle')
def poly(points,color=G):parts.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="4"/>')
svg('needs','Needs → wants → demands','A need is something missing. A want is a chosen solution. Demand includes the ability to pay.',lambda:chain(['Need','Want','Demand'],['Something is missing','A preferred solution','Want + purchasing power']))
svg('stp','Choose whom to serve and what to promise','Find groups, choose which to serve, and explain the offer. Each stage has two steps.',lambda:chain(['Segment','Target','Position'],['Identify bases; profile groups','Evaluate appeal; choose groups','Define benefit; develop mix']))
def supply():
 chain(['Supplier','Campus Tees','Customer'],['Inputs and capability','Print and coordinate','Use the final outcome']);txt(480,120,'MATERIALS AND PRODUCTS →',18,anchor='middle');txt(480,355,'← REQUIREMENTS INFORMATION',18,anchor='middle');txt(480,392,'Availability, status and changes travel both ways.',17,anchor='middle')
svg('supply','Manage flows and relationships together','Goods go towards customers. Orders usually go towards suppliers. Information moves both ways.',supply)
def integration():
 for i,(t,s) in enumerate([('1 · Baseline','Separate departments and buffers'),('2 · Functional','Coordinate related functions'),('3 · Internal','One connected company plan'),('4 · External','Include suppliers and customers')]):
  box(55+i*220,105+i*42,195,140,t,s,[B,M,O,'#d6ddbd'][i])
svg('integration','The scope of integration expands','Move from separate departments to working with suppliers and customers.',integration)
svg('fourrs','Four Rs, four distinct questions','Responsiveness, reliability, resilience and relationships each address a different requirement.',lambda:chain(['Responsive','Reliable','Resilient','Relationships'],['How quickly can we act?','How consistently do we deliver?','Can we recover from surprise?','Can we coordinate dependencies?']))
svg('costvalue','Two sources of competitive advantage','A cost and value advantage can be combined. Both dimensions increase toward the preferred high-high position.',lambda:grid(['Value leader','Cost + value leader','Commodity position','Cost leader'],'Cost advantage →','Value',['Preferred benefits','Efficient and differentiated','Little advantage','Relative efficiency']))
def experience():
 plotbase('Unit cost','Cumulative output');poly([(100+i*7.5,320-210*math.exp(-i/23)) for i in range(100)],G);txt(400,130,'Learning and experience can lower unit cost.',18);txt(400,160,'Cumulative output ≠ current production rate.',17,color=S)
svg('experience','Experience concerns cumulative output','Illustrative unit cost declines as cumulative output increases. This is not a measured dataset.',experience)
def valuechain():
 for i,t in enumerate(['Infrastructure','Human resource management','Technology development','Procurement']):box(75,77+i*44,810,37,t,'',B)
 for i,t in enumerate(['Inbound logistics','Operations','Outbound logistics','Marketing & sales','Service']):box(75+i*164,285,154,110,t,'',M)
 txt(480,430,'Primary activities supported by capabilities across the firm',17,anchor='middle')
svg('valuechain','Porter’s value chain','The model shows five main activities and four support activities. They affect value and cost.',valuechain)
svg('vrin','Four tests for a sustained resource advantage','Test whether a resource is valuable, rare, hard to copy and has no easy substitute.',lambda:chain(['Valuable','Rare','Inimitable','Non-substitutable'],['Addresses opportunity or threat','Not widely held by rivals','Hard to duplicate','No available strategic equivalent']))
def ara():
 box(365,80,230,105,'Actors','Actor bonds',M);box(100,290,260,110,'Resources','Resource ties',B);box(600,290,260,110,'Activities','Activity links',O);line(380,190,280,280,True);line(580,190,680,280,True);line(380,345,580,345,True);txt(480,250,'Interdependence',19,anchor='middle',weight='700')
svg('ara','ARA: who, what and doing','Actor bonds, resource ties and activity links affect each other.',ara)
def interaction():
 box(65,85,830,330,'Environment','',B);box(100,140,760,245,'Atmosphere','Power, dependence, cooperation and expectations','#e7eee2');box(140,240,220,100,'Actor A','Organisation + people',M);box(600,240,220,100,'Actor B','Organisation + people',O);line(375,280,585,280,True);txt(480,240,'Exchange episodes',16,anchor='middle');txt(480,370,'Repeated interaction → adaptation and established routines',16,anchor='middle')
svg('interaction','IMP: interaction sits inside a wider context','Firms and people exchange goods, information, money and social contact. The wider situation affects them.',interaction)
def networklevels():
 for r,t in enumerate(['Relationship','Small world','Wider world']):
  txt(38,140+r*90,t,17,weight='700')
  for c,l in enumerate(['Activities','Resources','Actors']):box(220+c*235,95+r*90,220,75,l,['Direct connection','Known connected ties','Beyond immediate view'][r],[M,B,O][c])
svg('networklevels','Three layers across three analysis levels','ARA parts differ from three levels: one relationship, nearby links and wider changes.',networklevels)
svg('makebuy','Ownership and coordination are different choices','Market contracting, quasi-integration and vertical integration form a continuum.',lambda:chain(['Market contracting','Quasi-integration','Vertical integration'],['Independent external supply','Close coordination without ownership','Activities under common ownership']))
def tiers():
 box(365,85,230,85,'Focal firm','',G); # dark label replaced below
 txt(480,120,'Focal firm',20,color='white',anchor='middle',weight='700')
 for x in [170,570]:box(x,225,220,90,'Tier 1','System supplier',M);line(480,175,x+110,215,True)
 for x in [75,285,505,715]:box(x,365,175,60,'Tier 2','',B);line(280 if x<480 else 680,320,x+85,355,True)
svg('tiers','A supplier base has structure, not just a count','Tier-one suppliers interface with the focal firm and coordinate lower-tier suppliers.',tiers)
svg('kraljic','Kraljic’s purchasing portfolio','Profit impact rises upwards. Supply risk rises to the right.',lambda:grid(['Leverage','Strategic','Routine','Bottleneck'],'Supply risk →','Impact',['Competition and volume','Partnership and planning','Rationalise administration','Protect continuity']))
svg('kraljicprocess','The matrix starts a wider management process','Classification is followed by market analysis, strategic positioning and action plans.',lambda:chain(['Classify','Analyse market','Position','Act'],['Profit impact and supply risk','Buyer and supply strength','Exploit, balance or diversify','Suppliers, stock, contracts and plans']))
svg('transformation','Operations transform inputs into outcomes','Inputs become outputs. Feedback helps improve the next order.',lambda:chain(['Inputs','Transformation','Outputs'],['Material, people, machines, capital','Connected processes and activities','Goods, services and feedback']))
def timeprocess():
 txt(70,110,'Before: 16 hours',20,weight='700');box(70,140,200,60,'Activity 4h','',M);box(270,140,600,60,'Waiting 12h','',O);txt(70,270,'After: 10 hours',20,weight='700');box(70,300,200,60,'Activity 4h','',M);box(270,300,300,60,'Waiting 6h','',O);txt(70,415,'Illustrative: halving waiting saves more than a small increase in machine speed.',17)
svg('timeprocess','Follow elapsed time, not only processing time','Work takes four hours. Waiting takes twelve. The new plan removes six hours of waiting.',timeprocess)
def fishbone():
 line(100,245,850,245,True);txt(760,218,'Late orders',20,weight='700')
 for x,y,t,s in [(270,100,'People','Training / roles'),(570,100,'Machines','Breakdowns / setup'),(270,390,'Material','Shortage / quality'),(570,390,'Methods','Queues / handovers')]:
  line(x,y,x+100,245);txt(x-65,y-25 if y<200 else y+20,t,22,weight='700');txt(x-65,y+2 if y<200 else y+45,s,16)
svg('fishbone','Organise possible causes before testing them','List possible causes under people, machines, materials and methods. Check which cause is real.',fishbone)
def ptime():
 chain(['Source','Make','Deliver'],['5 days','2 days','1 day']);line(65,340,895,340);txt(480,377,'P-time = 8 days · D-time = 3 days · gap = 5 days',20,anchor='middle');txt(480,418,'Prepare in advance, shorten the process or change the promise.',17,anchor='middle')
svg('ptime','Can the full process fit the customer’s wait?','Supply, printing and delivery take eight days. The customer will wait only three days.',ptime)
svg('postpone','Delay differentiation, preserve options','A common base becomes order-specific only when useful information is known.',lambda:chain(['Generic blanks','Confirmed order','Printed design'],['Prepare common resources','Customer information arrives','Commit to the specific variant']))
svg('leagile','Lean upstream · agile downstream','Prepare common blanks before the order. Print the customer design after the order.',lambda:chain(['Lean upstream','Decoupling point','Agile downstream'],['Stable common flow','Generic stock + order linkage','Respond to actual mix and variety']))
svg('generic','Match strategy to demand and supply timing','Demand predictability is horizontal; long supply lead time is above short supply lead time.',lambda:grid(['Lean','Hybrid / leagile','Kanban','Agile'],'Predictable demand ← → Unpredictable','Lead time',['Long lead: plan and optimise','Long lead: postpone differentiation','Short lead: replenish continuously','Short lead: quick response']))
svg('costtypes','Three independent cost dimensions','Fixed/variable, direct/indirect, engineered/discretionary classify different properties.',lambda:chain(['Behaviour','Traceability','Decision basis'],['Fixed or variable','Direct or indirect','Engineered or discretionary']))
def breakeven():
 plotbase('Cost / revenue (€)','Quantity (shirts)');poly([(90,365),(850,90)],G);poly([(90,255),(850,145)],'#b5704b');line(90,255,850,255,color=S,dash=True);line(596,182,596,365,color=S,dash=True);txt(620,175,'Break-even: 200',19,weight='700');txt(730,85,'Revenue',16);txt(745,140,'Total cost',16);txt(110,245,'Fixed cost €1,200',16)
svg('breakeven','Break-even: contribution covers fixed cost','Illustrative linear chart: F=1200, p=15, v=9; break-even is 200 shirts.',breakeven)
def reorder():
 plotbase('Units in stock','Working days');poly([(95,110),(440,330),(442,110),(787,330),(789,110),(860,155)],G);line(95,255,860,255,color='#b5704b',dash=True);line(95,330,860,330,color=S,dash=True);txt(570,246,'ROP 260',18);txt(570,322,'Safety stock 60',16);line(325,255,325,365,color=S,dash=True);txt(245,402,'Order → 5-day lead → receipt',16);txt(110,100,'660',16)
svg('reorder','Reorder before the stock is exhausted','Order size is 600. Daily use is 40. Delivery takes 5 days. Safety stock is 60. Reorder at 260.',reorder)
def eoq():
 plotbase('Annual relevant cost','Order quantity Q');
 for c,fn in [(G,lambda q:360000/q+q),('#b5704b',lambda q:360000/q),(S,lambda q:q)]:poly([(90+q*.6,365-fn(q)*.10) for q in range(150,1251,10)],c)
 line(450,245,450,365,dash=True);txt(465,240,'EOQ 600',19,weight='700');txt(580,113,'Total = ordering + holding',17);txt(570,150,'D=12,000 · K=30 · h=2',16)
svg('eoq','EOQ balances opposing costs','Ordering falls as Q increases; holding rises; their sum has an optimum at Q=600 in the worked example.',eoq)
def abc():
 vals=[8000,800,600,400,200]
 for i,v in enumerate(vals):
  h=v/35;parts.append(f'<rect x="{155+i*145}" y="{365-h}" width="85" height="{h}" rx="5" fill="{G if i==0 else M}"/>');txt(197+i*145,393,chr(65+i),18,anchor='middle');txt(197+i*145,350-h,f'€{v:,}',17,anchor='middle')
 txt(480,95,'One of five SKUs accounts for 80% of annual usage value.',19,anchor='middle')
svg('abc','Prioritise attention by annual usage value','Illustrative five-item dataset totals €10,000; the first item contributes €8,000.',abc)
svg('systems','Information tools support different decisions','ERP integrates processes; MPS plans output; MRP plans material; WMS supports warehouse execution.',lambda:chain(['ERP','MPS','MRP','WMS'],['Connect business data','Plan output and timing','What materials, how much, when?','Receive, locate, pick and dispatch']))
def pie():
 box(80,125,350,230,'Distributive','Divide a fixed pie: price with all other conditions fixed',B);box(530,125,350,230,'Integrative','Create value: combine price, volume, timing and service',M);txt(480,410,'A negotiation can create value and then negotiate how to share it.',18,anchor='middle')
svg('negotiationpie','Divide value · create value','A negotiation can divide existing value and find new value. It can do both.',pie)
def phases():
 labels=['Prepare','Greet','Introduce','Argue','Compromise','Close','Realise']
 for i,t in enumerate(labels):
  row=0 if i<4 else 1;j=i if i<4 else i-4;x=55+j*220;y=115+row*180;box(x,y,190,100,f'{i+1} · {t}','',M if row==0 else B)
  if (i<3 or 4<=i<6):line(x+195,y+50,x+215,y+50,True)
 line(810,220,810,270);line(810,270,150,270);line(150,270,150,290,True)
svg('phases','Agreement is not finished until it is implemented','Preparation, greeting, introduction, argumentation, compromise, closure and realisation.',phases)
Path('dist/diagrams.json').write_text(json.dumps(captions,ensure_ascii=False,indent=2))
print(f'{len(captions)} SVG diagrams generated')
