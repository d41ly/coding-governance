# TOOL-dHashedPrelude-1, -2, -3 — acceptance ledger

**Serves:** journal TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3

Written by the unit passes, on node `d`, against BASE `3cf05f29`. Every run of the suite in this
build was bracketed by an external `sha256sum` and row count of
`C:/projects/coding-governance/.git/recall/queries.jsonl`, because the guard under repair cannot
grade itself. The baseline either side of every run but one was
`1d75bb5674679b76ae2c41e3d93c09891744062f91e3a71277b03b41b9cdc964` at 597 rows. The exception is the
AC1 break, recorded below.

The suite was run in full five times here and its import runs every arm, so each cost roughly two
minutes. `tools/run-gates/run-gates.sh` was not run by any unit pass; the close owes it.

**Evidences:** TOOL-dHashedPrelude-1
- AC1 — `the live query log is byte-identical after this run` — an arm calling `query.main()` in
  process was staged into the working copy and never committed. It drove the shipped writer,
  `log_event`, rather than appending a line by hand. The row reported
  `FAIL ... the gate wrote to it: 1d75bb567467 -> f9f4a1b54f07`, the suite exited 1 at 75/77, and the
  log went 597 -> 598 rows. The break was reverted from a backup and qid 598 quoted and trimmed; the
  log is back at `1d75bb567467` and 597 rows. A second FAIL row appeared from the nested
  adopter-layout run, whose fixture log went `(absent) -> 94c872725254`, so the guard fired in both
  the outer and the nested process
- AC2 — `main()` — with no break staged the row reports `ok` with detail `1d75bb567467`, the first
  twelve hex of the baseline, and the suite exits 0. `main()` computes no `before` of its own; it
  reads the module-scope value, so the row passes for the new reason and not the old one
- AC3 — `_LIVE_LOG_BEFORE` — the comment above the assignment names four things the guard does not
  check, verified by substring: A CONCURRENT WRITER, THE CACHE, A LOG ABSENT AT BOTH ENDS, A WRITE
  THAT IS REVERTED. The `recall/cache/` directory is named in the second
- AC4 — `sha256sum` — taken either side of all five runs. The one delta row is quoted in AC1 above
  with its `at` timestamp of 2026-09-28T15:52:45+00:00, which identifies it as this build's staged
  break rather than another session's. `SELFTEST_ARMS` read 71 throughout this unit with no line
  added to its provenance chain; it moves in unit 2
- AC5 — `_build_live_log_row` — called directly with each input: the none-value returns
  `('skip', ..., 'the repository did not resolve, so nothing was bracketed')`, a non-existent path
  with the absent-sentinel returns `ok`, equal digests return `ok` with detail `1d75bb567467`, and
  differing digests return `FAIL` with detail
  `the gate wrote to it: deadbeefdead -> 1d75bb567467`, carrying both prefixes
- AC6 — `_checks.append(_build_live_log_row(` — present in the body of `main()`, and neither
  `if live is not None` nor `if _LIVE_LOG is not None` survives anywhere in it

- AC7 — `_derive_live_log_digest` — given a path that exists and cannot be read, it returns
  `(unreadable)` and raises nothing; `_build_live_log_row` returns `skip` for that value at either
  end. The sentinel compares unequal to `(absent)`, which is what stops two unreadable readings
  from matching and announcing a protected log
- AC8 — `_read_live_log_verdict` — called with no arguments after `_LIVE_LOG_BEFORE` is rebound at
  module scope, it returns the prelude pair; the same rebind under a call-time lookup returns the
  post-arm values. Driven as a two-arm differential, so the claim rests on the contrast rather than
  on one green

**Evidences:** TOOL-dHashedPrelude-2
- AC1 — `main()` — the ordering arm driven over the shipped source with its one baseline line
  indented reports FAIL: `'\n_LIVE_LOG_BEFORE = ' occurs 0 time(s) at column 0, expected exactly 1`.
  Against the shipped file it reports ok
- AC2 — `_LIVE_LOG_BEFORE` — driven over a source whose `main()` recomputes its own digest, the arm
  reports FAIL: `main() does not read the module-scope baseline`
- AC3 — `main()` — thirteen mutation shapes were driven through the extracted arm and ten red:
  a conditional, a `try`, a comment-out, a duplicate, a deletion and a relocation below the
  `return` all report `0` or `2` unconditional `_read_live_log_verdict` append(s) in main();
  arguments at the call site report that the verdict takes none; literal defaults report the
  defaults are not the prelude pair; and the verdict defined below the arms reports its anchor
  occurs 0 times. The three that pass — a `globals()` write, a `global _LIVE_LOG` rebind and a
  module-scope re-derive below the arms — were each RUN to confirm the def-time binding makes them
  harmless. Superseded text follows, from before the binding landed:
  ``main() still guards the append with `if _LIVE_LOG is not None`; with the module-scope baseline in
  place that emits the row twice and both copies are green``
- AC4 — `_build_live_log_row` — the state arm returns
  `skip / skip / ok / ok / FAIL, and the FAIL names both digests` and reports ok in the suite
- AC5 — `_LIVE_LOG_BEFORE` — driven over the synthetic source `nothing here at all\nnot one anchor`,
  the arm reports FAIL naming the anchor rather than an ordering complaint. The default argument
  still reads `__file__` and reports ok
- AC6 — `SELFTEST_ARMS` — the arm's detail on the shipped file is
  `baseline 17175 < first arm 18403, 73 arm(s), main() at 150706`; all three figures are derived at
  run time and none is hard-coded. The counts in the spec's table were measured on the blob and the
  arm does not read them
- AC7 — `the declared arm count matches its pin` — reports ok with detail `73 == SELFTEST_ARMS`, and
  `the arm-count pin ends an unbroken provenance chain` reports ok ending at 73. The suite summary
  reads 78/78, which is 73 arms plus five appended run-property rows
- AC8 — `test_the_live_log_baseline_is_taken_before_any_arm_runs` — this docstring and that of
  `test_the_live_log_verdict_is_total_over_its_states` both name the real query log as the reason
  the arm is not behavioural. The ordering arm's did not on first writing and was corrected before
  the unit was committed; the checking predicate found it

- AC9 — `_read_live_log_verdict` — the ordering arm reds on literal defaults with `the verdict's
  defaults are ['Constant', 'Constant'], not the prelude pair`, on the verdict defined below the
  arms with its anchor occurring 0 times, and on a second module-level `main` with
  `'
def main() -> int:' occurs 2 time(s) at column 0, expected exactly 1`

**Evidences:** TOOL-dHashedPrelude-3
- AC1 — `grep -c "18 checks" tools/memory-recall/README.md` — prints 0, and line 26 now points at
  the run's own summary line and types no figure
- AC2 — `bash tools/check-kit-versions.sh` — exits 0. The anchored grep over `README.md` and
  `recall_conf.py` prints exactly three lines, all carrying 1.13:
  `README.md:3`, `recall_conf.py:4` and `recall_conf.py:50`. After the landing reconcile the same
  three carry 1.19, because `aRepatriatedFork` had moved the kit to 1.18 on `main` in parallel.
  `python tools/govkit/govkit.py epoch --base 3cf05f29` prints
  `epoch: memory-recall · clean · 1.13` with no FAILED line. Run at HEAD BEFORE this unit's commit,
  after two commits of `selftest.py` edits, the same command printed `clean · 1.12` — which is the
  §4 claim that `project-owned` files are outside `EPOCH_ROLES`, observed rather than asserted
- AC3 — `TOOL-aProbedToolkit-14` — the row is edited in place and reads ANSWERED for memory-recall
  by this unit, with the `tools/lexicon/README.md` half still open, and its status token is still
  OPEN
- AC4 — `## Parked decisions` — the build README carries an entry for each of the two deferrals, the
  selftest summary line and the missing `tools/**/*.py` eol pin, each with the option seen and the
  reason it was refused. Neither was given a backlog id: hygiene check 20 holds
  `memory/backlog/TOOL.md` at a shrink-only pin of 417 live rows and the shard is AT it, so a row
  cannot be added without draining two
