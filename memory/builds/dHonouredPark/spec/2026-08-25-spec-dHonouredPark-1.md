# TOOL-dHonouredPark-1 — the authored roster pair becomes mandatory on every build README, and its Definition-of-Done term becomes a check that can fail

**Status:** SPECCED · rev-3 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 3 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md) | spec-audit | TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |

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
- **S5** — a malformed roster pair REFUSES, all the way to the caller. Three things are wrong today
  and fixing only the first fixes nothing:
  1. `roster_ids` pipes `region` into `grep -oE` into `sort -u`, so it takes SORT's status. `region`'s
     refusal is discarded and the lines printed before it are parsed as ids. (rev-2 said it takes
     grep's status; the terminal stage is `sort -u`.)
  2. **No caller tests that status.** `missing_units` assigns into a variable and then tests the
     variable for emptiness; `verb_plan` tests a command substitution for emptiness. The script sets
     `set -u` and not `set -e`. So propagating a status out of `roster_ids` changes nothing observable
     — round 2 established that rev-2's item would have gone green while the vacuous pass survived.
     The callers are in scope.
  3. The obvious fix is `set -o pipefail` on that pipeline, and it is WRONG on its own: a well-formed
     but EMPTY pair legitimately produces no ids, and `grep -oE` exits 1 on no match, so `pipefail`
     turns the legal empty case into a refusal. §5 declares the empty pair legal; AC6 pins it.

  The refusal must therefore come from `region`'s own status, tested explicitly, with the empty result
  distinguished from the malformed one.
- **S6** — the build READMEs without a pair gain one, seeded at migration from that build's own
  tracked spec ids, so no planned-but-unspecced unit is invented and none is lost. **The set is
  DERIVED at migration time, not authored here**: it was 51 of 62 at BASE and 52 of 63 at HEAD,
  inflated by this build's own README, and it will move again before this unit lands.
- **S7** — `build-complete` term 3 has no early return of its own, and rev-1's instruction to delete
  one was unimplementable. There is exactly ONE guard of the `[ -n "$want" ] || return 0` shape, and it
  is in `missing_units`. `roster_ids` has two guards of a DIFFERENT shape — a missing file and an
  absent open marker — which rev-2 quoted as if they were the same construct.

  With the pair mandatory everywhere, all three become unreachable: an absent file, an absent marker
  and an empty roster are each a refusal from S1 before this code runs. Deleting them is behaviourally
  INERT (verified: `comm` over an empty side emits one blank line, which command substitution strips to
  length 0 and `for` word-splits to zero iterations). This unit deletes them because they are dead, and
  says so, rather than claiming a behaviour change it does not make.

  Locate all three by reading `roster_ids` and `missing_units`, not by line number: rev-2 gave
  coordinates and they held different code.
- **S8** — the term reports a planned-but-unspecced unit by ID. `verb_plan:1614-1616` and term 3's
  `DOD_OUT` at `:2719-2720` already do this; the item is kept as a regression guard and is marked as
  green at BASE rather than presented as new work.
- **S9** — `TOOL-aPacedTurnstile-14` is closed in the same commit, with its row naming this unit.
- **S11** — this unit prices its own read-path charge and moves `READ_PATH_CEILING` by it, per owner
  ruling 2 and this build's rules slot. It charges its `memory/DECISIONS.md` row, and
  `memory/guides/UNATTENDED-PROTOCOL.md` if the protocol states the pair's mandatory status — which is
  checked, not assumed, and if it does then the edit goes to `tools/unattended/PROTOCOL.template.md`,
  because the guide is a byte-identical RENDER whose drift check refuses a direct edit. rev-2 carried
  this as a checklist bullet and an acceptance criterion; that is not declared scope.
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
- No change to `memory/project/readme-contract.txt` itself. That registry governs the canon and the
  slot budgets, this unit's population is a different question, and the two are simply unrelated —
  which is the whole content of ruling 1. rev-2 kept a bullet reading "No requirement that the
  contract's EXEMPT rows gain anything", which is the withdrawn constraint under a new name and
  contradicts S1 and S6 outright.

## 4. Design

### Data model

Unchanged. The pair holds authored id rows; `roster_ids` parses them and is the only reader.

### Inventory

Eleven build READMEs carry a well-formed pair. **A naive `grep -rln roster:units` returns thirteen** —
`aRuledFrontispiece` and `dFramedEntrypoint` name the marker in prose only — so the derivation is a
pair scan, not a mention scan, and any figure built on 13 is wrong.

The migration must not assume a carried pair is a populated one, and rev-2's inventory of which are
degenerate was wrong in both directions — so this section states the DERIVATION instead of a list.

For each build carrying a pair, compare the ids `roster_ids` extracts against the ids its tracked specs
define. `aStandingWrit` is the extreme case: its pair wraps `S0..S8` handles rather than ids and yields
ZERO, so it is inert. `dUnstalledConvoy` is under-populated at a scale rev-2 missed entirely, its pair
naming markedly fewer ids than its tracked specs. And the remedy rev-2 prescribed for two other builds
is a NO-OP, because each has a single tracked spec: re-seeding returns the identical id and leaves the
front-matter under-population it was meant to fix untouched.

So: re-seed every pair from its build's tracked spec ids, compute the before/after id counts per build,
and record which pairs actually changed. A list of degenerate builds authored here would be a fourth
authored count of a derived population in a build whose whole subject is that they rot.

The counts in this section are the BASE measurement and are re-derived at build time. AC8 asserts the
derivation rather than the number, because this build's own README already moved 62 to 63 between the
spec's base and its fold.

### Migration

Two commits, **migration FIRST**:

1. The READMEs gain their pairs, each seeded from that build's own tracked spec ids. Mechanical, and
   reviewable by re-running the derivation.
2. The engine and the gate.

That order is the whole point and rev-1 and rev-2 both stated it backwards in the sentence before
stating it forwards. A gate landing first reds every unpaired README on its own commit — about fifty
of them. Under rev-1's two-file population that rationale was false, which is how the audit found the
population error; under the ruled population it is the operative reason, and it is the same ordering
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
  WHICH condition it found. This is deliberately stronger than the driver's sibling message, which
  lists all three at once and distinguishes none because `region` collapses them into a single exit
  status. S2's reuse is of the VOCABULARY — absent, duplicated, transposed — not of that one-line
  message; rev-2 asked for both and they are incompatible.
- **AC3** — When a build's pair names an id no tracked spec defines,
  `bash tools/unattended/unattended.sh --plan <slug>` reports that id as MISSING and `build-complete`
  does not pass. **Green at BASE** — `unattended.test.sh:1586-1600` and `:968-974` already assert it —
  and kept as a regression guard, not as evidence this unit added coverage.
- **AC4** — When a build's pair equals its spec set, `build-complete` term 3 passes. **GREEN AT BASE**
  by the same argument that marks AC3 — an equal pair makes the difference empty and the term passes
  today — and kept as a regression guard. rev-2 added "and says so", which has no producer: the term's
  success path is a bare return and its message variable is assigned only on failing branches.
- **AC5** — When a pair's markers are duplicated, `roster_ids` exits non-zero rather than returning the
  ids printed before the refusal. Observed RED first: at BASE it returns a partial list and status 0.
- **AC6** — When a build README carries a well-formed but EMPTY pair, the leg exits 0 and
  `build-complete` term 3 passes: the build plans exactly its specced units. §5 declares this legal and
  the obvious `pipefail` implementation of S5 refuses it, so this criterion is the guard against the
  fix breaking the case it was not about.
- **AC7** — When the migration is re-run, `git diff` shows every migrated pair's ids equal to that
  build's tracked spec ids, across the whole DERIVED set. The set is computed by the migration, not
  read from this document.
- **AC8** — When `memory/backlog/TOOL.md` is read at HEAD, `TOOL-aPacedTurnstile-14` is CLOSED and
  names this unit.
- **AC9** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, the bar is
  green and the slot leg's summary line PRINTS A DERIVED PAIR COUNT alongside the tracked-README count
  it already prints. The requirement is that the number is derived and shown, not that the two agree:
  once S1's refusal exists a disagreement reds the leg before any summary prints, so rev-2's
  "asserts that number and the pair count agree" was a tautology dressed as the cure for the
  count-in-prose finding.
- **AC10** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both
  totals are recorded in the commit message and `.memory-tree.conf` carries this unit's own movement
  line, per S11.

## 7. Gates

**Declared skip, with its compensating check.** S5's and S10's driver arms live in
`tools/unattended/unattended.test.sh`, and NO command this spec names runs that file: the kit gate
skips `*.test.sh` outright, the kit's test legs are absent from `tools/gate-legs.json`, and a standing
owner instruction of 2026-08-23 forbids running those suites. Round 1 exonerated this unit on that
finding because rev-1 named no test file; rev-2 created the dependency and declared nothing. The
compensating check is unit 4's: each arm observed RED against a staged break at authoring time, with
the staged diff recorded in this unit's build record, and the owner handed
`bash tools/unattended/run-unattended-gates.sh` rather than `--selftests` being added below.

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
- rev-3 · 2026-08-25 · round-2 fold. Fixed §4's commit ORDER, which rev-1 and rev-2 both stated
  backwards in the sentence before stating it forwards. Deleted the non-goal that survived ruling 1's
  withdrawal under a new name and contradicted S1 and S6. Rewrote S5 after round 2 established the fix
  reached no consumer — no caller tests `roster_ids`' status, the pipeline ends in `sort` and not
  `grep`, and the obvious `pipefail` remedy refuses the legal EMPTY pair, now pinned by AC6. Rewrote S7
  against the code that is actually there: one guard of the quoted shape, in `missing_units`, and two
  of a different shape in `roster_ids`. Replaced the degenerate-pair list with a derivation after round
  2 found it wrong in both directions. Split AC2's incompatible halves, marked AC4 green at BASE and
  dropped its unproducible clause, de-tautologised AC8, took the read-path charge as declared scope
  (S11), and added the declared skip with its compensating check for arms no named command can run.
  AC numbering was RESEQUENCED in this revision; AC labels in the entries below refer to the
  numbering of the revision that wrote them, not to this one.

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
