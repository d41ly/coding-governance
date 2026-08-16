---
slug: cBriefedPilot
node: c
opened: 2026-08-14
streams: tooling+playbook
roster: TOOL
ids: TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 TOOL-cBriefedPilot-23 TOOL-cBriefedPilot-24 TOOL-cBriefedPilot-25 TOOL-cBriefedPilot-26 TOOL-cBriefedPilot-27 TOOL-cBriefedPilot-28 TOOL-cBriefedPilot-29 TOOL-cBriefedPilot-30 TOOL-cBriefedPilot-31 TOOL-cBriefedPilot-32 TOOL-cBriefedPilot-34 TOOL-cBriefedPilot-35 TOOL-cBriefedPilot-36
---

# cBriefedPilot — the instructions an unattended build runs on, made default and waivable

Node `c` · opened 2026-08-14 · streams tooling and playbook.

An unattended run is started with one chat command and then executes with nobody reading it. What it
executes *with* is one soft conditional sentence. The Skill's step 0 says "Read the build method
first, **if** this project ships one"; that pointer is the only link between `/unattended <slug>` and
any instruction about the work. The Skill says "spec" twice, both inside `--plan`'s blurb, and never
tells the agent to read a spec or to read the build README's content at all.

The instructions themselves are not missing. `memory/guides/BUILD-METHOD.md` carries all of them, and
the owner's eight stated defaults map onto sections that already exist — the wrap-up ask is M9 almost
word for word. What is missing is that nothing makes them DEFAULT, nothing makes them WAIVABLE, and
nothing observes whether a run followed them.

This build installs a directive layer: eleven named handles, each a POINTER into a build-method
section rather than a second copy of its rule, kit-owned and shrink-only, waivable only at preflight
by a named and reasoned owner turn that is recorded and surfaced.

This README is the **master overview and the owner decision menu**, per `memory/TEMPLATE-SPEC.md`.
Each unit below becomes its own conforming sub-spec under `spec/`.

## Start here

**State.** DESIGNED, not built. One design pass ran as a nine-agent panel — three independent
candidates, one judge synthesis, four adversarial lenses, one folding pass. It returned 51 raw
findings; 47 folded into the design, 4 were rejected on measured evidence, and 5 became the owner
questions below. Three of the four lenses returned BLOCKED before folding. The recording is
`build/2026-08-14-build-cBriefedPilot-1-design-pass.md`.

**Classification (M2), RE-DERIVED against the tree 2026-08-15.** All 22 units now carry a conforming
spec. Twenty classify READY. Unit 5 is FORKED and its fork is PARKED — freezing the anchor triple
with the base is scope and touches a governance carrier, neither of which a standing mandate
delegates. Unit 15 is FORKED and correctly so: its resolver is unit 21's verdict token, which the
hunt has not produced yet. The earlier reading of this block — four specced, eighteen MISSING — was
true when it was written and is kept nowhere, because a classification that has gone stale is worse
than one that was never written.

**All five owner decisions are RESOLVED**, answered 2026-08-14 and recorded below with their
reasoning. Two of the answers grew the roster from twenty units to twenty-two: P2 refused to let D6's
inversion ship on an excusing clause and bought a research unit instead, and P5 pulled the
protocol-table join into scope. One answer moved unit 13 from Tier 1 to Tier 2.

**Next action.** Build unit 1, then unit 21. Unit 1 is the paired accumulator every later flag
depends on; unit 21 is the research that decides whether D6 can be built at all, and it is the only
unit in the build whose write set lets it run alongside the rest. The M4 spec audit is recorded at
`reviews/2026-08-15-review-cBriefedPilot-1.md` — CLEAN WITH FIXES, no blockers, all fixes folded.

**The one thing that must not be lost.** Every directive is a POINTER. `BUILD-METHOD.md` M1 states
that nothing in it is stated anywhere else in this repo, and that a rule appearing both there and in
a carrier it points at is a defect in the method. A registry that restated the eleven rules would be
that defect, and the repo's own bug-class checklist selected `two-answers-to-one-question` for
exactly these paths before the design started.

## What was found

Six findings, from a read of the whole chain from `/unattended <slug>` to landing.

| # | Finding | Unit |
|---|---|---|
| F1 | The Skill's only link to any work instruction is one soft conditional, and the Skill never says to read a spec or the README's content | 9 |
| F2 | `/session-kickoff` Step 5b is gated by leg check 12 and by two conf keys, and nothing ever invokes it from the unattended path — so kickoff-first deadlocks at the READY card and unattended-only leaves the gate guarding an untravelled road | 11, 14 |
| F3 | M2 names the README's authored Units table as the roster; `--plan` deliberately cannot parse it and says so; the Skill calls the README the authorization only | 6, 11 |
| F4 | No per-pass read budget exists — M7 re-reads a 16.5 KB method whole at every pass boundary, and M11's six further carriers have their scopes in a seventh file | 16 |
| F5 | Backlog row `TOOL-aStandingWrit-3` says the instruction layer is unowned; `aWrittenMethod` closed all six of its units and the layer exists | 20 |
| F6 | Three rendered `.claude/skills/*/SKILL.md` held CRLF against their `eol=lf` pin, redding the `memory-recall skill wiring` leg | FIXED 2026-08-14 |

F6 was scoped as a unit in an early draft and deleted: it is a one-command wiring repair with an
existing remedy, and giving it an id would have put a spec, a review and a gate around `--fix`. It
was repaired on 2026-08-14 with `bash tools/check-wiring.sh --fix`. Two things are worth keeping from
the repair. `git status` read CLEAN while the byte-comparing leg read RED, because git normalises
through the `eol=lf` pin on comparison and the leg's `diff` does not — which is the catalogued class
`gate-green-by-accident-on-generated-bytes` observed live. And a fresh `git checkout` of the same
paths yields LF, so the CRLF was an artifact of how this worktree was created rather than an ongoing
treadmill; the repair sticks.

## The design

### Eleven handles, not eight

The owner named eight directives. Eight is the right number of *instructions* and the wrong number of
*waiver handles*: the eighth bundles four obligations with four different hazard profiles — commit
every pass, land only when done, reconcile conflicts, derive the wrap-up — and a single handle would
make waiving "reconcile conflicts gracefully" also waive "commit every pass". The owner's eight
survive as a column in the Skill's table, so the mapping stays visible.

| Handle | Carrier | From |
|---|---|---|
| `minimal-prose` | M10 | D1 |
| `sub-specced` | M2 | D2 |
| `forks-resolved` | M3 | D3 |
| `specs-reviewed` | M4 | D4 |
| `reuse-first` | M5 | D5 |
| `parallel-when-disjoint` | M6 | D6 |
| `passes-committed` | M6 | D8 |
| `diff-reviewed` | M8 | D7 |
| `land-once-done` | M8 | D8 |
| `conflicts-reconciled` | M8 | D8 |
| `wrap-up-derived` | M9 | D8 |

The registry is a kit-owned `DIRECTIVES_CORE` constant in `unattended.sh`, read by the leg's existing
`core_of()` parser — the same shape `PHASES_CORE` and `DOD_CORE` already use. It is not a conf key,
because a project could then declare zero directives, which is a global waiver carrying no name, no
reason and no record. It is not a registry document, because a document is a spelling nothing parses
and whose absence reads as silence. `DIRECTIVES_EXTRA` is the project extension point;
`DIRECTIVES_FLOOR` pins the core count shrink-only.

### Three deltas — the rest are pointers

Nine of the eleven handles point at a rule that already exists and needs no edit. Three things are
genuinely new:

1. **M6's inversion DID NOT SHIP, and M6 is unchanged.** The intent was to invert "Sequence is the
   default; parallelism is a claim you substantiate" under a standing mandate, so that two passes
   meeting M6's three conditions were OWED concurrency. The owner refused at P2 to let that ship on a
   clause excusing it where no mechanism exists, and bought unit 21's hunt instead.

   Unit 21's verdict is `parallelism route: none`, recorded with per-route observations at
   `build/2026-08-15-build-cBriefedPilot-2-parallelism-routes.md`. Unit 15 read that token and took
   branch B: the finding ships, the rule does not. **D6 is the one owner directive this build does
   not deliver**, and saying so here is the point of the branch — a record that described an
   inversion nobody built would be worse than the gap itself.

   The nearest survivor is a `Workflow` sidechain with one worktree per pass. It fails the evidence
   standard on two criteria that were NEVER RUN rather than two that failed, which is a distinction
   the recording preserves for whoever re-opens it. And the hunt found that the claim BLOCKING it —
   `REVIEW-PROTOCOL.md` asserting a sidechain inherits no hooks and no `CLAUDE.md` — is measurably
   false in both halves. Correcting a binding document is not unit 21's to do, so that is the owner's.
2. **`build-complete`** — a new Definition-of-Done item. D8's "merge and push ONLY when the entire
   build is fully done" had no checker; `--close` would block on nothing.
3. **`closing-review-recorded`** — a new Definition-of-Done item, for D7. It joins on the run's
   pinned BASE, which is what stops a pre-existing record satisfying it.

The DoD core moves from six items to eight, so `CORE_FLOOR`'s DoD half moves 6 → 8.

### The waiver, end to end

```
/unattended <slug> --waive parallel-when-disjoint,land-once-done
  │
  ├─ step 0 · read BUILD-METHOD.md WHOLE — no longer conditional
  ├─ step A · THE LAST OWNER TURN. One AskUserQuestion batching the named handles.
  │            DEFAULT-DENY: a handle named but not confirmed with a reason is NOT waived.
  ├─ step B · schedule the keepalive
  ├─ step C · preflight, carrying the confirmed pairs:
  │            --preflight <slug> --keepalive-id <id> \
  │              --waive parallel-when-disjoint --reason "…" --waive land-once-done --reason "…"
  ├─ step D · if this project ships /session-kickoff, invoke it — AFTER preflight, never before
  └─ from here M10 binds: never ask.
```

**The ordering guarantee is one branch, not a convention.** `--waive` is accepted by `--preflight`
alone, and only while no run-state file exists OR the requested set equals the recorded one. That
single refusal makes every other verb reject a
late answer, and makes a re-preflight after compaction unable to change a recorded set. It is what
keeps the design from contradicting M10's "never ask": the owner turn happens before the run is
unattended, and afterwards there is no verb that could take one.

**A waiver removes the DIRECTIVE, never a GATE, and is never a DoD override.** Waiving
`land-once-done` still owes `--override build-complete --reason "…"` at close. That separation keeps
the non-overridable `authorization-reachable` rule out of the waiver route by construction.

**No eighth authored fact.** Protocol §2 pins the authored region at exactly seven facts. A waiver is
written by the existing `park()` with a fixed grammar and a new `waiver` kind, so §2's fact 3 gains a
fourth kind rather than the file gaining a field, and M9's existing `open / parked` row carries it to
the wrap-up unedited.

### What the gate can and cannot see

Stated here because an override budget must not be spent on something no machine could have checked.

| Kind | Handles |
|---|---|
| Machine-checked | the registry join, the waiver record's shape, the kickoff road's order |
| Internal consistency over run-written tokens | `build-complete`, `closing-review-recorded` |
| Observed by nothing | `minimal-prose`, `parallel-when-disjoint` |

The last row is the honest one. Neither is observable, and the classification table says so rather
than adding an attestation line the run ticks for itself.

## Units

The roster. This table is the roster, not the `ids:` key.

*The `State` column is gone deliberately. Option A of this unit's resolved fork: `check_authorization`
byte-compares the roster slice across the pinned BASE, so anything inside the markers that MOVES as
units land makes `authorization-reachable` unmeetable — and that item has no override. State is
already derived twice, by `gen:build-index` and by `--plan`.*

<!-- roster:units -->
| # | Unit | Tier | Mechanism | Depends on |
|---|---|---|---|---|
| 1 | `TOOL-cBriefedPilot-1` | 1 | one accumulator parses repeated flag/value/reason triples; `--override` becomes repeatable | — |
| 2 | `TOOL-cBriefedPilot-2` | 1 | the kit-owned `DIRECTIVES_CORE` of eleven pointer pairs | — |
| 3 | `TOOL-cBriefedPilot-3` | 2 | `--waive` at preflight: validated, parked, staged | 1, 2 |
| 4 | `TOOL-cBriefedPilot-4` | 1 | preflight refuses when the derived build-method carrier is absent | — |
| 5 | `TOOL-cBriefedPilot-5` | 1 | the recorded BASE is written once, not re-pinned per preflight | — |
| 6 | `TOOL-cBriefedPilot-6` | 2 | `--plan` sees a planned unit that has no spec | — |
| 7 | `TOOL-cBriefedPilot-7` | 2 | the `build-complete` Definition-of-Done item, over a roster marker now MANDATORY in an unattended build's README (P3) | 1, 6 |
| 8 | `TOOL-cBriefedPilot-8` | 2 | the `closing-review-recorded` Definition-of-Done item | 1, 5 |
| 9 | `TOOL-cBriefedPilot-9` | 1 | the Skill's directive table and its hard step 0 | 2 |
| 10 | `TOOL-cBriefedPilot-10` | 1 | the Skill's waiver turn — one AskUserQuestion, default-deny | 9 |
| 11 | `TOOL-cBriefedPilot-11` | 1 | the Skill's kickoff step and the README-as-roster read | 10 |
| 12 | `TOOL-cBriefedPilot-12` | 2 | leg check 16 — the registry join, both directions | 2, 9 |
| 13 | `TOOL-cBriefedPilot-13` | 2 | leg check 17 — a waiver line names a declared handle and a reason, AND is present in the FIRST committed blob of the run-state file | 3, 12 |
| 14 | `TOOL-cBriefedPilot-14` | 1 | leg check 18 — the Skill names kickoff AFTER preflight | 11 |
| 21 | `TOOL-cBriefedPilot-21` | 2 | the parallelism mechanism hunt — does ANY route dispatch a build pass concurrently without voiding the directive layer? | — |
| 15 | `TOOL-cBriefedPilot-15` | 2 | M6's parallelism inversion — shape decided by unit 21; if no route survives, this unit ships the finding instead of the inversion | 21 |
| 16 | `TOOL-cBriefedPilot-16` | 1 | the method's pointers name the new layer; M10's delta index count is unit 16 §8's fork, three or four depending on unit 15's branch | 15 |
| 17 | `TOOL-cBriefedPilot-17` | 1 | `check-kit-versions.sh` pairs the shipped protocol marker | — |
| 18 | `TOOL-cBriefedPilot-18` | 2 | the protocol pair gains §10 and the domain-rules enumeration | 3, 7, 8, 13, 16 |
| 22 | `TOOL-cBriefedPilot-22` | 1 | check 16 arm A's join extended to the protocol's own §3 phase list and §4 DoD table | 12, 18 |
| 23 | `TOOL-cBriefedPilot-23` | 2 | a shrink-only floor on each suite's EXECUTED assertion count, plus a `mutate` helper that refuses a fixture edit changing no bytes | — |
| 19 | `TOOL-cBriefedPilot-19` | 1 | the kit identifies as version 1.5 | 17, 18, 22 |
| 20 | `TOOL-cBriefedPilot-20` | 1 | the dossiers, the closed rows, the stale row F5 names | all |
<!-- /roster:units -->

*Units 21 and 22 are listed in BUILD order, not id order — 21 must precede 15 because it decides
15's shape, and 22 follows 18 because it joins against the tables 18 writes.*

**This build has no valid parallel pair, and that is M6's own answer rather than a concession.** Unit
19 writes `memory/backlog/TOOL.md`, named verbatim in condition (3); and any two units that close a
spec both re-render `memory/LIVE.md` and the build README's generated region — a generated index with
its generator, also condition (3) — and both touch the run-state file. **Unit 21 is the exception
worth noting: it writes nothing but its own recording, so it is the one unit that could run
concurrently with the 1–14 chain — which is a pleasing demonstration of the very rule it exists to
investigate.**

**The ordering constraint that dominates.** `unattended kit gate`, `harness arms`, `method carriers`,
`kit version markers` and `unattended skill wiring` carry no `guard` in `tools/gate-legs.json`, so
they run on every commit's diff-scoped bar. Nothing may land in a state a later unit repairs.

## Owner decisions — RESOLVED

All five were put to the owner on 2026-08-14 and answered. Recorded here in full, because a decision
whose reasoning is not on disk is one the next session re-opens.

**P1 · Tamper evidence over waivers — RESOLVED (owner, 2026-08-14): buy the git join.** Leg check 17
grades the SHAPE of a waiver line, and the ordering guarantee lives inside a driver that is not the
only writer of the run-state file, because `park()` is a bare append. So a run can add a well-formed
waiver at pass 4 and the check accepts it. Unit 13 therefore also joins the worktree's waiver lines
to the FIRST committed blob of that file. **The honest limit, stated because protocol §9 disclaims
exactly this property:** run locally, the join proves little, since the run writes both sides. Its
value is that §9's *what actually binds* — the same leg re-run in a clone the run never touched — now
has something to catch. Unit 13 moves to Tier 2 on this.

**P2 · D6's parallelism inversion — RESOLVED (owner, 2026-08-14): block on a mechanism, and hunt for
one inside this build.** The inversion will NOT ship on a clause that excuses it. Direct agent spawns
are capped per prompt turn and an unattended run has no next prompt to reset the budget; a workflow
sidechain inherits no hooks and no `CLAUDE.md`, so passes dispatched there run outside the eleven
directives this build installs. Both known routes are bad. Unit 21 is a new research unit that asks
whether ANY route dispatches a build pass concurrently without voiding the directive layer, and unit
15 is now downstream of its answer. **If no route survives, unit 15 ships the finding rather than the
inversion** — which is a real possibility and is the reason the unit is scoped as research, not as a
foregone implementation.

**P3 · The roster marker — RESOLVED (owner, 2026-08-14): require it.** Every unattended build's
README carries the authored roster inside a marker pair. Two lines per build, against a
`build-complete` that would otherwise be vacuous for 24 of the 25 builds in the tree and blind to the
exact case D8 exists for. Folded into unit 7.

**P4 · `reuse-first`'s silent waiver — RESOLVED (owner, 2026-08-14): require the naming.** A waived
run's spec §10 must name the waiver.

*The design pass claimed this waiver reds the FULL bar at the push boundary. That claim is FALSE and
was corrected against source; it is kept here rather than deleted, because it was the question the
owner was asked to prioritise first and the correction is what changed the answer.* Measured: hygiene
check 12 leaves the body-assertion block at `if (hdr ~ /Tier-1/) next`, so §10 is unchecked on a
Tier-1 spec entirely; on Tier-2 the empty-body test is `/[^ 	]/`, which an `N/A` line satisfies, and
three Tier-2 specs in this corpus already ship one in a green tree. Nothing machine-checks §10's
CONTENT. So the hazard inverts — the waiver leaves the bar GREEN over a build that skipped the reuse
probes, which is worse than a loud failure because nothing reports it. The "refuse the handle" option
was motivated entirely by the loud-failure story and died with it.

**P5 · The protocol's own tables — RESOLVED (owner, 2026-08-14): fix in this build.** Protocol §3's
phase list and §4's DoD table are joined to `PHASES_CORE` and `DOD_CORE` by no leg, and this build
adds two rows to the second of them. Unit 22 extends check 16 arm A's join shape to both tables. The
gap is pre-existing, but this build is what makes it worse, and the join rides the leg unit 12 builds
anyway.

## Residual risks

1. **`closing-review-recorded` measures that a tracked review under this build names the run's pinned
   BASE** — not that it was adversarial, nor that it reviewed the diff. The join to a value pinned
   once is what stops a pre-existing record satisfying it; beyond that it is a construction cost.
2. **A BLOCKED closing review satisfies it.** Anchoring the verdict value was rejected on
   measurement: across this corpus zero review records carry `## Verdict: CLEAN`, so the anchor would
   make the item unsatisfiable against every record the repo has written. The landed-with-a-blocker
   path is covered by `build-complete` instead. Watch the first two runs.
3. **Pointer-not-copy is machine-held on the pairs and authorial on the gloss column.** No gate can
   see a gloss growing from a name into a restatement of the rule it points at. Three cells in the
   pre-fold design already did this. The only control is the review lens; a byte cap was refused
   because a budget permits a compressed rule.
4. **Kickoff-after-preflight is a sequence nobody has executed.** Leg check 18 asserts the ORDER of
   two lines in a template, not that the sequence works. Preflight stages the run-state file, so
   kickoff Step 1 meets a tree dirtied by its own reporting; its STOP conditions do not cover that
   and *should* pass — the word that precedes every reproduced bypass in this kit's history.
5. **Every waiver record and every verdict is written and read under the run's own uid.** Protocol
   §9's boundary is unchanged by this build, and P1 is the only thing that would move it.

## Method

The build method is `memory/guides/BUILD-METHOD.md`. The generated region below is rendered by
`gen_build_index.py` from the front matter and each spec's status header — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** CLOSED · 23 unit(s) · node c · opened 2026-08-14 · streams tooling+playbook · ids TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 TOOL-cBriefedPilot-23 TOOL-cBriefedPilot-24 TOOL-cBriefedPilot-25 TOOL-cBriefedPilot-26 TOOL-cBriefedPilot-27 TOOL-cBriefedPilot-28 TOOL-cBriefedPilot-29 TOOL-cBriefedPilot-30 TOOL-cBriefedPilot-31 TOOL-cBriefedPilot-32 TOOL-cBriefedPilot-34 TOOL-cBriefedPilot-35 TOOL-cBriefedPilot-36

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-cBriefedPilot-1 — the paired flag accumulator, and an `--override` that can be used twice](spec/2026-08-14-spec-cBriefedPilot-1.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cBriefedPilot-10 — the last owner turn, and why it is the last one](spec/2026-08-14-spec-cBriefedPilot-10.md) | CLOSED | rev-4 | 2026-08-16 |
| [TOOL-cBriefedPilot-11 — the kickoff step, taken after preflight, and the README read as a roster](spec/2026-08-14-spec-cBriefedPilot-11.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-12 — leg check 16, the registry joined both ways and the pointers resolved](spec/2026-08-14-spec-cBriefedPilot-12.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-13 — leg check 17, a waiver names a declared handle and was there in the first commit](spec/2026-08-14-spec-cBriefedPilot-13.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cBriefedPilot-14 — leg check 18, the kickoff road asserted as an order and not as a mention](spec/2026-08-14-spec-cBriefedPilot-14.md) | CLOSED | rev-1 | 2026-08-16 |
| [TOOL-cBriefedPilot-15 — M6's parallelism inversion, or the finding that it has no mechanism](spec/2026-08-14-spec-cBriefedPilot-15.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-16 — the method's pointers name the new layer](spec/2026-08-14-spec-cBriefedPilot-16.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-17 — the shipped protocol marker, paired to the constant it claims](spec/2026-08-14-spec-cBriefedPilot-17.md) | CLOSED | rev-1 | 2026-08-16 |
| [TOOL-cBriefedPilot-18 — the contract describes the directive layer, and publishes only what exists](spec/2026-08-14-spec-cBriefedPilot-18.md) | CLOSED | rev-5 | 2026-08-16 |
| [TOOL-cBriefedPilot-19 — the kit identifies as the version it now is](spec/2026-08-14-spec-cBriefedPilot-19.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cBriefedPilot-2 — the directive registry, eleven pointers and not one restated rule](spec/2026-08-14-spec-cBriefedPilot-2.md) | CLOSED | rev-1 | 2026-08-16 |
| [TOOL-cBriefedPilot-20 — the records this build leaves, and one row it should not have had to close](spec/2026-08-14-spec-cBriefedPilot-20.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cBriefedPilot-21 — the parallelism mechanism hunt, and what would settle it](spec/2026-08-14-spec-cBriefedPilot-21.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-22 — check 16's join, extended to the protocol's own two tables](spec/2026-08-14-spec-cBriefedPilot-22.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-3 — the owner's named, reasoned waiver, accepted at preflight and nowhere else](spec/2026-08-14-spec-cBriefedPilot-3.md) | CLOSED | rev-6 | 2026-08-16 |
| [TOOL-cBriefedPilot-4 — preflight refuses to start a run with no method to run it under](spec/2026-08-14-spec-cBriefedPilot-4.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-5 — the BASE is pinned once, which is what the contract already claims](spec/2026-08-14-spec-cBriefedPilot-5.md) | CLOSED | rev-1 | 2026-08-16 |
| [TOOL-cBriefedPilot-6 — `--plan` sees the planned unit that has no spec](spec/2026-08-14-spec-cBriefedPilot-6.md) | CLOSED | rev-4 | 2026-08-16 |
| [TOOL-cBriefedPilot-7 — `build-complete`, and the roster every unattended build now owes](spec/2026-08-14-spec-cBriefedPilot-7.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cBriefedPilot-8 — `closing-review-recorded`, joined to the base the run pinned once](spec/2026-08-14-spec-cBriefedPilot-8.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cBriefedPilot-9 — the Skill's directive table, and a step 0 that is no longer a suggestion](spec/2026-08-14-spec-cBriefedPilot-9.md) | CLOSED | rev-4 | 2026-08-16 |
| [TOOL-cBriefedPilot-23 — the arms meta-gate grades EXECUTION, not text](spec/2026-08-16-spec-cBriefedPilot-23.md) | CLOSED | rev-2 | 2026-08-16 |
<!-- /gen:build-index -->
