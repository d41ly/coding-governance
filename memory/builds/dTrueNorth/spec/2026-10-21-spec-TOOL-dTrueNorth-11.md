# TOOL-dTrueNorth-11 — the build-index and memory-hygiene self-test legs guard the spec-token checker their arms load

**Status:** CLOSED · rev-3 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 2

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-11-deviation-10.md](../build/2026-10-21-build-TOOL-dTrueNorth-11-deviation-10.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-11-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-11-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md](../build/2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md) | journal | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 TOOL-dTrueNorth-31 TOOL-dTrueNorth-32 TOOL-dTrueNorth-33 |
| [2026-10-21-prompt-TOOL-dTrueNorth-11-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-11-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |
| [2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md) | diff-review | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 28 at HIGH**, its item **H4**: the two self-test legs skip when only
`check-spec-tokens.py` changes. `TOOL-dTrueNorth-3` declares two new arms that run through
`read_carries_coverage`, which loads `tools/check-spec-tokens.py` from the kit's parent directory by
path: the build-index self-test arm and the check-29 arm of the hygiene self-test. Both legs are
guarded on `{prefix}/lib/` and `{prefix}/memory-tree/` only, so a commit that edits the checker alone
skips both, and the reuse key carries the earlier green forward over a join the arms did not run.
This unit adds the checker's exact path to both guards. It repairs `TOOL-dTrueNorth-3`.

## 2. Scope (IN)

- **S1** — In `tools/gate-legs.json`, the `guard` of `build-index selftest` and of
  `memory-hygiene self-test` each gains the pathspec `{prefix}/check-spec-tokens.py`, after the two it
  carries. Observed by AC1 and AC2.
- **S2** — The guard taxonomy stays a partition: the new pathspec resolves to
  `tools/check-spec-tokens.py`, the exact path the registry exempts from shipping
  (`tools/govkit/registry.toml:215`), so govkit selfcheck's 7c classes it `exempt` and nothing else
  (`tools/govkit/govkit.py:2574-2580`). Observed by AC3.

## 3. Non-goals (OUT)

- The `routed-commits selftest` guard, which `TOOL-dTrueNorth-12` widens for the unattended library.
- The kit descriptor's guards in `tools/memory-tree/kit.toml`, `["{kit}/"]` for both legs. The
  checker does not ship to an adopter, so an adopter's legs load no such file, and nothing compares
  a descriptor's guard with gov's manifest (`tools/govkit/govkit.py:2604`).
- A gate that reds any kit module loading a file outside its leg's guard, the finding's suggested
  left-shift. It is a separate gate, so a separate unit by M2, and the class already has its record,
  `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-3` — the two arms its §7 declares, which load `check-spec-tokens.py` through `read_carries_coverage`; without them the guard widens over nothing the legs read
- **hands-off** `TOOL-dTrueNorth-20` — the three guards-join hits S1's guard makes on dPinnedHandoff's live specs, and AC2 observed through `check-spec-tokens.py --legs-for` (the round-2 spec audit's ids 25 and 20)

## 4. Design

### Evidence

- Both legs carry `"guard": ["{prefix}/lib/", "{prefix}/memory-tree/"]` in `tools/gate-legs.json`,
  read at base.
- The guard predicate is git-pathspec semantics, the exact path or anything under it as a directory
  (`tools/check-spec-tokens.py:494-503`), so `{prefix}/memory-tree/` never covers a file in its parent.
- The `spec-tokens self-test` leg is guarded on `{prefix}/`, so the checker's own suite already runs
  on such a commit; the two legs here are the ones that do not.
- The class is recorded in `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`.

### Files touched (estimate)

- `tools/gate-legs.json`

### Alternatives rejected

- **Guarding on `{prefix}/`.** Every commit under `tools/` would then run both selftests, the breadth
  the guard exists to avoid, and the pathspec is broad by the guard join's floor.
- **Moving the join into the kit so the guard needs no widening.** That is the design question
  `TOOL-dTrueNorth-16` answers for id 10; the guard is wrong today whatever the answer.

## 5. Production-readiness checklist

- security — no new surface; a guard only widens when a leg runs.
- perf / scale — the two legs now run on a commit touching the checker, which `spec-tokens self-test`
  already runs on.
- error / empty / loading states — N/A: a guard has no empty state; an absent file trips nothing.
- observability — the runner's leg plan names both legs on such a commit.
- risks — none beyond the runs added.
- testing — AC1 to AC3 as probes of the manifest.
- migration — none.
- user docs — none; the manifest is the only home of a guard.

## 6. Acceptance criteria

- **AC1** — When `python3 -c "import json; print([l['guard'] for l in json.load(open( 'tools/gate-legs.json' )) if l['name'] in ('build-index selftest', 'memory-hygiene self-test')])"`
  runs, both lists end with the checker's pathspec, the `{prefix}` token joined to the file name
  `check-spec-tokens.py`, which resolves to `tools/check-spec-tokens.py`.
  Red when: either leg's guard lacks the path.
- **AC2** — When a probe applies the guard predicate of `tools/check-spec-tokens.py:494-503`, with
  `{prefix}` resolved to `tools`, to the path `tools/check-spec-tokens.py` over every leg in
  `tools/gate-legs.json`, the two legs are among those it trips; over the manifest at `271aa59d` they
  are not.
  Red when: a commit touching only the checker would still skip either leg.
- **AC3** — When the same probe classes the new pathspec by govkit selfcheck 7c's rules, it falls in
  exactly one class, `exempt`.
  Red when: the pathspec falls in two classes or none, which 7c reds.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `build-index selftest` · `memory-hygiene self-test` · `govkit selfcheck` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No suite arm lands with this unit: the guard is data the runner reads, and AC1 to AC3 observe it.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Does the build's grant lift veto 2 for the manifest edit?** `tools/gate-legs.json` is a
  governance carrier by `PLAY-dClosedLoop-10`'s list. `cl-dClosedLoop-0003` names the coverage
  report and memory hygiene's refusal, and these two legs carry the arms that observe both; a guard
  that skips them is that clause's gate failing open. RESOLVED (agent, 2026-10-21, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the guards of the two self-test
  legs that run cl-dClosedLoop-0003's arms · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 28 (HIGH, item H4).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.
- rev-3 · 2026-10-21 · §6 · the acceptance criteria name the modules this build creates (`deviation_join.py`, `asbuilt_view.py`, `design_lib.py`) quoted or bare, and a `git show`/`json.load` argument quoted, so the spec-tokens paths join, which reads the live tree at every `--dispatch`, stops refusing every unit before those modules exist. No criterion's observation moves.

## 10. Reuse audit

No existing seam fits beyond the manifest itself: a guard lives in one place, `tools/gate-legs.json`,
and this unit edits two rows of it. `python tools/codebase-map/reuse_lookup.py "resolve a sibling kit
directory with an injectable resolver"` ranked `resolve_kit_dir` and `kit_rel`, which locate a file
and say nothing about which legs run on it; the guard predicate read for AC2 is
`check_guard_trips` in `tools/check-spec-tokens.py`, and the class is recorded in
`memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
