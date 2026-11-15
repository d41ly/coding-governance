# TOOL-dDeclaredLoop-4 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-4

No merge bar, no self-test suite and no gate leg ran in this pass, and neither `stage_coverage.py
--selftest` nor the codebase-map selftest was run. The criteria were observed on node `d` (win32) by
probes of the unit's own code: the module over the tree, each of its plants by direct CLI from the loop
kit's folder, and `parse_dossier` and the new map arm's function called through `python -c`.

The seed, by the spec's rollout rules: every manifest row carries `["step.test"]`, and the rows whose
script `.githooks/pre-commit` runs on staged paths (`kickoff-manifest ratchet`, `template size
<=48KiB`, `codebase-map coverage + freshness`, `unattended skill wiring` and `memory hygiene`) carry
`step.build` before it. The git hooks `pre-commit`, `commit-msg` and `pre-rebase` claim `step.build`
and `pre-push` claims `step.test`. A harness hook on an event every session raises claims all the
steps; the SubagentStart hook, which reaches role agents alone, claims the steps of the workflows that
have roles: `step.plan`, `step.design` and `step.build`. Each dossier claims the union of its claimed
legs' and hooks' stages in the loop's order, or `["none"]` where it claims neither.

Owed to the close: every leg the spec's section 7 names, the `loop definition`, `loop item kind` and
`loop transition tables` legs beside them, `docs`, and the RED-first observation of both `New arm:`
lines: the module's plants through `--selftest`, with `unclaimed-leg` staged red by feeding the part
join's owner every part, and the map selftest's arm `test_stage_key` staged red against a parser that
refuses the key. The exit 2 `unarmed` path, a kit that does not resolve, was not probed.

**Evidences:** TOOL-dDeclaredLoop-4
- AC1 — `--plant unclaimed-leg` — `python stage_coverage.py --fixture --plant unclaimed-leg` exited 1 printing `stage-coverage: unclaimed leg kickoff-manifest ratchet · no claim`; `--plant unclaimed-hook` exited 1 printing `stage-coverage: unclaimed hook PostToolUse tools/memory-recall/recall-opened.js · no claim`.
- AC2 — `--plant stale-hook` — exited 1 printing `stage-coverage: stale hook PreToolUse tools/hooks/no-such-hook.js`; `--plant role-derived` exited 0 and its `role gov-builder` line read `workflow build · step.test`, the role file carrying no stage of its own.
- AC3 — `step.ship` — `--plant bad-tag` exited 1 printing the first dossier unclaimed with the value it carries, `agent-cap` and the list holding step.ship.
- AC4 — `item.build.exit` — `--plant stage-no-witness` exited 1, its `refused` line the definition reader's words: the item item.build.exit carries no witness.
- AC5 — `unarmed` — `--plant no-legs` exited 1 printing `stage-coverage: part · leg · unarmed — no leg in the tree`.
- AC6 — `inventories.json` — `python stage_coverage.py` over the seeded tree exited 0 with no unclaimed part and no stale claim, its leg and hook counts equal to the `gate-legs` count and the summed `git-hooks` and `harness-hooks` counts of the regenerated `memory/map/generated/inventories.json`, read at observation.
- AC7 — `MapError` — `parse_dossier` on the map selftest's fence with `stage = ["step.build"]` returned a `Dossier` whose `stage` is that list as the parser's tuple, None without the key, and with `stage = "step.build"` raised `MapError` reading `t: stage must be a list of non-empty strings`; `test_stage_key` called directly passed.
- AC8 — `loop stage coverage` — the row carries `"enforces": ["principle.p1"]`, `"stage": ["step.test"]` and no `guard`, read through `json.load`; the registry's `name = "loop stage coverage"` and the pin file's `loop stage coverage` row each counted once.
- AC9 — `KNOWN` — `grep -c '^KNOWN = {.*"stage"' tools/run-gates/run-gates.test.sh` printed 2.
- AC10 — `stage_coverage.py` — the help page `loop.md` carries the stage-claims section and its usage anchor, whose fingerprint `docs_leg.py --fingerprints` prints against `help/loop.md`; `tools/govkit/usage.toml` carries the script's row; the codebase-map README's `map_lib.py` entry names the optional `stage` key.
