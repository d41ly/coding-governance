**Serves:** research TOOL-dTendedCadence-35 TOOL-dTendedCadence-39 TOOL-dTendedCadence-48

# Promoted-fix brief — dTendedCadence, the round-1 promotions' mechanical reds

The round-1 spec audit's disposal authored fourteen promoted units, TOOL-dTendedCadence-35 to -48, under
`memory/builds/dTendedCadence/spec/`, staged and NOT committed. The main loop ran `tools/check-spec-tokens.py` and
hygiene checks 2, 5, 12, 13, 21 and 25 over them; hygiene printed nothing, and every red below is a token finding in
exactly one spec. Fix each in place, in the spec it names, and nothing else: no design change, no new scope, no edit
to a spec this list does not name. These specs have never been committed, so a fix stays at `rev-1` and owes no §9
line. Read the spec brief `memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md`,
section "What the last spec runs had to fix after their writers returned", before the first edit.

## A path the check reads as an untracked citation

- TOOL-dTendedCadence-48, AC30 (line 334): `git show f4597719:tools/drift-audit/drift_report.py | sed -n 4427,4438p`
  is read as the path `f4597719:tools/drift-audit/drift_report.py`, which is not tracked. Keep the observation and
  spell the revision apart from the path so no single token joins them: for example the command takes the path as
  an argument (`git show "f4597719:$p"` with `p` set to `tools/drift-audit/drift_report.py` in its own backticks), or
  the criterion cites the base's lines as `drift_report.py` lines 4427-4438 at base `f4597719`.

## A hand-off token the receiver never names

- TOOL-dTendedCadence-39 §3 (line 53) hands TOOL-dTendedCadence-48 the token `read_newest_record(root, run="security")`,
  and spec 48 spells the call with its added `carrying=` parameter (S17, line 76-78), never that exact token. Make
  the bullet's token one spec 48 names verbatim, `read_newest_record`, and keep the prose describing the call and the
  `carrying=` addition, so the join reads one token both specs spell.

## When you finish

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and fix any red it prints on these files.
Return the specs you edited and each fix. Commit nothing and do not run the index generator.
