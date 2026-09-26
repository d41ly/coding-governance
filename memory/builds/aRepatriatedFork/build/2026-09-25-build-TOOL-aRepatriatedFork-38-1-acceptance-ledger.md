# TOOL-aRepatriatedFork-38 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-38

Written by the unit pass on node a, and rewritten by the rev-3 fold of the closing diff review of
units 31 to 38 (2026-09-26), whose criteria it now answers; rev-2's lines are superseded. The probe
is a scratch script outside the tree feeding each of the eleven readers a temp conf beside bash
sourcing it. Each reader's own suite ran whole on the built tree; the old-bytes runs swapped in the
rev-2 reader, as `176e1060` holds it, and restored it, byte-compared. The lexicon arms ran as
a slice (its prologue plus the `--scaffold` block) in a temp file inside the kit dir, removed after.

**Evidences:** TOOL-aRepatriatedFork-38
- AC1 — `BAD` — the probe prints `BAD total 0` on the built tree over `K=#x`, `K= #x`, single- and double-quoted values with and without a trailing comment, and `K=plain   # note`; on the rev-2 bytes it prints `BAD total 13`: seven readers read `K=#x` as empty, `map_lib`, `drift_report` and `recall_conf` read `K= #x` as `#x`, and `adopt-lexicon.sh` kept three single-quoted values' quotes
- AC2 — `tools/memory-recall/selftest.py` — every suite passes whole on the built tree: memory-recall 76/76, codebase-map `PASS`, process-monitor 68, corpus_ids `all arms held`, drift-audit 265, runlog 1545, `render_playbook.py --selftest` 19 arms, `bash tools/check-spec-tokens.test.sh` 99, and the lexicon slice 97. With each rev-2 reader swapped in: `FAIL conf parser == bash … BLANKED: python '#' != bash ''`, codebase-map `FAIL conf restricted grammar: #`, `FAIL test_read_roots_drops_a_trailing_comment (got (…, [], []), wanted (…, ['#x'], []))`, `arm FAIL  a cutoff whose word opens with # is refused as a non-date, never read as off — expected rc 1, got 0`, `arm FAIL a conf value keeps no trailing comment — got ('mem ory', 'TOOL', '', '')`, `arm FAIL  conf parse agrees with bash: H=#x`, `FAIL BLANKED parses identically to sh — python='#' shell=''`, `FAIL AC10 conf: the kit's reader reads as bash sourcing does (a # opening the word)`, and both lexicon reader arms; with the scaffolder spelling `ratified=` the lexicon fixture arm prints `scaffold: the fixture carries the trailing comment this arm is about` in its FAILED list
- AC3 — `bash tools/check-kit-versions.sh` — exits 0 with codebase-map 1.12, drift-audit 1.15, lexicon 1.10, memory-recall 1.17, playbook-render 1.9, process-monitor 0.7 and runlog 1.2; the lexicon, memory-recall, drift-audit, runlog and process-monitor wiring checks exit 0
