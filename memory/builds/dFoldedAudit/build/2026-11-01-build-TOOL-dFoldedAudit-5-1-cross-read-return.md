# dFoldedAudit — the M2 cross-read's return

**Serves:** journal TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8

All five items are done: seven specs are folded to rev-2, and TOOL-dFoldedAudit-8 had nothing to fold. With the folds committed in a scratch clone, `unattended.sh --plan dFoldedAudit` reads READY for all eight. The pre-fold commit read FORKED on TOOL-dFoldedAudit-5, so the READY comes from the F1 mark. Nothing is committed and no index was regenerated.

**Gates:** hygiene checks 5, 12 and 25 exited 0 in that clone, with no finding naming this build. I ran no gate leg, and the clone is deleted.

## Folds by spec and rev

| Spec | Rev | What moved |
|---|---|---|
| TOOL-dFoldedAudit-5 | rev-2 | F1 marked `RESOLVED (agent, 2026-11-01, delegated)` to option (b), with `ratified 2026-11-01` in the header (item 1). `siblingEdits` now reads as `[]` under `promote-all`, because unit 4 returns the list under `by-nature` only. The review double's `addresses` now reaches unit 4's arms too, since row 17 reads them. |
| TOOL-dFoldedAudit-1 | rev-2 | The `.unattended.conf` writes now belong to unit 7 (item 2). The `planState` sentence is literal, reads `--plan <slug> --paths`, and AC12 greps it (item 3). See the unit 1 detail below. |
| TOOL-dFoldedAudit-2 | rev-2 | The driver header line `:22` gains both flags, with new AC14, because check 26 joins flags to the header and no spec owned that line. §5 now keys the same-day risk on the day a record began, not on a row's date. |
| TOOL-dFoldedAudit-3 | rev-2 | The return sentence names the `**Specs:**` line, which unit 5 says the disposal reads and refuses at row 17 if it differs. The marker is now called an engine marker: no entry mints `unattended-build@1.12`, so the hand move stands alongside "no kit version by hand". |
| TOOL-dFoldedAudit-4 | rev-2 | The hand-off bullet carries backticked `planState`. The hands-off join reads backticks only, so it had read nothing there. |
| TOOL-dFoldedAudit-6 | rev-2 | §4 said the prompt names the `lastReport` path. It names `<report stem>`, as units 3 and 4 write. |
| TOOL-dFoldedAudit-7 | rev-2 | The close's check is now a read of every ref, with today's measure (item 5). The key table no longer names unit 3 as a reader, since its §3 reads no key. |
| TOOL-dFoldedAudit-8 | rev-1 | No disagreement. I checked its revs, its quoted owner sentences and its M4 pointers. |

Unit 1 took three further folds in rev-2:
- **M4 text:** the first chain step now agrees with unit 5 §4 and F1. The repair clause and the role sentence now also name the review record, which units 4 and 6 need.
- **`help/`:** unit 1 and unit 7 each gave the policy prose to the other. No page moves, and §3 now says so.
- **Check 26:** the spec's description of it was wrong. It joins flags to the header and suite, and it needs every verb in `tools/unattended/SKILL.template.md`, a carrier no spec owned. That file, its render and its size row now belong to unit 1, with AC7, AC8 and the `unattended skill size` leg extended.

The M4 render goes from 30504 to 30565 bytes, leaving 155 of 30720, which still covers DL-20's roughly 60. My replication reproduced the writer's 30504 exactly, and all twelve AC literals I checked still hold, with `precision` at 0.

## Cross-read axes

- **Scope:** three disagreements, all fixed: the `.unattended.conf` owner, the `help/` ownership, and the Skill carrier no unit owned.
- **Interface:** nine disagreements, all fixed. The replayed hands-off join has no missing token, every §7 leg resolves against `tools/gate-legs.json`, and the `dispositions`, `siblingEdits`, row, flag, switch and verdict shapes all agree.
- **Ordering:** no unit depends on a later one, and every edge is reciprocal.
- **Acceptance:** lines 1 to 8 of the brief are implied by the union of the specs. I also walked AC6 to AC10, AC14 and AC15 by hand through unit 5's five steps under F1 (b); each prints what it claims.

**Line cites left alone:**
- "Fixture R" names different fixtures in units 2 and 5, but each is local to its spec.
- `tools/memory-tree/README.md:545` and `:550` are both true cites of one section.
- `tools/memory-tree/deviation_join.py:705-733` and `:715-733` make different claims.

## Item 5: agrees, with a condition

The design's landing-date value meets the idiom at `tools/unattended/unattended.sh:1009-1012` only if every old-contract record began before that date. Unit 7's check said "no run preflighted that day", which named no ref. The records that matter sit on run branches, so a read of `main` would miss them.

Measured today, `dTendedCadence` and `dScopedBuild` both began 2026-11-01 and hold old-shape spec exit rows on their run branches. A value of `2026-11-01` would red them; any later value would not. The rewritten check catches this.

## Choices for you, reported and not decided

1. **A hit at the close:** the design fixes the value at the landing date and the idiom wants it strictly past the newest record. They cannot both hold if the read finds a hit. Unit 7 parks the close on a hit and leaves the remedy open: land later, or set the day after the hit.
2. **Attended runs and the cutoff:** unit 1 has `/build` pass `disposal` with no preflight, so a blank `SPEC_FOLD_CUTOFF` keeps an adopter's unattended runs on the old rule but not its attended ones.
3. **The Skill size raise:** the render is 10237 of a 10240-byte row and needs two lines. I took the limits file's raise route, the same one the protocol row uses. That row's comment warns against prose coming back, so check you accept the raise.

**Design record:** step 1 of [chain] in `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md` still reads as it did before F1. It is outside `spec/`, so I left it.

## Files

The seven folded specs are in `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\`:
- `2026-11-01-spec-TOOL-dFoldedAudit-1.md`
- `2026-11-01-spec-TOOL-dFoldedAudit-2.md`
- `2026-11-01-spec-TOOL-dFoldedAudit-3.md`
- `2026-11-01-spec-TOOL-dFoldedAudit-4.md`
- `2026-11-01-spec-TOOL-dFoldedAudit-5.md`
- `2026-11-01-spec-TOOL-dFoldedAudit-6.md`
- `2026-11-01-spec-TOOL-dFoldedAudit-7.md`
