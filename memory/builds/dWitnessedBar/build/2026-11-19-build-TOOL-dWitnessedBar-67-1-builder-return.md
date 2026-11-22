**Serves:** journal TOOL-dWitnessedBar-67

# TOOL-dWitnessedBar-67 — builder return 1 (run `wf_02fcf431-8ee`), committed af84e1a7ac04b2f865f3d077c28bb51dbe3a479c

## Why

The spec was checked against the tree before the first write and matched: rev-4 cites the right symbols and paths, the three legacy_ledger_py copies were byte-identical, and the unit's starting state matched the spec's description. I built it as written in one pass commit. That commit sets the spec header to CLOSED (rev-4, 2026-11-21) and carries a Pass: TOOL-dWitnessedBar-67 trailer.

## Summary

Built TOOL-dWitnessedBar-67 in pass commit af84e1a7a on base 4ee815572.

**What changed**
- tools/lib/legacy_ledger.py, plus the identical block in tools/memory-tree/ and tools/gate-lint/ (all three checksums match):
  - S7: `_run_git` now passes `timeout=60`.
  - S9: a `--sha` whose resolved commit does not start with the given hex exits 2, names `--sha` and writes no home.
  - S18: `read_head_sha` now gives the reason `git for-each-ref listed <row>` or `git symbolic-ref printed <line>` instead of `exited 0`.
- tools/run-gates/verdict_backends.py (S10): the signer-temp sweep now writes one stderr line when the listing fails (naming the directory) or when the file test or age read fails (naming the entry). A missing entry stays silent.
- tools/govkit/govkit.py (S15): a comment beside `_check_exists_refused` names gen_build_index's `--asks --path` check and `1:x`.

**New test arms**
- run-gates.gov.test.sh: the record gains a fingerprint line ending in CR and the arm checks `rec_fp` (S2); a sweep probe with three stand-ins (S3/S10); the PM_SCRUB reader's words compared with what bash evaluates from the same lines (S4); a check that PM_SCRUB is assigned once (S17). Floor 47 -> 54.
- run-gates.evidence.test.sh: a last line with no LF (S11). Floor 316 -> 317.
- resolve-python.test.sh section 2o:
  - every fixture is now built with `-c init.defaultBranch=master init --ref-format=files`, with `GIT_CONFIG_NOSYSTEM`/`GIT_CONFIG_GLOBAL` exported for the block and unset after it (S6);
  - new cases: the one-file chain (S13), `--all` on the garbage fixture (S8), the timeout recorder (S7), the child-ref reason (S18) and the hex-named refs (S9);
  - the unit-65 block's "WHAT THIS DOES NOT CHECK" clause is rewritten.
- shell-role rows were widened through ratchet (widen-11) and then set to the measured counts: 1371, 706 and 2452. Widen itself writes the old count plus one; unit 68's row carries its measured count, so I followed that. This is recorded as a `Decided:` trailer.

**Records**: the acceptance ledger `2026-11-19-build-TOOL-dWitnessedBar-67-1-acceptance-ledger.md` has one line per criterion. `gen_build_index --write` output is committed; it rolled the build status to DEFERRED. `gen_map --write` changed nothing because no function was added. I declared the widen record with `--dispatch` before staging it.

**Checks that ran** (they stand in for the gov canary, run-gates evidence, the python resolver, and portability legs):
- Each suite's own arm lines were cut out and run with `eval` over scratch fixtures under %TEMP%/r67, which I deleted afterwards.
- The resolver cut gave 19 assertions and 0 fails, with an outer git config forcing `main` and `reftable` (AC5: every fixture read `files`). The gov cut gave 19 assertions and 0 fails. The evidence cut printed 5 ok.
- Every staged break turned red only on its own target: hook CR strip removed (red on `rec_fp '...\r'` on this Windows node), no OSError catch around the unlink, `exists()` instead of `is_file()`, the reader's `exit` dropped, a second PM_SCRUB statement, the `-n` guard dropped, the prefix check dropped, `timeout=` dropped, and the old `exited` reason restored.
- AC1, AC10, AC13, AC14, AC15 and AC17 were observed by grep and direct runs.
- `bash -n` passes on all three suites and py_compile on the three modules.
- The lexicon check passed for the new stand-in names.

**Owed to the close**
- The legs of §7.
- The RED-first observations for the three `New arm:` lines: gov (AC2, AC3, AC4, AC15), evidence (AC9) and resolver (AC5–AC8, AC11, AC16).
- AC12: unit 65's AC4 ledger line must be rewritten to name S14 and the per-file `grep -H` reading. The spec's section 1 and Rollout assign that to the main loop, so I did not write it.
- The AC5 red with `--ref-format=files` dropped belongs to unit 71.

**Checklist follow-up**: `gotchas --for-diff` flagged the "amendment leaves its other half standing" class. The unit-64 header in resolve-python.test.sh still says "Four fresh `git init`s ... each seed exits 1", above a loop that now builds five fixtures, the fifth of which arms. My follow-up edit was refused by scratch-guard because the unit is now CLOSED. The wording fix is the main loop's or a later unit's.

Nothing was skipped or timed out. I left the unstaged edits to help/reference/drive.md and units.md alone; they are not this unit's.
