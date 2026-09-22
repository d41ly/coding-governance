**Serves:** journal TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

# The round-8 fold — where round 7's own fixes were incomplete

Node `d`, 2026-08-24. Round 8 read the fold of round 7 and nothing else: one commit, `0a80f7bb`, over
round 7's recorded tip. **BLOCKED** — raw 20, confirmed 16, refuted 4, precision 0.80, collapsing to
ten distinct defects: two blockers, two highs, six lows.

**The governing observation, and it is the one to carry forward: round 7's fixes were right about the
mechanism and incomplete about the class, and two of them opened a new hole on the way through.**

## The two that were regressions, not residue

**`_conf_key` traded a parse defect for a liveness one.** Round 7's blocker 3 was a conf key resolved
by `sed | tr -d '"' | head -1` while every sibling sourced the file. The fix sourced it — and then
could not tell "the key is undeclared" from "the file aborted above the assignment". Four of five
abort shapes reach it, each a one-line append to a tracked file the graded run can commit itself, and
the leg then printed `bypass scan SKIPPED - no BYPASS_BAN declared` about a conf that declares it.
The arming `case` added in the same fold fires only on a NON-EMPTY value, so the one resolution that
turns the check off is precisely the state it exempts.

Worse, the sibling leg sources the same file in its MAIN shell: `exit 0` ended that leg at status 0
and `run-gates` read `GATE ok`, with every check unrun. Observed: pre-fold rc 0 with zero output.

**The first repair did not work either, and the reason is worth the sentence.** `. file || exit 9`
cannot catch an `exit` INSIDE the sourced file — the subshell ends at the status the file chose, so
`exit 0` still reads as a clean source. What works is a sentinel the source has to survive to print,
plus a cross-check against the file's own text for the `return 0` shape, which ends the source without
ending the subshell. Both legs carry that now, and the sibling leg STOPS on it rather than falling
through to the source that would end it.

**The class fix closed word-splitting and left C-quoting.** Round 7's high 1 converted five
enumerations from `for x in $(GITLS …)` to split-safe readers. With the default `core.quotePath`,
`git ls-files` emits a non-ASCII name as a quoted, octal-escaped literal — so the reader still gets a
path that does not exist. Four consequences at once: the flag in such a record is never read; the
tracked-but-absent refusal reds a legitimate tree with a false cause; the liveness counter now
DEFLATES, the opposite direction from the one round 7 fixed; and the census silently grades the piece
unrecorded. `GITLS` is `git -c core.quotePath=false ls-files -z` now, and **a NUL stream cannot ride a
heredoc** — command substitution strips NUL bytes, with a warning — so every consumer reads from a
process substitution, which is also the only form that keeps the loop in the current shell.

## The two highs, both of them "the gate can only fail in its own fixture"

The zero-teeth refusal round 7 added keyed on the repo-wide counter. The kit ships its fixture to
every adopter and check 1 reds on an empty playbook population, so that counter is effectively never
zero: the only tree where the refusal could fire was one that repointed the fixture's own root — which
is exactly what round 7's arm did. It is per-root now, and its arm is a SECOND playbook beside a full
fixture, which is the shape the comment always described.

And the sixth enumeration was never converted, in a fold whose own comment claimed the class covered
"every place this leg walks git ls-files output". It is the playbook population loop — the one whose
failure means a real playbook is never graded at all, and whose `BYPASS_ROOTS` then drops to zero,
disarming the guard added in the same fold.

## What was observed, per arm

Eleven arms added. **Ten of them observed RED against the pre-round-8 code and green against this
one**, in one control run each. The eleventh — the sibling leg's `exit 0` arm — was verified with a
hermetic probe instead, because its suite is the one the owner stopped: pre-fold **rc 0, zero output**,
post-fold **rc 1** with the refusal.

`check-playbook.test.sh` is at **120 assertions**, from 107 at the end of round 7.

## The lows, and one of them is about a test

- `_pbatch`'s empty-reply fill spells the batch's own rc, and `bash -c` exits **2** on a syntax error —
  which is exactly the value the multi-line refusal arm asserts. A harness that ran nothing reported a
  correct refusal. A `_PB_DEAD` flag now carries the fact the fill cannot express.
- `BYPASS_ROOTS` counted playbooks that declare a root rather than distinct roots.
- The `--help` budget was derived but summed a hand-typed list of five identifiers out of eight; it
  sums `${!BUDGET_@}` now, and the neighbouring `--checks` wall figure was dropped rather than typed.
- Moving check 10 left its whole header comment above an unrelated sweep.
- **The round-7 LOW-3 drift arm passed identically with its own fix reverted.** Both fixture builds
  named only their own token, so the merged-by-mistake spec set produced the same row count as the
  correct grouping and only the sibling assertion discriminated. The tokens cross now: build `one`'s
  README names `--two-flag`, so a slug collapse yields three rows where correct grouping yields two.
  Verified by reverting the two folded lines — both assertions red.

## What this fold did NOT close, said plainly

- **The newline-in-a-filename half of blocker 2 is unarmed.** This node's filesystem refuses to create
  such a name, so the arm cannot exist here. The `-z` in `GITLS` is there for it and is unexercised.
- **LOW 4 of round 7 — the blind-blame liveness arm — is still owed**, for the reason recorded in that
  unit's spec: the only reproducing route is an unborn HEAD, and the report refuses to run at all on a
  repo with no commits.
- **The gate selftest suite has still not been run end to end.** The arms added to it were verified
  standalone against hermetic probes built from its own setup.

## The pattern, stated because eight rounds is now evidence rather than anecdote

Every round of this build has returned BLOCKED, and rounds 4 through 8 each found defects that the
PREVIOUS round's fold introduced or left half-closed. The severity is falling — round 7's blockers
were reachable by ordinary edits, round 8's need a hostile conf line or a non-Latin filename — but the
loop has not terminated on its own. That is a fact for whoever decides whether round 9 runs, and it is
not a decision this record makes.
