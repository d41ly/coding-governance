# TOOL-dDeclaredLoop-85 — the write-tree capability probe has three answers, and only a probed absence takes the parent exemption

**Status:** CLOSED · rev-5 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-85-deviation-851.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-85-deviation-851.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-85-deviation-852.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-85-deviation-852.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-85-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-85-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-85-deviation-853.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-85-deviation-853.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-85-red-fix-28.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-85-red-fix-28.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-85-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-85-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-85-build-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-85-build-brief.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-85-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-85-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-86 |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
confirmed finding **id 24 at HIGH**, its item **H2**, alone in that item. The medium grade of the same
defect is item M2, id 9, batched into `TOOL-dDeclaredLoop-86`.

`TOOL-dDeclaredLoop-81` S1 answers that this git carries `merge-tree --write-tree` only when the joined
output of `git merge-tree -h` names `--write-tree`, and otherwise answers that it does not. A probe that
starts and then dies by a signal, exits with an unexpected code, or prints no usage text on either
stream reads as the feature's absence. 81 S2 maps that answer to `uncomputable`, which takes
`TOOL-dDeclaredLoop-69` S2's parents branch, and that branch never reads a merge whose policy blob
equals its first parent's. With git broken in the environment, such a merge reaches the default branch
untrailered. 81 rejects the self-merge probe of `tools/branch-reconcile/branch_reconcile.py#check_noop`
for exactly this fail-open and leaves its own probe open. A probe that cannot start raises `OSError` in
81 S1, which the push arm reports as `cannot judge`, exit 2: that refuses the whole push, a declared
merge included.

This unit gives the probe three answers and routes a failed probe, a start failure included, to 81's
`failed` state, the skeptic's corrected fix. It builds immediately after 81 and repairs the code
`TOOL-dDeclaredLoop-81` lands; 81's spec, landed by then, is not rewritten (§3).

## 2. Scope (IN)

- **S1** — `run_merge_tree_usage()` in `tools/loop/guard.py` runs `git merge-tree -h` under the
  environment `read_clean_env` gives, as 81 S1 runs it, and answers `(rc, stdout, stderr)`, both
  streams decoded as UTF-8 with replacement, letting `OSError` propagate. `resolve_write_tree_support`
  is its one caller. The in-process grade of 81 S4 swaps it for a twin for that grade alone. Observed
  by AC1, AC2, AC3.
- **S2** — `check_write_tree_usage(rc, text)` answers one of three strings, `text` being stdout and
  stderr joined by a newline. `supported`: the text names `--write-tree`. `unsupported`: `rc` is 129,
  a line of the text opens `usage: git merge-tree`, and the text does not name `--write-tree`.
  `probe failed`: anything else, a different exit code, a negative one for a signal, or no usage line
  on either stream included. 81 S1's one-argument predicate answering true or false is replaced by
  this one in place. Observed by AC4.
  **Readers:**
  by name: `tools/loop/guard.py`, the write-tree resolver that calls the predicate
  by value: NO VALUE READERS: the answer is read only by the resolver beside it in the same module
- **S3** — `resolve_write_tree_support()` answers `(answer, detail)`: `probe failed` with the detail
  `build_failure_detail(error, "")` when `run_merge_tree_usage` raises `OSError`, and otherwise
  `check_write_tree_usage(rc, text)` with the detail `build_failure_detail(rc, text)`. It is memoised
  with `functools.cache`, a failed probe included, so a broken git is probed once per process. The
  in-process grade of 81 S4 calls `resolve_write_tree_support.cache_clear()` before it installs its
  stand-ins and after it removes them, so no grade reads an answer another grade's twin or real probe
  left. 81 S1's `cannot judge` exit for a probe that cannot start is replaced by `probe failed`.
  Observed by AC1, AC2, AC4, AC5.
  **Readers:**
  by name: `tools/loop/guard.py`, the cannot-judge catch of its push arm and the in-process grade of its plants
  by value: `.githooks/pre-push`, the policy push arm block, which turns the arm's exit into the `policy-unrecorded` refusal
- **S4** — 81 S2's state table in `read_remerge_policy` reads the three answers. An octopus merge stays
  `uncomputable` and never probes. For a two-parent merge, `unsupported` is `uncomputable` with 81's
  reason `this git has no merge-tree --write-tree`; `probe failed` is `failed` with the detail
  `probe failed: <detail>`, and `run_merge_tree` is not called; `supported` runs 81's exit table over
  `run_merge_tree`'s answer. A `failed` merge is graded by 81 S3: the push arm prints
  `loop-guard: push · <sha8> graded against every parent — the clean re-merge failed: probe failed: <detail>`
  and owes each key that differs from some parent, each missing trailer or record the arm's own
  finding naming the merge and the key, so a declared `Gov-Policy:` trailer and record clear it.
  Observed by AC1, AC2, AC3.
  **Readers:**
  by name: `tools/loop/guard.py`, the states of its re-merge reader and the failed line of its push arm
  by value: `.githooks/pre-push`, the policy push arm block, which turns the arm's exit into the `policy-unrecorded` refusal
- **S5** — Three plants join `PLANTS` in `tools/loop/guard.py`, their scenarios branches of
  `run_guard_plant`, each graded in-process with `run_merge_tree_usage` swapped for a twin and
  `run_merge_tree` counted. `push-merge-probe-failed` and `push-merge-probe-silent` build the history of
  81's `push-merge-tree-fatal`, a merge whose policy blob equals its first parent's, with no trailer or
  record; the first twin raises `OSError("fx stand-in")`, the second answers `(129, "", "")`, and each
  owes exit 1 by an entry of `run_selftest`'s owed map. `push-merge-old-git-usage` builds the history of
  `push-merge-both-sides-clean`, as 81's `push-merge-no-write-tree` does, its twin answering
  `(129, "", "usage: git merge-tree <base-tree> <branch1> <branch2>\n")`, and owes exit 0. Observed by
  AC1, AC2, AC3, AC5.
- **S6** — `build_failure_detail(outcome, text)` in `tools/loop/guard.py` is the one spelling of every
  detail under `the clean re-merge failed:`. An `OSError` reads `start failed: <its text>`; an exit code
  reads `<rc>`, followed by a space and the first non-blank line of `text` where it has one. The probe
  passes its joined text; 81 S2's re-merge detail is built through it too, passing standard error, and
  passing `(0, "no tree id")` for an exit 0 that prints no tree id, so 81's lines print as 81 writes
  them. Observed by AC4, AC6.
- **S7** — The push arm's paragraph of the module docstring of `tools/loop/guard.py` and the merge
  sentence of the push-check paragraph of `help/policy.md`, as 81 S6 writes them, gain one clause: a
  git whose usage probe fails, cannot start or prints no usage text is graded as a failed re-merge, and
  only a usage text lacking `--write-tree` reads as a git without it. Observed by AC7.

## 3. Non-goals (OUT)

- Accepting exit 0 from the probe, and requiring a usage line for `supported` too: M2's fix beyond this
  one, id 9, a scope item of `TOOL-dDeclaredLoop-86`.
- The refusal text of a re-merge, not a probe, that dies by a signal or prints nothing on standard
  error: id 29, a scope item of `TOOL-dDeclaredLoop-86`; S6's builder spells what 81 S2 already spells.
- The `signal <n>` spelling, the probe's locale, a memo keyed to the probe it called, and a trailered
  probe plant: `TOOL-dDeclaredLoop-88` and `TOOL-dDeclaredLoop-90`, as the edges below record.
- Restating `TOOL-dDeclaredLoop-81`'s spec to the three answers, rev-4's S6 and its AC5. 81 builds and
  lands before this unit, and a landed spec is frozen (`memory/TEMPLATE-SPEC.md`: a landed record is
  frozen and is not rewritten); 81 rev-5's §3 already hands the third answer to this
  unit, so its reader is pointed here.
- A bug-class checklist entry that a feature probe has three outcomes and only a probed absence may take
  an exemption, the finding's left-shift: the class is recorded at the close; S5's plants are this
  probe's failure fixtures.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-81` — `resolve_write_tree_support`, `check_write_tree_usage`, `run_merge_tree`, S2's state table with its `failed` state, S3's every-parent grade and S4's in-process grade, in `tools/loop/guard.py`, which this unit gives a third answer, a route to `failed` and one detail builder
- **hands-off** `TOOL-dDeclaredLoop-86` — S2's predicate, whose `supported` and `unsupported` that unit narrows to exit 0 or 129 with a usage line (id 9)
- **hands-off** `TOOL-dDeclaredLoop-88` — `run_merge_tree_usage`, the memoised resolver, the probe detail, S2's predicate, the probe plants, AC2, AC5 and Files touched, which that unit keys, pins, unifies, narrows, extends and widens (the round-7 spec audit's ids 4, 10, 18, 19, 23, 25, 26, 27, 30, 31, 32)
- **hands-off** `TOOL-dDeclaredLoop-90` — S1 and S3, which that unit completes with `LC_ALL=C` and the probe-keyed memo (the round-8 spec audit's id 5)
- **hands-off** `TOOL-dDeclaredLoop-94` — S3's `OSError` spelling, which that unit restates to 88 S24's builder (the round-10 spec audit's id 20)

## 4. Design

### Evidence

Every code claim below was read on `branch/unattended-declared-loop-d56bf0` at `27143aff6` through
`git show`, `git grep` and `git archive`; this worktree is cut from main, which lacks the loop kit.

- Probed 2026-11-15 on node `d`, git 2.54.0.windows.1, in this worktree: PINNED, that date.
  `git merge-tree -h` exited 129, wrote nothing to standard error, and printed on standard output
  `usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>` and then
  `or: git merge-tree [--trivial-merge] <base-tree> <branch1> <branch2>`. A probe reading standard
  error alone answers absence on a capable git, which is why S2 joins both streams.
- A git before the feature prints only the trivial form: UNVERIFIED, from git's documentation, as 81
  §4 records, so `push-merge-old-git-usage` plants that text rather than an old git.
- `tools/loop/guard.py#read_remerge_policy`, built by `TOOL-dDeclaredLoop-59`, is the one `merge-tree`
  call in the module, run through `tools/loop/loop_witness.py#read_git`, which discards standard error;
  no probe exists at that tip. `tools/loop/guard.py#check_push_range` runs
  `tools/memory-tree/commit_trailers.py#read_commits`, one `git log`, before it grades any merge, so a
  git that cannot start at all exits 2 there before any probe runs, and catches `OSError` as
  `cannot judge`, exit 2.
- `TOOL-dDeclaredLoop-81` rev-5, unbuilt at that tip, writes `resolve_write_tree_support()` running the
  probe once per process under `read_clean_env`, the predicate `check_write_tree_usage(text)` true when
  the text names `--write-tree`, and a probe that cannot start raising `OSError` to `cannot judge`
  (81 S1). Its S2 names `uncomputable`, exactly an octopus merge or the probe's absence answer, with the
  reason `this git has no merge-tree --write-tree`; `conflicted` for exit 1; and `failed` for every
  other outcome of `run_merge_tree(p1, p2)`, an exit 0 printing no tree id included, its detail the
  exit code and the first non-blank line of standard error, `0 no tree id`, or
  `start failed: <the error's text>`. Its S3 prints
  `<sha8> graded against every parent — the clean re-merge failed: <detail>` and owes each key that
  differs from some parent (81 §8 F3). Its S4 grades a plant in-process with `run_merge_tree`, or the
  resolver itself, swapped by `unittest.mock.patch.object` and the re-merge counted as
  `merge-tree runs: <n>`. 81 §3 hands the probe's third answer to this unit. This spec is written on
  that committed text.
- `TOOL-dDeclaredLoop-78` rev-6, unbuilt, names C's states once in `read_remerge_policy`'s answer (78
  S1), and `TOOL-dDeclaredLoop-69` rev-3, unbuilt, sends `uncomputable` to its parents branch, which
  reads a merge only where the combined list names the policy file and its blob differs from its first
  parent's, and prints nothing for any other (69 S2).
- `tools/loop/guard.py#run_selftest` runs every plant through
  `tools/loop/loop_lib.py#run_selftest_cases`, which calls `main` in this process, so a memo set by one
  in-process grade outlives it into every later plant; `tools/loop/guard.py#run_fixture` holds a row
  when its exit and its one needle match, and exits as the last row did when every row held, else 3.
- `tools/loop/guard.py#run_guard_plant` builds `push-merge-both-sides-clean`'s history in one branch,
  a clean `--no-ff` merge of `side`'s cap raise and `main`'s `review.max-rounds`, whose blob differs
  from both parents', so the parents branch reads it and prints its line.

### The grade, after this unit

```
    support, detail = resolve_write_tree_support()        once per process, functools.cache
        run_merge_tree_usage raises OSError -> probe failed, build_failure_detail(error, "")
        else check_write_tree_usage(rc, stdout + "\n" + stderr), build_failure_detail(rc, that text)
    for merge M with parents P1..Pn:
        n != 2                     -> uncomputable, the octopus reason; never probes      (81 S2)
        support == "unsupported"   -> uncomputable, "this git has no merge-tree --write-tree"
        support == "probe failed"  -> failed, "probe failed: <detail>"; run_merge_tree not called
        support == "supported"     -> 81's exit table over run_merge_tree(P1, P2)
    failed -> 81 S3: the every-parent line, then a finding per missing trailer or record
```

### The plants

Each needle a plant reads from one grade is its own row over the same output, as 81 §4 writes.

| Plant | History | Twin | Owed |
|---|---|---|---|
| `push-merge-probe-failed` | 81's `push-merge-tree-fatal` | `run_merge_tree_usage` raising `OSError("fx stand-in")` | exit 1 naming `the clean re-merge failed: probe failed: start failed: fx stand-in`, `merge <sha8> · .governance/policy.toml · review.max-rounds` and `merge-tree runs: 0` |
| `push-merge-probe-silent` | 81's `push-merge-tree-fatal` | `run_merge_tree_usage` answering `(129, "", "")` | exit 1 naming `the clean re-merge failed: probe failed: 129`, `merge <sha8> · .governance/policy.toml · review.max-rounds` and `merge-tree runs: 0` |
| `push-merge-old-git-usage` | `push-merge-both-sides-clean` | `run_merge_tree_usage` answering 129 with the trivial usage line on standard error | exit 0 naming `graded against its parents only — this git has no merge-tree --write-tree` and `merge-tree runs: 0` |

The policy path is `tools/policy/guard.py#POLICY`. In the first two, an absence reading sends the merge
to 69 S2's parents branch, which skips it silently, so the grade exits 0 where 1 is owed; a
`supported` reading runs the real re-merge and counts 1. In the third, a `probe failed` reading grades
the merge against every parent, owing the cap and `review.max-rounds`, so the grade exits 1 where 0 is
owed. Each miss makes the plant exit 3.

### Inventory

- The top-level functions `run_merge_tree_usage` and `build_failure_detail`.
- The `PLANTS` keys `push-merge-probe-failed`, `push-merge-probe-silent` and `push-merge-old-git-usage`,
  and the owed-map entries of the first two.
- The answers `supported`, `unsupported` and `probe failed`, and the detail prefix `probe failed: `.

### Files touched (estimate)

- `tools/loop/guard.py`
- `help/policy.md`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The finder's fix, reading stdout only and requiring exit 129 for `supported`.** The skeptic judged it
  unsound: it ties the answer to one stream and one code where the corrected fix needs neither for a text
  that names the option; the narrowing to exit 0 or 129 is M2's and is batched.
- **Retrying the probe on failure.** A broken git fails twice, and a retry hides a flaky one; the failed
  answer refuses with its detail and a trailer clears a legitimate merge.
- **81 S1's `cannot judge` exit for a probe that cannot start.** It refuses the whole push, a declared
  merge included, which §8 F2 rejects; a git that cannot start at all already exits 2 at
  `read_commits`, before any probe.
- **Plants that swap `resolve_write_tree_support` itself, as 81's `push-merge-no-write-tree` does.**
  They would skip the predicate, the stream join and the detail, the code this unit adds.
- **One runner for the probe and the re-merge.** 81's plants count every `run_merge_tree` call as a
  re-merge, so a probe through it would read `merge-tree runs: 1` where none ran; each body is one
  `subprocess.run` call.
- **`tools/run-gates/measure_legs.py#LaunchFailed` for the start failure.** It is the run-gates kit's,
  about a suspended job root, and the loop kit does not require that kit; a plain `OSError` is what
  `subprocess` raises.

## 5. Production-readiness checklist

- security — closes the path on which a failed probe certifies an untrailered merge whose policy blob
  equals a parent's. A probe that cannot start now grades each merge against every parent instead of
  refusing the push: an untrailered change still refuses, a declared one passes (§8 F2).
- perf / scale — one probe per process, memoised whatever it answers; a plant clears the memo around
  its own grade only.
- error / empty / loading states — every probe outcome has a named answer; a failed one refuses with its
  detail.
- observability — the `failed` line prints `probe failed:` and the detail; the plant's
  `merge-tree runs:` line shows the re-merge was not run.
- risks — on a node whose git probe fails, every untrailered two-parent merge that changes policy keys
  now refuses; that is the defect closed, and a trailer clears it.
- testing — AC1 to AC3 and AC6 as plants, AC4 and AC5 as probes, AC7 as greps; the arm under §7,
  observed at the close.
- migration — none: the probe is unbuilt at that tip.
- user docs — `help/policy.md`, the push-check paragraph's merge sentence, by S7.

### Dependencies on units built beside this one

- `TOOL-dDeclaredLoop-59` is built: `read_remerge_policy` and the plant `push-merge-both-sides-clean`,
  whose history the third plant reuses, sit at that tip.
- `TOOL-dDeclaredLoop-69` (order 18), `TOOL-dDeclaredLoop-78` (order 19) and `TOOL-dDeclaredLoop-81`
  (order 20) are next and unbuilt. This spec is written on 69 rev-3, 78 rev-6 and 81 rev-5, and builds
  after 81 lands: S1 to S6 extend 81's resolver, predicate, state table, in-process grade and the
  history of `push-merge-tree-fatal`.
- `TOOL-dDeclaredLoop-112`, `TOOL-dDeclaredLoop-14`, `TOOL-dDeclaredLoop-45`, `TOOL-dDeclaredLoop-4`,
  `TOOL-dDeclaredLoop-46` and `TOOL-dDeclaredLoop-6` are being built or are next; this unit reads none of
  the code they change. 14, 4, 6 and 112 also list `memory/map/generated/symbols.json` among their
  files, and all six name `tools/run-gates/selftest-budgets.txt`; this unit edits only the
  `loop guard fixtures` row there and regenerates the render once from its own tree.
- `TOOL-dDeclaredLoop-86`, `TOOL-dDeclaredLoop-88`, `TOOL-dDeclaredLoop-90` and `TOOL-dDeclaredLoop-94`
  build after and restate this unit's names, as §3's edges record.

### What the change could newly red

| Artifact | Why | What keeps it green |
|---|---|---|
| `loop guard fixtures`, `guard.py --selftest` | it runs every plant in one process, so a memo or a twin could outlive its grade | the in-process grade clears the memo before and after and its swaps end with it (S3); the two plants owed 1 join the owed map |
| 81's `push-merge-tree-fatal`, `push-merge-unrelated-histories` and `push-merge-no-write-tree` | their failed and uncomputable lines are spelled through S6's builder and S4's table | the builder spells 81's details as 81 writes them (AC6); `push-merge-no-write-tree` swaps the resolver, which S4 reads unchanged |
| `push-merge-both-sides-clean`, `push-merge-resolution-edit`, `push-merge-carries-trailered`, `push-merge-conflict-pick`, 69's and 78's plants | their merges probe through the subprocess grade | the probe answers `supported` on git 2.54, PINNED 2026-11-15, so 81's exit table runs as before |
| `push-merge-octopus` | none: an octopus never probes | `uncomputable` keeps the octopus reason |
| `push-no-trailer`, `push-new-branch` | none: their ranges hold no merge | a non-merge is graded as before |
| `tools/run-gates/selftest-budgets.txt`, the `loop guard fixtures` row | the new plants lengthen the leg | the row is re-priced from a timed run of the leg alone, by the row's own rule |
| `memory/map/generated/symbols.json` | it lists the module's top-level functions | regenerated with `gen_map.py --write` for the two functions, held by `codebase-map coverage + freshness` |
| `tools/policy/check_policy.py`, its read of `help/policy.md` | it reads the page for the install-day deferral line | S7 touches only the push-check paragraph |
| `.githooks/pre-push.test.sh`, its policy push arms | they run a stand-in `guard.py` | untouched: the hook's logic does not move |

The govkit registry row for `loop guard fixtures` in `tools/govkit/registry.toml`, its subject pin in
`tools/govkit/subject-pins.tsv` and its row in `tools/gate-legs.json` name the leg and the module,
which do not move. A tree grep on that branch for `loop/guard.py` and the leg found no usage row, no
entry in the `DELEGATES` list of `tools/memory-tree/check-verdict-epoch.sh`, and no path on the watch
line of `memory/guides/SESSION-KICKOFF.md`. `tools/loop/README.md` names the module's modes, not its
plants or functions. The new code spells no install prefix.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/guard.py --fixture --plant push-merge-probe-failed` runs, it exits 1
  printing `the clean re-merge failed: probe failed: start failed: fx stand-in`,
  `merge <sha8> · .governance/policy.toml · review.max-rounds`, `merge-tree runs: 0` and `all held`.
  Red when: a probe that cannot start reads as the feature's absence, the parents branch skips the
  merge, and the plant exits 3.
- **AC2** — When `python tools/loop/guard.py --fixture --plant push-merge-probe-silent` runs, it exits 1
  printing `the clean re-merge failed: probe failed: 129`, `merge-tree runs: 0` and `all held`.
  Red when: a usage exit with no usage text reads as the feature's absence.
- **AC3** — When `python tools/loop/guard.py --fixture --plant push-merge-old-git-usage` runs, it exits 0
  printing `graded against its parents only — this git has no merge-tree --write-tree`,
  `merge-tree runs: 0` and `all held`.
  Red when: the predicate reads stdout alone and the old git's usage on standard error answers
  `probe failed`, so the merge owes its keys and the plant exits 3.
- **AC4** — When a `python -c` probe in `tools/loop/` imports `guard` and calls `check_write_tree_usage`
  on `(129, "usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>")`,
  `(129, "usage: git merge-tree <base-tree> <branch1> <branch2>")`, `(129, "")`,
  `(128, "fatal: not a git repository")` and `(-9, "")`, it answers `supported`, `unsupported`,
  `probe failed`, `probe failed` and `probe failed`; `build_failure_detail` answers `129` on
  `(129, "")`, `128 fatal: x` on `(128, "\n  \nfatal: x\n")` and `start failed: e` on
  `(OSError("e"), "")`; and `resolve_write_tree_support()` answers `supported` as its first element on this node.
  Red when: any outcome but a usage line lacking the option answers `unsupported`.
  fixture: the last call needs a git carrying the feature; node `d` runs git 2.54.0.windows.1, PINNED 2026-11-15.
- **AC5** — When a `python -c` probe in `tools/loop/` imports `guard` and calls
  `guard.main(["--fixture", "--plant", "push-merge-tree-fatal"])` and then
  `guard.main(["--fixture", "--plant", "push-merge-probe-silent"])` in that one process, both exit 1
  and the second prints `merge-tree runs: 0` and `all held`.
  Red when: the first grade's real probe leaves `supported` in the memo, so the second runs the real
  re-merge, counts 1 and exits 3.
- **AC6** — When `python tools/loop/guard.py --fixture --plant push-merge-tree-fatal` runs, it exits 1
  printing `the clean re-merge failed: 128 fatal: fx stand-in` and `all held`.
  Red when: the re-merge detail and the probe detail are spelled apart and the shared builder drops the
  first standard error line.
- **AC7** — When `grep -c "usage probe"` runs over `help/policy.md` and over `tools/loop/guard.py`, each
  prints at least 1.
  Red when: the page and the docstring still read every probe outcome but `supported` as a git without
  the feature.

## 7. Gates

`loop guard fixtures` · `policy fixtures` · `docs` · `measure-legs selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

This pass keeps the sibling-minted `loop guard fixtures` leg (`TOOL-dDeclaredLoop-2`) green, which runs
every plant of the guard's self-test in one process.

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC5 · the probe-failed, probe-silent and old-git-usage plants, staged red against TOOL-dDeclaredLoop-81's two-answer probe, which reads every failed probe as the feature's absence, and AC5 staged red by dropping the memo clear around the in-process grade · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Route a failed probe to `failed`, or refuse the whole range by name?** (a) every two-parent merge
  is `failed`, graded by 81 S3, so a trailered merge passes; (b) the range refuses with one line naming
  the probe. Both meet AC1's exit 1. (b) wedges every push on a broken git, trailered or not, a follow-up
  (a) does not leave, and (a) is the skeptic's corrected fix. RESOLVED (agent, 2026-10-24, delegated):
  (a), S4. widens: none · relaxes: none
- **F3 — One detail builder now, or the probe's own spelling with the unification left to 88?** 81
  rev-5 spells the re-merge's detail inline, and this unit's probe detail has the same shape.
  - (a) `build_failure_detail(outcome, text)`, one function both details pass through, written here at
    the shape's second instance, the charter's reuse rule; 88 S24 then widens it with its empty label
    and `signal <n>` rather than minting it.
  - (b) A probe-local spelling beside 81's inline one, as rev-4 wrote with `rc <n>`, and 88 S24, the
    round-7 audit's id 18, unifies the two later: two spellings of one line between this pass and 88's.
  Recommendation: (a). The body is written on it (S6), and its name is the one 88 S24 already uses.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: one builder at the second instance, under the charter's reuse rule
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-6 spec audit's id 24 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-5 · 2026-11-15 · §1 · S1 S2 S3 S4 S5 S6 S7 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6 AC7 · §7 ·
  §8 · §10 · re-grounded on branch/unattended-declared-loop-d56bf0 at `27143aff6` by the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-85-1-spec-writer; mechanism, carries, order and status kept.
  Written on TOOL-dDeclaredLoop-81 rev-5, 78 rev-6 and 69 rev-3: S1 takes no repository argument;
  S3 memoises with `functools.cache`, cleared around each in-process grade, and reads a start failure as
  `probe failed` where 81 exits 2; S4 prints 81 F3's every-parent line, not a refusal of its own; S5
  grades in-process over 81's histories, the old-git plant on one the parents branch reads; S6 is one
  detail builder spelled as 81 spells (F3); S7 brings the docstring and help clause; the restatement of
  81's spec and its criterion leave scope, 81 being landed and frozen when this unit builds; AC5 now
  observes the memo across two plants in one process; §5 names the dependencies and what could red.

## 10. Reuse audit

The seam is 81's `resolve_write_tree_support` and `check_write_tree_usage` in `tools/loop/guard.py`,
extended in place to three answers, 81's `failed` state, which a failed probe joins rather than minting
a fourth refusal, and 81's in-process grade, whose swap list gains `run_merge_tree_usage`. The detail
builder of S6 is extracted at its second instance, 81's re-merge detail being the first (§8 F3).
`python tools/codebase-map/reuse_lookup.py "spell a subprocess failure detail from its exit code and
first output line"`, run 2026-11-15 over this worktree's tree, which lacks the loop kit, ranked
`check_line` (`tools/runlog/runlog_lib.py`), `read_git_output` (`tools/memory-tree/tree_lib.py`) and
`render_line` first; none spells an exit and a first line. rev-1's query, `"probe whether a git
subcommand supports an option, distinguishing a failed probe"`, ranked `run_git`
(`tools/branch-reconcile/branch_reconcile.py` among others), `read_git_output` and `LaunchFailed`
(`tools/run-gates/measure_legs.py`); none answers a three-way capability, and the last is rejected
above, so no existing seam fits the probe beyond 81's.

Recall terms used: capability probe fail-open exemption merge-tree write-tree usage exit 129 probe failed unsupported failure detail memo
