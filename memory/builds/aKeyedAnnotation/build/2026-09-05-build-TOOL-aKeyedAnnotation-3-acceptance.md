<!-- **Serves:** journal TOOL-aKeyedAnnotation-3 -->
**Serves:** journal TOOL-aKeyedAnnotation-3

# aKeyedAnnotation unit 3 — acceptance ledger

**Evidences:** TOOL-aKeyedAnnotation-3

- AC1 — `python tools/drift-audit/drift_report.py --json` — the signal reports value 2 over a
  judgeable population of 400 cited ids, from 255 scanned source files against 108 anchored slugs,
  and the two are exactly the ids measured at this base. No fixture id among them.
- AC2 — `python tools/drift-audit/selftest.py` — both directions. A fabricated id planted under a
  slug that anchors a record raises the count by one; the same shape under a slug that anchors none
  does not move it. One half alone would pass for a signal that counts everything, the other for one
  that counts nothing.
- AC3 — `python tools/drift-audit/selftest.py` — a scratch tree whose memory root is emptied reports
  the signal DEAD with a zero slug count, rather than zero findings.
- AC4 — AMENDED, and the amendment is in the arm rather than the criterion. Declaring a family enum
  can only NARROW, because with none declared the engine falls back to a permissive family pattern.
  The arm was first written to declare a family and expect the count to RISE, which would have passed
  against an engine ignoring the conf entirely. It now runs narrow-then-wide: with `TOOL` alone the
  foreign id is invisible, and declaring the foreign family raises the count by exactly one.
- AC5 — `python tools/memory-tree/corpus_ids.py --report` — orphan count 0, unchanged from this
  base, proving the memory-side check was not widened.
- AC6 — deferred to the closing bar, which is where a full-bar criterion binds. The diff-scoped gates
  were green at this unit's commit.
- AC5b — AMENDED rev-4 — the criterion asked for a scratch tree where the source walk resolves to no
  tracked file, and that state is UNREACHABLE: this report is itself a tracked non-memory file, so a
  tree with the kit installed always has source to scan. Found by writing the arm and watching it
  refuse to go dead. The population that can actually collapse is the CITED set, so the arm binds the
  grammar to a family nothing uses and asserts the signal reports DEAD with a zero cited count while
  the scanned-file count stays non-zero. §2 S3 records the correction.
- AC5c — `python tools/drift-audit/selftest.py` — the fixture installs drift-audit with no recall kit
  beside it and blank pins, which is the adopter configuration this kit's own descriptor permits. The
  report RETURNS and the signal answers; it does not raise and does not take the other signals with
  it. Every arm in this suite runs in that configuration, so it is the default rather than a special
  case.
- AC5d — `python tools/drift-audit/drift_report.py --check --base-ref HEAD` — raising the pin from 2
  to 3 with no marker REDS, naming both values and the window; adding a `2 -> 3` marker within that
  window clears it. Observed both ways, then reverted.

## What the criterion for the ratchet does not say, and now does

The first attempt at AC5d ran `--check` on this branch and got exit 0 both ways, which looks exactly
like a ratchet that does not work. It is not: the ratchet compares the working value against the
value at the BASE ref and skips any key the base does not carry. A pin is therefore UNRATCHETED on
the branch that introduces it and binds from the next one onward. The criterion now states that
condition, because the obvious way to observe it passes green and reads as a broken mechanism.
