**Serves:** journal TOOL-dSafePassage-96

# TOOL-dSafePassage-96 — acceptance ledger

The unit as built, at spec rev-1. Product write: `tools/govkit/selftest.py`, inside
`check_floor_bash` only, each edit as the spec's §4 fenced text writes it. S1: the raise-path
`[dSP-95]` check gains `isinstance(cut94, OSError)` and its detail names `cut94`. S2: the
return-path `[dSP-95]` check gains `argv94 == ["bash", "x"]` and its detail names `argv94`. S3:
`shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)` sits after `steps94`'s placeholder and
before the `try` that calls `build_staged_copy`. `build_staged_copy` and
`tools/govkit/upgrade_steps.py` are not edited. `tools` did not move between the spec's base
`744d2551` and this pass's parent `dac8b346`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11) from this worktree's root. AC1 is the spec's command, with the `tmp`
directory in the run's scratchpad rather than `tempfile.mkdtemp`.

Owed at the close: AC2, AC3 and AC4, which are the RED-first observations of §7's two `New arm:`
lines (each break of §4 "Measured" staged in a `git archive HEAD tools` scratch tree), and the §7
legs at the bar.

**Evidences:** TOOL-dSafePassage-96
- AC1 — both runs on one `tmp` printed `ok` for `[dSP-87 AC5]`, `[dSP-91 L2]`, both `[dSP-94]` reads, both `[dSP-95]` restore checks, seven `[dSP-92]` lines and the last `[dSP-94]` line, each run then `[]`.
- AC2 — owed at the close, not run in this pass.
- AC3 — owed at the close, not run in this pass.
- AC4 — owed at the close, not run in this pass.
- AC5 — the grep printed one line, `tools/govkit/selftest.py:4494`, above the `try` at `:4495`; `git diff --numstat 744d2551 -- tools` printed one line, `5	2	tools/govkit/selftest.py`. Beside it, `read_handpicked_copies` over the edited selftest printed `([], 1)`.
