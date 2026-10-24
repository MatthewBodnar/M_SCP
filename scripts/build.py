from pathlib import Path
import re, json, html, shutil, sys
from urllib.parse import quote
import fitz
ROOT=Path(__file__).resolve().parents[1]
src=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'source-material'
out=ROOT/'dist'
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

lectures=json.loads((ROOT/'content/lectures.json').read_text())
chapters=[]
used_figures=set()
for number,lecture in enumerate(lectures,1):
    md=(ROOT/'content'/(lecture['id']+'.md')).read_text()
    body,sections=render(md)
    used_figures.update(re.findall(r'\[diagram:(.*?)\]',md))
    chapters.append({**lecture,'number':number,'html':body,'sections':sections,
        'words':len(md.split()),'minutes':max(1,round(len(md.split())/200))})
entries=json.loads((ROOT/'content/glossary-data.json').read_text())
source_meta=[]
(out/'sources').mkdir(exist_ok=True)
for p in sorted(src.glob('*')):
    if p.suffix not in ['.pdf','.docx']:continue
    name=slug(p.stem)+p.suffix
    shutil.copyfile(p,out/'sources'/name)
    source_meta.append({'title':p.stem,'url':'sources/'+name,'type':p.suffix[1:].upper(),
        'pages':len(fitz.open(p)) if p.suffix=='.pdf' else None})
past_papers=json.loads((ROOT/'content/past-papers.json').read_text())
(out/'sources/exams').mkdir(exist_ok=True)
for paper in past_papers:
    shutil.copyfile(src/'exams'/paper['file'],out/paper['url'])
    source_meta.append({'title':paper['title']+' — '+paper['file'],'url':paper['url'],
        'type':'PDF','pages':1,'kind':'past-exam'})
for source in source_meta:
    path=quote(source['url'],safe='/')
    source['publicUrl']='https://github.com/MatthewBodnar/M_SCP/blob/main/dist/'+path
    source['downloadUrl']='https://raw.githubusercontent.com/MatthewBodnar/M_SCP/main/dist/'+path
practice=json.loads((ROOT/'content/practice-exams.json').read_text())
practice_text='\n\n'.join('# '+p['title']+'\n\n'+'\n\n'.join(
    '## Question '+str(q['number'])+' — '+str(q['points'])+' points\n\n'+q['prompt']+
    '\n\nStudy answer:\n\n'+'\n\n'.join(q['answer']) for q in p['questions']) for p in practice['papers'])
words=sum(c['words'] for c in chapters)+sum(len((e['exact']+' '+e['simple']+' '+e['example']+' '+e['note']).split()) for e in entries)+len(practice_text.split())
data={'edition':'github-seven-lectures','chapters':chapters,'glossary':entries,'sources':source_meta,
    'figures':{key:figs[key] for key in sorted(used_figures)},'words':words,
    'practiceExams':practice,'pastPapers':past_papers,
    'sourceNote':'Seven short chapters follow the seven lecture PDFs. Source definitions keep their wording. Other explanations use simple English. The inventory review PDF was not uploaded; its chapter uses only the publisher abstract. Past exam PDFs stay in Sources. The practice questions are new.'}
(out/'course.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
book='\n\n'.join((ROOT/'content'/(lecture['id']+'.md')).read_text() for lecture in lectures)
book+='\n\n# Glossary\n\n'+'\n\n'.join('## '+e['term']+'\n\n'+e['exact']+'\n\nPlain English: '+e['simple']+'\n\nCampus Tees: '+e['example']+'\n\nNote: '+e['note'] for e in entries)
book+='\n\n# New practice papers\n\n'+practice['note']+'\n\n'+practice_text
(out/'study-guide.md').write_text(book)
print(json.dumps({'chapters':len(chapters),'chapterWords':sum(c['words'] for c in chapters),'totalWords':words,
    'glossary':len(entries),'diagramsUsed':len(used_figures),'sourceFiles':len(source_meta),
    'newPracticeQuestions':sum(len(p['questions']) for p in practice['papers'])}))
