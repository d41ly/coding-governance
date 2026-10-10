# TOOL-aLevelledCopy-9 — acceptance ledger

**Serves:** journal TOOL-aLevelledCopy-9

No merge bar and no self-test suite ran in this pass. Every criterion was observed directly on node
a, git 2.54.0.windows.1. `python tools/run-gates/check-receipt.py --selftest` printed 12 of 12 arms
ok and exited 0. Three staged copies of the checker went red. With the S1 pins removed and the
hostile environment kept, all four git arms printed `ARM FAIL` and the copy exited 1. With the
`.git` guard of `resolve_clean_oids` deleted, the no-`.git` arm printed `ARM FAIL`. With
`seed_hostile_env` left out of the window, the liveness arm printed `ARM FAIL`, reading eol
`unspecified` and object format `sha1`. The `ND` fixture ran alone in about 45 s under the default
`%TEMP%` and printed `[]`. It went red against two sources handed to `measure_mode_carry`. The
`govkit.py` taken with `git show` at dae09ec1f failed only the renamed row, which landed 100644.
A copy whose `resolve_landed_mode` returned gov's mode for every entry failed the renamed, diverged
and stale rows, and the missing row still passed. The close still owes `govkit selftest` run whole,
with `receipt sync`, `run-gates adopter e2e`, `govkit selfcheck`, `govkit refusal join`,
`govkit acceptance matrix`, the two recall legs, `codebase-map coverage + freshness`,
`lexicon naming predicates`, `spec tokens` and `memory hygiene`.

**Evidences:** TOOL-aLevelledCopy-9
- AC1 — `ARM ok` — `--selftest` printed `ARM ok` for the `(live)` arm and for arms (a) to (d), the `fixtures:` line read 12/12, and the exit was 0.
- AC2 — `ARM FAIL` — the scratch copy without the `attributesFile` line and the three window pins printed `ARM FAIL` for arms (a), (b), (c) and (d), because the re-checkout under the hostile `text=auto eol=lf` wrote no CR byte, and it exited 1.
- AC3 — `ARM ok` — the no-`.git` arm printed `ARM ok` under `--selftest`; the scratch copy with the `.git` guard deleted printed `ARM FAIL` for that arm and exited 1.
- AC4 — `ND` — `check_mode_never_down` printed `[]`, and `ls-files -s` read 100755 for `ren2.sh` at its new path with no entry left at `ren.sh`. The pre-build `govkit.py` landed `ren2.sh` at 100644.
- AC5 — amended rev-3 — the `missing` row is a control landing at gov's 100644, not a fourth 100755 row, because `classify_row` reads `missing` only where the index holds no entry. Observed: the read-only update printed `renamed`, `diverged`, `missing` and `stale` once each; `--write` left the other three rows at 100755 with gov's new bytes; the mirrored-rule copy failed those three and passed the missing row.
- AC6 — `two-answers-to-one-question` — `gotchas.py --check` exited 0 after `--write`, `grep -n roster` hit the new section's heading on line 114, and `--for-paths memory/builds/aLevelledCopy/README.md` listed `two-answers-to-one-question`.
- AC7 — `tmpfs` — `grep -n ext4` on spec 3 hit only its §9 rev-3 line, AC6's `fixture:` line names `tmpfs`, and the header reads `CLOSED · rev-3`.
