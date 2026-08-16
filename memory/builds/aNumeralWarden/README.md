---
slug: aNumeralWarden
node: a
opened: 2026-08-10
streams: tooling
roster: TOOL
ids: TOOL-aNumeralWarden-1 TOOL-aNumeralWarden-2 TOOL-aNumeralWarden-3 TOOL-aNumeralWarden-4
---

# aNumeralWarden — agent-cap reads the number, and the two caller-settable knobs go away

Node `a` · opened 2026-08-10 · streams tooling.

## Start here

**State.** CLOSED at rev-6. Landed on `origin/main` as merge `990f07b`, full bar green inside the
lander; S16 follows. The Rollout commits, each gated on the branch first: `3086cab` (S1-S13, the
bound-reading predicate) · `fb29755` (S14, the matcher widening) · `3aec132` (S15, the runtime count).
Every acceptance criterion AC1-AC29 is observed. All four §8 forks are resolved.

**What ships.** `agent-cap` 1.4: it resolves the bound at the call site, at the helper's default
parameter and at the `gov:bounded-fanout` width; refuses a set `AGENT_CAP`; counts direct `Agent`
spawns at 5 per user prompt; and admits a lens array of at most 5. Also moved: `settings-merge` 1.1,
`drift-audit` 1.1 (a narrowed `args` contract, with a migration paragraph in its README).

**One number, and it took a miscount to see it.** F2 asked why `MAX_LENSES` was 6 while everything
else was 5. The owner ratified 5 — against this spec's recommendation — and that turned out to be
right for a reason nobody had: the 6 was never a decision. The array counter scored a trailing comma
as an element, so every prettier-formatted 5-lens array measured 6 and the constant had been raised
to fit the error. Fix the count, and 5 is what every shipped harness already obeys.

**AC22 was measured, and it answered YES.** `PreToolUse` does fire for a direct `Agent` spawn,
`tool_name` is exactly `Agent`, and `session_id` / `prompt_id` / `tool_use_id` are all present. The
`SubagentStart` fallback does not apply and was not built. §8 F4 carries the evidence, including the
liveness probe that had to run first — settings ARE re-read mid-session, so the measurement could not
have been a false negative.

**What downstream can now proceed.** `TOOL-aUnmannedHelm-1` declared a dependency on this unit
landing; the agent-cap fold it was waiting on is built here.

**Read the spec's rev-5 and rev-6 revision-log entries before changing this code.** Between them they
record the design correction the build made against the spec (slots, not a count) and all four
instances of one root cause — a trailing comma read as an element — which bit the call-site walk, the
lens counter, and this spec's own non-goal.

The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-08-10 · streams tooling · ids TOOL-aNumeralWarden-1 TOOL-aNumeralWarden-2 TOOL-aNumeralWarden-3 TOOL-aNumeralWarden-4

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aNumeralWarden-1 — agent-cap enforces the verifier number, and reaches the modality it was blind to](spec/2026-08-10-spec-aNumeralWarden-1.md) | CLOSED | rev-6 | 2026-08-10 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-10-spec-aNumeralWarden-1.md](spec/2026-08-10-spec-aNumeralWarden-1.md)
- **`reviews/`**
  - [2026-08-10-review-aNumeralWarden-1.md](reviews/2026-08-10-review-aNumeralWarden-1.md)
  - [2026-08-10-review-aNumeralWarden-2.md](reviews/2026-08-10-review-aNumeralWarden-2.md)
<!-- /gen:build-docs -->
