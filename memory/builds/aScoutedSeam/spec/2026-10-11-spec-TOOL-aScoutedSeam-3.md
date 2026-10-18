# TOOL-aScoutedSeam-3 — the scout's diff mode: a landed diff checked against the tree and the `## reuse` seams

**Status:** SPECCED · rev-5 · 2026-10-18 · node a · Tier-2 · base ebce889c · streams tooling · order 3 · ratified 2026-10-18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md) | research | TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1 |
| [2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md](../build/2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py](../build/2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-10-judge-task.md](../build/2026-10-18-build-TOOL-aScoutedSeam-1-10-judge-task.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md](../build/2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md](../build/2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json](../build/2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py](../build/2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-build-TOOL-aScoutedSeam-3-1-system-and-held-out.md](../build/2026-10-18-build-TOOL-aScoutedSeam-3-1-system-and-held-out.md) | research | — |
| [2026-10-18-build-TOOL-aScoutedSeam-3-2-workflow-design-set.md](../build/2026-10-18-build-TOOL-aScoutedSeam-3-2-workflow-design-set.md) | research | — |
| [2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md) | research | TOOL-aScoutedSeam-1 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1 |
| [2026-10-18-prompt-DEPL-aScoutedSeam-1-brief.md](../prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-brief.md) | research | DEPL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 |
| [2026-10-18-prompt-TOOL-aScoutedSeam-3-1-spec-writer.md](../prompts/2026-10-18-prompt-TOOL-aScoutedSeam-3-1-spec-writer.md) | journal | — |
| [2026-10-18-prompt-TOOL-aScoutedSeam-3-brief-2.md](../prompts/2026-10-18-prompt-TOOL-aScoutedSeam-3-brief-2.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-18-prompt-TOOL-aScoutedSeam-3-brief.md](../prompts/2026-10-18-prompt-TOOL-aScoutedSeam-3-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Catch the duplicate a pre-spec scout cannot see, because it is written inside a helper during the
build. Half of gov's twelve measured reinventions were of that kind. Reviewing the landed diff solved
three gov cases that every pre-spec arm answering them missed, and it emitted the fewest MUSTs of any
arm (`2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`, arm D1). The shipped design is the one
measured best since: a deterministic list of the units the diff adds, and one verdict row per unit,
at the scout type's own `medium` (`2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md`).

## 2. Scope (IN)

- **S1** — `reuse-scout.js` accepts `mode: "diff"` with `base` and `head`, two commits the
  caller resolved, `units`, the lister output of S8, and the optional `reuse` lines the card's
  `## reuse` section carries. Its other args follow `TOOL-aScoutedSeam-1`'s stage convention:
  `task` is the caller's `handoff.py render --role gov-reuse-scout --part task` output, `roles` is
  what `handoff.py harness-args reuse-scout` prints, and `efforts` is what `handoff.py stage-efforts
  reuse` prints. Each refusal names its field before any spawn:
  - a base or head that is not 7 to 40 hex characters;
  - a missing `roles.diffCheck`;
  - a `units` that is absent, not a string, or whose first line is not the lister's
    `# added-units ` header. An absent `units` is refused rather than read as an empty list,
    because an empty list switches the prompt to self-enumeration (S2).

  The orient stage keys, which `harness-args` prints beside `diffCheck`, are logged as not read.
  - AC1 observes it.
- **S2** — One spawn of the `gov-reuse-scout` role under the stage key `diffCheck`, its options built
  by `TOOL-aScoutedSeam-1`'s `renderStageOpts`, its label `<build> · <unit> · diffCheck`. Its prompt
  is the task, then a COVERAGE instruction, then the diff return contract: `DIFF_SCHEMA` and the
  binding definitions restated. The instruction is written to the recipe of
  `2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md`, and its worked examples are the T1
  handoffs, `prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-13` to `-35-reuse-scout.md`. It says:
  - the job is coverage of a supplied list: the agent reads `git diff --stat` for `base..head`, then
    the added hunks, and judges added code against the tree at `base` only;
  - the list is `units`, verbatim. When its header counts zero, the prompt carries in its place the
    sentence "the lister found no added unit; enumerate them yourself from the hunks";
  - for each listed unit, in order, the agent returns one row: the unit, the nearest existing
    `path::symbol` or `none` with what it searched, a verdict from `duplicate`, `should-extend`,
    `new` or `not-a-unit`, and a one-line why. A `duplicate` or `should-extend` row also carries how
    the diff should use the seam instead, and its evidence as `file:line`;
  - then rows marked `added`, for what the lister cannot see: repeated literals, hardcoded design
    values beside an existing token, renamed copied bodies and rebuilt JSON nodes;
  - the failure it guards against, in these words: "Do not stop at the first duplicate. A listed
    unit without a row is incomplete.";
  - for each MUST line in `reuse`, whether the diff wires through it: `used`, `bypassed`, or
    `not-applicable` with a reason. T1 ran against empty cards, so this half is unmeasured.

  The agent chooses no binding. The harness derives it from the verdict: a `duplicate` row becomes a
  MUST seam, a `should-extend` row a SHOULD seam, and the other verdicts no seam.
  - AC2 and AC3 observe it.
- **S3** — The return shape of §4, derived deterministically from the agent's rows:
  - the seams, in row order, capped by `TOOL-aScoutedSeam-1`'s MUST rule: the first five MUSTs stay
    MUST, and every later MUST is demoted to SHOULD and counted in `demoted`, never lost;
  - at most 10 seams in `duplicates`, MUST first; every row stays in `rows`;
  - `uncovered`, the listed units no row answers.

  The cap is applied by one function both modes call, never a second copy. The blind judge read 11
  of 130 T1 seams at `medium` as misleading, clustered in a few cases, which is what the cap bounds
  (`2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`).
  - AC2 observes it.
- **S4** — The search procedure is a `## The diff check` section of
  `tools/codebase-map/reuse-lookup.agent.md`, beside the scout checklist `TOOL-aScoutedSeam-1` writes
  there. It says how to find a listed unit's nearest implementation: search the concept with
  synonyms across all file types in the tree at `base`, never git history or another checkout. It
  also says what each of the four verdicts means. The row grammar, the verdict set and the no-stop
  sentence are S2's return contract, which the roles README keeps in the harness, while a procedure
  stays in the document that owns it (`tools/roles/README.md:25-28`). The base role's body is not
  edited: it already points at that document.
  - AC3 observes it.
- **S5** — Where it runs. `memory/guides/BUILD-METHOD.md` is rendered from the memory-tree kit's
  `BUILD-METHOD.template.md`. In a build whose card carries `## reuse`, the template gains one
  sentence in the pass loop: after a unit's build pass and before its closing review, the caller runs
  the lister and then diff mode over the unit's range. Each `bypassed` MUST and each MUST duplicate
  becomes a fold item exactly as a review finding does.
  - AC4 observes it.
- **S6** — Diff mode's level is the `gov-reuse-scout` type's own, `medium` in gov. Gov's
  `tools/roles/house/policy.toml` carries no `[effort.stages.reuse]` table. `handoff.py stage-efforts
  reuse` still prints a `diffCheck` entry, because `resolve_stage_efforts` falls back to the stage's
  slot level for a key no stage table names (`tools/roles/roles_lib.py:561-566`). Today the
  `closing-review` workflow, which has no stage table, prints `diffFinder` at `gov-diff-reviewer`'s
  `high` that way. The harness writes no default: an `efforts` that omits `diffCheck` runs at the
  agent type's level too. Why `medium`: §8 F2.
  - AC3 and AC5 observe it.
- **S7** — The roles kit edits, landed in ONE commit with the harness's diff mode:
  - the `reuse` row in `tools/roles/workflows.toml` gains `diffCheck = "gov-reuse-scout"` in its
    `stages`;
  - `check_roles.py --write` re-renders the README's catalogue region.

  Two facts still bind the one commit. R11 compares the catalogue region with a fresh render of
  `workflows.toml` (`tools/roles/check_roles.py:376-388`), so the row and the render share it.
  `harness-args reuse-scout` prints every stage key of the row into each orient call too
  (`tools/roles/handoff.py:453-471`), and the harness refuses a key outside its `STAGE_KEYS`
  (`TOOL-aScoutedSeam-1` §4, Data model). So the row lands with the harness change that adds
  `diffCheck` to `STAGE_KEYS`. R12 binds nothing here, since no policy line names the key.
  `.claude/roles.json` and the agent types do not move: the harness list is unchanged, and a stage
  level reaches no agent type. The roles and codebase-map kit versions each move once where the kit
  epoch leg owes it, since that leg grades from the push base and `TOOL-aScoutedSeam-1`'s bumps may
  already sit behind it.
  - AC5 observes it.
- **S8** — The unit lister: a new mode of the codebase-map kit's range reader,
  `map_diff.py --added-units <base>..<head>`. It runs `git diff --no-color --no-ext-diff
  --src-prefix=a/ --dst-prefix=b/` over the range at git's default three lines of context, the shape
  the measured diffs were built with (`2026-10-11-build-TOOL-aScoutedSeam-1-4-bench.py`, line 178).
  It prints the units the diff adds in product files. Its rules are those of the measured
  `extract_units` and `render_units` in `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py`, ported
  unchanged:
  - **Population:** it skips memory, docs, help, test and fixture paths, test files, markdown,
    lockfiles, snapshots and images. It lists definitions, constants, shell functions, schema fields
    and JSON tree keys, in diff order, once per path and name.
  - **CSS:** the CSS custom-property and rule patterns run only in `.css`, `.scss` and `.less` files.
  - **Hunks:** a hunk that adds 4 or more lines and names no unit becomes a `hunk` unit, named by its
    line range and first added line, so logic added inside an existing function is still listed.
  - **Output and cap:** a header line, `# added-units <base>..<head> · <n> found`, then one
    `U<i>. <name>  [<kind> · <path>]` line per unit up to 60, then
    `... and <m> more units past the cap of 60; cover them as you read the diff.` when there are more.
  - **Exit:** 0 with the header, even at zero units. A range git cannot read exits 1 naming it and
    prints no header, unlike the digest's soft fail (`tools/codebase-map/map_diff.py:67-78`), so an
    unread range never reaches the agent as an empty list. It is refused without a range and beside
    another mode flag, and it keeps the unadopted-root refusal at line 273.

  The caller runs it and passes its stdout as `units`, because a Workflow script cannot run git.
  `tools/codebase-map/README.md` documents the mode beside the digest's others.
  - AC6 observes it.

## 3. Non-goals (OUT)

- A reuse lens inside `tools/workflows/tier2-review.template.js`. Its finder lenses are prompt
  literals aOrientedCast's review-harness unit leaves in place, so wiring one in is that build's later
  change (Edges).
- A gate leg that refuses a merge on a `bypassed` MUST. A diff-time verdict is agent judgement, and
  the fold is where judgement is answered. The deterministic refusal is `TOOL-aScoutedSeam-2`'s spec
  join.
- Running diff mode on a build that never ran the orient mode. It still finds duplicates, but its
  wiring half has nothing to check, so the method text names it only where `## reuse` exists.
- The orient mode adopting the enumerated method. The method record names it as a candidate, and it
  is untested.
- Patterns beyond the measured ones. A unit the lister misses is the agent's to add as an `added`
  row.

### Edges

- **consumes-from** `TOOL-aScoutedSeam-1` — the harness, the role slot, `STAGE_KEYS` and the MUST
  cap it extends; without it there is no script to add a mode to.
- **consumes-from** `KICK-aScoutedSeam-1` — the card's `## reuse` section the wiring half reads.
- **hands-off** `DEPL-aScoutedSeam-1` — the adopter checklist's `diffCheck` policy line, which this
  revision makes unnecessary: diff mode runs at the scout type's level, so an adopter adds no
  stage override.
- **consumes-from** external — aOrientedCast's roles kit, LANDED on local main at ebce889c: the
  `stages` table, `handoff.py stage-efforts` and its fallback to a stage's slot level.
- **hands-off** external — wiring a reuse lens into the Tier-2 review harness, after aOrientedCast's
  review-harness unit lands; aOrientedCast confirmed on 2026-10-11 that its lenses stay literals.

## 4. Design

### Data model

The diff-mode args add four keys to `TOOL-aScoutedSeam-1`'s table, and its `roles` and `efforts`
rows gain the stage key `diffCheck`:

| key | type | rule |
|---|---|---|
| `base` | string | 7-40 hex, resolved by the caller, never a ref name |
| `head` | string | 7-40 hex, resolved by the caller |
| `units` | string | `map_diff.py --added-units` stdout verbatim; its first line opens `# added-units ` |
| `reuse` | string | the `## reuse` section verbatim, or empty |

The lister's output, shown for two invented units:

```text
# added-units 1a2b3c4d..5e6f7a8b · 2 found
U1. read_brief_items  [def · tools/example/brief.py]
U2. -40,6 +40,11: if row.get("quoted"):  [hunk · tools/example/brief.py]
```

The agent returns `rows` and `wiring`, the `DIFF_SCHEMA` part. The harness derives the rest:

```json
{ "rows": [{"unit": "U1 read_brief_items", "nearest": "<path>::<symbol>", "verdict": "duplicate",
            "why": "", "how": "", "evidence": "", "added": false}],
  "duplicates": [{"binding": "MUST", "path": "", "symbol": "", "unit": "", "how": "", "evidence": ""}],
  "wiring": [{"seam": "<path> :: <symbol>", "verdict": "used", "why": ""}],
  "uncovered": [], "demoted": 0, "verdict": "clean", "lensesLive": 1 }
```

`verdict` is `bypassed` when a wiring row reads `bypassed`, else `duplicates-found` when
`duplicates` holds a MUST, else `clean`. The strongest finding wins.

### Flow

1. The caller resolves `base` and `head` with `git rev-parse`, runs `map_diff.py --added-units` over
   the range, and passes its stdout as `units` with the card's `## reuse` text.
2. The script validates its args, logs one type line and one effort line for `diffCheck`, then
   spawns one agent with the COVERAGE prompt.
3. The script derives `duplicates` from the rows, applies the cap, and computes `uncovered` from the
   `U<i>.` lines of `units`, then the verdict.
4. The caller turns each MUST duplicate and each `bypassed` MUST into a fold item; a SHOULD is
   reported, not folded.

### Inventory

| identifier | cell |
|---|---|
| `renderDiffTask`, `checkDiffArgs`, `deriveDiffReturn`, `deriveCappedMusts` | js.function |
| `DIFF_SCHEMA` | js.constant |
| `extract_added_units`, `render_added_units` | py.function |
| `UNIT_PATTERNS`, `UNIT_SKIP_RE`, `STYLE_FILE_RE`, `UNIT_CAP`, `HUNK_MIN_ADDED` | py constant, no naming cell |
| `--added-units` | checker verb, no naming cell |

`deriveCappedMusts` is the MUST cap extracted from `TOOL-aScoutedSeam-1`'s `deriveMerged`, which then
calls it, because diff mode is the cap's second caller.

### Files touched (estimate)

- `tools/workflows/reuse-scout.js`
- `tools/workflows/reuse-scout.test.sh`
- `tools/workflows/README.md`
- `tools/codebase-map/map_diff.py` (the `--added-units` mode)
- `tools/codebase-map/selftest.py` (the AC6 fixture)
- `tools/codebase-map/README.md`
- `tools/codebase-map/reuse-lookup.agent.md`
- `tools/codebase-map/map_lib.py` (`KIT_CODEBASE_MAP_VERSION`, where the epoch owes it)
- `tools/roles/workflows.toml` (the `reuse` row's `stages` only)
- `tools/roles/README.md` (the generated catalogue region, and the version marker where owed)
- `tools/roles/roles_lib.py` (`KIT_ROLES_VERSION`, where the epoch owes it)
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`

### Rollout

Inert until a caller passes `mode: "diff"`. The lister is a new flag of an existing CLI and changes
none of its other modes. The method sentence binds only a build whose card carries `## reuse`, which
exists only after an owner opt-in.

### Alternatives rejected

The figures are the blind judge's primaries covered of 23 diff cases, PINNED from
`2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`; the shipped design covers 14.

- **The open prompt at `extra` (D1).** It covered 11, with 0 misleading seams of 52. It cost a median
  31 minutes per diff on 2026-10-11, where T1 ran from 19 s to 4 min 57 s.
- **The enumerated prompt at `low`.** It covered 8, with 19 misleading seams of 105, about 18%. It
  bound 44 MUSTs, the most of any arm, and had the lowest mean score. The list made `low` list more,
  not find more.
- **The open prompt at `high`.** Never run. The open prompt at `medium` covered 7 and the enumerated
  one 14 at the same level, so the composition carried the gain and no level above was needed.
- **Grading the diff with the lookup.** The lookup matches names, and a duplicate's name is new by
  definition.
- **A deterministic duplicate detector over symbols.** It finds same-named copies; the measured
  duplicates were renamed re-implementations (`_marker_index` against `unfenced_lines`). The lister
  only enumerates, and the agent judges.
- **The lister as a `gen_map.py` mode, beside the house index.** That CLI reads the tree, and the
  lister reads a range, which `map_diff.py` already parses.

## 5. Production-readiness checklist

- security: read-only. The lister runs one `git diff` and writes nothing; the agent reads files and
  writes nothing. `units` is checked for the lister's header before any spawn.
- perf / scale: PINNED from T1, 2026-10-18, one `medium` agent per diff: 19 s to 4 min 57 s wall time
  and 1.7k to 24.1k output tokens. The blind judge read 11 of its 130 seams as misleading, about 8%,
  against 0 of 52 for D1 at `extra`; S3's cap bounds what reaches the fold. The lister is one regex
  pass over the diff text.
- error / empty / loading states: a dead agent returns `lensesLive` 0 and no verdict, never `clean`.
  A lister that finds nothing prints a zero header, and the prompt asks the agent to enumerate. An
  unreadable range exits 1 with no header, which S1 refuses.
- observability: the verdict, the rows, `uncovered` and `demoted` are the caller's fold input, and
  they are recorded with it.
- risks: a false `bypassed` sends a fold after a seam that does not fit, and a misleading MUST does
  the same. The fold answers both, the way it answers any review finding, and the cap bounds the
  second. The lister cannot see a duplicated literal inside an expression, a renamed body or a JSON
  node with no `slug`, `part` or `name` key; the `added` rows are where the agent covers them.
- testing: the stub suite of `TOOL-aScoutedSeam-1` gains the diff-mode arms, and the codebase-map
  self-test gains the lister's fixture.
- migration: N/A — a new mode on a new harness, and a new flag on an existing CLI.
- user docs: `tools/workflows/README.md` documents the mode beside the orient mode, and
  `tools/codebase-map/README.md` the lister.

## 6. Acceptance criteria

- **AC1** — When `reuse-scout.js` is given `mode: "diff"` with `base: "main"`, with `roles` lacking
  `diffCheck`, or with `units` absent or opening without the `# added-units ` header, the stub suite
  records a refusal naming that field and no spawn.
  Red when: a ref name reaches the agent and the review grades a moving range, the diff stage spawns
  with no agent type, or a missing `units` is read as an empty list.
- **AC2** — When the stub diff agent answers a three-unit `units` with rows for `U1` and `U2`, one of
  them `duplicate`, and one `bypassed` wiring row, the return's `verdict` is `bypassed`, its one
  `duplicates` entry binds MUST, and `uncovered` names `U3`. When it returns seven `duplicate` rows,
  `duplicates` holds five MUST and two SHOULD, and `demoted` reads 2.
  Red when: the verdict takes the first finding instead of the strongest, a listed unit with no row
  goes unreported, or the cap drops a seam instead of demoting it.
- **AC3** — When the shipped harness runs diff mode at the `diffCheck` level `handoff.py
  stage-efforts reuse` prints, `medium` in gov, with `units` from `map_diff.py --added-units`, on the
  three below-spec gov cases of `2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json`, `bench.py grade`
  reads at least two of them solved, with each run's `duplicates` collected as its seams. The cases
  are the quoted-headings brief reader, the pooled-sweep wall watchdog and the keyed-decisions id
  regex. T1 solved all three at `medium`.
  Red when: the COVERAGE instruction loses its row-per-listed-unit demand or its no-stop sentence,
  and the agent stops at its first duplicate as D1 did at `medium`.
  cost: three agents at `medium`, measured at 19 s to 4 min 57 s per diff in T1.
  fixture: `bench.py d1` rebuilds the parent worktrees and the diffs. The three cases' commits
  resolve in this repository, so the lister runs here.
  figure: the solved count DERIVED by `bench.py grade`; the cost PINNED from T1, 2026-10-18.
- **AC4** — When the memory-tree kit re-renders the method, the rendered `BUILD-METHOD.md` carries
  the diff-mode sentence written in `BUILD-METHOD.template.md`, and the two compare byte-identical.
  Red when: the live copy is edited by hand, so the render and the template disagree.
- **AC5** — When `handoff.py stage-efforts reuse` runs after this unit's commit, it prints
  `diffCheck` at `medium` beside `codeLens` and `designLens`, while `tools/roles/house/policy.toml`
  holds no `[effort.stages.reuse]` table. `handoff.py harness-args reuse-scout` prints all three
  keys, and `check_roles.py` prints no defect.
  Red when: the `reuse` row lands without `diffCheck`, so `harness-args` omits it and every diff call
  is refused, or the catalogue region is not re-rendered and R11 reds.
- **AC6** — When `extract_added_units` in `tools/codebase-map/map_diff.py` reads the self-test's
  fixture diff, it lists one `hunk` unit for a hunk adding five lines inside an existing Python
  function, a `css-rule` unit for `.card {` added to a `.css` file, no unit for the same line added
  to a `.py` file, and nothing under `tests/`. Given 61 units, `render_added_units` prints 60 unit
  lines and a line counting 1 more. Over a range git cannot read, `map_diff.py --added-units` exits 1
  and prints no header.
  Red when: a hunk adding logic inside an existing function gets no unit, a CSS pattern fires outside
  a style file, or an unreadable range prints a zero-unit header.
  fixture: the diff text is staged inside the self-test; the tree holds none today.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `build-method size` · `memory hygiene` · `recall floor` · `recall floor arms` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `roles catalogue` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/workflows/reuse-scout.test.sh · covers AC1 AC2 · stub diff returns staged per arm · none
New arm: tools/codebase-map/selftest.py · covers AC6 · a fixture diff staged in the self-test · none

## 8. Open questions

- **F1 — Should diff mode run per unit or once over the build's range before the closing review?** Per
  unit catches a duplicate before the next unit copies it. Once per build halves the cost on a large
  build. Recommendation: per unit, because two measured duplicates were copied forward by a sibling
  unit. RESOLVED (owner, 2026-10-18): per unit, as recommended.
- **F2 — Is `high` enough for diff mode, or should it default to `extra`?** `medium` was measured
  and lost 3 of 7 solved cases, and `extra` cost 31 minutes per diff; `high` was not measured.
  Recommendation: `high`, with AC3 as the measurement. The owner then asked for a measurement and a
  hypothesis on why `medium` lost cases. The hypothesis was the prompt's single-answer shape, and the
  measurement held it. Judged blind on the 23 diff cases:
  - the enumerated prompt at `medium` covers 14 primaries, with 11 misleading seams of 130;
  - the open prompt at `extra` covers 11, and at `medium` 7;
  - the enumerated prompt at `low` covers 8, with 19 misleading of 105.

  `high` with the open prompt was never run, and is no longer needed, because the composition
  carried the gain. Records: `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md`,
  `2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md` and
  `2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`.
  RESOLVED (owner, 2026-10-18): medium, with the enumerated-coverage prompt.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S6 · §4 · §5 · §8 · AC3 · the effort comparison measured the diff reviewer at
  `medium` solving 4 of 23 where `extra` solved 7. This mode therefore defaults to `high`, and F2
  asks whether `high` is enough.
- rev-3 · 2026-10-13 · S1 · S2 · S4 · S6 · S7 · §3 · §4 · §7 · §8 · §10 · AC1 · AC3 · AC5 · re-specced on the
  landed roles kit, following `TOOL-aScoutedSeam-1` rev-6. Diff mode is the third stage key of the
  `reuse` row, `diffCheck`, with args per that unit's stage convention; `roles.scout` and the
  `effort` arg go. Its `high` is a stage override in gov's policy, not a harness default, and S7
  lands the row and policy edits together. The diff procedure moves from the role body to
  `reuse-lookup.agent.md`. AC1 refuses a missing `diffCheck`, AC3 runs at the policy's level, and
  AC5 is new. F2 names its fallback as a policy level.
- rev-4 · 2026-10-18 · §4 · §8 · F1 closed as recommended, and F2 marked a measurement owed, with
  the effort unchanged. `TOOL-aScoutedSeam-1` rev-8 ships the harness as an engine file, so §4's
  files drop its template.
- rev-5 · 2026-10-18 · §1 · §2 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · §3 · §4 · §5 · §7 · §8 · §10 ·
  AC1 · AC2 · AC3 · AC5 · AC6 · F2 closed on T1 and the blind judge: `medium`, with the
  enumerated-coverage prompt. S2's prompt becomes a coverage job over a supplied unit list, one row
  per unit. S8 is the new lister, `map_diff.py --added-units`, and S1 takes and refuses its `units`
  arg. S3 adopts the cap of five MUSTs with demotion and adds `uncovered`. S4 holds the search
  procedure only. S6 and S7 carry no policy table, and S7's one commit is re-justified on R11 and
  `STAGE_KEYS`. AC1 and AC2 grow, AC3 runs at `medium`, AC5 needs no override, and AC6 is new. §4
  gains the args, the return, the inventory, the files and three rejected arms; §5 takes the T1 cost
  and precision; §7 a second arm; the DEPL edge now hands off a line to withdraw.

## 10. Reuse audit

The seam this unit extends is `TOOL-aScoutedSeam-1`'s harness and role, whose MUST cap it shares
through one extracted function. Its level is the roles kit's slot fallback, read by
`tools/roles/roles_lib.py`'s `resolve_stage_efforts` (lines 561-566) and printed by
`tools/roles/handoff.py`'s `print_stage_efforts` (line 474). Its review-shaped return copies the
finding shape of `tools/workflows/tier2-review.template.js`, so a fold reads it the way it reads a
review. The lister extends `tools/codebase-map/map_diff.py`, the kit's range reader, reusing its range
parsing (lines 259-266) and its adopted-root refusal (line 273); its rules are the measured
instrument's `extract_units`. `tools/codebase-map/reuse_lookup.py "list the definitions and constants
a git diff adds, from the added hunk lines of a range"` ranked `git`, `run_git` and `read_git_range`
by name stem, and none lists a diff's added units. The hunk walkers in
`tools/drift-audit/drift_report.py` (line 809), `tools/memory-tree/migrate_backlog.py` (line 2366)
and `tools/memory-tree/row_grammar.py` (line 1401) count or watch lines for other kits, and a
copy-installed kit carries nothing from another. `tools/memory-recall/query.py "parse unified diff
added lines hunks into units"` returned this build's own T1 records and briefs, and no landed lister.
So no existing seam fits beyond the three named.

Recall terms used: unified diff hunk added lines parse range base head lister units definitions map_diff
