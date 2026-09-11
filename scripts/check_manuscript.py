"""Offline consistency checks for this LaTeX survey (no model experiments)."""
import collections
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
main = (root / 'main.tex').read_text()
body = (root / 'manuscript.tex').read_text()
bib = (root / 'references.bib').read_text()
keys = re.findall(r'@\w+\{([^,]+),', bib)
citations = {key.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}', body) for key in group.split(',')}
labels = re.findall(r'\\label\{([^}]+)\}', main + body)
figures = re.findall(r'\\articlefigure\{([^}]+)\}\{[^\n]*\}\{([^}]+)\}', body)
labels.extend(label for _, label in figures)
refs = set(re.findall(r'\\(?:eq)?ref\{([^}]+)\}', body))
dois = re.findall(r'\bdoi\s*=\s*\{([^}]+)\}', bib, re.I)
errors = []
for name, values in [('bibliography key', keys), ('label', labels), ('DOI', [d.lower() for d in dois])]:
    errors.extend(f'duplicate {name}: {v}' for v, n in collections.Counter(values).items() if n > 1)
errors.extend(f'undefined citation: {v}' for v in citations - set(keys))
errors.extend(f'uncited bibliography entry: {v}' for v in set(keys) - citations)
errors.extend(f'undefined reference: {v}' for v in refs - set(labels))
for name, _ in figures:
    if not (root / 'figures' / 'original' / (name + '.pdf')).is_file():
        errors.append(f'missing figure: {name}')
    if not (root / 'figures' / 'original' / (name + '.png')).is_file():
        errors.append(f'missing figure preview: {name}')
inline_graphics = re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}', body)
for graphic in inline_graphics:
    if not (root / graphic).is_file():
        errors.append(f'missing inline figure: {graphic}')
tree_manifest = json.loads((root / 'figures/two_research_trees_manifest.json').read_text())
tree_keys = [key for node in tree_manifest['nodes'] for key in node['keys']]
paper_years = dict(re.findall(r'@\w+\{([^,]+),.*?\bdate\s*=\s*\{(\d{4})[^}]*\}', bib, re.S))
if collections.Counter(tree_keys) != collections.Counter(keys):
    errors.append('research trees must cover every bibliography entry exactly once')
citation_order = []
for group in re.findall(r'\\cite\w*\{([^}]+)\}', body):
    for key in map(str.strip, group.split(',')):
        if key not in citation_order:
            citation_order.append(key)
for node in tree_manifest['nodes']:
    expected = ','.join(str(citation_order.index(key) + 1) for key in node['keys'])
    if not node['label'].endswith('[' + expected + ']'):
        errors.append(f'stale reference number in tree: {node["label"]}')
    if node['year'] != int(paper_years[node['keys'][0]]):
        errors.append(f'stale publication year in tree: {node["label"]}')
bio_source = re.sub(r'%[^\n]*', '', (root / 'author_bios.tex').read_text())
portraits = re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}', bio_source)
for portrait in portraits:
    if not (root / portrait).is_file():
        errors.append(f'missing author portrait: {portrait}')
if r'\input{author_bios.tex}' not in re.sub(r'%[^\n]*', '', main):
    errors.append('author biographies are not included')
for required in ['人工智能辅助数据准备', '面向人工智能的数据准备', '具身数据准备',
                 'AI for Data Prep，简称AI4DP', 'Data Prep for AI，简称DP4AI']:
    if required not in body:
        errors.append(f'missing requested topic: {required}')
for retired in ['LM4DP', 'DP4LM']:
    if retired in body:
        errors.append(f'inconsistent direction abbreviation: {retired}')
if not 7500 <= len(re.findall('[\u4e00-\u9fff]', body)) <= 8500:
    errors.append('manuscript outside approximately 8000 Chinese characters')
report = {
    'references': len(keys), 'cited_references': len(citations),
    'figures': len(figures) + len(re.findall(r'\\caption(?:\[[^]]*\])?\{', body)),
    'tree_nodes': len(tree_manifest['nodes']), 'tree_references': len(tree_keys),
    'tables': body.count('\\begin{table}'),
    'author_portraits': len(portraits),
    'chinese_characters_in_manuscript_source': len(re.findall('[\u4e00-\u9fff]', body)),
    'errors': errors,
}
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
