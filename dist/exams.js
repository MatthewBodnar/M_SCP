'use strict';
// Practice data stays on this device, separately from chapter progress.
const examStore = readExamStore();
let examTimerInterval;

function readExamStore() {
  try {
    const saved = JSON.parse(localStorage.getItem('supply-lab-github-practice-v1')) || {};
    return {drafts: saved.drafts || {}, checks: saved.checks || {}, elapsed: Number(saved.elapsed) || 0, started: Number(saved.started) || null};
  } catch { return {drafts: {}, checks: {}, elapsed: 0, started: null}; }
}
function saveExamStore() {
  try { localStorage.setItem('supply-lab-github-practice-v1', JSON.stringify(examStore)); return true; }
  catch { return false; }
}
function examQuestions() { return course.practiceExams.papers.flatMap(p => p.questions.map(q => ({...q, paper: p}))); }
function examTopicCounts() {
  const counts = {};
  examQuestions().forEach(q => counts[q.topic] = (counts[q.topic] || 0) + 1);
  return Object.entries(counts).sort((a,b) => b[1]-a[1] || a[0].localeCompare(b[0]));
}
function practiceSpotlight(){return `<section class="past-spotlight"><div><span class="eyebrow">New questions · Familiar exam format</span><h2>Three short practice papers.</h2><p>Each has two 5-point and two 10-point questions. Write first, then check the short study answer.</p></div><a class="btn primary" href="#practice">Try a paper ↗</a></section>`}
function renderPracticeExams(){const data=course.practiceExams;return `<div class="page-heading"><div class="eyebrow">New questions based on the lectures</div><h1>Practise clear answers.</h1><p>Try one full paper or choose a topic. Your answers stay on this device.</p></div><div class="exam-overview"><div class="exam-score"><strong>2 × 5 + 2 × 10</strong><span>30 points · A 27–30 · B 24–26 · C 21–23 · D 19–20 · E 18 · FX 0–17</span></div><div class="exam-timer"><span>Practice stopwatch</span><output id="examTimer" aria-label="Practice elapsed time">00:00</output><div><button class="btn" id="examTimerToggle">Start</button><button class="btn" id="examTimerReset">Reset</button></div></div></div><details class="exam-guidance"><summary>How to use these questions</summary><p>${escapeHTML(data.note)}</p><p><strong>Describe:</strong> explain the idea. <strong>Exemplify:</strong> give an example. <strong>Discuss:</strong> explain benefits, limits or conditions.</p><p>For a calculation, show the formula, working, units and meaning.</p></details><div class="exam-paper-links">${data.papers.map(p=>`<button class="btn" data-pick-paper="${p.id}">${escapeHTML(p.title)} · 30 points</button>`).join('')}<button class="btn" id="exportExamDrafts">Download my answers ↓</button><a class="btn" href="#sources">Open old exam PDFs ↗</a></div><div class="exam-filter-bar"><label>Paper<select id="examPaperFilter"><option value="all">All practice papers</option>${data.papers.map(p=>`<option value="${p.id}">${escapeHTML(p.title)}</option>`).join('')}</select></label><label>Topic<select id="examTopicFilter"><option value="all">All topics</option>${examTopicCounts().map(([t])=>`<option>${escapeHTML(t)}</option>`).join('')}</select></label><label>Points<select id="examPointsFilter"><option value="all">5 and 10 points</option><option value="5">5 points</option><option value="10">10 points</option></select></label><output id="examCount" aria-live="polite">12 questions</output><button class="btn" id="examFilterReset">Show all</button></div><div class="exam-question-list">${examQuestions().map(q=>renderExamQuestion(q)).join('')}</div><p id="examEmpty" class="empty-state" hidden>No matching questions. Select Show all to reset.</p>`}
function renderExamQuestion(q) {
  const draft = examStore.drafts[q.id] || '';
  const checks = examStore.checks[q.id] || [];
  return `<article class="exam-question" id="${q.id}" data-paper="${q.paper.id}" data-topic="${escapeHTML(q.topic)}" data-points="${q.points}">
  <div class="exam-question-top"><span>${escapeHTML(q.paper.title)} · Question ${q.number}</span><span class="exam-points">${q.points} points</span></div>
  <span class="exam-topic">${escapeHTML(q.topic)}</span><h2>${escapeHTML(q.prompt)}</h2><p class="exam-plain"><strong>What it asks:</strong> ${escapeHTML(q.plain)}</p>
  <details class="exam-hint"><summary>Show a memory cue</summary><p>${escapeHTML(q.memory)}</p></details>
  <label class="exam-draft-label" for="draft-${q.id}">Your answer</label><textarea id="draft-${q.id}" data-draft="${q.id}" rows="5" placeholder="Write your answer. Add a short example when asked…">${escapeHTML(draft)}</textarea><div class="exam-draft-meta"><span data-save-status="${q.id}">${draft?'Draft restored on this device':'Saves on this device as you type'}</span><span data-word-count="${q.id}">${countExamWords(draft)} words</span></div>
  <details class="exam-answer"><summary>Show study answer · ${q.points} points</summary><div class="exam-model">${q.answer.map(p=>`<p>${escapeHTML(p)}</p>`).join('')}<p class="exam-pitfall"><strong>Watch out:</strong> ${escapeHTML(q.pitfall)}</p><p class="exam-model-note">A study answer, not an official marking scheme. Use your own words.</p></div></details>
  <details class="exam-checks"><summary>Check your answer</summary><div>${q.checklist.map((item,i)=>`<label><input type="checkbox" data-check-question="${q.id}" data-check-index="${i}" ${checks.includes(i)?'checked':''}><span>${escapeHTML(item)}</span></label>`).join('')}</div></details>
  <div class="exam-related"><span>Revise the concept:</span>${q.links.map(l=>`<a href="#${l.id}">${escapeHTML(l.label)} ↗</a>`).join('')}</div></article>`;
}
function countExamWords(text) { return text.trim() ? text.trim().split(/\s+/).length : 0; }
function examElapsed() { return examStore.elapsed + (examStore.started ? Math.max(0,Date.now()-examStore.started) : 0); }
function formatExamTime(ms) { const s=Math.floor(ms/1000); return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0'); }
function mountPracticeExams(section) {
  // A search result's deep link must remain visible even after earlier filtering.
  const reset = () => { ['examPaperFilter','examTopicFilter','examPointsFilter'].forEach(id=>document.getElementById(id).value='all'); filter(); };
  const filter = () => {
    const paper=$('#examPaperFilter').value, topic=$('#examTopicFilter').value, points=$('#examPointsFilter').value;
    let count=0;
    $$('.exam-question').forEach(el=>{el.hidden=!((paper==='all'||el.dataset.paper===paper)&&(topic==='all'||el.dataset.topic===topic)&&(points==='all'||el.dataset.points===points));if(!el.hidden)count++;});
    $('#examCount').textContent=count+' question'+(count===1?'':'s'); $('#examEmpty').hidden=count!==0;
  };
  ['examPaperFilter','examTopicFilter','examPointsFilter'].forEach(id=>document.getElementById(id).onchange=filter);
  $('#examFilterReset').onclick=reset;
  $$('[data-pick-paper]').forEach(b=>b.onclick=()=>{$('#examPaperFilter').value=b.dataset.pickPaper;$('#examTopicFilter').value='all';$('#examPointsFilter').value='all';filter();document.querySelector('.exam-question:not([hidden])')?.scrollIntoView();});
  $$('[data-draft]').forEach(input=>input.oninput=()=>{
    const id=input.dataset.draft;examStore.drafts[id]=input.value;
    const saved=saveExamStore();
    $(`[data-save-status="${id}"]`).textContent=saved?'Saved on this device':'Could not save. Download your answers to keep a copy.';
    $(`[data-word-count="${id}"]`).textContent=countExamWords(input.value)+' words';
  });
  $$('[data-check-question]').forEach(input=>input.onchange=()=>{
    const id=input.dataset.checkQuestion;
    examStore.checks[id]=$$(`[data-check-question="${id}"]`).filter(c=>c.checked).map(c=>Number(c.dataset.checkIndex));
    if(!saveExamStore())toast('This browser could not save your self-checks.');
  });
  const tick=()=>{if(!$('#examTimer')){clearInterval(examTimerInterval);return;}$('#examTimer').textContent=formatExamTime(examElapsed());$('#examTimerToggle').textContent=examStore.started?'Pause':'Start';};
  $('#examTimerToggle').onclick=()=>{if(examStore.started){examStore.elapsed=examElapsed();examStore.started=null;}else examStore.started=Date.now();saveExamStore();tick();};
  $('#examTimerReset').onclick=()=>{examStore.elapsed=0;examStore.started=null;saveExamStore();tick();};
  clearInterval(examTimerInterval);examTimerInterval=setInterval(tick,1000);tick();
  $('#exportExamDrafts').onclick=()=>{
    const text=['# My Supply Lab practice answers','',...examQuestions().flatMap(q=>[`## ${q.paper.title} · Q${q.number} · ${q.points} points`,q.prompt,'',examStore.drafts[q.id]||'(No answer written yet.)',''])].join('\n');
    const url=URL.createObjectURL(new Blob([text],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='my-exam-practice-answers.txt';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  };
  if(section)reset();
}
function indexPracticeExams() {
  for(const q of examQuestions())searchIndex.push({title:q.topic+' · '+q.paper.title+' Q'+q.number,chapter:'Practice · '+q.points+' points',url:'practice/'+q.id,text:[q.prompt,q.plain,q.memory,...q.answer,...q.checklist,q.pitfall].join(' ')});
}
