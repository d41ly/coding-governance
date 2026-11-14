# TOOL-aLightenedLoop-5 — the stop-guard caches the `--liveness` verdict, keyed on every input the verdict reads and expired by the liveness clock

**Status:** CLOSED · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 |
| [2026-11-14-build-TOOL-aLightenedLoop-5-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aLightenedLoop-5-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-build-TOOL-aLightenedLoop-5-red-fix-4.md](../build/2026-11-14-build-TOOL-aLightenedLoop-5-red-fix-4.md) | red-fix | — |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-answers.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-answers.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-3 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-5-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-5-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aLightenedLoop-5-fork-fold.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-5-fork-fold.md) | research | — |
| [2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md](../reviews/2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md) | diff-review | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/stop-guard.js` spawns `bash unattended.sh --liveness <slug>` on every `Stop` of a
bound session, which cost about 2.7 h over dSafePassage's 1,028 stops (13 s a spawn on a live run, <!-- PINNED 2026-11-14 -->
5 s on an attended slug). This unit serves that verdict from a per-worktree cache whenever no input <!-- PINNED 2026-11-14 -->
of the verdict has moved and the liveness clock cannot yet have flipped LIVE to STALE, so a stop costs
one `git show-ref` and a few file reads, and every decision, reason text and sidecar line stays
byte-identical to a fresh read. The cache is on by default, and `STOP_GUARD_LIVENESS_CACHE=off`
restores today's spawn on every stop.

## 2. Scope (IN)

- **S1** — `deriveLivenessKey` in `tools/unattended/stop-guard.js`: one sha256 over every input the
  driver's verdict reads apart from the clock and the moves (§4, "The key"), or null when the ref
  listing cannot be read. Observed by AC4, AC8.
- **S2** — `readLiveness` in the same file, returning `runLiveness`'s `{stdout, ok}` shape: a hit
  returns the stored driver stdout verbatim without spawning; a miss calls `runLiveness` unchanged
  and stores the result when S4 admits it. `checkSession` calls it where it calls `runLiveness`
  today. Observed by AC1, AC2, AC3.
- **S3** — the clock expiry: a stored LIVE entry is served only while a fresh read could not yet read
  STALE (§4, "The clock"). Observed by AC5.
- **S4** — the stored set: a zero-exit read with a parseable verdict other than STALE, and a LIVE
  only when its `last-move` and `stale-bound` lines are digit runs. Nothing else is written.
  Observed by AC6.
- **S5** — fail-open file handling: an absent, torn or unreadable cache file is a miss, and a cache
  that cannot be written changes nothing the hook decides, writes or prints. Observed by AC7.
- **S6** — `tools/unattended/README.md`, section "The sidecar", names the fourth file kind
  `liveness.<slug>.json` beside the three it lists, and the switch `STOP_GUARD_LIVENESS_CACHE=off`
  that stops it being read or written. Observed by AC9.
- **S7** — `memory/map/generated/` re-rendered for the two new functions. Observed by AC10.
- **S8** — the kill switch (§4, "The switch"): with `STOP_GUARD_LIVENESS_CACHE` exactly `off`,
  `readLiveness` returns `runLiveness`'s result and derives no key, reads no cache file and writes
  none. Observed by AC11.
- **S9** — `stop-guard.js`'s header states that a cache hit does not reproduce a probe fault, names
  the switch, and drops its claim that the hook "reads no mtime, transcript or git of its own"
  (`tools/unattended/stop-guard.js@241f63c7925b:40`), which the key's `git show-ref` makes false.
  Observed by AC12.
  **Readers:** by name: `tools/unattended/stop-guard.js`, whose header at line 40 is the one tracked
  file outside this spec that spells the claim, by a git grep for "reads no mtime" at base 846d51d3.
  by value: NO VALUE READERS — the claim is header prose; no code, gate or record compares, counts
  or derives anything from it.

## 3. Non-goals (OUT)

- No change to `runLiveness`, `parseLiveness`, `checkStop`, `renderBlock` or the sidecar line's
  fields. A hit feeds the same stdout to the same parser.
- No cache in `tools/unattended/gate-guard.js`, which calls `runLiveness` directly
  (`tools/unattended/gate-guard.js@35513cb705fe:723-725`) and keeps doing so.
- No change to the driver's `--liveness` verb, its clock or `RESUME_STALE_BOUND`.
- No new conf key or gate leg. The one new environment knob is the kill switch the owner chose
  under F2.
- No kit-version move: the lander's mint moves it.
- Nothing under `memory/builds/dDeclaredLoop/`.

### Edges

- **hands-off** external — `gate-guard.js`'s own liveness read could call `readLiveness` too; that
  is a follow-up the owner may file, not this unit's.
- **hands-off** external — the DEFERRED dWellOiledMachine units 28, 10, 21, 31 and 64 move
  `stop-guard.js` into a runtime kit or hook packs; they re-ground on this unit once it lands.

## 4. Design

### Evidence

Every claim below was read at base `846d51d3`.

- The one spawn site is `checkSession`'s loop:
  `tools/unattended/stop-guard.js@241f63c7925b:223`, `runLiveness` at `:107-115`, bounded by
  `LIVENESS_BOUND_MS` (`:97`, 60000) or `STOP_GUARD_LIVENESS_BOUND_MS`.
- The hook reads only two lines of the driver's stdout: `verdict:` and `phase:`
  (`parseLiveness`, `:118-126`). Both reach the sidecar line (`:228-233`) and `renderBlock` (`:242`).
- `checkStop` (`:139-156`) treats LIVE, STALE and UNBOUND alike (`run-open`), but `renderBlock`
  (`:166`) prints the verdict word and the sidecar records it, so serving LIVE where a fresh read says
  STALE changes rendered bytes. That is the STALE flip the brief names.
- The verdict is `derive_liveness`'s (`tools/unattended/unattended.sh@95b8f8404cc3:9030`), printed at
  `:9015`. It chooses, first match wins, TERMINAL, ELSEWHERE, FINISHED-UNSTAMPED, HELD, UNBOUND,
  STALE, LIVE (`:9104-9110`), and it reads:

| input | where read | what moves it |
|---|---|---|
| run-state file: `phase`, `witness`, `hold-code`, `session`, `run-branch`, `branch-ref` | `:9006`, `:9065`, `:9056`, `:9074`, `resolve_holder_worktree` | an edit of `RUN.md` |
| HEAD's copy of the run-state file and its last commit | `read_landing_commit`, `tools/unattended/lib-unattended.sh@a3e03db6b9f0:1705-1718` | a commit |
| the landed log `<common-dir>/unattended/landed.<slug>.log` | `:9054`, `resolve_landed_log` at `:1867` | `--landed` in any worktree, with no edit of `RUN.md` |
| the default-branch ref, remote-tracking when present | `:9039-9042` | a fetch or the lander's push, with no move of this worktree's HEAD |
| this worktree's symbolic HEAD | `resolve_holder_worktree`, `:9093` | a checkout |
| the conf: `RESUME_STALE_BOUND` and the two bounds its default derives from, `MEMORY_ROOT`, `GOV_DEFAULT_BRANCH` | sourced at `:748`, bound at `:859-860` | an edit of `.unattended.conf` |
| git config: the remote and `branch.<b>.remote` | `resolve_remote_sh`, `:2724` | `git remote` or `git config` |
| the driver's own code | `unattended.sh`, and `lib-unattended.sh` sourced at `:105` | an edit of either, which this repo's own runs make |
| the clock and the moves: commit, write, gate log, queue heartbeat, transcript, sub-agents | `derive_last_move`, `:8855`; `stale` at `:9100` | time, and every turn of the session |

The brief keys on "the run-state file's mtime plus HEAD". That key misses the landed log, the
remote-tracking ref, the conf, git config and the driver. The parity requirement in the brief's
prompt decides it: the existing suite arm `U61 with no line in the landed log the same stop is not
terminal` (`tools/unattended/stop-guard.test.sh@003d91bd43a9:628-630`) removes the landed log with
`RUN.md` and HEAD unchanged and expects a different verdict, so a two-input key fails an arm already
on the tree. The key below is the brief's key widened to the table, which the goal requires rather
than a choice.

### The key

`deriveLivenessKey(repo, kitDir, record, slug, sessionId)` returns the hex sha256 of these parts,
each written as `<name>\0<value>\0` in this order:

1. `session` — the payload's session id, so two sessions never share an entry.
2. `record` — the bytes of `<root>/<record>`, the lease's `record` path (`scanLeases`,
   `tools/unattended/run-lease.js@2d25214f56d2:161`).
3. `head` — the bytes of `<gitDir>/HEAD`, which carries the symbolic ref ELSEWHERE is keyed on.
4. `refs` — the stdout of `git --git-dir=<gitDir> show-ref --head`, spawned with `windowsHide`. It
   lists HEAD's sha and every branch, remote-tracking ref and tag, so a commit, a fetch and the
   lander's push all move it. A spawn error or non-zero exit returns null.
5. `landed` — the bytes of `<commonDir>/unattended/landed.<slug>.log`. `commonDir` is
   `<gitDir>/commondir` resolved against `gitDir` when that file exists, else `gitDir`, which is
   what `git rev-parse --git-common-dir` answers.
6. `conf` — the bytes of `<root>/.unattended.conf`.
7. `config` — the bytes of `<commonDir>/config`, then of `<gitDir>/config.worktree`.
8. `driver` — the bytes of `<kitDir>/unattended.sh`, then of `<kitDir>/lib-unattended.sh`.

An absent file is the value `absent`, never a miss: a repo with no landed log is the common case. A
file that exists and cannot be read returns null. Content is hashed, not mtimes: the files are small
except the driver, and hashing all of them took 2 ms on node a (PINNED, 2026-11-14), while an mtime
cannot see a same-size rewrite inside its granularity.

`git --git-dir` is named explicitly so git never walks up from the payload's cwd. The suite's stub
fixtures carry a `.git` directory holding only `HEAD` (`stop-guard.test.sh@003d91bd43a9:288-294`), so
`show-ref` fails there, the key is null, and every existing stub arm runs exactly as today.

### The clock

Only LIVE can change by time alone: `stale` turns `yes` once `TC_NOW - newest > RESUME_STALE_BOUND`
(`unattended.sh@95b8f8404cc3:9100`), and every move only pushes that later. TERMINAL, ELSEWHERE,
FINISHED-UNSTAMPED, HELD and UNBOUND read no clock, so they expire only when the key moves. STALE is
never stored, because the session's own transcript moves on every turn and turns it back to LIVE
through an input the key cannot see.

For a LIVE read, `readLiveness` takes `t0 = floor(Date.now() / 1000)` before the spawn and stores
`deadline = t0 - last-move + stale-bound`. Because the driver's `TC_NOW` is at or after `t0`, the
newest move is at or after `t0 - last-move`, so no fresh read can say STALE before `deadline + 1`. A
fresh read started at second `t` ends by `t + W`, where `W` is the hook's bound in whole seconds
rounded up, or it reads unreadable instead. So a stored LIVE is served at second `t` only when
`t + W + 1 <= deadline`. On node a's derived bound that window is most of the bound, since a
stopping session has just written its transcript.

### The switch

`STOP_GUARD_LIVENESS_CACHE` is read from the hook's own environment on every call to
`readLiveness`. Exactly `off` turns the cache off; unset, empty or any other value, `OFF` included,
leaves it on, and no value prints anything. Off means today's path: `runLiveness` is called and its
result returned, with no `git show-ref` spawn, no cache read and no store, and an existing
`liveness.<slug>.json` is left in place untouched. Unsetting the switch later reuses that file only
when its key and deadline still pass, so a stale entry is never served by turning the cache back on.

### Data model

`<gitDir>/unattended/liveness.<slug>.json`, beside `stop.<slug>.log` in the per-worktree sidecar
directory (`run-lease.js@2d25214f56d2:179-181`):

```json
{"key": "<sha256 hex>", "stdout": "<the driver's stdout, verbatim>", "deadline": 1794200000}
```

`deadline` is null for every stored verdict but LIVE. A hit needs a `key` equal to the derived one,
a string `stdout`, and for LIVE a numeric `deadline` passing the clock test. The file is written to
`liveness.<slug>.json.<pid>.tmp` and renamed over the target, so a reader never sees half a file. A
hit writes nothing. A miss that S4 does not admit leaves any older file in place: its key or its
deadline already fails.

### The flow inside `checkSession`

`const run = readLiveness(__dirname, repo, l, sessionId)` replaces the `runLiveness` call at `:223`.
Everything after it is unchanged. Inside `readLiveness`: when the switch reads `off`, return
`runLiveness(...)` at once. Otherwise derive the key; on null, return
`runLiveness(...)` and store nothing. Otherwise read the file; on a hit, return
`{ stdout: entry.stdout, ok: true }`. On a miss, take `t0`, call `runLiveness`, store when S4 admits
the result, and return it. Every read, parse, write and rename failure is caught and treated as a miss
or a skipped store, and nothing is written to stderr, so the hook's stderr stays as it is today.

### Inventory

| minted | kind | where |
|---|---|---|
| `deriveLivenessKey` | function, exported | `tools/unattended/stop-guard.js` |
| `readLiveness` | function, exported | `tools/unattended/stop-guard.js` |
| `liveness.<slug>.json` | sidecar file kind | `<gitDir>/unattended/` |
| `STOP_GUARD_LIVENESS_CACHE` | environment switch, `off` disables | read in `readLiveness` |

### What it does not check

- A probe fault or a hang past the bound that a fresh read would have hit is not reproduced while an
  entry is valid: the cache serves the last good verdict where a fresh read allows with
  `liveness-unreadable`. The owner accepted this under F1; the header says so (S9), and
  `STOP_GUARD_LIVENESS_CACHE=off` restores the fresh read on every stop.
- Inputs outside the repo: a global git config naming a remote, and the session's environment
  (`GOV_REMOTE`, `GOV_DEFAULT_BRANCH`). The environment is the session's and constant across its
  stops, and the session id is in the key.
- Whether the driver's verdict is right. The cache reproduces it and does not grade it.

### Files touched (estimate)

- `tools/unattended/stop-guard.js`
- `tools/unattended/stop-guard.test.sh`
- `tools/unattended/README.md`
- `memory/map/generated/symbols.json`, re-rendered by the map generator's `--write`, with whatever
  else under `memory/map/generated/` that render moves.

### Alternatives rejected

- **The brief's two-input key, run-state mtime plus HEAD.** It fails the existing U61 arm, and it
  serves LIVE after the lander's push where a fresh read says FINISHED-UNSTAMPED (§4, the table).
- **A fixed time-to-live on every entry.** A TTL short enough to be safe against the TERMINAL and
  FINISHED-UNSTAMPED flips would expire before the next stop, and those flips are not clock-driven.
- **Resolving the default-branch ref exactly in JavaScript.** It would copy the remote ladder, which
  is inlined byte-identically and gated (`unattended.sh@95b8f8404cc3:2715-2717`). Hashing every ref
  over-invalidates on an unrelated fetch, which costs a spawn and never a wrong verdict.
- **mtime and size instead of content.** Same cost on node a, and blind to a same-size rewrite.

### Rollout

The hook lands live, cache on, in this repo's own hook wiring. Setting
`STOP_GUARD_LIVENESS_CACHE=off` in the environment the hook runs with turns the cache off with no
code change. The kit epoch leg asks for a version move when
shipped bytes move, and the lander's mint makes it. An adopter receives it with its next kit update.

## 5. Production-readiness checklist

- security — no new input crosses a trust boundary: the cache is written and read by this hook in
  the worktree's own git dir, and a forged file can only make the hook serve stdout whose key matches
  the real inputs. The stored stdout is parsed by the same `parseLiveness` as a fresh one.
- perf / scale — a hit costs one `git show-ref` (73 to 678 ms over 141 refs on a contended node a,
  PINNED 2026-11-14 at `846d51d3`) and about 1.3 MB of hashing (2 ms). A miss costs that plus
  today's spawn.
- error / empty / loading states — S5: every cache failure is a miss or a skipped store.
- observability — the cache file itself. A hit and a miss write identical sidecar lines on purpose.
- risks — a verdict input missing from the key serves a stale verdict; §4's table is the defence,
  and AC4 moves each input. The fault path is accepted (F1), and the kill switch (S8) is the
  fallback for either.
- testing — the new arms in `tools/unattended/stop-guard.test.sh` (§7), on a `git init` fixture with
  the suite's counting stub, plus the real-tree parity probe in AC1.
- migration — N/A: no stored data predates this unit, and an old hook ignores the file.
- user docs — `tools/unattended/README.md`, section "The sidecar" (S6). No `help/` page names the
  stop-guard.

## 6. Acceptance criteria

- **AC1** — When the base hook, the file's bytes at `846d51d3` read with `git show`, and the built
  hook each run with `node` against a clone of this tree under `%TEMP%`, fed one `Stop` payload whose
  session a planted `RUN.md` binds, at phases BUILDING (LIVE), HELD and LANDED (TERMINAL), the
  built hook's miss and its following hit each print stdout byte-identical to the base hook's and
  exit 0, and their `stop.<slug>.log` lines equal the base's with `utc` removed. The sidecar is
  deleted before each run, so each reads block 1 of 6.
  Red when: the hit returns stdout other than the stored driver stdout, or a key part leaks into it.
  cost: about ten real `--liveness` spawns, 5 to 13 s each. <!-- PINNED 2026-11-14 -->
  fixture: a clone made by the probe; the tree holds no bound run of its own.
- **AC2** — When the AC1 probe times each `node tools/unattended/stop-guard.js` run, the built
  hook's hit is faster than the base hook's run at the same phase on node a, and both figures are
  recorded in the unit's acceptance ledger beside the probe that measured them.
  Red when: the hit still spawns the driver, so the two times match.
  figure: PINNED at observation, on a contended node read at about ±2×.
- **AC3** — When the stop-guard suite's new fixture, a `git init` tree with a committed `RUN.md`
  and the counting stub driver, takes two stops with nothing changed between
  them, the stub's counter reads 1, the two stdouts are identical, and `liveness.fx.json` exists
  in the fixture's sidecar directory.
  Red when: `checkSession` still calls `runLiveness` directly and the counter reads 2.
- **AC4** — When the same fixture moves exactly one input between two stops, for each of these
  moves in turn the counter rises by one: an edit of `RUN.md`; a commit; a checkout of another
  branch at the same sha; `git update-ref refs/remotes/origin/main`; an append to the common dir's
  `landed.fx.log`; an edit of `.unattended.conf`; `git config branch.fx.remote origin`; an edit of
  the kit copy's `unattended.sh`; and a stop under another session id bound by the same `RUN.md`.
  Red when: `deriveLivenessKey` drops any one part, which the staged break does one part at a time.
- **AC5** — When the stub prints LIVE with `last-move` and `stale-bound` lines and
  `STOP_GUARD_LIVENESS_BOUND_MS` sets the bound, a second stop is served from cache when
  `deadline - now` exceeds the bound plus one second, and spawns the stub when it does not.
  Red when: `readLiveness` ignores `deadline`, so the near-expiry stop is served from cache.
- **AC6** — When the stub prints STALE, exits non-zero, prints no `verdict:` line, or prints LIVE
  without a digit `last-move` or `stale-bound`, no `liveness.fx.json` is written and a second stop
  spawns the stub again.
  Red when: the store admits STALE, which the staged break does.
- **AC7** — When `liveness.fx.json` holds a torn line, and separately when `.git/unattended` cannot
  hold the cache file, the stop's stdout, exit code, sidecar line and stderr equal a run with no
  cache at all, compared with `cmp`.
  Red when: a JSON parse error escapes `readLiveness` and the hook exits through `main`'s fail-open
  catch with no sidecar line.
- **AC8** — When the suite's existing stub fixture, whose `.git` holds only `HEAD`, takes a stop,
  `deriveLivenessKey` returns null and no `liveness.fx.json` is written.
  Red when: `show-ref` runs without `--git-dir` and resolves an enclosing repository.
- **AC9** — When `grep -n 'liveness.<slug>.json' tools/unattended/README.md` and
  `grep -n 'STOP_GUARD_LIVENESS_CACHE' tools/unattended/README.md` run, each prints a line inside the
  section "The sidecar", and `git diff 846d51d3 -- tools/unattended/gate-guard.js`
  prints nothing.
  Red when: the README still says the sidecar holds three kinds.
- **AC10** — When `python tools/codebase-map/gen_map.py --check` runs after the build, it exits 0.
  Red when: `memory/map/generated/symbols.json` lacks `readLiveness` or `deriveLivenessKey`.
- **AC11** — When the AC3 fixture takes two stops with `STOP_GUARD_LIVENESS_CACHE=off` and nothing
  changed between them, the stub's counter reads 2 and no `liveness.fx.json` is written; and when a
  valid `liveness.fx.json` left by a stop with the switch unset is present, a stop with the switch
  `off` still raises the counter by one and leaves that file's bytes unchanged.
  Red when: `readLiveness` ignores `STOP_GUARD_LIVENESS_CACHE`, so the second stop is served from
  cache and the counter reads 1.
- **AC12** — When `grep -n 'does not reproduce' tools/unattended/stop-guard.js` and
  `grep -n 'STOP_GUARD_LIVENESS_CACHE' tools/unattended/stop-guard.js` run, each prints a line inside
  the header comment above `'use strict'`, and
  `grep -n 'reads no mtime, transcript or git' tools/unattended/stop-guard.js` prints nothing.
  Red when: the header still claims the hook reads no git of its own, or omits the fault caveat.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `recall floor` · `recall floor arms`

The first five grade this unit's change. `recall floor` and `recall floor arms` are owed by the
`memory/` guard the map re-render trips; the other three paths trip only the broad `tools/` guard,
as `python tools/check-spec-tokens.py --legs-for` printed at `846d51d3`. The stop-guard suite is
withheld by `tools/unattended/kit.toml` and runs in the unattended kit's pooled self-test tier,
which the main loop runs once at the close with the bar. No leg is added.

New arm: tools/unattended/stop-guard.test.sh · covers AC3 · `checkSession` calling `runLiveness` directly, so the counter reads 2 · none
New arm: tools/unattended/stop-guard.test.sh · covers AC4 · each key part dropped from `deriveLivenessKey` in turn · none
New arm: tools/unattended/stop-guard.test.sh · covers AC5 · the `deadline` test removed from the hit path · none
New arm: tools/unattended/stop-guard.test.sh · covers AC6 · the store admitting STALE · none
New arm: tools/unattended/stop-guard.test.sh · covers AC7 · the JSON parse unguarded in `readLiveness` · none
New arm: tools/unattended/stop-guard.test.sh · covers AC8 · `show-ref` spawned without `--git-dir` from a fixture nested in a git repository · none
New arm: tools/unattended/stop-guard.test.sh · covers AC11 · `readLiveness` ignoring `STOP_GUARD_LIVENESS_CACHE`, so the counter reads 1 · none

What these arms do not check: the real driver's verdict on a cache hit, which AC1 observes on a
clone, and an input absent from §4's table, which no arm can stage.

## 8. Open questions

- **F1 — Is the fault path acceptable?** While an entry is valid, a stop is served the last good
  verdict even when a fresh read would have hit a dead probe or run past the 60 s bound and allowed <!-- PINNED 2026-11-14 -->
  with `liveness-unreadable`. On a contended node a slow driver is the likely case: there the cached
  hook blocks with `run-open`, where today it allows. No cache can reproduce a fault it skipped.
  - (a) Accept it, and state in `stop-guard.js`'s header that a cache hit does not reproduce a
    fault. Parity holds for every verdict the tree determines.
  - (b) Do not build the unit.
  Recommendation: (a). The brief's parity is over the tree's verdicts, and a fault is not one of them.
  RESOLVED (owner, 2026-11-14): (a). The fault path is accepted, and `stop-guard.js`'s header states
  that a cache hit does not reproduce a fault (S9, AC12).
- **F2 — Does the charter's `[small]` rule require the cache to land dark?** The rule puts risky
  behaviour behind a default-off switch. The risk here is an input missing from the key.
  - (a) Default on, with no switch. AC1 and AC4 prove parity, and every cache failure falls back to
    today's spawn.
  - (b) Default on, with an environment kill switch `STOP_GUARD_LIVENESS_CACHE=off`.
  - (c) Default off behind a conf key, turned on by the owner later. The brief's timing is then
    measured with the key on, and no run gains until it is turned on.
  Recommendation: (a). A switch for a parity-proven read path is scaffolding the [yagni] rule refuses.
  RESOLVED (owner, 2026-11-14): (b). Default on, with the environment kill switch
  `STOP_GUARD_LIVENESS_CACHE=off` restoring today's spawn on every stop (§4 "The switch", S8, AC11).

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.
- rev-2 · 2026-11-14 · §1 §3 §4 §5 §8 · S6 S8 S9 · AC2 AC9 AC11 AC12 · folded the owner's F1 (a) and
  F2 (b) answers from 2026-11-14-prompt-TOOL-aLightenedLoop-5-fork-fold: the fault caveat and the
  dropped no-git claim in the header, the `STOP_GUARD_LIVENESS_CACHE=off` kill switch with its arm,
  and a backticked witness on AC2 after hygiene check 12 refused the opening commit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "cache a hook's spawned verdict keyed by file mtimes and
expire it by a clock"` returned no caching seam: its candidates were key and file readers such as
`read_conf_key` and `readConfKey`, none of which stores a result. No existing seam fits, so this
unit extends `runLiveness` in `tools/unattended/stop-guard.js` by wrapping it, and writes beside
`deriveSidecarPath`'s directory in `tools/unattended/run-lease.js`. The dispatch cache the brief
names, `derive_spec_token_key` with `gate-fingerprint.sh`, keys a gate verdict on file hashes in
shell and Python; its idea of hashing every input is reused, and its code is not callable from this
Node hook. Recall named `TOOL-aOrientedCast-24`, which is where `gate-guard.js` began calling
`runLiveness`, and that is why this unit wraps the function rather than changing it.

Recall terms used: `python tools/memory-recall/query.py "how does the stop-guard read liveness and
could its verdict be cached" --terms "stop-guard liveness verdict runLiveness cache spawn Stop hook
STALE RESUME_STALE_BOUND sidecar mtime HEAD"`
