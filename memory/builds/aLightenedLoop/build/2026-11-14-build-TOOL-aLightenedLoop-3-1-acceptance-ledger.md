# TOOL-aLightenedLoop-3 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-3

No merge bar, no self-test suite and no gate ran in this pass, and neither did the whole-tree
spec-token checker. The criteria a probe can reach were observed in the spec's pass probe, `l3.sh`
as §4 states it, built under `%TEMP%/l3`, with one change: its first line reads
`G=$(pwd -W 2>/dev/null || pwd)` where §4 reads `G=$(pwd)`. On this node Git Bash spells the
worktree `/c/projects/...`, and the stub's `spec_from_file_location` cannot open that path, so the
unchanged probe never imported the checker and every count read 0. With the Windows spelling every
line below is the probe's own output.

Three readings the close should know. First, AC1's `diff` prints 52 lines before and after this <!-- PINNED 2026-11-14 -->
pass, of which 26 are `<` or `>` lines: §4's "26 `diff` lines" counts the changed lines, and the <!-- PINNED 2026-11-14 -->
twins differ in exactly the install-prefix placeholders they did before. Second, the driver suite's
cache arm had a third step asserting the old over-sensitivity that §4 does not name: step a expected
a re-run because the declared dispatch row moved the run-state file. §4's "When the cache hits"
says that row no longer moves the key for a run with no packet, which the suite's fixture is, so
step a is inverted with b and c, at the same count of assertions. Third, the suite arms were written
and not run; the floor raises are counted off their own lines.

The owner's parity captures: `python tools/check-spec-tokens.py --spec` over this spec and over
unit 1's, once through the checker at `60ca1644b` (its source executed with `__file__` set to the
real path, so its kit resolves as it does in place) and once through this pass's: `cmp` printed
nothing for both, exit 0 and 0, 14 lines each; 1914 ms base and 1806 ms built for this spec, 1572 <!-- PINNED 2026-11-14 -->
ms and 1488 ms for unit 1's, node `a`. The driver's refusal and admit texts are untouched in the <!-- PINNED 2026-11-14 -->
diff; AC10's timing and whole-tree parity are the close's.

**Evidences:** TOOL-aLightenedLoop-3
- AC1 — `tools/workflows/unattended-build.template.js` — `grep -c "Before each unit's Workflow call, run"`
  printed 1 over it and 1 over `tools/workflows/unattended-build.js`; `diff` between them printed
  the same 52 lines as before, 26 changed. The suite's `"declare":` arms are the close's to observe. <!-- PINNED 2026-11-14 -->
- AC2 — `grep -c "The main loop declared this unit's write set" tools/workflows/unattended-unit.js` —
  printed 1; `grep -c "Declare the write set with" tools/workflows/unattended-unit.js` printed 0,
  `grep -c "A REFUSAL FROM IT IS BINDING" tools/workflows/unattended-unit.js` 1 and
  `grep -c "This run has NO run-state file" tools/workflows/unattended-unit.js` 1.
- AC3 — `derive_read_path` — loaded from `tools/lib/read_open.py` under `python -I -c`, it returned
  the realpath and False for a plain read, None for a `w` mode, None for an int path, None for
  `os.O_WRONLY` with mode None, the source file and False for a `.pyc` under `__pycache__`, and the
  name as spelled with `refused` True for `__pycache__/odd.pyc`.
- AC4 — `read_open_py` — the block extracted from `tools/lib/read_open.py`,
  `tools/check-spec-tokens.py` and `tools/policy/check_policy.py`, carriage returns dropped as the
  parity table drops them: `cmp` printed nothing for both pairs, and
  `grep -c "derive_read_path(" tools/policy/check_policy.py` printed 2. The parity row and the
  policy fixtures are the close's.
- AC5 — `manifest read a.txt 1 run ls-files 1 log 0` — printed by `bash "$SCRATCH/l3.sh"`.
- AC6 — `SPEC_TOKENS_INPUTS` — `python tools/check-spec-tokens.py --spec` over this spec with it
  naming a scratch file and without it: `cmp` over the two stdouts printed nothing, exit 0 and 0.
  The record held 41 lines, none `popen`, and `--input-key` over it printed a 40-hex digest in <!-- PINNED 2026-11-14 -->
  0.70 s. The whole-tree comparison is the close's. <!-- PINNED 2026-11-14 -->
- AC7 — `key popen 1 0` — printed by `bash "$SCRATCH/l3.sh"`.
- AC8 — `cache unchanged runs 1 skipped 1` — printed by `bash "$SCRATCH/l3.sh"`, then
  `cache unread runs 1 skipped 1`, `cache commit runs 1 skipped 1`, `cache edited runs 2`,
  `cache untracked runs 2 skipped 1` and `cache slug runs 3`.
- AC9 — `cache refused runs 5` — printed by `bash "$SCRATCH/l3.sh"`, then
  `cache foreign runs 6 noted 1 skipped 1`, `cache moved runs 8 said 1 skipped 1`,
  `cache untraced runs 10 said 2` and `cache off runs 12 said 2`. The probe's whole run took 38 s. <!-- PINNED 2026-11-14 -->
- AC10 — `bash "$SCRATCH/l3-time.sh"` — the close's to observe: it runs
  `run_spec_token_check aLightenedLoop`, the whole-tree checker, which only the main loop may run.
- AC11 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — printed
  nothing; `grep -c 'a digest of every file and git answer its last admitted run read' memory/guides/UNATTENDED-VERBS.md`
  printed 1, and `grep -c 'launcher, HEAD and the run-gates working-tree fingerprint' memory/guides/UNATTENDED-VERBS.md`
  printed 0.
