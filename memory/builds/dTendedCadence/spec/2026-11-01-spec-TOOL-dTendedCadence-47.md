# TOOL-dTendedCadence-47 — an offender that regresses after its ask closed is filed again, never absorbed as a `seen` receipt

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 8 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 45 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H12. Unit 15's `write_breach_ask` step (1) matches only a live ask carrying the marker
`maintain key <key hash>` (`OPEN`, `BLOCKED` or `DEFERRED`), and step (2) re-files the same stable
text (spec-15 S2, :55-65). When the ask has closed, as fixed and then regressed or as `WONTDO`, the
text's content key is already on record, so the filing only appends a receipt, route `seen`, and
nothing re-places the ask. Unit 8 has a `survivor` branch for this, for patch intakes only
(spec-8 :202-205). Every later breach of that offender is silently absorbed and printed as handled.
This unit gives step (1) its closed-ask case.

## 2. Scope (IN)

- **S1** — The closed ask. `read_closed_marker_ask(root, key_hash)` in
  `tools/drift-audit/maintain_file.py` answers the newest ask carrying the marker whose state is
  `CLOSED` or `WONTDO`, found by the same `git grep -F` over the tracked `BACKLOG.md` files and
  confirmed by `gen_build_index.py --asks --build <home> --all`, or None. It runs only when step (1)
  finds no live ask. Observed by AC1 and AC2.
- **S2** — The re-filing. When S1 answers an ask id, step (2)'s text gains one clause after the
  offender key, `· regressed after <ask id>`, so its content key differs from the closed ask's and a
  new intake is filed, route `filed`, which Entry places as an ask. A regression after that ask closes
  in turn names the newer id. The breach is printed `file — <reading> · key <key hash> · filed ·
  regressed after <ask id>`. Observed by AC1.
- **S3** — Step (1) is unchanged for a live ask, so an offender whose ask is still open stays `seen`
  and never files a second content key. Observed by AC2.

## 3. Non-goals (OUT)

- Where a `seen` clause is written and committed: id 44, TOOL-dTendedCadence-48.
- The band and probe fields of the text: id 10, TOOL-dTendedCadence-48.
- Unit 8's `survivor` branch for patch intakes, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-15` — `write_breach_ask`, its marker and its two steps, to which this unit adds the closed-ask case
- **hands-off** `TOOL-dTendedCadence-48` — `write_breach_ask`'s step (1), whose live-ask recurrence that unit's S23 turns into a receipt (review id 44)

## 4. Design

### Evidence

- Spec-15 S2 step (1) confirms liveness by `gen_build_index.py --asks --build <home>`; BUILD-METHOD
  M9 names the same generator's `--asks --build <slug> --all` for every ask, closed ones included.
- dWellOiledMachine-4 S1, as the finding's skeptic read it, makes a re-typed text append a receipt to
  the intake already on record.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_closed_marker_ask` | function, `maintain_file.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `regressed after <ask id>` | text clause | none |

### Files touched (estimate)

- `tools/drift-audit/maintain_file.py`: S1, S2
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Route the regression through unit 8's `survivor`.** `survivor` is the outcome of a landed patch
  build's offender; an ask has no patch build, so the branch would need a second meaning.
- **Re-open the closed ask.** A closed ask is another build's record, and this walk writes no row of
  it.

## 5. Production-readiness checklist

- security — N/A — a read of tracked backlog files and one more text clause.
- perf / scale — one more `git grep -F` and one generator call, only for an offender with no live ask.
- error / empty / loading states — a generator call that fails prints its line and files as step (2)
  does today, so a regression is never dropped on a failed read.
- observability — S2's line names the closed ask.
- risks — an offender that regresses every period after each fix files once per closure, which is
  the owner's signal that the fix does not hold.
- testing — the criteria of §6.
- migration — N/A — the route is new in this build.
- user docs — `help/maintain.md`'s section "When a reading breaches its pin" names the regression
  clause.

## 6. Acceptance criteria

- **AC1** — When `python maintain_file.py route` runs a breach under `maintain.on-breach =
  "file-ask"` in a fixture whose only ask carrying its marker reads `CLOSED`, with a recording filer,
  it prints `filed · regressed after <that id>`, and the recorded text carries that clause.
  Red when: the breach is recorded as `seen` against the closed ask's intake.
- **AC2** — When the same fixture's ask reads `OPEN`, the run prints `seen`, and every text the
  recording filer records, if any, is byte-equal to that ask's own filing text, so no new content key
  is filed.
  Red when: a live ask's offender is filed under a second content key.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · a marker carried by a CLOSED ask and by an OPEN one, staged against step (1) reading live asks only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 45 (HIGH, item H12) of the round-1 spec
  audit.

## 10. Reuse audit

The seams are unit 15's `write_breach_ask` and its marker search, and `gen_build_index.py --asks`,
called with `--all`. `python tools/codebase-map/reuse_lookup.py "find an ask carrying a marker and
whether it is closed"` ranked `ask_filed_in`, `ask_home_of` and `asks_filed_in`
(`tools/unattended/lib-unattended.sh`, fan-in 2, no seam) and `extract_prompt_marker`; the shell
helpers answer whether an id is filed, not its state, so the state read stays the generator's.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
