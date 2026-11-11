---
name: unvalidated-arg-reaches-an-agent-shell-line
description: a caller's argument is pasted raw into a command line an agent is told to run, so a value with a shell metacharacter reaches a shell-holding agent as an instruction, and only the sibling field beside it was refused
kind: class
universal: false
---

# A caller's argument pasted into an agent's shell line

## Symptom

A harness builds a prompt that tells an agent to run a command, and interpolates a caller's field
into that command. Nothing refuses the value before the agent spawns, so a field holding `;` or
`$(` becomes part of what the agent is told to execute. The harness usually guards a sibling field
for exactly this reason, which makes the unguarded one look covered.

## Where it bit

The closing diff review of the dFairHearing build,
2026-11-04-review-TOOL-dFairHearing-1-40-diff-review, id 1. The checklist agent of
`tools/workflows/tier2-review.template.js` was told to run the bug-class checker over the raw
`base` and `head`. At round 1 `head` was never checked and `base` only drew a warning, so a `head` of
HEAD;echo PWNED spawned that agent with the value in its command. The resume probe's two
rev-parse commands pasted the same values. The same diff refused three characters in `repo` for this
very reason.

## The fix

Refuse the field against a closed shape before any agent spawns, at every round, and name the field
in the error. An allow-list beats a deny-list: the shape admits what a real value needs and nothing
else, and a rule against a leading `-` keeps the value from reading as an option. Resolving the value
first does not help when the first agent to use it spawns before whatever resolves it.

## Its gate

Gated by `tools/workflows/tier2-review.test.sh`, its `FH43 AC1` arm.
