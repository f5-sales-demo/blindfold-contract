# Blindfold contract

This repository owns the native Blindfold binary envelope and certificate reconciliation contract.
Go and Rust consumers embed an immutable bundle at build time. Consumers do not download material
from this repository at runtime or invoke each other.

Version 1 is defined in [the specification](spec/v1.md). Synthetic fixtures are public test material;
they must never be used for tenant authentication or deployed certificates.

Run `python3 scripts/bundle.py` to produce the deterministic bundle and SHA256 checksum. Consumer
locks record the source commit and bundle checksum. The repository's conformance scenarios describe
required behavior; passing a unit test does not establish installed or live TLS acceptance.
