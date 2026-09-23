# TOOL-aRepatriatedFork-2 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-2

One unit pass under the mandate. It ran no merge bar and no self-test suite: neither
`check-install-prefix.test.sh` nor `resolve-python.test.sh` nor any kit suite was run whole. Every
criterion was observed by a direct run of the changed checker, generator or resolver against a
scratch fixture or a clone, and the two new self-test arms were run as slices of their suites. The
adopter trees were read only through clones.

## The fixtures

- **scripts/ clone**: `git clone --shared` of this worktree under `%TEMP%/r2s`, at 8cf89a61 plus
  this unit's diff as one overlay commit, then `git mv tools scripts` with the manifest, the
  self-test declaration and the count waivers repathed, because an adopter's own records spell its
  own prefix.
- **pre-fix clone**: the same kind of clone under `%TEMP%/r2c` at 8cf89a61, with this unit's gate
  copied over the one it carried.
- **inCMS-shaped fixture**: a scratch repo under `%TEMP%/r2f` holding memory-tree flat under
  `scripts/`, the recall kit under `scripts/recall/`, and a receipt row whose `source` is gov's
  memory-recall `extract.py`.
- **inCMS clone**: `git clone --local --shared` of `C:/projects/incms/main` at bc7e95589 under
  `%TEMP%/r2i`. The real tree was not written.
- **Arm slices**: `check-install-prefix.test.sh`'s prologue, `mkfix_source` and the new runtime
  section, run alone; then again against a gate copy with P1's `$VAR/` lead removed, which failed
  the P1 arm and passed the other two. The resolver's parity arm was run alone the same way, then
  against `merge-rows.py` with its two probes swapped, which failed on that copy, then restored.

**Evidences:** TOOL-aRepatriatedFork-2
- AC1 — `bash scripts/check-testsuite-counts.sh` — in the scripts/ clone it exited 0 and printed nothing, where 8cf89a61's bytes printed `no tools/gate-legs.json` and exited 2; the line-length and restatement gates in the same clone read their sidecars and printed their clean lines
- AC2 — `bash scripts/run-gates/run-selftests.sh --kit scripts/unattended --list` — in the scripts/ clone it listed 20 unattended rows, where gov's old `--kit tools/unattended` filter listed 0; the runner's three argv lines now read `"$RUNNER" --kit "$KIT_REL"` and carry no `tools/`
- AC3 — `bash scripts/memory-tree/check-verdict-epoch.sh 8cf89a61` — in the scripts/ clone it printed a `clean` verdict and exited 0, where 8cf89a61's bytes printed `tools/memory-tree/check-memory-hygiene.sh is missing` and exited 2
- AC4 — `cd scripts/drift-audit && python drift_report.py` — in the inCMS clone the three lexicon rows printed measured values (271 over 1081, 0 of 23, 1 of 1) with this unit's file, and `not asked` three times with inCMS's own
- AC5 — `resolve_kit_dir("memory-recall", "extract.py", "scripts")` — in the inCMS-shaped fixture it returned `scripts/recall`, and with the receipt row deleted it raised a LookupError naming the receipt and both probes; the parity slice held 39 assertions and reds on a drifted copy
- AC6 — `python scripts/settings-merge.py --resolve-fragment scripts/recall/recall-opened.fragment.json` — in the inCMS-shaped fixture it printed `scripts/recall/recall-opened.js`, and 8cf89a61's fragment printed `scripts/memory-recall/recall-opened.js`
- AC7 — `python scripts/memory-tree/gotchas.py --write` — in the scripts/ clone the INDEX.md command block names `scripts/memory-tree/gotchas.py`; `grep -c 'tools/' tools/memory-tree/gotchas.py` fell 23 to 21
- AC8 — `bash tools/check-install-prefix.sh --list` — none of the S6 lines is among arm 3's hit lines; in the fixtures the unattended repair hint read `scripts/memory-tree/gen_build_index.py` beside a kit and `scripts/gen_build_index.py` through the receipt, and agent-cap's harness pointer read `scripts/workflows/tier2-review.js`
- AC9 — `bash tools/check-install-prefix.sh` — over gov it exited 0 printing `runtime literals clean — 108 shipped code file(s), 24 marked line(s)` beside the two older arms' clean lines
- AC10 — `bash tools/check-install-prefix.sh --check` — in the pre-fix clone arm 3 exited 1 over 72 hit lines, naming `tools/drift-audit/drift_report.py:939` (P2+P3), `tools/process-monitor/procmon-hook.js:118` (P2) and `tools/unattended/run-unattended-gates.sh:302` (P1)

## The checklist's finding

The bug-class checklist over the closing commit selected `a-pair-exists-and-it-is-the-wrong-one`,
and it was live: arm 3's first JS reader paired a `/*` inside a quoted glob with the next `*/` and
read nothing in between, at `tools/hooks/agent-cap.js:301` and `tools/hooks/scratch-guard.js:648`.
The reader now tracks its strings, and a fourth arm puts a join after such a glob: the new reader
reds that fixture by line, and the old one passed it silently, which failed the arm. Gov's verdict
and the pre-fix clone's count did not move.

## Owed to the close

The suites that grade these files whole run once, at the close: `install-prefix self-test`,
`resolve-python`'s parity table, `agent-cap self-test`, `manifest-check self-test`,
`memory-recall kit selftest`, `drift-audit selftest`, `lexicon selftest`, `codebase-map kit
selftest`, `playbook render selftest`, `run-selftests self-test` and the rest of the spec's section 7.
`settings-merge.py --selftest` was run here, because its pin moved with the fragment, and passed.

## Section 8 F4

`tools/settings-merge.py`'s name-only fallback is marked `gov:prefix-literal` with its reason. The
owner's resolution also asks the settings-merge owner whether it should refuse instead; that
question is carried here for the close, since this pass cannot ask it.
