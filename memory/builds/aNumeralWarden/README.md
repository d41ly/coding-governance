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

**State.** One unit, BUILT at rev-5 on `branch/anumeralwarden-build-setup-b48e83`. All three Rollout
commits landed on the branch, each gated by the full bar: `3086cab` (S1-S13, the bound-reading
predicate) · `fb29755` (S14, the matcher widening) · `3aec132` (S15, the runtime count). Every
acceptance criterion AC1-AC27 is observed.

**Next action: the merge ask.** The branch is complete and green; merging to `main` and pushing each
need an explicit owner ask, so nothing has landed on `main`. Nothing else in this build is pending.

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
