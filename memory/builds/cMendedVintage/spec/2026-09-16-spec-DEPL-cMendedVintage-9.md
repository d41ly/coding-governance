# DEPL-cMendedVintage-9 — no descriptor destination under `{memory_root}/project/`

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |

<!-- /gen:spec-records -->

## 1. Goal

`{memory_root}/project/` is a closed NAME set: check 3 of `check-memory-hygiene.sh` admits a
whitelist plus whatever the target declares in its own `PROJECT_REGISTRY_EXTRA`, and gov cannot widen
either at an adopter — one takes the widening only on a later `update --kits memory-tree`, and a
forked checker takes it never. A descriptor that lands a file there therefore ships a red gate.
`TOOL-cMendedVintage-2` withdraws the one live instance; this unit makes the class unrepeatable by
refusing it in `selfcheck`, where gov grades its own descriptors before anyone installs them.

## 2. Scope (IN)

- **S1** The bare-target block inside selfcheck arm 7h — `tools/govkit/govkit.py:1888-1909`, where
  `_bare_rows` and `_bare_have` are already in hand — gains one predicate: no planned destination may
  resolve under the `{memory_root}/project/` prefix. Observed by AC1.
- **S2** The refusal message names the entry, the destination, and the REASON — that the case list in
  a target's `check-memory-hygiene.sh` is a closed name set gov cannot widen at that target. A
  refusal that says only "not allowed" sends the reader to this spec; one that says why sends them to
  the remedy. Observed by AC1.
- **S3** The reserved prefix is RESOLVED through the same context that resolved the destinations,
  never spelled as the literal `memory/project/`. A predicate holding its own copy of a token the
  rows were resolved with is two spellings of one fact, and a target declaring a different
  `memory_root` would be graded against gov's. Observed by AC2.
- **S4** The existing `r.note` at `tools/govkit/govkit.py:1907` gains the number of destinations this
  predicate graded. After `TOOL-cMendedVintage-2` the hit count is zero by design, and a zero with no
  population beside it is indistinguishable from a predicate that matched nothing because it ran
  over nothing. Observed by AC3.
- **S5** `tools/govkit/selftest.py` gains the arm that stages the break and asserts the refusal, and
  `tools/govkit/refusal_join.py`'s anchor set and shrink-only pins move to cover the new branch. A
  refusal branch no arm reaches is what that join exists to refuse. Observed by AC4.
- **S6** `WIRE-INTO-PROJECT.md`'s `## Maintenance` section gains a migration subsection for the
  residue: an adopter whose receipt already carries the gate-lint seed row gets NO withdrawal order,
  because `UPDATE_ROLE` maps `seed` to `report-reseed` and the override at
  `tools/govkit/govkit.py:6443` rewrites a `withdrawn` verdict to `current` or `patched`. The
  subsection names that site and the manual step. Observed by AC5.

## 3. Non-goals (OUT)

- No change to the `report-reseed` override at `tools/govkit/govkit.py:6443`. Its exemption set is
  `missing` and `renamed`, and adding `withdrawn` to it re-adjudicates every seed row in every
  receipt — a verdict change on a population no unit in this build has measured. This unit records
  the consequence and does not repair it.
- No change to `check-memory-hygiene.sh`, its case list, or `PROJECT_REGISTRY_EXTRA` in any tree.
- No refusal over any other reserved prefix. One predicate, one measured class; a general
  "reserved destinations" table would be a registry with one row.
- No `[[exempt]]` escape for this predicate. An exemption would be a declared way to ship the exact
  file a target's gate refuses, which is the state this unit exists to end.
- No change to gov's own `memory/project/` tree or to `.memory-tree.conf`'s
  `PROJECT_REGISTRY_EXTRA`.

### Edges

- **consumes-from** `TOOL-cMendedVintage-2` — that unit deletes the ONE descriptor rule this
  predicate would fire on. Without it this unit reds gov's own `selfcheck` on landing; with it the
  live hit count is zero and AC1 must stage its own break, which is why AC3's population count is
  scoped here rather than left implicit.
- **hands-off** external — the two live adopters need the S6 migration note read by a human. Nothing
  in this repo delivers it to them.

## 4. Design

### Data model

The block already builds everything the predicate needs:

| name | line | what it holds |
|---|---|---|
| `_bare_rows` | `govkit.py:1895` | every planned write against a bare temp target, `missing` included |
| `_bare_have` | `govkit.py:1896` | the destinations that are not `missing` — the set `silenced_legs` reads |
| `_bare_sel` | `govkit.py:1890` | the selection, which is every registry entry in install order |

MEASURED at BASE `859daa67` on 2026-09-16, by a read-only probe importing `read_descriptors`,
`derive_install_order` and `planned_writes` and running them against a temporary bare target: 26
entries selected, 277 planned rows, 269 non-missing destinations, and exactly ONE of them under a
`project/` segment — `memory/project/substitution-fed-loops.txt`, role `seed`, from `gate-lint`.
`{memory_root}` resolves to `memory` at a bare target through `canonical_ctx` and the
`ctx.setdefault` at `govkit.py:996`, which is why the row is present and not `missing`, and therefore
why the predicate is live rather than vacuous at the revision it was written against.

### Rollout

The predicate lands AFTER `TOOL-cMendedVintage-2` has drained its one live hit, so the first
`selfcheck` run carrying it is green. That ordering is deliberate and it costs something: the
population the arm was written against no longer exists in the tree, so the failing case is observed
on a staged break instead of on the tree. The staged break is the stronger observation anyway — it is
the one an adopter's future descriptor will reproduce — and the population count from S4 is what
keeps the green honest.

### Alternatives rejected

Grepping descriptor SOURCE text for `{memory_root}/project`: it misses a literal `memory/project/…`
destination and every destination assembled from two tokens, and it grades a string rather than the
path gov would actually write. The resolved destination is the fact; the source spelling is one of
several ways to write it.

Landing the predicate BEFORE the withdrawal, so the live hit is the observation: it reds gov's own
`selfcheck` leg for the length of one unit, which puts a red bar between two passes of this build for
no gain that the staged break does not also buy.

Refusing at `apply` rather than at `selfcheck`: `apply` runs in an adopter's tree, where the refusal
arrives after gov shipped the descriptor and stops THEM rather than US. `selfcheck` grades gov's own
declarations before anyone installs them, which is where a declaration defect belongs.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | one predicate and one message inside the 7h bare-target block; the note gains a count |
| `tools/govkit/selftest.py` | one arm staging a descriptor destination under the reserved prefix |
| `tools/govkit/refusal_join.py` | anchor set and the two shrink-only pins |
| `WIRE-INTO-PROJECT.md` | one `## Maintenance` subsection |

## 5. Production-readiness checklist

- security — no write path changes. The predicate refuses a declaration; it writes nothing and runs
  only inside `selfcheck`, which operates on a temporary directory it creates itself.
- perf / scale — one pass over 269 already-computed strings inside a block that already builds them.
  Not measurable against a `selfcheck` whose declared ceiling is 310 seconds.
- error / empty / loading states — the empty case IS the steady state after
  `TOOL-cMendedVintage-2`, and S4's population count is what distinguishes it from a dead predicate.
- observability — the refusal names entry, destination and reason; the note names the population.
- risks — the predicate could red a legitimate future destination under a `project/` segment that is
  not the memory tree's. Scoped by resolving the prefix from `memory_root` rather than matching any
  `project/` segment, so a kit's own `project/` subdirectory is untouched.
- testing — AC1 and AC2 run `selfcheck` against a scratch copy of the tree with a staged descriptor
  edit. The permanent arm is declared in section 7 and is not what any acceptance criterion runs.
- migration — S6's runbook subsection, and section 3's non-goal that the override itself is not
  repaired here.
- user docs — `WIRE-INTO-PROJECT.md` is the runbook and is the only page this touches. The two live
  adopters are named there, not in a kit README.

## 6. Acceptance criteria

- **AC1** — When a descriptor in a scratch copy of this tree is given a file rule whose `to` resolves
  under the reserved prefix and `python tools/govkit/govkit.py selfcheck` runs there, it exits
  non-zero and its output names the entry, the destination and the closed-case-list reason.
  Red when: the predicate reads a set the resolution never populates — `_bare_have` excludes
  `missing` rows — so a staged destination is graded by nothing and the run stays green.
  fixture: a scratch copy of this tree under this run's scratch root; the break is staged there and
  never in the worktree.
- **AC2** — When the same staged break spells the destination as a LITERAL `memory/project/<name>`
  rather than through `{memory_root}`, `python tools/govkit/govkit.py selfcheck` refuses it
  identically.
  Red when: the predicate compares the descriptor's source text instead of the resolved destination,
  which the token form would catch and the literal form would not.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs against this tree unmodified, it
  exits 0 and its gate-legs note reports the number of destinations the new predicate graded, and
  that number is greater than zero.
  Red when: the predicate runs over an empty collection and reports a reassuring zero hits, which is
  indistinguishable from a clean tree.
  figure: DERIVED — the count is printed by the note at observation time; the 269 in section 4 is
  PINNED to BASE `859daa67` as the reading that established the population is non-empty.
- **AC4** — When `python tools/govkit/refusal_join.py` runs, it exits 0 with the new branch in its
  anchor set and both shrink-only pins moved in the same commit.
  Red when: the predicate lands with no arm reaching it, which is exactly the unreached refusal
  branch that join exists to refuse.
- **AC5** — When `git grep -n 'report-reseed' -- WIRE-INTO-PROJECT.md` runs, the `## Maintenance`
  subsection names that override, the two adopters, and the manual step their receipt needs.
  Red when: the withdrawal ships with no note, so an adopter reads `current` over a row gov no longer
  writes and never learns their receipt disagrees with the descriptor.

## 7. Gates

`govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `memory hygiene` · `install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)` · `line length`

New arm: `tools/govkit/selftest.py` · a descriptor whose `to` resolves under the reserved prefix,
asserted to refuse · `refusal_join.py`'s two shrink-only pins move with it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "gate lint seed registry written into the memory tree"`
returned `registry.toml` as the govkit affordance seam and no symbol that resolves a destination, and
it reported `.sh` as an unscanned layer; the ranking it did return is name-token noise over
`*_registry` symbols in unrelated kits. The seam this unit extends was found by reading the engine
and then confirmed by running it: the bare-target block inside selfcheck arm 7h at
`tools/govkit/govkit.py:1888-1909`, which already calls `planned_writes` against a temporary target
and already holds `_bare_have`, so the predicate adds a test and no new resolution. `silenced_legs`
one line below is the exemplar for the message shape — it names the entry, the argv and what no rule
produces. The recall probe returned the records that settle the reason: `memory/map/features/gate-lint.md`
records why the seed rule was added, and `TOOL-dClosedLexicon-13` in `memory/DECISIONS.md` records
that a destination, not a role, is what classifies an entry — which is why this predicate keys on the
resolved destination.

Recall terms used: `--terms "gate-lint sh_hygiene seed role registry memory project whitelist
check-memory-hygiene descriptor destination silenced_legs adopter apply"`, with the question "why
does the gate-lint kit ship a seed registry under the memory tree and what refuses it there".
