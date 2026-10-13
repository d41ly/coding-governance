# TOOL-aOrientedCast-26 — spec writers run at high effort and builders at xhigh, as the owner ruled

**Status:** OPEN · rev-1 · 2026-10-13 · node a · Tier-1 · base 646d4a73581393acbf42f33864a9808c96d00a0c · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-1-7-owner-addendum.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-7-owner-addendum.md) | research | TOOL-aOrientedCast-1 TOOL-aOrientedCast-23 |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled on 2026-10-13, verbatim: "Change efforts: spec-writers should write at HIGH effort,
gov-builders should write code at xhigh effort." The record is
`memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-7-owner-addendum.md`.
This unit swaps the two roles' levels in the effort policy, so every route that reads it, the agent
types and the harness `efforts` argument alike, carries the new levels.

## 2. Scope (IN)

- **S1** — In `tools/roles/house/policy.toml`'s `[effort.roles]`, `gov-spec-writer` moves from
  `xhigh` to `high` (`:10`) and `gov-builder` from `high` to `xhigh` (`:12`). Nothing else in the
  file moves. Observed by AC1, AC2 and AC3.
- **S2** — The main loop's second pass re-renders the agent types with
  `python tools/roles/render_agents.py --write`, so `.claude/agents/gov-spec-writer.md` and
  `.claude/agents/gov-builder.md` carry the new `effort:` lines. Observed by AC4.

## 3. Non-goals (OUT)

- Any other role's level, the `default`, or a `[effort.stages.*]` table: none pins a spec-writer or
  builder stage (§4).
- A roles kit version move: `TOOL-aOrientedCast-25`, order 27, moves the kit after this unit (§4).
- A doc edit: neither the roles README nor `help/roles.md` states either role's level (§4, AC5).
- The fixtures that spell `xhigh` or `high` for a builder or spec writer in
  `tools/workflows/unattended-build.test.sh` and the roles and hooks suites: each is a literal its
  own fixture writes, never read from the policy.
- Editing a CLOSED spec, `TOOL-aOrientedCast-10`'s level table included: the policy file is the
  one source, and that table is a record of its moment.

## 4. Design

Read at `a75ade2e3` on 2026-10-13.

- **The edit.** Two values in `[effort.roles]` (`tools/roles/house/policy.toml:8-15`). The
  library reads them through `load_policy` and `resolve_effort` (`tools/roles/roles_lib.py`), and
  both levels are members of `EFFORT_LEVELS`, so R12 admits them.
- **The stage tables.** `[effort.stages.spec-review]` and `[effort.stages.spec-write]` override only
  `skeptic` and `synthesis` (`:17-23`), and no `build` table exists. So `spec-write`'s `specWriter`,
  `disposal` and `builder` keys and `build`'s `builder` key follow the role levels. At writing,
  `python tools/roles/handoff.py stage-efforts spec-write` printed
  `{"builder":"high","disposal":"xhigh","skeptic":"medium","specFinder":"medium","specWriter":"xhigh","synthesis":"medium"}`
  and `build` printed `{"builder":"high"}`; after the edit they print AC2's values.
- **The render.** `render_agents.py --write` writes each agent type's `effort:` line from the policy.
  It is the main loop's second pass: `--dispatch` refuses a write set that holds a generated output
  together with its generator's input, the pairing the build method's M6 condition 3 forbids
  (`tools/unattended/unattended.sh:13712`). `.claude/roles.json` carries no effort, so its bytes do not
  move. A session started before the render keeps the old types until it restarts.
- **The kit version.** `house/policy.toml` is a `seed` row of `tools/roles/kit.toml`, and the epoch
  leg counts a seed's bytes as the kit's (`EPOCH_ROLES`, `tools/govkit/govkit.py:12935`), so its move
  owes a later bump. `TOOL-aOrientedCast-25`, order 27, moves the roles kit from 1.3 to 1.4 after
  this unit, and the epoch leg clears every earlier move once a later commit bumps the version. Should
  that unit be retired before this one closes, the bump comes back here by a rev. An adopter's seeded
  policy is never rewritten by `govkit update`, so adopters keep their own levels.
- **The docs.** `help/roles.md` says only that the policy sets the effort (`:26`, `:43-44`), and the
  roles README names `gov-skeptic`'s two levels as its example (`tools/roles/README.md:167`); neither
  states a spec-writer or builder level, so neither moves.
- **What the CLI does with xhigh.** It runs `xhigh` as `high` on a model that lacks it
  (`tools/roles/README.md:171`); the agent line's `effort` field reports the level a transcript
  records, so the downgrade stays visible.
- **The write set** is disjoint from `TOOL-aOrientedCast-24`'s, which builds at the same step: that
  unit writes the hooks kit, the unattended kit and their rendered guides, none of these files.

### Files touched (estimate)

`tools/roles/house/policy.toml`
`.claude/agents/gov-spec-writer.md`
`.claude/agents/gov-builder.md`

The two agent types are the second pass's.

## 5. Acceptance criteria

- **AC1** — When `python -c "import sys, tomllib; d = tomllib.load(open(sys.argv[1], 'rb'))['effort']['roles']; print(d['gov-spec-writer'], d['gov-builder'])" tools/roles/house/policy.toml`
  runs, it prints `high xhigh`, and `git diff HEAD~1 HEAD --stat -- tools/roles/house/policy.toml`
  on the unit's commit shows one file with two lines changed each way.
  Red when: either value is not the ruled one, or another line of the policy moved.
- **AC2** — When `python tools/roles/handoff.py stage-efforts spec-write` runs, it prints
  `{"builder":"xhigh","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}`,
  and `python tools/roles/handoff.py stage-efforts build` prints `{"builder":"xhigh"}`.
  Red when: a stage override pins a spec-writer or builder stage to its old level, or the harness
  `efforts` argument misses the policy change.
- **AC3** — When `python -c "import sys; sys.path.insert(0, 'tools/roles'); import roles_lib as r; r.load_policy('tools/roles', r.load_roles('tools/roles'), r.load_workflows('tools/roles')); print('policy ok')"`
  runs, it prints `policy ok`.
  Red when: the edited policy fails the library's R12 validation, which raises naming the key.
- **AC4** — When the main loop's second pass has run `python tools/roles/render_agents.py --write`,
  `grep "^effort:" .claude/agents/gov-spec-writer.md .claude/agents/gov-builder.md` prints
  `effort: high` for the first and `effort: xhigh` for the second, and
  `python tools/roles/render_agents.py --check` exits 0.
  Red when: an agent type keeps its old level, or the committed render differs from a fresh one.
  permission: the render is the main loop's second pass, never the builder's.
- **AC5** — When `git grep -n -i -E "(spec-writer|builder).{0,40}(xhigh|high)" -- help/roles.md tools/roles/README.md`
  runs, it prints nothing, so no doc states a level this unit moves; and on the unit's commit
  `git diff HEAD~1 HEAD -- tools/roles/roles_lib.py | grep -c "KIT_ROLES_VERSION"` prints 0.
  Red when: a doc states either role's old level, or this unit moves the version
  `TOOL-aOrientedCast-25` moves once after it.

## 6. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm. The main loop runs the legs once, at the close; no pass runs one.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft.
