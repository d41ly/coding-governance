# Closing diff review — dCarriedReceipt, the five units built on node `a`

**Serves:** diff-review DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15

## Verdict: CLEAN WITH FIXES

**This was NOT the adversarial fan `memory/guides/REVIEW-PROTOCOL.md` specifies, and that is the
single most important sentence in this record.** This session was started under an explicit standing
instruction not to use workflows or spawn agents. The method's closing review is a `Workflow` script
running primed finder lenses into batched skeptics, and it was not run. What follows is a
single-reviewer pass over the cumulative diff, lensed by the six bug classes
`gotchas.py --for-diff` selected for this range. It is weaker than the specified review in exactly
the way one reviewer is weaker than an adversarial panel, and the Definition of Done is therefore
**not** met on the `diff-reviewed` directive. Treat this verdict as a self-review, not as
independent confirmation.

## Scope

Base `da9e4cd2` (`origin/main`, pinned as an immutable sha) to the branch tip, three-dot, so the
83 commits of main drift the merge brought in are outside the diff. 58 files; roughly two thousand
non-comment lines added to `tools/govkit/govkit.py` alone. The lenses were the checklist's:
`fixture-passes-by-finding-nothing`, `heredoc-escape-reaches-the-regex`,
`staged-break-substitutes-a-synthetic-value`, `two-answers-to-one-question`,
`armed-but-unreachable-rule`, `subprocess-resolves-a-different-shell`.

## Findings, all confirmed and all fixed in the diff

1. **`decline_findings` collapsed two different questions onto one field, and redded an operator for
   narrowing a selection.** A `[[decline]]` naming a kit outside the run's `--kits` was treated as
   stale and failed the run. A kit outside the REGISTRY is stale — nothing ships it, so the row
   excuses a gap that cannot exist. A kit inside the registry but outside this run's selection is
   simply not this run's business. Split into two branches; the second announces itself rather than
   dropping the row, because a decline that vanishes without saying why is the failure mode the whole
   unit is written against. Two arms added, over a genuine two-kit fixture.
2. **The arm written for finding 1 passed vacuously.** Its "sibling" gov was built from the same
   single-kit template, so `--kits demo` selected the only kit there was, the branch never ran, and
   the arm passed on the exit code alone. `fixture-passes-by-finding-nothing`, inside an arm written
   for a review finding. Rebuilt as a real two-kit registry with a liveness precondition asserting
   the fixture carries a decline for an unselected kit.
3. **`silenced_legs`'s finding suppressed the manifest write for EVERY leg** (found during the build
   of `-6`, recorded in its ledger and repeated here because it is the most dangerous shape in the
   diff). The write-back is guarded on the report being clean, so one defective leg silently took
   the healthy ones with it — the install "stood" while the target's runner stayed empty, which is
   the opposite of what the scope item says. Findings are raised after the write-back now.
4. **The `-14` AC8 arm was pinned to `HEAD`** and had gone vacuous the moment `-14` landed. Repinned
   to an immutable sha with the reason beside it. Not this build's unit, found while running its
   suite.
5. **`EVIDENCE_STATES` was declared and read by nothing** — the four states' real home was the
   branches that assign the field, and the constant would have drifted beside them saying nothing.
   Joined to both the values a real run writes and every literal the engine can assign, with a
   liveness arm so the membership assertions cannot pass over an empty set.

## Classes swept and found clean

- **`heredoc-escape-reaches-the-regex`** — the class was HIT during authoring, in a bash heredoc that
  turned `\n` into a newline inside a Python match string; recovered by writing through the editor
  instead. No committed regex or match string is authored through a shell heredoc. The one heredoc
  that ships, in `check-install-prefix.sh`, is single-quoted and expands nothing.
- **`subprocess-resolves-a-different-shell`** — every new spawn is a literal `git` argv or goes
  through `resolve_shell_argv`; the govkit selftest arm over this file's source still holds. The one
  new shell-side launcher resolution goes through `tools/lib/resolve-python.sh` and has NO fallback,
  which the repo's own idiom ban enforced during the build.
- **`staged-break-substitutes-a-synthetic-value`** — every RED in this build was staged with the real
  value: the actual withdrawn leg block, a real kit-path literal, a real line edit inside the guarded
  block. None substituted a simpler stand-in.
- **`two-answers-to-one-question`** — one net removal (`render_doc`'s second spelling), one net
  removal (the module docstring's verb COUNT), one avoided (`coverage_rows` memoises the plan rather
  than re-walking it), one gated (the carried-prefix artifact and `--list` emit from one function).

## What this review did NOT look at, said plainly

- The 83 commits of `main` the merge brought in. They are outside the three-dot diff by construction,
  and they landed through their own reviews.
- Whether the five units' DESIGNS are right. That is the spec audit, and the spec set converged at
  round 6 before this session began; nothing here re-opened it.
- Anything an independent skeptic would have found that one reviewer reading their own diff would
  not. That is the gap named at the top, and it is the reason this verdict is `CLEAN WITH FIXES`
  rather than `CLEAN`.

## One thing worth an owner's eye, not a blocker

`adopt` does not refuse a target that is mid-merge. It writes no bytes into the working tree, so the
staging hazard `-12`'s preconditions exist for does not arise — but `index_read` returns only stage-0
entries, so an unmerged path gets no row at all and the receipt silently describes a smaller tree
than the target has. Not destructive: such a file is simply unmanaged until a `--re-adopt`. Recorded
here rather than fixed, because adding a fourth refusal to a scope item that ratified three is a spec
decision.
