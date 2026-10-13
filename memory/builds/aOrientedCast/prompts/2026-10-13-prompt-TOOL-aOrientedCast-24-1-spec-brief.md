**Serves:** journal TOOL-aOrientedCast-24 TOOL-aOrientedCast-25

# Spec handoff — the second closing review's promotions

## Role

You are a code architect writing the specification for two batched units, each closing the
findings a closing review confirmed. You write no code. A builder builds from your spec alone. Each
fix closes its finding's CLASS, not just the instance, and seams into the code this build wrote.
Verify every claim about current code by reading it, and cite path and line. A choice you cannot
derive is a fork, resolved by M3 of the build method and marked `RESOLVED (agent, 2026-10-13,
delegated)`. You run no gate and no self-test; the only checks you may run are memory hygiene and
the lexicon. You write only the spec files of the units your roster names. You do not commit, and
you do not regenerate any index.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**The findings:**
`memory/builds/aOrientedCast/reviews/2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md`.
Read each item you are handed whole, with its `fixVerdict` and the skeptic's reasoning in the
appendix.

**Also read:** `memory/guides/BUILD-METHOD.md`; the "Invariants for every unit" section of
`memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`, which
binds you except for its order table; and the CLOSED specs whose code each unit changes, which are
TOOL-aOrientedCast-16 to -22 under `memory/builds/aOrientedCast/spec/`.

**The two specs**, under `memory/builds/aOrientedCast/spec/`, named `2026-10-13-spec-<unit id>.md`.
Each is status `OPEN`, `rev-1`, `node a`, base `646d4a73581393acbf42f33864a9808c96d00a0c`, Tier-2,
`streams tooling`. Each carries a `closes` header verb naming its review item ids as the review
spells them, and the order shown:

| Unit | Order | Closes | Scope |
|---|---|---|---|
| TOOL-aOrientedCast-24 | 26 | M1, M2, M3, M7, L1, L2, L3 | `tools/hooks/format-guard.js` reads tool-use ids only from a notification's header, never its result body; its turn scan skips the harness's mid-turn meta and compaction records; `tools/unattended/gate-guard.js` allows a question once the session's run has landed or aborted in place; the missing arms and the two docs that misstate behaviour |
| TOOL-aOrientedCast-25 | 27 | M4, M5, M6, L4, L5, L6, L7 | the marker line normalised one way in `tools/roles/handoff.py` and `tools/hooks/agent-cap.js`, put in one place per [one-fact]; fixture arms for check_roles R13 to R15, the stand-in refusal and `agents --run`; the third micro-format fence reader made to agree, or reduced to a call of the one reader; spec 21's AC2 and spec 22's AC6 corrected as ledger amendments, since a CLOSED spec is not edited; the roles dossier |

The two write sets must stay disjoint, so both units can be built without one editing the other's
files. If M4's fix must touch `agent-cap.js`, that half of M4 belongs to TOOL-aOrientedCast-24:
say so, and adjust both `closes` lines.

**Kit versions:** each unit bumps the kits it moves, once. TOOL-aOrientedCast-24 moves the hooks
kit (1.36 to 1.37) and the unattended kit (1.105 to 1.106). TOOL-aOrientedCast-25 moves the roles
kit (1.3 to 1.4). Read the carriers from `tools/check-kit-versions.sh` without running it.

**The agent-cap dossier** at `memory/map/features/agent-cap.md` sits within a few bytes of its cap.
A unit that adds to it splits it first, in the shape the map kit's README names.

Each new arm names its staged break. Its red-first observation is the main loop's at the close,
because builders run no gate.

**Return:**
- `authored`: the paths you wrote;
- `forks`: each fork with the option taken;
- `refused`: any finding you could not specify, with why;
- the memory hygiene exit status over your files, if you ran it.
