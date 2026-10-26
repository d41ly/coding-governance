# TOOL-dWellOiledMachine-40 — the commit queue pushes the build's branch as `build.push` says, taking no lander lock and running no bar but a declared branch bar

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 23 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0318@800a78ec whole
**Carries:** node:policy-key.build.push

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

No rule pushes a build's branch before its landing, so a take-over on another node cannot read the
witnesses the design says it reads (gap-rt-33): nothing in the driver pushes a build branch at this
base. This unit has the commit queue push the build's branch as `build.push` says, every pass commit
by default, each push taking no lock the lander holds and running no bar but a branch bar the
repository declares, so another node reads the holder's witnesses and derives the card's pointers
from the pushed branch (the night pass two, point 4; the owner's NT-19).

## 2. Scope (IN)

- **S1** — `build.push` (`every-item`, `every-pass`, `every-transition`, `at-landing`; default
  `every-pass`, every preset's cell), read once per queue run through the policy kit's
  `policy.py get build.push` as a subprocess, a refusal reading the catalogue default with one NOTE
  naming the key. `derive_push_due(value, event)` in `tools/runtime/commit_queue.py` answers whether
  a queue event, one of `item-witness`, `pass-commit`, `transition` and `landing`, pushes: each
  value pushes on its own event and on `landing`, and `every-item` on `pass-commit` too, since a
  pass commit is an item's witness. Observed by AC1.
- **S2** — The commit at the witness:
  `write_return_commit(repo, build, workspace, act, paths, event)` in `commit_queue.py`, called when
  a role return's item witness is recorded, commits the return's paths into the build's trail
  through I19's `enqueue_commit` (TOOL-dWellOiledMachine-11 S6), one commit per return, asks
  `derive_push_due` for `event`, runs S3 when it is due, and ends with the `next —` line
  `python <prefix>/runtime/next.py --tail <slug>` prints (I13, TOOL-dWellOiledMachine-2 S2). Its
  caller at each witness is the supervisor's act loop. Observed by AC2.
- **S3** — The push, `run_build_push(repo, branch)` in `commit_queue.py`: one
  `git push <remote> HEAD:refs/heads/<branch>` from the workspace the queue commits in, the remote
  resolved by the remote ladder `resolve_remote` (`tools/lib/resolve_remote.py:17`), printing
  `build push — <branch> <sha8> · <event>` or `build push — not pushed: <why>`. It reads and writes
  no file of the lander's: neither the marker `push-main-active` (`tools/push-main.sh:190`) nor any
  lock, and it waits on none. Its bar is the pre-push hook's non-default path: the branch bar
  `GOV_BRANCH_GATE_CMD` where `.githooks/gate-env.sh` declares one (`.githooks/pre-push:1145`), else
  the hook's `decision=skip-nondefault` exit (`:1166`); never `decision=full`. A failed push leaves
  the commit in place and is retried at the next due event. Observed by AC1, AC3.
- **S4** — The lander's verdict files on a non-default push: TOOL-dPlacedRequest-11 S4 moves the
  hook's clear of `pre-push-refusal`, `pre-push-bar` and `pre-push-allow` behind the default-branch
  test, cited here and not re-specced; this unit observes that a build-branch push made from the
  lander's own git dir during a landing leaves them intact. Observed by AC4.
- **S5** — The take-over reads the pushed branch: a successor on another node fetches
  `refs/heads/<branch>`, and the runtime kit's `next` (`next.py`, TOOL-dWellOiledMachine-2) and the
  card's `## pointers` (KICK-dKeptSession-13's `render_pointers`) are derived from that branch's
  commits, so the successor's `next —` line names the first unit with no witness on it and the
  closing review over `<base>..<branch>` receives every pushed return's rows. Observed by AC2.
- **S6** — The page `help/runtime.md` gains a section on the build push: the four values, when each
  pushes, that no lander lock is taken, which bar runs, and what a successor reads. Observed by AC5.

## 3. Non-goals (OUT)

- The commit queue, its serial order, the workspace and the sweep: TOOL-dWellOiledMachine-11.
- The verdict-file move in `.githooks/pre-push` and the claim-push lock's retirement:
  TOOL-dPlacedRequest-11 S4 and S6.
- The fence on the branch push: TOOL-dWellOiledMachine-60 routes this push through
  TOOL-dPlacedRequest-15's fenced push.
- A unit held off the build's node and its own branch: TOOL-dWellOiledMachine-41.
- A branch bar for this repository: none is declared, and this unit declares none.
- The return record's kind and store: TOOL-dWellOiledMachine-8.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-11` — `commit_queue`, the serial queue and its `enqueue_commit`, whose commits S2 makes and S3 pushes
- **consumes-from** `TOOL-dWellOiledMachine-2` — `next —`, the line each `write_return_commit` ends with and a successor's `next` prints from the pushed branch
- **hands-off** `TOOL-dWellOiledMachine-60` — `build.push`, the branch push that unit carries through the fence
- **hands-off** `TOOL-dWellOiledMachine-41` — `build.push`, the rule a unit holder's own branch is pushed by
- **consumes-from** external — TOOL-dPlacedRequest-11 S4's verdict-file clear behind the default-branch test; KICK-dKeptSession-13's `render_pointers`

## 4. Design

### Evidence

- The driver pushes no build branch: TOOL-dPlacedRequest-15 §3 records that
  `git grep -n "GIT push" tools/unattended/unattended.sh` finds nothing, and its claim writes push
  through `observe_remote`.
- The pre-push hook gates the default branch's line with the full bar and every other push only by a
  declared branch bar (`.githooks/pre-push:1-4`, `:1139-1166`); its run-log `ev end` line carries
  `decision <x>` (`:452`) in `pushes.log` under `<git-common-dir>/runlog/`
  (`tools/runlog/runlog_lib.py:39-40`).
- At this base the hook clears all three verdict files on every run, before the ref loop
  (`.githooks/pre-push:494`); TOOL-dPlacedRequest-11 S4 moves that clear.
- The lander's lock files live in its own git dir: `push-main-active` (`tools/push-main.sh:190`) and
  `claim-push.lock` (`:294-315`), the latter retired by TOOL-dPlacedRequest-11 S6.
- The night pass two measured 110 build-branch pushes at a median of 0.44 s with no bar
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:320-326`).

### When each value pushes

| `build.push` | `item-witness` | `pass-commit` | `transition` | `landing` |
|---|---|---|---|---|
| `every-item` | push | push | no | push |
| `every-pass` | no | push | no | push |
| `every-transition` | no | no | push | push |
| `at-landing` | no | no | no | push |

The `landing` push is the branch's last push before the lander's, so every value leaves the branch on
the remote before the landing reads it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_return_commit` | Python function in `commit_queue.py` | `write`, OK |
| `derive_push_due` | Python function in `commit_queue.py` | `derive`, OK |
| `run_build_push` | Python function in `commit_queue.py` | `run`, OK |
| `item-witness`, `pass-commit`, `transition`, `landing` | queue events | none |
| `build push —` | output line | none |

Each function name was checked with `python tools/lexicon/lexicon.py --suggest <name> --as
py.function`; each printed OK.

### Migration

None: the branch push is new, and the catalogue row exists (`tools/policy/catalogue.toml:998`).

### Files touched (estimate)

- `tools/runtime/commit_queue.py`
- `help/runtime.md`

### Alternatives rejected

- **Pushing through the lander.** The lander takes its marker and runs the full bar; a pass push
  would wait on a landing and pay the bar, both of which the clause forbids.
- **A push at every commit regardless of `build.push`.** The owner made it a key, "settable by
  policy, every pass commit by default".

## 5. Production-readiness checklist

- security — the push writes only the build's own branch, through the hook; no new credential path.
- perf / scale — one push per due event; the measured median is 0.44 s.
- error / empty / loading states — a failed push prints `build push — not pushed: <why>` and is
  retried at the next due event; the commit stays.
- observability — one `build push —` line per push and the hook's `pushes.log` line with its
  decision.
- risks — a push while the remote is unreachable delays a take-over's view until the next push.
- testing — the fixture cases AC1 to AC4 and the arm in §7.
- migration — none.
- user docs — `help/runtime.md`'s section (S6).

## 6. Acceptance criteria

The fixture is a bare remote and two clones, `na` and `nb`, under `%TEMP%` with short names, the
repository's `.githooks` as each clone's hooks path, the runtime, loop and policy kits installed, and
a planted build `fx` of five units on branch `build/fx`.

- **AC1** — When the queue in `na` replays one planted event sequence under each of the four values
  of `build.push`, the `build push —` lines match S1's table row for that value, and `git ls-remote`
  shows the branch at the last pushed commit.
  Red when: a value pushes on an event its row says no, or skips one it says push.
- **AC2** — When `na`'s queue commits the returns of units 1 to 3 under `every-pass` and `na`'s
  process is killed, `nb` fetches `build/fx` and `python next.py fx` prints a `next —` line naming
  unit 4's item, and
  `git diff --name-only <base>..origin/build/fx` lists the three returns' files.
  Red when: `nb` names unit 1, or a return is missing from the range.
- **AC3** — When `na` holds `push-main-active` and a landing whose hook runs a 60-second stub bar, a
  pass push from `nb` completes in under 10 seconds, and the last `ev end` line of `pushes.log` in
  `nb`'s runlog carries `decision skip-nondefault`; with `GOV_BRANCH_GATE_CMD` declared it carries
  that bar's decision.
  Red when: the push waits on the landing, or the line carries `decision=full`.
- **AC4** — When a build-branch push runs from the lander's git dir while the planted
  `pre-push-refusal`, `pre-push-bar` and `pre-push-allow` files are present, `cmp` finds each
  byte-equal to its copy taken before the push.
  Red when: a verdict file is cleared or rewritten.
- **AC5** — When `grep -n "build.push"` runs over the runtime kit's page `runtime.md`, the section
  names the four values, the lock that is never taken and the bar that runs.
  Red when: a value or either statement is missing.

## 7. Gates

`pre-push self-test` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/runtime/commit_queue.py · covers AC1 AC2 AC3 AC4 · the `--selftest` fixture's two clones and planted lander files, staged against a queue that never pushes · none

## 8. Open questions

- **F1 — Does `every-item` push at a pass commit?** (a) Yes, a pass commit is an item's witness; (b)
  only at a witness the queue records apart from a pass. (b) leaves the default's push uncovered by
  the finer value, so `every-item` would push less than `every-pass` on a build whose items are
  passes. Rung 1, v2:1300's order of the values from finest to coarsest. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Does every value push at the landing?** (a) Yes; (b) only `at-landing`. (b) lets a landing
  read a branch the remote lacks its last commits of, which no successor can read. Rung 1, the
  clause: "so a take-over on any node reads the witnesses the lease's holder wrote". RESOLVED
  (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended are the commit queue `commit_queue.py` (I19, TOOL-dWellOiledMachine-11), the
remote ladder `resolve_remote` (`tools/lib/resolve_remote.py:17`), and the pre-push hook's
non-default path with its branch bar (`.githooks/pre-push:1139-1166`), which already decides what a
build-branch push runs. The probe `python tools/codebase-map/reuse_lookup.py "commit each role return
and push the build branch without the lander lock or the bar"` ranked `build_commit`
(`tools/unattended/lib-unattended.sh`) and `build_fixture` by name stem; `build_commit` builds a
records commit over a range and pushes nothing. Scout C's lines cite `pre-push:494`, `push-main.sh:190`
and `:294-315`, which hold at this base; its product path `unattended-build.template.js` is the commit
queue's seam, TOOL-dWellOiledMachine-11's, and is not touched here.

Recall terms used: `python tools/memory-recall/query.py "when does the commit queue push a build
branch and which verdict files does the hook clear" --terms "build.push commit queue branch push
skip-nondefault verdict files pre-push lander lock take-over witness"`
