# The owner's prompt, verbatim, the brief it authorized, and what orientation found

**Serves:** research TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7

Handed to `/unattended` as the `--prompt` value on 2026-10-11, node `a`. The value carried no
whitespace and named a readable file, so by the Skill's routing table it is a path and the FILE'S
CONTENT is the prompt. The path was
`C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-deterministic-attended-workflows-943570/e131d82c-aaf3-45ad-abb9-258d7ab9ad1b/scratchpad/handoff-preflight-wiring.md`,
a temporary file the session "Deterministic workflows for attended builds" wrote, so its bytes are
carried here. It names no tracked id of this repo. It is quoted line for line below, so its own
headings and fence are not this record's.

## The prompt

> # Handoff — make the unattended preflight finish in seconds
>
> ## Role
>
> You are a performance engineer on the coding-governance repository, starting an unattended run from
> this prompt. You fix one defect class: a check that is correct but too slow where it runs. You weaken
> no check. Every refusal and every UNWIRED line it can print today it still prints, observed RED on a
> staged break. You measure before and after with the same instrument, A/B interleaved on the same
> host, and you report numbers, not impressions. You cut spawns; you never raise a timeout or a
> ceiling to make a slow thing pass.
>
> ## Task
>
> ### Symptom
>
> On node `a`, 2026-10-11, `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>`
> took 18.7 minutes (02:05:49 to 02:24:31). A third run sat in one step for more than 18 minutes. The
> owner expects seconds.
>
> ### What was measured
>
> The host was saturated by other sessions throughout: CPU 84% over 16 logical CPUs, 3.8 of 32 GB free,
> 75 bash, 27 claude and 12 `timeout` processes. A single spawn cost 0.5 to 2.5 s
> (`git rev-parse --show-toplevel` took 2.5 s, and even a builtin stalled 0.8 s). That amplifies the
> defect; it is not the defect.
>
> - **Preflight's own steps cost about 68 s of traced wall.** The seconds-scale ones are
>   `observe_remote` (15 s, an `ls-remote` under `timeout 60`), `observe_anchor` (9 s),
>   `resolve_claim_remote` (5 s) and `resolve_landed_log` (3 s).
> - **Then it waits on one child.** `check_wiring` runs `bash tools/check-wiring.sh --check` through
>   `run_bounded` under `timeout -k 5s 3600`, and preflight sits in `wait` on it. In the first run that
>   wait was about 16 of the 18.7 minutes, since the next step's `run-gates.sh --print-profile` started
>   at 02:23:12.
> - **`check-wiring.sh --check` alone, traced:** 787 s end to end, exit 0, 02:39:59 to 02:53:06. Its
>   straggler-inventory step hit its own timeout (exit 124) and printed a `note` saying so. Wall by
>   function, from the first 643 s of the trace:
>
>   | Function | Wall |
>   |---|---|
>   | `check_merge_rows` | 267 s |
>   | `matchers_of` | 76 s |
>   | `resolve_fragment_hook` | 43 s |
>   | `resolve_kit_dir` | 31 s |
>   | `check_hook_blobs` | 29 s |
>   | `json_str` | 26 s |
>   | `check_routed` | 25 s |
>   | `resolve_python` | 24 s, 106 calls |
>   | `resolve_kit_file` | 19 s |
>   | `check_scratch_guard` | 15 s |
>   | `check_ssh_keepalive` | 12 s |
>   | `check_eol` | 12 s, and still running |
>
> - **The hottest site** is `check_merge_rows`'s family-prefix harvest, around line 1252: a `while
>   read` loop running `[ -f "$p" ] && sed -n '…' "$p"` once per path. That is one `sed` per
>   `merge=rows` index, 244 files, 191 s. The same per-item shape recurs:
>   - `check_eol` runs one `git check-attr eol` per file;
>   - `json_str` and `matchers_of` parse each fragment's JSON with a `sed`/`grep` pipeline per key,
>     per fragment;
>   - `resolve_python` re-resolves the interpreter on every call, 106 times.
>
> - **The last step can then fail on the same cost.** A traced preflight passed every content check
>   after 26 minutes (02:30:51 to 02:56:56). It was then refused at check 109: the claim write's
>   `git push` of `refs/gov/runs/<slug>` was "killed by this kit's own 60s bound". That push runs
>   `.githooks/pre-push`, which works through about 960 lines of prelude, including per-ref work for
>   non-default refs (from about line 653), before it exits at "no push to the default branch"
>   (about line 963). `git ls-remote origin` alone took 11 s at the time. A refused preflight writes
>   nothing, so the only remedy today is another 26-minute run.
>
> ### The instrument
>
> ```bash
> env BASH_XTRACEFD=9 PS4='+${EPOCHREALTIME} ${LINENO} ' bash -x <script> <args> 9><trace-file>
> python <analyzer> <trace-file> <script>
> ```
>
> The analyzer is `trace_gaps.py`, which sits beside this file. It charges each gap to the trace line
> before it, so an untraced child (a `git`, a `python`, a child `bash` script) is charged to the line
> that started it. It aggregates by line and by enclosing function. Copy it into your build folder: an
> instrument kept only in a temp dir can be neither re-run nor re-derived. Also COUNT SPAWNS, before and
> after. Wall depends on the host, and the spawn count does not.
>
> ### Scope
>
> 1. **Decide what preflight needs from the wiring check**, measured rather than assumed. It may need
>    the whole of `check-wiring.sh --check`, or only the arms an unattended run depends on, such as
>    the stop-guard, gate-guard, stall-recorder and resume-tick wiring. Record each candidate you
>    tested and what it would stop catching.
> 2. **Collapse the per-item spawns in `check-wiring.sh`:**
>    - one `sed` or `awk` over every `merge=rows` index;
>    - one `git check-attr` over every path;
>    - each fragment's JSON parsed once, by one interpreter call;
>    - the python resolution cached once per run.
>
>    Keep each arm's verdict and its exact printed line.
> 3. **The other seconds-scale preflight steps**, where a cut is cheap and loses nothing.
> 4. **Cost becomes a verdict.** Preflight and the wiring check each declare a wall-clock ceiling,
>    and a run over it says so by name instead of waiting silently on a 3600 s bound.
>
> ### Acceptance
>
> - Spawn counts for `check-wiring.sh --check` and for a full preflight, before and after, from the
>   same instrument in the same session.
> - Preflight wall on node `a`, A/B interleaved with the old code on the same host state. The target
>   is at most 60 s for a whole preflight on node `a`.
> - Every arm of `check-wiring.sh` whose spawns you collapsed is observed RED on a staged break and
>   GREEN once restored, through a sliced arm and never the whole suite.
>
> ### Gates
>
> The merge bar at the close, run once. In passes, only direct checks and sliced self-test arms.
>
> ### Non-goals
>
> A concurrent unattended run (session "Deterministic workflows for attended builds") owns these
> paths; do not edit them:
> - `tools/roles/`
> - `tools/hooks/scratch-guard.js` and `tools/hooks/agent-cap.js`
> - `tools/workflows/unattended-build*`, `tools/workflows/unattended-unit.js` and
>   `tools/workflows/tier2-review*`
> - `skills/session-kickoff/`
> - `coding-governance-agents.template.md`
> - `tools/govkit/registry.toml`
>
> Late in its build it adds ONE arm to `tools/check-wiring.sh`. Whoever lands second reconciles that
> file additively.
>
> ### Limitations
>
> - Never kill a process you did not start. The host is shared, and its load is other sessions' work.
> - A git spawn costs about 0.75 s on this node even when idle, so batch git calls. A backgrounded
>   watchdog holds its caller's stdout. Killing a bar with `kill -9` strands the turnstile beacon.
>   Each of these has a memory note.
> - Never wrap the lander in `timeout`.

## The brief

### Goal

A whole `unattended.sh --preflight` on node `a` finishes in at most 60 s, measured A/B against the
old code on the same host state. `check-wiring.sh --check` stops paying one process per item, the
claim push stops outliving its bound, and a preflight or wiring check that runs long says so by name
instead of waiting silently on a 3600 s bound. No check is weakened.

### Items

1. Decide what preflight needs from the wiring check, measured rather than assumed, recording each candidate tested and what it would stop catching. [planned TOOL-aBriskPreflight-3]
2. Collapse the per-item spawns in `check-wiring.sh`: one call over every `merge=rows` index, one `git check-attr` over every path, each fragment's JSON parsed once, and python resolved once per run, keeping each arm's verdict and its exact printed line. [planned TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2]
3. Cut the other seconds-scale preflight steps where a cut is cheap and loses nothing: the bounded probes it waits on one after another, the phase it re-derives for every run record in the tree, and the claim push that runs the whole pre-push prelude. [planned TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6]
4. Cost becomes a verdict: preflight and the wiring check each declare a wall-clock ceiling, and a run over it says so by name. [planned TOOL-aBriskPreflight-7]

### Acceptance

- Spawn counts for `check-wiring.sh --check` and for a whole preflight, before and after, from one
  instrument in this session (forks and program starts, read from one xtrace per run).
- Preflight wall on node `a`, A/B interleaved with the old code on the same host state, each arm
  proving it ran by its `preflight OK` line. The target is at most 60 s.
- Every arm of `check-wiring.sh` whose spawns were collapsed is observed RED on a staged break and
  GREEN once restored, through a sliced arm and never the whole suite.
- Each touched arm prints the same lines, byte for byte, before and after on the same tree.

### Gates

The merge bar at the close, `bash tools/run-gates/run-gates.sh`, run once. Inside a pass only the
direct check its spec names and sliced self-test arms.

### Non-goals

- The paths the concurrent run aOrientedCast owns: `tools/roles/`, `tools/hooks/scratch-guard.js`,
  `tools/hooks/agent-cap.js`, `tools/workflows/unattended-build*`, `tools/workflows/unattended-unit.js`,
  `tools/workflows/tier2-review*`, `skills/session-kickoff/`, `coding-governance-agents.template.md`
  and `tools/govkit/registry.toml`.
- Raising any timeout, bound or ceiling to make a slow step pass.
- The driver's fork-free readers (`fact`, `runmd_of`, `readme_of`) and a fork-count arm, which
  aSparedSpawn-8 plans.
- A new `.unattended.conf` key: it owes a protocol key-table row, and the protocol is a governance
  carrier.

### Limitations

- Never kill a process this run did not start. The host is shared, and its load is other sessions'.
- A spawn costs 0.5 to 2.5 s on this node under load, so git calls are batched and every reading
  carries the host's spawn cost beside it.
- A backgrounded watchdog holds its caller's stdout; `kill -9` on a bar strands the turnstile
  beacon; the lander is never wrapped in `timeout`.
- aOrientedCast adds one arm to `tools/check-wiring.sh` late in its build; whoever lands second
  reconciles that file additively.
- The check-wiring kit self-test runs only sliced, one arm at a time, inside a pass.

### Reuse

- **Seams extended:** `run_bounded` in `tools/unattended/unattended.sh` (the one bounded runner and
  its process ledger); `read_derived_phase` and its callers; the arms of `tools/check-wiring.sh`,
  whose `check_merge_rows` already reads attributes through one `git check-attr --stdin`; the
  straggler layer of `.githooks/pre-push`.
- **Probe:** `reuse_lookup.py` on "batch per-item subprocess spawns into one call in a wiring
  check" named no batching helper; its nearest seams are `wired` and `resolve_kit_file`, both in
  the file this build edits.
- **Recall:** the query surfaced `TOOL-aPromptedMandate-9` (the wiring seam measured at 1m22s),
  `TOOL-aBoundedCeiling-6` (`run_bounded`), `TOOL-aBranchedMandate-2` (the eol arm under
  preflight) and `TOOL-aProvenReuse-6` (wall-clock arms flake under load).

## Drawn from the session

> 2. A preflight run with WIRING_CHECK="true" (the owner told me to bypass the wiring check) STILL took 17.7 min (03:05:56 to 03:23:36). So check-wiring is about a third of the cost, not all of it.

> 4. Check 109 refused two preflights in a row: the claim push of refs/gov/runs/<slug> is killed at REMOTE_BOUND=60 s, a file constant with no override. The push runs .githooks/pre-push's whole prelude before its skip-nondefault exit. A preflight that passed everything else is lost at its last step and costs another 17+ minutes to retry.

> The trace file is %TEMP%/aoc-pf-trace.txt on this node (PS4='+${EPOCHREALTIME} ${LINENO} '), and the analyzer is trace_gaps.py beside your handoff file.

— agent, the session "Deterministic workflows for attended builds", 2026-10-11, a cross-session message during orientation

## Owner confirmation

Asked: Accept this brief for unattended build aBriskPreflight? Goal: a whole preflight on node a in ≤60 s, A/B against the old code, with no check weakened. It plans seven units: two batch the per-item spawns in check-wiring.sh; one decides by measurement which wiring arms preflight needs; one starts preflight's bounded probes together; one stops re-deriving the phase of every run record; one lets pre-push leave early for a branchless push (the check-109 claim push); and one adds ceilings. It quotes the aOrientedCast session's message (WIRING_CHECK=true still took 17.7 min; the check-109 claim push). Use Other to edit it.

The option the owner chose carried a preview of the same four items, acceptance, gates and
non-goals as `## The brief` above.

Answer: Accept as written (Recommended)

Asked: What should a breached wall-clock ceiling DO? The wiring check is currently killed only at the 3600 s GATE_BOUND, and preflight as a whole has no ceiling.

Answer: Name it, refuse only wiring (Recommended) — the wiring check is killed at its own declared ceiling and preflight refuses check 4 naming that ceiling; preflight's own total over its ceiling prints a named breach line but still writes the record, because a refused preflight costs a whole re-run.

## What orientation found, before the roster was written

- **The tree.** This session's worktree was clean and level with `origin/main` at `b726385f2`, so
  the run starts in place. `ANCHOR_SCOPE="local"`, so the commit authorizes and no push is owed.
- **check-wiring.sh's per-item sites**, read in source: `check_merge_rows` reads attributes through
  one `git check-attr --stdin` already, then runs `[ -f ] && sed` once per `merge=rows` index;
  `check_eol` runs one `git check-attr eol` per candidate path; `json_str` is one `sed | head` per
  key per fragment and `matchers_of` a seven-stage pipeline over the whole settings file per call;
  `resolve_python` RUNS each candidate interpreter every time it is called, and `resolve_kit_file`
  calls it, then starts python again through `resolve_kit_dir`.
- **No arm grades the unattended kit's own hooks.** The stop-guard, gate-guard and stall-recorder
  fragments, and the resume tick, are graded by no arm of `check-wiring.sh` today, so a subset of
  the existing arms cannot select them. Two arms never move the exit status under `--check`: `eol`
  prints `note` at worst, and the straggler inventory prints `note`, `ok` or `skip`.
- **Preflight's own steps**, from the peer's 1561 s trace of an old-code preflight, re-analyzed here
  with its analyzer: `run_bounded` waited 754 s on four children run one after another — the wiring
  check (544 s), `push-main.sh --carry` (57 s), `push-main.sh --prepared` (43 s) and
  `run-gates.sh --print-profile` (55 s); `read_derived_phase` cost 306 s over 109 run records; the
  three remote observations are distinct (the anchor's `ls-remote`, the claims' `fetch`, the claim
  `push`), so none is a duplicate to drop; the claim push alone took 69 s.
- **A sibling build plans adjacent work.** aSparedSpawn (OPEN, forks left for the owner) plans
  fork-free readers in the driver and a fork-count arm over `check-wiring.sh --check` in its unit 8,
  and puts the cross-process memo of `resolve_python` and per-item loop classes out of its scope.
  This build takes those loop classes and leaves its readers and its arm alone.
