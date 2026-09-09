"""Replay stored Crossref query specifications into a separate snapshot directory.

The committed 2026-09-09 responses are immutable audit inputs. Live search ranking
may change; new snapshots deliberately do not overwrite the screened corpus.
"""
import argparse
import datetime
import json
import time
from pathlib import Path
import requests

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
for path in sorted((root / 'editorial/search').glob('Q*.json'), key=lambda p: int(p.stem[1:])):
    record = json.loads(path.read_text())
    dest = args.output / path.name
    if dest.exists():
        raise SystemExit(f'Refusing to overwrite snapshot: {dest}')
    response = requests.get('https://api.crossref.org/works', params=record['query'], timeout=50)
    response.raise_for_status()
    record.update(endpoint=response.url, retrieved=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  response=response.json())
    dest.write_text(json.dumps(record, ensure_ascii=False, indent=2))
    print(path.stem, len(record['response']['message']['items']))
    time.sleep(0.3)
