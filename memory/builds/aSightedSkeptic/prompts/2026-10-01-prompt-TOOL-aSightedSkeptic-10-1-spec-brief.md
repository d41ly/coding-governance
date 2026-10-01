**Serves:** journal TOOL-aSightedSkeptic-10

# Spec brief — TOOL-aSightedSkeptic-10, promoted from the closing review

Read first: the closing review record
`memory/builds/aSightedSkeptic/reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md`,
sections H1 and H2, and the shared spec brief beside this file
(`2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md`), whose invariants still bind.

The round CONVERGED with zero blockers and two HIGH findings, and the build method promotes every
HIGH to a unit whose mechanism closes it. Both are the same class: a spec S-line says a behaviour is
"Observed by ACn", the arm that AC names never exercises it, and staged breaks of the behaviour stay
green at 165 passed, 0 failed.

- **H1 (finding 13).** The synthesis-death and deferred-path `  CONFIRMED [` log lines carry
  `renderFixLine` (spec 2 S6) and the binding grade (spec 6 S9). No arm reads those log lines.
- **H2 (finding 14).** Spec 6 S8 keeps the uncertain count apart from the no-verdict count in the
  success `note`, the RUN INTEGRITY clause and the WARNING lines. The AC5 arm reads none of them, and
  no arm runs an all-uncertain round.

ONE unit, one mechanism: arms in `tools/workflows/tier2-review.test.sh` that discharge both claims,
each OBSERVED red by staging the break the review names (the review gives the exact breaks), with
`FLOOR_ASSERTIONS` raised by the count added. Plus the class's left-shift, which the build method
requires and which no cheap gate gives: a `memory/gotchas/` record for "an Observed-by claim no arm
discharges", with the anchors `gotchas.py` selects by, so the next spec that cites an AC for a
separately rendered surface is handed the class. Read two existing gotcha records first for the
shape; the memory-tree kit README states the record grammar.

No template change: the behaviour is correct today. If staging a break shows the template is in fact
wrong, that is a finding for the spec's §8, not a silent fix.

§6 witnesses: the named arms of the self-test, read at VERIFYING; the gotcha record by
`python tools/memory-tree/gotchas.py --for-paths tools/workflows/tier2-review.test.sh` selecting it;
the memory hygiene leg for the record's shape. The order verb is `order 10`.
