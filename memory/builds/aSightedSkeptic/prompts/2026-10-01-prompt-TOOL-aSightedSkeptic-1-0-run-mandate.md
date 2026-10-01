# Run mandate — aSightedSkeptic

**Serves:** journal TOOL-aSightedSkeptic-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-01. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> Open a full build and fix all 7 of your impact findings. This should work universally for any repo
> governed.

## What "your 7 impact findings" referred to

The prompt is deictic. It names a numbered list the session had just shown the owner, in an analysis
of `tools/workflows/tier2-review.js` at `ef1dcdb6`. A later reader cannot see that turn, so the list
is restated here from that analysis, in its order:

1. **Proposed fixes are never verified.** A finder's `fix` reaches the synthesis and the fold, and no
   skeptic judges it. In the sampled fold rounds, 51% of confirmed findings were defects introduced
   by the previous round's fix.
2. **Skeptics work blind.** The verify prompt carries no `repo`, no range, no `context` and no
   by-design list, so a skeptic reads whatever checkout its working directory is, cannot tell a
   pre-existing defect from one the diff introduced, and is told "by-design" refutes without being
   shown what is.
3. **Finders get no intent.** The closing-review invocation passes no `context`, which defaults to
   "the cumulative diff landing on main"; no lens reads the specs or their acceptance criteria.
4. **The regressions lens never receives the checklist.** Its brief says to run "the PROJECT's"
   checklist and names no command, and the harness has no argument that could carry it. A 45-file
   range selects 52 of 91 classes, too many for one agent.
5. **The lens set does not match the defects found.** Checks that cannot fail are 13–19% of sampled
   findings and no brief names them; the security brief is web-app shaped; one lens slot is unused.
6. **Severity has no definition.** Finders choose it freely, a skeptic can only confirm or refute, and
   a BLOCKER or HIGH drives the most expensive disposition.
7. **Intensity is fixed.** Every diff gets every lens; low precision clusters on small or hardened
   diffs and the harness has no light mode.

The analysis also named a measurement gap that sits outside the seven: the lens label is dropped at
the merge, refuted findings never reach the record, the success return carries a count rather than
the confirmed set, and recall is never measured.

## The one owner turn, and its answers

Asked once, before anything was written. Answers, verbatim labels:

- **Scope beyond the seven:** "Include + replay benchmark" — the measurement half AND a unit that
  replays a review shape over past pre-fix diffs and scores recall against their known findings.
- **Lens set for finding 5:** "5 lenses" — security rewritten surface-generic, correctness, seams,
  verification, intent; `regressions` retired and the checklist split across the five.
- **Spec audit before code:** "No, closing review only".

## What "universally for any repo governed" is read as

Every change lands in the shipped kit source — the review harness TEMPLATE and the render beside it —
and assumes nothing about an adopter beyond what the harness already requires: no path into another
kit, no memory-tree layout, no gotchas checker. Whatever a project-specific input is (its specs, its
bug-class checklist, its lens notes), it reaches the harness as a Workflow `args` field the caller
supplies, and its absence is announced rather than defaulted into silence.
