# PLAY-dOrderedCharter-85 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-85

Each line is a probe this pass ran at rev-1 of the spec, over `3279b49c7` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: each checker the criteria name is the close's, and where a line says
"owed" the main loop observes it after every unit is terminal. The probes ran a criterion's own command, or
`write_merge_fold` lifted out of the lander and called over a scratch fixture repository holding one merge.

**Evidences:** PLAY-dOrderedCharter-85
- AC1 — `write_merge_fold` — the criterion's `grep -n` over `tools/push-main.sh` reads, inside `cmd_prepare`, `run_gov_first`, then `write_merge_fold`, then `run_regen`, then `write_merge_fold` (PINNED, at 3279b49c7 with the pass applied). Over the fixture, the function returned 0 and left HEAD unmoved on a clean tree; on a dirty one it returned 0 with HEAD a merge of the same parents and subject, the tree clean and the new file tracked; with a first parent that does not exist it returned 1.
- AC2 — `push-main: prepared` — owed: the main loop runs this run's own `--prepare` after both units close.

**Owed to the close.** Every leg of the spec's Gates section, and the `New arm:` line's arm 41 in `tools/push-main.test.sh`,
observed red at the base lander and green at the close. One new refusal site carries no arm asserting its own text: the
prepare's fold before the regeneration, `could not fold the upgrade steps' output into the merge before the regeneration`.
