**Serves:** journal TOOL-aGraftedHelix-39

# Spec brief — TOOL-aGraftedHelix-39, adopted at VERIFYING

Tier-2, streams tooling, `order 23`. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states the twelve invariants that bind it.
In your OWN return, name the spec you author in `authored` by its unit id, `TOOL-aGraftedHelix-39`,
never by its path.

## What was observed

Unit 38's builder reported this, unconfirmed: a second `unattended.sh --dispatch` for the same open
pass, naming only NEW `--writes` paths, left that pass's earlier-declared paths outside the set its
next commit was graded against. The verb printed nothing to say so, and the builder re-declared the
full set by hand to get the commit through. The contract contradicts the report:
`memory/guides/UNATTENDED-VERBS.md`'s `--dispatch` entry says a declaration is APPEND-ONLY, that a
re-declaration is accepted "wider, NARROWER, or disjoint", and that "both rows stand".
`--check-commit` grades staged paths against "that pass's declarations". The driver's pass-open logic
(`unattended.sh` near the `THE LAST ROW CARRYING THIS SET` comment) reads the last row in places and
`--audit`'s union of same-anchor rows in others. The report may be a real divergence, or a misreading
of a refusal with another cause.

## What to decide

**Reproduce first**, in a fixture run-state file:

1. Dispatch a pass with paths A and B.
2. Commit under `Pass:` touching A.
3. Re-dispatch the same pass with only C.
4. Stage a change to B and run `--check-commit`.

Record what it prints and its exit code, and do the same for a re-dispatch made at the SAME anchor
and at a later one.

**If it reproduces**, the defect is the gap between the contract and every reader of a pass's
declarations. Make every reader answer "which paths may this pass write" from ONE derivation that
honours the contract, under the class `two-guards-one-question-two-answers`, and make `--dispatch`'s
own output state the effective set after the call.

**If it does not reproduce**, say so in §4 with what was tried. Then find what refused the builder's
commit, from its pass's rows in `memory/builds/aGraftedHelix/RUN.md` (unit 38, the dispatch rows
after `7db5d7a8`) and the refusal text the verbs print. Fix whichever message misled it, so the
refusal names its real cause.

Either way, the arm runs the four steps above, and it fails on the build's parent.
