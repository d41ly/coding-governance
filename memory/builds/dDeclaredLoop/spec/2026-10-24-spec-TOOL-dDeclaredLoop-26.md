# TOOL-dDeclaredLoop-26 — a build's composition pinned per step, its position read at the pin, and the move at the next step boundary

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 23 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0111@313dbc9c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A build runs each step under the composition it entered that step with, and moves to a newer one only
at its next step boundary, so an update or an overlay change landing mid-step never changes what the
build is doing (the owner's FA-7, "Next step boundary (Recommended)",
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:376`).
Today nothing pins a build to a composition and every reader takes the landed tip
(`memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md:33`).

## 2. Scope (IN)

- **S1** — The composition revision (I17): the full sha of the commit the composition is read from,
  which is the default branch's landed revision dGroundRules-2 S1's `derive_landed_revision` returns at
  the moment of the transition, written as its first eight hex digits or more. At that commit the
  overlay is the blob `.governance/instructions.toml` (dOrderedCharter-46 S1) and gov's packs are the
  `population` files of every `[[kind]]` row of `tools/playbook/kinds.toml` (dOrderedCharter-7 S4).
  One function, `derive_composition_revision(root)`, in the new module `tools/loop/composition.py`.
  Observed by AC5.
- **S2** — The pin. `composition` joins `TRANSITION_FIELDS` in `tools/loop/loop_transition.py`
  (TOOL-dDeclaredLoop-3 S1), so every transition record into a step carries ` · composition=<sha8>` on
  its trailer and its log record's `Composition` field, written through `write_transition`'s
  `--field composition=<value>` and read back through `read_transitions`. This unit computes the value
  and adds no channel. Observed by AC5.
- **S3** — The read at the pin. `read_step_composition(root, build)` returns the composition revision of
  the build's latest transition record into its current step, and `compose_at(root, rev)` composes
  every registered kind's rows from the blobs at that commit, passing the overlay through
  dOrderedCharter-46 S3's candidate read and composing through dOrderedCharter-35's `compose_rows`.
  TOOL-dDeclaredLoop-7's engine, `derive_position` in `tools/loop/position.py`, reads its definition
  rows through `compose_at` at that revision, never at the tip, for every item inside the step.
  Observed by AC1.
- **S4** — The move. At the next transition into a step the record pins the newer revision, and the
  witnesses of items the build held under the older one carry across through the change records'
  successors: an item tag a change record between the two revisions ended with one successor tag is
  read as that successor, its witness counting for it. The successor is read through
  dOrderedCharter-19's one tag resolver, over the index rows dOrderedCharter-15 S9's
  `extract_change_records` writes, never by parsing a change record here. Observed by AC2.
- **S5** — An item ending under a build. An item the build had witnessed, or was positioned on, whose
  tag a change record between the two revisions ended with no successor or with a split, carries no
  witness, and one order is filed for it through `write_row_order` (dSafePassage-9 S2) under
  `.governance/outbox/`, with kind `item-ended`, naming the build, the item, both revisions and the
  record. Observed by AC4.
- **S6** — Policy values naming a renamed boundary. `read_tag_policy(key, root, build)` reads a
  tag-valued key through dGroundRules-2's `resolve` and returns each tag redirected to its single
  successor at the build's pinned revision, so a value naming the old boundary acts on the new one
  from the boundary the build moves at. Each redirected tag files one order, kind `policy-renamed`,
  naming the key, the old tag and the successor, for the owner to re-pin the guarded file. The
  tag-valued keys are those dOrderedCharter-36 S4 reads as tag-valued. Observed by AC3.
- **S7** — A record with no pin. A transition record into a step written before this unit carries no
  `composition` field; `read_step_composition` then returns the landed tip with the state `unpinned`,
  and the build's next transition pins. Observed by AC6.
- **S8** — The fixture: `python tools/loop/composition.py --fixture --plant <case>` builds a scratch
  repository with two commits of a loop definition, a build's transition record and its witnesses,
  for the plants `rename`, `ended`, `split`, `policy-rename` and `unpinned`, each run against its
  expected observation by `--fixture` alone; the leg `loop composition fixtures` in
  `tools/gate-legs.json`, argv `python {prefix}/loop/composition.py --fixture`, declared in
  `tools/loop/kit.toml`. Observed by AC1 to AC6.
- **S9** — The page `help/loop.md` (TOOL-dDeclaredLoop-1 S7) gains a section on the pin: a build runs
  each step under the composition it entered it with and moves at the next boundary, and what an
  ended item and a renamed boundary file. Observed by AC7.

## 3. Non-goals (OUT)

- No composition mechanism: the overlay's rows, their composition and its landed revision are
  dOrderedCharter-35's, -32's and -46's, cited and called, never re-specced.
- No scenario and no recorded change in the revision: the scenarios a build was placed under are
  TOOL-dDeclaredLoop-27's field on the same record, and its own recorded changes TOOL-dDeclaredLoop-28's.
- No write to `.governance/policy.toml`. The redirect is read-side and the order asks the owner to
  re-pin, since the file is guarded owner-only (dGroundRules-6).
- No position engine: the derivation is TOOL-dDeclaredLoop-7's, which this unit points at a pinned
  revision.
- No update report row: the overlay's update report and its per-row states are dOrderedCharter-34's.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-3` — `Gov-Transition`, the transition record into a step whose `composition` field this unit fills; without its writer there is nothing to pin on
- **consumes-from** `TOOL-dDeclaredLoop-7` — `position`, the engine this unit points at the pinned revision; without it nothing derives a position from the pin
- **hands-off** `TOOL-dDeclaredLoop-27` — composition revision, the value S1 derives and S3 reads, beside which the scenario field is pinned
- **hands-off** `TOOL-dDeclaredLoop-19` — `read_tag_policy`, through which `review.breakpoints` is read so a renamed boundary keeps its breakpoint
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 39, each a scope item of that unit

## 4. Design

### Data model

The value a transition record into a step carries, beside `from`, `to`, `item` and `sha` (I8):

```
composition = 3f9c2a71        # the landed commit the step's composition is read from
```

The read at the pin, in order:

1. the build's transition records, read through `read_transitions(build, repo)`, newest first;
2. the newest record whose `to` is the build's current step: its `composition`, else `unpinned`;
3. `compose_at(root, rev)`: for each `[[kind]]` row at `rev`, the `population` blobs at `rev`, and the
   overlay blob at `rev` through `read_overlay(root, candidate=<blob text>)`, composed by
   `compose_rows`.

### The move, in order

At a transition into a step, before TOOL-dDeclaredLoop-3's writer runs:

1. `new = derive_composition_revision(root)`, `old = read_step_composition(root, build)`;
2. when `new` equals `old` nothing carries; else, for each item tag the build holds a witness for or
   is positioned on, the tag resolver's redirect between `old` and `new`: one successor carries the
   witness to it; none, or a list, files an `item-ended` order;
3. for each tag-valued key, `read_tag_policy` at `new`, each redirect filing a `policy-renamed` order;
4. `write_transition` records the transition with `--field composition=<new>`.

An order is idempotent by its slug, as `write_row_order` keys it, so a retried boundary files nothing
twice.

### Inventory

| Minted | Kind |
|---|---|
| `derive_composition_revision`, `read_step_composition`, `compose_at`, `read_tag_policy` | functions, `tools/loop/composition.py` |
| `composition` | transition record field (I8) |
| `item-ended`, `policy-renamed` | outbox order kinds through `write_row_order` |
| `unpinned` | the read state of a record with no pin |

Each function name is put to `python tools/lexicon/lexicon.py --suggest <name> --as py.function` in
the build pass.

### Migration

Builds in flight at landing carry records with no `composition`; S7 reads them at the tip, and the
first boundary each crosses pins it. No record is rewritten.

### Rollout

Live at landing: the pin only narrows what a mid-step reader sees.

### Files touched (estimate)

- `tools/loop/composition.py` (new)
- `tools/loop/loop_lib.py`: the definition read takes a revision
- `tools/loop/position.py`: the definition read through `compose_at`
- `tools/loop/loop_transition.py`: `composition` in `TRANSITION_FIELDS`, and the move called before
  `write_transition` writes
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop composition fixtures`
- `help/loop.md`: the section of S9

### Alternatives rejected

- **A digest over the composed rows as the revision.** It names the composition but cannot be read
  back: the position engine needs the rows, and a digest gives no commit to read them from.
- **Moving at once.** FA-7's second option; the owner took the next step boundary.
- **Never moving until landing.** FA-7's third option; a build would run a composition gov has since
  fixed for its whole life.
- **Rewriting the policy file at the boundary.** An agent write to a guarded owner-only file, which
  dGroundRules-6 refuses and veto 3 discards.

## 5. Production-readiness checklist

- security — no write but the outbox orders through their one writer; the policy file is read only.
- perf / scale — one compose per transition and per position read inside a step; blobs are read by
  `git cat-file`, one process per blob set.
- error / empty / loading states — a record with no pin reads `unpinned` at the tip and says so; a
  revision that names no commit is a refusal naming the record.
- observability — every carry, ended item and redirect is an order or a field on the record.
- risks — a build positioned on an item that ended files an order and loses that witness, so it may
  redo the item's successor work; the order names why.
- testing — the fixture plants of S8, run by the pass; the suite arm in §7 at the close.
- migration — as §4 says.
- user docs — `help/loop.md` gains the pin's section.

## 6. Acceptance criteria

- **AC1** — When `python composition.py --fixture --plant rename` lands a second commit renaming
  `item.build.fix-old` to `item.build.fix-new` while the fixture build is inside `building`, the
  position the fixture derives still names `item.build.fix-old` and reads the definition at the first
  commit.
  Red when: the position engine reads the tip, so the build is positioned on `item.build.fix-new` with
  no witness mid-step.
- **AC2** — When the same plant records the build's next transition into `testing`, that record's
  `composition` is the second commit's sha8 and the item `item.build.fix-new` reads witnessed by the
  witness `item.build.fix-old` held.
  Red when: the witness is keyed by the old tag only, so the renamed item reads unwitnessed after the
  move.
- **AC3** — When `python composition.py --fixture --plant policy-rename` holds `review.breakpoints`
  naming `item.build.fix-old` across the rename, `read_tag_policy` returns `item.build.fix-new` after
  the move, and one order file whose name carries `policy-renamed` appears in the fixture
  repository's outbox folder.
  Red when: the value is read raw, so the breakpoint names a tag no item carries and never fires.
- **AC4** — When `python composition.py --fixture --plant ended` and then `--plant split` end the
  positioned item with no successor and with two, each move carries no witness and files one
  `item-ended` order naming the build and the item.
  Red when: a split redirects to its first successor, so a witness carries to an item it never
  witnessed.
- **AC5** — When the `rename` plant's transition record is read on every channel the fixture's
  `transitions.record` selects, each carries `composition` with the same value, the landed commit
  `derive_composition_revision` returned.
  Red when: the field is written to the log channel only, so the trailer the other channels are held
  to carries no pin.
- **AC6** — When `python composition.py --fixture --plant unpinned` reads a build whose step record
  carries no `composition`, the read returns the tip with the state `unpinned`, and the build's next
  transition record carries a `composition`.
  Red when: a record with no pin refuses, so every build in flight at landing stops.
- **AC7** — When `grep -n "next step boundary" loop.md` runs over the help page at this unit's commit,
  it finds the section naming the `composition` field, `item-ended` and `policy-renamed`.
  Red when: the pin ships and the page still says a build reads the landed tip.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/composition.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `loop composition fixtures` leg's plants, its failing case staged by `rename` with the position engine reading the tip · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation,
  2026-10-24: `DRAFT` is not in the tuple, so a `DRAFT` header parses as no header. Liveness: the
  tuple would list it if the vocabulary admitted it. RESOLVED (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — What is a composition revision?** Options: (a) the landed commit the composition is read
  from; (b) a digest over the composed rows; (c) the overlay's blob alone. I17 names the overlay's
  landed revision plus gov's pack revisions, which one commit holds both of; (b) cannot be read back
  and (c) misses gov's packs. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3. widens: none.
  relaxes: none.
- **F3 — How is a policy value naming a renamed boundary re-pointed?** Options: (a) a read-side
  redirect plus an order to the owner; (b) a write of the new value into the policy file; (c) the
  redirect alone. (b) is an agent write to a guarded file, discarded by veto 3; (c) leaves the file
  naming a dead tag for ever. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3. widens: none.
  relaxes: none.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 26, the flow adoption's items 14 and 15
  and FA-7, and dOrderedCharter-15, -35, -46 and dSafePassage-9 read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

No existing seam pins a composition: `python tools/codebase-map/reuse_lookup.py "pin a composition revision on a transition record and derive position from it"`
ranked name stems only (`records`, `derive_clause_hash`, `derive_supersession_map`), and scout A found
that every build reads the landed tip
(`memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md:33`). The
unit extends seams its parents spec: the landed revision (dGroundRules-2 S1), the overlay's candidate
read (dOrderedCharter-46 S3), `compose_rows` (dOrderedCharter-35), the successor redirect of the tag
index (dOrderedCharter-15 S9, -19) and the outbox order writer (dSafePassage-9 S2, extracted at
`tools/govkit/govkit.py`'s withdrawn arm). `python tools/memory-recall/query.py` returned the brief's
row, the night pass instruments' clause text and scout A's row; scout A cites the change records'
`Successor` field as dOrderedCharter-15 S7, which agrees with that spec at base.

Recall terms used: composition revision pinned transition record step boundary successor rename change record overlay order
