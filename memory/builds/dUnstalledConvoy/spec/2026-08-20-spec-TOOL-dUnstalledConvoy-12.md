# TOOL-dUnstalledConvoy-12 — a hygiene check asserts every acceptance criterion of a closed unit is evidenced or amended

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

## 1. Goal

`TOOL-dUnstalledConvoy-11` defines the acceptance ledger. This unit adds the check that makes it
binding: for every unit closed at or after the declared cutoff, each acceptance criterion its spec
numbers must appear in a tracked ledger, in one of the two legal forms.

## 2. Scope (IN)

- **S1** — a new check inside `tools/memory-tree/check-memory-hygiene.sh`, not a new gate leg, for
  the reason units 6 and 11 give and which the kickoff manifest records as a trap.
- **S2** — the population is every **Tier-2** spec whose status is `CLOSED`, whose filename date is at
  or after `ACCEPTANCE_LEDGER_CUTOFF`, and which actually carries an acceptance-criteria HEADING.
  `WONTDO` specs are excluded: a retired unit built nothing. Review fold: M13. The first draft had no
  tier filter and read section 6 by NUMBER, but the spec format gives Tier-1 a light profile in which
  the section canon is not enforced — two closed Tier-1 specs in this corpus number their criteria
  under section 5 and carry Gates at section 6 — so the check would have redded specs that are legal
  under the very format it enforces, and would have silently made an acceptance section mandatory for
  Tier-1, a format change this build never states.
- **S2a** — this build's OWN closed specs are inside the population, by the cutoff resolution in
  `TOOL-dUnstalledConvoy-11`. They carry back-filled ledgers, so the check's first run measures real
  units rather than an empty set. Review fold: H2.
- **S3** — the criterion set is derived by locating the acceptance-criteria section BY HEADING TEXT,
  using the same regex the sibling acceptance-witness rule already uses a few hundred lines above,
  extracted into ONE shared fragment so the two checks cannot disagree. Labels are read in the three
  spellings that rule already sanctions. Review fold: M13.
- **S4** — for each criterion, a tracked record under the same build whose `**Serves:**` kind is
  `journal` and whose `**Evidences:**` line names the unit must carry a line for that label, in the
  OBSERVED form with a backticked token or the AMENDED form with a revision.
- **S5** — a Tier-2 spec in the population whose acceptance-criteria section names NO criterion label
  is a refusal, not a vacuous pass. Scoping it to Tier-2 is review fold M13; the refusal itself is the
  real defect it was written for. A closed unit with no numbered criteria cannot be evidenced, and a subset test over
  an empty set is the vacuity this repo has already paid for twice.
- **S6** — a ledger line whose form is neither OBSERVED nor AMENDED is a refusal naming the label and
  the two legal forms.
- **S7** — the check ANNOUNCES an empty population. A corpus where the cutoff excludes every closed
  spec prints a named line saying so, so the first green is not mistaken for coverage.
- **S8** — the check's header states what it does NOT check: that an observation token names anything
  real, that the observation was actually made, or that the amendment was justified. It reads shape
  and coverage, exactly as its sibling acceptance-witness rule does.

## 3. Non-goals (OUT)

- Validating an observation token's referent. The sibling rule reads shape only and says so; a
  second, stricter policy on the same kind of token would be two answers to one question.
- Grading a ledger line for a criterion the spec does not number. Extra lines are harmless; missing
  ones are the defect.
- Any Definition-of-Done item. The owner chose a hygiene check.
- Rewriting or grandfathering existing records. `ACCEPTANCE_LEDGER_CUTOFF` does that, and it is
  declared by unit 11.
- Reading a spec's §6 for anything but labels. Whether a criterion is a GOOD criterion is a review's
  question, not a gate's.

## 4. Design

### Inventory

| Case | Verdict |
|---|---|
| every numbered criterion has a legal ledger line | pass |
| a criterion has no ledger line | refusal naming the spec, the label and the build |
| a ledger line is in neither legal form | refusal naming the label and both forms |
| the spec numbers no criterion at all | refusal, by S5 |
| the spec is `WONTDO` | excluded, by S2 |
| the spec predates the cutoff | excluded, and counted in the announced line |
| the population is empty | announced line, by S7 |

### The two ways this check could ship unable to fail

Both are named because this repo's own bug catalogue says a gate satisfied by its own structure is
the recurring defect, and this check has exactly two routes to it.

The first is the empty population. Every closed spec in this corpus predates the cutoff on the day
the pair lands, so the check's first run sees nothing. S7's announced line is what keeps that from
reading as a pass, and the acceptance criteria below assert the line rather than the exit code.

The second is the empty criterion set. A spec whose §6 uses prose instead of numbered labels yields
no criteria, and "every criterion is evidenced" is vacuously true over none of them. S5 turns that
into a refusal, which is the same fix `build-complete`'s fourth term applies to its own empty-region
case.

### Why the label spelling is shared and not re-derived

`TEMPLATE-SPEC.md` sanctions three spellings for a criterion label and its acceptance-witness rule
already parses them. This check must use the same parse. Two checks disagreeing about what a label
looks like would produce a spec that satisfies one and reds the other, with no reading of the
document that resolves it.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | one check, three refusals, one announced line |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the cases in §6 and the `ARMS_FLOORS` bump |
| `.memory-tree.conf` | the `ARMS_FLOORS` entry this unit moves — a BUILD-WIDE shared write, review fold M7 |
| `tools/memory-tree/README.md` | the stated check COUNT and the delegation breakdown that partitions it — review fold M19 |
| the codebase-map dossier for this gate | the second carrier of that same count |

### Alternatives rejected

- **Deriving the criterion set from the ledger rather than the spec.** Rejected: it inverts the
  direction and makes the check unable to notice a criterion nobody evidenced, which is the whole
  subject.
- **Warning rather than failing.** Rejected: a warning is the state the rule is in today, where M2
  already says to change the spec before diverging and nothing observes it.
- **Keying the population on the build's run-state file.** Rejected in unit 11's F1: the rule is
  universal, and keying it on run mode makes it two rules.

## 5. Production-readiness checklist

- security — N/A — a read-only documentation check.
- perf / scale — one §6 scan per in-population spec and one record scan per build. The hygiene gate
  already walks both trees.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S5 and S7 are this item, and §4 names both as the correctness
  risk rather than a tidiness one.
- observability — three distinct refusals and one announced line.
- risks (concurrency, data-loss, rollback hazards) — read-only.
- testing + left-shift gates — the cases in §6. Hygiene checks in one numeric range are OFF unless a
  pin is armed, so a fixture tree written without pins arms nothing — the fixture must set the pin,
  or the arm passes by finding nothing.
- migration / rollback — the cutoff, declared by unit 11. Rollback is reverting the check and the
  conf key together.
- user docs — `memory/HYGIENE.md`, owned by unit 11.

## 6. Acceptance criteria

- **AC1** — A fixture with a closed spec dated after the cutoff, numbering three criteria and a
  ledger covering all three, passes, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC2** — The same fixture with one criterion missing from the ledger reds, naming the spec and the
  label, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC3** — A ledger line for a numbered criterion carrying neither a backticked token nor a revision
  reds, naming both legal forms, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC4** — A closed spec dated after the cutoff numbering NO criteria reds, per S5, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC5** — A `WONTDO` spec with no ledger passes.
- **AC6** — A closed spec dated BEFORE the cutoff passes, and is counted in the announced line, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC7** — Run against this repo as it stands, the check measures this build's OWN back-filled units
  rather than an empty set, and `bash tools/memory-tree/check-memory-hygiene.sh` exits 0. The
  empty-population line remains implemented and is exercised by a fixture instead. Review fold: H2.
- **AC9** — A CLOSED Tier-1 spec whose section 6 is not Acceptance criteria PASSES, observed in
  `tools/memory-tree/check-memory-hygiene.test.sh`. Review fold: M13.
- **AC10** — `grep` over `tools/memory-tree/README.md` finds the updated check count and the updated
  delegation breakdown, and the codebase-map dossier for this gate agrees. Review fold: M19.
- **AC11** — `bash tools/check-kit-versions.sh` and the `verdict epoch` leg are both green, with the
  kit-version bump carried by THIS unit's commit as the last of the pair. Review fold: H12.
- **AC12** — The check's header STATES what it cannot buy, observed by `grep` over
  `tools/memory-tree/check-memory-hygiene.sh`. Review fold: L1.
- **AC8** — Each refusal is observed RED against a fixture with the range pin ARMED before the unit
  lands, and `ARMS_FLOORS` for the hygiene checker matches its new `fail` call-site count.

## 7. Gates

`memory-tree hygiene` · `memory-tree hygiene selftest` · `harness arms` · `kit version markers` ·
`verdict epoch` · the full bar at the push boundary. Review fold: H12 — `verdict epoch` is the leg
this unit's commit ordering actually trips, and the first draft did not name it.

## 8. Open questions

- **F1 — does the check read the ledger from the SAME build only?** S4 scopes it to the build's own
  records. But the record-binding grammar deliberately lets a record name a spec in another build,
  because one closing review legitimately covers two. Options: same build only, which is simpler and
  matches how journals are filed; or repo-wide, which matches the binding grammar's stated
  intention. **Recommendation: repo-wide**, searching the whole record corpus for a `journal` record
  evidencing the unit. It costs one wider scan and it avoids a refusal on a legitimately cross-filed
  record, which would be a wedge with no in-band repair. Resolve before building — it changes S4's
  population and the check's cost line.

## 9. Revision log

- rev-2 · 2026-08-20 · folded the spec audit: M13 (the population is scoped to Tier-2 specs carrying an
  acceptance-criteria HEADING, located by the sibling rule's own regex, because a Tier-1 spec legal
  under the format would otherwise red), H2 (this build's own back-filled units are the first
  population, so the check ships exercised), M19 (the kit README and the dossier carry the check
  count, named outright instead of a conditional row that resolved to nothing), H12 (`verdict epoch`
  added to the gates, and this unit carries the kit-version bump), L1. Five new criteria.
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a hygiene check reads a spec section and the records that
serve it"` returns the memory-tree hygiene dossier and the `_resolve_cap` affordance seam, which is
the conf-resolution seam `ACCEPTANCE_LEDGER_CUTOFF` is read through — and whose own header records
that the engine pre-sets its keys and sources the conf OVER them, so a blank value means skip. That
matters here: the cutoff must not be silently skippable, and the resolution seam is where a key that
must not be skippable is re-normalised.

`python tools/memory-recall/query.py "how does a hygiene check avoid passing over an empty population
and where are the pins that arm one" --terms "hygiene check population empty vacuous pin armed range
skeleton acceptance witness label spelling cutoff arms floor"` returns the vacuous-selector class,
the range-pin arming trap and the acceptance-witness rule this check mirrors. Verified at source at
writing time: the record-binding grammar defines the `journal` kind and permits cross-build ids,
which is the evidence behind §8 F1.

Recall terms used: hygiene check population empty vacuous pin armed range skeleton acceptance witness
label spelling cutoff arms floor.
