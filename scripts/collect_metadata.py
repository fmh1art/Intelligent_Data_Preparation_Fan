"""Fetch publisher-deposited metadata; keep raw responses and endpoints for audit."""
import json, re, time
from pathlib import Path
from urllib.parse import quote
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'editorial' / 'metadata'
OUT.mkdir(parents=True, exist_ok=True)
queries = {
 'dm4ml':'Data Management for Machine Learning: A Survey',
 'aurum':'Aurum: A Data Discovery System',
 'sato':'Sato: Contextual Semantic Type Detection in Tables',
 'ditto':'Deep Entity Matching with Pre-Trained Language Models',
 'snorkel':'Snorkel: Rapid Training Data Creation with Weak Supervision',
 'raha':'Raha: A Configuration-Free Error Detection System',
 'activeclean':'ActiveClean: Interactive Data Cleaning For Statistical Modeling',
 'interactiveclean':'Interactive and Deterministic Data Cleaning: A Tossed Stone Raises a Thousand Ripples',
 'icl_er':'Cost-Effective In-Context Learning for Entity Resolution: A Design Space Exploration',
 'prepbench_final':'PrepBench: How Far Are We from Natural-Language-Driven Data Preparation?',
 'empower':'Empowering Tabular Data Preparation with Language Models: Why and How?',
}
text = (ROOT / 'references.bib').read_text()
requests_to_make = []
for block in re.split(r'(?=@\w+\{)', text):
 key = re.match(r'@\w+\{([^,]+),', block)
 doi = re.search(r'doi=\{([^}]+)\}', block)
 if key and doi:
  requests_to_make.append((key[1], 'https://api.crossref.org/works/' + quote(doi[1],safe=''), None))
for key, query in queries.items():
 requests_to_make.append((key, 'https://api.crossref.org/works', {'query.bibliographic':query,'rows':3}))
for key, url, params in requests_to_make:
 dest = OUT / (key+'.json')
 if dest.exists():
  continue
 try:
  r = requests.get(url, params=params, timeout=40, headers={'User-Agent':'AcademicSurveyCitationAudit/1.0'})
  if r.status_code == 429:
   time.sleep(3)
   r = requests.get(url, params=params, timeout=40)
  result = {'database':'Crossref','endpoint':r.url,'retrieved':'2026-09-09','status_code':r.status_code,'response':r.json() if r.ok else r.text[:1000]}
  dest.write_text(json.dumps(result, ensure_ascii=False, indent=2))
  if r.ok:
   msg = result['response']['message']
   items = msg.get('items',[msg])
   for item in items:
    print(key, item.get('title'), item.get('DOI'),item.get('published'),item.get('volume'),item.get('issue'),item.get('page'), flush=True)
  else:
   print(key, 'FAILED',r.status_code,flush=True)
 except requests.RequestException as exc:
  print(key, type(exc).__name__,flush=True)
 time.sleep(.3)
