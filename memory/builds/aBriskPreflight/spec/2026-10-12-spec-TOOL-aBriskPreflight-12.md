# TOOL-aBriskPreflight-12 — the closing review's mediums and lows: record bindings and ledgers, RB_TOOK at the child's end, the cache reset, four arms

**Status:** CLOSED · rev-3 · 2026-10-12 · node a · Tier-2 · base d19938f3 · streams tooling · order 6 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aBriskPreflight-12-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aBriskPreflight-12-acceptance-ledger.md) | journal | — |
| [2026-10-12-prompt-TOOL-aBriskPreflight-12-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aBriskPreflight-12-build-brief.md) | research | — |
| [2026-10-12-prompt-TOOL-aBriskPreflight-12-spec-brief.md](../prompts/2026-10-12-prompt-TOOL-aBriskPreflight-12-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1, confirmed two mediums and five lows
(`memory/builds/aBriskPreflight/reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md`,
sections M1, M2 and L1 to L5). BUILD-METHOD M4 promotes every one of them, batched into ONE unit, and this is
that unit. M1 reds hygiene checks 21 and 23 when the build lands, so it is owed before the lander
runs. M2 makes a fast-failing profile command report the wiring check's wall as its own duration.
The five lows are one uninitialised cache and four arms that are missing or cannot fail. Each item
takes the fix the review's skeptic judged SOUND; for M2, L2 and L3 that is the skeptic's corrected
fix, not the finder's.

## 2. Scope (IN)

- **S1** — M1, bindings. Each of the 15 unbound records in §4's Inventory gains a comment-marked
  `**Serves:**` line of kind `research` in its first 12 unfenced lines, naming the unit its
  filename ordinal names. Observed by AC1 and AC2.
- **S2** — M1, ledgers. Three `journal` records under `build/` carry an `**Evidences:**` acceptance
  ledger in unit 6's shape: one for TOOL-aBriskPreflight-4, one for TOOL-aBriskPreflight-7, and this
  unit's own, written in its pass. Observed by AC3.
- **S3** — M2, the figure. Both launch lines in `init_bounded` stamp the child's own end second with
  a builtin, and `read_bounded` sets `RB_TOOK` from that stamp when it holds one. The comment above
  `read_bounded` is rewritten to say so. Observed by AC4 and AC5.
- **S4** — M2, the record. Spec 4 takes a rev-4 that corrects its two sentences resting on the false
  premise that the wiring check's is the only `RB_TOOK` preflight prints. Observed by AC6.
- **S5** — L1. `_SJ_RC=""; _SJ_VIEW=""` is assigned at file scope in `tools/check-wiring.sh`
  beside `_SETTINGS_CACHE=""`, and the wiring suite gains the two-sided arm. Observed by AC7.
- **S6** — L2. The wiring suite gains a state whose declared merge=rows list is longer than 8000
  characters, with one undeclared family only in the first chunk and one only in the last. Observed
  by AC8.
- **S7** — L3. The driver suite's `BP4 AC4 every row names one driver pid` assertion is rewritten
  into one that can go red. Observed by AC9.
- **S8** — L4. The straggler suite gains a claim-only push arm with a sourcing marker, and its
  liveness twin. Observed by AC10.
- **S9** — L5. The driver suite's BP7 wiring-ceiling block gains the equal-pair case, and its
  host-gated skip branch counts the block's new total. Observed by AC11.

## 3. Non-goals (OUT)

- H1, the high finding. It is TOOL-aBriskPreflight-11's mechanism, and this unit edits no
  arithmetic of the ceilings instrument.
- A new class gate for L1, the review's grep of `${_X:-}`-tested globals against file-scope
  assignments. The class is already filed as `memory/gotchas/fixture-inherits-ambient-machine-state.md`,
  and S5's arm is the instance's regression gate. The class gate is a follow-up, not this batch.
- M1's left-shift beyond the fix. Checks 21 and 23 are the gate, and the class is already filed as
  `memory/gotchas/record-without-serves-or-with-a-round-counter.md`. Wiring `--print-bindings` into a
  pass's diff-scoped gates is a change to the unattended harness, which aOrientedCast owns.
- Moving any `.log` row into a fenced block, or retiring a `.log` file (§8 F1).
- Any change to a refusal text, an `UNWIRED` line or an exit status. Only the figure S3 measures moves.
- Running a merge bar or a self-test suite in the pass. Every criterion is a slice, a probe or a
  single checker run; the suites run once, at the close.

### Edges

- **hands-off** external — the one kit-version bump per touched kit, in every carrier
  `tools/check-kit-versions.sh` names, which the build-level rule places after each kit's LAST move
  in this build. This unit moves the check-wiring and unattended kits and one suite under
  `.githooks/`, and it cannot see whether a sibling moves one of them later, so the main loop owes
  the bump once every unit is terminal (§8 F5). The kickoff manifest's `watch:` line names no file
  this unit touches, verified 2026-10-12, so no `last-audit` re-stamp is owed.

## 4. Design

### Inventory

The 15 records S1 binds, every one an `A` row of `gen_build_index.py --print-bindings` at
`bb3883840`, each bound to the unit its filename ordinal names:

| Record under `memory/builds/aBriskPreflight/build/` | Serves |
|---|---|
| `2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh` | `research TOOL-aBriskPreflight-1` |
| `2026-10-11-build-TOOL-aBriskPreflight-1-run-timed.sh` | `research TOOL-aBriskPreflight-1` |
| `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` | `research TOOL-aBriskPreflight-1` |
| `2026-10-11-build-TOOL-aBriskPreflight-1-runs.log` | `research TOOL-aBriskPreflight-1` |
| `2026-10-11-build-TOOL-aBriskPreflight-1-trace-gaps.py` | `research TOOL-aBriskPreflight-1` |
| `2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` | `research TOOL-aBriskPreflight-1` |
| `2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py` | `research TOOL-aBriskPreflight-3` |
| `2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.sh` | `research TOOL-aBriskPreflight-4` |
| `2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh` | `research TOOL-aBriskPreflight-5` |
| `2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh` | `research TOOL-aBriskPreflight-6` |
| `2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh` | `research TOOL-aBriskPreflight-7` |
| `2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log` | `research TOOL-aBriskPreflight-7` |
| `2026-10-11-build-TOOL-aBriskPreflight-7-ab-run.sh` | `research TOOL-aBriskPreflight-7` |
| `2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log` | `research TOOL-aBriskPreflight-7` |
| `2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh` | `research TOOL-aBriskPreflight-7` |

The pass re-reads that report before writing and binds whatever `A` rows the build folder then
holds under the same rule, so a record a sibling added is bound too and none is missed by a stale
list. AC1 grades the 15 above, so it does not rest on a sibling's records.

Minted by this unit: the three ledger records, named
`2026-10-12-build-TOOL-aBriskPreflight-4-acceptance-ledger.md`,
`2026-10-12-build-TOOL-aBriskPreflight-7-acceptance-ledger.md` and
`2026-10-12-build-TOOL-aBriskPreflight-12-acceptance-ledger.md` under `build/`, each in hygiene
check 5's recording grammar. No function is minted, so no lexicon cell grades a new name; the
wrapper's two new variables, `_rbe` and `_rbr`, live only inside the child shell's script string.

### M1 — the binding line and the ledgers

The line is the comment-marked form `gen_build_index.py`'s `BIND_RE` admits and its selftest arms
(`#!/bin/sh` then `# **Serves:** ...`), with `aBranchedMandate-3-repro-c3.sh` as prior art.

- A `.sh` record takes it as line 2, under the shebang.
- A `.py` record takes it as line 1, above its module docstring. A comment before the docstring
  leaves the docstring the module's first statement.
- A `.log` record takes it as line 1. The ceilings instrument reads both `-7-` logs through one
  `awk`, where a line whose first field is `#` matches none of its branches. It falls to the final
  `{ prev = "" }`, and at line 1 of either file `prev` is already empty after the line before it.
  AC2 observes this rather than trusting the reading.

The two back-filled ledgers answer every criterion their spec numbers at the time of writing, in
the OBSERVED or AMENDED form `memory/HYGIENE.md` "Acceptance ledger" defines. Each answer shares a
backticked token with its criterion, as `LEDGER_TOKEN_CUTOFF` requires. Every OBSERVED line names
its source.

- Unit 4's lines come from `2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.md`, which records AC1
  to AC10.
- Unit 7's lines come from its build commit `feb305b0b`, whose message records AC1 to AC10 and AC12.
  AC11, a `grep` over `tools/unattended/README.md`, is recorded nowhere, so the pass re-runs it and
  says so on that line.
- A criterion a sibling revised after it was built, as TOOL-aBriskPreflight-11 may revise spec 7's
  constants, takes the AMENDED form naming that rev. The ledger is written at order 7, after the
  sibling is terminal.

A criterion with no recorded observation that cannot be re-observed in seconds is parked in
`RUN.md` with the reason. It is never written in the OBSERVED form untruly.

### M2 — the child's own end

The two launch lines in `init_bounded` change their wrapper script from
`: >"$RB_UP"; unset RB_UP; "$@"; exit $?` to:

```bash
: >"$RB_UP"; _rbe=$RB_UP.end; unset RB_UP; "$@"; _rbr=$?; printf "%(%s)T\n" -1 >"$_rbe"; exit $_rbr
```

The stamp path is captured before `RB_UP` is unset, so the command's environment is still as it
was: `_rbe` is a shell variable and is never exported. `printf '%(%s)T'` is a bash builtin, so no
process is added, and the driver already uses it at its `DRIVER_T0_US` assignment. The wrapper
stays a real parent, so the `$0` root token process-monitor's fence reads is unchanged. Both lines
change identically; the one-wrapper rule of `TOOL-aBoundedCeiling-6` is about one runner, which
this keeps.

`read_bounded`, after its `wait`, reads `$_d/up.end`. When it holds one all-digit second, `RB_TOOK`
is that second minus `_s`. Otherwise, as when the wrapper itself was killed before writing,
`RB_TOOK` stays the read-time figure it is today. The file is read with a builtin `read`, so no
process is added, and `rm -rf "$_d"` already removes it.

What moves: a probe read late now reports its own wall. A synchronous call's figure is the same
second, or one earlier when the read straddles a second boundary. A bounded kill still reports the
bound, because `timeout` returns to the wrapper, which then stamps. GB_WHY's `after ${RB_TOOK}s` on
a fast-failing profile reads the profile's own wall rather than the wiring check's. No refusal's
text, status or exit moves.

The comment above `read_bounded` currently says a probe read late "can only overstate a child that
had already finished". It is rewritten to say that the figure runs to the child's own end when the
wrapper stamped one, and to the read otherwise.

Spec 4 takes a rev-4, scoped `§4`. Its paragraph beginning "`RB_TOOK` runs from the child's own
start" drops the false premise that the wiring check's is the only `RB_TOOK` preflight prints, and
names `derive_gate_backstop`'s `GB_WHY` as the second reader. Its Alternatives-rejected bullet "A
wrapper stamp of each child's own end" gains a sentence saying TOOL-aBriskPreflight-12 adopted it
after the closing review found the premise false. The bullet stays as the record of what was
weighed. The §9 line names the review section M2.

### L1 — the cache reset

The line `_SJ_RC=""; _SJ_VIEW=""` is added beside `_SETTINGS_CACHE=""` in `tools/check-wiring.sh`,
before the parent's `matchers_of || :` prime. settings-merge.py's arm 17 lifts `matchers_of` alone
and reads `${_SJ_RC:-}`, so it still builds the view on its first call. The new arm extends the
suite's AC7 agent-cap block with two states.

- (a) `_SJ_RC=0` and a crafted `_SJ_VIEW` are exported over the fixture's settings file rewritten to
  the stale `Workflow`-only matcher of state AC7b. The view is captured from `matchers_of`'s own
  flatten over that block's correctly wired settings file. Expected: no `ok       agent-cap` line,
  the `wired under matcher 'Workflow'` refusal, and exit 1.
- (b) `_SJ_RC=0` and an empty `_SJ_VIEW` are exported over the correctly wired fixture. Expected:
  `ok       agent-cap`.

Before the fix, (a) prints `ok` over the injected view and (b) prints `UNWIRED`, so both sides red.
Not over a missing settings file, as rev-2 had it: the agent-cap arm re-reads the file for the
shipped path after `wired` answers, so a missing file reds there with or without the inherited view,
and (a) was observed passing under the staged break. A stale file is graded by the view alone.

### L2 — the chunk flush

The new state follows state 5d of the AC10 block, from 5d's restored green tree. It commits enough
`memory/backlog/*.md` indexes, which the fixture's `.gitattributes` declares `merge=rows`, for the
declared list to exceed 8000 characters. It uses many paths of about 50 characters rather than a
few long ones, to stay inside Windows MAX_PATH. The index that `git ls-files` lists FIRST leads one
row with the undeclared family `QFIRST`, and the index it lists LAST leads one row with `QLAST`;
every other index is empty.

Two assertions follow.

- A precondition: the fixture's declared list, measured by the same
  `git ls-files | git check-attr --stdin merge` the arm runs, sums past 8000 characters. Otherwise
  the state reds as a fixture no-op. With the sum past 8000 there are at least two chunks, so the
  first index is harvested only by the in-loop flush, and that is the durable liveness proof.
- The `UNWIRED  merge` line names both `QFIRST` and `QLAST`.

At pass time, the in-loop `sed -n -e "$expr" -- "$@";` rewritten to `:;` is observed to red the arm.

### L3 — a pid assertion that can fail

The assertion reads the four rows of `tRun.procs` from the BP4 AC2 run. It asserts three things:
field 1 holds four distinct all-digit values; field 3 is all-digit and equal on every row; and
field 3 equals no field-1 value. The label says what it grades, and is renamed to
`BP4 AC4 each row names its own child pid and the one driver pid`. The staged break writes a
constant into field 1. That is a break of identity rather than a simpler substitute value, so the
`staged-break-substitutes-a-synthetic-value` class does not apply.

### L4 — the claim push skips the layer

The arm sits after the S4 arms in fixture F1. It builds a hooks directory as a copy of F1's `hk`
whose `straggler-guard.sh` is a stub that creates a marker file when sourced, and points
`core.hooksPath` at it. Two pushes follow.

- A root commit over `mktree </dev/null`, pushed alone to `refs/gov/runs/y`. Expected: the push
  exits 0 and the marker is absent.
- The liveness twin: a root commit over a non-empty tree, pushed alone to `refs/gov/runs/z`.
  Expected: the marker exists.

The arm then restores `core.hooksPath` to F1's `hk`. The stub defines no `init_straggler_guard`, so
the hook's setup condition is false after sourcing and the twin's push is not refused by the stub.

### L5 — the equal pair

The equal-pair case is added inside the BP7 block's host-gated `else` branch. It uses a conf
declaring `GATE_BOUND="2"`, the driver copy's `WIRING_CEILING` mutated to `"2"`, and the 30 s
sleeper. It asserts `did not answer within the declared 2s bound` and no `wall-clock ceiling`. The
skip branch's counted figure, `n=$((n+12))` today, rises by the number of assertions added, so a
host without `timeout -k` still counts every one.

### Files touched (estimate)

`tools/check-wiring.sh`
`tools/check-wiring.test.sh`
`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`
`.githooks/straggler-guard.test.sh`
`memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md`
`memory/builds/aBriskPreflight/build/` (the 15 records and the three ledgers)
`memory/map/generated/symbols.json` (only if an arm adds a shell function, which this design avoids)

### Rollout

Live, with no flag. Every change is a record, an arm, a figure or an initialisation that removes
an inherited-state path; none adds a refusal. Order 7 places this unit after every other unit of
the build. If a sibling shares order 7 and writes a file in this list — TOOL-aBriskPreflight-11
writes the ceilings instrument — the two are not disjoint under M6 clause 1, and they must be
sequenced rather than dispatched together.

### Alternatives rejected

- M1: moving each `.log`'s rows into a fenced block of the unit's `.md` record and deleting the
  `.log` (§8 F1).
- M2: dropping `after ${RB_TOOK}s` from GB_WHY when it was read from a profile handle (§8 F2).
- L2: a broken copy of `tools/check-wiring.sh` run by the suite as a durable twin (§8 F3).
- L3: deleting the assertion with a note (§8 F4).

## 5. Production-readiness checklist

- security — L1 closes an inherited-environment path: an exported `_SJ_RC` can no longer stand in for
  the settings read. The end-stamp file sits in the same private `mktemp -d` as the capture files and
  is removed with them. No new write path or surface.
- perf / scale — No process is added: the stamp and its read are builtins. Each new arm adds seconds,
  except L2's state, which commits about 160 files once in its fixture.
- error / empty / loading states — A missing, empty or non-numeric end stamp falls back to today's
  read-time figure.
- observability — S3 makes one printed duration true where it was false. No line is added or lost.
- risks — The ceilings instrument's output under S1's `.log` lines (AC2). A ledger line whose source
  is missing (§4, parked rather than written).
- testing — The six new arms of §7, each observed red on its staged break at pass time, plus AC5's
  scratch probe.
- migration — N/A — no format, state or conf key changes.
- user docs — N/A — this repository has no `help/` tree, and the driver comment S3 rewrites is the
  runner's documentation.

## 6. Acceptance criteria

Each slice is the suite's prologue plus the one block named, run as a temporary script whose kit
directory is pinned, from the run's scratch directory, and deleted before the pass commits. A
fixture repository goes under a short path in TEMP, never in this worktree. "Restored, it passes"
closes every staged break.

- **AC1** — When `python tools/memory-tree/gen_build_index.py --print-bindings` runs after the pass,
  each of the 15 records in §4's Inventory prints an `S` row of kind `research` naming exactly the
  unit the Inventory names, and none prints an `A` row.
  Red when: any of the 15 still prints `no Serves line in the first 12 unfenced lines`, or binds
  another unit.
- **AC2** — When `bash memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh`
  runs at the pass's parent and again after S1, its stdout and exit status are byte-identical. Also,
  `bash -n` exits 0 on each bound `.sh` record and `python -m py_compile` exits 0 on each bound `.py`
  record.
  Red when: a `.log` binding line moves a row the instrument reads, or a binding line breaks a
  script's syntax.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh --offenders` runs with the pass's
  records staged, no `check 21` line names any of the 15 records, and no `check 23` line names
  TOOL-aBriskPreflight-4, TOOL-aBriskPreflight-7 or TOOL-aBriskPreflight-12.
  Red when: a ledger misses a criterion its spec numbers, or answers one with a token the criterion
  does not carry.
  cost: the full hygiene engine, minutes on node `a`, not seconds.
  fixture: the ledgers are untracked until staged, and the bindings report reads tracked files only.
- **AC4** — When the slice of the driver suite's BP4 block with the new arm runs against the built
  driver, the arm's preflight prints `the declared GATE_PROFILE_CMD exited 3 after <n>s` with n below
  12. In that arm's `pf_fixture` the wiring stub runs `sleep 12; exit 0`, the lander stub `exit 1`,
  and the profile stub `exit 3`. With `read_bounded`'s end-stamp read deleted as a staged break, n
  reads 12 or more and the arm reds.
  Red when: `RB_TOOK` still runs to the read, so the profile reports the wiring stub's wall.
  figure: 12 s is a PINNED stub value; n is DERIVED per run.
- **AC5** — When a scratch probe extracts `run_bounded`, `init_bounded` and `read_bounded` from the
  built driver by their definition lines and sources them with `GATE_BOUND=2`, `GATE_BOUND_LIVE=1`,
  `ROOT` set and `write_proc_record` stubbed, all of the following hold.
  - `run_bounded bash -c 'sleep 30'` returns 124 or 137 with `RB_TOOK` from 2 to 9.
  - `run_bounded bash -c 'exit 3'` returns 3.
  - `init_bounded bash -c 'exit 4'`, read through `read_bounded` 5 s later, returns 4 with `RB_TOOK`
    at most 3, the margin being two spawns at node `a`'s measured cost.
  - The same with the handle's `up.end` deleted before the read reports `RB_TOOK` of 5 or more.
  - `run_bounded env` leaves neither `RB_UP` nor `_rbe` in `RB_STDOUT`.
  Red when: the stamp is lost on a bounded kill, a late read overstates, the fallback is missing, or
  the wrapper leaks a variable into the command's environment.
  figure: 2, 3, 5, 9 and 30 are PINNED probe values; each `RB_TOOK` is DERIVED.
- **AC6** — When `grep -n "can only overstate" tools/unattended/unattended.sh` and
  `grep -n "The one probe whose" memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md`
  run, both print nothing. Spec 4's status header reads `rev-4`, and its §9 carries a rev-4 line
  naming `§4` and the review's M2.
  Red when: either false premise still stands, or spec 4 changed with no rev.
- **AC7** — When the slice of the wiring suite's AC7 block with S5's two states runs against the
  built script, state (a) prints no `ok       agent-cap` line, prints the `wired under matcher
  'Workflow'` refusal and exits 1, and state (b) prints
  `ok       agent-cap`. With the file-scope `_SJ_RC=""; _SJ_VIEW=""` line deleted as a staged break,
  both states red.
  Red when: an inherited `_SJ_RC` still stands in for the settings read.
- **AC8** — When the slice of the wiring suite's AC10 block with S6's state runs against the built
  script, the precondition finds the declared list longer than 8000 characters, and one
  `UNWIRED  merge` line carrying `does not declare` names both `QFIRST` and `QLAST`. With the in-loop
  `sed -n -e "$expr" -- "$@";` rewritten to `:;` as a staged break, `QFIRST` is absent and the state
  reds.
  Red when: the flush loses the first chunk, or the fixture never crosses 8000 characters.
  figure: 8000 is the script's PINNED chunk limit; the fixture's length is DERIVED per run.
- **AC9** — When the slice of the driver suite's BP4 block runs against the built driver, the
  rewritten pid assertion passes. With `write_proc_record`'s first printed field set to the constant
  `999999` as a staged break, it reds. That constant is a pid no process holds, not `1`, because the
  driver's reaper reads that ledger and a break must not name a live process. The old assertion, `BP4 AC4 every row names one driver pid`, is run
  once under that same break before the rewrite and passes, which is the defect.
  Red when: the new assertion passes under the constant, as the old one does.
- **AC10** — When the slice of the straggler suite's F1 setup, F3 and S4 arms with S8's arm runs,
  the push to `refs/gov/runs/y` exits 0 with no marker, and the push to `refs/gov/runs/z` leaves the
  marker. With the predicate's `"tree 0"` comparison in `.githooks/pre-push` changed to
  `"tree X"` as a staged break, the first push leaves the marker and the arm reds.
  Red when: a claim-only push still sources the straggler library.
- **AC11** — When the slice of the driver suite's BP7 block with S9's case runs against the built
  driver, the case prints `did not answer within the declared 2s bound` and no `wall-clock ceiling`.
  With `derive_wiring_bound`'s `-lt` changed to `-le` as a staged break, it reds. The skip branch's
  `n=$((n+<k>))` equals the number of assertions the `else` branch makes, counted by `grep` over
  the block.
  Red when: an equal pair is given to the ceiling, or the skip branch undercounts.

## 7. Gates

`unattended kit gate` · `check-wiring self-test` · `straggler-guard arms` · `transition-audit arms` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `testsuite counts (every bar self-test prints one)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `pass-order history` · `brief-recorded`

The pass verifies with AC1 to AC11 only. The listed legs run once, at the close, after the last
unit is terminal. `kit epoch` reds until the hand-off in §3 Edges is discharged.

New arm: tools/unattended/unattended.test.sh · covers AC4 · a profile stub exiting 3 at once behind a wiring stub sleeping 12 s, red while RB_TOOK runs to the read · none

New arm: tools/unattended/unattended.test.sh · covers AC9 · the BP4 AC2 run's four ledger rows, red when field 1 is one constant · none

New arm: tools/unattended/unattended.test.sh · covers AC11 · a 2 s WIRING_CEILING under a 2 s GATE_BOUND, red at -le · the BP7 skip branch's counted figure

New arm: tools/check-wiring.test.sh · covers AC7 · an exported _SJ_RC=0 over a stale and over a correct settings file, red without the file-scope reset · none

New arm: tools/check-wiring.test.sh · covers AC8 · a merge=rows list past 8000 characters with QFIRST first and QLAST last, red when the in-loop flush reads nothing · none

New arm: .githooks/straggler-guard.test.sh · covers AC10 · a sourcing-marker stub library under an empty-tree and a non-empty-tree claim push, red when the predicate stops matching · none

## 8. Open questions

- **F1 — How a `.log` record is bound.** (a) A comment-marked `**Serves:**` line at line 1. (b) Its
  rows moved into a fenced block of the unit's `.md` record, and the `.log` deleted.
  Recommendation: (a). RESOLVED (agent, 2026-10-12, delegated): (a), by M3's rule. (b) breaks the
  ceilings instrument, which reads both `-7-` logs by path, so it fails AC2. It also strands the
  paths `RUN.md`'s dispatch rows name. (a) keeps every reader and is observed byte-identical by AC2.
- **F2 — How GB_WHY stops misreporting the profile's duration.** (a) The end stamp of §4.
  (b) Dropping `after ${RB_TOOK}s` from GB_WHY when it was read from a profile handle.
  Recommendation: (a). RESOLVED (agent, 2026-10-12, delegated): (a), by M3's rule. (b) deletes
  a figure and fixes one reader; every later late-read probe would inherit the same lie. (a) makes the
  figure true for every reader at no process cost. It changes the wrapper text, which the brief and
  the review's skeptic both name, and touches no governance carrier.
- **F3 — How S6's state proves it reaches the in-loop flush.** (a) A precondition assertion that
  the declared list exceeds 8000 characters, plus the staged break observed at pass time. (b) A
  durable twin running a broken copy of `tools/check-wiring.sh`. Recommendation: (a).
  RESOLVED (agent, 2026-10-12, delegated): (a). With the list past 8000 the first index can be
  harvested only by the in-loop flush, so `QFIRST` present is itself the liveness signal, in every
  run. (b) runs the script from another path, where its kit resolution is UNVERIFIED, and that is a
  second way for the twin to red for a reason other than the flush.
- **F4 — Rewrite or delete the BP4 AC4 pid assertion.** Recommendation: rewrite.
  RESOLVED (agent, 2026-10-12, delegated): rewrite, by M3's rule. It grades spec 4 AC4's pid clause,
  where deletion leaves that clause graded by row presence only.
- **F5 — Who bumps the touched kits' versions.** (a) This unit, in its pass. (b) The main loop, once
  every unit is terminal. Recommendation: (b). RESOLVED (agent, 2026-10-12, delegated): (b). The
  build-level rule bumps each kit once after its last move, and this unit cannot see whether a
  sibling moves the unattended kit later. A bump here could be re-owed by that move, and the
  `kit epoch` leg would then red at the close anyway.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, promoted from the closing diff review round 1 (M1, M2, L1 to
  L5), authored by this run and unreviewed.
- rev-2 · 2026-10-12 · status header (§1 header line) order 7 -> 6, scope S1 to S7 unchanged: no item
  here depends on TOOL-aBriskPreflight-11, whose F2 is parked for the owner, and order 7 would hold
  this unit behind that park at check 49.
- rev-3 · 2026-10-12 · §4 L1 state (a), AC7, AC9 and §7's AC7 arm line, found at build time. (a)
  ran over NO settings file, and under the staged break it still printed `UNWIRED  agent-cap`,
  because the arm re-reads the file for the shipped path, so it could not red; it now runs over the
  stale `Workflow`-only file of state AC7b. AC9's staged-break constant `1` -> `999999`, a pid no
  process holds, since the driver's reaper reads the ledger the break writes.

## 10. Reuse audit

Every item extends a seam that already exists; no new mechanism is introduced.

- `python tools/codebase-map/reuse_lookup.py "bounded child elapsed time measured to its own end"`
  ranks `init_bounded` in `tools/unattended/unattended.sh`. That runner, with `read_bounded`, is the
  seam S3 extends. The `printf '%(%s)T'` builtin is prior art in the same file.
- `python tools/codebase-map/reuse_lookup.py "record binding Serves line on a build instrument"`
  ranks only name-stem neighbours, none of them a binding seam. The seam is the grammar itself:
  `BIND_RE` in `tools/memory-tree/gen_build_index.py`, whose selftest arms the comment-marked form.
  `aBranchedMandate-3-repro-c3.sh` is prior art for that form.
- The ledgers copy `2026-10-11-build-TOOL-aBriskPreflight-6-acceptance-ledger.md`.
- S5 copies the `_SETTINGS_CACHE=""` idiom at `tools/check-wiring.sh` line 95.
- Each arm extends an existing block: BP4's `pf_fixture`, the BP7 ceiling block, state 5d of the
  wiring suite's AC10 block, its AC7 agent-cap block, and the straggler suite's S4 arms.
- The recall probe's hits, verified against source at writing: `TOOL-aClosedDocket-3` pins the
  bounded arms to `RB_TOOK` rather than the harness clock, so S3 must keep a bounded kill's figure
  at the bound, which §4 does. Spec 4's §4 is the record S4 corrects.

Recall terms used: `--terms "RB_TOOK read_bounded init_bounded wrapper end stamp elapsed probe preflight Serves binding journal acceptance ledger"`,
with the question "how should a bounded probe report the elapsed time of a child that finished
before it was read, and how do build instruments carry a record binding".
