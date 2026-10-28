**Serves:** journal TOOL-dSafePassage-80

# TOOL-dSafePassage-80 — acceptance ledger

The unit as built, at spec rev-5. Product writes: `tools/gate-legs.json` (S1, S2, S3, S6, S7, five
`"ceiling":` lines), `tools/run-gates/ceiling-evidence.txt` (S4, the close's three rows committed as
the working tree held them, no `--write` run), `tools/run-gates/selftest-budgets.txt` (S5, the
`upgrade-walk` row), `tools/govkit/upgrade_walk.py` (S8, the probe stop in `main`'s case loop) and
`memory/guides/SESSION-KICKOFF.md` (S9, the `last-audit` re-stamp; §B re-read, no line moves).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) over this worktree's working copy and index, by §4's probes written to the run's
scratchpad and by `git diff --cached`.

Where the build met what the spec does not say: AC6's command is the `upgrade-walk` leg's own
command, which scratch-guard row G1 refuses a role agent, so it was not run here. In its place a
stubbed probe loaded `upgrade_walk.py` by path, replaced every seam that clones, builds or walks
(`load_engine`, `build_release_tree`, `run_walk_case`, `run_case_arms` and the readers), and drove the
real `main` loop.

Owed at the close: AC2 (`derive-ceilings.py --check`, G1 for a role agent), AC6's real run, AC7's
`manifest-check.sh --staged` as a standalone command (the pass commit's pre-commit hook runs it), the
§7 legs at the bar, and the `New arm:` line's RED-first observation, the `upgrade-walk` row of
`foreign-prefix.gov.test.sh`'s population.

**Evidences:** TOOL-dSafePassage-80
- AC1 — `python <scratch>/ceiling_probe.py` — printed `step-gate 130 4.4 124.4 5.6 ok least`, `docs 130 2.7 122.7 7.3 ok least`, `upgrade-walk 14360 7177.0 14354.0 6.0 ok least`, `routed commits name a specced unit 510 253.0 506.0 4.0 ok least`, `spec tokens (a spec's own names resolve) 740 366.0 732.0 8.0 ok least`, `ALL-SHORT []`.
- AC2 — owed to the main loop: a role agent may not run the checker (G1).
- AC3 — `git diff --cached -U0 -- tools/gate-legs.json` — five hunks, each one `-` and one `+` `"ceiling":` line: 300 to 510, 60 to 130, 60 to 130, 7200 to 14360, 390 to 740.
- AC4 — `python <scratch>/budget_probe.py` — printed `unbudgeted []` and `upgrade-walk 10770 10770 argv-empty`.
- AC5 — `git diff --cached -U0 -- tools/run-gates/ceiling-evidence.txt` — three hunks: `@@ -114,0 +115 @@` adds `routed commits name a specced unit` at `253.0`, node `a`; `@@ -133 +134 @@` replaces `spec tokens (a spec's own names resolve)` `195.0` with `366.0`, node `a`; `@@ -144,0 +146 @@` adds `upgrade-walk` at `7177.0`, node `a`. No other line removed.
- AC6 — the real run is owed (G1). `python <scratch>/probe_stop.py tools/govkit/upgrade_walk.py` — under `FOREIGN_PREFIX_PROBE=1` it printed `probe: 0 ['up'] 0 True no arms field`, the summary naming `up 1 passed 0 red` and no other case; unset, it walked all nine cases and the arms once with no marker; `0`, the same; `OK`. With HEAD's `upgrade_walk.py` in place the same probe raised `AssertionError` on the probe line, so it can fail.
- AC7 — `git diff --cached -U0 -- memory/guides/SESSION-KICKOFF.md` — one hunk, the `last-audit:` line replaced by one naming `460ffb587be40302572d24350330b4da458bbaf8`, the HEAD the pass was built on. `manifest-check.sh --staged` ran as the pass commit's pre-commit hook.
