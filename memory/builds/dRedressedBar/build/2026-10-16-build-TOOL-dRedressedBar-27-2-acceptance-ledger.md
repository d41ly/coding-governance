# TOOL-dRedressedBar-27 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-27

The build pass of spec 27 rev-2. It restored the first build pass's work from
`2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md`, whose embedded files, with their `| `
prefix stripped, equal the saved scratch copies byte for byte. It changed that work where rev-2
requires: the agent-returns record was re-collected now rather than taken from the saved copy, so it
also holds the two returns made since that copy, the first unit-27 build pass's and the rev-2 spec
writer's. The pass wrote the eight unit ledgers, the re-collected
`2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, the 37 foreign bullets in fifteen
ledgers, this ledger and spec 27's status cell. The index generator then rendered the records row
each of the nine new ledgers adds, the build README's unit-27 row, status line and record count, and
`memory/LIVE.md`'s row for the build, which leaves that table now that every unit is CLOSED.

`<red>` is `3f052d89e`. `<w27>` and `<parent>` are both `0cdad5eb9`, the spec-writer commit whose
subject names `TOOL-dRedressedBar-27` and which carries the five revision entries; the pass found all
five there before writing anything. `<p27>` is the commit that adds this ledger, carrying
`Pass: TOOL-dRedressedBar-27`.

No merge bar, no self-test suite and no gate leg ran in this pass. The readings below come from the
§4 probe, a Python program in the session scratchpad run with `-I`, which re-derives check 23
through `git ls-tree` and `git show` and is not committed, and from small scratch programs beside it:
a hunk check, a revision-entry lookup and a `<w27>` diff check. The `<p27>` readings were made over
the staged index that became `<p27>`. The probe stands in for check 23 of the `memory hygiene` leg,
which the close runs with `recall floor` and `recall floor arms`. The unit adds no arm, so no
RED-first observation is owed.

## Foreign lines, before and after

Each target's key, arm, class and evidence, then its bullet as check 23 reads it: every line from
the `- ACn` line to the next bullet, `**Evidences:**` line or heading, at `<parent>` and at `<p27>`.
An added token's evidence names the commit and path `git grep -F` finds it at.

### TOOL-aOrientedCast-22/AC7 · arm 3 · class U

In
`memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md`.
`amended rev-2` names the rev-2 entry of
`memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-22.md`, written at `<w27>`: the
live refusal was owed to the main loop's session at the close, and no record observes it. The
reading opens NOT OBSERVED, and the wrap quotes the criterion's `AskUserQuestion` as the refusal
never seen live. No later aOrientedCast record observes it.

At `<parent>`:

~~~~text
- AC7 — `PreToolUse` — owed to the main loop's live session at the close, after the merge and a restart; not observable by a fixture.
~~~~

At `<p27>`:

~~~~text
- AC7 — amended rev-2, the spec's entry recording that this criterion was never observed — NOT OBSERVED —
  `PreToolUse` — owed to the main loop's live session at the close, after the merge and a restart; not observable by a fixture. Never seen live: the refusal of an `AskUserQuestion` call.
~~~~

### TOOL-aSparedSpawn-1/AC5 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-1-acceptance-ledger.md`.
Added `REUSE_SCHEMA`, for "the schema line". `git grep -F` finds it at the unit's pass commit
`810fbdefc` in `tools/run-gates/run-gates.evidence.test.sh`, 6 hits, the AC5 arm's digest among
them.

At `<parent>`:

~~~~text
- AC5 — `run-gates.evidence.test.sh` AC5 arm, sliced — green 3 of 3; with the schema line out of
  the digest it redded. The first draft placed its control before the miss and stayed green on
  that break, because a run that reuses every leg empties the ledger; reordered, rev-3 records it.
~~~~

At `<p27>`:

~~~~text
- AC5 — `run-gates.evidence.test.sh` AC5 arm, sliced — green 3 of 3; with the schema line
  (`REUSE_SCHEMA`) out of the digest it redded. The first draft placed its control before the miss
  and stayed green on that break, because a run that reuses every leg empties the ledger;
  reordered, rev-3 records it.
~~~~

### TOOL-aSparedSpawn-10/AC9 · arm 2 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-acceptance-ledger.md`.
The check field's command wrapped after `--only`; it is joined onto line 1, so the first line
carries the complete token. No token is added. The spec side has none, so the join is silent.

At `<parent>`:

~~~~text
- AC9 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only
  run-gates-2leg` — calibrated on its 5-fork specimen, then "ok run-gates-2leg · measured 95 ·
  ceiling 99 · base 97"; the row's reason names the stated margin, the readings it sits over and the
  stale direction's bound at 95.

Checked as well, none of them a bar leg run: `sh_hygiene.py --spawn-idioms` with the leg's pathspecs
exited 0 with every registered count unchanged; `sh_hygiene.py --location-probes` exited 0;
`lexicon.py` exited 0 over the six new shell function names; `check-spec-tokens.py` exited 0 with no
hit on this spec; `gen_map.py --check` exited 0 after `--write`.
~~~~

At `<p27>`:

~~~~text
- AC9 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-2leg`
  — calibrated on its 5-fork specimen, then "ok run-gates-2leg · measured 95 · ceiling 99 · base
  97"; the row's reason names the stated margin, the readings it sits over and the stale
  direction's bound at 95.

Checked as well, none of them a bar leg run: `sh_hygiene.py --spawn-idioms` with the leg's pathspecs
exited 0 with every registered count unchanged; `sh_hygiene.py --location-probes` exited 0;
`lexicon.py` exited 0 over the six new shell function names; `check-spec-tokens.py` exited 0 with no
hit on this spec; `gen_map.py --check` exited 0 after `--write`.
~~~~

### TOOL-aSparedSpawn-11/AC10 · arm 2, 3 · class U

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md`.
`amended rev-4` names the rev-4 entry of
`memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-11.md`, written at `<w27>`:
AC10's timings were owed at VERIFYING, and no record observes them. The line said "OWED at
VERIFYING; no figure exists yet". The reading opens NOT OBSERVED, and the wrap quotes the
criterion's `check-pass-order.sh` and `check-brief-recorded.sh` as what was never timed. The
"Checked as well" paragraph check 23 reads into this bullet does not move.

At `<parent>`:

~~~~text
- AC10 — each touched suite and the two checkers timed at base and after on a frozen clone — OWED at
  VERIFYING; no figure exists yet. The AC4 arm adds two reports and 54 in-process reads per run.

Checked as well, none of them a bar leg over a suite: `sh_hygiene.py --spawn-idioms` with the changed
files as pathspecs found no count change for any of them, `sh_hygiene.py` over the substitution-fed
loop registry exited 0, and `lexicon.py` exited 0 after `gen_map.py --write`, where a second `GIT`
definition had first moved both of its pins by one (spec rev-3).
~~~~

At `<p27>`:

~~~~text
- AC10 — amended rev-4, the spec's entry recording that this criterion was never observed —
  NOT OBSERVED — each touched suite and the two checkers timed at base and after on a frozen clone
  — OWED at VERIFYING; no figure exists yet. The AC4 arm adds two reports and 54 in-process reads
  per run. Never timed: `check-pass-order.sh` and `check-brief-recorded.sh`.

Checked as well, none of them a bar leg over a suite: `sh_hygiene.py --spawn-idioms` with the changed
files as pathspecs found no count change for any of them, `sh_hygiene.py` over the substitution-fed
loop registry exited 0, and `lexicon.py` exited 0 after `gen_map.py --write`, where a second `GIT`
definition had first moved both of its pins by one (spec rev-3).
~~~~

### TOOL-aSparedSpawn-11/AC2 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md`.
Added `process.exit`, for "the exit stub". `git grep -F` finds it at the unit's pass commit
`086b3a66d` in `tools/hooks/agent-cap.test.sh`, 5 hits, among them
`const STOP = { stop: 'process.exit' }`, in the runner the instrument cuts from that suite and
stages.

At `<parent>`:

~~~~text
- AC2 — `direct-checks.sh runner` with the exit stub staged to drop its code in a copy of the runner —
  the parity mode exited 1 with 5 disagreements, the first "DISAGREE BASE hook on ...fix/raw.js:
  in-process exit 0, node exit 2"; unstaged, 28 verdicts over 14 payloads, 5 real denies, 0
  disagreements. The same break in a scratch copy of the suite is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC2 — `direct-checks.sh runner` with the exit stub (`process.exit`) staged to drop its code in a
  copy of the runner — the parity mode exited 1 with 5 disagreements, the first "DISAGREE BASE hook
  on ...fix/raw.js: in-process exit 0, node exit 2"; unstaged, 28 verdicts over 14 payloads, 5 real
  denies, 0 disagreements. The same break in a scratch copy of the suite is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-11/AC3 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md`.
Added `gov:sequential-agents`, for "the marker strip". `git grep -F` finds it at `086b3a66d` in the
instrument
`memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-direct-checks.sh`, 2 hits.

At `<parent>`:

~~~~text
- AC3 — `direct-checks.sh runner` with the marker strip staged to a no-op — the property exited 1:
  "73 denied at BASE, 2 denial(s) lost, 0 ratified". The suite-copy form is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC3 — `direct-checks.sh runner` with the marker strip (`gov:sequential-agents`) staged to a no-op
  — the property exited 1: "73 denied at BASE, 2 denial(s) lost, 0 ratified". The suite-copy form
  is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-11/AC6 · arm 3 · class U

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md`.
`amended rev-4` names the same rev-4 entry of spec 11: AC6's suite run was owed at VERIFYING, and no
record observes it. The line's reading is of the diff only. The reading opens NOT OBSERVED, and the
wrap quotes the criterion's `git archive` as the run that was owed.

At `<parent>`:

~~~~text
- AC6 — `check-hook-destinations.test.sh` — OWED at VERIFYING, with the staged reset removal. Read in
  the diff: one `scratch` builds the tree once and resets it per arm to the recorded fixture commit,
  all nine `d=$(scratch)` calls are bare `scratch`, and no arm deletes the shared tree.
~~~~

At `<p27>`:

~~~~text
- AC6 — amended rev-4, the spec's entry recording that this criterion was never observed —
  NOT OBSERVED — `check-hook-destinations.test.sh` — OWED at VERIFYING, with the staged reset
  removal. Read in the diff: one `scratch` builds the tree once and resets it per arm to the
  recorded fixture commit, all nine `d=$(scratch)` calls are bare `scratch`, and no arm deletes the
  shared tree. Never run: the hook-destinations suite, in which `git archive` runs once.
~~~~

### TOOL-aSparedSpawn-11/AC7 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md`.
Added `build_commit`, for "two declared calls". `git grep -F` finds it at `086b3a66d` in the
instrument
`memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-direct-checks.sh`, 7 hits.

At `<parent>`:

~~~~text
- AC7 — `direct-checks.sh ac7` — "u=WANT,WANT m=WANT,WANT other= capped=WANT walks undeclared=2
  declared=3": two declared calls over one range walked once, the other range and the capped
  newest-first window walked their own, and every answer equalled the undeclared one. With the key
  staged to omit the range in a copy of the library the third call answered from the memo
  (`other=WANT`, `declared=2`) and the step redded. The suite arm in `check-unattended.test.sh`,
  counting through the same PATH stub, is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC7 — `direct-checks.sh ac7` — "u=WANT,WANT m=WANT,WANT other= capped=WANT walks undeclared=2
  declared=3": two declared `build_commit` calls over one range walked once, the other range and the capped
  newest-first window walked their own, and every answer equalled the undeclared one. With the key
  staged to omit the range in a copy of the library the third call answered from the memo
  (`other=WANT`, `declared=2`) and the step redded. The suite arm in `check-unattended.test.sh`,
  counting through the same PATH stub, is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-12/AC5 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md`.
Added `TREE_CLEAN` and `no`, for "a tracked file dirtied". `git grep -F` finds both at the unit's
pass commit `f848fe22e` in `tools/run-gates/run-gates.sh`, whose `TREE_CLEAN=no` is the runner's
reading of a dirty tree.

At `<parent>`:

~~~~text
- AC5 — `direct-checks.sh` — with a kx record present, a bar where kx moved and `KX_RED=1` printed
  `GATE FAIL  kx suite` and left no kx record. With ky's record removed and a tracked file dirtied,
  ky executed green and no ky record was written. The suite arm is owed at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC5 — `direct-checks.sh` — with a kx record present, a bar where kx moved and `KX_RED=1` printed
  `GATE FAIL  kx suite` and left no kx record. With ky's record removed and a tracked file dirtied,
  under which the runner's `TREE_CLEAN` reads `no`, ky executed green and no ky record was written.
  The suite arm is owed at VERIFYING.
~~~~

### TOOL-aSparedSpawn-12/AC6 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md`.
Added `guard`, for the held and selected legs. `git grep -F` finds it at `f848fe22e` in the
instrument
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh`, 9 hits,
its fixture legs' `"guard"` fields among them.

At `<parent>`:

~~~~text
- AC6 — `direct-checks.sh` — after a commit adding `ky/extra.sh`, which no kit ships, ky was held
  while the stub govkit answered. With `GOVKIT_STUB_OFF=1` the bar printed `govkit is not reachable`
  exactly once, ky ran naming `ky/extra.sh moved since <sha8>`, and kx was held unchanged on its
  diff. In the default mode a held leg still printed `set GATE_SELFTESTS=1 to run` and no selection
  line appeared. The suite arm is owed at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC6 — `direct-checks.sh` — after a commit adding `ky/extra.sh`, which no kit ships, ky was held
  while the stub govkit answered. With `GOVKIT_STUB_OFF=1` the bar printed `govkit is not reachable`
  exactly once, ky ran by its `guard` naming `ky/extra.sh moved since <sha8>`, and kx was held unchanged on its
  diff. In the default mode a held leg still printed `set GATE_SELFTESTS=1 to run` and no selection
  line appeared. The suite arm is owed at VERIFYING.
~~~~

### TOOL-aSparedSpawn-13/AC11 · arm 2 · class U

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md`.
`amended rev-6` names the rev-6 entry of
`memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-13.md`, written at `<w27>`: the
two whole bars were never run, and no record observes them. The line said "not run". The reading
opens NOT OBSERVED, and the wrap's existing `a` already shares with the criterion's own `cost:`
line.

At `<parent>`:

~~~~text
- AC11 — not run — it needs two whole bars with the self-test tier on a frozen clone, hours on node
  `a`, which no pass may run. It is owed at VERIFYING as the reused count and seconds a second bar in
  a fresh worktree reports.
~~~~

At `<p27>`:

~~~~text
- AC11 — amended rev-6, the spec's entry recording that this criterion was never observed —
  NOT OBSERVED — not run — it needs two whole bars with the self-test tier on a frozen clone, hours
  on node `a`, which no pass may run. It is owed at VERIFYING as the reused count and seconds a
  second bar in a fresh worktree reports.
~~~~

### TOOL-aSparedSpawn-13/AC3 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md`.
Added `clock`, for "`clk` executed". `git grep -F` finds it once at the unit's pass commit
`ca969ce3a` in the instrument
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-13-direct-checks.sh`, in
`clk`'s own manifest row, `"reads": {"clock": "fixture"}`.

At `<parent>`:

~~~~text
- AC3 — `direct-checks.sh` — with `GATE_REUSE_DAY=1` against an earning bar on today's day, `clk`
  executed and `pure` was reused. The suite arm is owed at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC3 — `direct-checks.sh` — with `GATE_REUSE_DAY=1` against an earning bar on today's day, `clk`
  (which reads `clock`) executed and `pure` was reused. The suite arm is owed at VERIFYING.
~~~~

### TOOL-aSparedSpawn-13/AC5 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md`.
Added `TREE_CLEAN` and `no`, for "an untracked guarded file". `git grep -F` finds both at
`ca969ce3a` in `tools/run-gates/run-gates.sh`, whose `TREE_CLEAN=no` is the runner's reading of a
dirty tree.

At `<parent>`:

~~~~text
- AC5 — `direct-checks.sh` — on a cleared cache a bar with `RED=1` left no entry under the red leg's
  key and wrote its green sibling's. A bar on a tree holding an untracked guarded file left the entry
  count at 7. A reused leg's entry bytes were unchanged after the reusing bar. The suite arm is owed
  at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC5 — `direct-checks.sh` — on a cleared cache a bar with `RED=1` left no entry under the red leg's
  key and wrote its green sibling's. A bar on a tree holding an untracked guarded file (under which
  the runner's `TREE_CLEAN` reads `no`) left the entry count at 7. A reused leg's entry bytes were
  unchanged after the reusing bar. The suite arm is owed at VERIFYING.
~~~~

### TOOL-aSparedSpawn-14/AC3 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md`.
Added `REFUSAL_CEILINGS`, for "above its ceiling". `git grep -F` finds it at the unit's pass commit
`118c5c83e` in `tools/memory-tree/check-arms.py`, 16 hits, the ceiling registry the selftest grades
through `--check`'s walk.

At `<parent>`:

~~~~text
- AC3 — `check-arms.py --selftest` — a fixture gate whose census is one above its ceiling reds
  naming the gate and the retirement review; at the ceiling it passes; staged break
  `ceiling compare` turns the arm red.
~~~~

At `<p27>`:

~~~~text
- AC3 — `check-arms.py --selftest` — a fixture gate whose census is one above its ceiling (its
  `REFUSAL_CEILINGS` token) reds naming the gate and the retirement review; at the ceiling it
  passes; staged break `ceiling compare` turns the arm red.
~~~~

### TOOL-aSparedSpawn-14/AC4 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md`.
Added `memory/DECISIONS.md`, for "the fixture decision log". `git grep -F` finds it at `118c5c83e`
in `tools/memory-tree/check-arms.py`, in the selftest's refusal of an id no `memory/DECISIONS.md`
row carries.

At `<parent>`:

~~~~text
- AC4 — `check-arms.py --selftest` — tokens lacking a date and lacking an id each red naming the
  token, an id the fixture decision log does not carry reds, an id carried only as a prefix of a
  longer one is not carried, and a valid ceiling prints
  `ceiling <gate> 2/2 · 2026-10-12 · TOOL-tBudget-1`; staged breaks `ceiling date` and
  `ceiling id carried` each turn an arm red.
~~~~

At `<p27>`:

~~~~text
- AC4 — `check-arms.py --selftest` — tokens lacking a date and lacking an id each red naming the
  token, an id the fixture decision log (`memory/DECISIONS.md`) does not carry reds, an id carried only as a prefix of a
  longer one is not carried, and a valid ceiling prints
  `ceiling <gate> 2/2 · 2026-10-12 · TOOL-tBudget-1`; staged breaks `ceiling date` and
  `ceiling id carried` each turn an arm red.
~~~~

### TOOL-aSparedSpawn-14/AC7 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md`.
Added `--check`, for the planted gate's refusal. `git grep -F` finds it at `118c5c83e` in
`tools/memory-tree/check-arms.py`, 10 hits, the walk the selftest grades through.

At `<parent>`:

~~~~text
- AC7 — `check-arms.py --selftest` — a family pattern matching no site in the planted gate reds
  naming the family; staged break `family dead pattern` turns the arm red.
~~~~

At `<p27>`:

~~~~text
- AC7 — `check-arms.py --selftest` — a family pattern matching no site in the planted gate reds
  under `--check` naming the family; staged break `family dead pattern` turns the arm red.
~~~~

### TOOL-aSparedSpawn-16/AC11 · arm 3 · class A

In `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md`.
Spec 16's rev-3 moved S10 with AC11 to the build's exit, and its rev-4 names that ask,
`TOOL-aSparedSpawn-25`. The answer opens `amended rev-3`, `--dispatch` moves into the wrap, and the
wrap adds `TOOL-aSparedSpawn-25`.

At `<parent>`:

~~~~text
- AC11 — `--dispatch` — MOVED to the build's exit with S10 at rev-3, so no check observes it in this unit; it is an ask, not a discharge.
~~~~

At `<p27>`:

~~~~text
- AC11 — amended rev-3, the spec's entry that moved S10 with this criterion to the build's exit as a named ask —
  `--dispatch` — MOVED to the build's exit with S10 at rev-3, so no check observes it in this unit; it is an ask, not a discharge. The spec's rev-4 entry names that ask, `TOOL-aSparedSpawn-25`.
~~~~

### TOOL-aSparedSpawn-16/AC12 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md`.
Added `age.*` and `age.${heldkeys[$i]}`, for the base runner's count. `age.*` is the criterion's
spelling: `git grep -F` finds it at the unit's pass commit `6dfa3523a` in
`memory/builds/aSparedSpawn/spec/2026-10-12-spec-TOOL-aSparedSpawn-16.md`, 5 hits, the criterion's
among them. The evidence's instance is `age.${heldkeys[$i]}`, found at the instrument's base
`f53211e6c` (the unit's ledger, line 8) in `tools/run-gates/run-gates.sh`, 3 hits, the first at line
3097.

At `<parent>`:

~~~~text
- AC12 — `direct-checks.sh reuse` — changed runner: with K1's count at 9, a K2 execution on a dirty tree, then a K1 reuse, the next K1 run printed `GATE ok    pa  (executed: reused on 10 runs in a row)` and the age line; base runner: that run printed `GATE reuse pa`. The evidence arm `16-AC12` is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC12 — `direct-checks.sh reuse` — changed runner: with K1's count at 9, a K2 execution on a dirty tree, then a K1 reuse, the next K1 run printed `GATE ok    pa  (executed: reused on 10 runs in a row)` and the age line; base runner: counting in its per-name `age.*` file (`age.${heldkeys[$i]}` at f53211e6c) that run printed `GATE reuse pa`. The evidence arm `16-AC12` is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-16/AC18 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md`.
Added `GATE ok    <leg>  (sampled against a cached ok)`, the template of the printed line the answer
already quotes. `git grep -F` finds it at `6dfa3523a` in
`memory/builds/aSparedSpawn/spec/2026-10-12-spec-TOOL-aSparedSpawn-16.md`, once.

At `<parent>`:

~~~~text
- AC18 — `direct-checks.sh reuse` — changed runner: `GATE ok    pa  (sampled against a cached ok)` on a drawn leg, the aged tail on a count of 10, and `GATE FAIL  pa  (exit 1) (sampled against a cached ok)` on a drawn red; base runner: the plain lines. The canary arm 9d2 is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC18 — `direct-checks.sh reuse` — changed runner: `GATE ok    pa  (sampled against a cached ok)` (an instance of `GATE ok    <leg>  (sampled against a cached ok)`) on a drawn leg, the aged tail on a count of 10, and `GATE FAIL  pa  (exit 1) (sampled against a cached ok)` on a drawn red; base runner: the plain lines. The canary arm 9d2 is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-2/AC2 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-acceptance-ledger.md`.
Added `GATE_CALIBRATION_RATES`, for "the seam's rates". `git grep -F` finds it at the unit's pass
commit `01e40f561` in `tools/run-gates/run-gates.test.sh`, 5 hits, the seam arm 12a drives.

At `<parent>`:

~~~~text
- AC2 — `check_sp_value` arm 12a — the seam's rates flat after K=4 picked 4 and rates still rising picked 8, under a `false` spawn command that reds any timed loop. With the selection changed to take the maximum, the flat case picked 6 and the arm redded.
~~~~

At `<p27>`:

~~~~text
- AC2 — `check_sp_value` arm 12a — the seam's rates (`GATE_CALIBRATION_RATES`) flat after K=4 picked 4 and rates still rising picked 8, under a `false` spawn command that reds any timed loop. With the selection changed to take the maximum, the flat case picked 6 and the arm redded.
~~~~

### TOOL-aSparedSpawn-2/AC6 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-acceptance-ledger.md`.
Added `spawnpause=2`, for the row arm 12e declares; it contains the criterion's `spawnpause`.
`git grep -F` finds it at `01e40f561` in `tools/run-gates/run-gates.test.sh`, 2 hits.

At `<parent>`:

~~~~text
- AC6 — `check_sp_value` arm 12e — with no floor recorded, one `run-gates: NOTE` and one `spawn: … INERT` line printed, no pauses row was written, and three legs reported. With the absent floor read as 0, both lines vanished and two pauses rows were written, so the arm redded.
~~~~

At `<p27>`:

~~~~text
- AC6 — `check_sp_value` arm 12e (its row declares `spawnpause=2`) — with no floor recorded, one `run-gates: NOTE` and one `spawn: … INERT` line printed, no pauses row was written, and three legs reported. With the absent floor read as 0, both lines vanished and two pauses rows were written, so the arm redded.
~~~~

### TOOL-aSparedSpawn-3/AC3 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md`.
Added `GATE_WALL=50`, for "a 50 s wall". `git grep -F` finds it once at the unit's pass commit
`321a8dbb6` in the instrument
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-3-direct-checks.sh`, on the ac3
bar's line.

At `<parent>`:

~~~~text
- AC3 — `direct-checks.sh ac3` — after, a 30 s ceiling under a 50 s wall: the breach printed
  `still running at the wall: stall (its serial retry)` and no `GATE ok` or `GATE FAIL` line for the
  leg. A first draft at a 10 s ceiling and an 18 s wall named only the sleeper, because the release
  came 10 to 14 s after the first attempt's end on this host; both arms now carry the wider window.
  The canary's 9l arm is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC3 — `direct-checks.sh ac3` — after, a 30 s ceiling under a 50 s wall: under `GATE_WALL=50` the
  breach printed `still running at the wall: stall (its serial retry)` and no `GATE ok` or
  `GATE FAIL` line for the leg. A first draft at a 10 s ceiling and an 18 s wall named only the sleeper, because the release
  came 10 to 14 s after the first attempt's end on this host; both arms now carry the wider window.
  The canary's 9l arm is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-3/AC4 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md`. The
double-quoted FAIL text is backticked inside its quotes:
`timed out after 3s, again on its serial retry`, which carries the criterion's
`again on its serial retry`. `git grep -F` finds it once at `321a8dbb6` in the instrument
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-3-direct-checks.sh`, in the
FAIL line it counts.

At `<parent>`:

~~~~text
- AC4 — `direct-checks.sh ac4` — after: one FAIL line for the leg, reading "timed out after 3s, again
  on its serial retry" with the serial attempt's HOST note; the set-aside `1.tail.leg` reads
  `timeout` and started before the sleeper ended, and `1.retry.leg` started after it. Its first run
  read a floor an earlier case had written to the shared floor path, which the instrument and the
  canary's 9m arm now remove first. The 9m arm is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC4 — `direct-checks.sh ac4` — after: one FAIL line for the leg, reading
  "`timed out after 3s, again on its serial retry`" with the serial attempt's HOST note; the
  set-aside `1.tail.leg` reads `timeout` and started before the sleeper ended, and `1.retry.leg`
  started after it. Its first run read a floor an earlier case had written to the shared floor path,
  which the instrument and the canary's 9m arm now remove first. The 9m arm is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-3/AC7 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md`.
Added `NR == FNR`, the criterion's spelling: `git grep -F` finds it at the unit's pass commit
`321a8dbb6` in `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-3.md`, 3 hits, the
criterion's among them. The evidence's instance is `NR==FNR`, found once in the "before" runner
`286b839a` (the unit's ledger, line 9) in `tools/run-gates/run-gates.sh`, at line 4036, the ledger
merge. The answer names `286b839a` and that spelling beside the criterion's.

At `<parent>`:

~~~~text
- AC7 — `direct-checks.sh ac7` — before: a second bar that reused its one leg left
  `gate-ledger.tsv` with 0 rows; after: 1 row. The canary's 9d assertion is OWED at VERIFYING.

Checked as well, none of them a bar leg over the tree: `check-arms.py --check` reports the same six
unarmed `run-gates.sh` exit sites as before this pass; `sh_hygiene.py --spawn-idioms` over the leg's
pathspecs exited 0 once the three new canary reads took a here-string instead of a pipe;
`lexicon.py` exited 0; `check-spec-tokens.py` reported nothing for this spec; `gen_map.py --write`
added `run_tail_retry`.
~~~~

At `<p27>`:

~~~~text
- AC7 — `direct-checks.sh ac7` — before: on the base runner at 286b839a, whose ledger merge is the
  `NR == FNR` program the criterion names (spelled `NR==FNR` there), a second bar that reused its
  one leg left `gate-ledger.tsv` with 0 rows; after: 1 row. The canary's 9d assertion is OWED at
  VERIFYING.

Checked as well, none of them a bar leg over the tree: `check-arms.py --check` reports the same six
unarmed `run-gates.sh` exit sites as before this pass; `sh_hygiene.py --spawn-idioms` over the leg's
pathspecs exited 0 once the three new canary reads took a here-string instead of a pipe;
`lexicon.py` exited 0; `check-spec-tokens.py` reported nothing for this spec; `gen_map.py --write`
added `run_tail_retry`.
~~~~

### TOOL-aSparedSpawn-32/AC1 · arm 3 · class U

In `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md`.
`amended rev-5` names the rev-5 entry of
`memory/builds/aSparedSpawn/spec/2026-10-12-spec-TOOL-aSparedSpawn-32.md`, written at `<w27>`: the
range was read at origin's moved tip `6e8f8b1da`, where rev-4's §4 (f) moved the merge, and never at
`37200355d`. The reading opens NOT OBSERVED at the range the criterion names, and the wrap quotes
the criterion's `git diff 69e0ff0f5 37200355d -- F` as the range not read.

At `<parent>`:

~~~~text
- AC1 — the two-parent diff over the staged merge (`git diff -U0 69e0ff0f5 6e8f8b1da -- F`, every
  added line searched for in the index) — 11 files; origin's added lines absent from the result: 4 in
  the runner, 5 in the hook, 4 in the evidence suite, 1 in the README, 1 in `.memory-tree.conf`, 1 in
  `agent-cap.test.sh`, 1 in the hygiene suite, 2 in the dossier, 0 elsewhere. Each is a line both
  sides rewrote, kept as its composite: `HEAD_SHA=$RG_HEAD` (origin's read, this build's no-spawn
  fact), the nine-field ledger row with the builtin seconds read, `read_green_file` and the two
  scoped decision lines carrying both sides' fields, `lineage_reuses=0` initialised beside this
  build's `reuses=0`, the summed `FLOOR_ASSERTIONS` (evidence 208 + 26 = 234, hygiene 613 + 5 = 618),
  the `ARMS_FLOORS` line with both pairs, `agent-cap`'s `node nr.js` calls with origin's
  `unset GIT_DIR GIT_WORK_TREE`, and dossier prose condensed to its 20480-byte cap.
~~~~

At `<p27>`:

~~~~text
- AC1 — amended rev-5, the spec's entry recording that this criterion's range was never read —
  NOT OBSERVED at the range the criterion names — the two-parent diff over the staged merge
  (`git diff -U0 69e0ff0f5 6e8f8b1da -- F`, every added line searched for in the index) — 11 files;
  origin's added lines absent from the result: 4 in
  the runner, 5 in the hook, 4 in the evidence suite, 1 in the README, 1 in `.memory-tree.conf`, 1 in
  `agent-cap.test.sh`, 1 in the hygiene suite, 2 in the dossier, 0 elsewhere. Each is a line both
  sides rewrote, kept as its composite: `HEAD_SHA=$RG_HEAD` (origin's read, this build's no-spawn
  fact), the nine-field ledger row with the builtin seconds read, `read_green_file` and the two
  scoped decision lines carrying both sides' fields, `lineage_reuses=0` initialised beside this
  build's `reuses=0`, the summed `FLOOR_ASSERTIONS` (evidence 208 + 26 = 234, hygiene 613 + 5 = 618),
  the `ARMS_FLOORS` line with both pairs, `agent-cap`'s `node nr.js` calls with origin's
  `unset GIT_DIR GIT_WORK_TREE`, and dossier prose condensed to its 20480-byte cap. Never read:
  `git diff 69e0ff0f5 37200355d -- F`, the range the criterion names; the pass read origin's moved
  tip 6e8f8b1da, where the spec's §4 (f) took the merge.
~~~~

### TOOL-aSparedSpawn-32/AC12 · arm 2 · class O

In `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md`.
Reflowed so the token `lineage` ends line 1. No token is added.

At `<parent>`:

~~~~text
- AC12 — the fixture's runner section — RED at the merge; GREEN on the pass tree: full with both
  knobs records `lineage` and prints `not used: GATE_REUSE`, and without the full flag records `env`
  and prints `GATE_REUSE_LINEAGE is not used without GATE_FULL`.
~~~~

At `<p27>`:

~~~~text
- AC12 — the fixture's runner section — RED at the merge; GREEN on the pass tree: full with both knobs records `lineage`
  and prints `not used: GATE_REUSE`, and without the full flag records `env` and prints
  `GATE_REUSE_LINEAGE is not used without GATE_FULL`.
~~~~

### TOOL-aSparedSpawn-34/AC1 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md`.
Added `git diff 6e8f8b1da main -- F`, the criterion's spelling: `git grep -F` finds it at the unit's
pass commit `e435aafe4` in
`memory/builds/aSparedSpawn/spec/2026-10-13-spec-TOOL-aSparedSpawn-34.md`, 2 hits. It sits beside
the `-U0` form the pass ran, which the answer already carried and which `git grep -F` finds at
`e435aafe4` in the unit's own ledger. `-U0` changes no added line.

At `<parent>`:

~~~~text
- AC1 — the two-parent diff over the staged merge: every line `git diff -U0 6e8f8b1da main -- F` adds, searched for in the result, per conflicted product or suite file — absent, and each a composite named above: 11 in the runner (the knob list, the profile initialiser, the template line, and the eight lines local main added that call `ts_now`), 3 in the driver, 2 in the unattended suite, 2 in the run-gates suite, 1 each in the run-log suite, the hygiene suite, the drift-audit selftest, the manifest-check suite and the pre-push suite (each a floor or a union list), and 0 in `gate-profiles.txt` and `check-memory-hygiene.sh`.
~~~~

At `<p27>`:

~~~~text
- AC1 — the two-parent diff over the staged merge: every line `git diff -U0 6e8f8b1da main -- F` (the criterion's `git diff 6e8f8b1da main -- F`, whose added lines `-U0` does not change) adds, searched for in the result, per conflicted product or suite file — absent, and each a composite named above: 11 in the runner (the knob list, the profile initialiser, the template line, and the eight lines local main added that call `ts_now`), 3 in the driver, 2 in the unattended suite, 2 in the run-gates suite, 1 each in the run-log suite, the hygiene suite, the drift-audit selftest, the manifest-check suite and the pre-push suite (each a floor or a union list), and 0 in `gate-profiles.txt` and `check-memory-hygiene.sh`.
~~~~

### TOOL-aSparedSpawn-4/AC10 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md`.
Added `PROCMON_WHY`, for "the `run-gates: process-monitor:` line". `git grep -F` finds it at the
unit's pass commit `eaab1dd38` in `tools/run-gates/run-gates.sh`, 6 hits, the value that line
prints.

At `<parent>`:

~~~~text
- AC10 — `direct-checks.sh procmon` — python execs before the first dispatch, base against cut: found
  kit 4 and 3, missing kit 3 and 2, refusing scope 4 and 3; the `run-gates: process-monitor:` line
  equals the base's for all three, the refusal's paths included. The SPAWNS arm's in-suite form is OWED.
~~~~

At `<p27>`:

~~~~text
- AC10 — `direct-checks.sh procmon` — python execs before the first dispatch, base against cut: found
  kit 4 and 3, missing kit 3 and 2, refusing scope 4 and 3; the `run-gates: process-monitor:` line
  (which prints `PROCMON_WHY`) equals the base's for all three, the refusal's paths included. The SPAWNS arm's in-suite form is OWED.
~~~~

### TOOL-aSparedSpawn-4/AC12 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md`.
Added `"$(cat <<'RKD'`, for "its wrapper reverted". `git grep -F` finds it once at `989e9234b` in
`tools/hooks/agent-cap.test.sh`, at line 72, the wrapper the revert restores. The instrument
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-4-direct-checks.sh` composes
the idiom at run time and does not carry the literal.

At `<parent>`:

~~~~text
- AC12 — `direct-checks.sh ban` — the S12 predicate over a scratch copy of `agent-cap.test.sh` with its
  wrapper reverted fired once, at line 73, and stayed silent on a comment spelling the idiom. The
  resolve-python suite's ban arm is OWED at VERIFYING.

Also observed directly: `fork-count.sh --only` on a frozen root read the one-leg row at 72 twice (its
ceiling 72; the parent read 95) and the two-leg row at 74 twice (the parent read 130), so the two-leg
row is lowered to 74; `sh_hygiene.py --spawn-idioms` narrowed to the runner reported no rising count in
the runner or any touched suite once the runner's `cat-file` row fell to 15 and its `printf-subst` row
went; `check-arms.py --check` still reports the same six unarmed exit sites in the runner.
~~~~

At `<p27>`:

~~~~text
- AC12 — `direct-checks.sh ban` — the S12 predicate over a scratch copy of `agent-cap.test.sh` with its
  wrapper reverted (to `"$(cat <<'RKD'`) fired once, at line 73, and stayed silent on a comment spelling the idiom. The
  resolve-python suite's ban arm is OWED at VERIFYING.

Also observed directly: `fork-count.sh --only` on a frozen root read the one-leg row at 72 twice (its
ceiling 72; the parent read 95) and the two-leg row at 74 twice (the parent read 130), so the two-leg
row is lowered to 74; `sh_hygiene.py --spawn-idioms` narrowed to the runner reported no rising count in
the runner or any touched suite once the runner's `cat-file` row fell to 15 and its `printf-subst` row
went; `check-arms.py --check` still reports the same six unarmed exit sites in the runner.
~~~~

### TOOL-aSparedSpawn-4/AC6 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md`.
Added `input_key`, for "all six ledger keys". `git grep -F` finds it at the unit's pass commit
`eaab1dd38` in `tools/run-gates/run-gates.sh`, 8 hits, the function that writes the key column.

At `<parent>`:

~~~~text
- AC6 — `direct-checks.sh keys` — over a dirty tree (an edited tracked file, an untracked file under a
  guard, a staged edit), all six ledger keys, a directory guard, a nested one, two files, a glob that
  takes the per-leg path, an absent path and an unguarded leg, equal the base runner's, and a
  `GATE_REUSE` bar reused all six on the precomputed keys, on the final runner. The base is the
  parent, which carries the reuse-key unit's definition. The evidence suite's per-leg and
  backwards-union arms are OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC6 — `direct-checks.sh keys` — over a dirty tree (an edited tracked file, an untracked file under a
  guard, a staged edit), all six `input_key` ledger keys, a directory guard, a nested one, two files, a glob that
  takes the per-leg path, an absent path and an unguarded leg, equal the base runner's, and a
  `GATE_REUSE` bar reused all six on the precomputed keys, on the final runner. The base is the
  parent, which carries the reuse-key unit's definition. The evidence suite's per-leg and
  backwards-union arms are OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-4/AC8 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md`.
Added `PS4`, for "its trace descriptor". `git grep -F` finds it at `eaab1dd38` in the instrument
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-4-direct-checks.sh`, 4 hits.

At `<parent>`:

~~~~text
- AC8 — `direct-checks.sh forks` — the counter read the specimen's declared 5 forks and 1 exec, and the
  same specimen with its trace descriptor closed first refused with 2. The run-log suite's SPAWNS arm
  carries the same counter and is OWED at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC8 — `direct-checks.sh forks` — the counter read the specimen's declared 5 forks and 1 exec, and the
  same specimen with its trace descriptor (the one its `PS4` trace writes to) closed first refused
  with 2. The run-log suite's SPAWNS arm
  carries the same counter and is OWED at VERIFYING.
~~~~

### TOOL-aSparedSpawn-6/AC6 · arm 2 · class A

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-6-acceptance-ledger.md`.
Spec 6's rev-2 names AC6 and makes the run the owner's equivalence run. The answer opens
`amended rev-2`, naming that entry, and the wrap's two tokens already share with the criterion.

At `<parent>`:

~~~~text
- AC6 — not run — owed at the owner's equivalence run: each shard once with
  `UNATTENDED_HARNESS=process` and once with `inproc`, compared by assertion count and sorted
  assertion multiset.
~~~~

At `<p27>`:

~~~~text
- AC6 — amended rev-2, the spec's entry that names AC6 and makes this run the owner's equivalence
  run once the harness landed dark — not run — owed at the owner's equivalence run: each shard once
  with `UNATTENDED_HARNESS=process` and once with `inproc`, compared by assertion count and sorted
  assertion multiset.
~~~~

### TOOL-aSparedSpawn-6/AC8 · arm 2 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-6-acceptance-ledger.md`. The
bullet's own `exit 3` becomes its check field on line 1; it contains the criterion's `exit`.
`git grep -F` finds it once at the unit's pass commit `786644cee` in the unit's own ledger.

At `<parent>`:

~~~~text
- AC8 — the two tail predicates, each confirmed byte-identical to the suite's text and run alone —
  the top-level-exit scan found only the declared missing-library exit on line 90 of the real driver,
  and also line 731 in a copy staged with an undeclared `exit 3`. The namespace comparison read empty
  on two dumps of the 327 sourced definitions. It named `readme_of` and `verb_list` once one was
  doubled and the other unset, and read empty again after re-sourcing the driver. The arms inside
  their shard are owed at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC8 — `exit 3` — the two tail predicates, each confirmed byte-identical to the suite's text and
  run alone — the top-level-exit scan found only the declared missing-library exit on line 90 of
  the real driver, and also line 731 in a copy staged with an undeclared `exit 3`. The namespace
  comparison read empty on two dumps of the 327 sourced definitions. It named `readme_of` and
  `verb_list` once one was doubled and the other unset, and read empty again after re-sourcing the
  driver. The arms inside their shard are owed at VERIFYING.
~~~~

### TOOL-aSparedSpawn-8/AC10 · arm 2 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md`. The
wrapped check-field command is joined onto line 1, so the first line carries the complete token. No
token is added.

At `<parent>`:

~~~~text
- AC10 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt <scratch root> --only
  unattended-status --sites` over a scratch repository holding the kits with `_ac10=$(:)` inserted
  below the driver's `set -u`, and over its unbroken twin — the staged root redded `measured 48 ·
  ceiling 47 · delta +1 · base 57` with the top ten `file:line` sites and the `--sites` hint, the twin
  read `ok … measured 47`, and the two `--sites` tables differed by `unattended.sh:58` alone once the
  sites below it were shifted back by one line. A first staged root that was no git repository read
  76, which is why every fixture here is a repository.
~~~~

At `<p27>`:

~~~~text
- AC10 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt <scratch root> --only unattended-status --sites`
  over a scratch repository holding the kits with `_ac10=$(:)` inserted below the driver's `set -u`,
  and over its unbroken twin — the staged root redded `measured 48 · ceiling 47 · delta +1 · base 57`
  with the top ten `file:line` sites and the `--sites` hint, the twin read `ok … measured 47`, and the
  two `--sites` tables differed by `unattended.sh:58` alone once the sites below it were shifted back
  by one line. A first staged root that was no git repository read 76, which is why every fixture
  here is a repository.
~~~~

### TOOL-aSparedSpawn-8/AC11 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md`.
Added `skipped — <id> · <why>`, the template of the printed line
`skipped — unbuildable · its fixture setup exited 3…` the answer already quotes. `git grep -F` finds
it once at the unit's pass commit `d5e7fc276` in
`memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-8.md`.

At `<parent>`:

~~~~text
- AC11 — `bash tools/gate-lint/fork-count.sh <copy of the ceilings> .` — with `check-wiring` raised to 54 against its count of 50 (max(3, 5 %)
  is 3) redded `STALE ceiling 54 is more than 3 above the measured 50`, and a row whose setup is
  `exit 3` printed `skipped — unbuildable · its fixture setup exited 3…` and the summary read `0 passed
  · 1 red · 1 skipped`.
~~~~

At `<p27>`:

~~~~text
- AC11 — `bash tools/gate-lint/fork-count.sh <copy of the ceilings> .` — with `check-wiring` raised to 54 against its count of 50 (max(3, 5 %)
  is 3) redded `STALE ceiling 54 is more than 3 above the measured 50`, and a row whose setup is
  `exit 3` printed `skipped — unbuildable · its fixture setup exited 3…` (an instance of
  `skipped — <id> · <why>`) and the summary read `0 passed · 1 red · 1 skipped`.
~~~~

### TOOL-aSparedSpawn-8/AC12 · arm 3 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md`.
Added `tools/unattended/unattended.sh`, beside `unattended-status`. `git grep -F` finds it once at
`d5e7fc276` in `memory/project/fork-ceilings.txt`, in that row's command.

At `<parent>`:

~~~~text
- AC12 — `bash tools/gate-lint/fork-count.sh` over each fixture, the tree at base `22efab65` and at
  the pass's tip side by side — forks per invocation, base then tip: `unattended-status` 57 → 47, `check-unattended` 709 →
  684, `run-gates-1leg` 72 → 72, `run-gates-2leg` 97 → 95, `memory-hygiene` 219 → 221 (the fixture
  copies the tree's conf, which grew), `manifest-check` 108 → 108, `check-wiring` 55 → 50. Every tip
  count repeated exactly on three runs except `run-gates-2leg`, which read 95, 95, 95 and 96, its pool
  polling its workers; its ceiling is 96 and the rest sit at their counts. The driver entrypoint is
  lower at the tip. A full run against the landed ceilings passed six rows and redded that row at 96
  before its ceiling moved; the leg's own green run over the final file is owed at VERIFYING.
~~~~

At `<p27>`:

~~~~text
- AC12 — `bash tools/gate-lint/fork-count.sh` over each fixture, the tree at base `22efab65` and at
  the pass's tip side by side — forks per invocation, base then tip: `unattended-status` (the row whose command runs `tools/unattended/unattended.sh`) 57 → 47, `check-unattended` 709 →
  684, `run-gates-1leg` 72 → 72, `run-gates-2leg` 97 → 95, `memory-hygiene` 219 → 221 (the fixture
  copies the tree's conf, which grew), `manifest-check` 108 → 108, `check-wiring` 55 → 50. Every tip
  count repeated exactly on three runs except `run-gates-2leg`, which read 95, 95, 95 and 96, its pool
  polling its workers; its ceiling is 96 and the rest sit at their counts. The driver entrypoint is
  lower at the tip. A full run against the landed ceilings passed six rows and redded that row at 96
  before its ceiling moved; the leg's own green run over the final file is owed at VERIFYING.
~~~~

### TOOL-aSparedSpawn-8/AC6 · arm 2 · class O

In `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md`. The
wrapped check-field command is joined onto line 1, so the first line carries the complete token. No
token is added.

At `<parent>`:

~~~~text
- AC6 — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt .
  ':!*.test.sh' ':!memory/'` over the tree — exit 0, each class's scanned, gated and near-miss counts
  printed, 0 sites for each BANNED class, 2099 registered sites in 292 rows; over a scratch copy of the
  shell population with `x=$(date +%s)` appended to `tools/check-wiring.sh` it exited 1 printing
  `tools/check-wiring.sh:1772: [epoch-date] x=$(date +%s) — use $EPOCHSECONDS…`, and with a pathspec
  selecting nothing it refused with 2. Every count in the registry was derived by the scan.
~~~~

At `<p27>`:

~~~~text
- AC6 — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  over the tree — exit 0, each class's scanned, gated and near-miss counts printed, 0 sites for each
  BANNED class, 2099 registered sites in 292 rows; over a scratch copy of the shell population with
  `x=$(date +%s)` appended to `tools/check-wiring.sh` it exited 1 printing
  `tools/check-wiring.sh:1772: [epoch-date] x=$(date +%s) — use $EPOCHSECONDS…`, and with a pathspec
  selecting nothing it refused with 2. Every count in the registry was derived by the scan.
~~~~

## The criteria

**Evidences:** TOOL-dRedressedBar-27
- AC1 — `ok obs` — the probe's `grade` mode over the staged tree, for the 64 keys of units 2, 4, 5,
  7, 9, 11, 18 and 20, printed 60 `ok obs` and 4 `ok amd`, the amended four being unit 18's AC1,
  AC2, AC5 and AC15. Each key answered from its unit's own ledger as §4 names it: 4 from the
  `-2-1-` ledger, 4 from `-4-1-`, 10 from `-5-1-`, 7 from `-7-1-`, 7 from `-9-1-`, 7 from
  `-11-1-`, 17 from `-18-2-` and 8 from `-20-1-`, and none from the set-aside record. It printed no
  `ORPH` line. Red half: at `<red>` the `red` mode printed `GAP 64`, exactly the arm-1 list of §4
  "Today's red", and `grade` printed `GAP` for each of the 64. At `<parent>` the probe printed the
  same 102 keys as at `<red>`: the set-aside record prefixes every embedded line with `| `, so
  check 23 reads none of its copies as an answer.
- AC2 — `ok obs` — over the eight arm-2 keys: 5 `ok obs`, for `-10/AC9`, `-32/AC12`, `-6/AC8`,
  `-8/AC10` and `-8/AC6`, and 3 `ok amd`, for `-11/AC10`, `-13/AC11` and `-6/AC6`. Red half: at
  `<red>` all eight printed `BAD`, `-11/AC10` as `BAD+TOKBAD`.
- AC3 — `TOKBAD` — over the 30 arm-3 keys none printed `TOKBAD`: 25 `ok obs` and 5 `ok amd`. Red
  half: at `<red>` all 30 printed `TOKBAD`. Over the whole population of 793 units, the `red` mode
  on the staged tree printed `GAP 0`, `BAD 0`, `TOKBAD 0` and `ORPH 0`.
- AC4 — `LOST` — the probe's `words` mode over the 37 target bullets at `<parent>` and on the
  staged tree printed `words: 37 bullets compared, 0 LOST`. A hunk check over `git diff -U0` from
  `<parent>` to the staged tree, for the fifteen foreign ledgers, read 36 hunks and none outside a
  target bullet's span on either side. Its first draft held each hunk to a single bullet and flagged
  the two hunks that span adjacent targets, `-11/AC2` with `-11/AC3` and `-16/AC11` with
  `-16/AC12`, which is how it is known to fire. Over `<w27>`, `0cdad5eb9`, against its parent, each
  of the five specs gained exactly one entry inside its revision log: `TOOL-aSparedSpawn-11` rev-4,
  `-13` rev-6, `-32` rev-5, `TOOL-aOrientedCast-22` rev-2 and `TOOL-dRedressedBar-18` rev-9. Its
  `**Status:**` line moved only two fields, its rev to that entry's number and its date to
  2026-10-16. Spec 18 also gained one `gen:spec-records` row. `memory/builds/aSparedSpawn/README.md`
  changed three rows, one for each of its three specs, and `memory/builds/aOrientedCast/README.md`
  one. `gen_build_index.py --check` in a clone checked out at `<w27>` exited 0 and printed
  `build-index: clean (1520 artifact(s))`. Over the five specs, the staged tree differs from
  `<parent>` only in spec 18's `gen:spec-records` region, by the row for its new ledger.
- AC5 — `git grep -F` — the token table's 31 rows, over 26 keys, each searched at the commit and path
  its entry above names: 31 found, 0 missing. The criterion-spelled tokens `age.*`, `NR == FNR`,
  `skipped — <id> · <why>`, `GATE ok    <leg>  (sampled against a cached ok)` and
  `git diff 6e8f8b1da main -- F` were each found in the owning spec, and each entry names the
  evidence's instance beside it. Each of the eleven AMENDED answers' `amended rev-<n>` names an entry
  of its spec's revision log at `<w27>` that names the answer's label: `-6/AC6` rev-2, `-16/AC11`
  rev-3, unit 18's AC1, AC2 and AC5 rev-7, and the six U lines. Each U line, `-11/AC6` and
  `-11/AC10` at rev-4, `-13/AC11` at rev-6, `-32/AC1` at rev-5, `TOOL-aOrientedCast-22/AC7` at
  rev-2 and `TOOL-dRedressedBar-18/AC15` at rev-9, opens `amended rev-<n>` with that entry, carries
  no backtick on its first line, and its reading opens NOT OBSERVED.
- AC6 — `.memory-tree.conf` — `git diff` from `<parent>` to the staged tree over
  `.memory-tree.conf`, `tools/`, `memory/HYGIENE.md` and `memory/project/` printed nothing.
- AC7 — `wf_0e7a57a1-02c` — the re-collected record holds that return at line 5556, labelled
  `dRedressedBar · TOOL-dRedressedBar-18 · build`, and `grep -c '^\*\*Evidences:\*\* '` over it
  printed `0`. Every line under `## Returns` at `<parent>` is present in the re-collection in the
  same order, and the one line of `<parent>` the re-collection lacks is the header sentence above
  `## Returns`, which now says the record was last regenerated at TOOL-dRedressedBar-27. The
  collector was cut verbatim from the record's fenced block at `<parent>` and run with `-I` over the
  session's `subagents` directory. Its output is the saved scratch copy's 189 returns with two more
  after them.
- AC8 — `**Serves:** journal TOOL-dRedressedBar-27` — this record carries it, one entry under
  "Foreign lines, before and after" for each of the 37 targets, and this block answering AC1 to
  AC8. Each entry's first fenced block is the bullet the probe's `bullet` mode printed at
  `<parent>`, and its second the bullet it printed on the staged tree.
