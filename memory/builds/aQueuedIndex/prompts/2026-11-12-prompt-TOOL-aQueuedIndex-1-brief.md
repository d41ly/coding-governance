# Brief — aQueuedIndex: writers of the shared tag index queue instead of failing

**Serves:** research TOOL-aQueuedIndex-1

## The prompt

> fix the tag index contention so bars don't flake

## The brief

### Goal
Make the shared tag index's writers wait for one another, so a bar whose `tags` and `instruction edits` legs meet one
unbuilt tree runs both green instead of redding one on `database is locked`.

### Items
1. Every write to the index takes its write lock before it reads, so a second writer queues behind the first rather than being refused at once. [planned TOOL-aQueuedIndex-1]
2. The busy timeout outlasts a full tree build, which took 77 to 100 seconds on node a. [planned TOOL-aQueuedIndex-1]
3. A writer that waited re-reads whether its tree was built while it queued, and skips the rebuild when it was. [planned TOOL-aQueuedIndex-1]

### Acceptance
A fixture arm races two index writers over one unbuilt tree and observes both exit green, red at BASE. Five races of
`gov_tag.py check` against `instructions_edit.py check` on a fresh index in a scratch clone of the unit's commit all exit
0, where one race at BASE reds.

### Gates
`tags (the resolver's checks)`, `instruction edits (manifest checks)`, `lexicon naming predicates`, `spec tokens (a spec's own names resolve)`,
and the full bar at the close.

### Non-goals
No change to what the index stores or how a tree's rows are parsed; no new index file or schema version; no write-ahead
log, since every worktree opens the one file.

### Limitations
The index lives in the common git directory, so every worktree of a node shares it; a fixture that races writers must use
its own scratch repository, never the node's index. A bar's wall clock grows by the waiter's wait.

### Reuse
The seam is the index open in `tools/playbook/tag_index.py#load_index` and its write blocks, each already wrapped to raise
the `locked or unwritable` refusal; the busy timeout is the module's one constant. The reuse probe named no other writer of
the index.

## Drawn from the session

> Reproduced on the first try. The tags check died at 31 s, well inside its 60 s busy timeout, so this isn't a timeout running out. It looks like SQLite's deadlock refusal instead.
— agent, 2026-11-12, the first race in a scratch clone at 97e0841d7

> Three races out of three are now green. The fix needs both parts: `isolation_level="IMMEDIATE"`, so the waiter queues instead of deadlocking, and a busy timeout longer than a full tree build.
— agent, 2026-11-12, after the IMMEDIATE-only and IMMEDIATE-plus-600-s races

## Owner confirmation

Asked: Proposed brief for build aQueuedIndex, one unit (TOOL-aQueuedIndex-1) in tools/playbook/tag_index.py. Every write to the shared tag index takes its lock first (BEGIN IMMEDIATE), so the second writer queues rather than SQLite refusing it on the spot. The busy timeout grows from 60 s to cover a full tree build: a fresh build took 77 to 100 s, and 600 s passed 3 of 3 races. A writer that waited re-checks whether the tree was built while it queued, and skips rebuilding it. Acceptance: a fixture arm that races two index writers, plus 5 of 5 races of the tags and instruction-edits checks on a fresh index in a scratch clone, all green. The scratch-clone race reproduced the flake 1 of 1 at today's code. Accept this brief?
Answer: Accept (Recommended)
