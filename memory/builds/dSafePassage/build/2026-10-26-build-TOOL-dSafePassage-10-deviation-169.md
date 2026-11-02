# TOOL-dSafePassage-10 deviation 169 — a class row spells its functions' path through `{prefix}`

**Serves:** deviation TOOL-dSafePassage-10

- **Departs from:** TOOL-dSafePassage-10@rev-4 [§4 "Data model"]
- **Hand-off:** spec-to-code
- **Before:** `reader = "govkit/step_gate.py:read_agent_members"`, a bare `<path under the tool root>:<function>`.
- **After:** `reader = "{prefix}/govkit/step_gate.py:read_agent_members"`, the same path under the tool root spelled through the `{prefix}` token, resolved by govkit's `resolve_prefix_token` at load; `plant` and `witness` alike.
- **Cause:** builder discovery
- **Reason:** `tools/check-install-prefix.sh` counts a kit segment followed by a file under any literal lead in every tracked file under the tool root, and drains only the render tokens, which is why the registry spells each descriptor `{prefix}/<kit>/kit.toml`. The bare spelling would red that leg on all 18 function paths.
- **Evidence:** `tools/govkit/surface-classes.toml`, and this unit's acceptance ledger, AC1: `--list` loads every row's reader and plant through the token.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-10, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-10
