**Serves:** journal TOOL-dTotalRecall-115
**Caused-by:** TOOL-dTotalRecall-115

# TOOL-dTotalRecall-115 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `3a1f4ba1d` from [2026-11-25-prompt-TOOL-dTotalRecall-115-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-115-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `19a209739`.

## Why

Built to spec rev-1 with no divergence: S1 to S7 are in one commit, and the spec is set to CLOSED. The §4 code was taken as written. (DERIVED 2026-11-25, the pass)

## Summary

BUILT
- tools/lib/gov-feed.sh#derive_record_rows drops every row whose key the log already holds.
- check_feed's record arm walks from every reachable logged commit and prints `duplicate`. The ref arm skips `record` lines.
- The header comment is updated, and the four carriers take the block's bytes.
- The `rr_` block of tools/unattended/unattended.test.sh gains the merge landing, `keyless.sh` and the re-cut `whole.sh`. FLOOR_ASSERTIONS goes 4223 to 4228 and FLOOR_SHARD_8 1440 to 1445 (DERIVED 2026-11-25).
- The shell-role rows were widened by widen-28. The door raises a row by one, so I set the counts to the measure, as widen-22's rows were (a `Decided:` trailer records it).
- The acceptance ledger is at memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-115-1-acceptance-ledger.md.

CHECKS RUN (DERIVED 2026-11-25)
- AC1 to AC3: the §4 probe in a scratch repository gave 2, 3, 4 and 4 lines over four keys, with every check 0. The copied line printed one `duplicate` and nothing else. `extra` and `missing` each printed alone with exit 1. (DERIVED 2026-11-25, the pass)
- The same probe over the base block was red: `extra` at the second landing and five lines after the third. With the key test turned into `1` it gave five lines and `duplicate`.
- Two extra probe cases: a refused walk appended nothing, and an absent log dropped nothing.
- AC4, AC5 and AC7 were read as §6 spells them, all green. (DERIVED 2026-11-25, the pass)
- AC6: the merge-landing arms' sequence, run as a probe with the same mutate scripts, printed `3 0`, `0 0 0`, `1` and `1 1 1`. Over the base block the first two printed `4 1` and `0 1 0`, and the copied line `1 0 4`. This stands in for the unattended suite until the close.
- A python probe calling sh_hygiene's scan functions, HEAD against the edited tree, moved no spawn, temp, quoting, stage or location-probe count in the six files. Only an ungated herestring near-miss rose by 1, in the suite. This stands in for the shell hygiene legs. (DERIVED 2026-11-25, the pass)
- The first record walk over this repository, 73,560 rows, took 3.2 s, under NODE_LOCK_BOUND. check_feed over that full feed took 11.5 s unlocked. (DERIVED 2026-11-25, the pass)
- The commit hooks passed. No gate, suite, bar or selftest ran.
- gotchas --for-diff ran over the commit. The one class I acted on is two-answers-to-one-question, handed back below.

OWED TO THE CLOSE
- Every §7 leg. (DERIVED 2026-11-25, the pass)
- The `New arm:` RED-first observation of the `rr_` block's DTR115 arms: the keyless copy, and today's block printing `extra`.
- The re-cut AC2 `whole.sh` arm.

HANDED BACK, not edited because no file here is in the spec's Files touched
- tools/unattended/VERBS.template.md, around line 858, and tools/unattended/STOPS.template.md, around line 304, still say `--feed check` compares with the walk "up to the newest one" a branch reaches, and VERBS does not name `duplicate` for record events. Their dogfood copies memory/guides/UNATTENDED-VERBS.md and memory/guides/UNATTENDED-STOPS.md say the same. The walk is now from every reachable logged commit. None of the specs of units 116 to 121 names either template file. (DERIVED 2026-11-25, the pass)
- The `unread <ref> walk` refusal of check_feed has no suite arm, as before this unit.
