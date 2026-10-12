# Acceptance ledger — the two-bar check's overlap guard reads the admitted slots

**Serves:** journal TOOL-aPairedSlots-14

Observed on node a on 2026-10-12. A script sources the changed check and feeds `check_overlap`
fixture run records; the guard it replaces, copied from the check as it stood, read a fixture
`check.tsv`. A real pair run at one slot, the staged red the review suggested, was not run: it costs two
full bars, about three hours on node a, and the spec states the skip.

**Evidences:** TOOL-aPairedSlots-14
- AC1 — `check_overlap` — records holding slots 1 and 2, each admitted before the other ended, passed
  with exit 0. Slots 1 and 1, slots 1 and 2 with the second admitted after the first ended, and a
  record with no `slot` key each failed with exit 1 and a line naming why. The replaced guard accepted
  a serialized pair whose two bars were started together.
