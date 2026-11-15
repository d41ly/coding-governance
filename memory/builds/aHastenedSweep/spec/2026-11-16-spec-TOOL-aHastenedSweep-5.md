# TOOL-aHastenedSweep-5 — the memory-tree kit contract names every `gotchas.py` verb the hygiene shell launches

**Status:** SPECCED · rev-1 · 2026-11-16 · node a · Tier-2 · base f25308f0 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md](../prompts/2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md) | research | TOOL-aHastenedSweep-6 |

<!-- /gen:spec-records -->

## 1. Goal

The hygiene shell launches `gotchas.py --check-with-ids` on every unscoped run and
`gotchas.py --check` under `--only`. The `memory-tree/gotchas` contract in
`tools/memory-tree/kit.toml` names neither verb, so a target that owns an older `gotchas.py` gets a
wrong red on checks 13 to 19, and `govkit check` and `govkit update` never say why. This unit adds
one contract clause per verb, with the shell as consumer, so the parity report names the clause the
owned copy is missing. It closes H1 of the closing review's round 1,
`reviews/2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md`.

## 2. Scope (IN)

- **S1** — The `memory-tree/gotchas` contract gains a clause
  `imports = ["cmd_check_with_ids", "main"]` whose `consumer` is `check-memory-hygiene.sh`. It stands
  for the unscoped run's `--check-with-ids` launch. Observed by AC1, AC2 and AC4.
- **S2** — The same contract gains a clause `imports = ["cmd_check", "main"]` whose `consumer` is
  `check-memory-hygiene.sh`. It stands for the scoped run's `--check` launch. Observed by AC2, AC3
  and AC4.
- **S3** — One comment block above the two clauses. It names this unit and H1, says each clause
  stands for one launch of the shell, and says what an `imports` clause does not measure: the verb's
  dispatch in `main` and the frame shape. Observed by AC4.
- **S4** — The existing `--for-paths` probe clause stays byte for byte, and no other file under
  `tools/` changes. The shell keeps the loud red of its frame-failure fallback, and no two-launch
  fallback is added. Observed by AC5 and AC6.
- **S5** — On the live tree, the whole hygiene output and its exit code are `cmp`-equal at this
  unit's parent and at this unit. Observed by AC7.

## 3. Non-goals (OUT)

- No edit to `check-memory-hygiene.sh` or `gotchas.py`. The shell's fallback on a frame that does
  not split stays the loud red it is, and no silent second launch is added on a usage exit.
- No `probe` clause for either verb (§4, Alternatives rejected).
- No clause for `gotchas.py --declares`, `--for-diff`, `--write` or `--report`. The hygiene shell
  launches none of them (§4, Evidence).
- No new govkit selftest arm and no change to `tools/govkit/govkit.py`. The grader and its arm exist.
- None of the review's left-shift gates. The `private-verb-call-without-a-kit-contract-clause` leg,
  which would collect every launch a kit's shells make and demand a clause for each, is filed as an
  ask by the main loop at the close.
- No kit version move on the branch: the lander mints it.
- Nothing under `memory/builds/dDeclaredLoop/`, that run's worktree, its branch or its run-state file.
- No self-test suite and no bar inside the pass, a sliced suite included.

### Edges

- **consumes-from** external — the `--check-with-ids` verb, its `cmd_check_with_ids` function and
  the shell's one-process launch, all landed by the CLOSED order-3 unit of this build. The S1 clause
  names that function, and without it the clause would fail on gov's own copy.
- **hands-off** external — the live-tree A/B of AC7, the `govkit selfcheck` observation of AC4 when
  the role hook refuses it in the pass, the legs §7 lists and the filing of the left-shift ask. All
  are the main loop's at the close, recorded in this unit's acceptance ledger under a `Pass: none`
  commit.

## 4. Design

### Evidence

Read at `13863b03` on 2026-11-16.

- The shell launches `gotchas.py` at exactly two sites, and no other shell under `tools/` launches it
  with a verb (`grep -n 'gotchas\.py' tools/memory-tree/check-memory-hygiene.sh`). The unscoped
  launch is `--check-with-ids` (`tools/memory-tree/check-memory-hygiene.sh@71e199ce1cc2:3226`), and
  the scoped one is `--check` (`tools/memory-tree/check-memory-hygiene.sh@71e199ce1cc2:3257`). The
  frame-failure fallback is at `:3234`.
- The `memory-tree/gotchas` contract opens at `tools/memory-tree/kit.toml@692d09175768:442` and holds
  one clause, the `--for-paths` probe with consumer
  `kickoff-manifest:SKILL.md unattended:SKILL.template.md`, at `:445-448`.
- `gotchas.py#main` dispatches `--check-with-ids` to `gotchas.py#cmd_check_with_ids` and `--check` to
  `gotchas.py#cmd_check`. All three are top-level `def`s at the tip.
- At the build's base, `gotchas.py` binds `cmd_check` (`tools/memory-tree/gotchas.py@0cb445ff98ba:574`)
  and `main` (`:1443`) and no `cmd_check_with_ids`. Its usage line (`:1498`) lists no
  `--check-with-ids`, which is the review's measured exit 2.
- `govkit.py#measure_contract_parity` grades an `imports` clause statically: it parses the owned file
  and collects the names bound at top level, `if` and `try` bodies included, and reports
  `imports <missing names>`. It runs a `probe` clause in the target with a 60 s timeout (PINNED, the
  function's constant at `37f075e4e93e`), on the stated premise that every declared probe is a print
  mode.
- `govkit.py#derive_parity_lines` is what `check` and `update` both print. For a failing clause it
  prints `FAILS <why> — needed by <consumer>`. It reds the run only when the consumer is installed as
  a receipt `engine` row on a leg the receipt emitted.
- `govkit.py#selfcheck` refuses a clause whose `consumer` is not a tracked gov file, or that carries
  neither or both of `probe` and `imports` (`tools/govkit/govkit.py@37f075e4e93e:2185-2218`). Its
  note line is `contract <id> (<entry>:<source>): <n> clause(s)`.
- The contract's original design left `gotchas.py --check` out because it "has no stdout signature on
  a clean tree" (`memory/builds/aRepatriatedFork/spec/2026-09-23-spec-DEPL-aRepatriatedFork-13.md`,
  section 4, "The contract list gov holds stable"). `gotchas.py#cmd_check` prints nothing at exit 0
  on a tree with no record. That rules out a non-vacuous probe for `--check`, and an `imports` clause
  is the form left.
- The govkit selftest's `aRF-13 AC6` arm already observes a failing `imports` clause printed as
  `FAILS imports <name> — needed by <consumer>` (`tools/govkit/selftest.py@866a0710fd4c:1357-1360`).
- No page under `help/` and no line of `tools/memory-tree/README.md` names a contract clause
  (`grep -rln 'adopter-owned\|clauses hold' help/` prints nothing).

### The clauses

Appended to the `memory-tree/gotchas` contract, after the `--for-paths` clause:

```toml
# TOOL-aHastenedSweep-5 (closing review round 1, H1). One clause per launch the hygiene shell makes of
# this program: `--check-with-ids` on an unscoped run, `--check` under `--only`. An owned copy that
# predates the one-process verb lacks `cmd_check_with_ids` and is named here, where the shell would
# otherwise red checks 13 to 19 with a usage line. `imports` measures the names, never that `main`
# dispatches the verb to them or the `\x1d<rc>` frame the shell splits.
[[contract.clause]]
imports = ["cmd_check_with_ids", "main"]
consumer = "check-memory-hygiene.sh"
[[contract.clause]]
imports = ["cmd_check", "main"]
consumer = "check-memory-hygiene.sh"
```

The consumer word resolves against the memory-tree entry's home, the same way the five
`gen_build_index.py` clauses' consumer does.

### What it does not check

- A copy that binds `cmd_check_with_ids` while its `main` never dispatches `--check-with-ids` holds
  the S1 clause and still reds checks 13 to 19. The grader measures surface, not behaviour, as its
  docstring says.
- A copy whose frame differs from `<stderr><stdout>\x1d<rc>\n` holds the clause too. The
  `gotchas.py --selftest` with-ids arm guards gov's own frame, and the shell's fallback reds a frame
  that does not split.
- A target whose owned copy fails S1 now has `govkit check` exit 1 whenever the installed hygiene
  shell sits on an emitted leg. That is the intended move: the leg is already red there, and the
  report now names the cause.

### Inventory

N/A — the unit mints no identifier. The two clauses name functions that exist at the tip.

### Files touched (estimate)

- `tools/memory-tree/kit.toml`
- `memory/builds/aHastenedSweep/build/2026-11-16-build-TOOL-aHastenedSweep-5-1-acceptance-ledger.md`

### Rollout

One pass at order 4. The spec lands in a records commit before the code. The pass edits
`kit.toml`, runs AC1 to AC6, writes the acceptance ledger, and flips the status to CLOSED as its last
change.

### Alternatives rejected

- **A `probe` clause for `--check-with-ids` whose `expect` is the two-frame shape.** It measures the
  dispatch and the frame, which `imports` cannot. But it runs both checks over the target's whole
  corpus on every `check` and `update`, against the 60 s timeout (PINNED, above) the grader states
  for print modes. A
  slow target then fails the clause on a correct copy, and with the shell on an emitted leg that is
  a wrong red: the defect class H1 closes. The live-tree walk alone took 22.80 s on node a (PINNED
  2026-11-15 in the order-3 unit's spec, section 4, Evidence).
- **A `probe` clause for `--check`.** It has no stdout signature on a clean tree (§4, Evidence), so
  every `expect` either matches nothing on a correct copy or matches a copy that crashed.
- **One clause naming both functions.** A failure line would then not say which launch breaks, and
  the brief asks for one clause per verb.
- **An end-to-end `govkit check` over an adopted fixture target.** It needs a target adopted with the
  memory-tree kit and an `[[own]]` row. `check` and `update` reach the clause only through
  `govkit.py#measure_contract_parity`, which AC1 to AC3 call directly, and the govkit selftest
  already guards the printed line.
- **A two-launch fallback in the shell on a usage exit.** It would cure the instance and leave the
  contract silent. The review judged it instance-only.

## 5. Production-readiness checklist

- security — No new write path, surface or grant. An `imports` clause parses the owned file and
  imports nothing of the adopter's.
- perf / scale — Two static clauses add one AST parse of the owned file per `check` or `update`, and
  only on a target that owns `gotchas.py`. The parse is shared across clauses.
- error / empty / loading states — An owned file that is missing or does not parse fails every
  clause, as today.
- observability — A target owning an older copy now sees `FAILS imports cmd_check_with_ids` with the
  hygiene shell as consumer.
- risks — A target owning an older copy turns `govkit check` red where the hygiene shell is wired on
  an emitted leg. The leg is red there already, and this names the cause.
- testing — The pass runs AC1 to AC6 by hand over fixtures under `%TEMP%/hs5f`. AC7 and the §7 legs
  run at the close.
- migration — N/A — no data, conf key or adopter step changes. An adopter that owns `gotchas.py`
  reads the new clause on its next `update`.
- user docs — N/A — no page under `help/` names a contract clause (§4, Evidence).

## 6. Acceptance criteria

`$SCRATCH` is the run's scratch directory and `$WT` the worktree root. `t5-parity.py` is a probe
script in `$SCRATCH`. It puts `$WT/tools/govkit` on `sys.path`, loads `govkit.py` by path, reads the
`memory-tree/gotchas` contract from `$WT/tools/memory-tree/kit.toml` with `tomllib`, and calls
`measure_contract_parity(<dir>, <contract>, <own path>)`. With `--consumer <word>` it keeps only the
clauses whose `consumer` is that word. It prints `<held>/<n> clauses hold`, then one `FAILS <why>`
line per failing clause.

The fixtures sit under `%TEMP%/hs5f`, a short path. `old/gotchas.py` is
`git show f25308f0:tools/memory-tree/gotchas.py`. `new/gotchas.py` is the tip's copy. `nock/gotchas.py`
is the tip's copy with `def cmd_check(` renamed to `def cmd_check_gone(`.

- **AC1** — When `python "$SCRATCH/t5-parity.py" --consumer check-memory-hygiene.sh %TEMP%/hs5f/old gotchas.py`
  runs, it prints `1/2 clauses hold` and exactly one `FAILS imports cmd_check_with_ids` line.
  Red when: the S1 clause is absent, so it prints `1/1 clauses hold`, or it names a function the
  base copy also binds.
  fixture: built by the pass from the base blob; no tree holds one today.
- **AC2** — When the AC1 command runs over `%TEMP%/hs5f/new`, it prints `2/2 clauses hold` and no
  `FAILS` line. Over `%TEMP%/hs5f/nock` it prints `1/2 clauses hold` and exactly one
  `FAILS imports cmd_check` line.
  Red when: a clause names an attribute the shipped copy does not bind, or the S2 clause is absent.
- **AC3** — When `python "$SCRATCH/t5-parity.py" "$WT" tools/memory-tree/gotchas.py` runs with no
  filter, it prints `3/3 clauses hold`. The `--for-paths` probe clause runs in gov's own tree here.
  Red when: an added clause fails gov's own copy, or the edit breaks the existing probe clause.
- **AC4** — When `python -c` reads `tools/memory-tree/kit.toml` with `tomllib` and prints each clause
  of `memory-tree/gotchas` as its kind, its list and its consumer, it prints the `--for-paths` probe
  line, then `imports cmd_check_with_ids,main check-memory-hygiene.sh`, then
  `imports cmd_check,main check-memory-hygiene.sh`. `grep -c 'TOOL-aHastenedSweep-5' tools/memory-tree/kit.toml`
  prints 1. `python tools/govkit/govkit.py selfcheck` prints
  `contract memory-tree/gotchas (memory-tree:gotchas.py): 3 clause(s)` and no failure naming
  `memory-tree/gotchas`.
  Red when: a consumer word names no tracked gov file, or a clause carries both `imports` and
  `probe`.
  permission: `govkit selfcheck` is a gate leg; where the role hook refuses it in the pass, the main
  loop observes it with §7's legs at the close.
- **AC5** — When `git diff --name-only HEAD~1..HEAD -- tools/` runs on the pass commit, it prints
  only `tools/memory-tree/kit.toml`. `git diff HEAD~1..HEAD -- tools/memory-tree/kit.toml` shows only
  added lines, all below the `--for-paths` clause.
  Red when: the pass edits the shell, `gotchas.py` or the existing clause.
- **AC6** — When
  `grep -cF '[ "$_onepy" = 1 ] || { ids=$_both; _idsrc=1; got=""; _gotrc=1; _onepy=1; }' tools/memory-tree/check-memory-hygiene.sh`
  runs, it prints 1.
  Red when: a pass adds a silent two-launch fallback in place of the loud red.
- **AC7** — When the whole `check-memory-hygiene.sh` runs from the worktree root on the live tree,
  once from this unit's parent's `tools/` extracted with `git archive` under `%TEMP%/hs5a` and once
  from the unit's own, `cmp` of the two outputs exits 0 and the exit codes match.
  Red when: any byte of any check's output moves.
  cost: two full hygiene runs, each about 805–1093 s on node a (PINNED, 2026-11-15 bar ledgers).
  permission: the main loop's at the close, under a `Pass: none` commit; a unit pass does not run it.
  fixture: the live tree at the close's tip.

## 7. Gates

`govkit selfcheck` · `policy fixtures` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms`

No `New arm:` line: the unit adds data to a contract the existing grader reads, and the govkit
selftest's `aRF-13 AC6` arm already observes a failing `imports` clause. A pass checks its own change
with AC1 to AC6. The close runs the bar once, and AC7 is the main loop's there.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-16 · initial draft from `prompts/2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md`,
  closing H1 of `reviews/2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md`,
  grounded at `13863b03`.

## 10. Reuse audit

The seam this unit extends is the `memory-tree/gotchas` `[[contract]]` in
`tools/memory-tree/kit.toml`, graded by `tools/govkit/govkit.py#measure_contract_parity` and printed
by `tools/govkit/govkit.py#derive_parity_lines`. The unit adds two clauses in the existing `imports`
shape and no code. `python tools/codebase-map/reuse_lookup.py "declare which program verbs an
adopter-owned engine must keep for its consumer"` ranked `adopt`, `engine` and `declares` first,
none of them this seam, and named `build_owned_row` in `govkit.py`, the row this contract is graded
against. Recall named `DEPL-aRepatriatedFork-13`, the spec that designed the contract and left
`gotchas.py --check` out for want of a stdout signature, and this build's closing review record.

Recall terms used: `python tools/memory-recall/query.py "how does govkit tell a target that owns a
kit program which verbs its consumers still call" --terms "kit.toml contract clause consumer
adopter-owned imports probe expect govkit parity gotchas"`
