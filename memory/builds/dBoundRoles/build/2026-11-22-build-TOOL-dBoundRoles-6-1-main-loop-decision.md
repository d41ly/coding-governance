**Serves:** journal TOOL-dBoundRoles-6

# TOOL-dBoundRoles-6 — the main loop's decision over the first builder's divergence

The spec-fix handoff rendered for this divergence
(`prompts/2026-11-22-prompt-TOOL-dBoundRoles-6-fix-1-spec-writer.md`) could not be spawned. TOOL-dBoundRoles-17 now
writes `item=` on every rendered marker, and this session's spawn guard is the primary tree's
`tools/hooks/agent-cap.js`, which predates that unit and refuses the new marker under rule 6. A role agent the unit
harness spawns is not refused, so the build continues through the harness, and a spec writer cannot run directly
until the run lands.

So the main loop decides the return's items by M3 as delegated resolutions, and the next builder builds them as
recorded deviations in its own pass. widens: none · relaxes: none.

1. The write set names the `kit.policy` change record, `help/policy.md`, `help/roles.md`, `help/red-fix-lane.md` and
   `tools/policy/README.md`; the pass updates each page and the README's guard section and case count for what S2,
   S3, S5 and S6 change, as the docs rule owes.
2. The builder re-grounds every `tools/hooks/agent-cap.js` citation at HEAD, which TOOL-dBoundRoles-17 changed.
3. `tools/roles/handoff.py#extract_drive_lines` and the role half of `#render_work_order` move into
   `tools/roles/roles_lib.py`, and `handoff.py` imports them back, so `render_role_section` needs no import of
   `handoff.py` and the logic stays in one core. The template read takes the kit directory it is handed, so the
   renderer's ranked selftest keeps passing over its fixture kit.
4. `tools/policy/guard.py` carries its own inlined `resolve_kit_dir`, the shape every copy-installed kit uses, since
   its header forbids importing `policy.py`.

The builder writes one deviation record carrying items 1, 3 and 4 against the spec at rev-7.
