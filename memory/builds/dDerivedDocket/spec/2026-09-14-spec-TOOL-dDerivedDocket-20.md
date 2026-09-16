# TOOL-dDerivedDocket-20 — unattended carriers and the two-key refusal

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 |

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
  import allow-list (`tools/unattended/check-unattended.sh:116-120`, `:181-186`) gain
  `SHARED_RECORDS` and `GENERATED_INDEXES`, and the `__kit-default__` resolution of an undeclared
  `SHARED_RECORDS` to `$MEMORY_ROOT/DECISIONS.md $MEMORY_ROOT/backlog`
  (`tools/unattended/unattended.sh:290`, `:328`) moves into `tools/unattended/lib-unattended.sh`
  beside the predicate, so the driver and the leg resolve the default once
  (`memory/gotchas/two-readers-of-one-config-one-re-derived.md`). Observed by AC1.
- **S2** The comment at `tools/unattended/lib-unattended.sh:202-205` stops claiming that template
  section 1 mandates a backlog row. It says instead that a row is owed only by a unit planned before
  its spec (design §2.3), and that `build_commit` excludes whatever `SHARED_RECORDS` and the index
  halves of `GENERATED_INDEXES` declare, in either backlog mode. Observed by AC2.
- **S3** Protocol text, in `tools/unattended/PROTOCOL.template.md` and its installed copy, true in
  both backlog modes: the planned-unit sentence of §2's anchor ban names an ask in the run's own
  build; §11's declined disposition names an ask the run files in its own build; one paragraph
  states that every ask, disposition and header verb a run writes sits in its own folder under the
  folder slug (the charter §2 exception, design §8), and that a sequential pass may declare its own
  build's `BACKLOG.md`; one pointer names the companion guide; and §2's anchor-ban paragraph covers
  every tracked file under the run's build folder, not only the run-state file (design §19.7 layer
  1, enforced by unit 18 S3), and names the link-wrapped `--asks --ready` paste as the sanctioned
  way to cite a foreign ask. Net growth at most 300 B; if the anchor-ban sentence cannot fit, the
  paragraph keeps one sentence stating the folder-wide scope and points at the companion guide for
  the paste rule. Observed by AC3.
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
  without `--all` lists live asks only (unit 7 S12). Net growth at most 250 B and 3 lines. Observed by
  AC7.
- **S8** `tools/workflows/unattended-build.js` accepts an optional `closes` list per unit and writes
  "this unit closes <ids>; run no gate" into that unit's SPEC prompt (fix F7), with an arm in
  `tools/workflows/unattended-build.test.sh`. Observed by AC8.
- **S9** A sweep of every protocol and Skill sentence that describes ids, slugs, the prompt path or
  backlog rows, read against the driver as unit 16 leaves it; each sentence changed or kept is listed
  with its verdict in this unit's build record. The sweep record also pairs every leg rule units 16
  to 19 add with the carrier sentence that states it (G3 class item 7). Observed by AC9.
- **S10** Declarations in the same commit: the guide's row in `memory/project/method-carriers.txt`
  if it names the build method; its `guides` inventory key claimed in
  `memory/map/features/unattended.md` with the map regenerated; `ARMS_FLOORS` moved for each new
  `fail` branch. Observed by AC10.

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
  points at. Added by this spec; that unit's spec owes the matching hands-off line.
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
(`tools/unattended/unattended.sh:4773-4855`), and makes the declaration of the other meaningless.
The predicate compares the kit's own two keys and nothing else, so it lands in any adopter
unchanged. Gov declares no overlap at BASE (`.unattended.conf:206-207`), so it lands green; the
switch-over edits both keys in one commit and this is what catches a half edit.

### Wording that is true in both modes

Every sentence this unit writes must stay true while gov and every adopter are still in shards mode,
because the flip is one later commit. The table is the rule for each edit.

| Carrier sentence at BASE | Rewritten as | Phrase the criterion greps |
|---|---|---|
| M6 clause 3, "`memory/DECISIONS.md`, `memory/backlog/*.md`, the run-state file" | "`memory/DECISIONS.md`, an authored backlog shard, the run-state file": a generated view is already the clause's last case | none; AC7 counts `memory/backlog` to 0 |
| protocol §2, "a planned unit is minted as a backlog row" | a planned unit is minted as an ask in the run's own build before the run-state file names it | `minted as an ask in the run's own build` |
| protocol §11, fails 1 or 2, "a BACKLOG row naming what was seen" | an ask filed in the run's own build, carrying what was seen and why it was declined | `an ask filed in the run's own build` |
| `tools/unattended/lib-unattended.sh:202-205`, "template section 1 MANDATES a backlog row" | S2's sentence | none; AC2 counts the retired phrase to 0 |
| protocol §2 anchor ban, scoped to the run-state file's authored rows | every tracked file under the run's build folder; cite a foreign ask by the link-wrapped `--asks --ready` paste | `every tracked file under the run's build folder` |
| none at BASE: protocol, the own-folder paragraph of S3 | every ask, disposition and header verb a run writes sits in its own folder under the folder slug | `sits in its own folder under the folder slug` |
| none at BASE: protocol, the pointer of S3 | one sentence naming the companion guide | `UNATTENDED-ASKS.md` |

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

The guide exists because the protocol cannot hold this text: it is at 57815 B against the guide cap
of 61440 B (`tools/memory-tree/check-memory-hygiene.sh:84`) and at least five units of this build
add to it. Moving section 7 into `UNATTENDED-VERBS.md` is the precedent (the pair comment at
`tools/unattended/check-unattended.sh:1586-1592`).

### The build method's budget

The rendered copy is 26439 B and 337 lines against its 27648 B and 350-line budget at BASE: 1209 B
and 13 lines of headroom, both PINNED as measured at `abac6d59`. Unit 19 takes at most 300 B, this
unit at most 250 B and 3 lines, and unit 31 replaces text rather than adding a paragraph. M1 forbids
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
`memory/guides/BUILD-METHOD.md` · `tools/workflows/unattended-build.js` ·
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
  permission: this unit may not run the unattended suites; each refusal is observed by hand in the
  fixture, and the leg itself runs at the one post-build bar.
- **AC2** — When `git grep -n "MANDATES a backlog row" -- tools/unattended` runs, it returns nothing,
  and the comment above `build_commit` names the planned-before-spec rule.
  Red when: the false sentence survives beside the function whose exclusion it misstates.
- **AC3** — When both copies of the protocol are compared, `bash tools/unattended/check-unattended.sh`
  check 10 finds them byte-identical and `memory/guides/UNATTENDED-PROTOCOL.md` has grown by at most
  300 B; `git grep -c "a planned unit is minted as a backlog row"` prints 0 for each copy, and
  `git grep -c` for each phrase in §4's table prints 1 per copy, except `UNATTENDED-ASKS.md`, which
  the `ASKS_CMD` row unit 16 writes also names, and which prints at least 1.
  Red when: an edit lands in one copy only, the copy breaches the guide cap other units share, the
  retired sentence survives, or a new sentence is absent, which an empty edit under the budget would
  pass.
  permission: the leg run is observed at the one post-build bar.
- **AC4** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it reports
  `UNATTENDED-ASKS.md` installed and equal to `ASKS.template.md`, and check 10 reports the
  `UNATTENDED-ASKS.md` pair among its pairs, with a pair count equal to the length of check 10's own
  pair list; the level-2 headings of the installed `UNATTENDED-ASKS.md` are, in order, the sections
  §4 lists: routes; the mandate's six properties; orientation per ask; owner-call parking; discovery
  filing; the `asks-disposed` terms with the F3 hardening, the override route and the KEEP rule; the
  repoint rule; and the `ASKS_CMD` call shapes.
  Red when: the guide is installed with no byte-compare pair, so the adopter's copy drifts unseen, or
  the guide is empty or lacks a listed section, so unit 17's hand-off lands nowhere.
  permission: observed at the one post-build bar.
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
  the rendered copy has grown by at most 250 B and 3 lines, and
  `grep -c "memory/backlog" memory/guides/BUILD-METHOD.md` prints 0.
  Red when: M6 still names the shard directory, which reads false for a builds-mode tree, or the
  growth takes line headroom unit 19 and unit 31 were priced against.
  permission: the size leg runs at the one post-build bar.
- **AC8** — When `bash tools/workflows/unattended-build.test.sh` evaluates the harness with a unit
  carrying `closes`, the SPEC prompt for that unit contains the ids and "run no gate", and a unit
  without `closes` gets the prompt unchanged.
  Red when: the ids reach the prompt for every unit, so one unit's asks are attributed to another.
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

`unattended kit gate` · `unattended skill wiring` · `kit/dogfood doc parity` · `build-method size` · `method carriers (every pointer declared)` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `workflow script syntax` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · confs nesting a path in each direction, and one relying on the `SHARED_RECORDS` default · `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`
New arm: `tools/unattended/unattended.test.sh` · the same conf read at driver start · none, the conf-load refusal is not a `fail` branch
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
`build_commit`, which at BASE starts at line 207 with the false comment at 202-205; design §8 puts a
closeout step on `--close` here, which unit 17 absorbed; design §19.8 U12 puts the guide in the DoD
unit, which unit 17's own §8 moved here.

Recall terms used: `SHARED_RECORDS GENERATED_INDEXES build_commit dispatch condition-3 records commit
planned unit backlog row`
