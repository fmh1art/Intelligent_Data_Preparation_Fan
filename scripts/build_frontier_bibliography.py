"""Assemble the cited bibliography from cached publisher/API records."""
from pathlib import Path
import json
import re
import requests
import bibtexparser
from lxml import html

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'editorial/frontier_sources'
records = {}
selection = {}

def parse_bib(text):
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    return bibtexparser.loads(text, parser=parser)

def fetch(key, url):
    path = P / (key + '.txt')
    if not path.exists():
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        path.write_bytes(r.content)
    return path.read_text()

def add(key, entry, source):
    entry = dict(entry)
    entry['ID'] = key
    for k in ['abstract', 'editor', 'month', 'pdf', 'series', 'address']:
        entry.pop(k, None)
    if 'year' in entry:
        entry['date'] = entry.pop('year')
    if 'journal' in entry:
        entry['journaltitle'] = entry.pop('journal')
    if entry.get('doi'):
        entry.pop('url', None)
    records[key] = entry
    selection[key] = source

body = (ROOT / 'manuscript.tex').read_text()
order = []
for group in re.findall(r'\\cite\w*\{([^}]+)\}', body):
    for key in group.split(','):
        if key not in order:
            order.append(key)
old = parse_bib((ROOT / 'editorial/previous_8k/references.bib').read_text())
for entry in old.entries:
    if entry['ID'] in order:
        add(entry['ID'], entry, 'previously verified: editorial/metadata and editorial/EVIDENCE.md')

for key in ['dolma', 'selfinstruct', 'picard']:
    entry = parse_bib((P / (key + '.bib')).read_text()).entries[0]
    add(key, entry, str(P.relative_to(ROOT) / (key + '.bib')))

for key in ['nalir', 'demonstrations', 'collapse', 'doremi']:
    item = json.loads((P / (key + '.json')).read_text())['message']['items'][0]
    expected = {'nalir': 'Constructing an interactive natural language interface for relational databases',
                'demonstrations': 'What Makes Good In-Context Examples for GPT-3?',
                'collapse': 'AI models collapse when trained on recursively generated data',
                'doremi': 'DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining'}
    assert item['title'][0].lower() == expected[key].lower()
    is_journal = key in ['nalir', 'collapse']
    entry = {'ENTRYTYPE': 'article' if is_journal else 'inproceedings',
             'title': item['title'][0], 'doi': item['DOI'],
             'author': ' and '.join(a['family'] + ', ' + a.get('given', '') for a in item['author']),
             'date': str(item['published']['date-parts'][0][0]),
             'journaltitle' if is_journal else 'booktitle': item['container-title'][0]}
    for a,b in [('volume','volume'),('issue','number'),('page','pages'),('publisher','publisher')]:
        if item.get(a): entry[b] = item[a].replace('-', '--') if a == 'page' else item[a]
    add(key, entry, str(P.relative_to(ROOT) / (key + '.json')) + ': first exact-title item')

for key, url in {
    'less':'https://proceedings.mlr.press/v235/xia24c.html',
    'mimicgen':'https://proceedings.mlr.press/v229/mandlekar23a.html',
}.items():
    h = html.fromstring(fetch(key, url))
    texts = h.xpath('//pre//text()|//code//text()')
    text = '\n'.join(texts)
    entry = parse_bib(text).entries[0]
    add(key, entry, url)

rag_url = 'https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html'
fetch('rag_publisher', rag_url)
for key, file in [('dinsql','dinsql'),('dclm','dclm'),('datajuicer2','datajuicer2'),('rag','rag_publisher')]:
    h = html.fromstring((P / (file + '.txt')).read_text())
    def meta(name): return h.xpath('//meta[@name="citation_' + name + '"]/@content')
    entry = {'ENTRYTYPE':'inproceedings', 'title':meta('title')[0],
             'author':' and '.join(meta('author')),
             'booktitle':(meta('conference_title') or meta('journal_title') or ['Advances in Neural Information Processing Systems'])[0],
             'date':str({'dinsql':2023,'dclm':2024,'datajuicer2':2025,'rag':2020}[key])}
    for a,b in [('volume','volume'),('doi','doi')]:
        if meta(a):entry[b]=meta(a)[0]
    if meta('firstpage') and meta('lastpage'):entry['pages']=meta('firstpage')[0]+'--'+meta('lastpage')[0]
    entry['url'] = meta('pdf_url')[0]
    add(key, entry, str(P.relative_to(ROOT) / (file + '.txt')) + ': publisher citation metadata; year is conference year')

arxiv = {re.search(r'abs/([^v]+)', e['id']).group(1):e for e in json.loads((P/'arxiv_parsed.json').read_text())}
for key, ident in {'fineweb2':'2506.20920','openthoughts':'2506.04178','robomind2':'2512.24653',
                   'agibot':'2503.06669','droid':'2403.12945','oxe':'2310.08864'}.items():
    e = arxiv[ident]
    names = e['authors']
    if key == 'oxe':
        authors = '{Open X-Embodiment Collaboration}'
    elif key == 'agibot':
        authors = '{AgiBot-World-Contributors}'
    else:
        authors = ' and '.join(names[:3]) + (' and others' if len(names)>3 else '')
    entry = dict(ENTRYTYPE='online', author=authors, title=' '.join(e['title'].split()),
                 date=e['published'][:10], url=e['id'].replace('http:','https:'), urldate='2026-09-10',
                 note='预印本，arXiv:' + ident + '，核读版本更新于' + e['updated'][:10])
    add(key, entry, 'arxiv_batch.xml and arxiv_parsed.json; version explicitly retained')

for key,title,url in [
    ('agibot2026','AgiBot World 2026: Dataset Card','https://huggingface.co/datasets/agibot-world/AgiBotWorld2026'),
    ('agibot2026_release','AGIBOT Open-Sources AGIBOT WORLD 2026 Dataset to Accelerate Embodied AI Development','https://www.agibot.com/article/231/detail/54.html')]:
    add(key,dict(ENTRYTYPE='online',author='{AGIBOT}',title=title,date='2026',urldate='2026-09-10',url=url),url)

assert set(records) == set(order), (set(order)-set(records), set(records)-set(order))
db = bibtexparser.bibdatabase.BibDatabase()
db.entries = [records[key] for key in order]
writer = bibtexparser.bwriter.BibTexWriter()
writer.order_entries_by = None
(ROOT / 'references.bib').write_text('% GB/T 7714—2015; selected from uploaded manuscript and verified primary sources.\n' + writer.write(db))
(P / 'selection.json').write_text(json.dumps(selection,ensure_ascii=False,indent=2))
(P / 'citation_order.json').write_text(json.dumps(order,ensure_ascii=False,indent=2))
print('Wrote', len(order), 'cited references')
