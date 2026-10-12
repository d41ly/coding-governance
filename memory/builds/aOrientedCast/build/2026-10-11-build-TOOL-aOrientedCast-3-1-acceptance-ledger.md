# TOOL-aOrientedCast-3 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-3

Direct checks only; no gate, suite or bar ran in the pass. AC1, AC3 and AC8 ran on the worktree's
real render. AC2, AC4, AC5 and AC6 ran from one probe script in the pass's scratch, which staged each
break with a byte replacement that refuses unless it matches once, ran `render_agents.py`, and
restored: a tracked role file or workflow table by `git checkout --`, the renderer from a byte copy
taken first, and a rendered file from the bytes read before the break. Every arm the two new legs
carry was seen RED on its break and GREEN once restored: three `--check` breaks and the harness move
exited 1 naming their paths and 0 after, and three `--selftest` breaks exited 1 naming arms 1, 8 and
10 and `PASS (24 assertions)` after. AC7 is the live probe recorded in
`2026-10-11-build-TOOL-aOrientedCast-3-agent-type-rerun.md`. The close owes
`codebase-map coverage + freshness`, which is AC9's `test_codebase_map.py` run, `govkit selfcheck`,
which reds on both new legs until TOOL-aOrientedCast-8 declares them in the roles kit's descriptor,
and the rest of the spec's §7 list, the two new legs included.

**Evidences:** TOOL-aOrientedCast-3
- AC1 — `omitClaudeMd: true` — `--write` then `--check` exited 0 printing `render_agents: 9 agent type(s) and 1 index graded`, nine being the catalogue's `agent`-true roles; each of the nine types carries `omitClaudeMd: true` and its role's `workflow` and `writes` lines, `gov-session.md` does not exist, and `roles.json` holds all ten roles with `gov-session` at `"agent": false`.
- AC2 — `stale` — one byte appended to `gov-builder.md` exited 1 `drift .claude/agents/gov-builder.md`; `roles.json` deleted exited 1 `missing .claude/roles.json`; `writes` edited in gov-builder's role file exited 1 naming `gov-builder.md` and `roles.json` as `drift`; a copy `gov-retired.md` listed in the index exited 1 `stale .claude/agents/gov-retired.md`. A digest of every owned file was equal before and after each `--check`. The following `--write` unlinked `gov-retired.md` and rewrote the index to its original bytes while a foreign `my-agent.md` kept its bytes, and once every break was restored the check exited 0.
- AC3 — `unchanged` — over a tree with no rendered types, `--write` printed ten `wrote` lines and `render_agents: 9 agent type(s) changed — a Claude Code session started before this write cannot spawn the change; …`; run again at once it printed `render_agents: unchanged — 9 agent type(s) and 1 index fresh` and no restart line.
- AC4 — `## House rules` — `render_role` for `gov-builder` plus the `### charter` blocks from `extract_charter_sections` for §3, §7, §9, §11 and §12 equalled the type's body after its front matter, 18317 characters, byte for byte; one line staged into the house overlay and `--write` put `## House rules` and the line into the type, and the restore and a second write took both away, leaving the type equal to its first render.
- AC5 — `roles.json` — the index's `harnesses` equalled the workflow table's three `workflow`-driver harnesses resolved by `resolve_harness_path`, neither empty; the `build` harness staged to the resolving `drift-audit-code.js` made `--check` exit 1 `drift .claude/roles.json`, and the restore exited 0.
- AC6 — `--selftest` — `render_agents.py --selftest` exited 0 with `PASS (24 assertions)`; the `omitClaudeMd` emission staged out exited 1 naming arm 1, the zero-role refusal staged out exited 1 naming arm 8, and an absent harness staged to raise exited 1 naming arm 10.
- AC7 — `NONE` — one nested `claude -p` on `2.1.292 (Claude Code)` in a clone at `58c109be`: a2, a3, w1 and w2 each logged one `SubagentStart` and one `PreToolUse` `Write` on one `agent_id` with nothing between, `agent_type` reading `gov-builder` or `gov-spec-writer` on both, and wrote `NONE`; the controls a1 and w3 were valid and wrote the codeword. The research record carries the six rows, the version and the instrument.
- AC8 — `eol: lf` — `git check-attr eol` answered `eol: lf` for each of the nine rendered types and for `.claude/roles.json`.
- AC9 — `last-audit` — `grep` found `roles render wiring` and `roles render selftest` once each in `tools/gate-legs.json`, once each in `tools/govkit/subject-pins.tsv` and once each in the roles dossier's claims, and `roles render selftest` once in `tools/run-gates/selftest-budgets.txt`; the manifest's `last-audit` line moved from `b1250a10` to `58c109be`. The `test_codebase_map.py` run is the `codebase-map coverage + freshness` leg, owed by the close.
