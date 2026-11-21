const QUESTIONS = [
  {id:"Q01", text:"Can AI hallucination be addressed by changing the architecture beneath the model?", terms:["CARA","reasoning","context","evidence","epistemic","citation"]},
  {id:"Q02", text:"How can we constrain AI as power while universalizing bounded capabilities?", terms:["AI","effect","authority","capability","sovereignty"]},
  {id:"Q03", text:"What comes after today’s application-centered computing stack?", terms:["sovereign","constitutional computing","computing","software","substrate","open source"]},
  {id:"Q04", text:"Can systems compose without silently dropping their constraints?", terms:["composition","constraint","translation","compiler","interface"]},
  {id:"Q05", text:"How can people regain inspectable, renegotiable control of their computers?", terms:["sovereign","user","authority","inspectable","reconstruct","software"]},
  {id:"Q06", text:"How can meaning survive translation across models, systems, and institutions?", terms:["meaning","semantic","translation","binding","continuity"]},
  {id:"Q07", text:"How do we turn a powerful idea into a testable, evidence-bearing system?", terms:["specification","configuration","implementation","evidence","realization"]},
  {id:"Q08", text:"What structures determine which futures can become real?", terms:["possibility","Dynatology","manifold","admissible","collapse"]},
];

let papers = [];
let territory = null;
let questionTerms = null;
const grid = document.querySelector("#paper-grid");
const count = document.querySelector("#library-count");
const search = document.querySelector("#search");
const sort = document.querySelector("#sort");
const filter = document.querySelector("#active-filter");
const dialog = document.querySelector("#paper-dialog");
const dialogContent = document.querySelector("#dialog-content");

function esc(value="") { return String(value).replace(/[&<>'"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[c])); }
function doiHref(value="") { const doi=String(value).trim(); if(/^https?:\/\//i.test(doi)) return doi; if(/^10\.\d{4,9}\//.test(doi)) return `https://doi.org/${doi}`; return ""; }
function href(path) { return `../${String(path).split("/").map(encodeURIComponent).join("/")}`; }
function haystack(p) { return [p.title,p.abstract_text,...(p.keywords||[]),...(p.profiles||[]),...(p.territories||[])].join(" ").toLowerCase(); }
function safeDescription(source="") {
  const allowed=new Set(["P","BR","EM","STRONG","B","I","UL","OL","LI","CODE","PRE","BLOCKQUOTE","A","H3","H4"]);
  const doc=new DOMParser().parseFromString(`<body>${source}</body>`,"text/html");
  [...doc.body.querySelectorAll("*")].forEach(node=>{
    if(!allowed.has(node.tagName)){node.replaceWith(...node.childNodes);return;}
    const link=node.tagName==="A"?node.getAttribute("href"):null;
    [...node.attributes].forEach(attr=>node.removeAttribute(attr.name));
    if(node.tagName==="A"){
      if(link&&/^https?:\/\//i.test(link)){node.setAttribute("href",link);node.setAttribute("rel","noopener noreferrer");}
    }
  });
  return doc.body.innerHTML;
}

function visiblePapers() {
  const query = search.value.trim().toLowerCase();
  let result = papers.filter(p => (!territory || p.territories.includes(territory)) && (!questionTerms || questionTerms.some(t => haystack(p).includes(t.toLowerCase()))) && (!query || haystack(p).includes(query)));
  if (sort.value === "chronology-desc") result.sort((a,b)=>(b.earliest_documented_timestamp||"").localeCompare(a.earliest_documented_timestamp||""));
  else if (sort.value === "chronology-asc") result.sort((a,b)=>(a.accession_number||0)-(b.accession_number||0));
  else if (sort.value === "date-desc") result.sort((a,b)=>(b.publication_date||"").localeCompare(a.publication_date||""));
  else if (sort.value === "date-asc") result.sort((a,b)=>(a.publication_date||"9999").localeCompare(b.publication_date||"9999"));
  else if (sort.value === "references") result.sort((a,b)=>(b.reference_count||0)-(a.reference_count||0));
  else result.sort((a,b)=>a.title.localeCompare(b.title));
  return result;
}

function render() {
  const visible = visiblePapers();
  count.textContent = `${visible.length} of ${papers.length} current editions`;
  grid.innerHTML = visible.map((p,i)=>`<button class="paper-card" data-index="${papers.indexOf(p)}"><div class="meta"><span>${esc(p.accession_id)} · ${esc(p.territories.join(" · "))}</span><span>${esc(p.earliest_documented_date||"DATE UNRESOLVED")}</span></div><h3>${esc(p.title)}</h3><p>${esc(p.abstract_text)}</p><div class="tags">${(p.profiles||[]).slice(0,4).map(x=>`<span>${esc(x)}</span>`).join("")}</div></button>`).join("") || `<p>No current edition matches this view.</p>`;
  grid.querySelectorAll(".paper-card").forEach(card => card.addEventListener("click",()=>openPaper(papers[Number(card.dataset.index)])));
}

function setFilter(label, nextTerritory=null, terms=null) {
  territory = nextTerritory;
  questionTerms = terms;
  document.querySelectorAll("nav button").forEach(b=>b.classList.toggle("active", b.dataset.territory===territory));
  if (label) { filter.hidden=false; filter.innerHTML=`${esc(label)} <button aria-label="Clear filter">×</button>`; filter.querySelector("button").onclick=()=>setFilter(null); }
  else { filter.hidden=true; filter.textContent=""; }
  render();
  document.querySelector("#library").scrollIntoView({behavior:"smooth"});
}

function openPaper(p) {
  const keywords=(p.keywords||[]).map(k=>`<span>${esc(k)}</span>`).join("");
  dialogContent.innerHTML=`<p class="eyebrow">${esc(p.accession_id)} · CURRENT INTEGRATED EDITION</p><h2>${esc(p.title)}</h2><p class="dialog-sub">${esc(p.authors.join(", "))} · Earliest documented ${esc(p.earliest_documented_date)}${p.publication_date?` · Published ${esc(p.publication_date)}`:""}${doiHref(p.doi)?` · <a href="${esc(doiHref(p.doi))}" target="_blank" rel="noopener noreferrer">Zenodo DOI</a>`:""}</p><div class="dialog-description">${safeDescription(p.description_html||`<p>${esc(p.abstract_text)}</p>`)}</div><div class="tags">${keywords}</div><div class="file-actions"><a href="${href(p.formats.pdf.path)}">Read PDF</a>${doiHref(p.doi)?`<a href="${esc(doiHref(p.doi))}" target="_blank" rel="noopener noreferrer">Zenodo record</a>`:""}<a href="${href(p.formats.html.path)}">Read HTML</a><a href="${href(p.formats.markdown.path)}">View Markdown</a><a href="${href(p.receipt_path)}">Receipt</a></div><div class="receipt">Chronology basis · ${esc(p.chronology_basis)} · ${esc(p.chronology_confidence)} confidence<br>Release root · ${esc(p.release_root_sha256)}<br>License · ${esc(p.license)} · Each format has its own SHA-256 in the detached receipt.</div>`;
  dialog.showModal();
}

document.querySelector("#question-grid").innerHTML=QUESTIONS.map(q=>`<button class="question" data-question="${q.id}"><small>${q.id}</small><strong>${esc(q.text)}</strong></button>`).join("");
document.querySelectorAll(".question").forEach(button=>button.addEventListener("click",()=>{const q=QUESTIONS.find(x=>x.id===button.dataset.question);setFilter(`${q.id} · ${q.text}`,null,q.terms)}));
document.querySelectorAll("[data-territory]").forEach(button=>button.addEventListener("click",()=>setFilter(button.dataset.territory,button.dataset.territory,null)));
document.querySelectorAll("[data-territory-card]").forEach(card=>card.addEventListener("click",()=>setFilter(card.dataset.territoryCard,card.dataset.territoryCard,null)));
search.addEventListener("input",render); sort.addEventListener("change",render);
dialog.querySelector(".close").addEventListener("click",()=>dialog.close());
dialog.addEventListener("click",event=>{if(event.target===dialog)dialog.close()});

fetch("../metadata/corpus.json").then(r=>{if(!r.ok)throw new Error(`${r.status} ${r.statusText}`);return r.json()}).then(data=>{papers=data.papers;render()}).catch(error=>{count.textContent="Corpus index unavailable";grid.innerHTML=`<p>Start the local server with <code>python tools/serve.py</code> and open <code>/site/</code>.<br>${esc(error.message)}</p>`});
