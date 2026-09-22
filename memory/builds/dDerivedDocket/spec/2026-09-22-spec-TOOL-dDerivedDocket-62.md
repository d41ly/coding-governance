# TOOL-dDerivedDocket-62 — one worktree answers for a slug, and every other copy reads ELSEWHERE

**Status:** SPECCED · rev-2 · 2026-09-22 · node d · Tier-2 · base 07997375 · streams tooling · order 32

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 61 moves the lease out of one per-slug file under the git common dir and into the run-state
file, which is one tracked copy per worktree, and every clock `--liveness` reads belongs to the
calling worktree. Measured at `07997375`, the resume tick already grades each copy on its own: one
record carried by two worktrees is resumed twice, and the stale sibling is resumed while the run's
own worktree reads LIVE. Give each slug ONE answer per node: only the worktree whose checked-out
branch is the record's run branch acts, and every other copy reads the named verdict `ELSEWHERE`.
There the tick prints a named skip and kills nothing, and the resume matrix refuses, numbered,
naming the run's branch. This is route (a) of finding B1 in the G8 round-1 audit of unit 61, and it
also closes that audit's M5 pre-preflight re-bind for a re-run started on a new branch.

## 2. Scope (IN)

- **S1** `resolve_holder_worktree <run-state file>` in `tools/unattended/unattended.sh`. The run's
  branch is the `run-branch` fact, else the `branch-ref` fact, the key `gate-guard.js` already
  applies, and a worktree holds the slug when its `git symbolic-ref -q HEAD` names that ref. It sets
  `HW_REF` and `HW_HEAD` and returns 0 when this worktree holds, 1 when this worktree has another
  branch or a detached or unreadable HEAD, and 2 when the record names no branch. Observed by AC1,
  AC4 and AC8.
- **S2** `--liveness` reads `verdict: ELSEWHERE` on a return of 1, second in the verdict order after
  `TERMINAL`, and prints a fifteenth key, `holder-ref`, after `stale-bound`: the ref, or `absent`, on
  every run that reaches a verdict. An `unreadable` HEAD is the verb's existing dead probe and
  refuses at `fail 52`. Observed by AC1 and AC8.
- **S3** `tools/unattended/resume-tick.sh` reads `holder-ref` and prints two named skips that kill
  and launch nothing: `skip · ELSEWHERE` on that verdict, and `skip · NO RUN BRANCH` where a verdict
  that would act meets `holder-ref: absent`. Its header's decision table gains both rows. Observed by
  AC2, AC3 and AC8.
- **S4** The resume matrix refuses outside the holder worktree. `check_holder_worktree <slug>
  <run-state file>` holds the one new `fail 58` branch, which names the run's branch, the worktree
  that has it checked out or that none does, and this worktree's HEAD, after the `--status` block
  when no id was passed. On a record naming no branch it announces that and lets the call through.
  `verb_resume` calls it at the head of unit 61's re-bind row and directly ahead of the first HELD
  row, and nowhere else. Observed by AC4, AC5, AC6 and AC8.
- **S5** `tools/unattended/stop-guard.js` ALLOWS a stop whose verdict is `ELSEWHERE`, with reason
  `elsewhere`, directly after unit 61's `held` row; `REASONS` and the header's decision table gain
  it. Observed by AC7.
- **S6** The carriers say what the code now does: the verb carrier's `--liveness` entry, the stop
  contract's §8, the protocol's KEEPALIVE paragraph, and the Skill's tick paragraph, what-wakes
  paragraph and Resume section, every render re-rendered. The driver's `print_liveness` header and
  the tick's and the stop-guard's decision tables follow. Observed by AC9.
- **S7** NO capped carrier grows: the protocol, the stop contract and the verb carrier, each as
  template and render, end the pass no larger in bytes or in lines than they began it, funded by the
  trims §4 names. Observed by AC10.
- **S8** The suite arms follow the code. The new arms §7 names are written and each is staged RED;
  `add_sibling_worktree` sits beside the tick suite's `build_fixture`, which now writes
  `run-branch: refs/heads/main`; the driver suite's three `--liveness` key-count and key-order arms
  expect fifteen keys; and every existing arm that reaches a guarded row off the record's branch is
  retargeted onto that branch at the same commit, one for one, which moves no floor. Each suite's
  executed-assertion floor rises by exactly the assertions its new arms carry, counted off their
  blocks and never read off a run: the driver suite's `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, its
  new arms written in region two beside the arms they extend, and the resume-tick and
  stop-guard suites' `FLOOR_ASSERTIONS`. Observed by AC11.
- **S9** The unit's hygiene: no kit version moves, no kit file gains a kit-path literal, every new
  function name passes the lexicon, the new `fail` branch is armed, and no pinned row of
  `memory/project/unarmed-branches.txt` moves. Observed by AC12.

## 3. Non-goals (OUT)

- Route (b), one clock merged across every worktree that carries the slug. §8 F1.
- A holder that moves to the default-branch worktree once a `primary` landing is pushed. §8 F7.
- `--status` in a non-holder worktree. It acts on nothing, and the refusal S4 adds is its backstop,
  so it keeps printing what unit 61 has it print from the copy it reads. A follow-up.
- A holder test on the writing verbs `--preflight`, `--hold`, `--close`, `--landed`, `--abort`,
  `--park`, `--dispatch` and `--brief`. They are the holding session's own acts, no out-of-session
  actor reaches them, and `verb_landed` runs on the default branch under `primary` by its own header
  (`tools/unattended/unattended.sh:3946`). §4 says what unit 28's argument still rests on because of
  this.
- Short-circuiting the four clocks in an ELSEWHERE copy. Every key still prints on every run that
  reaches a verdict, and skipping the reads is a follow-up.
- A linked worktree in every tick fixture, the audit's left-shift as written. §8 F8.
- Detecting one branch forced into two worktrees. §5 risk (4).
- M5's Skill half, the check-51 sentence and unit 61's AC13 grep, and M3's clock scoping. Both are
  unit 61's own fold. H1 and H2 are promoted to units of their own.
- A `memory/DECISIONS.md` row. The rule lands in the stop contract's §8, a binding carrier, and the
  choice of route is this spec's §8 F1.
- Any kit version constant. The unattended kit stands unreleased at 1.29 on this branch.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-61` — the re-keyed resume matrix, whose re-bind row inside
  the derived-terminal branch and whose observed-landing row place this unit's two call sites;
  `--liveness`'s HELD verdict and verdict order, into which ELSEWHERE goes second; the tick's named
  HELD arm and the stop-guard's `held` row, beside which the new ones sit; and the landed log whose
  observation AC6 reads. Without it the rows this unit guards do not exist in the shape it guards.
- **consumes-from** `TOOL-dDerivedDocket-28` — the per-slug ledger under the git common dir and its
  reap on the `--resume` rows that hold the lease. AC4 reads that ledger byte-unchanged after a
  refused call from a sibling worktree, and §4 states what that unit's prune-race argument rests on
  now.
- **hands-off** external — the gotcha record for the class the audit names: state moved from the git
  common dir into a tracked file becomes one copy per worktree, and every actor that walks worktrees
  must join on the slug. In this kit the class is gated by the arms S8 adds; the record, with the
  dossier claim a new gotcha owes, is a follow-up outside this build.

## 4. Design

### What the merged tree does, measured

Measured on node `d` 2026-09-22 at `07997375` with git 2.54.0.windows.1 (PINNED), over a scratch
repository holding a conf, a README and one committed BUILDING record with session `S1`,
`run-branch: refs/heads/run` and a dead pid, its commit and files aged an hour past a one-second
`RESUME_STALE_BOUND`:

| Fixture | Observation |
|---|---|
| the main worktree on `run`, and a worktree added on `wave` after the record commit | `--liveness` reads `verdict: STALE` in both, and `resume-tick.sh --dry-run` prints `resumed · attempt 1` for both, each out-file under that worktree's own git dir |
| the same with one gate log dated now under the main worktree's git dir only | the main worktree reads `skip · verdict LIVE`, and the linked one is still `resumed · attempt 1` |
| `git worktree add ../fx-2 run`, then `git checkout run` inside the linked worktree | both refuse with exit 128, `'run' is already used by worktree at` the main worktree's path |
| `schtasks /query /tn gov-resume-tick` on node `d` | no such task: the tick is not registered on this node |

The first two rows are B1's tick half, already live at this base for any record that carries a
`session` fact; unit 61's Rollout is what gives this build's record one. The third row is the
property this unit rests on. M5 cannot be measured here, because unit 61's re-bind row is not built.

### One holder per slug

The run's branch is fact 13, `run-branch`, which `--preflight` writes on both anchors from
`GIT symbolic-ref -q HEAD` (`tools/unattended/unattended.sh:4943`), else fact 10, `branch-ref`, for
a record written before fact 13 existed (`:4990`). That is the key `resolveRunPhase` in
`tools/unattended/gate-guard.js` already applies (`:598`). Its header gives this unit's reason at
`:64`: two stale BUILDING records on branches nobody has checked out must key nothing, so the key is
the branch and never the existence of a record. The holder worktree is the one whose HEAD names that
ref, and git refuses to check a branch out in a second worktree, measured above. So on one node at
most one worktree holds a slug, and the checkout decides which, never a clock.

`resolve_holder_worktree <run-state file>` sets `HW_REF` to the run's branch, empty when the record
carries neither fact. When `HW_REF` is set it runs `GIT symbolic-ref -q HEAD` in the calling
worktree, the derivation fact 13 is written from, and sets `HW_HEAD` to the ref, to `detached` on
that command's exit 1, or to `unreadable` on any other failure. It returns 0 when `HW_HEAD` equals
`HW_REF`, 1 when they differ, and 2 when `HW_REF` is empty. It sets globals, so no caller runs it
through a substitution. It writes nothing and prints nothing.

### `--liveness`, and the verdict order

`print_liveness` calls it after the state block, at `:5540`. On a return of 1 with `HW_HEAD` reading
`unreadable`, and no dead probe already named, it names this one before the dead-probe test at
`:5570`, so the refusal is the existing `fail 52` and no verdict prints. The verdict chain at `:5578`
becomes TERMINAL, ELSEWHERE, FINISHED-UNSTAMPED, HELD, UNBOUND, STALE, LIVE: unit 61's order with
ELSEWHERE second.

- TERMINAL stays first. A recorded terminal is frozen, and an observed landing is in the common-dir
  log unit 61 writes, so every copy that carries either reads the same, and acting on it is nothing.
- ELSEWHERE precedes FINISHED-UNSTAMPED. Under in-place landing the primary tree carries the
  unobserved LANDING record too once it fast-forwards, and two copies reading an acting verdict is
  the measured shape above.
- ELSEWHERE precedes HELD. A sibling copy holds whatever phase the record had when that worktree
  branched, so it cannot tell a held run from a working one.

The fifteenth key, `holder-ref`, prints `HW_REF` or `absent` after `stale-bound`, on every run that
reaches a verdict. The clock keys are still measured and printed in an ELSEWHERE copy; they describe
that worktree and decide nothing there. The header's key list and verdict list follow.

### The tick

`read_liveness` (`tools/unattended/resume-tick.sh:235`) reads `holder-ref:` into `RL_HOLDER`, and a
missing line reads `absent`, so a driver older than the tick reads as naming no branch, the side that
acts nowhere. `run_tick` (`:255`) gains two named skips.

- Beside unit 61's HELD arm in the case at `:269`, ELSEWHERE prints `skip · ELSEWHERE · the run's
  branch is <ref>, and this worktree is not on it, so nothing is killed or launched from this copy`.
- After that case, where the verdict would act, `RL_HOLDER` reading `absent` prints `skip · NO RUN
  BRANCH · the record names neither run-branch nor branch-ref, so no one worktree holds it and no
  copy of it is acted on`.

The walk in `scan_worktrees` (`:346`) is unchanged. It still asks `--liveness` in every worktree and
never decides the holder itself, because the header's rule is that the tick re-derives nothing
`--liveness` answers.

### The resume matrix

`check_holder_worktree <slug> <run-state file>` returns 0 when `resolve_holder_worktree` returns 0.
On 2 it prints `unattended: this record names no run branch (neither run-branch nor branch-ref), so
which worktree drives it cannot be shown and this worktree's copy is graded on its own clocks` and
returns 0. On 1 it prints the `--status` block first when no `--keepalive-id` was passed, as every
no-id row does under the stop contract's §8. It then reads the worktree whose `branch` line equals
`HW_REF` from `GIT worktree list --porcelain`, the listing `verb_landed` already walks at `:3980`,
and refuses once:

```
fail 58 "this worktree is not on the run's branch, so its copy of the record is not the run's, and
resuming, taking over or re-binding from it would drive one slug from a stale copy; the run is
driven from the worktree that has <ref> checked out: <path | no worktree on this node has it
checked out, so check it out first>. Nothing was written. This worktree: <ref | a detached HEAD |
an unreadable HEAD>"
```

Nothing is written, reaped or pruned, and it returns 1. `verb_resume` calls it at two sites, each
`|| return 1`, and one invocation reaches at most one of them:

| Site | Rows it guards |
|---|---|
| the head of unit 61's re-bind row, inside the derived-terminal branch at `:5746` | a pushed landing re-bound with an id |
| directly after unit 61's observed-landing row, ahead of the first HELD row | every HELD row and every working row, on every clock, with an id and without |

Unguarded, and unchanged: `check_asks_pinned`, the `--scheduled` refusals, `refuse_if_terminal
--recorded` with an id at `:5745`, the derived terminal resumed with no id, and the observed landing.
Each writes nothing, and each is the answer every copy that carries the record gives (§8 F5). A
durable restart's prompt names the worktree `--hold` ran in, and the tick relaunches in the worktree
it read, so both land in the holder worktree and pass.

Measured by an awk scan of each call's nearest preceding checkout (PINNED, `07997375`): two of the
driver suite's `--resume` and `--liveness` calls run off the record's branch. The no-id resume on a
landed fixture checked out as `main` (`tools/unattended/unattended.test.sh:2992`) is the unguarded
derived-terminal row. The `--scheduled` resume on a detached HEAD (`:7977`) meets check 60 before
the matrix. Both keep their output. The builder re-runs the scan at the pass's parent, because unit
61's arms join the population first, and S8 retargets whatever it finds in a guarded row.

### The stop-guard

`checkStop` (`tools/unattended/stop-guard.js:135`) returns an allow with reason `elsewhere` on that
verdict, directly after unit 61's `held` row, so the stop is allowed before `background-tasks` is
consulted and no block is spent on it. `REASONS` (`:94`) and the header's decision table gain the
row. The hook runs `--liveness` in the worktree its payload's `cwd` names, so a session whose cwd
sits in a sibling worktree reads that sibling's copy, which cannot say whether the run is open.
§8 F4 weighs the block.

### What unit 28's prune-race argument rests on now

Unit 28 §4 "Pruning and concurrency" argues that rewriting the common-dir ledger cannot race an
append, because pruning happens only in four reaping verbs, "each of which holds the slug's lease
when it reaps", and `--resume` reaps only on a row that holds it. Under unit 61 as specified, holding
is decided on the calling worktree's copy and clocks, so two worktrees can each reach a holding row
for one slug, and the argument has no single holder under it: B1's third case.

With this unit, the `--resume` half rests on `check_holder_worktree`. The take-over and holder rows
unit 28 reaps on are reached only in the one worktree whose HEAD is the run's branch, git lets no
second worktree check it out, and a refused call from any other worktree reaps, prunes and writes
nothing, which AC4 reads back. The other three reaping verbs, `--preflight`, `gates-green` inside
`--close`, and `--hold`, are not matrix rows, and this unit does not guard them. That each runs only
in the holder's worktree rests, as it did under unit 4's lease file, on the contract that a session
drives its run from the run's worktree. `--preflight` re-admits only the recorded keepalive (check
82, `:4769`) and `--hold` refuses a `--reaped` naming another id (check 56); those are identity
checks and not worktree checks. A record naming no run branch keeps the per-copy reading, so for
that population the argument rests on nothing mechanical, and that population is measured empty.

### Where the text goes

Every figure is PINNED, measured at `07997375` on node `d` against that base's text with `wc -c`.
Unit 61 edits three of these places first, the protocol's stop-guard clause, the `--liveness` entry
and the whole of §8, so the pass re-measures at its parent.

| Carrier | Edit | Bytes | Lines |
|---|---|---|---|
| protocol, template and render | the stop-guard clause of the KEEPALIVE paragraph at `tools/unattended/PROTOCOL.template.md:393` gains ", reading the run's own worktree," | +33 | 0 |
| protocol | "The tick acts only on a lease the INDEX holds, on the node that took it" gains ", in the worktree on the run's branch" | +37 | 0 |
| protocol | "Registering the tick is the owner's, one line per OS in the kit README; `--check` reports it as INFO." is removed: the kit README's registration section carries both facts | −102 | 0 |
| verb carrier, template and render | the `--liveness` entry at `tools/unattended/VERBS.template.md:93` gains `ELSEWHERE`, and its closing clause becomes "then the `stale-bound` it was graded against and the `holder-ref` a worktree must have checked out" | −4 | 0 |
| stop contract, template and render | §8 gains one row and one sentence | +286 | derived |
| stop contract | §9's history sentence beginning "What changed is the sentence that followed it" is removed | −195 | derived |
| stop contract | §10's placement sentence beginning "It is here rather than there because the protocol is at its cap" is removed | −124 | derived |

The protocol nets −32 bytes, the verb carrier −4 and the stop contract −33, and neither the protocol
paragraph nor the verb entry re-wraps to more lines. The stop contract's §8 row reads `| any other |
from a worktree not on the run's branch | refuses, numbered, naming the branch and its worktree;
writes nothing |`. It sits below the three rows unit 61's table answers with nothing to resume: the
recorded terminal, the derived terminal resumed with no id, and the observed landing. Those move
above unit 61's re-bind row, which is sound because their conditions are disjoint from it, so the
first-match order answers nothing differently. The sentence joins the first paragraph below the
table, so it adds no blank line: "The run's branch is `run-branch`, else `branch-ref`, and git checks
a branch out in one worktree at most; a record naming neither is graded where it is read." Its line
delta is derived at the build commit against the two trims, which free about three lines.

The Skill carries no size row. Its tick paragraph at `tools/unattended/SKILL.template.md:29`, in the
list of refusals unit 61 writes as expected before `--preflight`, gains "or, on a re-run build whose
branch still carries the earlier run's record, check 58 naming another branch". Its what-wakes
paragraph at `:75` has the stop-guard, reading the run's own worktree, refuse a turn end. Its Resume
section at `:835` gains, after the refused-resume sentence: "A check-58 refusal that names the run's
branch means this worktree is not the run's: reap only the job you just scheduled, and resume from
the worktree the refusal names."

### Inventory

| Identifier | Kind | Cell, and the lexicon answer at writing |
|---|---|---|
| `resolve_holder_worktree` | driver function | `sh.function`: OK, leads with `resolve` |
| `check_holder_worktree` | driver function | `sh.function`: OK, leads with `check` |
| `add_sibling_worktree` | tick-suite helper | `sh.function`: OK, leads with `add` |
| `HW_REF`, `HW_HEAD` | driver globals | no shell variable cell is declared |
| `RL_HOLDER` | tick global | no shell variable cell is declared |
| `holder-ref` | `--liveness` key | a key, after `stale-bound` |
| `ELSEWHERE` | `--liveness` verdict | a value, beside `TERMINAL` |
| `elsewhere` | stop-guard reason | a value, beside `held` |
| `NO RUN BRANCH` | tick skip tag | beside `ATTEMPTS EXHAUSTED` and `IN-FLIGHT` |

`refuse_if_elsewhere` was the first name tried for the refusal, and the lexicon answered that
`refuse` is not in the declared table, so the refusal is a `check`, as `check_asks_pinned` already
is.

### Migration

Nothing migrates, because nothing is written: the key is facts 13 and 10, both already recorded, and
no fact or file is added. What changes is which copies are acted on, so the population is every
worktree whose HEAD carries a record with a `session` fact. Measured on node `d`, 2026-09-22, at
`07997375` (PINNED):

- The tree tracks 59 run-state records, and exactly one carries a `session` fact: a LANDED record
  that carries both branch facts.
- 25 records carry neither branch fact. Every one is ABORTED, LANDED or LANDING, and none carries a
  session, so the population §8 F3's skip reaches is empty.
- The node has 12 worktrees, and two carry this build's record. The run worktree
  `build-readme-governance-18d6ea` has `refs/heads/branch/backlog-maintenance-mechanics-10588f`
  checked out, the record's `branch-ref`, so it holds. The wave worktree `wf_f6394001-255-1` has
  `refs/heads/worktree-wf_f6394001-255-1` checked out, so its copy reads ELSEWHERE.
- The audit counted six `wf_*` worktrees earlier the same day. The count moves with every wave, and
  concurrent waves are the owner's ruling of 2026-09-21, so the rule keys on the branch and never on
  the count. Each wave worktree is made on its own `worktree-wf_<id>` branch, and git refuses to
  check the run's branch out there while the run worktree has it, so every wave worktree reads
  ELSEWHERE by construction, whatever phase its copy carries.
- This build's record carries `branch-ref` and no `run-branch`. It was preflighted at `e7da7bf5`,
  whose driver had no fact-13 writer, since `7e9bbeff` is not its ancestor, so it is keyed by fact
  10, which names the local branch exactly.
- The two other BUILDING records, `aClosedDocket` and `aUnblockedFleet`, name branches that do not
  exist locally on node `d`, so no worktree here holds either. Their `--resume` refuses at 58 naming
  that branch, where under unit 61 alone it would claim a live session drives them. That is the
  audit's M3 population, and taking one over now starts by checking its branch out.

### Rollout

The unit lands inside this build's own run, after unit 61, whose Rollout gives this build's record
its `session`, `pid` and `lease-utc` facts. From that records commit until this unit merges into the
run branch, every wave worktree branched after it carries a session-bearing copy that the tick and
the matrix would grade per worktree. That window is inert on node `d`, as measured: no tick is
registered there, a sidechain agent's stop is not a `Stop` event the hook grades, and
`tools/workflows/unattended-unit.js` and `unattended-build.js` name neither `--resume` nor a
keepalive id. Registering the tick is the owner's act, and it should wait for this unit. Rollback is
a revert of the build commit, after which every copy is graded per worktree again, with nothing on
disk to undo.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/resume-tick.sh` · `tools/unattended/stop-guard.js` ·
`tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` ·
`tools/unattended/STOPS.template.md` · `memory/guides/UNATTENDED-STOPS.md` ·
`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`tools/unattended/SKILL.template.md` · `.claude/skills/unattended/SKILL.md` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/resume-tick.test.sh` ·
`tools/unattended/stop-guard.test.sh`

### Alternatives rejected

- Route (b), the merged clock. §8 F1.
- Keying on `branch-ref` alone. §8 F2.
- Moving the holder to the default-branch worktree at a pushed `primary` landing. §8 F7.
- The tick reading the `branch` lines of the `git worktree list --porcelain` it already walks and
  deciding the holder itself. It is a second spelling of the holder rule beside `--liveness`, which
  the tick's header forbids.
- A per-slug holder record under the git common dir. It is the lease file the ruling retired, under
  another name.
- Spawning `gate-guard.js` from the driver for the key. It costs a node start per `--liveness`, and
  that hook fails open by contract, which is the wrong direction for an actor that kills.

## 5. Production-readiness checklist

- security — The key is facts the run's own verbs wrote and the calling worktree's HEAD, which any
  session with shell access can move. So the test stops an accidental second driver acting from a
  stale copy, and not a malicious one, as unit 61's §5 says of the lease. The refusal prints a
  worktree path from `git worktree list --porcelain`, which any caller can already list.
- perf / scale — `--liveness` pays one more git spawn, and `--resume` one, two on the refusal path.
  PINNED, node `d` 2026-09-22: `--liveness` averaged 0.71 s over the fixture. An ELSEWHERE copy still
  pays the whole clock: a tick over two worktrees took 2.69 s against 1.57 s over one.
- error / empty / loading states — A record naming no branch prints `holder-ref: absent`, the tick
  skips it by name, and the matrix announces the per-copy reading. An unreadable HEAD is `fail 52`.
  `tools/push-main.sh` detaches the run worktree for the seconds of a `--prepare` (`:380`), and in
  that window every copy reads ELSEWHERE, so nothing acts, which is the safe direction.
- observability — `verdict: ELSEWHERE` and the `holder-ref` key; the tick's `skip · ELSEWHERE` and
  `skip · NO RUN BRANCH`; the stop-guard's `elsewhere` sidecar reason; and a check-58 message naming
  the branch, the worktree holding it and this worktree's HEAD.
- risks — (1) A holding session that ends its turn from a sibling worktree is allowed to (§8 F4); the
  recovery is the tick in the run's worktree once the run reads STALE there, 5400 s in gov, and only
  where the tick is registered, which node `d` is not. (2) Under `primary`, a `--resume` issued from
  the default-branch tree for `fail 55`'s remedy refuses naming the run's branch, and because each
  copy is re-bound where it sits, `--landed` then runs from the run's worktree too. (3) A re-run
  started on its predecessor's own branch still reaches unit 61's re-bind row before its
  `--preflight`, which then refuses at check 2: unit 61's §5 risk (4). (4) `git worktree add -f` or
  `git checkout --ignore-other-worktrees` puts one branch in two worktrees, and both then hold and
  each grades its own copy. (5) A run whose worktree was removed, or left detached by the lander's
  failure at `tools/push-main.sh:407`, is acted on by no copy until its branch is checked out again.
  (6) A run branch renamed mid-run leaves the record naming the old ref, with the same effect.
- testing — The arms §7 names, each staged RED in the pass and executed once at VERIFYING under
  attribution; the direct observations in §6 are fixture runs of the driver, the tick and the hook.
- migration — §4 Migration: no fact or file is added, and the population a new skip or refusal
  reaches is measured.
- user docs — The verb carrier's `--liveness` entry, the stop contract's §8, the protocol's KEEPALIVE
  paragraph, and the Skill's tick, what-wakes and Resume text.

## 6. Acceptance criteria

- **AC1** — When `--liveness tRun` runs in both worktrees of the two-worktree fixture with a gate log
  dated now under the run worktree's `<git-dir>/gate-logs/` only, the run worktree prints
  `verdict: LIVE` and the linked worktree prints `verdict: ELSEWHERE`. Each prints the fourteen keys
  it printed at `07997375`, in that order, then `holder-ref: refs/heads/run` as its fifteenth and
  last line. With the gate log removed, the run worktree prints `verdict: STALE` and the linked one
  still prints `verdict: ELSEWHERE`.
  Red when: the linked copy is graded on its own clocks and reads STALE while the run's own worktree
  reads LIVE, as measured at `07997375`, where the tick then resumes the linked copy.
  fixture: a scratch repository whose main worktree is on branch `run`, holding a conf, a README and
  one committed record with `run-branch: refs/heads/run`, a session and a dead pid, aged past a
  one-second bound, plus a worktree added on `wave` after that commit; §4 measured it, and the tree
  holds none.
- **AC2** — When `bash tools/unattended/resume-tick.sh --repo <fixture> --dry-run` runs over AC1's
  fixture with its gate log, it prints `skip · verdict LIVE` for the run worktree and
  `skip · ELSEWHERE` naming `refs/heads/run` for the linked worktree, and no `resumed ·` decision.
  With the gate log removed, it prints exactly one `resumed · attempt 1`, for the run worktree, and
  the linked worktree's ELSEWHERE skip again.
  Red when: a copy in a worktree not on the run's branch reaches the kill-and-relaunch row, measured
  at `07997375` as `resumed · attempt 1` for the linked worktree while the run worktree read LIVE; or
  the rule suppresses the run's own resume as well.
- **AC3** — When the run worktree of AC1's fixture moves its record to `HELD` and commits it there,
  so the linked worktree still carries the aged BUILDING copy, `resume-tick.sh --dry-run` prints unit
  61's `skip · HELD` for the run worktree, `skip · ELSEWHERE` for the linked worktree, and no
  `resumed ·` decision. In the tick suite, the same fixture with its recorded pid a live background
  `sleep` and no `--dry-run` leaves that `sleep` alive and never invokes the stub `claude`.
  Red when: the tick kills the holder's process and relaunches the run from a stale BUILDING copy in
  a sibling worktree, B1's first case.
  permission: the non-dry-run half is the tick suite's arm, a held kit suite on no bar leg, executed
  in the orchestrator's attributed VERIFYING run; the pass observes the dry-run decisions.
- **AC4** — On the authorized fixture with a linked worktree on `wave`, `CLAUDE_CODE_SESSION_ID=T`
  `--resume tRun --keepalive-id C` run in the linked worktree refuses at check 58 naming
  `refs/heads/unit` and the run worktree's path, and `--resume tRun` with no id there prints the
  `--status` block and then the same refusal. After both, `git status --porcelain` prints nothing in
  either worktree, and unit 28's `tRun.procs` ledger in the common dir's `unattended` directory is
  byte-unchanged. With every commit aged past `RESUME_STALE_BOUND`, the id call still refuses in the
  linked worktree, and run in the run worktree it prints `presumed-stopped` and takes the run over.
  Red when: a sibling copy reaches the matrix and is graded on that worktree's clocks, so a second
  session takes the slug over while its holder is live elsewhere, B1's second case; or a refused call
  reaps or prunes the shared ledger, the race unit 28's argument excludes.
  fixture: an authorized record at a pinned BASE over a local bare remote, committed on `unit` at a
  working phase with lease facts naming session `S` and keepalive `k1`, the shape the driver suite's
  prologue builds, plus unit 28's ledger holding one record; the tree holds none outside that suite.
- **AC5** — When AC4's id call runs in the linked worktree after `git checkout --detach` there, its
  check-58 message names `a detached HEAD`. When the run worktree is first moved off `unit` with
  `git checkout -b parked`, the message names `refs/heads/unit` and says that no worktree on this
  node has it checked out. Once `unit` is checked out in the run worktree again, the same call run
  there reaches the matrix rows unit 61 specifies.
  Red when: the refusal names no branch or no place, so its remedy is a guess; or a worktree regains
  the run by any act but checking the run's branch out.
- **AC6** — Under `LANDER_MODE="in-place"`, take a fixture whose committed LANDING record names
  `run-branch: refs/heads/unit` and is pushed to a local bare `origin`, so `--status` prints
  `phase LANDED (derived:`, and check out a new branch `rerun` at that commit: a re-run build's
  worktree before its `--preflight`. There `--resume tRun --keepalive-id k9` refuses at check 58
  naming `refs/heads/unit`, `git status --porcelain` prints nothing, and a following
  `--preflight tRun --keepalive-id k9` meets no check-2 refusal. Back on `unit`, the same `--resume`
  takes unit 61's re-bind row and stages the record. With unit 61's landed log naming the landing
  commit, the call on `rerun` prints nothing to resume and writes nothing.
  Red when: a keepalive tick issued before a re-run's `--preflight` re-binds the previous run's record
  and leaves the staged difference that preflight refuses at check 2, the audit's M5 against unit 61
  as specified; or the guard reaches the observed-landing row, so `--resume` refuses a landing that
  `--liveness` reads TERMINAL in every worktree.
- **AC7** — When `node tools/unattended/stop-guard.js` is fed a Stop payload bound to the record's
  session and its liveness reads `verdict: ELSEWHERE`, it exits 0, prints nothing on stdout, and its
  sidecar line carries `"reason":"elsewhere"`. With the real driver, a payload whose `cwd` is AC1's
  linked worktree allows with that reason, and the same payload with `cwd` at the run worktree, whose
  copy reads BUILDING and LIVE, is blocked with `run-open`.
  Red when: a copy in a worktree not on the run's branch blocks with `run-open` and tells the session
  to `--plan` from a stale copy; or the carve-out reaches the run's own worktree, so a live run's
  turn end goes unrefused.
- **AC8** — Over AC1's fixture with the `run-branch` line removed from both copies and no
  `branch-ref`, with no gate log, `--liveness` prints `holder-ref: absent` and `verdict: STALE` in
  both worktrees, and `resume-tick.sh --dry-run` prints two `skip · NO RUN BRANCH` decisions and no
  `resumed ·`. On AC4's fixture with both branch facts removed, `--resume tRun --keepalive-id k1`
  prints the no-run-branch announcement and then the matrix's holder row.
  Red when: the tick kills and relaunches a record no worktree can be shown to hold; or the matrix
  refuses the holder's own resume of a run preflighted on a detached HEAD, which wedges it for ever.
- **AC9** — At the build commit, `grep -c 'ELSEWHERE' tools/unattended/VERBS.template.md` and
  `grep -c 'holder-ref' tools/unattended/VERBS.template.md` each print 1;
  `grep -c "from a worktree not on the run's branch" tools/unattended/STOPS.template.md` prints 1;
  `grep -c "in the worktree on the run's branch" tools/unattended/PROTOCOL.template.md` and
  `grep -c "reading the run's own worktree" tools/unattended/PROTOCOL.template.md` each print 1,
  while `grep -c 'Registering the tick' tools/unattended/PROTOCOL.template.md` prints 0;
  `grep -c "reading the run's own worktree" tools/unattended/SKILL.template.md`,
  `grep -c 'check 58 naming another branch' tools/unattended/SKILL.template.md` and
  `grep -c 'means this worktree is not the run' tools/unattended/SKILL.template.md` each print 1; and
  `grep -c 'NO RUN BRANCH' tools/unattended/resume-tick.sh`,
  `grep -c 'ELSEWHERE' tools/unattended/resume-tick.sh` and
  `grep -c 'elsewhere' tools/unattended/stop-guard.js` each print at least 2.
  Red when: a carrier still says the stop-guard refuses every open run's turn end, or that the tick
  acts wherever the index holds a lease, so an agent following it waits for a refusal or a relaunch
  that no longer comes.
  permission: that each render is byte-identical to its template is the `unattended skill wiring`
  and `unattended kit gate` legs over the real tree, observed at the VERIFYING bar.
- **AC10** — When `git cat-file -s` and `wc -l` read `tools/unattended/PROTOCOL.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/STOPS.template.md`,
  `memory/guides/UNATTENDED-STOPS.md`, `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md` at the build commit and at its first parent, no build-commit
  figure is greater than its parent's.
  Red when: an addition lands without its trim, so the protocol, already over its cap under a
  curation-debt waiver, grows; or the reading is taken against this spec's figures instead of the
  parent commit.
  figure: the −32, −4 and −33 bytes of §4 are PINNED at `07997375` against that base's text; the
  not-greater test is derived at the build commit.
- **AC11** — When the orchestrator's attributed run reads `verdict clean` over the driver,
  resume-tick and stop-guard suites at VERIFYING, the arms §7 names are among the
  executed ones, with the driver suite's three `--liveness` key arms expecting fifteen keys ending in
  `holder-ref`, and the tick suite's `build_fixture` writing `run-branch: refs/heads/main`; and each
  floor S8 names reads, at the build commit, its figure at the first parent plus exactly the
  assertions this unit's new blocks carry, read with `git show` at both.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or an
  existing arm that reached a guarded row off the record's branch was deleted rather than
  retargeted, so the executed count falls while the floors rose by the new arms alone; or a floor is
  left where the arms found it, or moves by a number no new arm accounts for.
  permission: the three suites are held kit suites on no bar leg, so they run in the orchestrator's
  attributed VERIFYING run and never in this pass.
- **AC12** — When `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` runs for
  `resolve_holder_worktree`, `check_holder_worktree` and `add_sibling_worktree`, each prints `OK`.
  The new check-58 branch has an arm. The rows of `memory/project/unarmed-branches.txt` for the
  driver, which pin checks 9, 27, 29, 49 and 56, are unchanged, with no `fail` line of those numbers
  added or removed. `grep -c 'KIT_UNATTENDED_VERSION=1.29' tools/unattended/unattended.sh` prints 1,
  and no added line of a shipped kit file spells a `tools/<kit>/` literal.
  Red when: a name leads with a verb the table does not carry; a pinned row's ordinal moves under it
  unnoticed; the unreleased kit moves a version; or a new line spells a path the install-prefix ban
  forbids.
  permission: the verdicts are the `lexicon naming predicates`, `harness arms (fail branches armed or
  pinned)`, `kit version markers` and `install-prefix (shipped surface)` legs, observed at the
  VERIFYING bar.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a linked worktree added on `wave` after the record commit, with the take-over and no-id calls refused there and the ledger read back, the detached and no-holder message variants, the in-place re-run on a new branch with and without the observation, and the no-run-branch announcement; staged RED by a driver copy whose `check_holder_worktree` always returns 0 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, each raised by exactly the new arms' assertions, counted off their blocks
New arm: `tools/unattended/resume-tick.test.sh` · `add_sibling_worktree` over a live run, a stale run, a HELD run beside a stale BUILDING copy whose recorded pid is a live `sleep`, and a record naming no run branch; staged RED by a driver copy whose verdict chain drops the ELSEWHERE row · `FLOOR_ASSERTIONS`, raised by exactly the new arms' assertions, counted off their blocks
New arm: `tools/unattended/stop-guard.test.sh` · a stubbed `verdict: ELSEWHERE` bound to the payload's session; staged RED by a hook copy without the `elsewhere` row · `FLOOR_ASSERTIONS`, raised by exactly the new arm's assertions, counted off its block

The driver suite's key arms at `tools/unattended/unattended.test.sh:5880`, `:5882` and `:5897`
move from fourteen keys to fifteen, and the tick suite's `build_fixture` at
`tools/unattended/resume-tick.test.sh:147` gains the `run-branch` line. Neither is an arm this unit
adds, and neither moves a floor.

Every floor follows this build's practice, set by the CLOSED units 25, 30, 49 and 54: a unit raises
its suite's executed-assertion floor by exactly the arms it adds, derived from the blocks rather than
read off a run, which this pass does not make. The driver's new arms are written in region two, so
`FLOOR_SHARD_1` does not move.

## 8. Open questions

- **F1 — which route gives one answer per slug.** Options: (a) act only in the worktree whose
  checked-out branch is the record's run branch, every other copy reading a named non-holder
  verdict; (b) `derive_last_move` takes the newest move across every worktree whose index names the
  same slug and session. RESOLVED (agent, 2026-09-22, delegated): (a), the audit's smaller route and
  the one the orchestrator's brief names, decided under the delegated M3 rule as unit 61's F1 was.
  (b) gives every copy the same verdict, and so the same act: two worktrees reading one STALE would
  each kill and relaunch, because the tick's in-flight and attempt state is per worktree. It also
  costs one clock per carrying worktree on every `--liveness` call, which the tick makes once per
  worktree, and a sibling's unrelated commit would keep a dead holder fresh, widening the audit's M3.
  (a) needs no new clock, and the uniqueness it rests on is git's.
- **F2 — which fact names the run's branch.** Options: (a) `branch-ref` alone, as the audit wrote it;
  (b) `run-branch`, else `branch-ref`. RESOLVED (agent, 2026-09-22, delegated): (b). Fact 10 is
  written only where the second anchor fired, so a default-branch run carries none, by the driver's
  own account at `tools/unattended/unattended.sh:4938`, and (a) would give the protocol's primary
  anchor no holder anywhere. (b) is `gate-guard.js`'s key at `:598`, so the two readers key one run
  to one worktree, and this build's record, which carries only fact 10, is keyed exactly as (a)
  would key it.
- **F3 — a record naming neither fact.** Options: (a) graded per copy by every actor, as at this
  base; (b) the tick acts on it nowhere, by a named skip, while the matrix and the stop-guard grade
  the copy they read and the matrix says so; (c) as (b), with the matrix refusing too. RESOLVED
  (agent, 2026-09-22, delegated): (b). The tick is the one actor that kills a process and launches a
  skip-permissions session with nobody watching, so its safe side is acting nowhere. (c) would
  refuse for ever the holder's own resume of a run preflighted on a detached HEAD, which
  `check_branch` admits (`:1758`). (a) leaves B1 open for that population, which is measured empty.
- **F4 — what the stop-guard does with ELSEWHERE.** Options: (a) allow, reason `elsewhere`; (b) fall
  through to `run-open`; (c) a new block naming the run's worktree. RESOLVED (agent, 2026-09-22,
  delegated): (a). The copy cannot tell a HELD run from a working one, so (c) blocks a held session,
  and (b) tells the session to `--plan` from a stale copy. Every other path on which the hook cannot
  read the run allows, which its header states as its rule. The cost is §5 risk (1).
- **F5 — which rows the refusal guards.** Options: (a) every row after `check_asks_pinned`; (b) the
  re-bind row, every HELD row and every working row, leaving unguarded the recorded terminal, the
  derived terminal resumed with no id and the observed landing. RESOLVED (agent, 2026-09-22,
  delegated): (b). Each unguarded row writes nothing, and each is the answer every copy carrying the
  record gives, which is the one-answer property itself: a recorded terminal is frozen, and the
  observation sits in the common-dir log. (a) would turn a landed record's nothing-to-resume into a
  refusal from the primary tree, and it changes the arm at `tools/unattended/unattended.test.sh:2992`.
  Both options keep the `--scheduled` refusals ahead of the matrix, so the detached-HEAD arm at
  `:7977` still meets check 60.
- **F6 — the refusal's number.** Options: (a) a new branch of check 58; (b) a new check number.
  RESOLVED (agent, 2026-09-22, delegated): (a). Check 58 is the matrix's refusal of a second driver,
  which this is, it carries no pinned row, and a new number could collide with one minted by a unit
  ordered before this one.
- **F7 — the holder of a pushed `primary` landing.** Options: (a) always the run-branch worktree;
  (b) the default-branch worktree once the witness is on the default branch, where `verb_landed`'s
  header says landing happens. RESOLVED (agent, 2026-09-22, delegated): (a). `verb_landed` calls no
  `check_branch` (`:3946`), and the driver suite runs a `primary` `--landed` from the run branch at
  `tools/unattended/unattended.test.sh:9126`, so `fail 55`'s remedy and the landing both work from
  the run's worktree. (b) would read the landing session's own worktree as ELSEWHERE, taking the
  stop-guard's `landing-unstamped` block away from the session it exists for, and would need the
  ancestry test in a second caller. The residual is §5 risk (2).
- **F8 — the linked worktree in the tick suite.** Options: (a) every `build_fixture` adds one, the
  audit's left-shift as written; (b) `add_sibling_worktree`, called by the arms whose property is the
  worktree walk. RESOLVED (agent, 2026-09-22, delegated): (b). PINNED on node `d` 2026-09-22, a tick
  over two worktrees took 2.69 s against 1.57 s over one, so (a) adds about 1.1 s to each of the
  suite's 39 tick runs, about 44 s, for arms whose properties are not the walk. The class stays
  gated: every actor the verdict reaches has an arm over two copies, and a new tick row can reach
  the walk only through `--liveness`, whose verdict order AC1 observes.

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, promoted from B1 of the G8 round-1 audit of unit 61 by route
  (a), grounded on `07997375` and on unit 61 as specified, with B1's tick half re-measured over a
  two-worktree scratch fixture.
- rev-2 · 2026-09-22 · §2 S8 · §6 AC11 · §7 · each suite's executed-assertion floor rises by
  exactly the arms this unit adds, counted off their blocks and never read off a run, where rev-1
  moved none: the practice the CLOSED units 25, 30, 49 and 54 set. This unit's consumes-from edges
  are now answered by hands-off lines in `TOOL-dDerivedDocket-61` and `TOOL-dDerivedDocket-28`.
  `TOOL-dDerivedDocket-64` declares no edge to this unit: route (a) leaves `derive_last_move` per
  worktree, as unit 61 extracts it, so that unit's heartbeat term consumes nothing written here. No
  design, other criterion, edge or order moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether this worktree is the one that has the
run's branch checked out"` returns no seam for this work: its candidates are name-stem matches
(`run`, `check`, `build_run_model`) in the Python kits, and its header prints `unscanned layers:
.sh`, the layer the driver and the tick are written in. So no existing seam fits in the corpus the
probe reads. The seams this unit extends were found by reading source: `resolveRunPhase` in
`tools/unattended/gate-guard.js` (`:586`), which keys a record to the worktree whose own HEAD equals
`run-branch`, else `branch-ref`; the fact-13 writer in `verb_preflight`
(`tools/unattended/unattended.sh:4943`), whose `git symbolic-ref -q HEAD` this unit reads back; and
`verb_landed`'s walk of `git worktree list --porcelain` for a LANDING sitting in another worktree
(`:3980`), the listing the refusal's path lookup reads.

Recall terms used: `python tools/memory-recall/query.py "which worktree may act on an unattended
run when several worktrees carry a copy of its run-state file" --terms "worktree common-dir lease
resume-tick liveness per-worktree copy run-branch branch-ref gate-guard take-over holder"`. It
returned the audit's B1 itself; TOOL-aDeferredBar-3's S2, the branch key this unit reuses;
TOOL-aUnblockedFleet-7, the lander marker every worktree of one clone shares; TOOL-aWokenSentinel-13,
which made the tick's knobs root-scoped for the same one-answer reason; and unit 61's common-dir
landed log.
