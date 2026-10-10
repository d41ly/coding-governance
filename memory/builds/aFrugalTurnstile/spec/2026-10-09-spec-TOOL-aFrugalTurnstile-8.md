# TOOL-aFrugalTurnstile-8 — push-main starts the post-merge bar after a landing where it is declared

**Status:** CLOSED · rev-2 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-build-TOOL-aFrugalTurnstile-8-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-8-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md](../reviews/2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md) | diff-review | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 TOOL-aFrugalTurnstile-11 DEPL-aFrugalTurnstile-1 PLAY-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D10. After a landing push succeeds, `tools/push-main.sh` reads `GATE_POST_MERGE`
at the landed tip and, when it reads `local`, starts the post-merge full bar on that tip detached,
records where it went, and returns without waiting. That is how a landing that took the scoped bar
gets its full bar on this host, so a red can bind the next landing (design D7, D8).

## 2. Scope (IN)

- **S1** — A new function `run_post_merge` in `tools/push-main.sh`, called once after each
  successful landing push: in `cmd_land` after `write_lander_marker || exit 1`, and on the attended
  path after the same call. It is never called on a refused, unreachable, unchanged or raced push.
  Observed by AC1 and AC8.
- **S2** — The declaration is read at the LANDED tip, `git rev-parse HEAD` after the push, from
  `.githooks/gate-env.sh` at that commit by `git show`, parsed by a verbatim copy of the hook's
  `read_policy_key`. It is never read from the working tree, from R or from the environment.
  Observed by AC4, AC5 and AC6.
- **S3** — `local`: the post-merge script is found through the existing sibling-kit resolver,
  `resolve_kit_dir "$py" run-gates post-merge.sh "$self_dir"`, and started detached with all three
  standard streams redirected, so the lander's own stdout and any `$(...)` capture of it close when
  push-main exits. Observed by AC1.
- **S4** — The start is recorded twice: one stderr line naming the sha, the pid and the log, and a
  key-per-line start record in the git common dir. Observed by AC2.
- **S5** — `ci` prints one line saying remote CI owns the post-merge bar and starts nothing. A value
  outside `local ci` prints one line naming it and starts nothing. Undeclared prints nothing.
  Observed by AC3, AC4 and AC5.
- **S6** — Every failure to start is a printed line and never changes push-main's exit status: the
  landing already happened. Observed by AC7.
- **S7** — The copied `read_policy_key` is held byte-identical to the hook's by a new parity arm.
  Observed by AC9.

## 3. Non-goals (OUT)

- Retrying a failed or killed post-merge bar.
- Reading `refs/gov/bar-red`, or anything else about the post-merge verdict. The hook binds it.
- Bounding the post-merge bar's wall time. The runner it calls holds its own wall.
- Starting a post-merge bar from any path other than push-main's two landing paths. A raw
  `git push --no-verify` starts nothing, and that is the documented bypass, not a gap to close here.
- Editing `.githooks/pre-push`, `tools/process-monitor/` or the post-merge script itself.
- Gov's own `GATE_POST_MERGE` declaration. It is decided at the close, after the code exists.

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-6` — the post-merge script, its `<sha> [--remote <name>]` argument shape and its home in the run-gates kit; without it the resolver finds nothing and S6's not-started line is all a `local` landing gets
- **hands-off** external — a post-merge bar that dies before publishing a verdict, because the process-monitor reaper killed it past its age ceiling or the host rebooted, publishes neither red nor green; design D7 carries no pending state, and this unit only reports the start
- **hands-off** external — the adopter's remote-CI job that `GATE_POST_MERGE=ci` promises, which is the runbook's declaration and not this lander's

## 4. Design

### Where it goes

`run_post_merge` sits in the "SHARED BY BOTH PATHS" region of `tools/push-main.sh`, directly after
`write_lander_marker`, with the copied `read_policy_key` immediately above it. The two call sites
are the only additions to the landing paths:

```bash
    if [ "$rc" -eq 0 ]; then
      write_lander_marker || exit 1
      run_post_merge
      cls=landed
```

Both `cmd_land` and the attended loop carry exactly that block today, so the insertion is the same
line in two places. `run_post_merge` returns 0 on every path.

### The function

```bash
run_post_merge() {  # -> 0 always; one stderr line whenever the landed tip declares anything
  local tip blob pm py dir gcd log pid winpid
  tip=$(git rev-parse HEAD 2>/dev/null) || return 0
  blob=$(git show "$tip:.githooks/gate-env.sh" 2>/dev/null) || return 0
  pm=$(read_policy_key "$blob" GATE_POST_MERGE)
  case "$pm" in
    '')    return 0 ;;
    ci)    echo "push-main: post-merge bar — GATE_POST_MERGE=ci at ${tip:0:8}, so remote CI runs it; nothing started here." >&2
           return 0 ;;
    local) ;;
    *)     echo "push-main: post-merge bar NOT started — GATE_POST_MERGE at ${tip:0:8} is '$pm', outside 'local ci'." >&2
           return 0 ;;
  esac
  # resolve python, then the run-gates kit holding post-merge.sh, beside THIS script
  # resolve the common dir absolutely, as write_lander_marker does
  # start detached, all three streams redirected, record, print
}
```

The skeleton above is the contract; the three commented steps are written as the existing
functions write them. Python comes from `resolve_python`, the kit directory from `resolve_kit_dir`
followed by the file test `check_merge_losses` uses, and the common dir from the
`cd "$(git rev-parse --git-common-dir)" && pwd` form `write_lander_marker` uses.

**The start.**

```bash
  log="$gcd/gate-post-merge-${tip:0:8}.log"
  nohup "${BASH:-bash}" "$top/$dir/post-merge.sh" "$tip" --remote "$remote" </dev/null >"$log" 2>&1 &
  pid=$!
  winpid=$(cat "/proc/$pid/winpid" 2>/dev/null || true)
```

All three descriptors are redirected because a backgrounded job that keeps the caller's stdout
makes every `$(...)` capture of push-main wait for the job, and `disown` does not close the
descriptor (memory note "A backgrounded job holds the caller's stdout"). `nohup` (rev-2) keeps a
hangup sent to the lander's session from killing the child; `setsid` is not used because Git-Bash
on node a ships none, measured 2026-10-10 by `command -v setsid`. The child's argv carries
the absolute path under `$top`, which is a declared process-monitor root in any repo that adopts
that kit, so the child is attributable by the kit's fence. `--remote "$remote"` hands the child the
remote this lander resolved and pushed to, so the two cannot pick different remotes.

**No literal names the run-gates kit.** A kit file names nothing outside itself by literal; the
install-prefix gate is a pure ban over every tracked line, comments included. The function and its
comments spell the kit only as the `run-gates` and `post-merge.sh` resolver arguments.

### Data model

The start record, `<git-common-dir>/gate-post-merge.start`, overwritten on every start. Key, TAB,
value, one per line, the grammar `gate-full-green` already uses:

| key | value |
|---|---|
| `sha` | the landed tip, 40 hex |
| `pid` | `$!`, the MSYS pid on Windows |
| `winpid` | `/proc/<pid>/winpid` where it exists, else empty |
| `log` | the absolute log path |
| `started` | `date -u +%Y-%m-%dT%H:%M:%SZ` |
| `by` | `push-main` |

`winpid` is there because process-monitor keys every row on the Windows pid. The log is per sha so a
second landing that starts while the first bar still writes cannot truncate it.

### Messages

One line per outcome, on stderr, each prefixed `push-main: `:

| outcome | line |
|---|---|
| started | `post-merge bar started on <sha8> — pid <pid>, log <log>` |
| `ci` | `post-merge bar — GATE_POST_MERGE=ci at <sha8>, so remote CI runs it; nothing started here.` |
| outside the set | `post-merge bar NOT started — GATE_POST_MERGE at <sha8> is '<value>', outside 'local ci'.` |
| no python | `post-merge bar NOT started — no usable python launcher, so the run-gates kit could not be located. The landing stands.` |
| no kit | `post-merge bar NOT started — no run-gates kit holding post-merge.sh beside this lander. The landing stands.` |
| no common dir | `post-merge bar NOT started — the git common dir could not be resolved. The landing stands.` |
| record unwritable | `post-merge bar started on <sha8> — pid <pid>, log <log>; the start record could not be written.` |

### Inventory

| identifier | cell | lexicon |
|---|---|---|
| `run_post_merge` | `sh.function` | `python tools/lexicon/lexicon.py --suggest run_post_merge --as sh.function` printed OK on 2026-10-09 |
| `read_policy_key` | `sh.function` | a verbatim copy of the hook's, already graded in two files |
| `gate-post-merge.start` | a file under the git common dir | not a code identifier |
| `gate-post-merge-<sha8>.log` | a file under the git common dir | not a code identifier |

`start_post_merge` was the first name and the lexicon refused it: `start` is not a verb in this repo's
table, which reserves lifecycle words. `run` fits because the function runs the launch to completion
and reports its outcome; the bar it launches is the child's to finish.

### Files touched (estimate)

- `tools/push-main.sh` — the copy, the function and its two call sites.
- `tools/push-main.test.sh` — the new arms (run at VERIFYING, not in the pass).
- `memory/map/generated/symbols.json` — `gen_map.py --write`, because a new shell function stales it.

### Alternatives rejected

- **Registering the child with the process-monitor kit.** The brief asks for it and the kit has no
  registration input: see F1.
- **The log under the worktree's own git dir.** An in-place landing lands from a linked worktree, and
  removing that worktree after the landing deletes `.git/worktrees/<name>/`, taking the log of a bar
  that may still be running. The common dir outlives every worktree.
- **One fixed log name.** A second landing's `>` would truncate a log the first bar is still writing.
- **Asking the hook for the declaration.** The hook has no read-only verb for a policy key, and
  adding one is a change to a file this unit does not own.
- **A shared library copy of the parser.** The lib dir is gov-internal and every copy-installed kit
  inlines its contents, so a lib canonical still yields an inline copy plus a parity table; the
  direct parity arm is the same guarantee with one fewer file.

## 5. Production-readiness checklist

- security — no new input surface: the value is read from a committed blob at the landed tip, and
  only two literal values act. The child runs the bar declared at that sha, which the post-merge
  script owns.
- perf / scale — the lander pays one `git show` and, under `local`, one resolver call and one fork.
  The bar's cost is the child's, queued by the host turnstile.
- error / empty / loading states — every failure to start is one named line and exit 0, S6.
- observability — the stderr line, the start record and the per-sha log.
- risks — the process-monitor reaper grades a row ORPHAN once it outlives `PROCMON_AGE_CEILING`
  (14400 s in gov's conf on 2026-10-09) with its parent gone, and the lander is always gone by then;
  under `reap-orphans` a post-merge bar longer than four hours is killed and publishes nothing. The
  child's survival when the session that ran push-main ends is UNVERIFIED on Windows: AC1 proves it
  outlives push-main, not the agent harness above it.
- testing — direct fixtures in §6; the arms in §7 at VERIFYING.
- migration — none. Undeclared is today's behaviour and prints nothing.
- user docs — the runbook's declaration table is DEPL-aFrugalTurnstile-1's; this unit adds the
  header lines of `tools/push-main.sh` that say what the lander does after a landing and what it
  does NOT check, which is whether the bar it started ever finished.

## 6. Acceptance criteria

Every criterion is observed in one scratch fixture under `%TEMP%/ft8`, never inside the worktree: a
bare remote, a work repo with the lander copied to its kit prefix exactly as the push-main suite's
`setup_repo` does, no pre-push hook wired, and a stub `post-merge.sh` in a `run-gates` directory beside
the lander that sleeps 8 seconds and then writes its own argv to a marker file. Each new decision is
first run against `tools/push-main.sh` as it is at base `bef97330`, where it must show the old
behaviour, then against the changed file.

- **AC1** — When `GATE_POST_MERGE=local` is committed in `.githooks/gate-env.sh` and the attended
  landing runs as `out=$(bash <prefix>/push-main.sh 2>&1)`, the capture returns in under 8 seconds,
  and about 10 seconds later the marker holds the landed sha followed by `--remote origin`.
  Red when: the marker never appears, which is the base file's behaviour, or the capture takes 8
  seconds or more because the child kept the lander's stdout.
  fixture: built per landing; the tree holds none today.
- **AC2** — When AC1's landing has run, its stderr carries exactly one line matching
  `post-merge bar started on <sha8> — pid`, and `gate-post-merge.start` in the common dir carries
  `sha`, `pid`, `log` and `by push-main` rows whose `sha` equals `git rev-parse HEAD` and whose `log`
  names an existing file. Red when: the line or any of the four rows is absent, or the recorded sha is
  not the landed one.
- **AC3** — When the landed tip declares `GATE_POST_MERGE=ci`, `grep -c 'remote CI runs it'` over the
  lander's stderr is 1 and no marker appears within 12 seconds. Red when: the stub runs, or the line
  is missing.
- **AC4** — When the landed tip declares no `GATE_POST_MERGE`, `grep -c 'post-merge'` over the
  lander's stderr is 0 and no marker appears within 12 seconds. Red when: any post-merge line is
  printed, or the stub runs.
- **AC5** — When the landed tip declares `GATE_POST_MERGE=yes`, stderr carries the `outside 'local ci'`
  line naming `yes`, and no marker appears. Red when: the stub runs for a value outside the set.
- **AC6** — When R declares `GATE_POST_MERGE=local` and the landed commit deletes that line, no marker
  appears and `grep -c 'post-merge'` is 0; when the working tree carries an uncommitted `local` over a
  landed tip that declares nothing, the lander refuses the dirty tree as it does today and starts
  nothing. Red when: the declaration is read from R, the working tree or `GATE_POST_MERGE` in the
  environment, shown by exporting `GATE_POST_MERGE=local` for one run and seeing a marker.
- **AC7** — When `local` is declared and the stub `post-merge.sh` is removed from the fixture, the
  lander exits 0 and stderr carries the `no run-gates kit holding post-merge.sh` line; the remote's
  default branch equals the landed sha. Red when: the exit status is not 0, or nothing is printed.
- **AC8** — When `local` is declared and the IN-PLACE path lands, `--prepare --slug tB` then
  `--land --slug tB` from a linked worktree on a run branch, the marker appears holding the prepared
  merge's sha, which `git rev-parse HEAD` in that worktree reads. Red when: only the attended path
  starts the bar, which is the shape of a call added at one of the two sites.
  fixture: a linked worktree on a run branch over the same bare remote, as the suite's in-place block
  builds one.
- **AC9** — When the slice `awk '/^read_policy_key\(\)/,/^}/'` of `tools/push-main.sh` is compared by
  `diff` with the same slice of `.githooks/pre-push`, it prints nothing; when one byte of a scratch copy
  of the lander's function is changed and the same compare runs over the copy, it prints the differing
  line. Red when: the two copies differ, or the staged break prints nothing, which would mean the slice
  matched no function at all.

## 7. Gates

`push-main self-test` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/push-main.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · a stub post-merge script in a run-gates directory beside the fixture lander, and a gate-env declaration per case · none
New arm: tools/push-main.test.sh · covers AC9 · a byte changed in a scratch copy of the lander's parser · none

The close runs these. A pass runs only the §6 fixture.

## 8. Open questions

- **FACT-QUESTION · F1 — Does the process-monitor kit have a convention for recording a long-lived
  child, as design D10 and the brief assume?**
  Probe: read every input `tools/process-monitor/*.py` opens, `grep -n "open(\|environ" tools/process-monitor/*.py`.
  Observation that decides it: an input other than `.process-monitor.conf`, the `PROCMON_*`
  environment and the process census would be a registration channel. Liveness: the same grep does
  print the conf reads in `scope.py` and `reap.py`, so it can produce a hit.
  Observed on 2026-10-09: it opens only `.process-monitor.conf` and the health log, and reads only
  `PROCMON_ROOT`, `PROCMON_BACKEND` and `PROCMON_REAP_MODE` from the environment. Attribution is a
  property of the process tree, from roots declared in the conf. So D10's "records its pid with the
  process-monitor convention" cannot work as written: there is no convention.
  RESOLVED (agent, 2026-10-09, delegated): the child is made attributable by construction, its argv
  carrying the absolute path under the repository root, and its pid and Windows pid are written to the
  lander's own start record. Adding a registration input to process-monitor was rejected under the
  build method's veto 2, a new public surface on another kit.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · §4 "The start": the child is started under `nohup`. What disagreed: the build
  ground asks for a child detached from the lander's session, and rev-1's bare `&` leaves it open to
  a hangup; `setsid` is absent from Git-Bash on node a, so `nohup` is the portable form.

## 10. Reuse audit

The seam this unit extends is `resolve_kit_dir`, found by
`python tools/codebase-map/reuse_lookup.py "resolve a sibling kit directory from this script"` as a
SEAM with 67 installs, already inlined in `tools/push-main.sh` and called there by
`check_merge_losses` and `run_minter`; `run_post_merge` is their third caller, with the same file
test. The parser is `read_policy_key`, copied from `.githooks/pre-push`. For the detached start, no
existing seam fits: `reuse_lookup.py "start a detached background job after a landing push and record its pid"`
returned only record and pid readers, `check_pid_alive` and `read_pid_image` among them, none of which
starts anything. The recall probe returned the brief and design D10 and no earlier record of a
lander starting a child.

Recall terms used: push-main lander marker detached background child pid process-monitor orphan reap stdout landing
