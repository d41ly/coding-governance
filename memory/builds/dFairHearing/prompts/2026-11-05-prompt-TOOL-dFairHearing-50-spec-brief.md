# Spec brief — TOOL-dFairHearing-50: the reds the close's first suite baseline found

**Serves:** research TOOL-dFairHearing-50

## The prompt

> /unattended dFairHearing

— owner, the run's mandate. No pass may run a suite, so the close's baseline at `948e4141b` was the first run of these arms: six of twelve suites read red.

## The brief

### Goal
Write the spec for `TOOL-dFairHearing-50` at `memory/builds/dFairHearing/spec/2026-11-05-spec-TOOL-dFairHearing-50.md`. It repairs every red below, so each suite named exits 0. Commit nothing; the main loop commits.

### Items
Every line here is the main loop's reading of a suite log. Re-ground each one on today's tree and say so where it is wrong. A log line is quoted as the suite printed it.

1. `tools/workflows/tier2-review.test.sh`, `the args header documents all 31 fields read off a` — missing `length`. Its field regex at :451 takes `twinFigures.a.length` at `tools/workflows/tier2-review.js:3235` for a read of the args alias, because `\b` holds after a dot. Fix the arm's regex.
2. `tools/workflows/tier2-review.test.sh`, `FH23 AC27 the real stdout cut inside its item list` — the fixture's real stdout has one item, so cutting it leaves no `- ` line, and the harness reports `no bug class selected` where its head lines state one class. The arm has never run before. The defect is the harness's: the `cut` computation at the checklist acquisition (`tools/workflows/tier2-review.template.js` and its render) runs only when a `- ` line exists. A return whose head line states more than zero classes and holds no item is a cut, so it must be a `checklistError`. A genuine zero-selection return stays `no bug class selected`.
3. `tools/workflows/check-review-join.test.sh:386`, `harness: the verifier count is bounded`, greps `Math.ceil(allFindings.length / MAX_VERIFIERS)`; the harness spells `verifyOrder.length`. Fix the needle.
4. `tools/workflows/check-review-join.test.sh`, `discovery: an empty population is still not a pass` and `the empty refusal does not name both directories`. Unit 16 dropped `agent-cap.js` from `SELF_EXCLUDE` on purpose, so the `$E` and `$H4` fixtures' hook copy under the kit prefix makes the population non-empty. Move each fixture's hook copy to the `.claude/hooks/` fallback the gate already reads, outside the population. Keep the exclusion as it is.
5. `tools/workflows/check-verifier-fanout.sh`, six arms (`AC3`, `AC5`, `FH27 AC1`, `AC25` twice, `AC26`): the `--slots` call hands node `"$f:$_l"`, and MSYS does not convert an absolute path with a suffix, so node reads ENOENT and the gate exits 2. Fix the gate, not the arms: give node a spelling it can open, with no new spawn on a relative path, and fall back cleanly where `cygpath` is absent. Say which spelling a Linux run sees.
6. `tools/check-playbook-parity.test.sh`, `S1 an empty kit derivation reds before reporting coverage`: unit 27 planted a third kit in the fixture and the arm's staging at :492 still removes two. Add the third.
7. `tools/workflows/unattended-build.test.sh`, `MT zero confirmed and 48 unverified` (:1098) and `MT20 the callee ran over the measured shape` (:1120): the needles predate unit 5's `merged` key. Read the real output first, then fix the needles.
8. `tools/workflows/unattended-build.test.sh`, `DGR74 LIVENESS`, `DGR74 ...after a stderr notice` and `DGR83 a hook that denies printing nothing`: unit 16 moved `WRITER_MARK` from the hook to `tools/workflows/check-verifier-fanout.js`, so the `sed` staging at :2301 and its liveness grep stage nothing. Read `tools/workflows/check-protocol-parity.test.sh:706` to `:733` and decide whether the writer-split question still reaches a stub hook. If it does not, the arms, the notice's wording, or the gate is wrong: say which, from the code.
9. `tools/workflows/unattended-build.test.sh`, `RA6-1 ...and its check-verifier-fanout.sh once` (got 2) and `RA6-1 ...and the tool root plus gov's home for them nowhere` (got 6). This one may be a real gap: a renamed kit's rendered review protocol still spells the old kit home. Find which lines of `tools/workflows/REVIEW-PROTOCOL.template.md` the render's kit-cite pass misses, and fix the render or the template. The first count may be a legitimate new cite: then the arm's number moves, and the spec says why.
10. `tools/check-spec-tokens.test.sh`, `parity: a manifest suite invocation BAR does not match`: `measure-legs selftest` carries a 500 s ceiling and is not declared exempt. This red is inherited from base `8bec4cefd`. Declare it exempt the way its siblings are, in the same list.
11. Unit 48's two leftovers. Its builder could not fix the two docstrings in `tools/check-spec-tokens.py` (about :936 and :995) that call `read_carries_specs` the WONTDO filter's one home, now false, nor a header the generator's grammar refuses being graded here but set apart by the carries join. State the true filter homes. Then check whether `tools/workflows/README.md`, `memory/guides/UNATTENDED-VERBS.md`, `memory/guides/UNATTENDED-STOPS.md` or `memory/guides/REVIEW-PROTOCOL.md` list the harness's stop exits; if one does, `walk-red` joins that list.

12. Clear the traps this close has already hit:
    - Header: Tier-1 unless item 2, 5, 8 or 9 turns out to change behaviour past a mechanical fix, then Tier-2 with reasons. `order 33`, no ask clause, status `OPEN`.
    - List every path: renders beside templates, `memory/LIVE.md`, the build README, `memory/map/generated/symbols.json` if a definition moves, and any kit version marker a move owes.
    - `--dispatch` refuses a generated file declared beside its generator. Staging `tools/gate-legs.json` needs the kickoff manifest's `last-audit` re-stamp and delta line in the same commit.
    - A test floor counted by hand is not a run: say the floors move, and leave them to the close.
    - Acceptance sweep: split every backticked span on whitespace. Each word holding a `/` must be a tracked path exactly, or lead with `$`, `<`, a quote or `~`. Check the `BAR` pattern at `tools/check-spec-tokens.py:419` to `:424`, and put no `python -c` probe in the Acceptance section.
    - Every change-log line names a section, a scope id or an acceptance id. New text cites no check, section or method rule by a bare number.
    - `tools/gate-legs.json` legs for every file touched go on the Gates leg line, or the guards join reds.

The main loop may add items from a bar running now. Leave the spec open to one revision.

### Acceptance
A spec conforming to `memory/TEMPLATE-SPEC.md`, one criterion per item. Each criterion names the suite and the arm label, so the close's run is what observes it. A pass runs no suite, so each criterion also names a probe the builder can run: a grep, a fixture or a direct call of the changed code.

### Gates
None you run.

### Non-goals
No code, and no other spec. No new gate beyond what an item needs. Not touching `tools/run-gates/run-gates.sh`, since a run that edits the grader cannot land itself.
