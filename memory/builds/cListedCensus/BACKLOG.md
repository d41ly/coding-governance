# cListedCensus — asks

## Asks
- TOOL-cListedCensus-2 · filed 2026-10-13 · the two sibling scanners list their population case-sensitively, the defect `TOOL-cListedCensus-1`'s closing review found in ps-hygiene (H1): `tools/gate-lint/sh_hygiene.py` lists `git ls-files -z "*.sh"`, a pathspec glob that is case-sensitive even under `core.ignorecase`, and `tools/gate-lint/encoding_posture.py` keeps `.endswith(".py")`. A tracked `deploy.SH` or `Tool.PY` is never graded and the green line counts the narrower set. List with no pathspec, match the suffix in any case, and add the selftest arm. · accept each scanner's `--selftest` carries an arm tracking an upper-case suffix that is observed RED against the current listing before the change

## Dispositions
- SEV · TOOL-cListedCensus-2 · LOW · an upper-case `.sh` or `.py` suffix is rare in a tracked tree, and no instance is known in gov or an adopter
- KEEP · TOOL-cListedCensus-2 · found by the closing review of TOOL-cListedCensus-1 on 2026-10-13 and not adopted: it rewrites both sibling scanners, which that unit's spec put OUT
