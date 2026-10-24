# TOOL-dDeclaredLoop-85 — the write-tree capability probe has three answers, and only a probed absence takes the parent exemption

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-85-deviation-851.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-85-deviation-851.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
confirmed finding **id 24 at HIGH**, its item **H2**, alone in that item. The medium grade of the same
defect is item M2, id 9, batched into `TOOL-dDeclaredLoop-86`.

`TOOL-dDeclaredLoop-81` S1 answers "supported" only when the usage text of `git merge-tree -h` names
`--write-tree`, and has no answer for a probe that fails. A probe that cannot start, dies by a signal,
exits with an unexpected code, or prints nothing on the stream read answers false. 81 §4 maps false to
`uncomputable`, which takes `TOOL-dDeclaredLoop-69` S2's parent-equality exemption. With git broken in the
environment, a merge whose policy blob equals one parent's is skipped untrailered. 81 rejects
`branch_reconcile`'s self-merge probe for exactly this fail-open and leaves its own probe open.

This unit gives the probe three answers and routes a failed probe to 81's `failed` state, the skeptic's
corrected fix. It builds immediately after 81 and repairs `TOOL-dDeclaredLoop-81`.

## 2. Scope (IN)

- **S1** — `run_merge_tree_usage(repo)` in `tools/loop/guard.py` runs `git merge-tree -h` and answers
  `(rc, stdout, stderr)`, letting `OSError` propagate. A plant replaces it in-process for its own call
  alone, as 81 S4 replaces `run_merge_tree`. Observed by AC1, AC2, AC3.
- **S2** — `check_write_tree_usage(rc, text)` answers one of three strings, `text` being stdout and stderr
  joined. `supported`: the text names `--write-tree`. `unsupported`: `rc` is 129, a line of the text opens
  `usage: git merge-tree`, and the text does not name `--write-tree`. `probe failed`: anything else, a
  different exit code or no usage line on either stream included. Observed by AC4.
- **S3** — `resolve_write_tree_support()` answers `probe failed` when `run_merge_tree_usage` raises
  `OSError`, and otherwise `check_write_tree_usage`'s answer, with a detail string for the refusal:
  `start failed: <strerror>`, or `rc <n>` followed by the first non-blank line of the text, or by
  `(no output)` where the text has none.
  The answer is memoised once per process, a failed probe included, so a broken git is probed once.
  Observed by AC1, AC2, AC4.
- **S4** — The grade reads the three answers. An octopus merge stays `uncomputable` whatever the probe
  answered. Only `unsupported` makes a two-parent merge `uncomputable`. `probe failed` makes it 81 S2's
  `failed` without running the re-merge, graded by 81 S3, and its refusal is
  `policy: <merge8> — the clean re-merge failed: probe failed: <detail>`, naming the keys. A declared
  `Gov-Policy:` trailer clears it as 81 S3 states. Observed by AC1, AC2, AC3.
- **S5** — Three plants join `guard.py --fixture`, each a two-parent merge whose policy blob equals the
  run parent's, with no trailer. `push-merge-probe-failed`: the probe twin raises `OSError`.
  `push-merge-probe-silent`: the probe twin answers 129 with both streams empty.
  `push-merge-old-git-usage`: the probe twin answers 129 with
  `usage: git merge-tree <base-tree> <branch1> <branch2>` on stderr and nothing on stdout.
  Observed by AC1, AC2, AC3.
- **S6** — 81's text is restated to the three answers, as a rev bump of 81 with its §9 line: S1 names
  them, S2's "S1 answering false" and S5's "with S1 answering false" read `unsupported`, the §4 grade
  carries S4's three branches, and AC4 and AC5 name `unsupported`. Observed by AC5.

## 3. Non-goals (OUT)

- Accepting exit 0 from the probe, and requiring a usage line for `supported` too: M2's fix beyond this
  one, id 9, a scope item of `TOOL-dDeclaredLoop-86`.
- The refusal text of a re-merge, not a probe, that fails to start or dies by a signal: id 29, a scope
  item of `TOOL-dDeclaredLoop-86`.
- A bug-class checklist entry that a feature probe has three outcomes and only a probed absence may take
  an exemption, the finding's left-shift: the class is recorded at the close; S5's plants are this
  probe's failure fixtures.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-81` — `resolve_write_tree_support`, `check_write_tree_usage`, S4's in-process plant hook and S2's `failed` state, in `tools/loop/guard.py`, which this unit gives a third answer and a route to `failed`
- **hands-off** `TOOL-dDeclaredLoop-86` — S2's predicate, whose `supported` and `unsupported` that unit narrows to exit 0 or 129 with a usage line (id 9)

## 4. Design

### Evidence

Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, at the worktree root: PINNED, that date.

- `git merge-tree -h` exited 129 with 898 bytes on stdout and 0 bytes on stderr. Its first lines were
  `usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>` and
  `   or: git merge-tree [--trivial-merge] <base-tree> <branch1> <branch2>`. A probe reading stderr alone
  answers false on a capable git, which is why S2 joins both streams.
- 81 S1 answers true "when the text names `--write-tree`" and its §4 grade reads
  `if n != 2 or not supported: C = uncomputable`
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`, §2 S1, §4).
- 81 §4 rejects `tools/branch-reconcile/branch_reconcile.py:648-651`'s self-merge probe because "a broken
  object store fails the probe, reads as absence, and hands the merge back to the exemption" (81 §4,
  Alternatives rejected).
- A git before the feature prints only the trivial form: UNVERIFIED, from git's documentation, as 81 §4
  records, so `push-merge-old-git-usage` plants that text rather than an old git.

### The grade, after this unit

```
support, detail = resolve_write_tree_support()      # once per process; OSError -> probe failed
for merge M with parents P1..Pn:
    if n != 2:                        C = uncomputable                 # 69 S2, 59 S3's line
    elif support == "unsupported":    C = uncomputable                 # 69 S2, 59 S3's line
    elif support == "probe failed":   C = failed("probe failed", detail)   # 81 S3, re-merge not run
    else:                             81's table: rc 0 -> present | absent, 1 -> conflicted, else failed
```

### Files touched (estimate)

- `tools/loop/guard.py`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`

### Alternatives rejected

- **The finder's fix, reading stdout only and requiring exit 129 for `supported`.** The skeptic judged it
  unsound: it ties the answer to one stream and one code where the corrected fix needs neither for a text
  that names the option; the narrowing to exit 0 or 129 is M2's and is batched.
- **Retrying the probe on failure.** A broken git fails twice, and a retry hides a flaky one; the failed
  answer refuses with its detail and a trailer clears a legitimate merge.
- **`LaunchFailed` of `tools/run-gates/measure_legs.py:192` for the start failure.** It is the run-gates
  kit's, about a suspended job root, and the loop kit does not require that kit; a plain `OSError` is what
  `subprocess` raises.

## 5. Production-readiness checklist

- security — closes the path on which a failed probe certifies an untrailered merge whose policy blob
  equals a parent's.
- perf / scale — unchanged: one probe per process, memoised whatever it answers.
- error / empty / loading states — every probe outcome has a named answer; a failed one refuses with its
  detail.
- observability — the refusal prints `probe failed:` and the detail; 81 S4's `merge-tree runs:` line
  shows the re-merge was not run.
- risks — on a node whose git cannot run, every untrailered two-parent merge that changes policy keys now
  refuses; that is the defect closed, and a trailer clears it.
- testing — AC1 to AC5 as plants, a probe and greps; the arm under §7, observed at the close.
- migration — none: `tools/loop/guard.py` is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant push-merge-probe-failed` runs, it exits 1 printing
  `the clean re-merge failed: probe failed: start failed` and `merge-tree runs: 0`.
  Red when: a probe that cannot start reads as `unsupported`, the merge is graded against its parents
  only, and the arm exits 0.
- **AC2** — When `--plant push-merge-probe-silent` runs, it exits 1 printing
  `the clean re-merge failed: probe failed: rc 129`.
  Red when: a usage exit with no usage text reads as the feature's absence.
- **AC3** — When `--plant push-merge-old-git-usage` runs, it prints `graded against its parents only`,
  59 S3's line, and `merge-tree runs: 0`, and exits 0 as 69 S2 grades a merge equal to a parent.
  Red when: the predicate reads stdout alone and the old git's stderr usage answers `probe failed`.
- **AC4** — When a `python -c` probe imports `guard` from `tools/loop/` and calls
  `check_write_tree_usage` on `(129, "usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>")`,
  `(129, "usage: git merge-tree <base-tree> <branch1> <branch2>")`, `(129, "")` and
  `(128, "fatal: not a git repository")`, it answers `supported`, `unsupported`, `probe failed` and
  `probe failed`, and `resolve_write_tree_support()` answers `supported` on this node.
  Red when: any outcome but a usage line lacking the option answers `unsupported`.
- **AC5** — When `grep -c "answering false\|not supported"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`, it prints 0, and
  `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over it piped to `grep -c "probe failed"` prints at least 1.
  Red when: 81 still describes a two-answer probe beside this unit's code.

## 7. Gates

`recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

This pass keeps the sibling-minted `loop guard fixtures` leg (`TOOL-dDeclaredLoop-2`) green, which runs
`guard.py --fixture`; the leg is outside the base manifest.

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 · the probe-failed, probe-silent and old-git-usage plants, staged against TOOL-dDeclaredLoop-81's two-answer probe, which reads a failed probe as the feature's absence · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Route a failed probe to `failed`, or refuse the whole range by name?** (a) every two-parent merge
  is `failed`, graded by 81 S3, so a trailered merge passes; (b) the range refuses with one line naming
  the probe. Both meet AC1's exit 1. (b) wedges every push on a broken git, trailered or not, a follow-up
  (a) does not leave, and (a) is the skeptic's corrected fix. RESOLVED (agent, 2026-10-24, delegated):
  (a), S4. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-6 spec audit's id 24 (HIGH, item H2).

## 10. Reuse audit

The seam is 81's `resolve_write_tree_support` and `check_write_tree_usage` in `tools/loop/guard.py`,
extended in place to three answers, and 81's `failed` state, which a failed probe joins rather than
minting a fourth refusal. `python tools/codebase-map/reuse_lookup.py "probe whether a git subcommand
supports an option, distinguishing a failed probe"` ranked `git`, `probe`, `run_git`
(`tools/branch-reconcile/branch_reconcile.py` among others), `read_git_output` (`tools/memory-tree/tree_lib.py`)
and `LaunchFailed` (`tools/run-gates/measure_legs.py`); none answers a three-way capability, and the last
is rejected above, so no existing seam fits the probe beyond 81's. The memory-recall query returned the
round-6 report's H2, 81 itself and `DEPL-dRatifiedSeam-5`, an index read with no liveness on git's exit
code, the same dead-probe shape.

Recall terms used: capability probe fail-open exemption merge-tree write-tree usage exit 129 probe failed unsupported
