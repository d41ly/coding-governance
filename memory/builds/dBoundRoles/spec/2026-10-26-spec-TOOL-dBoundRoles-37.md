# TOOL-dBoundRoles-37 — govkit's roles install case derives the agent types and house overlays it expects from the roster and the seed rows, so no roster change leaves a typed count to red

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 4 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md) | research | TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |
| [2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md) | research | TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 4 at
HIGH**, report item **H5**. Id 47 is the same defect seen from the blast-radius lens at MEDIUM, report
item M25, and takes its own scope item in `TOOL-dBoundRoles-43`.

`tools/govkit/selftest.py:2837` checks `len(agents) == 9` and `:2838` checks ten seeded house
overlays, both typed. `TOOL-dBoundRoles-1` S2 and S3 add four roles with four empty overlays and remove
the two reviewers, so both literals are wrong once unit 1 lands. The `govkit selftest` leg's guard in
`tools/gate-legs.json` covers `{prefix}/govkit/` and three other paths, none under `tools/roles/`, so a
guarded run skips the leg and the red surfaces on a later, unrelated govkit change.

This unit replaces both literals with sets derived at run time: the agent-true roles of the installed
roles kit, and the `house/*.md` entries of the roles descriptor's seed rows. A roster change then
moves the expectation with it. It repairs `TOOL-dBoundRoles-1` and builds one step after it (order 4).

## 2. Scope (IN)

- **S1** — The derivation, `derive_roles_expected(kit, descriptor)` in `tools/govkit/selftest.py`,
  returning `(agents, overlays)`. `agents` is the set of slots of `kit`'s `agents/*.agent.md` whose
  front matter sets `agent: true`, read through the installed kit's own `roles_lib.load_roles`
  (`tools/roles/roles_lib.py:330`), loaded by path with `importlib.util`, so the selftest carries no
  second front-matter grammar. `overlays` is the set of `include` entries matching `house/*.md` in the
  descriptor's `[[files]]` rows whose `role` is `seed`, the rows `check_roles_default` already reads
  through `gk.read_descriptors` (`tools/govkit/selftest.py:2720`, the rules at `:2745`). Observed by
  AC1 and AC2.
- **S2** — The two checks of `check_roles_install` compare sets. "renders nine agent types" becomes
  "renders one agent type per agent-true role": the `gov-*.md` stems under the target's
  `.claude/agents` equal `agents`. "seeds ten house overlays" becomes "seeds every house overlay its
  descriptor lists": the `house/*.md` names under the installed kit equal `overlays`. Each failure
  prints both sets and their difference. Observed by AC2 and AC3.
- **S3** — Built once. Where `TOOL-dWitnessedBar-23` S6 has landed the same derivation at the build run's
  base, this pass keeps it, routes it through S1's function if it is spelled inline, and adds nothing
  beside it; otherwise this pass builds S1 and S2 in that section's form (§8 F2). Observed by AC3.

## 3. Non-goals (OUT)

- The docstring of `check_roles_install` (`tools/govkit/selftest.py:2769`), which still says "nine
  agent types, ten seeded house overlays": `TOOL-dBoundRoles-43`'s, for id 47.
- The `OC8 AC2` check that every house overlay is a seed row (`:2756`), which reads the files present:
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

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/govkit/selftest.py:2837-2839` holds the two typed checks, and `:2818` resolves the installed
  kit as `kit`.
- `tools/roles/kit.toml:35-40` names ten `house/*.md` seeds and `house/policy.toml` in one `seed` row.
- `.claude/roles.json` at base sets `agent` true for nine of ten roles, `gov-session` false.
- `tools/gate-legs.json`'s `govkit selftest` row has the guard `{prefix}/govkit/`,
  `{prefix}/hooks/kit.toml`, `{prefix}/settings-merge.py` and `{prefix}/codebase-map/kit.toml`.

### The checks after this unit

```python
agents_want, overlays_want = derive_roles_expected(kit, descs["roles"][0])
agents_got = {p.stem for p in (t / ".claude" / "agents").glob("gov-*.md")}
overlays_got = {"house/" + p.name for p in (kit / "house").glob("*.md")}
check("OC8 AC4 ...renders one agent type per agent-true role", agents_got == agents_want, ...)
check("OC8 AC4 ...seeds every house overlay its descriptor lists", overlays_got == overlays_want, ...)
```

`descs` is read once per call through the same `gk.read_descriptors(GOV_ROOT, reg, rep)` that
`check_roles_default` uses. A set compare is stronger than a count: a renamed role whose file count is
unchanged still reds.

### Inventory

Minted: `derive_roles_expected` and the two check labels. The function is asked of
`python tools/lexicon/lexicon.py --suggest derive_roles_expected --as py.function` at the pass.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 4. Dispatch sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`),
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
- error / empty / loading states — an empty `overlays` set is legal and compares equal to an empty
  `house` folder, the state `TOOL-dBoundRoles-19` leaves.
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

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the OC8 AC4 roles install case with S2's set checks, staged by removing one rendered `gov-*.md` from the scratch target after its apply, which reds "renders one agent type per agent-true role" naming the missing slot · none

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

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 4
  (HIGH, item H5; id 47 shares the defect at MEDIUM, item M25).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dBoundRoles-49 and -50, promotions of the round-1 audit of units 37 to 44; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-23` S6, which specifies the same two derivations, and the descriptor read
`check_roles_default` already makes (`tools/govkit/selftest.py:2720`, its rule walk at `:2745-2757`).
`python tools/codebase-map/reuse_lookup.py "derive an expected count from a kit seed list instead of a literal"`
ranked `counts`, `seed`, `kit_rel` and `resolve_kit_dir`, none a derivation of a roster count; the
recall probe returned `TOOL-dWitnessedBar-23` S6 as the existing design, which this unit reuses rather
than restating.

Recall terms used: `python tools/memory-recall/query.py "how is a govkit selftest count kept from drifting when the roles roster changes" --terms "govkit selftest OC8 agent types house overlays count seed roster derived literal drift"`
