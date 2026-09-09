"""Check review ledgers and arithmetic against committed records, offline."""
from pathlib import Path
import collections
import json
import re

root = Path(__file__).resolve().parents[1]
folder = root / 'editorial/search'
ledger = json.loads((folder / 'screening.json').read_text())
counts = json.loads((folder / 'counts.json').read_text())
coverage = json.loads((folder / 'coverage.json').read_text())
bibkeys = set(re.findall(r'@\w+\{([^,]+),', (root / 'references.bib').read_text()))
expected = {}
for n in range(9,17):
    raw = json.loads((folder / f'Q{n}.json').read_text())
    assert raw['query']['rows'] == 15
    assert 'query.title' in raw['query']
    for rank, item in enumerate(raw['response']['message']['items'], 1):
        expected[f'Q{n}:{rank:02}'] = item['DOI'].lower()
records = {r['record_id']:r['doi'] for r in ledger['raw_records']}
assert records == expected
works = ledger['works']
assert len(works) == counts['deduplicated_works']
assert len(records) == counts['fixed_query_records']
assert len(records)-len(works) == counts['duplicate_records']
assert set(r for w in works for r in w['records']) == set(records)
assert sum(w['stage1']=='exclude' for w in works) == counts['stage1_excluded']
assert sum(w['stage1']=='retain' for w in works) == counts['stage2_reviewed']
assert sum(w['stage2']=='exclude_scope_sample' for w in works) == counts['stage2_scope_excluded']
included = {w['bibkey'] for w in works if w['stage2']=='include'}
assert len(included) == counts['query_included']
assert included <= bibkeys
assert len(bibkeys) == counts['baseline']+counts['query_included']+counts['additional_included'] == counts['total']
assert set(coverage['task_tags']) | set(coverage['background_keys']) == bibkeys
assert set(coverage['task_tags']).isdisjoint(coverage['background_keys'])
assert dict(collections.Counter(t for tags in coverage['task_tags'].values() for t in tags)) == coverage['task_counts']
assert set(coverage['workflow_tags']) <= set(coverage['task_tags'])
assert len(coverage['task_tags']) == coverage['method_or_benchmark_count']
assert len(coverage['workflow_tags']) == coverage['workflow_count']
# Only arithmetic rechecks; these assertions do not validate original experiments.
assert round(66.09-52.83,2) == 13.26
assert round(87.85-70.21,2) == 17.64
assert round(67.18-61.70,2) == 5.48
assert round(97.21-67.18,2) == 30.03
assert round(0.02140/0.11540*100,1) == 18.5
text = (root / 'manuscript.tex').read_text()
assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text)
assert 'SCREEN_' not in text
assert r'\sub\section' not in text
print('PASS: 120 records, 117 works, screening/coverage/bibliography consistency and result arithmetic.')
