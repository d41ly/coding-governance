**Serves:** journal TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15

# Spec handoff — the closing review's promotions

## Role

You are a code architect writing the specification for four small units, each closing findings a
closing review confirmed. You are not writing any code right now. A builder will build from your
spec alone. Each unit's design is the narrowest change that closes its findings at the CLASS, not
just the instance, and seams into the code the build already wrote. Verify every claim about
current code by reading it, and cite path and line. A choice you cannot derive is a fork, resolved
by M3 of the build method and marked `RESOLVED (agent, 2026-10-12, delegated)`. You run no gate and
no self-test; the only checks you may run are memory hygiene and the lexicon. You write only the
four spec files. You do not commit, and you do not regenerate any index.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**The findings:**
`memory/builds/aOrientedCast/reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md`.
Read each item you are handed whole, its `fixVerdict` and the skeptic's corrected fix included. A fix
the skeptic called unsound is NOT the design; its correction is the starting point.

**Also read:** `memory/guides/BUILD-METHOD.md`, then the "Invariants for every unit" in
`memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`, which
bind you. Then read the CLOSED specs whose code each unit changes.

**The four specs**, all under `memory/builds/aOrientedCast/spec/` with the filename
`2026-10-12-spec-TOOL-aOrientedCast-<n>.md`. Each is status `OPEN`, `rev-1`, `node a`, base
`646d4a73581393acbf42f33864a9808c96d00a0c`, `streams tooling`. Each carries a `closes` header verb
naming its review item ids as the review spells them, and the order shown here:

| Unit | Order | Tier | Closes | Mechanism |
|---|---|---|---|---|
| TOOL-aOrientedCast-12 | 12 | Tier-1 micro-spec, per `memory/TEMPLATE-SPEC.md` | H1 and M1 | the `roles render selftest` row in `tools/run-gates/selftest-budgets.txt` gets its empty argv column. The class also gets a check: a budgets row whose argv column holds prose is refused, wherever the file's reader or its existing check parses rows. Find the seam rather than adding a new script. |
| TOOL-aOrientedCast-13 | 13 | Tier-2 | H2 | the seeded `tools/roles/house/policy.toml` names the `lexicon naming predicates` leg, which a default adopter install does not hold, so the roles catalogue and render red there. Design how a gate allowlist names a leg that may be absent in a target: tolerate it as a note, or name it by something every install holds. Choose by M3. |
| TOOL-aOrientedCast-14 | 14 | Tier-2 | M2 and M3 | the two hooks findings. `scanCommandHeads` in `tools/hooks/scratch-guard.js` must step past every launcher option and option argument (`bash -o pipefail`, `bash -e -x`, `python -X utf8`, `env -u FOO`) and rescan a `-c` body. Rule 6 in `tools/hooks/agent-cap.js` and `checkRoleGate` must anchor on `CLAUDE_PROJECT_DIR` before the payload cwd, as `checkRouted` already does. |
| TOOL-aOrientedCast-15 | 15 | Tier-2 | M4, M5, L1, L2 and L3 | the remaining minors, batched as M4 of the build method orders. Its write set must not intersect TOOL-aOrientedCast-14's. |

Each new arm names its staged break. Its red-first observation is the main loop's at the close,
because builders run no gate.

**Return:**
- `authored`: the four paths;
- `forks`: each fork with the option taken;
- `refused`: any finding you could not specify, with why;
- the memory hygiene exit status over your four files, if you ran it.
