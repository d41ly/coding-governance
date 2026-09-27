# TOOL-aRepatriatedFork-10 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-10

One unit pass under the mandate. It ran no merge bar and no self-test suite. Every criterion below
was observed by a direct run of the checker or the adopter against a scratch fixture under
`%TEMP%`, and every red case was observed by running b858ce1a's bytes over the same fixture. No
adopter tree was read for an observation: no criterion of this unit names one, and nc's migration is
nc's own commit.

## The fixtures

- **Engine fixture** `%TEMP%/rf10h`: one build, `tOne`, carrying a build-root `STATUS.md`, an
  unbound dated record `build/2026-08-01-build-tOne-1.md`, an undated `build/result.json`, and a
  tracked `project/pass-order-waiver.txt`, with `RECORD_UNBOUND_PIN="9"` so check 21's pin branch
  never supplied the red. Run with `legacy-files.txt` empty, then listing the two build files, under
  each value of `RECORD_UNDATED_ARTIFACTS`. The only other finding in every run was check 9's
  build-index drift, which the fixture did not regenerate.
- **Render fixture** `%TEMP%/rf10`: the four templates and `adopt-memory-tree.sh` copied flat into
  `scripts/`, a receipt whose top-level `prefix` is `scripts` and whose one file row carries a decoy
  nested `prefix`, and a conf declaring `INDEX_CAP_LINES="500"` and `ENTRY_CAP_UNIT="bytes"`.
- **Red cases**: b858ce1a's `tools/memory-tree/` via `git archive` over the engine fixture, and
  b858ce1a's adopter and HYGIENE template over the render fixture. The engine at b858ce1a named
  `pass-order-waiver.txt` under check 3, `STATUS.md` under check 4 and the listed record under
  check 21. The render at b858ce1a wrote one `INDEX_CAP_LINES=0` and a bare
  `codebase-map/gen_map.py`.

**Evidences:** TOOL-aRepatriatedFork-10
- AC1 — `legacy-files.txt` — unlisted, check 4 names the build's `tOne/STATUS.md`; listed, check 4 reports nothing. b858ce1a's engine still named it when listed
- AC2 — `legacy-files.txt` — the listed record is absent from check 21's rows under the new engine and present under b858ce1a's
- AC3 — `RECORD_UNDATED_ARTIFACTS=exempt` — check 21 does not name `result.json` and stderr carries `check 21: 1 undated non-markdown artifact(s) not graded (RECORD_UNDATED_ARTIFACTS=exempt)`; blank and `grade` both name it, and blank prints no count
- AC4 — `RECORD_UNDATED_ARTIFACTS=Exempt` — exit 2, `RECORD_UNDATED_ARTIFACTS='Exempt' (not one of: grade exempt)`
- AC5 — `memory/project/pass-order-waiver.txt` — check 3 reports nothing for it with no `PROJECT_REGISTRY_EXTRA`; b858ce1a's check 3 named it
- AC6 — `bash tools/memory-tree/adopt-memory-tree.sh --render` — the rendered `memory/HYGIENE.md` reads `is: 500` twice and `is: bytes`, and `grep -c INDEX_CAP_LINES=0` returns 0; b858ce1a's render returned 1
- AC7 — `memory/TEMPLATE-SPEC.md` — the render names `scripts/codebase-map/gen_map.py` and `scripts/codebase-map/map_extractors.py`; b858ce1a's named them bare, because its `TOOL_ROOT` was the empty parent
- AC8 — `python tools/check-kit-placeholders.py` — exit 1 over b858ce1a's `tools/memory-tree/HYGIENE.template.md`, naming `INDEX_CAP_LINES` and `ROTATION_MODE`; exit 0 over the built tree, 17 rendered templates scanned
- AC9 — amended rev-2 — `bash scripts/check-build-readme-comments.sh` run where the script is absent exits 127 with `No such file or directory` naming it; the README ships the runnable script and says the runner half is unobserved. The section 9 rev-2 line logs the change
- AC10 — `bash tools/check-kit-versions.sh` — exit 0 at 2.86 in all nine carriers; `tools/memory-tree/README.md` gains the four-route table naming `PROJECT_REGISTRY_EXTRA`, `legacy-files.txt`, `RECORD_UNDATED_ARTIFACTS` and the project leg
