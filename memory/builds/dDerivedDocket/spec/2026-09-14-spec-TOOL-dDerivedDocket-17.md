# TOOL-dDerivedDocket-17 — asks-disposed DoD item and freeze

**Status:** SPECCED · rev-6 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |
| [2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |

<!-- /gen:spec-records -->

## 1. Goal

A run pointed at a set of asks can reach `--close` today with a mandated ask still undecided, and
no Definition-of-Done item notices, because none of the twelve concerns asks
(`tools/unattended/unattended.sh:407`). Add a thirteenth core item, `asks-disposed`, that reads the
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
  `ASKS_CMD` witness and never re-implements the fold. Observed by AC2, AC3, AC4, AC5, AC6, AC13,
  AC14, AC16, AC17, AC18, AC19 and AC20.
- **S3** The `asks-at-landing` fact: one line of `<id>=<STATUS>` pairs, written by the code path that
  writes `units-at-landing`, after it and before any terminal write, only for a record that pins a
  mandate or whose F (§4) is non-empty. A witness failure at that point refuses the verb before any
  terminal write. Observed by AC8 and AC15.
- **S4** `CORE_FLOOR`'s DoD half moves from 12 to 13 in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`, in the same commit as S1. The phase half is left
  exactly as unit 4 leaves it. Observed by AC9.
- **S5** Protocol §4, in `tools/unattended/PROTOCOL.template.md` and its installed copy
  `memory/guides/UNATTENDED-PROTOCOL.md`, byte-identical: the count sentence reads "Thirteen", and a
  row for `asks-disposed` joins the table. Leg check 16's count-word table in
  `tools/unattended/check-unattended.sh` is extended past `twelve`, because today it maps
  `thirteen` to -1 and would red the leg on the correct sentence. The row and the count word add at
  most 200 B to each protocol copy AND ARE PAID FOR IN THE SAME EDIT, because no cap is raised in
  this build and the free space does not cover every unit that wants it. The passage that leaves
  §4 is the paragraph beginning `The two attested items have a VERB, the only way to write one`,
  down to the sentence ending `not the trust assumption §9 states`; it moves into the `--attest`
  entry of `tools/unattended/VERBS.template.md` and its installed copy
  `memory/guides/UNATTENDED-VERBS.md`, the verbs half of the contract, which already carries that
  verb and states most of this paragraph in shorter form — one fact in one place, and §7 of the
  protocol records the same move as a byte decision. §4 keeps one sentence pointing at the verb
  entry, and that sentence does NOT reuse the moved paragraph's opening clause
  `The two attested items have a VERB, the only way to write one`, so the phrase AC1 counts belongs
  to the destination by construction and a correctly performed move cannot red it. The paragraph is
  larger than the row, so each protocol copy is SMALLER at this unit's
  commit than at its parent. No other unit of this build trims that paragraph. Observed by AC1
  and AC10.
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
  unit 20's. This unit writes the protocol §4 row that leg check 16 requires, the §7 byte-decision
  line recording S5's move, and the `--attest` entry of the verbs pair that §4's paragraph moves
  into; the companion-guide contract prose stays with unit 20. §4 Files touched lists all of them,
  and a builder scoping from the single-carrier sentence this bullet used to carry would under-write
  and red AC1's third `Red when:`.
- Setting `ASKS_CMD` in gov and the real-tree staged RED are unit 35's.
- V10 itself is a verdict of the memory-tree engine (units 6 and 8). This unit enforces its rule for
  this build's own asks at `--close` and adds no verdict to the engine.
- `DOD_NO_OVERRIDE` does not change, so the Skill's non-overridable paragraph and check 16's join
  over it do not change either.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-16` — `ASKS_CMD` and the pinned `asks:`, `asks-ready:`
  and `m-base:` facts, and the P5 line matcher that enumerates F, and the one TSV parse the witness
  reuses. Without them T1 to T5 have no mandate to grade and no range to bound T4.
- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute <BASE>`, whose
  attributed verdict, `verdict clean` with every inherited suite filed, is the only criterion the
  unattended suites, red at BASE (TOOL-aHoistedPass-36), can meet.
- **consumes-from** `TOOL-dDerivedDocket-2` — the prepared merge whose first parent is the
  advertised tip, which is why excluding that tip leaves exactly the run's commits.
- **consumes-from** `TOOL-dDerivedDocket-15` — the `--asks --tsv` row shape the witness parses
  (the status, decided-by, home and closers fields, and the closing examined line). Without it T2
  has nothing to read.
- **consumes-from** `TOOL-dDerivedDocket-48` — the witness capture that keeps the producer's stderr
  off the row stream. The G3 round-2 record's B1 measured that `run_bounded` merges both streams,
  so §4's parse refuses on a healthy producer; §4 and S2 keep their current text and take that
  unit's answer.
- **hands-off** `TOOL-dDerivedDocket-18` — the leg's re-derivation that every LANDED record carrying
  a mandate carries `asks-at-landing`.
- **hands-off** `TOOL-dDerivedDocket-20` — the contract text for T0 to T5, the override route and
  the KEEP rule in the companion guide, and the Skill steps that keep a run from reaching T3 with an
  undisposed discovery.
- **hands-off** `TOOL-dDerivedDocket-22` — moving the `asks-at-landing` freeze to `--close`, beside
  `units-at-landing`, under in-place landing, and the derived-LANDED endpoint the run's-own-commits
  function takes.
- **hands-off** `TOOL-dDerivedDocket-19` — the run's-own-commits function the cross-run arm calls.
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of `asks-disposed` on a fixture
  run holding an undisposed mandated ask, once gov sets `ASKS_CMD`.

## 4. Design

### Data model

The scope set is the union of two sets, each enumerated BEFORE the witness and independently of it.
M is the pinned `asks:` fact, expanded through the kit's existing range expansion. F is every ask
filed in THIS build's own `memory/builds/<slug>/BACKLOG.md` at HEAD, enumerated by unit 16's P5 line
matcher in `tools/unattended/lib-unattended.sh` over the rows `^- <ID> · filed ` whose id carries
this build's slug. That is a line match, because filing is not status
(`tools/unattended/lib-unattended.sh:18-19`; unit 16 S7 argues the same for `unit` asks).

The witness is unit 16's call shape 2,
`<ASKS_CMD> --tsv --ready <ids of M ∪ F> --target <slug> --at <rev>`, run through `run_bounded` at
the commit the verb examines, and parsed by the same TSV
parse unit 16's preflight uses, never a second parser. T2 compares the witness's rows and its
`examined` count against |M ∪ F| as enumerated above, never against a set read back from the
witness: a witness that omits an F ask would otherwise shrink F to match
(`memory/gotchas/inputs-inside-the-subjects-reach.md`). The witness prints unit 15's TSV: one `ask`
line per id with eleven fields, then `examined<TAB><n>`. A line whose first field is not `ask`, or
that does not carry eleven fields, is a parse refusal rather than a row, because a column-order
change in the producer must read as a dead probe and never as a pass.

What that parse is handed is not settled in this spec. At `fb07ca25` `run_bounded` redirects both
streams into one capture file and reads it back (`tools/unattended/unattended.sh:191-196`), so the
producer's stderr notices — unit 15 §4 routes the waiver line and unit 7's S11 liveness line there
on every healthy call — arrive inside the text this rule refuses on, and the witness reads as a DEAD
PROBE on a producer that is working. The G3 round-2 record's B1 promoted that to
`TOOL-dDerivedDocket-48`, which chooses between a capture that keeps stderr on its own channel and a
parse that skips non-row lines. This spec keeps the rule above and S2 as written and takes that
answer; T2's dead-probe verdict is the term that inherits it.

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
| T4 | an ask in M derived CLOSED by a sha among the run's own commits (below) that is not a CLOSED unit's build commit | UNMET naming the sha |
| T5 | an ask in M not derived CLOSED by a CLOSED spec of this build, and named by no owed-class park row | UNMET naming the ask |

**The run's own commits.** One function in `tools/unattended/lib-unattended.sh`, named at build
time through `lexicon.py --suggest`, lists the commits reachable from an endpoint, not reachable
from a base, and not reachable from any of the one or more exclusion tips it is given. T4 calls it
with HEAD at `--close`, `m-base:`,
and the default branch's advertised tip as `--close` already observes it. Under in-place landing
`--close` runs on the prepared merge, whose first parent is the advertised tip (unit 2 §4), so
default-branch commits landed since `m-base:` are excluded and a foreign build's CLOSED row landed in
the window is not the run's; T5 already owns 'closed with someone else's evidence'. Unit 19's
cross-run arm calls the same function, with one exclusion tip per merge its terminal walk reads, and
unit 22 supplies the endpoint for a derived-LANDED record
(§8 F5).

A bound breach in T2 reads "never answered", the same distinction `gates-green` draws
(`tools/unattended/unattended.sh:3286-3291`), because a breach and a red are different faults.

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
scope abandonment (`tools/unattended/unattended.sh:436-441`).

### The override

`--close --override asks-disposed --reason <text>` goes through the loop at
`tools/unattended/unattended.sh:3144-3172` unchanged. That loop refuses a missing reason with check
12, refuses a reason spelling the bypass flag, and writes the `override` park row after the DoD
loop. F3 governs every close that carries no override.

### The freeze

`asks-at-landing: <id>=<STATUS> <id>=<STATUS> …` is one line, sorted by slug and then numeric
sequence, never by string. It is computed by the witness over M ∪ F at the tree the verb examines.
It is written by the code path that writes `units-at-landing`
(`tools/unattended/unattended.sh:2525-2527`), after it and before any terminal write, through
`set_fact`, which inserts each new key directly under the `## Run facts` heading
(`tools/unattended/unattended.sh:2876-2887`); the record reads newest-first, so the freeze sits on
the line BEFORE `units-at-landing`. That preserves the `TOOL-dSealedTally-1` ordering: a refusal
there leaves a non-terminal, repairable record. A record with no mandate and an empty F gets no
line, so every existing record is unchanged.

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
- the run's-own-commits function in `tools/unattended/lib-unattended.sh`, which unit 19 shares;
- one driver refusal code, number allocated at build time.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/lib-unattended.sh` ·
`tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md`, the pair S5's paragraph
moves into ·
`.unattended.conf` · `tools/unattended/.unattended.conf.example` · `.memory-tree.conf` ·
`tools/drift-audit/drift_report.py` · `tools/drift-audit/selftest.py` ·
`memory/map/features/unattended.md` · `memory/map/generated/`, regenerated and staged in the commit
that stages `tools/drift-audit/drift_report.py`, because the pre-commit fast leg runs the
codebase-map gate whenever a `.py` is staged (dUnstagedSymbol, `1a774fcd`). This unit moves no kit
version constant, under the build's one-owner rule that the unit first to change a kit's bytes in
build order owns that kit's one move.
Its drift-audit bytes (S6) ride unit 13's move of `KIT_DRIFT_AUDIT_VERSION`, because unit 13 changes
`tools/drift-audit/` bytes first, and its unattended bytes ride unit 1's move (unit 1 S9).

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
- testing — one arm per term and per new `fail` branch; the unattended suites run at the build's
  one post-build bar and are read through unit 1's `--attribute <BASE>`.
- migration — additive. Every existing record takes T0. `CORE_FLOOR` moves with the item.
- user docs — the protocol §4 row here, and the attested-verb paragraph S5 moves into the
  `--attest` entry of the verbs pair; the companion contract text is unit 20's.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs after S1, S4 and S5, check 16's
  DoD join and its count-sentence join are both green over thirteen items; and when `wc -c` runs at
  this unit's build commit over `memory/guides/UNATTENDED-PROTOCOL.md` and over
  `tools/unattended/PROTOCOL.template.md`, each reads STRICTLY BELOW what `git cat-file -s`
  reports for the same path at this unit's parent commit, and below the 61440 B guide cap, while
  `memory/guides/UNATTENDED-VERBS.md` reads under that same cap with the moved paragraph in it. The
  LINE count of each of the three, from `git cat-file -p <commit>:<path> | wc -l`, is below the
  750-line half of that cap, which
  `tools/memory-tree/check-memory-hygiene.sh:84` declares beside the byte half. The move is
  witnessed by a phrase INSIDE the moved paragraph rather than by size, which a file well under its
  cap satisfies either way: `git grep -c 'the only way to write one'` returns 1 in
  `tools/unattended/VERBS.template.md` and 1 in `memory/guides/UNATTENDED-VERBS.md` and 0 in both
  protocol copies at this unit's commit, and exactly the reverse at its parent. And check 10 of the
  same leg finds BOTH pairs byte-identical, the protocol pair and the verbs pair.
  Red when: the protocol still states "Twelve", or the table lacks the `asks-disposed` row, so the
  join reports an item enforced by `--close` that the contract never names; or the row lands
  without S5's trim beside it, so a copy is LARGER at this unit's commit than at its parent and
  this unit spends headroom the rest of this build's protocol edits are priced against; or the
  paragraph is deleted rather than moved, so the verbs half never gains what §4 gave up; or it
  reaches one half of the verbs pair only, so the pair diverges while every size read still passes.
  permission: unit passes run no gate legs (fix F7, and the unit child prompt since
  TOOL-aProbedUnit-1), so this green run of the leg over the real tree is observed at the one
  post-build bar the main loop runs at VERIFYING, after the last unit, where `unattended kit gate`
  is unheld and any bar reaches it. AC9's staged break is the pass's OWN direct
  check and runs the leg's own command over a scratch copy carrying the break, which
  `memory/guides/BUILD-METHOD.md` M6 sanctions and `tools/unattended/gate-guard.js` admits, because
  it is neither a suite FILE invocation nor a run over the real tree; that real-tree run is the one
  the build brief's owner rule forbids in a pass. The byte read above is a `wc -c` in the pass.
- **AC2** — When `--close` runs in `tools/unattended/unattended.test.sh` on a fixture run with no
  `asks:` fact and a blank `ASKS_CMD`, the item is MET and prints a `skipped — asks-disposed` line.
  Red when: the item is MET with no announcement, which is a skip that reads as coverage.
- **AC3** — When the fixture's `ASKS_CMD` prints one row fewer than the scope, the item is UNMET as
  a DEAD PROBE naming the missing id.
  Red when: the arm iterates the rows it received rather than the scope, so the missing id passes.
- **AC4** — When a mandated ask derives OPEN with no hold, `--close` is UNMET naming it; when the
  ask's pinned grade is `yes`, this build's own file holds a `BLOCKED` row on it, and a `decision`
  park row whose reason spells `veto 2` names it, the item is MET.
  Red when: a hold row in a FOREIGN build's file admits the ask.
- **AC5** — When a mandated ask derives CLOSED by a sha among the run's own commits that is not a
  CLOSED unit's build commit, the item is UNMET naming the sha under T4; when a foreign build's
  `CLOSED · <that ask> · by <its own sha>` lands on the fixture's default branch after `m-base:` and
  reaches the run through a prepared merge whose first parent is the advertised tip, T4 does not name
  that sha, and T5 names the ask.
  Red when: the arm admits any CLOSED status without reading its evidence, or walks the plain
  `m-base..HEAD`, so under in-place landing it names a sha this run never wrote.
- **AC6** — When a KEEP row names a mandated ask and no CLOSED spec of this build `advances` it, the
  item is UNMET; with such a spec it is MET. When an in-range WONTDO row names a `yes` ask with no
  `stale:` reason, the item is UNMET.
  Red when: KEEP is admitted with no delivered partial, or the in-range WONTDO passes.
- **AC7** — When `--close --override asks-disposed --reason x` runs on a fixture failing T3, the
  close succeeds and writes an `override` park row; the same call with no reason is refused by check
  12. Proven in `tools/unattended/unattended.test.sh`.
  Red when: the override is refused with check 21, which would mean the item joined
  `DOD_NO_OVERRIDE` against the owner's ruling.
- **AC8** — When `--landed` runs on a mandated fixture, the record gains exactly one
  `asks-at-landing` line, written in the same verb run as `units-at-landing` and before
  `phase: LANDED`; when the witness fails there, the verb refuses, the record still reads its
  non-terminal phase, and it carries no `asks-at-landing` line. `--landed` on a record with no
  mandate and an empty F writes no `asks-at-landing` line; over a mandate holding `EXMP-aFoo-2` and
  `EXMP-aFoo-10` the freeze lists `-2` first.
  Red when: the refusal fires after `phase: LANDED` is written, which is the wedge
  `TOOL-dSealedTally-1` removed; or the freeze is written onto every record, or sorted as strings.
- **AC9** — When `asks-disposed` is deleted from `DOD_CORE` while `.unattended.conf` declares a DoD
  floor of 13, `bash tools/unattended/check-unattended.sh` reds check 3, 'CORE Definition-of-Done set
  has shrunk below its floor' (`tools/unattended/check-unattended.sh:729-731`).
  Red when: the floor stays at 12, so deleting the new item passes the shrink-only pin.
- **AC10** — When `tools/unattended/check-unattended.test.sh` feeds check 16 a protocol stating
  "Thirteen kit-owned core items", the sentence parses to 13.
  Red when: the word table still stops at twelve and maps the correct sentence to -1.
  permission: that file is a self-test suite, which `tools/unattended/gate-guard.js` denies before
  VERIFYING, so the arm runs at the one post-build bar the main loop runs at VERIFYING, after the
  last unit; in the pass the same protocol text is fed to the word table by hand in a scratch copy.
- **AC11** — When `python tools/drift-audit/drift_report.py` runs over a fixture holding two
  `override` rows for `asks-disposed` and one for `gates-green`, `asks_disposed_overrides` reads 2
  and is not gateable; over a fixture with no run-state file it reads DEAD PROBE.
  Red when: the signal counts overrides of every item, or reports 0 over no records.
- **AC12** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs at the
  build's one post-build bar, its attribution summary reads `verdict clean`, meaning no NEW FAIL, no
  `DEAD PROBE at L` and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or
  `DEAD PROBE at R` is named by its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows. Every arm this
  unit added passes, each observed RED with its fix unstaged.
  Red when: an arm is wired without its failing case ever being seen; or the attributed run is read
  by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or pushed
  past its budget, reads as clean; or an inherited failure is attributed away with no record filing
  it.
  cost: one run of the unattended suites, which is the unit's single sanctioned suite run (D12-h).
  permission: the run drives the unattended self-test suites, which `memory/guides/BUILD-METHOD.md`
  M6 keeps out of a unit pass, so it is the run the main loop makes at VERIFYING, after the last
  unit. `tools/unattended/gate-guard.js` denies the same runner before VERIFYING, so the hook and
  the method agree. Which run covers it: `tools/gate-legs.json` carries NO leg for the unattended
  suites, so this is one of the attributed suite runs the main loop makes beside its bar, and no
  bar reaches it — not a plain one and not
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. In the pass each arm's RED is
  observed by hand against a scratch fixture. That folds the conservative reading of the D12-h
  conflict and does not decide it: S7, §5 and §10 keep the ruling's wording, and the run record
  parks it for the owner.
- **AC13** — When `--close` runs in `tools/unattended/unattended.test.sh` on a no-mandate fixture
  whose own `BACKLOG.md` files an ask that has no disposition row and is not terminal, with
  `ASKS_CMD` set, the item is UNMET naming that ask under T3.
  Red when: F is read from the witness's `home` field, so an F ask is graded only if the witness
  chose to print it.
- **AC14** — When the fixture's `ASKS_CMD` prints every row except one F ask's, the item is UNMET as
  a DEAD PROBE naming that ask.
  Red when: T2 compares the witness against the set it returned, so the omission shrinks F to match
  and T3 passes vacuously.
- **AC15** — When `--landed` runs on a no-mandate fixture record whose build filed an ask, the record
  gains an `asks-at-landing` line naming it.
  Red when: the freeze keys on the `asks:` fact alone, so a self-filed ask's answer is never frozen.
- **AC16** — When a mandated fixture ask is derived CLOSED by a CLOSED spec of this build whose
  header `closes` it, `--close` reports `asks-disposed` MET.
  Red when: the arm reds every CLOSED mandated ask, so every legitimate ask-driven run needs the
  override.
- **AC17** — When this build's CLOSED unit spec `closes` a mandated ask and this build's file also
  carries `CLOSED · <that ask> · by <the sha that unit's build_commit returns>`, T4 does not name the
  sha and the item is MET.
  Red when: T4 names a CLOSED unit's own build commit, so a run cannot record its own unit's
  evidence.
- **AC18** — When `--close` runs on four fixtures — `ASKS_CMD` set with no `asks:` fact and an empty
  F; an `asks:` fact with `ASKS_CMD` blank; a witness whose `examined` count differs from the scope;
  and a witness that sleeps past the bound — the item reads, in order, MET printing
  `nothing to dispose`; UNMET under T1 naming the preflight refusal that should have fired; UNMET as
  a DEAD PROBE; and UNMET printed as never answered, not as a red.
  Red when: a branch is omitted or inverted, so a T1 record passes as not adopted or a bound breach
  reads as a red.
- **AC19** — When a mandated `legacy` ask is BLOCKED by this build's row and no park row names it,
  the item is UNMET under T5; with a `rescope` park row whose act is in `PARK_ACTS_OWED` naming it,
  the item is MET.
  Red when: T5 admits a held ask with no owed-class park row, so a run abandons scope silently.
- **AC20** — When a mandated ask graded `yes` is held by this build's row and named by a `decision`
  park row whose reason carries neither `veto 2` nor `veto 3`, the item is UNMET; when a `yes` ask's
  hold target is an owner-call ask this run filed under its own slug, UNMET; the same self-filed hold
  on a `no` ask, with its `decision` park row, is MET.
  Red when: either F3 restriction is dropped, so a run meets the item with no delivered work.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `drift-audit records` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture run per term T0 to T5, the override, and the freeze refusal · the driver suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/unattended.sh`
New arm: `tools/unattended/check-unattended.test.sh` · a protocol copy stating "Thirteen" and one with the row removed · the leg suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`
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
- **F5 — what is T4's range under in-place landing?** Options: the plain `m-base..HEAD`; excluding
  the first parent of the first two-parent commit on HEAD's first-parent chain; excluding everything
  reachable from the advertised default tip. The first counts every default-branch commit landed
  since `m-base:` as the run's own; the second misreads a run branch that merged the default branch
  plainly. RESOLVED (agent, 2026-09-14, delegated): the third, through one library function unit 19
  shares; it restates design fix F4's 'T4's range is `m-base..HEAD`' as the run's own commits within
  it.
- **F6 — which unit's version move do this unit's drift-audit bytes ride?** S6 changes
  `tools/drift-audit/drift_report.py` and `tools/drift-audit/selftest.py`, and unit 13, ordered
  earlier, changes the same kit. Options: (a) unit 13, the first unit in build order to change
  drift-audit bytes, the rule unit 9 F9 applies to check-wiring and G4 round 1 set for run-gates;
  (b) unit 21, which rev-2 of its S8 named as the earliest to scope the move; (c) this unit moves
  `KIT_DRIFT_AUDIT_VERSION` itself. (c) breaks the build's one-owner rule, and (b) names an owner
  later than two units that change the bytes. RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator:
  (a). This unit moves no drift-audit constant, and Files touched names the move it rides.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Diverges from DR §19.5 and §19.8 U12 in three places, each by
  a ruling or a fork above: `DOD_NO_OVERRIDE` does not gain the item (D12-b); the companion guide
  moves to unit 20 (F3); and leg check 16's count-word table is extended, a need DR did not record
  and the regrounding found at `tools/unattended/check-unattended.sh:2065-2068`. Two edges not in
  the brief's table are added: consumes-from unit 15, whose TSV the witness parses, and hands-off
  unit 22 and unit 35, which DR §21.4 U20 and U15 name as moving and arming this item.
- rev-2 · 2026-09-14 · §3 §4 §5 §8 · S2 S3 · AC4 AC5 AC8 AC9 AC12 AC13 AC14 AC15 AC16 AC17 AC18 AC19
  AC20 · spec audit round 1 (G3) folded: H3 F enumerated before the witness by the P5 matcher, T2
  compares against it (AC13 to AC15); M1 T4 grades the run's own commits through one library function
  unit 19 shares (§8 F5; restates design fix F4's letter), consumes-from unit 2, hands-off unit 19;
  M2 the witness names unit 16's call shape 2; H9 `--attribute <BASE>`, consumes-from unit 1; M12
  AC8 asserts order, not adjacency; M13 AC9 names check 3; M20 the success path (AC16, AC17); M21
  AC18 to AC20 and AC4's grade and reason; L2 AC8's no-mandate and numeric-order arms. The library
  function joins the Inventory and Files touched.
- rev-3 · 2026-09-16 · spec-audit round 2 fold. It moves §3 Edges, §4 Files touched, §6 AC12 and
  §8 F6.
  - Plan c1 E38, G1 H1 (2, 24), a sibling fold from the G1 round-2 record: AC12 reads unit 1's
    `verdict clean` (unit 1 S10) and the inherited-suite filing, its `Red when:` gains the
    NEW-count-alone reading, and the §3 consumes-from edge to unit 1 names the attributed verdict in
    place of the NEW set. Fold verification then gave AC12's `Red when:` the rest of plan c1 §12's
    standard consumer text, the over-budget reading and the unfiled inherited failure, so it goes red
    on every half of unit 1 S10's criterion, as the other consumers' criteria do.
  - The fold-2 verifier problem on unit 21, kit version ownership, decided by the orchestrator and
    recorded as §8 F6: the unit first to change a kit's bytes in build order owns that kit's one
    version move, so unit 13 owns the drift-audit move. Files touched now says this unit moves no
    version constant: S6's drift-audit bytes ride unit 13's move, and its unattended bytes ride unit
    1 S9. Fold verification reworded F6's option (b) to say rev-2 of unit 21 S8 named it, because
    unit 21 S8 no longer scopes the drift-audit move.
  - Third pass, from the orchestrator's decision on the fold verifier's terminal-row exclusion
    problems (unit 19 §8 F8, a content-based run side): §4's run's-own-commits function takes one or
    more exclusion tips, because unit 19's terminal walk excludes one parent at each merge it reads.
    T4's call, with the advertised tip alone, is unchanged.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). No S-item, term or fork moves. Every
  driver and leg citation in §1, §4, §6 AC9 and §10 is re-pointed, because `unattended.sh` and
  `check-unattended.sh` grew through aDeferredBar (`1afd26c9`), aProbedUnit (`5493495a`) and
  aRatifiedRulings (`b6bbfa7b`); each cited block is byte-identical at its new line, `DOD_CORE`
  still holds twelve items, `CORE_FLOOR` still reads `12:12` and check 16's word table still stops
  at twelve. §4 Files touched names the staged map regeneration dUnstagedSymbol's pre-commit leg
  (`1a774fcd`) requires for S6's `.py`. AC1 gains a `permission:` line, because TOOL-aProbedUnit-1's
  child prompt now binds F7's no-gate rule in every pass; it places AC9's staged break in a scratch
  copy, because the build brief forbids a hand-run checker over the real tree. §10 records the
  suite-run conflict with ruling D12-h in AC12, reported and not decided, and the protocol's 1116 B
  of remaining headroom that S5's row spends.
  Extended 2026-09-20, same base, by the regrounding consolidation pass · S5 · AC1 AC10 AC12 · §7.
  AC12 gains a `permission:` line deferring the `--attribute <BASE>` suite run, and AC10 one for its
  `check-unattended.test.sh` arm, both to the one post-build bar the main loop runs at VERIFYING.
  That folds the conservative reading of the D12-h conflict and does not decide it: S7, §5 and §10
  keep the ruling's wording, and the run record parks it. S5 prices its protocol row at 200 B of the
  1116 B of headroom and AC1 reads the file's size against the 61440 B cap at the pass, because no
  cap is raised in this build. §7's two unattended `New arm:` lines name the suites' executed-
  assertion floors beside the `ARMS_FLOORS` pins; the `tools/drift-audit/selftest.py` line keeps
  `none`, because that suite pins no such floor. No criterion here asserts that a phrase counts
  zero.
  Extended again on the closing consolidation pass · S5 · §4 · §5 · §10 · AC1 AC12, with the
  header date moved to the last-change date and the rev kept. The D12-h conflict is FOLDED rather
  than decided: every attributed run in this build is read as the one the main loop makes at
  VERIFYING, so AC12's own sentence, §5's testing line and §10 stop placing it at this unit's end,
  while the ruling itself stays parked for the owner. S5's protocol row is now NET ZERO OR NEGATIVE on its carrier rather than
  priced against shared headroom. S5 names the one passage this unit trims, §4's attested-verb
  paragraph, and the verbs pair it moves into; AC1 reads both protocol copies at the pass against
  the PARENT commit's size and reds a copy that grew, a trim that deleted rather than moved, and
  a verbs copy over its own cap. The paragraph is larger than the row, so this unit FREES
  headroom for the other protocol spenders of this build instead of competing with them.
  Extended again on the close-out pass, same base and rev · §10 · AC1 AC12. AC12's `permission:`
  line takes the owed cross-edit's wording verbatim and keeps the hook clause beside it, and it now
  says which run covers the suite run: `tools/gate-legs.json` carries no leg for the unattended
  suites, so it is an attributed suite run beside the bar the main loop makes at VERIFYING and no
  bar reaches it, held flags or not. AC1 reads Rule 1 narrowly, which is how it was already meant:
  the leg's own command over a scratch copy carrying the staged break IS the pass's direct check
  under `memory/guides/BUILD-METHOD.md` M6, and only the run over the real tree defers. §10 stops
  calling the D12-h mechanics decided — the question is parked for the owner and the run folds the
  conservative reading meanwhile — and its headroom sentence follows S5's net-negative pricing
  instead of describing a share this unit no longer takes. The close-out verifier restored ruling
  D12-h's OWN words in that §10 sentence: the ruling says the suites run once at the unit's end,
  and stating it in the folded terms left the paragraph parking a conflict it had just defined
  away. AC12 and the `cost:` line are untouched.

- rev-5 · 2026-09-20 · spec-audit round 3 fold, the G3 round-2 record, which exited BOUNDED.
  §3 · §3 Edges · §4 · AC1. M3 (5): AC1's destination half read a size under a cap, which a file
  well under that cap satisfies whether the paragraph moved or was deleted, and never read
  `tools/unattended/VERBS.template.md` at all. It now counts the phrase `the only way to write one`
  at 1 in each half of the verbs pair and 0 in each protocol copy at this unit's commit, with the
  reverse at its parent, and asserts check 10 finds BOTH pairs byte-identical; its `Red when:` gains
  the one-half-only reading. The same edit gives that size criterion the LINE half of the guide cap
  beside the byte half, because `tools/memory-tree/check-memory-hygiene.sh:84` declares both. M7
  (17): §3's "writes only" sentence named one carrier where S5 and §4 Files touched mandate three,
  so it now names the protocol §4 row, the §7 byte-decision line and the `--attest` entry of the
  verbs pair. One finding is PROMOTED and folded nowhere: B1 (21), inherited here through unit 16's
  call, goes to `TOOL-dDerivedDocket-48`; §4's data-model section states the measured capture and
  points at it, §3 gains the consumes-from edge, and the parse rule, S2 and T2 keep their current
  text. No cap is raised, no term moves, and §7 does not move. The fold verifier named the witness
  for the new line-count half, `git cat-file -p <commit>:<path> | wc -l`, where the fold wrote only
  "read the same way".
- rev-6 · 2026-09-20 · §2 · S5 · the round-3 fold's verifier, repairing the M3 fold above in the
  safe direction. AC1 counts `the only way to write one` at 0 in both protocol copies at this
  unit's commit, while S5 also says §4 keeps one sentence pointing at the verb entry; a builder who
  spells that kept pointer with the moved paragraph's own opening clause performs the move
  correctly and reds the criterion. S5 now says the kept sentence does not reuse that clause, which
  makes the witness phrase unique to the destination by construction. AC1 does not move, and the
  false RED it could have produced cannot arise.

## 10. Reuse audit

The seams are the driver's own. `dod_met` in `tools/unattended/unattended.sh` is extended with one
arm, and its `pieces-complete` arm is the precedent for a term zero that is MET and announced
(`:3315-3318`). The override path is reused unchanged, and `set_fact` beside `units-at-landing` is
the freeze's write site. `reuse_lookup.py "definition of done item grading delivered asks at close"`
returns no seam in the driver, because the lookup's scan coverage reports `.sh` as an unscanned
layer, so the lookup is blind to the whole kit this unit extends. The `unattended` dossier's shared
seams, read instead, name no second DoD mechanism. Where DR and the source disagree: DR says
`DOD_NO_OVERRIDE` gains the item, which the owner's D12-b ruling reverses. DR's line citations for
`DOD_CORE`, `DOD_NO_OVERRIDE` and `units-at-landing` are `abac6d59` lines; at BASE `fb07ca25`
`unattended.sh` is 280 lines longer, and this spec cites the moved lines. No build landed in that
window adds a DoD item, an ask witness, a freeze or a run's-own-commits function: the kit library
gained only `read_brief_paths`, and `tools/drift-audit/` is byte-identical.

Two landed facts bear on this unit without moving its design. The protocol stands at 60324 B
against its 61440 B guide cap at `fb07ca25`, 1116 B of headroom that S5 no longer draws on: the row
is funded by the paragraph S5 moves out, so this unit is net negative on that carrier at its own
pass and the headroom stays whole for the build's other protocol writers. And ruling D12-h, in its own
words, lets this unit run the unattended suites once at its end (AC12), while since `5493495a`
the unit child prompt of `tools/workflows/unattended-unit.js` and M6 of
`memory/guides/BUILD-METHOD.md` forbid any self-test suite inside a pass, and
`tools/unattended/gate-guard.js` denies
`run-unattended-gates.sh` before VERIFYING. That question is PARKED for the owner — no child
prompt and no hook amends a ratified ruling — and until an owner turn takes it the run folds the
CONSERVATIVE reading, which is the one both machines already enforce: the attributed run is the one
the main loop makes at VERIFYING, after the last unit, which is what AC12 and §5 are written to.

Recall terms used: `pieces-complete DOD_NO_OVERRIDE override CORE_FLOOR units-at-landing freeze
Definition-of-Done close verb mandate scope abandonment PARK_ACTS_OWED`
