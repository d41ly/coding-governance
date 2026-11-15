**Serves:** research TOOL-aMeasuredDrag-1

# Evidence brief — performance review, base aebbb4a72 (2026-11-15, node a, Windows+MSYS)

## Gate ledger aggregate (all worktree ledgers, 1972 rows, 49 bar runs). Columns: median_s max_s n leg
  2038.7   7932.6   17 unattended kit gate
   701.0   1041.7   24 memory hygiene
   676.4   3183.7   23 govkit acceptance matrix
   590.8   2454.0   23 routed commits name a specced unit
   294.0   5401.4   23 pass-order history
   291.5    421.6   10 instruction edits (manifest checks)
   265.3    867.0   22 transition-audit arms
   263.2    359.4    9 tags (the resolver's checks)
   255.4    631.2   22 spawn budget (forks per hot entrypoint)
   235.7    902.6   23 brief-recorded
   221.1    301.2   22 straggler-guard arms
   137.8   1214.9   23 marker contracts
   132.6    263.1   25 drift-audit records
   107.1    156.6    8 memory hygiene (the pass checks)
    78.1    316.3    8 help page commands
    54.5    165.1    8 edges (every declared edge parses, is registered and resolves)
    51.3    145.6    9 positional (the citation check alone)
    46.3     80.1   23 spec tokens (a spec's own names resolve)
    45.4     83.1   23 review-protocol parity (kit vs dogfood)
    45.2    497.2   25 hook destinations (every declared hook path ships)
    41.0     78.8   23 recall floor
    37.5     90.3   20 policy check
    36.9    293.1   26 every held leg is budgeted, every budget row resolves
    33.8    194.9   25 govkit selfcheck
    33.4    137.6   23 agent-cap restatement
    31.9    180.2   23 playbook validity gate
    29.9     94.5    8 instruction render (one renderer of record)
    27.0    210.7   23 kit version markers
    25.8    213.0   25 testsuite counts (every bar self-test prints one)
    24.2     44.6   13 step-gate
    23.8     36.1   11 writing practice (records and units)
    23.8     63.5   23 verifier fan-out
    21.4     78.7   13 step-rows-frozen
    20.9    113.6   26 method carriers (every pointer declared)
    18.3     61.5   25 lexicon wiring
    16.7     22.6    8 python reads (a name never bound, an import outside its guard)
    16.5    120.6   23 micro-format definitions
    15.9     43.6   23 review-join ban (no ref-keyed join)
    14.8     20.4    8 spec tokens (the pass's own spec)
    14.4     98.8   23 unattended skill wiring
    13.7     27.4   15 docs
    11.9     55.0   25 playbook parity
    10.6     14.2   25 lexicon naming predicates
    10.0     24.5   27 install-prefix (shipped surface)
    10.0     53.7   25 kit epoch (shipped bytes move, the version moves)
     9.6     70.8   26 dead-path carriers (deleted files still named)
     9.3    109.9   26 kickoff-manifest ratchet
     8.8     22.9   23 build-method size
     8.8     45.4   23 process-monitor wiring
     8.4     31.5    8 help reference pages
     8.2     13.4    8 layer dependencies (the core never depends on an expansion)
     8.1     12.2   25 codebase-map coverage + freshness
     7.6     12.5    8 one-owner
     6.8     22.2   23 unattended skill size
     6.6     27.2   23 charter size
     6.5     30.5   25 playbook render wiring
     6.4     20.8   23 template size <=48KiB
     5.5     21.5   22 roles render wiring
     5.4     22.2   22 kit/dogfood doc parity
     5.3     13.3   26 encoding posture (text IO names its encoding)
bar runs 49 median summed leg-seconds/run 2039 max 23427

gate-legs.json: 175 legs; chunks selftests 75, declarations 57, product 22, wiring 13, records 5, e2e 3; declared ceilings sum 215924 s
health.log last 24h: run-gates retry-passed x22 (legs retried after 420s timeout: tags, instruction edits); drift signal legs_retried_after_timeout=91/102

## Commit mix since 2026-10-15 (gov, non-merge, 2745 commits)
   1537 records
    504 spec
    264 build
    176 tool
     38 fix
     19 feat
     16 tools
      6 mint
lines changed: memory/ 1,263,948 vs tools/+skills/ 184,388 (about 7:1)
Adopters since 2026-10-01: incms/main fix 326 records 277 docs 182 chore 171 spec 140 feat 135; nicocares/main records 386 build 233 fix 195 docs 153 spec 149 feat 117

## Prior owner-side measurements (auto-memory, re-verify before trusting)
### slowdown-audit-2026-11-14

On 2026-11-14 I audited session c5f50d22: 458 h wall, 157 workflows and 469 agents. I also timed the same verbs on origin/main 846d51d39, on node a with a live run beside it, so every timing is noisy by about 2x.

**Session costs:**
- Idle-wake ticks: 666 turns, 24.5 h of main-loop busy time, and 795k output tokens.
- Builders: a median 9.6 min before the first product edit and 5.1 min after the last one, about 31 h in total.
- `--dispatch`: about 5.3 min per call, about 19 h in total.
- Commits plus `gen_build_index --write`: about 17 h.
- Divergences: 23 runs, about 8 h of builders.
- stop-guard: 9.3 s on each of 1028 Stops.

**Still true on main 846d51d39:**
- `gen_build_index.py --write` takes 68–106 s, rewrites all 3206 artifacts when none changed, and adds about 3 s to the next `git status`.
- A one-line ledger commit's pre-commit hook takes about 230 s:
  - `gen_build_index --check --staged` takes 67 s and does not skip.
  - `--check-coverage --staged` takes 34 s to grade nothing.
- `--dispatch` runs the whole-tree spec-token check (62 s). Its cache key includes HEAD, so every pass commit misses. The builder runs it itself, so a refusal costs a spawned builder.
- `--liveness` takes 13 s, and the stop-guard runs it on every Stop.

**Already fixed since the session:**
- aSwiftRefusal, aSmoothedDispatch and aBatchedPacket fixed the dispatch costs.
- aSmoothedDispatch-6 fixed the write-gate Edit blocks.
- dPavedRoad-2 fixed the format-guard re-sends.

**How to apply:** re-measure before building any of the candidates. See [[hygiene-staged-leg-costs-16-minutes]] and [[unattended-leg-suite-costs-4h-on-node-a]].
### hygiene-check-12-costs-minutes

Measured over session db957487 (dFairHearing + aSmoothedDispatch, 2026-11-02..11): `check-memory-hygiene.sh --only 12[,…]` took a mean 257-404 s per run; spec writers ran it 27 times, and full hygiene 161 times (mean 128 s), 8h20m of agent tool time in all. The pre-commit `--staged` hook added 217 commits x 66-110 s.

**Why:** check 12 grades every spec in the tree, not the one a writer touched, with per-spec forks at ~0.75 s each under MSYS.

**How to apply:** when briefing a spec writer, tell it to grade only its own spec (`check-spec-tokens.py --spec`, and hygiene scoped to its build if a scope flag exists); never ask for a full or `--only 12` run inside a pass. A scoped check 12 is the speed-up candidate. Related: [[hygiene-staged-leg-costs-16-minutes]], [[a-git-spawn-costs-751ms]].
### unattended-leg-suite-costs-4h-on-node-a

**A `git` process spawn costs ~751 ms on this node** (Cygwin bash, measured 2026-09-06 as the
`git log -1 --format=%s` plus `printf | tr` pair, per commit walked). Any gate leg that spawns per
commit or per file is therefore priced in hours, and the git work itself is irrelevant next to the
spawn count.

`pass-order history` was the worked example and it is now FIXED, so do not carry its old numbers:

| | seconds | note |
|---|---|---|
| before | 10,184 | 2.8 h, exit 0 — red on COST, green on CONTENT |
| after | 591 | same tree, summary line byte-identical, all seven counters |
| after, at a tip grading 108 units not 89 | 510 | ceiling is 5400 |

The fix was **one pass over history into a cache, not a bigger ceiling**. Its ceiling had already
been re-declared 900 → 2400 → 5400 by successive sessions and it still redded; the population had
grown (`TOOL-aStagedLane-1` widened it from 45 graded units to 89) and re-declaring only chases that.
A second bottleneck was the same shape: the spec scan read every spec blob under a build, so a
29-unit build did 870 reads at four spawns each, fixed with one `git grep -n` candidate filter.

**When a leg is slow, count its process spawns before you touch its ceiling.** Raising a ceiling to
get your own push through is the "claiming the key IS the unblock" move the charter names.

## Diagnosing a gate timeout, in order

1. Count concurrent bars: `ps -ef | grep '[r]un-gates.sh'`. Contention inflated this leg 1.6x once
   (597 s alone, 968 s under six sibling bars) and I twice drew a wrong conclusion from a contended
   reading — see [[redirected-gate-output-looks-stalled]] and the open row `TOOL-aUnblockedFleet-8`.
2. Re-run the single leg ALONE and time it.
3. Read per-leg seconds from `<git-dir>/gate-ledger.tsv`, one row per leg.
4. Only then decide between content, cost and contention — and if it is cost, look for a spawn in a
   loop before you look at the number in `tools/gate-legs.json`.

A verdict-preserving rebuild owes an exhaustive equivalence check, not an argument: here, all 2187
cache entries were diffed byte-for-byte against the old per-commit tokenisation before the change
was trusted.
### unit-builder-stacks-suites-per-pass

A `tools/workflows/unattended-unit.js` pass, left to the spec's own acceptance criteria, will run
every self-test suite its criteria name — and run them CONCURRENTLY: unit 2 of `aRatifiedRulings`
(2026-09-13) had six `check-unattended.test.sh --shard 2/2` copies, two `-x` full runs, eight
`--shard N/8` runs and a `run-gates.sh` bar all alive at once on a 16-core box, each spawning
`check-unattended.sh` per fixture. Five hours, nothing finishing. The owner stopped it.

**Why:** the spec's red-first rule ("observe the failing case before landing") is read per arm, and
the parent build's briefs said "assert a positive artifact that the arm ran" — so the agent ran the
whole suite per fixture, per break, per side. Nothing in the harness bounds that; M6's "diff-scoped
gates per pass, the full bar once at the push boundary" is in the method the agent skims.

**How to apply:** put it in the `ground` argument and the brief, first paragraph, in capitals: a
pass runs the FAST diff-scoped gates and NOTHING held — no self-test suite, no held leg, no bar. A
unit whose SUBJECT is a suite runs that suite once per measurement, alone. State the count. The
full bar is `--close`'s and the push boundary's. Also: `TaskStop` on the workflow does NOT kill the
suites it spawned; kill them by command line, and check the cwd of anything named `run-gates.sh`
before killing — another session's bar looks identical from the process list.
[[polling-loops-contaminate-timings]] [[kill-9-on-a-bar-strands-its-turnstile-beacon]]
### slow-spawns-are-a-kernel-pool-leak

On 2026-10-11 an unattended `--preflight` took 14-26 minutes. Profiling the code
(`tools/check-wiring.sh --check` 787 s, `read_derived_phase` 306 s) was real but secondary: the
host spawned EVERY process slowly with the CPU at 40%. `/usr/bin/true` cost 1120 ms, a bare
`$(...)` fork 794 ms, and native `cmd /c exit` from PowerShell 706 ms, so MSYS was not the cause.
`Get-Counter '\Memory\Pool Paged Bytes','\Memory\Pool Nonpaged Bytes'` read 18.2 GB paged and
6.6 GB nonpaged after 6.5 days of uptime. The commit charge was 60.8 of 67.7 GB, free pages were
48 MB, and processes' private memory summed to only about 25 GB.

Still unrebooted on 2026-10-12: 20.2 GB paged + 6.2 GB nonpaged at 7.3 days, `/usr/bin/true` 408 ms.
aPairedSlots's two-bar A/B ran entirely on that leak, so its "one slot" verdict wants a re-measure
after a reboot.

**Why:** a kernel pool leak starves process creation, and that cost multiplies across scripts that
spawn thousands of times. Code profiles then point at whichever loop spawns most, which reads like
a code defect.

**How to apply:** before profiling any "it's slow" report on node a, run the two microbenchmarks
(`/usr/bin/true` x10, native `cmd /c exit` x10) and the pool counters. Pools in the GB range mean
the owner reboots, ideally after reaping sessions; the spawn-count fix is still worth doing but is
not the remedy. Identifying the leaking tag needs poolmon or RAMMap as admin. Related:
[[unattended-leg-suite-costs-4h-on-node-a]], [[wsl2-spawns-are-500x-cheaper]].
### wsl2-spawns-are-500x-cheaper

Measured 2026-10-09 on node `a`: WSL2 distro `claude-u26` (git 2.53, python 3.14, node 22, nproc 16)
spawns `true` in ~1.2 ms and forks a subshell in ~1.2 ms; MSYS Git-Bash pays 21 ms quiet and
632-818 ms loaded per spawn, 89-315 ms per `$(...)`. `git` against the repo on `/mnt/c` costs
45-91 ms a call, so any WSL run needs its own clone on WSL's ext4 disk.

Two traps: run `wsl.exe` with `MSYS_NO_PATHCONV=1` and a script FILE (inline `bash -c` quoting and
`/mnt/c` paths are mangled by MSYS); and Linux git sees every Windows worktree as prunable, so a
`git worktree prune`/`gc` from WSL against `C:/projects/coding-governance/.git` would delete them.
WSL may only fetch from the primary. CI is `windows-latest` on purpose.

This is the lead lever in aSparedSpawn's menu (unit B1). Related: [[process-creation-is-the-suite-cost]].
### hygiene-staged-leg-costs-16-minutes

Measured 2026-08-27, node `a`, uncontended, 16 cores, on `coding-governance` at `f5dff6ae`:

| run | seconds |
|---|---|
| `check-memory-hygiene.sh --staged`, as shipped | **963** |
| same, with check 23 guarded | **54** |

So check 23 is **94% of the pre-commit leg's wall clock** and the fix is 17.8x.

**The defect.** `tools/memory-tree/check-memory-hygiene.sh:1114` opens `if [ -n "$alcut" ]; then` —
the cutoff only, never `$STAGED`. Its four structural siblings all guard on `[ "$STAGED" = 0 ]`
(`:667`, `:1051`, `:1066`, `:1076`). It is the one delegating corpus-walker that never got the guard,
so it walks all 317 specs and 307 records on every commit regardless of what is staged. The fix is
`if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then`. No coverage moves: `.githooks/pre-push:229` runs the
full `run-gates.sh` at the push boundary, where the unguarded pass already lives.

Second-largest, same path: check 9 at `:599` guards on `[ "$STAGED" = 0 ] || <memory/ staged>`, and
`.githooks/pre-commit:48` only invokes the gate when `memory/**` is staged — so the right disjunct is
true by construction and `gen_build_index.py --check` re-renders the whole index every commit.

**Why:** the script's own comment at `:111-112` records that "a fork is ~50-100 ms under
MSYS/Windows" and that this exact per-file-spawn class once cost "minutes on a large adopter tree".
Check 23 reintroduced the class the file already documents fixing elsewhere.

**How to apply:** never raise a commit timeout here — background it (see
[[taskstop-leaves-detached-bash-running]]). When timing any gate on this box, kill leftover
`check-memory-hygiene|pre-commit` processes by PID and verify zero remain first; a stale run from a
previous attempt silently doubles the number. Do NOT let subagents run gates during a measurement —
they were told not to on 2026-08-27 and did anyway, invalidating one run.

Static command-shape attribution from a `bash -x` trace put check 23 at only 69%; the A/B says 94%.
Trust the A/B — summing recognised command shapes undercounts loop internals.
### live-chain-packet-join-costs-170s-at-close

At dGroundRules' close (2026-10-25, node a) the `spec tokens` leg took 170s alone and timed out at its 180s ceiling twice in the bar (attributed CONTENDED, which the close reads as the run's own). At origin/main the same leg took 5s. The whole cost is the packet join's `packet.py --check <slug>`, and inside it `carries.py --report <slug>`, which spawns `git show` once per chain spec revision (4095 spawns, 143s). It only runs while the build's chain run is live, which is exactly its own close.

**Why:** `carries.py` is a pinned packet instrument; only the owner moves a pin (`packet.py --repin`), so a run cannot batch it through `git cat-file --batch` itself. The run was handed off HELD owner-decision.

**How to apply:** before a chain build's close, time `python tools/check-spec-tokens.py` alone; near 180s, raise it with the owner early instead of spending two hour-long closes. Also: the lander's `--prepare` kit mint touches watched files, so a re-stamp commit of the kickoff manifest on top of the prepared merge is owed (precedent `6d2ed123a`). Related: [[in-place-close-attest-before-prepare]], [[no-selftests-in-the-final-bar]].

**Recurred 2026-10-27, dWellOiledMachine (125 specs):** the ceiling had been raised to 390s (TOOL-dGroundRules-87, from a 195s reading), but spec tokens ran 512s alone and routed commits ran 358s alone against 300s. Both were green unbounded. The close redded both as CONTENDED, and a gates-green override needs all-INHERITED. The run was handed off HELD owner-decision at 0075cd1c4. The cost grows with chain size, so a fixed ceiling keeps losing. The real fix is carries.py batching under an owner repin.

**Resolved 2026-10-28.** TOOL-dWellOiledMachine-127 raised spec tokens to 940 s and routed commits to 760 s, sized from main-loop solo readings: R1 465.2 s; R2a 378.7 s WHOLE; R2b 322.1 s RANGE plus WHOLE. It landed at 1c31d2602.
- The scratch-guard hook refuses ANY agent a gate leg's argv, so the main loop must take the readings, and the spec must say so.
- Even at 760 s, routed commits timed out once in the pre-push pool and passed on its serial retry.
- dRankedPlan raised the same two ceilings in parallel (TOOL-dRankedPlan-82: 830 s; TOOL-dRankedPlan-83: 710 s). It reconciled onto dWellOiledMachine's higher values, taking main's side and re-stamping `last-audit` after the reconcile. It landed at ec469ed88. Before raising a ceiling, check other live chain branches for the same raise.

## Environment facts
- 34 worktrees; 43 non-terminal builds in memory/LIVE.md; memory/ holds 12038 files (205 MB); tools/ 499 files
- A git/process spawn under MSYS on node a: ~21 ms quiet, 0.6-0.8 s loaded
- In-flight speed-up build aTrimmedWait on branch/speedups-9c2e63 (tip 057f26ba4); earlier ones: aSwiftRefusal, aSmoothedDispatch, aBatchedPacket, aLightenedLoop, aSparedSpawn, aFrugalTurnstile, aQueuedIndex, aLiftedCeiling
- agent-cap hook rule 6: every Agent/Workflow call must be a rendered handoff or a harness listed in .claude/roles.json
