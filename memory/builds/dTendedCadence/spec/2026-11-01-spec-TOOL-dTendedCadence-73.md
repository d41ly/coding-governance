# TOOL-dTendedCadence-73 — the role counts govkit's selftest and the runbook state are derived from the roles kit, so an eleventh role reds nothing it did not change

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 23 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-74 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 29 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, item H8. Unit 59 S11 and AC11 grep for spelled counts only under `tools/roles`. Unit 10's
eleventh role, `gov-maintainer` with an agent file and a house overlay (spec-10 §4 Files touched), also
breaks `tools/govkit/selftest.py:2837-2838`, which asserts nine rendered agent types and ten seeded
house overlays, and `WIRE-INTO-PROJECT.md:709`, which tells adopters "The ten files under
`<prefix>/roles/house/`". The `govkit selftest` leg's guard does not cover `tools/roles/`
(`tools/gate-legs.json`), so the build's guarded bar never runs it and the red surfaces on remote CI's
full run. This unit derives both counts from the roles kit and widens the criterion to every file that
spells one.

## 2. Scope (IN)

- **S1** — The selftest counts. The roles case of `tools/govkit/selftest.py` derives its expected agent
  count from the rendered `.claude/roles.json` of the scratch target, the roles whose `agent` is true,
  and its expected overlay count from the source kit's `tools/roles/house/*.md`, and compares the
  rendered agents and the seeded overlays with those. The literals 9 and 10 at `:2837-2838`, and the
  counts spelled at `:2769` and `:6887`, are not kept. Observed by AC1.
- **S2** — The runbook. `WIRE-INTO-PROJECT.md:709` reads "The files under `<prefix>/roles/house/`",
  naming no count. Observed by AC2.
- **S3** — The criterion, in place. Unit 59 S11 and AC11 read `git grep -n -i "the ten\|ten
  declared\|one of the ten\|ten files\|ten house\|nine agent" -- tools/roles WIRE-INTO-PROJECT.md
  tools/govkit`, which exits 1 printing nothing at the close; at base it prints ten lines (PINNED
  2026-11-01 by that command). Corrected in spec-59's text, a rev bump with a §9 line naming review
  id 29. Observed by AC2.

## 3. Non-goals (OUT)

- Adding `tools/roles/` to the `govkit selftest` leg's guard in `tools/gate-legs.json`: the report's
  left-shift gate, a gate change of its own; S1 makes the leg's verdict independent of the count.
- The roles kit's own spelled counts: unit 59 S11's original population, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-59` — S11 and AC11, whose grep this unit widens to every file that spells a role count
- **consumes-from** `TOOL-dTendedCadence-10` — the eleventh role and its house overlay, the change the derived counts absorb

## 4. Design

```python
idx = json.loads((t / ".claude" / "roles.json").read_text(encoding="utf-8"))
want_agents = sum(1 for r in idx["roles"].values() if r.get("agent"))
want_house = len(list((ROOT / "tools" / "roles" / "house").glob("*.md")))
check("OC8 AC4 ...renders one agent type per agent role", len(agents) == want_agents, ...)
check("OC8 AC4 ...seeds every house overlay", len(list((kit / "house").glob("*.md"))) == want_house, ...)
```

`render_roles_index` writes each role's `agent` flag into the index
(`tools/roles/render_agents.py:212`), so the index is the renderer's own answer to "which roles get an
agent type". The source house directory is what the installer seeds, so the overlay count follows the
kit. A floor is kept: each expected count must be at least 1, so an empty index cannot pass.

### Inventory

Minted: nothing.

### Files touched (estimate)

- `tools/govkit/selftest.py`: S1
- `WIRE-INTO-PROJECT.md`: S2
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-59.md`: S3

### Alternatives rejected

- **Bump the literals to 10 and 11.** The next role reds the same leg on a file its unit never names.
- **Derive the agent count from `tools/roles/agents/*.agent.md`.** It counts the `agent: false` roles
  too (ten files at base against nine rendered types), so it needs a second reading of the flag the
  index already carries.

## 5. Production-readiness checklist

- security — N/A — a test's expectation and a runbook sentence.
- perf / scale — one JSON read and one glob per run of the case.
- error / empty / loading states — an index with no agent role, or a kit with no overlay, fails the
  floor and names itself.
- observability — each check prints the rendered and the expected names, as it does today.
- risks — the derived count follows the renderer, so a renderer that drops a role from both the index
  and the agents still passes; the role catalogue's own leg grades the catalogue.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no adopter state moves.
- user docs — `WIRE-INTO-PROJECT.md`, S2.

## 6. Acceptance criteria

- **AC1** — When `grep -n "== 9\|== 10" selftest.py` runs in `tools/govkit/`, no hit sits in the roles
  case, and that case, run once against a scratch kit carrying one extra house overlay and one extra
  agent role, passes; run against a scratch target whose rendered agents lack one role, it fails.
  Red when: a role-count literal survives, or the derived count passes a missing agent.
- **AC2** — When the grep of S3 runs, it exits 1 printing nothing, and `grep -n "files under
  .<prefix>/roles/house/." WIRE-INTO-PROJECT.md` matches with no count before it.
  Red when: a spelled role count survives the eleventh role outside `tools/roles`.
  figure: the ten base hits are PINNED 2026-11-01.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `recall floor` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the roles case over a scratch kit with one more role and overlay, staged against the literals 9 and 10 once unit 10 lands · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 29 (HIGH, item H8) of the round-1 spec
  audit of units 49 to 59.

## 10. Reuse audit

The seam is the roles kit's rendered index, `render_roles_index` (`tools/roles/render_agents.py:207`),
whose `agent` flag the selftest reads, and the govkit selftest's existing roles case
(`tools/govkit/selftest.py:2835-2840`). `python tools/codebase-map/reuse_lookup.py "count the role
agents a roles kit renders"` ranked name stems only, `counts`, `resolve_kit_dir`, `render` and
`kit_rel`, none a counter of role agents, so the seam is named here from source.

Recall terms used: `python tools/memory-recall/query.py "where is the number of roles spelled"
--terms "roles kit house overlays agent types govkit selftest spelled count runbook gov-maintainer
eleventh role"`
