# TOOL-aPiecewiseGrade-6 — one per-slug lock in the sidecar holds a dispatch's spec-token state from the start half to the end of the read half

**Status:** SPECCED · rev-1 · 2026-11-16 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-6-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-6-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-6-review-brief.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-6-review-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Two `--dispatch` calls of one slug in one worktree can overlap, and the second's start half then
sweeps the first's next cache generation and its input record while the first still depends on them
(item 1 of `2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1`). This unit puts every
write to a slug's spec-token state under one lock directory in the sidecar, taken at the start half
and given back at the end of the read half. A dispatch that cannot take it grades with the cache off
and records nothing. The lock is the claim-push lock's primitive, extracted into a factory both
callers share.

## 2. Scope (IN)

- **S1** — The three claim-push lock functions become one factory, `check_dir_lock_stale`,
  `write_dir_lock` and `remove_dir_lock`. The factory takes the hold's length in seconds and a
  health-event stem as arguments. `write_claim` calls it with `$(( REMOTE_BOUND + 10 ))` and the stem
  `claim-push`, so its `until` bytes and its two event names do not change. The old names
  `check_claim_push_lock_stale`, `write_claim_push_lock` and `remove_claim_push_lock` are replaced by
  the factory's names. Observed by AC6 and AC9.
  **Readers:**
  by name: `tools/unattended/unattended.sh`, at `write_claim` and the header comments; `tools/unattended/unattended.test.sh`, the GH37 block's extraction loop, its calls, one `mutate` pattern and its `unset -f` line; `memory/map/generated/symbols.json`, three symbol ids.
  by value: NO VALUE READERS — a function name carries no value that any reader compares or counts.
- **S2** — The start half takes `spec-tokens.<slug>.lock` under the sidecar root before its skip
  lookup, with a hold of `GATE_BOUND` plus 60 seconds and the stem `spec-tokens`. Holding it, the
  start half does everything it does today. Observed by AC1 and AC3.
- **S3** — A start half that cannot take the lock sets `ST_STATE` to `busy`. It makes no lookup, reads
  no tree state, and leaves the input record, the sweep and `mktemp` alone. It starts the checker with
  `SPEC_TOKENS_INPUTS`, `SPEC_TOKENS_CACHE` and `SPEC_TOKENS_CACHE_NEXT` all empty. The read half
  prints one new line, grades as today, and records no key and no name. Observed by AC2.
- **S4** — The read half gives the lock back on each of its five returns after the skip decision,
  and `remove_spec_token_check` gives it back after it waits for the checker. A busy run holds nothing
  to give back. Observed by AC4.
- **S5** — Every line `--dispatch` prints today keeps its bytes. The busy line in §4 is the one line
  added. Observed by AC5.
- **S6** — The new code adds no `fail` call, no `exit 1`, no command substitution and no `mv`, so the
  harness-arms leg and the four shell-hygiene legs have no new site to admit. Observed by AC7.
- **S7** — The verbs guide states the lock in both copies, which stay byte-identical. The kit README
  names the two new health events. Observed by AC8.
- **S8** — The codebase map's symbols index is regenerated for the three renamed functions. Observed
  by AC9.

## 3. Non-goals (OUT)

- No change to a verdict, a refusal line, the summary line or an exit status of `--dispatch` or the
  checker.
- No edit to `tools/check-spec-tokens.py`, which TOOL-aPiecewiseGrade-5 writes concurrently.
- No edit to a CLOSED spec of this build. This unit is the correction to TOOL-aPiecewiseGrade-2.
- No move of the start half after the claim check, and no lock across worktrees. Each worktree has
  its own sidecar root, so two worktrees never share this state.
- No change to the claim-push lock's behaviour: its `until`, its staleness rule, its guard and its
  event names keep their bytes.
- No owner pid in the lock. That is F1's option (b), not built unless the owner picks it.
- No row raised in any shrink-only registry, and no kit version bump by hand.

### Edges

- **consumes-from** external — TOOL-aPiecewiseGrade-2's per-slug cache, CLOSED at `4cdddad5c`: the name file, the generations, the sweep and the two halves this lock wraps
- **consumes-from** external — TOOL-aGraftedHelix-37's claim-push lock, landed: the `mkdir` lock with `until`, `owner` and the `.break` guard that S1 extracts

## 4. Design

### What the code does today

Read at HEAD `fccef94ef`, where the driver's blob is `e57e48e3` (the review's), the suite's
`9c0c1e5e`, the library's `eb8c9250` and the verbs guide's `62c441b6`.

- `init_spec_token_check` (`tools/unattended/unattended.sh#init_spec_token_check`) resolves the sidecar
  root and sets `ST_REC` and `ST_IN` (`tools/unattended/unattended.sh@e57e48e3:14605`). It looks the key
  up and may return `skip` (`tools/unattended/unattended.sh@e57e48e3:14609`). Otherwise it reads the
  tree state and sets `ST_STATE=run` (`tools/unattended/unattended.sh@e57e48e3:14611`). Then it runs
  `rm -f "$ST_IN"` and `mkdir -p "$_stdir"` (`tools/unattended/unattended.sh@e57e48e3:14614`), sweeps
  every generation but the live one (`tools/unattended/unattended.sh@e57e48e3:14617`) and makes the
  next with `mktemp -d`. No lock is taken anywhere in it.
- `run_spec_token_check` (`tools/unattended/unattended.sh#run_spec_token_check`) copies the nine `ST_`
  globals into locals and empties them. Its returns after the skip decision are the skip line's, the
  check-49 refusal's, `[ -n "$_stat" ] || return 0`
  (`tools/unattended/unattended.sh@e57e48e3:14667`), the recorded branch's, and the final one after the
  not-recorded line (`tools/unattended/unattended.sh@e57e48e3:14691`). The recorded branch writes the
  key, writes `.live` and runs `rm -rf "$_stcache"`.
- `verb_dispatch` calls the start half at `tools/unattended/unattended.sh@e57e48e3:14986`, the read
  half at `tools/unattended/unattended.sh@e57e48e3:15078`, and the claim check after both
  (`tools/unattended/unattended.sh@e57e48e3:15107`). The two window refusals call
  `remove_spec_token_check` before `return 1`, and the suite's text arm
  (`tools/unattended/unattended.test.sh@9c0c1e5e:8115`) holds that.
- The only lock in the kit is the claim-push trio (`tools/unattended/unattended.sh#write_claim_push_lock`,
  `tools/unattended/unattended.sh#check_claim_push_lock_stale`,
  `tools/unattended/unattended.sh#remove_claim_push_lock`). The take uses `mkdir`. It writes
  `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` into `until` and the token into `owner`. It breaks a stale
  lock only under the `.break` guard, and it appends `claim-push-guard-cleared` or
  `claim-push-lock-broken` to the health log. Staleness means a passed `until`, or no `until` and an
  age over two minutes. The release removes the lock only while `owner` reads the caller's token.
  `write_claim` is its one caller (`tools/unattended/unattended.sh@e57e48e3:2618`). A grep of every
  tracked kit shell file for `mkdir` beside `lock`, and for `flock`, found no other lock.
- The suite's GH37 block extracts the trio by name with `sed` and drives it over plain directories
  (`tools/unattended/unattended.test.sh@9c0c1e5e:17991`).
- `GATE_BOUND` is the checker's bound: `init_bounded` reads `${RB_BOUND:-${GATE_BOUND:-0}}`
  (`tools/unattended/unattended.sh#init_bounded`), and `RB_BOUND` is empty at the dispatch. The conf
  reader refuses a `GATE_BOUND` of 0 (`tools/unattended/unattended.sh@e57e48e3:3187`), and the default
  is 3600 s.
- `add_health_event` accepts an event that is a lowercase token of letters, digits and dashes
  (`tools/unattended/lib-unattended.sh#add_health_event`). `check_slug_shape` admits letters, digits
  and dashes only (`tools/unattended/unattended.sh@e57e48e3:3107`), so `spec-tokens.<slug>.lock`
  cannot match another slug's glob or the generation glob `spec-tokens.<slug>.specs.*`.

### S1 — the factory

The three functions keep their bodies, renamed, with two changes to the take:

```bash
write_dir_lock() { # lock dir · owner token · seconds it may hold · health-event stem -> 0 taken, 1 busy
  ...
        add_health_event "$(resolve_health_log "$ROOT")" unattended "$4-guard-cleared" "$g"
  ...
  printf '%s\n' "$(( $EPOCHSECONDS + $3 ))" >"$lk/until" 2>/dev/null || :
  ...
    add_health_event "$(resolve_health_log "$ROOT")" unattended "$4-lock-broken" "$lk"
```

`write_claim` passes `"$(( REMOTE_BOUND + 10 ))" claim-push`, so its `until` and its event names come
out byte-identical. The header comment above the trio names both callers and keeps its "WHAT THIS
DOES NOT CHECK" paragraph. In the GH37 block, the extraction loop, each call, the `mutate` pattern
naming `check_claim_push_lock_stale`, and the `unset -f` line take the new names. Each call passes
`"$(( REMOTE_BOUND + 10 ))" claim-push`. Its assertions do not move.

### S2 and S3 — the take, and the busy branch

The start half's sidecar block becomes:

```bash
  _stdir=$(resolve_sidecar_dir) && [ -n "$_stdir" ] && ST_REC="$_stdir/spec-tokens.$1.key" && ST_IN="$_stdir/spec-tokens.$1.inputs"
  if [ -n "$ST_IN" ]; then
    mkdir -p "$_stdir" 2>/dev/null
    ST_LOCK="$_stdir/spec-tokens.$1.lock"; ST_OWN="$BASHPID.$RANDOM"
    # ponytail: a killed run's lock is broken only at its deadline; F1 (b) records the owner's pid if that window costs.
    write_dir_lock "$ST_LOCK" "$ST_OWN" "$(( ${GATE_BOUND:-0} + 60 ))" spec-tokens \
      || { ST_OWN=""; ST_REC=""; ST_IN=""; ST_STATE=busy; }
  fi
  if [ -n "$ST_REC" ] && [ -f "$ST_REC" ] && [ -f "$ST_IN" ]; then
    # the lookup, unchanged
  fi
  if [ "$ST_STATE" != busy ]; then
    ST_TREE=$(read_tree_state "$ST_PY") || ST_TREE=""
    ST_STATE=run
  fi
  if [ -n "$ST_IN" ]; then
    rm -f "$ST_IN" 2>/dev/null
    # the name read, the shape check, the sweep and mktemp, unchanged
  fi
```

The `mkdir -p` moves up from the run block, because the lock's own `mkdir` needs the sidecar root to
exist. With `ST_REC` and `ST_IN` empty, a busy run skips the lookup and the run block. So
`ST_NEXT` and `ST_CACHE` stay empty, and `init_bounded` starts the plain checker. With `ST_TREE`
empty, the read half returns before the key's write site. A busy run keeps `ST_LOCK`, for its line,
and an empty `ST_OWN`, so it can never give back a lock it does not hold.

`ST_LOCK` and `ST_OWN` join the nine globals at their declaration, at the start half's head, in
`remove_spec_token_check`, and in the read half's copy line as `_stlock=$ST_LOCK` and
`_stown=$ST_OWN`. The header comment's "nine ST_ globals" becomes eleven.

The read half prints the busy line where the fingerprint's cache-off line prints today, as its other
arm:

```bash
  if [ "$_stst" = busy ]; then
    echo "unattended: dispatch — spec-token cache off: another dispatch of $slug holds its lock, or the lock cannot be made, so the checker runs whole and records nothing: $_stlock"
  elif [ -z "$_stat" ]; then
    # the fingerprint's cache-off line, unchanged
  fi
```

The line names both causes. A failed `mkdir` that is not contention, such as an unwritable sidecar,
also lands here, and the factory cannot tell the two apart. Every other branch of the read half
treats `busy` as `run`. So the admit note and the check-49 refusal print as they do today, and the
grading is the plain run's.

### S4 — giving the lock back

`remove_dir_lock "$_stlock" "$_stown"` goes before each of the read half's five returns after the
skip decision:

- the skip line's return;
- the check-49 refusal's `return 1`, after the `fail` line;
- `[ -n "$_stat" ] || return 0`, which becomes a braced group;
- the recorded branch's return, after the `.live` write and the old generation's `rm -rf`;
- the final return, after the not-recorded line.

`remove_spec_token_check` calls `remove_dir_lock "${ST_LOCK:-}" "${ST_OWN:-}"` after its
`read_bounded` and before it empties the globals. With an empty path and token, the release reads no
owner and removes nothing, so the blank, missing and nopython returns need no call. The window
refusals in `verb_dispatch` already route through `remove_spec_token_check`, so their lines do not
move.

### Why this closes item 1

Every write to a slug's state now happens inside one held lock: the `.inputs` removal, the checker's
writes into `.inputs` and the next generation, the key write, the `.live` write, the sweep and the
old generation's `rm -rf`. A second start half of the same slug cannot take the lock, so it sweeps
nothing and removes nothing. Its checker reads no cache and writes no record. The first run's read
half then names its own generation as it would alone.

The review also noted that the sweep runs before the claim check. A caller with no claim now sweeps
only when no dispatch of the slug in this worktree holds the lock. So it sweeps only generations no
running dispatch depends on. Its later check-108 refusal leaves state that a real grading wrote.

### Staleness, and a run killed partway

The lock's `until` is the take's time plus `GATE_BOUND` plus 60 seconds (PINNED literal, chosen not
measured). The checker starts after the take and is killed at `GATE_BOUND` plus the 5-second `-k`
grace, so a live holder's `until` passes after its checker is bounded out. The 60 seconds also cover
the lookup's replay before the checker and the key's replay after it. Staleness is the factory's
rule, unchanged: a passed `until`, or no `until` and an age over two minutes.

| killed | what it leaves | what the next dispatch of the slug does |
|---|---|---|
| between the take's `mkdir` and its `until` write | a lock with no `until` | runs busy until the lock is two minutes old, then breaks it |
| anywhere between the take and the release | a lock with `until`, maybe a next generation, maybe an `.inputs` | runs busy, grading correctly, until `until` passes. Then it breaks the lock under the guard, logs `spec-tokens-lock-broken`, and sweeps what the killed run left |
| a surviving checker (the driver died, its child did not) | a process still writing the next generation and `.inputs` | where `timeout -k` runs, that child is killed at `GATE_BOUND` plus 5 s from its start, before `until` passes, so no breaker races it |
| inside the release's `rm -rf` | part of a lock directory, maybe without `owner` or `until` | the age rule breaks it after two minutes |

### What the design does not check

- **A holder that outlives `until`.** On a host with no runnable `timeout -k`, the checker runs
  unbounded and can outlive the deadline. The lock is then breakable while held, and the overlap the
  lock closes reopens for that window. A clock stepped forward does the same. Both are the
  claim-push lock's own stated limits.
- **The factory's abandoned-guard gap**, carried from TOOL-aGraftedHelix-37's header: two writers
  removing one abandoned guard while a third takes a fresh one can admit two breakers.
- **A killed run's window.** For up to `GATE_BOUND` plus 60 s after a kill, every dispatch of that
  slug in that worktree runs whole and prints the busy line. Findings stay correct. F1 is the choice
  of whether that cost is worth a pid check.
- **A driver from before this unit** takes no lock, so it still races a new one in the same worktree.
  Every dispatch in a worktree runs the one installed driver.
- **The busy line's cause.** It cannot say whether the lock was held or could not be made.

### The pass probe, `$SCRATCH/pg6.sh`

The probe builds a fixture repository at `$TEMP/pg6`, as unit 2's `pg2.sh` does. The repository holds
the checker, the memory-tree kit and the run-gates fingerprint script, copied into its tool root. The
probe sources the built driver and loads its conf. The seed has two clean live specs in build `tA`, a
`tB` spec that reds in another build, and an empty waiver file. `D` is the sidecar root, `N` is
`$D/spec-tokens.tA.live`, `K` is `$D/spec-tokens.tA.key`, `I` is `$D/spec-tokens.tA.inputs`, `L` is
`$D/spec-tokens.tA.lock`, and `H` is the health log `resolve_health_log` answers. One admitted call
primes the cache before the first step.

| step | what happens | the line it prints |
|---|---|---|
| `overlap` | `K` removed. In a subshell, `init_spec_token_check tA` runs, then the probe polls for the started checker's `up.end` stamp (600 polls of 0.1 s). A nested subshell then runs `run_spec_token_check tA` whole, its output captured. Then the first subshell runs `run_spec_token_check tA` | `overlap second-busy <n> next <0|1> inputs <0|1> named-first <0|1>` |
| `busy` | `K` removed, and `L` planted with `until` 600 s ahead and `owner` `w-other`. Then the call | `busy said <n> admitted <n> key <0|1> kept <0|1> held <0|1>` |
| `busyred` | `L` still planted, a `tA` spec made to red, then the call. Then the red edit and `L` are undone | `busyred refused <n> held <0|1>` |
| `stale` | `K` removed, and `L` planted with `until` 5 s past and `owner` `w-dead`. Then the call | `stale said <n> key <0|1> named <0|1> lock <0|1> event <n>` |
| `release` | five calls, each followed by a test for `L`: a repeat call over the same tree (skip), a `tA` spec made to red (refusal), unit 2's `moved` stub (not recorded), `init_spec_token_check tA` then `remove_spec_token_check` (window refusal), and the fingerprint script moved aside (cache off) | `release skip <0|1> refused <0|1> moved <0|1> window <0|1> cacheoff <0|1>` |

In the `overlap` step, `second-busy` counts the busy line in the nested call's output. `next` is 1
when the first start half's `ST_NEXT` directory still exists after the nested call. `inputs` is 1
when `I` exists after the nested call. `named-first` is 1 when `N` names that same directory's base
name after the first read half. The checker's stamp is polled so that `I` exists before the second
start half runs. Without the stamp, whether the second sweep could reach `I` would depend on timing.

In the `busy` step, `said` counts the busy line. `admitted` counts the admit note naming
`spec-tokens: memory/builds/tB/`. `key` is 1 when `K` exists. `kept` is 1 when `N`, `I` and the
listing of `$D/spec-tokens.tA.specs.*` hash the same before and after the call. `held` is 1 when
`L/owner` still reads `w-other`. In `busyred`, `refused` counts the line
`--dispatch refuses: the declared spec-token checker reds over the live tree`. In `stale`, `named` is
1 when `N` holds a well-formed generation name that names a directory, `lock` is 1 when `L` exists
after the call, and `event` counts `spec-tokens-lock-broken` in `H`. In `release`, each field is 1
when `L` is absent after its call.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `write_dir_lock` | shell function, the factory's take | `--suggest write_dir_lock --as sh.function`: OK, leads with `write` |
| `remove_dir_lock` | shell function, the factory's release | `--suggest remove_dir_lock --as sh.function`: OK, leads with `remove` |
| `check_dir_lock_stale` | shell function, the factory's staleness rule | `--suggest check_dir_lock_stale --as sh.function`: OK, leads with `check` |
| `ST_LOCK` and `ST_OWN` | the tenth and eleventh globals between the two halves | no declared cell for a shell global |
| `_stlock` and `_stown` | locals of the read half | no declared cell for a shell local |
| `busy` | a new `ST_STATE` value | no declared cell |
| `spec-tokens.<slug>.lock`, with its guard `spec-tokens.<slug>.lock.break` | sidecar lock directory | no declared cell |
| `spec-tokens-lock-broken` and `spec-tokens-guard-cleared` | health events, composed from the stem | `add_health_event`'s lowercase-token rule |

No conf key, check number or refusal line is minted. The three suggest runs were made at `fccef94ef`
with `python tools/lexicon/lexicon.py`, and a `git grep` for the three names found no existing site.

### Docs, and what the change owes beyond the code

- The verbs guide, in both copies. After the sentence ending "goes live only where the key is
  recorded." in `tools/unattended/VERBS.template.md`
  (`tools/unattended/VERBS.template.md@62c441b6:262`), and identically in
  `memory/guides/UNATTENDED-VERBS.md`, add:

  ```
  One dispatch of a build at a time holds that cache, under a lock in the sidecar root; a dispatch
  that cannot take the lock says so, runs the checker whole and records nothing.
  ```

  The guide already exceeds its byte budget in warn mode, so this adds to a warning and reds
  nothing. The sentence is the shortest one that states the new line's meaning.
- `tools/unattended/README.md`, at the health-event sentence naming `claim-push-guard-cleared`
  (`tools/unattended/README.md@4d2c0eef:283`), add that the driver appends `spec-tokens-lock-broken` or
  `spec-tokens-guard-cleared` for a dispatch's `spec-tokens.<slug>.lock` (TOOL-aPiecewiseGrade-6).
- The codebase map: `python tools/codebase-map/gen_map.py --write` renders three symbol ids under
  their new names. The `unattended` dossier names no moved path.
- No `help/` page names the dispatch cache or the claim-push lock, grepped at `fccef94ef`.
- The kit epoch leg sees shipped bytes move, and the lander's mint moves the version.
- No fork-ceiling row moves. The registry holds no `--dispatch` row, and `--status` reaches neither
  lock. A dispatch spends two more processes, the take's `mkdir` and the release's `rm -rf`, counted
  from the code (DERIVED, re-derived by reading the two halves).

### Rollout

The builder finds each site by its text, since every cited line moves: the trio's three definitions,
`write_claim`'s two lock lines, the start half's sidecar block, the read half's copy line and its five
returns, `remove_spec_token_check`, and the globals' declaration. The suite's new arms sit after unit
2's block, before step f deletes the fingerprint script. The driver suite's assertion floor rises by
the count of new assertions, which the close confirms from a real run.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Call the claim-push trio as it stands.** Its deadline is `REMOTE_BOUND` plus 10 s, which is 70 s,
  and a checker run near 69 s would see its lock broken mid-run. Its event names would also misname
  the lock.
- **A second lock written beside it for spec tokens.** A copy of the first, which the charter's
  `[reuse]` rule forbids at a kind's second instance.
- **Move the start half after the claim check.** The window comment above the start half says a
  write moved above the read moves the tree state the read half compares. And sibling passes of one
  run hold the same claim, so the claim never serialises them.
- **Sweep only generations older than the name file.** It protects the next generation but not the
  `.inputs` record, the key or the `.live` write, and it adds a second clock rule to the sweep.
- **Make a busy run wait for the lock.** A dispatch would block for up to a whole checker run, and the
  cache-off run costs the same time with no wait.
- **Let a busy run look the key up.** A skip read beside a holder could read a key and a record from
  two different runs. Running whole is correct with no read.
- **A helper for the release.** The release is one call to the factory at each site.

## 5. Production-readiness checklist

- security — the lock sits in the worktree's git dir beside the key and the record. Its path comes from
  the sidecar root and a slug `check_slug` validated, never from a file. Its `owner` token makes a
  release a no-op for anyone but the taker, so a run whose lock was broken never removes the breaker's
  lock. A caller with no claim deletes only state no running dispatch depends on.
- perf / scale — two more processes per dispatch, the take's `mkdir` and the release's `rm -rf`
  (DERIVED from the code). A busy dispatch costs one whole checker run, about 43 s (PINNED 65111499e,
  the review's figure), in place of an incremental run.
- error / empty / loading states — no sidecar root means no lock and the cache off, as today. A lock
  that cannot be made is the busy branch. A failed release leaves a lock that goes stale at its
  deadline.
- observability — the busy line names the lock's path. A broken lock and a cleared guard each append
  a health event.
- risks — a release left off one path would hold the lock until its deadline, and every dispatch
  meanwhile runs whole. AC4 observes all five paths and the window refusal.
- testing — the pass probe above, and the driver suite's new arms observed RED then GREEN at the
  close.
- migration — none. The first dispatch after install makes the lock and gives it back.
- user docs — the verbs guide in both copies, and the kit README's health-event sentence.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg6.sh"`, described in §4, removed after the
pass.

- **AC1** — When `bash "$SCRATCH/pg6.sh"` runs, it prints
  `overlap second-busy 1 next 1 inputs 1 named-first 1`.
  Red when: the start half takes no lock, or ignores a failed take, so the second start half sweeps
  the first's next generation and removes its `.inputs`, and the first read half names nothing.
- **AC2** — When `bash "$SCRATCH/pg6.sh"` runs, it prints `busy said 1 admitted 1 key 0 kept 1 held 1`
  and `busyred refused 1 held 1`.
  Red when: a busy run still arms the cache or records a key, so `key` or `kept` moves; it gives back
  a lock it does not hold, so `held` reads 0; or it stops grading, so `admitted` or `refused` reads 0.
- **AC3** — When `bash "$SCRATCH/pg6.sh"` runs, it prints `stale said 0 key 1 named 1 lock 0 event 1`.
  Red when: the take never breaks a lock whose `until` has passed, so the run prints the busy line and
  records nothing.
- **AC4** — When `bash "$SCRATCH/pg6.sh"` runs, it prints
  `release skip 1 refused 1 moved 1 window 1 cacheoff 1`.
  Red when: any of the read half's returns after the skip decision, or `remove_spec_token_check`, does
  not give the lock back.
- **AC5** — When `git diff -U0 fccef94ef -- tools/unattended/unattended.sh | grep -cE '^-.*(echo "unattended: dispatch|fail 49 |WC_WHY=)'`
  runs, it prints 0, and the same with `^\+` prints 1, the busy line.
  Red when: an existing dispatch line, check-49 refusal or claim-push reason is edited, or a second
  line is added.
  fixture: the diff base is the HEAD this spec was written at, and no other unit of the build edits
  the driver.
- **AC6** — When `grep -c 'claim_push_lock' tools/unattended/unattended.sh tools/unattended/unattended.test.sh`
  runs, both counts are 0. When `grep -n 'write_dir_lock "' tools/unattended/unattended.sh` runs, it
  names two call sites, one passing `"$(( REMOTE_BOUND + 10 ))" claim-push` and one passing the stem
  `spec-tokens`.
  Red when: an old name survives, or the claim-push caller passes another hold or stem, so its `until`
  or its event names move.
- **AC7** — When `git diff -U0 fccef94ef -- tools/unattended/unattended.sh | grep -E '^\+' | grep -E '\$\([^(]|fail [0-9]|exit 1|(^|[^a-z_])mv ' | grep -vc 'add_health_event "\$(resolve_health_log "\$ROOT")"'`
  runs, it prints 0.
  Red when: the change adds a command substitution, a `fail` call, an `exit 1` or an `mv`, each a site
  the hygiene or harness-arms legs would have to admit.
- **AC8** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs, it
  prints nothing. `grep -c 'One dispatch of a build at a time holds that cache' memory/guides/UNATTENDED-VERBS.md`
  prints 1, and `grep -c 'spec-tokens-lock-broken' tools/unattended/README.md` prints 1.
  Red when: one copy is edited without its twin, or either sentence is missing.
- **AC9** — When `python tools/codebase-map/gen_map.py --check` runs, it exits 0, and
  `grep -c '"id": "write_dir_lock"' memory/map/generated/symbols.json` prints 1.
  Red when: the index still carries the claim-push names, or it was not regenerated.

## 7. Gates

`unattended kit gate` · `spec-tokens self-test` · `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · after unit 2's block: the overlap of two same-slug start halves with the first's next generation, `.inputs` and name surviving; a planted live lock running the cache off, grading, recording nothing and holding the planted lock; a planted lock past its deadline broken and logged; and the lock absent after each of the five paths out. Staged RED at the close by ignoring the take's status, by dropping the busy branch's `ST_STATE`, by making `check_dir_lock_stale` answer busy, and by cutting the skip return's release · the driver suite's assertion floor, raised by the count of new assertions, which the close confirms

New arm: tools/unattended/unattended.test.sh · covers AC6 · the GH37 block moved onto the factory's names, extracting `write_dir_lock` and passing `"$(( REMOTE_BOUND + 10 ))" claim-push`; its existing staged breaks re-run unchanged, and it is staged RED by passing a hold of 0, which reds its "until is a deadline in the future" assertion · none

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but the
spec-token checker's `--spec` over this file and the memory hygiene gate.

## 8. Open questions

- **F1 — How is a killed run's lock judged stale?**
  Options:
  - (a) By the factory's rule, unchanged: `until` passed, or no `until` and an age over two minutes,
    with `until` set to `GATE_BOUND` plus 60 s. No new code in the factory. A surviving checker is
    bounded out before `until` passes, so no breaker races it. The cost is that for up to
    `GATE_BOUND` plus 60 s after a kill, which is 3660 s at the default, every dispatch of that slug
    in that worktree runs whole, about 43 s each, and prints the busy line.
  - (b) As (a), or when the owner is gone. The take also writes a `pid` file holding `$BASHPID` and
    its `read_proc_token` token, and `check_dir_lock_stale` reads a lock stale when
    `check_proc_gone` says that process is gone. The claim-push lock writes no `pid` file, so its rule
    does not move. A killed run's lock breaks at the next dispatch. But a checker that outlived its
    driver keeps writing `.inputs` and its generation beside the breaker's run, so the file would also
    have to hold the checker wrapper's pid from `ST_HANDLE`, and the rule would read the lock stale
    only when both are gone. That costs one more write and one more check.
  Recommendation: (a). It is the existing rule, it is safe against a surviving checker, and its cost
  is visible on every dispatch it touches and lands only after a kill. The `ponytail:` comment at the
  take names (b) as the upgrade path.

## 9. Revision log

- rev-1 · 2026-11-16 · initial draft from brief `2026-11-16-prompt-TOOL-aPiecewiseGrade-6-1-spec-writer`,
  the owner's "Promote, build now" on item 1 of
  `2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1`, grounded at `fccef94ef` (driver blob
  `e57e48e3`).

## 10. Reuse audit

The seam this unit extends is the claim-push lock, `write_claim_push_lock`,
`check_claim_push_lock_stale` and `remove_claim_push_lock` in `tools/unattended/unattended.sh`. It is
the kit's only lock, and this unit extracts it as the factory at its second instance. The other seams
are `run_spec_token_check` and its start half, at the sidecar block and the five returns; the `ST_`
globals, which carry two more; `resolve_sidecar_dir`, the one spelling of the sidecar root; and
`add_health_event`, which the factory already calls. `tools/codebase-map/reuse_lookup.py` for "take
a directory lock with an owner token and a deadline, and break a stale lock left by a killed run"
ranked generic name stems only (`run`, `run_git`, `resolve_prefix_token`), and its one `lock` hit,
`read_lock` in `tools/playbook/instruction_units.py`, reads a pin file and holds nothing. So the seam
was found by a `git grep` of the kit's shell files for `mkdir` beside `lock` and for `flock`. Recall's
top hits were TOOL-aPiecewiseGrade-2, the cache this lock wraps, the review item, and
TOOL-aGraftedHelix-37, the lock's own break rule.

Recall terms used: `python tools/memory-recall/query.py "serialise two same-slug dispatches so one start half never sweeps another run's cache generation" --terms "lock mkdir owner deadline stale break guard claim-push sweep generation sidecar dispatch"`
