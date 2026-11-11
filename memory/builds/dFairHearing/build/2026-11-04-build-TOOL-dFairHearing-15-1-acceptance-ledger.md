# Acceptance ledger — TOOL-dFairHearing-15

**Serves:** journal TOOL-dFairHearing-15

Built against spec rev-6 and committed as the pass commit `7b2153c28`, whose parent is `a882a5e60`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-15-1-builder-return.md`, and every observation below is that return's. No suite, gate or bar ran in the pass: the checks were scratch probes standing in for the `tier2-review self-test` leg, and the suite's new arms and the spec's legs are owed to the close. The replay, its decision and the `--all-ungated` change were not built here, because the spec's hands-off edges give them to later units.

**Evidences:** TOOL-dFairHearing-15
- AC1 — `resume:checklist` — a stub-agent node probe of the new render, run the way the suite runs it, saw `resume:checklist` as the first spawn, of Plan type, then `resume:probe`. The prompt named both checker paths, and C1, C2 and C3 reached the finders. All 13 of the probe's checks passed, and against the previous render it failed 9, with AC2 and AC4 passing there by design
- AC2 — `resume:checklist` — the same probe passed this case: a checklist the caller passes takes priority and no `resume:checklist` agent spawns
- AC3 — `WARNING:` — the same probe passed all three outcomes. When the agent reports no checker or no item line, returns an error, or dies, the log carries one `WARNING:` with the reason and RUN INTEGRITY reads `Checklist: NONE swept — not acquired: <reason>`
- AC4 — `resume:checklist` — the same probe passed this case: a spec audit never fetches a checklist, so no `resume:checklist` agent spawned
- AC5 — `byDesign` — the real `gotchas.py --for-diff 3708a705..HEAD` stdout, saved under the scratch directory, gave all 137 items in the checker's order as C labels, and its 3 by-design entries reached `byDesign` and were never swept as classes
- AC6 — `tools/memory-tree/gotchas.py` — by grep, the render holds `tools/memory-tree/gotchas.py` and no raw `{{TOOL_ROOT}}`. `tools/workflows/kit.toml` is untouched: its `tier2-review.template.js` row has listed `TOOL_ROOT` since unit 8, and the spec's rev-2 edge hands that half to unit 23
- AC7 — `coding-governance-agents.template.md` — `git grep "run it before any review"` over `coding-governance-agents.template.md` and `AGENTS.md` printed nothing, after `AGENTS.md` was re-rendered with `adopt-playbook.sh --target .`. The first `kit:memory-tree` fence was removed, and the second still opens and closes
- AC8 — amended rev-3 — the revision log's rev-3 line adds the hands-off edge to unit 25, which runs this unit's replay and supersedes AC8 and AC9. Its rev-4 line moves the replay to unit 30 and its rev-5 line moves the scoring and the decision to unit 35. The builder return built none of it here. Unit 30's replay verdict record states paired 4 of 4 for each arm and pooled recall of 26/59 and 25/59
- AC9 — amended rev-3 — the same revision log lines supersede this criterion, and the builder return built neither the decision nor the flag here. Unit 30's replay verdict record decides that the selected arm holds, so the flag does not land and unit 35 leaves the checker unchanged
