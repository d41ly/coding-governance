---
slug: aNumeralWarden
node: a
opened: 2026-08-10
streams: tooling
roster: TOOL
ids: TOOL-aNumeralWarden-1
---

# aNumeralWarden — agent-cap reads the number, and the two caller-settable knobs go away

Node `a` · opened 2026-08-10 · streams tooling.

## Start here

**State.** Code is BUILT and LANDED on `origin/main` as merge `990f07b`, full bar green inside the
lander. The three Rollout commits, each gated on the branch first: `3086cab` (S1-S13, the
bound-reading predicate) · `fb29755` (S14, the matcher widening) · `3aec132` (S15, the runtime
count). Every acceptance criterion AC1-AC27 is observed. What ships: `agent-cap` 1.3 resolves the
bound at the call site, the default parameter and the `gov:bounded-fanout` width, refuses a set
`AGENT_CAP`, and counts direct `Agent` spawns at 5 per user prompt. Also moved: `settings-merge` 1.1,
`drift-audit` 1.1.

**The unit is NOT closed, and one thing is why: F2 is still open.** No code is owed — F2 moves none,
as §3 said — but a spec may not go terminal while §8 names an unresolved question, and hygiene check
12 enforces that. So the only remaining action is the owner's decision on F2 (`MAX_LENSES` is 6 while
`MAX_VERIFIERS` is 5); §8 carries its three options and a recommendation. Ratify it, then flip this
unit to CLOSED.

**AC22 was measured, and it answered YES.** `PreToolUse` does fire for a direct `Agent` spawn,
`tool_name` is exactly `Agent`, and `session_id` / `prompt_id` / `tool_use_id` are all present. The
`SubagentStart` fallback does not apply and was not built. §8 F4 carries the evidence, including the
liveness probe that had to run first — settings ARE re-read mid-session, so the measurement could not
have been a false negative.

**One fork is still open: F2** (`MAX_LENSES` is 6 while `MAX_VERIFIERS` is 5). No code moved for it,
as §3 said. F1 and F3 were ratified at build by their own recommendations; F4 is measured and closed.

**What downstream can now proceed.** `TOOL-aUnmannedHelm-1` declared a dependency on this unit
landing; the agent-cap fold it was waiting on is built here.

**Read the spec's rev-5 revision-log entry before changing this code** — it records the one design
correction the build made against the spec (slots, not a count) and the two predicate defects caught
by running the new gate over the real tree first.

Records live under `spec/`, `build/` and `reviews/`. The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-08-10 · streams tooling · ids TOOL-aNumeralWarden-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aNumeralWarden-1 — agent-cap enforces the verifier number, and reaches the modality it was blind to](spec/2026-08-10-spec-aNumeralWarden-1.md) | INPROGRESS | rev-5 | 2026-08-10 |
<!-- /gen:build-index -->
