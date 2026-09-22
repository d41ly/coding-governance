# Build brief — TOOL-aRatifiedRulings-4

**Serves:** journal TOOL-aRatifiedRulings-4

The pass this brief was handed to builds unit 4 of `aRatifiedRulings` at rev-3, the last unit. The
spec is `memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-4.md` and it is
authoritative; the ruling it implements is `TOOL-aLeakedHandle-9` in `memory/DECISIONS.md`.

## THE OWNER'S INSTRUCTION, FIRST

**A pass runs the fast diff-scoped gates and nothing held.** No self-test suite, no held leg, no
`run-gates.sh` bar inside this pass. `run-gates.test.sh` is the canary — `chunk: selftests`, held,
13200 s ceiling — and you do NOT run it whole. Observe your ONE new arm by running the arm's own
fixture in isolation, the way the parent build's unit 3 did with a direct reproduction: the spec's
§4 says how. The full bar is `--close`'s and the push boundary's.

## What the pass builds

`report_one` in `tools/run-gates/run-gates.sh`: when rc=137 and NO ceiling was declared, the tail
prints `(killed after <secs>s)` with no ceiling clause, reading the same `$WORK/<i>.sec` the ledger
reads as field 2 — the parent's unit 3 built the declared-ceiling branch beside it; match its shape.
One arm in `tools/run-gates/run-gates.test.sh`, asserting the VALUE against the ledger row byte for
byte, placed where the spec's §4 says so its skip announces itself if the guard is false.

## What two audit rounds settled

- **The red case is FIXTURE-ONLY, by class name.** Every leg in `tools/gate-legs.json` declares a
  ceiling, so the branch cannot fire on a real leg; the fixture strips one. That is
  `staged-break-substitutes-a-synthetic-value` and the ruling accepted it. Say so in the ledger.
- **AC5 strips the ceiling for YOUR fixture leg only** — never by stubbing `timeout` for the whole
  runner, which reds the canary's own clamp and wall arms. Read the spec's §4 for the seam.
- **`memory/guides/SESSION-KICKOFF.md` is in the write set** because `run-gates.sh` is a watched
  file: re-verify §B and re-stamp `last-audit`. Unit 1 already re-stamped this build; you are the
  second of the two, and the kickoff-manifest merge exception says the later re-stamp supersedes.
- **`KIT_RUN_GATES_VERSION`** — the spec's §3 states whether this unit bumps it and cites the
  precedent it follows. Do what the spec says; do not re-argue it.

## The rules this pass is bound by

- The arm's failing case OBSERVED RED first against the unfixed source, with a positive artifact
  that it ran: the parent's unit-3 arm printed both numbers (`600's` where the ledger held `2.144's`).
- Commit with the unit id in the subject; then `python tools/memory-tree/gotchas.py --for-diff
  HEAD~1..HEAD` and act on it. Flip the spec status header in the same commit.
- Re-declare WIDER with `--dispatch` before the commit if the set grows.

## What the pass must not do

- Do not change any verdict, the ledger, or the summary format. One branch, one arm.
- No sibling unit's files. No bar. Never `git stash`.
