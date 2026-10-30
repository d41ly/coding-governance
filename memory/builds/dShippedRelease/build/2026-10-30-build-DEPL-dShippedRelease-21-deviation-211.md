# DEPL-dShippedRelease-21 deviation 211 — the clause's consumer list corrected from source, and govkit marked not installable beside lib

**Serves:** deviation DEPL-dShippedRelease-21

- **Departs from:** `cl-dClosedLoop-0431@3ef16038`
- **Hand-off:** design-to-spec
- **Before:** a `kit.toml` for govkit and lib, lib's marked not installable, and each `*/kit.toml` consumer naming how it treats one: `regen.py`, `check-kit-placeholders.py`, `run-gates.sh`, `check-hook-destinations.sh`, `render_playbook.py` and govkit's descriptor checks
- **After:** the kit factory's purpose field and a `kit.toml` for govkit and lib, today's kits reviewed, lib's and govkit's marked not installable and each `*/kit.toml` consumer naming how it treats one, two of them reading the registry and not that glob: `regen.py`, `check-kit-placeholders.py`, `run-gates.sh`, `check-hook-destinations.sh`, `render_playbook.py`, govkit's descriptor checks, `lib-unattended.sh`, `render_agents.py` and `map_extractors.py`, each consumer's leg run on a tree with both descriptors and one seen red on a planted lib descriptor (DA-M16, FM10)
- **Cause:** design defect
- **Reason:** two named consumers do not read the glob the clause says they read, so the clause's own word is wrong about them, and three unnamed readers of a descriptor or a tool directory would otherwise stay ungraded. Marking lib alone would put the deployer in `--all` once it has a descriptor, though the registry already says it is never installed into a target. Both changes keep the clause's intent and tighten it; neither loosens a seen-red case. Also follows through as: ask DEPL-dShippedRelease-32.
- **Evidence:** `tools/check-hook-destinations.sh:112`, `:138`; `tools/playbook/render_playbook.py:806-810`; `tools/unattended/lib-unattended.sh:857`; `tools/roles/render_agents.py:171-195`; `tools/codebase-map/map_extractors.py:85`; `tools/govkit/registry.toml:301`; `tools/govkit/govkit.py:908`
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer stage of the harness's spec run for dShippedRelease, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0431@3ef16038
- **Caused-by:** cl-dClosedLoop-0431@3ef16038
