# TOOL-dPavedRoad-1 — a spec writer grades its own spec: `check-spec-tokens.py --spec` reads the named spec whatever its status, and the writer's role may run it

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 1 · closes TOOL-dFairHearing-54 TOOL-aDeferredBar-6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-dPavedRoad-1-ledger.md](../build/2026-11-10-build-TOOL-dPavedRoad-1-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-dPavedRoad-1-bar-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-bar-fix-brief.md) | research | — |
| [2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md](../prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md) | research | TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4 |
| [2026-11-10-review-TOOL-dPavedRoad-1-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-dPavedRoad-1-closing-diff-round1.md) | diff-review | TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4 |

<!-- /gen:spec-records -->

## 1. Goal

About 17 of the 37 corrections dSafePassage sent to its agents were spec-token hits the writer
could not see. That figure is PINNED from the brief, which measured it from dSafePassage's
transcript on 2026-11-10. The writer could not see them for three reasons, each read in the code:
its role text forbids every gate but two, the checker grades only `LIVE` specs, and it grades only
tracked ones, while a writer's spec is uncommitted when the writer returns. This unit adds a
`--spec` mode that grades the named specs as if live, whatever their status and whether or not git
tracks them, grants the writer's role the leg, and tells the writer to run it.

## 2. Scope (IN)

- **S1** — `tools/check-spec-tokens.py --spec <path>...` grades exactly the named specs, each as if
  it were live. Its status is not read, and the spec need not be tracked by git. Observed by AC1.
- **S2** — under `--spec`, every per-spec join runs over the named specs as the full run runs it.
  The hands-off join reads its sibling map from the named spec's own build folder on disk. Four
  arms that read the corpus rather than a spec do not run, and each says so on its report line:
  the carries join, the packet join, the stale-waiver arm and the stale high-water arm (§4 "What
  runs under --spec"). Observed by AC2 and AC3.
- **S3** — a `--spec` operand that is absent, names no file, lies outside the repository or is not
  a spec under `memory/builds/<slug>/spec/` is refused with exit 2 and a `REFUSING` line naming
  it. Observed by AC4.
- **S4** — the checker's module docstring documents `--spec` beside `--list` and `--legs-for`
  (check-spec-tokens.py:239-249), including the four arms it does not run. NOT OBSERVED by a
  criterion: it is prose, read at the closing review.
- **S5** — `tools/roles/house/policy.toml` grants `gov-spec-writer` the leg
  `spec tokens (a spec's own names resolve)`, written with the optional `?` marker, and the role
  index and agent types are re-rendered from it. Observed by AC5 and AC6.
- **S6** — line 36 of `tools/roles/agents/gov-spec-writer.agent.md` tells the writer to run
  `python tools/check-spec-tokens.py --spec <path>` over each spec it wrote and to fix every hit
  before it returns (§4 "The role text"). Observed by AC7.
- **S7** — `tools/check-spec-tokens.test.sh` gains the `--spec` arms §7's `New arm:` line names,
  and its `FLOOR_ASSERTIONS` rises by their count. Observed at the close through that line, which
  covers AC1 to AC4; NOT OBSERVED by a pass criterion, because a pass runs no suite.

## 3. Non-goals (OUT)

- No change to what the full run grades. Without `--spec` the population is still the tracked
  `LIVE` specs (check-spec-tokens.py:365, 1544-1554), so a DEFERRED spec stays ungraded there.
  TOOL-dGatedProse-11 asks for that change and stays open.
- No carries or packet join under `--spec`. The carries join reads each chain-build spec's tracked
  history, which an uncommitted spec does not have. The full run at the close still grades both.
- No change to `tools/hooks/scratch-guard.js`. Its G1 row compares a command's whole argv, which
  is why `--spec` is admitted today (§4 "What the grant admits"). Changing that match is a
  separate mechanism.
- No change to the spec-audit policy, the dispatch order gate, the packet regeneration or the
  manifest ratchet, and no new role.
- No help page. The checker is gov-internal: `tools/govkit/registry.toml:226-233` exempts it from
  shipping, so no page under `help/` documents it. `help/roles.md:44-46` already says the
  `[gates]` table lists the legs a role may run, which stays true.

### Edges

none

The other three units of dPavedRoad write `tools/hooks/format-guard.js`, `tools/roles/handoff.py`
and `tools/memory-tree/check-memory-hygiene.sh`. None of them is in this unit's write set, and this
unit reads none of them.

## 4. Design

Every line cited here was read at `ae6735c1`, the default-branch tip. The working branch's HEAD,
`14320c98`, changes nothing under `tools/` or `.claude/`.

### Why the writer could not see its hits

1. The role text: `tools/roles/agents/gov-spec-writer.agent.md:36` says the writer may run the
   memory hygiene gate and the naming lexicon, "and no other gate". Its rendered copy is
   `.claude/agents/gov-spec-writer.md:32`. A `git grep` of that sentence finds those two files and
   no other outside `memory/builds/`.
2. The status filter: `LIVE` admits only OPEN, SPECCED, INPROGRESS and BLOCKED
   (check-spec-tokens.py:365), and `main` keeps only specs that match it (:1549-1552).
3. The tracked filter: the population is drawn from `read_tracked`, which is `git ls-files`
   (:556-557, :1536, :1544-1545). A writer does not commit, so its spec is in no population at all,
   whatever its status.
4. The hook: the writer's allowlist in `.claude/roles.json` is `memory hygiene` and
   `lexicon naming predicates`, from `tools/roles/house/policy.toml:27`. Records in the recall
   probe show writers refused when they ran the bare leg.

### The --spec population

`main` reads the operands after `--spec`, in the same way `--legs-for` reads its operands
(:1537-1538): every later argument that does not open with `-`. The branch sits after the
`SPEC_DATE` refusal (:1539-1543) and takes the place of the population walk (:1544-1558) for this
mode only.

Each operand is resolved against the working directory and made relative to the root as a POSIX
path. It must then match the walk's own pattern, `memory/builds/[^/]+/spec/.*\.md$` (:1545),
because every dated join reads the filename date through `SPEC_DATE` and the hands-off join reads
the build from the path's third segment (:850). The refusals, each exit 2:

| operand | line |
|---|---|
| none after the flag | `spec-tokens: REFUSING — --spec names no spec` |
| not a file | `spec-tokens: REFUSING — --spec <operand> is not a file` |
| outside the root, or not under a build's `spec/` folder | `spec-tokens: REFUSING — --spec <operand> is not a spec under memory/builds/<slug>/spec/` |

Then `specs` and `unretired` are both the named list and `frozen` is 0. `LIVE` is not consulted.
The tracked set `files` is still read, because the path, cites and arm-labels joins resolve against
it, and the named spec need not be in it.

### What runs under --spec

| arm | under `--spec` | why |
|---|---|---|
| legs, legline, paths, bar, guards, cites, claims, covers, source, ac-order | graded as written | the loop at :1633-1803 reads only `specs` |
| hands-off | graded; sibling map from disk | below |
| size | hits graded; stale rows not reported | the stale loop (:1393-1403) reads any row whose spec is not in `specs` as terminal |
| supersede | graded | :1858 reads only `specs` |
| arm-labels | graded over the named specs | :1862 reads `unretired` |
| waiver rows | applied to hits; stale rows not reported | :1871-1875 calls a row stale when no graded spec produces it, so a one-spec run would call almost every row stale |
| carries | not run | :1825-1844 reads every tracked chain-build spec and its history |
| packet | not run | :1847-1853 reads live chain runs, not specs |

The hands-off sibling map: the full run builds it from the tracked `LIVE` specs (:1808). Under
`--spec` it is `read_spec_uids` (:806-820) over every `.md` file on disk under each named spec's
own `memory/builds/<slug>/spec/` folder whose text matches `LIVE`, plus the named specs. It reads
siblings on disk because a writer's group siblings are uncommitted when it runs. It keeps the
`LIVE` test because the full run treats a hand-off to a terminal sibling as silent, and `--spec`
must not red what the full run passes.

The report: the first summary line (:1885) opens `spec-tokens: --spec · <n> named spec(s) graded
whatever their status ·` and then its usual fields. The carries and packet lines read
`spec-tokens: carries join · skipped under --spec` and `spec-tokens: packet join · skipped under
--spec`. Every other line keeps its text. Exit codes are unchanged: 1 on an unwaived hit, 0
otherwise, 0 under `--list`.

The checker writes no file: it has no `write_text`, `write_bytes` or open-for-write call. So a
writer running it stays inside the spec-writer role's write boundary.

### The grant

`tools/roles/house/policy.toml:27` becomes:

```toml
gov-spec-writer = ["memory hygiene", "lexicon naming predicates?", "spec tokens (a spec's own names resolve)?"]
```

The `?` is required. The policy file is a seed every adopter receives (`tools/roles/kit.toml:31-40`),
and the checker is gov-only (`tools/govkit/registry.toml:226-233`). In an adopter's manifest the
leg is therefore absent, and an unmarked name there is an R12 defect (roles_lib.py:494-499). The
lexicon grant is marked for the same reason (commit `8eccf905b`). Then
`python tools/roles/render_agents.py --write` renders `.claude/roles.json` and the agent types.

### What the grant admits

This was measured in the hook, and the reader should know it. Row G1 takes a leg's words from its
first path-bearing word (scratch-guard.js:1366-1368), so this leg's words are the single script
path. It then requires the command's argv to have exactly that length (:1378). The `--spec`
command has three words, so it is no G1 match, and it is admitted with or without the grant. The
hook's header states this as its ceiling (:123-127). What the grant admits is the bare corpus run,
`python tools/check-spec-tokens.py`, which took 465.2 s at 2026-10-28
(tools/run-gates/ceiling-evidence.txt:134, PINNED). The brief names the grant, and it is the
declared one: if G1 is ever tightened to match a leg's scoped variants, the grant keeps `--spec`
admitted. The role text steers the writer to `--spec`, never to the bare run.

### The role text

`tools/roles/agents/gov-spec-writer.agent.md:36` becomes these three lines. The phrase
`check-spec-tokens.py --spec` stays on one line so that AC7's grep finds it:

```markdown
- You may run the memory hygiene gate and the naming lexicon over your specs, and, where this
  repository has it, `python tools/check-spec-tokens.py --spec <path>` over each spec you wrote,
  fixing every hit it names before you return. You run no other gate.
```

The rendered copy `.claude/agents/gov-spec-writer.md` follows from `render_agents.py --write`. The
body substitutes only `{{MEMORY_ROOT}}` (roles_lib.py:53, :605), so the path is spelled as gov
installs it. That is correct wherever the checker exists, because it ships nowhere else.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/roles/house/policy.toml`
- `tools/roles/agents/gov-spec-writer.agent.md`
- `.claude/roles.json`
- `.claude/agents/gov-spec-writer.md`

### Alternatives rejected

- **The house overlay instead of line 36.** `tools/roles/house/gov-spec-writer.md` is empty and is
  appended under `## House rules` (help/roles.md:42-43). Line 36's "and no other gate" would then
  contradict the overlay. The overlay is also a seed every new adopter receives, so it reaches
  adopters just as the engine line does.
- **Grading every DEFERRED spec in the full run.** That changes what the bar grades, which the
  brief's non-goals exclude. It is TOOL-dGatedProse-11's mechanism.
- **Telling the writer to run `--list` over the tree** (TOOL-aDeferredBar-6's candidate). `--list`
  grades only tracked `LIVE` specs, so it never sees the writer's uncommitted spec. It also costs
  the full corpus run.

## 5. Production-readiness checklist

- security: no new write path. The checker opens files for reading only, and `--spec` refuses an
  operand outside the root or outside a build's `spec/` folder. The grant widens a role's gate list
  by one read-only leg.
- perf / scale: `--spec` reads the named specs, their build's spec folder and the manifest. It
  does not run the carries and packet joins, which read history and live runs. The three cutoff
  relations still read the history of `.memory-tree.conf` only (:722-753). Unmeasured; the
  builder records the figure as AC1's `cost:`.
- error / empty / loading states: S3's three refusals, exit 2. An empty population cannot arise,
  because an operand must name a file.
- observability: the first summary line names the mode and the count, and the carries and packet
  lines say they were skipped. A `--spec` run therefore cannot be read as the full run.
- risks: a writer running the bare leg, which the grant admits, pays the corpus cost. The role
  text names `--spec` only. A `--spec` green does not mean the bar is green: the carries join, the
  packet join and every other spec still grade at the close.
- testing: AC1 to AC7, and §7's `New arm:`. Checklist classes selected for these paths:
  fixture-passes-by-finding-nothing, answered by AC1's and AC6's negative halves, and
  criterion-asserts-what-its-own-command-cannot-show, answered by each criterion naming a line its
  command prints.
- migration: N/A — no data or state. The seed's new line reaches only a new adopter, because
  `update` never rewrites a seed.
- user docs: N/A — the checker is gov-internal and exempt from shipping (registry.toml:226-233), and
  `help/roles.md` already describes `[gates]` in terms this unit leaves true.

## 6. Acceptance criteria

- **AC1** — Set up a clone of the tree under %TEMP% holding an untracked DEFERRED fixture spec for
  this build, dated 2026-11-10, whose acceptance section lists AC2 before AC1. When
  `python tools/check-spec-tokens.py --spec <path>` runs over the fixture in that clone, it exits 1
  and prints a hit line carrying `[ac-order]` and the fixture's path.
  Red when: the population still filters on `LIVE` or on `git ls-files`, so the fixture is graded
  by nothing and the run exits 0.
  fixture: a clone under %TEMP%/<short-name>, into which the pass writes the fixture; the tree
  holds none. `SPEC_AC_ORDER_CUTOFF` (2026-10-23) arms the join for this date.
  cost: the wall time of one `--spec` run, recorded by the builder.
- **AC2** — When the fixture's labels are put back in ascending order and the same `--spec` command
  reruns, it exits 0, prints no `STALE` line, and prints `skipped under --spec` on the carries and
  packet lines.
  Red when: the stale-waiver arm or the stale high-water arm runs over the one-spec population, so
  the rows in `memory/project/spec-token-waivers.txt` print as STALE and the run exits 1.
- **AC3** — Add a second untracked fixture spec in the same build folder, status OPEN, whose H1
  carries the uid that the first fixture's `**hands-off**` bullet names, and which does not spell a
  backticked token that bullet promises. When `--spec` runs over the first fixture, it exits 1 with
  a `[handoff]` hit naming that token.
  Red when: the sibling map reads only tracked `LIVE` specs, so the bullet is counted silent and
  the run exits 0.
  fixture: the same clone; `SPEC_HANDOFF_CUTOFF` (2026-10-02) arms the join for this date.
- **AC4** — When `--spec` names `README.md`, and again when it names a path that does not exist,
  `python tools/check-spec-tokens.py` exits 2 each time and prints a `REFUSING` line naming the
  operand.
  Red when: the run grades the file, exits 0 or 1, or a missing operand raises a traceback.
- **AC5** — When `python tools/roles/render_agents.py --write` runs after the policy edit,
  `.claude/roles.json` lists `spec tokens (a spec's own names resolve)` in `gov-spec-writer`'s
  `gates`. A following `python tools/roles/render_agents.py --check` then exits 0.
  Red when: the policy line lacks the name, or its `?` is dropped and the render refuses with R12
  in a tree whose manifest lacks the leg.
- **AC6** — Pipe a Bash PreToolUse payload to `node tools/hooks/scratch-guard.js`, with the
  worktree as `cwd`, `agent_type` `gov-spec-writer` and the command
  `python tools/check-spec-tokens.py`. It prints no `a role agent runs no gate` line. The same
  payload with `agent_type` `gov-builder` exits 2 and prints that line. With `--spec <path>`
  appended, the `gov-spec-writer` payload exits 0.
  Red when: the rendered index lacks the leg, so the `gov-spec-writer` payload is refused as row
  G1, just like the builder's.
- **AC7** — When
  `grep -c "check-spec-tokens.py --spec" tools/roles/agents/gov-spec-writer.agent.md .claude/agents/gov-spec-writer.md`
  runs, it counts 1 in each file.
  Red when: line 36 still grants the two legs alone, or the render was not rerun and the rendered
  copy counts 0.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `roles catalogue` · `roles render wiring` · `roles render selftest`

The guarded legs above follow from §4's files: `tools/check-spec-tokens.py` trips
`memory-hygiene self-test`, `build-index selftest` and `policy fixtures`, and the two rendered files
under `.claude/` trip `check-wiring self-test` and `lexicon naming predicates`. Each was computed
against the manifest's guards with the broad guards excluded.

New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC2 AC3 AC4 · in the suite's scratch repo, a DEFERRED spec with a descending label list, an untracked OPEN sibling missing a hands-off token, a waiver row only another spec produces, and a non-spec operand, each graded under --spec, beside the bare run leaving the DEFERRED spec ungraded · FLOOR_ASSERTIONS rises by the arms added, counted at build

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "grade one named spec file whatever its
status"` returned 33 candidates. None of them selects this checker's population. The nearest are
the memory-tree kit's single-spec readers, `read_spec_revisions` and `parse_spec_h1`, which read one
spec's history or H1 and select nothing. No new seam is needed: the unit extends the checker's own
population walk (check-spec-tokens.py:1544-1558), its operand branch shape for `--legs-for`
(:1537-1538), and `read_spec_uids` (:806-820) for the sibling map. The grant extends the `[gates]`
table (policy.toml:25-28) through `load_policy`'s optional-name rule (roles_lib.py:494-509).

The recall probe returned the asks this unit closes: TOOL-dFairHearing-54, whose accept clause is
this unit's S1, S5 and S6, and TOOL-aDeferredBar-6, which wants the writer told to run the checker.
It also returned TOOL-dGatedProse-11, the full run's liveness, which §3 leaves open. Two writers'
returns, dFurnishedOrders' and dOrderedCharter's, record scratch-guard refusing them the bare leg.
That agrees with G1's whole-argv match (scratch-guard.js:1378), so nothing in the records
disagreed with the source.

Recall terms used: `python tools/memory-recall/query.py "may a spec writer role run the spec token checker over a deferred spec" --terms "spec-tokens check-spec-tokens deferred live population role gates allowlist gov-spec-writer policy scratch-guard writer self-check"`
