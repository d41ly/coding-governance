# TOOL-dDeclaredLoop-81 — a clean re-merge that fails is its own state and never takes the parent exemption; only a probed absence of the feature does

**Status:** DEFERRED · rev-5 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 20 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-81-deviation-811.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-81-deviation-811.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-81-deviation-812.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-81-deviation-812.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-81-deviation-813.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-81-deviation-813.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-81-red-fix-27.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-81-red-fix-27.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-81-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-81-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-81-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-81-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-82 |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md`)
confirmed finding **id 28 at HIGH**, its item **H2**, alone in that item. `TOOL-dDeclaredLoop-78` S1 makes
the clean re-merge C `uncomputable` on any `merge-tree --write-tree` exit other than 0, and only
`uncomputable` takes `TOOL-dDeclaredLoop-69` S2's parents branch, whose grade exempts a key equal to any
parent's and never reads a merge the combined list does not name. That puts git's fatal exit 128 in the
same bucket as an octopus merge or a git without the feature. Exit 128 covers unrelated histories,
missing objects and a broken object store.

A run branch built from an orphan commit keeps the old policy bytes and is merged into main with
`--allow-unrelated-histories`. The re-merge exits 128, M's policy blob equals the orphan parent's, the
parents branch never reads the merge, and the old policy keys reach main with no `Gov-Policy:` trailer.
The guard fails open on a failed dependency. The landed code already does so:
`tools/loop/guard.py#read_remerge_policy` answers a parents-only reason for every exit but 0, and
`tools/loop/guard.py#check_push_range` skips a merge its combined list does not name before the re-merge
runs.

This unit gives a failed re-merge its own state, graded against every parent without the exemption, and
detects the missing feature by a probe instead of an exit code. It repairs `TOOL-dDeclaredLoop-78`.

## 2. Scope (IN)

- **S1** — `resolve_write_tree_support()` in `tools/loop/guard.py` answers whether this git carries
  `merge-tree --write-tree`. It runs `git merge-tree -h` once per process, under the environment
  `read_clean_env` gives, and passes its standard output and standard error joined to
  `check_write_tree_usage(text)`, which is true when the text names `--write-tree`. The answer is
  memoised. A probe that cannot start raises `OSError`, which the push arm already reports as
  `cannot judge`, exit 2. No exit code of a real re-merge is ever read as the feature's absence.
  Observed by AC4, AC5.
- **S2** — `read_remerge_policy` names two states beside 78's `present` and `absent`. `uncomputable` is
  now exactly an octopus merge or S1 answering false, and the re-merge is then never run; S1's answer
  reads as the reason `this git has no merge-tree --write-tree`. An exit 1 is `conflicted`, keeping 59's
  reason `its re-merge conflicts, merge-tree exit 1` and 69 S2's parents branch, which
  `TOOL-dDeclaredLoop-75` S27 widens. Every other outcome is `failed`: an exit 0 printing no tree id,
  exit 128, a usage exit 129 from a git S1 found capable, a negative exit for a signal, or an `OSError`
  at start. Its detail is the exit code followed by the first non-blank line of git's standard error
  where there is one, `0 no tree id` for the first case, and `start failed: <the error's text>` for the
  last. The parents-only reason `merge-tree --write-tree exited <n>` leaves the answer, since no exit
  now reaches the parents branch through it. Observed by AC1, AC3, AC4.
  **Readers:**
  by name: `tools/loop/guard.py`, the parents-only reasons of its re-merge reader and the merge sentences of its module docstring; `help/policy.md`, the merge sentence of its push-check paragraph
  by value: `.githooks/pre-push`, the policy push arm block, which turns the arm's exit into the `policy-unrecorded` refusal
- **S3** — A `failed` C never takes 69 S2's parents branch. The push arm prints
  `loop-guard: push · <sha8> graded against every parent — the clean re-merge failed: <detail>`, then
  grades M against each parent in parent order: each leaf whose value at M differs from its value at
  some parent is owed, an absent key reading as its own value as 59 §4 states, and its trailer's old
  value is the first such parent's. A merge whose values equal every parent's owes nothing. M or a
  parent that does not parse is 78 S3's finding naming the side. Each owed leaf owes the
  `Gov-Policy:` trailer and the change record 69 owes, and each missing one is the arm's own finding
  naming the merge and the key, so a declared trailer and record clear a legitimate unrelated-history
  merge (§8 F2). Observed by AC1, AC2, AC3.
- **S4** — The re-merge runs through one function, `run_merge_tree(p1, p2)`, answering
  `(rc, stdout, stderr)` from `git merge-tree --write-tree` under `read_clean_env`'s environment and
  letting `OSError` propagate to `read_remerge_policy`, which reads it as S2's start failure.
  `read_remerge_policy` is its one caller. A plant grades in-process with `run_merge_tree`, or S1, swapped
  for a stand-in for that grade alone, counting the re-merge calls, and prints `merge-tree runs: <n>`.
  Observed by AC3, AC4.
- **S5** — Three plants join `PLANTS` in `tools/loop/guard.py`, their scenarios a branch of
  `run_guard_plant`, and `push-merge-unrelated-histories` and `push-merge-tree-fatal` each owe exit 1 by
  an entry of `run_selftest`'s owed map. §4 The plants gives each history. Observed by AC1, AC2, AC3,
  AC4.
- **S6** — The push arm's paragraph and the WHAT THIS DOES NOT CHECK paragraph of the module docstring of
  `tools/loop/guard.py`, and the merge sentence of the push-check paragraph of `help/policy.md`, say that
  a merge whose clean re-merge fails is graded against every parent and owes a trailer and a record for
  each key that differs from one, and that only an octopus merge, a conflicting re-merge or a git
  without `merge-tree --write-tree` is graded against its parents alone. The sentence saying any other
  exit of `merge-tree` is graded against the parents leaves both. NOT OBSERVED by a criterion: prose,
  held by the `docs` leg and read at the closing review.
  **Readers:**
  by name: `tools/loop/guard.py`, the push arm and WHAT THIS DOES NOT CHECK paragraphs of its module docstring; `help/policy.md`, the merge sentence of its push-check paragraph
  by value: NO VALUE READERS: the sentences are prose that no tool compares, counts or derives from

## 3. Non-goals (OUT)

- Which re-merges exit 1 with the policy path outside the conflicts, and how C reads there:
  `TOOL-dDeclaredLoop-75` S27, unchanged in this unit, as its hands-off bullet to 75 records; the
  restatement of S27's body as present, absent or refused is id 4, `TOOL-dDeclaredLoop-82`.
- Retrying the re-merge with `--allow-unrelated-histories`: rejected in §4, measured.
- A parent blob that does not parse: 78 S3's finding, unchanged, which S3 reuses; its parent-side
  plant is id 29, `TOOL-dDeclaredLoop-82`.
- A probe whose output names no usage at all, which S1 reads as false: `TOOL-dDeclaredLoop-85` gives the
  probe its third answer, `probe failed`, routed to `failed`.
- A bug-class checklist entry that a guard mapping a subprocess's failure codes refuses each by name and
  lets only a probed absence take an exemption, the finding's left-shift: the class is recorded at the
  close; S5's plants are this grade's fatal-exit fixtures.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-78` — the three states of C that `read_remerge_policy` names in `tools/loop/guard.py`, whose `uncomputable` this unit narrows to an octopus merge or a probed absence of the feature
- **hands-off** `TOOL-dDeclaredLoop-75` — the exit table, in which S27's exit 1 stays the one non-zero exit graded on C or on the parents and every other exit is the failed state, refused untrailered, never a fall to the parents
- **hands-off** `TOOL-dDeclaredLoop-82` — the exit table, beside which that unit restates S27's exit-1 body as present, absent or refused (id 4)
- **hands-off** `TOOL-dDeclaredLoop-83` — S2's exit table, which that unit writes into 75 S27 in place of its fallback to the parents (the round-6 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-84` — S2's exit table, which that unit writes into 78's states and grade and into 82 S4 and AC4 (the round-6 spec audit's id 7)
- **hands-off** `TOOL-dDeclaredLoop-85` — `resolve_write_tree_support`, `check_write_tree_usage` and S4's plant hook, which that unit gives a third answer, `probe failed`, routed to the `failed` state, and restates in S1, S2, S5, §4, AC4 and AC5 (the round-6 spec audit's id 24)
- **hands-off** `TOOL-dDeclaredLoop-86` — S3's state names and parent-side parse refusal, the `failed` refusal text for a start failure, a signal and an empty stderr, and §4 Evidence's quotation of 75 S27, which that unit amends (the round-6 spec audit's ids 3, 18, 29)
- **hands-off** `TOOL-dDeclaredLoop-88` — S1's probe signature and rule, S3's state names, §4's grade and AC5, which that unit restates to the three-answer probe (the round-7 spec audit's ids 3, 6, 9, 12, 19, 21)
- **hands-off** `TOOL-dDeclaredLoop-90` — the edge to 78 that counts C's states, which that unit restates to five, and S3's `conflicted` token, which its criterion reads (the round-8 spec audit's ids 7, 26)

## 4. Design

### Evidence

Every code claim below was read on `branch/unattended-declared-loop-d56bf0` at `89baa328c` through
`git show` and `git archive`; this worktree is cut from main, which lacks the loop kit.

- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, in a scratch repository under `%TEMP%`: PINNED,
  that date. With `p.toml` at `k = 1` on `main` and an orphan `run` holding `k = 2`,
  `git merge-tree --write-tree main run` printed `fatal: refusing to merge unrelated histories` and
  exited 128. The same call with `--allow-unrelated-histories` exited 1, printing
  `CONFLICT (add/add): Merge conflict in p.toml`: the policy path is conflicted, which is 69 S2's
  parents branch and its exemption.
- Probed 2026-11-15 on node `d`, git 2.54.0.windows.1, in this worktree: PINNED, that date.
  `git merge-tree -h` exited 129, wrote nothing to standard error, and printed on standard output
  `usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>` and then
  `or: git merge-tree [--trivial-merge] <base-tree> <branch1> <branch2>`. A git before the feature prints
  only the trivial form, `usage: git merge-tree <base-tree> <branch1> <branch2>`: UNVERIFIED here, from
  git's documentation, so AC5 passes that text rather than running an old git.
- `tools/loop/guard.py#read_remerge_policy`, built by `TOOL-dDeclaredLoop-59`, answers an octopus
  reason for other than two parents, runs `merge-tree --write-tree` through
  `tools/loop/loop_witness.py#read_git`, which answers the exit and standard output and discards standard
  error, answers `its re-merge conflicts, merge-tree exit 1` for exit 1, and
  `merge-tree --write-tree exited <n>` for any other non-zero exit or an empty output. It is the one
  `merge-tree` call in the module.
- `tools/loop/guard.py#check_push_range` reads a merge only where `git diff-tree --cc` lists the policy
  file, so a merge whose blob equals one parent's is skipped before the re-merge runs; it prints
  `<sha8> graded against its parents only — <reason>` for a reason, and owes the leaves on which M
  differs from every parent and from a computable C. It catches `OSError` as `cannot judge`, exit 2,
  which the policy push arm block of `.githooks/pre-push` refuses as it refuses exit 1.
- `tools/loop/guard.py#read_policy_blob` already runs git through `subprocess.run` under
  `tools/loop/loop_witness.py#read_clean_env`, the form `run_merge_tree` takes to keep standard error.
- `tools/policy/guard.py#derive_leaf_changes` answers each differing leaf as `(old, new)`, None for
  absent, so a union over the parents in order, keeping each leaf's first answer, gives S3's owed set and
  old values.
- Every push plant of `tools/loop/guard.py#run_guard_plant` grades `--push-range` in a subprocess, so a
  stand-in set in the fixture's process never reaches that grade. The plant `write-guarded-rollback`
  already runs in-process, spying with `unittest.mock.patch.object` and writing its own output, and the plant
  `floor-off-run` already reads one output against two needles by appending a second row.
  `tools/loop/guard.py#run_fixture` prints `all held` when every row held and exits as the last row did,
  else 3, and `tools/loop/guard.py#run_selftest` owes each plant its owed-map exit, 0 by default,
  through `tools/loop/loop_lib.py#run_selftest_cases`, which calls `main` in this process.
- `tools/branch-reconcile/branch_reconcile.py#check_noop` probes the same capability once, by merging
  the default ref with itself, and its comment records why: a per-tip failure is also what unrelated
  histories produce, "and that is no statement about git".
- `TOOL-dDeclaredLoop-69` rev-3, unbuilt at that tip, makes a computable C the whole reference past 44's
  pre-filter and keeps 59's grade, behind the combined list, for every other merge (69 S1, S2, §4 The
  grade). `TOOL-dDeclaredLoop-78` rev-6, unbuilt, names C's states in `read_remerge_policy`'s answer,
  with `uncomputable` on any exit but 0, and adds the side-naming does-not-parse finding (78 S1, S3).
  This spec is written on those committed texts.

### The grade, restated

```
supported = resolve_write_tree_support()       # once per process, lazily: git merge-tree -h names --write-tree
for merge M in the range, with parents P1..Pn:
    blob(P1) is none -> 44's printed line, not graded                         # 44, unchanged
    state, C = read_remerge_policy(P1..Pn)
        uncomputable   n != 2, or not supported; run_merge_tree never called   # this unit (S2)
        present        run_merge_tree exits 0, its tree holds the file         # 78 S1
        absent         run_merge_tree exits 0, its tree lacks the file; C = {} # 78 S1
        conflicted     run_merge_tree exits 1                                   # 59's reason, 75 S27 widens
        failed         anything else, with its detail                           # this unit (S2)
    present | absent:          69 S1 and 78 S3, unchanged
    uncomputable | conflicted: 69 S2, unchanged: read only where the combined list names the file,
                               59's line naming the reason, owed = the leaves equal to no parent's value
    failed:                                                                     # this unit (S3)
        print "<sha8> graded against every parent — the clean re-merge failed: <detail>"
        M or a parent that does not parse -> 78 S3's finding naming the side
        owed = for P1..Pn in order, derive_leaf_changes(Pi, M), each leaf's first answer kept
    each owed leaf: the trailer render_policy_trailer(k, its old, val(M,k)) and a record naming
        derive_row_tag(k) among read_added_units(M, listed); each missing one is a finding
```

The summary line's `changing` count takes a `failed` merge where its owed set is non-empty or a side
does not parse, as 69 counts the C branch.

### The plants

Each plant builds on the base `write_guard_plant` commits. Every non-merge commit in a range carries its
trailer and its change record. Each history's merge commit is graded from main's tip before the merge,
or from main's tip where `run` merges, so the range holds the merge and `run`'s own commits.

| Plant | History | Graded | Owed |
|---|---|---|---|
| `push-merge-unrelated-histories` | `run` is cut from the base with `git checkout --orphan` and committed, a root commit whose policy file sets no `review` table; `main` sets `review.max-rounds = 4`; `main` merges `run` with `--allow-unrelated-histories --no-commit`, which conflicts add/add on the policy file and exits 1 as `push-merge-conflict-pick` expects of its merge, takes `run`'s policy file, and commits, first with the trailer `policy.review.max-rounds 4 -> none` and a record naming `policy.review.max-rounds`, then, reset, with neither | `--push-range` in a subprocess, as the other push plants | the first scenario exit 0 naming `0 finding(s)` and `the clean re-merge failed: 128`; the second exit 1 naming `the clean re-merge failed: 128` and `merge <sha8> · .governance/policy.toml · review.max-rounds` |
| `push-merge-tree-fatal` | `run`, cut from the base, commits a file outside the policy file; `main` sets `review.max-rounds = 4`; `run` merges `main` with `--no-commit`, takes back its own policy file, and commits with no trailer or record | in-process, `run_merge_tree` answering `(128, "", "fatal: fx stand-in\n")` | exit 1 naming `the clean re-merge failed: 128 fatal: fx stand-in`, `merge <sha8> · .governance/policy.toml · review.max-rounds` and `merge-tree runs: 1` |
| `push-merge-no-write-tree` | the history of `push-merge-both-sides-clean`, built by the same branch of `run_guard_plant` | in-process, `resolve_write_tree_support` answering false and the real `run_merge_tree` counted | exit 0 naming `graded against its parents only — this git has no merge-tree --write-tree` and `merge-tree runs: 0` |

In the first two the merge's policy blob equals one parent's and differs from the other's, so the
combined list never names it and 69 S2's parents branch would skip it. In the third the merge's blob
differs from both parents', so the parents branch reads it, prints its line and owes nothing, each key
equalling one parent's value.

The in-process grade is a nested function of `run_guard_plant`, as the spy of `write-guarded-rollback`
is. Under `contextlib.chdir` into the scratch repository and `contextlib.redirect_stdout`, it swaps the
named attributes of `sys.modules[__name__]` with `unittest.mock.patch.object`, wraps `run_merge_tree`, the
stand-in or the real one, in a counter, calls `check_push_range(base, "HEAD")`, appends
`merge-tree runs: <n>` to what it printed, and writes the whole to standard output. Each needle a plant
reads from one grade is its own row over the same output, as `floor-off-run` does. The swap ends with
the grade, and S1's memo never holds a stand-in's answer, since the stand-in is a different attribute.

### Inventory

- The top-level functions `resolve_write_tree_support`, `check_write_tree_usage` and `run_merge_tree`.
- The `PLANTS` keys `push-merge-unrelated-histories`, `push-merge-tree-fatal` and
  `push-merge-no-write-tree`, and the owed-map entries of the first two.
- The reason `this git has no merge-tree --write-tree`, the line
  `<sha8> graded against every parent — the clean re-merge failed: <detail>`, and the plant line
  `merge-tree runs: <n>`.

### Files touched (estimate)

- `tools/loop/guard.py`
- `help/policy.md`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The self-merge probe of `tools/branch-reconcile/branch_reconcile.py#check_noop`.** It needs a
  readable commit, so a broken object store fails the probe, reads as absence, and hands the merge back
  to the exemption: the fail-open this unit closes. The usage text needs no object. The function is also
  another kit's, which the loop kit does not require.
- **Re-running the re-merge with `--allow-unrelated-histories`.** Measured above: the policy file
  conflicts add/add, which reaches the parents branch and its exemption again.
- **Refusing a failed re-merge whatever the trailer says.** No trailer could clear a legitimate
  unrelated-history merge; S3 owes the keys that differ and lets a declared trailer pass (§8 F2).
- **An environment variable that makes the guard's own process answer a stand-in.** It would let any
  pusher set the probe to false and send every merge to the parents branch: a switch the guard cannot
  tell from an attack. The in-process swap lives only in the fixture's own process.
- **The first parent's value as every owed leaf's old value.** Where M equals the first parent, the
  owed line would run from a value to itself and record no change, the defect 69 §8 F2 rejects on its
  branch.

## 5. Production-readiness checklist

- security — closes a path on which an old policy reaches the default branch untrailered through a
  fatal git error; a re-merge that cannot start or dies by a signal refuses by name as well. A git
  without `merge-tree --write-tree` still sends every two-parent merge to the parents branch and its
  exemption, as an octopus merge is sent; the module docstring says so (S6).
- perf / scale — one `git merge-tree -h` per process, run only when a two-parent merge reaches the
  re-merge; the re-merges are 69's, unchanged in number.
- error / empty / loading states — every re-merge outcome has a named state; a failed one prints its
  detail, and an empty standard error leaves the exit code alone.
- observability — the `failed` line names the merge, the exit code and git's first standard error line,
  and each finding names the merge and the key; a plant prints the re-merge count.
- risks — an unrelated-history merge, or one whose re-merge fails on a broken store, that changes policy
  keys now owes a trailer and a record for each key differing from a parent, including keys the other
  side already carried; that is the defect closed, and the author declares them.
- testing — AC1 to AC4 as fixture plants and AC5 as a probe; the arm under §7, observed at the close.
- migration — none: the `failed` state is unbuilt at that tip.
- user docs — `help/policy.md`, the push-check paragraph's merge sentence, by S6.

### Dependencies on units built beside this one

- `TOOL-dDeclaredLoop-59` is built: `read_remerge_policy`, its parents-only line and reasons, and the
  plant `push-merge-both-sides-clean`, whose history the third plant reuses, sit at that tip.
- `TOOL-dDeclaredLoop-69` (order 18), next, writes the C branch, the parents branch behind the combined
  list and the C-sided trailer value. This spec is written on its rev-3 and builds after it lands.
- `TOOL-dDeclaredLoop-78` (order 19), next, names C's three states in `read_remerge_policy`'s answer and
  writes the side-naming parse finding S3 reuses. This spec is written on its rev-6 and builds after it
  lands.
- `TOOL-dDeclaredLoop-75`, `TOOL-dDeclaredLoop-82` to `TOOL-dDeclaredLoop-86`, `TOOL-dDeclaredLoop-88`
  and `TOOL-dDeclaredLoop-90` build after and restate this unit's names, as §3's edges record.
- `TOOL-dDeclaredLoop-7`, `TOOL-dDeclaredLoop-14`, `TOOL-dDeclaredLoop-45` and `TOOL-dDeclaredLoop-4`
  are being built or are next; this unit reads none of the code they change.

### What the change could newly red

| Artifact | Why | What keeps it green |
|---|---|---|
| `loop guard fixtures`, `guard.py --selftest` | `run_selftest` owes each plant its exit and `all held`, in one process | the two plants owed 1 join the owed map; the in-process swap ends with each grade, so no later plant sees a stand-in |
| `push-merge-both-sides-clean`, `push-merge-resolution-edit`, `push-merge-carries-trailered`, 69's and 78's plants | their merges call the probe and the re-merge | the probe answers true on any git carrying the feature, and their re-merges exit 0 or 1, so each state and verdict holds |
| `push-merge-conflict-pick` | its re-merge exits 1 | `conflicted` keeps 59's reason and the parents branch |
| `push-merge-octopus` | none: an octopus never probes | `uncomputable` keeps the octopus reason |
| `push-no-trailer`, `push-new-branch` plants | none: their ranges hold no merge | a non-merge is graded as before |
| `tools/run-gates/selftest-budgets.txt`, the `loop guard fixtures` row | the new plants lengthen the leg | the row is re-priced from a timed run of the leg alone, by the row's own rule |
| `memory/map/generated/symbols.json` | it lists the module's top-level functions | regenerated with `gen_map.py --write` for the three functions, held by `codebase-map coverage + freshness` |
| `tools/policy/check_policy.py`, its read of `help/policy.md` | it reads the page for the install-day deferral line | the edit touches only the push-check paragraph |
| `.githooks/pre-push.test.sh`, its policy push arms | they run a stand-in `guard.py` | untouched: the hook's logic does not move |

The govkit registry row for `loop guard fixtures`, its subject pin in `tools/govkit/subject-pins.tsv` and
its row in `tools/gate-legs.json` name the leg and the module, which do not move. A tree grep for
`loop/guard.py` and the leg on that branch found no usage row, verdict-epoch delegate or kickoff watch
entry naming either. The new code spells no install prefix.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/guard.py --fixture --plant push-merge-unrelated-histories` grades the
  orphan merge with no trailer or record, that scenario exits 1 naming `the clean re-merge failed: 128`
  and `merge <sha8> · .governance/policy.toml · review.max-rounds`, and the plant prints `all held` and
  exits 1.
  Red when: exit 128 reads as `uncomputable`, the parents branch skips the merge its combined list does
  not name, the scenario exits 0 and the plant exits 3.
- **AC2** — When the same plant's first scenario grades the merge carrying
  `Gov-Policy: policy.review.max-rounds 4 -> none` and a record naming `policy.review.max-rounds`, it
  exits 0 naming `0 finding(s)` and printing `the clean re-merge failed: 128`.
  Red when: a failed re-merge refuses whatever the trailer names, wedging a declared merge.
- **AC3** — When `python tools/loop/guard.py --fixture --plant push-merge-tree-fatal` runs, it exits 1
  printing `the clean re-merge failed: 128 fatal: fx stand-in`,
  `merge <sha8> · .governance/policy.toml · review.max-rounds`, `merge-tree runs: 1` and `all held`.
  Red when: the merge is skipped because M's policy blob equals a parent's, so the plant exits 3.
- **AC4** — When `python tools/loop/guard.py --fixture --plant push-merge-no-write-tree` runs, it exits 0
  printing `graded against its parents only — this git has no merge-tree --write-tree`,
  `merge-tree runs: 0` and `all held`.
  Red when: the plant still runs a re-merge where S1 answers false, so the count reads 1 and the C branch
  grades the merge without the parents-only line.
- **AC5** — When a `python -c` probe in `tools/loop/` imports `guard` and calls `check_write_tree_usage`
  on git 2.54's usage line `usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>`, it
  answers True, on `usage: git merge-tree <base-tree> <branch1> <branch2>` it answers False, and
  `resolve_write_tree_support()` answers True on this node.
  Red when: the predicate matches `merge-tree` alone, so the trivial-form usage answers True.
  fixture: the third answer needs a git carrying the feature on the node; node `d` runs git 2.54.0.windows.1, PINNED 2026-11-15.

## 7. Gates

`loop guard fixtures` · `policy fixtures` · `docs` · `measure-legs selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop guard fixtures` leg (`TOOL-dDeclaredLoop-2`) green, which runs
every plant of the guard's self-test.

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 · the three plants beside 69's and 78's; AC1 and AC3 staged red by routing `failed` back to `uncomputable`, as TOOL-dDeclaredLoop-78 builds it; AC2 staged red by refusing every `failed` merge whatever its trailer; AC4 staged red by calling the re-merge whatever S1 answers · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Refuse a failed re-merge outright, or grade it without the exemption?** (a) refuse by name
  whatever the trailer says; (b) owe each key that differs from some parent and refuse only untrailered
  keys. Both meet the skeptic's plant, an untrailered orphan merge exiting 1 printing
  `the clean re-merge failed`; (a) leaves a legitimate unrelated-history merge no way through, a
  follow-up (b) does not leave. RESOLVED (agent, 2026-10-24, delegated): (b), S3.
  widens: none · relaxes: none
- **F3 — How does a `failed` merge read in the arm's output?** rev-4 wrote the refusal
  `policy: <merge8> — the clean re-merge failed: <rc> <stderr first line>`, naming the keys, before the
  push arm was built.
  - (a) One informational line, `<sha8> graded against every parent — the clean re-merge failed:
    <detail>`, printed as 59's parents-only line is, and the arm's own per-key findings for the owed
    trailers and records: one finding form across every branch, as 78 §8 F2 keeps for its parse finding.
  - (b) A finding of its own carrying the detail and the keys, beside or in place of the per-key
    findings: a second form for the same miss, and a merge whose trailers are declared would need a
    rule to suppress it.
  Recommendation: (a). The body is written on it, and every downstream grep, `the clean re-merge
  failed: 128` and `the clean re-merge failed: start failed:`, reads the line it prints.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: one informational line plus the arm's per-key findings, so every branch uses one finding form
  widens: none · relaxes: none
- **F4 — Two plants for the unrelated-history merge, or one with two scenarios?** rev-4 named
  `push-merge-unrelated-histories` and `push-merge-unrelated-histories-trailered`.
  - (a) One plant whose first scenario carries the trailer and record and whose second, after a reset,
    carries neither, as `push-merge-resolution-edit` runs its two: one scratch history, and no sibling
    spec names the second plant.
  - (b) Two plants, each building the same orphan history in its own scratch repository.
  Recommendation: (a). The body is written on it, and AC2 reads the first scenario.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: one plant with a trailered and a bare scenario, since no sibling names a second plant
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-5 spec audit's id 28 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-83 and TOOL-dDeclaredLoop-84 and TOOL-dDeclaredLoop-85 and TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-5 · 2026-11-15 · §1 · S1 S2 S3 S4 S5 S6 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 · §7 · §8 · §10 ·
  re-grounded on branch/unattended-declared-loop-d56bf0 at `89baa328c` by the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-81-1-spec-writer; mechanism, carries, order and status kept.
  Written on TOOL-dDeclaredLoop-69 rev-3 and TOOL-dDeclaredLoop-78 rev-6 over the built
  `read_remerge_policy`: S2 names `conflicted` and `failed` beside 78's states and takes the catch-all
  parents-only reason out of the answer; S3 grades `failed` against every parent with the first
  differing parent's value as the old one, in the arm's finding form (F3); S4 keeps standard error,
  names no repository argument and grades in-process, since the push plants grade in a
  subprocess a stand-in never reaches; S5 folds the trailered plant into a scenario (F4) and gives
  `push-merge-no-write-tree` a history the parents branch reads; S6 brings the docstring and help
  sentence; §5 names the dependencies and what could red; §7 gains the legs the touched paths owe.

## 10. Reuse audit

The seams are 59's `tools/loop/guard.py#read_remerge_policy` and its single `merge-tree --write-tree`
call, which `run_merge_tree` becomes; 69's and 78's branches in `tools/loop/guard.py#check_push_range`,
which gain one state; the arm's finding form and 78's parse finding; `tools/policy/guard.py#derive_leaf_changes`,
taken over each parent; and the plant loop of `tools/loop/guard.py#run_guard_plant` with the in-process
swap `write-guarded-rollback` already uses. This unit mints no second caller of `merge-tree`.
`python tools/codebase-map/reuse_lookup.py "probe whether this git supports merge-tree --write-tree before grading a merge"`,
run on this worktree's main tree, which lacks the loop kit, ranked `tree`, `git`, `write`, `probe`,
`run_git` (`tools/branch-reconcile/branch_reconcile.py` among others) and `read_git_output`
(`tools/memory-tree/tree_lib.py`); none reads git's usage text. A grep for `merge-tree` on that branch
found `tools/branch-reconcile/branch_reconcile.py#check_noop`, the one existing capability probe, weighed
and rejected above for its fail-open on a broken store, so no existing seam fits the probe; and
`tools/loop/loop_witness.py#read_git` discards standard error, so `run_merge_tree` takes the
`subprocess.run` form `tools/loop/guard.py#read_policy_blob` already uses.

Recall terms used: merge-tree write-tree exit 128 fatal unrelated histories refuse fail-open exemption guard policy probe usage
