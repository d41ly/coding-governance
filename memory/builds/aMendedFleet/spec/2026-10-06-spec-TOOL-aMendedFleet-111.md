# TOOL-aMendedFleet-111 — closing review round 1 minors, code: a rename-safe overlap diff, the lander's kit paths, an all-zero push base, LIVE's dirty inputs, a merge-aware pickaxe, true resume texts under the Plan default, a dead install-prefix exemption

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-06 · order 108

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1, confirmed nine minor findings whose fixes write code:
findings 3, 4, 5, 6, 7, 9, 10, 18 and 19 of
`memory/builds/aMendedFleet/reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md`. M4 promotes
a closing review's minors into one batch per disjoint write set, and this is the code batch. Each
finding is its own scope item, its own criterion and its own left-shift arm, and every one of the
nine was re-verified as still present at the worktree HEAD `e83b29b6`.

## 2. Scope (IN)

- **S1** — FINDING 3. `check_cross_run_overlap` in `tools/unattended/unattended.sh` lists this run's own
  paths with `git diff --no-renames --name-only "$anc...HEAD"`, so a file this run renamed is listed
  under its source path as well as its destination, as the `theirs` read below it already is.
  Observed by AC1.
  **Readers:** by name: `check_cross_run_overlap` is called by `print_overlaps` for `--overlaps` and
  by the preflight path for the kickoff card's `overlaps —` cell. by value: the awk JOIN in the same
  function, which reads the `ours` file line by line and matches each path against the ref's paths.
- **S2** — FINDING 4, the skeptic's corrected fix. `check_merge_losses` and `run_minter` in
  `tools/push-main.sh` test that the file they will run exists at `$top/$dir` before running it. When
  it does not, each prints its existing skip line — "no lexicon kit beside this lander" and "no govkit
  deployer beside this lander" — and returns 0, so a python exit 2 for a missing file is never graded
  as a DEAD PROBE or a refused mint. Observed by AC2.
  **Readers:** by name: `cmd_prepare` calls both, and the attended landing path calls `run_minter`.
  by value: the callers' `if ! ...` tests, which read the return code; a skip returns 0 as the other
  two skip branches already do.
- **S3** — FINDING 5. An all-zero `GATE_PUSH_BASE` reads as UNSET in both consumers, so a push that
  creates the default branch falls back to the merge-base exactly as it did before this build. In
  `tools/memory-tree/check-verdict-epoch.sh`, before the line that adopts `GATE_PUSH_BASE` as `BASE`;
  in `cmd_epoch` of `tools/govkit/govkit.py`, by testing the value with its zeros stripped. The hook's
  export is unchanged. Observed by AC3 and AC4.
  **Readers:** by name: `.githooks/pre-push` exports the value and its test asserts the exported
  bytes; these two consumers are the only readers in the tree. by value: the `BOUNDARY` flag in the
  shell gate and the `boundary` local in `cmd_epoch`, which an all-zero value set to 1 and now leaves
  0, so a move no bump dates prints `owed at the lander` instead of failing.
- **S4** — FINDING 6. When `.memory-tree.conf` sets `LIVE_LANDED_UNCLOSED` to 1, the dirty-input test
  in `write_ask_views` and in `write_run_record` of `tools/unattended/unattended.sh` counts EVERY
  unstaged tracked path as an input, because the render then reads product source through drift-audit's
  `git grep` over the working tree. The value is read with `read_conf_value` from
  `tools/unattended/lib-unattended.sh`. With the key blank or absent the inventory is unchanged.
  Observed by AC5.
  **Readers:** by name: the `gates-green` verb calls `write_ask_views`, and the post-dispatch path and
  `--close` call `write_run_record`. by value: each helper's refusal line, which names the dirty paths
  and the `stage or discard` remedy, and its early return, which keeps the stale view unstaged.
- **S5** — FINDING 7. The pickaxe in `tools/memory-tree/hygiene-parity.test.sh` that derives `FLOOR`
  passes `--no-patch --diff-merges=first-parent`, so a version value a prepared merge minted is found.
  `--no-patch` is not optional: measured on git 2.54, `--diff-merges=first-parent` alone prints the
  merge's patch, and the harness's `tail -1` then reads a diff line as the floor sha. The other reader
  of the class, the bump search in `tools/memory-tree/check-verdict-epoch.sh`, takes `--no-patch`
  too, because it currently feeds every patch line to `verat` as a candidate sha. Observed by AC6.
  **Readers:** by name: `tools/memory-tree/hygiene-parity.test.sh`, whose later lines read `FLOOR`,
  and `tools/memory-tree/check-verdict-epoch.sh`, whose bump loop hands each line to `verat`.
  by value: `FLOOR` is the revision the harness checks baselines against, and the epoch gate's
  `verat` comparison decides which candidate is the bump.
- **S6** — FINDING 9. In `tools/workflows/tier2-review.template.js`, re-rendered into
  `tools/workflows/tier2-review.js`, every deferred `note`, the synthesis-died `log` and its note
  depend on `workerType`. Under a named type each says this run wrote no result file and a re-run
  dispatches every finder and skeptic again, plus the synthesis where it died. Under `none` each keeps
  its current "dispatch only" wording. Every return carrying `pending` also carries `durable`, true
  only when `workerType` is `none`, so a programmatic caller reads the fact rather than the prose.
  The header comment on the review key and the comment above the third deferred return say the same.
  Observed by AC7.
  **Readers:** by name: `tools/workflows/unattended-build.template.js` reads `exit`, `pending` and
  `key` from this return; the Workflow caller reads `note`. by value: NO VALUE READERS, because
  `durable` is a new additive field and no program in the tree reads it yet.
- **S7** — FINDING 19, the skeptic's corrected fix. The spec-audit call to `tier2-review.js` in
  `tools/workflows/unattended-build.template.js`, re-rendered into `tools/workflows/unattended-build.js`,
  passes `workerType: 'none'`, so the audit's lens and batch files are durable and its deferred
  `next` text, which promises the re-run reuses them, is true. The relaunch line of the take-over in
  `tools/unattended/unattended.sh` and step 8 of `tools/unattended/STOPS.template.md`, re-rendered into
  `memory/guides/UNATTENDED-STOPS.md`, name the condition: the re-run reuses the files a review run
  under `workerType: 'none'` wrote, and a review under a named type, the default of a direct call,
  dispatches every judge again. A hold can name any deferred review, the closing diff review included.
  Observed by AC8.
  **Readers:** by name: the build harness's `auRaw` adapter reads the callee's return, and the
  take-over in `unattended.sh` prints the relaunch line from the `hold-run` fact. by value: the review
  key, which a `none` call computes as every run before the Plan default did.
- **S8** — FINDING 10. The remaining resume promises say when they hold. The deferral bullet at
  lines 603-604 of `tools/unattended/VERBS.template.md`, re-rendered into
  `memory/guides/UNATTENDED-VERBS.md`, says the results are on disk because the build harness runs its
  audit under `workerType: 'none'`. The deferred-platform comment in `unattended-build.template.js`
  says the same. The `tier2-review.js survives a dead fan` paragraph of
  `memory/map/features/review-harnesses.md` says a judge writes its file only under `none`. And
  `memory/gotchas/amendment-leaves-its-other-half-standing.md` gains the review's checklist line, "a
  change to a durability default re-reads every resume promise", with `tools/workflows/tier2-review.template.js`
  as a backticked anchor, so the next change to that file selects the class. Observed by AC9.
  **Readers:** by name: `tools/memory-tree/gotchas.py` derives anchors from the gotcha's backticked
  paths, and `memory/gotchas/INDEX.md` is its generated listing. by value: `--for-diff` and
  `--for-paths`, which now select the class for a diff touching the review harness template.
- **S9** — FINDING 18. The `\bgd\b` alternative leaves `NONKIT` in `tools/check-install-prefix.sh`: its
  only fixture line and only census site were deleted by `TOOL-aMendedFleet-38`, so it guards a
  spelling nobody writes, which the suite's own census comment calls the defect. The AC5 homonym
  fixture of `tools/check-install-prefix.test.sh` gains one clean line per remaining alternative that
  no line exercises today, `git`, `session` and `transcript`, the `git` one spelled through a call so
  `derive_operand`'s call-collapse is exercised again. Observed by AC10.
  **Readers:** by name: `check_homonym` and the dot-directory branch of the scan read `NONKIT`.
  by value: the clean-homonym arm of `tools/check-install-prefix.test.sh`, which reads the checker's
  exit over the fixture, and the `install-prefix (shipped surface)` leg, whose tree count §4 measured
  unchanged by the drop.

## 3. Non-goals (OUT)

- Changing the default `workerType` of `tier2-review.js`, or adding `workerType: 'none'` to the
  documented closing-review call in BUILD-METHOD M8. Either reverses `TOOL-aMendedFleet-93`'s measured
  default for every review, attended ones included; this unit makes the texts true instead.
- Exporting `GATE_PUSH_BASE` only when it is non-zero. The hook's comment and its AC9 arm state the
  all-zero value as the contract, and `.githooks/gate-env.sh` tells an adopter's bar it may read it.
- A generator-owned input pathspec list in `gen_build_index.py`, the review's "better still" for
  finding 6. It is a new CLI surface on another kit, for a gap S4 closes with the inventory the
  helpers already take.
- Dropping the `session` and `transcript` alternatives, which the same tree probe finds exempting
  nothing here. They are name heuristics an adopter's tree can need; S9 exercises them in the fixture.
- The four install-prefix hits in `skills/session-kickoff/manifest-check.test.sh` that red the checker
  at HEAD. They predate this unit and S9 neither adds nor removes one.
- The assertion floors of arms this build added before this unit, findings 12, 14, 15, 16 and 17.
  This unit raises each suite's floor by its own arms only.
- Kit version bumps: the lander mints them (`TOOL-aMendedFleet-65`).

### Edges

- **hands-off** `TOOL-aMendedFleet-112` — the floor raises for the arms this build added before this
  unit, in `tools/unattended/unattended.test.sh` and `tools/workflows/tier2-review.test.sh`, which this
  unit also writes; it is ordered after this one and recounts on top of this unit's raises.
- **hands-off** external — kit version minting, which the lander performs at the landing.

## 4. Design

### Evidence

Read at the worktree HEAD `e83b29b6`. Every finding is still present.

- Finding 3: line 2336 of `unattended.sh` runs `diff --name-only "$anc...HEAD"` with no `--no-renames`,
  while the ref read and the slug-less spec read in the same function both pass it.
- Finding 4: `check_merge_losses` runs `"$top/$dir/lexicon.py"` and `run_minter` runs
  `"$top/$dir/govkit.py"`, where `$dir` is resolved from `$self_dir` and `$top` is the cwd's toplevel.
- Finding 5: line 187 of `check-verdict-epoch.sh` adopts any non-empty `GATE_PUSH_BASE`, and lines
  12370-12371 of `govkit.py` do the same. `.githooks/pre-push` line 1450 exports `$main_remote`, all
  zeros on a branch-creating push, and already guards that value for `GATE_ATTRIBUTE` at line 1380 and
  for the merge-loss block at line 733.
- Finding 6: `write_ask_views` counts an unstaged path as an input only under the memory root, the conf
  or the generator's directory, and `write_run_record` passes the same three pathspecs. This repo's
  `.memory-tree.conf` sets `LIVE_LANDED_UNCLOSED="1"`, and `read_landed_unclosed` in
  `gen_build_index.py` then runs drift-audit's `signal_spec_status` against the working tree.
- Finding 7: line 67 of `hygiene-parity.test.sh` runs `git log --format=%H -S...` with no diff-merges
  option. Measured on git 2.54 at HEAD: adding `--diff-merges=first-parent` alone makes the same
  command print the merge's patch, so `tail -1` returned the text ` MEMORY_ROOT=memory` instead of a
  sha. With `--no-patch` added it returns a sha. `govkit.py` line 12317 already passes both options.
  A `git grep` over tracked scripts for `log` with `-S` or `-G` finds no other kit-version reader.
- Findings 9, 10 and 19: `tier2-review.template.js` line 182 defaults `workerType` to `Plan`, and the
  notes at 888, 1181, 1209 and 1516 and the log at 1467 still promise "dispatch only". The
  spec-audit call of `unattended-build.template.js` passes no `workerType`. The relaunch line in
  `unattended.sh` near line 6646, STOPS step 8, VERBS lines 603-604 and the `review-harnesses.md`
  paragraph at line 65 each promise reuse unconditionally. BUILD-METHOD M8's documented closing-review
  call passes no `workerType` either, so a hold on a deferred closing review cannot honour them.
- Finding 18: a staged copy of `check-install-prefix.sh` with each `NONKIT` alternative removed in
  turn, run over this tree, printed 4 spellings for `\bgd\b`, `session` and `transcript`, the same as
  the unchanged checker, and 6, 6 and 9 for `git`, `common` and `sdir`. PINNED, measured 2026-10-06.
  The AC5 homonym fixture holds no line any of `git`, `session` or `transcript` exempts.

### Mechanism

- S3's shell form is one `case` on the value: empty or carrying a non-zero character is kept, anything
  else is cleared. The Python form tests `os.environ.get("GATE_PUSH_BASE", "").strip("0")`.
- S4 reads the key once per helper call. Under it, `write_ask_views`'s first loop adds every listed
  unstaged path to `dirty`, and `write_run_record` drops its pathspec. Untracked files stay outside,
  because `git grep` without `--untracked` reads tracked files only.
- S6 derives one `durable` constant from `workerType` beside `judgeOpts`, and each note picks its tail
  from it. `pending` keeps its meaning, the labels that did not return; `durable` says whether the
  rest is reusable.

### Inventory

One new return field, `durable`, on every `tier2-review.js` return that carries `pending`, and one
constant of the same name beside `judgeOpts`. No new function, flag or conf key.

### Rollout

Templates are edited and their renders regenerated in the same commit:
`check-protocol-parity.test.sh --render` writes the two workflow renders, and the unattended kit's
render writes `UNATTENDED-VERBS.md` and `UNATTENDED-STOPS.md`. The gotcha edit re-renders
`memory/gotchas/INDEX.md` through `gotchas.py`. Each arm raises its suite's floor by exactly the
assertions it adds, with a RAISED line, before unit 112 recounts. The dossiers of the touched kits are
refreshed on touch.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/check-verdict-epoch.test.sh`
- `tools/memory-tree/hygiene-parity.test.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/check-install-prefix.sh`
- `tools/check-install-prefix.test.sh`
- `memory/map/features/review-harnesses.md`
- `memory/gotchas/amendment-leaves-its-other-half-standing.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **The review's finding 7 fix as written**, `--diff-merges=first-parent` alone. Rejected by the
  measurement above: it turns an empty floor into a wrong one.
- **Keeping `\bgd\b` with a synthetic fixture line**, the review's second option. The suite's census
  rule says an exemption whose spelling no tracked file writes is the defect; a synthetic line would
  keep it green while the tree holds no instance.
- **Setting `pending` to every judge label under a named type.** The skeptic batch labels are
  derived from the findings a re-run will raise, so no label set is knowable before it; `durable`
  states the fact without inventing labels.
- **Reading drift-audit's `EVIDENCE_GLOBS` in the helpers.** It needs a Python import of the drift
  project layer from bash; every tracked unstaged path is a superset that costs at most a refusal
  naming a path the render did not read, and the refusal says how to clear it.
- **A tree-wide grep of every "re-run … only" claim against the call site's `workerType`.** Which call
  site a sentence describes is a judgement no predicate makes; S8's gotcha anchor routes the class to
  the review checklist instead, and S6's and S7's arms gate the two instances that can be gated.

## 5. Production-readiness checklist

- security — S1 removes a false clean result from an advisory probe; S2 removes a false refusal at the
  lander; neither widens a write surface. S4 refuses more, never less.
- perf / scale — no new process on a hot path; S5's `--no-patch` removes one `git show` per patch line
  from the epoch gate's bump search.
- error / empty / loading states — S2 skips a missing kit the way a missing python already is; S3
  treats an all-zero base as no base; S4's refusal names the dirty paths and the remedy.
- observability — S6 and S7 make every deferral say what a re-run costs; `durable` exposes it to code.
- risks — S4 may refuse a render over an unrelated unstaged edit outside the evidence globs; the
  line names it and staging or discarding clears it.
- testing — AC1 to AC10, each on a staged break, and the arms under `New arm:` in §7.
- migration — N/A: no stored shape changes; `durable` is an additive return field.
- user docs — S7 and S8 are the doc changes; the workflows README already states the durability rule.

## 6. Acceptance criteria

- **AC1** — When, in a scratch clone where this run's commit renames one tracked shell file and an
  unmerged remote ref edits that file under its old name, `bash tools/unattended/unattended.sh
  --overlaps` runs, its `overlaps —` output names the old path as shared with that ref.
  Red when: `--no-renames` is removed from the `ours` read and the probe prints `no shared path`.
  fixture: the unattended suite's `--overlaps` block builds a remote and refs; the tree has none.
- **AC2** — When a scratch clone with `tools/lexicon/lexicon.py` and `tools/govkit/govkit.py` deleted
  runs this worktree's `tools/push-main.sh --prepare` against a prepared fixture, its output carries the
  "no lexicon kit beside this lander" and "no govkit deployer beside this lander" lines, and carries
  neither `DEAD PROBE` nor `REFUSED`.
  Red when: the file test is removed and python's exit 2 for the missing file is graded.
  fixture: case 24 of the push-main suite builds a lander fixture; the clone deletes the two files.
- **AC3** — When `GATE_PUSH_BASE=0000000000000000000000000000000000000000 bash
  tools/memory-tree/check-verdict-epoch.sh` runs at the worktree root, its exit code and verdict line
  equal those of the same command with `GATE_PUSH_BASE` unset.
  Red when: the run exits 2 naming the all-zero commit.
- **AC4** — When `GATE_PUSH_BASE=0000000000000000000000000000000000000000 python tools/govkit/govkit.py
  epoch` runs at the worktree root, its output equals that of the same command with the variable unset.
  Red when: it prints `FAILED · no base to compare against` and exits 1.
- **AC5** — When, in a scratch clone whose `.memory-tree.conf` keeps `LIVE_LANDED_UNCLOSED="1"`, an
  unstaged edit to a tracked file under `tools/` adds a citation of a non-terminal id and
  `write_ask_views` then `write_run_record` run, each prints its `not re-rendered` refusal naming that
  file, and `memory/LIVE.md` stays unstaged.
  Red when: the helper stages a `memory/LIVE.md` whose Landed-unclosed count reflects the unstaged edit.
  fixture: the unattended suite sources the driver's functions, so a scratch arm can
  call either helper directly; the tree holds no clone carrying the key today.
- **AC6** — When, in a scratch clone where a merge made with `git commit-tree` is the only commit that
  introduces a new `KIT_MEMORY_TREE_VERSION` value, the parity harness derives its floor, `FLOOR` is
  that merge's 40-hex sha. And `git grep -nE "log.* -[SG].*KIT_[A-Z_]*_VERSION"` over the tree prints
  only lines that also carry `--no-patch` and `--diff-merges=first-parent`.
  Red when: `FLOOR` is empty or not a sha, or the grep prints a line lacking either option.
- **AC7** — When a scratchpad stub runner evaluates `tools/workflows/tier2-review.js` with every lens
  agent returning null, once with `workerType` absent and once with `none`, the absent run's deferred
  `note` says the re-run dispatches every finder and skeptic again and its return carries `durable`
  false, and the `none` run's note says "dispatch only" and carries `durable` true. The same holds for
  a synthesis agent returning null.
  Red when: the absent run's note says "dispatch only", or `durable` is missing.
  cost: a stub runner in the scratchpad, as `TOOL-aMendedFleet-67`'s ledger built one.
- **AC8** — When a stub runner evaluates `tools/workflows/unattended-build.js` with a recording
  `workflow` stub and `specAudit` declared, the args the spec-audit call passes carry `workerType`
  `none`; and `grep -n "workerType" memory/guides/UNATTENDED-STOPS.md` hits step 8.
  Red when: the spec-audit args carry no `workerType`, or step 8 promises reuse with no condition.
- **AC9** — When `grep -n "workerType" memory/guides/UNATTENDED-VERBS.md memory/map/features/review-harnesses.md`
  runs, it hits the deferral bullet and the durability paragraph; and
  `python tools/memory-tree/gotchas.py --for-paths tools/workflows/tier2-review.template.js` lists
  `amendment-leaves-its-other-half-standing`.
  Red when: either document still promises reuse with no condition, or the class is not selected.
- **AC10** — When `bash tools/check-install-prefix.sh` runs at the worktree root, it reports the same
  spelling count it reports at HEAD; and when `\bgd\b` is staged back into `NONKIT`, or `session` is
  staged out of it, the new liveness arm reds naming that alternative.
  Red when: the drop raises the tree's count, or an alternative no fixture line matches passes.
  figure: DERIVED at observation time; §4 measured 4 at HEAD.

## 7. Gates

`unattended kit gate` · `push-main self-test` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `govkit selftest` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `tier2-review self-test` · `unattended-build self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `install-prefix (shipped surface)` · `install-prefix self-test` · `verifier fan-out self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · covers AC1 · this run renames a file another ref edits under its old name, staged red by removing `--no-renames` from the `ours` read · `FLOOR_SHARD_1` and `FLOOR_ASSERTIONS` move by the arm
New arm: `tools/unattended/unattended.test.sh` · covers AC5 · `LIVE_LANDED_UNCLOSED=1` with an unstaged citation edit under `tools/`, staged red by restoring the memory-root-only inventory · `FLOOR_SHARD_2` and `FLOOR_ASSERTIONS` move by the arm
New arm: `tools/push-main.test.sh` · covers AC2 · the lander run against a tree without the lexicon and govkit files, staged red by removing the file tests · its floor moves by the arm
New arm: `tools/memory-tree/check-verdict-epoch.test.sh` · covers AC3 AC6 · `ARM_GPB` set to forty zeros expects the merge-base fallback, and the tree grep for a kit-version pickaxe lacking either option, staged red by deleting the zero test and the `--no-patch` · none
New arm: `tools/govkit/selftest.py` · covers AC4 · `GATE_PUSH_BASE` set to forty zeros beside the aMF-65 S6 arms, staged red by deleting the zero strip · its floor moves by the arm
New arm: `tools/workflows/tier2-review.test.sh` · covers AC7 · the deferred note and `durable` under an absent and a `none` workerType, staged red by restoring the unconditional wording · `FLOOR_ASSERTIONS` moves by the arm
New arm: `tools/workflows/unattended-build.test.sh` · covers AC8 · the spec-audit args carry `workerType` `none`, staged red by deleting it · its floor moves by the arm
New arm: `tools/check-install-prefix.test.sh` · covers AC10 · every `NONKIT` alternative matches a homonym fixture line, staged red by re-adding `\bgd\b` · `FLOOR_ASSERTIONS` moves by the arm

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from findings 3, 4, 5, 6, 7, 9, 10, 18 and 19 of the closing
  review's round 1, each re-verified at HEAD `e83b29b6`.

## 10. Reuse audit

Every seam is already in the tree. S1 extends the `--no-renames` read the same function's `theirs`
side uses. S2 reuses the two skip lines `check_merge_losses` and `run_minter` already print. S3 copies
the hook's own all-zero guard, `${main_remote//0/}` at lines 733 and 1380 of `.githooks/pre-push`, into
its two consumers. S4 reuses `read_conf_value` in `tools/unattended/lib-unattended.sh`. S5 copies the
option pair `govkit.py` line 12317 already passes. S6 extends the `workerType` constant and
`judgeOpts` in `tier2-review.template.js`. S8 extends the existing gotcha
`memory/gotchas/amendment-leaves-its-other-half-standing.md` rather than adding a class.
`python tools/codebase-map/reuse_lookup.py "treat an all-zero push base as unset and list renamed paths
by both names in a path join"` returned only name-stem neighbours such as `read_id_list`,
`resolve_compare_base` and `derive_rename_map`, none of which reads a push base or joins two path
lists, so no other seam fits; its scan reported no unscanned layer. Recall returned
`TOOL-aMendedFleet-93`, which set the Plan default and accepted the loss of resume,
`TOOL-aMendedFleet-67`, which added `workerType`, and `TOOL-aMendedFleet-60`, which built the overlap
probe. Where the review and the tree disagree: finding 7's fix as written prints a patch line as the
floor on git 2.54, so S5 adds `--no-patch`; the epoch gate's own bump search has the same patch-line
input; and the same tree probe that found `\bgd\b` dead found `session` and `transcript` exempting
nothing here either, recorded in §3 rather than dropped.

Recall terms used: `python tools/memory-recall/query.py "what did the closing review of aMendedFleet
find about resume promises, all-zero push bases and rename-blind diffs" --terms "deferred-platform
workerType Plan durable resume GATE_PUSH_BASE all-zero --no-renames overlap pickaxe diff-merges NONKIT
homonym LIVE_LANDED_UNCLOSED"`
