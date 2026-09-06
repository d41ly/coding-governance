# Acceptance ledger — TOOL-aHonedRuleset-3

**Serves:** journal TOOL-aHonedRuleset-3

Tier-2 · node a · 2026-09-06

The kickoff engine's six interactive exits moved verbatim into
`tools/unattended/PROTOCOL.template.md` as a new §13, the engine kept a short pointer, and check 12's
exit-count arm was repointed to count in the INSTALLED protocol rather than in the engine. The floor
follows its subject.

## Acceptance criteria

**Evidences:** TOOL-aHonedRuleset-3

- AC1 — MET — `grep -cE '^[0-9]+\. \*\*Step '` returns **6** over
  `tools/unattended/PROTOCOL.template.md` and **0** over `skills/session-kickoff/SKILL.md`
- AC2 — MET — the engine measures 16998 / 18432, **1434 bytes under**, against a floor of 1200 and
  the 207 measured at base. The first pointer draft came in at 84 bytes of recovery against AC2's
  90-byte sibling floor in `TOOL-aHonedRuleset-5`; the pointer was tightened rather than the
  criterion moved
- AC3 — MET — `bash tools/memory-tree/check-memory-hygiene.sh --staged` exits 0, so the rendered
  protocol is inside `GUIDE_CAP_BYTES` and `GUIDE_CAP_LINES`
- AC4 — MET — `bash tools/unattended/check-unattended.sh` exits 0 with the new section and the
  rewritten `KICKOFF_EXITS` row present
- AC5 — MET, **observed RED before the arm was trusted.** With one numbered exit deleted from BOTH
  protocol copies, the gate exits 1 printing
  `5 against 6 in memory/guides/UNATTENDED-PROTOCOL.md` — the new message, naming the document it now
  reads rather than the engine. Restored, and the leg returns to exit 0
- AC6 — MET — `check-arms.py --report` shows check 12 branches 2 and 3 (the Step 5b heading and the
  READY prompt string) still ARMED, so moving the count disarmed neither
- AC7 — **SPLIT at rev-7; one half MET, one half WAIVED with evidence.** MET:
  `python3 tools/memory-tree/check-arms.py --check` exits 0 with check 12 branch 4 reported ARMED.
  WAIVED: `check-unattended.test.sh` fails 26 arms and did so BEFORE this unit existed — the fixture
  seds for `Ten kit-owned core items` against a protocol saying `Twelve` (0 hits at base `6ec402bd`),
  and its baseline conf declares no `DISPOSITION_CUTOFF`. Zero of the 26 touch check 12, the exit
  count, or any line this unit edits, grepped rather than assumed. Filed as `TOOL-aHonedRuleset-16`
- AC8 — MET — `grep -rn 'Step 5b exit' tools/ memory/guides/ .claude/` returns nothing outside build
  records
- AC9 — MET — `kit-dogfood-parity.test.sh` and `adopt-unattended.sh --check` both exit 0
- AC10 — MET — `bash tools/check-install-prefix.sh` reports `carried-prefix clean — 118 recorded
  file(s), 5 hand-justified, none rising`
- AC11 — MET — `check-template-size.sh` on the engine prints no `TEMPLATE-SIZE WARN` line. It briefly
  did after the closing review's F8 wording fix added 7 bytes; the high-water was re-bumped 16991 to
  16998 to match, the same act `TOOL-aHonedRuleset-5` S14 performs
- AC12 — MET — the Step 5b section greps 1 for `guides/UNATTENDED-PROTOCOL.md`, against 0 at base, so
  a build that deleted the block and left no pointer would fail this
- AC13 — MET — `grep -rn 'Step 5b says which one per exit'` returns nothing outside build records
- AC14 — MET, **widened to the CLASS at rev-5.** No `KICKOFF_EXITS` row in any of the three prose
  carriers still says the ENGINE enumerates, and `grep -c 'MEASURE it against your own engine'`
  returns 0. Round 1's fold had gated the one instance it named and left two carriers false
- AC15 — MET, **as a DELTA.** `git grep -l 'gov:kit unattended@'` over the three carrier trees counts
  14 before this unit's first edit and 14 after, with 0 answering to `1.17`. §8 F4 records why no
  bump is taken: the ruled version was already in the tree

## The fork building uncovered

S8 said the kit version moves 1.17 to 1.18. Measured, the tree was already at 1.18 —
`d19b4e40` moved it between this spec's base and this build's — so S8 had no work left and AC15, as
written, graded another build's work. §8 F4 resolves it (agent, delegated): the owner named 1.18 and
1.18 is what ships, so the ruling is satisfied; 1.19 was refused because three builds are in flight
against that constant and claiming an absolute would repeat the defect this run's own unit-8 audit
had blocked on one round earlier.
