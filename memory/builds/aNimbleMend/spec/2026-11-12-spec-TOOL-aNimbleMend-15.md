# TOOL-aNimbleMend-15 — the closing review's thirteen mediums and four lows, batched: the pass-leg tooling, the commit grader, the hooks, three guards and two help pages say and check what they do

**Status:** INPROGRESS · rev-2 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aNimbleMend-15-1-acceptance-ledger.md](../build/2026-11-12-build-TOOL-aNimbleMend-15-1-acceptance-ledger.md) | journal | — |
| [2026-11-13-build-TOOL-aNimbleMend-15-override-1.md](../build/2026-11-13-build-TOOL-aNimbleMend-15-override-1.md) | override | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-15-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-15-brief.md) | research | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-15-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-15-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build confirmed thirteen MEDIUM and four LOW items, and the build
method's M4 batches them into this one unit. Each is fixed as the review record states it, so the
two mechanisms land with their contained defects closed and each fix held by an arm that can fail.

The record is
`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`.
An item below is named by its heading there, `M1` to `M13` and `L1` to `L4`.

## 2. Scope (IN)

- **S1** — M1. `tools/workflows/unattended-unit.js` writes the builder's `sha` into `nextAction`
  only when it matches `/^[0-9a-f]{7,64}$/`. Any other value names no commit there. Observed by AC1.
- **S2** — M2. `tools/run-gates/pass_legs.py#read_red_counts` skips a run-log line whose `run`
  value opens `pass-`, and its docstring says so. Observed by AC2.
- **S3** — M3. `cmd_check` and `cmd_apply` of `tools/run-gates/pass_legs.py` compare the rendered
  text with the LF text `read_manifest` returned. `cmd_apply` writes only on a real difference and
  keeps the file's own line ending. Observed by AC3.
- **S4** — M4. The ledger writer of `tools/run-gates/run-gates.sh` records `retried` only for a
  retry that exited 0, and the retry's own status for one that did not. Observed by AC4.
- **S5** — M5. In `tools/gate-legs.json` the guards of `scratch-guard self-test` and
  `routed-commits selftest` name `{prefix}/policy/`, and the guard of `policy fixtures` names
  `{prefix}/run-gates/` whole and no single file of that kit. Observed by AC5.
- **S6** — M6. The `[[regenerate]]` row of `tools/run-gates/kit.toml` runs its `argv` and its
  `check` behind the leg shim, so the freshness preflight grades the manifest beside the kit under
  any runner. Observed by AC6.
- **S7** — M7. `tools/memory-tree/routed_commits.py` reads a blank `LEG_MANIFEST` as the manifest
  beside the resolved run-gates kit. The write gate's open-red reader in `tools/hooks/scratch-guard.js`,
  which `TOOL-aNimbleMend-14` made close the lane on a blank key, reads a blank key the same way, so
  both halves of the lane open on a default install. The conf example and `help/red-fix-lane.md` state the key, and
  the adopter case of `tools/policy/check_policy.py` writes no `LEG_MANIFEST` line. Observed by AC7.
- **S8** — M8. The pass-budget block of the run-gates evidence suite gains arms for `--write`,
  `--report` and `--check`, spec 2's fixtures F and B as code. Observed by AC8.
- **S9** — M9. The self-test of `tools/memory-tree/routed_commits.py` gains three arms that reach
  the real `read_lane_state` through a stubbed `read_policy_value`. Observed by AC9.
- **S10** — M10. Section 14 of the run-gates canary suite gains one arm that runs the pass-leg
  adapter through the runner's freshness preflight, built against S6. Observed by AC10.
- **S11** — M11. The scratch-guard suite runs the lane with no policy kit beside the hook, and the
  canary suite runs the adapter on a refused key read. The two unknown-value arms are stated as
  unreachable defence in each suite's WHAT THIS DOES NOT CHECK. Observed by AC11.
- **S12** — M12. `.githooks/pre-commit` runs the red-fix join's staged form on a commit that stages
  no memory path, and the two reference hook blocks say the same. Observed by AC12.
- **S13** — M13. The unit harness spells the pass-leg command with the commit the builder started
  from, and `tools/workflows/unattended-build.template.js` hands out the command with no base.
  Observed by AC13.
- **S14** — L1. `checkLane` of `tools/hooks/scratch-guard.js` reads the ledger and applies the role
  tests first, and reads the policy key only when a red is open and the writer is admissible.
  Observed by AC14.
- **S15** — L2. The pass-leg section of `tools/run-gates/README.md` documents `scope_of`. Observed
  by AC15.
- **S16** — L3. The main loop re-measures, by each row's own tool, the budget row of the three
  suites the review names and of every suite whose floor this unit raises. No hand types a reading.
  Observed by AC16.
- **S17** — L4. The switch section of `help/red-fix-lane.md` states what still runs with the key
  off. Observed by AC17.
- **S18** — The five bug classes the review mints join the catalogue under `memory/gotchas`, one
  record each, and the catalogue index is rendered again by `gotchas.py --write`. Observed by AC18.

## 3. Non-goals (OUT)

- H1 of the review record, which is unit 14 of this build, with its class
  `carried-forward-row-read-as-current`.
- The two refuted findings, ids 3 and 25, and the two builder questions the review did not judge.
- A second fallback for gotchas check 18. S7 moves the commit grader's read alone.
- A runner field naming a filtered manifest, M2's other branch. The run id's prefix decides.
- An adopter step that seeds `LEG_MANIFEST` or pins the manifest to `eol=lf`.
- A row in `memory/project/fork-ceilings.txt` for the hook (§4, "Alternatives rejected").
- A leg of their own for the two pass-and-lane cases. S16 reports the reading; a split is a new
  unit if the row cannot hold.
- Suppressing the `graded 0` line of the limits pass, which spec 10's AC6 requires.
- Any kit version, which the lander's `mint` moves, and any edit to a CLOSED spec of this build.

### Edges

- **consumes-from** external — the code of this build's CLOSED units 1 to 13: the pass-leg rule,
  adapter and run point, the lane, its record, its limits, the help pages and the acceptance cases
  this unit corrects. Each correction is stated here and no closed spec is edited.
- **consumes-from** external — the head-bounded open-red reader that unit 14 of this build leaves
  in the scratch guard, with the ledger fixture helper of its suite. S11 and S14 build on the hook
  as that unit leaves it, and order 14 precedes this unit.
- **consumes-from** external — the held tier's leg shim, the `--leg` mode of `run-held-wsl.sh`,
  landed by TOOL-aSparedSpawn-5. S6 calls it.
- **hands-off** external — the budget readings of S16 and the RED then GREEN observation of every
  arm in §7, which are the main loop's at the close.

## 4. Design

### Evidence

Read at `d5b59614`, the branch tip, where units 1 to 13 are built. Unit 14 builds before this unit
and moves lines of the scratch guard, so that file is cited by symbol.

- **M1.** `tools/workflows/unattended-unit.js@cc51bcb4f638:229` declares `sha` a bare string, and
  line 373 of that blob concatenates it into `nextAction`. `cfg.passLegs` is shape-tested at line
  155.
- **M2.** `read_red_counts` counts every `p=gates`, `ev=once` line and never reads `run`.
  `tools/run-gates/pass-legs.sh@b43c2a9aeada:329` builds the run id as `pass-` and a stamp.
- **M3.** `read_manifest` replaces CRLF with LF. `cmd_apply` and `cmd_check` then compare the
  render, encoded, with `resolve_manifest_path().read_bytes()`.
- **M4.** `tools/run-gates/run-gates.sh@970e3e89a3e9:5381` sets `lst=retried` whenever
  `<i>.retry.sec` exists. The retry's exit is in `$WORK/<i>.retry.rc`, read at line 4682 of that
  blob, and the retry row's second field is its status, read at line 2577.
- **M5.** The three guard rows are as the review prints them. `tools/policy/` is carried by one
  guard today and `tools/run-gates/` by seven, by `check-spec-tokens.py --legs-for` on 2026-11-12.
- **M6.** `tools/run-gates/kit.toml@ba6fffbdd4bc:161` is `check = ["python", "{kit}/pass_legs.py",
  "--check"]`. `tools/run-gates/regen.py#run_command` passes the environment through and resolves
  an `argv` headed `bash`, and `check_operand` asks only that the script after it is in the tree.
- **M7.** `routed_commits.py` reads `LEG_MANIFEST` from the conf once and names a blank value in
  the violation. `tools/memory-tree/.memory-tree.conf.example@3efd8c1034ca:274` ships it blank.
  `tools/memory-tree/backlog.py#resolve_kit_dir` is already imported by `read_guarded_paths`.
  `tools/policy/check_policy.py@743b1e144707:4667` appends the key by hand, and it writes the
  adopter's manifest as the sibling of the run-gates kit directory, where the fallback looks.
- **M9.** `read_policy_value` is imported by name into `routed_commits`, so a stub of that module
  global reaches the real `read_lane_state`.
- **M12.** `.githooks/pre-commit@45cc7740dda0:228` runs hygiene `--staged` only where a memory
  path is staged. `tools/memory-tree/build_records.py@b854dda5daec:639` already stages
  `staged, unrecorded at HEAD` against the join itself, so the join is held and the hook's filter
  is not. The hook file is gov's own; an adopter copies the block at
  `WIRE-INTO-PROJECT.md@350d2517e2b2:278` or `tools/memory-tree/README.md@270d1a34e7c5:125`.
- **M13.** `tools/workflows/unattended-build.template.js@a13ede7739a8:607` spells
  `--base HEAD~1`. The unit harness runs no command of its own, and its attended branch has no
  run-state file, so no recorded tip exists on disk in that mode.
- **L1.** `checkLane` resolves the policy helper and reads the key before `readOpenReds` and
  `loadRoleIndex`.
- **L1's named leg.** `tools/gate-lint/fork-count.sh@e97c34c2a418:11` counts distinct `BASHPID`
  values of a bash trace. The hook is a node process.

### The fixes

**S1.** One test, `/^[0-9a-f]{7,64}$/`, on the returned `sha`. Passing, the sentence is unchanged.
Failing, it reads that the pass commit is HEAD when the command runs. The return's own `sha` field
and the log line keep the raw value, as they did before unit 7.

**S13.** The parent's `PASS_LEGS` constant ends at `pass-legs.sh`, and its comment loses the claim
of one commit per pass. `tools/workflows/unattended-build.js` is rendered again by
`check-protocol-parity.test.sh --render`, never edited. In the child, `UNIT_SCHEMA` gains an
optional string `base`, and the builder's prompt gains one sentence in both modes, with or without
`passLegs`: read `git rev-parse HEAD` before the first write and return it as `base`. `nextAction`
then spells `<passLegs> --base <base>` when `base` passes S1's shape test and neither it nor `sha`
is a prefix of the other. Otherwise it spells `<passLegs> --base <rev>` and says the builder
returned no usable base, so `<rev>` is the commit HEAD named before the dispatch. No return path
spells a relative rev.

**S2.** A module constant holds the prefix `pass-`, with a comment naming the adapter line that
writes it. A skipped line adds to neither `bars`, `red_bars`, `reds` nor the window's two stamps.

**S3.** Both verbs compare strings. `cmd_apply` writes the render with CRLF restored when the bytes
it read held CRLF. The message of `--check` stays for a real difference.

**S4.** Where `<i>.retry.sec` exists the seconds and end stamp are the retry's, as today. The
status is `retried` when `<i>.retry.rc` reads 0. Otherwise it is the second field of
`<i>.retry.leg`, and `fail` where that row does not read. The comment above the clause and the
README's paragraph on the `retried` status say the same. A red row still carries no key.

**S5.** Three guard edits and nothing else of the three rows. `python tools/run-gates/pass_legs.py
--apply` runs after the edit only if `--check` asks for it.

**S6.** The row becomes:

```toml
argv = ["bash", "{kit}/run-held-wsl.sh", "--leg", "python", "{kit}/pass_legs.py", "--apply"]
check = ["bash", "{kit}/run-held-wsl.sh", "--leg", "python", "{kit}/pass_legs.py", "--check"]
```

The shim unsets `GATE_LEGS` and maps the python launcher. The comment above the row states which
file the check grades. `tools/run-gates/README.md` says the same where it describes the row.

**S7.** A new function `resolve_leg_manifest(repo, conf)` in `routed_commits.py` returns the conf's
value when it is non-blank. Otherwise it returns `gate-legs.json` beside the run-gates kit that
`resolve_kit_dir("run-gates", "run-gates.sh", KIT)` finds, as a posix path relative to `repo`, and the
empty string where no kit resolves or the path leaves the repository. The violation for the empty
string still opens `LEG_MANIFEST is blank`. The conf example's comment names the grader's use and
the fallback. The help page's section "What the commit owes" names the key and the fallback.

**S8.** Arms, in a scratch kit and a scratch repository: a planted `runlog/gates.log` and
`gate-ledger.tsv`, then `--write` under `GOV_NODE=f` asserting the evidence rows and the
`scope_of` credit; `--report` asserting one row per verdict and the order; `--check` green, then
red after a typed field and after a missing one; `--write` with no run log exiting 1 on
`DEAD PROBE`; `--write` with `GOV_NODE` unset exiting 2.

**S9.** Three arms stub the module global `read_policy_value`, by the `globals()` spelling the arms
beside them use: one raises `ValueError('policy:
refused …')`, one returns `'maybe'`, one raises `LookupError`. The first two assert RANGE lists the
fix commit as `names no unit` with the reader's line. The third asserts `1 red-fix` with the NOTE
line. A fourth arm holds S7: a blank key in a fixture with a run-gates kit beside it admits the
commit.

**S10.** The arm copies `regen.py` and `kit.toml` into the fixture kit, plants a red row and a
cost row for `alpha` and `beta`, and runs the adapter with `GATE_REGEN_CHECK` unset. It asserts
exit 0 with no `NOT checked` line. A `pass_leg` then typed on `gamma` must make the preflight
refuse. The policy cases keep `GATE_REGEN_CHECK=0`, whose planted row is typed by design.

**S11.** The scratch-guard arm copies the hook, `agent-cap.js` and what they require into a
scratch directory with no policy sibling, runs the L-AC2 `on` row there, and asserts exit 0 with
the NOTE text in the witness. The adapter arm runs it once with `GOV_DEFAULT_BRANCH` naming no
branch and asserts exit 0, the reader's line on stderr, no marker and an unchanged run record. No
arm plants an unknown value through `policy.toml`, because the reader refuses one first.

**S12.** The hygiene block of the hook gains an else branch. With no memory path staged it runs
`build_records.py join red-fix --staged` from the resolved memory-tree kit, through the python
resolver the hook already sources for its policy guard, and a non-zero exit fails the commit. A
kit or launcher that does not resolve prints the hook's announced skip. The two reference blocks
gain the same branch. `help/red-fix-lane.md` says the refusal is the hook's and that a hook
without the branch leaves the finding to the next full hygiene run.

**S14.** `checkLane` computes the git directory, the reds and the role index first. With no red
open, a broken index, or a writer steps 4 to 6 of `checkRedLane` would not admit, it returns the
composed verdict unread. Only then does it read the key. One behaviour moves: a refused key read
with no red open appends no line. The step-10 comment and the docstring of `checkRedLane` state
the new order. Spec 8's wording of the old order stands corrected by this paragraph.

**S15.** One paragraph: what the key names, the Refusal for an unknown parent, and that a scoped
leg's evidence row holds its own reds plus its parent's.

**S16.** At the close the main loop times each leg alone by its own `argv` on node `a`, rewrites
the row from that reading at the file's stated margin, and runs `derive-ceilings.py --write`.

**S17.** The switch section says the limits pass and the join grade history whatever the key
reads, and that each prints one line on every run.

**S18.** One record each, in the shape of `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`:

| Class | Anchored on | Gated by |
|---|---|---|
| `agent-output-interpolated-into-an-instruction` | `tools/workflows/unattended-unit.js` | S1's and S13's arms |
| `inherited-env-retargets-a-check` | `tools/run-gates/kit.toml`, `tools/run-gates/regen.py` | S10's arm |
| `fixed-base-assumes-one-commit-per-pass` | `tools/workflows/unattended-build.template.js` | S13's arm |
| `budget-row-not-remeasured-after-added-arms` | `tools/run-gates/selftest-budgets.txt` | checklist only |
| `off-switch-leaves-new-output-standing` | `help/red-fix-lane.md` | checklist only |

The six existing classes the review cites take no new record; their left-shift is the arm of the
item that cites them.

### What it does not check

- A `base` the builder returns well-shaped and wrong. A commit older than the pass widens the
  scope, which is safe. The builder's own first commit narrows it, as the fixed rev did.
- The prefix `pass-` is spelled in the adapter and in the module. Nothing compares the two.
- A runner other than the adapter that hands the bar runner a filtered list under another run id.
- An adopter hook copied before this unit. It runs no join on a product-only commit.
- Whether a guard names every file its suite reads. S5 closes the three gaps traced.
- The unknown-value arms of the hook and the adapter, which no fixture reaches.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `resolve_leg_manifest` | `tools/memory-tree/routed_commits.py` | `py.function`; `lexicon.py --suggest` answered OK on 2026-11-12 |
| the return field `base` | `UNIT_SCHEMA` of the unit harness | no cell grades a schema key; the spelling of `sha` beside it |
| the module constant for `pass-` | `tools/run-gates/pass_legs.py` | the builder asks `lexicon.py --suggest` before naming it |
| five class slugs | `memory/gotchas` | the slugs the review record prints |

### Migration

Additive. An adopter whose conf leaves `LEG_MANIFEST` blank gains the fallback. A ledger row that
read `retried` over a failed retry reads its real status from the next run. The contract between
the two harnesses moves in one kit, and they release together.

### Rollout

No new switch. Each fix sits behind the key its mechanism already asks.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/run-gates/pass_legs.py`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/kit.toml`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/selftest-budgets.txt`
- `tools/gate-legs.json`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/README.md`
- `tools/policy/check_policy.py`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `WIRE-INTO-PROJECT.md`
- `help/red-fix-lane.md`
- `memory/gotchas/`

### Alternatives rejected

- **M13, the main loop supplies the tip it recorded.** The review allows it. The attended mode
  records no tip on disk, and the review's arm needs a base the harness itself spells. The class
  S18 mints for M1 admits an agent field behind a shape test, and S13 falls back to this option's
  sentence when the test fails.
- **M2, a runner field.** It adds a field to the run log for one reader.
- **M6, a second name for the filtered list.** It is a runner knob, which owes the push boundary a
  class, as unit 13 found.
- **M7, an adopter that seeds the key.** It writes an adopter's conf for a value the kit can
  derive.
- **M12, the documentation branch.** It leaves the unrecorded fix to the close's bar.
- **M12, a hygiene-suite arm**, as the review words it. The join's staged refusal is already
  staged there; the unguarded line is the hook's, so the arm is the hook suite's.
- **L1, a fork-ceiling row for the hook.** The counter traces bash and the hook is node.
  UNVERIFIED: whether a bash child of node writes to the trace. The scratch-guard arm of S14 fails
  on the order itself and reads no clock.
- **L4, no line where no fix is graded.** It contradicts spec 10's AC6.

## 5. Production-readiness checklist

- security — S1 and S13 shape-test every agent field that reaches `nextAction`. S14 admits no
  write the old order refused. S7 reads a manifest only inside the graded repository.
- perf / scale — S14 takes the key read off every refusal with no red open. S12 adds one python
  start to a commit staging no memory path. S6 adds one shell start to the preflight.
- error / empty / loading states — no kit resolves in S7 and the violation stands; no base in S13
  and the sentence names none; no launcher in S12 and the hook announces the skip.
- observability — the ledger shows a failed retry's status; `nextAction` shows the base it used.
- risks — S4 moves a status other tools read. The drift report sums `retried` from run records,
  never the ledger, and reuse accepts neither status. S13 moves a contract two scripts share.
- testing — AC1 to AC3, AC5 to AC7, AC9, AC12, AC13, AC15, AC17 and AC18 are probes a pass runs.
  The rest are the main loop's, and so is every arm of §7.
- migration — additive; see §4, "Migration".
- user docs — `help/red-fix-lane.md` by S7, S12 and S17; the two kit READMEs by S4, S6, S12, S15.

## 6. Acceptance criteria

`<s>` is the run's scratch directory.

- **AC1** — When `grep -c "0-9a-f\]{7,64}" tools/workflows/unattended-unit.js` runs, it prints 1
  or more.
  Red when: the raw `sha` is still concatenated. At base it prints 0.
- **AC2** — When `python -c "import sys,pathlib; sys.path.insert(0,'tools/run-gates'); import pass_legs as p; f=pathlib.Path(sys.argv[1]); f.write_text('p=gates\tev=once\trun=b1\tstarted=s1\tfail.1=a\np=gates\tev=once\trun=pass-1\tstarted=s2\tfail.1=a\n',encoding='utf-8'); r=p.read_red_counts(f,{'a'}); print(r['bars'],r['reds']['a'],r['last'])" <s>/gates.log`
  runs, it prints `1 1 s1`.
  Red when: a pass-leg line is counted as a bar. At base it prints `2 2 s2`.
- **AC3** — When a CRLF copy of `tools/gate-legs.json` is written to `<s>/crlf.json` and
  `python tools/run-gates/pass_legs.py --check` runs with `GATE_LEGS` naming it, it exits 0; after
  `--apply` under the same variable the copy's bytes are unchanged.
  Red when: either verb compares with raw bytes. At base `--check` exits 1.
- **AC4** — When the runner runs over a fixture whose one leg passes its ceiling and fails its
  retry, `cut -f1,3` over that fixture's `gate-ledger.tsv` prints the leg with `fail` or `timeout`.
  Red when: the row reads `retried`.
  permission: the main loop's; the fixture starts the bar runner, which a role agent's hook
  refuses.
- **AC5** — When `python tools/check-spec-tokens.py --legs-for tools/policy/catalogue.toml` runs it
  lists `scratch-guard self-test`; over `tools/policy/guarded-paths.txt` it lists
  `routed-commits selftest`; over `tools/run-gates/held_halves.py` it lists `policy fixtures`.
  Red when: a guard still misses its sibling kit. At base none of the three is listed.
- **AC6** — When `grep -c '"--leg", "python", "{kit}/pass_legs.py"' tools/run-gates/kit.toml`
  runs, it prints 2.
  Red when: either half of the row still starts python bare. At base it prints 0.
  figure: 2 is PINNED on 2026-11-12, the row's `argv` line and its `check` line.
- **AC7** — When `python -c "import sys; sys.path.insert(0,'tools/memory-tree'); import routed_commits as r; print(r.resolve_leg_manifest('.',{}), r.resolve_leg_manifest('.',{'LEG_MANIFEST':'named'}))"`
  runs, it prints `tools/gate-legs.json named`; `grep -c 'LEG_MANIFEST=' tools/policy/check_policy.py`
  prints 0; and `grep -c 'LEG_MANIFEST' help/red-fix-lane.md` prints 1 or more.
  Red when: a blank key still reds every lane commit, the case still types the key, or the page
  is silent. At base the first raises, the second prints 1 and the third prints 0.
- **AC8** — When `python <s>/kit/run-gates/pass_legs.py --check` runs over a scratch copy of the
  module, its two evidence files and a two-row manifest the rule selects one row of, it exits 0;
  with a `pass_leg` field typed on the other row it exits 1 naming that row.
  Red when: the arm's fixture cannot make `--check` fail.
  permission: the arms themselves are the main loop's to observe, per §7.
- **AC9** — When `grep -c 'globals()\["read_policy_value"\] = ' tools/memory-tree/routed_commits.py`
  runs, it prints 3 or more.
  Red when: an arm stubs `read_lane_state` and never reaches the real function. At base it
  prints 0.
  permission: the self-test that runs the arms is a leg's own, so their verdict is the main
  loop's.
- **AC10** — When the canary suite's section 14 runs, its preflight arm prints `ok` twice: for a
  pass-leg run that exits 0 with no `NOT checked` line, and for the refusal after a typed
  `pass_leg`.
  Red when: `regen.py` is absent from the fixture kit, so the preflight never runs.
  permission: the main loop's; the arm is a suite's.
- **AC11** — When the scratch-guard suite and the canary suite run, the no-policy-kit row prints
  `ok` on exit 0 with the NOTE text, and the refused-read row of `pass-legs.sh` prints `ok` on exit
  0 with no marker.
  Red when: either arm runs with the policy kit resolved, so the branch it names is not reached.
  permission: the main loop's; both arms are suites'.
- **AC12** — When `grep -c 'join red-fix --staged' .githooks/pre-commit WIRE-INTO-PROJECT.md tools/memory-tree/README.md`
  runs, each of the three lines ends in 1 or more.
  Red when: the hook or a reference block still runs the join only beside a staged memory path.
  At base each prints 0.
- **AC13** — When `grep -c 'base HEAD~1' tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-unit.js`
  runs, each line ends in 0, and `grep -c "base: { type: 'string' }" tools/workflows/unattended-unit.js`
  prints 1.
  Red when: the template keeps the relative rev, or the render was not regenerated. At base the
  first two print 1.
- **AC14** — When `node tools/hooks/scratch-guard.js` reads an unrouted product write on stdin, in
  a worktree whose ledger holds no open red and with `GOV_DEFAULT_BRANCH` naming no branch, its
  refusal holds no line opening `policy: refused`.
  Red when: the key is still read before the ledger, so the reader's line is appended.
  permission: the main loop's, through the suite arm of §7; the payload is the one the suite's
  `run_write` helper builds.
- **AC15** — When `grep -c 'scope_of' tools/run-gates/README.md` runs, it prints 1 or more.
  Red when: the paragraph is absent. At base it prints 0.
- **AC16** — When `git log -1 --format=%H -- tools/run-gates/selftest-budgets.txt` runs after the
  close, it names a commit made at the close, and the rows of `policy fixtures`,
  `routed-commits selftest` and `scratch-guard self-test` each name that day's reading.
  Red when: a row still names its reading from before this build.
  permission: the main loop's; each reading is a whole run of a held suite.
  figure: every reading is DERIVED, written from the tool's own output.
- **AC17** — When `grep -c 'red-fix limits' help/red-fix-lane.md` runs, it prints 1 or more.
  Red when: the switch section still describes the write gate and the pushed range alone. At
  base it prints 0.
- **AC18** — When `ls memory/gotchas` is filtered by
  `grep -c -E 'agent-output-interpolated|inherited-env-retargets|fixed-base-assumes|budget-row-not-remeasured|off-switch-leaves'`
  it prints 5, and `python tools/memory-tree/gotchas.py --for-paths tools/workflows/unattended-unit.js`
  lists `agent-output-interpolated-into-an-instruction`.
  Red when: a class is missing, or a record names no path and is never selected.
  figure: 5 is PINNED on 2026-11-12, the classes the review record marks new, less unit 14's.

## 7. Gates

`unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `policy fixtures` · `run-gates canary` · `run-gates evidence` · `run-gates gov canary` · `measure-legs selftest` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `routed-commits selftest` · `branch-guard self-test` · `recall floor` · `recall floor arms` · `gotchas selftest` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `docs` · `help page commands` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `testsuite counts (every bar self-test prints one)` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `python reads (a name never bound, an import outside its guard)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `writing practice (records and units)`

The brief's close is the full bar once, with the full-bar switch set, without the self-tests and
without the unattended kit gate leg. Most arms below sit in the held tier, so the main loop
observes each RED and then GREEN by itself. The kit epoch leg expects the lander's `mint`.

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · a builder return whose sha holds a space and a backtick, asserting that text is absent from `nextAction`; staged with the shape test taken out of a copy of the harness · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/workflows/unattended-build.test.sh · covers AC13 · a builder return whose base is a third sha, asserting the command names it and no relative rev, and a return with no base asserting the fallback sentence; staged with the fixed rev restored in a copy · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC2 AC3 AC8 · a run-log line with a pass-leg run id and a fail field, a CRLF manifest, and S8's arms; each staged in the fixture's own copy of the module with the fix taken out · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/run-gates/run-gates.test.sh · covers AC4 · a ceiling that fires and a retry that fails, asserting the ledger status; staged with the status clause restored in the fixture's copy of the runner · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/run-gates/run-gates.test.sh · covers AC6 AC10 AC11 · section 14 with `regen.py` and `kit.toml` in the fixture kit, the typed-field refusal, and the adapter's refused key read; staged with the shim taken out of the fixture's descriptor · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/hooks/scratch-guard.test.sh · covers AC11 AC14 · the hook copied with no policy sibling, and a refused key read with no red open; the second staged with the old order restored in a copy of the hook · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/memory-tree/routed_commits.py · covers AC7 AC9 · the self-test's three reader arms and the blank-key arm beside a run-gates kit; staged by stubbing `read_lane_state` in place of the reader · none

New arm: tools/policy/check_policy.py · covers AC7 · the adopter case on an untouched default conf; staged with the fallback taken out of the installed grader · none

New arm: .githooks/pre-commit.test.sh · covers AC12 · a product-only commit on top of an unrecorded fix, refused; staged with the else branch taken out of a copy of the hook · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · S7 gains the write gate's half: `TOOL-aNimbleMend-14`, built after rev-1, closes the lane on a blank `LEG_MANIFEST`, so the adopter case of S7 and AC7 cannot drop the key until the hook reads a blank key as the grader does.

## 10. Reuse audit

Every fix extends the seam its `Where` line names in the review record, in place. Three reach a
second seam. S6 calls the held tier's leg shim, the `--leg` mode of
`tools/run-gates/run-held-wsl.sh`, which unit 13 already put each pass leg behind. S7 calls
`tools/memory-tree/backlog.py#resolve_kit_dir`: `python tools/codebase-map/reuse_lookup.py "resolve
the leg manifest beside the run-gates kit when the conf key is blank"` ranked it a seam, and
`read_guarded_paths` beside the new function already imports it. S12 calls the join verb of
`tools/memory-tree/build_records.py` that check 31 delegates to. For S13, no existing seam fits a
base the harness can read by itself: the unit harness runs no command, and the evidence is its
attended branch, which has no run-state file. `gotchas.py --for-paths` over the estimate selected
`held-suite-guard-misses-a-sibling-kit` and `a-runner-knob-owes-a-push-class`; the first prefers
exact files to a sibling's directory where a shared guard would tip past the broad floor, and S5
names the two directories because both stay under or already over that floor.

Where the review and the source disagreed: M12 asks for a hygiene-suite arm, and the join's staged
refusal is already staged in `build_records.py`; L1 names the spawn budget leg, whose counter
traces bash. §4, "Alternatives rejected", holds both.

Recall terms used: `python tools/memory-recall/query.py "a review's medium and low findings
batched into one repair unit over the pass legs and the red-fix lane" --terms "pass leg red-fix
lane ledger retried guard sibling kit LEG_MANIFEST preflight GATE_LEGS shim nextAction budget row"`
