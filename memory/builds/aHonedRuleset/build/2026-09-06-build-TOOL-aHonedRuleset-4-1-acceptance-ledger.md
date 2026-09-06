# Acceptance ledger — TOOL-aHonedRuleset-4

**Serves:** journal TOOL-aHonedRuleset-4

Tier-2 · node a · 2026-09-06

The charter's §8 agent-cap bullet already pointed at `tools/hooks/README.md` for the marker spellings
and the resolvable-bound grammar, then restated that grammar behind its own pointer; two neighbouring
bullets restated the enforcement location a third and fourth time. The restatement went, the two
bullets folded into one, and the wrong array-literal claim was corrected on both carriers.

## Acceptance criteria

**Evidences:** TOOL-aHonedRuleset-4

- AC1 — MET — `bash tools/check-playbook-parity.sh` exits 0 printing `pairs in agreement`
- AC2 — MET, and this is the criterion that mattered. Each of the five `PAIRS` stated-side
  extractions was run against the template ALONE and each returned NON-EMPTY: `lens-array bound` 5,
  `agent-cap hook matcher` `Workflow|Agent`, `verify-agent total` 5, `bounded-helper width` 5,
  `resolved-K ceiling` 5. My first draft split `at most 5 verify agents TOTAL` and
  `array LITERAL of ≤5 elements` across line wraps, which the per-line `sed` would have resolved to
  nothing; the build script now REFUSES to write a tree where any of the five is not on exactly one
  physical line, so the failure mode is structurally unreachable rather than merely avoided
- AC3 — MET — `bash tools/check-agent-cap-restatement.sh` exits 0 reporting `clean — 86 markdown
  file(s) scanned, 2 waiver(s)`, so the `at most 5 verify agents TOTAL` waiver row is still live
- AC4 — MET — the template measures **48531**, against a ceiling of 48611 and a base of 49144. 613
  below base, of which 126 is `TOOL-aHonedRuleset-2`'s and **487** is this unit's
- AC5 — MET — `adopt-playbook.sh --target . --check` prints `region matches a fresh render`
- AC6 — MET — `bash tools/check-line-length.sh` exits 0, `0 over 450 characters`
- AC7 — MET in BOTH halves. `grep -rc 'passes unmarked'` returns 0 for the template, `AGENTS.md` and
  `tools/hooks/README.md`; `grep -n 'array LITERAL of ≤5 elements'` on the template returns exactly
  one line; and the POSITIVE half added at rev-5 returns at least 1 for `is a receiver` in both the
  template and the hook README. Without that half, deleting `tools/hooks/README.md:117` outright
  would have passed every criterion while violating S8
- AC8 — MET — `git diff --cached --name-only` on the landing commit lists exactly **five** files:
  the two charter carriers, `memory/guides/SESSION-KICKOFF.md`, `tools/hooks/README.md` and
  `memory/backlog/TOOL.md`. The unit-3 records were split into their own commit precisely so this
  assertion stayed about the code
- AC9 — **NOT MET AS WRITTEN.** The push-boundary bar came back RED on four legs, none on this unit's
  subject: three reproduce at base and the fourth was check 23, which this ledger answers
- AC10 — MET in both halves — `grep -c 'both fire a main-loop'` returns 0, and exactly one bullet
  survives between `- Persist each Tier-2 run` and `- Verify before "done"`
- AC11 — MET — the `TOOL-dFramedEntrypoint-1` row reads CLOSED and names `builds/aHonedRuleset/`
- AC12 — **SKIPPED, on an explicit owner directive mid-run: "skip self-tests".** The
  `GATE_SELFTESTS=1` run this criterion asks for did not happen, so the five `tools/hooks/` self-test
  legs are UNOBSERVED by this build. Stated plainly rather than left to read as green. What bounds it:
  this unit's diff touches `tools/hooks/README.md` only — no hook behaviour, no constant, no matcher
  — and `check-agent-cap-restatement` (AC3) and `playbook parity` (AC1) both grade the surviving
  prose and both are green

## Figures replaced by measurement

§4's files-touched table, its high-water paragraph and its Alternatives bullet all carried a
PREDICTED 48485 bytes and 107 of margin against a build that landed 48531 and 153. The 46-byte gap
has a cause worth keeping: holding each parity phrase on its own physical line costs bytes the §4
candidate block never had to spend, because a candidate block is not graded by that gate. The M6
checklist selected `amendment-leaves-its-other-half-standing` on the build commit and was right.
