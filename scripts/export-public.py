"""Create a public static-site export without redistributing original document binaries."""
from pathlib import Path
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = Path(sys.argv[1]).resolve()
ORIGIN = 'https://supply-chain-study-lab.open-pike-1567.chatgpt.site'
if DEST == ROOT or DEST in ROOT.parents:
    raise SystemExit('Choose a separate export directory.')
DEST.mkdir(parents=True, exist_ok=True)
if any(DEST.iterdir()):
    raise SystemExit('Use an empty destination to preserve existing files.')
for name in ['content', 'dist', 'scripts']:
    for source in (ROOT/name).rglob('*'):
        if not source.is_file() or source.suffix.lower() in ['.pdf', '.docx', '.pyc'] or '__pycache__' in source.parts:
            continue
        target = DEST/source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
for name in ['README.md', 'index.html', '.gitignore', '.nojekyll', '.openai/hosting.json']:
    target=DEST/name;target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/name,target)

data=json.loads((DEST/'dist/course.json').read_text())
for source in data['sources']:
    if not source['url'].startswith('https://'):
        source['url']=ORIGIN+'/'+source['url']
    source['external']=True
for paper in data['pastExams']['papers']:
    if not paper['url'].startswith('https://'):
        paper['url']=ORIGIN+'/'+paper['url']
data['sourceNote']+=' Original document binaries remain in the private Study Lab; this public export links to them.'
(DEST/'dist/course.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
(DEST/'content/past-exams.json').write_text(json.dumps(data['pastExams'],ensure_ascii=False,indent=2)+'\n')
(DEST/'content/source-register.json').write_text(json.dumps([s for s in data['sources'] if s.get('kind')!='past-exam'],ensure_ascii=False,indent=2)+'\n')
readme=(DEST/'README.md').read_text()
readme=readme.replace('All 16 original course files plus the 3 past-exam PDFs available in the source reader.', 'Links to all 16 original course files and 3 past-exam PDFs in the private Study Lab. Original document binaries are excluded from this public repository.')
readme=readme.replace('Original PDFs become available offline after opening them online.', 'Original documents remain in the private Study Lab and are not part of this public export’s offline cache.')
readme=readme.replace('`source-material/` retains the supplied originals; the exam PDFs are in `source-material/exams/`.', 'The private source checkout retains `source-material/`. This public export rebuilds from the recorded glossary data and source register in `content/`; its document links point to the private Study Lab.')
(DEST/'README.md').write_text(readme)
with (DEST/'.gitignore').open('a') as f:f.write('\n# Keep original document binaries in the private Study Lab.\nsource-material/\ndist/sources/\n')
print(json.dumps({'export':str(DEST),'files':sum(p.is_file() for p in DEST.rglob('*')),'original_document_binaries':0}))
