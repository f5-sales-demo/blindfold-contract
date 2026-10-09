"""Build a deterministic JSON bundle without timestamps or host paths."""

import hashlib
import json
from pathlib import Path


def build_bundle(root: Path) -> None:
    """Write the version 1 bundle and its reproducible checksum."""
    files = {
        str(p.relative_to(root)): p.read_text()
        for directory in ("spec", "fixtures")
        for p in sorted((root / directory).rglob("*"))
        if p.is_file()
    }
    payload = (
        json.dumps(
            {"version": 1, "files": files}, sort_keys=True, separators=(",", ":")
        )
        + "\n"
    ).encode()
    output = root / "dist"
    output.mkdir(exist_ok=True)
    (output / "blindfold-contract-v1.txt").write_bytes(payload)
    (output / "SHA256SUMS").write_text(
        hashlib.sha256(payload).hexdigest() + "  blindfold-contract-v1.txt\n"
    )


if __name__ == "__main__":
    build_bundle(Path(__file__).resolve().parents[1])
