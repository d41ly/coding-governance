**Serves:** research TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92

# Round-13 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-91-1-spec-writer.md`, run direct/a6017c2e91b795038, one per stop, extracted from its transcript by script.

## Return 1

Both fixes are made, and the hygiene gate `--only 2,12,25` now prints no dWitnessedBar finding and no FAILED line. I did not run `check-spec-tokens.py`, since my role admits only the hygiene gate and the lexicon. In its place I loaded its `BAR` pattern and applied it to every backticked token in unit 92's §6; none matched, so the main loop's run should show no dWitnessedBar hit. I also didn't add the `New arm:` line the brief asks for; the reason is below.

**TOOL-dWitnessedBar-91**: I reworded S1 rather than adding a `**Readers:**` clause, because it retires nothing. Check 25 fired on the word "removed" in "neither initialiser was removed to make a count pass". That sentence is a guard that the two `rec_sha=""` initialisers survive, not the retirement of a name. The third bullet now ends "so both initialisers still stand when the other two counts pass", which keeps the meaning. S1 still sets aside 90 AC2's count clause in place of it, but that is a criterion, not a named code thing, so it needs no Readers clause.

**TOOL-dWitnessedBar-92**: AC8 was the hit, because it named the suite's path as a bare backticked token. It now spells out three whole one-line probes, each `grep -c '<comment>' tools/run-gates/run-gates.gov.test.sh`, says they are probes of the suite's text and never a run of it, and keeps its note-check clause. As whole commands the tokens start with `grep`, so they no longer match the runner-at-command-position pattern. The criteria are unchanged.

**Decision for you: the `New arm:` line.** I left §7 of unit 92 without one, which means the brief's instruction to name the suite there is not done. Unit 92 adds or moves no arm; S9 only restores comments. Its §3 lists "a `New arm:` line" under Non-goals, and its §4 Evidence states that units 91 and 92 declare none, "so a re-render that lists them leaves the length at 28 and the owner at unit 90". The owner derivation in §4 picks the last spec with a `New arm: tools/run-gates/run-gates.gov.test.sh` line. Adding one would move ownership of the floor from unit 90 to unit 92 and push the length to 29, contradicting the spec's own design. The brief's own note that a grep over the suite's text "is a probe, not a run" covers AC8 as rewritten. If you still want the line, it needs a rev bump and a §3/§4 change, which is outside this brief.

Both specs stay at rev-1, unstaged and uncommitted. I touched no H1 or other spec and ran no index generator.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-91.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-92.md
