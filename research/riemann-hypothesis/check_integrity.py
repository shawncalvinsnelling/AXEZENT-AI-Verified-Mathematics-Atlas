"""Check the declared release files. Integrity is not mathematical validity."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def check():
    records = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
    if not records:
        raise RuntimeError("Empty manifest")
    for name, item in records.items():
        p = Path(name)
        if p.is_absolute() or ".." in p.parts:
            raise RuntimeError("Unsafe manifest path")
        target = ROOT / p
        if target.is_symlink() or not target.is_file():
            raise RuntimeError(f"Missing or nonregular release file: {name}")
        data = target.read_bytes()
        if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise RuntimeError(f"Release file mismatch: {name}")
    print(f"PASS_FILE_INTEGRITY: {len(records)} files; not a proof of correctness")
    return len(records)

if __name__ == "__main__":
    check()
