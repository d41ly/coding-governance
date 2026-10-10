# Appendix — Slow legs and suites: govkit and the unattended kit, where the time goes and what to cut

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-08, kept verbatim below its first heading. It ran no suite: every saving is an ESTIMATE from static spawn counts against the profiled bar in `2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`, and the synthesis that ranks across all five is `2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md`. Line citations are against `fa68a767` plus this unit's fixes.


Read-only research, node a, 2026-10-08, worktree `gate-runner-profiling-optimization-5d1f1e` at
9289116b5 plus this session's uncommitted edits. I ran no leg, suite or self-test. Every count below
is a static count of spawn sites. Static counts include conditional branches, and they miss loop
multipliers. Treat every seconds figure as an estimate. The basis is written beside each figure.

## Calibration used for every estimate

These were measured now, one shot each, on a box that was running a timing-sensitive test. Treat
them as contended figures.

| unit | cost now | earlier record |
|---|---:|---|
| `$(:)`, a bare fork with no exec, in a shell holding a 1.6 MB variable | 89 ms (210 ms in a `seq` loop) | 10 ms on node d (gotcha) |
| `/usr/bin/true`, an exec | 265 ms | grep 181 ms, `bash -c` 251 ms (aGradedDoorway-7 S3) |
| `git rev-parse` | 225 ms | 371 ms (S3) |
| `python -c "import sys"` | 0.89 s | — |
| `bash -n tools/unattended/unattended.sh`, which is parse only | 0.75 s | — |
| `printf -v x` | 8 µs | — |
| bash 5.3 funsub `${ :; }` | 2.1 ms | — |
| `git log --follow --diff-filter=A -- <one RUN.md>` | 0.37 s | — |
| ONE `git log --name-status -M` over every `RUN*.md` in history (5545 lines) | 0.53 s | — |

Three conclusions from this table drive the rest of the document:

1. **A fork costs about as much as an exec on this node.** So `$(fact_of …)`, `$(printf …)` and
   `$(normpath …)` cost as much as a git call. That matches this session's `normpath` finding, and
   the repo's gotcha only half-states it.
2. **A history walk costs no more than a spawn.** A `--follow` walk took 0.37 s, which is the price
   of `git rev-parse`. One whole-history walk over all records took 0.53 s. So batching history
   reads replaces N spawns with one spawn, and the walk itself is not what costs.
3. **The driver costs about 0.75 s per call before any preamble runs**, because bash parses 13.3k
   lines plus the 2.1k-line lib on every call. Only a persistent process removes that floor. A lazy
   preamble does not.

Bash on this node is 5.3.9, so `${ cmd; }` no-fork substitution is available. It is **not usable in
shipped kit code**. Ubuntu 24.04 CI ships bash 5.2, macOS ships 3.2, and the syntax is a parse
error there that kills the whole script. The portable equivalent is a function that sets a global
(`printf -v REPLY` or a named out-variable), which this session already used for `normpath`/`_np`.

## Ranked levers

The "pooled" column scales a quiet-seconds estimate by the 2-4x contention ratio the measurements
show: check-wiring ran 2322 s pooled against 601 s serial, and pass-order 1050 s against 576 s.

| # | leg / suite | lever | est. seconds saved | effort | risk |
|---|---|---|---|---|---|
| 0 | every leg | **Operator action, not code:** add a Defender real-time exclusion for the repo, the worktrees and `%TEMP%`. aGradedDoorway-7 S3 measured 6.4-13x per-spawn price against node d and named this as the largest single factor. I did not perform it, because it is a security-settings change. | 50-85% of all spawn-bound wall | owner, minutes | security posture; owner decision |
| 1 | unattended driver suite (8 shards) | Fork-free `fact`. There are 190 `$(fact …)` sites in `unattended.sh`, plus 103 `$(printf …)`. Convert them to out-variable readers. | 2000-4000 s pool work (≈1450 driver calls × 10-20 executed forks × 0.1-0.2 s) | M: mechanical, 300 sites | L: pure readers; the trailing-newline semantics must match |
| 2 | unattended gate selftest (8 shards) and the repo leg | Fork-free readers in `check-unattended.sh`: `fact_of` (30 sites), `core_of`/`read_bare_const` (≈22 forks per run, each re-reading about 800 driver lines), and `$(printf …)` (60 sites). Read every driver constant with ONE awk into an assoc array. | gate suite: 449 runs × ~40-60 forks × ~0.1-0.2 s ≈ 2700-5000 s pool work. Repo leg: see #4 | M | L |
| 3 | pass-order history, brief-recorded, and their two self-tests | Memoize `build_commit`'s range in `lib-unattended.sh:1084`. Every id in a build passes the same `"$base..HEAD $HR_EXCL"`, so the rev-list runs once per build, or once in total when `base` is behind the advertised tip. Return the result through a global, never `$(…)`. | pass-order ≈ 656 ids × 3 spawns ≈ 380 s primary / 700 s pooled. brief-recorded ≈ 484 × 3 ≈ 290 / 500 s | S: one lib function plus 2 callers | L |
| 4 | unattended kit gate (repo leg) | Per-record history tables. Memoize `read_landing_commit`, which runs ≈8 spawns and is called up to 4 times per LANDING record. Do ONE `git cat-file --batch` for every `HEAD:RUN*.md` and README blob. Do ONE `git log --name-status -M` walk for first-add, last-touch and sibling floors, replacing per-record `log --follow`, `log -1` and the sibling walks. | ≈600-900 spawns ≈ 150-250 s primary / 400-700 s pooled | M | M: `--follow` copy-following must be reproduced, or its waiver kept |
| 5 | unattended kit gate (repo leg) | #2 applied to the 82-record loop. `check-unattended.sh:1965-2884` holds 71 `$(` sites, 19 of them `fact_of`. Parse all `## Run facts` blocks once into `FACT[file|key]`. | ≈82 × 20-30 forks ≈ 1600-2400 forks ≈ 300-500 s primary | S-M | L |
| 6 | govkit selftest | Shard it the way the bash suites are sharded: `--shard N/M` over the 13k-line `main()`, with `GOV_PIN` and the other prologue state computed once per shard. | wall 3775 → ~1000-1200 s at 4 shards. Pool work unchanged | M | L-M: arms share module-level fixtures |
| 7 | govkit selftest and the product | Make `blob_at` (`govkit.py:6123`, one `git show` per file, 23 call sites inside per-row loops) read through one persistent `git cat-file --batch` per verb. | ≈20-40 git spawns saved per plan/apply/update; ≈200-400 s quiet in the suite. Adopters' `apply`/`update` speed up too | M | M: missing-object and error semantics must match `returncode != 0 → None` |
| 8 | hook destinations self-test | Build `scratch()` once. It currently does `git archive HEAD \| tar -x` of all 3633 files (78 MB) followed by `git add -A` and a commit, and does that **9 times**. Reset between arms with `git reset --hard` + `git clean -fdq`, or archive only the paths the gate reads. | ≈8 × 20-50 s ≈ 160-400 s quiet / 400-700 s pooled | S | L-M: an arm must not be made vacuous by a missing path (arm 1 is the control) |
| 9 | hook destinations self-test and the repo leg | Collapse the gate's per-fragment process trio (`check-hook-destinations.sh:97,103,104`: python json, `check-wiring.sh --resolve-fragment`, `settings-merge.py --resolve-fragment`) into one multi-fragment call per reader. Fold the two govkit-importing pythons (`:49`, `:69`) into one. | ≈30 → 3 process chains per invocation. Repo leg 113 → ~30 s; suite ≈12 × 20-25 s ≈ 250-300 s | M: two readers gain a list form | L: the parity arm still compares two independent readers |
| 10 | unattended driver suite | Lazy driver preamble: resolve `GENERATED_INDEXES`, `SHARED_RECORDS` and `_two_key` (`unattended.sh:653-662`, ≈10 spawns) only for the verbs that read them. Those verbs are preflight (via `check_cross_run_overlap`), dispatch, close, abort, authorization (via `dod_met`), check-commit and overlaps. Resume, status, hold, review, landed, plan and the rest, about 55% of the suite's call mix, skip it. | ≈700 calls × ~2 s ≈ 1400 s pool work | S-M | M: a misdeclared conf currently refuses on EVERY verb, and an arm may assert that |
| 11 | unattended-build self-test | Run one persistent node worker (bash `coproc`) instead of `node -e` per `run_wf`. There are 167 static sites, and each call re-reads and recompiles 2369 lines of JS. | ≈190 × 0.5-0.9 s ≈ 100-170 s serial (199 s → ~30-60 s); pooled ≈400-500 s | M | M: per-case env (`RUN_WF_SCHEMA`) must travel in the request, and a worker crash must respawn loudly |
| 12 | gate-guard selftest | Drive the ~100 payload arms in process through `require(HOOK)`. `gate-guard.js:672` already exports `checkCommand`, `main` and the rest. Build the payload in node rather than one python per arm (`gate-guard.test.sh:169`). Keep about 5 real-process arms for stdin, exit-code and meta checks. | ≈100 × (0.9 python + 0.5 node) ≈ 140 s → ~20 s | S-M | L-M |
| 13 | govkit selftest | Run govkit through an import shim (`-c "import govkit; …"`) so its 854 KB script compiles to `.pyc` once rather than on every `run()`. The cheap half of an in-process harness. | ≈300 runs × 0.3-0.5 s ≈ 100-150 s | S | very low |
| 14 | govkit selftest | Full in-process harness: `govkit.main(argv)` with redirected stdout and stderr and a cwd context. `main` returns an int, has no `os.chdir`, and has 2 `sys.exit` sites. | ≈300 × 1.2 s ≈ 360 s quiet, on top of #13 | M | M: module globals set by option parsing (`COVERAGE`, `ANSWERS`, `TO_REV`, `WRITE`, …) leak between calls; exit-code, encoding and lock arms must stay subprocess |
| 15 | check-wiring self-test | Resolve python lazily in `check-wiring.sh:465`. Today it spends 0.9 s on `python -c "import sys"` every invocation, even for checks that never run python. Also fold the double `settings-merge.py` run on the failure path (`:186`, `:189`) into one. | ≈60-120 invocations × 0.9 s ≈ 55-110 s quiet / 150-300 s pooled | S | L: the "no python" refusal must still fire where python is needed |
| 16 | check-wiring self-test | Build a template repo once and `cp -r` it for each of the 33 `newrepo` calls. Each `newrepo` costs 8 git spawns (`check-wiring.test.sh:35-40`). | ≈33 × 7 × 0.25 ≈ 60 s | S | L |
| 17 | unattended gate selftest | A record-or-kit scope selector for `check-unattended.sh`, so record arms skip the kit self-scans. The kit self-scans are checks 26, 28, 32, 33, 39, 41, 47, 48 and 51, and they grade the same kit bytes on every arm. Run the full conforming control once per shard. | perhaps 30-50% of each fixture run ≈ 3000-5000 s pool work | M | M: reopens a route aGradedDoorway-7 S3 closed, and that closure rests on a misreading (see the gate-suite section) |
| 18 | unattended kit gate, pass-order, brief-recorded | Key the impure input instead of banning reuse. The runner's reuse unit (`run-gates.sh:2233`) skips every `impure` leg. If the advertised tip sha were part of `input_key`, a non-authoritative `GATE_REUSE` bar could reuse all three. Pre-push never sets `GATE_REUSE`, so the landing bar is unchanged. | ≈5800 s pool work on a re-run bar with an unchanged tree and remote | S-M | M: the key must name every outside input (ls-remote URL, conf) |

**Rebuild options,** each kept with every arm and staged break:

- **(R1) A Python record layer for `check-unattended.sh`.** One process computes the per-record
  derived facts: phase, witness resolution, landing commit, first and last commit dates, ancestry
  and the dispatch windows. It emits them as TSV, and the bash checks keep their verdicts and byte
  messages. The repo leg would drop to an estimated 100-200 s.
  - **Cost:** 2-4 weeks.
  - **Risk:** it duplicates predicates the lib shares with the driver, which is the repo's
    two-readers class, unless the driver also reads the facts through the helper.
- **(R2) A full Python port of the 13.3k-line driver.** I do not recommend it. The cost runs to
  months. The 16.6k-line suite asserts byte-exact refusal text, and the driver's verb semantics are
  shell-shaped (`exit` inside verbs, EXIT traps, sourced conf). Levers #1, #10 and #2 reach roughly
  half the saving for a few percent of the effort.
- **(R3) A driver server mode** (`--serve` on a coproc: parse plus preamble once, a subshell per
  verb). It would remove the 0.75 s parse floor and the ≈3 s preamble per call, which is the largest
  remaining term in the driver suite after #1. It must re-source `.unattended.conf` whenever its
  hash changes, because `mkconf` rewrites the conf between arms. The preamble's own refusals are
  under test, so that path must stay a real process.
  - **Cost:** 1-2 weeks.
  - **Risk:** high.

## Flake risks (wall-clock-timed arms)

| file:line | what | risk |
|---|---|---|
| `tools/unattended/unattended.test.sh:7822-7824` | `run_bounded` must return in `< 20 s` against a 2 s bound | Medium under a 1-2 s spawn price plus kill latency |
| `tools/unattended/unattended.test.sh:7831-7837` | grandchild arm `< 20 s`, and the CONTROL must take `>= 20 s` (`sleep 30`) | Low-medium; the control direction is safe, the `< 20` direction is the exposed one |
| `tools/unattended/unattended.test.sh:13515-13563` | 0.1 s polls capped at 100 iterations, about 10 s, waiting for a child to exec | Medium under load: exec latency is 1-2 s and Defender scans first exec |
| `tools/unattended/unattended.test.sh:8618-8627, 8849` | `sleep 1` to order second-resolution UTC stamps (`STOP_UTC < LEASE_UTC`) | Low |
| `tools/unattended/resume-tick.test.sh:199-203` | `read_stub_log` polls 20 × 0.5 s, a 10 s cap, for a backgrounded stub's line | Medium |
| `tools/unattended/resume-tick.test.sh:233-238` | `derive_winpid` waits 10 × 0.5 s, 5 s, for `ps` to show the sleeper | Medium |
| `tools/unattended/resume-tick.test.sh:248-255` | `read_task_gone` waits 25 × 0.2 s, 5 s, via `tasklist` for a kill to land | Medium: `tasklist` itself costs about 1 s under load |
| `tools/govkit/selftest.py:6013-6015` | waits 30 s for the first concurrent `update --write` to create its lock | Low-medium: a python start plus git ops under 2 s spawns |
| `tools/unattended/gate-guard.test.sh:215,221,535` | `timeout` appears only inside payload strings | none |
| `tools/unattended/check-unattended.test.sh` | no sleeps or timeouts found | none |

---

## unattended kit gate — `bash tools/unattended/check-unattended.sh` (repo subject)

**(a) What it guarantees.** Every tracked run-state record and the kit's own declarations are
consistent with the driver's vocabularies, the history and the advertised remote tip: 51 numbered
checks.

**(b) Measured cost.** 3937 s pooled. Other readings: 1538 s in the primary ledger, 708 s and
176 s quiet (aLeakedHandle-1, dLoggedFlight-11), and a historical spread of 190-3837 s
(aQuenchedHarness-8).

**(c) Where the time goes.** The populations, counted at HEAD:

- 82 tracked `RUN*.md` files, made of 73 live `RUN.md` (47 LANDED, 15 LANDING, 8 ABORTED,
  2 BUILDING, 1 HELD) and 9 archived.
- 64 of them carry review rows. 946 dispatch rows. 4930 commits.

The script has 400 `$(` sites, 77 `GIT` calls and 155 loops.

- **Record loop**, `check-unattended.sh:1965-2884`. 71 `$(` sites per record, 19 of them
  `$(fact_of …)` (`:852`). `fact_of` itself has no spawn, so each call costs only its fork.
  - Conditional git work: `read_landing_commit` (`lib-unattended.sh:1565`) costs `git diff`, awk,
    then `git show | extract_run_facts(awk) | sed | head | tr` and `git log -1`, about 8 spawns.
    It is called at `:455`, `:2052`, `:2532` and `:2794` for the same LANDING file.
  - `check_landed_facts_due` and `read_first_commit_date` (`lib:1608`) run a `git log --follow`
    plus one `git log --full-history` per archived sibling.
  - Estimate: 82 × 25-40 spawns ≈ 2000-3300.
- **Check 2's review loop**, `:651-835`, 64 records. Each pays `grep`, `extract | awk`,
  `region(awk)`, `git show | awk`, `git log --follow | tail`, `printf | sort` and a large awk:
  about 10 spawns, ≈ 640 in total.
- **Check 23**, `:3976-4253`. 17 graded passes, each with `pass_commit`, `next_anchor`,
  `git log`, a per-declared-path `git log` and `diff-tree | grep | tr`: ≈ 15-25 spawns each,
  ≈ 300-400 in total.
- **Smaller loops.** The halt-code loop `:910`, 82 × 1-2 forks, and the `:3747` loop, 82 × ~5.
- **Fixed prologue and kit self-scans.**
  - About 22 `core_of`/`read_bare_const` forks (`:465-575`). Each scans about 800 driver lines in
    a bash `read` loop.
  - Check 28's per-kit-file scan (`:5021-5089`): about 12 files × 3 spawns, plus 17 raw git hits
    × 3, ≈ 90.
  - Checks 26, 33, 47, 48 and 51: awk, grep and comm over the kit.
  - Estimate: ≈ 300-400 spawns.
- **Total:** ≈ 3500-5000 spawns × 0.25-0.3 s ≈ 900-1500 s. That reproduces the 1538 s primary
  reading, and pool contention explains 3937 s.

**(d) Levers.** #5 fork-free fact reads (≈300-500 s primary). #4 history tables: one
`cat-file --batch`, one `log --name-status -M` (measured 0.53 s for every record), and a memoized
`read_landing_commit` (≈150-250 s). #2's single-awk constant read (≈20 forks, ≈5 s, small here
but ×449 in the suite). #18 keyed reuse. Together #4 and #5 are estimated to take the leg from
≈1500 s to ≈300-500 s primary.

**(e) Rebuild.** R1 above.

## pass-order history — `bash tools/unattended/check-pass-order.sh`

**(a)** Every unit built in the range HEAD carries past the advertised tip had a graded spec at its
build commit's parent.

**(b)** 1050 s pooled, 576 s primary. The log reads: 656 units graded, 653 unbuilt in range,
84 builds cut off.

**(c)** Where the time goes:

- **Per README.** `for readme` (`check-pass-order.sh:314`) runs over all 150 builds, cut-off ones
  included. Each pays `git show HEAD:readme | sed | head` (`:321`), 3 spawns plus a fork. The 66
  surviving builds add the RUN blob, `extract_run_facts | sed | head`, `cat-file -e`, and
  `git show | awk` for ids (`:349-370`), about 8 more spawns.
- **Per id**, 656 of them, `:398`: `$(build_commit …)` forks, then forks again for
  `$(GIT rev-list …)` inside `lib-unattended.sh:1100` and runs git. That is 3 spawns for a range
  that is **identical for every id of a build** and here holds a handful of commits (range
  `40a8b8c3..fa68a767`).
- **Total:** ≈ 450 + 530 + 1970 ≈ 2950 spawns ≈ 590 s, which matches 576 s.

**(d)** #3, the `build_commit` memo: compute `rev-list HEAD $HR_EXCL` once, and per build subtract
`base`'s reach. When `base` is reachable from the advertised tip the set is unchanged, and
`_ADVH_REACH`-style tables already exist in the checker. Add a `cat-file --batch` for all READMEs
and RUN blobs at HEAD. Together they take ≈2950 spawns to about 60, so 576 s → ≈30-50 s primary.

## brief-recorded — `bash tools/unattended/check-brief-recorded.sh`

**(a)** Every unit built in range has a brief row, with a matching blob hash, in its run's record
at the build commit.

**(b)** 793 s pooled, 490 s primary. 484 units graded, 481 unbuilt in range.

**(c)** It is the same shape as pass-order: `:356-388` per README, and `:399` `build_commit` per id
with the same per-build range. The `:424-427` per-later-commit `build_commit` loop only runs for
built ids, of which there are 3.

**(d)** The same lib fix (#3) plus a `cat-file --batch` takes 490 s → ≈30-50 s. Both legs share
`build_commit`, so the fix lands once.

## govkit selftest — `python tools/govkit/selftest.py`

**(a)** govkit's plan, apply, update, adopt, check, mint, epoch and selfcheck verbs, its receipt
provenance and its static shell-exec declarations: about 1800 `ok` assertions.

**(b)** 3775 s pooled, and it FAILED. 3445 s in the primary ledger. The quiet worst of 7 readings
is 1065 s.

**(c)** The script is 15.2k lines, and `main()` alone is 13k (`selftest.py:2113`). Static sites:

- 212 `run()` (`:217`). Each one is a fresh `python govkit.py`: 0.89 s startup, plus compiling the
  854 KB script, which a run-as-script **never** caches as `.pyc` (≈0.3-0.5 s).
- Inside each govkit verb, git spawns. The main one is `blob_at` (`govkit.py:6123`), one
  `git show` per file per row, called from per-row loops at `:4428`, `:4994`, `:6992`, `:7147`,
  `:7264`, `:8161-8162`, `:8989-8990` and elsewhere. A memory-tree fixture ships about 30 files.
- 405 `git()` (`:579`).
- 145 `settle()` at 2 git each, and 74 `make_target()` at 6 git each (`:676-701`).
- 92 other subprocess calls and 57 `bash` invocations.

Estimate: ≈300-400 govkit runs × (1.3 s python + 5-15 git) plus ≈1100 fixture git spawns ≈
1000-1500 s quiet. Nothing in the suite runs concurrently: `main` is one linear 13k-line body.

**(d)** Levers:

- #6 sharding is the wall lever: 3775 → ≈1000.
- #7 is a batched `blob_at`, which also helps adopters.
- #13 is the import shim, nearly free.
- #14 is the in-process harness.
- `make_target` as a template copy (`shutil.copytree` of one pre-built repo, or writing
  `.git/config` directly in place of 3 `git config` spawns) saves ≈75 s.

The FAIL is separate from cost. This session's working tree already adds the `cmd_mint`
`SHELL_EXEC_SITES` row (`govkit.py:4281`) and the `check_by_design_parity.py` stub
(`selftest.py:13200`) for the two FAIL classes in the log. The 3775 s figure is a red run's
duration.

**(e) Rebuild.** No rewrite is warranted. The suite is already Python. The cost is process and
git spawns, which #6, #7, #13 and #14 address.

## check-wiring self-test — `bash tools/check-wiring.test.sh`

**(a)** `check-wiring.sh` wires and verifies hooksPath, the agent-cap, scratch-guard and recall
hooks, receipts, EOL, merge rows and the skill install, and refuses each broken wiring by name: 170
assertions.

**(b)** It timed out pooled at 2322 s against its 2320 ceiling. The serial retry took 601 s, and
the historical reading is 589 s.

**(c)** Where the time goes:

- 106 static checker invocations (`chk`, `chke`, `skill_run`), plus loops, for about 120. Each pays
  `check-wiring.sh`'s top-level `resolve_python`: one 0.9 s python run at `:465`, unconditional.
- Each invocation also pays `git rev-parse`, a share of the 161 `$(` sites, and on owned-hook arms
  `settings-merge.py` at `:186`. On failure that runs twice, at `:189`.
- 33 `newrepo` at 8 git spawns each (`check-wiring.test.sh:35-40`).
- 23 commits.
- Estimate: 120 × ≈4-5 s + ≈300 fixture spawns ≈ 600 s, which matches the serial retry.

**(d)** #15, lazy python plus the single settings-merge call: ≈55-110 s quiet. #16, the template
repo: ≈60 s. Run independent arm groups concurrently, each in its own `mktemp` repo (the arms
already `cd` into fresh repos): wall /2-3. Together, ≈601 → ≈250-300 s serial.

**(e)** No rebuild is warranted.

## hook destinations self-test — `bash tools/check-hook-destinations.test.sh`

**(a)** Every hook fragment's declared destination is a shipped file, no adopter writes into
`.claude/hooks/`, and the two readers agree: 18 assertions.

**(b)** 969 s pooled, 262-335 s quiet. That is ≈15-50 s per assertion. The repo leg alone costs
113 s.

**(c)** Two costs:

- **`scratch()`** (`check-hook-destinations.test.sh:128-137`) runs 9 times. Each run extracts
  `git archive HEAD` (3633 files, 78 MB, almost all of it `memory/`) with Defender scanning every
  write, then runs `git add -A` and a commit over all of it.
- **Each of ≈12 gate invocations** pays:
  - 2 python processes that import the 854 KB govkit and walk 297 destinations
    (`check-hook-destinations.sh:49,69`);
  - for each of 10 fragments, a python JSON read (`:97`);
  - a full `check-wiring.sh` startup (`:103`), including its own python resolve;
  - a `settings-merge.py` run (`:104`).

That is ≈32 process chains, about 12 of them python, per invocation.

**(d)** #8, one scratch with reset between arms: ≈160-400 s quiet. #9, multi-fragment readers and
one govkit python: suite ≈250-300 s, repo leg 113 → ≈30 s. Together ≈300 s → ≈40-60 s quiet.

**(e)** No rebuild is warranted.

## unattended-build self-test — `bash tools/workflows/unattended-build.test.sh`

**(a)** The `unattended-build.js` Workflow script's control flow, prompts, schemas and dispositions
under doubled `agent`, `workflow` and `parallel`: 853 assertions.

**(b)** It timed out pooled at 702 s against its 700 ceiling. The serial retry took 199 s.

**(c)** Each `run_wf` (`:156`) is one `node -e` that reads and evals the 2369-line script. There
are 167 static sites, plus layout and other `node` calls (19) and 74 git sites. Estimate:
≈190 × 0.6-0.9 s ≈ 115-170 s, which matches 199 s.

**(d)** #11, the coproc worker: 199 → ≈30-60 s serial. A cheaper interim is to cache the
`export const meta` rewrite to a temp `.js` once rather than per case. That saves only the string
replace, not node startup, so it is minor.

**(e)** No rebuild is warranted.

## Held unattended suites

### unattended gate selftest, 8 shards — `check-unattended.test.sh --shard N/8`

**(a)** Every branch of `check-unattended.sh`, armed RED with a GREEN control, against one scratch
repo reset between arms.

**(b)** Shard readings 517-2083 s, ceilings 1730-6117 s. The eight-wide idle longest shard was
922 s. About 449 leg invocations in total; one region alone grew from 67 to 139 leg-run sites.

**(c)** Two costs:

- **Fixture reset is cheap.** `reset_tree` (`:384`) is 5 git spawns.
- **The cost is the ≈449 full leg runs.** On node a each costs ≈20-30 s: the shard readings divided
  by their leg runs. That is ≈100-150 spawns, mostly the fixed prologue (≈22 `core_of` forks) and
  the kit self-scans (checks 26, 28, 32, 33, 39, 41, 47, 48 and 51), which grade **the same kit
  bytes on every arm** that does not mutate the kit.

aBatchedArm-1 recorded "cutting spawns further" as bounded by aTracedSpawn-2 at about 2 s per
invocation of real non-spawn work. Against today's 20-30 s per run that bound leaves about 10x
headroom: it closed that build's scope, it did not refute the route.

aGradedDoorway-7 S3 rejected `--only <n>` because "check bodies are 9.5% of wall". That 9.5% was
**user CPU**. The spawns it attributes to "fixed overhead" are issued from inside those same check
bodies (check 28's loop, for example). So a scope selector removes more than that figure implies.
This needs one traced census before anyone relies on it.

**(d)** #2, fork-free readers and the single-awk constant read: ≈2700-5000 s pool work. #17, the
record/kit scope selector: ≈3000-5000 s, at medium risk. Batching arms that share a tree state
(aBatchedArm-4/5) already exists.

**(e)** R1 helps here too, because each leg run's record layer becomes one process.

### unattended driver selftest, 8 shards — `unattended.test.sh --shard N/8`

**(a)** Every verb and refusal of the 13.3k-line driver.

**(b)** The whole reading was 17142 s pooled. Shard ceilings 1224-6444 s, all estimates.

**(c)** Where the time goes:

- **About 1450 driver calls**: 1324 `run --verb` sites plus 119 `bash "$SCRIPT"`, before loops.
  The verb mix is preflight 318, close 151, resume 122, dispatch 95, status 73, and so on.
- **Each call pays a floor**: 0.75 s of bash parse, plus the preamble.
  - The preamble is `dirname`/`basename` forks (`unattended.sh:84,120`), `git rev-parse` (`:479`),
    `resolve_shared_records`, and `resolve_generated_indexes` (still about 10 spawns after this
    session's fix: `cd`/`dirname`, `derive_self_rel`, `read_conf_value`, 2 `mktemp`, `git ls-files`,
    awk), plus `scan_shared_index_overlaps` (`:653-662`) and the runlog start. ≈15-20 spawns,
    about 3-4 s.
- **Then each verb's body**, with 190 `$(fact …)` sites available to it.
- **Fixture work**: 359 `reset_tree` (`:493`, 3 git spawns plus `mkconf`), 885 commits and
  167 pushes.
- Estimate: ≈1450 × 4-5 s ≈ 6000-7000 s preamble and parse, plus ≈2000-3000 s fixture git, plus
  verb bodies. Consistent with 17142 s pooled.

**(d)** Ranked: #1 fork-free `fact` and `printf -v` (≈2000-4000 s), then #10 lazy preamble
(≈1400 s), then consolidating `reset_tree`'s checkout, reset and clean into
`git checkout -qf -B unit "$UNIT0" && git clean -qfd` (≈359 × 0.25 s ≈ 90 s).

**(e)** R3 server mode removes the remaining parse and preamble floor (≈1450 × ~1 s after #10), at
high risk. R2 is not recommended.

### unattended playbook selftest — `check-playbook.test.sh` (418 s)

About 25 leg runs (`run`, `rc`, 12 `probe` arms at `:117-135`) over a 748-line checker with 79
spawn sites. Each probe copies the fixture, `sed`s it, runs the whole leg and restores. Two levers:

- Run the 12 probes concurrently, each in its own copy of `$W`: wall /3-4, at low risk because
  probes are independent by construction (`cp "$KEEP"` before and after).
- Fork-free readers in `check-playbook.sh`.

Estimated 418 → ≈150 s.

### unattended resume-tick selftest (131 s)

8 tick invocations over 4 fixture repos and 11 commits. The cost is small. The polls are the flake
risk listed above (`:199-203`, `:233-238`, `:248-255`), and the remedy is to raise each cap to
about 30 s. A poll that exits on success costs nothing extra on a quiet box.

### unattended gate-guard selftest (≈144-220 s)

About 100 arms. Each pays a python JSON builder (`gate-guard.test.sh:169`), a `resolve_native`
path conversion and a node hook process (`:173`). Lever #12 takes it to ≈20 s.

### unattended pass-order and brief-recorded selftests (111 s and 115-177 s)

49 and 45 leg runs respectively, over fixtures of 35 and 22 commits. Each leg run pays the per-id
`build_commit` spawns, so #3 cuts these proportionally, by an estimated 30-50%.

### cross-component (339 s)

3 driver or leg invocations over 3 fixture repos. Most of the cost is the driver floor, which #1
and #10 address.

## What to do first, if anyone asks

1. **#3 (`build_commit` memo).** One lib function, two repo legs. It is the largest seconds saved
   per line changed: about 650 s primary, 1200 s pooled. Write it as a new arm whose RED is
   observed first (§7).
2. **#1, #2 and #5 (fork-free readers).** Mechanical. They hit the repo leg and three held suites
   at once.
3. **#8 (hook-destination scratch).** A one-function change, worth ≈300 s.
4. **Before #4, #10 and #17: a traced spawn census of one leg run and one driver call.** Use
   `PS4='+ ${EPOCHREALTIME} ${LINENO} ' bash -x` plus a `GIT` shadow counter in the lib, because
   `bash -x` does not follow children (gotcha `bash-x-does-not-follow-children`). That replaces the
   static estimates here with counts.
