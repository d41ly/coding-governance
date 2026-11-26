# Brief — TOOL-aPrunedIndex-24: the held-answer rules get arms the bar runs

**Serves:** research TOOL-aPrunedIndex-24 TOOL-aPrunedIndex-17

## The prompt

> Build them first

The owner gave this answer in the building session on 2026-11-26. The question was "How should the three small code findings be handled?", with the choices "File as asks, land" and "Build them first". The findings are items 1, 4 and 5 of `memory/builds/aPrunedIndex/reviews/2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md`; read them whole. This is the one unit BUILD-METHOD M4 batches them into.

## The brief

### Goal
The rules unit 17 states for its held git answers each have an arm that the `tags bundle selftest` leg runs and that reds when the rule is broken, and `HELD_FLAGS` holds no member its code never reads.

### Items
1. A plant or an extension of an existing plant in `tools/playbook/gov_tag.py`, rowed in `tools/playbook/tag_bundle.py#SELFTEST_ROWS`, makes spec 17's AC2 read table permanent: `derive_held_key` gives each listed read its expected key or `None`, including the `.git`-exists guard (review item 1, id 5).
2. The same arm, or a sibling, makes AC3 permanent: inside `set_git_held()` a failing read (the all-zero `^{tree}`) spawns git on each of two calls and stores nothing, while a held read spawns once (review item 4, id 6).
3. `"--"` leaves `HELD_FLAGS`, which then holds `{"--full-tree", "--name-only", "-r", "-z"}` (review item 5, id 4). The arm of item 1 shows the key table unchanged.

### Acceptance
Each arm passes on the built tree and is seen red under a staged break of the rule it guards: the `.git`-exists guard removed, a failed read stored, and a wrong key for a listed read. `tags bundle selftest` still prints `PASS — the tag plants, <n> rows` with the new row count, and its wall stays within its 159 s budget row.

### Gates
tags bundle selftest; lexicon naming predicates; memory hygiene; spec tokens (a spec's own names resolve)

### Non-goals
No edit to `tools/playbook/tag_index.py` or its import closure. No change to the five plants' verdicts or output lines. No ceiling or budget row moves. `tools/loop/position.py` and `tools/memory-tree/routed_commits.py` stay untouched. Tier 1.

## Owner confirmation

Asked: How should the three small code findings be handled? (file as asks and land, or build them first)
Answer: Build them first
