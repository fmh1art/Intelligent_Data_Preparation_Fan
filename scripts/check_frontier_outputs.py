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

maps_review = json.loads((ROOT / 'figures/reviews/flat_research_trees.json').read_text())
taxonomy = json.loads((ROOT / maps_review['taxonomy_audit']).read_text())
assert taxonomy['images'] == maps_review['images'], 'Branch audit belongs to different images'
map_sources = {}
for item in maps_review['images']:
    image_file = ROOT / item['file']
    assert hashlib.sha256(image_file.read_bytes()).hexdigest() == item['sha256']
    pixmap = fitz.Pixmap(str(image_file))
    assert item['size_px'] == [pixmap.width, pixmap.height]
    map_sources[item['tree']] = pixmap
assert set(map_sources) == {'left', 'right'} and len(maps_review['images']) == 2
manifest = json.loads((ROOT / maps_review['manifest']).read_text())
assert len(taxonomy['nodes']) == len(manifest['nodes']) == 49 and not taxonomy['missing']
assert sorted(int(ref) for node in taxonomy['nodes']
              for ref in node['references'].split(',')) == list(range(1, len(order) + 1))

# Validate the recorded visual audit against the bibliography-linked manifest.
# Branch lanes and tag bounds were read from the hash-bound PNGs, not predicted
# from prompts. Lanes are audit bounds, not drawn panels. Text and connectivity
# remain visual checks.
branches = {branch['id']: branch for branch in taxonomy['branches']}
assert len(branches) == len(taxonomy['branches']) == 12
assert {tree: sum(b['tree'] == tree for b in branches.values())
        for tree in ['left', 'right']} == {'left': 6, 'right': 6}
expected_nodes = {tuple(node['keys']): node for node in manifest['nodes']}
assert {tuple(n['keys']) for n in taxonomy['nodes']} == set(expected_nodes)

def valid_box(box, tree):
    x0, y0, x1, y1 = box
    source = map_sources[tree]
    return 0 <= x0 < x1 <= source.width and 0 <= y0 < y1 <= source.height

def overlaps(a, b):
    return max(a[0], b[0]) < min(a[2], b[2]) and max(a[1], b[1]) < min(a[3], b[3])

for branch in branches.values():
    assert valid_box(branch['lane_bbox_px'], branch['tree'])
    assert branch['heading_visually_verified'] and branch['dedicated_stem_visually_verified']
    assert not branch['cross_branch_paper_connectors']
    for other in branches.values():
        if branch['tree'] == other['tree'] and branch['id'] != other['id']:
            assert not overlaps(branch['lane_bbox_px'], other['lane_bbox_px']), 'Overlapping branch lanes'

for node in taxonomy['nodes']:
    expected = expected_nodes[tuple(node['keys'])]
    assert all(node[key] == expected[key] for key in expected), 'Node differs from manifest'
    assert node['references'] == ','.join(str(order.index(key) + 1) for key in node['keys'])
    branch = branches[node['branch_id']]
    assert (node['tree'], node['branch']) == (branch['tree'], branch['title']), 'Wrong topic branch'
    x0, y0, x1, y1 = node['tag_bbox_px']
    bx0, by0, bx1, by1 = branch['lane_bbox_px']
    assert valid_box(node['tag_bbox_px'], node['tree'])
    assert bx0 <= x0 < x1 <= bx1 and by0 <= y0 < y1 <= by1, 'Paper tag outside its branch lane'
    assert node['y_center_px'] == (y0 + y1) / 2 and node['uncertainty_px'] >= 0
    assert node['label_and_membership_visually_verified']
    if 'reference_ocr' in node:
        token = node['reference_ocr']
        assert x0 <= token['left_px'] <= x1 and y0 <= token['top_px'] <= y1, 'OCR token outside tag'

for newer in taxonomy['nodes']:
    for older in taxonomy['nodes']:
        if newer['branch_id'] != older['branch_id']:
            continue
        if newer['keys'] != older['keys']:
            assert not overlaps(newer['tag_bbox_px'], older['tag_bbox_px']), 'Overlapping paper tags'
        if newer['year'] > older['year']:
            assert (newer['y_center_px'] + newer['uncertainty_px'] <
                    older['y_center_px'] - older['uncertainty_px']), 'Chronological inversion within branch'
map_pages = {tree: [] for tree in map_sources}
for page in pdf:
    for item in page.get_images():
        for tree, source in map_sources.items():
            if (item[2], item[3]) == (source.width, source.height):
                rendered = fitz.Pixmap(pdf, item[0])
                if rendered.samples == source.samples:
                    assert page.rect.width > page.rect.height, 'Research map needs a landscape page'
                    map_pages[tree].append(page.number + 1)
assert all(len(pages) == 1 for pages in map_pages.values()), 'Each research map must appear once with unchanged pixels'
assert map_pages['left'] != map_pages['right'], 'Research maps need separate pages'

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
    'research_maps': {'pages': map_pages, 'nodes': 49, 'references': len(order),
                     'images': [{'file': item['file'], 'size_px': item['size_px'], 'nodes': item['nodes']}
                                for item in maps_review['images']],
                     'branches': len(branches),
                     'taxonomy': 'PASS: every node is inside its assigned branch lane',
                     'branch_chronology': 'PASS: zero cross-year inversions within branches',
                     'visual_audit': maps_review['taxonomy_audit']},
    'rendered_document': {'file': 'build/main.pdf', 'pages': len(pdf),
                          'chart_pages': [page.number + 1 for page in chart_pages]},
    'checks': 'PASS: citation order, original figure assets, PDF text, charts, portraits and TeX/Biber logs',
}
(BUILD / 'frontier_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
