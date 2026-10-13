# TOOL-aOrientedCast-16 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-16

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: `python -c` and
scratch-script probes of `roles_lib.parse_charter`, `check_rule_tags` and `render_charter_blocks`
over `AGENTS.md` and inline texts; `check_roles.check_roles` called as a function over gov and over
a copy of the kit under a short `%TEMP%` path with one staged break at a time; two `git init`
repositories under `%TEMP%`, each holding a copy of the kit, a conf and a charter, where the copy's
`render_agents.py --write` and `--check` ran; `handoff.py render --stdout --part task` from gov's root;
and the three `git grep` lines of AC7 over `tools/roles`. The rendered agent types shrink from
117717 bytes (gov's current `.claude/agents/gov-*.md`) to 45979 (the scratch render). Owed to the
main loop: the re-render pass this unit's brief names — `render_agents.py --write` into gov's
`.claude/agents/` (with `.claude/roles.json` byte-identical) and `adopt-roles.sh --scaffold` for
`.claude/skills/build/SKILL.md`, after which `render_agents.py --check` exits 0 and AC7's grep over
`.claude/skills/build .claude/agents` prints nothing; then at the close (M8) the three `New arm:`
lines of §7, each RED on its staged break and GREEN restored (render self-test arms 4, 14 and 15,
the checker's R4 and R5 breaks, the wiring leg's staged rule-line edit), and every leg §7 lists.

The re-render pass ran at the main loop, declared at `b61ec1c4`: `render_agents.py --write` wrote the
nine types and left `.claude/roles.json` byte-identical, `adopt-roles.sh --scaffold` re-rendered
`.claude/skills/build/SKILL.md`, `adopt-roles.sh --check` exited 0, `check_roles.py` exited 0 against
`AGENTS.md` as a tagged charter, and AC7's grep over `.claude/skills/build .claude/agents` printed
nothing. The `New arm:` observations remain owed at the close.

**Evidences:** TOOL-aOrientedCast-16
- AC1 — `parse_charter` — over `AGENTS.md` it returned shape `tagged` with the 44 tags the probe's own `^- \[([a-z0-9][a-z0-9-]*)\] ` match found in section 1, each mapped to its whole line in the same order, and carried `Protocols — read the one whose trigger holds` then `Facts`, each body a substring of the file ending on the line before the next `## ` heading or `<!-- /gov:playbook -->`.
- AC2 — `render_charter_blocks` — `parse_charter` returned `legacy` with no rules and nothing carried for a `## §1 — One` / `## §2 — Two` text, and raised `RolesError` naming R0 for a doc of neither shape, a tagged doc without `## Facts` (naming `Facts`) and one repeating `[one]` (naming `one`); `yagni, nope` raised naming R4 and `nope`; `yagni, nope?` returned the yagni line and the carried blocks with one note naming `nope?`; the legacy structure returned an empty string.
- AC3 — `check_roles.check_roles` — over gov it returned no defect and a summary of 55 rule tags and 5 protocol file names against `AGENTS.md`, a tagged charter; over the kit copy, `nope` appended to `gov-builder`'s `rules` gave exactly one R4 line naming `nope` and `gov-builder.agent.md` (beside the copy README's R11), `BUILD-METHOD.md` in `gov-spec-writer`'s body exactly one R5 line, and in `gov-skeptic`'s overlay exactly one R10 line; a scratch root charter without its `[cross-os]` line gave no defect and one `roles: note:` line for each of the two roles citing `cross-os?`, `gov-builder` and `gov-diff-reviewer`.
- AC4 — `render_agents.py --write` — in a `git init` repository whose `CHARTER` holds `git show 646d4a73:AGENTS.md`, the copy's render exited 0, printed exactly one `render_agents: note` line carrying `reseed` and naming `AGENTS.md`, and wrote no type carrying `## Charter`; `check_roles.check_roles` there returned no R4 line and one `roles: note:` line with the same text.
- AC5 — `render_agents.py --check` — in a scratch repository holding a copy of gov's kit and `AGENTS.md`, `--write` then `--check` exited 0; every type's text after its front matter equalled `render_role` plus `## Charter` plus `render_charter_blocks` byte for byte, `gov-builder.md` carried the `- [cross-os]` line, and no type carried `### charter §`; rendering every slot against the charter and against its `[verify]` line one word longer moved exactly the six slots whose `rules` cite `verify`. Gov's own `.claude/agents/` render is the re-render pass's, as the paragraph above states.
- AC6 — `handoff.py render` — `--role gov-researcher --build aOrientedCast --unit TOOL-aOrientedCast-16 --input question=probe --stdout --part task` exited 0, its output ended with `render_charter_blocks`'s text for `gov-researcher` and its trailing newline, and it carried no `### charter §` block; the spawn guard's admission is the `roles adopter self-test` leg's arm 6, owed at the close.
- AC7 — `rules:` — `git grep -n -E '^charter:' -- tools/roles/agents` and the protocol-file grep over `tools/roles/agents tools/roles/house` printed nothing, each role file's `rules:` line equals its row of §4 "The role files", and the section-number grep printed nothing over `tools/roles`; its `.claude/skills/build .claude/agents` half is owed by the re-render pass.
