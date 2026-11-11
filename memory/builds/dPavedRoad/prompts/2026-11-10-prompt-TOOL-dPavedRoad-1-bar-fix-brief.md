**Serves:** research TOOL-dPavedRoad-1

# Brief: TOOL-dPavedRoad-1's install-prefix red

## The brief

### Goal
The merge bar at `d08106d4d` reds on `install-prefix (shipped surface)`: `tools/roles/agents/gov-spec-writer.agent.md:37` spells the kit path `tools/check-spec-tokens.py` in the role text this unit added. The leg is a pure ban with no waiver, because `govkit apply` writes the role bytes verbatim and the path resolves to nothing at an adopter installed at another prefix. Respell that sentence so it names no kit path, keeping its meaning: the writer runs the spec-token checker's `--spec` mode over each spec it wrote, where the repository has it. Then re-render with `python tools/roles/render_agents.py --write` so `.claude/agents/gov-spec-writer.md` carries the same bytes, and keep the spec's AC7 true (its count of the sentence in each of its two files).

### Items
1. **TOOL-dPavedRoad-1 — writers self-check spec tokens.** `tools/check-spec-tokens.py --spec <path>` grades that one spec as if it were live, whatever its status, and `tools/roles/house/policy.toml` adds the spec-tokens leg to `gov-spec-writer`'s gates.

### Acceptance
`grep -n 'tools/check-spec-tokens' tools/roles/agents/gov-spec-writer.agent.md .claude/agents/gov-spec-writer.md` prints nothing; `python tools/roles/render_agents.py --check` exits 0; the spec's AC7 count still reads 1 in each file, or the spec's AC7 wording names the new spelling.

### Gates
`bash tools/run-gates/run-gates.sh`, legs from `tools/gate-legs.json`.

### Non-goals
No change to `--spec`'s behaviour, to the policy grant, or to any other role's text.
