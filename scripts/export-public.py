"""Export the complete website and original documents approved for public publication."""
from pathlib import Path
import json
import shutil
import sys

ROOT=Path(__file__).resolve().parents[1]
DEST=Path(sys.argv[1]).resolve()
if DEST==ROOT or DEST in ROOT.parents:
    raise SystemExit('Choose a separate export directory.')
DEST.mkdir(parents=True,exist_ok=True)
if any(DEST.iterdir()):
    raise SystemExit('Use an empty destination to preserve existing files.')
for name in ['content','dist','scripts','source-material']:
    for source in (ROOT/name).rglob('*'):
        if not source.is_file() or source.suffix=='.pyc' or '__pycache__' in source.parts:
            continue
        target=DEST/source.relative_to(ROOT)
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
for name in ['README.md','index.html','.gitignore','.nojekyll','.openai/hosting.json']:
    target=DEST/name;target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/name,target)
print(json.dumps({'export':str(DEST),'files':sum(p.is_file() for p in DEST.rglob('*')),'original_documents':19}))
