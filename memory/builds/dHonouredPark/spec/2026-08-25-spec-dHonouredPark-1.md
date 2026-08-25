# TOOL-dHonouredPark-1 — the authored roster pair becomes mandatory on every build README, and its Definition-of-Done term becomes a check that can fail

**Status:** SPECCED · rev-2 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 3 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |

<!-- /gen:spec-records -->

## 1. Goal

`build-complete` term 3 asks whether any unit is PLANNED but unspecced. It reads the authored
`roster:units` pair. Eleven build READMEs carry one; on the rest the term returns early and passes. It
has never once reported a missing unit. The owner ruled the pair becomes mandatory and its presence
gated, which turns a term that cannot fail into one that can and closes `TOOL-aPacedTurnstile-14`.

**The population is every tracked build README.** rev-1 bound the assertion to the set
`memory/project/readme-contract.txt` marks BOUND — two rows — and the spec audit established that this
was never ruled. That registry's own header declares its subject as *which build READMEs the heading
canon and the slot budgets bind*; a roster is neither a heading nor a slot budget. The organic-growth
constraint the owner ruled governs the CONTRACT. Ruling 2 says plainly that 51 build READMEs gain a
pair and the gate needs a presence assertion, and rev-1's non-goal 4 was the spec author's inference
presented as a constraint. **Owner ruling, 2026-08-25: the roster gate binds every tracked build
README.** Non-goal 4 is withdrawn.

## 2. Scope (IN)

- **S1** — a presence assertion over EVERY tracked build README: each carries a well-formed
  `roster:units` pair. Refused when absent, duplicated or transposed, each by name.
- **S2** — the refusal reuses the driver's own vocabulary. `units_refusal` at
  `tools/unattended/unattended.sh:1557` already spells "carries no single well-formed pair … (absent,
  duplicated or transposed)" for the sibling region. rev-1 said "absent, unpaired, or inverted" —
  three different words for the same three conditions, forty lines from a message that already names
  them.
- **S3** — the pair's POSITION is already reserved. `scan_canon` stops the authored walk at
  `PLAN_OPEN` where one is present, so the canon needs no sixth slot. But `scan_canon` runs only where
  `canon=rel in bound` (`gen_build_index.py:1270`, `:1533`), which is two files — so the presence
  assertion does NOT ride it. It rides the leg's unconditional walk, beside triggers 1 and 2
  (`:1258-1268`), which already grade every tracked build README.
- **S4** — the assertion applies the DRIVER's marker discipline, not the engine's. `region()`
  (`unattended.sh:467-475`) ends `if (bad || no != 1 || nc != 1 || cat < oat) exit 3`, so a duplicated
  or transposed pair is malformed; `_marker_index` (`gen_build_index.py:965-970`) returns the first
  match with no duplicate or order notion. An assertion built on the engine's helper would ACCEPT
  what the driver REJECTS, which is two answers to one question in the two tools that both read this
  marker.
- **S5** — `roster_ids` stops discarding the refusal. It pipes `region … | grep -oE`
  (`unattended.sh:1491-1492`) and takes GREP's status, so `region`'s exit 3 is swallowed and the lines
  printed before the failure are parsed as ids. A malformed pair currently yields a partial id list
  and no error.
- **S6** — the build READMEs without a pair gain one, seeded at migration from that build's own
  tracked spec ids, so no planned-but-unspecced unit is invented and none is lost. **The set is
  DERIVED at migration time, not authored here**: it was 51 of 62 at BASE and 52 of 63 at HEAD,
  inflated by this build's own README, and it will move again before this unit lands.
- **S7** — `build-complete` term 3's vacuous pass is removed at its actual location. rev-1's S4 said
  to delete "the term's own early return"; there is no such construct — `unattended.sh:2716-2721` is
  three lines with no early return. The guards are `[ -n "$want" ] || return 0` in `roster_ids`
  (`:1489-1490`) and the same shape in `missing_units` (`:1513`), both shared with `--plan`. With the
  pair mandatory everywhere, an absent pair is a refusal from S1 and those guards are unreachable —
  but deleting either is behaviourally INERT (verified: `comm` emits one blank line, which command
  substitution strips to length 0 and `for` word-splits to zero iterations). This unit deletes them
  for the reason they are dead, and says so, rather than claiming a behaviour change it does not make.
- **S8** — the term reports a planned-but-unspecced unit by ID. `verb_plan:1614-1616` and term 3's
  `DOD_OUT` at `:2719-2720` already do this; the item is kept as a regression guard and is marked as
  green at BASE rather than presented as new work.
- **S9** — `TOOL-aPacedTurnstile-14` is closed in the same commit, with its row naming this unit.
- **S10** — arms: a README with no pair, with a duplicated pair, with a transposed pair, with a pair
  naming an id no spec carries, and with a pair equal to its spec set. **The fourth is the one the
  term exists for and it is already armed** — `unattended.test.sh:1586-1600` and the term-3 arm at
  `:968-974` assert exactly it, against fixture builds where slug and id agree by construction. The new
  arms are the first three and S5's swallowed-refusal case.

## 3. Non-goals (OUT)

- No change to the CANON. The pair sits after the last canonical slot, where `scan_canon` already
  permits it, and it is not a sixth authored slot.
- No change to what `check_authorization` freezes. That moved to the generated unit-ID set at
  `TOOL-aBoundedVerdict-11` and pointing it back at the authored pair was tried there and reverted as
  a tautology; this unit does not revisit it.
- No renderer for the pair. It stays AUTHORED — `gen_build_index.py` has never written between those
  markers and must not start, or the planned-but-unspecced question becomes derivable from the specs
  that exist, which is the tautology above.
- No movement of `exempt-pin`. It is 61 against 2 bound and 63 tracked, which is consistent; the
  migration adds pairs without touching contract membership, so no pin movement is owed. Stated so a
  builder does not helpfully adjust it.
- No requirement that the contract's EXEMPT rows gain anything. The contract governs the canon and the
  slot budgets and is untouched here; this unit's population is a different set that happens to
  include all of it.

## 4. Design

### Data model

Unchanged. The pair holds authored id rows; `roster_ids` parses them and is the only reader.

### Inventory

Eleven build READMEs carry a well-formed pair. **A naive `grep -rln roster:units` returns thirteen** —
`aRuledFrontispiece` and `dFramedEntrypoint` name the marker in prose only — so the derivation is a
pair scan, not a mention scan, and any figure built on 13 is wrong.

Three of the eleven are degenerate and the migration must not treat them as populated. `aStandingWrit`'s
pair wraps `S0..S8` handles rather than ids and yields ZERO ids under `roster_ids`' own pattern;
`aMeteredTurnstile` and `dSettledRoster` yield ONE each against multi-unit builds. The first is inert
and is migrated to ids like the rest with the inertness recorded as fixed; the other two are
under-populated rather than broken and are re-seeded from their own spec ids.

The counts in this section are the BASE measurement and are re-derived at build time. AC8 asserts the
derivation rather than the number, because this build's own README already moved 62 to 63 between the
spec's base and its fold.

### Migration

Two commits. The engine and the gate first; the READMEs second, because their content is derived per
build and the diff is mechanical and reviewable by re-running the derivation. **The gate lands AFTER
the migration, or it reds every unpaired README on its own commit** — about fifty of them. Under
rev-1's two-file population that rationale was false, which is how the audit found the population
error; under the ruled population it is the operative reason, and it is the same ordering
`TOOL-aRuledFrontispiece-1` used for the slot contract.

### Alternatives rejected

**Delete the reader, the report and the term.** The other option the owner was offered. It removes a
Definition-of-Done item that cannot fail, which is attractive, and it also removes the only structure
in the kit that can express a unit somebody planned and nobody specced. The owner chose to make the
signal real rather than to stop asking.

**Derive the roster from the specs.** Tried inside `TOOL-aBoundedVerdict-11` and reverted: the
generated region is rendered FROM the specs that exist, so `roster_ids` becomes a subset of `spec_ids`
by construction and the term is empty always. That is the assertion-between-two-derived-values class
this tree names. S6's one-time SEED is a different thing — it fixes a starting value that thereafter
diverges as a human adds a planned unit; a renderer never diverges.

**Bind the contract's BOUND set.** rev-1's design, withdrawn on the owner's ruling. It gated two files
while migrating fifty, so after the migration about sixty pairs would carry no assertion at all and a
later deletion would silently restore term 3's vacuous pass on that build — the exact failure this
unit exists to remove, reintroduced by the scoping.

**Bind only non-terminal builds.** Offered to the owner and declined. It would have spared closed
builds a gate that can only ever red on them, at the cost of a population nothing else in the tree
derives.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` for S1-S4 · `tools/unattended/unattended.sh` for S5, S7 and S8
· about fifty build READMEs for S6 · `memory/backlog/TOOL.md` for S9 · both kits' version sites · the
`build-readme-surface` dossier · `memory/DECISIONS.md` for this unit's ruling row.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one marker lookup per tracked build README, on a leg that already reads every one of
  them for triggers 1 and 2.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a README with an EMPTY pair is legal and means the build plans
  exactly its specced units; it is distinct from an ABSENT pair, which refuses.
- observability — S8 is the observability: the term names ids rather than a count. S5 is the other
  half — a malformed pair currently produces a partial answer and no error.
- risks — the ordering, stated in §4 rather than left to be discovered. Second risk: S4's marker
  discipline. Building the assertion on the engine's first-match helper would pass a duplicated pair
  that the driver refuses, and the two tools would disagree about the same bytes.
- read path — this unit charges `memory/DECISIONS.md` for its ruling row and
  `memory/guides/UNATTENDED-PROTOCOL.md` if the protocol states the pair's mandatory status, which is
  checked rather than assumed. Both are capped members; at BASE the path has 60 B of headroom and one
  decision row has historically cost ~122 B, so the ceiling moves in the same commit per this build's
  rules slot.
- testing + left-shift gates — S10's arms. Three are new, one is already armed and marked as such, and
  the swallowed-refusal case has never been exercised.
- migration / rollback — two commits, both invertible; the pairs are additive and inert if the gate is
  reverted.
- user docs — `memory/HYGIENE.md` via its template gains the pair's grammar and its mandatory status.

## 6. Acceptance criteria

- **AC1** — When any tracked build README carries no `roster:units` pair, the slot leg exits 1 naming
  that file, observed RED against a staged deletion before the arm is written.
- **AC2** — When a build README carries that marker duplicated or transposed, the leg exits 1 naming
  which condition it found, in the same words `unattended.sh:1557` uses for the sibling region.
- **AC3** — When a build's pair names an id no tracked spec defines,
  `bash tools/unattended/unattended.sh --plan <slug>` reports that id as MISSING and `build-complete`
  does not pass. **Green at BASE** — `unattended.test.sh:1586-1600` and `:968-974` already assert it —
  and kept as a regression guard, not as evidence this unit added coverage.
- **AC4** — When a build's pair equals its spec set, `build-complete` term 3 passes and says so.
- **AC5** — When a pair's markers are duplicated, `roster_ids` exits non-zero rather than returning the
  ids printed before the refusal. Observed RED first: at BASE it returns a partial list and status 0.
- **AC6** — When the migration is re-run, `git diff` shows every migrated pair's ids equal to that
  build's tracked spec ids, across the whole DERIVED set. The set is computed by the migration, not
  read from this document.
- **AC7** — When `memory/backlog/TOOL.md` is read at HEAD, `TOOL-aPacedTurnstile-14` is CLOSED and
  names this unit.
- **AC8** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, the bar is
  green and the slot leg's own summary line reports the pair present on every tracked build README,
  **printing the count it derived** rather than matching a figure written here. `do_check_format`
  already prints `len(tracked)` at `gen_build_index.py:1553`; this criterion asserts that number and
  the pair count agree, which is the only form that cannot go stale.
- **AC9** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both totals
  are recorded and `.memory-tree.conf` carries this unit's own movement line.

## 7. Gates

`unattended kit gate` · `build README slot contract` · `memory hygiene` (incl. checks 9 and 16) ·
`build-index selftest` · `check-arms.py` floors — this unit adds `fail` branches to the driver, which
units 3 and 4 both list and rev-1 omitted · `check-kit-versions.sh` · `check-verdict-epoch.sh` ·
`kit/dogfood doc parity`.

## 8. Open questions

- **F1 — does the presence assertion live in the driver or on the slot-contract leg?** The SLOT LEG,
  per S3: the driver has no notion of the population, and a presence check there would only run when a
  run exists, which is not when a README is authored. S4 records the condition that answer carries —
  the leg must not inherit `_marker_index`'s first-match semantics.
- **F2 — RESOLVED.** rev-1 asked what happens to a build EXEMPT today that becomes bound later. The
  contract's membership no longer scopes this assertion, so the question does not arise.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s first park.
- rev-2 · 2026-08-25 · spec-audit fold. **Population widened to every tracked build README on the
  owner's ruling of 2026-08-25**; non-goal 4 withdrawn as an unruled inference, and §4's migration
  ordering rationale — false under the two-file scoping — restored as the operative reason. Counts
  moved from authored figures to derivations (S6, AC6, AC8). Added S4 and S5 for the engine/driver
  marker-discipline split and the swallowed `region` refusal. Rewrote rev-1's S4 as S7 after the audit
  found it named a construct that does not exist. Marked AC3 and S8 as green at BASE. Added the
  degenerate-pair inventory, the 13-vs-11 grep trap, the exempt-pin non-goal, and the read-path charge.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `roster units authored pair planned unspecced missing
units build complete term vacuous authorization frozen id set marker discipline`.

The seam is `roster_ids` in `tools/unattended/unattended.sh`, the pair's ONE reader, with
`missing_units` and `build-complete` term 3 above it — verified by grep over the driver, which returns
the definition, those two callers and nothing else. `scan_canon` in `gen_build_index.py` is the second
seam and already stops the authored walk at `PLAN_OPEN`, so the position this unit requires is one the
canon already reserves — but `scan_canon` itself is gated on the bound set and is therefore NOT the
host for the assertion, which is the correction rev-2 makes to rev-1's §8 F1.

Two negative findings worth recording. `check_authorization` deliberately does NOT read this pair, and
a reuse pass that wired the presence assertion through it would re-create the tautology
`TOOL-aBoundedVerdict-11` reverted. And the two tools that read this marker do not agree about what
well-formed means: the driver refuses duplicates and transpositions, the engine's helper takes the
first match. That disagreement is pre-existing, is not caused by this unit, and would be inherited by
any assertion built on the engine's helper — which is why S4 exists.
