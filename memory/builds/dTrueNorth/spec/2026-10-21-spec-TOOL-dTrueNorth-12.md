# TOOL-dTrueNorth-12 — the routed-commits self-test reaches the strip through a resolver and builds its own design in the fixture

**Status:** OPEN · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 4

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 30 at HIGH**, its item **H5**. Through `deviation_join.py`,
`routed_commits.py --selftest` reads three things outside the leg's guard and outside an adopter's
tree: `GEN_REGION_AWK` from `tools/unattended/lib-unattended.sh`, the live tree's `DESIGN_RECORD`
`[chain]` section, and its `DESIGN_VIEW`. The leg is guarded on `{prefix}/lib/` and
`{prefix}/memory-tree/` only and ships to adopters, and `TOOL-dTrueNorth-7` edits the library in this
same build. An edit to the library alone skips the leg or reuses its earlier green, and an adopter
without the unattended kit or gov's records runs a shipped self-test that cannot build its fixture.
This unit takes the skeptic's corrected fix: the strip is reached through a resolver a test can
replace, a missing kit is a named skip of the plants that read the strip, the fixture builds a small
design of its own, and the leg's guard names the library. It repairs `TOOL-dTrueNorth-4`. The second
self-test that copies gov's live design, `TOOL-dTrueNorth-6`'s, is the same class at MEDIUM, id 42
(item M16), batched into `TOOL-dTrueNorth-16`.

## 2. Scope (IN)

- **S1** — `read_gen_region_awk(resolve=None)` in `tools/memory-tree/deviation_join.py` returns the
  value of the `GEN_REGION_AWK=` assignment in the unattended kit's `lib-unattended.sh`, the kit found
  by `backlog.resolve_kit_dir("unattended", "lib-unattended.sh", <this kit's directory>)` or by the
  `resolve` callable a caller injects, the shape `read_landed_unclosed` takes. The value is read from
  the file, never copied into the module. This supersedes `TOOL-dTrueNorth-4` S4's fixed path to
  `tools/unattended/lib-unattended.sh`. Observed by AC2.
- **S2** — The unresolved kit, two readings. In the live join with the `DESIGN_*` keys declared, a
  kit that does not resolve is a refusal naming it, exit 2, because a population read without the
  strip would count status-only revisions as members. Under `--fixture` and in the host's self-test,
  it is one line, `deviation: SKIP — the unattended kit does not resolve, so the plants that read the
  generated-region strip are not run: <reason> · <plants>`, and every other plant runs. The plants
  named are those whose verdict reads the strip: `status-only`, `header-rev`, `gen`, `status-gen` and
  `gen-text` (`TOOL-dTrueNorth-4` AC5), and any further plant whose verdict changes when the strip is
  stubbed to the identity, which the pass finds by running every plant so stubbed. Observed by AC1.
- **S3** — The fixture's design is its own. `build_design_fixture(repo)` writes, in the fixture's
  commits, a design record whose `[chain]` section holds two fixture builds of two clauses each, and
  the view of it in the as-built row grammar, both from constants in the module; the pin commit and
  the clause-move plants edit those. Nothing reads the live tree's `DESIGN_RECORD` or `DESIGN_VIEW`.
  This supersedes `TOOL-dTrueNorth-4` §4 "The fixture"'s "the tree's `DESIGN_RECORD` `[chain]`
  section and its `DESIGN_VIEW` file copied in whole, never a synthetic chain". Observed by AC3.
- **S4** — In `tools/gate-legs.json`, the `routed-commits selftest` guard gains
  `{prefix}/unattended/lib-unattended.sh`. Observed by AC4.
- **S5** — The dependency S2 refuses on is declared where the kit declares its conditional siblings:
  one `requires_if` row in `tools/memory-tree/kit.toml` naming the kit `unattended` when any of
  `DESIGN_RECORD`, `DESIGN_BASELINE` or `DESIGN_VIEW` is set, its `why` naming the strip the live join
  reads and the fixture's named skip. Like the rows beside it, it selects no kit and installs nothing.
  Observed by AC5.

## 3. Non-goals (OUT)

- `TOOL-dTrueNorth-6`'s fixture, which copies the live design the same way: `TOOL-dTrueNorth-16`'s
  item for id 42, which reuses S3's builder.
- The plants' verdicts. Every plant `TOOL-dTrueNorth-4` AC6 tables exits as that table states over
  the fixture design; only where the design comes from moves.
- An install-prefix concern the finder raised and the skeptic did not establish: with S1 the module
  spells no path under the unattended kit, so there is nothing for that leg to read.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-4` — `deviation_join.py`, its fixture, its plants and the host call from `routed_commits.py`'s self-test; without them there is no strip read and no fixture to make hermetic
- **hands-off** `TOOL-dTrueNorth-16` — `build_design_fixture`, the second instance of which its item for id 42 extracts into a shared factory
- **hands-off** `TOOL-dTrueNorth-20` — the four `DESIGN_*` keys in `kit.toml`'s `conditional_keys` beside S5's row, which names all four, AC5 observed by a TOML read, `read_gen_region_awk` refusing a missing or empty strip, and the guards-join hit S4 makes on `TOOL-dTrueNorth-7` (the round-2 spec audit's ids 11, 26, 10, 15, 36 and 24)

## 4. Design

### Evidence

- `GEN_REGION_AWK` is assigned at `tools/unattended/lib-unattended.sh:1045`.
- `backlog.resolve_kit_dir(home, anchor, here)` (`tools/memory-tree/backlog.py:1749`) resolves a
  kit through the install receipt, then a probe beside the caller, and raises `LookupError` naming
  the places it looked.
- `read_landed_unclosed(root, conf, resolve=None)` (`tools/memory-tree/gen_build_index.py:1678`)
  is the precedent for an injectable resolver over a sibling kit, refusing by name when it does not
  resolve.
- The leg ships as a `subject = "kit"` row with `guard = ["{kit}/"]`
  (`tools/memory-tree/kit.toml:337-341`), and gov's manifest guards it on `{prefix}/lib/` and
  `{prefix}/memory-tree/`.
- The memory-tree kit's descriptor requires no kit (`tools/memory-tree/kit.toml:7`) and declares its
  conditional siblings as `requires_if` rows (`:8`), so an adopter may lack the unattended kit.

### The fixture design

Two builds, `dFixA` and `dFixB`, two clauses each, `cl-dFix-0001` to `cl-dFix-0004`, their texts
plain sentences holding one backticked name each. The record carries the `[chain]` table and a
`Baseline:` line, committed first; the pin is that commit. The view is the four rows, each `since`
`baseline`, in the row grammar `design_lib.VIEW_ROW` reads. The clause-move plant amends one clause
in a later commit; the baseline plant moves the record's `Baseline:` line.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `read_gen_region_awk` | function, `deviation_join.py` | `py.function`, OK |
| `build_design_fixture` | function, `deviation_join.py` | `py.function`, OK |

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/routed_commits.py` (its self-test's call into the fixture only)
- `tools/gate-legs.json`
- `tools/memory-tree/kit.toml` (one `requires_if` row)

### Alternatives rejected

- **A named refusal when the kit is absent, the finder's first fix.** The skeptic judged it unsound:
  inside a shipped self-test of a kit that does not require the unattended kit, a refusal reds that
  self-test in every such adopter.
- **A copy of the awk in the module.** `TOOL-dTrueNorth-4` S4 refuses one, and two copies of the
  strip drift.

## 5. Production-readiness checklist

- security — no new surface; the resolver reads a receipt row and a probe path inside the tree, and
  skips a receipt path that escapes it.
- perf / scale — one file read for the awk; the fixture writes four short files.
- error / empty / loading states — an unresolved kit is a refusal live and a named skip under the
  fixture; neither reads as green over the plants it did not run.
- observability — the SKIP line names the reason and every plant it held back.
- risks — an adopter's self-test no longer observes the strip plants; the SKIP line says so on every
  run, and gov, where the kit resolves, runs them all.
- testing — AC1 to AC4 as probes; the arm under §7.
- migration — none.
- user docs — the module docstring; no page under `help/` covers the self-test.

## 6. Acceptance criteria

- **AC1** — When a probe copies `tools/lib/` and `tools/memory-tree/` into a scratch git repository
  under `%TEMP%` that holds no unattended kit and runs
  `python3 <scratch>/tools/memory-tree/deviation_join.py --fixture --plant status-only --policy refuse`,
  it prints the `deviation: SKIP` line naming the unattended kit and the held plants and exits 0, and
  `--fixture --plant pass-revision --policy refuse` there still exits 1.
  Red when: the fixture raises, or reds, when the kit is absent.
  fixture: a scratch repository under a short `%TEMP%` path; the tree holds none.
- **AC2** — When a probe loads the module and calls `read_gen_region_awk()` on the tree, it returns
  the bytes `sed -n "s/^GEN_REGION_AWK='\(.*\)'$/\1/p" tools/unattended/lib-unattended.sh` prints, and
  with `resolve` a stub raising `LookupError` it raises `LookupError` naming the kit.
  Red when: the value comes from a literal in the module.
- **AC3** — When `python3 tools/memory-tree/deviation_join.py --fixture` runs in a scratch clone whose
  `.memory-tree.conf` blanks every `DESIGN_*` key and which holds no `DESIGN_RECORD` file, it exits 0,
  and each plant of `TOOL-dTrueNorth-4` AC6 exits as that table states.
  Red when: the fixture reads the live tree's design record or view.
  fixture: a scratch clone under a short `%TEMP%` path.
- **AC4** — When `python3 -c "import json; print([l['guard'] for l in json.load(open('tools/gate-legs.json')) if l['name'] == 'routed-commits selftest'])"`
  runs, the list holds the library's pathspec, the `{prefix}` token resolving so that it names
  `tools/unattended/lib-unattended.sh`.
  Red when: a commit touching only the library would skip the leg.
- **AC5** — When `grep -n 'kit = "unattended"' tools/memory-tree/kit.toml` runs, it prints one
  `requires_if` row whose `when_any_key_set` names the three `DESIGN_*` keys of S5.
  Red when: the live join's sibling dependency is undeclared, so `govkit selfcheck` grades nothing.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py (its selftest) · covers AC1 AC3 · the deviation fixture run under a resolver stub raising LookupError, and over a tree with every DESIGN_* key blank, red against the base module that reads the live records and a fixed library path · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Does the build's grant lift veto 2 for the kit and manifest edits?** All three are governance
  carriers by `PLAY-dClosedLoop-10`'s list. `cl-dClosedLoop-0004` names the join at the commit
  through the routed-commit attribution, which this leg hosts; S4 guards that leg and S5 declares the
  sibling the join reads. RESOLVED
  (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3
  the deviation join's strip resolver, its fixture design, its requires_if row and the
  routed-commits self-test guard cl-dClosedLoop-0004's join runs in · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 30 (HIGH, item H5).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "resolve a sibling kit directory with an
injectable resolver"` ranked `resolve_kit_dir` (`tools/memory-tree/backlog.py`,
`tools/lib/resolve_kit_dir.py`) as a seam with 71 installs, and `kit_rel`. The seam this unit extends
is `backlog.resolve_kit_dir`, the resolver the kit's engines already import, with
`read_landed_unclosed`'s `resolve=` as the injection precedent; the fixture design follows
`TOOL-dTrueNorth-2`'s arm, which builds a two-build fixture view, record and deriver in its scratch
repositories. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
