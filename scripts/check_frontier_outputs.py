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
assert all(page.rotation == 0 and page.rect.width < page.rect.height for page in pdf), \
    'All manuscript pages must be unrotated portrait pages'
for required in ['RoboMIND', 'FineWeb2', 'AgiBot', '52.83', '66.09', '参考文献', '作者简介']:
    assert required in normalized, 'Missing PDF content: ' + required
notes = re.findall(r'\bnote\s*=\s*\{([^}]+)\}', bib)
for note in notes:
    assert re.sub(r'\s+', '', note) in normalized, 'Missing bibliography note: ' + note
assert all(name in pdf[-1].get_text() for name in ['范举', '范梅浩'])
assert len(pdf[-1].get_images()) == 2, 'Missing author portraits'

maps_review = json.loads((ROOT / 'figures/reviews/author_research_maps.json').read_text())
manifest = json.loads((ROOT / maps_review['manifest']).read_text())
assert len(manifest['nodes']) == 49
assert sorted(order.index(key) + 1 for node in manifest['nodes']
              for key in node['keys']) == list(range(1, len(order) + 1))
assert {item['tree'] for item in maps_review['figures']} == {'left', 'right'}
assert len(maps_review['figures']) == 2
map_pages = {}
map_title_positions = {}
branches = {(node['tree'], node['branch']) for node in manifest['nodes']}
assert len(branches) == 12

# These are author-supplied vector PDFs. The historical PNG coordinate audit
# does not apply. Check the actual source text, references and vector content,
# then confirm both PDF figures are present in the compiled document.
for item in maps_review['figures']:
    source_file = ROOT / item['file']
    assert hashlib.sha256(source_file.read_bytes()).hexdigest() == item['sha256']
    assert '{' + item['file'] + '}' in body, 'Source PDF is not included in manuscript'
    source_pdf = fitz.open(source_file)
    assert len(source_pdf) == 1, 'Research map source must be a single page'
    source = source_pdf[0]
    assert item['size_pt'] == [source.rect.width, source.rect.height]
    assert len(source.get_drawings()) == item['vector_paths'] > 0
    assert not source.get_images(), 'Expected vector artwork, not a raster image'
    nodes = [node for node in manifest['nodes'] if node['tree'] == item['tree']]
    assert len(nodes) == item['nodes']
    expected = {
        tuple(order.index(key) + 1 for key in node['keys']): node
        for node in nodes
    }
    paper_labels = re.findall(r'\((20\d\d)\)\s*(\*)?\s*\[([\d,\s]+)\]', source.get_text())
    observed = {}
    reference_positions = {}
    for year, star, refs in paper_labels:
        numbers = tuple(int(ref.strip()) for ref in refs.split(','))
        assert numbers not in observed, 'Duplicate paper reference in source figure'
        observed[numbers] = (int(year), bool(star))
        matches = source.search_for('[' + ','.join(map(str, numbers)) + ']')
        assert len(matches) == 1, 'Missing or ambiguous reference label position'
        reference_positions[numbers] = (matches[0].y0 + matches[0].y1) / 2
    assert observed == {refs: (node['year'], node['preprint_version'])
                        for refs, node in expected.items()}, 'Paper years/references differ from manifest'
    for newer_refs, newer in expected.items():
        for older_refs, older in expected.items():
            if newer['branch'] == older['branch'] and newer['year'] > older['year']:
                assert reference_positions[newer_refs] < reference_positions[older_refs], \
                    'Chronological inversion within branch'

    title = re.sub(r'\s+', '', item['title'])
    pages = [page for page in pdf
             if any(title == re.sub(r'\s+', '', line) for line in page.get_text().splitlines())]
    assert len(pages) == 1, 'Each research map must appear once'
    page = pages[0]
    embedded_text = re.sub(r'\s+', '', page.get_text())
    for block in source.get_text('blocks'):
        if block[6] == 0:
            assert re.sub(r'\s+', '', block[4]) in embedded_text, 'Missing source figure text'
    assert len(page.get_drawings()) >= item['vector_paths'], 'Missing vector artwork'
    assert not page.get_images(), 'Research map page was rasterized'
    map_pages[item['tree']] = [page.number + 1]
    map_title_positions[item['tree']] = page.search_for(item['title'])[0].y0
    source_pdf.close()
assert map_pages['left'] == map_pages['right'], 'Research maps must share one portrait page'
assert map_title_positions['left'] < map_title_positions['right'], 'AI for Data Prep must be above Data Prep for AI'
assert len(pdf[map_pages['left'][0] - 1].get_drawings()) >= sum(
    item['vector_paths'] for item in maps_review['figures']), 'Missing vector paths on the shared figure page'

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
                     'layout': 'Two figures stacked on one unrotated portrait page',
                     'pdf_sources': maps_review['figures'],
                     'branches': len(branches),
                     'source_content': 'PASS: PDF source hashes, text, vector paths, paper years and references',
                     'branch_chronology': 'PASS: reference labels place newer papers higher within each branch',
                     'source_observations': maps_review['source_observations'],
                     'provenance': 'figures/reviews/author_research_maps.json'},
    'rendered_document': {'file': 'build/main.pdf', 'pages': len(pdf),
                          'chart_pages': [page.number + 1 for page in chart_pages]},
    'checks': 'PASS: citation order, original figure assets, PDF text, charts, portraits and TeX/Biber logs',
}
(BUILD / 'frontier_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
