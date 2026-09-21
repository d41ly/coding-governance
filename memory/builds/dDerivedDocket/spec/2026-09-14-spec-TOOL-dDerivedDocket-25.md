# TOOL-dDerivedDocket-25 — runner scratch hygiene and a tree-moved exit

**Status:** CLOSED · rev-6 · 2026-09-22 · node d · Tier-2 · base fb07ca25 · streams tooling · order 24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-22-build-TOOL-dDerivedDocket-25-1-acceptance-ledger.md](../build/2026-09-22-build-TOOL-dDerivedDocket-25-1-acceptance-ledger.md) | journal | — |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |
| [2026-09-20-review-TOOL-dDerivedDocket-21-spec-audit-g4-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-21-spec-audit-g4-round2.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

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
  dispatches. The ambient `TMPDIR` is `/tmp` when the variable is unset or empty, which is where
  `mktemp -d` itself falls back and is the state the kickoff manifest's `scratch-guard` trap records
  on a node of this repository. At start each bar sweeps every `gate-work.*` directory whose `owner` names this
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
- **S5** — the TREE MOVED exit. When `tree_moved=yes` (`tools/run-gates/run-gates.sh:1818-1819`)
  and no leg failed, the runner prints `gates TREE MOVED — the tree changed while the bar ran, so no
  verdict describes it`, writes `verdict TREE MOVED` into the run record, writes no full-green
  stamp, and exits 3. A bar that failed AND moved stays RED with exit 1, and its RED line names the
  move. The header's exit-code line (`tools/run-gates/run-gates.sh:3`) and
  `tools/run-gates/README.md` gain exit 3. Observed by AC1 and AC7 for the behaviour and by AC10 for
  the two documents, which no behavioural criterion can read.
- **S6** — the kit version. NOT OBSERVED by a criterion here: this unit moves no version constant. A
  new exit code is a contract change a caller reads, so the run-gates kit must move, and it moves
  once in this build's landing range, in `TOOL-dDerivedDocket-1`, whose S9 moves it; this unit's
  bytes ride that move. `kit version markers` grades only the final tree's constant-marker
  agreement.
- **S7** — the kickoff manifest. `memory/guides/SESSION-KICKOFF.md`'s trap that every hermetic leg
  runs `mktemp -d` into the ambient `TMPDIR` and that a reader should point `TMPDIR` at an empty dir
  before blaming the diff (`:242-245` at BASE) is rewritten: the runner now redirects each leg's
  `TMPDIR` into its own scratch and sweeps a dead bar's, so the growth comes only from bars that
  predate this unit or run another repository. `last-audit` is re-stamped in the same commit with a
  delta line in the commit message, because `tools/run-gates/run-gates.sh` is in the manifest's
  `watch:` list. The rewrite LANDS NET ZERO on that carrier. The passage is the four-line §B trap
  bullet at `memory/guides/SESSION-KICKOFF.md:242-245`, and its replacement is written no longer
  than the bullet it replaces. The measured detail it drops, the node-`a` entry count and the advice
  to point `TMPDIR` at an empty dir, moves to the scratch section of `tools/run-gates/README.md`,
  the document that owns the runner's scratch and which S5 already has this unit writing. Observed
  by AC8 and AC9.

## 3. Non-goals (OUT)

- **The driver's reading of exit 3.** DR 21.4 U23 put "`gates-green` reads that as UNMET and
  re-runs once" in this unit. It moves to the gate-wall unit named in the edges below, which already
  rewrites `gates-green` and is the one unit of the three that may run the unattended suite (D12-i8).
  The gate-wall unit's `gates-green` table is then the one place the driver maps a runner exit; the
  inherited-red policy unit's reading of exit 1 is an arm of that table, declared by an edge between
  those two units. The pre-push hook needs no change for exit 3: any non-zero status already blocks
  a push.
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
`tools/run-gates/run-gates.turnstile.test.sh`, `tools/run-gates/run-gates.runlog.test.sh`,
`tools/run-gates/README.md`, `memory/guides/SESSION-KICKOFF.md`, `memory/map/features/run-gates.md`
(prose refresh on touch).

### Alternatives rejected

- **Redirect `TMPDIR` to an external root.** TOOL-aTetheredScratch-2 rev-1 specced it and its audit
  refuted it by measurement: no external root exists on these nodes, and a drive-letter spelling
  breaks four arms of the template-size self-test because `tools/check-template-size.sh` normalises
  through `cd && pwd` while `mktemp` echoes `TMPDIR` verbatim. S1 differs on the discriminating
  point: its root is the runner's own `mktemp -d` result, in the MSYS spelling, and AC6 is the
  observation that the spelling hazard did not return.
- **An EXIT trap per leg** (TOOL-aMeteredTurnstile-2's first suggestion). It needs an edit in each of
  the legs' `mktemp -d` sites and still leaks on signal 9. One export plus one sweep covers both.

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
  BASE behaviour at `tools/run-gates/run-gates.sh:1898`.
  permission: the arm's suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC2** — When two fixture bars are killed by signal 9 while a leg holds `mktemp -d` scratch, a
  third bar's `TMPDIR entries <n>` line reports the same n the first bar printed. Red when: the sweep
  is skipped, and n grows by the two leaked `gate-work.*` directories.
  fixture: a private ambient `TMPDIR` inside the arm, so another session's scratch cannot move n.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC3** — When a second bar starts while the first still runs, with the turnstile off in the
  fixture, the first bar's `gate-work.*` directory survives and its verdict is unchanged, and a
  `gate-work.*` directory whose `owner` names another common dir survives too. Red when: the sweep
  keys on the name or on age alone and removes a live or foreign owner's scratch. The arm lives in
  `tools/run-gates/run-gates.turnstile.test.sh`.
  permission: the turnstile suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC4** — When a fixture leg runs `mktemp -d` and prints the path, that path lies under the run's
  `gate-work.*/tmp` and is gone after `bash tools/run-gates/run-gates.sh` exits. Red when: `TMPDIR` is
  exported after dispatch, or not at all, and the path lands in the ambient `TMPDIR`.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC5** — When the runner is started as `bash tools/run-gates/run-gates.sh` and a fixture leg
  sleeps, `/proc/<runner-pid>/cmdline` read from the beacon's `pid` file carries an absolute path
  ending in `tools/run-gates/run-gates.sh`. Red when: the re-exec is removed and the argv stays
  relative, which is the TOOL-aReapedSpinner-14 condition.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC6** — When the post-build bar runs with `GATE_FULL=1 GATE_SELFTESTS=1`, the
  `template size gate selftest` leg is green under the redirected `TMPDIR`. Red when: S1 exports a
  drive-letter spelling, the four-arm failure TOOL-aTetheredScratch-2 measured.
  permission: the bar it names IS the build's one post-build bar, run after the last unit; this
  unit's pass runs no bar.
- **AC7** — When one fixture leg fails an assertion while another edits a tracked file mid-bar,
  `bash tools/run-gates/run-gates.sh` in the canary's scratch repo exits 1, its RED line names the
  moved tree, and the run record holds no `verdict TREE MOVED`.
  Red when: TREE MOVED outranks a failed leg, so exit 3 hides a real red and the gate-wall unit's
  re-run ends UNMET naming the move instead of the leg.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs on the unit's commit, check 5
  passes with the re-stamped `last-audit`, and the §B `TMPDIR` trap names the runner's own scratch
  redirect.
  Red when: the stamp moves and the trap still says every hermetic leg writes into the ambient
  `TMPDIR`, which passes the gate while the stamp asserts a re-verification that did not happen.
  permission: the command is the `kickoff-manifest ratchet` leg; it runs at the build's one
  post-build bar.
- **AC9** — When `wc -c < memory/guides/SESSION-KICKOFF.md` is read at this unit's commit and at its
  parent, the reading at this unit's commit is NO LARGER than the reading at the parent, and
  `grep -c 'at an empty dir' tools/run-gates/README.md` prints at least 1.
  Red when: S7's replacement is longer than the trap bullet it replaces, so a carrier other units of
  this build write too grows on a unit that priced itself at nothing; or the measured detail is dropped
  from the manifest and lands in no other document, so a trap a session front-loads leaves the tree
  silently. The second witness is a phrase from the ADVICE, not `mktemp -d`: S1 already puts that
  token in every sentence this unit writes about the runner's scratch, so a witness on it would
  print 1 whether the displaced detail landed or not. The cap half is red by the `memory hygiene` leg's index-cap check; the NET delta against
  the parent is the half no leg reads, which is why this criterion reads it.
  permission: both readings are `wc -c` and `grep -c` over tracked files in the pass. NO CAP IS
  RAISED by this unit: moving the 61440 is an owner turn.
- **AC10** — When `tools/run-gates/run-gates.sh` and `tools/run-gates/README.md` are read at this
  unit's commit, the runner's own exit-code header line (`tools/run-gates/run-gates.sh:3`) names
  exit 3 as TREE MOVED beside the exits 0, 1 and 2 it carries at BASE, and the README's exit-code
  section names exit 3 as TREE MOVED too.
  Red when: either stops at exit 2, so a caller-facing contract exists only in behaviour and a reader
  of the runner meets TREE MOVED as an undocumented status. AC1 and AC7 grade the BEHAVIOUR and
  neither reads file text; unit 26's AC8 reads the README half again for exit 4 and the precedence of
  exits 1, 3 and 4, but that is a LATER unit, so nothing in this unit's own pass would notice the
  omission.
  permission: both are reads of tracked files in the pass; no gate leg and no suite is involved.

## 7. Gates

`run-gates canary` · `run-gates turnstile` · `run-gates run-log line` · `template size gate selftest` · `kit version markers` · `kickoff-manifest ratchet` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · a leg that edits a tracked file mid-bar · the canary's executed-assertion floor
New arm: tools/run-gates/run-gates.test.sh · a failing leg beside a leg that edits a tracked file mid-bar · the canary's executed-assertion floor
New arm: tools/run-gates/run-gates.test.sh · two bars killed by signal 9 with scratch held · the canary's executed-assertion floor
New arm: tools/run-gates/run-gates.turnstile.test.sh · a live second bar beside a running first · the turnstile suite's executed-assertion floor
New arm: tools/run-gates/run-gates.runlog.test.sh · a leg that edits a tracked file mid-bar, joined to the run-log exit table · the run-log suite's executed-assertion floor

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
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 M7, M20, L7, H5; G1 M11). M7 with G1 M11:
  the run-gates move is unit 1's, so S6 is a NOT OBSERVED pointer, `tools/run-gates/kit.toml` leaves
  Files touched, and the rev-1 version pin is gone; AC7 now holds M20's failed-and-moved criterion,
  and S5 names it. L7: S7 rewrites the kickoff manifest's TMPDIR trap and re-stamps it (AC8, gate
  `kickoff-manifest ratchet`). H5: §3's claim that every driver reading of a runner exit sits in one
  spec now names the inherited-red arm and its edge.
- rev-3 · 2026-09-16 · regrounded on fb07ca25 (origin/main). Line citations re-read at fb07ca25,
  where TOOL-aRatifiedRulings-4's bound-0 kill tail in `report_one` pushed the runner's later lines
  down: §2 S5's `tree_moved` pair is `run-gates.sh:1818-1819` and §6 AC1's green exit is
  `run-gates.sh:1898`, while every cite above line 1468 held. §2 S7's kickoff trap is `:242-245`,
  its text unchanged. §2 S2 says the ambient `TMPDIR` is `/tmp` when the variable is empty, the
  state the kickoff manifest's `scratch-guard` trap (aProbedUnit) records, so S3's entries count
  names a real directory there. §4 drops a `mktemp -d` site count this rev could not reproduce at
  either base. §10's BASE paragraph describes fb07ca25. No S-item landed on main, and no landed
  build sweeps a dead bar's scratch or gives the runner a TREE MOVED exit. §7's four `New arm:`
  lines name the floor each one raises instead of `none`: both suites carry an executed-assertion
  floor, and both moved on main in the window (TOOL-aRatifiedRulings-4 raised the canary's, and
  577cffbb raised the turnstile's with the claim control it gave scenario 4c).
  Extended 2026-09-20, same base, by the build-wide consolidation pass. §6's six criteria are
  evened out: AC2 to AC6 and AC8 gain the `permission:` line AC1 and AC7 already carried, so
  every criterion whose observation is a held suite or a merge-bar leg command places that run
  at the build's one post-build bar. That folds the CONSERVATIVE reading of BUILD-METHOD M6 and
  `tools/unattended/gate-guard.js`; the ruling conflict behind it is parked for the owner in
  this build's `RUN.md` and is not decided here. AC8's command is the `kickoff-manifest ratchet`
  leg's own argv, which is why it defers too. §7's four `New arm:` third fields already name the
  floor each raises and are unchanged: neither suite this unit touches is one of the two that
  pin an executed-assertion floor under the build-wide arm-line rule. The one capped carrier
  this unit writes is `memory/guides/SESSION-KICKOFF.md`, 20057 bytes against the 61440 its
  class declares.
  Extended again 2026-09-20, same base, by the closing consolidation pass, which applied the
  build's NET-ZERO rule to every capped carrier rather than only to the contested ones. The
  headroom argument is no longer load-bearing: §2 S7 now NAMES the passage it rewrites, the
  §B trap bullet at `memory/guides/SESSION-KICKOFF.md:242-245`, and the document its dropped
  detail moves to, `tools/run-gates/README.md`, and new §6 AC9 reads the carrier at this unit's
  commit against its PARENT and reds any growth. Naming the passage is what lets the orchestrator
  see that no sibling unit trims the same lines: inside this closing set the passages taken are
  this §B trap, the ceiling line, the §B M6 claim and the `last-audit:` stamp, and specs outside
  the set write the same file, so the join across the whole build is the orchestrator's and no
  count of it is typed here. The header date moves
  to the last-change date; the rev does not, because the unit's scope did not move.
  Verified in the same pass: AC9's second witness was `grep -c 'mktemp -d'`, which S1 already puts
  into every sentence this unit writes about the runner's scratch, so it would have printed 1
  whether the displaced detail landed or not — a witness that cannot fail for the reason its
  `Red when:` gives. It now reads a phrase from the ADVICE that moves, `at an empty dir`, which
  appears nowhere in `tools/run-gates/README.md` at HEAD.
  Closed 2026-09-20, same base, by the last consolidation pass before the spec audits re-run.
  Every `permission:` line naming a HELD leg now spells the VERIFYING run
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` instead of "with `GATE_SELFTESTS=1`", so
  the canary, the turnstile suite and the template-size self-test cannot be read as covered by a
  plain bar. Two rulings reached this spec and changed nothing in it. §2 S7 REWRITES a real §B
  passage, the `TMPDIR` trap bullet, and does not merely re-stamp `last-audit:`, so it is a
  genuine replacement rather than the bookkeeping stamp the orchestrator ruled is neither a trim
  nor a collision. And the scoped net-zero rule binds a carrier with less than 2048 bytes free:
  `memory/guides/SESSION-KICKOFF.md` has 41383 of its 61440 free, so AC9's no-larger reading is
  STRICTER than the rule now requires; it is kept as written because a replacement written no
  longer than what it replaces is what §2 S7 promises, and a criterion should grade the promise.
  Rule 1's narrow reading moved nothing: AC8 runs `manifest-check.sh` over the real tree and keeps
  deferring. The header date stays at the last-change date; the rev does not move.
- rev-4 · 2026-09-20 · spec-audit round 3 fold, G4 round 2 · S5 · AC10. L1: S5 requires the runner's
  own exit-code header line and the README's exit-code section to gain exit 3, and declared itself
  observed by AC1 and AC7 — two criteria that grade BEHAVIOUR and read no file text, AC1 the exit and
  the printed line, AC7 the exit-1 precedence. AC9's only grep of the README reads `at an empty dir`,
  a phrase from S7's displaced advice. So the documentation half of S5 was unobserved, and unit 26's
  AC8, which does read the README's exit-code section, is a later unit whose pass could not catch an
  omission made here. New AC10 reads both documents at this unit's commit and reds when either stops
  at exit 2, and S5's `Observed by` now splits the behaviour half from the document half. Nothing
  else moved: §7 gains no leg, because both readings are tracked-file reads in the pass, and the
  carrier accounting is untouched — `memory/guides/SESSION-KICKOFF.md` still has 41383 of its 61440
  free, so the scoped net-zero rule still does not bind it and AC9 stays voluntarily stricter.
- rev-5 · 2026-09-21 · order re-declared from 25 to 24 in the status header only, derived from the §3 edges. The remaining
  units run in concurrent waves where M6's three conditions hold (owner, 2026-09-21); a wave shares
  one order, and this unit runs at order 24, beside TOOL-dDerivedDocket-30. No criterion, design or edge moved.
- rev-6 · 2026-09-22 · the build pass, on the tree at 5c33fd5a (origin/main merged in at c23d5701), where
  every §2 citation had moved down about 600 lines and still named the code it describes. Three
  divergences, each found by reading a consumer the design did not list. (1) The run-log suite
  enumerates every `exit` below the runner's `cleanup` trap and reds one with no arm or exemption,
  so S5's exit 3 needs an arm there: an AC2 bar over a moved tree, joined to that table, which puts
  `tools/run-gates/run-gates.runlog.test.sh` in Files touched and its leg on §7. Its exit text is the
  whole `echo "gates TREE MOVED — …"; exit 3` line and never a bare `exit 3`, which the suite's own
  staged break plants as the unarmed exit it must catch. (2) S3's line counts a directory other legs
  write into concurrently, and two readers compare whole bar outputs: the canary's width arm, which
  now filters `TMPDIR entries` the way it filters the profile line and checks its presence, and the
  run-log suite's failed-append arm, whose bars now run over a private ambient `TMPDIR`. (3) The
  `$WORK/tmp` refusal of §5 sits ABOVE the `cleanup` trap beside the `mktemp -d` it extends, removes
  `WORK` itself and needs no run-log arm; the sweep removes a dead dir's `owner` record LAST, so a
  sweep that fails part-way leaves a dir the next bar can still prove dead. S4's re-exec also skips a
  `$0` naming no file beside the kit dir and carries `-x`. The canary's arms are its section 8,
  section 7 being the red attribution's. No criterion moved.

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "sweep leaked scratch directories of a
  dead gate run and report a moved tree"` returned symbol-name neighbours only (`tree` in
  `tools/memory-recall/selftest.py`, `load_map_tree`), and its header reports `.sh` as an unscanned
  layer. That is a blind layer rather than a miss, so the seam was found by reading source: this
  unit extends `tools/run-gates/run-selftests.sh:571`, the landed per-slot `TMPDIR="$d/tmp"`
  redirect under a private `mktemp -d` root (TOOL-aPooledSweep-3), and it copies the dead-pid
  predicate of `ts_sweep_queue`.
- **DR against BASE fb07ca25.** DR cites `run-gates.sh:611` for `ts_alive`; BASE agrees. DR says
  each bar sweeps any `$WORK` whose pid is dead, but at BASE `WORK` is still an anonymous
  `mktemp -d` (`tools/run-gates/run-gates.sh:979`) with no recorded pid, so S2's named directory and
  `owner` file are new rather than a reuse. Between `abac6d59` and fb07ca25 the runner moved only in
  its version pair and in `report_one`'s kill tail: `KITDIR`, `ts_alive`, `ts_sweep_queue`, `WORK`,
  `cleanup` and the exit-code header did not move, no `TMPDIR` export was added, and
  `run-selftests.sh`, `.githooks/pre-push` and `tools/process-monitor/scope.py` did not change. The
  turnstile suite gained a claim control on its ceiling arm, which AC3's new arm sits beside.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: `python tools/memory-recall/query.py "why does the gate runner leak scratch
  repos into TMPDIR and how should a moved tree be reported" --terms "TMPDIR mktemp scratch leak
  sweep tree_moved fingerprint gates-green absolute-path reap attributable runner beacon"`. Top hits:
  TOOL-aBranchedMandate-6, TOOL-aMeteredTurnstile-2, the aMeteredTurnstile TMPDIR measurement,
  TOOL-aReapedSpinner-14, and the TOOL-aTetheredScratch-2 spec whose refutation §4 records.
