#!/usr/bin/env python3
"""Verify every manifest-listed payload; no network or research execution."""
import hashlib
import json
from pathlib import Path, PurePosixPath

base = Path(__file__).resolve().parent
manifest = json.loads((base / 'catalog/MANIFEST.json').read_text())
errors = []
for item in manifest['files']:
    rel = PurePosixPath(item['path'])
    if rel.is_absolute() or '..' in rel.parts:
        errors.append('unsafe path: ' + item['path'])
        continue
    p = base.joinpath(*rel.parts)
    if not p.is_file():
        errors.append('missing: ' + item['path'])
        continue
    if p.stat().st_size != item['size_bytes'] or hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
        errors.append('checksum: ' + item['path'])
if errors:
    raise SystemExit('FAILED\n' + '\n'.join(errors))
print(f"OK: {len(manifest['files'])} manifest-listed files verified")
