# TOOL-dTrackedAtlas-4 — the Atlas page regenerates on node d after main moves, behind a switch whose default is on

**Status:** SPECCED · rev-1 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · ratified 2026-11-19 · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-4-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-4-spec-brief.md) | research | — |

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

## 3. Non-goals (OUT)

- Generating, stamping or checking the page: the generator and its `--out` are
  `TOOL-dTrackedAtlas-2`'s, the stamp and `--check --page` are `TOOL-dTrackedAtlas-3`'s, and this unit
  only runs them.
- A row in `tools/policy/catalogue.toml` and a key in `.governance/policy.toml`: both are under, or
  read by, `tools/`, which this build may not touch. The move is an ask the main loop files at the
  close (§3 "Edges").
- A git hook, an edit to `tools/push-main.sh`, an OS scheduled task, or a harness cron job: §8 F1.
- Fetching from the remote. A landing made on another node reaches this page when something on node
  d next moves `refs/remotes/origin/main`.
- Regenerating when run claims move without the tree moving: claims are not page inputs
  (`TOOL-dTrackedAtlas-3` §4 "What it does not check").
- Publishing or committing the page, and any page other than the one `atlas.page` names.
- A `help/` page: no kit ships this hook, and the policy move the ask names brings the
  `help/policy.md` row with it.
- A gate, a suite arm or a self-test: the hook is a build-folder instrument, checked by its fixture
  observations.

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
| the fast path | none set; 56 to 68 ms measured | the harness `timeout` of 10 s kills it |
| each git call | `GIT_BOUND_S`, 300 s | the step fails and is logged |
| the page check | `CHECK_BOUND_S`, 300 s | read as not current, so the page regenerates |
| the generation | `GEN_BOUND_S`, 1500 s | the step fails and is logged |
| the whole runner | `RUN_BOUND_S`, 2400 s, armed as a timer | kills its child, logs `failed — no answer within 2400 s`, releases the lock, exits 1 |

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
check reads only the file's `env` block, so neither grades this group. A session reads its hooks at
start, so the group takes effect in sessions started after the checkout carries it.

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
| `sidecars(page)` | function | the six paths of §4 "The page's folder", the pid's two included |
| `runHook(input)` | function | the fast path; returns 0 |
| `runRunner()` | function | the runner; returns 0, or 1 after a failed regeneration |
| `regenerate(root, tip, py, paths)` | function | the regeneration steps; returns the log line's outcome and reason |

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
  runner start per 60 s; a regeneration costs a checkout of about 13 s plus one generation.
- error / empty / loading states — No conf, no folder, a held lock, an unresolved tip, a failing
  check, generation or rename: each is a named exit or log line, and the page stays as it was.
- observability — The log sidecar, one line per handled tip; the stdout line for a missing folder.
- risks — A wedged generation is killed at 2400 s. A browser holding the page open can refuse the
  rename on Windows, which logs `failed` and keeps the old page.
- testing — The fixture observations of §6, on a scratch clone.
- migration — N/A — a new file pair and one appended settings group; nothing existing changes shape.
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

- **AC1** — When the stamp `$H/closed-loop-atlas.regen.stamp` is younger than 60 s and
  `echo '{"tool_input":{"command":"ls"}}' | node "$C/$REGEN"` runs, it exits 0 within 1 s, prints
  nothing, and the stamp's modification time, read with `stat -c %Y`, is unchanged.
  Red when: the stamp is older than 60 s, where the same call moves its modification time and a
  runner starts.
- **AC2** — When a landing `T1` appends a line to `memory/builds/dWitnessedBar/RUN.md`, the stamp is
  deleted, and `echo '{"tool_input":{"command":"bash tools/push-main.sh --land --slug x"}}' | node "$C/$REGEN"`
  runs, it exits 0 within 2 s; then, once `$H/closed-loop-atlas.regen.log` gains a line naming
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
- **AC6** — When a landing appends `raise SystemExit(3)` to `$ATLAS` and the runner runs, it exits 1,
  the log's last line names `failed`, the page is byte-identical to before, and no
  `$H/regen-*` folder and no `$H/*.regen-*.html` file remain.
  Red when: the scratch checkout's removal is skipped, where `$H/regen-<pid>` remains and
  `git -C "$C" worktree list` lists it.
- **AC7** — When `$H/closed-loop-atlas.regen.lock` is written fresh by hand before a landing and the
  runner runs, it exits 0 within 2 s and the log gains no line; with the lock's modification time set
  older than 2400 s by `touch -d`, the run logs `stale lock removed` and handles the tip.
  Red when: the lock is ignored, where the first run handles the tip.
- **AC8** — When a `node -e` one-liner parses `.claude/settings.json` in `$W`, it finds exactly one
  `PostToolUse` group with matcher `Bash|PowerShell` whose command names `$REGEN`, with a `timeout`
  of 10, and `$W/$REGEN` exists.
  Red when: the same one-liner run at the run's base finds no such group.
- **AC9** — When AC2 to AC7 have run, `git -C "$C" status --porcelain` lists only `$CONF`,
  `git -C "$C" worktree list` lists one checkout, `git -C "$C" log origin/main` holds only the
  fixture's landings, and the files under `$H` are the page and its stamp, tip and log sidecars.
  Red when: the regeneration commits the page, which `git -C "$C" log` then shows.

## 7. Gates

The close runs the plain bar once. The legs below are those the files touched keep green; the
guarded `check-wiring self-test` is an on-demand leg the plain bar does not run, and it builds its
own fixture settings. No suite arm is added or moved, so no arm line is declared.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates`

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
  detached runner. Loses if its fast path costs more than 1 s, if its detached child dies with it, or
  if its wiring reds a leg only a `tools/` edit clears. Tested: 56 to 68 ms (PINNED, §4); the
  detached child outlived its parent and the tool call; and §4 "The wiring" names the two readers of
  the file, neither grading a hook group. It survives. Its limit is §4 "What it does not check": a
  console landing waits for the next tool call on the node.
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

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.

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

Recall terms used: `python tools/memory-recall/query.py "what regenerates a derived page or report after a landing onto main without anyone running it" --terms "post-merge landing GATE_POST_MERGE detached hook PostToolUse throttle stamp regenerate atlas switch policy default-on"`
