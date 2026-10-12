# Acceptance ledger — the counting-semaphore turnstile

**Serves:** journal TOOL-aPairedSlots-2

Observed on node a on 2026-10-11. The turnstile suite's new arms 29 to 33 were sliced with the
suite's prologue and run over the changed runner: 14 assertions, PASS. Each mechanism was then
broken alone in a copy of the changed runner and its arm run again; each read RED.

**Evidences:** TOOL-aPairedSlots-2
- AC1 — `queued at position` — under `GATE_TURNSTILE_SLOTS=2` two bars in two repositories held at
  once (occupancy peak 2) and a third queued; with the claim limited to slot 1 the second bar held no
  slot (its header read slot `-`).
- AC2 — `2 of 2 bar slots on this host are held` — the third bar's queue line carried it with both
  holders' pids, its header recorded `slots` 2, and the holders' headers recorded `slot` 1 and 2;
  with the claim limited to slot 1 the line named one holder.
- AC3 — `reaping the beacon of a dead holder` — printed once for a planted dead slot 2 while slot 1's
  holder ran on with its nonce unchanged, and the bar behind it claimed and ran; with the reap limited
  to slot 1 the dead slot was never reaped.
- AC4 — `ts_release` — a run whose slot-2 nonce was replaced, as a successor's claim would replace it,
  left that directory in place on release, and slot 1's holder kept its own; with the release's nonce
  guard removed the successor's beacon was deleted.
- AC5 — `gate queue: nested under` — a runner started by the slot-2 holder's leg printed it; with
  nesting reading slot 1 only it did not nest.
- AC6 — `gate queue: acquired` — at the default count a fixture bar's stdout from the profile line
  to that line, and its header's key set, equalled the pre-unit runner's on the same fixture (4 lines,
  29 keys), and arm 33 found no slot key and no slots clause. Arms 1 to 28 run sliced at VERIFYING.
