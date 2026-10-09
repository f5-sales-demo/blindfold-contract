"""Build a deterministic JSON bundle without timestamps or host paths."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = {
    str(p.relative_to(root)): p.read_text()
    for directory in ("spec", "fixtures")
    for p in sorted((root / directory).rglob("*"))
    if p.is_file()
}
payload = (json.dumps({"version": 1, "files": files}, sort_keys=True, separators=(",", ":")) + "\n").encode()
output = root / "dist"
output.mkdir(exist_ok=True)
(output / "blindfold-contract-v1.json").write_bytes(payload)
(output / "SHA256SUMS").write_text(hashlib.sha256(payload).hexdigest() + "  blindfold-contract-v1.json\n")
