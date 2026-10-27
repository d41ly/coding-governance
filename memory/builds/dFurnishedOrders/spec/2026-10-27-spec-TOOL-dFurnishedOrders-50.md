# TOOL-dFurnishedOrders-50 — unit 48's `govkit selftest` home rows priced in the guards join: a home only where `apply` runs or renders from it, no guard pushed into the broad set, and every live spec the rows reach carrying the leg or a waived, asked row

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 84ab3c6f · streams tooling · order 28 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-50-deviation-501.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-50-deviation-501.md) | deviation | — |
| [2026-10-27-build-TOOL-dFurnishedOrders-50-round6-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-50-round6-fix-return.md) | research | TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-50-round6-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-50-round6-fix-brief.md) | research | TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 |
| [2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`)
confirmed finding **id 17 at HIGH**, report item **H1**. No other id shares that item.

`TOOL-dFurnishedOrders-48` S17 adds a `{prefix}/<home>/` row to the `govkit selftest` guard for every
non-flat entry `--all` selects. Most of those directories are carried by 5 legs or fewer, so the
guards join of `tools/check-spec-tokens.py` reads them (`BROAD_LEG_FLOOR`, `:362`;
`derive_guarded_legs`, `:589-608`). Every live spec dated on or after `SPEC_GUARD_LEGS_CUTOFF`
(`.memory-tree.conf:356`, `2026-09-22`) whose Files touched trips such a row then owes `govkit selftest`
on its §7 leg line. This unit's probe counted 37 such specs at `84ab3c6f`. Four are other builds'
specs, which this build may not write (README, build-level rules). Unit 48 names none of this.

The same probe found a second effect the report did not name. `{prefix}/hooks/` is carried by
exactly 5 legs today (`agent-cap self-test`, `scratch-guard self-test`, `verifier fan-out self-test`,
`review-join self-test`, `hook destinations self-test`). A sixth makes it BROAD, which drops it from
the join for all six. That is the guards join's motivating case (`tools/check-spec-tokens.py:358-359`).

This unit repairs `TOOL-dFurnishedOrders-48` and builds one step after it (order 28). It narrows the
home term to the homes `apply` runs or renders from. It holds the broad set unchanged by those rows.
It disposes of the specs the rows reach under the standing ruling the earlier widenings used.

## 2. Scope (IN)

- **S1** — A home only where `apply` runs or renders from it. In `check_selftest_guard_coverage`'s
  required set (unit 48 S16, S17), the home term `{prefix}/<home>/` holds only a non-flat entry whose
  descriptor does one of three things. It declares a non-empty `[adopt]` `argv`, the test govkit makes
  at `tools/govkit/govkit.py:1928`. It carries a `[[regenerate]]` block. Or it has a `[[files]]` rule
  of role `rendered`. At `84ab3c6f` that keeps 15 homes. It leaves out `hooks`, whose `[adopt]` is
  `via = "settings-merge"` (`tools/hooks/kit.toml:102`, `:116`), and `gate-lint` and
  `pytest-parallel-guardrails`, whose `argv` is empty with a `why_no_adopter`
  (`tools/gate-lint/kit.toml:32-35`, `tools/pytest-parallel-guardrails/kit.toml:42-45`). Their
  descriptors stay required by unit 48 S14. The `govkit selftest` row in `tools/gate-legs.json`
  ends holding exactly the home rows the narrowed term requires, whatever unit 48's pass landed.
  Observed by AC1.
- **S2** — No guard pushed into the broad set. Count the legs that carry each guard over
  `tools/gate-legs.json`, by the rule of `derive_guarded_legs`. The set of guards carried by more
  than 5 legs comes out the same with and without the `govkit selftest` row's `{prefix}/<home>/`
  rows. At `84ab3c6f` that set is `{prefix}/lib/` (37), `{prefix}/memory-tree/` (13), `{prefix}/`
  (12), `.githooks/` (9), `{prefix}/memory-recall/` (7) and `{prefix}/run-gates/` (7). The narrowed
  home rows leave it unchanged: `{prefix}/workflows/` reaches 5 and stays joined. Observed by AC2.
- **S3** — The reach, derived. The population is every tracked spec under `memory/builds/*/spec/`
  that meets four conditions. It is LIVE (status `OPEN`, `SPECCED`, `INPROGRESS` or `BLOCKED`, the
  checker's `LIVE`). Its filename date is on or after `SPEC_GUARD_LEGS_CUTOFF`. It carries a Gates
  heading. And a path its `### Files touched` declares, read by `read_spec_writes`
  (`tools/memory-tree/design_lib.py:528`), trips a `govkit selftest` home row by `check_guard_trips`
  (`:589`) while its §7 leg line lacks `govkit selftest`. That is the guards join's own reader and trip
  rule (`tools/check-spec-tokens.py:353-355`, `:1613-1618`). The join names a spec's first tripping
  declared path, and so does this population. The pass derives the population on its tip. At `84ab3c6f`
  it held 37 specs: 33 of this build and 4 of others (§4 "The reach at authoring"). Observed by AC3.
- **S4** — This build's own specs in the reach carry the leg. Every unit of this build ordered before
  this one is terminal at this pass, because each unit's spec closes in its own build commit, so its
  spec leaves the population. Units 51 and 52 name `govkit selftest` on their §7 leg lines as
  authored. A live spec of this build that S3 still names at the pass gains `govkit selftest` on its
  §7 leg line in a spec pass (a rev bump with its §9 line) before this unit's build pass. This unit
  never waives one. Observed by AC3.
- **S5** — Other builds' specs in the reach: one waiver row and one ask per build. Each composite
  token `govkit selftest <- <path>` that S3 names on another build's spec becomes a row of
  `memory/project/spec-token-waivers.txt`. Its reason names `[guards]`, the specs it hits, unit 48
  S17's widening, the ask and the row count, under ER:388, worded as the dGroundRules rows
  (`memory/project/spec-token-waivers.txt:36-41`). That is 33 rows today, 37 at `84ab3c6f`'s reach,
  and re-derived at the pass. This build's `BACKLOG.md` gains one ask per other build, minted with the
  next free ids of this build's family. Each ask names its specs and the leg, and is accepted when
  those specs carry `govkit selftest` or go terminal. The file's stale-row rule
  (`memory/project/spec-token-waivers.txt:3-5`) then makes the cure's commit take their rows out. Each
  gains a `SEV` row (LOW) and a `KEEP` row (the cure is another build's spec), worded as
  `TOOL-dGroundRules-109` (`memory/builds/dGroundRules/BACKLOG.md:16`, `:45-46`). Observed by AC3 and
  AC4.
- **S6** — The relaxation is recorded. The pass writes a deviation record
  `2026-10-27-build-TOOL-dFurnishedOrders-50-deviation-501.md` in this build's `build/` folder, in the
  grammar of `memory/builds/dGroundRules/build/2026-10-24-build-TOOL-dGroundRules-20-deviation-74.md`.
  It departs from `TOOL-dRetiredFork-20` (the shrink-only waiver registry). It carries
  `**Bound:** spec-token-waivers shrink-only count`, `**Tier:**`, `**Reason:**` naming §8 F1's refused
  options, and `**Surface:** memory/project/spec-token-waivers.txt`. The commit's `Decided:` trailer
  cites §8 F1 under ER:388 with its `widens:` and `relaxes:` values (the README's fork rule).
  Observed by AC4.

## 3. Non-goals (OUT)

- Revising another build's spec. The README refuses that write, so outside this build it writes only
  ask rows, as S5 does.
- Lowering `govkit selftest`'s scoped-bar cost. Unit 48 §4 "What the guard costs" prices it, and S1
  narrows it as a side effect, not as a goal.
- Moving `BROAD_LEG_FLOOR`, or teaching the guards join a second row spelling. Either changes another
  unit's gate to make this one's rows fit.
- The minors of the same report: `TOOL-dFurnishedOrders-52`. That includes id 12, which moves the
  arm's covered rule onto `check_guard_trips`.
- The report's left-shift gate (a spec-tokens mode that previews a proposed guard's reach): no clause
  of this build names it. S3's probe is that preview for this widening.
- Where a landed criterion of unit 48 cannot hold as written, its ledger answers it AMENDED, naming
  this unit.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-48` — S17's home rows, S14's descriptor rows and S16's `check_selftest_guard_coverage`, whose required set S1 narrows and whose reach S2 to S5 dispose of (id 17)
- **hands-off** `TOOL-dFurnishedOrders-52` — the narrowed required set of `check_selftest_guard_coverage`, over which unit 52 S16 moves the covered rule onto `check_guard_trips` (ids 17 and 12)
- **hands-off** `TOOL-dFurnishedOrders-57` — S3's reach, S5's waiver rows and asks and AC3, whose population unit 57 S1 reads from the checker and whose keys unit 57 S2 holds to its tokens (id 23 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-58` — S1, S5, AC2 to AC4, the Inventory, the Rollout and the write set, which unit 58 S22 to S27 settle (ids 4, 28, 19, 22, 5, 26 of the seventh audit)

## 4. Design

### The home term, after this unit

```
home(entry) := "{prefix}/<home>/"  if entry non-flat, selected by --all, and its descriptor has
                 [adopt].argv non-empty  or  [[regenerate]]  or  a [[files]] role "rendered"
               nothing              otherwise (the descriptor key stays required, unit 48 S14)
guard rows   := the home(entry) set, plus unit 48 S14 and S18's rows; no other home row
```

| home | adopt argv | regenerate | rendered | kept |
|---|---|---|---|---|
| agent-instructions, codebase-map, process-monitor, run-gates | yes | - | - | yes |
| playbook, policy | yes | yes | - | yes |
| branch-reconcile, drift-audit, lexicon, memory-recall, memory-tree, roles, runlog, unattended | yes | yes | yes | yes |
| workflows | - | yes | yes | yes |
| hooks, gate-lint, pytest-parallel-guardrails | - | - | - | no |

(Read from each `tools/*/kit.toml` at `84ab3c6f`.)

### The reach at authoring

Probe: each live, post-cutoff spec with a Gates heading, its declared paths read by
`read_spec_writes` and tripped by `check_guard_trips` against S1's rows, with the leg counts of S2.
It is a read of tracked files with no write (PINNED, 2026-10-27, `84ab3c6f`):

| reached spec | count | composite token (first tripping path) |
|---|---|---|
| `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md` | 1 | `govkit selftest <- tools/workflows/unattended-build.template.js` |
| `memory/builds/aScoutedSeam/spec/2026-10-11-spec-DEPL-aScoutedSeam-1.md` | 1 | `govkit selftest <- tools/unattended/.unattended.conf.example` |
| `memory/builds/aScoutedSeam/spec/2026-10-11-spec-KICK-aScoutedSeam-1.md` | 1 | `govkit selftest <- tools/unattended/VERBS.template.md` |
| `memory/builds/aScoutedSeam/spec/2026-10-11-spec-TOOL-aScoutedSeam-3.md` | 1 | `govkit selftest <- tools/workflows/reuse-scout.js` |
| this build's units 1 to 49 (not 4, 6, 21, 25, 30, 35 to 37, 40, 41, 43 to 48) | 33 | terminal before this pass (S4) |

The four other-build specs carry earlier `[guards]` rows for `policy fixtures` and
`routed-commits selftest` (`memory/project/spec-token-waivers.txt:34`, `:36-38`), so S5 extends a
disposal those builds already hold.

### What it does not check

- The reach is read from Files touched as written, the join's own limit
  (`tools/check-spec-tokens.py:99-100`). A spec that writes under a kit home and never declares it
  is reached by neither.
- S2 compares the broad set with and without this leg's home rows. A guard another unit pushes over
  the floor is that unit's to price.

### Inventory

Minted: nothing. S1 narrows a term of unit 48's arm, and S5 adds rows and asks in existing grammars.

### Migration

None: unit 48's arm and rows land one step earlier in the same build run.

### Rollout

Live at landing, at order 28, after unit 48 and beside unit 51. Its `tools/gate-legs.json` edit is
a watched path (`memory/guides/SESSION-KICKOFF.md:6`), so the pass bundles its own re-stamp, as
unit 48 S3 states. govkit's version moves for the kit epoch leg where its shipped bytes move. Between
unit 48's pass and this one, the guards join reds on the reach. No bar runs between them, and the
close's bar reads this unit's rows.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/project/spec-token-waivers.txt`
- `memory/builds/dFurnishedOrders/BACKLOG.md`
- `memory/builds/dFurnishedOrders/build/2026-10-27-build-TOOL-dFurnishedOrders-50-deviation-501.md`
- `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`
  when the staged `.py` edit moves it)

### Alternatives rejected

- **Revise the four other-build specs' §7 lines.** The README refuses writes outside this build
  beyond an ask row.
- **Waive every reached spec, this build's included.** This build's own specs can carry the leg, and
  a waiver where the cure is in reach is the shrink-only registry growing for nothing.
- **Keep the `{prefix}/hooks/` row.** It makes `{prefix}/hooks/` broad and drops the five hook legs
  from the guards join, a gate seen red losing its population. agent-cap has no adopter or render to
  cover.
- **Spell the hooks row without its slash.** `check_guard_trips` reads it identically, but the leg
  count would split one guard into two keys. That is a second spelling made to slip past the floor.

## 5. Production-readiness checklist

- security — no surface moves. The waiver rows widen a declared registry under a recorded ruling
  (S6).
- perf / scale — S1 takes three kit homes out of `govkit selftest`'s scoped-bar selection. S3 reads
  the live specs once per pass.
- error / empty / loading states — an empty reach writes no row and no ask. A reached spec of this
  build stops the pass before its build commit (S4).
- observability — the waiver reasons and the asks name each reached spec. The deviation record names
  the relaxed bound.
- risks — a spec authored elsewhere after this pass and before the close can enter the reach. The
  close's `spec tokens` leg names it, and the main loop disposes of it the same way.
- testing — AC1 to AC4 by probes and fixtures; the arm of §7 at the close.
- migration — none.
- user docs — none: no user-facing step changes.

## 6. Acceptance criteria

- **AC1** — When `check_selftest_guard_coverage` runs over this tree, its required set holds
  `tools/roles/` and `tools/workflows/` and no `tools/hooks/`, `tools/gate-lint/` or
  `tools/pytest-parallel-guardrails/` directory, and still holds `tools/hooks/kit.toml`. The
  `govkit selftest` row of `tools/gate-legs.json` carries no `{prefix}/hooks/` row. Over a parsed
  registry whose gate-lint descriptor copy declares `[adopt]` `argv = ["bash", "x.sh"]`, the set gains
  `tools/gate-lint/`.
  Red when: a home `apply` runs nothing from is required, or one it runs an adopter from is dropped.
  fixture: a scratch descriptor copy, passed as the arm's argument.
- **AC2** — When `python -c` counts, over `tools/gate-legs.json`, the legs carrying each guard (a
  guard listed twice in one row counts once), then lists the guards carried by more than 5 legs, it
  prints the same set with and without the `govkit selftest` row's `{prefix}/<home>/` rows. Over a
  scratch manifest copy whose `govkit selftest` row gains `{prefix}/hooks/`, the two sets differ by
  that guard.
  Red when: a home row of this leg pushes a joined guard into the broad set.
  figure: the six broad guards of S2 are PINNED from 2026-10-27; the pass's sets are DERIVED.
- **AC3** — When `python -c` derives S3's population on the pass tip, every spec it names belongs to
  another build, and each composite token it names is a row of
  `memory/project/spec-token-waivers.txt` whose reason opens `[guards]`. With one of those rows
  removed from a scratch copy of that file, the probe names the token as unwaived.
  Red when: a live spec the rows reach neither carries `govkit selftest` nor holds a waived, asked row.
  figure: 37 reached specs, 4 of other builds, PINNED from 2026-10-27; the pass's reach is DERIVED.
- **AC4** — When `grep -n "govkit selftest" memory/builds/dFurnishedOrders/BACKLOG.md` runs, it prints
  one ask row per other build that AC3's reach names, plus a `SEV` and a `KEEP` row for each. The ask
  rows name every reached spec of that build. The deviation record `-deviation-501.md` in this build's
  `build/` folder carries `**Bound:**`, `**Tier:**`, `**Reason:**` and `**Surface:**` lines.
  Red when: a waiver row holds a hit that no ask will cure, or the relaxation goes unrecorded.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the guard-coverage arm's home term over a descriptor copy that declares an adopter and over the three homes it drops, staged by restoring unit 48's unnarrowed home term after deleting `tools/govkit/__pycache__` and running Python with `-B` · none

The close's `spec tokens` leg is the whole-tree reading of AC3.

## 8. Open questions

- **F1 — How is the reach of unit 48's home rows disposed of?** Options: (a) this build's own
  reached specs carry the leg, and each other build's reached spec gets a `[guards]` waiver row and an
  ask; (b) a waiver row for every reached spec; (c) land no home row the join would read, by keeping
  the rows out of the guard. (b) waives specs whose cure is in this build's reach. (c) re-opens the
  round-4 finding unit 48 S17 closed (unit 48 §8 F2), an arm whose reads its guard does not see. (a)
  is the disposal TOOL-dGroundRules-18 §8 F2, TOOL-dGroundRules-20 §8 F1 and TOOL-dTrueNorth-20 F3
  took. RESOLVED (agent, 2026-10-27, delegated): (a), rung 5, citing ER:388 and those precedents,
  recorded as deviation 501 (S6). widens: memory/project/spec-token-waivers.txt · relaxes:
  spec-token-waivers shrink-only count
- **F2 — Which homes does the guard need (S1)?** Options: (a) every non-flat home, as unit 48 S17
  wrote; (b) the homes whose descriptor runs an adopter, regenerates or renders. Unit 48 S17 gives
  its reason as "which covers its adopter scripts and render templates", and (b) is exactly that
  reason. (a) also makes `{prefix}/hooks/` broad (S2). RESOLVED (agent, 2026-10-27, delegated): (b),
  rung 3, unit 48 S17's own stated reason and the measured floor. widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F4 — The unit this one repairs is unbuilt.** `TOOL-dFurnishedOrders-48` is specced and unbuilt at
  `84ab3c6f`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on it at the pass and
  records any item a landed unit already left in S1's end state, rung 1, the brief's rule. widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-5 promotions, id 17
  (HIGH, item H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-57, TOOL-dFurnishedOrders-58, promoted from the spec audit of the round-6 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended:

- The guards join's own reader and trip rule, `read_spec_writes` and `check_guard_trips`
  (`tools/memory-tree/design_lib.py:528`, `:589`), and its breadth rule `derive_guarded_legs`
  (`tools/check-spec-tokens.py:589-608`), for S2 and S3.
- govkit's own adopter test, `[adopt]` `argv` (`tools/govkit/govkit.py:1926-1930`), for S1.
- Unit 48's `check_selftest_guard_coverage`, for S1.
- The `[guards]` waiver grammar and the ask, SEV and KEEP rows of the earlier widenings
  (`memory/project/spec-token-waivers.txt:32-41`, `memory/builds/dGroundRules/BACKLOG.md:16-18`,
  `:45-46`), for S5.

`python tools/codebase-map/reuse_lookup.py "waive a guards join hit another build's live spec owes
after a guard widening"` ranked `hit`, `live`, `build` and `build_commit`, name-token neighbours none
of which disposes of a guard's reach. The recall probe returned TOOL-dGroundRules-109, -110 and -111,
TOOL-dGroundRules-20 §4 "The guard's reach into other builds' live specs", TOOL-dGroundRules-23 and
TOOL-dTrueNorth-21. Each disposes of a widening's reach by waiver and ask, and none disagrees with the
waiver file or the checker as read.

Recall terms used: `python tools/memory-recall/query.py "how is a guard widening's reach into other
builds' live specs disposed" --terms "guard widening spec-token waivers guards join live spec ask
section 7 leg ER:388 broad floor"`
