**Serves:** journal TOOL-dSafePassage-5

# TOOL-dSafePassage-5 — acceptance ledger

The unit as built, at spec rev-11. New: `tools/govkit/upgrade_walk.py` (the leg and its CLI),
`tools/govkit/fixture_target.py` (`build_target`, `make_target` moved there unchanged), and the
fixture `tools/govkit/fixtures/release-0/` (`pin.txt`, `deploy.toml`, `plants.toml`, `arms.toml`,
`arms/arm_step.py`, `seed/AGENTS.md`). `selftest.py` calls `build_target` at every former
`make_target` site, its two local wrappers renamed `build_own_target` and `build_levelled_target`,
and gains two `[dSafePassage-5]` rows (`--list`, `--list --pin HEAD`). The leg row `upgrade-walk`
in `tools/gate-legs.json`, its `[[exempt_leg]]`, its subject pin, its dossier claim, its `[[usage]]`
row and the `help/upgrade-steps.md` section land with it. This pass starts from the fifth
dispatch's change set and adds rev-11's `kill` compare: the re-run and `up` digests are read with
the killed step's `steps` row without `via` (`derive_tree_digest(..., unvia=<id>)`), and the re-run's
row must carry `"via": "witness"` exactly when the step's witness, run through `run_step_isolated`
over a copy of the killed state, answers `ok`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each case was run on node d
(Windows) as the leg's own CLI, one `--case` per run; the logs of the cases this pass did not
change are the fifth dispatch's (`TOOL-5-wip5/logs-pass5/` in the run's scratchpad), over the same
code but the `kill` compare. A follow-up commit pins `core.autocrlf=false` on the scratch clone,
which the bug-class checklist selected (`fixture-inherits-ambient-machine-state`); after it,
`--case down` exited 0 (570 s) and `--case kill --step govkit/receipt-schema-4` exited 0 (714 s),
the cases the clone's bytes reach first, and the other cases' runs above predate the pin.

**Evidences:** TOOL-dSafePassage-5
- AC1 — `upgrade_walk.py --list` exit 0 at this pass: `pin 60d90cb71db51e651aa1c5efe3f6d48ba21a997d · landed ref 1a61f21a… · 3 step(s)`, step 1 `govkit/receipt-schema-4`, step 2 `lib/python-floor-3.15`, step 3 `agent-cap/fanout-cap-to-agents-in-flight`, then 7 plant, 2 gov_plant, 1 condition and 9 arm rows. The selftest row over it is owed at the close.
- AC2 — `--case up` exit 0 (fifth dispatch, 231 s): release-0 by the pinned clone's own apply, `exit 0 · receipt schema 3`, `the policy adopter's re-run committed .governance/policy.json`, each of the 3 steps `applied · witness ok`, `GREEN`.
- AC3 — `--case down` exit 0 (420 s): `the rollback's digest equals release-0's`; `--inject lossy-down` exit 1: `the digest differs at .uw-arm/lossy, :index .uw-arm/lossy`.
- AC4 — `--case reup` exit 0 (537 s): `the second walk's digest equals the first's`.
- AC5 — `--case plants` exit 0 (211 s): 7 passed, `fanout-cap · carried · runtime.agents-in-flight reads 2`, `edited-render` and `edited-retired` `ordered`; `--inject drops-plant` exit 1: `engine-edit · tools/memory-tree/README.md: expected carried`.
- AC6 — `--case skip` exit 0 (887 s): the schema step and the fan-out step load-bearing by their digest, the floor step `floor-below: unskipped it reads failed, skipped applied`; `--inject no-op` exit 1: `upgrade-walk/no-op · not load-bearing`.
- AC7 — `--case kill` exit 0 at this pass (1014 s): `govkit/receipt-schema-4 · lock holder dead, no row for it (schema-3 receipt), the re-run equals up, via witness as its witness holds, the rollback equals release-0`; `lib/python-floor-3.15 · forced · … it failed interrupted:, the re-run equals up, via witness as its witness holds …`; the fan-out step `… no via …`; summary `kill 3 passed 0 red · forced kill lib/python-floor-3.15`. Red at the fifth dispatch before rev-11's compare: the schema step `the re-run's digest differs from up's at .governance/install.json`. Arms at this pass: `--inject witness-first` exit 1, `differs from up's at .uw-arm/1-payload`; `--inject not-rerunnable` exit 1, `differs from up's at .uw-arm/0-lines`.
- AC8 — `--case fail` exit 0 (558 s): the schema step `the receipt at schema 3, its line not recorded`; the floor step `forced · … last applied govkit/receipt-schema-4, it failed with exit 1`; the fan-out step `last applied lib/python-floor-3.15, it failed with exit 1`.
- AC9 — `--case shims` exit 0 (236 s): `the clone holds no tag`, `read_releases returned none`, `shims: 0 declared`; `--inject held-shim --inject drops-shim` exit 1: `upgrade-walk/held-shim · its forwarder tools/check-kit-versions.sh is gone from the walked target`.
- AC10 — `--case isolation` exit 0 (142 s): each of the 3 steps `isolated`; `--inject breaks-isolation` exit 1: `upgrade-walk/breaks-isolation · breach`.
- AC11 — `upgrade_walk.py --list --pin HEAD` exit 2 at this pass: `the pin e818aace carries an [[upgrade]] row at tools/govkit/steps.toml:14` (and `:30`, `tools/hooks/kit.toml:138`); `--case up --inject missing-plant` exit 2 (fifth dispatch): `tools/upgrade-walk-no-such-file.md is absent at release-0`.
- AC12 — `python tools/govkit/upgrade_walk.py` with no arguments was not run: the whole leg is longer than a role agent's 600 s command bound. The per-case runs above stand in for it, every case green and every arm red on its case; the whole leg's run, its time and the `ceiling` it sets are owed at the close.
- AC13 — `git grep -n -F "upgrade-walk"` finds the leg's name in `tools/gate-legs.json`, `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv` and `memory/map/features/govkit.md`; `tools/run-gates/ceiling-evidence.txt` gains its row only from `derive-ceilings.py --write` over AC12's measured run, owed at the close with it, and the leg's `ceiling` of 7200 stands until then.
- AC14 — `git grep -n -w -e "def build_target" -e "make_target"` over `tools/govkit/` less the two excluded files printed one line, `tools/govkit/fixture_target.py:17:def build_target(...)`.
- AC15 — `git grep -n -e "upgrade_walk.py"` finds `help/upgrade-steps.md:296-302` and `tools/govkit/usage.toml:187`, its `script:` row. `python tools/govkit/docs_leg.py` is a gate leg the role hook refuses here: owed at the close.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, for `tools/govkit/upgrade_walk.py`, observed in `dsp5b` at `83817478f` with the break staged alone and restored. The break was `--case skip --step upgrade-walk/no-op --inject no-op`, which exited 1 after 677 s with `upgrade-walk: RED: skip · upgrade-walk/no-op · not load-bearing: skipped, the digest equals up's and its witness exits 0`. Restored without the arm (`--case skip --step agent-cap/fanout-cap-to-agents-in-flight`), it exited 0 after 507 s with `skip · agent-cap/fanout-cap-to-agents-in-flight · load-bearing · the digest differs at 6 path(s)` and `upgrade-walk: GREEN`. Only the `no-op` arm of `arms.toml` was staged.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f` given `refs/remotes/origin/main` at main's `1a61f21a` and `origin/HEAD` pointed at it. Under tools/govkit/selftest.py (the main-level `upgrade_walk` block), the break was `check_release_pin` dropping its `[[upgrade]]` hits: `FAIL [dSafePassage-5] upgrade_walk.py --list --pin HEAD exits 2 naming an [[upgrade]] row the pin carries — exit 0`. Restored, GREEN: both dSP-5 arms `ok` under that origin, with `upgrade-walk: step 1 · govkit/receipt-schema-4`, `step 2 · lib/python-floor-3.15`. In a plain `--shared` clone, `origin/HEAD` names this worktree's branch, so `--list` reds at HEAD with agent-cap walking first, before and after the break. That red is inconclusive for this break, but it is AC1's own "Red when" case, so it also shows that arm red.
