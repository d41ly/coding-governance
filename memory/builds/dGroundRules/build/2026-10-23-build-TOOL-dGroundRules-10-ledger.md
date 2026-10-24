# TOOL-dGroundRules-10 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-10

No merge bar, gate leg or self-test suite ran in this pass. Each criterion a fixture can reach was
observed before the commit, with this unit's edit in the worktree: the ten `limit-` cases and
`mirror-worktree-loosened` through the kit's own fixture CLI, one case per run, each in its own
repository under the system temp directory, and the rest through probes of the reader, the hook and
the renders. The naming lexicon, the one leg the builder role may run, printed `lexicon OK` with the
verb offenders at 1204, the pin `.lexicon.conf` now holds. The New arms' RED-first observations are
the close's.

**Evidences:** TOOL-dGroundRules-10
- AC1 — `limit-conf-lowers` — `python tools/policy/check_policy.py --fixture limit-conf-lowers`, exit 0, 2 assertions, 0 wrong: `get runtime.agents-in-flight` printed `2`, and `--explain` printed "policy: runtime.agents-in-flight · default · .governance/policy.toml is absent at 96fcc3a1, local main: this clone has no remote; the catalogue default; lowered to 2 by FANOUT_CAP at .agent-cap.conf:1".
- AC2 — `limit-conf-no-raise` — `--fixture limit-conf-no-raise`, exit 0, 1 assertion: printed `6`, the default the case read from the catalogue row at run time, with "FANOUT_CAP=8 at .agent-cap.conf:2 does not lower it" in the reason.
- AC3 — `limit-conf-malformed` — `--fixture limit-conf-malformed`, exit 0, 1 assertion: the reader exited 2, stdout empty, stderr exactly "policy: refused · .agent-cap.conf:1 · FANOUT_CAP must be an integer of at least 1".
- AC4 — `limit-settings-render` — `--fixture limit-settings-render`, exit 0, 6 assertions: `settings --write` at 8 wrote both keys as "8"; after a committed policy write of 6, `settings --check` exited 1 naming both keys; `--write` wrote both as "6" and `--check` exited 0 printing "policy: settings fresh · .claude/settings.json".
- AC5 — `python tools/run-gates/regen.py --list` — printed "regen: stage 1 · policy · .claude/settings.json" with the row's `settings --write` and `settings --check` argv. The render of this repository's `.claude/settings.json` and the `python policy.py settings --check` exit 0 after it are owed at the close: the builder does not rewrite the settings of the session running in the worktree (S3). Before it, `settings --check` here exits 1 naming both keys absent, "runtime.agents-in-flight resolves 6".
- AC6 — `limit-hook-admits-eight` — `--fixture limit-hook-admits-eight`, exit 0, 3 assertions: with `.claude/roles.json` declaring one agent-true role and one harness, a landed limit of 8, settings rendered at 8 and `FANOUT_CAP=8` in `.agent-cap.conf`, the handoff-valid `Agent` call and the registered harness's `Workflow` call each exited 0 with empty stderr through the hooks kit's agent-cap.js.
- AC7 — `limit-hook-six-spawns` — `--fixture limit-hook-six-spawns`, exit 0, 7 assertions: six `Agent` payloads of one `session_id` and `prompt_id` each exited 0, and the fixture's `.git/agent-cap` is absent under its git common dir.
- AC8 — `limit-hook-rules-kept` — `--fixture limit-hook-rules-kept`, exit 0, 4 assertions: a raw `parallel` over `items.map` exited 0, `boundedParallel(thunks, 50)` exited 0, a verifier per finding exited 2 with "caps verify-stage agents at 5 TOTAL, this hook's MAX_VERIFIERS", and a ref-keyed join exited 2 naming "a ref-keyed verdict join".
- AC9 — `limit-hook-env-cap` — `--fixture limit-hook-env-cap`, exit 0, 2 assertions: `AGENT_CAP=50` over a clean script exited 0, and the case's `git grep -n -- --print-cap -- tools` printed nothing, exit 1; the same command over this worktree printed nothing, exit 1.
- AC10 — `limit-hook-settings-over` — `--fixture limit-hook-settings-over`, exit 0, 4 assertions: under a landed limit of 2, settings at 3 exited 2 naming `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` and "python tools/policy/policy.py settings --write"; no `env` exited 2 naming both keys absent; settings at 2 exited 0; with the kit copy's `tools/policy/` removed, settings at 3 exited 0.
- AC11 — `limit-hook-local-over` — `--fixture limit-hook-local-over`, exit 0, 2 assertions: settings at 2 and `settings.local.json` setting either variable to 5 exited 2, each naming ".claude/settings.local.json: env.<KEY> is 5, above runtime.agents-in-flight 2". `--fixture mirror-worktree-loosened`, exit 0, 3 assertions: with L's limit 2 and the working-tree `policy.json` hand-edited to 8, the real hook with settings at 3 exited 2 naming "above runtime.agents-in-flight 2", and `arm_mirror_landed` found 0 findings.
- AC12 — `grep -c "const MAX_VERIFIERS = 5" tools/workflows/tier2-review.js` — printed `1`; `grep -n "boundedParallel(thunks, cap = " tools/workflows/tier2-review.js` printed "18:async function boundedParallel(thunks, cap = 6) {", the value `policy.py get runtime.agents-in-flight --rev HEAD` printed, `6`.
- AC13 — `node tools/hooks/agent-cap.js --only=scripts` — `tier2-review.js`, `drift-audit-code.js` and `drift-audit-state.js`, each piped as a `Workflow` payload, exited 0. `unattended-build.js` exited 2: its `SPEC_WRITERS` renders the limit, 6, on a `gov:fixed-verifiers` split, which rule 2 judges against `MAX_VERIFIERS`, 5. The `gov:fixed-writers` split that judges writers against the limit is `TOOL-dGroundRules-18`'s (§3 hands-off), so this half is owed until that unit.
- AC14 — `git grep -n "AGENT_CAP\|print-cap\|FANOUT_CAP" -- README.md WIRE-INTO-PROJECT.md tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md tools/hooks/README.md` — printed eight lines: a `FANOUT_CAP` line that lowers the limit through the reader, the hook README's line that a set `AGENT_CAP` is read by nothing, its legacy-home section and the `{{FANOUT_CAP}}` width; none says a set `AGENT_CAP` is refused, names the print mode, or calls `FANOUT_CAP` a ceiling of five. `help/agent-limit.md` names `runtime.agents-in-flight` on three lines and `policy.py settings --write` on two.
- AC15 — `python check_policy.py --live` — owed at the close, the main loop's live run.
- AC16 — `python check_policy.py --live` — owed at the close, the main loop's live run.
- AC17 — `python check_policy.py --live` — owed at the close, the main loop's live run.

Owed at the close, observed by no command in this pass:

- The four `New arm:` lines of §7, each RED on its staged break and GREEN restored.
- The §7 legs over the built tree. `verifier fan-out` and the `unattended-build self-test` arm that admits the build harness stay red on `unattended-build.js` until `TOOL-dGroundRules-18`, as AC13 records. `kit version markers` and `kit epoch` grade the bump the landing mints: every `gov:kit agent-cap@` carrier stays at 1.40 on the branch.
- AC5 after the main loop's `python tools/run-gates/regen.py --write`, and AC15 to AC17.
- The two `[cite]` waivers: a probe of the cites join's own `CITE` and `LIVE` patterns and line count over every spec printed two live hits on `TOOL-aOrientedCast-28`, each WAIVED by its row, no stale `agent-cap.js` row, and three on this unit's own spec, which its CLOSED status takes out of the graded set; `TOOL-dFairHearing-22`'s `:2269-2272` is DEFERRED and ungraded, so it takes no row. `spec tokens` itself is the close's.
