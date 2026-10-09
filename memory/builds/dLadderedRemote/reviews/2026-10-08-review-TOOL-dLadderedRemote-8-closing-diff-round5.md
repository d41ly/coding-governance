**Serves:** diff-review TOOL-dLadderedRemote-8

# Tier-2 closing diff review — dLadderedRemote, ROUND 5

One reviewer agent, run directly on 2026-10-08, node `d`, READ-ONLY. It was primed with the round-1
brief, the round-4 record and unit 8's spec. It ran the HEAD, round-4 and round-3 copies of the ban
over 29 planted lines, ran the HEAD self-test against each copy, and ran each over a clone of HEAD.

**Reviewed range:** `da0c5a447...011449f63`, which is unit 8. **ROUND: 5.**

## Verdict: CLEAN WITH FIXES

N2, N3 and N4 are CLOSED. N1 is closed for the line round 4 quoted, but not for its class, and finding
1 below carries it. No BLOCKER, HIGH or MEDIUM.

This round's four LOW items are NOT strictly fewer than round 4's four, so the diff review does not
re-arm. By M4 the loop EXITS here. All four are promoted into one batch unit,
`TOOL-dLadderedRemote-9`, which is built from its spec as written and reviewed by no further round.

## Findings

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| 1 | LOW | `tools/check-remote-literals.sh` list-in-call shape | Only a list that is the call's LAST argument is caught, but this codebase passes argv lists followed by keyword arguments (`run([...], check=True)`). Round 3's gate caught those. | unit 9 |
| 2 | LOW | the ban's header | The colon-path sentence reads backwards, and "never a missed one" is false for a path holding `:<digits>:` followed by a comment leader. | unit 9 |
| 3 | LOW | `WIRE-INTO-PROJECT.md` | The straggler guard lets the pin choose without a warning when the observed HEAD carries no conf, and falls back to `main` where migrate-backlog refuses. | unit 9 |
| 4 | LOW | the ban's header | A key list or tuple passed into a call whose last element is the name is a hit, and the header does not say so. | unit 9 |
