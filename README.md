# Supply Lab — seven-lecture GitHub edition

Seven short chapters follow the seven lecture PDFs. Each chapter links its lecture and recommended readings, keeps the source definitions, and uses short explanations with Campus Tees examples.

This repository is independent of the shared ChatGPT Study Lab. The shared website keeps its existing 14-chapter version. This GitHub edition has no hosted Site project ID and is not deployed to that Site.

## Chapters

1. Introduction to marketing and industrial marketing — lecture and module reading list. No separate paper is named in these slides.
2. SCM and strategy fundamentals — Christopher's chapter 1 excerpt and Barney (1991), matched to the module reading list by topic.
3. Purchasing and supply management — Gadde & Håkansson (1994) and Kraljic (1983).
4. Inventory management — glossary and the recommended Panigrahi et al. (2024) review. The full review PDF was not uploaded; the chapter clearly labels its short publisher-abstract summary and links the publisher.
5. Operations management — glossary and Naylor, Naim & Berry (1999).
6. Industrial networks — Ford & Mouzas (2013).
7. Negotiations — Larsson (2020).

The chapter text is about 4,100 words. Explanations aim at B2 English or simpler. Formal course terms remain, with simple meanings beside them. Source quotations, paper titles and exact glossary text keep the original wording.

## Practice and tools

- Three new practice papers, each with two 5-point and two 10-point questions.
- Twelve fresh prompts and short study answers, with saved drafts, answer checks and a stopwatch.
- The original past-exam questions are not reused in the new practice bank. The three original PDFs remain in Sources.
- All 25 glossary entries keep their exact source text and have short meanings and Campus Tees examples.
- Eighteen selected diagrams appear in the chapters. All 31 original SVG files remain in the repository.
- EOQ, reorder-point and break-even calculators, a Kraljic explorer, search, text-size controls and dark mode.
- All 19 original uploaded documents remain available, including lecture PDFs, reading PDFs, the glossary and the old exam PDFs.

The questions and answers are study material, not official grading rubrics or predictions of the next exam.

## Run or host

The ready-to-use static website is in `dist/` and has no JavaScript package dependencies.

```sh
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. Use an HTTP server, because the app loads `course.json` with `fetch`.

GitHub Pages can publish **main → / (root)**. The root `index.html` forwards to `dist/`. `.nojekyll` is included. Any other static host can serve `dist/` directly.

## Edit and check

`content/lectures.json` maps the seven lectures to the original files and readings. The seven Markdown files contain the short chapters. `content/practice-exams.json` contains the new question bank. `content/glossary-data.json` keeps the exact glossary and simple explanations. `source-material/` keeps the original uploads.

The build uses Python with `PyMuPDF`. Checking glossary source text also uses `python-docx`.

```sh
python3 scripts/build.py
python3 scripts/check.py
node --check dist/app.js
node --check dist/exams.js
node scripts/check-calculations.cjs
```

`python3 scripts/diagrams.py` can regenerate the original 31 SVG assets. The build selects the ones used by the short chapters.

The checks verify the seven lecture links, reading links, source files, exact glossary text, new practice-paper structure, chapter anchors and diagram references. They also check that no new prompt copies a supplied past-exam question.

## Source scope and local data

The original authors retain rights to their documents. The owner explicitly approved publishing the 19 uploaded originals in this public repository. The missing inventory review is linked through the publisher; it has not been added as an uploaded PDF.

Progress, preferences and practice drafts stay in the browser's local storage. They do not sync to another device or to the separate shared Study Lab. Use **Download my answers** to keep a text copy. The core website and selected diagrams work offline after an online visit. Original source files are cached after they are opened online.
