# TOOL-dWellOiledMachine-70 — the slot reap and the stale-lock break by rename into a graveyard, with the residual window named

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 36 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-70-deviation-701.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-70-deviation-701.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 38, item H7, at HIGH. TOOL-dWellOiledMachine-9 S4 copies the turnstile's nonce-guarded clear
and claims that a slot re-claimed between judgement and removal survives, while its source,
`tools/run-gates/run-gates.sh:1741-1743`, says that guard only narrows TOOL-aReapedTicket-4's race and
does not close it. Two reapers can each pass the nonce check, and the second delete removes a
successor's fresh slot; the ledger then under-counts, and `add_reservation` admits agents past
`runtime.agents-in-flight`. TOOL-dWellOiledMachine-12's `hold_lock` breaks a stale lock the same way.
This unit reaps by rename, which exactly one racer wins, restores what the winner finds was not the
slot it judged, and states the window that remains as a named ceiling.

## 2. Scope (IN)

- **S1** — The slot reap by rename. `remove_reservation` and `remove_stale_slots`
  (`tools/runtime/slots.py`, 9 S4) clear a judged slot `slot.<k>` by `os.rename` to
  `<ledger>/graveyard/slot.<k>.<reaper nonce>`, a name unique to this reaper. A rename that fails
  because the slot is gone means another reaper won: this one counts nothing and moves on. Observed by
  AC1.
- **S2** — The re-check after the win. The winner reads `nonce` inside the renamed directory. When it
  is the nonce it judged, the graveyard entry is deleted. When it is not, a successor claimed the index
  between the judgement and the rename: the winner renames the entry back to `slot.<k>`, or, when that
  index was claimed again meanwhile, to the first free index up to `slot.<limit>`, then the first free
  index above it, so the successor's slot is still counted; `remove_reservation` finds a reservation's
  slots by their `res` file, never by index. Observed by AC2.
  **Readers:** by name: READER NOT IN TREE — `slots.py` and `locks.py` are TOOL-dWellOiledMachine-9's and -12's, unbuilt at HEAD. by value: NO VALUE READERS — the renamed entries are read only by the reaper that made them.
- **S3** — The graveyard swept. Each `remove_stale_slots` first deletes every graveyard entry whose
  name's reaper is no longer running and whose `nonce` file is absent or matches no live slot, so a
  reaper killed between S1 and S2 leaves nothing counted twice and nothing lost forever. Observed by
  AC3.
  **Readers:** by name: READER NOT IN TREE — `slots.py` and `locks.py` are TOOL-dWellOiledMachine-9's and -12's, unbuilt at HEAD. by value: NO VALUE READERS — the renamed entries are read only by the reaper that made them.
- **S4** — The ceiling stated. `SLOT_REAP_WINDOW` in `slots.py`'s docstring, TOOL-aPacedTurnstile-4's
  form: between S1's rename and S2's restore a successor's slot is absent from the count, so an
  `add_reservation` counting in that instant may admit one reservation over the limit. 9 S4's sentence
  "a slot re-claimed between judgement and removal survives" is replaced in the code's comment by this
  statement, and spec 9 takes a rev bump at this unit's pass naming this unit and finding 38. Observed
  by AC4.
  **Readers:** by name: READER NOT IN TREE — `slots.py` and `locks.py` are TOOL-dWellOiledMachine-9's and -12's, unbuilt at HEAD. by value: NO VALUE READERS — the renamed entries are read only by the reaper that made them.
- **S5** — The lock break by rename. `hold_lock`'s stale break (`tools/runtime/locks.py`,
  TOOL-dWellOiledMachine-12 S2) renames a lock older than `stale_s` to `<path>.stale.<own token>`,
  re-reads its pid and start time there, deletes it when they are the ones judged stale, and renames
  it back when they are not, with the same stated window. Observed by AC5.

  **Readers:** by name: READER NOT IN TREE — `slots.py` and `locks.py` are TOOL-dWellOiledMachine-9's and -12's, unbuilt at HEAD. by value: NO VALUE READERS — the renamed entries are read only by the reaper that made them.
## 3. Non-goals (OUT)

- No change to the bash turnstile in `run-gates.sh`: its holder already reaps by rename, and its
  ticket path deletes by unique name (`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md:211-214`).
- No closing of the residual window: a lock over the whole ledger would serialise every reservation,
  and the window is one reservation wide.
- No change to the slot's files, the limit or the reservation id.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-9` — `remove_reservation`, `remove_stale_slots` and the slot ledger whose reap this unit replaces
- **consumes-from** `TOOL-dWellOiledMachine-12` — `hold_lock` in `locks.py`, whose stale break this unit replaces

## 4. Design

### Evidence

- `run-gates.sh:1741-1743`: the nonce read first and again "narrows TOOL-aReapedTicket-4's race to the
  instant between the re-read and the `rm`; it does not close it".
- TOOL-aPacedTurnstile-4 prescribes holder reap by rename because "exactly one racer wins", and names
  the residual window it leaves (`spec-aPacedTurnstile-4.md:211-214`).
- 9 S4 claims survival (`spec-9.md:45-48`); `grep -n "graveyard\|rename"` over specs 9, 43 and 45
  prints nothing.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SLOT_REAP_WINDOW` | constant naming the ceiling, in the docstring | none |
| `graveyard/` | directory under the slot ledger | none |
| `reaper-race`, `successor-restore`, `graveyard-sweep` | `slots.py --fixture` plants | none |
| `stale-break-race` | `session_binding.py --fixture` plant | none |

### Files touched (estimate)

- `tools/runtime/slots.py`
- `tools/runtime/locks.py`
- `tools/runtime/session_binding.py` (S5's fixture plant)
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-9.md` (S4's rev bump)

### Alternatives rejected

- **A rename to a fixed graveyard name.** Reaper B renames `slot.k`, claimer C re-creates it, and
  reaper A then renames C's fresh slot over a fixed name; the skeptic's reading of finding 38 shows the
  survival case stays red. The reaper's own nonce in the name makes each rename distinct, and S2's
  re-check restores what was not judged.
- **One lock file over the whole ledger.** It serialises every reservation and every reap of every
  session in the clone, to close a window one reservation wide.

## 5. Production-readiness checklist

- security — none: a node-local ledger.
- perf / scale — one rename and one read per reaped slot, where today is one delete.
- error / empty / loading states — a lost rename is another reaper's win and counts nothing; a
  reaper killed mid-reap leaves a graveyard entry S3 sweeps.
- observability — `slots.py status` prints graveyard entries pending a sweep as `graveyard · <n>`.
- risks — the stated window admits at most one reservation over the limit while a restore is in
  flight; S4 names it.
- testing — AC1 to AC5 and the arms in §7.
- migration — none: the graveyard is created at the first reap.
- user docs — `help/runtime.md`'s ledger section names the window.

## 6. Acceptance criteria

- **AC1** — When `python slots.py --fixture --plant reaper-race` starts two `remove_stale_slots` against
  one stale slot twenty times, each run ends with exactly one reap and no error.
  Red when: both reapers report a reap, or one deletes the other's work.
- **AC2** — When `--plant successor-restore` replaces the judged slot's `nonce` between the judgement and
  the rename, the slot is present at an index afterwards with the successor's `nonce` and `res`, and
  `slots.py status` counts it.
  Red when: the successor's slot is gone, as the delete of 9 S4 leaves it.
- **AC3** — When `--plant graveyard-sweep` leaves a graveyard entry from a killed reaper, the next
  `remove_stale_slots` deletes it, and a live slot is untouched.
  Red when: an orphan entry stays or a live slot is swept.
- **AC4** — When `grep -n "SLOT_REAP_WINDOW" slots.py` runs, it prints the docstring's
  statement, and `grep -c "survives" slots.py` prints 0.
  Red when: the code still claims the race closed.
- **AC5** — When `python session_binding.py --fixture --plant stale-break-race` starts two writers
  against one stale lock twenty times, every run's record holds both writes and no live lock is
  broken.
  Red when: a fresh lock taken after the judgement is deleted.

## 7. Gates

`policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/runtime/slots.py · covers AC1 AC2 AC3 · the three plants staged against the nonce-guarded delete of 9 S4 · none
New arm: tools/runtime/session_binding.py · covers AC5 · the race plant staged against `hold_lock`'s delete-on-stale · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 38 (H7).

## 10. Reuse audit

The seam reused is the turnstile's holder reap by rename into a graveyard (TOOL-aPacedTurnstile-4),
carried into `slots.py` and `locks.py` with a per-reaper name; TOOL-aReapedTicket-4 is the open ask
that names the race, DEFERRED (`memory/backlog/TOOL.md:241`). The probe
`python tools/codebase-map/reuse_lookup.py "reap a stale slot directory without deleting a successor"`
ranked `ReapRefused`, `check_claim_push_lock_stale` and `derive_int_slots`, none a rename reap in
Python, and the recall query's first hit was TOOL-aReapedTicket-4 itself, so the bash turnstile is the
one prior art and no Python seam fits.

Recall terms used: `python tools/memory-recall/query.py "how is a stale turnstile slot reaped without
a race" --terms "slot reap nonce graveyard rename race successor turnstile stale lock aReapedTicket"`
