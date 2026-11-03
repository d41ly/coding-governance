**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-4 DEPL-dShippedRelease-95

# dShippedRelease — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck`](2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-DEPL-dShippedRelease-1-parents-crosscheck`](../prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation, led by spec 1 (specs 1, 4, 5, 12, 30 and 58)

I found one MISMATCH in Group A (specs 1, 4, 5, 12, 30, 58), and the revision caused it: sr4 cites wm58 by a line number that moved. I found one UNKNOWN UNTIL BUILT, and it predates the revision. RH finds no MISMATCH in this group. No Group A spec reads a lease's session, `lease`-mode class or epoch through `--claims`, parses a lease commit, files a second ask or reads tr2 F6, wm58 F5 or wm6 F4 as open.

The earlier triage was half right. Specs 1, 12 and 30 depend on no part of wm58 that F5 touched. Specs 4 and 5 do depend on S5's holder test, which since rev-5 is read through tr2 F6 (a)'s verb, but neither names a surface for that read. So the revision changes nothing either spec states.

The probes behind the evidence:
- `git diff --stat 5d1c82ac0 66c5b8dbf` over the six parents' spec folders names only tr2, wm41, wm58 and wm6.
- `git show 66f7b8d32` changed only wm58 S4, F5 and §9 (plus 5 new header lines). In wm6 it changed only S6, S7, F4 and §9. wm58 S5 is unchanged context.
- `git show 5d1c82ac0:<wm58>` line 288 reads "`--verb deploy.unlease` exits 2 printing `not-closing-verb`". At HEAD that text is at wm58:293, and wm58:288 is AC3's `not-holder` line.
- `print_claims` at `tools/unattended/unattended.sh:2397` runs `cut -f1-5` over rows ordered slug, node, status, age, verdict, sha, session (`:2373`). So `--claims` gives status and verdict but no session or epoch.

## 1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | `deploy_fixture.py` follows the door fixture's shape: a bare remote and two clones under `%TEMP%` with short names | cite | AGREES | sr1:94-96 · wm58:136-137 (S10, unrevised) |
| 1 | `refs/gov/landing/` lies outside the door's coordination namespaces (leases, mail, requests, runs) | cite | AGREES | sr1:117-118 · wm58:57-60 (S2, unrevised) |
| 4 | `run_unlease` moves wm58 S9's body (writer check, unit leases, mailbox, build lease) | cite | AGREES | sr4:83-85, :423 · wm58:125-135 |
| 4 | S8's writer check reads the build lease as wm58 S7 does: class `mine` under `read_claims`' `lease` mode, in-kit, not through the holder verb | RH | AGREES | sr4:84-85, :295 · wm58:99-101, :126-127 (S7 and S9, untouched by rev-5) |
| 4 | wm58 S5 needs a live build lease, held by the writer, to prune the mailbox, so the mailbox closes before the tombstone | cite | AGREES | sr4:90-91, :405-407 · wm58:85-89 ("holds that build's lease as its holder, read as S4 (c) reads it"), S4 (c) now via the verb at wm58:78-82 |
| 4 | The door admits `deploy.unlease`'s tombstone and prunes once the name is in `DOOR_CLOSING_VERBS`; sr4 names no surface for the door's holder read | cite | AGREES | sr4:93-95, :294 · wm58:78-82 · tr2:348-353 lists wm58 S4 (c) and S5 among the verb's users |
| 4 | wm58 S6 hands this build the addition of `deploy.unlease` to `DOOR_CLOSING_VERBS` | cite | AGREES | sr4:94-95 · wm58:94-98 |
| 4 | F2: wm58 S5 needs each copy under the build folder | cite | AGREES | sr4:381-382 · wm58:86-88 |
| 4 | F5: wm58 S9 exits early on a `landed` tombstone with a message that goes stale here | cite | AGREES | sr4:397-398 · wm58:127-128 |
| 4 | F5: wm58's acceptance at `:288` asserts `not-closing-verb` for `deploy.unlease` | cite | MISMATCH | sr4:398-399 · wm58:288 is now AC3's `not-holder` line; the assertion moved to wm58:292-293 |
| 4 | F5's ask stands: wm58 still asserts `not-closing-verb` for `deploy.unlease` and still writes `withdrawn` in S9 | cite | AGREES | sr4:401-404 · wm58:129, :292-294 |
| 4 | S11 `check_unleased` and AC9 read lease status (terminal, `live`) through `--claims` | RH | AGREES | sr4:107-108, :346-347 · pr1:204-208; status is field 3 and verdict field 5 (`unattended.sh:2373`) |
| 4 | Adapter rows at `point.command-adapters`, `class = "idempotent"`, `run` the verb, so the supervisor runs them through wm6 S8 | cite | AGREES | sr4:132-137, :360-362 · wm6:113-122 (S8, unrevised) |
| 5 | F4: a post that recreates a mail ref after `run_unlease` is one the door lets no agent prune | cite | AGREES | sr5:303-305 · wm58:85-91; S5 requires the lease held live (via S4 (c)), else only the owner's guarded command |
| 5 | AC9: a second clone that took the lease over can run the closing items; `--claims` reads `live` until then | cite / RH | AGREES | sr5:267-270 · wm58:89 (the take-over session counts as holder) · pr1:204-208 (status is in the five fields) |
| 12 | `refs/gov/landing-queue/` is outside the door, as `refs/gov/waits/` is | cite | AGREES | sr12:195-196 · wm58:57-60 |
| 12 | S2 skips an entry whose build lease reads neither `live` nor `held` in `--claims` | RH | AGREES | sr12:43 · pr1:204-208 · `unattended.sh:2373` (status and verdict only, no session) |
| 30 | The door admits S2's `landed` write through S4 (a), because the tip, the draw's own hold, names the writer | cite | AGREES | sr30:206-207 · wm58:76-77 (S4 (a), not touched by rev-5) |
| 58 | wm6 S8 runs a command item only through its adapter row | cite | AGREES | sr58:20-22 · wm6:118-119 |
| 58 | AC3: `supervise.py --check-adapters` prints a count of rows | cite | UNKNOWN UNTIL BUILT | sr58:104-105 · wm6:116-118, :296-298 give its refusals and exit codes but no printed count |

## 2. MISMATCH

- **sr4 §8 F5, the line citation.**
  - sr4:397-399: "TOOL-dWellOiledMachine-58 S9 writes `withdrawn`, exits early on a `landed` tombstone with a message that goes stale here, and its acceptance at `:288` asserts `not-closing-verb` for this name".
  - wm58:288 today: "it exits 2 printing `not-holder` and every `refs/gov/mail/fx/` ref is still on the remote." The cited text now sits at wm58:292-293: "`--case closing-build --verb deploy.unlease` exits 2 printing `not-closing-verb`" (AC4, wm58:290-295).
  - Change: re-point `:288` to `:292-293`. A section citation ("wm58 AC4") would survive the next renumbering. The ask's substance stands.
  - Cause: the revision. At `5d1c82ac0`, wm58:288 was this line; `66f7b8d32` added 3 record rows and 2 lines to S4, moving it 5 lines down.

## 3. UNKNOWN UNTIL BUILT

- **sr58 AC3's printed count:** wm6's build run decides whether `--check-adapters` prints a row count. If it doesn't, sr58 has to take the count itself (for example by counting rows in `points.toml`).

## 4. Hits RH does not bind, and pr34 against tr2

- **sr1:355:** `read_claims`' bounded fetch into `CLAIM_CACHE` is only a model for the landing record's read path. It reads no lease's holder, class or epoch.
- **sr30 S2, "reads the root's lease class" (sr30:47, :141-149):** the routes are status only (tombstone, `held` hold, live, absent). The drawer never holds the root's lease (sr30:109), so "live, under another holder" needs no session read. Neither the read nor the S2 epoch bump (sr30:49, :157, AC9) goes through a revised unit.
- **sr5:52, "holder-only":** a `WAIT_OUTCOMES` name from wm18, not a lease read.
- **sr12:219, :225, :235, "stale holder":** the landing turn's fence (pr15), not a holder read.
- **sr4 S8 and wm58 S7/S9:** RH says the `lease`-mode class is read through the holder verb. wm58 S7 and S9 still read `mine` through `read_claims` inside the unattended kit itself, and rev-5 left that alone. The verb serves readers outside the kit, so this is not a conflict.
- **pr34 S22 against tr2 F6:** pr34:106-108 already specs a read-only `unattended.sh --lease status` printing `<tail> <fleet tag> <session> <status> <verdict> <epoch>`. tr2:341-342 says "no read-only verb of that unit prints a lease's `session`" and asks dPlacedRequest for one (tr2:353-356). Neither spec names the other. tr2's ask duplicates a verb pr34 already specs, which may be a second surface for the same fact.
- **Group A and that surface:** no Group A spec reads `--lease status`, `read_lease_epoch` or the holder verb (probe: 0 hits in each of the six), so no Group A spec reads a lease's holder or epoch through a surface different from its revised parent's.

## 5. Revised parent sections each spec cites but no assumption depends on

- **sr1:** cites wm58 S2 and S10 only, neither revised; none.
- **sr4:** depends on wm58 S5 and, through it, S4 (c). It cites wm6 S8 only, so wm6 S6, S7 and F4 are not cited; none.
- **sr5:** depends on wm58 S5; none.
- **sr12:** cites "wm58's door" but depends only on S2's namespace list; S4 (c), S5 and F5 are not depended on.
- **sr30:** cites wm58 S4 but depends only on clause (a); the revised clause (c) is not depended on.
- **sr58:** cites wm6 S8 only; wm6 S6, S7 and F4 are not cited; none.

Files:
- `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-10-30-spec-DEPL-dShippedRelease-4.md`
- `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-10-30-spec-DEPL-dShippedRelease-58.md`
- `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-58.md`
- `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-6.md`
- `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-2.md`
- `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-34.md`

## Group B, rule-wide, led by spec 95 (13 specs)

Group B, led by DEPL-dShippedRelease-95, has no RH-bound assumption: none of the 13 specs relies on a revised parent unit for a holder or epoch read. So the table has no rows, there is no MISMATCH or UNKNOWN UNTIL BUILT, and every probe hit is a line under 4.

Probes, all read-only:
- `grep -nE 'dWellOiledMachine-(6|41|58)\b|dTotalRecall-2\b'` over the whole spec folder found only specs 1, 4, 5, 12, 30 and 58, all in Group A. Over the 13 Group B specs it found nothing.
- The F4, F5 and F6 hits in specs 6, 11, 15, 125, 138 and 144 are all those specs' own §8 forks, for example sr15:444 "Who owns the kit", sr138:122 "The `deploy items` guard" and sr144:277 "Where does the token walk run".
- `git diff --name-only 5d1c82ac0 66c5b8dbf -- memory/builds/dPlacedRequest/spec` printed nothing, so pr1, pr15, pr16, pr26 and pr34 read the same at the base and today.
- `grep -rn -- '--lease status\|dPlacedRequest-34'` over the dTotalRecall and dWellOiledMachine specs printed nothing.

1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|

No rows: no Group B spec relies on tr2, wm6, wm41 or wm58 for a lease's `session`, `lease`-mode class or `epoch`. Each hit is placed under 4.

2. MISMATCH: none.

3. UNKNOWN UNTIL BUILT: none.

4. Rule-wide hits RH does not bind, and pr34 S22 against tr2 F6
- **sr6:134, :214-215.** "A stale holder's rollback" is the holder of an engine compare-and-swap on a deployment id. It reads no lease.
- **sr11:44-47.** `holder-only` is a `WAIT_OUTCOMES` flag of TOOL-dWellOiledMachine-18, which was not revised. It reads no lease field.
- **sr15:79-85, :94-95, :286-287.** This is the release-cadence lease `run/release/<E>`, which the spec takes and holds itself through `--lease acquire` and `take-over` (pr1 S5). It records the epoch from its own acquire output into `.pick`, and it learns "foreign" from the acquire's refusal. It never reads another holder's record.
- **sr78:175 (S59).** "Exit 3 re-reads the lease epoch: still the holder" is about unit 15's release lease, a lease the spec holds itself. It relies on no revised unit. It names no surface for the re-read, which is a design gap of its own and out of scope.
- **sr78:85, :360.** The "dead holder" is a `landing-turn` wait swept by `waits.py`, not a lease read.
- **sr68:30 and sr94:20, :29, :63.** They read the build lease as terminal through `--claims`. Status is one of the five `--claims` fields (pr1 "The rows"), and wm6:107-108 reads status the same way. RH covers only `session`, `lease`-mode class and `epoch`.
- **sr94:29-30, :68 and sr125:45 (S17).** They read "a held lease of this session" through `--lease fence` (TOOL-dPlacedRequest-15). That is a holder read through a different surface from the tr2 holder verb that wm58:79 and wm41:47 use. But neither spec relies on a revised unit for it, and its edges are dShippedRelease-internal or dPlacedRequest only. So RH does not bind it.
- **sr69:31.** It only writes (`--lease release build <slug>` with no `--as`), and the write is governed by pr16. No holder or epoch read.
- **sr95:30-31 (S2), :57, :85, :121.** `read_lease_epoch` fetches the ref and parses the tip record's `epoch` itself, a pattern RH names. It cites no revised unit and was later superseded inside dShippedRelease (sr125:54 S26, then sr138:77 S48, then sr144:63 S34). So RH does not bind.
- **sr123:31, :35-37, :49.** S2 writes `record-epoch` through `read_lease_epoch`. S4's `--lease released` walks the lease chain (pr26 S1). Both are dShippedRelease's own reads of a lease it hands over. No revised unit is relied on.
- **sr125:54 (S26), :64 (S36).** The proposed `--lease epoch` act over `read_claims` was withdrawn by sr138:77 and sr144:63. `--lease released --from` reads dShippedRelease's own hand-over chain. Neither relies on a revised unit.
- **sr129:26-34, :64, :81.** Fixture plants that reach `read_lease_epoch` and unit 123 S4. Internal only.
- **sr138:33 (S4), :77 (S48) and sr144:63 (S34), :238.** `read_lease_epoch` reads the build lease's epoch as field 6 of pr34 S22's `--lease status build <slug>`. wm6:100 (S6) and wm6:108 (S7) read the same fact, the build lease's epoch, through "the holder verb TOOL-dTotalRecall-2 §8 F6 (a) picked". So one fact is read through two surfaces. dShippedRelease cites no revised unit for this read, so RH does not bind it.
- **pr34 S22 against tr2 F6.** tr2:341-342 says "no read-only verb of that unit [pr1] prints a lease's `session`", and tr2:348-356 asks dPlacedRequest for one. Yet pr34:106-109 already specs `--lease status` as read-only, printing `<tail> <fleet tag> <session> <status> <verdict> <epoch>`. pr34:468-470 (AC22) tests that it prints the holder's session, and it was unchanged since `5d1c82ac0`. It lacks only an explicit `mine`/foreign column, which `placement.py check` already derives from it. No revised parent names pr34 or `--lease status`, so tr2's ask may duplicate an act that is already specced. Only dPlacedRequest's build run, answering that ask, decides whether the two surfaces become one.

5. Citation specs: none in Group B. All 13 are rule-wide by population, and none cites tr2, wm6, wm41 or wm58.

Files:
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-10-30-spec-DEPL-dShippedRelease-95.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-11-01-spec-DEPL-dShippedRelease-138.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-11-01-spec-DEPL-dShippedRelease-125.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-2.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-6.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-34.md
