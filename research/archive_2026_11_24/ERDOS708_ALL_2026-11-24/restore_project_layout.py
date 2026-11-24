#!/usr/bin/env python3
"""Restore all original substantive project paths from deduplicated payloads."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path, PurePosixPath

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def safe(root, relative):
    part = PurePosixPath(relative)
    if part.is_absolute() or '..' in part.parts:
        raise ValueError('Unsafe path: ' + relative)
    target = root.joinpath(*part.parts).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError('Path escapes destination')
    return target

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=None)
    args = ap.parse_args()
    base = Path(__file__).resolve().parent
    out = (args.output or base / 'restored_projects').resolve()
    rows = json.loads((base / 'catalog/PATH_ALIASES.json').read_text())
    jobs = []
    for row in rows:
        src = safe(base, row['archive_path'])
        dst = safe(out, row['original_path'])
        if sha(src) != row['sha256']:
            raise ValueError('Source checksum mismatch: ' + str(src))
        if dst.exists() and (not dst.is_file() or sha(dst) != row['sha256']):
            raise FileExistsError('Different existing file: ' + str(dst))
        jobs.append((src, dst))
    made = 0
    for src, dst in jobs:
        if dst.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        made += 1
    print(f'Checked {len(jobs)} original paths; restored {made} files to {out}')

if __name__ == '__main__':
    main()
