# TOOL-dFramedEntrypoint-10 — the authored roster pair becomes mandatory, and its Definition-of-Done term becomes a check that can fail

**Status:** SPECCED · rev-1 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 3 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`build-complete` term 3 asks whether any unit is PLANNED but unspecced. It reads the authored
`roster:units` pair, 11 of 62 build READMEs carry one, and on the other 51 the term returns early and
passes. It has never once reported a missing unit. The owner ruled the pair becomes mandatory and its
presence gated, which turns a term that cannot fail into one that can and closes
`TOOL-aPacedTurnstile-14`.

## 2. Scope (IN)

- **S1** — a presence assertion: every build README the contract BINDS carries a well-formed
  `roster:units` pair. Refused when absent, when unpaired, or when inverted, each by name.
- **S2** — the pair's POSITION is already reserved. `scan_canon` stops the authored walk at
  `PLAN_OPEN` where one is present, so the canon needs no sixth slot and no change; this unit makes
  a reservation into a requirement.
- **S3** — the 51 build READMEs without a pair gain one. Its contents are DERIVED at migration from
  that build's own tracked spec ids, so no planned-but-unspecced unit is invented and no existing one
  is lost; a build whose roster equals its spec set is the honest starting state.
- **S4** — `build-complete` term 3 stops returning early on an absent pair. With the pair mandatory,
  an absent one is a REFUSAL from S1 rather than a vacuous pass here, so the term's own early return
  becomes unreachable and is deleted rather than left as a second opinion about the same condition.
- **S5** — the term reports a planned-but-unspecced unit by ID, not as a count, so the finding names
  what to act on.
- **S6** — `TOOL-aPacedTurnstile-14` is closed in the same commit, with its row naming this unit.
- **S7** — arms: a bound README with no pair, with an unpaired marker, with an inverted pair, with a
  pair naming an id no spec carries, and with a pair equal to its spec set. The fourth is the one the
  term exists for and the one that has never fired.

## 3. Non-goals (OUT)

- No change to the CANON. The pair sits after the last canonical slot, where `scan_canon` already
  permits it, and it is not a sixth authored slot.
- No change to what `check_authorization` freezes. That moved to the generated unit-ID set at
  `TOOL-aBoundedVerdict-11` and pointing it back at the authored pair was tried there and reverted as
  a tautology; this unit does not revisit it.
- No renderer for the pair. It stays AUTHORED — `gen_build_index.py` has never written between those
  markers and must not start, or the planned-but-unspecced question becomes derivable from the specs
  that exist, which is the tautology above.
- No requirement on EXEMPT READMEs. S1 binds what the contract binds; a build outside the registry is
  outside this too, which is the population discipline `dFramedEntrypoint` established.

## 4. Design

### Data model

Unchanged. The pair holds authored id rows; `roster_ids` already parses them and is the only reader.

### Inventory

62 build READMEs, 11 carrying a pair. 51 gain one at migration, each seeded from that build's tracked
spec ids. One build's pair — `aStandingWrit`'s — wraps `S0..S8` handles rather than ids and is inert;
it is migrated to ids like the rest and the inertness recorded as fixed rather than silently kept.

### Migration

One commit for the engine and the gate; the 51 READMEs in a second, because their content is derived
per build and the diff is mechanical and reviewable by re-running the derivation. The gate lands
AFTER the migration, or it reds 51 files on its own commit — the same ordering
`TOOL-aRuledFrontispiece-1` used for the slot contract, and for the same reason.

### Alternatives rejected

**Delete the reader, the report and the term.** The other option the owner was offered. It removes a
Definition-of-Done item that cannot fail, which is attractive, and it also removes the only structure
in the kit that can express a unit somebody planned and nobody specced. The owner chose to make the
signal real rather than to stop asking.

**Derive the roster from the specs.** Tried inside `TOOL-aBoundedVerdict-11` and reverted: the
generated region is rendered FROM the specs that exist, so `roster_ids` becomes a subset of
`spec_ids` by construction and the term is empty always. That is the assertion-between-two-derived-
values class this tree names.

### Files touched (estimate)

`tools/unattended/unattended.sh` for S1, S4 and S5 · `tools/memory-tree/gen_build_index.py` if the
presence assertion rides the slot-contract leg rather than the driver · 51 build READMEs ·
`memory/backlog/TOOL.md` for S6 · both kits' version sites · the `build-readme-surface` dossier.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one marker lookup per bound README, on a leg that already reads every one of them.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a bound README with an EMPTY pair is legal and means the build
  plans exactly its specced units; it is distinct from an ABSENT pair, which refuses.
- observability — S5 is the observability: the term names ids rather than a count.
- risks — the ordering. A gate landing before the migration reds 51 files in its own commit, and the
  spec says so rather than leaving it to be discovered.
- testing + left-shift gates — five arms, and the fourth must be observed RED first, because it is
  the case that has never occurred in this corpus.
- migration / rollback — two commits, both invertible; the pairs are additive and inert if the gate
  is reverted.
- user docs — `memory/HYGIENE.md` via its template gains the pair's grammar and its mandatory status.

## 6. Acceptance criteria

- **AC1** — When a BOUND build README carries no `roster:units` pair, the gate exits 1 naming that
  file, observed RED against a staged deletion before the arm is written.
- **AC2** — `<!-- roster:units -->` — when a bound README carries that marker unpaired or inverted,
  the gate exits 1 naming which of the two it found.
- **AC3** — When a build's pair names an id no tracked spec defines,
  `bash tools/unattended/unattended.sh --plan <slug>` reports that id as MISSING, and
  `build-complete` does not pass. This is the case the term exists for and it has never fired.
- **AC4** — When a build's pair equals its spec set, `build-complete` term 3 passes and says so.
- **AC5** — `git diff` after re-running the derivation shows each migrated pair's ids equal to that
  build's tracked spec ids, across all 51.
- **AC6** — `memory/project/readme-contract.txt` — when a README it lists as EXEMPT carries no pair,
  the gate exits 0; the requirement binds the contract's population and nothing else.
- **AC7** — When `memory/backlog/TOOL.md` is read at HEAD, `TOOL-aPacedTurnstile-14` is CLOSED and
  names this unit.
- **AC8** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, the bar is
  green, and the `unattended kit gate` and slot-contract legs both pass over 62 READMEs.

## 7. Gates

`unattended kit gate` · `build README slot contract` · `memory hygiene` · `build-index selftest` ·
`check-kit-versions.sh` · `check-verdict-epoch.sh` · `kit/dogfood doc parity`.

## 8. Open questions

- **F1 — does the presence assertion live in the unattended driver or on the slot-contract leg?**
  The driver owns the term that reads the pair; the slot leg already walks every build README and
  knows the bound population. Recommendation: the SLOT LEG, because the population is the registry's
  and the driver has no notion of it — and a presence check in the driver would only run when a run
  exists, which is not when a README is authored.
- **F2 — what happens to a build that is EXEMPT today and becomes bound later?** It gains the pair as
  part of its conformance, which is the organic path the owner ruled for the contract itself.
  Recommendation: as specced; no separate mechanism.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s first park.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `roster units authored pair planned unspecced missing
units build complete term vacuous authorization frozen id set`. The seam is `roster_ids` in
`tools/unattended/unattended.sh`, the pair's ONE reader, with `missing_units` and `build-complete`
term 3 above it — verified by grep over the driver, which returns the definition, those two callers
and nothing else. `scan_canon` in `gen_build_index.py` is the second seam and already stops the
authored walk at `PLAN_OPEN`, so the position this unit requires is one the canon already reserves.
The negative finding worth recording: `check_authorization` deliberately does NOT read this pair, and
a reuse pass that wired the presence assertion through it would re-create the tautology
`TOOL-aBoundedVerdict-11` reverted.
