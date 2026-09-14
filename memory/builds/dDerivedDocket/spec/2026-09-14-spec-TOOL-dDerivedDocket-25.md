# TOOL-dDerivedDocket-25 — runner scratch hygiene and a tree-moved exit

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

The merge bar leaks its legs' scratch into the ambient `TMPDIR` and never sweeps it, a bar killed
by signal 9 leaves its whole scratch dir behind, a killed runner tree cannot be attributed by the
process-monitor fence because the runner's argv is relative, and a bar whose tree moved under it
still exits 0. This unit makes the runner own its scratch, sweep a dead bar's scratch, carry an
absolute argv, and exit with a distinct TREE MOVED status. It closes TOOL-aMeteredTurnstile-2 and
TOOL-aReapedSpinner-14 and removes the stop entries i66 and i67 (`aPacedTurnstile/RUN.md:36,38`,
the run editing the tree its own bar graded) plus the adjacent i22, as DR 21.4 U23 lists them.
The header carries no `closes` verb because the status parser at BASE does not know it.

## 2. Scope (IN)

- **S1** — the scratch redirect. Before the first leg dispatches, `tools/run-gates/run-gates.sh`
  creates `$WORK/tmp` and exports `TMPDIR` pointing there, so every leg's `mktemp -d` and every
  Python `tempfile` lands inside the run's own scratch dir and the existing `cleanup` trap
  (`tools/run-gates/run-gates.sh:1040`) removes it. The spelling is the one `mktemp -d` returned,
  never a drive-letter rewrite. Observed by AC4 and AC6.
- **S2** — owned scratch and the dead-owner sweep. `WORK` is created as a named `gate-work.*`
  directory under the ambient `TMPDIR` (captured before S1 redirects it), with an `owner` file
  holding the runner pid, the resolved git common dir and the start epoch, written before any leg
  dispatches. At start each bar sweeps every `gate-work.*` directory whose `owner` names this
  repository's common dir and whose pid fails `ts_alive` (`tools/run-gates/run-gates.sh:611`), and
  announces each sweep on stderr with the pid. Observed by AC2 and AC3.
- **S3** — the entries line. After the sweep the runner prints `TMPDIR entries <n>`, the count of
  top-level entries in the ambient `TMPDIR`, once per bar, and writes the same figure into the run
  record header. Observed by AC2.
- **S4** — absolute self-invocation. When `$0` is not absolute, the runner re-executes itself as
  `bash "$KITDIR/run-gates.sh" "$@"` immediately after `KITDIR` is resolved
  (`tools/run-gates/run-gates.sh:34`) and before any output, lock or scratch exists. Its argv, and
  the argv every leg subshell inherits by fork, then carries an absolute repo path the fence can
  reach. Observed by AC5.
- **S5** — the TREE MOVED exit. When `tree_moved=yes` (`tools/run-gates/run-gates.sh:1812-1813`)
  and no leg failed, the runner prints `gates TREE MOVED — the tree changed while the bar ran, so no
  verdict describes it`, writes `verdict TREE MOVED` into the run record, writes no full-green
  stamp, and exits 3. A bar that failed AND moved stays RED with exit 1, and its RED line names the
  move. The header's exit-code line (`tools/run-gates/run-gates.sh:3`) and
  `tools/run-gates/README.md` gain exit 3. Observed by AC1.
- **S6** — the kit version. `KIT_RUN_GATES_VERSION` and its `gov:kit` marker move from 1.6 to 1.7,
  because a new exit code is a contract change a caller reads. Observed by AC7.

## 3. Non-goals (OUT)

- **The driver's reading of exit 3.** DR 21.4 U23 put "`gates-green` reads that as UNMET and
  re-runs once" in this unit. It moves to the gate-wall unit named in the edges below, which already
  rewrites `gates-green` and is the one unit of the three that may run the unattended suite (D12-i8).
  That keeps every driver-side reading of a runner exit in one spec. The pre-push hook needs no
  change for exit 3: any non-zero status already blocks a push.
- **Legacy litter.** Scratch left by bars before this unit has no `owner` file and is never swept.
  The by-name sweep of named residue was TOOL-aTetheredScratch-2's and is not repeated.
- **Sweeping another repository's scratch.** The sweep reads only `gate-work.*` directories whose
  `owner` names this common dir; see §8 F1.
- **The beacon reap race.** TOOL-aReapedTicket-4 (a bare `rm -rf` of the holder beacon racing a
  successor) is untouched here.
- **Callers.** `.githooks/pre-push:292` and `.unattended.conf`'s `GATE_CMD` keep their relative
  spelling, because S4 makes the runner absolute whoever calls it; see §8 F2.

### Edges

- **hands-off** `TOOL-dDerivedDocket-26` — the TREE MOVED verdict and exit 3, which the no-silent-pass rule there must count as a verdict line
- **hands-off** `TOOL-dDerivedDocket-27` — exit 3, which the driver's `gates-green` re-runs once there
- **hands-off** `TOOL-dDerivedDocket-28` — an absolute runner argv, without which the process ledger's reap is refused by the fence

## 4. Design

### Data model

```
<ambient TMPDIR>/gate-work.XXXXXXXX/       # WORK, created by `mktemp -d` with a template
  owner                                    # pid<TAB>common-dir<TAB>start-epoch, one line
  tmp/                                     # exported as TMPDIR for every leg
  <i>.rc  <i>.pid  <i>.out ...             # unchanged
<git-dir>/gate-run/<id>/verdict            # gains `verdict TREE MOVED` as a value
```

The `owner` file is written with the same tmp-then-`mv` shape the run record already uses, so a
sweeper never reads a half-written line. A directory with no readable `owner` is never swept: an
owner the sweep cannot read is one it cannot prove dead.

### The sweep

`scan_dead_work` runs once, right after `WORK` exists, which is after the turnstile, so a bar still
queued never sweeps. For each
`gate-work.*` entry it reads `owner`, skips its own, skips any entry whose common dir differs from
this run's, and removes the directory when `ts_alive <pid>` fails. The predicate mirrors
`ts_sweep_queue` (`tools/run-gates/run-gates.sh:735`): a live pid only withholds the sweep, and the
comment block at `tools/run-gates/run-gates.sh:730-734` already records why a cross-runtime pid can
only err toward withholding. Every removal prints
`run-gates: sweeping the scratch of a dead bar (pid <p>)` on stderr.

### The re-exec

Placed on the line after `KITDIR=$(cd "$(dirname "$0")" && pwd)`, guarded on `case "$0" in /*)`,
and it uses `exec`, so the pid is unchanged and nothing the caller holds is lost. `KITDIR` is in the
MSYS spelling there, which `tools/process-monitor/scope.py`'s `build_normalized` already folds to the
drive-letter form a declared root uses. The loop guard is the absolute `$0` itself.

### Rollout

The runner change lands whole. A caller that treats every non-zero exit as a failure, which is every
caller at BASE, reads exit 3 correctly as "not green" before the driver learns the finer meaning.

### Inventory

`scan_dead_work` (the sweep) and `write_work_owner` (the owner record), in the `sh.function` cell;
both lead with a declared verb. No new leg, no new conf key, no new file outside the scratch dir.

### Files touched (estimate)

`tools/run-gates/run-gates.sh`, `tools/run-gates/run-gates.test.sh`,
`tools/run-gates/run-gates.turnstile.test.sh`, `tools/run-gates/README.md`,
`tools/run-gates/kit.toml` (version), `memory/map/features/run-gates.md` (prose refresh on touch).

### Alternatives rejected

- **Redirect `TMPDIR` to an external root.** TOOL-aTetheredScratch-2 rev-1 specced it and its audit
  refuted it by measurement: no external root exists on these nodes, and a drive-letter spelling
  breaks four arms of the template-size self-test because `tools/check-template-size.sh` normalises
  through `cd && pwd` while `mktemp` echoes `TMPDIR` verbatim. S1 differs on the discriminating
  point: its root is the runner's own `mktemp -d` result, in the MSYS spelling, and AC6 is the
  observation that the spelling hazard did not return.
- **An EXIT trap per leg** (TOOL-aMeteredTurnstile-2's first suggestion). It needs an edit in each of
  the 63 `mktemp -d` sites and still leaks on signal 9. One export plus one sweep covers both.

## 5. Production-readiness checklist

- **security** — the sweep deletes directories, so it is bounded three ways: the `gate-work.` name,
  a readable `owner` naming this common dir, and a dead pid. Nothing else under `TMPDIR` is touched.
- **perf / scale** — one `ls` of the ambient `TMPDIR` per bar plus one `kill -0` per owned entry.
  The leak this removes cost about 1.5x on `git init` (TOOL-aMeteredTurnstile-2, measured).
- **error / empty / loading states** — an unwritable `$WORK/tmp` refuses the run with exit 2, the
  way an unwritable `WORK` already does (`tools/run-gates/run-gates.sh:979`). An empty `TMPDIR`
  prints `TMPDIR entries 0`.
- **observability** — the entries line, one stderr line per swept dir, and `verdict TREE MOVED` in
  the run record.
- **risks** — a pid table shared across two MSYS runtimes could answer dead for a live bar in the
  other runtime. The stated mitigation is the precedent's: a different runtime also mounts a
  different `/tmp` on these nodes, so the two scratch roots do not meet. Residual, stated.
- **testing** — arms in `tools/run-gates/run-gates.test.sh` for S1 to S5 and one in
  `tools/run-gates/run-gates.turnstile.test.sh` for the live-owner case, each with its break staged
  and observed red before landing.
- **migration** — none. Old scratch stays until a person removes it.
- **user docs** — `tools/run-gates/README.md` exit codes and the scratch section.

## 6. Acceptance criteria

- **AC1** — When a fixture leg edits a tracked file mid-bar and every leg passes,
  `bash tools/run-gates/run-gates.sh` in the canary's scratch repo exits 3, prints
  `gates TREE MOVED — `, and leaves `verdict TREE MOVED` in the run record, with the arm in
  `tools/run-gates/run-gates.test.sh`. Red when: the runner exits 0 over the moved tree, which is the
  BASE behaviour at `tools/run-gates/run-gates.sh:1892`.
  permission: the arm's suite is held; it runs at the build's one post-build bar with
  `GATE_SELFTESTS=1`, never in this unit's pass.
- **AC2** — When two fixture bars are killed by signal 9 while a leg holds `mktemp -d` scratch, a
  third bar's `TMPDIR entries <n>` line reports the same n the first bar printed. Red when: the sweep
  is skipped, and n grows by the two leaked `gate-work.*` directories.
  fixture: a private ambient `TMPDIR` inside the arm, so another session's scratch cannot move n.
- **AC3** — When a second bar starts while the first still runs, with the turnstile off in the
  fixture, the first bar's `gate-work.*` directory survives and its verdict is unchanged, and a
  `gate-work.*` directory whose `owner` names another common dir survives too. Red when: the sweep
  keys on the name or on age alone and removes a live or foreign owner's scratch. The arm lives in
  `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC4** — When a fixture leg runs `mktemp -d` and prints the path, that path lies under the run's
  `gate-work.*/tmp` and is gone after `bash tools/run-gates/run-gates.sh` exits. Red when: `TMPDIR` is
  exported after dispatch, or not at all, and the path lands in the ambient `TMPDIR`.
- **AC5** — When the runner is started as `bash tools/run-gates/run-gates.sh` and a fixture leg
  sleeps, `/proc/<runner-pid>/cmdline` read from the beacon's `pid` file carries an absolute path
  ending in `tools/run-gates/run-gates.sh`. Red when: the re-exec is removed and the argv stays
  relative, which is the TOOL-aReapedSpinner-14 condition.
- **AC6** — When the post-build bar runs with `GATE_FULL=1 GATE_SELFTESTS=1`, the
  `template size gate selftest` leg is green under the redirected `TMPDIR`. Red when: S1 exports a
  drive-letter spelling, the four-arm failure TOOL-aTetheredScratch-2 measured.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, the runner's version constant and its
  `gov:kit` marker agree at 1.7. Red when: one of the two is bumped without the other.

## 7. Gates

`run-gates canary` · `run-gates turnstile` · `template size gate selftest` · `kit version markers` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · a leg that edits a tracked file mid-bar · none
New arm: tools/run-gates/run-gates.test.sh · two bars killed by signal 9 with scratch held · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · a live second bar beside a running first · none

## 8. Open questions

- **F1** — Should the sweep remove any dead bar's scratch on the host, as DR 21.4 U23 words it, or
  only this repository's? Options: (a) any `gate-work.*` with a dead owner; (b) only those whose
  `owner` names this common dir. (a) sweeps more, and it deletes directories belonging to another
  repository's runs, which widens the delete surface past what this unit's tier priced (M3 veto 3).
  RESOLVED (agent, 2026-09-14, delegated): (b). Another repository's bar sweeps its own on its next
  run, so AC2 is met by (b) alone.
- **F2** — Who makes the runner's argv absolute? Options: (a) every caller passes an absolute path,
  as TOOL-aReapedSpinner-14 suggests for the launcher and the hook; (b) the runner re-executes itself
  through its absolute path. Both satisfy AC5 for those two callers; only (b) also covers the
  operator's own `bash tools/run-gates/run-gates.sh`, the charter's catalogued invocation, and it
  leaves the hook adopters receive verbatim untouched. RESOLVED (agent, 2026-09-14, delegated): (b),
  the most feature-rich survivor, with no veto tripped.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U23. Diverges from DR in two places, both
  recorded in §3 and §8: the `gates-green` re-run moves to the gate-wall unit, and the absolute
  argv comes from a runner re-exec rather than from the callers.

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "sweep leaked scratch directories of a
  dead gate run and report a moved tree"` returned symbol-name neighbours only (`tree` in
  `tools/memory-recall/selftest.py`, `load_map_tree`), and its header reports `.sh` as an unscanned
  layer. That is a blind layer rather than a miss, so the seam was found by reading source: this
  unit extends `tools/run-gates/run-selftests.sh:571`, the landed per-slot `TMPDIR="$d/tmp"`
  redirect under a private `mktemp -d` root (TOOL-aPooledSweep-3), and it copies the dead-pid
  predicate of `ts_sweep_queue`.
- **DR against BASE.** DR cites `run-gates.sh:611` for `ts_alive`; BASE agrees. DR says each bar
  sweeps any `$WORK` whose pid is dead, but at BASE `WORK` is an anonymous `mktemp -d`
  (`tools/run-gates/run-gates.sh:979`) with no recorded pid, so S2's named directory and `owner`
  file are new rather than a reuse.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: `python tools/memory-recall/query.py "why does the gate runner leak scratch
  repos into TMPDIR and how should a moved tree be reported" --terms "TMPDIR mktemp scratch leak
  sweep tree_moved fingerprint gates-green absolute-path reap attributable runner beacon"`. Top hits:
  TOOL-aBranchedMandate-6, TOOL-aMeteredTurnstile-2, the aMeteredTurnstile TMPDIR measurement,
  TOOL-aReapedSpinner-14, and the TOOL-aTetheredScratch-2 spec whose refutation §4 records.
