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
    if not (root / 'figures' / (name + '.png')).is_file():
        errors.append(f'missing figure: {name}')
    if not (root / 'figures' / 'prompts' / (name + '.md')).is_file():
        errors.append(f'missing figure prompt: {name}')
bio_source = re.sub(r'%[^\n]*', '', (root / 'author_bios.tex').read_text())
portraits = re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}', bio_source)
for portrait in portraits:
    if not (root / portrait).is_file():
        errors.append(f'missing author portrait: {portrait}')
if r'\input{author_bios.tex}' not in re.sub(r'%[^\n]*', '', main):
    errors.append('author biographies are not included')
for pattern in ['具身智能', '机器人', 'Open X-Embodiment', '科普综述']:
    if pattern in main + body + bib:
        errors.append(f'out-of-scope term in publication sources: {pattern}')
report = {
    'references': len(keys), 'cited_references': len(citations),
    'figures': len(figures), 'tables': body.count('\\begin{table}'),
    'author_portraits': len(portraits),
    'chinese_characters_in_manuscript_source': len(re.findall('[\u4e00-\u9fff]', body)),
    'errors': errors,
}
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
