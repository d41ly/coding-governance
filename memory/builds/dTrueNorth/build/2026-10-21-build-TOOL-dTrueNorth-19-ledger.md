# TOOL-dTrueNorth-19 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-19

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the one
name the pass mints (`--suggest read_git_bytes --as py.function`, OK). Every criterion below was
observed by a probe of the changed code at the working tree over `55c7df4a9`: the generator's
`cmd_print_bindings` and `derive_audit_writers` in-process, and its `--print-bindings` CLI in a child,
over one fixture git repository under `%TEMP%/u19fx`, with the `HEAD` copy of `tools/` extracted by
`git archive` into `%TEMP%/u19base` so the probe is seen to move. The probe mirrors the selftest arms
this pass adds, scenario for scenario; the arms themselves, the `build-index selftest` and
`memory hygiene` legs, and the `New arm:` line's RED-first observation are owed to the close.

**Evidences:** TOOL-dTrueNorth-19
- AC1 — `cmd_print_bindings` — in-process over a fixture repository under `%TEMP%` whose one commit
  adds 601 unpinned `spec-audit` records under `memory/builds/tOne/reviews/`, the shortest path 101
  bytes, beside `tools/workflows/tier2-review.js` carrying `renderAuditBinding`, with
  `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"`: no `OSError`, 601 `P` rows and `Q<TAB>601<TAB>2026-01-01<TAB>0`,
  in 0.13 s. The `HEAD` kit's `cmd_print_bindings` at that commit raised `FileNotFoundError: [WinError
  206] The filename or extension is too long`, the red: its argv carried 61302 characters of paths.
- AC2 — `derive_audit_writers` — the same fixture on a branch drops the function from the harness and
  deletes one record, then a later commit re-adds it beside a record first added there; the log lists
  the re-added path twice, and `derive_audit_writers` over the two returned only the first-added
  record, so the re-add is keyed to its first adding commit, whose harness carries the function.
  Keeping the newest add would return both. The `HEAD` reader keeps the oldest too, by the last of a
  newest-first walk, so this arm's red is a staged break, owed at the close.
- AC3 — `cmd_print_bindings` — with `git log` resolving to a stub script that prints `fatal: the stub
  refuses git log` and exits 128, the call raised `Problem`: `` `git log --no-renames --diff-filter=A
  --reverse --format=%x00%H --name-only -- :(glob)memory/builds/*/reviews/**` exited 128: fatal: the
  stub refuses git log``; and the generator's `--print-bindings` there, run by the host's `python`
  through a shim that installs the same stub and then runs the script as `__main__`, exited 2
  printing that line. A `git log` raising
  `FileNotFoundError` at the spawn raised `Problem` naming the command and `could not start`. The
  `HEAD` kit under the same shim exited 1 on a `CalledProcessError` traceback, the red.
- AC4 — `cmd_print_bindings` — a last commit deletes the harness and adds a record: its `P` row
  printed, and `Q<TAB>603<TAB>2026-01-01<TAB>1` counts only the record a present harness lacking the
  function wrote as exempt. The `HEAD` reader already grades a `missing` answer, so this arm's red is
  the staged break the `New arm:` line names, owed at the close.

Over the real tree, `--print-bindings` exits 0 printing `Q<TAB>0<TAB>2026-10-22<TAB>0`. With the cutoff
passed in-process as 2026-09-01 it graded 159 `spec-audit` records, and the glob reader's
record-to-adding-commit map equalled the argv reader's for all 159; none sits outside the pathspec.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, the splice break (each product function the unit's pass commit changed put back to its text at that commit's parent, each function it added stubbed to raise), 6 of its 6 arms red. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.
