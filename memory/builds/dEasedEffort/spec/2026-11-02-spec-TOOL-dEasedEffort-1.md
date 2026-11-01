# TOOL-dEasedEffort-1 — the orienter and builder run at high, the closing review's finders and skeptics at medium

**Status:** SPECCED · rev-1 · 2026-11-02 · node d · Tier-2 · base 2a6f3975 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dEasedEffort-1-brief.md](../prompts/2026-11-02-prompt-TOOL-dEasedEffort-1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The owner's prompt rules, verbatim: "Change gov-orienter gov-builder builder (spec-write) and builder
(build) to 'high' from 'xhigh' by default. Change gov-diff-reviewer gov-skeptic diffFinder
(closing-review) and skeptic (closing-review) to 'medium' by default." The record is
`memory/builds/dEasedEffort/prompts/2026-11-02-prompt-TOOL-dEasedEffort-1-brief.md`. This unit moves
four values in the seeded effort policy, so every route that reads it carries those levels: the
rendered agent types and the harness `efforts` argument alike.

## 2. Scope (IN)

- **S1** — In `[effort.roles]` of `tools/roles/house/policy.toml`, `gov-orienter` (`:9`) and
  `gov-builder` (`:12`) move from `xhigh` to `high`. The `builder` stage of `spec-write` and of
  `build` follows the role. Observed by AC1 and AC2.
- **S2** — In the same table, `gov-diff-reviewer` (`:13`) and `gov-skeptic` (`:14`) move from `high`
  to `medium`. The `diffFinder` and `skeptic` stages of `closing-review` follow their roles. Nothing
  else in the file moves. Observed by AC1 and AC2.
- **S3** — The sentence at `tools/roles/README.md:184` names the role that still runs at two levels,
  and reads, at its existing two-space indent:
  "That is how `gov-synthesizer` runs at `medium` in spec review and `high` in closing review."
  Observed by AC4 and AC5.
- **S4** — The main loop's second pass runs `python tools/roles/render_agents.py --write`, so the
  four agent types under `.claude/agents/` carry the new `effort:` lines. Observed by AC3.

## 3. Non-goals (OUT)

- Any other role's level, or the `default`.
- `gov-synthesizer` and the closing review's `synthesis` stage, which stay `high`.
- The `[effort.stages.*]` tables. Their `skeptic` rows stay, though they now equal the role (§4).
- The `roles.effort.*` keys in `tools/policy/catalogue.toml`, which no reader serves yet (§4).
- An adopter's seeded policy, which `govkit update` never rewrites.
- A by-hand move of `KIT_ROLES_VERSION`, or of any other kit version.
- Editing a CLOSED spec's level table: `TOOL-aOrientedCast-10`'s table records its moment.
- The fixtures that spell a level their own test writes, in
  `tools/workflows/unattended-build.test.sh`, `tools/hooks/format-guard.test.sh` and
  `tools/roles/adopt-roles.test.sh`.

### Edges

- **hands-off** external — the roles kit's version move, which the lander's `govkit.py mint` writes
  at landing, so this build's branch owes no bump.

## 4. Design

Read at `f137c2c6e` on 2026-11-02. This is Tier-2 by the build README's classification (M2): both
source files are shipped kit files.

- **The edit.** Four values in `[effort.roles]` (`tools/roles/house/policy.toml:8-15`). `load_policy`
  (`tools/roles/roles_lib.py:398`) reads them, and both target levels are members of `EFFORT_LEVELS`
  (`tools/roles/roles_lib.py:45`), so R12 admits them.
- **The stage levels.** `resolve_stage_efforts` (`tools/roles/roles_lib.py:596`) gives a stage its
  `[effort.stages.<workflow>]` entry, else its slot's level. The policy holds tables for `spec-review`
  and `spec-write` only, each overriding `skeptic` and `synthesis` (`tools/roles/house/policy.toml:17`).
  No table pins a `builder`, `diffFinder` or closing-review `skeptic` stage, and the slots are the ones
  `tools/roles/workflows.toml:37`, `:57` and `:67` map. So those stages follow the roles.
- **The skeptic's stage rows.** Each `skeptic` row now equals the role. R12 refuses no such row
  (`tools/roles/roles_lib.py:472`), and the brief keeps them, so `stage-efforts spec-review` does not
  move.
- **The orienter.** `orient` has no `stages` table (`tools/roles/workflows.toml:14`), so
  `handoff.py stage-efforts orient` refuses with exit 1. The orienter's level reaches it through its
  agent type alone.
- **The surviving two-level role.** With `gov-skeptic` at `medium` everywhere, `gov-synthesizer` is
  the one role whose stages differ: `medium` in `spec-review`, `high` in `closing-review`. That is why
  S3 names it. `memory/map/features/review-harnesses.md:87` says the harness serves the two reviews
  at two levels, which stays true for the same reason.
- **The harnesses.** They hold no default level. `tools/workflows/tier2-review.template.js:259` reads
  `efforts` from the caller, and an unnamed stage runs at its agent type's level.
- **The render.** `render_agents.py --write` writes each agent type's `effort:` line from the policy.
  `.claude/roles.json` carries no effort, so its bytes do not move. The other five agent types are
  already at their levels, and `render_agents.py --check` exits 0 today, so the render moves four
  lines only.
- **Who renders, and why that is a choice.** The brief and the build README give the render to the
  main loop, and this spec keeps that. No refusal forces it, though. `tools/roles/kit.toml:125`
  pairs `.claude/agents` with `render_agents.py`, and the policy is not that row's generator, so
  `--dispatch` (`tools/unattended/unattended.sh:13944`) would accept both paths in one declaration.
- **The kit version.** `house/policy.toml` is a `seed` row and the README an `engine` row, and both
  are in `EPOCH_ROLES` (`tools/govkit/govkit.py:13322`). A branch owes no bump: the epoch verb grades
  one only at the push boundary, and the lander mints it (`tools/push-main.sh:26`).
- **The other homes.** `.governance/policy.toml` holds no effort key. `git grep -n "roles\.effort" -- tools`
  finds only the catalogue rows and `tools/policy/unsummarised-keys.txt`, so those keys are declared
  and read by nothing here. Outside the records and the fixtures, only the policy and its render
  under `.claude/agents/` spell these levels.
- **The docs.** `help/roles.md:44` and `help/policy.md:233` name the policy file and its tables, and
  neither states a level. `tools/roles/README.md:186` lists the levels as a vocabulary, which stays.

### Stage levels

Measured on 2026-11-02. "Today" is the live `handoff.py stage-efforts` output. "After" is the same
library over a scratch copy of the kit with the four values moved, and AC2 re-derives it.

| Workflow | Today | After |
|---|---|---|
| `spec-write` | `{"builder":"xhigh","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}` | `{"builder":"high","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}` |
| `spec-review` | `{"skeptic":"medium","specFinder":"medium","synthesis":"medium"}` | unchanged |
| `build` | `{"builder":"xhigh"}` | `{"builder":"high"}` |
| `closing-review` | `{"diffFinder":"high","skeptic":"high","synthesis":"high"}` | `{"diffFinder":"medium","skeptic":"medium","synthesis":"high"}` |

### Inventory

This unit mints no identifier.

### Rollout

1. The build pass edits the policy and the README, answers AC1, AC2, AC4 and AC5 in the unit's
   acceptance ledger, and sets the spec CLOSED in its own commit, as
   `tools/workflows/unattended-unit.js:314` requires.
2. The main loop's second pass runs the render, observes AC3, adds AC3's ledger line, and commits
   with a `Pass: none` trailer, the form `tools/workflows/unattended-unit.js:312` gives a commit that
   names the unit and is no pass. The ledger arm grades outside `--staged` only
   (`tools/memory-tree/check-memory-hygiene.sh:117`), so the build pass's commit is not refused for
   the line still owed, and the bar at the close reads the full ledger.
3. A harness call composes `efforts` from `handoff.py stage-efforts` after the build pass, so this
   build's closing review already runs at the new levels. An agent type takes its new level in a new
   session (`tools/roles/README.md:188`).

### Files touched (estimate)

`tools/roles/house/policy.toml`
`tools/roles/README.md`
`.claude/agents/gov-orienter.md`
`.claude/agents/gov-builder.md`
`.claude/agents/gov-diff-reviewer.md`
`.claude/agents/gov-skeptic.md`

The four agent types are the second pass's.

### Alternatives rejected

- **Render inside the build pass.** It is legal, and `175f86981` and `e3603ff15` both did it. The
  build README's rule assigns the render to the main loop, and following that rule leaves the bytes
  the same, so no design reason overrides the record.
- **A `[effort.stages.closing-review]` table.** It would set the harness levels and leave the agent
  types at the old ones, so a direct spawn would disagree with a harness spawn. The prompt rules the
  roles too.

## 5. Production-readiness checklist

- security: N/A — no write path, surface or grant moves; the `[gates]` table is untouched.
- perf / scale: orientation, builds and closing reviews spend less per agent, which is the ruling.
- error / empty / loading states: N/A — a bad level already refuses through R12, unchanged.
- observability: the agent line reports the level a transcript records
  (`tools/roles/README.md:108`), and each harness logs every stage's level with its source.
- risks: a closing review's finders and skeptics reason less deeply, and a builder or orienter that
  reached `xhigh` no longer does. That is the owner's ruling, and `gov-synthesizer` stays `high`.
- testing: no test added; AC1 to AC5 observe the values, and no suite reads the seeded levels.
- migration: N/A — adopters keep their seeded levels, and a session restart picks up the agent types.
- user docs: no `help/` page states a level, so none moves (AC4).

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/roles'); import roles_lib as r; k = 'tools/roles'; ro = r.load_roles(k); p = r.load_policy(k, ro, r.load_workflows(k)); print(' '.join('%s=%s' % (s, r.resolve_effort(p, s)) for s in sorted(ro) if ro[s]['keys'].get('agent', 'true') != 'false'))"`
  runs, it prints
  `gov-builder=high gov-diff-reviewer=medium gov-orienter=high gov-researcher=medium gov-reuse-scout=medium gov-skeptic=medium gov-spec-reviewer=medium gov-spec-writer=high gov-synthesizer=high`,
  and `git diff --numstat 2a6f3975 HEAD -- tools/roles/house/policy.toml` shows 4 lines added and 4
  deleted.
  Red when: a moved role's level is not the ruled one, another role's level moved, the file fails
  `load_policy`'s R12 validation, or a line beyond the four moved.
  figure: PINNED — the printed levels are the ruling and the other roles' levels at 2026-11-02.
- **AC2** — When `python tools/roles/handoff.py stage-efforts <workflow>` runs for each workflow, it
  prints `{"builder":"high","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}`
  for `spec-write`, `{"skeptic":"medium","specFinder":"medium","synthesis":"medium"}` for
  `spec-review`, `{"builder":"high"}` for `build`, and
  `{"diffFinder":"medium","skeptic":"medium","synthesis":"high"}` for `closing-review`.
  Red when: a stage override pins a moved stage to its old level, the `synthesis` stage of
  `closing-review` moved, or a `[effort.stages.*]` row moved.
- **AC3** — When the main loop's second pass has run `python tools/roles/render_agents.py --write`,
  `grep "^effort:" .claude/agents/gov-orienter.md .claude/agents/gov-builder.md .claude/agents/gov-diff-reviewer.md .claude/agents/gov-skeptic.md`
  prints `effort: high` for the first two and `effort: medium` for the last two,
  `git diff --name-only 2a6f3975 HEAD -- .claude` prints exactly those four paths, and
  `python tools/roles/render_agents.py --check` exits 0.
  Red when: an agent type keeps its old level, the render moved another file under `.claude`, or
  the committed render differs from a fresh one.
  permission: the render and this observation are the main loop's, after the build pass.
- **AC4** — When `git grep -n -i -E "(gov-orienter|gov-builder|gov-diff-reviewer|gov-skeptic).{0,60}\b(xhigh|high|medium)\b" -- help tools/roles/README.md`
  runs, it prints nothing, so no doc states a level this build moved.
  Red when: `tools/roles/README.md:184` still names `gov-skeptic`, which is what the grep prints
  today, or a doc gains a moved role's level on one line. It cannot see a level more than 60
  characters from the role, or wrapped onto the next line.
- **AC5** — When `grep -c "That is how .gov-synthesizer. runs at .medium. in spec review and .high. in closing review" tools/roles/README.md`
  runs, it prints `1`, and AC2's output gives `synthesis` the level `medium` in `spec-review` and
  `high` in `closing-review`.
  Red when: the sentence names a role with one level, or the two levels it states disagree with
  `handoff.py stage-efforts`.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm. The main loop runs these legs once, at the close, with the full bar, and
no pass runs one. The second pass comes before the bar, because the agent types lag the policy until
the render.

What no leg checks: that the seeded levels are the ones the owner ruled. They are seed data, so R12
grades their membership of `EFFORT_LEVELS` and nothing grades their value. AC1 and AC2 observe that
once, and no leg re-observes it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft.

## 10. Reuse audit

The seam is `tools/roles/house/policy.toml`, read through `load_policy`, `resolve_effort` and
`resolve_stage_efforts` in `tools/roles/roles_lib.py`. `tools/codebase-map/reuse_lookup.py` run on
"seeded effort policy levels per role rendered into agent types and harness efforts" names
`load_policy` a SEAM and returns both resolvers. This unit extends that seam with data and adds no
code. `render_agents.py --write` carries it to the agent types, and `handoff.py stage-efforts` to
the harnesses. Recall returned `TOOL-aOrientedCast-10`, the policy file's design, and
`TOOL-aOrientedCast-26`, the same kind of move, whose spec is the precedent.

Where the records and the source disagreed. `TOOL-aOrientedCast-26` said `--dispatch` refuses a
generated output together with its generator's input, and this build's brief and README carry that
forward. The refusal pairs an output with its declared generator only, and that unit's own commit,
`175f86981`, records running the render in one pass for that reason. §4 states the source's reading.
The same spec's line citations into `tools/roles/README.md` and `tools/unattended/unattended.sh`
have moved, and the scouts' `tools/roles/roles_lib.py` citations for the two resolvers have too, so
§4 cites the lines at `f137c2c6e`.

Recall terms used: effort policy.toml gov-orienter gov-builder gov-skeptic xhigh stage-efforts
render_agents resolve_effort roles_lib, with the question "where do role effort levels live and how
does a level change reach agent types and harness stages".
