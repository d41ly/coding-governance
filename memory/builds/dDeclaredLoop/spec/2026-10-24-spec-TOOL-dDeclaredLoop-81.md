# TOOL-dDeclaredLoop-81 — a clean re-merge that fails is its own state and never takes the parent exemption; only a probed absence of the feature does

**Status:** OPEN · rev-3 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 20 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-81-deviation-811.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-81-deviation-811.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-82 |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md`)
confirmed finding **id 28 at HIGH**, its item **H2**, alone in that item. `TOOL-dDeclaredLoop-78` S1 makes
the clean re-merge C `uncomputable` on any `merge-tree --write-tree` exit other than 0, and only
`uncomputable` takes `TOOL-dDeclaredLoop-69` S2's parent-equality exemption. That puts git's fatal exit
128 in the same bucket as an octopus merge or a git without the feature. Exit 128 covers unrelated
histories, missing objects and a broken object store. A run branch built from an orphan commit keeps the
old policy bytes and is merged into main with `--allow-unrelated-histories`: the re-merge exits 128,
M's policy blob equals the orphan parent's, the merge is skipped, and the old policy keys reach main with
no `Gov-Policy:` trailer. The guard fails open on a failed dependency.

This unit gives a failed re-merge its own state, graded without the exemption, and detects the missing
feature by a probe instead of an exit code. It repairs `TOOL-dDeclaredLoop-78`.

## 2. Scope (IN)

- **S1** — `resolve_write_tree_support()` in `tools/loop/guard.py` answers whether this git carries
  `merge-tree --write-tree`, by running `git merge-tree -h` once per process and passing its usage text
  to `check_write_tree_usage(text)`, true when the text names `--write-tree`. The answer is memoised, and
  no exit code of a real re-merge is ever read as the feature's absence. Observed by AC4, AC5.
- **S2** — C gains a fourth state, `failed`. `uncomputable` is now exactly an octopus merge or S1
  answering false, and the re-merge is then never run. A re-merge exiting 0 is 78 S1's `present` or
  `absent`. Exiting 1 is 69 S2's conflicted case, which `TOOL-dDeclaredLoop-75` S27 widens. Every other
  outcome is `failed`, carrying the code and git's first stderr line: exit 128, a usage exit 129 from a
  git S1 found capable, death by a signal, or a failure to start. Observed by AC1, AC3.
- **S3** — A `failed` C never takes 69 S2's parent-equality exemption. The merge is skipped only when M's
  policy blob equals every parent's blob. Otherwise each key whose value at M differs from its value at
  some parent is owed, an absent key reading as its own value as 59 §4 states, and with any owed key not
  named by a `Gov-Policy:` trailer the refusal is
  `policy: <merge8> — the clean re-merge failed: <rc> <stderr first line>`, naming the keys. A declared
  trailer clears it, so a legitimate unrelated-history merge is not wedged. Observed by AC1, AC2, AC3.
- **S4** — The re-merge runs through one function, `run_merge_tree(repo, p1, p2)`, answering
  `(rc, stdout, stderr)` and counting its calls; a plant replaces it, or S1, in-process for its own call
  alone, and prints `merge-tree runs: <n>`. Observed by AC3, AC4.
- **S5** — Four plants join `guard.py --fixture`. `push-merge-unrelated-histories`: main moves policy key
  `k` from 1 to 2, an orphan run branch holds the old file at `k = 1`, and main merges it with
  `--allow-unrelated-histories` keeping `k = 1`, with no trailer. `push-merge-unrelated-histories-trailered`:
  the same merge carrying `Gov-Policy: k`. `push-merge-tree-fatal`: a two-parent merge whose policy blob
  equals the run parent's, `run_merge_tree` answering 128. `push-merge-no-write-tree`: the same merge
  with S1 answering false. Observed by AC1, AC2, AC3, AC4.

## 3. Non-goals (OUT)

- Which re-merges exit 1 with the policy path outside the conflicts, and how C reads there:
  `TOOL-dDeclaredLoop-75` S27, unchanged in this unit, as its hands-off bullet to 75 records; the
  restatement of S27's body as present, absent or refused is id 4, `TOOL-dDeclaredLoop-82`.
- Retrying the re-merge with `--allow-unrelated-histories`: rejected in §4, measured.
- A parent blob that does not parse: 78 S3's refusal, unchanged; its parent-side plant is id 29,
  `TOOL-dDeclaredLoop-82`.
- A bug-class checklist entry that a guard mapping a subprocess's failure codes refuses each by name and
  lets only a probed absence take an exemption, the finding's left-shift: the class is recorded at the
  close; S5's plants are this grade's fatal-exit fixtures.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-78` — the three states of C in `check_push_range` of `tools/loop/guard.py`, whose `uncomputable` this unit narrows to an octopus merge or a probed absence of the feature
- **hands-off** `TOOL-dDeclaredLoop-75` — the exit table, in which S27's exit 1 stays the one non-zero exit graded on C or on the parents and every other exit is the failed state, refused untrailered, never a fall to the parents
- **hands-off** `TOOL-dDeclaredLoop-82` — the exit table, beside which that unit restates S27's exit-1 body as present, absent or refused (id 4)
- **hands-off** `TOOL-dDeclaredLoop-83` — S2's exit table, which that unit writes into 75 S27 in place of its fallback to the parents (the round-6 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-84` — S2's exit table, which that unit writes into 78's states and grade and into 82 S4 and AC4 (the round-6 spec audit's id 7)
- **hands-off** `TOOL-dDeclaredLoop-85` — `resolve_write_tree_support`, `check_write_tree_usage` and S4's plant hook, which that unit gives a third answer, `probe failed`, routed to the `failed` state, and restates in S1, S2, S5, §4, AC4 and AC5 (the round-6 spec audit's id 24)
- **hands-off** `TOOL-dDeclaredLoop-86` — S3's state names and parent-side parse refusal, the `failed` refusal text for a start failure, a signal and an empty stderr, and §4 Evidence's quotation of 75 S27, which that unit amends (the round-6 spec audit's ids 3, 18, 29)
- **hands-off** `TOOL-dDeclaredLoop-88` — S1's probe signature and rule, S3's state names, §4's grade and AC5, which that unit restates to the three-answer probe (the round-7 spec audit's ids 3, 6, 9, 12, 19, 21)

## 4. Design

### Evidence

Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, in a scratch repository under `%TEMP%`: PINNED, that
date.

- With `p.toml` at `k = 1` on `main` and an orphan `run` holding `k = 2`, `git merge-tree --write-tree
  main run` printed `fatal: refusing to merge unrelated histories` and exited 128.
- The same call with `--allow-unrelated-histories` exited 1, printing `CONFLICT (add/add): Merge
  conflict in p.toml`: the policy path is conflicted, which is 69 S2's parent branch and its exemption.
- `git merge-tree -h` exited 129 and printed `usage: git merge-tree [--write-tree] [<options>] <branch1>
  <branch2>`, its option list naming `--write-tree`. A git before the feature prints only the trivial
  form, `git merge-tree <base-tree> <branch1> <branch2>`: UNVERIFIED here, from git's documentation, so
  AC5 plants that text rather than an old git.
- `tools/branch-reconcile/branch_reconcile.py:648-651` probes the same capability once, by merging the
  default ref with itself, and its comment records why: a per-tip failure is also what unrelated
  histories produce, "and that is no statement about git".
- 78 S1 and its §4 grade take `uncomputable` on any exit other than 0
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md`, §2 S1, §4); 75 S27 keeps
  "any other exit code grades against the parents alone"; 59 S3 names only the octopus and exit 129.

### The grade, restated

```
supported = resolve_write_tree_support()             # once per process: git merge-tree -h names --write-tree
for merge M in the range, with parents P1..Pn:
    if n != 2 or not supported:   C = uncomputable    # merge-tree never run
    else:
        rc, out, err = run_merge_tree(repo, P1, P2)
        C = present(blob) | absent                    if rc == 0     # 78 S1
            conflicted                                if rc == 1     # 69 S2, widened by 75 S27
            failed(rc, first line of err)             otherwise      # 128, 129, signal, start failure
    present | absent:          78 S2, unchanged
    uncomputable | conflicted: 69 S2, unchanged, with 59 S3's printed line where uncomputable
    failed:
        skip only when blob(M) == blob(Pi) for every i
        owed = { k : val(M,k) != val(Pi,k) for some i }
        owed not all trailered -> refuse "the clean re-merge failed: <rc> <line>", naming the keys
```

### Files touched (estimate)

- `tools/loop/guard.py`

### Alternatives rejected

- **The self-merge probe of `branch_reconcile.py:648-651`.** It needs a readable commit, so a broken
  object store fails the probe, reads as absence, and hands the merge back to the exemption: the
  fail-open this unit closes. The usage text needs no object. The function is also another kit's, which
  the loop kit does not require.
- **Re-running the re-merge with `--allow-unrelated-histories`.** Measured above: the policy file
  conflicts add/add, which reaches the parent branch and its exemption again.
- **Refusing a failed re-merge whatever the trailer says.** No trailer could clear a legitimate
  unrelated-history merge; S3 owes the keys that differ and lets a declared trailer pass.

## 5. Production-readiness checklist

- security — closes a path on which an old policy reaches the default branch untrailered through a
  fatal git error.
- perf / scale — one `git merge-tree -h` per process; the re-merges are 78's, unchanged in number.
- error / empty / loading states — every re-merge outcome has a named state; a failed one refuses with
  its code and git's own line.
- observability — the refusal names the merge, the exit code, git's first stderr line and the keys; S4
  prints the re-merge count.
- risks — an unrelated-history merge that changes policy keys now owes a trailer for each; that is the
  defect closed.
- testing — AC1 to AC5 as plants and a probe; the arm under §7, observed at the close.
- migration — none: the rule is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant push-merge-unrelated-histories` grades the orphan
  merge, it exits 1 printing `the clean re-merge failed: 128` and naming key `k`.
  Red when: exit 128 reads as `uncomputable`, the parent exemption skips the merge, and the arm exits 0.
- **AC2** — When `--plant push-merge-unrelated-histories-trailered` grades the same merge carrying
  `Gov-Policy: k`, it exits 0.
  Red when: a failed re-merge refuses whatever the trailer names, wedging a declared merge.
- **AC3** — When `--plant push-merge-tree-fatal` runs, it exits 1 printing
  `the clean re-merge failed: 128` and the stub's stderr line, and `merge-tree runs: 1`.
  Red when: the merge is skipped because M's policy blob equals a parent's.
- **AC4** — When `--plant push-merge-no-write-tree` runs, it prints `graded against its parents only`,
  59 S3's line, and `merge-tree runs: 0`, and exits 0 as 69 S2 grades a merge equal to a parent.
  Red when: the plant still runs a re-merge, or the feature's absence is read off an exit code.
- **AC5** — When a `python -c` probe calls `check_write_tree_usage` on git 2.54's usage line
  `usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>` it answers True, on
  `usage: git merge-tree <base-tree> <branch1> <branch2>` it answers False, and
  `resolve_write_tree_support()` answers True on this node.
  Red when: the predicate matches `merge-tree` alone, so the trivial-form usage answers True.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop guard fixtures` leg (`TOOL-dDeclaredLoop-2`) green, which runs
`guard.py --fixture`; the leg is outside the base manifest.

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 · the unrelated-histories, tree-fatal and no-write-tree plants, staged against TOOL-dDeclaredLoop-78's C, which reads every non-zero exit as uncomputable · none

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

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-5 spec audit's id 28 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-83 and TOOL-dDeclaredLoop-84 and TOOL-dDeclaredLoop-85 and TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 78's state split in `check_push_range` and the single `merge-tree --write-tree` call 59 S2
makes; this unit names one more outcome of that call and mints no second caller.
`python tools/codebase-map/reuse_lookup.py "detect whether git supports an option before calling it"`
ranked `git`, `run_git` (`tools/branch-reconcile/branch_reconcile.py` among others), `read_git_output`
and `build_git_env` (`tools/memory-tree/tree_lib.py`); a grep for `merge-tree` across `tools/` found
`branch_reconcile.py:648-651`, the one existing capability probe, weighed and rejected above for its
fail-open on a broken store, so no existing seam fits the probe; `tools/loop/guard.py` is unbuilt at base.

Recall terms used: merge-tree write-tree exit 128 fatal unrelated histories refuse fail-open exemption guard policy
