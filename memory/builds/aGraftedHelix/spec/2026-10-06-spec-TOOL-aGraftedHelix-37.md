# TOOL-aGraftedHelix-37 — breaking a stale claim-push lock is a step one writer wins

**Status:** CLOSED · rev-3 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 21 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-37-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-37-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md](../build/2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md) | journal | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-33 TOOL-aGraftedHelix-34 TOOL-aGraftedHelix-35 TOOL-aGraftedHelix-36 TOOL-aGraftedHelix-38 TOOL-aGraftedHelix-39 TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41 |
| [2026-10-06-prompt-TOOL-aGraftedHelix-37-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-37-1-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Unit 36 serialised the claim writer and the lander with the directory lock `claim-push.lock`, and a
writer that finds that lock stale breaks it with `rm -rf` and then `mkdir`, with no re-check. Two
writers that read the same stale deadline can both break it and both proceed, which removes the
serialisation the lock exists for. This unit makes the break a step only one writer can win, makes
that winner re-read the lock before it removes it, bounds what a crash inside the break leaves
behind, and says in the function's header what the mechanism still does not cover.

## 2. Scope (IN)

- **S1** — The take moves out of `write_claim` into `write_claim_push_lock <lock dir> <owner token>`
  in `tools/unattended/unattended.sh`, returning 0 when taken and 1 when busy. The staleness rule
  unit 36 inlined moves unchanged into `check_claim_push_lock_stale <lock dir>`: a deadline in
  `until` already passed, or no readable deadline and a directory older than two minutes. A writer
  whose `mkdir` fails and that reads the lock stale breaks it only after it takes the guard
  directory `<lock dir>.break` with `mkdir`. Holding the guard it re-reads the rule, and only a lock
  still stale is broken and made again. It writes `until` and `owner` before it releases the guard.
  A re-read that finds the lock live, or a re-make that loses to a plain `mkdir`, releases the guard
  and reports busy. `write_claim` keeps its busy `WC_WHY` text byte for byte. Observed by AC1, AC2
  and AC7.
- **S2** — A guard left by a crash is bounded. A writer that cannot take the guard and finds it older
  than one minute removes it and reports busy, and never takes the guard in the same call. A younger
  guard reports busy and stays. The next call breaks the lock through the ordinary path. Observed by
  AC3 and AC4.
- **S3** — The lock names its owner. `write_claim` passes `$BASHPID.$RANDOM` as the owner token,
  and the take writes it to the lock's `owner` file. Every release in `write_claim` goes through
  `remove_claim_push_lock <lock dir> <owner token>`, which clears the lock only while `owner` still
  reads that token. `until` stays a bare epoch, so the lander's wait reads it as before. Observed by
  AC5 and AC7.
- **S4** — The two self-heals are logged. A stale lock broken appends `claim-push-lock-broken`, and an
  abandoned guard cleared appends `claim-push-guard-cleared`, each through `add_health_event` with
  source `unattended` and the path as its detail, after the guard is released. The kit README's
  health-log paragraph names both events beside `claim-taken-over`. Observed by AC3 and AC6.
- **S5** — The headers. The comment above `write_claim_push_lock` states the mechanism and carries a
  `WHAT THIS DOES NOT CHECK:` clause naming four gaps: the abandoned-guard removal is itself
  unguarded, an owner that outlives its recorded deadline, a wall-clock step, and a writer in another
  git dir. `write_claim`'s header stops saying a stale lock is "cleared and taken once" and points at
  the new function. Observed by AC6.
- **S6** — The driver suite gains one block, `GH37`, beside the GH36 AC14 lock arms in region two.
  It extracts the three functions from the shipped driver with `sed` and runs them in a scratch dir,
  never against a copy typed into the suite. It holds four arms: the two-writer race, the
  abandoned-guard bound, the interleaved abandoned guard, and the owner check. Each arm's staged
  break goes through `mutate`, and an empty extraction fails naming the function.
  `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the assertions the block adds. Observed by AC1, AC3,
  AC4, AC5 and AC9.
- **S7** — The records. The class record
  `memory/gotchas/decision-re-derived-by-a-second-process.md` gains this third instance, a stale
  lock broken on a stale read, and its gate section names the GH37 arms. The dossier
  `memory/map/features/unattended-stops.md` says a stale lock is broken under the guard. The
  `unattended` kit version bumps once, after this unit's last move in the kit, in every carrier
  `tools/check-kit-versions.sh` pairs, and the guides are re-adopted. Observed by AC8 and AC9.

## 3. Non-goals (OUT)

- **No change to the lander.** `check_claim_push_clear` in `tools/push-main.sh` reads `until` and
  waits, never removes, and never looks at `owner` or the guard. Its header sentence that the writer
  clears a stale lock on its next take stays true.
- **No change to the staleness rule.** The deadline formula, now plus `REMOTE_BOUND` plus ten
  seconds, and the two-minute age for a lock with no deadline stay as unit 36 set them.
- **No new dependency, conf key, env override or leg.** `flock` is not used. The guard's one-minute
  age is a literal beside the lock's two-minute one. The arms live in a suite that already exists
  (shared invariant 5).
- **The turnstile is not touched.** `ts_try_reap` in `tools/run-gates/run-gates.sh` carries the same
  class, filed as `TOOL-aReapedTicket-4` and still OPEN. It is another kit's code (shared invariant
  2), and §10 records what this unit's measurement says about that ask's candidate.
- **No serialisation of the abandoned-guard removal.** Guarding that removal needs another guard, and
  the same question one level down. S2 bounds the wedge and S5 states the residual.
- **No change to `REMOTE_BOUND` or the push bound.** A push that outlives its recorded deadline stays
  the gap `write_claim`'s header already names.

### Edges

- **consumes-from** external — the claim-push lock, its `until` file, `write_claim`'s busy and
  marker paths and the lander's wait, as unit 36 built them and as they stand at `5ec5ef30`, the tip
  this spec was grounded on; this unit builds none of them.
- **hands-off** external — the same race in the run-gates turnstile's reap, an OPEN ask of the
  aReapedTicket build that this unit's §10 measurement bears on and does not close.

## 4. Design

### Evidence

Read at `5ec5ef30`, the run branch's tip, which carries unit 36's build.

- `tools/unattended/unattended.sh:2071` is `write_claim`. The lock block is `:2076-2090`, and its
  break is `:2083`, `rm -rf "$lk"; mkdir "$lk" 2>/dev/null || busy=1`, with no re-read between the
  stale decision at `:2081-2082` and the removal. The busy reason is `:2099-2100`, and the release is
  `:2130`, `[ -z "$lk" ] || rm -rf "$lk"`, which removes whatever lock sits at the path.
- The header at `:2056-2064` says the lock serialises the two writers, and that a stale lock "is
  cleared and taken once" (`:2062`). Its `WHAT THIS DOES NOT CHECK` at `:2063` names only the
  unbounded push.
- `tools/push-main.sh:211-234` is `check_claim_push_clear`. It reads `until` as digits alone and
  treats anything else as no deadline, so a token written into `until` would turn every wait into
  the 120-second ceiling. That is why S3 writes a separate `owner` file.
- `tools/unattended/unattended.test.sh:14400-14418` is the GH36 AC14 block, inside the region-two
  block `:14347-14507`, 160 lines against the suite's 2500-line block cap.
- `tools/run-gates/run-gates.sh:1057-1064` is the turnstile's `ts_release`, which removes its beacon
  only while `nonce` reads its own value. S3 follows that pattern without calling it.
- `flock` is absent from node `a`'s Git Bash (`command -v flock` prints nothing), and
  `tools/run-gates/run-gates.sh:1265` records the same.

### Probes run while speccing, all on node a, 2026-10-06

Every probe ran in this session's scratchpad over plain directories, never a repository. The
harness pre-stages a `claim-push.lock` whose `until` passed five seconds ago. It starts each writer
in a subshell that spins until a `go` file exists, then calls the take. A writer whose take returns
0 proceeds and never releases inside the trial, and the harness counts trials in which more than one
proceeded. The current code was measured by extracting `:2078-2089` verbatim into a scratch
function. All figures are PINNED at `5ec5ef30`, and AC2 re-derives them.

| arrangement | current code | guard (C1) | rename (C2) |
|---|---|---|---|
| two writers, released together | 0 of 100 | — | — |
| two writers, the second's `date` sleeps 1 s | 20 of 20 | 0 of 20 | 0 of 20 |
| two writers, the second's `date` waits for the first's verdict | 10 of 10 | 0 of 10 | — |
| the same, guard re-read cut | — | 10 of 10 | — |
| as row 2 plus a third writer starting 1.5 s after `go` | — | 0 of 10 | 10 of 10 |

The race is real on node `a`, but it needs one writer to lag the other by about one process spawn.
Its stale read must come before the first writer's removal, and its own removal after the first
writer's `mkdir`. Released together, both remove the same stale lock and one `mkdir` wins. A lagging
writer reproduces it on every trial. The suite arm therefore shadows the second writer's `date` with
a command first on that writer's `PATH` that waits, bounded at ten seconds, for the first writer's
verdict file, and it starts the first writer only once the second has entered that wait, so the
losing order is forced rather than released on `go` and hoped for. That waits
without a fixed sleep, so it holds on a fast host as well as a slow one, and it took about 0.6 s a
trial here. Rows 3 and 4 also show the arm can fail: the re-read cut is its staged break.

The abandoned-guard probe pre-stages a stale lock and a guard aged two minutes. A guard younger than
one minute: busy, and the guard stays. Aged: busy, and the guard is removed. The next call: taken,
with a future `until`. A lock with no `until` aged three minutes: taken.

The interleaved abandoned-guard probe drives two writers in a fixed order. Writer 2 reads the
guard's age while it is still old. Writer 1 removes that guard and enters the break, then waits for
writer 2's verdict before its re-read compares. Writer 2 then acts on its old reading.

| abandoned-guard rule | trials with two writers proceeding |
|---|---|
| the remover takes the guard in the same call | 4 of 4 |
| the remover reports busy (S2) | 0 of 4, and none proceeds that call |

The 100-trial run printed 17 `rm` refusals reading `Permission denied`, Windows refusing to delete a
file another process held open. A removal refused inside a take leaves the path occupied, so the
`mkdir` after it fails and the writer reports busy.

### S1 — the take, under a guard

```sh
check_claim_push_lock_stale() { # lock dir -> 0 when its deadline passed, or it has none and is older than two minutes
  local lu=""; { read -r lu <"$1/until"; } 2>/dev/null || :
  case "$lu" in *[!0-9]*) lu="" ;; esac
  if [ -n "$lu" ]; then [ "$lu" -lt "$(date +%s)" ]; return; fi
  [ -n "$(find "$1" -maxdepth 0 -mmin +2 2>/dev/null)" ]
}

write_claim_push_lock() { # lock dir · owner token -> 0 taken, 1 busy
  local lk="$1" g="$1.break" broke=""
  if ! mkdir "$lk" 2>/dev/null; then
    check_claim_push_lock_stale "$lk" || return 1
    if ! mkdir "$g" 2>/dev/null; then
      if [ -n "$(find "$g" -maxdepth 0 -mmin +1 2>/dev/null)" ]; then
        rm -rf "$g"
        add_health_event "$(resolve_health_log "$ROOT")" unattended claim-push-guard-cleared "$g"
      fi
      return 1
    fi
    if ! check_claim_push_lock_stale "$lk"; then rmdir "$g" 2>/dev/null; return 1; fi
    rm -rf "$lk"
    mkdir "$lk" 2>/dev/null || { rmdir "$g" 2>/dev/null; return 1; }
    broke=1
  fi
  printf '%s\n' "$(( $(date +%s) + REMOTE_BOUND + 10 ))" >"$lk/until" 2>/dev/null || :
  printf '%s\n' "$2" >"$lk/owner" 2>/dev/null || :
  if [ -n "$broke" ]; then
    rmdir "$g" 2>/dev/null
    add_health_event "$(resolve_health_log "$ROOT")" unattended claim-push-lock-broken "$lk"
  fi
  return 0
}

remove_claim_push_lock() { # lock dir · owner token -> removes it only while its owner file reads that token
  local o=""; { read -r o <"$1/owner"; } 2>/dev/null || :
  [ -n "$2" ] && [ "$o" = "$2" ] && rm -rf "$1"
  return 0
}
```

Why the re-read under the guard is sufficient: while one writer holds the guard, nothing but the
owner's own release and a plain `mkdir` on an absent path can change the lock. A release removes
only the owner's lock, and a plain `mkdir` succeeds only where the path is empty, in which case the
breaker's `mkdir` loses and it reports busy. So a breaker never removes a lock another breaker made,
and a breaker that arrives after the winner released the guard re-reads the fresh deadline and
reports busy. A lock just made by a plain `mkdir` and not yet holding `until` reads live, because
its directory is younger than two minutes.

`write_claim` becomes, where `RUNLOG_GITDIR` is set:

```sh
lk="$RUNLOG_GITDIR/claim-push.lock"; own="$BASHPID.$RANDOM"
write_claim_push_lock "$lk" "$own" || { lk=""; busy=1; }
...
[ -z "$lk" ] || remove_claim_push_lock "$lk" "$own"
```

`lu` leaves `write_claim`'s locals. The busy branch, the marker test after the take, and the release
on every path are unchanged in order.

### S2 — what bounds a crash inside the break

A writer holds the guard for one re-read, one removal, one `mkdir` and two writes. A crash there
leaves one of three states, and each one clears:

- **The old stale lock and the guard.** The next breaker finds the guard older than one minute,
  removes it and reports busy. The call after that breaks the lock.
- **No lock and the guard.** The next plain `mkdir` takes the lock and never consults the guard. The
  guard waits for the next stale lock and is removed then.
- **A fresh lock with no `until`, and the guard.** The lock reads live for two minutes by its age,
  then stale, and the first case follows.

The remover reports busy rather than taking the guard because a remover that takes it lets two
writers in. Each acts on its own old reading of the guard's age, and the interleaved probe in this
section measured that four times in four. With the busy rule a double break needs a crash in the
window first. Then two writers must remove the abandoned guard at once, a third must take a fresh
guard between their two removals, and a fourth must take the guard while the third holds it. S5
states that residual.

### S5 — the header

The comment above `check_claim_push_lock_stale` and `write_claim_push_lock` says what the take does
and ends with:

```sh
# WHAT THIS DOES NOT CHECK: removing an abandoned guard is itself unguarded, so two writers removing
# one at once while a third takes a fresh guard between them can admit two breakers; that needs a
# writer to die or stall for a minute inside the break, then four writers in one git dir in one
# window. An owner that outlives its
# recorded deadline (no runnable `timeout -k`) is breakable while it pushes, and its own release can
# land between a breaker's re-read and its removal. Both the deadline and the age are wall-clock
# reads, so a clock stepped forward breaks a live lock. A writer in another git dir takes another lock.
```

`write_claim`'s header at `:2062` loses "is cleared and taken once" and says the take, the break and
the release are `write_claim_push_lock` and `remove_claim_push_lock`, whose header states their
limits.

### S6 — the GH37 block

The block sits after the GH36 AC14 block, inside the same region-two block. It needs no fixture
repository and no remote.

1. Extract `check_claim_push_lock_stale`, `write_claim_push_lock` and `remove_claim_push_lock` with
   `sed -n '/^<name>() {/,/^}$/p' "$SCRIPT"` into one scratch file. Each extraction that prints
   nothing fails naming that function, since an empty file would grade nothing. Set
   `REMOTE_BOUND=60` and `ROOT="$TMP"` as plain assignments. Stub `resolve_health_log` to print a
   scratch path, and `add_health_event` to append its third argument to the file it is handed. Then
   source the file. A writer's shadows of `date`, `find` and `rm` are executables in a directory put
   first on that writer's `PATH`, never shell functions: a function named for a command leads with
   no declared verb, so the lexicon leg counts it, and its verb pin may only fall.
2. **The race.** Five trials, two writers, a stale lock pre-staged in each. Writer 2's `date` is
   shadowed as §4's probe describes, writer 2 starts first, and writer 1 starts once writer 2's
   shim has marked itself waiting, so writer 2's stale read precedes writer 1's whole take. Assert
   no trial has two writers proceeding and every trial has exactly one. Then `mutate` a copy, deleting the re-read line under the guard, re-source it, rerun
   the five trials, and assert at least one trial had two. The exactly-one assertion keeps a take
   that always reports busy from passing.
3. **The bound.** A stale lock and a fresh guard: busy, and the guard stays. The guard aged two
   minutes with `touch -d "@<epoch>"`: busy, the guard is gone, and the health stub holds
   `claim-push-guard-cleared`. The next call is taken, `until` holds digits in the future, `owner`
   holds the token passed, no `.break` directory remains, and the stub holds
   `claim-push-lock-broken`. Then `mutate` the copy so an aged guard is never removed, re-source it,
   and assert the call after the aged one is still busy.
4. **The interleaving.** One trial of §4's interleaved abandoned-guard probe: no trial has two
   writers proceeding. Then `mutate` the copy so the abandoned-guard removal goes on to take the
   guard, and assert two writers proceeded. Each wait is bounded at ten seconds, as the race's is.
5. **The owner.** A lock whose `owner` reads `w-other`: `remove_claim_push_lock` with `w-me` leaves
   it. The same call with `w-other` removes it. Then `mutate` the copy so the owner comparison is
   cut, re-source it, and assert the `w-me` release removes a lock `w-other` holds.

The stubs and assignments shadow the library's health functions in the suite's own shell, so the
block re-sources `lib-unattended.sh` on its way out.

Every assertion is a `same` or `hit` line, and each `mutate` counts one, so the rise of both floors
is counted off the block's own lines.

### Inventory

| identifier | where | cell |
|---|---|---|
| `check_claim_push_lock_stale` | `tools/unattended/unattended.sh` | `sh.function` |
| `write_claim_push_lock` | `tools/unattended/unattended.sh` | `sh.function` |
| `remove_claim_push_lock` | `tools/unattended/unattended.sh` | `sh.function` |
| `own` | `write_claim`'s locals | shell local |
| `claim-push.lock.break` | the git dir | guard directory, empty |
| `owner` | inside `claim-push.lock` | file, one token |
| `claim-push-lock-broken`, `claim-push-guard-cleared` | the health log | event tokens, source `unattended` |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
on 2026-10-06 and answered OK. `take`, `clear`, `release` and `acquire` were each refused as outside
the declared table, which is why the take is a `write_` and the release a `remove_`. No check
number, leg, conf key or file is minted. No Python or JavaScript symbol is added, and the map does
not scan shell, so its symbol index does not move.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/README.md`
- `memory/gotchas/decision-re-derived-by-a-second-process.md`
- `memory/map/features/unattended-stops.md`
- every version carrier `tools/check-kit-versions.sh` pairs for the `unattended` kit, and the guides
  `tools/unattended/adopt-unattended.sh` re-adopts from them

### Rollout

One pass, in these steps, each verified by its own criteria before the next:

1. AC2's reproduction over the parent's driver, recorded before any edit.
2. `tools/unattended/unattended.sh`: S1, S3 and S4, then S5's two headers.
3. `tools/unattended/unattended.test.sh`: S6, then both floors.
4. Records: S7's class record, dossier and README paragraph, then the version bump and re-adopt.

### Alternatives rejected

Each was tested by a probe that could make it lose, and the probe's result is in the tables above.

- **C2, rename the stale lock to a private name, re-read it there, put a fresh one back.** It wins
  every two-writer trial, because the put-back restores the lock it moved by mistake. It loses 10 of
  10 when a third writer arrives while the path is empty between the rename and the put-back, and
  the put-back then fails over the newcomer's lock. Two writers then proceed. §8 F1.
- **C3, `flock`.** It releases on process death, so it would need no staleness at all. It is absent
  from node `a`'s Git Bash, and the turnstile's own header records the same. §8 F1.
- **C4, the turnstile's ticket queue.** It is another kit's code, which shared invariant 2 forbids
  calling. Its reap path is the same unguarded removal, filed as `TOOL-aReapedTicket-4` and still
  OPEN, so reusing it would import this defect rather than close it. §8 F1.
- **The abandoned-guard remover takes the guard.** It loses 4 of 4 in the interleaved probe. §8 F2.
- **The release under the guard.** It closes the owner's release window, but every release then
  needs the guard. A guard held by a breaker, or abandoned, would leave a live-looking lock in place
  until its deadline, and every claim push and landing in that git dir would wait for it. §8 F3.

## 5. Production-readiness checklist

- security — Closes a window in which two claim pushes in one git dir proceed together, and with them
  the verdict-file erasure unit 36's lock prevents. No credential, endpoint, ref or new surface. The
  guard and `owner` live in the git dir beside the lock, and `owner` carries a pid and a random
  number, nothing identifying.
- perf / scale — The common path adds one builtin write of `owner` at the take and one builtin read
  at the release, and no process spawn. The break path adds two `mkdir`/`rmdir` spawns, one re-read,
  and one health append that spawns git once, all off the common path. The new arms cost about 10 s
  on node `a`, most of it the two five-trial races.
- error / empty / loading states — A busy lock, a busy guard, a guard young enough to stay and a lost
  re-make each report busy, and `write_claim` returns its existing not-completed code with its
  existing reason. A refused `rm -rf` on Windows makes the re-make fail, which reports busy. An
  `owner` that failed to write leaves the lock to its deadline, which the next breaker breaks.
- observability — Two new health events, `claim-push-lock-broken` and `claim-push-guard-cleared`,
  counted by the orientation card's `health —` line. No new stdout line.
- risks — Edits to `unattended.sh` shift lines under the install-prefix waivers, which are
  line-keyed, so the builder reads that leg's verdict and re-keys any moved waiver. The race arm
  depends on a `PATH` shim of `date` being found from inside a command substitution, which holds
  because assigning `PATH` clears bash's command hash. The
  arm's waits are bounded, so a stuck writer ends its trial rather than the suite.
- testing — Every new assertion is observed red on its staged break before it lands. AC2 reproduces
  the defect on the parent's driver. The suite runs once at VERIFYING, at the main loop.
- migration — None. A lock left by unit 36's code has no `owner`, so its writer's own release, which
  is still unit 36's code in that process, removes it as before. A new writer treats it as any lock.
- user docs — The kit README's health-log paragraph and the two record files.

## 6. Acceptance criteria

Criteria naming a slice run it in the session scratchpad under a name that is not a suite name. A
slice is the suite's prologue plus the block the criterion names. Each staged break is made in a
scratch copy and restored before the next criterion, which `git diff --quiet` against the pass's
commit confirms.

- **AC1** — When a slice of the driver suite runs its GH37 block at the pass's commit, the race arm's
  assertions pass: no trial has two writers proceeding and all five have exactly one. Its `mutate`
  copy with the guard's re-read deleted reports at least one trial with two.
  `grep -c "^write_claim_push_lock() {" tools/unattended/unattended.sh` prints 1.
  Red when: the re-read under the guard is cut, so two writers proceed and the arm's first assertion
  FAILs.
- **AC2** — When §4's race harness, rebuilt in the scratchpad, runs five trials with the lagging
  second writer over the lock block of `tools/unattended/unattended.sh` as `git show` prints it at
  the pass's parent, two writers proceed in at least one trial. Over `write_claim_push_lock` extracted from the pass's
  commit, two writers proceed in none, and the acceptance ledger records both counts.
  Red when: the fixed take lets two writers proceed in any trial, or the parent's block shows none,
  which would mean the harness cannot see the race.
  figure: both counts are DERIVED at observation; §4's 10 of 10 and 0 of 10 are PINNED at `5ec5ef30`.
- **AC3** — When the GH37 bound arm runs in the same slice, a fresh guard leaves the call busy and the
  guard in place. A guard aged two minutes leaves the call busy, removes the guard and logs
  `claim-push-guard-cleared` to the health stub. The next call is taken, and its lock holds a future
  `until` and the passed token in `owner`, with no `claim-push.lock.break` directory left and
  `claim-push-lock-broken` logged. Its `mutate` copy that never removes an aged guard leaves the
  call after the aged one busy.
  Red when: an aged guard refuses every later call, so the next call is still busy.
- **AC4** — When the GH37 interleaving arm runs in the same slice, no trial has two writers
  proceeding. Its `mutate` copy, whose abandoned-guard removal goes on to `mkdir` the guard, reports
  two.
  Red when: the remover takes the guard in the same call.
- **AC5** — When the GH37 owner arm runs in the same slice, `remove_claim_push_lock` with a token
  other than the one `owner` holds leaves the lock directory, and with the held token removes it.
  Its `mutate` copy with the owner comparison cut removes the lock on the foreign release.
  Red when: the owner comparison is cut from a scratch copy, so the foreign release removes the lock.
- **AC6** — When the comment block above `check_claim_push_lock_stale` is printed with
  `awk '/^#/ { b = b $0 "\n"; next } /^check_claim_push_lock_stale\(\)/ { printf "%s", b; exit } { b = "" }' tools/unattended/unattended.sh`,
  it carries `WHAT THIS DOES NOT CHECK:` and the phrases `abandoned guard`, `outlives`, `clock` and
  `another git dir`. `grep -c "cleared and taken once" tools/unattended/unattended.sh` prints 0, and
  `grep -c "claim-push-guard-cleared" tools/unattended/README.md` prints at least 1.
  Red when: the header is silent on any of the four gaps, or the README omits an event.
- **AC7** — When a slice of the driver suite runs its GH32 AC6 and GH36 AC14 blocks at the pass's
  commit, every assertion keeps its verdict: a live lock skips the beat naming `claim-push.lock`, an
  expired lock is broken and the claim renewed with no lock directory left, and a write the marker
  refused leaves no lock. A slice of the lander suite through its cases 2d and 2e still prints
  `waited` on a live lock and `proceeding past a claim-push lock` on an expired one.
  Red when: the lander reads `owner` as a deadline, or a refused write leaves its lock.
- **AC8** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, its `unattended` line reads `clean` at the bumped version.
  `bash tools/check-kit-versions.sh` and `bash tools/unattended/adopt-unattended.sh --check` each
  exit 0.
  Red when: the kit's shipped bytes moved and its version did not, or an installed guide differs from
  its template.
  figure: the version is DERIVED from the pass's parent at observation.
- **AC9** — When `git diff <the pass's parent> -- tools/unattended/unattended.test.sh` is filtered by
  `grep -cE '^\+ *(hit|miss|same|mutate) '`, the count equals the rise of `FLOOR_ASSERTIONS` and of
  `FLOOR_SHARD_2`, and their comments name this unit. `python tools/memory-tree/gotchas.py --check`
  exits 0, `grep -c "GH37" memory/gotchas/decision-re-derived-by-a-second-process.md` prints at least
  1, and every line of `python tools/codebase-map/test_codebase_map.py` reads `ok`.
  Red when: a floor rises by a number the block does not carry, or the class record names no gate
  for this instance.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `gotchas selftest` · `push-main self-test` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `line length` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · GH37: the two-writer race, the abandoned-guard bound, the interleaved abandoned guard and the owner check; each staged break through mutate as §6 names it · FLOOR_ASSERTIONS and FLOOR_SHARD_2, by the assertions added

The driver suite is not on the bar. A pass runs every criterion above directly, through slices, and
the main loop runs the suite once at VERIFYING.

## 8. Open questions

- **F1 — What makes breaking a stale lock a step only one writer can win?** The options: a guard
  directory taken with `mkdir`, under which the breaker re-reads (C1); a rename of the stale lock to
  a private name, a re-read there, and a put-back when it was fresh (C2); `flock` (C3); the
  turnstile's ticket queue (C4). The probes in §4 decide between C1 and C2: C2 loses 10 of 10 to a
  third writer arriving in the gap its rename opens, and C1 holds in every arrangement measured. C3
  fails veto 2, a dependency absent on node `a`. C4 fails veto 2, another kit's code, and carries
  the same defect as an OPEN ask.
  RESOLVED (agent, 2026-10-06, delegated): C1, the guard directory `<lock dir>.break` with a re-read
  under it.
- **F2 — What bounds a guard abandoned by a crash?** The options: (a) a guard older than one minute is
  removed by the writer that finds it, which reports busy; (b) the same, but the remover takes the
  guard; (c) a pid written into the guard and tested for liveness; (d) no bound. (d) wedges every
  later breaker, which the brief forbids. (b) loses 4 of 4 in the interleaved probe. (c) still needs
  (a) for a crash between the guard's `mkdir` and the pid write, which is the window it would exist
  for, so it is (a) plus a read and a process probe.
  RESOLVED (agent, 2026-10-06, delegated): (a), one minute, the remover reporting busy.
- **F3 — Does the release check that the lock is still its own?** The options: no check, stated as a
  gap; an `owner` token compared before the removal, the turnstile's nonce pattern; or the release
  taken under the guard. The token closes the release that removes a breaker's fresh lock, except in
  the read-to-removal window, and costs one builtin read. Under the guard every release depends on
  the guard being free, and a held or abandoned guard leaves a live-looking lock to its deadline.
  Neither trips a veto, and the token leaves the smaller follow-up.
  RESOLVED (agent, 2026-10-06, delegated): the `owner` token, compared by `remove_claim_push_lock`.
- **F4 — Are the break and the guard removal self-heals the health log records?** I3 says every
  automatic self-heal appends one line, and both recover from a crashed writer. Logging costs one git
  spawn on the break path alone. Leaving them silent keeps the class the health log exists to end.
  No veto trips, since the health log and its writer are this kit's own surface.
  RESOLVED (agent, 2026-10-06, delegated): log both, after the guard is released.
- **FACT-QUESTION · F5 — Does the double take reproduce on the current code on node a, and under what
  arrangement?** Probe: §4's harness over `:2078-2089` extracted verbatim at `5ec5ef30`. Liveness:
  the lagging-writer arrangement produced 20 of 20 and 10 of 10, so the probe can return a positive.
  Observation: 0 of 100 released together, 20 of 20 with a 1 s lag, 10 of 10 with the verdict wait.
  RESOLVED (agent, 2026-10-06, delegated): it reproduces whenever one writer lags by about one spawn.
  The arm uses the verdict wait with five trials, since every lagging trial measured showed it.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the unit 37 spec brief, grounded at `5ec5ef30` against
  unit 36's lock, with the race, guard and interleaving probes run on node `a`.
- rev-2 · 2026-10-06 · at build: §2's S6, "each arm's staged break goes through `mutate`", and §4's
  S6 disagreed, the latter giving the bound and owner arms no break, so both now carry one in the
  suite, named in AC3 and AC5. The interleaving arm's waits go from two seconds to ten, the race's bound: a two
  second wait that fires under a loaded bar breaks the forced order and reds the `mutate` assertion
  with no defect present. The block re-sources the kit library after its stubs.
- rev-3 · 2026-10-06 · at build, S6 in §4 and the risks line of §5: the writers' shadows of `date`, `find` and `rm` become executables
  on a per-writer `PATH`. Written as nested shell functions, as rev-1 had them, the lexicon leg read
  `date`, `find`, `rm` and a second `date` as four verb offenders, 1068 against its pin of 1064.
  The race arm no longer releases its writers together on `go`: writer 1 starts once writer 2's
  shim marks itself waiting, so writer 2's stale read precedes writer 1's whole take by
  construction rather than by the fork order of two background starts.

## 10. Reuse audit

The map probes were these two:

```bash
python tools/codebase-map/reuse_lookup.py "break a stale lock directory so only one process wins"
python tools/codebase-map/reuse_lookup.py "a stale lock left by a crashed writer that every later writer must not wedge on"
```

Both `reuse_lookup.py` probes ranked name-stem neighbours only, `StaleHeader`, `write` and
`write_text`, and both printed
`unscanned layers: .sh`. Their miss is therefore no evidence about the driver or the lander, which
are shell, and those were read by hand. A `git grep` for `mkdir` locks over the shell kits found two:
this lock and the run-gates turnstile's beacon. The first probe surfaced the turnstile's decisions,
`TOOL-aPacedTurnstile-1` onward. The seams extended are `write_claim`'s lock block, which becomes
`write_claim_push_lock`, and its release line, which becomes `remove_claim_push_lock`. The staleness
rule moves unchanged into `check_claim_push_lock_stale`. The suite's GH36 AC14 block and the
extracted-function pattern of its `run_bounded` arms are extended in place, and `add_health_event`
is reused for S4. The owner token follows `ts_release`'s nonce pattern in
`tools/run-gates/run-gates.sh` without calling it, since it is another kit's code.

Recall surfaced `TOOL-aReapedTicket-4` first, the same race in the turnstile's reap, still OPEN.
Its candidate fix is a rename to a unique name and then a delete. §4's measurement says a rename
alone is no re-read, and a rename with a re-read and a put-back lost 10 of 10 to a third writer. It
also surfaced unit 36's spec and acceptance ledger and the rescope row in the run-state file that
adopted this unit. Recall and the code disagreed once: unit 36's spec says a stale lock "is cleared
and `mkdir` tried once more", which reads as safe, and the code does exactly that with no re-read
between. §4 follows the code.

Recall terms used: claim-push.lock stale lock mkdir rm-rf break nonce release turnstile beacon reap check-then-act wedge

The question passed with them: "how is a stale lock broken safely when two processes find it at
once, and what bounds a crash inside the break".
