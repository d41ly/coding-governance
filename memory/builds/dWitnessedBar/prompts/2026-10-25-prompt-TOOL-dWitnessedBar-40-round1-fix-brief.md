**Serves:** research TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51

# Round-1 fix brief — the promoted specs' check hits and the five re-pins, before the round-2 audit

The round-1 spec audit's disposal wrote TOOL-dWitnessedBar-40 to -51 and folded hands-off edges into the 30
roster specs as rev-2. Clear every finding below, changing nothing else, so that
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding and the main
loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit.

- Units 40 to 51 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. The roster specs
  are at rev-2, uncommitted: an edit to one of them joins its rev-2 entry, so extend that rev-2 §9 line to say
  what moved; do not bump to rev-3.
- Touch no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role
  admits the hygiene gate and the lexicon only; the specs are staged, so `--only 2,12,25` grades them in place.

## 1. TOOL-dWitnessedBar-51 does not parse past AC30

At line 564 a fence opens inside AC30 and never closes, so every line after it goes unread. That one defect is
why check 12 reports §7 to §10 missing, the rev-1 entry absent from §9, the §10 evidence missing and AC30 naming no
failure mode, and why check-spec-tokens refuses the spec's binding lines. Respell AC30's planted tail so it opens
no fence: describe the line in words, or quote it without a run of three or more backticks at a line start. Then
re-run check 12 and fix whatever it still reports on unit 51.

**Size.** Unit 51 is 48965 bytes against the 49152 ceiling. If your fixes would take it over, do not trim
criteria: return instead with a proposed split of unit 51 into two units over disjoint write sets (BUILD-METHOD
M4: a minors batch splits only along disjoint write sets), naming which findings go to each. The main loop then
mints the second unit and briefs a writer.

## 2. Check 25 — retirements owe a Readers clause

- TOOL-dWitnessedBar-44 S4.
- TOOL-dWitnessedBar-51 S28, S31 and S48.

Each is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason. A reader not
yet in the tree is written `READER NOT IN TREE` with the parent spec that creates it. Where the item retires
nothing, reword it so it no longer reads as a retirement, keeping its meaning, and say which you chose.

## 3. Check-spec-tokens

- **[handoff]** Unit 28's §3 hands `declared-with-runners` to unit 51, and unit 51 never names it. Name it in
  backticks in unit 51 where it reads it, or correct unit 28's bullet if unit 51 does not read it.
- **[carries] stale pins.** Deviations 31, 71, 161, 211 and 281 amend five clauses, so the as-built view now hashes
  their text anew. Re-pin each carrier's `**Carries:**` line to the view's hash, and say in its §8 which deviation
  moved it (one line on the pin, as a RESOLVED mark in the `RESOLVED (agent, 2026-10-25, delegated)` shape):
  - TOOL-dWitnessedBar-3: `cl-dClosedLoop-0341@65d333f3` (deviation 31)
  - TOOL-dWitnessedBar-7: `cl-dClosedLoop-0345@72933671` (deviation 71)
  - TOOL-dWitnessedBar-16: `cl-dClosedLoop-0354@13f6f9b8` (deviation 161)
  - TOOL-dWitnessedBar-21: `cl-dClosedLoop-0359@5c408077` (deviation 211)
  - TOOL-dWitnessedBar-28: `cl-dClosedLoop-0366@337938da` (deviation 281)
- **[carries] token.** The amended text of cl-dClosedLoop-0354 carries the token
  `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md:1087-1090`,
  which none of its carriers names. Name it, in backticks, in TOOL-dWitnessedBar-16 where it states the population
  rule.

Return what you changed per finding and the dWitnessedBar lines `--only 2,12,25` prints after your edits.
