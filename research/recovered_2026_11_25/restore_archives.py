#!/usr/bin/env python3
"""Restore the exact recovered research archives from verified binary pieces."""
from argparse import ArgumentParser
from pathlib import Path, PurePosixPath
import hashlib
import io
import json
import stat
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parent

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def store(path, data):
    if path.exists():
        require(path.is_file() and path.read_bytes() == data, f"Refusing overwrite: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)

def safe_extract(z, dest):
    require(z.testzip() is None, "ZIP CRC check failed")
    base = dest.resolve()
    for info in z.infolist():
        rel = PurePosixPath(info.filename)
        require(not rel.is_absolute() and ".." not in rel.parts and "\\" not in info.filename,
                f"Unsafe archive path: {info.filename}")
        require(not stat.S_ISLNK(info.external_attr >> 16), f"Unsafe symlink: {info.filename}")
        target = (dest / rel).resolve()
        require(target == base or base in target.parents, f"Unsafe target: {target}")
        if info.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            store(target, z.read(info))

def main():
    ap = ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=Path("recovered_2026_11_25"))
    ap.add_argument("--unpack", action="store_true", help="Extract the nested original research ZIPs")
    ap.add_argument("--verify-g9", action="store_true", help="Unpack and rerun original upper-13 verification")
    args = ap.parse_args()
    manifest = json.loads((ROOT / "archives" / "manifest.json").read_text())
    chunks = []
    for part in manifest["parts"]:
        data = (ROOT / "archives" / part["file"]).read_bytes()
        require(len(data) == part["size"], f"Wrong size: {part['file']}")
        require(sha256(data) == part["sha256"], f"Wrong SHA-256: {part['file']}")
        git_hash = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        require(git_hash == part["git_blob"], f"Wrong Git blob: {part['file']}")
        chunks.append(data)
    combined = b"".join(chunks)
    require(len(combined) == manifest["size"], "Wrong combined size")
    require(sha256(combined) == manifest["sha256"], "Wrong combined SHA-256")
    combined_path = args.output / manifest["file"]
    store(combined_path, combined)
    with zipfile.ZipFile(io.BytesIO(combined)) as z:
        safe_extract(z, args.output)
    verifier = None
    for package in manifest["original_packages"]:
        path = args.output / "original_packages" / package["file"]
        require(sha256(path.read_bytes()) == package["sha256"], f"Wrong package SHA-256: {path.name}")
        with zipfile.ZipFile(path) as z:
            require(z.testzip() is None, f"Corrupt original ZIP: {path.name}")
            if args.unpack or (args.verify_g9 and "bounds_12_to_13" in path.name):
                dest = args.output / "unpacked" / path.stem
                safe_extract(z, dest)
                if "bounds_12_to_13" in path.name:
                    verifier = dest / "G9_12_OR_13_PROOF" / "verify_all.py"
        print("Verified:", path.name)
    print("Complete original archive restored:", combined_path)
    if args.verify_g9:
        require(verifier is not None and verifier.is_file(), "Original g(9) verifier missing")
        subprocess.run([sys.executable, str(verifier.resolve())], cwd=verifier.parent, check=True)
        print("g(9) upper-13 computation replayed; upstream finite-case dependencies still apply.")

if __name__ == "__main__":
    main()
