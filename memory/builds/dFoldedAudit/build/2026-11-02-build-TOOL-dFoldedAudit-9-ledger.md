# TOOL-dFoldedAudit-9 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-9

The acceptance criteria were observed by this unit's builder over the tree of this commit, on Fixture G of section 6 at `%TEMP%/fa9g`, built fresh per criterion, by two scratch probes of the driver and the leg as CLIs. No gate, suite or bar ran. Each new arm's RED-first observation is the close's, and it is not recorded here.

The driver probe executed 111 assertions on the rows the arm block carries, with the policy kit and with its skip path, and both paths counted 111. The leg probe executed 14 on Fixture G. The check-unattended block spells the same populations over `mkdisp`, and that block has never run.

**Evidences:** TOOL-dFoldedAudit-9

- AC1 — `--dispatch builds nothing while the chain reads CONTINUE` — `--chain-verdict` printed `round 1 · CONTINUE · reason open · audit FIX-dFix-2`, the dispatch exited 1 printing `UNATTENDED check 118 FAILED` and the refusal naming that id, and the record held no `dispatch · item` row.
- AC2 — `--dispatch builds nothing while the chain reads HOLD` — exit 1 naming `review.spec-audit.chain-ceiling` over the four promoting rounds, and again after `--park` and a hand-written `handoff · item owner-decision` row.
- AC3 — `chain-ceiling = 6` — the committed policy file moved the refusal from HOLD to `CONTINUE` naming FIX-dFix-7, and a fifth clean round auditing that id exited 0 with a row in the record.
- AC4 — `unattended: dispatch — chain dFix · round 1 · STOP · reason clean` — exit 0 and one row, and over FA5's AC6 record exit 0 printing `STOP · reason own-work`.
- AC5 — `--dispatch reads a terminal spec exit no chain round records` — exit 1 naming `s2` beside an older STOP, and the same with no chain record; after that round's `--record-round` the refusal named `CONTINUE` and the subject sentence was gone.
- AC6 — `reason unreviewed` — a record carrying `spec-audit: 2026-11-01`, with no row and no chain record, exited 1 printing `round 0`.
- AC7 — `unattended: dispatch — chain` — absent, with exit 0, over AC1's hand-committed record under a blank cutoff at BASE, an `EARLY` record, and `disposal = "promote-all"` with the policy kit.
- AC8 — `no spec audit is declared or recorded` — printed at exit 0 over one row on subject `dFix`.
- AC9 — `--folded and --promoted are counted only at a spec audit's terminal exit past SPEC_FOLD_CUTOFF` — printed when a run commit dated a blank key, and the same call exited 0 when a run commit blanked a dated one.
- AC10 — `spec subject(s) S1 record a terminal row` — printed for the first tree, and no `UNATTENDED check 2 FAILED` line for the second.
- AC11 — `read_fold_cutoff` — with `anchor-sha:` at main's tip, `anchor-kind: local` and `base:` on a run commit above it, the call refused and the leg printed the first line. With `base:` at a dated commit, an anchor above it and an anchor at it each exited 0.
- AC12 — `UNATTENDED check 118 FAILED` — printed by the dispatch, beside `--review cannot record this spec audit exit: ` from AC9's call and a check 2 line naming the record, for each of `return 0`, `SPEC_FOLD_CUTOFF="soon"` and no `base:`.
- AC13 — `base:` — with none in the record, the closing review's call exited 0 and wrote its row.
- AC14 — `round 4 · HOLD · reason ceiling` — printed with a second line carrying `--handoff dFix --code owner-decision`, and `grep -c 'derive_chain_verdict "' tools/unattended/unattended.sh` printed 1.
- AC15 — `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh` — printed 318 and 264, equal to the parent commit's.

Beyond section 6, seven staged breaks on scratch copies of the driver each went red at the criterion named: the gate call deleted, the sourced key at `read_spec_exit_rule`, the rule test deleted, a park row passing a HOLD, a read at `base:` and not the merge-base, the `spec-audit` fact unread, and the unrecorded-exit refusal cut. An eighth, `rv_foldpast` on the sourced key on a scratch leg, went red at AC10, AC11 and AC12. These stand in for no owed observation, because they ran on the probe and not on the arms.

Over this repository's own tracked records, the two reads gave section 5's pin: 99 records hold a review row, 62 hold one off the slug, all 62 read blank and none read unknown, in 20 s by the library's own functions. The no-process row test agreed with an awk reading of the same rows on all 99. This build's own record reads a blank cutoff, the rule `old`, and a silent gate, as the rollout states.

Owed at the close: the bar, and the six `New arm:` lines of section 7, each RED on its staged break and GREEN once restored. `FLOOR_ASSERTIONS` moved 3082 to 3193 and `FLOOR_SHARD_1` 565 to 676 in the driver suite, counted by the probe on both paths, and `FLOOR_ASSERTIONS` 1092 to 1106 and `FLOOR_SHARD_2` 118 to 132 in the leg suite, counted off the block's lines.
