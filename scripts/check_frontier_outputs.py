"""Check the compiled LaTeX survey without reading or generating Word files."""
import hashlib
import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
body = (ROOT / 'manuscript.tex').read_text()
bib = (ROOT / 'references.bib').read_text()

order = []
for group in re.findall(r'\\cite\w*\{([^}]+)\}', body):
    for key in map(str.strip, group.split(',')):
        if key not in order:
            order.append(key)
saved_order = json.loads((ROOT / 'editorial/frontier_sources/citation_order.json').read_text())
assert order == saved_order, 'Citation metadata differs from manuscript'
bbl = (BUILD / 'main.bbl').read_text()
assert re.findall(r'\\entry\{([^}]+)\}', bbl) == order, 'Biber citation order differs'

provenance = json.loads((ROOT / 'figures/original/provenance.json').read_text())
for name, expected in provenance['exported_assets_sha256'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name

pdf = fitz.open(BUILD / 'main.pdf')
alltext = ''.join(page.get_text() for page in pdf)
normalized = re.sub(r'\s+', '', alltext)
assert '\ufffd' not in alltext, 'Replacement character in PDF'
assert all(len(page.get_text().strip()) > 30 for page in pdf), 'Empty page'
for required in ['RoboMIND', 'FineWeb2', 'AgiBot', '52.83', '66.09', '参考文献', '作者简介']:
    assert required in normalized, 'Missing PDF content: ' + required
notes = re.findall(r'\bnote\s*=\s*\{([^}]+)\}', bib)
for note in notes:
    assert re.sub(r'\s+', '', note) in normalized, 'Missing bibliography note: ' + note
assert all(name in pdf[-1].get_text() for name in ['范举', '范梅浩'])
assert len(pdf[-1].get_images()) == 2, 'Missing author portraits'

tree_review = json.loads((ROOT / 'figures/reviews/fig00_two_research_trees.json').read_text())
tree_file = ROOT / tree_review['final_file']
assert hashlib.sha256(tree_file.read_bytes()).hexdigest() == tree_review['sha256']
tree_source = fitz.Pixmap(str(tree_file))
tree_pages = []
for page in pdf:
    for item in page.get_images():
        if (item[2], item[3]) == (tree_source.width, tree_source.height):
            rendered = fitz.Pixmap(pdf, item[0])
            assert rendered.samples == tree_source.samples, 'Research tree pixels changed in PDF'
            tree_pages.append(page.number + 1)
assert len(tree_pages) == 1, 'Research tree must appear exactly once'

chart_pages = [page for page in pdf
               if '国外学者' in page.get_text() and '国内学者' in page.get_text()]
assert len(chart_pages) == 2, 'Missing original chart'
for page in chart_pages:
    assert any(d['rect'].width > 100 and d['rect'].height > 100
               for d in page.get_drawings()), 'Clipped chart area'
log = (BUILD / 'main.log').read_text()
assert not re.search(r'Overfull|Missing character:|undefined|LaTeX Error', log), 'TeX log errors'
assert not re.search(r'(?m)^.*(?:ERROR|WARN) -', (BUILD / 'main.blg').read_text()), 'Biber warnings'

report = {
    'revised_body_chinese_characters': len(re.findall('[\u4e00-\u9fff]', body)),
    'sections': [
        {'title': section.split('}')[0],
         'chinese_characters': len(re.findall('[\u4e00-\u9fff]', section))}
        for section in body.split('\\section{')[1:]
    ],
    'cited_references': len(order),
    'preprint_version_notes': len(notes),
    'research_tree': {'pages': tree_pages, 'nodes': 49, 'references': len(order),
                      'image_size_px': [tree_source.width, tree_source.height]},
    'rendered_document': {'file': 'build/main.pdf', 'pages': len(pdf),
                          'chart_pages': [page.number + 1 for page in chart_pages]},
    'checks': 'PASS: citation order, original figure assets, PDF text, charts, portraits and TeX/Biber logs',
}
(BUILD / 'frontier_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
