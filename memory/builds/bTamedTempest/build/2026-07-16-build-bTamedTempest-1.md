# Build summary — TOOL-bTamedTempest-1 (pytest-parallel-guardrails kit 1.0)

Landed `c2f608e7` (direct commit on `main`, node b). Spec CLOSED at rev-2.

## What shipped vs spec

All of S1–S7, byte-faithful to the rev-2 spec. Deltas discovered during build (all folded into
the shipped files, none contradicting the spec):

- crashprobe's `import pytest` is guarded (`try/except ImportError` around the
  `pytest.hookimpl(trylast=True)` acquisition) — AC1's bare-stdlib import-execution would
  otherwise fail on the gate machines, which have python but not pytest. Hooks are inert without
  pytest anyway.
- The self-test hands Windows-python NATIVE paths via `cygpath -m` (identity fallback on POSIX):
  MSYS-form `/c/...`/`/tmp/...` paths broke the import-execution check on exactly the platform
  the kit targets (§11's own MSYS class, met in the wild during the build).

## Verification

- Kit self-test: OK (inventory · py_compile ×3 · bare-stdlib import-execution with probe-log
  creation · version constant · 4 gov:kit marker pairs · knob presence · CR-stripped
  `faulthandler_timeout < timeout` · template-name glob check).
- `run-gates.sh`: 14/14 after the TREE regen + manifest re-stamp (the two reds were the stale
  generated `memory/tooling/TREE.md` and ratchet check 5 — watched `run-gates.sh` changed; the
  re-audit also closed the pre-existing unstamped `check-memory-hygiene.sh` debt from the kit-1.2
  landing).

## Provenance

Upstream: inCMS ARCH-eGuidingConcierge-12/-19 + ARCH-eVigilantCanary-1/-2 (diagnosed 2026-07-14,
fixed 2026-07-16; 4300-test suite went 3-for-3-hanging → two consecutive clean runs).
Pre-code review: wf_d878c8a9-bb3, 15 raw → 11 confirmed (all folded), 4 refuted → `reviews/`.

## Erratum exported upstream

The review's finding 1 (session_timeout is not a hang bound of ANY kind — it cannot fire on a
wedged test even serially) also corrects the inCMS pyproject comment and one clause of
ARCH-eVigilantCanary-1's correction paragraph. Owed to inCMS as a doc-comment erratum; this kit
ships the corrected wording.
