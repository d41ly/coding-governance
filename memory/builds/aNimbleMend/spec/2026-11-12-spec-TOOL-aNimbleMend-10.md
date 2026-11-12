# TOOL-aNimbleMend-10 — the inline lane's limits, graded on every `Red-fix:` commit

**Status:** SPECCED · rev-1 · 2026-11-12 · node a · Tier-2 · base 1265772c · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |

<!-- /gen:spec-records -->

## 1. Goal

The inline lane admits a product change with no spec, so what such a change may be has to be a
gate and not a sentence. This unit grades every commit carrying a `Red-fix:` trailer against four
limits in the commit grader that already reads each commit's paths, and gives the same predicate a
verb that grades one commit in seconds.

## 2. Scope (IN)

- **S1** — A limits pass, `check_red_fix_limits`, in `tools/memory-tree/routed_commits.py`, run by
  `check_routed_commits` over every non-merge commit of each population that carries a `Red-fix:`
  trailer. A finding moves the leg's exit to 1. Observed by AC1 to AC5.
- **S2** — Limit L1, the size bound: at most 3 changed paths under `ROUTED_PATHS`, and at most 60
  changed lines, both sides of the diff counted, over them. A binary path counts as over the bound. Observed by
  AC1.
- **S3** — Limit L2, no guarded policy file: the commit touches no path the policy kit's
  `guarded-paths.txt` lists. Where no policy kit resolves, every path under `.governance/` is
  refused instead. Observed by AC2.
- **S4** — Limit L3, no spec edit: the commit touches no path under any build's `spec/` folder, by
  `tree_lib.py#build_spec_path_re`. That covers a spec revision, a fork marked resolved, another
  build's spec and a CLOSED spec alike. Observed by AC3.
- **S5** — Limit L4, no new surface: the commit adds no path under `ROUTED_PATHS`. A rename is read
  as a deletion and an addition, so it is refused too. Observed by AC4.
- **S6** — The waiver is the existing one. A sha in `ROUTED_COMMIT_WAIVED` excuses a limits finding
  in the WHOLE half, the RANGE half reads no waiver, and the stale-waiver rule counts a limits
  finding as a violation. Observed by AC5.
- **S7** — One summary line on every run, after the routing lines and before the deviation join's,
  naming the count graded and the bound, so a population holding no fix commit says so. Observed by
  AC6.
- **S8** — A verb, `routed_commits.py --red-fix-limits <rev>`, that grades the one commit `<rev>`
  names with the same predicate and prints the same finding lines. Exit 0 inside the limits, 1 over
  one, 2 when the rev names no commit or the commit carries no trailer. Observed by AC1 to AC4 and
  AC7.
- **S9** — The limits pass makes no `git` call in a population holding no fix commit, and at most
  one per population otherwise, whatever the commit count. Observed by AC6.

## 3. Non-goals (OUT)

- Admitting the fix, and deciding whether the named leg is an open red. Both are
  TOOL-aNimbleMend-8's.
- The fix's record and its join, which are TOOL-aNimbleMend-9's.
- "No new feature" and "no design choice" as such. No reader can tell a feature from a fix inside
  60 lines of an existing file. L1 and L4 bound what a feature could be, and §4 says what is left
  unchecked.
- Calling the verb from a hook or from the run point. This unit ships the verb; no hook is changed
  here.
- A policy key for the bound. TOOL-aNimbleMend-1 mints two keys and the bound is neither. It is two
  constants in one file until an adopter asks for another figure.
- A second waiver list. `ROUTED_COMMIT_WAIVED` is the one escape for a landed commit.
- Reading the lane's switch. A fix commit in history is graded whether the lane is on or off, and a
  tree that never used the lane holds none.
- The kit version, which the lander's `mint` moves once, after the last unit.

### Edges

- **consumes-from** `TOOL-aNimbleMend-8` — the `red_fix` list on each commit
  `read_routed_commits` returns, the `Red-fix:` values of that commit. Without it no commit is in
  this unit's population.

## 4. Design

### Evidence

- `routed_commits.py#read_routed_commits` reads every commit of a range in one `git log` pass:
  sha, parents, date, subject, the `Pass:` trailer and `--name-only --no-renames` paths. It reads
  no line counts and no path status.
- `routed_commits.py#check_routed_commits` grades two populations at a resolvable base, RANGE and
  WHOLE beside it, applies `ROUTED_COMMIT_WAIVED` in WHOLE alone, and reds a waiver naming no
  violation as stale.
- `routed_commits.py#check_deviation_join` is hosted after the routing lines and never moves the
  exit. This pass is hosted the same way and does move it.
- The self-test's AC6 arm holds the `git` spawn count constant between 3 and 30 routed commits.
- `tools/policy/guarded-paths.txt` lists four paths at 1265772c, all under `.governance/`. The
  pre-commit hook and `tools/policy/guard.py` read it at HEAD.
- `tools/memory-tree/backlog.py#resolve_kit_dir` is the kit's inline resolver of a sibling kit,
  already used by `build_records.py#read_override_value` to find the policy kit.
- The three fix units the prompt cites measure as follows over `ROUTED_PATHS`, by
  `git show --numstat`: PLAY-dOrderedCharter-80 at 82711535 is 11 paths and 433 lines;
  PLAY-dOrderedCharter-81 at 84a28f63 is 2 paths and 49 lines; PLAY-dOrderedCharter-82 at a5741d9a
  is 2 paths and 47 lines. These are PINNED, measured 2026-11-12. Unit 80 fixed several legs in one
  commit and added arms; units 81 and 82 are each one bar's narrowest fix.

### The limits

| # | Limit | Predicate over one fix commit | Finding names |
|---|---|---|---|
| L1 | size | more than 3 paths under `ROUTED_PATHS`, or more than 60 added plus deleted lines over them, or a binary one | both counts and both bounds |
| L2 | guarded policy file | a path equal to a line of the resolved `guarded-paths.txt`; with no list, a path under `.governance/` | the path |
| L3 | spec edit | a path matching `build_spec_path_re` for this tree's `MEMORY_ROOT` | the path |
| L4 | new surface | a path under `ROUTED_PATHS` whose status is an addition | the path |

A commit over several limits prints one line per limit. The lines follow one header:

```
routed-commits FAILED — a Red-fix commit is outside the inline lane's limits:
  <sha8> <subject> — L1 size: 5 path(s), 140 line(s); the bound is 3 and 60
```

The summary line, on every run and once per population:

```
routed-commits: red-fix limits · graded <N> · bound 3 path(s), 60 line(s) · <W> waived
```

The two bounds are named constants beside `SAY`, each with a comment naming this unit and F1.

### The read

The trailer's presence comes from the first log pass: a fix commit is one whose `red_fix` list,
which TOOL-aNimbleMend-8 adds to `read_routed_commits`, is not empty. This unit adds no field to
that format string. A fix commit is graded whether or not it also names a unit, since
TOOL-aNimbleMend-8 reads the trailer only on a commit that names none. Line counts and path status need a second read. It is one
`git log` per population over the fix commits alone, carrying both the numeric and the raw status
form, and it is not made when the population holds no fix commit. The list is read at the working
tree's `guarded-paths.txt`, once per run, and only when a fix commit exists.

### The verb

```
python tools/memory-tree/routed_commits.py --red-fix-limits <rev>
```

It loads the conf as the leg does, resolves `<rev>`, and grades that commit alone, merge or not. It
reads no waiver. It is the probe a builder or the main loop can run straight after a fix commit,
where the leg itself runs at the close.

### What this does not check

- Whether the change is a fix. A 60-line change to an existing file that adds a behaviour passes
  all four limits.
- A new surface made inside an existing file: a new leg row in `tools/gate-legs.json`, a new key in
  a catalogue, a new verb in a script. L4 reads path status, not content.
- A deleted path. Removing a file is how several of the cheap legs are fixed, so L4 does not refuse
  it; F2 asks whether it should.
- The build README, `memory/DECISIONS.md` and every other record outside `spec/`.
- A fix commit that also removes a line of `guarded-paths.txt`. The list is read as the tree
  holds it, not at the commit's parent.
- A merge commit in the leg's populations, which this leg never grades.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| function `check_red_fix_limits` | `routed_commits.py` | the `lexicon naming predicates` leg |
| constants `RED_FIX_MAX_PATHS`, `RED_FIX_MAX_LINES` | `routed_commits.py` | AC1 |
| verb `--red-fix-limits` | `routed_commits.py#main` | AC7 |

### The fixture

One scratch repository, built by the self-test's own `build_fixture` and, for a pass's probe, by
hand under a short path in the host temp directory. Its conf is `set_fixture_conf`'s defaults, so
`ROUTED_PATHS` is `src/`.

| Commit | Trailer | Holds | Expected |
|---|---|---|---|
| c1 | none | `src/a.txt`, `src/b.txt`, `src/c.txt`, `src/d.txt`, the spec of `TOOL-tFix-1`, `.governance/policy.toml` | not graded by the limits |
| c2 | `Red-fix: leg one` | 3 lines changed in `src/a.txt` | inside every limit |
| c3 | `Red-fix: leg one` | one line changed in each of four `src/` files | L1, by paths |
| c4 | `Red-fix: leg one` | 61 lines changed in `src/a.txt` | L1, by lines |
| c5 | `Red-fix: leg one` | one line in `src/a.txt` and one in `.governance/policy.toml` | L2 |
| c6 | `Red-fix: leg one` | one line in `src/a.txt` and one in the spec | L3 |
| c7 | `Red-fix: leg one` | adds a fifth file under `src/` | L4 |

Each fix commit also names `TOOL-tFix-1` in its subject, so the routing half of the leg is green
whatever TOOL-aNimbleMend-8 decides about a fix commit with no unit.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **A new checker file and a new leg.** The limits are a predicate over the commits and paths
  `routed_commits.py` already reads, at the populations it already derives, with the waiver it
  already has. A second file would re-derive the range, the conf and the fixture builder.
- **Grading at the write gate, in `tools/hooks/scratch-guard.js`.** The hook sees one Edit or Write
  call. A size bound and a path set are properties of the whole commit, and a change made through a
  shell never reaches the hook.
- **Refusing every path under `.governance/`.** The policy kit owns the guarded list in one file,
  and a second spelling here would drift from it. The whole directory is the fallback only where
  that list cannot be found.
- **A bound in changed files alone.** One file can hold a rewrite. Unit 80's largest file moved 230
  lines.

## 5. Production-readiness checklist

- security — this unit narrows a write lane and adds no surface. L2 is deny by default where the
  guarded list does not resolve. The rev given to the verb is passed to `git` as one argument.
- perf / scale — no `git` call where no fix commit exists, and one per population otherwise; S9
  and AC6 hold it.
- error / empty / loading states — an empty population prints the summary line with zero graded; an
  unreadable conf or a failed `git` call is the leg's existing exit 2.
- observability — the summary line, and one line per commit per limit.
- risks — a limits finding on a commit already on the default branch reds every later bar until its
  sha is waived, as a routing violation does today. The RANGE half refuses it before it is pushed.
- testing — the fixture above, through the verb in a pass and through the self-test arm of §7 at
  the close.
- migration — additive: one more output line from the leg, and no finding in a tree with no fix
  commit.
- user docs — the leg's paragraph in `tools/memory-tree/README.md` states the four limits and the
  verb. The lane's help page is TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/routed_commits.py --red-fix-limits <sha>` runs in the
  fixture for c2, c3 and c4, it exits 0 for c2, and exits 1 for c3 and for c4 with a line naming
  `L1`, the measured counts and the bound.
  Red when: the bound counts paths outside `ROUTED_PATHS`, counts only added lines, or reads 60
  changed lines as over it.
  fixture: the scratch repository of §4, "The fixture"; the tree holds none today.
  figure: 3 and 60 are PINNED constants of this unit, open under F1.
- **AC2** — When the same `--red-fix-limits` verb runs for c5, it exits 1 naming `L2` and
  `.governance/policy.toml`; and with the policy kit made unresolvable, it still exits 1 for c5.
  Red when: the limit reads no list and passes, or an unresolved kit turns the limit off.
- **AC3** — When the `--red-fix-limits` verb runs for c6, it exits 1 naming `L3` and the spec's
  path.
  Red when: a fix commit can revise a spec.
- **AC4** — When the `--red-fix-limits` verb runs for c7, it exits 1 naming `L4` and
  the added path.
  Red when: path status is not read, so an added file passes as a change.
- **AC5** — When `python tools/memory-tree/routed_commits.py` runs in the fixture with
  `ROUTED_COMMIT_WAIVED` blank, it exits 1 and lists c3 to c7 under the limits header and not c2;
  with those five shas waived it exits 0 and the summary reads `5 waived`; with c2's sha added it
  exits 1 naming that sha as stale.
  Red when: the pass does not move the exit, or a waived limits finding is reported as a stale
  waiver.
  figure: 5 is DERIVED from the fixture's commits.
- **AC6** — When the leg runs in a fixture holding no `Red-fix:` commit, it prints
  `red-fix limits · graded 0` once per population, and `routed_commits.GIT_SPAWNS` rises by the
  same amount over 3 routed commits as over 30.
  Red when: the pass makes a `git` call per commit, or prints nothing where it graded nothing.
- **AC7** — When `--red-fix-limits` is given a rev naming no commit, and then c1, which carries no
  trailer, each run exits 2 with a `routed-commits REFUSED` line saying which.
  Red when: a commit that is no fix reads as inside the limits.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `policy fixtures` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `docs` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. `policy fixtures` guards
`tools/memory-tree/routed_commits.py`. `routed-commits selftest` holds the new arm and is in the
held tier, so the close runs it only where it asks for that tier.

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the fixture's c3 to c7, one commit per limit, and a trailer-free fixture for the spawn count · none

## 8. Open questions

- **F1 — What is the size bound?** The prompt asks for a stated bound and names none. The measured
  precedents are in §4, "Evidence".
  - Option A: 3 paths and 60 lines. It admits units 81 and 82 with about a fifth to spare and
    sends unit 80 to a spec.
  - Option B: 5 paths and 120 lines. It doubles the room and still refuses unit 80.
  - Option C: 12 paths and 450 lines, so that unit 80 would have passed. It bounds almost nothing.
  - Recommendation: A. A fix larger than every single-bar precedent is the case the prompt sends
    through a spec, and a commit that is over can be split per leg.
- **F2 — What stands in for "no new surface"?** A surface cannot be read from a diff, so the gate
  needs a proxy.
  - Option A: no added path under `ROUTED_PATHS`. Deletions pass.
  - Option B: no added and no deleted path. It also refuses the fix of a dead-path or docs red made
    by removing a stale file.
  - Option C: A, and also no change to `tools/gate-legs.json` or to a catalogue file. It refuses a
    fix to a leg's own row, such as a wrong guard.
  - Recommendation: A. It is the one reading that never refuses a narrowest fix among the measured
    precedents, and what it leaves open is stated in §4.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.

## 10. Reuse audit

The seam is the commit grader. `python tools/codebase-map/reuse_lookup.py "bound the size of a
commit and refuse guarded policy files or closed spec edits"` ranked `read_routed_commits` and
`check_routed_commits` of `tools/memory-tree/routed_commits.py`, and reading the file confirms the
fit: one log pass per population, the RANGE and WHOLE halves, `ROUTED_COMMIT_WAIVED` with its stale
rule, `test_routed_path` for the product set, and `build_fixture` for scratch histories. The spec
predicate is `tree_lib.py#build_spec_path_re`, the guarded list is `tools/policy/guarded-paths.txt`
and the way to it is `backlog.py#resolve_kit_dir`. For a size bound on a commit, no existing seam
fits: `grep -rnE "numstat|shortstat" tools/memory-tree` at 1265772c prints nothing, so the line count
is the one new read. Recall returned TOOL-dScopedBuild-3, a DEFERRED design that grades each pushed
commit's paths against its unit's write set beside `check_deviation_join`; it is unbuilt, and this
unit takes the same host. It also returned the deviation join's hosting record, TOOL-dTrueNorth-4,
whose shape S7 follows.

Recall terms used: `python tools/memory-recall/query.py "how is a typed build record joined to the
commit it describes and how is a commit graded for what it may touch" --terms "typed record kind
build_records deviation join routed commits trailer hygiene check guarded-paths red fix inline lane
size bound"`
