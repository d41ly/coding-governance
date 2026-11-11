# Spec brief — TOOL-dFairHearing-46: the bar's own reds in replay_scorer.py, and its stated-count reader

**Serves:** research TOOL-dFairHearing-46

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Write the spec for `TOOL-dFairHearing-46` at `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-46.md`. The close ran the bar's lint legs on this branch and on a frozen clone of BASE `8bec4cefd`. Every red below passes at BASE, so it is this build's own. This unit repairs them all in `tools/workflows/replay_scorer.py`, and the stated-count defect a replay run met. Commit nothing; the main loop commits.

### Items
Run each leg's command from `tools/gate-legs.json` read-only to see its current output, then scope a fix:
1. **encoding posture:** the four `subprocess.run` calls with no `encoding=`.
2. **drift-audit records:** the `PROOF_DIR` and `HELD_OUT_FILE` constants spell `TOOL-aScoutedSeam-1`, a non-terminal spec, from product source. The set is shrink-only: remove the cause, never list it.
3. **govkit selfcheck:** the file names an adopter by brand once. Cite the record id and the adopter's short name instead, as the leg's message says.
4. **install-prefix:** the two selftest lines that spell `tools/workflows/planted.py`.
5. **The stated-count reader:** `extract_stated_count`'s regex `confirmed\W{0,6}(\d+)` read a synthesis's prose "3 confirmed, 0 blocker" as 0, which voided replay attempt `f2s1` (`memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-30-replay-verdict.md`). Read the shape line, not the prose. The class gets a regression arm in the scorer's selftest, or a catalogue record if no gate fits, and `ARMS_DECLARED` moves with any arm added.

One `New arm:` line per arm the unit adds, each naming a break that reds on today's code. Write the unit's departure record the way unit 43's deviation record was written, and carry `order 29`, no ask clause, as unit 43's design explains. Unit 43 does not write this file, so the two write sets stay disjoint. Keep them so; check that yours pairs no generated file with its generator.

### Acceptance
A spec conforming to `memory/TEMPLATE-SPEC.md`, with one criterion per item that reds on today's code and greens on a correct build. Check the acceptance section's backticked words against `tools/check-spec-tokens.py`'s `BAR` pattern (lines 419 to 424). Every change-log line names a section, a scope id or an acceptance id. New text cites no check, section or method rule by a bare number.

### Gates
None you run beyond those read-only leg commands.

### Non-goals
No code, and no other spec. Nothing outside `tools/workflows/replay_scorer.py`, its selftest's record and this unit's own records.
