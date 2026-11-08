# Fix brief — the replays' pre-run corrections folded into specs 25, 30 and 35

**Serves:** research TOOL-dFairHearing-25 TOOL-dFairHearing-30 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-37 TOOL-dFairHearing-40

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Break the cycle the reorder found (`memory/builds/dFairHearing/prompts/2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief.md`'s return): units 32, 37 and 40 each correct the replays' procedure AND read the records the replays leave. The main loop resolved it as option 1, delegated by M3: fold every correction that must hold BEFORE a replay runs into the replay unit's own spec (25, 30 or 35), under M4's repair rule ("A repair unit corrects an UNBUILT sibling's spec itself", owner 2026-11-01), and leave in 32, 37 and 40 only the work that reads or completes the runs' records afterwards. Commit nothing; the main loop commits.

### Items
1. Mark the fork in spec 25's §8 in the template's shape, `RESOLVED (agent, 2026-11-03, delegated)`, option 1, with M3's reason: option 2 spends the ten runs on the old procedure and patches the records after, the defect class unit 35 was promoted to close; option 1 leaves no follow-up. Carry `widens:` and `relaxes:` (each `none` unless the fold changes a bound) as README rule 5 asks.
2. Move into specs 25, 30 and 35, each as scope items with criteria that can go red: from 32, S14, S17, S18, S20 and S21's pre-run halves (the orchestrating-commit binding, the one clone envelope, the placement step through a temporary index, per-attempt clone names and the two-attempt cap, the void and re-run rule); from 37, the per-arm clone, path and status items; from 40, the "reports stay on disk" items. Name each by its source id, and say in the replay spec's §9 which source item it now carries.
3. In 32, 37 and 40, re-word each moved item as carried by the replay unit (a hands-off edge to it), keeping only the post-run reading and completion work; their edges and §3 text must then no longer correct a unit ordered before them. Units 32, 35 and 37's §4 sentences that reason M4 refuses a repair of an unbuilt sibling are corrected to today's M4.
4. Re-run the reorder's check: no unbuilt unit's spec is corrected by a unit ordered after it, and no `consumes-from` edge points forward. Adjust orders only if the fold needs it.
5. Rev bump and one §9 line per spec touched, naming this brief. Every §9 line names a section, a scope id or an acceptance id, as `memory/TEMPLATE-SPEC.md` and hygiene check 12 require. The reorder pass's own §9 lines in specs 32 (rev-5), 36 (rev-4), 38 (rev-3) and 39 (rev-2) name none, and check 12 refused their commit: re-word each to name the header's `order` field, for example `§ header`, or the section it changed. Leave each status header's state as it is.

### Acceptance
The return lists, per moved item, its source and its new home, and the check of item 4 reads zero forward corrections and zero forward consumes-from edges.

### Gates
None you run; the main loop runs the spec-token checker before committing.

### Non-goals
No change to a replay's bar or to what any run measures. No code, no write outside the six specs named in Serves and the §9 lines of specs 36, 38 and 39.
