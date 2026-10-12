# Acceptance ledger — the drift history is created with its header already in it

**Serves:** journal TOOL-aPairedSlots-11

Observed on node a on 2026-10-12. A harness loads the drift self-test from a kit directory and runs
its two-writers arm alone: the changed arm over the changed writer, then the changed arm over the
writer as it stood before this unit, then the previous arm over the previous writer.

**Evidences:** TOOL-aPairedSlots-11
- AC1 — `test_drift_history_two_writers` — over the changed writer, with the second writer run inside
  the first one's `os.link`, line 0 was the header and `read_history_groups` returned two groups and
  no skip reason: four checks, no failure. Over the previous writer the arm's interleaving never ran,
  since that writer publishes with no link, and the reader saw one group. The previous arm passed over
  the previous writer while counting header lines, which is how its layout went unseen.
- AC2 — `write_drift_history` — writing to an existing empty history, the changed writer put the
  header on line 0 and the row after it; the previous writer left the row with no header.
