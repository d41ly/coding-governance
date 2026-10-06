# TOOL-aEvidencedLens-10 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-10

`review_replay.py` scores a spec-audit report against a past one by file and section. The pass commit
`da5d530bd` says six arms were added and 25 are declared, and its spec amendment `89b627247` moved the
known-to-score path into `measure_replay`, shared by main and the arms, so the window arm can red. The
criteria are read from the main loop's VERIFYING run of `python tools/workflows/review_replay.py
--selftest` in a frozen clone at `0c8dd1761`, which printed `ok` for 25 arms and closed
`selftest: 25/25 arms`. Each criterion below names the arm the spec pairs with it; the arm's name is
the observation, and what the arm asserts inside is its body, not restated here. AC8's grep was re-run
on the tree at `5a1643c8d`.

**Evidences:** TOOL-aEvidencedLens-10
- AC1 — `--selftest` — every one of the 25 arm lines printed `ok`, including `no-appendix`, `section-ref`, `window-0`, `kind-mismatch`, `subject-pins` and `per-lens-known`, and the closing line read `selftest: 25/25 arms`; `grep -n "ARMS_DECLARED *="` over the tool at `5a1643c8d` printed `ARMS_DECLARED = 25`, the base 19 plus six.
- AC2 — `no-appendix` — the arm `no-appendix` printed `ok`.
- AC3 — `extract_section_ref` — the arm `section-ref` printed `ok`.
- AC4 — `--window 10` — the arm `window-0` printed `ok`; per `89b627247` the window forcing lives in `measure_replay`, which that arm reaches.
- AC5 — `kind-mismatch` — the arm `kind-mismatch` printed `ok`.
- AC6 — `subjects none-stated` — the arm `subject-pins` printed `ok`.
- AC7 — `per-lens known:` — the arm `per-lens-known` printed `ok`.
- AC8 — `kind-mismatch` — at `5a1643c8d`, `grep -n "spec-audit" tools/workflows/README.md` printed lines 245, 259 and 265; the replay section from line 259 names spec mode, the section rule (a match is the same file and the same SECTION, the window forced to 0) and the `kind-mismatch` refusal in either direction.
