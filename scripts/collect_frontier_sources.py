"""Cache primary-source metadata for the revision based on the uploaded DOCX."""
from pathlib import Path
import json
import time
import requests
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'editorial/frontier_sources'
OUT.mkdir(exist_ok=True)
session = requests.Session()
session.headers['User-Agent'] = 'DataPreparationSurvey/1.0 (academic bibliography verification)'
log = []

def get(key, url, params=None, extension='json'):
    try:
        response = session.get(url, params=params, timeout=35)
        (OUT / (key + '.' + extension)).write_bytes(response.content)
        record = dict(key=key, url=response.url, status=response.status_code)
        log.append(record)
        print(key, response.status_code, flush=True)
        response.raise_for_status()
        return response
    except Exception as exc:
        log.append(dict(key=key, error=str(exc)))
        print(key, type(exc).__name__, flush=True)
        return None

ids = '2310.08864,2403.12945,2310.17596,2503.06669,2512.24653,2506.20920,2506.04178,2406.11794,2402.04333'
r = get('arxiv_batch', 'https://export.arxiv.org/api/query',
        {'id_list': ids, 'max_results': 20}, 'xml')
if r is not None:
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    entries = []
    for item in ET.fromstring(r.content).findall('a:entry', ns):
        entries.append({
            'id': item.findtext('a:id', namespaces=ns),
            'title': item.findtext('a:title', namespaces=ns),
            'summary': item.findtext('a:summary', namespaces=ns),
            'published': item.findtext('a:published', namespaces=ns),
            'updated': item.findtext('a:updated', namespaces=ns),
            'authors': [a.findtext('a:name', namespaces=ns) for a in item.findall('a:author', ns)]})
    (OUT / 'arxiv_parsed.json').write_text(json.dumps(entries, ensure_ascii=False, indent=2))

queries = {
    'nalir': 'An Interactive Natural Language Interface for Querying Relational Databases',
    'rag': 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks',
    'demonstrations': 'What Makes Good In-Context Examples for GPT-3',
    'collapse': 'AI models collapse when trained on recursively generated data',
    'doremi': 'DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining',
}
for key, title in queries.items():
    r = get(key, 'https://api.crossref.org/works', {'query.title': title, 'rows': 3})
    if r is not None:
        for item in r.json()['message']['items'][:2]:
            print(' ', item.get('title'), item.get('DOI'), flush=True)
    time.sleep(0.3)

pages = {
    'dolma': 'https://aclanthology.org/2024.acl-long.840.bib',
    'selfinstruct': 'https://aclanthology.org/2023.acl-long.754.bib',
    'picard': 'https://aclanthology.org/2021.emnlp-main.779.bib',
    'less': 'https://proceedings.mlr.press/v235/xia24c.html',
    'dinsql': 'https://proceedings.neurips.cc/paper_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html',
    'dclm': 'https://proceedings.neurips.cc/paper_files/paper/2024/hash/19e4ea30dded58259665db375885e412-Abstract-Datasets_and_Benchmarks_Track.html',
    'datajuicer2': 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/76dbd7e897be2eb883ede598b91270fb-Abstract-Datasets_and_Benchmarks_Track.html',
    'agibot2026': 'https://huggingface.co/datasets/agibot-world/AgiBotWorld2026/raw/main/README.md',
    'agibot2026_release': 'https://www.agibot.com/article/231/detail/54.html',
    'droid_project': 'https://droid-dataset.github.io/',
    'oxe_project': 'https://robotics-transformer-x.github.io/',
    'mimicgen_project': 'https://mimicgen.github.io/',
}
for key, url in pages.items():
    get(key, url, extension='bib' if url.endswith('.bib') else 'txt')

(OUT / 'requests.json').write_text(json.dumps(log, ensure_ascii=False, indent=2))
