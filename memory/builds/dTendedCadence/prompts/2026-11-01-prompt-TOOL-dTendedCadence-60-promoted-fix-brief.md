**Serves:** research TOOL-dTendedCadence-60 TOOL-dTendedCadence-67 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70

# Promoted-fix brief — dTendedCadence, the round-3 promotions' mechanical reds

The round-3 spec audit's disposal authored fifteen promoted units, TOOL-dTendedCadence-60 to -74, under
`memory/builds/dTendedCadence/spec/`, staged and NOT committed. The main loop ran `tools/check-spec-tokens.py` over
them, and every red below is a token finding in exactly one spec. Fix each in place, in the spec it names, and
nothing else: no design change, no new scope, no edit to a spec this list does not name. These specs have never been
committed, so a fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", its first two bullets, before the first edit.

## A path a criterion cites that does not exist at HEAD

- TOOL-dTendedCadence-67 cites `memory/maintenance/2026-11-01-maintenance-2026-11-01.md` (lines 70 and 113), a record
  its own fixture writes, as a full path the token check reads as an untracked citation. Name it in §6 by a form the
  check does not join to the tree: the basename, or a path the command takes as an argument, and keep the full path
  only where §2, §4 or Files touched need it.

## A hand-off token the receiver never names

- TOOL-dTendedCadence-69 §3 (line 49) hands TOOL-dTendedCadence-70 `read_remote_record_ref`, and spec 70 never names
  it. Name it in spec 70, in backticks, where unit 70 reads the always-run verdict that call answers (its matching
  `consumes-from TOOL-dTendedCadence-69` bullet and the criterion that reads it), or correct unit 69's bullet if unit
  70 does not read it. Say which in your return.

## When you finish

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and fix any red it prints on these files.
Return the specs you edited and each fix. Commit nothing and do not run the index generator.
