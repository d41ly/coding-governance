**Serves:** diff-review TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-7

# Tier-2 closing diff review — dLadderedRemote, ROUND 4

One reviewer agent, run directly on 2026-10-08, node `d`, READ-ONLY. It was primed with the round-1
brief, the round-3 record and unit 7's spec. It ran the HEAD and round-3 copies of the ban side by
side over 27 planted lines and over a clone of HEAD.

**Reviewed range:** `d9c349d95...da0c5a447`. That holds the govkit spawn-site row, the kickoff
engine's two restored command spans, and unit 7. **ROUND: 4.**

## Verdict: CLEAN WITH FIXES

All five round-3 items are CLOSED. No BLOCKER, HIGH or MEDIUM. Four new LOW items, strictly fewer
than round 3's five, are promoted into one batch unit, `TOOL-dLadderedRemote-8`. Two of them are
regressions unit 7's narrowing introduced against round 3's tip. Neither has a live instance in the
tree.

## Findings

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| N1 | LOW | `tools/check-remote-literals.sh` last-argument shape | Closing on `)` only lost an argv LIST inside a call whose git verb is outside the remedy set, such as `["git", "remote", "show", "origin"])`. The header still claims only a non-last argument is unseen. | unit 8 |
| N2 | LOW | the comment filter | It splits a hit on its first colon, so on a POSIX checkout a comment line in a path holding a colon reads as a hit. The merge comment claims colon-path safety. | unit 8 |
| N3 | LOW | the `${...}` default shape | An indirect expansion `${!ref:-origin}` escapes the narrowed head. | unit 8 |
| N4 | LOW | `WIRE-INTO-PROJECT.md`, `skills/session-kickoff/SKILL.md`, the govkit row comment | The runbook's "only cross-check" overstates it: with nothing observed, the pin selects. The skill omits the `.` and unknown-name rungs. The govkit comment says one interpolated value where there are two. | unit 8 |
