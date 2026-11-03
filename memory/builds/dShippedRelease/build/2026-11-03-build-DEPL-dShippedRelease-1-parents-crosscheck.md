**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-4

# dShippedRelease's specs against the parent specs revised by merge `362790f10`: a read-only cross-check

Node d, 2026-11-03, base `66c5b8dbf` (origin/main). dShippedRelease's spec run began at `5d1c82ac0`,
the parent of its first spec commit `63ca805ed`. That base holds every earlier re-ground merge
(`191ba7ab5`, `2bd5e10d4`, `933e67399`, `57bc3b918`, `0c0f3a183`, `7d0f5b756`) and the fork picks
`ccd1292ea`; `git merge-base --is-ancestor` puts each inside it and `362790f10` outside it. Between
`5d1c82ac0` and `66c5b8dbf` one commit, `66f7b8d32` (merge `362790f10`, the owner's pick on
TOOL-dTotalRecall-2 §8 F6), moved any spec of the six parents: TOOL-dTotalRecall-2 to rev-7 and
TOOL-dWellOiledMachine-58, -41 and -6 to rev-5, rev-4 and rev-5. `git diff --name-only 5d1c82ac0
66c5b8dbf -- memory/builds/<parent>/spec/` names nothing else for dWitnessedBar, dBoundRoles,
dLinkedLibrary or dFurnishedOrders. The owner asked for this pass on 2026-11-03 although an earlier
triage said none was owed. This record is not an audit: no spec was edited by it, and its one
mismatch feeds the re-ground brief
[`2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground`](../prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground.md).

**Counts:** 20 assumptions · 18 AGREES · 1 MISMATCH · 1 UNKNOWN UNTIL BUILT, over 19 specs (the 6
citation specs, 20 rows; the 13 rule-wide candidates, 0 rows, every hit unbound). 1 spec holds a
MISMATCH: 4. By rule: 1 citation. It comes from the revision: wm58's added lines moved the `:288` that
sr4 §8 F5 cites.

## Method

- **Population by citation.** `grep -P` over `spec/*.md` for the four revised units, both
  `TOOL-<build>-<n>` and the bare `<build>-<n>`, plus continuation lists (`…-58 … and -6`) and
  `wm`/`tr` aliases: 6 specs. 1 (wm58), 4 (wm58, wm6), 5 (wm58), 12 (wm58), 30 (wm58) and 58 (wm6).
  None cites tr2 or wm41, and no spec cites any of the four by `:<line>`.
- **Population by rule.** The revision applies one rule, RH: a build lease's `session`, `lease`-mode
  class and `epoch` are read through the one read-only holder verb over `read_claims` that tr2 §8 F6
  (a) picked (tr2:340-357), never through `--claims`' five fields (pr1:204-208), and no unit builds a
  second read or files a second ask (wm6:348-351). A text probe for `--claims`, `read_claims`,
  `holder`, `epoch` and `refs/gov/leases` on a line naming a lease or claim named 13 candidates: 6,
  11, 15, 68, 69, 78, 94, 95, 123, 125, 129, 138 and 144. The other hits (3, 7, 8, 10, 13, 17, 21,
  25, 26, 63, 65, 66, 67, 100, 106, 119, 145) were judged by the main loop to name a spec's own §8 F6,
  a placeholder, a kit's version epoch, a lock's holder or a field name.
- **Readers.** Two `gov-spec-reviewer` agents, read-only, one per group of the brief
  [`2026-11-03-prompt-DEPL-dShippedRelease-1-parents-crosscheck`](../prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-crosscheck.md),
  their handoffs beside it. Their returns, every MISMATCH's both sides quoted with its `Change:` and
  `Cause:`, are
  [`2026-11-03-build-DEPL-dShippedRelease-1-crosscheck-returns`](2026-11-03-build-DEPL-dShippedRelease-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the returns' tables by script, stable-sorted by
  spec, derived the counts from it, and re-read row 10's both sides. It changed no verdict.
- **Aliases:** `srN:L` is line L of `spec/2026-1?-??-spec-DEPL-dShippedRelease-N.md`; `trN:L`,
  `wmN:L` and `prN:L` of dTotalRecall's, dWellOiledMachine's and dPlacedRequest's spec N; all at
  `66c5b8dbf`.
- **What it does not check:** the rules the earlier re-grounds applied (R1 to R9 of
  dWellOiledMachine's 2026-10-28 brief), since every one of them was in this build's base; anything
  a parent's build run decides; the specs neither population reached. The probe is a text heuristic.
  No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.

## The earlier triage, re-verified

It said the specs citing wm58 rely on sections other than F5. Half right: specs 1, 12 and 30 rely on
wm58 S2, S10 and S4 (a), none of which rev-5 touched. Specs 4 and 5 rely on wm58 S5's holder test,
which since rev-5 reads the holder through tr2 F6 (a)'s verb (wm58:78-89), but neither names a
surface for that read, so the revision changes nothing either states. What the triage missed is the
line drift: rev-5 added five lines above wm58's acceptance, and sr4 §8 F5 cites it by line.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | sr1 | A | `deploy_fixture.py` follows the door fixture's shape: a bare remote and two clones under `%TEMP%` with short names | cite | AGREES | sr1:94-96 · wm58:136-137 (S10, unrevised) |
| 2 | sr1 | A | `refs/gov/landing/` lies outside the door's coordination namespaces (leases, mail, requests, runs) | cite | AGREES | sr1:117-118 · wm58:57-60 (S2, unrevised) |
| 3 | sr4 | A | `run_unlease` moves wm58 S9's body (writer check, unit leases, mailbox, build lease) | cite | AGREES | sr4:83-85, :423 · wm58:125-135 |
| 4 | sr4 | A | S8's writer check reads the build lease as wm58 S7 does: class `mine` under `read_claims`' `lease` mode, in-kit, not through the holder verb | RH | AGREES | sr4:84-85, :295 · wm58:99-101, :126-127 (S7 and S9, untouched by rev-5) |
| 5 | sr4 | A | wm58 S5 needs a live build lease, held by the writer, to prune the mailbox, so the mailbox closes before the tombstone | cite | AGREES | sr4:90-91, :405-407 · wm58:85-89 ("holds that build's lease as its holder, read as S4 (c) reads it"), S4 (c) now via the verb at wm58:78-82 |
| 6 | sr4 | A | The door admits `deploy.unlease`'s tombstone and prunes once the name is in `DOOR_CLOSING_VERBS`; sr4 names no surface for the door's holder read | cite | AGREES | sr4:93-95, :294 · wm58:78-82 · tr2:348-353 lists wm58 S4 (c) and S5 among the verb's users |
| 7 | sr4 | A | wm58 S6 hands this build the addition of `deploy.unlease` to `DOOR_CLOSING_VERBS` | cite | AGREES | sr4:94-95 · wm58:94-98 |
| 8 | sr4 | A | F2: wm58 S5 needs each copy under the build folder | cite | AGREES | sr4:381-382 · wm58:86-88 |
| 9 | sr4 | A | F5: wm58 S9 exits early on a `landed` tombstone with a message that goes stale here | cite | AGREES | sr4:397-398 · wm58:127-128 |
| 10 | sr4 | A | F5: wm58's acceptance at `:288` asserts `not-closing-verb` for `deploy.unlease` | cite | MISMATCH | sr4:398-399 · wm58:288 is now AC3's `not-holder` line; the assertion moved to wm58:292-293 |
| 11 | sr4 | A | F5's ask stands: wm58 still asserts `not-closing-verb` for `deploy.unlease` and still writes `withdrawn` in S9 | cite | AGREES | sr4:401-404 · wm58:129, :292-294 |
| 12 | sr4 | A | S11 `check_unleased` and AC9 read lease status (terminal, `live`) through `--claims` | RH | AGREES | sr4:107-108, :346-347 · pr1:204-208; status is field 3 and verdict field 5 (`unattended.sh:2373`) |
| 13 | sr4 | A | Adapter rows at `point.command-adapters`, `class = "idempotent"`, `run` the verb, so the supervisor runs them through wm6 S8 | cite | AGREES | sr4:132-137, :360-362 · wm6:113-122 (S8, unrevised) |
| 14 | sr5 | A | F4: a post that recreates a mail ref after `run_unlease` is one the door lets no agent prune | cite | AGREES | sr5:303-305 · wm58:85-91; S5 requires the lease held live (via S4 (c)), else only the owner's guarded command |
| 15 | sr5 | A | AC9: a second clone that took the lease over can run the closing items; `--claims` reads `live` until then | cite / RH | AGREES | sr5:267-270 · wm58:89 (the take-over session counts as holder) · pr1:204-208 (status is in the five fields) |
| 16 | sr12 | A | `refs/gov/landing-queue/` is outside the door, as `refs/gov/waits/` is | cite | AGREES | sr12:195-196 · wm58:57-60 |
| 17 | sr12 | A | S2 skips an entry whose build lease reads neither `live` nor `held` in `--claims` | RH | AGREES | sr12:43 · pr1:204-208 · `unattended.sh:2373` (status and verdict only, no session) |
| 18 | sr30 | A | The door admits S2's `landed` write through S4 (a), because the tip, the draw's own hold, names the writer | cite | AGREES | sr30:206-207 · wm58:76-77 (S4 (a), not touched by rev-5) |
| 19 | sr58 | A | wm6 S8 runs a command item only through its adapter row | cite | AGREES | sr58:20-22 · wm6:118-119 |
| 20 | sr58 | A | AC3: `supervise.py --check-adapters` prints a count of rows | cite | UNKNOWN UNTIL BUILT | sr58:104-105 · wm6:116-118, :296-298 give its refusals and exit codes but no printed count |

## The mismatch, both sides quoted

Row 10 is quoted in section 2 of Group A's return. sr4:397-399 says wm58's "acceptance at `:288`
asserts `not-closing-verb` for this name"; at `66c5b8dbf` wm58:288 is AC3's `not-holder` line, and the
`not-closing-verb` assertion for `deploy.unlease` is AC4 at wm58:290-295 (`git show
5d1c82ac0:<wm58>` puts it at :288). The ask F5 states still stands; only the citation is stale.

## UNKNOWN UNTIL BUILT

- Row 20: whether `supervise.py --check-adapters` prints a row count (sr58 AC3) is wm6's build run's;
  wm6 S8 and AC7 state its refusals and exit codes only.

## Rule-wide hits RH does not bind

Group B found no RH-bound assumption in its 13 specs; its section 4 gives one line per hit. In short:
sr6 and sr78's dead holder are an engine's compare-and-swap and a `landing-turn` wait; sr11's
`holder-only` is a wm18 wait outcome; sr15 and sr78 S59 take and hold their own release lease; sr68,
sr94, sr12 and sr4 read status, which is a `--claims` field; sr69 only writes; sr95, sr123, sr125,
sr129, sr138 and sr144 read dShippedRelease's own hand-over epoch and cite no revised unit.

## Parked for the owner

- **One fact, two surfaces: the build lease's epoch.** dPlacedRequest unit 34 S22 already specs a
  read-only `unattended.sh --lease status <kind> <name> [<sub>]` printing `<tail> <fleet tag>
  <session> <status> <verdict> <epoch>` (pr34:106-109, AC22 at :468-470), unchanged since
  `5d1c82ac0`. tr2 F6 says no read-only dPlacedRequest verb prints a lease's `session` (tr2:341-342),
  citing unit 1 only, and its owner-picked (a) asks dPlacedRequest for one, printing `fleet-tag`,
  `session`, `lease`-mode class and `epoch` (tr2:348-356). dShippedRelease's `read_lease_epoch`
  reads the build lease's epoch from `--lease status` (sr138 S48, sr144 S34), while wm6 S6 and S7 will
  read the same epoch through the F6 (a) verb. Both readers, once built, read one fact through two
  surfaces; sr94 and sr125 S17 read "a held lease of this session" through a third, `--lease fence`
  (pr15). RH does not bind dShippedRelease, which relies on no revised unit for these reads, so no
  dShippedRelease spec was edited. The choice is the owner's or dTotalRecall's build run's: (a) name
  `--lease status` as tr2 F6 (a)'s verb and narrow the ask to the one column it lacks, the
  `lease`-mode class, which `placement.py check` already derives from it; or (b) keep the ask as
  picked and re-point sr138 and sr144 to the new verb when it lands. Recommendation: (a), one fact in
  one place, with no new verb.
- **Parent text that looks wrong (not edited):** wm6's rev-5 re-points its F6 citation to
  `tr2:337-354`, while F6 runs from tr2:340 to tr2:357 (tr2:336-339 is F5).

## Follow-ups outside this pass

- sr78 S59 "re-reads the lease epoch" of its own release lease and names no surface for the read: a
  dShippedRelease design gap, not a parent mismatch.

## For the re-ground

One spec, by one row: sr4, row 10 (re-point §8 F5's `:288` to wm58 AC4). Brief:
[`2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground`](../prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground.md).

## After the re-ground

The writer's return is
[`2026-11-03-build-DEPL-dShippedRelease-1-reground-returns`](2026-11-03-build-DEPL-dShippedRelease-1-reground-returns.md).
It refused no row and re-read both sides. sr4 moved to rev-5: §8 F5 now cites wm58's
`not-closing-verb` assertion as "its acceptance's AC4"; F5 stays `RESOLVED`, its ask untouched. Every
other `:<line>` cite in sr4 names `unattended.sh`, `lib-unattended.sh`, `layer-memory.md` or
`flow-steps.md`, none of them a revised spec, so it found nothing more. The spec stays `DEFERRED`,
at 39593 bytes, and carries one spec-revised record,
[`2026-11-03-build-DEPL-dShippedRelease-4-deviation-43`](2026-11-03-build-DEPL-dShippedRelease-4-deviation-43.md).
No fork was opened or resolved. The one owner question stays the one under "Parked for the owner".
