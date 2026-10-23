# TOOL-dGroundRules-33 — the `policy fixtures` guard holds `selftest.py`, and a trace of every source file a case reads reds one the guard misses

**Status:** DEFERRED · rev-4 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 11 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-33-deviation-21.md](../build/2026-10-23-build-TOOL-dGroundRules-33-deviation-21.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-33-deviation-62.md](../build/2026-10-23-build-TOOL-dGroundRules-33-deviation-62.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-34 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 26 to 32
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md`)
exited CONVERGED with finding **id 26 at HIGH**, item **H1**, which no other id shares. This unit is
id 26's promotion. It repairs `TOOL-dGroundRules-32`, which sits at order 10, so it builds at
order 11.

`TOOL-dGroundRules-32` S16 makes `build_fresh_target` take its answer values from `DEPLOY_FULL` in
`tools/govkit/selftest.py`, and no unit adds that file to the `policy fixtures` guard. An edit to
`DEPLOY_FULL` alone therefore skips the leg or reuses its stale green, while the three installing
cases would red on the tree. This is the recorded class
`memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`, and it has now recurred across four units
(20, 23, 25 and 32), each adding the file its own case reads by hand. This unit adds the one file the
review names, and closes the class for in-process reads: in `--fixture` mode `check_policy.py` traces
every source file it opens and reds each one whose path the `policy fixtures` guard does not cover.

## 2. Scope (IN)

- **S1** — The guard line. The `policy fixtures` row in `tools/gate-legs.json` gains
  `{prefix}/govkit/selftest.py`, spelled as that file spells its other exact paths.
  Observed by AC1.
- **S2** — The trace. In `--fixture` mode, before the first case runs, `check_policy.py` installs
  `add_source_read` with `sys.addaudithook`. On each `open` event whose mode reads and writes
  nothing, it resolves the path against the working directory, and keeps it, as a path relative to
  the source repository's top level in `/` form, when it sits under that top level and under no case's
  temporary directory. Observed by AC2, AC3.
- **S3** — The join. After the selected cases, `check_guard_trace` pipes every kept path to
  `python <source tool root>/check-spec-tokens.py --legs-for -`, as `TOOL-dGroundRules-25` S25's
  census does, and prints `policy-fixture: guard-trace · WRONG <path> · not under the policy fixtures guard`
  for each path whose output does not name `policy fixtures`. An unreachable checker is a `WRONG`,
  never a pass. It prints `policy-fixture: guard-trace · <n> source read(s)` first, so an empty
  trace is visible and is a `WRONG` of its own. Observed by AC2, AC3, AC4.
- **S4** — The build's sweep. The first `--fixture` run over the built tree reports every in-process
  read the guard misses; each reported path is added to the `policy fixtures` row in this unit's
  commit, so the run ends with no `guard-trace` `WRONG`. Observed by AC3.

## 3. Non-goals (OUT)

- Reads made by a subprocess: `git`, the deployer run from the snapshot, `node` and the shell
  enforcers. The audit hook sees only this process. `TOOL-dGroundRules-25` S24's derived imports and
  sourced files and `TOOL-dGroundRules-32` S3 and S10's derived descriptors and adopters keep
  covering them, and `fixtures-guard-census` keeps holding them.
- The route by which `build_fresh_target` reads `DEPLOY_FULL`: finding 19, an item of
  `TOOL-dGroundRules-34`. Whatever the route, the read lands on `{prefix}/govkit/selftest.py`, which
  S1 guards.
- Changing the leg's argv, subject or chunk, or any other leg's guard.
- A trace outside `--fixture` mode. `--repo` and the default run read the target, never the source.

### Edges

- **consumes-from** `TOOL-dGroundRules-32` — `build_fresh_target`'s answer values from `DEPLOY_FULL` (S16) and the guard lines S3 and S10 add, which S1 extends to the file S16 reads
- **consumes-from** `TOOL-dGroundRules-25` — `fixtures-guard-census`'s pipe to `check-spec-tokens.py --legs-for -` (S25), the one guard-match rule S3 reuses
- **hands-off** `TOOL-dGroundRules-34` — the `{prefix}/govkit/selftest.py` guard line and the trace, under which that unit's `ast` read of `DEPLOY_FULL` (finding 19) is held by the leg that runs it
- **hands-off** `TOOL-dGroundRules-35` — `add_source_read`, whose bytecode-cache reads that unit records as the source file each was compiled from (id 22 of the round-1 spec audit of units 33 and 34)
- **hands-off** `TOOL-dGroundRules-36` — `check_guard_trace`, whose join that unit narrows to the reads git does not ignore, with a count of the rest (id 7 of the round-1 spec audit of units 33 and 34)
- **hands-off** `TOOL-dGroundRules-37` — S4's additions to the `policy fixtures` row, which that unit holds to the files git tracks (id 1 of the round-1 spec audit of units 33 and 34)
- **hands-off** `TOOL-dGroundRules-38` — `add_source_read`, which that unit keeps off the source's git directory and common directory (id 18 of the round-1 spec audit of units 33 and 34)
- **hands-off** `TOOL-dGroundRules-43` — `add_source_read`'s event filter and `check_guard_trace`'s parse and working directory (ids 20, 27 and 12 of the round-1 spec audit of units 33 and 34)
- **hands-off** `TOOL-dGroundRules-49` — the guard trace, which that unit stages to observe the help page's guard line (id 11 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-52` — `add_source_read` and `check_guard_trace`, whose path decoding, unmapped-cache line and failure `WRONG` that unit amends or observes (ids 9, 34, 37 and 38 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-64` — AC4's staging, which that unit spells whole as `GUARD_OUT_SELFTEST` and `READ_SELFTEST` (the adopted discovery of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23, except where a line names another
revision.

- `tools/govkit/selftest.py:703-712` assigns `DEPLOY_FULL`, whose `[answers]` table holds
  `manifest_path` and `user_skills`; `:195` runs `resolve_gov_pin` at import.
- The `govkit selftest` row of `tools/gate-legs.json` guards `{prefix}/govkit/`; the `policy fixtures`
  row does not exist at base, so its guard is exactly what units 1, 17, 18, 20, 23, 25 and 32
  declare, and a grep of every spec of this build for `selftest.py` finds no guard addition naming it
  (review id 26, re-read 2026-10-23 at `f4d31452a`).
- `python -c` with `sys.addaudithook` recording `open` events, then
  `pathlib.Path("tools/govkit/selftest.py").read_text()`, recorded
  `('open', 'tools\\govkit\\selftest.py', 'r')` on Python 3.14.6 on this node (run 2026-10-23): the
  path arrives as the caller spelled it, relative and with `\`, so S2 resolves it before it compares.
- `--legs-for` is a query that prints, per path, the legs whose guard it trips
  (`tools/check-spec-tokens.py:179-182`, `:638`).

### The trace

```text
add_source_read(event, args):              # sys.addaudithook, installed once by --fixture
    if event != "open": return
    path, mode = args[0], args[1] or "r"
    if path is an int or any of "wax+" in mode: return
    p = resolve(path)
    if p under source top level and under no case temporary directory:
        kept.add(p relative to the top level, "/"-joined)

check_guard_trace():                       # after the selected cases
    print "policy-fixture: guard-trace · <len(kept)> source read(s)"
    WRONG if kept is empty
    out = run(python <source tool root>/check-spec-tokens.py --legs-for -, stdin = kept)
    WRONG if the checker did not run
    for each kept path whose lines in out name no "policy fixtures": WRONG naming it
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `add_source_read` | py.function | `tools/policy/check_policy.py` |
| `check_guard_trace` | py.function | `tools/policy/check_policy.py` |
| `guard-trace` | a `policy-fixture:` line label | `tools/policy/check_policy.py` |

`lexicon.py --suggest` answered OK for `add_source_read` and `check_guard_trace` under
`py.function` on 2026-10-23.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The one guard line alone (§8 F1 (a)).** It closes this instance and leaves the class open for the
  next file a case reads by name, the fifth recurrence.
- **A typed list of the files each case reads, joined to the guard.** A second carrier of the same
  fact, which the next case forgets exactly as the guard was forgotten.

## 5. Production-readiness checklist

- security — N/A: the hook reads event arguments and writes nothing; no write surface is added.
- perf / scale — one set insert per `open` event and one `--legs-for` run per `--fixture` run.
- error / empty / loading states — an empty trace and an unreachable checker are each a named
  `WRONG`, never a pass.
- observability — each `WRONG` names the path; the count line says how many reads were traced.
- risks — the hook sees only in-process reads (§3); a path the build's sweep adds to the guard widens
  when the leg runs, never when it is skipped.
- testing — the guard-trace lines under `--fixture`, with AC1 to AC4.
- migration — none.
- user docs — N/A: a gov-only leg.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the policy kit's files by bare name,
`check_policy.py` under the kit, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` runs on the
  built tree, its output names `policy fixtures`.
  Red when: an edit to `DEPLOY_FULL` alone can skip the leg that runs the installing cases.
- **AC2** — When a scratch copy of the built tree carries one `open()` of the repository's root
  `README.md`, staged into the first line of `build_fresh_target`, and
  `python check_policy.py --fixture adopter-fresh-target` runs there, it prints
  `guard-trace · WRONG README.md`.
  Red when: a case reads a source file outside the guard and the leg stays silent.
- **AC3** — When `python check_policy.py --fixture` runs on the built tree, it prints the
  `guard-trace` count line with a count above zero and no `guard-trace` `WRONG`.
  Red when: a source file a case reads in process sits outside the `policy fixtures` guard.
  figure: the count is DERIVED from the run at observation time.
- **AC4** — When selftest.py is staged out of the `policy fixtures` row in a scratch
  copy's `gate-legs.json` and a case there reads selftest.py in process, the run prints
  `guard-trace · WRONG tools/govkit/selftest.py`.
  Red when: the guard can lose the file the answer values come from with nothing to say so.
  fixture: the in-process read is `TOOL-dGroundRules-34` S23's; before that unit, the staged copy
  adds one `open()` of selftest.py to `build_fresh_target`, as AC2 does for `README.md`.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the trace;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture`, the `guard-trace` join) · covers AC2 AC4 · one in-process read of a file outside the `policy fixtures` guard staged into `build_fresh_target`, then `selftest.py` staged out of the guard · none

## 8. Open questions

- **F1 — How is the file `build_fresh_target` reads kept inside the guard of the leg that runs it?**
  (a) The guard gains `{prefix}/govkit/selftest.py` and `fixtures-guard-census` holds it, the
  review's fix. (b) (a)'s guard line, and a trace of every source file the `--fixture` process opens,
  each joined to the guard through `--legs-for`. (c) A typed list of the files each case reads,
  joined to the guard. (a) meets AC1 and AC4 for this file and leaves the class open: four units have
  each added their own file by hand, and the fifth is a follow-up nothing names. (c) is a second
  carrier of the fact the guard holds, forgotten the same way. (b) meets every criterion and leaves
  no follow-up for in-process reads. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 26 (HIGH, item H1) of the round-1 spec
  audit of units 26 to 32, from the review's sound fix and its left-shift, the class gate, with
  `DEPLOY_FULL`, the leg manifest and the audit hook's `open` event read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-35, TOOL-dGroundRules-36, TOOL-dGroundRules-37, TOOL-dGroundRules-38 and TOOL-dGroundRules-43 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 33 and 34 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-49`, `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.
- rev-4 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-64`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.

## 10. Reuse audit

The seams extended are the `policy fixtures` row in `tools/gate-legs.json` and the guard-match rule
`TOOL-dGroundRules-25` S25 already routes through `check-spec-tokens.py --legs-for -`, so the trace
spells no match rule of its own (`--legs-for`, `tools/check-spec-tokens.py:638`, verified at source).
`python tools/codebase-map/reuse_lookup.py "which gate leg guard covers a file a fixture case reads"`
ranked `read`, `read_text`, `legs`, `leg`, `fixture` and `covers`, none of which records what a
process opens. No existing seam fits the trace itself: no tool in the tree installs an audit hook (a
grep of `tools/` for `addaudithook` printed nothing on 2026-10-23). The recall probe returned
`TOOL-aHeardState-6`, which puts this class on the bug-class checklist a reviewer reads rather than
on a detector; `TOOL-dGroundRules-20`, the guard's first widening by hand; this audit's H1; and the
round-1 and round-2 items that widened the guard again. All agree with source, and the repetition is
the evidence for §8 F1 (b).

Recall terms used: `python tools/memory-recall/query.py "how does a held suite's guard learn every
sibling file its cases read" --terms "policy fixtures guard held suite sibling kit legs-for
selftest.py DEPLOY_FULL fixture census"`
