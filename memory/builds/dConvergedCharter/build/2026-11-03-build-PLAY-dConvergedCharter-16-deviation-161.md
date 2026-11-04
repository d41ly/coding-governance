# PLAY-dConvergedCharter-16 deviation 161 — the kickoff engine's text ships per repository in its kit when the `/session-kickoff` Skill retires

**Serves:** deviation PLAY-dConvergedCharter-16

- **Departs from:** cl-dClosedLoop-0490@166e1002
- **Hand-off:** design-to-spec
- **Before:** the `/session-kickoff` Skill retired once the orientation scout and `kickoff.runs` have landed, `manifest-check.sh` and its fragments moved to a kit home of their own, a forwarding stub in `skills/session-kickoff/` for `install.deprecation-window` releases, then the directory removed.
- **After:** the same, and the engine's procedure, the Skill's body below its front matter, moved with them into the kit home as `KICKOFF-ENGINE.md`, shipped by the `kickoff-manifest` entry to each repository at `{prefix}/KICKOFF-ENGINE.md`, which the orientation scout and an inline orientation read in place of the Skill.
- **Cause:** design defect
- **Reason:** the clause retires the Skill once the orientation scout has landed, and the scout as specced runs "the engine's Steps 0 to 4" by loading the Skill (TOOL-dFurnishedOrders-1 S7, S8; `tools/roles/agents/gov-orienter.agent.md:30`), so retiring the Skill with its text leaves the scout no engine. PLAY-dConvergedCharter-16 §8 F2 weighed three homes: the kit file, which serves the scout and the inline orientation TOOL-dFurnishedOrders-1 S8 keeps; the scout's own definition, which a repository without the roles kit never receives; and an ask on dFurnishedOrders, which parks the clause. The kit file moves the text's install location from a machine link to a file in each repository's prefix, a veto-2 change no clause names, so the standing ruling takes it.
- **Evidence:** the clause, `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:36`; the scout's load, `tools/roles/agents/gov-orienter.agent.md:30`, `tools/workflows/orient.agent.md:23`, `tools/workflows/orient-counterfactual.js:102`; the entry's machine-scoped link row, `tools/govkit/entries/kickoff-manifest.kit.toml`; rung 5, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dConvergedCharter's spec run, citing ER:388, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0490@166e1002
- **Caused-by:** PLAY-dConvergedCharter-16
- **Surface:** the engine text's install location, from the machine's `{user_skills}/session-kickoff` link to `{prefix}/KICKOFF-ENGINE.md` in each repository
