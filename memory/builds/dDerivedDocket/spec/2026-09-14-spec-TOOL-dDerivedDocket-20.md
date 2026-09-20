# TOOL-dDerivedDocket-20 — unattended carriers and the two-key refusal

**Status:** SPECCED · rev-5 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 |
| [2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 |

<!-- /gen:spec-records -->

## 1. Goal

Units 15 to 19 give the unattended kit an ask mandate, a readiness grade and a completion item, but
a run reads its instructions from the Skill, the protocol and the build method, and all three still
describe backlog rows in a shared shard. Bring those carriers and one companion guide into line with
the per-build model without making any of them false for a tree still in shards mode, and add the
one refusal the kit owes its own conf: a path declared as both a shared record and a generated
index.

## 2. Scope (IN)

- **S1** One predicate in `tools/unattended/lib-unattended.sh` names every path in `SHARED_RECORDS`
  that overlaps the index half of a `GENERATED_INDEXES` pair, through the library's `overlaps`. The
  driver refuses at conf load on a non-empty answer, as its `GATE_BOUND` refusal does, and the leg
  reports it under a new check code. It reads no memory-tree state. The leg's conf initialiser and
  import allow-list (`tools/unattended/check-unattended.sh:116-121`, `:181-186`) gain
  `SHARED_RECORDS` and `GENERATED_INDEXES`, and the `__kit-default__` resolution of an undeclared
  `SHARED_RECORDS` to `$MEMORY_ROOT/DECISIONS.md $MEMORY_ROOT/backlog`
  (`tools/unattended/unattended.sh:337`, `:387`) moves into `tools/unattended/lib-unattended.sh`
  beside the predicate, so the driver and the leg resolve the default once
  (`memory/gotchas/two-readers-of-one-config-one-re-derived.md`). Observed by AC1.
- **S2** The comment at `tools/unattended/lib-unattended.sh:242-245` stops claiming that template
  section 1 mandates a backlog row. It says instead that a row is owed only by a unit planned before
  its spec (design §2.3), and that `build_commit` excludes whatever `SHARED_RECORDS` and the index
  halves of `GENERATED_INDEXES` declare, in either backlog mode. Observed by AC2.
- **S3** Protocol text, in `tools/unattended/PROTOCOL.template.md` and its installed copy, true in
  both backlog modes: the planned-unit sentence of §2's anchor ban names an ask in the run's own
  build; §11's declined disposition names an ask the run files in its own build; one paragraph
  states that every ask, disposition and header verb a run writes sits in its own folder under the
  folder slug (the charter §2 exception, design §8), and that a sequential pass may declare its own
  build's `BACKLOG.md`; one pointer names the companion guide, spelled so that it and no other
  sentence in either copy carries the phrase §4's table pins to that row, which is what AC3 counts,
  so §11's kept sentence below is free to be a second sentence naming the same file; and §2's
  anchor-ban paragraph covers
  every tracked file under the run's build folder, not only the run-state file (design §19.7 layer
  1, enforced by unit 18 S3), and names the link-wrapped `--asks --ready` paste as the sanctioned
  way to cite a foreign ask. That text adds at most 250 B per copy AND IS PAID FOR IN THE SAME
  EDIT, because no cap is raised in this build and the free space does not cover every unit that
  wants it. The passage that leaves is §11's paragraph beginning `Decide AT ONCE`, down to the
  sentence ending `because the reader it defers to is the one who left`; it MOVES into the
  DISCOVERY FILING section of the companion guide S4 creates, which §4 already lists and AC4
  already asserts by heading, so no section is added — `tools/unattended/ASKS.template.md` and
  its installed copy `memory/guides/UNATTENDED-ASKS.md`, which carry the ask contract and the
  dispositions and draw on their own 61440 B cap rather than this one. §11 keeps one sentence
  pointing there. The paragraph is larger than what this unit adds, so each protocol copy is
  SMALLER at this unit's commit than at its parent. No other unit of this build trims that
  paragraph. Observed by AC3.
- **S4** A companion guide: `tools/unattended/ASKS.template.md`, installed as
  `memory/guides/UNATTENDED-ASKS.md` by `tools/unattended/adopt-unattended.sh`, declared in the kit
  descriptor with an LF pin, and byte-compared as a pair in leg check 10 beside the protocol, verbs
  and stops pairs (unit 4 S10 adds the stops pair first). It carries the ask contract of design
  §19.2 to §19.6 as the rulings amended it, and the `asks-disposed` terms, override route and KEEP
  rule unit 17 hands off. Observed by AC4.
- **S5** Skill routing, in `tools/unattended/SKILL.template.md` and its render: a slug whose README
  carries `asks:` starts a run as today; ids, a prompt naming ids, or a filing-home slug run
  `--preflight`, relay the scaffold recipe its refusal prints, reap the keepalive and stop; a value
  mixing a slug and ids is refused before anything runs. Observed by AC5.
- **S6** Skill steps, each pointing into the guide for its rule: orientation per mandated ask,
  owner-call parking for an ask that is not ready, discovery filing with its severity row in the
  same commit, the repoint rule, the authority rule unit 19 states in the protocol, a pre-flip
  BASE, which parks with the recipe `migrate_backlog.py --recipe` prints and never relocates (design
  A10), and the rule that a scaffolded build's first spec commit deletes `status: OPEN` (unit 15
  §4), pointing at the guide's routes section, which states it. Observed by AC6.
- **S7** The build method, in `tools/memory-tree/BUILD-METHOD.template.md` and its rendered copy: one
  M2 sentence making a unit's `closes` list the only carrier of grouping; M6 clause 3 naming "an
  authored backlog shard" where it names `memory/backlog/*.md`; one M9 table row, asks filed and
  disposed, derived from `gen_build_index.py --asks --build <slug> --all`, because the table form
  without `--all` lists live asks only (unit 7 S12). That text adds at most 160 B and 2 lines AND
  IS PAID FOR IN THE SAME EDIT, on the same rule: the passage that leaves is M6's paragraph
  beginning `It takes a COMMITTED range`, down to the sentence ending `that is the next pass`,
  which is CLI prose about a memory-tree kit tool rather than a rule of the method. It MOVES
  beside that tool's own row in `tools/memory-tree/README.md`, the kit README M6 already routes
  prose to for exactly this reason, and M6 keeps one line carrying the trap and the pointer. The
  paragraph is larger in both bytes and lines than what this unit adds, so the rendered copy is
  SMALLER and SHORTER at this unit's commit than at its parent. No other unit of this build
  trims that paragraph. Observed by AC7.
- **S8** Fix F7's "run no gate" half LANDED on main and is not rebuilt here. `GROUND` tells every
  stage and every SPEC writer that no gate, suite or bar runs inside a unit pass and that the bar
  runs once at the close (`tools/workflows/unattended-build.template.js:461-463`,
  TOOL-aProbedUnit-1), and the child prompt repeats it mode-independently, overriding any section 7
  (`tools/workflows/unattended-unit.js:168-175`). The remainder is the attribution: the harness
  accepts an optional `closes` list per unit and writes "this unit closes <ids>" into that unit's
  SPEC prompt, with an arm in `tools/workflows/unattended-build.test.sh`. Since
  TOOL-dPolishedVitrine-1 that harness is RENDERED, so the edit lands in
  `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-build.js` is
  re-rendered by `bash tools/workflows/check-protocol-parity.test.sh --render` in the same commit.
  Observed by AC8.
- **S9** A sweep of every sentence in the protocol and in `tools/unattended/SKILL.template.md`
  that describes ids, slugs, the prompt path or backlog rows, read against the driver as unit 16 leaves it; each sentence changed or kept is listed
  with its verdict in this unit's build record. The sweep record also pairs every leg rule units 16
  to 19 add with the carrier sentence that states it (G3 class item 7). Observed by AC9.
- **S10** Declarations in the same commit: the guide's row in `memory/project/method-carriers.txt`
  if it names the build method; its `guides` inventory key claimed in
  `memory/map/features/unattended.md` with the map regenerated; `ARMS_FLOORS` moved for each new
  `fail` branch. Observed by AC10.
- **S11** — the version. NOT OBSERVED by a criterion here: the `unattended-build` engine's
  `meta.version`, and the `gov:kit unattended-build@` marker beside it, do not move, though S8 is
  the first edit of that kit's bytes in build order. `tools/check-kit-versions.sh` names no carrier
  for that kit, so the build-wide criterion — a value strictly greater than both BASE's and the
  `origin/main` tip's, across every carrier that script names — has an empty carrier set and nothing
  to read, and the kit reaches adopters through the `tools/workflows/` descriptor rather than
  through a version gate. Decided by the orchestrator in the regrounding consolidation pass, and
  stated rather than left silent.

## 3. Non-goals (OUT)

- Every mechanism these carriers describe is another unit's: READY, the clause grammar and `--probe`
  are unit 15's; the driver behaviour unit 16's; the DoD item unit 17's; the leg's second opinions
  unit 18's; authority unit 19's. A carrier that disagrees with its unit is fixed in the carrier.
- Gov's `.unattended.conf` does not change here. Dropping `memory/backlog` from `SHARED_RECORDS` and
  adding the two `GENERATED_INDEXES` pairs are the switch-over's (unit 34).
- The charter's unattended landing exception and its backlog wording are `PLAY-dDerivedDocket-1`'s;
  the memory-tree README and the backlog dossier are unit 36's.
- The per-item §8 fork format and M6's delegated-pass rule are unit 31's, which shares the build
  method's byte budget with this unit and unit 19.
- No closeout step on `--close`. Design §8 put one here; unit 17's `asks-disposed` item absorbed it.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-12` — `--recipe`, the text a run on a pre-flip BASE parks
  with.
- **consumes-from** `TOOL-dDerivedDocket-15` — the clause grammar, READY and `--probe` that the guide
  states as contract and orientation calls, and the rule that a scaffolded build's first spec commit
  deletes `status: OPEN`.
- **consumes-from** `TOOL-dDerivedDocket-16` — the recipe refusal, the pinned facts, `--plan --asks`
  and the UNDECIDED shape the Skill routes on.
- **consumes-from** `TOOL-dDerivedDocket-17` — the contract text for T0 to T5, the override route and
  the KEEP rule, which the guide carries.
- **consumes-from** `TOOL-dDerivedDocket-19` — the authority rule in protocol §1, which the Skill
  points at. Added by this spec; that unit's spec already carries the matching hands-off line, at
  `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-19.md:115`.
- **consumes-from** `TOOL-dDerivedDocket-18` — the folder-wide anchor ban whose carrier sentence S3
  writes.
- **consumes-from** `TOOL-dDerivedDocket-7` — the `--asks --build <slug> --all` form the M9 row
  derives from.
- **hands-off** `TOOL-dDerivedDocket-22` — the unattended-suite arms that unit's single attributed
  run executes first.
- **hands-off** `TOOL-dDerivedDocket-34` — the two-key refusal, which the switch-over's AC8 reads
  when it edits both keys in one commit.

## 4. Design

### The two-key refusal

A path in `SHARED_RECORDS` may never be declared by a pass. An index in `GENERATED_INDEXES` may be,
alone. One path in both makes `--dispatch` answer by whichever rule it reaches first
(`tools/unattended/unattended.sh:5051-5131`), and makes the declaration of the other meaningless.
The predicate compares the kit's own two keys and nothing else, so it lands in any adopter
unchanged. Gov declares no overlap at BASE (`.unattended.conf:236-237`), so it lands green; the
switch-over edits both keys in one commit and this is what catches a half edit.

### Wording that is true in both modes

Every sentence this unit writes must stay true while gov and every adopter are still in shards mode,
because the flip is one later commit. The table is the rule for each edit.

| Carrier sentence at BASE | Rewritten as | Phrase the criterion greps |
|---|---|---|
| M6 clause 3, "`memory/DECISIONS.md`, `memory/backlog/*.md`, the run-state file" | "`memory/DECISIONS.md`, an authored backlog shard, the run-state file": a generated view is already the clause's last case | none; AC7 counts `memory/backlog` to 0 |
| protocol §2, "A planned unit is minted as a backlog row" | a planned unit is minted as an ask in the run's own build before the run-state file names it | `minted as an ask in the run's own build` |
| protocol §11, fails 1 or 2, "a BACKLOG row naming what was seen" | an ask filed in the run's own build, carrying what was seen and why it was declined | `an ask filed in the run's own build` |
| `tools/unattended/lib-unattended.sh:242-245`, "template section 1 MANDATES a backlog row" | S2's sentence | none; AC2 counts `section 1 MANDATES` to 0 |
| protocol §2 anchor ban, scoped to the run-state file's authored rows | every tracked file under the run's build folder; cite a foreign ask by the link-wrapped `--asks --ready` paste | `every tracked file under the run's build folder` |
| none at BASE: protocol, the own-folder paragraph of S3 | every ask, disposition and header verb a run writes sits in its own folder under the folder slug | `sits in its own folder under the folder slug` |
| none at BASE: protocol, the pointer of S3 | one sentence naming the companion guide, spelled to carry the phrase beside it | `the ask contract and the dispositions live in` |

### The companion guide

Sections, in order: which invocation reaches which route (E1 and the E3 recipe; E2 dropped, E4 and
E5 routed to E3, design §20.1), with the rule that a scaffolded build's first spec commit deletes
`status: OPEN`; the mandate's six properties with P5 and P6; orientation per ask, including the
stale, duplicate and REOPEN records of design §19.5 and §19.6; owner-call parking, the four rows and
the park; discovery filing; the `asks-disposed` terms with the F3 hardening, the override route of
ruling D12-b and the KEEP rule of ruling D12-c; the repoint rule; the `ASKS_CMD` call shapes, from
unit 16 §4, which the protocol's §8 row points at rather than listing. The grammar and
the grades are stated once, in unit 15's module, and the guide points there rather than copying
them, because a paraphrase and its source are two answers to one question.

The guide exists because the protocol cannot hold this text: it is at 60324 B at BASE `fb07ca25`
against the guide cap of 61440 B (`tools/memory-tree/check-memory-hygiene.sh:84`), which leaves
1116 B where `abac6d59` left 3625 B, and at least five units of this build add to it. This unit
claims no SHARE of that headroom, and no cap is raised here. S3's edit is NET ZERO OR NEGATIVE on
each protocol copy: the passage it trims, §11's paragraph beginning `Decide AT ONCE`, is larger than
the text S3 adds and MOVES into the companion guide's DISCOVERY FILING section, so each copy is
smaller at this unit's commit than at its parent, which is what AC3 compares against rather than a
declared allowance. The companion guide S4 adds is a NEW file
carrying its own 61440 B cap, so it draws nothing from this headroom. Moving section 7 into
`UNATTENDED-VERBS.md` is the precedent (the pair comment at
`tools/unattended/check-unattended.sh:1624-1630`).

### The build method's budget

The rendered copy is 27264 B and 347 lines against its 27648 B and 350-line budget at BASE
`fb07ca25`: 384 B and 3 lines of headroom, both measured there, where `abac6d59` left
1209 B and 14 lines. aRatifiedRulings, aDeferredBar and aProbedUnit spent the difference. NO CAP IS
RAISED in this build — moving M1's budget is an owner turn under veto 2 — and no SHARE of that
headroom is claimed here. S7's edit is NET ZERO OR NEGATIVE on the rendered copy: the passage it
trims, M6's paragraph beginning `It takes a COMMITTED range`, is larger in both bytes and lines than
what S7 adds and MOVES beside that tool's own row in `tools/memory-tree/README.md`, so the copy is
smaller and shorter at this unit's commit than at its parent, which is what AC7 compares against.
Only the byte half binds, because no checker reads the line half of that budget row
(`tools/template-size-limits.txt:84-85`). M1 forbids
stating any rule twice, so the M2 sentence is the only place the grouping rule is written; the guide
points at M2.

### Fail codes and self-tests

The leg's branch takes a new check code, allocated at build time as the next free integer, because
other units of this build allocate codes concurrently. This unit is not in the build's self-test
list, so each new branch is observed RED by hand in a scratch fixture repo with a local bare remote
(ruling D12-h, method b), and the unattended-suite arms run first in unit 22's attributed run (its
AC13); no bar leg runs those suites (§8 F4).

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| the two-key predicate | kit library shell function | lexicon shell function cell, checked with `lexicon.py --suggest` |
| `ASKS.template.md`, `UNATTENDED-ASKS.md` | kit template and installed guide | none |
| `closes` | a per-unit field of the build harness's `units` argument | JavaScript property, lower case as its siblings |
| one leg check code | integer | allocated at build time |

### Files touched (estimate)

`tools/unattended/lib-unattended.sh` · `tools/unattended/unattended.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.test.sh` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `tools/unattended/ASKS.template.md` (new) ·
`memory/guides/UNATTENDED-ASKS.md` (new) · `tools/unattended/adopt-unattended.sh` ·
`tools/unattended/kit.toml` · `tools/unattended/SKILL.template.md` ·
`.claude/skills/unattended/SKILL.md` · `tools/memory-tree/BUILD-METHOD.template.md` ·
`memory/guides/BUILD-METHOD.md` · `tools/memory-tree/README.md`, where S7's moved paragraph
lands · `tools/workflows/unattended-build.template.js` ·
`tools/workflows/unattended-build.js` ·
`tools/workflows/unattended-build.test.sh` · `memory/project/method-carriers.txt` ·
`memory/map/features/unattended.md` · `memory/map/generated/` · `.memory-tree.conf` for
`ARMS_FLOORS`.

### Alternatives rejected

- **Rewrite the carriers for builds mode only.** Every shards-mode reader, gov included until the
  switch-over, would be told something false.
- **Put the ask contract in the protocol.** It does not fit under the guide cap, and the verbs guide
  is the precedent for moving a section out.
- **The refusal in the driver only.** The bar would then say nothing about a conf that no run has
  read yet.

## 5. Production-readiness checklist

- security — no new write path. The refusal narrows what a contradictory conf can make `--dispatch`
  accept; the carriers tell a run to execute a `seen` command only through `--probe`.
- perf / scale — one comparison of two short lists at conf load and on the leg.
- error / empty / loading states — the refusal names each overlapping pair; an undeclared
  `SHARED_RECORDS` resolves to its kit default in both callers; a blank `GENERATED_INDEXES` compares
  as an empty set.
- observability — the refusal line, and the sweep's list of sentences in the build record.
- risks — a carrier sentence can still disagree with its unit's code; the sweep reads them against
  the driver once, and leg check 10 checks copies against copies, never against the code.
- testing — arms for both new branches observed by hand; the harness arm in its own suite; the
  unattended-suite arms run first in unit 22's attributed run (its AC13); the byte-compare legs and
  `kit/dogfood doc parity` at the post-build bar.
- migration — a new guide file every adopter receives on upgrade, and nothing else changes shape.
- user docs — this unit IS the user-facing docs for the unattended ask path.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture's conf declares `memory` in `SHARED_RECORDS` and a
  `GENERATED_INDEXES` pair whose index half is `memory/LIVE.md`; separately, the reverse nesting,
  `memory/LIVE.md` shared and `memory` as an index half; and separately leaves `SHARED_RECORDS`
  undeclared with a `GENERATED_INDEXES` pair over `memory/backlog`:
  `bash tools/unattended/unattended.sh --status` refuses at conf load naming both keys in each case,
  and `bash tools/unattended/check-unattended.sh` reports the new check in each; with gov's conf both
  are silent.
  Red when: the predicate compares strings for equality, so both nested pairs pass, or the leg reads
  the undeclared key as empty, so the driver refuses a conf the bar passes.
  permission: the three fixture cases are the pass's OWN direct check — the driver's and the leg's
  own commands over a scratch fixture conf, which `memory/guides/BUILD-METHOD.md` M6 sanctions and
  `tools/unattended/gate-guard.js` admits, because neither is a suite FILE invocation. What defers
  is the gov-conf half, which is the leg over the REAL tree: it is read at the bar the main loop
  makes at VERIFYING, after the last unit, where `unattended kit gate` runs unheld. This unit runs
  no unattended suite in the pass.
- **AC2** — When `git grep -n "section 1 MANDATES" -- tools/unattended` runs, it returns nothing, and
  the comment above `build_commit` names the planned-before-spec rule. That phrase, not rev-2's
  `MANDATES a backlog row`: the sentence wraps between `MANDATES a` and `backlog row` at
  `tools/unattended/lib-unattended.sh:242-243`, so the longer grep already matched nothing at BASE
  and was a criterion that could not fail.
  Red when: the false sentence survives beside the function whose exclusion it misstates, or the grep
  phrase spans a line break again, so the arm passes over unchanged prose.
- **AC3** — When both copies of the protocol are compared, `bash tools/unattended/check-unattended.sh`
  check 10 finds them byte-identical, and `git cat-file -s` run at this unit's parent and at its
  commit reports a SMALLER size at the commit for `memory/guides/UNATTENDED-PROTOCOL.md` and for
  `tools/unattended/PROTOCOL.template.md`, each also under the 61440 B guide cap and under the
  750-line half `tools/memory-tree/check-memory-hygiene.sh:84` declares beside it;
  `git grep -c "deferred costs the whole finding"` prints 1 for the installed
  `UNATTENDED-ASKS.md` and 0 for each protocol copy, so §11's paragraph moved rather than
  being deleted; `git grep -c "minted as a backlog row"` prints 0 for each copy, and
  `git grep -c` for each phrase in §4's table prints 1 per copy at this unit's commit, the pointer
  row's `the ask contract and the dispositions live in` among them, and that one phrase prints 0 per
  copy at its parent, the same parent comparison this criterion already makes for bytes. The bare
  `UNATTENDED-ASKS.md` string is deliberately out of this criterion: the `ASKS_CMD` row unit 16
  writes names the same file, and §11's kept sentence may name it a second time, so no count of it
  distinguishes a pass that wrote S3's pointer sentence from one that did not.
  Red when: an edit lands in one copy only, the copy breaches the guide cap other units share, the
  retired sentence survives, or a new sentence is absent, which an empty edit under the budget would
  pass; or the retired-sentence grep is re-tightened to a phrase that leads with the lower-case `a`
  of `a planned unit`, which the protocol spells `A` at the head of its sentence
  (`memory/guides/UNATTENDED-PROTOCOL.md:256`), so the count is 0 before the unit does anything; or
  a copy is the same size or LARGER at this unit's commit than at its parent, so this unit spent
  headroom unit 19 and this build's other protocol writers are priced against instead of funding
  its own text, which is why the comparison is against the parent commit rather than against a
  declared share; or §11's paragraph was DELETED rather than moved, so the contract lost a rule
  and the carrier shrank for the wrong reason; or the pointer row is graded by counting the bare
  `UNATTENDED-ASKS.md` string, which the earlier-ordered unit 16 already writes into the same table,
  so a pass that never writes S3's pointer sentence passes green; or the pinned phrase is one
  §11's kept sentence also carries, so a correct pass lands 2 per copy and the criterion reds on a
  correct build.
  permission: the leg run is observed at the one post-build bar the main loop runs at VERIFYING,
  after the last unit; the byte count and both greps are read in the pass.
- **AC4** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it reports
  `UNATTENDED-ASKS.md` installed and equal to `ASKS.template.md`, and check 10 reports the
  `UNATTENDED-ASKS.md` pair among its pairs, with a pair count equal to the length of check 10's own
  pair list; `wc -c` on the installed guide reads under the 61440 B guide cap
  (`tools/memory-tree/check-memory-hygiene.sh:84`), which it carries as a new file of its own; the
  level-2 headings of the installed `UNATTENDED-ASKS.md` are, in order, the sections
  §4 lists: routes; the mandate's six properties; orientation per ask; owner-call parking; discovery
  filing; the `asks-disposed` terms with the F3 hardening, the override route and the KEEP rule; the
  repoint rule; and the `ASKS_CMD` call shapes.
  Red when: the guide is installed with no byte-compare pair, so the adopter's copy drifts unseen, or
  the guide is empty or lacks a listed section, so unit 17's hand-off lands nowhere, or it lands over
  the guide cap this build may not raise.
  permission: `bash tools/unattended/adopt-unattended.sh --check` is the `unattended skill wiring`
  leg's own argv and check 10's pair count is the `unattended kit gate` leg over the real tree, and a
  pass runs no gate leg, so both runs are observed at the one post-build bar the main loop runs at
  VERIFYING, after the last unit. The hook admits the verb, but the child prompt of
  `tools/workflows/unattended-unit.js` bans a GATE inside a pass whether or not the hook sees it. In
  the pass the installed guide's headings and the `wc -c` byte count are read straight off the tree,
  and the install is observed by comparing the installed file with `ASKS.template.md` by hand.
- **AC5** — When the rendered Skill is read, its routing table carries a row sending ids, a prompt
  naming ids, and a filing-home slug to the recipe `--preflight` prints, and its opening fence
  refuses a value mixing a slug and ids.
  Red when: a prompt naming ids still routes to the prompt path, where the run writes its own
  mandate and ruling D12-a is bypassed.
- **AC6** — When the rendered Skill is read, every orientation, parking and filing step names the
  guide section it follows, and the pre-flip step names `migrate_backlog.py --recipe` and forbids
  `--relocate`.
  Red when: a step restates a rule the guide or the protocol holds, so two carriers answer one
  question.
- **AC7** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs it passes,
  `git cat-file -s` run at this unit's parent and at its commit reports a SMALLER size at the
  commit for `memory/guides/BUILD-METHOD.md` and for `tools/memory-tree/BUILD-METHOD.template.md`,
  the rendered copy also under the 27648 B declared at `tools/template-size-limits.txt:86`;
  `wc -l` over the rendered copy at those same two commits reports FEWER lines at the commit and
  under the line budget its own `**Budget:` line declares;
  `grep -c "memory/backlog" memory/guides/BUILD-METHOD.md` prints 0; and
  `grep -c "resolves to an empty range" tools/memory-tree/README.md` prints 1, so M6's paragraph
  moved rather than being deleted.
  Red when: M6 still names the shard directory, which reads false for a builds-mode tree; or the
  rendered copy is the same size or LARGER at this unit's commit than at its parent, so this unit
  spent byte headroom unit 19 and unit 31 are priced against; or its line count holds or grows,
  which NO checker would catch (`tools/template-size-limits.txt:84-85`) and which is how that
  document reaches a budget no unit of this build may raise; or M6's paragraph was DELETED rather
  than moved, so the trap it states reaches nobody.
  permission: the size leg runs at the one post-build bar the main loop runs at VERIFYING, after the
  last unit; the byte counts, the line counts and both greps are read in the pass.
- **AC8** — When `bash tools/workflows/unattended-build.test.sh` evaluates the harness with a unit
  carrying `closes`, the SPEC prompt for that unit contains the ids, and a unit without `closes` gets
  the prompt unchanged; `bash tools/workflows/check-protocol-parity.test.sh --check` reports the
  template and its rendered copy identical.
  Red when: the ids reach the prompt for every unit, so one unit's asks are attributed to another; or
  the edit lands in the rendered `tools/workflows/unattended-build.js` alone, which the
  `review-protocol parity (kit vs dogfood)` leg reds and the next `--render` silently reverts.
  permission: `bash tools/workflows/check-protocol-parity.test.sh --check` carries a read-only verb,
  which `tools/unattended/gate-guard.js` admits, so it is the pass's own direct check, and the same
  file runs as the `review-protocol parity (kit vs dogfood)` leg at the one post-build bar.
  `tools/workflows/unattended-build.test.sh` is run by NO bar leg: no row of `tools/gate-legs.json`
  names it at BASE, which the open ask `TOOL-dBriefedPass-7` records and unit 29 §3 states, and a
  bare suite run is denied before VERIFYING, so its `closes` arm is observed by hand at VERIFYING,
  after the last unit, in the same run that makes the post-build bar.
- **AC9** — When this unit's sweep record under `memory/builds/dDerivedDocket/build/` is read, it
  lists every protocol and Skill sentence naming ids, slugs, the prompt path or backlog rows, each
  with kept or changed and the driver behaviour it was read against, and a second list pairing each
  leg rule units 16 to 19 add with its carrier sentence.
  Red when: the sweep is claimed with no list, which is an assertion with no observation behind it,
  or a leg rule has no carrier sentence.
- **AC10** — When `python3 tools/codebase-map/test_codebase_map.py` and
  `bash tools/memory-tree/check-method-carriers.sh` run, both pass with the guide tracked.
  Red when: the new `guides` key is unclaimed, or the guide names the build method undeclared.
  permission: both are gate legs, observed at the one post-build bar.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit/dogfood doc parity` · `build-method size` · `method carriers (every pointer declared)` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · confs nesting a path in each direction, and one relying on the `SHARED_RECORDS` default · the leg suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`
New arm: `tools/unattended/unattended.test.sh` · the same conf read at driver start · the driver suite's executed-assertion floor; `ARMS_FLOORS` does not move, because the conf-load refusal is not a `fail` branch
New arm: `tools/workflows/unattended-build.test.sh` · a unit carrying `closes` and one without · none

## 8. Open questions

- **F1 — where does the two-key refusal fire?** Options: (a) the leg only, which spec 34's AC8 reads;
  (b) the driver only; (c) both, through one library predicate. (a) lets a run start on a
  contradictory conf; (b) lets the bar pass one no run has read. RESOLVED (agent, 2026-09-14,
  delegated): (c).
- **F2 — where does the ask contract live?** Options: the protocol, or a companion guide. RESOLVED
  (agent, 2026-09-14, delegated): the companion, as design §19.8 U12 proposed and unit 17 handed off,
  because the protocol cannot hold it under its cap.
- **F3 — the stale sentences design §19.8 U14 cites from the contract reader's report §8.** That
  report is untracked scratch, so its list cannot be read. RESOLVED (agent, 2026-09-14, delegated):
  S9's sweep re-derives the list from the carriers against the driver, recorded sentence by sentence.
- **F4 — which stage first executes this unit's unattended-suite arms?** Options: (a) add this unit
  to the build's self-test list; (b) unit 22's single `run-unattended-gates.sh --attribute <BASE>`
  run, the next permitted run after this unit; (c) the landing's compensating check, which is on
  demand and bound to no unit. (a) contradicts owner rulings D12-h and D12-i8, which name the
  permitted units, so it is not an option here; (c) guarantees neither execution nor attribution
  before landing. RESOLVED (agent, 2026-09-14, delegated): (b), with a hands-off to unit 22.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from design §8, §19.6 and §19.8 U4 and U14, fix F7, and the
  companion guide unit 17 moved here. Adds consumes-from units 12, 15 and 19, not in the brief's
  table; units 12 and 15 carry the matching lines, and unit 19's spec owes one.
- rev-2 · 2026-09-14 · §3 §4 §5 §7 §8 · S1 S3 S4 S6 S7 S9 · AC1 AC3 AC4 AC9 · spec audit round 1
  (G3) folded: M4 the protocol's anchor ban covers the whole folder, S9 pairs leg rules with carriers,
  consumes-from unit 18; M5 the unattended-suite arms run first in unit 22's attributed run (§8 F4),
  hands-off unit 22; M6 hands-off unit 34; M7 the leg imports both keys, the default resolved once in
  the library; M24 AC1 nests pairs both ways; M25 AC3 phrase greps through §4's new column, AC4
  headings; L5 the M9 row names `--all`, consumes-from unit 7; L6 AC4 asserts the pair's presence;
  H10 one Skill step deleting the scaffold's `status: OPEN`, stated in the guide's routes section; M2
  the guide lists the `ASKS_CMD` call shapes. The guide's section names no count of shapes, because
  unit 16 §4 also names unit 24's read-back (G4 L2); AC3's pointer phrase counts at least 1, because
  unit 16's protocol row names the guide too; AC1 and AC4 cite the installed guide and the index
  half without an untracked path, so the spec-token join stays clean.
- rev-3 · 2026-09-20 · regrounded on fb07ca25 (origin/main). §2 §4 §7 §10 · S1 S2 S8 · AC2 AC8.
  Citations that moved under the aRatifiedRulings,
  dPolishedVitrine, aDeferredBar, aReplayedCard and aProbedUnit merges, each block byte-identical at
  its new line: S1's `__kit-default__` init and resolution to `tools/unattended/unattended.sh:337`
  and `:387`; S2's and §4's false `build_commit` comment to
  `tools/unattended/lib-unattended.sh:242-245`, with `build_commit` itself now at `:247`; §4's
  condition-3 block to `tools/unattended/unattended.sh:5051-5131`; the verbs-pair comment to
  `tools/unattended/check-unattended.sh:1624-1630`; and gov's two keys to `.unattended.conf:236-237`.
  S1's leg-initialiser range is corrected to `tools/unattended/check-unattended.sh:116-121`, which
  did not move and was one line short at rev-2. `overlaps` is still at
  `tools/unattended/lib-unattended.sh:105` and the allow-list still at `:181-186`.
  S8 becomes a pointer plus its remainder: TOOL-aProbedUnit-1 and TOOL-aDeferredBar-1 landed fix F7's
  "run no gate" half in `GROUND` at `tools/workflows/unattended-build.template.js:461-463` and in the
  child prompt at `tools/workflows/unattended-unit.js:168-175`, so this unit builds only the `closes`
  attribution. TOOL-dPolishedVitrine-1 made that harness RENDERED from
  `tools/workflows/unattended-build.template.js`, declared at `tools/workflows/kit.toml:60-62`, so the
  edit lands in the template and is re-rendered in the same commit; §4 Files touched names the
  template, §7 gains `review-protocol parity (kit vs dogfood)`, the leg that grades the pair, and AC8
  reads the pair rather than the landed "run no gate" text.
  AC2's grep is corrected from `MANDATES a backlog row` to `section 1 MANDATES`: the sentence wraps
  between the two words, so rev-2's phrase matched nothing at either base and the criterion could not
  fail. §4's table row follows.
  Both shared budgets are re-measured at BASE. BUILD-METHOD is 27264 B and 347 lines of 27648 B and
  350, leaving 384 B and 3 lines where `abac6d59` left 1209 B and 14; the protocol is 60324 B of
  61440 B, leaving 1116 B where it left 3625 B. This unit's 250 B and unit 19's 300 B no longer both
  fit under BUILD-METHOD, which §4 states and which the orchestrator settles.
  Verification pass, same regrounding: AC3 carried the SAME could-not-fail shape AC2 did, by case
  rather than by a wrap. The protocol spells the sentence `A planned unit is minted as a backlog row`
  at `memory/guides/UNATTENDED-PROTOCOL.md:256`, so rev-2's lower-case `a planned unit is minted as a
  backlog row` counted 0 at both bases; AC3 now greps `minted as a backlog row`, which counts 1 per
  copy at BASE, its Red-when names the case class, and §4's table quotes the sentence as spelled. The
  verbs-pair comment is at `tools/unattended/check-unattended.sh:1624-1630`, not `:1623-1629`
  (`:1623` is the `PREFIX=` assignment); the same off-by-one rode in from rev-2's `:1586-1592`, whose
  comment began at `:1587`.
  Extended 2026-09-20, same base, by the regrounding consolidation pass · §2 S3 S7 S11 · §4 · AC3
  AC4 AC7 AC8 · §7. The two capped carriers are TRIMMED to fit rather than left oversubscribed,
  because no cap is raised in this build: S7 falls from 250 B and 3 lines to 160 B and 2 lines
  against BUILD-METHOD's 384 B, beside unit 19's cut to 120 B, which leaves 104 B for unit 31; S3
  falls from 300 B to 250 B against the protocol's 1116 B, beside unit 19's cut to 350 B. AC7, AC3
  and AC4 now read each file's SIZE against its cap at the pass, the new companion guide included,
  as well as its growth. §4's two budget paragraphs state both splits.
  S11 says what the silence used to: this unit is the first in build order to change
  `unattended-build` bytes and moves no version, because `tools/check-kit-versions.sh` names no
  carrier for that kit, so the build-wide version criterion has nothing to read. That is the
  orchestrator's decision, recorded here in unit 37 S9's shape.
  AC8's `permission:` line stops calling both of its commands suites that a bar runs: the
  `--check` form is a read-only verb `tools/unattended/gate-guard.js` admits and is the pass's own
  check, while `tools/workflows/unattended-build.test.sh` is named by no row of
  `tools/gate-legs.json` and is observed by hand at VERIFYING. AC4's line went the other way on the
  verifier's read: `adopt-unattended.sh --check` is the `unattended skill wiring` leg's own argv, so
  the no-gate rule the child prompt states reaches it whatever the hook sees, and its run stays at
  the post-build bar beside check 10's; only the headings and the byte count are read in the pass. §7's two unattended `New arm:` lines name the suites'
  executed-assertion floors, which both suites pin, in place of a bare `ARMS_FLOORS` note and a bare
  `none`; the `unattended-build.test.sh` line keeps `none`, because that suite pins no such floor.
  AC2's, AC3's and AC7's zero-count phrases were re-run at HEAD in this pass: `section 1 MANDATES`
  hits once, `minted as a backlog row` once per protocol copy and `memory/backlog` once in the
  rendered build method, so each criterion can now fail and none is green before the unit acts.
  Extended again on the closing consolidation pass · S3 S7 · §4 · AC3 AC7. Trimming the two
  shares to fit was not enough, because a share is a claim about a build-wide sum and neither
  sum closed. Both carriers are now NET ZERO OR NEGATIVE at this unit's own pass, funded inside
  the same edit: S3 names §11's `Decide AT ONCE` paragraph, which MOVES into the companion guide
  S4 creates and which draws on its own cap, and S7 names M6's `It takes a COMMITTED range`
  paragraph, CLI prose about a memory-tree tool, which MOVES beside that tool's row in
  `tools/memory-tree/README.md`. Each keeps a pointer line where it stood, and each is larger
  than what this unit adds, so both spenders it used to compete with get headroom back instead.
  AC3 and AC7 compare every carrier copy against this unit's PARENT commit rather than against a
  budget, AC7 counts the build method's LINES itself because no checker reads that half, and
  each names the destination phrase so a DELETION cannot pass as a move. Both destination
  phrases were counted at HEAD and return 0 there, so neither criterion is green before the unit
  acts. §4 Files touched gains the memory-tree README.
  Extended again on the close-out pass, same base and rev · AC1. Rule 1 reads narrowly here, which
  is how the criterion was always meant: the driver and leg commands run over AC1's scratch fixture
  conf ARE the pass's direct check under `memory/guides/BUILD-METHOD.md` M6, and what defers is the
  gov-conf half, the same leg over the real tree, which the bar the main loop makes at VERIFYING
  covers unheld. Nothing else moved. No `permission:` line in this spec names a held leg: every leg
  §7 lists resolves in `tools/gate-legs.json` with a subject of `repo` and a chunk outside
  `selftests`, so a plain bar reaches each of them and no flag clause is owed.
- rev-4 · 2026-09-20 · §4 · AC3 · the spec-audit round 3 fold, the G3 round-2 record, which
  exited BOUNDED. Recorded as its own entry with a single bump rather than as an extension of the
  rev-3 line: the five sibling specs of this group took that form for the same fold, and a reader
  must be able to tell from the header that a round-3 pass touched this spec. M6 (14): §4's two budget paragraphs still priced this unit's edits as SHARES
  of free space — 250 B of the protocol's 1116 B, 350 B attributed to unit 19, 160 B of the build
  method's 384 B with 104 B left over — although the closing consolidation pass had already made S3
  and S7 net-zero-or-negative and moved AC3 and AC7 to a parent comparison. Both paragraphs are
  rewritten to that rule: each names the passage its edit trims, says it is larger than what the
  unit adds, and claims no share; the share arithmetic and the sentence parking the build-wide sum
  with the orchestrator are gone, because the fold that closed the question preceded them. The
  measured BASE figures stay as the reason the companion guide exists, and unit 19's own §4 Budgets,
  which hands its headroom back rather than claiming 350 B, is no longer contradicted here. M8 (35):
  AC3's `UNATTENDED-ASKS.md` clause accepted `at least 1`, which the `ASKS_CMD` row the
  earlier-ordered unit 16 writes already satisfies, so a pass that never wrote S3's pointer sentence
  passed green. It now asserts the count is exactly ONE MORE in each protocol copy at this unit's
  commit than at its parent, the shape AC3 already uses for bytes, and its `Red when:` names the
  sibling-supplied string. That SUPERSEDES rev-2's record of `at least 1` as the accepted reading.
  No S-item moves, no cap is raised, §7 does not move, and no finding of this record is promoted
  out of this spec.
  One format correction rides along: AC3's protocol clause read the byte half of the guide cap
  alone, and `tools/memory-tree/check-memory-hygiene.sh:84` declares a 750-line half beside it,
  so that clause now reads both.
- rev-5 · 2026-09-20 · §2 · S3 · §4 · AC3 · the round-3 fold's verifier, repairing the M8 fold
  above. That fold made AC3 assert exactly ONE MORE `UNATTENDED-ASKS.md` per protocol copy at the
  commit than at the parent, which is the mandated delta only if S3 mandates exactly one new
  mention. S3 mandates a pointer sentence AND keeps a §11 sentence pointing at the same guide, so a
  correct pass can land +2 and red a criterion. AC3 now grades the pointer row by a phrase unique to
  that sentence, `the ask contract and the dispositions live in`, at 1 per copy at the commit and 0
  at the parent, and the bare `UNATTENDED-ASKS.md` string leaves the criterion entirely, since unit
  16's `ASKS_CMD` row and §11's kept sentence both name the same file. §4's phrase table carries the
  new phrase in the pointer row, which was the one row with no phrase of its own, and S3 says the
  pointer sentence is spelled to carry it and that §11's kept sentence is deliberately uncounted.
  This was the review's own first option, which the M8 fold did not take.

## 10. Reuse audit

The seams are the kit's own: `overlaps` in `tools/unattended/lib-unattended.sh:105`, the `GATE_BOUND`
conf-load refusal in `tools/unattended/unattended.sh`, leg check 10's pair loop, and the verbs
guide's install and descriptor rows, which the companion guide copies. `python
tools/codebase-map/reuse_lookup.py "refuse a path declared under two conf keys"` returned `load_conf`,
`ConfError` and `parse_conf` in other kits and reports `.sh` unscanned, so no shell seam was visible
to it; the source was read instead. Recall returned `TOOL-aLeakedHandle-5`, a pass that could not
file a backlog row because `memory/backlog` is a shared record, which is the blocked filing S3's
paragraph removes, and `TOOL-dBriefedPass-3`, which is why the build commit's exclusion set matters.

Where the design and BASE disagree: design §8 cites `tools/unattended/lib-unattended.sh:197-220` for
`build_commit`, which at BASE `fb07ca25` starts at line 247 with the false comment at 242-245, having
started at 207 with the comment at 202-205 when the design was written; design §8 puts a closeout
step on `--close` here, which unit 17 absorbed; design §19.8 U12 puts the guide in the DoD unit,
which unit 17's own §8 moved here.

BASE is `fb07ca25`, origin/main, which HEAD `94fd2f54` merges without changing code. From `abac6d59`
to it, the seams this unit extends kept their shapes and moved lines only: `overlaps`, the two-key
init and resolution, condition 3's flat and nested halves, check 10's pair loop and the leg's
allow-list. Nothing landed that refuses a path declared under both keys, and gov's own conf still
declares no overlap, so S1 lands green as it did. Two landings reach this unit's carriers.
TOOL-dPolishedVitrine-1 made `tools/workflows/unattended-build.js` a RENDERED copy of
`tools/workflows/unattended-build.template.js`, and its round-1 F4 (`2814aaa5`) left the
`review-protocol parity (kit vs dogfood)` leg unguarded in both carriers so it runs on every bar;
S8, §4 Files touched and §7 follow. TOOL-aProbedUnit-1 and TOOL-aDeferredBar-1 landed fix F7's
"run no gate" sentence in `GROUND` and in the child prompt, which S8 now points at instead of
rebuilding. The same landings put a rule this unit must not contradict in front of its own
criteria: BUILD-METHOD M6 and `tools/unattended/gate-guard.js` deny a self-test suite or the bar
inside a pass before VERIFYING, while owner rulings D12-h and D12-i8 let a unit run the unattended
suites at its end. §4's fail-codes paragraph, §5 testing and §8 F4 are left exactly as the fork
resolved them; the conflict is build-wide, reported rather than decided here, and the run defers
every such observation to the VERIFYING run.

Recall terms used: `SHARED_RECORDS GENERATED_INDEXES build_commit dispatch condition-3 records commit
planned unit backlog row`
