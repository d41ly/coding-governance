# TOOL-aOrientedCast-11 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-11

Direct checks only: under the owner's rule for this run, the rule this unit encodes, no gate, suite,
slice or self-test ran in this pass. What ran: a hand probe in the run's scratch directory that
pipes the spec's §4 payloads, built as JSON, into `node tools/hooks/scratch-guard.js` from this
worktree (36 payloads) and from a scratch repository under a short `%TEMP%` root (AC3, 4 states),
reading each exit code and stderr; a staged throw in a scratch copy of the hook for S6, which
refused the `gov-builder` payload naming the throw and admitted the main loop's; a `python` probe of
`load_policy`, `render_agents.py --check` and `check_roles.check_roles` over a scratch copy of the
kit with the builder's leg name staged to `nope` and restored; parse-only checks (`node --check`,
`bash -n`, `ast.parse`); the renders (`render_agents.py --write`, `adopt-memory-tree.sh --render`,
`check-protocol-parity.test.sh --render`, `gen_map.py --write`); and the lexicon. RED first: the
same 36 payloads against the parent's hook (`git show HEAD:tools/hooks/scratch-guard.js`) failed
all 13 refusals, each exiting 0 where the arm wants 2, and passed the 23 admissions; against the
pass's hook all 36 passed. Owed to the main loop at the close (M8): the two `New arm:` lines of §7,
the 32 `run_role_bash` arms of `scratch-guard.test.sh` under `scratch-guard self-test`
(`FLOOR_ASSERTIONS` moved 260 to 292 by a hand count, not a run) and arm 12 of
`render_agents.py --selftest` under `roles render selftest`, each RED on its staged break and GREEN
restored; and every leg §7 lists, `kit epoch` and `kit-versions` among them for the four bumps.

**Evidences:** TOOL-aOrientedCast-11
- AC1 — `node tools/hooks/scratch-guard.js` — from this worktree after the render, every REFUSED payload exited 2 for `gov-builder` naming `G2 runner`, `G3 suite`, or `G1 leg` with `roles catalogue` for the `check_roles.py` line, the PowerShell line included; the hygiene line exited 0 for `gov-spec-writer` and 2 for `gov-builder` and `workflow-subagent`; the lexicon line exited 0 for `gov-builder` and `gov-spec-writer` and 2 for `gov-skeptic`; every line exited 0 with no `agent_type`.
- AC2 — `node tools/hooks/scratch-guard.js` — every NEAR-MISS payload exited 0 with empty stderr: seven for `gov-builder`, from `gotchas.py --for-diff` to the commit message naming the bar, and `manifest-check.sh --card --path` for `gov-orienter`.
- AC3 — `gates.manifest` — in a scratch repository under `%TEMP%`, the bar-runner payload for `gov-builder` exited 0 with no index; with an index holding `{` it exited 2 naming the index and `is not JSON`, while `ls` exited 0; with an index whose `gates.manifest` named no file, `python tools/roles/check_roles.py` exited 0 with one witness line naming `G1 leg unarmed`, and the runner line still exited 2 naming `G2 runner`.
- AC4 — `nope` — after `python tools/roles/render_agents.py --write`, a `json.load` of `.claude/roles.json` held `gates.manifest` `tools/gate-legs.json`, the two names for `gov-spec-writer`, the one for `gov-builder` and an empty list on every other role; with the builder's entry staged to `nope`, `load_policy` raised naming it, `render_agents.py --check` exited 2, and `check_roles.check_roles` over a scratch copy of the kit returned one R12 defect naming it; restored, `--check` exited 0.
- AC5 — `python tools/roles/render_agents.py --check` — `grep -c "selftest. flag, a fixture"` printed 0 over `unattended-unit.js`, `unattended-build.template.js`, `gov-builder.agent.md` and `gov-spec-writer.agent.md`; `render_agents.py --check` exited 0 grading 9 agent types and 1 index; a second `check-protocol-parity.test.sh --render` moved no byte of `unattended-build.js`.
- AC6 — `last-audit` — `wc -c memory/guides/BUILD-METHOD.md` printed 29157; `grep -c "New arm:"` printed 1; the method was rendered from its template by `adopt-memory-tree.sh --render`, so both carry the same M6 and M8 sentences; the `last-audit` line of `memory/guides/SESSION-KICKOFF.md` names the parent 7bd7ab2e4 where it named 6855d6ae7.
