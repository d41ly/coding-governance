**Serves:** journal TOOL-aGraftedHelix-29..32

# Spec brief — TOOL-aGraftedHelix-29 to -32, promoted by closing review round 1

The source of every unit here is the closing diff review's record,
`memory/builds/aGraftedHelix/reviews/2026-10-05-review-TOOL-aGraftedHelix-1-closing-diff-round1.md`:
read the section each unit names WHOLE, including its Fix and Left-shift lines, which a skeptic judged
SOUND. The shared brief beside this file (`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`)
states twelve shared invariants; they bind these units too, except that its interface section
describes code as it was planned — read the CURRENT code, which has moved through 28 built units and
two reconciling merges with origin/main. The claim refusals are checks 107 to 111. No spec audit is
run (the opt-in is the owner's alone); the closing review of the rotated run is these specs' first
review, so write each to survive it.

The run was ROTATED: the previous record is `RUN.ABORTED.6410435d.md`, and the live one was
re-preflighted onto `018b5675`. Spec `order` values: 29 is 13, 30 is 14, 31 is 15, 32 is 16.

## TOOL-aGraftedHelix-29 — Tier-2 — H1 (finding id 1)

The by-design block the review harness hands every lens and skeptic is rendered from the invariant
records in the tree UNDER review, so a diff that adds or edits a `kind: invariant` record writes its
own review exemption — this round's three entries were all added by the range. Render the by-design
block for `--for-diff <base>..<head>` from the invariant records as they stood at `<base>`: an
invariant the range adds or edits must not exempt anything in that range. Keep the class-item half of
the checklist reading the tree under review (a checklist item can only widen a review). State what
the change leaves open — the `--for-paths` spec-audit channel has no range to compare against — and
decide whether it is closed here or named as open.

## TOOL-aGraftedHelix-30 — Tier-2 — H2 (finding id 20), the left-shift

This run had to be rotated because a reconciling merge brought in a new authorization rule
(check 89) that refused the run's own record at `--close`, where `authorization-reachable` takes no
override and the BASE blob cannot change. The defect is the TIMING: nothing evaluated the
authorization predicate against the merged driver until `--close`. Give the driver a way to evaluate
`authorization-reachable` (the same predicate `--close` runs, never a copy) without closing, and make
the reconciling path run it: the lander's `--prepare` merge, and the protocol's instruction for a
mid-run `git merge <remote>/<default>`. A refusal there must name the exits (rotation, hand-off) the
review lists. Record in a gotcha or invariant the class "a reconciling merge brings in a check the
running record cannot satisfy", unless a gate covers it.

## TOOL-aGraftedHelix-31 — Tier-2 — H3 (finding id 21)

`--settle`, merged in from dUnstuckLanding, never writes the run claim, so a settled hand-off stays
`held` on the remote for good and the next run of the slug is refused at check 107. Apply the review's
fix (the status-write block `--landed` uses, `landed` on the handed branch, `aborted` on the
lease-dead branch), add `--settle` to STOPS §7's status-write list, and build the left-shift: a class
gate in the unattended suite that enumerates every function writing a terminal phase and asserts each
also writes the claim or sits on a named exemption list, so the next terminal writer reds until it
says which.

## TOOL-aGraftedHelix-32 — Tier-2 — the 21 minors, batched (M1-M9, L1-L4)

One unit by the owner's promote-every-finding ruling: MEDIUMs M1 to M9 and LOWs L1 to L4, each fixed
as its section's Fix line states, each left-shifted as its Left-shift line states. Several share a
defect at two grades (M8 with L1, M9 with L2): fix the defect once and say both ids. Where a fix lands
in a file another unit of this batch also writes, sequence them inside the unit. Plus one
OBSERVATION from the rotation, to reproduce before fixing: the first `--preflight` after the abort
printed `--preflight refused; the run-state file is unchanged` while it had already retired the
ABORTED record to its archive name and written a new RUN.md, both staged; its output was not
captured, and an immediate retry from a reset tree succeeded. Try to reproduce it in a fixture
(a retired record plus a refusal after the rotation); if it reproduces, it is the
destructive-step-before-its-precondition class and the fix orders the rotation after every refusal;
if it does not, say so in §4 with what was tried.
