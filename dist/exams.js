'use strict';
// Practice data stays on this device, separately from chapter progress.
const examStore = readExamStore();
let examTimerInterval;

function readExamStore() {
  try {
    const saved = JSON.parse(localStorage.getItem('supply-lab-exams-v1')) || {};
    return {drafts: saved.drafts || {}, checks: saved.checks || {}, elapsed: Number(saved.elapsed) || 0, started: Number(saved.started) || null};
  } catch { return {drafts: {}, checks: {}, elapsed: 0, started: null}; }
}
function saveExamStore() {
  try { localStorage.setItem('supply-lab-exams-v1', JSON.stringify(examStore)); return true; }
  catch { return false; }
}
function examQuestions() { return course.pastExams.papers.flatMap(p => p.questions.map(q => ({...q, paper: p}))); }
function examTopicCounts() {
  const counts = {};
  examQuestions().forEach(q => counts[q.topic] = (counts[q.topic] || 0) + 1);
  return Object.entries(counts).sort((a,b) => b[1]-a[1] || a[0].localeCompare(b[0]));
}
function pastExamSpotlight() {
  if (!course.pastExams) return '';
  return `<section class="past-spotlight"><div><span class="eyebrow">New · From your actual past papers</span><h2>12 questions. Three complete papers.</h2><p>Write your answer, reveal a model and check the missing pieces. Start with the repeated themes: bullwhip, purchasing and risk.</p></div><a class="btn primary" href="#past-exams">Open past exams ↗</a></section>`;
}
function renderPastExams() {
  const data = course.pastExams;
  return `<div class="page-heading"><div class="eyebrow">Your three supplied Inspera papers</div><h1>Practise the real questions.</h1><p>Try an answer before revealing the model. Your drafts and self-checks stay on this device. Each paper has 4 questions and 30 points.</p></div>
  <div class="exam-overview"><div class="exam-score"><strong>2 × 5 + 2 × 10</strong><span>30 points per paper · A 27–30 · B 24–26 · C 21–23 · D 19–20 · E 18 · FX 0–17</span></div><div class="exam-timer"><span>Practice stopwatch</span><output id="examTimer" aria-label="Practice elapsed time">00:00</output><div><button class="btn" id="examTimerToggle">Start</button><button class="btn" id="examTimerReset">Reset</button></div></div></div>
  <details class="exam-guidance"><summary>What these papers tell you</summary><p>${escapeHTML(data.note)}</p><p>Repeated themes deserve practice. They do not establish the next paper's content. Five-point answers need clear definitions and examples; ten-point answers should develop mechanisms, application and discussion when asked.</p><div class="exam-topic-list">${examTopicCounts().map(([t,n])=>`<span>${escapeHTML(t)} <b>${n} / 12</b></span>`).join('')}</div></details>
  <div class="exam-paper-links">${data.papers.map(p=>`<a class="btn" href="${p.url}" target="_blank" rel="noopener">${escapeHTML(p.title)} · Original PDF ↗</a>`).join('')}<button class="btn" id="exportExamDrafts">Download my answers ↓</button></div>
  <div class="exam-filter-bar"><label>Paper<select id="examPaperFilter"><option value="all">All three papers</option>${data.papers.map(p=>`<option value="${p.id}">${escapeHTML(p.title)}</option>`).join('')}</select></label><label>Topic<select id="examTopicFilter"><option value="all">All topics</option>${examTopicCounts().map(([t])=>`<option>${escapeHTML(t)}</option>`).join('')}</select></label><label>Points<select id="examPointsFilter"><option value="all">5 and 10 points</option><option value="5">5 points</option><option value="10">10 points</option></select></label><output id="examCount" aria-live="polite">12 questions</output><button class="btn" id="examFilterReset">Show all</button></div>
  <div class="exam-question-list">${examQuestions().map(q=>renderExamQuestion(q)).join('')}</div><p id="examEmpty" class="empty-state" hidden>No questions match these filters. Select Show all to reset.</p>
  <details class="exam-guidance"><summary>Sources for the added explanations</summary><p>The original course readings remain in Original sources. Bullwhip and SCOR are supplemented with these primary references; the risk and sustainability cases are illustrative applications.</p>${data.references.map(r=>`<p><a class="exam-reference" href="${escapeHTML(r.url)}" target="_blank" rel="noopener">${escapeHTML(r.title)} ↗</a><br>${escapeHTML(r.scope)}</p>`).join('')}</details>`;
}
function renderExamQuestion(q) {
  const draft = examStore.drafts[q.id] || '';
  const checks = examStore.checks[q.id] || [];
  return `<article class="exam-question" id="${q.id}" data-paper="${q.paper.id}" data-topic="${escapeHTML(q.topic)}" data-points="${q.points}">
  <div class="exam-question-top"><span>${escapeHTML(q.paper.title)} · Question ${q.number}</span><span class="exam-points">${q.points} points</span></div>
  <span class="exam-topic">${escapeHTML(q.topic)}</span><h2>${escapeHTML(q.prompt)}</h2><p class="exam-plain"><strong>What it asks:</strong> ${escapeHTML(q.plain)}</p>
  <details class="exam-hint"><summary>Show a memory cue</summary><p>${escapeHTML(q.memory)}</p></details>
  <label class="exam-draft-label" for="draft-${q.id}">Your answer</label><textarea id="draft-${q.id}" data-draft="${q.id}" rows="5" placeholder="Explain the idea in your own words, add an example, and discuss the trade-offs when asked…">${escapeHTML(draft)}</textarea><div class="exam-draft-meta"><span data-save-status="${q.id}">${draft?'Draft restored on this device':'Saves on this device as you type'}</span><span data-word-count="${q.id}">${countExamWords(draft)} words</span></div>
  <details class="exam-answer"><summary>Reveal model answer · ${q.points} points</summary><div class="exam-model">${q.answer.map(p=>`<p>${escapeHTML(p)}</p>`).join('')}<p class="exam-pitfall"><strong>Watch out:</strong> ${escapeHTML(q.pitfall)}</p><p class="exam-model-note">Study model, not an official marking scheme. Use the concepts and reasoning; there is no required word count supplied.</p></div></details>
  <details class="exam-checks"><summary>Self-check your coverage</summary><div>${q.checklist.map((item,i)=>`<label><input type="checkbox" data-check-question="${q.id}" data-check-index="${i}" ${checks.includes(i)?'checked':''}><span>${escapeHTML(item)}</span></label>`).join('')}</div></details>
  <div class="exam-related"><span>Revise the concept:</span>${q.links.map(l=>`<a href="#${l.id}">${escapeHTML(l.label)} ↗</a>`).join('')}</div></article>`;
}
function countExamWords(text) { return text.trim() ? text.trim().split(/\s+/).length : 0; }
function examElapsed() { return examStore.elapsed + (examStore.started ? Math.max(0,Date.now()-examStore.started) : 0); }
function formatExamTime(ms) { const s=Math.floor(ms/1000); return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0'); }
function mountPastExams(section) {
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
  $$('[data-draft]').forEach(input=>input.oninput=()=>{
    const id=input.dataset.draft;examStore.drafts[id]=input.value;
    const saved=saveExamStore();
    $(`[data-save-status="${id}"]`).textContent=saved?'Saved on this device':'Could not save on this device. Download your answers to keep a copy.';
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
function indexPastExams() {
  for(const q of examQuestions())searchIndex.push({title:q.topic+' · '+q.paper.title+' Q'+q.number,chapter:'Past exams · '+q.points+' points',url:'past-exams/'+q.id,text:[q.prompt,q.plain,q.memory,...q.answer,...q.checklist,q.pitfall].join(' ')});
}
