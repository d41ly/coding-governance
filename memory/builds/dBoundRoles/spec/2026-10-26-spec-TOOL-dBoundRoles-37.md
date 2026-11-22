# TOOL-dBoundRoles-37 — govkit's roles install case derives the agent types and house overlays it expects from the roster and the seed rows, so no roster change leaves a typed count to red

**Status:** CLOSED · rev-5 · 2026-11-22 · node d · Tier-2 · base 462d20f3 · streams tooling · order 4 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-37-deviation-371.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-deviation-371.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-37-deviation-372.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-deviation-372.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md) | research | TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |
| [2026-11-22-build-TOOL-dBoundRoles-37-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dBoundRoles-37-1-acceptance-ledger.md) | journal | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md) | research | TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 |
| [2026-11-22-prompt-TOOL-dBoundRoles-1-reground-e-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-1-reground-e-brief.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 |
| [2026-11-22-prompt-TOOL-dBoundRoles-14-spec-tokens-a-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-spec-tokens-a-brief.md) | journal | TOOL-dBoundRoles-14 TOOL-dBoundRoles-2 TOOL-dBoundRoles-1 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-49 TOOL-dBoundRoles-16 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-15 |
| [2026-11-22-prompt-TOOL-dBoundRoles-37-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-37-build-brief.md) | journal | — |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 4 at
HIGH**, report item **H5**. Id 47 is the same defect seen from the blast-radius lens at MEDIUM, report
item M25, and takes its own scope item in `TOOL-dBoundRoles-43`.

At base `462d20f3`, `tools/govkit/selftest.py:2837` checked `len(agents) == 9` and `:2838` ten seeded
house overlays, both typed, and `TOOL-dBoundRoles-1` S2 and S3, adding four roles with four empty
overlays and removing the two reviewers, would have made both wrong. The `govkit selftest` leg's guard
in `tools/gate-legs.json` covers `{prefix}/govkit/` and four other paths (PINNED at
`tools/gate-legs.json@e07c84d3`), none under `tools/roles/`, so a guarded run skips the leg and a red
would surface on a later, unrelated govkit change.

`TOOL-dWitnessedBar-23` S6 has since landed both as derivations, spelled inline in
`check_roles_install` (`tools/govkit/selftest.py@c2b02d78:3232-3250`): the agent-true roles of the
source roles kit through its own `roles_lib.load_roles`, and the `house/*.md` entries of its
descriptor's seed rows. No literal is left to red. This unit takes S3's landed branch, which §8 F2's
probe now selects: it lifts the inline derivation into S1's one function, which AC1 probes without
running a case, and routes the two checks through it. It repairs `TOOL-dBoundRoles-1` and builds one
step after it (order 4).

## 2. Scope (IN)

- **S1** — The derivation, `derive_roles_expected(kit, descriptor)` in `tools/govkit/selftest.py`,
  returning `(agents, overlays)`. `agents` is the set of slots of `kit`'s `agents/*.agent.md` whose
  front matter does not set `agent: false`, an absent key counting true as the landed derivation counts
  it (`@c2b02d78:3240-3241`), read through that kit's own `roles_lib.load_roles`
  (`tools/roles/roles_lib.py#load_roles`), loaded by path with `importlib.util`, so the selftest carries
  no second front-matter grammar. `overlays` is the set of `include` entries matching `house/*.md` in
  the `[[files]]` rows of `descriptor`, a parsed roles descriptor, whose `role` is `seed`, as the landed
  code reads `tools/roles/kit.toml` with `tomllib` (`@c2b02d78:3242-3245`). The call site passes gov's
  source kit, `KIT_DIRS["roles"]`, as the landed derivation does. Observed by AC1 and AC2.
- **S2** — The two landed checks of `check_roles_install` (`@c2b02d78:3246-3250`) compare S1's sets,
  their labels kept: "renders one agent type per agent role (<n>)", the `gov-*.md` stems under the
  target's `.claude/agents` equal to `agents`, and "seeds one house overlay per seed-list entry (<n>)",
  the `house/*.md` names under the installed kit equal to `overlays`, with its non-empty guard. Each
  failure prints both sets, as the landed messages do. Observed by AC2 and AC3.
- **S3** — Built once. Where `TOOL-dWitnessedBar-23` S6 has landed the same derivation at the build run's
  base, this pass keeps it, routes it through S1's function if it is spelled inline, and adds nothing
  beside it; otherwise this pass builds S1 and S2 in that section's form (§8 F2). It has landed inline
  at `a01362eb0`, so this pass takes the first branch. Observed by AC3.

## 3. Non-goals (OUT)

- The docstring of `check_roles_install` (`tools/govkit/selftest.py#check_roles_install`):
  `TOOL-dBoundRoles-43`'s, for id 47. At `a01362eb0` it no longer says "nine agent types, ten seeded
  house overlays"; TOOL-dWitnessedBar-23 S6 rewrote it, so unit 43's item finds it done.
- The `OC8 AC2` check that every house overlay is a seed row (`@c2b02d78:3150`), which reads the files present:
  `TOOL-dBoundRoles-19` S5 re-points it when the house files leave the kit.
- Widening the `govkit selftest` leg's guard to `tools/roles/` (§4 "Alternatives rejected").
- The report's left-shift text beyond the derivation. The derivation is the regression: no literal is
  left to drift.

### Edges

- **consumes-from** `TOOL-dBoundRoles-1` — the roster S2 and S3 change and the seed rows of `tools/roles/kit.toml` its overlays join, which S1 reads (id 4)
- **consumes-from** external — `TOOL-dWitnessedBar-23` S6, the same two counts derived for the tester's arrival; S3 builds on it where it has landed
- **hands-off** `TOOL-dBoundRoles-19` — the derived overlay set, so S5's "OC8 count of ten" needs no re-pointed literal: the house files leave the seed rows and `overlays` reads empty (id 4)
- **hands-off** `TOOL-dBoundRoles-43` — `derive_roles_expected` and the two set checks, whose docstring id 47's item rewrites (id 47)
- **hands-off** `TOOL-dBoundRoles-49` — `derive_roles_expected` and the descriptor read, whose `overlays` set unit 49 ties the default plan's roles seed rows to (id 23 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-50` — S1's agent predicate, which unit 50 restates with its absent-key default, and §8 F2's probe, whose landed derivation it records (ids 15 and 19 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-54` — the installed kit's `roles_lib.load_roles` load inside `derive_roles_expected`, through which unit 54 reads every role slot (id 14 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/govkit/selftest.py:2837-2839` holds the two typed checks, and `:2818` resolves the installed
  kit as `kit`.
- `tools/roles/kit.toml:35-40` names ten `house/*.md` seeds and `house/policy.toml` in one `seed` row.
- `.claude/roles.json` at base sets `agent` true for nine of ten roles, `gov-session` false.
- `tools/gate-legs.json`'s `govkit selftest` row has the guard `{prefix}/govkit/`,
  `{prefix}/hooks/kit.toml`, `{prefix}/settings-merge.py` and `{prefix}/codebase-map/kit.toml`.

Re-read at `a01362eb0` on 2026-11-22:

- `grep -n 'len(agents) == 9' tools/govkit/selftest.py` prints nothing; the derivation sits inline in
  `check_roles_install` (`tools/govkit/selftest.py@c2b02d78:3232-3250`), and `:3213` resolves the
  installed kit as `kit`.
- `tools/roles/kit.toml@b9102919:39-42` names eleven `house/*.md` seeds, `gov-tester`'s among them, and
  `house/policy.toml` in one `seed` row.
- `.claude/roles.json` sets `agent` true for ten of eleven roles, `gov-session` false.
- The `govkit selftest` guard adds `{prefix}/process-monitor/census.py` to the four above.

### The checks after this unit

```python
agents_want, overlays_want = derive_roles_expected(KIT_DIRS["roles"], tomllib.loads(
    (KIT_DIRS["roles"] / "kit.toml").read_text(encoding="utf-8")))
agents_got = {p.stem for p in (t / ".claude" / "agents").glob("gov-*.md")}
overlays_got = {"house/" + p.name for p in (kit / "house").glob("*.md")}
check("OC8 AC4 ...renders one agent type per agent role (%d)" % len(agents_want), agents_got == agents_want, ...)
check("OC8 AC4 ...seeds one house overlay per seed-list entry (%d)" % len(overlays_want),
      bool(overlays_want) and overlays_got == overlays_want, ...)
```

Both wants are read from gov's tree and both gots from the target, as the landed comment states
(`@c2b02d78:3232-3235`), so the install is graded against what it was handed. A set compare is as
strong as the landed sorted-list compare: a renamed role whose file count is unchanged still reds.

### Inventory

Minted: `derive_roles_expected` and the two check labels. The function is asked of
`python tools/lexicon/lexicon.py --suggest derive_roles_expected --as py.function` at the pass.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 4. Dispatch sorts a tie by id string (`tools/workflows/unattended-build.js@9da9556b:692-697`),
so `TOOL-dBoundRoles-21` builds before this unit at the same order.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Widen the leg's guard to `tools/roles/agents/`, `tools/roles/house/` and `tools/roles/kit.toml`.**
  The guard-legs join of `tools/check-spec-tokens.py` would then owe `govkit selftest` on the §7 line of
  every live spec whose Files touched names one of those paths. Measured on 2026-10-26 over the live
  specs of this tree: nine dBoundRoles specs name one and do not name the leg, so the widening reds
  `spec tokens` on nine specs this unit does not own.
- **Re-type the counts unit 1 leaves.** They move again at `TOOL-dBoundRoles-19` and at
  `TOOL-dWitnessedBar-23`, which is the defect.

## 5. Production-readiness checklist

- security — no new write path; the selftest reads a scratch target it built.
- perf / scale — one `load_roles` over about a dozen role files per install case.
- error / empty / loading states — an empty `overlays` set reds the landed overlay check's non-empty
  guard (`@c2b02d78:3250`), so an empty population never reads as coverage; `TOOL-dBoundRoles-19` S5
  re-points the OC8 house checks when its house files leave the seed rows.
- observability — each failing check prints both sets and their difference.
- risks — a descriptor whose seed row is not a list include yields no overlays; the check then reds
  against any seeded file, which names the gap.
- testing — AC1 to AC3 by probe and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0,'tools/govkit'); import selftest as s; ..."`
  imports S1's module as a library, runs no case, and prints
  `s.derive_roles_expected(s.KIT_DIRS["roles"], <the roles descriptor>)` over gov's tree after unit 1, the
  first set equals the slots `.claude/roles.json` marks `agent` true and the second equals the
  `house/*.md` entries of `tools/roles/kit.toml`'s seed row.
  Red when: either set is typed, so it disagrees with the roster or the seed row it claims to read.
  figure: both sets are DERIVED at observation time.
- **AC2** — When the same probe runs over a scratch copy of the roles kit carrying one more role file
  with `agent: true`, the first set gains exactly that slot.
  Red when: the derivation counts a fixed number, so an added role leaves it unmoved.
  fixture: the scratch copy is built under the run's scratch path by the pass.
- **AC3** — When `grep -nE 'len\(agents\) == [0-9]|glob\("\*\.md"\)\)\) == [0-9]' tools/govkit/selftest.py`
  runs on the built tree, it prints nothing.
  Red when: a typed count is left beside the roster it counts.
  figure: it prints nothing at `a01362eb0` too, the literals gone with TOOL-dWitnessedBar-23 S6; the
  criterion holds them gone.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the OC8 AC4 roles install case with S2's set checks, staged by removing one rendered `gov-*.md` from the scratch target after its apply, which reds "renders one agent type per agent role", its message naming both sets · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause unit 1
  carries whole and the coverage region would read it carried in parts; veto 1 discards it. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set and every
  promoted spec of the chain follows. widens: none · relaxes: none
- **FACT-QUESTION · F2 — Has `TOOL-dWitnessedBar-23` S6 landed the derivation at the build run's
  base?** Probe: `grep -n 'len(agents) == 9' tools/govkit/selftest.py` at that base. Observation at
  `462d20f3`: it prints line 2837, so the derivation has not landed. Liveness: that unit's AC3 makes the
  same grep print nothing, so the probe moves when it lands. RESOLVED (agent, 2026-10-26, delegated):
  the pass reads the probe; with a hit it builds S1 and S2, with none it keeps the landed derivation and
  routes it through S1. widens: none · relaxes: none
  Observation at `a01362eb0`: the probe prints nothing, and `want_agents` and `want_house` sit at
  `tools/govkit/selftest.py@c2b02d78:3240` and `:3245`, so the probe moved and the second branch holds.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 4
  (HIGH, item H5; id 47 shares the defect at MEDIUM, item M25).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dBoundRoles-49 and -50, promotions of the round-1 audit of units 37 to 44; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-54, a promotion of the round-1 audit of units 45 to 51; nothing else moved.
- rev-4 · 2026-11-22 · §7 · the leg line gains `policy fixtures`, whose guard holds `tools/govkit/selftest.py`
  that §4 Files touched names, by `2026-11-22-prompt-TOOL-dBoundRoles-14-spec-tokens-a-brief`; nothing else
  moved.
- rev-5 · 2026-11-22 · §1 · S1 S2 S3 · §3 · §4 · §5 · AC3 · §7 · §8 F2 · §10 · re-grounded at HEAD
  `a01362eb0` by `2026-11-22-prompt-TOOL-dBoundRoles-1-reground-e-brief`. TOOL-dWitnessedBar-23 S6
  landed the derivation inline, so F2's probe now selects S3's keep-and-route branch: S1 states the
  landed predicate and source kit, S2 keeps the landed labels, messages and non-empty overlay guard,
  and §5 no longer calls an empty overlay set legal. The docstring non-goal is already met; the guard
  count is four other paths; every citation is re-pointed to a symbol or a blob. Unit 1's roster
  change was checked against TOOL-dBoundRoles-1's spec, not HEAD.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-23` S6's landed derivation, spelled inline in `check_roles_install`
(`tools/govkit/selftest.py@c2b02d78:3232-3250`), which S1 lifts into one function, beside the descriptor
read `check_roles_default` makes (`tools/govkit/selftest.py#check_roles_default`, its rule walk at
`@c2b02d78:3141-3157`).
`python tools/codebase-map/reuse_lookup.py "derive an expected count from a kit seed list instead of a literal"`
ranked `counts`, `seed`, `kit_rel` and `resolve_kit_dir`, none a derivation of a roster count; the
recall probe returned `TOOL-dWitnessedBar-23` S6 as the existing design, which this unit reuses rather
than restating.

Recall terms used: `python tools/memory-recall/query.py "how is a govkit selftest count kept from drifting when the roles roster changes" --terms "govkit selftest OC8 agent types house overlays count seed roster derived literal drift"`
