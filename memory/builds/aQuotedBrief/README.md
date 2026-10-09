---
slug: aQuotedBrief
node: a
opened: 2026-10-09
streams: tooling
roster: TOOL
ids: TOOL-aQuotedBrief-1 TOOL-aQuotedBrief-2 TOOL-aQuotedBrief-3
---

# aQuotedBrief — a prompt fired mid-session stands on its own, starts clean, and closes every item

## The problem this build exists to solve

A prompt-mode run records only the bytes the owner typed. Fired mid-session, a prompt such as "yes,
spec it as a build" leans on the conversation, and no resumed session, compaction or later reader
sees that conversation. The run's build README then carries the agent's paraphrase with nothing
upstream to check it against. Separately, a run starts on whatever branch the session is on, so
commits the session made earlier ride into the landing under the run's authorization. And nothing
checks that every item the owner listed reached an end: `build-complete` grades the roster the run
wrote for itself, so an item merged away or dropped at orientation still closes green.

## Expected improvements

- A prompt record reads whole with no chat: goal, items, acceptance, gates, and the session words it
  relied on, quoted.
- A brief that draws on the session reaches the owner once, before the push that authorizes it.
- Every brief item ends planned, stale, duplicate or parked, and `--close` grades that.

## Detriments if this is not built

- Mid-session prompts stay unsafe, so the owner keeps restating context into every invocation.
- A resumed run rebuilds its scope from a README paraphrase nobody can check.
- Unreviewed session commits can land under a run's authorization.

## Build-level rules

Three units, one mechanism each. Unit 1 defines the brief and its confirmation. Unit 2 starts a run
whose tree is dirty or whose branch carries commits in a fresh worktree, and refuses a first
preflight on a branch carrying anything beyond this build's folder. Unit 3 gives each brief
item a disposition and grades it as a new `build-complete` term, so no core DoD item is added and no
adopter's `CORE_FLOOR` moves. It does not use asks: both adopters run `BACKLOG_MODE` `shards`. Unit 3
consumes unit 1's items section; unit 2 is independent of both.
Both refusals are guards against accident, not a security boundary: a run with shell access can
rewrite its own history. The kit version moves once, after the last unit lands. Owner decisions,
2026-10-09: confirmation applies only to a session-derived brief, an edit there is not confirmed
again, and an unclean tree starts the run in a fresh worktree rather than stopping it.
M2 classification at preflight (base 6473ae38): all three units READY. Units 1 and 2 share
`unattended.sh`, its suite and the verbs template, so they build in sequence, 1 then 2 then 3.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aQuotedBrief-1` | SPECCED | the prompt record carries a self-contained brief, the session words it used, and the owner's confirmation when it used any |
| 2 | `TOOL-aQuotedBrief-2` | SPECCED | a run that cannot start clean starts in a fresh worktree, and a first preflight refuses a branch carrying commits beyond this build's folder |
| 3 | `TOOL-aQuotedBrief-3` | SPECCED | each brief item carries its disposition at BASE, joined to the roster, and a seventh `build-complete` term grades it |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-10-09 · streams tooling
ids TOOL-aQuotedBrief-1 TOOL-aQuotedBrief-2 TOOL-aQuotedBrief-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aQuotedBrief-1 — the prompt record carries a self-contained brief, its session sources, and the owner's confirmation](spec/2026-10-09-spec-TOOL-aQuotedBrief-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aQuotedBrief-2 — a run that cannot start clean starts in a fresh worktree, and a first preflight refuses a carried branch](spec/2026-10-09-spec-TOOL-aQuotedBrief-2.md) | 1 | 2 | CLOSED | rev-4 | 2026-10-09 |
| [TOOL-aQuotedBrief-3 — every brief item carries its disposition, and `build-complete` grades each one](spec/2026-10-09-spec-TOOL-aQuotedBrief-3.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aQuotedBrief-1 TOOL-aQuotedBrief-2 TOOL-aQuotedBrief-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aQuotedBrief-1`, `TOOL-aQuotedBrief-2` | yes |
| 2 | `TOOL-aQuotedBrief-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
