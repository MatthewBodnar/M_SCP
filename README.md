# Supply Lab — Marketing & Supply Chain Management

A complete interactive revision website for the supplied Module 5 lectures, readings, glossary and past papers.

**Live website:** https://supply-chain-study-lab.open-pike-1567.chatgpt.site

**Repository:** https://github.com/MatthewBodnar/M_SCP

- 33,259 words of chapters, glossary explanations and past-exam practice.
- 14 connected chapters and 31 scalable SVG diagrams with zoom, pan and reset.
- All 25 glossary entries, retaining the original wording alongside simpler explanations and examples.
- EOQ, reorder-point and break-even calculators and an interactive Kraljic explorer.
- All 12 questions from the three supplied Inspera papers, checked against the original PDFs.
- Model answers, memory cues, coverage checklists, paper/topic/point filters and a practice stopwatch.
- Device-local answer drafts and self-checks, with an answer download button.
- Full-course search including past-exam answers, text-size controls, focus/dark modes and reading progress.
- Links to all 16 original course files and 3 past-exam PDFs in the private Study Lab. Original document binaries are excluded from this public repository.
- Responsive layouts and offline caching of the core website and diagrams after an initial online visit. Original documents remain in the private Study Lab and are not part of this public export’s offline cache.

## Run

The ready-to-use website is in `dist/`. It has no JavaScript package dependencies or backend.

```sh
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. Use HTTP, since course data is loaded with `fetch`; opening an HTML file directly is insufficient.

## Edit and rebuild

`content/` contains the 14 chapter Markdown files and `past-exams.json`. The latter retains the exact question wording, original point values, teaching answers, checklist items and chapter links. The private source checkout retains `source-material/`. This public export rebuilds from the recorded glossary data and source register in `content/`; its document links point to the private Study Lab.

The build requires Python packages `python-docx` and `PyMuPDF`. The output is committed, so rebuilding is optional when hosting or reading.

```sh
python3 scripts/diagrams.py
python3 scripts/build.py
python3 scripts/check.py
node --check dist/app.js
node --check dist/exams.js
node scripts/check-calculations.cjs
```

`scripts/check.py` validates all chapters, glossary entries, diagram references and source files, compares all 12 question prompts with their PDFs, checks the 5/5/10/10 point structure and verifies links to specific course sections. Calculation checks cover worked values, changed inputs and invalid inputs.

## Hosting

Any static host can serve `dist/` unchanged. Relative asset paths support a project subdirectory. To use GitHub Pages, select **Settings → Pages → Deploy from a branch → main → / (root)**; the root `index.html` forwards visitors into `dist/`. GitHub Pages must be enabled in repository settings; uploading this repository alone does not enable it. The live website above is already published separately. `.openai/hosting.json` retains its existing Site identity and output configuration.

There is no analytics service or external runtime dependency. Progress, answers and preferences remain in the browser's `localStorage`; they do not synchronise across devices or origins. Changing hosts does not carry existing saved drafts to the new address. Use **Download my answers** to retain a text copy.

## Sources and scope

The original course draws on the uploaded lectures, the operations/inventory glossary and readings by Barney; Christopher; Ford & Mouzas; Gadde & Håkansson; Kraljic; Naylor, Naim & Berry; and Larsson. Original authors retain rights to their documents. The exact source wording, simplified explanations, invented cases and historical examples are identified in the website.

The initial 28,094-word website was rebuilt from the recovered 16 uploads after the earlier working draft was lost. This edition preserves that material and adds the three supplied past papers and expanded explanations for bullwhip, risk, sustainability and SCOR. The SCOR and bullwhip sections identify supplementary primary references. Classic SCOR and the current Digital Standard are distinguished because the supplied papers do not specify a version. The separate Panigrahi et al. review named on a slide and optional background readings were not provided as full texts.

The dates and official marking schemes of the three past papers were not supplied. Model answers and self-checks are study material, not official grading rubrics. Topic counts describe the supplied papers and do not predict the next exam. Announced grade thresholds are retained from the teacher's information.
