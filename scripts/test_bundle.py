"""Verify deterministic contract publication and required conformance entries."""
import hashlib
import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BundleTests(unittest.TestCase):
    def test_rebuild_matches_committed_bytes_and_checksum(self):
        target = ROOT / "dist/blindfold-contract-v1.txt"
        before = target.read_bytes()
        subprocess.run(["python3", str(ROOT / "scripts/bundle.py")], check=True)
        self.assertEqual(before, target.read_bytes())
        expected = (ROOT / "dist/SHA256SUMS").read_text().split()[0]
        self.assertEqual(expected, hashlib.sha256(before).hexdigest())
        bundle = json.loads(before)
        self.assertEqual(bundle["version"], 1)
        self.assertIn("fixtures/synthetic-inputs.json", bundle["files"])
        self.assertIn("fixtures/pinned-reference.json", bundle["files"])
        scenarios = json.loads(bundle["files"]["spec/conformance.json"])
        self.assertIn("complete-exponent", scenarios["protocol"])
        self.assertIn("strict-trust-hostname", scenarios["qualification"])

if __name__ == "__main__":
    unittest.main()
