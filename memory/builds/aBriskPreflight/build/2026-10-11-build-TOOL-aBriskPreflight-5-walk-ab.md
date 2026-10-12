# TOOL-aBriskPreflight-5 — the A/B: the live-run walk derives each record once

**Serves:** research TOOL-aBriskPreflight-5

Node `a`, 2026-10-11, the build pass. Spec rev-2. The built driver is blob `3978ec873692`, the
`tools/unattended/unattended.sh` the pass commit carries; BASE's is blob `1512622e1530` at
`b726385f`, written with BASE's `lib-unattended.sh` to the scratch dir by `git show`. Every run
read this worktree's own tracked records at the spec commit `04a009a59`, with `AREF` and `ASHA`
taken from `origin/main` at `d19938f35`, so no run read the network.

## The instrument

`2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh`. It cuts a driver's text above its
argument parser, copies it beside its library into a scratch dir, appends its own harness body and
runs that copy from the root, so every function is the driver's own and no verb runs. Its header
states what each mode prints and when it exits 1. Each primed arm reports what the prime cached and
how many git processes the walk after it started, counted from `GIT_TRACE`, so a walk that never read
the cache cannot pass as one that did. The traced runs use the build's two instruments,
`2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` and
`2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`, the latter given the harness and its
library as the span source.

## Host state, one line beside each traced run

| Run | At (UTC) | Five spawns | Fork | Pool Paged | Pool Nonpaged | CPU |
|---|---|---|---|---|---|---|
| `walk-base-traced` | 06:57:23 | 1.26 s | 0.04 s | 17933 MB | 6199 MB | 42% |
| `walk-built-traced` | 06:59:03 | 0.81 s | 0.03 s | 17934 MB | 6199 MB | 55% |

The two ran back to back, the traced walls 94.5 s and 19.5 s and the untraced ones 75.9 s and
16.4 s, each including about 9 s of the driver's own prologue. The spawn cost moved between the two
lines, so the walls are not a comparison; the counts below do not depend on load.

## The population (AC1)

`--fields` against the built driver printed:

```
primed plain: cached-phase=89 cached-landing=18 (non-empty 18) cached-anc=18 git-in-primed-walk=0 batch-failures=0 differences=0
records=89 landing=17 held=1 differences=0
```

89 is the count `git ls-files` gives for the two run-record globs, one more than the 88 the spec
counted at writing. 17 LANDING and one HELD under `owner-decision` are
the 18 the landing step cached, every one non-empty and every one an ancestor of the tip. The primed
walk started no git process, so every answer it compared came from the cache.

## The walk (AC2)

`--walk` against BASE's driver and the built one, untraced. The two stdouts are byte-identical by
`cmp`: 21 lines, 18 `EXCLUDED … derived LANDED` lines and an announcement of two concurrent runs,
`aClosedDocket` and `aUnblockedFleet`. The built run's stderr ends `cache=0`; BASE's reads
`cache=absent`. The traced pair's `.out` files differ only in their first line, the library's
`resolve_generated_indexes` notice on stderr, which `run-traced.sh` merges and which names each
harness's own scratch dir.

## Failed batches (AC3)

`--fields --fail-batch`, the `git` on PATH exiting 128 for one batched call per arm:

```
primed diff: cached-phase=89 cached-landing=0 (non-empty 0) cached-anc=0 git-in-primed-walk=73 batch-failures=1 differences=0
primed rev-list: cached-phase=89 cached-landing=18 (non-empty 18) cached-anc=0 git-in-primed-walk=18 batch-failures=1 differences=0
records=89 landing=17 held=1 differences=0
```

With the listing failed, nothing landing-shaped was cached and the walk ran the old reading: 73 git
processes, four per landing record (`diff -U0`, `show`, `log`, `merge-base`) and a second `show`
for the HELD one. With the rev-list failed, the landing commits stayed cached and ancestry fell back
to one `merge-base` each. Both arms read zero differences.

## The spawn counts (AC4)

| Run | Forks | Execs | `git` | `sed` | `awk` | `head` | `tr` |
|---|---|---|---|---|---|---|---|
| BASE `walk-base-traced` | 288 | 193 | 79 | 21 | 20 | 19 | 19 |
| built `walk-built-traced` | 52 | 65 | 26 | 2 | 2 | 0 | 0 |

- `execs` fell by 128, against a floor of 6 × 17 − 3 = 99.
- `forks` fell by 236, against a floor of 89 − 6 = 83.

Both counts include the probe's own top level and the cut prologue. Those are the same program in
both runs except that each prologue is its own driver's: the built one carries main's merged changes,
which accounts for its one `timeout` and one `rm`, both outside the walk.

## The other criteria

- **AC5** and **AC6** — one slice, the suite's prologue, the derived-LANDED fixture and its helpers,
  then the AC8 driver block and S5's new arm beside it, run alone from `tools/unattended/` with its
  fixture repositories under `%TEMP%`. Against the built driver it passed, 31 assertions. Each staged
  break was a copy of the built driver beside it differing by one line, chosen through a
  `SLICE_DRIVER` override of the slice's `SCRIPT`. With the cached ancestry forced to 1, the AC8
  block's first three assertions failed: `1 concurrent unattended run(s)` and the `phase LANDING`
  line went missing, and `EXCLUDED memory/builds/tRun/RUN.md` appeared, while S5's arm passed. With
  the `git diff --name-only` result emptied after the call, S5's arm failed the same three ways for
  `tRun`, `2 concurrent unattended run(s)` among them, while its staged-never-committed `tStaged`
  line still passed and the AC8 block passed whole. The slice and both copies were deleted before
  AC8 ran.
- **AC7** — the lines calling `read_derived_phase` outside `read_derived_phase` and
  `check_single_live`, listed at BASE and in the built driver by an `awk` that tracks the enclosing
  function as check 39 does and skips comment lines, are the same 12 lines, compared by `diff` with
  the line numbers dropped.
- **AC8** — `python tools/codebase-map/gen_map.py --check` exits 0 after the slice files were
  deleted; the pass adds no function, so `symbols.json` does not move.

## Bug classes the checklist selected, read against the batch

- `porcelain-diff-names-a-rename-by-its-destination` — the listing is porcelain, so renames are on.
  A rename needs a deletion in the compared set, and every path handed to the listing passed
  `[ -f ]` in the working tree, which `git diff HEAD` compares against, so none of them is deleted
  and each changed one is listed under its own name. A quoted path never reaches the listing, and a
  failed listing returns before anything landing-shaped is cached, which AC3's diff arm observes.
- `empty-field-collapses-unless-it-is-last` — the rows split on 0x1F, which is not IFS whitespace;
  a row with both fact values empty reads as three fields, measured on this host's bash 5.3.
- `line-count-reads-empty-capture-as-one` — `mapfile` over an empty capture yields one empty row,
  which the row loops skip.
- `second-implementation-is-not-a-second-opinion` — the batched `awk` is a second reader of the two
  facts, so AC1 compares it with `fact` over every tracked record, and the probe's own `landing` and
  `held` counts are read by `fact`, never by the cache under test.

Two predicate runs back the gate legs §6 names, neither of them a leg: check 39's own `awk` over
the built driver prints `C39-READERS-SEEN` and no line; and `sh_hygiene.scan_file` counts the same
gated sites in the built driver as in the spec commit's, 6 heredoc-fed and 3 variable-fed, both
registered before this unit.
