---
slug: aRuledFrontispiece
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aRuledFrontispiece-1
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
self-consistent wrong render. Unit 3 adds front-matter keys and must state why they are not the
refused schema, or record a falsification.

`TOOL-aMouldedFolio-2` S4 renders the FULL roster in the build README and only its COUNT in
`LIVE.md` and the ledger shards. That decision is what makes the `**Build status:**` line 577
characters wide in the largest build, which is the line fork 3's cap now refuses. Unit 5 keeps the
full roster and wraps it; replacing it with a count would reverse a recorded decision and belongs in
a spec that says so.

## Where the sources actually are

Both over-cap lines in the corpus are GENERATED, not authored: the `ids:` front-matter line, which
`--write` rewrites, and the `**Build status:**` line inside the region. The remedy is a renderer
change in both cases. Only `aUnmannedHelm/README.md:78` is an authored line over the cap.

Check 7's 300-character budget is a single hardcoded literal in one `awk` pass over the whole index
set, so fork 3's relaxed tier cannot be a global bump — it needs a per-class cap, the same way
`guides/` already carries its own byte and line budget.

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aRuledFrontispiece-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRuledFrontispiece-1 — the build README gets a slot contract and an immutable authored plan](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-1.md) | OPEN | rev-1 | 2026-08-16 |

Records live under `spec/`.
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. This table is the roster; the `ids:` key above is not.

`BUILD-METHOD.md` M2 says `ids:` "is NOT a roster — it is a reservation range written as ranges and
unions". That has been false since `TOOL-aMouldedFolio-2` made `ids:` DERIVED from the id corpus:
`--write` rewrote this build's ten authored ids down to the one that has a spec, within a minute of
the folder being opened. M2 and the generator are two answers to one question, which is the class
this build exists to close. **Unit 9 owns that correction** — it is now a scope item there, not an
observation in a README.

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

| # | Id | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aRuledFrontispiece-1` | 2 | the authored/generated boundary — the plan pair and the one bounded prose block |
| 2 | *pending* | 2 | build order and parallel groups — status-header verbs and their region |
| 3 | *pending* | 2 | dependency edges — front-matter slug keys and their region |
| 4 | *pending* | 2 | the document inventory region |
| 5 | *pending* | 2 | index-set membership at the relaxed cap tier |
| 6 | *pending* | 2 | the standalone README-format gate leg |
| 7 | *pending* | 1 | the status-file retirement |
| 8 | *pending* | 2 | the unattended check-8 terminal-phase carve-out |
| 9 | *pending* | 2 | the build method's roster and parallelism contract |
| 10 | *pending* | 2 | the corpus retrofit and the kit version bump |

## The order is TOTAL, and this build has no parallel lane

Unit 1 is first because it defines where a generated region may live and what an authored region is;
units 2, 3 and 4 render into that structure. Units 2, 3, 4, 5 and 10 all write
`tools/memory-tree/gen_build_index.py`, so M6 clause 1 sequences them on the write set alone. Unit 6
is after 1 through 5 because the leg pins the format those units define. Unit 10 is last because it
re-renders the corpus against everything above it and carries the kit version bump.

Units 7, 8 and 9 touch none of the generator, and unit 7 shares `check-memory-hygiene.sh` with unit
5 while unit 6 shares `AGENTS.md` with unit 7. So the write sets still intersect and the sequence
holds.

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
- **The version bump and the corpus retrofit are the same unit but not the same commit.** The
  generator, its arms and the leg land before any README is re-rendered, so the retrofit commit is a
  pure re-render reviewable as `--check` output rather than as a 38-file diff.
- **`memory/DECISIONS.md` is append-only.** A unit that reverses `TOOL-aMouldedFolio-1` or
  `TOOL-aMouldedFolio-2` mints a new id naming the record it supersedes; it never edits it.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal `non_terminal_specs_cited_by_product_source` sits at its pin with zero tolerance,
  and its globs include `tools/`, `skills/`, `.claude/` and `memory/guides/SESSION-KICKOFF.md` by
  file path. Units 6, 8 and 9 all edit files inside those globs.
- **Every unit that changes a renderer re-runs `python tools/memory-tree/gen_build_index.py --check`
  and reads the artifact count from the gate**, never from this file.

## Parked

Nothing parked yet.
