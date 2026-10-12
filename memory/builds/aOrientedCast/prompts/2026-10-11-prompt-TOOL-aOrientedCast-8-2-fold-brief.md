**Serves:** journal TOOL-aOrientedCast-8

# Fold handoff — TOOL-aOrientedCast-8's builder found a fork the spec did not state

## Role

You are a software architect maintaining one unit specification. You write no product code. You
change the spec only where this handoff names it, as a `rev-N` bump with its `§9` line, and you mark
the fork in place in the shape `memory/TEMPLATE-SPEC.md` §8 states. Leave every other sentence
alone, and return only what the return contract asks for.

## Task

**Spec:** `memory/builds/aOrientedCast/spec/2026-10-11-spec-TOOL-aOrientedCast-8.md`, rev-3, in
`C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**What the builder observed.** It ran a default `plan` and `apply` from `DEPLOY_REGISTRY_DEFAULT`
into a scratch target, where the playbook lands at `docs/PARALLEL.md`. The memory-tree seed there
writes `CHARTER="AGENTS.md"`, and no `AGENTS.md` exists. The roles adopter's `--scaffold` then
printed `render_agents: ... R0 — CHARTER names AGENTS.md, which is not a file` and exited 1, which
S4's exit table calls correct. But S5 declares only `[[outcome]] code = 0`, and govkit fails an
apply whose adopter exits with no declared outcome (`tools/govkit/govkit.py` near line 7750). So
every default install without a governing doc at `CHARTER` fails, and AC4's nine agent types cannot
be observed in the shape-6 fixture.

**Resolve it as a new fork, marked `RESOLVED (agent, 2026-10-11, delegated)` to option 1:**
1. **Taken.** The adopter treats an absent governing doc as a DECLARED outcome. It still renders the
   `/build` Skill, skips the agent types and the role index, prints one line naming the missing doc
   and the conf key, and exits with a new code that S5 declares as an `[[outcome]]`.
   `check-wiring`'s roles arm (S8) reports `UNWIRED roles` naming the same doc.
2. **Rejected: deriving `CHARTER` from the playbook's path in the memory-tree seed or in govkit.**
   That changes another kit's install behaviour, a public surface M3's veto 2 keeps for the owner.
   File it as a §3 Edge `hands-off` for an ask.
3. **Rejected: a governing doc declared only in the AC3 and AC4 fixtures.** Real adopters stay
   broken.

Amend S4's exit table, S5's outcomes, S8 and AC4 to match. Add an acceptance criterion: in the
shape-6 fixture with no doc at `CHARTER`, the default `apply` succeeds, the Skill is rendered, no
`.claude/agents/` file is written, and `check-wiring` prints the UNWIRED line. Its red half is the
adopter at rev-3 behaviour, which the builder already observed failing the apply.

**A second fact to write into §6's preamble.** `govkit apply` copies gov's COMMITTED bytes into the
target, so AC3, AC4 and the new criterion are observable only after the pass commit. They are
observed against the committed tree, and their ledger lines land in a follow-up commit carrying
`Pass: none`. Say so, and say that this is the one unit of the build whose acceptance follows its
commit.

**Rules.**
- No product code.
- No commit: the main loop commits after you return.
- Do not run the build-index generator.
- No merge bar, and no `*.test.sh` suite.
- Run `python tools/check-spec-tokens.py` once at the end.

**Return:**
- `folded`: the new rev and what moved;
- `forks`: the fork's id and the option taken;
- the `check-spec-tokens.py` exit status.
