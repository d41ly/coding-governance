**Serves:** research TOOL-dScopedBuild-1 TOOL-dScopedBuild-7

# dScopedBuild's specs against the parent specs revised by merge `362790f10`: a read-only cross-check

Node d, 2026-11-03, base `66c5b8dbf` (origin/main). dScopedBuild's spec run began at `5f0b11f12`,
the parent of its first spec commit `807775940`. That base holds every earlier re-ground merge
(`191ba7ab5`, `2bd5e10d4`, `933e67399`, `57bc3b918`, `0c0f3a183`, `7d0f5b756`) and the fork picks
`ccd1292ea`; `git merge-base --is-ancestor` puts each inside it and `362790f10` outside it. Between
`5f0b11f12` and `66c5b8dbf` one commit, `66f7b8d32` (merge `362790f10`), moved any spec of the four
parents: TOOL-dWellOiledMachine-6, -41 and -58, which read TOOL-dTotalRecall-2 rev-7's owner-picked
holder verb. `git diff --name-only 5f0b11f12 66c5b8dbf -- memory/builds/<parent>/spec/` names nothing
for dIndexedDesign, dWitnessedBar or dFurnishedOrders; dIndexedDesign has no re-ground merge and its
specs are byte-identical across the range. The owner asked for this pass on 2026-11-03 although an
earlier triage said none was owed. This record is not an audit: no spec was edited by it, and its one
mismatch feeds the re-ground brief
[`2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground.md).

**Counts:** 10 assumptions · 8 AGREES · 1 MISMATCH · 1 UNKNOWN UNTIL BUILT, over 2 specs (the 2
citation specs; the rule probe named no further candidate). 1 spec holds a MISMATCH: 1. By rule: 1
citation. It is pre-existing: wm6 named no transition record at `5f0b11f12` either. No mismatch comes
from the revision.

## Method

- **Population by citation.** `grep -P` over `spec/*.md` for the four revised units, both
  `TOOL-<build>-<n>` and the bare `<build>-<n>`, plus continuation lists and `wm`/`tr` aliases: 2
  specs, 1 and 7, both citing wm6 (S1 and S8). None cites wm41, wm58 or tr2, and none cites by
  `:<line>`.
- **Population by rule.** The revision applies one rule, RH: a build lease's `session`, `lease`-mode
  class and `epoch` are read through the one read-only holder verb over `read_claims` that tr2 §8 F6
  (a) picked, never through `--claims`' five fields, and no unit builds a second read or files a
  second ask (wm6:348-351). The probe the brief reports named no candidate. **That claim was wrong in
  part:** the reader found that `lease` alone hits sb3, sb5, sb12, sb34, sb35, sb38, sb40 and sb41,
  all of them the unit write-set lease (`item.build.unit-lease`, `routed_commits.py --unit-lease`),
  and checked each; none reads a build lease's session, class or epoch.
- **Reader.** One `gov-spec-reviewer` agent, read-only, by the brief
  [`2026-11-03-prompt-TOOL-dScopedBuild-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-crosscheck.md),
  its handoff beside it. Its return, the MISMATCH's both sides quoted with its `Change:` and `Cause:`,
  is
  [`2026-11-03-build-TOOL-dScopedBuild-1-crosscheck-returns`](2026-11-03-build-TOOL-dScopedBuild-1-crosscheck-returns.md).
  Its prose says 8 assumptions; its table has 10 rows, and the table wins.
- **The main loop** assembled the table below from the return's table by script, derived the counts
  from it, and re-read row 1's both sides (`grep -ci transition` on wm6 prints 0; dl3:60 names
  `write_transition`). It changed no verdict.
- **Aliases:** `sbN:L` is line L of `spec/2026-11-01-spec-TOOL-dScopedBuild-N.md`; `wmN:L`, `trN:L`
  and `dlN:L` of dWellOiledMachine's, dTotalRecall's and dDeclaredLoop's spec N; all at `66c5b8dbf`.
- **What it does not check:** the rules the earlier re-grounds applied, all in this build's base;
  anything a parent's build run decides; the 32 specs the citation population did not reach beyond
  the rule probe. No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | sb1 | A | wm6, "the executor", owns the file-backed transition record for `build.exit` | cite | MISMATCH | sb1:108 against wm6, which has no transition record (`grep -c -i transition` prints 0 at `5f0b11f12` and at `66c5b8dbf`). Its only item witness is a reconcile row's landed effect (wm6:118-119). The writer is TOOL-dDeclaredLoop-3 S5 `write_transition` (dl3:60), called through `loop_transition.py record` as wm3:60 and wm46:84 do |
| 2 | sb1 | A | No read of a lease's session, `lease`-mode class or epoch | RH | AGREES | sb1 contains no lease, epoch, `--claims`, `read_claims`, holder or `refs/gov` term. Its one "mine" (sb1:162) is attribution's "not mine", not a lease class |
| 3 | sb7 | A | wm6 S1 and S8 own the executor, its beat and its adapter contract | cite | AGREES | sb7:91 against wm6:45-54 (S1, the supervisor and its beat) and wm6:113-122 (S8, the adapter contract). Neither section moved in `66f7b8d32` |
| 4 | sb7 | A | wm6 S8 supplies `point.command-adapters` | cite | AGREES | sb7:102 against wm6:6 (`**Carries:** node:point.command-adapters`) and wm6:113 |
| 5 | sb7 | A | S6's row (`point`, `name`, `class = "idempotent"`, `run`) fits the S8 contract | cite | AGREES | sb7:73-76 against wm6:114-116 ("declares `run`, an argv, and `class`, `idempotent` or `reconcile`", with `probe` only for `reconcile`). The `point =` and `name =` keys follow wm20's `[[adapter]]` shape (wm20:148-150) |
| 6 | sb7 | A | The supervisor runs Build's `build.core` item, an `executor`-actor item (flow-steps:298), through that row | cite | AGREES | sb7:75-76 against wm6:52 and :118 ("runs a command item only through its row"). wm25:93 routes `executor` like `command`, "a command item run through its adapter row (its S8)" |
| 7 | sb7 | A | The supervisor matches the item to S6's row by `name = "build.core"`, and runs `run` as `--build-core <slug>` with the build's slug | cite | UNKNOWN UNTIL BUILT | sb7:54, :74-75 against wm6:113-122. S8 states neither how a command item finds "its row" nor whether a `run` argv takes a per-build argument. The three rows wm6 registers (lander, record door, bar) take no slug |
| 8 | sb7 | A | `python supervise.py --check-adapters` passes S6's row and refuses it once `class` is removed (AC7) | cite | AGREES | sb7:241-244 against wm6:116-118 (`check_command_adapter_row` refuses a row with no `class`, and `--check-adapters` runs it over every row) and wm6:296-299 (AC7) |
| 9 | sb7 | A | wm6's `points.toml` is a build-run precondition for S6's row | cite | AGREES | sb7:174-176 against wm6:229 (`tools/runtime/points.toml`: the `point.command-adapters` row). The file itself comes from wm20 (wm6:169), which wm6 already consumes |
| 10 | sb7 | A | No read of a lease's session, `lease`-mode class or epoch | RH | AGREES | sb7 contains none of those terms. Its beat and fence are wm6's (sb7:91), and it reads no lease itself |

## The mismatch, both sides quoted

Row 1 is quoted in section 2 of the return. sb1:108's non-goal names "A file-backed transition record
for `build.exit`: the executor's (TOOL-dWellOiledMachine-6)". wm6 names no transition record; the
writer is TOOL-dDeclaredLoop-3 S5's `write_transition` (dl3:60), which dWellOiledMachine's units reach
through `python loop_transition.py record` (wm3:60). Pre-existing, not caused by the revision.

## UNKNOWN UNTIL BUILT

- Row 7: how `supervise.py` matches a command item to its `[[point]]` row, and whether a row's `run`
  argv takes the build's slug (sb7 S6, `--build-core <slug>`), is wm6's build run's; wm6 S8 states
  neither, and the three rows wm6 registers take no slug.

## Parked for the owner

- **Parent text that looks wrong (not edited):** wm6:179's external edge still reads "the epoch read
  §8 F4 asks for" and does not name tr2 F6 (a)'s holder verb, which S6 and S7 now name; and wm6's
  rev-5 cites F6 as `tr2:337-354`, while F6 runs from tr2:340 to tr2:357.

## For the re-ground

One spec, by one row: sb1, row 1 (re-point the non-goal's owner to TOOL-dDeclaredLoop-3's
`write_transition`). Brief:
[`2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground.md).

## After the re-ground

The writer's return is
[`2026-11-03-build-TOOL-dScopedBuild-1-reground-returns`](2026-11-03-build-TOOL-dScopedBuild-1-reground-returns.md).
It refused no row and re-read both sides (wm6 has no transition record; dl3:60 and wm3:60 name the
writer and its verb). sb1 moved to rev-4: the §3 non-goal names TOOL-dDeclaredLoop-3 S5's
`write_transition`, reached through `loop_transition.py record` by the `build.exit` command item, and
stays a non-goal. §3's Edges never named wm6 for the record, so they did not move. The spec stays
`DEFERRED`, at 28037 bytes, and carries one spec-revised record,
[`2026-11-03-build-TOOL-dScopedBuild-1-deviation-13`](2026-11-03-build-TOOL-dScopedBuild-1-deviation-13.md).
No fork was opened or resolved.

## Owner ruling, 2026-11-03

The owner answered this pass's report with "fix, take recommendations on the forks, land it".

- **wm6:179's edge and wm6's F6 citation:** fixed in TOOL-dWellOiledMachine-6 rev-6: the edge names
  TOOL-dPlacedRequest-34 S22's `--lease status`, and F4 cites TOOL-dTotalRecall-2 §8 F6 by name.
  Record:
  [`deviation-65`](../../dWellOiledMachine/build/2026-11-03-build-TOOL-dWellOiledMachine-6-deviation-65.md).
