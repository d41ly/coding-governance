# TOOL-aRoutedQuill-11 — spec brief

**Serves:** journal TOOL-aRoutedQuill-11

node a · 2026-10-10 · authored by the run's main loop. A unit the closing review promoted.

- **Source.** H2 in `reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md` (the same defect as M2, ids 16 and 24; finding 16's proposed fix was
  judged UNSOUND, use the skeptic's corrected one). `check_routed` in `tools/check-wiring.sh`
  reads `${MEMORY_ROOT:-memory}`, while the gate's `checkUnarmed` in `tools/hooks/scratch-guard.js`
  treats an absent MEMORY_ROOT as unarmed and refuses every write. check-wiring prints `ok routed`
  for a conf the gate refuses.
- **Mechanism, one.** One reader: check-wiring takes the armed-or-unarmed verdict from the gate's own
  `readConfKey`/`checkUnarmed` (for example `node -e` requiring scratch-guard.js), and prints the
  gate's own reason; a parity arm feeds one set of confs to both and asserts they agree.
- **Out.** M4 and L2 (check-wiring's "any scratch-guard group" reading and its no-conf wording) stay
  in the minors batch, TOOL-aRoutedQuill-12, built after this unit.
- **Tier.** Tier-2: a shipped checker's verdict changes.
- **Order 9.** After TOOL-aRoutedQuill-10.
