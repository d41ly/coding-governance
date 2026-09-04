**Serves:** diff-review DEPL-dRatifiedSeam-1 TOOL-dRatifiedSeam-1

# Closing diff review — dRatifiedSeam

Tier-2 · node d · 2026-09-03 · subject: the cumulative diff `a69e57d7...HEAD`, four code files
(`tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/workflows/unattended-build.js`,
`tools/workflows/unattended-build.test.sh`)

## Verdict: CLEAN WITH FIXES

Sixteen findings across two reviewers, **two of them blockers that invalidated what this run had
already reported as built**. Eleven are fixed in this build; four are filed as
`DEPL-dRatifiedSeam-2` through `-5`; one is REJECTED with its reason. The verdict grades the exit
state, and the exit state is clean — but the entry state was a unit that did not work and a landing
that could write outside the adopter's repository.

## Shape

Two independent cold agents rather than a workflow fan. That was not a preference: an earlier M4
audit on this same build lost five lenses twice to server 529s, because a fan discards every
sibling when one dies and returns `findings: []` — indistinguishable from a clean pass. Independent
agents each keep their own result.

One hunted correctness across all four files. One did nothing but ask whether the relaxation had
opened a path to destroying an adopter's work, with the specific attacks named: `..` escapes,
absolute destinations, symlinks, case-insensitive collisions, staged leftovers, and whether the
landing could fire read-only. Splitting that question out is why it was answered properly.

## The two blockers

**`TOOL-dRatifiedSeam-1` did not work, and this run reported it as built.** `tier2-review.js` has
never returned a `verdict` key — its returns carry `blockers`, `report`, `highs`, `precision`. So
the adapter's `auRaw.verdict` was undefined, its own throw fired on every real invocation, and BUILD
was still unreachable. The failure had moved from an agent that refuses to a script that throws.

**The 28-arm suite was green because the double returned a shape the callee never produces.** The
fixture invented `verdict` and `reportPath`. The harness and its callee had never met. This is the
fixture-grading-the-fixture class, written by me, inside the unit whose subject is an unreachable
stage.

Rebuilt three ways, each part where its capability lives: the SCRIPT holds `Workflow` and calls the
review; an AGENT holds a shell and records the round; the DRIVER owns the
`CONVERGING|CONVERGED|NON-CONVERGENT|CEILING` vocabulary, because convergence is a property of the
SEQUENCE of rounds and no JS can compute it. Two further defects surfaced inside that rebuild: the
`--review` call had been deleted with the old agent and nothing replaced it, so **no round was
recorded at all**; and `AUDIT_SCHEMA`'s enum was silently lost, so `"ok"` would have passed the
verdict check and fallen through to BUILD.

## The safety findings, four reproduced end to end

`update` writes into a repository gov does not own. The landing block had no containment check at
all, where every other destination producer in the engine has one:

- `prefix = "../ESCAPED"` landed four files in a SIBLING directory of the target, at exit 0, while
  `plan` refuses the identical configuration. An absolute `C:/…` prefix worked too.
- A **dangling symlink** defeated the occupancy refusal: `.exists()` follows links, so it read
  absent and `write_bytes` landed the bytes at the link target, outside the tree — with a sane
  prefix and no tampering. A string-normalised containment check would have missed this; `resolve()`
  catches both.
- A per-entry `kit = ".git/hooks"` token landed an executable the adopter's next commit runs.
- An ordinary `.gitignore` minted a receipt row for a file git never tracked, and every LATER
  `update` then refused the install forever, blaming the operator.
- `--kits` did not bind the landing loop, so a scoped run landed sources for excluded kits —
  including a rename destination, leaving two copies of one gov source.
- An `OSError` escaped as a traceback, leaving files staged in the adopter's index with no receipt.
- It landed rules `apply` deliberately skips: unresolved tokens, machine scope, link. A literal
  `{docs_home}` directory was created and staged.

## What the reviewers found in my own arms

Three separate instances of grading a copy instead of the subject, two of them in arms written to
prevent exactly that:

- the S4 removal arm compared the fallen count in the TEST — a tautology, since one fewer than a
  number is never at least that number.
- the S4 LIVENESS arm built a SECOND copy of the truth table and asserted `len({True, False}) == 2`,
  a constant. Deleting a row from the real table left it green.
- the harness double, above.

That is the dominant failure mode of this work, not an incident.

## The rejected finding

`set(before) <= set(after)` was proposed for the count-versus-set gap. The gap is real: since the
relaxation, deleting one tracked file and landing another satisfies `after >= before`. But a RENAME
legitimately removes the old path and the `[-11]` fixture renames, so the assertion reds on correct
behaviour — measured, on `tools/demo/content.txt`. Filed as `DEPL-dRatifiedSeam-4` instead. An
assertion that fires on legal work is worse than the gap it closes, because it teaches everyone to
ignore the arm.

## The mutation controls, including the one that was wrong

Every fix was mutation-tested. Twice the MUTATION was wrong rather than the arm: `>` to `>=` does
not make a drop look like a rise, and removing one False row from a two-False table does not lose a
direction. A control that cannot fail proves as little as a check that cannot, and noticing that is
the only reason those two arms are trusted now.

## Residue

Four findings filed rather than built, the largest being that landed files sit outside the
verify/rollback pass. Fixing it moves a write into the machinery that guards against data loss in a
foreign repository, which deserves its own unit and its own review rather than a fold at the end of
a build that has already absorbed two blockers.

The M4 spec audit for this build remains SELF-review; the cold pass on the specs is still unpaid.

## A seventeenth finding, from the closing bar itself

The total bar (`GATE_FULL=1 GATE_SELFTESTS=1`) was run at the `--no-ff` merge commit before the
push, which is where the merge protocol asks for it. It came back 92/93 with the `govkit selftest`
leg red on 46 arms, every one of them an `update` arm.

None of them was about the tree. `update` defaults to `--to HEAD`, and `demand_published_vintage`
refuses a commit this checkout can reach from NO ref. A `--no-ff` merge made on a detached head is
exactly that commit, so the leg refused the vintage rather than grading anything. Measured both
ways: `git for-each-ref --contains` returns nothing for the merge commit and returns its own branch
ref for the branch tip, and the same suite over the byte-identical branch-tip tree passed all 1074
arms.

So the leg's verdict is decided by commit topology rather than by the content under test, and it
reds precisely at the moment the merge protocol says to run a gate. Filed as
`DEPL-dRatifiedSeam-6`. It is not folded here because the fix belongs in the leg or in how the
fixture pins its gov vintage, not in this build's diff — and a leg that reds for a reason unrelated
to its subject is the mirror image of one that greens for a reason unrelated to its subject, which
is the class this whole build has been chasing.
