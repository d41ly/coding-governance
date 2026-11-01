**Serves:** journal TOOL-dSafePassage-95

# TOOL-dSafePassage-95 — acceptance ledger

The unit as built, at spec rev-2. Product write: `tools/govkit/selftest.py`, inside
`check_floor_bash` only, each edit as the spec's §4 fenced text writes it. S1's `stand94` follows
`stub92` and is the one name `read_stub_tail` uses for the stand-in. S2's `pyc94` and `mtime94`
join the third `[dSP-94]` check. S3's two `[dSP-95]` restore checks follow the two `[dSP-94]`
checks after `[dSP-91 L2]`. S4's `steps94` is staged by `build_staged_copy` and loaded in a `try`
that sets `sentinel94`, and `read_fallback_argv`'s memo read sits in its own `try`. S5's
`src94.count(anchor94) == 1` joins the second `[dSP-94]` check. `tools/govkit/upgrade_steps.py` and
`tools/govkit/steps/python_floor.py` are not edited.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11) from this worktree's root. AC1 and AC2 are the spec's commands, with the
`tmp` directory in the run's scratchpad rather than `tempfile.mkdtemp`.

Owed at the close: AC4, which is the RED-first observation of §7's six `New arm:` lines (each
break of §4 "Measured" staged in a `git archive HEAD tools` scratch tree, the `rmtree` and
`os.utime` breaks at N = 6), and the §7 legs at the bar, `govkit selftest` among them going red to
green on `[dSP-71] AC4`.

**Evidences:** TOOL-dSafePassage-95
- AC1 — printed `ok   [dSP-87 AC5]`, `ok   [dSP-91 L2]`, two `ok   [dSP-94]` lines, `ok   [dSP-95] the read gives the parent's bash cache back`, `ok   [dSP-95] the read that raises gives the copy's bash cache back`, seven `ok   [dSP-92]` lines, one `ok   [dSP-94]` line, then `[]`.
- AC2 — printed `([], 1)`, `ok` for both `[dSP-71] AC4` lines and for `[dSP-71] AC3`, then `[]`.
- AC3 — the `os.utime(stand94, ns=(0, 0))` grep printed one line, `:4543`, after `stand94.write_text` at `:4541`; the `stub92 / "upgrade_steps.py"` grep printed nothing; `git diff --numstat 0e5967090 -- tools` printed one line, `30	11	tools/govkit/selftest.py`; the records-stripped comparison of 94's spec printed `True`.
- AC4 — owed at the close, not run in this pass.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in a scratch clone of `390033278` (batch g, `2026-11-01-prompt-TOOL-dSafePassage-91-1-researcher.md`), each break staged alone and restored. `[dSP-71] AC4` (tools/govkit/selftest.py `check_staged_copies`), with the stand-in spelled back as `stub92 / "upgrade_steps.py"`: `FAIL [dSP-71] AC4 no line of selftest.py outside build_staged_copy stages the engine in a bare local directory … — outside: [4530]; inside: 1` and `FAIL [dSP-71] AC4 a hand-picked copy appended to selftest.py is named by its line — named: [4530, 19818]` (at HEAD S1 folded 0e5967090's lines 4523, 4525, 4527 into one name, so the guard names 4530 alone). In check_floor_bash: the `finally` cut reds both `[dSP-95]` (`argv94 ['bash', 'x']; None`); the restore moved onto the return path reds the raise-path `[dSP-95]` alone (`cut94 OSError(22, …)`); the replacement losing its colon reds `[dSP-95] the staged copy of upgrade_steps.py loads — SyntaxError("expected ':'")` with the second `[dSP-94]` and the raise-path `[dSP-95]`, the run continuing; a second anchor appended reds the second `[dSP-94]` (`anchor count 2`) beside the loads FAIL; os.utime cut, 6 of 6 RED (`pyc True; mtime_ns 1793532381806939300`); shutil.rmtree cut, 6 of 6 RED; the cache removed before pyc94: `pyc False; mtime_ns 0`. GREEN restored after each: `FAILURES []`. Record note: 95's Measured row for the check_runs break names only the two `[dSP-94]` checks; at HEAD it also fails the return-path `[dSP-95]`, because 96 added `argv94 == ["bash", "x"]` to it — a stale record, not a red.
