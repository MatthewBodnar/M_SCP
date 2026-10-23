from pathlib import Path
import re,json,html,shutil,sys
ROOT=Path(__file__).resolve().parents[1];src=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'source-material';out=ROOT/'dist'
def slug(t):return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
def inline(s):
 s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 return s
figs=json.loads((out/'diagrams.json').read_text())
def render(md):
 lines=md.splitlines();res=[];sections=[];i=0;ids={}
 while i<len(lines):
  l=lines[i].strip()
  if not l:i+=1;continue
  if l.startswith('# '):i+=1;continue
  if l.startswith('##'):
   level=len(l)-len(l.lstrip('#'));t=l[level:].strip();sid=slug(t);ids[sid]=ids.get(sid,0)+1
   if ids[sid]>1:sid+='-'+str(ids[sid])
   res.append(f'<h{level} id="{sid}">{inline(t)}</h{level}>')
   if level==2:sections.append({'id':sid,'title':t})
   i+=1;continue
  if l.startswith('[diagram:'):
   key=l[9:-1];f=figs[key];res.append(f'<figure class="diagram"><button class="diagram-open" data-diagram="{key}" aria-label="Enlarge diagram: {html.escape(f["title"])}"><img src="diagrams/{key}.svg" alt="{html.escape(f["description"])}" loading="lazy"><span class="diagram-hint">⤢ Explore diagram</span></button><figcaption>{html.escape(f["title"])}</figcaption></figure>');i+=1;continue
  if l.startswith('[lab:'):
   res.append('<div class="lab-embed" data-lab="'+l[5:-1]+'"></div>');i+=1;continue
  if l.startswith('[answer:'):
   res.append('<details class="answer"><summary>'+inline(l[8:-1])+'</summary><div>');i+=1;continue
  if l=='[/answer]':res.append('</div></details>');i+=1;continue
  if l.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.match(r'^:?-+:?$',c) for c in cells):rows.append(cells)
    i+=1
   res.append('<div class="table-scroll" tabindex="0" aria-label="Scrollable comparison table"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in r)+'</tr>' for r in rows[1:])+'</tbody></table></div>');continue
  if l.startswith('>'):
   q=[]
   while i<len(lines) and lines[i].strip().startswith('>'):q.append(lines[i].strip()[1:].strip());i+=1
   res.append('<blockquote>'+inline(' '.join(q))+'</blockquote>');continue
  if re.match(r'^\d+\. ',l):
   res.append('<ol>')
   while i<len(lines) and re.match(r'^\d+\. ',lines[i].strip()):res.append('<li>'+inline(re.sub(r'^\d+\. ','',lines[i].strip()))+'</li>');i+=1
   res.append('</ol>');continue
  p=[l];i+=1
  while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','>','|','[')):
   p.append(lines[i].strip());i+=1
  res.append('<p>'+inline(' '.join(p))+'</p>')
 return '\n'.join(res),sections
summaries=[
 'Needs, wants, demand and the promise you make to customers.',
 'Flows, whole-chain value, integration and the four Rs.',
 'Barney’s resource-based view and the original VRIN tests.',
 'ARA, interaction, networking and the three levels of analysis.',
 'Make or buy, core competence and supplier relationships.',
 'Four quadrants, the wider process and a strong exam discussion.',
 'Transformation, quality, seven wastes and process improvement.',
 'P-time, D-time, postponement and the decoupling point.',
 'EOQ, reorder point, break-even, ABC and valuation examples.',
 'Connect the glossary’s systems, identifiers and logistics roles.',
 'BATNA, value creation, seven phases and cultural awareness.',
 'Apply the entire module to one event-shirt order.',
 'Model answers, practice prompts and common exam mistakes.',
 'Retrieve the key ideas, formulas and names from memory.'
]
chapters=[]
for n,p in enumerate(sorted((ROOT/'content').glob('*.md'))):
 md=p.read_text();title=md.splitlines()[0][2:];body,sections=render(md)
 chapters.append({'id':p.stem,'number':n+1,'title':title,'summary':summaries[n],'html':body,'sections':sections,'words':len(md.split()),'minutes':max(1,round(len(md.split())/200))})
# The DOCX paragraphs are copied verbatim into the exact-source field.
from docx import Document
p=next(src.glob('*.docx'),None)
if p:
 paras=[x.text for x in Document(p).paragraphs];start=paras.index('3PL – Third Party Logistics');entries=[]
 current=None
 for text in paras[start:]:
  if text.startswith('Appendix A'):break
  # Glossary headings are non-empty paragraphs followed by prose, with known heading names.
  headings=['3PL – Third Party Logistics','4PL – Fourth Party Logistics','ABC classification','Agile supply chain management','Business Process Reengineering (BPR)','EOQ – Economic Order Quantity','ERP – Enterprise Resource Planning','JIT – Just In Time','Kanban','Kaizen','FIFO – First In First Out','Lean supply chain management','LIFO – Last In First Out','MPS – Master Production Schedule','MRO = Maintenance, repair, and operating','MRP – Material Requirements Planning','MUDA – Waste','QR – Quick Repsonse','RFID = Radio-frequency identification','Safety Stock','Six Sigma','SKU – Stock Keeping Unit','TQM – Total Quality Management','VMI = Vendor-managed inventory','WMS – Warehouse Management System']
  if text.strip() in headings:
   if current:entries.append(current)
   current={'term':text.strip(),'exact':[]}
  elif current and text.strip():current['exact'].append(text)
 if current:entries.append(current)
else:
 entries=json.loads((ROOT/'content/glossary-data.json').read_text())
plain=[
 ('An outside firm performs logistics work for your business.','Campus Tees hires a fulfilment company to pack and ship orders.','The service scope varies; it need not cover every supply-chain activity.'),
 ('One provider coordinates the broader logistics network and its strategy.','A provider designs the network and oversees warehouses and carriers.','Focus on the coordination role, not merely provider size.'),
 ('Give the most economic attention to the items representing the most value.','One SKU accounts for €8,000 of a €10,000 annual usage-value total.','80/20 is an illustration, not a mandatory exact split. Critical low-value items still matter.'),
 ('Be able to respond to changing demand using knowledge and flexible capabilities.','Switch the final print mix when confirmed club orders change.','Agile does not mean unlimited spending or speed without coordination.'),
 ('Redesign a core process radically rather than only improve one small step.','Replace disconnected forms with a redesigned order-to-delivery flow.','Contrast the scale of redesign with Kaizen’s ongoing improvement emphasis.'),
 ('Choose the lot size balancing annual order-event cost and stockholding cost.','D=12,000, K=30, h=2 gives EOQ=600 units.','The basic model minimises the sum, not each cost separately. Fewer orders reduce annual ordering cost; a unit-price discount is not assumed.'),
 ('Integrate business processes and data so departments can coordinate.','Sales, purchasing and finance use consistent order information.','Software alone does not create accurate data or well-designed processes.'),
 ('Provide materials close to when they are needed instead of building unnecessary stock.','Replenish packing material in reliable small flows.','JIT requires quality, reliable processes and coordination; it is not a literal zero-stock command.'),
 ('Use a signal to authorise replenishment after consumption.','An empty bin triggers a refill card.','Signal rules and quantities must fit demand and replenishment lead time.'),
 ('Keep making and evaluating improvements.','Refine the artwork checklist after discovering a recurring error.','Continuous improvement can involve people across the organisation.'),
 ('Assign the oldest inventory costs to the units sold first.','Ten units at €2 then ten at €3; selling ten gives FIFO cost of €20.','Physical rotation and accounting cost assumptions are related but distinct.'),
 ('Reduce waste and improve flow while maintaining the required service.','Remove duplicate entry and shorten queues.','Lean does not require removing every useful buffer without understanding its role.'),
 ('Assign the newest inventory costs to the units sold first.','The same purchases produce LIFO cost of €30 for ten sold units.','This explains the concept; it does not claim universal accounting permission.'),
 ('Plan what finished output to produce and when.','Schedule 300 event shirts next week.','MRP then translates the output plan into material requirements.'),
 ('Supplies keep the operating system running rather than becoming the main sold product.','A printer belt or cleaning material supports production.','The source wording is narrower than broad operational usage; learn its wording and the underlying support role.'),
 ('Work out required materials, quantities and timing from the production plan.','300 shirts minus 80 suitable blanks on hand implies 220 additional blanks before other adjustments.','A complete MRP system also considers receipts, reservations, lead times and planning rules.'),
 ('Look for seven forms of unnecessary resource use.','A batch waits for approval, is moved unnecessarily and then needs reprinting.','Motion is people moving; transport is goods moving. Waste categories can interact.'),
 ('The paragraph describes QR-code scanning to identify and track stock.','Scan a code when receiving a carton.','The heading has the source’s spelling. QR codes and agile quick-response strategy are different uses of QR.'),
 ('Use radio tags to identify or track items.','A reader captures a tagged carton movement.','Accurate events and processes are still required.'),
 ('Hold a protective buffer against uncertain demand or supply.','60 extra blanks protect against variation beyond expected lead-time demand.','The needed buffer depends on service ambition and variability.'),
 ('Use data to reduce defects and variation in a process.','Measure misprints and test which process changes reduce them.','Do not use the label as a synonym for every quality initiative.'),
 ('Give each separately managed stock variant an identity.','Small white and medium white shirts have different SKUs.','A SKU is the identity; barcode, QR and RFID are ways to encode or capture it.'),
 ('Make quality and ongoing improvement a responsibility across the organisation.','Sales and printing prevent specification errors together.','The source’s replacement claim is a broad teaching description; TQM, lean and Six Sigma can coexist.'),
 ('The supplier monitors stock and initiates replenishment under agreed rules.','The carton supplier reviews usage and refills within agreed limits.','VMI does not automatically specify who owns the inventory.'),
 ('Support daily warehouse execution and location control.','Guide receiving, put-away, picking and dispatch.','A WMS has a different focus from broader ERP integration and MRP planning.')]
assert len(entries)==25,(len(entries),[e['term'] for e in entries])
for e,(simple,example,note) in zip(entries,plain):e.update(simple=simple,example=example,note=note,exact='\n\n'.join(e['exact']) if isinstance(e['exact'],list) else e['exact'],id=slug(e['term']))
# Keep source originals available alongside the explanatory course.
source_meta=[];(out/'sources').mkdir(exist_ok=True)
for i,p in enumerate(sorted(src.glob('*'))):
 if p.suffix not in ['.pdf','.docx']:continue
 name=re.sub(r'[^a-z0-9]+','-',p.stem.lower()).strip('-')+p.suffix;shutil.copyfile(p,out/'sources'/name)
 pages=None
 if p.suffix=='.pdf':
  import fitz
  pages=len(fitz.open(p))
 source_meta.append({'title':p.stem,'url':'sources/'+name,'type':p.suffix[1:].upper(),'pages':pages})
if not source_meta:source_meta=json.loads((ROOT/'content/source-register.json').read_text())
past_exams=json.loads((ROOT/'content/past-exams.json').read_text())
(out/'sources/exams').mkdir(exist_ok=True)
for paper in past_exams['papers']:
 p=src/'exams'/paper['file']
 if p.exists():shutil.copyfile(p,out/paper['url'])
 source_meta.append({'title':paper['title']+' — '+paper['file'],'url':paper['url'],'type':'PDF','pages':1,'kind':'past-exam',**({'external':True} if paper['url'].startswith('https://') else {})})
exam_text='\n\n'.join('# '+p['title']+'\n\n'+'\n\n'.join('## Question '+str(q['number'])+' — '+str(q['points'])+' points\n\n'+q['prompt']+'\n\nWhat it asks: '+q['plain']+'\n\nModel answer:\n\n'+'\n\n'.join(q['answer'])+'\n\nSelf-check:\n'+'\n'.join('- '+item for item in q['checklist'])+'\n\nWatch out: '+q['pitfall'] for q in p['questions']) for p in past_exams['papers'])
words=sum(c['words'] for c in chapters)+sum(len((e['exact']+' '+e['simple']+' '+e['example']+' '+e['note']).split()) for e in entries)+len(exam_text.split())
data={'chapters':chapters,'glossary':entries,'sources':source_meta,'figures':figs,'words':words,'pastExams':past_exams,'sourceNote':'The earlier working draft did not survive the environment reset. The initial 28,094-word edition was rebuilt from the 16 original uploads and prior review notes, with 31 redrawn study diagrams. This edition preserves that material and adds the three supplied past papers, all 12 questions, study model answers, and expanded bullwhip, risk, sustainability and SCOR explanations. Primary references supplement bullwhip and SCOR and are identified in Past exams. The separate Panigrahi et al. review named on the inventory slide and optional further readings were not supplied as full texts. The dates and official marking schemes for the past papers were not supplied.'}
(out/'course.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
(out/'study-guide.md').write_text('\n\n'.join(p.read_text() for p in sorted((ROOT/'content').glob('*.md')))+'\n\n# Glossary\n\n'+'\n\n'.join('## '+e['term']+'\n\n'+e['exact']+'\n\nIn plain English: '+e['simple']+'\n\nExample: '+e['example']+'\n\nClarification: '+e['note'] for e in entries))
(out/'study-guide.md').write_text((out/'study-guide.md').read_text()+'\n\n# Supplied past papers and study model answers\n\n'+past_exams['note']+'\n\n'+exam_text)
print(json.dumps({'chapters':len(chapters),'words':words,'glossary':len(entries),'diagrams':len(figs),'sourceFiles':len(source_meta)}))
