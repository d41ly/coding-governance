---
slug: aRuledFrontispiece
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-2 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-6 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11
---

# aRuledFrontispiece — the build README becomes a generated, gated surface

Node `a` · opened 2026-08-16 · streams tooling.

A build's `README.md` is the entry point of every attended and unattended build and the target of
`gen_build_index.py`, hygiene checks 2/3/9, the unattended kit's authorization path and the codebase
map. It is also, today, mostly freeform prose. One generated region carries the status table; the
document inventory, the build order, which units may run in parallel, and the edges to other builds
are either absent or hand-written beside the specs that own them.

This build inverts that ratio. The README keeps exactly one bounded block of authored prose and one
immutable authored plan; everything else is rendered from the sources that already own it.

## What the owner decided at kickoff

Eight forks were put and answered before any spec was written. They are recorded here because five
of them reverse or constrain a rule stated elsewhere in this repo, and a spec that re-litigates one
has misread this table rather than found a new option.

| # | Fork | Resolution |
|---|---|---|
| 1 | the roster's class, against `cBriefedPilot` | Option A split — the authored PLAN sits inside a `roster:units` marker pair, the DERIVED state renders outside it |
| 2 | where the format check rides | a standalone gate leg, not a delegated hygiene check |
| 3 | index-set membership and caps | IN, at 25600 bytes and 350 characters per line, with NO independent line cap |
| 4 | edge encoding | build slugs |
| 5 | verb rollout | permitted in this build, required in a follow-up commit |
| 6 | `STATUS.md` | delete the slot |
| 7 | the two LANDED run-state files | a terminal-phase carve-out in the unattended kit's check 8 |
| 8 | `LIVE.md` and the ledger | no change, which follows from fork 4 |

Fork 1 also resolves an open fork belonging to another build. `cBriefedPilot` spec-7 §8 states three
options for what may live inside the roster marker pair, recommends Option A, and records
`Resolver: owner` unresolved. The owner picked Option A here. That build's units 6, 7, 11 and 18 are
therefore compatible with this one rather than superseded by it, and no spec in this build may
render the authored plan as derived output.

## Two decisions this build must not silently reverse

`TOOL-aMouldedFolio-1` refused a front-matter SCHEMA and made `ids:` derived rather than validated,
on the ground that parity and freshness gates are TRUTH-BLIND — both stay green over a
self-consistent wrong render. `TOOL-aRuledFrontispiece-1` adds a front-matter key as its S10,
absorbed from the superseded `TOOL-aRuledFrontispiece-3`, and must state why it is not the refused
schema, or record a falsification. The superseded spec carries that argument and is where to read it.

**Below this line, every unit is named by ID, never as "unit N".** The `#` column of the Units table
is build ORDER and the id sequence is MINT order, and they stopped agreeing the moment the audit
reordered the build. An earlier version of this file used the bare word for both.

`TOOL-aMouldedFolio-2` S4 renders the FULL roster in the build README and only its COUNT in
`LIVE.md` and the ledger shards. That decision is what makes the `**Build status:**` line the widest
in the corpus, and it is the line fork 3's cap now refuses. `TOOL-aRuledFrontispiece-5` keeps the
full roster and wraps it; replacing it with a count would reverse a recorded decision and belongs in
a spec that says so.
`render_region`'s own comment says `unit(s)` and `ids` answer different questions and are
deliberately not reconciled, which is the same decision stated in the code.

**No width is quoted here on purpose.** Two independent measurements of that line during this build
disagreed by five characters, which is exactly the drift a restated number produces. Every unit reads
it from the file.

## Where the sources actually are

Both over-cap lines in the corpus are GENERATED, not authored: the `ids:` front-matter line, which
`--write` rewrites, and the `**Build status:**` line inside the region. Only
`aUnmannedHelm/README.md:78` is an authored line over the cap.

The remedy is NOT symmetric between the two, and an earlier revision of this section said it was.
Wrapping the `**Build status:**` line is a renderer change. Wrapping the `ids:` line is not: front
matter is parsed as `key: value` at column 0 by `parse_front_matter`, which refuses an indented
continuation, and `check-unattended.sh` check 13 parses the same block. That makes it a parser change
touching every reader. `TOOL-aRuledFrontispiece-5` takes a third route instead — excluding the
front-matter block from check 7's measurement, which is scoping WITHIN a file of the kind check 7
already does for fenced blocks. That route is wider than fork 3's literal words, which is why it was
parked; the owner RESOLVED it on 2026-08-16 as P2, having been told it was wider before deciding.

Check 7's 300-character budget is a single hardcoded literal in one `awk` pass over the whole index
set, so fork 3's relaxed tier cannot be a global bump — it needs a per-class cap, the same way
`guides/` already carries its own byte and line budget.

<!-- gen:build-index -->
**Build status:** OPEN · 11 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-2 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-6 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRuledFrontispiece-1 — the build README gets a slot contract and an immutable authored plan](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-1.md) | OPEN | rev-4 | 2026-08-17 |
| [TOOL-aRuledFrontispiece-10 — the corpus retrofit and the kit version bump](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-10.md) | OPEN | rev-2 | 2026-08-16 |
| [TOOL-aRuledFrontispiece-2 — build order and parallel groups become a header verb and a region](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-2.md) | WONTDO | rev-3 | 2026-08-17 |
| [TOOL-aRuledFrontispiece-3 — dependency edges between builds, declared once and rendered both ways](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-3.md) | WONTDO | rev-3 | 2026-08-17 |
| [TOOL-aRuledFrontispiece-4 — the build README gets a generated document inventory](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-4.md) | WONTDO | rev-3 | 2026-08-17 |
| [TOOL-aRuledFrontispiece-5 — the build README joins the hygiene index set at its own cap tier](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-5.md) | OPEN | rev-2 | 2026-08-16 |
| [TOOL-aRuledFrontispiece-6 — the slot contract becomes a leg of its own on the merge bar](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-6.md) | OPEN | rev-2 | 2026-08-16 |
| [TOOL-aRuledFrontispiece-7 — the STATUS.md slot is retired](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-7.md) | OPEN | rev-2 | 2026-08-16 |
| [TOOL-aRuledFrontispiece-8 — check 8 stops judging a run it can no longer repair](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-8.md) | OPEN | rev-2 | 2026-08-16 |
| [TOOL-aRuledFrontispiece-9 — the build method's roster claim and its parallelism test are corrected](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-9.md) | OPEN | rev-2 | 2026-08-16 |
| [TOOL-aRuledFrontispiece-11 — the corpus is conformed to the slot contract, by hand](spec/2026-08-17-spec-TOOL-aRuledFrontispiece-11.md) | OPEN | rev-1 | 2026-08-17 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-1.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-1.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-10.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-10.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-2.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-2.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-3.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-3.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-4.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-4.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-5.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-5.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-6.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-6.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-7.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-7.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-8.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-8.md)
  - [2026-08-16-spec-TOOL-aRuledFrontispiece-9.md](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-9.md)
  - [2026-08-17-spec-TOOL-aRuledFrontispiece-11.md](spec/2026-08-17-spec-TOOL-aRuledFrontispiece-11.md)
- **`reviews/`**
  - [2026-08-16-review-aRuledFrontispiece-1.md](reviews/2026-08-16-review-aRuledFrontispiece-1.md)
  - [2026-08-17-review-aRuledFrontispiece-2.md](reviews/2026-08-17-review-aRuledFrontispiece-2.md)
<!-- /gen:build-docs -->

## Units — the authored roster (M2)

One mechanism per unit. This table is the roster; the `ids:` key above is not.

`BUILD-METHOD.md` M2 says `ids:` "is NOT a roster — it is a reservation range written as ranges and
unions". That has been false since `TOOL-aMouldedFolio-2` made `ids:` DERIVED from the id corpus:
`--write` rewrote this build's ten authored ids down to one within a minute of the folder being
opened, and restored all ten once the sibling specs existed. The surviving id was not "the one with a
spec" — `rosters()` scans every tracked file under the memory root, excluding this build's own README
for its own slug plus `LIVE.md` and the ledger, so it was the one some OTHER tracked file named, with
a documented fallback to the authored value when the corpus names nothing. M2 and the generator are
two answers to one question, which is the class this build exists to close. **Unit 9 owns that
correction**, and states the derivation that way rather than the way this paragraph first did.

Each cell is a label. The unit's §1 Goal owns the full statement and this table deliberately does not
restate it.

Units 2 and 3 each pair an input-format change with the render that consumes it. That is one
mechanism, not two: neither half is observable alone, and a spec for the format change by itself
could not write a §6 acceptance criterion that names an observable result.

A row gains its id when its spec lands. **A planned unit may not be named by id here before then**,
and that is a measured constraint rather than a style choice: hygiene check 14 reds any id cited but
never defined, this table cited nine of them, and the orphan waiver registry is shrink-only and
already one row above its seed. The sequence number is the stable handle until the spec exists.

This is the same gap `TOOL-cBriefedPilot-6` is open against — a planned unit with no spec is
invisible — and it constrains fork 1: an authored plan cannot carry a forward id reference, so
whatever unit 2 renders as build order must key on something that exists before the spec does.

The `*pending*` placeholders this table carried while the specs were being written are gone now that
every unit has one. The constraint that produced them stands and is the reason it is recorded here
rather than forgotten.

| # | Id | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aRuledFrontispiece-1` | 2 | the generated surface — slot contract, `--check-format`, and all four regions |
| 2 | `TOOL-aRuledFrontispiece-8` | 2 | the unattended check-8 terminal-phase carve-out |
| 3 | `TOOL-aRuledFrontispiece-5` | 2 | the cap tier, the roster wrap, and the curation disposition |
| 4 | `TOOL-aRuledFrontispiece-7` | 1 | the status-file retirement |
| 5 | `TOOL-aRuledFrontispiece-9` | 2 | the build method's roster and parallelism contract |
| 6 | `TOOL-aRuledFrontispiece-11` | 2 | the corpus surgery — authored prose relocated, plans wrapped |
| 7 | `TOOL-aRuledFrontispiece-10` | 2 | the corpus re-render and the kit version bump |
| 8 | `TOOL-aRuledFrontispiece-6` | 2 | the slot contract becomes a leg on the merge bar |

**Three units were superseded at the second review round**, not abandoned. `TOOL-aRuledFrontispiece-2`,
`-3` and `-4` are `WONTDO` with a successor pointer to `-1`, and their bodies stay on disk because
they carry the design reasoning and the rejected alternatives for the three regions.

They were separate because build order, dependency edges and the document inventory are separate
AFFORDANCES. They could not be built separately because they are one MECHANISM: all four regions are
rendered by one function in one file, and every one of their acceptance criteria referenced a sibling
unit's commit tip. Two review rounds each dissolved the previous round's cross-unit contradictions
and produced a comparable number of new ones. M2 warns that two mechanisms in one spec make a pass
unreviewable; this build hit the inverse, where one mechanism split across four specs made every pass
unbuildable. Splitting finer was making it worse, so the fix was to stop splitting.

**Position 3 is after position 1 for a measured reason.** The cap tier cannot be installed before the
regions exist, because the corpus it must hold is the corpus WITH them. Installed first it would pass
over a compliant tree and red the moment the regions landed; installed after, it is measured against
what actually ships and its curation disposition is taken once, against real numbers.

**Unit 11 was created by the M4 spec audit, not planned.** The audit returned BLOCKED with seven
blockers, five of them against the retrofit unit, which had accumulated four mechanisms: wrapping
rosters, relocating prose, re-rendering, and the version bump. It also claimed authored bytes the leg
unit claimed, with no document naming the loser. Splitting the authored surgery out resolves four of
the seven and restores M2's one-mechanism-per-spec rule.

**The `#` column is BUILD ORDER and the id sequence is MINT order.** They are different questions and
this build is the case that separates them: `TOOL-aRuledFrontispiece-8` was minted eighth and builds
second. Unit 3's own §4 records the same separation from another build's corpus, where a spec named
unit 6 sits at sequence 2. Read the order from this column, never from an id.

## The order is TOTAL, and this build has no parallel lane

The order in the table above is the binding one, and it is NOT the order this section first stated.
Two authors independently showed the first ordering would have left the merge bar red across two
consecutive units, which M6 forbids: a pass whose gate is red is not followed by another.

`TOOL-aRuledFrontispiece-1` is first because it defines where a generated region may live and what an
authored region is. Everything that renders does so into that structure.

**`TOOL-aRuledFrontispiece-8` moves to second, from eighth.** Check 8 of the unattended kit
byte-compares each run-state file's copied region against its build README's `gen:build-index` slice,
and both tracked run-state files are in a terminal phase the driver refuses to re-copy. The carve-out
therefore has to land BEFORE the first unit that changes what that slice renders, which is
`TOOL-aRuledFrontispiece-5`'s wrap. Under the first ordering the bar was red from that wrap until the
carve-out three units later. The unit has no dependency on anything above it, so moving it costs
nothing.

The three region units follow, sequenced on their write set alone: they all write
`tools/memory-tree/gen_build_index.py`, which M6 clause 1 settles without needing a second argument.
Their marker pairs are distinct from `gen:build-index`, which `check-unattended.sh` extracts BY NAME,
so none of the three disturbs the carve-out's subject.

**`TOOL-aRuledFrontispiece-6` moves to last, from sixth.** The leg makes the slot contract binding,
and five build READMEs violate that contract today — including this one. A leg cannot land red, so it
cannot precede the retrofit that conforms the corpus. The alternative, folding the five relocations
into the leg's own commit, was rejected because relocating an authored marker pair is not a
re-render, and this build's rules say the retrofit commit is one.

`TOOL-aRuledFrontispiece-10` is second-to-last: it re-renders the corpus against everything above it
and carries the kit version bump, which the verdict-epoch leg requires at or after the last commit
that moves the engine.

There is a second and more interesting reason, and it is the subject of unit 9. M6 clause 3 already
names the build README and "any generated index with its generator" as shared mutable records, and
clause 2 bans two passes where one writes what the other reads as a generator input. Every spec
status header in this folder is a generator input for this folder's README, and every pass changes
one. Under M6 as written, no two passes of ANY build in this repo can run concurrently, which makes
the clause vacuous rather than strict. Unit 9 owns that rewrite. This build is its first evidence
and does not claim a parallel lane it cannot substantiate.

## Build-level rules

- **`KIT_MEMORY_TREE_VERSION` moves once, in unit 10.** The verdict-epoch leg requires the constant
  to move whenever a non-comment line of the hygiene engine moves, and seven spellings mirror it. A
  unit bumping it mid-build would date the engine's verdicts against a partial change.
- **The corpus is touched twice, by two units, and only one of those is a re-render.** An earlier
  version of this rule said the retrofit commit is "a pure re-render reviewable as `--check` output
  rather than as a 38-file diff". That stopped being true when the owner chose the position-bound
  prose contract on 2026-08-16: conforming the corpus means MOVING authored sections in a double-digit
  number of build READMEs, which no `--check` output can review and which belongs to other nodes'
  build records. Unit 9 of the order does that surgery, in one commit, touching no generated byte and
  carrying a per-file record because the diff alone is not reviewable. Unit 10 of the order is the
  re-render, and it IS reviewable as `--check` output, because by then nothing authored is moving.
- **No unit hand-inserts a generated marker pair.** `--write` creates a missing pair at its canonical
  slot. Without that, the region units would each have shipped a renderer with no call site anywhere
  in the corpus — the largest defect the first spec audit found, and one no single spec owned.
- **Two legs are RED for a declared window, and that is accepted rather than hidden.** The
  verdict-epoch leg reds from position 1 until the kit version bump at position 7, and the
  kickoff-manifest ratchet reds until its re-stamp at position 8. Both are structural: the
  verdict-epoch gate's own header states the ONE-bump-per-range convention, so a multi-unit build
  that moves the engine cannot be green on that leg at every tip, and the ratchet is discharged once
  at the end by design. M6 says a pass whose gate is red is not followed by another; read literally
  that forbids every multi-unit build this repo has ever run, which is the same over-strictness
  `TOOL-aRuledFrontispiece-9` corrects in M6's parallelism clause. **The window is declared here with
  its discharge point so a red leg inside it is expected and a red leg outside it is a defect.** No
  other leg may be red at any tip.
- **`memory/DECISIONS.md` is append-only.** A unit that reverses `TOOL-aMouldedFolio-1` or
  `TOOL-aMouldedFolio-2` mints a new id naming the record it supersedes; it never edits it.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal `non_terminal_specs_cited_by_product_source` sits at its pin with zero tolerance,
  and its globs include `tools/`, `skills/`, `.claude/` and `memory/guides/SESSION-KICKOFF.md` by
  file path. Units 6, 8 and 9 all edit files inside those globs.
- **Every unit that changes a renderer re-runs `python tools/memory-tree/gen_build_index.py --check`
  and reads the artifact count from the gate**, never from this file.

## Parked — four RESOLVED by the owner, one still open

**P1 through P4 are RESOLVED (owner, 2026-08-16), each to the option the spec already builds.** No
spec changes as a result; the parks stay recorded because a later reader needs to know these were
decided rather than defaulted, and because P2 and P3 each authorise something wider than the words
the original fork used.

**P6 · position 6 — restructuring another node's roster table.** Fork 1's Option A split, applied at
corpus scale, means moving derived columns out of roster tables inside build records owned by nodes
`b` and `c`. The first spec audit named this an owner item; it was then answered by a spec rather
than by an owner, which is how an unasked question becomes a decision nobody made. The surgery unit
proceeds on the reading that Option A authorises it, and the owner may overrule.

**P7 · position 3 — the byte tier's outlier.** The largest build README is 24715 bytes against the
25600-byte tier the owner set, and the four regions add roughly 2200. No unit may raise a number the
owner chose. The build uses the repo's existing mechanism for exactly this case — a row in the
shrink-only `memory/project/curation-debt.txt`, which is empty today — so the tier holds and the
outlier drains rather than being grandfathered by widening. Flagged because the owner set 25600
before those regions were measurable.

**P5 is still open.** It was raised and not put to the owner, so it must not be marked resolved. The
`KIT_UNATTENDED_VERSION` bump stands as the spec author wrote it until the owner says otherwise, and
it is the cheapest of the five to reverse.

Each spec author reached a decision whose options differ in WHAT GETS BUILT, not in how. M3 puts
those outside a resolver's authority with no standing mandate, so each is parked with its question,
the options seen, and the reason it was not taken. Every one is currently built the FIRST way; the
park records what it would take to change that, not a blocked unit.

**P1 · unit 4 of the order — how many directions are authored.** The spec ships ONE front-matter key
naming a build's parents and DERIVES the child set by inverting it. Authoring both directions puts
two answers to one question in two files that no leg on this bar reconciles, and `TOOL-aMouldedFolio-1`
refused exactly that shape. Refused to author both because the decision it contradicts is recorded and
binding; the author asked that an overrule be explicit rather than taken from silence.
RESOLVED (owner, 2026-08-16): one authored key, children derived. No spec changes.

**P2 · unit 6 of the order — whether front matter is measured at all.** Fork 3 set a 350-character
line cap. The `ids:` line cannot be wrapped without changing `parse_front_matter` and every reader of
it, so the spec excludes the whole front-matter block from check 7's measurement instead. That is
scoping within a file, which check 7 already does for fenced blocks, and it changes no current
verdict because no index-set member opens with front matter today. Refused to treat it as settled
because it is wider than the words the fork used.
RESOLVED (owner, 2026-08-16): exclude the front-matter block from check 7's measurement. This
widens fork 3 deliberately and the owner was told so before deciding.

**P3 · unit 10 of the order — one script or two.** The leg's argv reuses
`gen_build_index.py --check-format` rather than a new `check-build-readme.sh`. A new tracked shell
gate defining `fail()` enters `check-arms.py`'s population and demands a sibling test, a per-branch
arm and an `ARMS_FLOORS` row, and would shell out to the same Python anyway. It also happens to
satisfy the drift-audit inventory pin for free, since that path is already named in the charter's gate
suite. Refused to call this "standalone" without asking, because fork 2's word was standalone and this
is a new LEG on an existing script.
RESOLVED (owner, 2026-08-16): reuse the existing script. "Standalone" binds the LEG, not the file.

**P4 · unit 3 of the order — one verb or two.** The spec ships `order <n>` alone and makes units
sharing an order value the parallel group. A separate `group` verb creates a contradiction class —
one label spanning two steps, two labels inside one step — needing its own refusal branches to render
an identical region. Refused to ship the second verb because it buys no output; flagged because unit
8 of the order edits the build-method contract these verbs live under, and the two would conflict.
RESOLVED (owner, 2026-08-16): one `order` verb. Unit 8 of the order must not introduce a second.

**P5 · unit 2 of the order — a kit version nothing compels.** The spec bumps
`KIT_UNATTENDED_VERSION`. No gate requires it: the version check only asserts the constant and the
marker agree. The author kept it because the kit is copy-installed and two adopters would otherwise
hold the same version with different refusals. Refused to drop it silently; it is the cheapest of the
five to reverse.
