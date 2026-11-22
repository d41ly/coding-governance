**Serves:** journal TOOL-dWitnessedBar-60

# TOOL-dWitnessedBar-60 — builder return 1 (run `wf_ddec5eff-e0c`), committed a3ee7a20d

## Why

TOOL-dWitnessedBar-60 is built and committed in one pass commit (subject names the unit, trailers `Pass: TOOL-dWitnessedBar-60` and Co-Authored-By). The spec status is CLOSED, rev-4, 2026-11-20. Before any edit, every code claim in the spec checked out against the tree: the four hook clear loops, BAR_SCRUBBED_KNOBS, the 23-name PM_SCRUB and its fold, the 7-name _gknobs, and _gfrom after the scrub at the scoped call. Both callers at base lack exactly the seven names in S2, and the driver suite's sed cuts are as cited. There was no divergence.

## Summary

## TOOL-dWitnessedBar-60: built and committed, gates and RED-first observations owed at the close

The unit is in commit a3ee7a20d (base b82f6b194399b4c1c2c007ffe40c9a96c48001cb). I ran no gate, suite or bar. Every criterion was checked by a probe of the changed code, listed below.

### What changed
- **`.githooks/pre-push`:** a new `BAR_CLEARED_KNOBS` list holds the eight knobs the hook clears. One loop over it replaces the four separate clears. `ENV_CLEARED` keeps the old order, which the hook suite's TOOL-dWitnessedBar-56 AC7 arm depends on.
- **`tools/run-gates/post-merge.sh`:** `PM_SCRUB` gains the seven missing names: `GATE_BASE_FROM`, `GATE_SELECTION`, `GATE_REGEN_CHECK`, `GATE_REUSE_PUSH`, `GATE_REUSE_DIGEST_ENV`, `GATE_REUSE_SAMPLE`, `GATE_REUSE_DAY`.
- **`tools/unattended/unattended.sh`:** `_gknobs` gains the same seven. I left the `_gknobs` comment alone, because the spec gives it to TOOL-dWitnessedBar-63 S29.
- **`tools/run-gates/run-gates.gov.test.sh`:** a new `check_bar_scrub_parity` function (the lexicon accepted the name) and three assertions: the shipped files, a `PM_SCRUB` copy with `GATE_SELECTION` cut, and a hook copy with no `BAR_CLEARED_KNOBS` line. `FLOOR_ASSERTIONS` goes from 35 to 38.
- **`tools/run-gates/run-gates.evidence.test.sh`:** after the AC5 run, a post-merge run with `GATE_SELECTION` and `GATE_BASE_FROM=inherited` inherited from the caller. `FLOOR_ASSERTIONS` goes from 310 to 311.
- **Shell-role ledger:** these five paths were declared in an extra `--dispatch` before I wrote them, and it admitted them.
  - `memory/project/shell-role.txt`: the rows for post-merge.sh (309), the evidence suite (2421) and the gov suite (547) are set to their measured counts, the way unit 58 did it.
  - The same file: the hook's row is lowered from 1721 to 1718, because the merged loop is shorter and the ledger flags a count that fell.
  - `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-60-widen-4.md`: the widen record.
  - `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-60-1-acceptance-ledger.md`: the acceptance ledger, one line per criterion.
  - `memory/builds/dWitnessedBar/RUN.md`: committed with the pass, since `--dispatch` writes rows in it.
- **Index regeneration:** `gen_build_index.py --write` rewrote `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README and the spec's records table, and all four are committed. The README's build status now reads DEFERRED, because unit 28 is deferred; that is the generator's output, not an edit of mine.

### Checks that ran (standing in for gates)
- **AC1** (stands in for `pre-push self-test` and `pre-push bar self-test`):
  - The spec's `sed` cut prints the eight names, and `grep -c GATE_SELECTION` prints 2 for post-merge.sh and 1 for unattended.sh.
  - I sourced the hook's new loop with four knobs set: `ENV_CLEARED` came out in the old order and none of the four was left in the environment.
- **AC2** (stands in for `run-gates gov canary`): I cut the parity function from the gov suite and ran it.
  - Over the built tree it printed nothing and returned 0.
  - Over the `PM_SCRUB` copy with `GATE_SELECTION` cut it printed "PM_SCRUB … lacks GATE_SELECTION" and returned 1.
  - Over the hook copy with no `BAR_CLEARED_KNOBS` line it printed "BAR_CLEARED_KNOBS reads empty" and returned 1.
  - Over the callers as they were at base it named exactly the seven names for each caller.
  - Over missing files all four "reads empty" lines appeared.
- **AC3** (stands in for `run-gates evidence`): I built a scratch bare remote and clone under %TEMP%, the same way the suite builds its post-merge fixture.
  - The new post-merge.sh exited 0, printed "not honoured from the environment: GATE_BASE_FROM GATE_SELECTION", and the bar's environment dump held neither knob (count 0), on both a first and a second run of the same commit.
  - The base commit's post-merge.sh in the same fixture gave count 1, so the check can fail.
- **AC4:** the spec's `sed` cut prints all 14 names. The `_gscrub` grep names the scoped call, which still carries `_gfrom` after the scrub. `env -u GATE_BASE_FROM GATE_BASE_FROM=inherited` delivers `inherited` to the child.
- **Other:** all five scripts pass `bash -n`. The shell-role counts came from the ledger tool's `--measure` mode, which grades nothing. `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit; I checked the classes it selected against the change and none needed a fix.

### Owed at the close (main loop)
- **Legs:** `pre-push self-test`, `pre-push bar self-test`, `measure-legs selftest`, `run-gates evidence`, `run-gates gov canary`, `scratch-guard self-test`, `tier2-review self-test`, `memory hygiene`.
- **New arm, `run-gates.gov.test.sh` (AC2):** see it fail with `GATE_SELECTION` cut from a copy of `PM_SCRUB`, then pass restored. The floor of 38 is counted by reading only.
- **New arm, `run-gates.evidence.test.sh` (AC3):** see it fail with the old `PM_SCRUB` restored, then pass. The floor of 311 is counted by reading only.
- **Shell-role leg:** it was not run to grade the five changed rows. That happens at the close under `memory hygiene` or its own leg.
- **Gap the close review should know about:** the parity function's "reads empty" lines for `BAR_SCRUBBED_KNOBS`, `PM_SCRUB` and `_gknobs` have no test arm in the suite. AC2 asks only for the hook's `BAR_CLEARED_KNOBS` case; I saw the other three only in my missing-files probe.

No command hit its time limit and nothing was skipped. The uncommitted changes to `help/reference/drive.md` and `help/reference/units.md` were in the tree before this pass started and were neither staged nor touched.
