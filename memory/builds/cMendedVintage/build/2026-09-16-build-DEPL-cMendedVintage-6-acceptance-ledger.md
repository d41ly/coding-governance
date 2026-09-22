# cMendedVintage — the acceptance ledger for unit 6

**Serves:** journal DEPL-cMendedVintage-6

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commits, `959cbc40` and the spec follow-up `0ddee337`,
both 2026-09-16. Two kinds of line follow and they are not the same evidence. Where a criterion is
answered by a file or a grep that could be taken from here, it was, against this worktree, and the
result is given. Where it is answered by a run against a scratch target at a foreign prefix, that
run exists only in the building pass's record and the commit is cited AS the record. No merge bar,
no `*.test.sh` and no self-test runner ran in this pass, and `check-playbook.sh` — a leg two of
these criteria name — was read, never executed.*

## The one thing worth reading twice

**The data loss was reproduced before it was closed, and that is the load-bearing observation
here.** Commit `959cbc40` records a plan at prefix `scripts` with the two `rendered` rules in place
and the `project-owned` claim deliberately absent: it printed BOTH spellings, gov's as a `write`
row. That is AC1's own Red-when observed true against the real engine, on the arrangement a reader
would most plausibly have shipped, and it is why the third rule exists at all. With the claim added
the same plan printed only the prefixed pair and gov's two copies as `ORDER [project-owned]`.

**AC5 was never observed, and the spec's revision log says so in its own words.** It needs a
receipt, and `apply` refuses the scratch install without `memory-tree` and `review-harness` beside
it, which is a three-kit setup rather than a check. Nobody has run the two-update sequence the
criterion describes. What stands in its place is an argument one level up from AC1, given below and
labelled as an argument.

**Evidences:** DEPL-cMendedVintage-6

- AC1 — `plan` — commit `959cbc40` records the run at prefix `scripts` both ways round: without the
  S3 claim, both spellings printed and gov's was a `write` row; with it, only the prefixed pair
  printed and gov's two copies came out as `ORDER [project-owned]`, the same shape this descriptor's
  withheld self-tests already print. The clause that was graded is rev-2's narrowed one — no `write`
  row whose basename opens with `tools~`, rather than no destination at all — because a
  `project-owned` row is marked ORDER by construction and `apply` writes neither. Rev-2 logs that
  narrowing, and it is a real weakening of the criterion: the original wording could not have been
  met by any design that withholds through a destination claim, which is the design S3 mandates.
  This pass did not stand up a foreign-prefix target, so the plan output itself is the commit's
  record; what was read here is the descriptor, whose two `rendered` rules carry
  `{prefix}~{kit_id}` in their `to` and whose `project-owned` rule names gov's two copies by their
  repo paths.
- AC2 — `bash tools/unattended/adopt-unattended.sh` — the first half is the commit's record: run at
  prefix `scripts`, it wrote both records at the derived name with `piece:` lines naming files that
  exist in that tree, reported as pieces 2, verified 2. The second half was taken here rather than
  borrowed. A grep for the loop's own `repathed fixture record` message over
  `tools/unattended/adopt-unattended.sh` returns nothing at exit 1 at this tip, and the block that
  replaced the loop renders both templates through the script's existing `render` function, refuses
  on an unfilled `{{KIT_DIR}}`, refuses a missing template rather than skipping it, and writes only
  when the bytes differ. The rename is deleted, not disabled — no path is left that moves a file
  over an adopter's copy.
- AC3 — `bash tools/unattended/check-playbook.sh` — the RED is the sharper half and is the commit's
  record: a template copied INTO `fixture-records/` reds this leg as an orphan record, which is
  exactly why the templates sit in the kit root, and the leg was clean again once it was removed.
  That commit does NOT name which tree that clean run was in, and this pass did not replay it, so
  the criterion's this-repo half rests on an unattributed sentence. Its scratch-target half is
  evidenced separately and quantitatively by the same commit's pieces 2, verified 2 at prefix
  `scripts`. What can be read here at this tip is the placement the criterion is really about: both
  templates are tracked in the kit root, and no template sits under `fixture-records/`, which holds
  the two piece-records and the run's own set file and nothing else.
- AC4 — `python tools/govkit/govkit.py selfcheck` — commit `959cbc40` records this and
  `python tools/check-kit-placeholders.py` clean, alongside `check-kit-versions.sh`,
  `check-install-prefix.sh` reporting `none rising`, and `adopt-unattended.sh --check`. Neither of
  the two commands this criterion names was re-run here; both are merge-bar legs and no leg ran in
  this pass. What was read instead is the pair the criterion's Red-when is about: each new
  `rendered` rule declares `placeholders = ["KIT_DIR"]`, and each template carries `{{KIT_DIR}}`
  twice, in its title line and in its `piece:` line, and carries no other token.
- AC5 — `update --write` — NOT OBSERVED, by the building pass or by this one. Spec rev-2 records the
  reason and this ledger does not improve on it: the criterion needs a receipt, and `apply` refuses
  the scratch install without `memory-tree` and `review-harness` beside it, which is a three-kit
  setup rather than a check. So nobody has run that verb twice in a row against a scratch target
  with `GOVKIT_RERENDER=1` exported, and nobody has seen the second run print no `missing` row for
  either record or compared the two files byte for byte across the runs. What IS established sits
  one level up in AC1, and the spec says so too: at a foreign prefix gov's spelling appears on no
  `write` row, so an update lands no file there for a rename to clobber, and the rename itself is
  gone from the adopter, which AC2 above takes at this tip. That is an argument from the mechanism,
  not the two-run observation this criterion asks for, and the difference is the whole reason for
  writing it down. It is owed.

## What this ledger does NOT claim

That the merge bar is green, or that any leg of it ran, in either pass. The section 7 names are
unobserved for this unit here: `govkit selfcheck`, `kit placeholders`, `playbook validity gate`,
`unattended kit gate`, `unattended skill wiring`, `kit version markers` and
`install-prefix (shipped surface)`. Four of them are cited above as commit records. This kit's own
self-tests are withheld from the bar by the 2026-08-23 owner ruling, which the spec's section 7
states itself, so no suite would have covered this change at the push boundary either.

That the churn was observed stopping at a real adopter. It was not. The spec's migration section
says the hand-renamed copies the two live adopters already hold are overwritten by this render on
their next run, and nothing in this tree measures whether they are. Its section 8 records the one
adopter-shaped thing that WAS measured, and it is a
negative: a `cp -r` copy-install reads no descriptor, so such a target receives gov's two records
beside the rendered pair and `check-playbook.sh` reports each as an orphan note. Measured at prefix
`scripts`, and reported rather than closed.

That S6's version bump is graded by any criterion. None covers it; `kit version markers` is the leg
that does. Read from here instead: `959cbc40` moves `KIT_UNATTENDED_VERSION` from 1.24 to 1.25, and
the two new templates carry `gov:kit unattended@1.25` as their first line — which is also the byte
rev-2 had to add to both records, and the reason section 3's unchanged-bytes non-goal was rescoped
to the body by `0ddee337`.

That `0ddee337` is graded by any criterion either. It edits one sentence of the spec's own non-goal
so that a rule stops returning two verdicts about which record bytes moved. It changes no behaviour
and no criterion covers it; it is named here so the unit's second commit is not silently absent
from its own record.
