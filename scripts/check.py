from pathlib import Path
from collections import Counter
import re,json,hashlib,xml.etree.ElementTree as ET
import fitz
from docx import Document
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'dist/course.json').read_text())
lectures=json.loads((root/'content/lectures.json').read_text())
assert len(d['chapters'])==len(lectures)==7
assert len(list((root/'content').glob('*.md')))==7
assert len(d['glossary'])==25 and len(d['sources'])==19
assert sum(c['words'] for c in d['chapters'])<5000
sources={s['url']:s for s in d['sources']}
lecture_sources={s['url'] for s in d['sources'] if s['title'].startswith('Sub-module')}
assert {c['lectureUrl'] for c in d['chapters']}==lecture_sources
used=set();chapter_ids={c['id'] for c in d['chapters']}
for number,c in enumerate(d['chapters'],1):
 assert c['number']==number and c['id']==lectures[number-1]['id']
 assert 'Campus Tees' in c['html']
 for section in c['sections']:assert 'id="'+section['id']+'"' in c['html']
 for reading in c['readings']:
  if reading.get('external'):
   assert reading['url'].startswith('https://www.emerald.com/') and reading['available'] is False
   assert 'Abstract only' in reading['note']
  else:assert reading['url'] in sources
 used.update(re.findall(r'data-diagram="(.*?)"',c['html']))
 assert not re.search(r'\[(diagram|lab|answer):',c['html'])
 assert c['html'].count('<details')==c['html'].count('</details>')
assert used==set(d['figures'])
for key in used:ET.parse(root/'dist/diagrams'/f'{key}.svg')
def slug(t):return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
for original in (root/'source-material').glob('*'):
 if original.suffix not in ['.pdf','.docx']:continue
 published=root/'dist/sources'/(slug(original.stem)+original.suffix)
 assert hashlib.sha256(original.read_bytes()).digest()==hashlib.sha256(published.read_bytes()).digest()
for source in d['sources']:
 assert (root/'dist'/source['url']).stat().st_size>1000
 assert source['publicUrl'].startswith('https://github.com/MatthewBodnar/M_SCP/blob/main/dist/')
 assert source['downloadUrl'].startswith('https://raw.githubusercontent.com/MatthewBodnar/M_SCP/main/dist/')
# The exact definitions must still match the uploaded glossary, not our rewritten explanations.
terms={e['term'] for e in d['glossary']};original_entries={};current=None
for para in Document(next((root/'source-material').glob('*.docx'))).paragraphs:
 text=para.text
 if text.startswith('Appendix A'):break
 if text.strip() in terms:
  current=text.strip();original_entries[current]=[]
 elif current and text.strip():original_entries[current].append(text)
assert len(original_entries)==25
for e in d['glossary']:
 assert e['exact']=='\n\n'.join(original_entries[e['term']]),e['term']
 assert e['simple'] and e['example'] and e['note']
# Read the supplied papers directly to check that the new bank does not copy their prompts.
def norm(t):return re.sub(r'[^a-z0-9]+',' ',t.lower()).strip()
original_text=[]
for paper in d['pastPapers']:
 original=root/'source-material/exams'/paper['file'];published=root/'dist'/paper['url']
 assert hashlib.sha256(original.read_bytes()).digest()==hashlib.sha256(published.read_bytes()).digest()
 original_text.append(norm(' '.join(p.get_text() for p in fitz.open(original))))
questions=[]
assert len(d['practiceExams']['papers'])==3
for paper in d['practiceExams']['papers']:
 assert [q['points'] for q in paper['questions']]==[5,5,10,10]
 for q in paper['questions']:
  assert all(norm(q['prompt']) not in text for text in original_text)
  assert q['answer'] and q['checklist'] and q['plain'] and q['memory']
  assert len(' '.join(q['answer']).split())<=160
  for link in q['links']:assert link['id'] in chapter_ids
  questions.append(q['id'])
assert len(questions)==len(set(questions))==12
assert 'pastExams' not in d
assert 'project_id' not in json.loads((root/'.openai/hosting.json').read_text())
print('Passed: 7 lecture chapters; reading links; 25 unchanged source definitions; 19 unchanged original files; 18 used diagrams; 12 fresh questions in three 5/5/10/10 papers; GitHub edition detached from hosted Site.')
