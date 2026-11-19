# TOOL-dTrackedAtlas-4 — the Atlas page regenerates on node d after main moves, behind a switch whose default is on

**Status:** CLOSED · rev-7 · 2026-11-19 · node d · Tier-2 · base 9e21ac76 · streams tooling · ratified 2026-11-19 · order 4 · closes TOOL-dTrackedAtlas-7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-1-runlog-27295082.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-1-runlog-27295082.md) | journal | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 TOOL-dTrackedAtlas-12 TOOL-dTrackedAtlas-18 |
| [2026-11-19-build-TOOL-dTrackedAtlas-4-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-4-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js](../build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js) | research | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json](../build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-3-name-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-3-name-fold.md) | research | TOOL-dTrackedAtlas-3 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-3-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-4-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-4-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-ac6-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-ac6-fold.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-f3-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-f3-fold.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-map-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-map-fold.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-pin-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-pin-fold.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-spec-brief.md) | research | — |
| [2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

After a landing moves `main` on node d, the page at
`C:/projects/coding-governance-atlas/closed-loop-atlas.html` is regenerated from the landed tree with
no command typed for it, so the page the owner opens states the tree as it now is. The behaviour is
a switch, `atlas.regenerate`, whose default is `on` and whose other value is `off`, and on a node
without the page's folder it does nothing and says so.

## 2. Scope (IN)

- **S1** — A harness hook, `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js`,
  run after every Bash and PowerShell tool call. Its fast path reads one small file and stats two
  paths, starts no process unless its throttle window has passed, and then starts its own runner
  detached and returns. Observed by AC1, AC2 and AC5.
- **S2** — The runner, the same file run as `--run`: under a lock, it reads the tip of
  `refs/remotes/origin/main`, asks `TOOL-dTrackedAtlas-3`'s page check whether the page is current
  at that tip, and when it is not, regenerates the page in a scratch checkout of the tip, checks the
  result, and moves it over the page. Observed by AC2, AC3, AC6 and AC7.
- **S3** — The switch's interim home, `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json`,
  holding `atlas.regenerate` and `atlas.page`, as §8 F2 resolved. Observed by AC4.
- **S4** — The wiring: one `PostToolUse` group in `.claude/settings.json` running the hook. Observed
  by AC8.
- **S5** — One log line per tip the runner handles, saying what it did or why it skipped, and one
  stdout line when the page's folder is absent. Observed by AC2, AC3, AC4, AC5 and AC6.
- **S6** — It never commits, pushes or fetches, and writes only inside the page's folder, the scratch
  checkout's git admin entry excepted, which it removes. Observed by AC9.
- **S7** — The codebase map's claim of S4's hook: a new dossier,
  `memory/map/features/closed-loop-atlas.md`, and the map's artifacts regenerated, as §4 "The
  codebase map's claim" gives. Observed by AC10.
- **S8** — The loop table's stage claim of S4's hook: one `[[hook]]` row in `tools/loop/loop.toml`,
  as §4 "The loop table's stage claim" gives and §8 F3 resolved. Observed by AC10.

## 3. Non-goals (OUT)

- Generating, stamping or checking the page: the generator and its `--out` are
  `TOOL-dTrackedAtlas-2`'s, the stamp and `--check --page` are `TOOL-dTrackedAtlas-3`'s, and this unit
  only runs them.
- A row in `tools/policy/catalogue.toml` and a key in `.governance/policy.toml`: both are under, or
  read by, `tools/`, which this build touches only for §8 F3's row. The move is an ask the main loop
  files at the close (§3 "Edges").
- A git hook, an edit to `tools/push-main.sh`, an OS scheduled task, or a harness cron job: §8 F1.
- Fetching from the remote. A landing made on another node reaches this page when something on node
  d next moves `refs/remotes/origin/main`.
- Regenerating when run claims move without the tree moving: claims are not page inputs
  (`TOOL-dTrackedAtlas-3` §4 "What it does not check").
- Publishing or committing the page, and any page other than the one `atlas.page` names.
- A `help/` page: no kit ships this hook, and the policy move the ask names brings the
  `help/policy.md` row with it.
- A new gate, suite arm or self-test: the hook is a build-folder instrument, checked by its fixture
  observations. Its wiring is still graded by existing legs, which §4 "The wiring" names.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-2` — the generator's `--out <page>` with its defaults,
  `--ref HEAD` and `--claims cache`; without it there is nothing to run.
- **consumes-from** `TOOL-dTrackedAtlas-3` — `--check --page <page> --ref <rev>`, its exit table
  and its `atlas: current` line; without it every tip move regenerates, and a checkout whose
  generator predates that unit answers `--check` with its old summary line, which §4 "The runner"
  refuses to read as current.
- **hands-off** external — one ask, filed by the main loop at the close: move `atlas.regenerate`
  into the policy kit's catalogue with the row §4 "The switch" gives, read it from
  `.governance/policy.toml`, retire the interim JSON, and add the `help/policy.md` row.

## 4. Design

### The hook's fast path

The harness pipes the tool call's JSON to the hook on stdin. The file runs as the hook when started
with no argument. Every path through it exits 0, as `tools/process-monitor/procmon-hook.js#main`
does, so a fault never blocks a tool call.

1. Read stdin as JSON; a parse failure reads as `{}`.
2. Read the conf beside the script, `path.join(__dirname, CONF_NAME)`. An absent or unparseable conf,
   or an `atlas.page` that is not an absolute path ending in `.html` with no `..` segment, exits
   silently: a checkout with no usable conf has nothing configured.
3. When the page's folder does not exist, print one stdout line
   `atlas-regen: nothing done — no page home at <folder> on this node`, but only when the call's
   `tool_input.command` contains `push-main.sh`, and exit. Elsewhere this path is silent, so a node
   without the folder sees one line per lander call and none on any other tool call. The field is
   read as `tools/unattended/gate-guard.js@1252442ee677b5c5b4ba08a414b6a7f7c511c77a:947` reads it.
4. When the stamp sidecar's modification time is less than `THROTTLE_S` seconds old, exit.
5. Write the stamp, then start `process.execPath <this file> --run` with `detached: true`,
   `stdio: "ignore"` and `windowsHide: true`, `unref()` it and exit.

The stamp is written before the start, not after the work, so a runner that crashes is retried once
per window and never once per tool call. The fast path neither reads `.git` nor spawns git: it
learns that `main` moved only through the runner, so the window bounds how often a runner starts.

Measured on node d on 2026-11-19 (PINNED): a node script doing steps 1, 2 and 4 over a piped input
took 56 to 68 ms across six runs, wall time including the pipe. A detached node child started this
way outlived both its parent and the Bash tool call that started it.

### The runner

`--run` derives the repository root as `path.resolve(__dirname, "../../../..")` and the sidecars from
the page path, and does the following. It drops `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`,
`GIT_COMMON_DIR`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_NAMESPACE` and
`GIT_PREFIX` from its environment first, the family `tools/run-gates/post-merge.sh` drops before its
first git call.

1. Read the conf as the fast path does. With no page folder, print the fast path's line and exit 0.
2. Take the lock: create the lock sidecar exclusively, holding the pid and the UTC time. When it
   exists and is younger than `RUN_BOUND_S`, exit 0 silently, because another runner holds it. When
   it is older, remove it, log `stale lock removed`, and take it.
3. Remove any `regen-<digits>` folder left in the page's folder by a killed runner, with
   `git worktree remove --force`, then a recursive delete of what remains, then `git worktree prune`.
4. Repeat at most `ROUNDS` times:
   1. `tip` is `git rev-parse --verify -q refs/remotes/origin/main^{commit}`. A failure handles the
      key `unresolved` instead of a tip, logging `failed — refs/remotes/origin/main does not resolve`.
   2. When the tip sidecar already holds that key, stop.
   3. When `atlas.regenerate` is `off`, log `skipped — atlas.regenerate is off`. When it is any value
      outside `on` and `off`, log `skipped — atlas.regenerate is '<value>', outside on off`. A
      missing key reads as the default, `on`.
   4. Otherwise run the page check, `<python> <root>/<GENERATOR> --check --page <page> --ref <tip>`,
      in `root`. Exit 0 with a first stdout line starting `atlas: current` logs
      `current — <that line>`. Any other answer regenerates, and the log names the check's first line.
   5. Write the key to the tip sidecar, whatever the outcome.
5. Release the lock and exit 0, or 1 when a regeneration in this run failed.

To regenerate at `tip`:

1. `git worktree add --detach <folder>/regen-<pid> <tip>`.
2. In it, `<python> <GENERATOR> --out <temp page>`, then
   `<python> <GENERATOR> --check --page <temp page> --ref <tip>`, which must exit 0 with
   `atlas: current`.
3. Rename the temp page over the page and log `regenerated in <s> s, <KB> KB`.
4. On any failure, log `failed — <the step> — <its first stderr line>`, delete the temp page and leave
   the page as it was.
5. In every case, remove the scratch checkout with `git worktree remove --force`.

The generation runs in a scratch checkout because the generator reads dClosedLoop's records from its
own checkout's working tree (`TOOL-dTrackedAtlas-2` §4 "Where the actual state enters") and stamps
`HEAD` with the working tree's differences (`TOOL-dTrackedAtlas-3` §4 "The stamp"). The session's
own checkout is at neither the tip nor clean, in general. Measured on node d on 2026-11-19 over a
local clone of this repository (PINNED): `git worktree add --detach` took 10.8 s for 13751 files and
its removal 2.6 s.

`<python>` is resolved once per run by `bash -c '. tools/lib/resolve-python.sh && resolve_python'`
in `root`, the resolver every instrument of this repo uses. An empty answer logs
`failed — no python resolved` and handles the tip.

A log line is `<UTC ISO time> <tip, first 12 hex, or unresolved> <outcome> — <why>`, appended to the
log sidecar. Outcomes are `regenerated`, `current`, `skipped` and `failed`. The tip sidecar records
the tip the runner last handled, whatever it did. It is not the page's generation commit: a page
current at a newer tip keeps its older stamp. Deleting the tip sidecar makes the next runner handle
the present tip again.

After writing the page, the runner re-reads the tip, so a landing made during a regeneration is
handled in the same run, up to `ROUNDS` times.

### Bounds

| Bound | Value | On expiry |
|---|---|---|
| the fast path | none set; 56 to 68 ms measured | the harness `timeout` of `10 s` kills it |
| each git call | `GIT_BOUND_S`, `300 s` | the step fails and is logged |
| the page check | `CHECK_BOUND_S`, `300 s` | read as not current, so the page regenerates |
| the generation | `GEN_BOUND_S`, `1500 s` | the step fails and is logged |
| the whole runner | `RUN_BOUND_S`, `2400 s`, armed as a timer | kills its child, logs `failed — no answer within 2400 s`, releases the lock, exits 1 |

The landing itself is never slowed: the hook fires after the lander's tool call has returned, and
the runner holds no lock the lander takes. A runner can compete for CPU with a bar running at the
same time; nothing here lowers its priority.

### The page's folder

For a page `<folder>/<stem>.html`, every file this unit writes is in `<folder>`:

| Sidecar | Path | Writer |
|---|---|---|
| stamp | `<folder>/<stem>.regen.stamp` | the fast path, at each runner start |
| lock | `<folder>/<stem>.regen.lock` | the runner, for its lifetime |
| tip | `<folder>/<stem>.regen.tip` | the runner, once per handled tip |
| log | `<folder>/<stem>.regen.log` | the runner, appended |
| temp page | `<folder>/<stem>.regen-<pid>.html` | the generator, renamed or deleted |
| scratch checkout | `<folder>/regen-<pid>/` | `git worktree add`, removed |

The folder is never created. The one write outside it is git's admin entry for the scratch checkout
under the common dir's `worktrees/`, which `git worktree remove` deletes.

### The switch

The conf, read from the checkout the hook runs in, as its working copy:

```json
{
  "atlas.regenerate": "on",
  "atlas.page": "C:/projects/coding-governance-atlas/closed-loop-atlas.html"
}
```

The policy row the hand-off ask carries, in `tools/policy/catalogue.toml`'s shape:

```toml
[[key]]
name = "atlas.regenerate"
allowed = ["on", "off"]
default = "on"
summary = "Whether node d regenerates the Closed Loop Atlas page after main moves: on, or off, the page then left as it is."
usage = 'atlas.regenerate = "off"'
owner = "dTrackedAtlas"
```

Switching off is an edit of the conf. An uncommitted edit turns it off for that checkout alone,
and a landed one for every checkout carrying it.

### The wiring

One group appended to the `PostToolUse` array of `.claude/settings.json`, beside the existing groups:

```json
{
  "matcher": "Bash|PowerShell",
  "hooks": [
    {
      "type": "command",
      "command": "node \"${CLAUDE_PROJECT_DIR}/memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js\"",
      "timeout": 10
    }
  ]
}
```

It is a group of its own, so a kit adopter rewriting the process monitor's group leaves it alone.
`tools/check-hook-destinations.sh` reads only tracked fragment files and adopter scripts
(`tools/check-hook-destinations.sh@bee72010fa7854f384fa85b3b55110c05cea53d2:224`), and the policy
check reads only the file's `env` block, so neither grades this group. Two other readers do. The
codebase map's `harness-hooks` inventory keys every command hook the file wires as its event and
script, here `PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js`
(`tools/codebase-map/map_extractors.py@302cdbd33b5b3fbc8996b44bc4765227e499f7f4:171`), and §4 "The
codebase map's claim" gives that key its owner. The loop kit's stage coverage joins the same key to
a `[[hook]]` row of `tools/loop/loop.toml`
(`tools/loop/stage_coverage.py@5a7404bf4a92b10b7a72568cd048c9b60f76c912:91`), and §4 "The loop
table's stage claim" gives that row, as the owner resolved §8 F3. A session reads its hooks at start,
so the group takes effect in sessions started after the checkout carries it.

### The codebase map's claim

The builder writes a new dossier, `memory/map/features/closed-loop-atlas.md`, whose fence is the
block below, copied whole, and then runs `python tools/codebase-map/gen_map.py --write`.
`memory/map/baseline.toml` is not touched: it is reserved for the initial backfill, and
`tools/codebase-map/test_codebase_map.py#test_baseline_never_gains_a_key` refuses a key it gains.

```toml
feature = "closed-loop-atlas"
title = "The chain build state the schedule and the Closed Loop Atlas share, the page's stamp and stale check, and its regeneration on node d after main moves"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dTrackedAtlas-1", "TOOL-dTrackedAtlas-2", "TOOL-dTrackedAtlas-3",
  "TOOL-dTrackedAtlas-4"]

stage = ["step.plan", "step.deploy"]

[claims]
gate-legs = []
kits = []
git-hooks = []
harness-hooks = ["PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js"]
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py",
  "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js",
  "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py",
  "memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py",
]
```

- The claim kinds are the map's inventory ids, every one present, as
  `tools/codebase-map/map_lib.py#parse_dossier` requires; only `harness-hooks` holds a key.
- `stage` is the loop kit's step claim, which `tools/loop/stage_coverage.py#read_stage_parts` reads
  from the fence; a dossier with none reds the `loop stage coverage` leg as
  `unclaimed dossier closed-loop-atlas`. It names `step.plan` because the schedule and the Atlas
  answer what can start next, and `step.deploy` because the page regenerates after a landing.
- `status` is `shipped`: the dossier lands in the commit carrying unit 4, the build's last unit.
- The globs name this build's code: unit 1's derivation, unit 4's hook and conf, and the two
  dClosedLoop instruments units 1 to 3 edited. The pages and ledgers are records and stay out. Each
  path read `UNMAPPED` through `tools/codebase-map/map_lib.py#attribute_paths` against every dossier
  and `memory/map/FOUNDATION.md` on 2026-11-19 (PINNED), so no glob overlaps another dossier's.
- Probed on 2026-11-19 (PINNED): `tools/codebase-map/map_lib.py#parse_dossier` parses the fence;
  its title is 149 bytes (PINNED), under `tools/codebase-map/map_lib.py#_CARD_TITLE_BYTES`; and
  `tools/codebase-map/map_lib.py#render_cards_md` renders its card in 925 bytes (PINNED),
  under `tools/codebase-map/map_lib.py#FEATURE_CARD_CAP_BYTES`, so nothing is cut.
- The prose carries the headings `## Constraints & why`, `## Shared seams` and `## Gaps`, which
  `tools/codebase-map/test_codebase_map.py#test_dossier_prose_headings_pinned` grades, and
  `## Reuse affordance`, from which a new dossier is never exempt. Its one `seam:` line names unit
  1's `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive`,
  reused for any reader of chain build state and extended via a new field of its result. No digit
  run stands before an inventory noun in the prose, which
  `tools/codebase-map/test_codebase_map.py#test_dossier_prose_carries_no_typed_count` refuses.

`--write` renders the four artifacts of `tools/codebase-map/gen_map.py#_artifacts`. Three change:
`memory/map/generated/inventories.json` gains the key, `memory/map/generated/MAP.md` lists it beside
its owner, and `memory/map/generated/CARDS.md` gains the dossier's card.
`memory/map/generated/symbols.json` is rewritten with the same bytes, because its extractors read
only `tools/`, `.githooks/` and `skills/` (`tools/codebase-map/map_extractors.py#SHELL_ROOTS`,
`tools/codebase-map/map_extractors.py#_live_py`,
`tools/codebase-map/map_extractors.py#_build_js_layer`).

### The loop table's stage claim

The builder inserts one row into `tools/loop/loop.toml`, in the shape of the other `[[hook]]` rows
(`tools/loop/loop.toml@b6651f2140d4e9dced399959f6475c2ab4bff0e7:1141`), a blank line on each side:

```toml
[[hook]]
key = "PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js"
stage = ["step.deploy"]
```

- `key` is the `harness-hooks` key of §4 "The wiring", spelled whole. The script is not under the
  tool root, so it carries no `{prefix}/`, as the row keyed
  `SessionStart skills/session-kickoff/manifest-check.sh` carries none
  (`tools/loop/loop.toml@b6651f2140d4e9dced399959f6475c2ab4bff0e7:1182`).
  `tools/loop/stage_coverage.py#derive_part_claims` expands only a `{prefix}/` and joins every
  other key as written.
- `stage` is the owner's pick: the hook acts only after a landing.
- The row goes after the `pre-rebase` row and before the
  `PostToolUse {prefix}/memory-recall/recall-opened.js` row
  (`tools/loop/loop.toml@b6651f2140d4e9dced399959f6475c2ab4bff0e7:1157`). The harness rows run in
  byte order of their keys, and `m` sorts before `{`, as the two `SessionStart` rows already show.
- The comment above the rows says a harness hook on an event every session raises serves all five
  steps (`tools/loop/loop.toml@b6651f2140d4e9dced399959f6475c2ab4bff0e7:1137`). This row is the
  first exception, so the builder appends one line to that comment, directly below its third line,
  keeping it true of the rows it heads. The line is the fenced one below, no wider than that
  comment's second line, and nothing else in the file changes.

```toml
# The Atlas regeneration's row (TOOL-dTrackedAtlas-4) claims step.deploy alone: it acts after a landing.
```

- An adopter's copy of the table carries the row and never reads it. The `loop stage coverage` leg
  is gov's own `[[exempt_leg]]`
  (`tools/govkit/registry.toml@aec2b8e3d547a329461575c1ba97f0107908cea4:931`), whose reason says an
  adopter's copy would read hooks its tree does not hold as stale. The `skills/` row stands the same
  way.
- The row moves the loop kit's shipped bytes, so the kit's version owes a move. The lander mints it
  at the landing, `tools/govkit/govkit.py#cmd_mint`, and a branch owes none
  (`tools/govkit/govkit.py#cmd_epoch`), so neither `tools/loop/loop_lib.py` nor
  `tools/loop/README.md` is in Files touched.

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `CONF_NAME` | constant | `"2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json"` |
| `SWITCH` | constant | `"atlas.regenerate"` |
| `ALLOWED` | constant | `["on", "off"]` |
| `DEFAULT` | constant | `"on"` |
| `TIP_REF` | constant | `"refs/remotes/origin/main"` |
| `GENERATOR` | constant | `"memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py"` |
| `THROTTLE_S` | constant | `60` |
| `GIT_BOUND_S`, `CHECK_BOUND_S`, `GEN_BOUND_S`, `RUN_BOUND_S` | constants | `300`, `300`, `1500`, `2400` |
| `ROUNDS` | constant | `3` |
| `readConf()` | function | `{regenerate, page}`, or `null` for no usable conf |
| `deriveSidecars(page)` | function | the six paths of §4 "The page's folder", the pid's two included |
| `runHook(input)` | function | the fast path; returns 0 |
| `runRunner()` | function | the runner; returns 0, or 1 after a failed regeneration |
| `runRegeneration(root, tip, py, paths)` | function | the regeneration steps; returns the log line's outcome and reason |

### What it does not check

- That the remote-tracking ref is the remote's tip: the runner trusts this clone's ref and never
  fetches.
- A landing made at a console with no Claude Code session running on node d, until the next tool
  call of any session on the node.
- That a detached child survives a harness that kills its hooks' process tree. The probe above ran
  under this harness's Bash tool, not under its hook runner.
- Code under `tools/` that the generator reuses: `TOOL-dTrackedAtlas-3`'s digest does not cover it,
  so a tip moving only `tools/` reads current.
- A page edited by hand after a regeneration.

### Files touched (estimate)

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json`
`.claude/settings.json`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-ledger.md`
`memory/map/features/closed-loop-atlas.md`
`memory/map/generated/inventories.json`
`memory/map/generated/MAP.md`
`memory/map/generated/CARDS.md`
`tools/loop/loop.toml`

### Alternatives rejected

- The trigger mechanisms weighed are §8 F1, and the switch's homes §8 F2.
- Generating in the session's own checkout: neither at the tip nor clean, as §4 "The runner" says.
- A stamp written after the runner's work, as the process monitor writes its own: a runner that
  crashed before writing it would be restarted on every tool call.
- Regenerating on every tip move without the page check: `TOOL-dTrackedAtlas-3` §7 F1 measured 70
  of 92 first-parent commits touching no page input, each a full regeneration for nothing.

## 5. Production-readiness checklist

- security — The runner runs the generator from `refs/remotes/origin/main`, code the merge bar of
  the node that landed it graded, with no network and no secret. The page path is validated at the
  conf read, its folder is never created, and the only folder deleted is a `regen-<digits>` one
  inside it. An unknown switch value skips: deny by default.
- perf / scale — 56 to 68 ms added to each Bash or PowerShell tool call (PINNED, §4); at most one
  runner start per `60 s`; a regeneration costs a checkout of about 13 s (DERIVED, §4's measured
  add and removal) plus one generation.
- error / empty / loading states — No conf, no folder, a held lock, an unresolved tip, a failing
  check, generation or rename: each is a named exit or log line, and the page stays as it was.
- observability — The log sidecar, one line per handled tip; the stdout line for a missing folder.
- risks — A wedged generation is killed at `2400 s`. A browser holding the page open can refuse the
  rename on Windows, which logs `failed` and keeps the old page.
- testing — The fixture observations of §6, on a scratch clone.
- migration — N/A — a new file pair, a new dossier, the map's regenerated artifacts, one appended
  settings group and one inserted loop table row; nothing existing changes shape.
- user docs — The hook file's header states the switch, the sidecars and how to switch off; the
  `help/policy.md` row arrives with the catalogue move.

## 6. Acceptance criteria

The commands run on node d after units 1 to 3 are built, from a worktree root `$W` carrying this
unit, with these names set. `$C` is a scratch clone of `$W`'s tip, whose `origin` is a bare clone
holding that tip as `main`, so a plain `git push` lands with no hook. The real page is never
written.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
T=$(cygpath -u "$LOCALAPPDATA")/Temp; C=$T/ta4fx; H=$T/ta4h; P=$H/closed-loop-atlas.html
REGEN=memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js
CONF=memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
git clone -q "$W" "$C" && git clone -q --bare "$W" "$T/ta4o" && mkdir "$H"
git -C "$C" remote set-url origin "$T/ta4o" && git -C "$C" push -q -f origin HEAD:main
# then $CONF in $C is edited in its working copy so that atlas.page reads $P
```

A landing below is a commit in `$C` followed by `git -C "$C" push -q origin HEAD:main`. Running the
runner means `node "$C/$REGEN" --run`. A first run writes the page at the clone's tip `T0`.

- **AC1** — When the stamp `$H/closed-loop-atlas.regen.stamp` is younger than `60 s` and
  `echo '{"tool_input":{"command":"ls"}}' | node "$C/$REGEN"` runs, it exits 0 within `1 s`, prints
  nothing, and the stamp's modification time, read with `stat -c %Y`, is unchanged.
  Red when: the stamp is older than `60 s`, where the same call moves its modification time and a
  runner starts.
- **AC2** — When a landing `T1` appends a line to `memory/builds/dWitnessedBar/RUN.md`, the stamp is
  deleted, and `echo '{"tool_input":{"command":"bash tools/push-main.sh --land --slug x"}}' | node "$C/$REGEN"`
  runs, it exits 0 within `2 s`; then, once `$H/closed-loop-atlas.regen.log` gains a line naming
  `T1`'s first 12 hex and `regenerated`, `"$PY" "$ATLAS" --check --page "$P" --ref origin/main` run
  in `$C` exits 0 with `atlas: current`, and the page's `stamp.commit` equals
  `git -C "$C" rev-parse origin/main`.
  Red when: the same check, run after the push and before the hook, exits 1 with `atlas: stale`.
  cost: one scratch checkout and one generation, minutes rather than seconds.
- **AC3** — When a landing `T2` changes only `memory/builds/dTrackedAtlas/README.md`, a path outside
  the page's inputs, and the runner runs, it exits 0, the log's last line names `T2` and `current`,
  and `cmp` finds the page byte-identical to a copy taken before.
  Red when: the page check is skipped, where the same run regenerates and the page's `stamp.commit`
  moves to `T2`.
- **AC4** — When `$CONF` in `$C` sets `atlas.regenerate` to `off`, a landing `T3` appends a line to
  `memory/builds/dWitnessedBar/RUN.md`, and the runner runs, it exits 0, the log's last line names `T3`
  and `skipped — atlas.regenerate is off`, the page is byte-identical, and
  `--check --page "$P" --ref origin/main` exits 1 with `atlas: stale`; with the value `maybe` after a
  landing `T4`, the line names `'maybe'`.
  Red when: the switch is set back to `on` after a landing `T5`, where the same run logs
  `regenerated`.
- **AC5** — When `$CONF` in `$C` points `atlas.page` at `$T/ta4none/closed-loop-atlas.html`, an absent
  folder, the hook given AC2's input prints one line beginning `atlas-regen: nothing done — no page home`
  and exits 0, the hook given AC1's input prints nothing, `node "$C/$REGEN" --run` prints the same
  line and exits 0, and `$T/ta4none` still does not exist.
  Red when: the folder check is removed, where the runner's lock write fails on the absent folder
  and no such line prints.
- **AC6** — When a landing inserts the line `raise SystemExit(3)` into `$ATLAS` directly above its
  one `if __name__ == "__main__":` line, with
  `sed -i '/^if __name__ == "__main__":$/i raise SystemExit(3)' "$C/$ATLAS"` before the commit, and
  the runner runs, it exits 1, the log's last line names `failed`, the page is byte-identical to
  before, and no `$H/regen-*` folder and no `$H/*.regen-*.html` file remain. The planted line runs
  after the module's top-level code and before `main` is called, so every run of that tree's
  generator exits 3 with nothing on stdout: `"$PY" "$C/$ATLAS" --check --page "$P" --ref origin/main`
  run in `$C` after the landing shows it. The runner's page check runs `$C`'s working copy, which
  carries the line, so its answer is exit 3 with no `atlas: current` line, which §4 "The runner"
  reads as not current, and the runner regenerates. The generation in the scratch checkout of the tip
  carries the same line, so its `--out` step exits 3 before writing the temp page, and the runner
  logs `failed` and leaves the page as it was.
  Red when: the scratch checkout's removal is skipped, where `$H/regen-<pid>` remains and
  `git -C "$C" worktree list` lists it.
- **AC7** — When `$H/closed-loop-atlas.regen.lock` is written fresh by hand before a landing and the
  runner runs, it exits 0 within `2 s` and the log gains no line; with the lock's modification time set
  older than `2400 s` by `touch -d`, the run logs `stale lock removed` and handles the tip.
  Red when: the lock is ignored, where the first run handles the tip.
- **AC8** — When a `node -e` one-liner parses `.claude/settings.json` in `$W`, it finds exactly one
  `PostToolUse` group with matcher `Bash|PowerShell` whose command names `$REGEN`, with a `timeout`
  of 10, and `$W/$REGEN` exists.
  Red when: the same one-liner run at the run's base finds no such group.
- **AC9** — When AC2 to AC7 have run, `git -C "$C" status --porcelain` lists only `$CONF`,
  `git -C "$C" worktree list` lists one checkout, `git -C "$C" log origin/main` holds only the
  fixture's landings, and the files under `$H` are the page and its stamp, tip and log sidecars.
  Red when: the regeneration commits the page, which `git -C "$C" log` then shows.
- **AC10** — When the probe below runs in `$W`, it prints `[] []`, the map's own
  `"$PY" -B tools/codebase-map/gen_map.py --check` exits 0 there, and the output of
  `"$PY" -B tools/loop/stage_coverage.py` run there holds no line containing
  `unclaimed dossier closed-loop-atlas`, and none containing
  `hook PostToolUse memory/builds/dTrackedAtlas/`, the unclaimed and stale forms both.
  Red when: the dossier's `harness-hooks` row is emptied in `$W`'s working copy, where the probe's
  first list names the hook's key; or S8's `[[hook]]` row is taken out of `tools/loop/loop.toml`
  there, where the stage coverage output prints a line beginning
  `stage-coverage: unclaimed hook PostToolUse`, naming `$REGEN` and ending `· no claim`.

  ```bash
  "$PY" -B -c "import sys; sys.path.insert(0, 'tools/codebase-map'); import map_lib as m, map_extractors as e, coverage_join as cj; t = m.load_map_tree(e.inventory_ids()); c = cj.compute_coverage(e.all_inventories(), m.owners_of(t), t.baseline); print(c.unclaimed.get('harness-hooks', []), c.stale_claims.get('harness-hooks', []))"
  ```

## 7. Gates

The close runs the bar once with the self-test suites on, the bar §8 F3 (a) owes for an edit under
`tools/`. The legs below are those the files touched keep green; `check-wiring self-test` builds its
own fixture settings. No suite arm is added or moved, so no arm line is declared.
`codebase-map coverage + freshness` grades the dossier's claim both ways and the generated
artifacts' bytes. `loop stage coverage` grades the dossier's `stage` and S8's `[[hook]]` row both
ways, and it is the one leg that reads `[[hook]]` rows. `loop definition` parses
`tools/loop/loop.toml` whole through `tools/loop/loop_lib.py#read_definition`, so it reds a row that
breaks the file's TOML; `tools/loop/loop_lib.py#check_loop` grades only the step, workflow and
disposition-alias tables, so it reads no `[[hook]]` row. `kit epoch (shipped bytes move, the version moves)`
grades, at the push boundary, the loop kit's version move the lander mints for the row. The dead-path
leg reads the dossier's prose.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `loop stage coverage` · `loop definition` · `kit epoch (shipped bytes move, the version moves)` · `dead-path carriers (deleted files still named)`

## 8. Open questions

- **F1 — What fires the regeneration after a landing?** Candidates differing in mechanism, each with
  what would make it lose written before its test (M12):
  (a) A git `reference-transaction` hook in `.githooks/`, firing when `refs/remotes/origin/main`
  commits. Loses if a tracked hook file reds an unguarded leg only a `tools/` edit clears, if it does
  not fire on the lander's push, or if it adds more than 100 ms to every ref update. Tested on a
  scratch clone with a bare remote on 2026-11-19: it fired `committed refs/remotes/origin/main` on
  `git push`, so it survives the second test. It fails the third: five commits took 379 ms each with
  a one-line hook and 52 ms without (PINNED), since a commit runs the hook seven times. It fails the
  first: `.githooks/**` is in govkit's declared surface
  (`tools/govkit/registry.toml@aec2b8e3d547a329461575c1ba97f0107908cea4:28`), and
  `tools/govkit/govkit.py@cf818f88cfd1aeb208eb01af9ad413cc784c17f5:3666` fails a tracked surface
  path no entry or exemption names, under the unguarded `govkit selfcheck` leg. A `post-merge` hook
  loses earlier still: `--land` pushes `HEAD` and merges no local branch
  (`tools/push-main.sh@cd8cf5622e82726547fd8f5dd7a8e7815eb0e904:1233`).
  (b) A Claude Code `PostToolUse` hook in `.claude/settings.json`, throttled by a stamp, starting a
  detached runner. Loses if its fast path costs more than `1 s`, if its detached child dies with it, or
  if its wiring reds a leg only a `tools/` edit clears. Tested: 56 to 68 ms (PINNED, §4); the
  detached child outlived its parent and the tool call; and §4 "The wiring" names the two readers of
  the file, neither grading a hook group. It survives. Its limit is §4 "What it does not check": a
  console landing waits for the next tool call on the node. Rev-5 found the third test failing on a
  reader that test missed, the loop kit's stage coverage, and the owner's resolution of §8 F3 clears
  it with one `tools/` row, §4 "The loop table's stage claim".
  (c) A durable scheduled task running the page check. An OS task is a persistent machine change
  the owner must approve, M3's veto 2, so it is parked rather than picked. A harness cron job does
  not outlive its session: the store is in-memory and session-scoped
  (`.unattended.conf@537a26d99de0558aa2927fb2d89557e769923c57:114`).
  (d) The lander's own after-landing step, `tools/push-main.sh#run_post_merge`. It starts only the
  post-merge bar, and extending it edits `tools/`, which this build may not.
  RESOLVED (agent, 2026-11-19, delegated): (b), the one candidate surviving its tests and the vetoes.
- **F2 — Where does the switch live until the policy catalogue can hold it?**
  (a) A JSON conf in this build's folder, beside the hook, holding `atlas.regenerate` and the page
  path, with the catalogue row written in this spec for the move.
  (b) A per-clone git config key. It works, but no review sees it and no other node can read it.
  (c) A key in `.governance/policy.toml`. Vetoed: `tools/policy/policy.py@8883f7773622357bfe53afbc2bef7368c506dc08:602`
  reds a key no catalogue row matches under the unguarded `policy check` leg, and the row is under
  `tools/`.
  (d) A variable in `.claude/settings.json`'s `env`. That block is rendered from the policy, so a
  hand-set variable there is a second source beside the rendered one.
  (a) is tracked, in one place, readable without a spawn, and its move into the catalogue is a copy
  of the row in §4 "The switch". It trips none of M3's vetoes.
  RESOLVED (agent, 2026-11-19, delegated): (a), the most feature-rich option by M3's rule.
- **F3 — The hook's key needs a stage claim only a `tools/` edit adds: what carries it?** The
  wiring's `harness-hooks` key is a part `tools/loop/stage_coverage.py#derive_part_claims` joins to
  a claim, and a hook's one claim home is a `[[hook]]` row of `tools/loop/loop.toml`
  (`tools/loop/loop.toml@b6651f2140d4e9dced399959f6475c2ab4bff0e7:98`). With no row, the
  unguarded `loop stage coverage` leg prints
  `stage-coverage: unclaimed hook PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js · no claim`
  and exits 1. Measured on node d on 2026-11-19 (PINNED): the key and the dossier added in memory to
  the parts `tools/loop/stage_coverage.py#read_stage_parts` returns gave that line, and the dossier's
  own line until a `stage` was set. The build's rule forbids the row: nothing under `tools/`, since
  a touch there owes a `GATE_SELFTESTS=1` bar this run may not run
  (`memory/builds/dTrackedAtlas/README.md@451f102e2dd13cf1304b6f0f4f314fe8cc8f28b9:38`). So F1 (b)
  loses by its own third test, and F1's other candidates had lost already.
  (a) One row in `tools/loop/loop.toml`, beside the process monitor's
  (`tools/loop/loop.toml@b6651f2140d4e9dced399959f6475c2ab4bff0e7:1162`), with `key` the hook's key
  above and `stage = ["step.deploy"]`, the owner lifting the build rule for that file and the close
  running a `GATE_SELFTESTS=1` bar. Every criterion holds, and AC10 then also observes no
  `unclaimed hook` line. It needs an owner turn, since the bar it owes is one this run may not run.
  (b) Wire the group in an untracked settings file on node d, the user's or the checkout's local
  one, so no inventory key, row or claim arises. It rewrites S4 and AC8, and it is a persistent
  change outside review on the machine, M3's veto 2.
  (c) Land unit 4 without S4, the settings group and (a)'s row joining §3's hand-off ask. It fails
  AC8 and §1's "no command typed for it" until the ask lands, M3's veto 1.
  (d) Park unit 4: the run closes with units 1 to 3, and the unit waits for the owner's pick.
  Recommendation: no option survives M3's vetoes under the mandate, so (d) for this run. On the
  owner's turn, (a): the row is the claim home the loop kit declares, it is one data row, and no
  criterion is lost.
  RESOLVED (owner, 2026-11-19): (a), the one [[hook]] row in tools/loop/loop.toml, stage = ["step.deploy"].
  The owner's words: "approve unit 4's loop.toml row then land it". The build's rule against
  `tools/` is lifted for that one file, §4 "The loop table's stage claim" gives the row, and the
  close runs the self-test bar the option names.

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.
- rev-2 · 2026-11-19 · §4 · §5 · §6 · §8 · the pass legs' reds after `390c2bc05`, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-1-3-spec-writer: the figures of the Bounds table, the
  checklist, AC1, AC2, AC7 and F1 (b) that are constants or thresholds this spec declares now sit
  in code spans, and the checkout cost is marked DERIVED from §4's measurement. No design change.
- rev-3 · 2026-11-19 · §4 · the lexicon's verb pin, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-3-name-fold: the inventory's `sidecars` and `regenerate` are
  renamed `deriveSidecars` and `runRegeneration`, each leading with a declared verb. No design
  change.
- rev-4 · 2026-11-19 · §6 · AC6's planted break, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-4-ac6-fold: the line appended after the generator's closing
  `sys.exit` never ran, so it is now inserted above the `if __name__` guard, and AC6 states what the
  page check answers on that tree and why the runner then logs `failed`. No other criterion plants
  code, and no section had the builder flip the status. No design change.
- rev-5 · 2026-11-19 · S7 · §3 · §4 · §5 · AC10 · §7 · §8 · the codebase map's claim of the wired
  hook, folded from 2026-11-19-prompt-TOOL-dTrackedAtlas-4-map-fold after the pre-commit map gate
  refused the build: §4 "The codebase map's claim" gives the new dossier's fence, Files touched
  gains it and the three artifacts whose bytes `gen_map.py --write` changes, §7 gains the map,
  stage-coverage and dead-path legs, AC10 observes the claim, and §3 and §4 "The wiring" stop
  saying no reader grades the group. §8 F3 is new and open: the key also needs a `[[hook]]` row in
  `tools/loop/loop.toml`, which this build may not write. No change to the hook's design.
- rev-6 · 2026-11-19 · §4 · the writing-practice pins, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-4-3-spec-writer: the dossier title's and card's measured
  byte figures in "The codebase map's claim" are marked PINNED on their lines. No design change.
- rev-7 · 2026-11-19 · S8 · §3 · §4 · §5 · AC10 · §7 · §8 · the owner's resolution of F3, folded
  from 2026-11-19-prompt-TOOL-dTrackedAtlas-4-f3-fold: F3 is RESOLVED (owner, 2026-11-19) to (a).
  S8 and §4 "The loop table's stage claim" give the one `[[hook]]` row and its comment line, Files
  touched gains `tools/loop/loop.toml`, AC10 also observes no unclaimed or stale hook line, §7
  gains the `loop definition` and `kit epoch` legs and the self-test bar, and the sentences of §3,
  §4 "The wiring", §7 and F1 (b) that cited F3 as open now cite its resolution. A shipped kit edit
  sets Tier-2 under the manifest's tier rule
  (`memory/guides/SESSION-KICKOFF.md@22b6155febd410581bffa0a0af325e0f24590552:128`), and the header
  moves from DEFERRED to SPECCED and from advancing to closing TOOL-dTrackedAtlas-7. No change to
  the hook's design.

## 10. Reuse audit

The seams extended: the process monitor's hook, `tools/process-monitor/procmon-hook.js#main`, whose
fail-open fast path and stamp throttle this hook follows, though it keeps its stamp in the page's
folder and so needs no copy of `tools/process-monitor/procmon-hook.js#resolveStamp`; the post-merge
bar's detached run of a landed sha in a scratch worktree, `tools/run-gates/post-merge.sh`, whose
environment scrub it repeats; `tools/lib/resolve-python.sh` for the interpreter; and
`TOOL-dTrackedAtlas-3`'s page check as the staleness predicate.
`python tools/codebase-map/reuse_lookup.py "run a command after a landing onto the default branch without anyone typing it"`
ranked name-stem helpers (`run`, `run_git`, `check_landed_facts_due`, `read_landing_commit`), none
a trigger. A second probe, `"harness hook that throttles a background job by a stamp file and spawns
no process on the fast path"`, ranked `stamp` in the pre-push suite and path helpers, none a hook.
`grep` finds no detached spawn under `tools/`, `skills/` or `.claude/`, which the recall hit
`KICK-dKeptSession-21` also records, so the detached start is new here. Seam read and not taken:
`tools/push-main.sh#run_post_merge`, §8 F1 (d). The recall probe returned `TOOL-aFrugalTurnstile-8`,
the lander starting the post-merge bar, and `PLAY-dClosedLoop-28`.
The map claim extends the codebase map's dossier contract, `tools/codebase-map/map_lib.py#parse_dossier`,
in the shape `memory/map/features/process-monitor.md` uses for its own `PostToolUse` hook; no
existing dossier fits a build-folder hook, since each is scoped to one kit and
`memory/map/FOUNDATION.md` holds shared substrate.
The stage claim extends the loop table's `[[hook]]` row kind, which
`tools/loop/stage_coverage.py#derive_part_claims` joins, in the shape of the row keyed
`SessionStart skills/session-kickoff/manifest-check.sh`, the one other key outside the tool root.

Recall terms used: `python tools/memory-recall/query.py "what regenerates a derived page or report after a landing onto main without anyone running it" --terms "post-merge landing GATE_POST_MERGE detached hook PostToolUse throttle stamp regenerate atlas switch policy default-on"`
