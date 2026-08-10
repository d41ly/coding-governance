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

**State.** One unit, SPECCED at rev-4, reviewed twice: a full Tier-2 at rev-2 and a scoped Tier-2 on
the folded-in S14 at rev-4. Nothing is built.

**Next action.** Commit 1 of the three-commit rollout — scope items S1 through S13, the
bound-reading predicate — is buildable now and depends on nothing outside this repo.

**Before S15, run AC22 first.** S15 assumes a `PreToolUse` hook fires for a direct `Agent` spawn,
and that is NOT established: the hook documentation does not enumerate matchable tool names, and it
documents a separate `SubagentStart` event which explicitly cannot block. Measure it with a
throwaway hook before writing any S15 code. F4 in the spec carries the fallback.

**Four forks are open** in section 8 of the spec, including F4 above. None blocks commit 1.

**No blocking dependency.** The earlier cycle with `TOOL-aUnmannedHelm-1` was dissolved at rev-4 by
making S15 an atomic count that reads no run-state file.

Records live under `spec/`, `build/` and `reviews/`. The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node a · opened 2026-08-10 · streams tooling · ids TOOL-aNumeralWarden-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aNumeralWarden-1 — agent-cap enforces the verifier number, and reaches the modality it was blind to](spec/2026-08-10-spec-aNumeralWarden-1.md) | SPECCED | rev-4 | 2026-08-10 |
<!-- /gen:build-index -->
