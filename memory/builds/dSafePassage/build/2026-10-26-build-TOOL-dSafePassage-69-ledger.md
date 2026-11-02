**Serves:** journal TOOL-dSafePassage-69

# TOOL-dSafePassage-69 — acceptance ledger

The unit as built, at spec rev-2. `tools/govkit/steps.toml`: the floor row's down names `3.12`, its
comment saying why (S1). `tools/lib/python_floor.py`: `check_down_floor`'s static branch runs
`_scan_pep701` only where the restored floor is below 3.12, the docstring saying so (S2); `main`'s
`down` prints its mode line, findings, count line and success lines on stderr, the count line naming
the first finding (S3). `tools/govkit/upgrade_steps.py`: `run_step_isolated` gives an up or a down
that exits non-zero with only whitespace on stderr a one-line tail naming that and stdout's last line
(S4). `tools/lib/resolve-python.test.sh` arm 1e gains three checks and `check_step_isolation` in
`tools/govkit/selftest.py` one `[dSP-69]` check (S5). `help/python-floor.md` and
`help/upgrade-steps.md` updated (S6).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each probe ran on node d
(Windows), from the worktree root.

**Evidences:** TOOL-dSafePassage-69
- AC1 — a probe reading the floor row's down with `tomllib`, taking `down[3]` and calling `check_down_floor(".", prior, "60d90cb7")` printed `3.12 interpreter C:\Users\daily-agent\AppData\Roaming\uv\python\cpython-3.12-windows-x86_64-none\python.exe []` in 17 s. Red at HEAD `dbd1d6b01` per the spec's §4 table: the row named `3.11`, and the finding at `tools/memory-recall/check-recall.py:394`.
- AC2 — the same probe with `pf.resolve_floor_interpreter = lambda v: None` printed `3.12 static []`, and with `3.11` `3.11 static ['tools/memory-recall/check-recall.py:394: a # in a replacement field']`. A scratch git fixture under `%TEMP%` holding a committed `v = f"{'#':>3}"` in `hash.py` graded statically printed `('static', [])` at 3.12 and `('static', ['hash.py:1: a # in a replacement field'])` at 3.11.
- AC3 — `python -I tools/lib/python_floor.py down 3.11 . 60d90cb7 2>/dev/null` printed nothing and exited 1. With `2>&1 >/dev/null` it printed `python-floor down: mode static, because no interpreter at 3.11 resolves here`, then `tools/memory-recall/check-recall.py:394: a # in a replacement field`, then `python-floor down: 1 finding(s) under the floor 3.11, the first tools/memory-recall/check-recall.py:394: a # in a replacement field; nothing was written`, exit 1.
- AC4 — `run_step_isolated` over a `git init` scratch target with `gov_root` this checkout, row `fixture/x` whose up and witness are `["python", "-c", "print('the reason'); raise SystemExit(3)"]`: the up returned `{'verdict': 'failed', 'rc': 3, 'tail': "fixture/x up: exit 3 with nothing on stderr, where a step writes its failure; stdout's last line: the reason"}`, the witness `tail` `''`, and an up writing `to err` on stderr kept `tail` `'to err'`. Red: the same probe over HEAD `4ef2e9fb9`'s `upgrade_steps.py` returned the up's `tail` `''`.
- AC5 — owed at the close: `python -I tools/govkit/upgrade_walk.py --case kill --step lib/python-floor-3.15` is the `upgrade-walk` gate leg's own case, which no pass may run.
- AC6 — `git grep -n -e "down 3.11" -e "under 3.11" -- help/python-floor.md` printed nothing; `git grep -n -F "down 3.12" -- help/python-floor.md` printed one line, line 74, the step's down.
- AC7 — owed at the close: `python -I tools/govkit/upgrade_walk.py --case down`, the same leg's case.

Owed at the close: both `New arm:` lines of the spec's §7 red on their staged break and green
restored — arm 1e's three checks through the resolver self-test, the `[dSP-69]` check through
`govkit selftest` — and the spec's §7 gates. `bash -n` over the edited suite file and `ast.parse` over
the three edited Python files passed.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line in scope, `tools/lib/resolve-python.test.sh` arm 1e. The break was `30ba39028`'s `python_floor.py` hunks reversed, which brings back the stdout report and the ungated `_scan_pep701`. All three checks went red: `FAIL the down printed on stdout, which the step's tail never reads: python-floor down: mode static, …`, `FAIL the down's last stderr line does not count its finding and name the first:`, and `FAIL the static grade of a committed '#' in a replacement field did not pass under 3.12 and name hash.py:1 under 3.11: ('static', ['hash.py:1: …', …])`. Restored: `SLICE PASS (9 assertions)`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-69 check), the break was `run_step_isolated` keeping the stderr-only tail: `FAIL [dSP-69] an up that fails with nothing on stderr stops with a tail naming that and its stdout — up {'verdict': 'failed', 'rc': 3, 'tail': ''}`. Restored, GREEN: 1 of 1 `ok`.
