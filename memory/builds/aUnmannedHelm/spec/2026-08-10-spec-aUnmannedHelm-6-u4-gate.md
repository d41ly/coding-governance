# TOOL-aUnmannedHelm-6 — the gate, and the three legs that carry it

**Status:** INPROGRESS · rev-2 · 2026-08-10 · node a · Tier-2 · base 20f8082e · streams tooling · ratified 2026-08-10 · review wf_077104e6

## 1. Goal

Make every claim units 2 and 3 make checkable on the merge bar. This is unit 4 of seven; the master
scope and the ratified decision menu live in this build's `README.md`.

Until this unit lands, the phase vocabulary, the Definition-of-Done core set and the kit/dogfood
parity of the protocol pair are enforced by prose alone. The dossier says so in its `Gaps`, which is
the honest form of the hole and not a substitute for closing it.

## 2. Scope (IN)

- **S1 · `tools/unattended/check-unattended.sh`**, the leg. Eleven checks over the tree, each with
  its own named refusal.
- **S2 · witness PRESENCE as its own `fail` branch**, separate from witness resolution, with its own
  arm. The drift oracle's judgeability discipline is reused for resolution and deliberately not for
  presence.
- **S3 · the at-most-one-live invariant**, so "the run" is well-defined for anything keying on it.
- **S4 · the two-granularity population guard**, in the engine's OWN shape: red only when the
  precondition is non-zero and the population is empty; silent on the all-zero young tree.
- **S5 · a shrink-only COUNT floor on the kit's core sets** (`CORE_FLOOR`), plus the independent
  assertion that every TERMINAL phase is in the vocabulary. A project may extend both sets and can
  reach neither number. Restated at rev-2 — the membership form this said at rev-1 was measured
  unfailable; see §4.
- **S6 · the kit/dogfood parity of the protocol pair**, one pair, with the same normalisation the
  memory-tree harness uses and for the reason unit 2 recorded.
- **S7 · THREE `gate-legs.json` entries** — the gate, its sibling test, and unit 3's driver test —
  each cited by path in the charter's gate-suite list.
- **S8 · `tools/unattended/check-unattended.test.sh`**, arming every branch positively.

## 3. Non-goals (OUT)

- **The adopter `--check` and the adopter e2e.** Unit 7's, and two further legs. The review's budget
  of four is met across the two units, plus the driver test, for five.
- **Re-deriving the unit table.** The leg COMPARES the run-state file's generated region against the
  build README's slice. It does not render either.
- **Checking the freshness of the README's own slice.** The memory-tree gate's check 9 owns that,
  and duplicating it would be a second answer to a question that already has one.
- **Judging whether the owner MEANT the mandate.** Unreachable. The leg checks reachability and
  shape, which is what unit 2 says is checkable.
- **Any agent-cap edit.** `TOOL-aNumeralWarden-1`'s.

## 4. Design

### The eleven checks

| # | Asserts | Why it is not covered by another leg |
|---|---|---|
| 1 | `.unattended.conf` exists and every required key is declared | nothing else reads the file |
| 2 | the vocabulary is non-empty, the CORE count is at or above its floor, and every TERMINAL phase is in it | an empty vocabulary makes every phase check vacuously true |
| 3 | the DoD set is non-empty and the CORE count is at or above its floor | deleting an item is otherwise a silent, reason-free override |
| 4 | every run-state file's phase is IN the declared vocabulary | unit 1 deliberately kept the file out of check 8, so this is the only place |
| 5 | every phase claim carries a witness — PRESENCE | absence is otherwise the cheapest way to say nothing |
| 6 | a present witness RESOLVES, or is skipped as unjudgeable | the drift oracle's discipline, reused only here |
| 7 | at most one run-state file is non-terminal | "the run" must be well-defined |
| 8 | each run-state file's generated region equals its README's slice | the copy could go stale against its source |
| 9 | each recorded BASE equals the merge-base git reproduces | a recorded BASE the run could quietly move is not a pin |
| 10 | the shipped protocol equals the installed copy, modulo the install prefix | a kit ships what a repo runs, or it ships drift |
| 11 | no run-state file contains the declared bypass flag | the landing rule, checked where the record is |

Check 6 is the only one allowed to be silent on missing data, and only because check 5 has already
refused it. That ordering is the whole reason presence is its own branch.

### The population guard, in the engine's own shape

Two granularities, never one:

- **PRECONDITION** — does a file named `RUN.md` exist ANYWHERE under the memory root?
- **POPULATION** — does one exist at the exact path the leg selects, `<M>/builds/<slug>/RUN.md`?

Equal-and-zero is a young tree and is SILENT: a repo with no unattended run yet is not a violation,
and a guard that cannot tell that from a mis-segmented selector makes every fresh adopter red on
install. Precondition non-zero with an empty population is the mis-segmentation, and that reds.

This is not a paraphrase of the memory-tree guard, it is the same contract stated for a different
selector, and the recorded reason is that the first draft of that guard did exactly the inverse and
redded a freshly scaffolded tree.

### The core-set floor is a COUNT, because membership could not fail

The kit's core sets live in ONE place — the driver's `PHASES_CORE` and `DOD_CORE` — and the leg reads
them from there rather than restating them. A second spelling would be the drift the check exists to
catch, one file away from the thing it checks.

That single-sourcing is also what made the obvious assertion vacuous. The leg composes the effective
set as core plus the project's extras, so core is a subset BY CONSTRUCTION and "every core member is
present" can never fire. Written at rev-1, armed cleanly, tested nothing. It was caught the only way
it could be: by writing the red fixture and watching it stay green.

What is pinned instead is a shrink-only COUNT — `CORE_FLOOR="<phases>:<dod>"` in `.unattended.conf`,
the shape `ARMS_FLOORS` and `baseline.toml` already use. The NAMES stay in the driver; the number is
what the gate holds. Deleting a core member drops the count below the floor and reds; adding one is
free; raising the floor is a deliberate edit that says why. An UNDECLARED floor is its own refusal,
because omitting the key is the quietest way to disarm a shrink-only pin.

Alongside it, one genuine membership assertion: every TERMINAL phase must be in the effective
vocabulary. Those two sets are declared independently, so that check has something to disagree
about — which is exactly what the subset form did not.

### The three legs, and why the sibling tests are legs

This repo runs no sibling test that is not its own leg, and the charter records why: a Tier-2 review
found four of seven defects, including a blocker, in the one file no leg executed. So the driver's
test and the gate's test are legs, not files someone remembers to run.

Each leg is cited by path in the charter's gate-suite list, because the drift signal
`_charter_mentions_every_leg` measures exactly that and an uncited new leg moves it.

### Files touched

New: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`. Edited:
`tools/gate-legs.json` (three entries), `AGENTS.md` (the gate-suite citations), `.memory-tree.conf`
(the new gate's `ARMS_FLOORS` row), `memory/map/features/unattended.md` (the `gate-legs` claim its
`Gaps` currently declares empty).

### Alternatives rejected

- **One leg running everything.** The sibling tests would then be invoked by a leg rather than being
  legs, which is the shape the charter records as having hidden a blocker.
- **Restating the core sets in the leg.** Two spellings of one declaration, one file apart — and
  the reason the count floor is a count rather than a list.
- **Asserting core ⊆ effective.** Unfailable: the leg composes the effective set FROM core. Measured.
- **A population guard keyed on the population alone.** Silent on a young tree AND on a
  mis-segmented selector, which is the state that cannot be diagnosed.
- **Folding witness presence into resolution.** Measured on the oracle it would have reused: a claim
  with no sha of its own is counted unjudgeable and skipped, so the fold makes the check unfailable
  in exactly the case it exists for.

## 5. Production-readiness checklist

- **security** — read-only. The leg writes nothing, which is what lets it run on the bar.
- **perf / scale** — one pass over the tracked run-state files (currently at most one), plus one
  byte comparison. Against the 239 s bar this is noise.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — the young tree is the defined empty and is silent; an empty
  declaration is a refusal.
- **observability** — every refusal names itself and the file it is about.
- **risks** — the dominant one is a check that cannot fail. Every branch gets a red fixture AND a
  green control, because silence proves nothing on its own.
- **testing + left-shift gates** — a positive arm per branch, plus both population-guard states.
- **migration / rollback** — additive; the legs are new.
- **user docs** — the protocol already states every rule this leg enforces; the leg adds no second
  description of them.

## 6. Acceptance criteria

- **AC1** — With a core phase member deleted FROM THE DRIVER, check 2 reds naming the count and its
  floor; with a project member ADDED via the conf, it is green. Both observed. Same for a core DoD
  item and check 3. With `CORE_FLOOR` undeclared, check 1 reds — an absent pin is not a passed one.
- **AC2** — With a run-state file whose phase is outside the declared vocabulary, check 4 reds naming
  the token; with a legal phase it is silent. Both observed.
- **AC3** — With a phase claim carrying no witness, check 5 reds; with an unresolvable witness,
  check 6 reds; with a resolving witness both are silent. All three observed, and check 5's fixture
  proves check 6 is not what fired.
- **AC4** — With two non-terminal run-state files, check 7 reds naming both; with one, silent. Both
  observed.
- **AC5** — With the generated region edited away from the README's slice, check 8 reds; re-copying
  clears it. With the recorded BASE edited, check 9 reds naming the merge-base it expected. All
  observed.
- **AC6** — With the shipped protocol edited, check 10 reds and prints the diff; re-rendering clears
  it. Both observed.
- **AC7** — On a tree with a `RUN.md` under the memory root but NOT at the selected path, the
  population guard reds naming mis-segmentation. On a tree with no `RUN.md` anywhere, every check is
  silent and the leg exits 0. Both observed — the second is the arm whose absence made the
  equivalent guard red a freshly scaffolded repo.
- **AC8** — `bash tools/run-gates.sh` runs all three new legs, and the charter cites each by path.
  Observed by the run-gates canary and by grep.

## 7. Gates

The standing bar. Newly relevant: the run-gates canary (`tools/run-gates.test.sh`), which asserts
the legs are single-sourced from the manifest and that the runner hardcodes none; `check-arms.py`,
which discovers the new gate; and the drift-audit records leg, whose
`handkept_inventories_disagreeing_with_source` signal reads the charter's leg citations.

**Build-wide constraint this unit inherits:** `non_terminal_specs_cited_by_product_source` measures
2 against a pin of 2, zero headroom.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as unit 4 of seven, carrying the four obligations the Tier-2
  review pinned on it: three manifest entries rather than one, witness presence as its own `fail`
  branch, the at-most-one-live invariant, and the population guard in the engine's own
  two-granularity shape rather than the inverted one the master spec carried at rev-2.
- rev-2 · 2026-08-10 · BUILT on the unit branch, unmerged. 22 branches, all 22 armed; 42 assertions;
  three legs registered and cited in the charter; `ARMS_FLOORS` gains `22:22`.

  **S5 changed shape, because the specced form was a check that cannot fail.** The spec said "every
  CORE member must be present in the effective set". The leg COMPOSES the effective set as core plus
  the project's extras, so core is a subset by construction and the assertion can never fire — the
  vacuous-selector class one level up, written into a spec whose §5 names that exact risk. It was
  caught the only way it could be: by writing the red fixture and watching it stay green.

  The replacement is a shrink-only COUNT (`CORE_FLOOR` in `.unattended.conf`, `6:6`), the shape
  `ARMS_FLOORS` and `baseline.toml` already use. The member NAMES still live only in the driver, so
  there is no second spelling; what is pinned is how many there are. Deleting a core member drops the
  count and reds; adding one is free; raising the floor is a deliberate edit. The project layer can
  reach neither number, which is the property F3 asked for and the subset form never had.

  Added alongside it, and falsifiable where the subset check was not: every TERMINAL phase must be in
  the effective vocabulary. Those two sets are declared independently, so the check has something to
  disagree about. Also added: an undeclared `CORE_FLOOR` is its own refusal — omitting the key is the
  quietest way to disarm a shrink-only pin.

## 10. Reuse audit

The seams this unit wires through rather than reinvents:

- `tools/memory-tree/check-memory-hygiene.sh` `pop_guard` — the two-granularity contract, restated
  for this leg's selector and NOT re-implemented as a one-granularity check.
- `tools/unattended/unattended.sh` `PHASES_CORE` / `DOD_CORE` — the single source of the kit's core
  sets; the leg reads them from the driver rather than carrying a second spelling.
- `tools/memory-tree/kit-dogfood-parity.test.sh` — the normalisation discipline for the protocol
  pair, bounded to one pair for the standalone-install reason unit 2 recorded.
- `tools/drift-audit/drift_report.py` — the judgeability discipline, for witness RESOLUTION only.
- `tools/gate-legs.json` + `tools/run-gates.sh` — the single-sourced leg manifest; the runner is not
  edited, only the manifest.
- `tools/memory-tree/check-arms.py` — discovers the new gate automatically via the `fail` helper,
  which is why the sibling test is written before the leg is registered rather than after.
