# Acceptance ledger — the order-1 units: the slots knob, the backstop arm, the procmon fixture

**Serves:** journal TOOL-aPairedSlots-1 TOOL-aPairedSlots-6 TOOL-aPairedSlots-8

Observed on node a on 2026-10-11, each on a scratch fixture or a slice, each failing case staged
first. The suites the units extend run sliced again at VERIFYING.

**Evidences:** TOOL-aPairedSlots-1
- AC1 — `slots=3` — a fixture row declaring `slots=3` printed a `slots` line reading 3 and a row
  declaring none read 1; the base runner refused the same row with "unknown knob key 'slots' (known:
  width timeout wall mempause)".
- AC2 — `GATE_TURNSTILE_SLOTS=2` — over a row declaring none the profile printed 2; `abc` left the
  row's 3 and printed one NOTE; the base runner printed no `slots` line at all.
- AC3 — `gate profile:` — at the value 1 the profile line was byte-identical to the base runner's on
  the same fixture; at 2 and 3 it carried `, slots <n>`; a copy printing the field unconditionally
  differed from base.
- AC5 — `check_knob_classes` — sliced out of the pre-push hook's self-test over the changed runner it
  printed nothing; with the base class list it printed `unclassified-or-twice GATE_TURNSTILE_SLOTS (0)`.

**Evidences:** TOOL-aPairedSlots-6
- AC1 — `parse_gate_profile` — sliced, over the real runner's profile, now printing `slots 1`, and
  over a stub printing `slots 2`, it set wall, queue and ceiling_max with nothing missing; a copy that
  refuses an unknown key returned 1 naming `slots`.

**Evidences:** TOOL-aPairedSlots-8
- AC1 — `procmon-stamp` — sliced at the session seam while a loop wrote and cleared the real common
  dir's `procmon-stamp` every 0.1 s: the original arms read 10 passed, 1 failed
  (`test_broken_monitor_names_the_failure` got silence), the changed arms 11 passed, 0 failed.
- AC2 — `grep -nF '"$GD/procmon-stamp"'` — over the changed suite it printed nothing; over the
  original it named seven lines.
