# TOOL-dBoundRoles-19 widen 20 — dead-path-waivers widened

**Serves:** widen TOOL-dBoundRoles-19

- **Population:** dead-path-waivers
- **Keys:** `.governance/steps/roles/house-overlays-to-instructions.before.json	"tools/roles/house/gov-session.md": {`, `{prefix}/roles/kit.toml	"file:{prefix}/roles/house/gov-session.md", "file:{prefix}/roles/house/gov-skeptic.md",`, `{prefix}/roles/kit.toml	"installable:{prefix}/roles/house/gov-session.md", "installable:{prefix}/roles/house/gov-skeptic.md",`
- **Reason:** the before-image of gov's own house step names the house texts it restores, and the house step row names, on its surfaces key, the files an adopter's install loses, which is what the step gate reads them by
- **Caused-by:** TOOL-dBoundRoles-19
