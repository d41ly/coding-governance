# The baseline: where a preflight's 18 to 26 minutes go, measured before any unit is built

**Serves:** research TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7

Node `a`, 2026-10-11, BASE `b726385f2`. Every figure here names the run it came from, and every run
names the host state it was taken under, because this host's spawn cost moves by a factor of
fifty with its kernel pool and a reboot mid-build would read as a speed-up.

## The instruments

Committed beside this record, so a figure can be re-derived and re-run:

- `2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` — reads one xtrace written with
  `env SHELLOPTS=xtrace BASH_XTRACEFD=9 PS4='+${EPOCHREALTIME} ${BASHPID} ${BASH_SOURCE##*/}:${LINENO} '`.
  `SHELLOPTS` is exported, so every bash process in the tree, child scripts and bounded children
  included, writes its own rows into the one file. It reports two counts that do not depend on the
  host's load — **forks** (distinct `BASHPID` values, less the first) and **execs** (rows whose
  first word is not a builtin, keyword, assignment or a function the named scripts define) — and
  the wall, attributed per function and per line by the gap to the next row. Its docstring states
  what it cannot count: a program started by a program that is not bash (git running a hook, python
  starting a subprocess), and a fork that traced nothing.
- `2026-10-11-build-TOOL-aBriskPreflight-1-trace-gaps.py` — the owner's analyzer, handed over beside
  the prompt, carried unchanged in behaviour. One function is renamed, `func_of` to `resolve_func`,
  because a records-only `.py` is graded by the lexicon leg and `func` is not a declared verb.
- `2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh` — one line of host state beside every
  timing: five `/usr/bin/true` spawns, one `$(...)` fork, and the Pool Paged, Pool Nonpaged and
  Committed bytes counters with the CPU load.
- `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` and `-run-timed.sh` — one traced run and
  one untraced timed run, each appending a `label=… rc=… wall=…` row.

The rows the runs appended are `2026-10-11-build-TOOL-aBriskPreflight-1-runs.log`.

## Host state

Every reading below was taken with Pool Paged near 17.3 GB and Pool Nonpaged near 6.2 GB, where
about 1 GB and 0.3 GB are normal; the session "Deterministic workflows for attended builds" reported
the same leak and that the owner reboots for it. Five `/usr/bin/true` cost 3.7 to 4.0 s, so one
spawn cost about 0.75 s, against 21 ms quiet on this node (aMeteredSweep). The two counts are what
carries across a reboot; the walls do not.

## check-wiring.sh --check at BASE, traced (run `cw-base-traced`)

568 s wall, rc 0, **355 forks and 387 execs**: `sed` 182, `grep` 56, `git` 37, `head` 21, `tr` 19,
`python3` 17, `dirname` 16, `wc` 10, `cat` 7, `cksum` 6. Wall by function, top of the table:

| Function | Wall | What it does per item |
|---|---|---|
| `check_merge_rows` | 178 s | the family harvest: `[ -f ] && sed` once per `merge=rows` index, 120 indexes, 131 s; the smoke's `grep -c` once per family per id, 12 calls, 15 s |
| `check_backlog_stragglers` | 71 s | `migrate_backlog.py --stragglers` hit its own `timeout 60` and printed the `note … exited 124` line |
| `check_eol` | 43 s | one `git check-attr eol` per candidate path, 10 paths |
| `matchers_of` | 37 s | a seven-stage pipeline over the whole settings file, once per `wired` call |
| `resolve_fragment_hook` | 31 s | `json_str`, two `dirname`, a `sed` per fragment |
| `resolve_kit_dir` + `resolve_kit_file` + `resolve_python` | 52 s | `python3 -c 'import sys'` re-run on every call, then python again with a `cat` heredoc |
| `json_str` | 16 s | one `sed \| head` per key per fragment |

Fifteen lines printed, every arm `ok` or `skip` but the straggler `note`.

## The pre-push hook on a claim-shaped push (run `hook-base`)

`.githooks/pre-push origin <url>`, fed one `refs/gov/runs/x <sha> refs/gov/runs/x 0000…` line,
the sha a parentless empty-tree commit built the way `write_claim` builds one, in a throwaway local
clone so the push journal of the shared git dir is not written. 53 s wall traced, rc 0, **45 forks
and 31 execs**, reaching the `skip-nondefault` exit. About 35 s of it is the straggler layer's
setup — `init_straggler_guard` (7 s), its `resolve_remote_sh` (8 s), `resolve_kit_dir` (9 s),
`resolve_python` (3 s), `read_blob_at` (4 s), `read_conf_value` (2 s) — spent to ask one
`check_has_delta` that a parentless empty-tree commit can only answer "no". The claim write runs this
hook inside `git push` under `REMOTE_BOUND=60`, so at this spawn cost the push cannot fit, and
check 109 refuses a preflight that passed everything else. The peer session reported the same
hook at 46 s and four consecutive check-109 refusals.

## A whole old-code preflight, from the peer's trace

`%TEMP%/aoc-pf-trace.txt`, 1561 s, `PS4='+${EPOCHREALTIME} ${LINENO} '` (no file column, so a
lib-unattended.sh line is charged to whatever unattended.sh function holds the same line number).
Re-analyzed here with the owner's analyzer:

- `run_bounded` waited 754 s on four children, **one after another**: `check-wiring.sh --check`
  (544 s), `push-main.sh --carry` (57 s), `push-main.sh --prepared` (43 s) and
  `run-gates.sh --print-profile` (55 s). None reads another's output.
- `read_derived_phase` cost about 306 s. `check_single_live` calls it for every tracked
  `RUN.md` and `RUN.*.md` (109 records), each through a `$(fact …)`, and again for every record it
  counts live; a LANDING record also runs `read_landing_commit` (a `git show | extract | sed | head
  | tr` pipeline and a `git log -1`). Most of the population is retired archives, terminal by
  construction.
- The 129 rows at "L61" are the `GIT` wrapper at `lib-unattended.sh:61`, every kind of git call,
  197 s, not 129 `rev-parse --show-toplevel` calls: the driver resolves its root once.
- The three remote observations are distinct — the anchor's `ls-remote --symref HEAD`, the claims'
  `fetch` of `refs/gov/runs/*`, and the claim `push` (69 s, the hook above) — so none is a
  duplicate to drop.

## This build's own preflight at BASE (run `pf-real-base`)

`unattended.sh --preflight aBriskPreflight --keepalive-id 0fe01023`, untraced, from this worktree
against the real remote: **1218.6 s wall, rc 0**, `preflight OK` at base `271a90045`. Host state
just before: five spawns 3.97 s (0.8 s each), Pool Paged 17319 MB, Nonpaged 6280 MB, CPU 31%; just
after, five spawns 5.33 s. It printed 18 `EXCLUDED … derived LANDED` lines (the in-place LANDING
records the live-run count derives one by one), two concurrent runs, four remote claims, and the
claim push completed inside its 60 s bound this time. It was not traced, deliberately: tracing the
hook slows the claim push, which was already the step that failed four times for the peer, and a
refused preflight writes nothing. The whole-preflight spawn count is taken at the A/B, on a fixture
build in a throwaway clone, where a traced refusal costs nothing.

## What the units take from this

- **1** — the merge-rows harvest becomes one `sed` over every index, the smoke's per-id `grep -c`
  one pass, and the eol population one `git check-attr --stdin`.
- **2** — each fragment read once, the settings file flattened once per run, python resolved once
  and every kit file it locates resolved through one interpreter start.
- **3** — the candidates to measure once 1 and 2 land: the whole check; the arms whose verdict can
  move the exit status under `--check` (every arm but `eol` and the straggler inventory, which
  print `note` at worst); and a subset keyed on the unattended kit's own hooks, which no arm
  grades today, so that candidate cannot be selected from the existing arms at all.
- **4** — the four bounded children start together at the top of the precondition block and each
  is collected where it is read today, so output order and every refusal stay where they are.
- **5** — the live-run count reads every record's phase in one pass and derives a record once.
- **6** — the straggler layer runs only over pushed branches, and resolves its python and kit only
  when one is pushed.
- **7** — the owner's ruling: a wiring check over its declared ceiling is killed and refuses
  check 4 naming the ceiling; a preflight over its own prints a named breach line and still
  writes the record.
