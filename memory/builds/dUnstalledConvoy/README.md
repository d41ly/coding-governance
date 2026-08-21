---
slug: dUnstalledConvoy
node: d
opened: 2026-08-20
streams: tooling+playbook
roster: TOOL+PLAY
ids: PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 TOOL-dUnstalledConvoy-13 TOOL-dUnstalledConvoy-14 TOOL-dUnstalledConvoy-15 TOOL-dUnstalledConvoy-16 TOOL-dUnstalledConvoy-17 TOOL-dUnstalledConvoy-18 TOOL-dUnstalledConvoy-19
---

# dUnstalledConvoy — an unattended run may change its own scope, dispatch disjoint work concurrently, evidence what it built, and reach a terminal state it can actually get to

Node `d` · opened 2026-08-20 · streams tooling+playbook.

The owner reports four breaking issues in both unattended build modes. Each was verified against
source before a line of this file was written, and each is stronger than reported: **every one of the
five ABORTED runs in this tree aborted for exactly these causes.** The abort reasons are quoted per
defect below and are the primary evidence for this build.

## Measured at BASE `2dc9df35`

| Quantity | Value | Where |
|---|---|---|
| run-state files in the tree | 13 | `memory/builds/*/RUN.md` |
| of those, `ABORTED` | 5 | 38 per cent |
| aborts caused by the four defects below | **5 of 5** | quoted in each section |
| `READ_PATH_CEILING` margin | 7 152 B of 112 987 | `corpus_ids.py --report` |
| `BUILD-METHOD.md` margin | 1 961 B and **7 lines** of 22 528 / 290 | `wc` against M1's stated budget |
| template margin | 989 B of 49 152 | `check-template-size.sh` |

**The line margin is the binding constraint, not the byte margin.** Four of the six read-path files
are in this build's write set, and `BUILD-METHOD.md` has seven lines of headroom while two units edit
it. Every unit that touches a budgeted carrier RE-MEASURES from the gate and never carries a number
out of this file. A unit that does not fit raises a fork rather than editing the constant — M1's
budget is a stated constraint of a governance carrier, and M3 veto 2 makes changing one an owner turn.

## Defect A — a run may not rescope, so it parks and stalls

`BUILD-METHOD.md` M3 states it outright: a fork whose options differ in what gets built "is not
yours — park it." M2's classification loop has four actions and none of them retires a unit.

> `dClosedLexicon` · **REFUSED TO DECIDE: whether to ship P3 weakened, cut it from the ratified
> scope, or land the sound remainder** — all three are scope calls the standing mandate does not
> delegate. Nothing merged, nothing pushed.

> `aWalkedCorpus` · Raising another build's shrink-only pin **is a SCOPE decision a standing mandate
> does not delegate**, so it is parked rather than absorbed.

> `cBriefedPilot` · WHAT I REFUSED TO DECIDE: **whether 16 of 22 units is a landable build. That is a
> scope decision, reserved to the owner by M3 and not delegated by a standing mandate.** The branch is
> green and needs one command to merge if the owner agrees.

That third one is the sharpest case in the corpus. The bar was GREEN on every leg of a full run, the
work was complete enough to land, and the run stopped because the method gave it no way to say so.

**The mechanism already exists and is legal.** `WONTDO` is terminal for the `build-complete` DoD
item, and `check_authorization`'s roster test compares the BASE and HEAD unit-ID sets as a SUBSET —
**additions are admitted and removals are refused.** So retiring a unit by status flip is legal,
superseding it by adding a replacement id is legal, and deleting an id is structurally refused.
Nothing tells a run any of that. Units 4, 5 and 6 supply the authority, the verb and the check.

## Defect B — the parallelism directive names the opposite of its own handle

`parallel-when-disjoint` points at M6, whose first sentence is "Sequence is the default; parallelism
is a claim you substantiate." The handle appears in exactly two places in the tree, a Skill table row
and a driver constant, and nothing enforces it.

The prior verdict `parallelism route: none` is weaker than it reads. Its own record says R2, the
`Workflow` sidechain, **cleared E1 and E2 and failed on E3 and E4 — both recorded as NEVER RUN**, and
that R5, one worktree per pass, was measured viable. The record closes: "someone re-opening this
needs to know the gap is unmeasured evidence, not adverse evidence." A live backlog row says the
routes are re-openable on exactly that evidence. M4 already mandates `Workflow` dispatch for spec
audits, so the route is in daily use in this repo.

**A live, uncovered drift is load-bearing here.** `AGENTS.md` and
`coding-governance-agents.template.md` both still assert that orchestration sidechains inherit
"neither your hooks nor the governing doc". Measured on the day the routes were hunted, both halves
are FALSE — the probe's first message carried the whole governing doc, and a `SubagentStart` hook
fired and was obeyed. `REVIEW-PROTOCOL.md` was corrected; the charter and the SHIPPED PRODUCT
TEMPLATE were not, so every adopter receives the refuted sentence. No backlog row covers it. This is
the repo's own `two-answers-to-one-question` class, and the sentence is the one that blocked the
parallelism inversion in the first place.

The conclusion that sentence supports happens to survive for a DIFFERENT reason — a sidechain agent
holds no `Agent` tool at all, so it cannot fan out — and unit 9 must preserve the conclusion while
deleting the false premise. A correction that also flips the conclusion would be wrong.

## Defect C — nothing observes whether a build followed its specs

Specs number their scope and their acceptance criteria. Nothing joins a built unit back to those
numbers. `build-complete` reads terminal STATUS only. `closing-review-recorded` is explicit in the
protocol that it "measures that a review of what shipped exists and is bound to THIS run, never what
the review concluded." So conformance is unobservable, exactly as reported.

M2 already carries the rule — "READY → build what it says; to diverge, change the spec first" — and
it is unenforced. Units 12 and 13 make divergence visible rather than trusted.

## Defect D — LANDED is unreachable, and a run parked before it blocks the whole fleet

Three checks, each correct on its own, compose into a deadlock recorded as an OPEN backlog row that
**no spec in this tree targets**.

The root cause is one line: `PHASES_TERMINAL="LANDED ABORTED"`. **`LANDING` is not terminal**, so a
run that reaches it and cannot push stays live forever, and leg check 7's `nlive <= 1` counts it
against every later run on the fleet.

> `aBoundedVerdict` · gates-green is unreachable and the fix is outside this mandate: another run
> **is live at LANDING, LANDING is not terminal, and check 7 counts it against every later run.**

> `aMeteredTurnstile` · **The work is merged to LOCAL main and is complete; only the push to shared
> main is blocked**, and the machine is what blocks it.

The second abort reached the owner's proposed remedy empirically before it was proposed.

## Owner decisions — RESOLVED 2026-08-20

Put to the owner at kickoff with the evidence above, and answered before any spec was written. Two
answers OVERRIDE the recommendation that was put beside them; both are recorded as the owner's, with
the cost the recommendation was protecting against stated in the unit that owns it.

| Fork | Resolution |
|---|---|
| D — how a locally-merged build reaches a terminal state | **RELAX `LANDED` to accept a local-main witness.** The recommendation was a separate terminal phase preserving `LANDED` as the remote-observed claim; the owner chose the simpler vocabulary. Unit 1 states the cost. |
| A — how much scope authority a mandate delegates | **FULL delegation inside the build's stated goal**, including adding units. The recommendation was retire-and-supersede without widening. Unit 4 states what this removes from M3 veto 2. |
| B — the parallelism default | **Measure E3 and E4 first, then invert M6** on the result. Refuses to ship on argument where the original refusal refused to ship on measurement. Unit 8 is CONDITIONAL on unit 7's verdict. |
| C — where the fidelity record binds | **A hygiene check over an acceptance ledger.** Not a DoD item: a ninth blocking item is one more way for a finished build to wedge, which is the defect class this build exists to remove. |

## Build-level rules

- **Every unit touching a budgeted carrier re-measures from its gate.** The three margins above are
  measurements at BASE, not allowances. `BUILD-METHOD.md`'s SEVEN-line headroom binds units 4 and 8,
  which both edit it; if the pair does not fit, that is a fork, not an edit to M1.
- **A new CHECK inside an existing gate, never a new gate LEG.** Units 6, 11 and 13 each add a check.
  Adding a LEG trips a growing set of meta-gates and costs the leg manifest, a kit descriptor row and
  a coverage assert; adding a check inside an existing gate costs an `ARMS_FLOORS` bump and one arm
  per `fail` call site. This is a recorded trap in the kickoff manifest, not a preference.
- **A kit-shipped document and this repo's installed copy are ONE mechanism.** Any unit whose
  Files-touched names a kit template moves that template's render in the SAME commit. The
  enumeration this rule used to carry named four units and the tables name six, which is a derived
  count written in prose beside the thing it counts — the class this repo gates against elsewhere.
  Each unit's own table is the operative list. Note the two pairs are graded by DIFFERENT mechanisms:
  the protocol pair by the kit gate's single byte comparison, the Skill pair by re-running the
  adopter's check mode, because the Skill render carries interpolated tokens and can never be
  byte-identical to its template. Review fold: L2, H13.
- **Every new check gets its failing case OBSERVED before it lands** — stage the break, confirm RED,
  unstage. Three of this build's checks grade records the RUN ITSELF writes, so each owes an explicit
  statement of what it cannot buy in its own header — and that statement is a SCOPE item, so every
  unit carrying one also carries a criterion that greps for it. A build-level rule nothing observes is
  the same defect one level up. Review fold: L1.
- **`.memory-tree.conf` is a BUILD-WIDE shared write, and it makes seven units mutually non-disjoint.**
  Every unit that adds a `fail` call site moves that file's `ARMS_FLOORS` entry, and two units add a
  cutoff key beside it. Seven of the thirteen therefore write one line-range of one file. They may
  NEVER be dispatched as a concurrent pair, and each one's Files-touched table names the conf
  explicitly rather than hiding the edit inside a test-file row. This is the build's own answer to the
  rule units 10 and 11 are building. Review fold: M7.
- **The leg output contract is owned by ONE unit, and it is `TOOL-dUnstalledConvoy-6`.** Four units
  specify a check that prints an announced skip line and still exits 0, while the leg's header states
  `Exit 0 + no output = clean` and its selftest hard-asserts empty output three times. Under the order
  below unit 6 lands first among them, so it owns amending the contract and its green-control arms in
  the same commit as the first skip line. The other three cite it and specify no contract change of
  their own. Owner decision, 2026-08-20. Review fold: H1.
- **No spec id in this build may be cited from product source while its status is non-terminal.** The
  drift signal reads `1 of 25` against a pin of 2, so one slot is free and a second citation reds it.

## The order is TOTAL

**REORDERED 2026-08-20 on the spec audit, by owner decision.** The first draft put the rescope chain
seventh, eighth and ninth. Five confirmed defects were one shape — a unit obliged to use a mechanism a
LATER unit builds — and the audit's cheapest single fix was to move that chain to the front. It closes
H14 and M11 outright and defuses M6. The prior order is not reconstructed here; git carries it.

| # | Unit | Why here |
|---|---|---|
| 1 | `PLAY-dUnstalledConvoy-1` | deletes a false sentence every later unit's agents read, and depends on nothing |
| 2 | `TOOL-dUnstalledConvoy-4` | the scope authority — every later unit that amends anything needs it to exist |
| 3 | `TOOL-dUnstalledConvoy-5` | the `--rescope` verb the authority points at |
| 4 | `TOOL-dUnstalledConvoy-6` | the roster check, and the unit that owns the leg output contract |
| 5 | `TOOL-dUnstalledConvoy-7` | the E3/E4 measurement |
| 6 | `TOOL-dUnstalledConvoy-9` | the dispatch verb — moved AHEAD of the inversion so its pointer is live on arrival |
| 7 | `TOOL-dUnstalledConvoy-8` | the M6 inversion, CONDITIONAL on unit 5 of this order |
| 8 | `TOOL-dUnstalledConvoy-10` | the dispatch check |
| 9 | `TOOL-dUnstalledConvoy-3` | the landing contract |
| 10 | `TOOL-dUnstalledConvoy-1` | `verb_landed` |
| 11 | `TOOL-dUnstalledConvoy-2` | check 15, the second opinion |
| 12 | `TOOL-dUnstalledConvoy-11` | the ledger grammar |
| 13 | `TOOL-dUnstalledConvoy-12` | the ledger check, and the LAST commit carries the kit-version bump |

Three orderings are load-bearing rather than tidy. The authority and the verb precede everything that
records an amendment, because at any earlier position M3 still says a scope fork is not yours and the
verb does not exist — the exact stall three aborted runs recorded. The dispatch verb precedes the M6
inversion, because the inversion's rule points at that verb and would otherwise ship inert with a dead
pointer for several passes while M7 makes every run re-read it. And the kit-version bump rides the
LAST commit of the ledger pair, because `verdict epoch` refuses a bump that is an ancestor of the
engine edit it dates. Review fold: H14, H12, M6, M11.

`TOOL-dUnstalledConvoy-8` is CONDITIONAL: if the measurement records E3 or E4 as anything other than
CLEARED, it does not ship an inversion, and the build records the loss per M12 rather than shipping
the rule anyway. The owner's answer authorized the inversion ON the measurement, not instead of it.

## Units — the authored roster (M2)

One mechanism per unit. Each cell is a label; the unit's `§1` Goal owns the statement.

<!-- roster:units -->
| Unit | Tier | Mechanism |
|---|---|---|
| `TOOL-dUnstalledConvoy-1` | 2 | `verb_landed` accepts a local-main witness and records which kind it took |
| `TOOL-dUnstalledConvoy-2` | 2 | leg check 15 grades both witness kinds instead of assuming a remote ancestor |
| `TOOL-dUnstalledConvoy-3` | 2 | the protocol and Skill state the relaxed terminal and what it costs |
| `TOOL-dUnstalledConvoy-4` | 2 | M2 and M3 gain the amendment vocabulary and the delegated scope authority |
| `TOOL-dUnstalledConvoy-5` | 2 | the `--rescope` verb records an amendment in the run-state file |
| `TOOL-dUnstalledConvoy-6` | 2 | the leg refuses a roster change with no rescope record behind it |
| `TOOL-dUnstalledConvoy-7` | 2 | E3 and E4 are measured, and the verdict is recorded with its losses |
| `TOOL-dUnstalledConvoy-8` | 2 | M6's default inverts to parallel-on-proof, conditional on unit 7 |
| `PLAY-dUnstalledConvoy-1` | 2 | the charter and the shipped template drop the refuted sidechain premise |
| `TOOL-dUnstalledConvoy-9` | 2 | the driver records a dispatch's declared write sets |
| `TOOL-dUnstalledConvoy-10` | 2 | the leg compares declared write sets against the paths the commits touched |
| `TOOL-dUnstalledConvoy-11` | 2 | the acceptance-ledger record grammar |
| `TOOL-dUnstalledConvoy-12` | 2 | a hygiene check asserting every AC of a CLOSED spec is evidenced |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 13 unit(s) · node d · opened 2026-08-20 · streams tooling+playbook
ids PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11
ids TOOL-dUnstalledConvoy-12 TOOL-dUnstalledConvoy-13 TOOL-dUnstalledConvoy-14 TOOL-dUnstalledConvoy-15 TOOL-dUnstalledConvoy-16 TOOL-dUnstalledConvoy-17 TOOL-dUnstalledConvoy-18 TOOL-dUnstalledConvoy-19

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [PLAY-dUnstalledConvoy-1 — the charter drops a refuted premise while keeping the conclusion it happened to support](spec/2026-08-20-spec-PLAY-dUnstalledConvoy-1.md) | CLOSED | rev-2 | 2026-08-20 |
| [TOOL-dUnstalledConvoy-1 — `verb_landed` accepts a local-main witness, and records which kind it took](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-1.md) | CLOSED | rev-3 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-10 — the leg compares a declared write set against the paths the pass actually committed](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-10.md) | CLOSED | rev-5 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-11 — a journal record gains an acceptance ledger, so a built unit says which criterion each observation satisfied](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-11.md) | CLOSED | rev-3 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-12 — a hygiene check asserts every acceptance criterion of a closed unit is evidenced or amended](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-12.md) | CLOSED | rev-3 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-2 — leg check 15 grades both witness kinds, and announces the case it cannot reach](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-2.md) | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-3 — the contract states the relaxed terminal, its two anchors, and what the weaker one cannot buy](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-3.md) | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-4 — M2 and M3 gain the amendment vocabulary, and a mandate delegates scope inside the build's stated goal](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-4.md) | CLOSED | rev-3 | 2026-08-20 |
| [TOOL-dUnstalledConvoy-5 — the `--rescope` verb records an amendment, and records it as a declaration rather than a summary](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-5.md) | CLOSED | rev-5 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-6 — the leg refuses a roster amendment with no record behind it, and announces the case it cannot compare](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-6.md) | CLOSED | rev-3 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-7 — E3 and E4 are measured, and the verdict is recorded with the test that would have lost](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-7.md) | CLOSED | rev-3 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-8 — M6's default inverts to parallel-on-proof, and the directive stops naming the opposite of its own handle](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-8.md) | CLOSED | rev-3 | 2026-08-21 |
| [TOOL-dUnstalledConvoy-9 — the driver records a dispatch's declared write sets, and refuses the two disjointness conditions a machine can decide](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-9.md) | CLOSED | rev-4 | 2026-08-21 |
<!-- /gen:build-units -->

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md](build/2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-11 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 |
| [2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md](build/2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md) | journal | TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 |
| [2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md](reviews/2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md) | spec-audit | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-20-spec-PLAY-dUnstalledConvoy-1.md](spec/2026-08-20-spec-PLAY-dUnstalledConvoy-1.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-1.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-1.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-10.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-10.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-11.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-11.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-12.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-12.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-2.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-2.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-3.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-3.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-4.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-4.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-5.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-5.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-6.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-6.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-7.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-7.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-8.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-8.md)
  - [2026-08-20-spec-TOOL-dUnstalledConvoy-9.md](spec/2026-08-20-spec-TOOL-dUnstalledConvoy-9.md)
- **`build/`**
  - [2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md](build/2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md)
  - [2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md](build/2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md)
- **`reviews/`**
  - [2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md](reviews/2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md)
<!-- /gen:build-docs -->
