# TOOL-aNimbleMend-12 — the acceptance suite: one pass-leg run and one inline fix, end to end, in a scratch adopter and in a clone of gov, with each switch on and off

**Status:** CLOSED · rev-2 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aNimbleMend-12-1-acceptance-ledger.md](../build/2026-11-12-build-TOOL-aNimbleMend-12-1-acceptance-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 |
| [2026-11-12-prompt-TOOL-aNimbleMend-12-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-12-build-brief.md) | research | — |
| [2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md](../reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md) | diff-review | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-13 |

<!-- /gen:spec-records -->

## 1. Goal

Each unit of this build proves its own piece in its own fixture, and no fixture runs the pieces in
the order a build runs them: a pass leg goes red, the lane opens, the fix is committed, the leg
goes green, the record is joined. This unit adds two outcome cases to the policy kit's fixture
suite that run that order once in an installed scratch adopter and once in a clone of gov, and
that show each switch set `off` leaving what the tree did before.

## 2. Scope (IN)

- **S1** — Two outcome cases in `tools/policy/check_policy.py#CASES`, `pass-and-lane-adopter` and
  `pass-and-lane-gov`, both run by one function, `run_pass_lane_case`, and each runnable alone as
  `python tools/policy/check_policy.py --fixture <case>`. Observed by AC1 and AC6.
- **S2** — The adopter case's target: the deployer's install of the kits the flow needs into a
  fresh repository, by `build_install_target` and one `apply` through `run_govkit`, with every
  installed file found through its receipt row. Observed by AC1.
- **S3** — The gov case's target: `build_source_snapshot`'s clone of the tree under test, with no
  remote, so its local `main` is the landed revision the policy readers read. Observed by AC6.
- **S4** — The flow of §4, "The flow", in both targets with both keys at their defaults: steps 1
  to 11 and their expected outcomes. Observed by AC1, AC2, AC3 and AC6.
- **S5** — The lane switch: with `bar.inline-red-fixes` set `off` on the target's `main`, the
  write gate's refusal of the product write is byte-identical to its refusal with no red open, and
  the commit grader's pushed-range half lists the fix commit as naming no unit. Observed by AC4.
- **S6** — The pass-leg switch: with `pass.fast-legs` set `off` on the target's `main`, the adapter
  exits 0 with one line naming the key, and the run record and the gate ledger are byte-identical
  to what they were before the call. Observed by AC5.
- **S7** — The `policy fixtures` row of `tools/gate-legs.json` gains a guard entry for each file
  the two cases execute that the guard does not hold, as §4, "The guard", lists them. Observed by
  AC7.
- **S8** — `tools/policy/README.md` names the two cases where it names the suite's outcome cases,
  with what each observes and what neither does. Observed by AC8.
- **S9** — The build's two tree-wide acceptance sentences, observed once on gov's own tree at the
  close: the declared list holds no excluded leg and passes its budget gate, and one run of the
  adapter over the last unit pass's diff ends inside the limit. NOT OBSERVED by an arm: they
  are readings of gov's own declared list on node `a`, which a fixture cannot hold. AC9 and AC10
  record them.

## 3. Non-goals (OUT)

- Any arm a building unit owns. The lane's decision rows, the grader's table, the join's six
  findings, the limits, the adapter's findings, the budget gate's planted over-budget list and the
  hooks' role-gate row are each graded in that unit's own suite. This suite runs the pieces in
  order and asserts the seams between them.
- A red planted on one of gov's real legs. The gov case declares one planted row and strips the
  field from every other row of its clone (§4, "The gov clone"; F2).
- Running the unit harness. A workflow script runs only inside the harness tool, so the case
  performs the main loop's part of a pass and reads the harness's constant as text.
- Running the derivation's write verb in the adopter. An installed adopter has no bar run log, so
  the case observes the empty list and then plants the field on one row.
- The hooks' refusal of the adapter to a role agent, and the gate guard's phases.
- A comparison against the base commit's code run side by side (F1).
- A page under `help/`, and the kit version markers, which the lander's `mint` moves once.

### Edges

- **consumes-from** `TOOL-aNimbleMend-1` — both keys, their `off` value, and the rule that a reader
  takes the landed revision. Without them S5 and S6 have no switch, and a key set on a branch
  would change nothing.
- **consumes-from** `TOOL-aNimbleMend-2` — the pass-leg field on a manifest row, and the fact that
  an installed adopter declares none until its write verb runs. Without it step 1 has no empty
  list to observe and step 3 no row to plant.
- **consumes-from** `TOOL-aNimbleMend-7` — the harness constant that spells the adapter's
  invocation, which the gov case reads. Without it the command a main loop is told to run is not
  the command this suite observed.
- **consumes-from** `TOOL-aNimbleMend-8` — the lane at the write gate and at the commit grader, and
  the trailer. Without it steps 5, 6 and 11 have nothing to admit.
- **consumes-from** external — the rest of the built tree the flow runs: the adapter and its run
  record, the figures and budget verbs, the `red-fix` record door and its join, and the limits
  verb. A step whose subject the tree does not hold is a WRONG line naming it, never a skip.
- **hands-off** external — the main loop observes the arm of §7 RED and then GREEN at the close,
  and makes the two readings of S9 there.

## 4. Design

### Evidence

Read at 97e0841d; line numbers are of `tools/policy/check_policy.py@5796989f`.

| Fact | Where |
|---|---|
| The suite's cases are one table, `CASES`, of `(name, arm, function)`, and an outcome case has no arm. | `:4587-4642` |
| `--fixture <case>` runs the one case named. | `:4760-4771` |
| `build_install_target(name, ids)` snapshots the tree under test, runs the deployer's `intake` over a fresh repository and returns the target and the snapshot. | `:1138-1181` |
| `run_govkit` runs the snapshot's own deployer and refuses any root the snapshot builder did not make. | `:1184-1205` |
| An installed file is found through `read_receipt_rows`, by its path's ending. | `:1208-1211`, `:1459` |
| `check_hook_call` runs a hook with a JSON payload on stdin and judges exit code and stderr. | `:2898-2909` |
| `print_checks` prints one `policy-fixture: <case> · <scenario> · <what> · ` line per check and `WRONG:` on a miss. | `:1574-1578` |
| The `limit-` cases are the precedent: one planted repository per case, one key, a hook run against it. | `:2934-3232` |
| `check_guard_trace` reds a source file the suite reads that trips no `policy fixtures` guard, and says it cannot see a file a child process reads. | `:4233-4245` |
| `check_guard_lines` reds a guard entry that names no tracked file. | `:4298-4306` |
| The leg is gov's own, an `[[exempt_leg]]`, so no adopter runs these cases. | `tools/govkit/registry.toml@1922070d:738-740` |
| The leg's budget row is 970 s against 644 s measured over 150 cases (PINNED, 2026-10-25, in the row). | `tools/run-gates/selftest-budgets.txt@0737691e:84` |
| The leg's guard holds `scratch-guard.js`, `agent-cap.js`, `routed_commits.py`, `tree_lib.py`, `gotchas.py`, the policy kit and the harness template, and holds no file of the adapter and not `build_records.py`. | the `policy fixtures` row of `tools/gate-legs.json` |
| Gov's conf routes `tools/` and `skills/` and names its leg manifest. | `.memory-tree.conf`, `ROUTED_PATHS` and `LEG_MANIFEST` |

### The two targets

**The adopter.** `build_install_target(name, ids)` with the registry ids `policy`, `run-gates`,
`agent-cap` and `memory-tree`, widened by `derive_requires_closure`, then
`run_govkit(snapshot, top, "apply", "--target", <target>)`, as `run_fresh_target` installs its
own. The case then
writes what an adopter would have written by hand, and commits it on `main`:

- in the target's `.memory-tree.conf`, `ROUTED_PATHS="src/"`, `LEG_MANIFEST` naming the installed
  manifest, and a `ROUTED_COMMIT_CUTOFF` before the fixture's first commit;
- one build folder under the target's memory root, holding one conforming spec whose id is spelled
  in a family the target's conf declares, so the record door has a build and a unit;
- `src/app.txt` holding the one line `ok`.

The target has no remote, so its local `main` is the landed revision.

**The gov clone.** `build_source_snapshot(top)`, then every remote removed and `main` set to the
clone's HEAD. It keeps gov's conf, role index and policy file as they are. The product path is a
planted file, `tools/planted-pass-leg.txt`, and the record's build and unit are this build's
folder and this unit's id, which the clone holds. The case removes the pass-leg field from every
row of the clone's manifest, so the run costs one leg (F2).

Both targets get a `GATE_TURNSTILE_DIR` of their own in the environment of every adapter call, so
no step waits behind a real bar on the host.

### The planted leg

One row appended to the target's leg manifest, carrying the pass-leg field as the manifest spells
it:

```json
{"name": "planted pass leg", "argv": ["python", "-c", "import sys; sys.exit('BROKEN' in open(sys.argv[1], encoding='utf-8').read())", "<product file>"], "chunk": "product", "subject": "repo", "ceiling": 60, "pass_leg": true}
```

`<product file>` is `src/app.txt` in the adopter and `tools/planted-pass-leg.txt` in the gov clone.
The leg is red exactly while that file holds the word `BROKEN`. The row carries no `guard`, so it
runs on every diff.

### The flow

Each step is one check line. `P` is the product write: a `Write` payload for the product file,
with the target as `cwd`, a session id that has no orientation card, and no `agent_type`, which is
the main loop. `R0` is the stderr of step 2.

| # | Scenario | What the case does | Expected |
|---|---|---|---|
| 1 | `install` | adopter only: runs the adapter with `--base HEAD` before any row carries the field | exit 0 and the adapter's empty-list line |
| 2 | `on` | plants the leg, commits; runs the join and keeps its counts; sends `P` to the write gate | the gate refuses, as it refuses any product write with no routed unit; `R0` kept |
| 3 | `on` | writes `BROKEN` to the product file and commits it as the pass commit; runs the adapter with `--base HEAD~1` | exit 1; the run record's `leg` line for the planted leg reads `fail`; the ledger holds a red row for it |
| 4 | `on` | sends `P` | exit 0, and one witness line naming `planted pass leg` and `Red-fix:` |
| 5 | `lane-off` | commits the policy file with the lane key `off`; sends `P`; then commits the key's removal | the gate refuses, and its stderr equals `R0` byte for byte |
| 6 | `on` | writes `ok` back and commits with the trailers `Red-fix: planted pass leg` and `Pass: none`, no unit id; runs the limits verb on `HEAD` | the verb exits 0 |
| 7 | `on` | runs the adapter with `--base HEAD~1` | exit 0; the `leg` line reads `ok` |
| 8 | `on` | sends `P` | the gate refuses, and its stderr equals `R0`: the lane closed with the red |
| 9 | `on` | runs the record door for the fix commit, with the leg, a red line, and step 7's command and result as the re-run; commits the record | exit 0, and one record of the kind in the build folder |
| 10 | `on` | runs the join | exit 0, and the summary's fix-commit and record counts each one above what the join printed at step 2, with `0 owed` |
| 11 | `on` | adopter only: runs the commit grader with `GATE_PUSH_BASE` at the pass commit | the pushed-range summary holds `1 red-fix`, and no violation line names the fix commit |
| 12 | `lane-off` | adopter only: commits the lane key `off`; runs the grader as in step 11 | the pushed-range half lists the fix commit as `names no unit` |
| 13 | `legs-off` | commits the pass-leg key `off`; hashes the run record and the ledger; runs the adapter with `--base HEAD~1`; hashes them again | exit 0, one stdout line naming `pass.fast-legs`, and both hashes unchanged |

The gov case adds two checks and drops steps 1, 11 and 12. The grader's other half grades gov's
whole history, and the leg that runs this grader over gov's tree measured 636.8 s in the owner's
prompt. The grader reads a tree's conf and history and no role index, so the adopter's two steps
are the observation.

| # | Scenario | What the case does | Expected |
|---|---|---|---|
| g1 | `setup` | reads `PASS_LEGS` from `tools/workflows/unattended-build.template.js` as text | it names the adapter's path under the tool root and `--base`, the invocation steps 3, 7 and 13 run |
| g2 | `on` | after step 4, sends `P` with `agent_type` set to a role of gov's index that declares no product write | the gate refuses |

Every key flip is a commit on `main` that touches the policy file alone. Where the target carries
a policy mirror, the flip is followed by `policy.py mirror --write` and a second commit of the
mirror, the two-commit order TOOL-aNimbleMend-1's rollout states, so no read is refused for a
stale mirror. Steps 6 and 9 are adjacent commits, so the record is the fix's next commit, which
the join's staged form requires. In the adopter the join's counts at step 2 are zero, so step 10
reads `1 fix commit(s) · 1 record(s) · 0 owed`. Every
expected string is the one the built tree prints: where a sibling's revision moved a line, the
case asserts the line as built, and no expectation is copied from a spec.

### What "byte for byte" is, here

The case holds no copy of the old texts. It compares two outputs of the tree under test:

- the write gate's refusal with the lane key `off` and a red open, against its refusal with the
  key `on` and no red open, which is the path every product write took before this build;
- the run record and the ledger before and after an adapter call with the pass-leg key `off`.

The grader's half is step 12's violation text, `names no unit`, the words the grader prints today
for a commit with no id.

### The guard

`tools/gate-legs.json`'s `policy fixtures` row gains, in its `guard` list:

```text
{prefix}/run-gates/pass-legs.sh
{prefix}/run-gates/pass_legs.py
{prefix}/memory-tree/build_records.py
```

Each is executed by a case through an installed copy or the clone, which `check_guard_trace`
cannot see, and none is in the guard at 97e0841d. `check_guard_lines` requires each to be tracked,
which units 2 and 5 make true before this unit builds. The bar runner is not added: it is the
adapter's engine, every bar already runs it, and guarding this 644 s leg on it would run the leg <!-- PINNED 2026-11-12 -->
on every runner edit.

### What it does not check

- That the old behaviour equals the base commit's bytes. The comparison is between two paths of
  the built tree (F1). The texts of the unchanged path are pinned by the write gate's own suite.
- Any of gov's real legs red. The gov clone runs one planted row.
- The harness, the router sentences, or a role agent's refusal at the hooks.
- The adopter's own derivation of a list.
- The return of the unit harness with the pass-leg key `off`, which TOOL-aNimbleMend-7's F1
  decides.
- A lane commit already in history under a key turned `off`. Step 12 grades the pushed range.
- The commit grader in gov's own tree. The close's bar runs that leg over gov's history.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| function `run_pass_lane_case` | `tools/policy/check_policy.py` | cell `py.function`; `lexicon.py --suggest run_pass_lane_case --as py.function` answered OK on 2026-11-12 |
| cases `pass-and-lane-adopter`, `pass-and-lane-gov` | `CASES` | no cell grades a case name |
| scenario labels `install`, `setup`, `on`, `lane-off`, `legs-off` | check lines | no cell grades a label |
| fixture leg name `planted pass leg` | the targets' manifests | no cell grades a fixture leg |

### Migration

None. Two cases join a table, and three entries join one guard.

### Rollout

No switch. The cases run where the `policy fixtures` leg runs, which is gov's bar alone.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `tools/gate-legs.json`

### Alternatives rejected

- **A shape in `tools/govkit/matrix.py`.** The matrix grades repo shapes of the deployer and cites
  the mechanism suites rather than re-running them, and its leg measured 1084.3 s in the owner's
  prompt. These cases grade two policy switches, which is what the policy fixtures already do for
  the agent limit.
- **A new suite file.** It would need a third copy of the snapshot, install and hook-call helpers
  this suite already holds, and a new leg with its own guard, budget row and registry rows.
- **Four cases, one per target and mechanism.** The lane's red comes from the pass-leg run, so two
  of the four would rebuild what the other two had just run, at one install each.
- **Running the cases from each kit's own suite.** No kit suite holds an installed target with the
  policy kit beside the other three, which is why TOOL-aNimbleMend-5 hands its key-off arm here.

## 5. Production-readiness checklist

- security — The cases write only under their own temporary roots and remove them in a `finally`,
  as every case of the suite does. The lane is exercised with a main-loop payload and with a role
  that may not write product, so a lane that admits the second is a WRONG line.
- perf / scale — One install and one snapshot per run of both cases. The planted leg runs in under
  a second, and the gov clone declares no other leg. The added wall time is UNVERIFIED until the
  close measures the leg; `run_fresh_target` is the nearest reading and prints its own seconds.
- error / empty / loading states — A missing deployer, a refused install, or a step whose subject
  the tree lacks is a WRONG line naming it. A case that asserts nothing is a WRONG, as the suite's
  count line requires.
- observability — One `policy-fixture:` line per step, each with what it observed.
- risks — The leg's budget row is 970 s. If the two cases take the leg past it, the row is <!-- PINNED 2026-11-12 -->
  re-measured by its file's own rule at the close. The conf keys an installed adopter needs for
  the write gate and the grader are written by the case, and a key this spec did not foresee is
  the builder's to add and to name in the ledger.
- testing — The two cases are the tests. §7 declares their arm, staged red at the close.
- migration — None.
- user docs — `tools/policy/README.md`, S8. The help pages are TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

`A` is `python tools/policy/check_policy.py --fixture pass-and-lane-adopter` and `G` is
`python tools/policy/check_policy.py --fixture pass-and-lane-gov`. Each prints one
`policy-fixture:` line per step of §4, "The flow", then the suite's count line. `<kit>` is the
run-gates kit's directory, `tools/run-gates` in this repository; its two new files are spelled
through it because neither is tracked before units 2 and 5 build.

- **AC1** — When `A` runs, it prints 13 step lines, none holding `WRONG:`, its `install` line
  quotes the adapter's empty-list line, and its last line reads `0 wrong`.
  Red when: the install lacks a kit the flow needs, a receipt row is missing, or any step fails.
  cost: one snapshot and one install, minutes.
  figure: 13 is DERIVED from the flow table; the count line's own figure is the suite's.
- **AC2** — When `A` runs, the line of step 3 shows exit 1 and the planted leg `fail`, the line of
  step 4 shows exit 0 with `planted pass leg` and `Red-fix:` in the witness, and the line of
  step 8 shows a refusal equal to `R0`.
  Red when: a red pass leg does not reach the ledger, the lane does not open on it, or the lane
  stays open after the leg ran green.
- **AC3** — When `A` runs, the line of step 2 shows the gate refusing the product write while no
  red is open, the line of step 10 shows `1 fix commit(s) · 1 record(s) · 0 owed`, and the line of
  step 11 shows `1 red-fix` with the fix commit absent from the violations.
  Red when: a product write that answers no red is admitted, the record does not join its commit,
  or the grader refuses a well-formed lane commit.
- **AC4** — When `A` runs, the line of step 5 reads that the refusal with `bar.inline-red-fixes`
  `off` equals `R0` over the same number of bytes, and the line of step 12 shows the fix commit
  listed as `names no unit`.
  Red when: the key `off` leaves the lane open at the gate, adds a line to the refusal, or leaves
  a pushed lane commit admitted.
- **AC5** — When `A` runs, the line of step 13 shows exit 0, one stdout line naming
  `pass.fast-legs`, and the run record and the ledger each with the same hash before and after.
  Red when: the adapter runs a leg, writes a record or prints a verdict with the key `off`.
- **AC6** — When `G` runs, it prints 12 step lines, none holding `WRONG:`; its `setup` line shows
  `PASS_LEGS` naming the adapter and `--base`; its g2 line shows the gate refusing a role that
  declares no product write while the red is open; and its lines for steps 4, 5, 8 and 13 show
  what AC2, AC4 and AC5 state for the adopter.
  Red when: the lane or the adapter behaves in gov's own conf, role index and prefix other than in
  an adopter's, or the harness names a command the adapter does not take.
  cost: one snapshot of the working tree, under a minute, and thirteen short steps.
  figure: 12 is DERIVED from the two flow tables, ten shared steps and two of gov's own.
- **AC7** — When `python tools/check-spec-tokens.py --legs-for -` reads the three paths of §4,
  "The guard", on stdin, it names `policy fixtures` for each, and `git ls-files` lists each.
  Red when: an edit to the adapter, the derivation module or the record door alone would skip the
  leg whose cases execute it.
- **AC8** — When `grep -c -e "pass-and-lane-adopter" -e "pass-and-lane-gov" tools/policy/README.md`
  runs it prints at least 2.
  Red when: the kit's README lists its outcome cases and omits these two.
- **AC9** — When `python <kit>/pass_legs.py --budget` runs in gov's tree at the close, it exits 0,
  prints no `PASS-BUDGET FAILED` line, and its last line opens `pass-budget:` with a declared
  count above 0.
  Red when: the declared list is empty, holds a self-test, a kit-subject leg or the unattended kit
  gate, holds a leg over the cap, or its cost rows sum past the limit.
  figure: the count and the sum are DERIVED by the verb from the manifest and the cost rows.
- **AC10** — When `bash <kit>/pass-legs.sh --base <rev>` runs once in gov's tree on node `a` at the
  close, `<rev>` being the parent of the last unit pass's commit, the `over` line of
  `gate-pass-legs.txt` under the git dir reads `none` or `tolerance`, and its `wall_s` is at most
  the `limit_s` beside it.
  Red when: one pass's run of the declared list takes longer than the limit.
  cost: up to the limit, about eleven minutes.
  permission: the main loop runs it, once, before the close's bar; a role agent's hook refuses the
  adapter.
  figure: `wall_s`, `limit_s` and `over` are DERIVED by the adapter at the run; this spec pins none.

## 7. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy check` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once. `policy fixtures` holds the two cases and is in the held tier, so
the close runs it only where it asks for that tier; AC1 and AC6 are the direct runs of the two
cases alone. The two canaries and `measure-legs selftest` guard the leg manifest S7 edits. The kit
epoch leg expects the lander's `mint`.

New arm: tools/policy/check_policy.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the lane's decision made to return null for every writer, which turns step 4 WRONG in both cases, then the adapter's key read removed, which turns step 13 WRONG · none

## 8. Open questions

- **F1 — What does "the old behaviour holds byte for byte" compare?** The build's acceptance says
  it of each switch set `off`, and the old behaviour is the base commit's.
  - **A, two paths of the built tree.** With the lane key `off` and a red open, the gate's refusal
    is compared with its refusal under `on` and no red, the path every product write took before
    this build; with the pass-leg key `off`, the record and the ledger are compared before and
    after. The suite needs no history and runs in any clone. It does not prove the unchanged path
    itself kept its bytes; the write gate's own suite pins those texts.
  - **B, the base commit's code beside the built tree.** The case extracts the hooks kit and its
    libraries at the run's pinned base with `git archive`, runs both hooks over one payload and
    compares. It is the sentence read literally. It binds a suite arm to one historical sha, it
    cannot run in a shallow clone, and it reds every later, intended change to the refusal text.
  - **C, pinned literals.** The case holds the base's refusal text as a string. It is B's
    staleness with a hand-typed copy.
  - Recommendation: A.
  RESOLVED (agent, 2026-11-12, delegated): A, two paths of the built tree. B and C bind a suite arm to one historical sha or a hand-typed copy of it.
- **F2 — What does the gov case run as its pass-leg list?**
  - **A, one planted row, every other row's field removed in the clone.** The lane, the adapter,
    the grader and the record run under gov's own conf, role index, policy file and prefix, in
    about a minute. Gov's real list is read at the close by AC9 and timed by AC10.
  - **B, gov's declared list plus the planted row.** Every pass of the fixtures leg then runs the
    whole list, about 400 s by TOOL-aNimbleMend-2's reading, twice, inside a leg budgeted at <!-- PINNED 2026-11-12 -->
    970 s, and any real leg red in the clone for its own reason turns the case WRONG. <!-- PINNED 2026-11-12 -->
  - Recommendation: A.
  RESOLVED (agent, 2026-11-12, delegated): A, one planted row. Gov's real list is read and timed at the close.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seam is the policy kit's fixture suite. `python tools/codebase-map/reuse_lookup.py "an
acceptance suite installs gov into a scratch adopter and observes a mechanism with its policy
switch on and off"` ranked `scratch`, `adopt`, `read_policy_value`, `build_scratch_gov` in
`tools/govkit/fixture_target.py` and `run_in_gov` in `tools/govkit/matrix.py`. Reading them:
`build_scratch_gov` makes an empty synthetic gov a fixture fills, and `run_in_gov` runs the
deployer from a frozen clone of HEAD, which `tools/policy/check_policy.py#run_govkit`'s own
docstring rejects for grading the bytes under test. The seam this unit extends is in that file:
`build_source_snapshot` and `build_install_target` for the two targets, `run_govkit` for the
install, `read_receipt_rows` for each installed path, `check_hook_call` for the write gate,
`run_case_argv` for each command and `print_checks` for the lines, with the `limit-` cases as the
shape of one key observed through a hook in a planted repository. For running a pass-leg run and a
lane fix in order, no existing seam fits: `grep -n "pass-legs\|Red-fix" tools/policy/check_policy.py
tools/govkit/matrix.py tools/unattended/cross-component.test.sh` finds nothing at 97e0841d, the
mechanisms being this build's. Recall returned TOOL-dGroundRules-16, the fresh target as a standing
case, and TOOL-dGroundRules-32, whose fixtures `adopter-fresh-target` and `census-default-adopter`
are the install cases these two sit beside; and PLAY-dOrderedCharter-78, which records that a case
needing a kit absent or present needs a scratch install and not gov's own engine.

Recall terms used: `python tools/memory-recall/query.py "where does an end to end acceptance suite
install gov into a scratch adopter and observe a policy switch on and off" --terms "acceptance
matrix scratch adopter fixture policy key default switch byte-identical cross-component e2e
install"`
