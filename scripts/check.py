from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1];d=json.loads((root/'dist/course.json').read_text());assert len(d['chapters'])==14;assert len(d['glossary'])==25;assert len(d['figures'])==31;assert len(d['sources'])==19;assert d['words']>=28000
used=set()
for c in d['chapters']:
 for s in c['sections']:assert 'id="'+s['id']+'"' in c['html']
 used.update(re.findall(r'data-diagram="(.*?)"',c['html']))
 assert '[diagram:' not in c['html'] and '[answer:' not in c['html'] and '[lab:' not in c['html']
 assert c['html'].count('<details')==c['html'].count('</details>')
for key in d['figures']:ET.parse(root/'dist/diagrams'/f'{key}.svg')
assert used==set(d['figures']),(used ^ set(d['figures']))
for source in d['sources']:
 if source.get('external'):assert source['url'].startswith('https://supply-chain-study-lab.open-pike-1567.chatgpt.site/sources/')
 else:assert (root/'dist'/source['url']).stat().st_size>1000
for e in d['glossary']:assert e['exact'] and e['simple'] and e['example'] and e['note']
import fitz
def norm(t):return re.sub(r'\s+',' ',re.sub(r'(\w)-\s*\n\s*(\w)',r'\1-\2',t)).strip()
papers=d['pastExams']['papers'];assert len(papers)==3
question_ids=set();compared_papers=0
for paper in papers:
 assert [q['points'] for q in paper['questions']]==[5,5,10,10]
 original=root/'source-material/exams'/paper['file'];text=None
 if original.exists():
  published=root/'dist'/paper['url']
  assert hashlib.sha256(original.read_bytes()).digest()==hashlib.sha256(published.read_bytes()).digest()
  pdf=fitz.open(original);text=norm(' '.join(p.get_text() for p in pdf));compared_papers+=1
 else:assert paper['url'].startswith('https://supply-chain-study-lab.open-pike-1567.chatgpt.site/sources/exams/')
 for q in paper['questions']:
  assert q['id'] not in question_ids;question_ids.add(q['id'])
  if text is not None:assert norm(q['prompt']) in text,(paper['file'],q['prompt'])
  assert q['answer'] and q['checklist'] and q['memory'] and q['pitfall']
  for link in q['links']:
   page,_,section=link['id'].partition('/')
   if page=='lab':continue
   ch=next(c for c in d['chapters'] if c['id']==page)
   if section:assert any(s['id']==section for s in ch['sections']),(q['id'],link)
assert len(question_ids)==12
print(f'Content checks passed: 14 chapters, 28,000+ words, 31 referenced SVGs, 25 glossary entries, 19 source references and 12 complete questions. PDF wording comparison: {compared_papers}/3 locally available papers.')
