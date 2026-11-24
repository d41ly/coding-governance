# TOOL-dBoundRoles-18 widen 19 — dead-path-waivers widened

**Serves:** widen TOOL-dBoundRoles-18

- **Population:** dead-path-waivers
- **Keys:** `.governance/install.json	"path": "tools/roles/agents/gov-diff-reviewer.agent.md",`, `.governance/install.json	"source": "tools/roles/agents/gov-diff-reviewer.agent.md"`, `.governance/install.json	"path": "tools/roles/agents/gov-spec-reviewer.agent.md",`, `.governance/install.json	"source": "tools/roles/agents/gov-spec-reviewer.agent.md"`, `.governance/install.json	"path": "tools/roles/house/gov-diff-reviewer.md",`, `.governance/install.json	"source": "tools/roles/house/gov-diff-reviewer.md"`, `.governance/install.json	"path": "tools/roles/house/gov-spec-reviewer.md",`, `.governance/install.json	"source": "tools/roles/house/gov-spec-reviewer.md"`, `{prefix}/roles/kit.toml	"installable:{prefix}/roles/agents/gov-spec-reviewer.agent.md",`, `{prefix}/roles/kit.toml	"installable:{prefix}/roles/agents/gov-diff-reviewer.agent.md"]`
- **Reason:** gov's own source-mode receipt is written by the deployer and never by hand, so it names the two reviewer agents and their house texts until gov's next apply; and the reviewers step row names, on its surfaces key, the paths an adopter's install loses, which is what the step gate reads them by
- **Caused-by:** TOOL-dBoundRoles-18
