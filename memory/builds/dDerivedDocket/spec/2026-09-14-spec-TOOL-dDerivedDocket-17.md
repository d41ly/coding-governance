# TOOL-dDerivedDocket-17 — asks-disposed DoD item and freeze

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |

<!-- /gen:spec-records -->

## 1. Goal

A run pointed at a set of asks can reach `--close` today with a mandated ask still undecided, and
no Definition-of-Done item notices, because none of the twelve concerns asks
(`tools/unattended/unattended.sh:348`). Add a thirteenth core item, `asks-disposed`, that reads the
same fold the family view renders and decides whether every mandated ask, and every ask this build
filed itself, ended in a state the owner can accept. Freeze what it read at landing, because REOPEN
(owner ruling D4) makes CLOSED non-absorbing and a landed record's answer would otherwise change
under it.

## 2. Scope (IN)

- **S1** `DOD_CORE` gains `asks-disposed:machine`, making thirteen core items. The item does NOT
  join `DOD_NO_OVERRIDE`: by owner ruling D12-b it is overridable with a recorded reason, through
  the generic `--override` loop that already refuses an override with no reason and writes an
  `override` park row. Observed by AC1 and AC7.
- **S2** A `dod_met` arm for `asks-disposed` that evaluates terms T0 to T5 of §4, with the F3
  hardening for asks graded `yes` and the D12-c KEEP rule. The arm reads status only from the
  `ASKS_CMD` witness and never re-implements the fold. Observed by AC2, AC3, AC4, AC5 and AC6.
- **S3** The `asks-at-landing` fact: one line of `<id>=<STATUS>` pairs, written by the code path that
  writes `units-at-landing` and immediately after it, only for a record that pins a mandate or whose
  build filed asks. A witness failure at that point refuses the verb before any terminal write.
  Observed by AC8.
- **S4** `CORE_FLOOR`'s DoD half moves from 12 to 13 in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`, in the same commit as S1. The phase half is left
  exactly as unit 4 leaves it. Observed by AC9.
- **S5** Protocol §4, in `tools/unattended/PROTOCOL.template.md` and its installed copy
  `memory/guides/UNATTENDED-PROTOCOL.md`, byte-identical: the count sentence reads "Thirteen", and a
  row for `asks-disposed` joins the table. Leg check 16's count-word table in
  `tools/unattended/check-unattended.sh` is extended past `twelve`, because today it maps
  `thirteen` to -1 and would red the leg on the correct sentence. Observed by AC1 and AC10.
- **S6** A report-only drift-audit signal, `asks_disposed_overrides`, counting `override` park rows
  that name `asks-disposed` across every tracked run-state file. Owner ruling D12-b makes the item
  overridable on the condition that overrides are counted; without the count the override is
  silent. Observed by AC11.
- **S7** Every new `fail` branch gets an arm in `tools/unattended/unattended.test.sh` or
  `tools/unattended/check-unattended.test.sh`, and `ARMS_FLOORS` in `.memory-tree.conf` moves in
  the same commit. Each arm is observed RED with its fix unstaged. Observed by AC12.

## 3. Non-goals (OUT)

- `ASKS_CMD`, the pinned `asks:`, `asks-ready:` and `m-base:` facts, P5, P6 and READY at preflight.
  Those are unit 16's, and this unit reads them.
- The `--asks --tsv` print mode and its column order are unit 15's. The status fold is unit 6's.
- The leg's second opinion that `asks-at-landing` is present on a landed record is unit 18's.
- Moving the freeze to `--close` under in-place landing is unit 22's.
- The contract prose for T0 to T5, the override route and the KEEP rule in the companion guide,
  and the Skill's filing steps (a SEV row in the same commit as the ask, closeout timing) are
  unit 20's. This unit writes only the protocol §4 row that leg check 16 requires.
- Setting `ASKS_CMD` in gov and the real-tree staged RED are unit 35's.
- V10 itself is a verdict of the memory-tree engine (units 6 and 8). This unit enforces its rule for
  this build's own asks at `--close` and adds no verdict to the engine.
- `DOD_NO_OVERRIDE` does not change, so the Skill's non-overridable paragraph and check 16's join
  over it do not change either.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-16` — `ASKS_CMD` and the pinned `asks:`, `asks-ready:`
  and `m-base:` facts. Without them T1 to T5 have no mandate to grade and no range to bound T4.
- **consumes-from** `TOOL-dDerivedDocket-15` — the `--asks --tsv` row shape the witness parses
  (the status, decided-by, home and closers fields, and the closing examined line). Without it T2
  has nothing to read.
- **hands-off** `TOOL-dDerivedDocket-18` — the leg's re-derivation that every LANDED record carrying
  a mandate carries `asks-at-landing`.
- **hands-off** `TOOL-dDerivedDocket-20` — the contract text for T0 to T5, the override route and
  the KEEP rule in the companion guide, and the Skill steps that keep a run from reaching T3 with an
  undisposed discovery.
- **hands-off** `TOOL-dDerivedDocket-22` — moving the `asks-at-landing` freeze to `--close`, beside
  `units-at-landing`, under in-place landing.
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of `asks-disposed` on a fixture
  run holding an undisposed mandated ask, once gov sets `ASKS_CMD`.

## 4. Design

### Data model

The scope set is the union of two sets. M is the pinned `asks:` fact, expanded through the kit's
existing range expansion. F is every ask whose `home` field in the witness is this build's slug.

The witness is one invocation of `ASKS_CMD` over M ∪ F at HEAD, run through `run_bounded`, printing
unit 15's TSV: one `ask` line per id with eleven fields, then `examined<TAB><n>`. A line whose first
field is not `ask`, or that does not carry eleven fields, is a parse refusal rather than a row,
because a column-order change in the producer must read as a dead probe and never as a pass.

The driver additionally reads two things by LINE MATCH only, which is filing and not status
(`tools/unattended/lib-unattended.sh:18-19`): disposition rows in THIS build's
`memory/builds/<slug>/BACKLOG.md`, and the header tail verbs of THIS build's specs. It never reads a
foreign build's file to decide anything.

### The terms, evaluated in order

| Term | Condition | Verdict |
|---|---|---|
| T0 | no `asks:` fact and `ASKS_CMD` blank | MET, announced as not adopted |
| T0 | no `asks:` fact, `ASKS_CMD` set, and F empty | MET, announced as nothing to dispose |
| T1 | an `asks:` fact while `ASKS_CMD` is blank | UNMET, naming preflight's refusal that should have fired |
| T2 | the witness yields a row count or examined count that is not the scope size, or omits an id | UNMET as a DEAD PROBE naming the missing ids |
| T3 | an ask in M in none of the admitted end states below, or an ask in F with no disposition row and not terminal | UNMET naming the ask |
| T4 | an ask in M derived CLOSED by a sha inside `m-base..HEAD` that is not a CLOSED unit's build commit | UNMET naming the sha |
| T5 | an ask in M not derived CLOSED by a CLOSED spec of this build, and named by no owed-class park row | UNMET naming the ask |

A bound breach in T2 reads "never answered", the same distinction `gates-green` draws
(`tools/unattended/unattended.sh:3088-3093`), because a breach and a red are different faults.

**T3's admitted end states for an ask in M:**

1. derived CLOSED or WONTDO, subject to T4 and to the F3 rules below;
2. live, and held by a `BLOCKED · <id> · on …` or `DEFERRED · <id> · until …` row in THIS build's
   file;
3. a `KEEP · <id> · …` row in THIS build's file, admitted only when a CLOSED spec of this build
   carries `advances <id>` in its header tail. That is owner ruling D12-c: KEEP after a delivered
   partial, and never as a silent way not to do the work.

**The F3 hardening, for an ask whose pinned `asks-ready:` grade is `yes`:**

- A hold admitted by end state 2 must be named by a `decision` park row whose reason names the
  tripped M3 veto, spelled `veto 2` or `veto 3`.
- A hold whose target is an owner-call ask this run filed under its own slug is admitted only for
  an ask graded `no` or `legacy`.
- A WONTDO decided by a row in THIS build's file that is present at HEAD and absent at `m-base` is
  UNMET, unless the row's reason carries `stale:` and a `decision` park row names the ask.
  Otherwise a run could meet the item with no delivered work.

**T5's owed classes** are a `decision` park row naming the ask, or a `rescope` park row whose act is
in `PARK_ACTS_OWED`. The argument is that constant's own: M3 delegates scope resolution and never
scope abandonment (`tools/unattended/unattended.sh:377-382`).

### The override

`--close --override asks-disposed --reason <text>` goes through the loop at
`tools/unattended/unattended.sh:2946-2974` unchanged. That loop refuses a missing reason with check
12, refuses a reason spelling the bypass flag, and writes the `override` park row after the DoD
loop. F3 governs every close that carries no override.

### The freeze

`asks-at-landing: <id>=<STATUS> <id>=<STATUS> …` is one line, sorted by slug and then numeric
sequence, never by string. It is computed by the witness over M ∪ F at the tree the verb examines.
It is written directly after `units-at-landing` (`tools/unattended/unattended.sh:2435-2437`) and
before the terminal writes, preserving the `TOOL-dSealedTally-1` ordering: a refusal there leaves a
non-terminal, repairable record. A record with no mandate and no filed ask gets no line, so every
existing record is unchanged.

The refusal takes a new driver code, allocated at build time as the next integer above the driver's
highest, because other units of this build allocate codes concurrently and a number pinned here
could collide.

### Rollout

Dark. Gov's `ASKS_CMD` stays blank until unit 35, so every run takes T0 and announces it, and no
record gains an `asks-at-landing` line. The floor moves in the same commit as the item, so the
leg's shrink-only pin never sits one below a live count.

### Inventory

Minted identifiers, each named at build time through
`python tools/lexicon/lexicon.py --suggest <identifier> --as <cell>` where it is a function name:

- the DoD item `asks-disposed`, in `DOD_CORE`;
- the run fact `asks-at-landing`;
- the drift signal `asks_disposed_overrides`;
- one driver refusal code, number allocated at build time.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`.unattended.conf` · `tools/unattended/.unattended.conf.example` · `.memory-tree.conf` ·
`tools/drift-audit/drift_report.py` · `tools/drift-audit/selftest.py` ·
`memory/map/features/unattended.md`.

### Alternatives rejected

- **D12-b option (a), non-overridable.** The design recommended it on the `pieces-complete`
  argument. The owner ruled overridable with a recorded reason (DR §20), and the ruling is cited
  here, not re-decided.
- **Reading dispositions from the family view.** The view lists live asks only, so a terminal ask is
  absent from it by design (DR §5.3), and the item must grade terminal asks too.
- **Freezing at `--close` now.** Under the primary lander the tree at `--close` is not the landed
  tree. The move belongs with in-place landing, which is unit 22.

## 5. Production-readiness checklist

- security — the item reads records at HEAD, this build's own files and the run-state file. The
  witness is a project-declared command from the conf, never ask text, and it runs bounded. A
  `seen` command is never executed here.
- perf / scale — one bounded witness call per `--close` and one per `--landed`; the parse is linear
  in the scope size.
- error / empty / loading states — an empty scope is MET and announced; a short witness is a named
  DEAD PROBE; a bound breach is named as never answered.
- observability — every UNMET line names the ask id and the term; overrides are counted by drift.
- risks — a change to unit 15's TSV shape breaks the parse, and the parse is written to refuse
  rather than misread. The item reads a run-writable record for its park rows, which the protocol's
  §9 uid limit already states.
- testing — one arm per term and per new `fail` branch; the unattended suites run once, at the
  unit's end (D12-h), and are read against unit 1's baseline.
- migration — additive. Every existing record takes T0. `CORE_FLOOR` moves with the item.
- user docs — the protocol §4 row here; the companion contract text is unit 20's.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs after S1, S4 and S5, check 16's
  DoD join and its count-sentence join are both green over thirteen items.
  Red when: the protocol still states "Twelve", or the table lacks the `asks-disposed` row, so the
  join reports an item enforced by `--close` that the contract never names.
- **AC2** — When `--close` runs in `tools/unattended/unattended.test.sh` on a fixture run with no
  `asks:` fact and a blank `ASKS_CMD`, the item is MET and prints a `skipped — asks-disposed` line.
  Red when: the item is MET with no announcement, which is a skip that reads as coverage.
- **AC3** — When the fixture's `ASKS_CMD` prints one row fewer than the scope, the item is UNMET as
  a DEAD PROBE naming the missing id.
  Red when: the arm iterates the rows it received rather than the scope, so the missing id passes.
- **AC4** — When a mandated ask derives OPEN with no hold, `--close` is UNMET naming it; when this
  build's own file holds a `BLOCKED` row on it and a `decision` park row names it, the item is MET.
  Red when: a hold row in a FOREIGN build's file admits the ask.
- **AC5** — When a mandated ask derives CLOSED by a sha inside `m-base..HEAD` that is not a CLOSED
  unit's build commit, the item is UNMET naming the sha.
  Red when: the arm admits any CLOSED status without reading its evidence.
- **AC6** — When a KEEP row names a mandated ask and no CLOSED spec of this build `advances` it, the
  item is UNMET; with such a spec it is MET. When an in-range WONTDO row names a `yes` ask with no
  `stale:` reason, the item is UNMET.
  Red when: KEEP is admitted with no delivered partial, or the in-range WONTDO passes.
- **AC7** — When `--close --override asks-disposed --reason x` runs on a fixture failing T3, the
  close succeeds and writes an `override` park row; the same call with no reason is refused by check
  12. Proven in `tools/unattended/unattended.test.sh`.
  Red when: the override is refused with check 21, which would mean the item joined
  `DOD_NO_OVERRIDE` against the owner's ruling.
- **AC8** — When `--landed` runs on a mandated fixture, the record gains an `asks-at-landing` line
  on the line after `units-at-landing`; when the witness fails there, the verb refuses and the
  record still reads its non-terminal phase.
  Red when: the refusal fires after `phase: LANDED` is written, which is the wedge
  `TOOL-dSealedTally-1` removed.
- **AC9** — When `asks-disposed` is deleted from `DOD_CORE` while `.unattended.conf` declares a DoD
  floor of 13, `bash tools/unattended/check-unattended.sh` reds check 1.
  Red when: the floor stays at 12, so deleting the new item passes the shrink-only pin.
- **AC10** — When `tools/unattended/check-unattended.test.sh` feeds check 16 a protocol stating
  "Thirteen kit-owned core items", the sentence parses to 13.
  Red when: the word table still stops at twelve and maps the correct sentence to -1.
- **AC11** — When `python tools/drift-audit/drift_report.py` runs over a fixture holding two
  `override` rows for `asks-disposed` and one for `gates-green`, `asks_disposed_overrides` reads 2
  and is not gateable; over a fixture with no run-state file it reads DEAD PROBE.
  Red when: the signal counts overrides of every item, or reports 0 over no records.
- **AC12** — When `bash tools/unattended/run-unattended-gates.sh --selftests` runs once at the end
  of the unit, every arm this unit added passes and the run shows no NEW failure against unit 1's
  held-suite baseline; each arm was observed RED with its fix unstaged.
  Red when: an arm is wired without its failing case ever being seen.
  cost: one run of the unattended suites, which is the unit's single sanctioned suite run (D12-h).

## 7. Gates

`unattended kit gate` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `drift-audit records` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture run per term T0 to T5, the override, and the freeze refusal · `ARMS_FLOORS` for `tools/unattended/unattended.sh`
New arm: `tools/unattended/check-unattended.test.sh` · a protocol copy stating "Thirteen" and one with the row removed · `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`
New arm: `tools/drift-audit/selftest.py` · a fixture with override rows for two items, and one with no run-state file · none

## 8. Open questions

- **F1 — may `asks-disposed` be overridden?** The design recommended no, on the `pieces-complete`
  argument. RESOLVED (owner, 2026-09-13): D12-b, overridable with a recorded reason like
  `gates-green`; overrides are counted by drift as `asks_disposed_overrides`, report-only.
- **F2 — KEEP on a mandated ask?** RESOLVED (owner, 2026-09-13): D12-c, allowed only after a CLOSED
  unit of this build `advances` the ask.
- **F3 — does the DR's companion guide `UNATTENDED-ASKS.md` belong to this unit, as DR §19.8 U12
  places it, or to the carriers unit?** M2 requires one mechanism per spec, and a new document is a
  separate mechanism from a DoD item. Moving it to unit 20 keeps this unit to one mechanism and puts
  the guide beside the rest of the ask contract text it carries, which DR §19.2 to §19.6 spread over
  four units. RESOLVED (agent, 2026-09-14, delegated): the guide moves to unit 20; this unit writes
  only the protocol §4 row that leg check 16 requires in the same commit as the item.
- **F4 — where does the freeze sit before unit 22 lands?** RESOLVED (agent, 2026-09-14, delegated):
  at `--landed`, beside `units-at-landing`, as DR §19.5 states; unit 22 moves both together.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Diverges from DR §19.5 and §19.8 U12 in three places, each by
  a ruling or a fork above: `DOD_NO_OVERRIDE` does not gain the item (D12-b); the companion guide
  moves to unit 20 (F3); and leg check 16's count-word table is extended, a need DR did not record
  and the regrounding found at `tools/unattended/check-unattended.sh:2065-2068`. Two edges not in
  the brief's table are added: consumes-from unit 15, whose TSV the witness parses, and hands-off
  unit 22 and unit 35, which DR §21.4 U20 and U15 name as moving and arming this item.

## 10. Reuse audit

The seams are the driver's own. `dod_met` in `tools/unattended/unattended.sh` is extended with one
arm, and its `pieces-complete` arm is the precedent for a term zero that is MET and announced
(`:3117-3120`). The override path is reused unchanged, and `set_fact` beside `units-at-landing` is
the freeze's write site. `reuse_lookup.py "definition of done item grading delivered asks at close"`
returns no seam in the driver, because the lookup's scan coverage reports `.sh` as an unscanned
layer, so the lookup is blind to the whole kit this unit extends. The `unattended` dossier's shared
seams, read instead, name no second DoD mechanism. Where DR and the source disagree: DR says
`DOD_NO_OVERRIDE` gains the item, which the owner's D12-b ruling reverses; DR's line citations for
`DOD_CORE`, `DOD_NO_OVERRIDE` and `units-at-landing` hold at BASE, because `unattended.sh` did not
move between `09a22d2b` and `abac6d59`.

Recall terms used: `pieces-complete DOD_NO_OVERRIDE override CORE_FLOOR units-at-landing freeze
Definition-of-Done close verb mandate scope abandonment PARK_ACTS_OWED`
