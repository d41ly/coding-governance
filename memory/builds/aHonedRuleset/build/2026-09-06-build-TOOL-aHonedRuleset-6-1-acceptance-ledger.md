# Acceptance ledger — TOOL-aHonedRuleset-6

**Serves:** journal TOOL-aHonedRuleset-6

Tier-2 · node a · 2026-09-06

`tools/memory-tree/BUILD-METHOD.template.md` declared a byte and line budget for itself, said in the
same passage that no gate enforced the pair, and sat 12 bytes under the byte half. The owner ruled
option (b) on 2026-09-04: delete the claim rather than make it enforceable. The passage went, the
guide was re-rendered through the kit's own render path, and a second commit removed the two
sentences elsewhere in the file that only made sense while the budget stood.

## Acceptance criteria

**Evidences:** TOOL-aHonedRuleset-6

- AC1 — MET — `grep -c 'BUILD-METHOD.template.md' tools/template-size-limits.txt` returns 0 and the
  same grep over `tools/gate-legs.json` returns 0. Asserted rather than assumed, because the
  ruling's whole product is that nothing measures this file
- AC2 — **NAMED SKIP**, witnessed by `tools/gate-legs.json`. This unit adds no gate, so §7's
  stage-the-break rule has no subject and no RED is owed. The witness that nothing was added:
  `grep -c 'check-template-size.sh' tools/gate-legs.json` returns 3, unchanged from base.
  Recorded as a skip rather than omitted, because a skip that looks like a pass is
  indistinguishable from coverage
- AC3 — MET — `python tools/govkit/govkit.py selfcheck` exits 0 and
  `git diff --stat -- tools/govkit/subject-pins.tsv` is empty: no leg was added, so no pin moved
- AC4 — MET — the census prints the template with source `NONE`, a `-` ceiling and a `-` free
  column, and the `# uncapped:` tally rose 18 to 19. That is the degradation `ceiling_for`'s own
  docstring calls designed, observed rather than trusted, and it is the accepted consequence of the
  ruling: this file JOINS `TOOL-aScouredKit-23`'s population
- AC5 — MET — `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0 reporting 4 pairs in
  agreement, proving the guide was re-rendered rather than hand-edited
- AC6 — MET — `bash tools/memory-tree/check-memory-hygiene.sh --staged` exits 0 on the commit, so
  check 6 passes on the re-rendered guide
- AC7 — MET, with its figures MOVED at rev-6 and the move recorded. `wc -c` reports **23403** and
  `wc -l` reports **306**, against a base of 24564 / 317. The budget passage alone is 1101 bytes over
  11 lines and was observed at exactly 23463 / 306 before S1's second half; the two dangling
  sentences took the byte figure to 23403 and left the line count alone, because both came out from
  within lines rather than as lines. I wrote 305 first and the measurement corrected it
- AC8 — MET — `grep -n 'No gate enforces the pair'` returns no hit and `grep -n 'Budget:'` returns no
  hit. Both halves of the claim are gone, not one
- AC9 — MET — `bash skills/session-kickoff/manifest-check.sh` exits 0 after the commit, proving the
  S3 re-stamp landed in the same commit as `memory/guides/BUILD-METHOD.md`, the watched pathspec this
  unit stages. Run again after the follow-up commit, which stages the same pathspec and carries its
  own re-stamp

## What the M6 checklist caught that the criteria did not

Run on this unit's own build commit, `gotchas.py --for-diff` selected
`amendment-leaves-its-other-half-standing` and the class was live: with the budget deleted, M3 still
read *the delegation does not reach veto 2's governance-carrier clause, M1's own budget included* and
M7 still read *It is capped so this stays cheap*. Two sentences asserting a cap the file no longer
declares. No acceptance criterion covered them — AC8 greps only the passage's own two strings — so
the checklist, not the criteria, is what closed the deletion.
