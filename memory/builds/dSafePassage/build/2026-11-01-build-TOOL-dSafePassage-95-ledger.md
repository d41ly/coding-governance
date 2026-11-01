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
