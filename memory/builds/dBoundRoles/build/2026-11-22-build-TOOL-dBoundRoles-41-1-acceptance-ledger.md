**Serves:** journal TOOL-dBoundRoles-41

# TOOL-dBoundRoles-41 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `fe9b73c83`. The render probes ran `tools/roles/handoff.py render` in a git
fixture repository under the host temp folder, holding a copy of this tree's roles, loop and playbook-register files
with the roles kit scaffolded by its adopter, the policy kit absent, and a build folder `tFix` whose scratch spec's
prose, outside any fence, quotes `cmd:<command>` and a well-formed example `blob:` key; the base renders ran a copy
of `tools/roles/handoff.py` as it stands at that base, beside the changed one. No gate, suite or bar ran in the
pass: arm 40 of `tools/roles/adopt-roles.test.sh`, the arm the spec's `New arm:` line declares, its RED-first
observation, and the legs its gate line lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-41
- AC1 — `--input spec=` — `render --role gov-builder --build tFix --unit TOOL-tFix-1` handing the scratch spec exited 0 and wrote `2026-11-23-prompt-TOOL-tFix-1-2-builder.md`; the base copy exited 0 on it too, the spec's spans sitting inside the handed fence of `TOOL-dBoundRoles-38`. Under a card whose route quotes the same two spans, the base copy exited 1 naming ``anchor `cmd:<command>` — malformed`` and the example key as resolving to no handed fact, and the changed render exited 0. The graded text is built in `tools/roles/handoff.py#render_handoff`. OWED: arm 40's AC1 assertions and their RED-first observation, `render_handoff` passing the whole section to `check_anchors`, at the close.
- AC2 — `--input question=` — `render --role gov-orienter` with `--input prompt=` naming the scratch spec and a question holding the backticked `record:memory/nowhere.md@0123456789ab` exited 1, its stderr naming that anchor as resolving to no fact this work order hands, and the prompts folder held no new file; with the anchor removed it exited 0. OWED: arm 40's AC2 assertion and its RED-first observation, a graded text dropping the typed value, at the close.
- AC3 — `## Task` — the AC1 render's prompt file and the base copy's file of the same inputs hold equal `## Task` bytes and the equal marker field `task-sha=5e9103034148`; the orienter render, the skeptic's render with a typed diff, the item render of a fixture `[[item]]` row and the prompt writer's `--for gov-builder` render each printed the same bytes through both copies. AMENDED by `TOOL-dBoundRoles-50` S7 and S8: inside one render of the current kit, the `## Task` the marker hashes is the composition `render_work_order_section` returned from the opening, practices and reads parts `render_handoff` appended, and `handoff.derive_section_sha` of the written section equals the marker's task-sha; across this unit's change, the kits at `fe9b73c83` and at `cf8515f98` rendered equal `## Task` bytes and task-sha `f907a5631c66` for a span-free spec and a typed question, as the acceptance ledger of `TOOL-dBoundRoles-50` records.
- AC4 — `grep -n "graded" tools/roles/README.md` — names, on the paragraph **Anchors resolve to handed facts**, the graded text `render_handoff` passes to the check, the authored text it grades with a typed `--input` value among it, and the handed content left out of the graded text, each handed block keeping its heading and fact line.
