# TOOL-aOrientedCast-10 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-10

Direct checks only: under the owner's rule for this run no gate, suite or self-test ran in this
pass, and the three new suite arms of §7 (render arm 11, the review suite's `efforts:` block, the
build suite's OC10 block) are written and owed to the main loop, which observes each RED on its
staged break and GREEN at the close. What ran: `python -c` and scratch drivers calling the new
library functions, `render_agents.run_mode` and `check_roles.check_roles` over scratch copies of the
kit; `handoff.py stage-efforts`; `render_agents.py --write` and `--check` (neither a leg's argv);
the renderers whose output is committed; two node drivers copying each harness suite's stub shape;
parse-only checks (`bash -n`, `node --check`) of the edited suites; and the lexicon. RED first: the
review driver failed 9 checks against the parent render of `tier2-review.js`, the build and unit
driver 22 against the parent renders, and the AC4 driver failed its effort-line and refusal checks
with `resolve_effort` patched to ignore role entries and `extra` added to the levels; each is green
on the pass's tree. The suite floors were raised by hand-counted sites (review 301 to 314, build 612
to 631), not by a run. Gov's re-render of `.claude/agents/` lands in the pass's second commit, since
`--dispatch` refused declaring it beside its generator (spec rev-2).

**Evidences:** TOOL-aOrientedCast-10
- AC1 — `load_policy` — a `python -c` call over `tools/roles` with its own roles and workflows, then `resolve_effort` per agent role, printed gov-builder high, gov-diff-reviewer high, gov-orienter xhigh, gov-researcher medium, gov-reuse-scout medium, gov-skeptic high, gov-spec-reviewer medium, gov-spec-writer xhigh, gov-synthesizer high: the owner's table row for row.
- AC2 — `check_roles.check_roles` — over a scratch copy of the kit, each of the seven staged breaks (`extra` for gov-builder, `gov-nobody`, `gov-session`, `orient`, `diffFinder` under `spec-review`, `default` absent, the file absent) made `load_policy` raise `RolesError` naming its dotted key or the file, and the checker returned exactly one `R12` defect whose text is that refusal line; the clean copy loaded and carried no R12 defect.
- AC3 — `python tools/roles/render_agents.py --write` — wrote all nine types under `.claude/agents/`, each carrying one `effort:` line equal to AC1's level on the line before `omitClaudeMd: true`; `--check` then exited 0; with `gov-builder` staged to `max` and no re-render `--check` exited 1 naming `drift .claude/agents/gov-builder.md`, and restored it exited 0.
- AC4 — `build_fixture` — a scratch driver over the arm-11 catalogue through `run_mode`: `r-one.md` carried `effort: high` and `r-two.md` `effort: low`, each before `omitClaudeMd: true`; with `r-two = "extra"` the call returned 2 naming `effort.roles.r-two` and the five levels, and the fixture's agent directory was byte-identical.
- AC5 — `python tools/roles/handoff.py stage-efforts spec-review` — `spec-review` printed `{"skeptic":"medium","specFinder":"medium","synthesis":"medium"}`, `closing-review` `{"diffFinder":"high","skeptic":"high","synthesis":"high"}`, `build` `{"builder":"high"}`; `orient` and `nope` each exited 1 naming the workflow.
- AC6 — `{ builder: 'max' }` — scratch node drivers copying each suite's stubs: a spec audit with the three keys at `medium` spawned every `find:`, `verify:` and `synth` with `effort: 'medium'` and the resume probe with none; a diff review with `{ diffFinder: 'high' }` gave the five `find:` spawns `high` and no `verify:` spawn the key; the unit harness with `{ builder: 'max' }` spawned its builder at `max`; the build harness forwarded `{ skeptic: 'medium' }` alone into its review call's `efforts` and `{ builder: 'high' }` into `dispatch.args`; `[]`, `{ finder: 'high' }` and `{ skeptic: 'High' }` (`builder` for the unit) each threw opening with the harness name and `` `efforts` `` before any spawn, in all three harnesses.
- AC7 — `grep -c "stage-efforts"` — printed 4 for `tools/roles/SKILL.template.md` and for `.claude/skills/build/SKILL.md`, and 1 each for `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md` and `tools/workflows/README.md`; the Skill was rendered fresh by `adopt-roles.sh --scaffold` in this pass, and the byte comparison of the `roles render wiring` leg is owed to the main loop.
- AC8 — `grep -c policy.toml tools/roles/kit.toml` — printed 1, the line inside the seed rule's include list, and `grep -n "seed\", 0) == 14" tools/govkit/selftest.py` printed the default-plan arm's seed comparison at line 6160; the arm itself is owed to the main loop's `govkit selftest` leg.
- AC9 — owed to the main loop — the live probe of §4 "The probe": a nested `claude -p` session in a throwaway clone at this unit's commits, whose rendered agent types this session's registry predates; this pass launched no nested session.
