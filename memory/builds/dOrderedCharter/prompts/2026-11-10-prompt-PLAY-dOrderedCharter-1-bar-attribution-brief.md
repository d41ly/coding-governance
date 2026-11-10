**Serves:** research PLAY-dOrderedCharter-1

# Brief: attribute the close bar's sixteen failing legs, own or inherited

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. The close's full bar over 3c63fe888 failed sixteen legs. The fix unit that follows needs to know which reds this
build introduced and which it inherited, so it fixes exactly the own ones.

## The brief

### Goal

For each failing leg, name its offenders, attribute each one OWN or INHERITED with evidence, and give the narrowest fix for each OWN
one.

### Items

1. The legs' logs are under the worktree's git dir, `gate-logs/`, one per leg, named from the leg: kickoff-manifest ratchet, memory
   hygiene, shell hygiene (a fork spent on builtin work), install-prefix (shipped surface), method carriers, harness arms, dead-path
   carriers, remote literals, govkit selfcheck, docs, lexicon naming predicates, govkit acceptance matrix, policy check, every held
   leg is budgeted, lexicon wiring, and tags, which timed out at its ceiling twice and has no verdict.
2. Per leg, quote the failing lines only, not the informational or waived ones.
3. Attribute each offender: OWN when the offending text was added or changed on this branch since its merge base with local `main`,
   INHERITED when it already stood at the merge base. Cite the evidence: the diff, `git log -S` or `git blame`.
4. For each OWN offender, give the narrowest fix and say whether it writes product code under `tools/` or `skills/`, which needs a
   builder, or only a record or registry row, which the main loop writes.
5. For tags, say from its log and its declared ceiling whether it is a cost problem or a hang.

### Acceptance

- A table, leg by offender, with OWN or INHERITED, evidence, fix and who, then a count of wholly inherited legs and the OWN fixes
  grouped by file; under 1200 words, payload first, "unclear" where the logs and git do not settle it.

### Gates

None: read-only. Run no gate, bar or suite.

### Non-goals

- No edit, stage or commit of any file.
