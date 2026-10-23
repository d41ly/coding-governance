# TOOL-dGroundRules-23 — the registry join holds each census row's destination and entry to what the deployer installs

**Status:** DEFERRED · rev-5 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 7 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-23-deviation-11.md](../build/2026-10-23-build-TOOL-dGroundRules-23-deviation-11.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-23-deviation-57.md](../build/2026-10-23-build-TOOL-dGroundRules-23-deviation-57.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-23-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-23-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-23-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-23-build-brief.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-23-mark-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-23-mark-task.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-24 TOOL-dGroundRules-22 TOOL-dGroundRules-25 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 13 to 21
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md`)
exited CONVERGED with finding **id 38 at HIGH**, which shares item **H1** with id 10
(`TOOL-dGroundRules-22`). This unit is id 38's promotion. It repairs `TOOL-dGroundRules-17`, which
sits at order 6, so it builds at order 7.

Id 38 is H1 seen from the failure envelope, and its skeptic rejected the finder's fix for a reason
of its own: `tools/govkit/registry.toml:296` exempts `{prefix}/govkit`, so an adopter has no
registry, and a shipped arm cannot resolve an enforcer "by the registry entry that ships it" there.
`TOOL-dGroundRules-22` therefore records each row's destination and entry statically in the census.
A static copy of a descriptor fact drifts unless something compares the two, and the place that can
compare them is gov's own tree, where the registry lives. This unit is that comparison: it extends
`TOOL-dGroundRules-17`'s gov-only `budgets-ships-join` so every census row's `installed` and `kit`
equal what the deployer's own resolver says the entry writes.

## 2. Scope (IN)

- **S1** — The join. `budgets-ships-join` in `CASES` of `tools/policy/check_policy.py` loads
  `govkit.py` from the source repository's derived tool root through `importlib`, reads the
  registry and its descriptors with `load_registry` and `read_descriptors`, and resolves each
  entry's writes with `resolve_entry` under `canonical_ctx`. For each `ships = true` census row it
  asserts that the entry its `kit` names writes the row's `enforcer` source, and that the
  destination it writes, with gov's tool root spelled `{prefix}`, equals the row's `installed`.
  Observed by AC1, AC2.
- **S2** — Both ways. The same join asserts that no other entry writes a shipped row's enforcer
  source, and that each `ships = false` row carries neither field, as `TOOL-dGroundRules-17` S6
  asserts its `ships` flags against the `[[exempt]]` rows. Observed by AC2.
- **S3** — Every path derived. The case locates `govkit.py` and the registry from the kit's own
  resolved tool root, never as a literal kit segment, as `TOOL-dGroundRules-16` §4 states for its
  own case. Observed by AC1.
- **S4** — The guard. The `policy fixtures` row in `tools/gate-legs.json` gains
  `{prefix}/govkit/govkit.py`, `{prefix}/govkit/entries/` and the descriptor of each entry a census
  row's `kit` names, exact files, each one the row does not already carry, derived from the census
  at build. Observed by AC3.

## 3. Non-goals (OUT)

- The row fields and the shipped arm that grades an adopter at `installed`:
  `TOOL-dGroundRules-22`, id 10's promotion, which shares item H1.
- Any read of the registry by a shipped arm. The join runs only under `--fixture`, in the
  `policy fixtures` leg, which is gov's alone (`TOOL-dGroundRules-1` §4 "The adopter").
- A second expander of `[[files]]` rules. The join asks govkit's own resolver (§8 F1).

### Edges

- **consumes-from** `TOOL-dGroundRules-17` — `budgets-ships-join`, its `[[exempt]]` half and the `{prefix}/govkit/registry.toml` guard line, which this unit extends
- **consumes-from** `TOOL-dGroundRules-22` — the census fields `installed` and `kit`, which this join holds to the registry; without them it has nothing to compare
- **hands-off** `TOOL-dGroundRules-32` — `budgets-ships-join` and its guard lines, which that unit routes through `read_shipped_descriptors` and extends to every census kit's descriptor (findings 13, 5)
- **hands-off** `TOOL-dGroundRules-34` — `budgets-ships-join`'s in-process `importlib` load of the deployer, which that unit routes through `resolve_govkit` (id 3 of the round-1 spec audit of units 26 to 32)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `tools/govkit/registry.toml:296` is the `{prefix}/govkit` `[[exempt]]` row: "never installed into
  a target".
- `resolve_entry(root, desc, ctx)` (`tools/govkit/govkit.py:452`) returns `writes`, each resolved
  destination mapped to the row whose `src` lands there, after the project-owned carve-out
  (`:470-492`).
- `canonical_ctx(eid)` (`tools/govkit/govkit.py:498-508`) resolves `{prefix}` to gov's own derived
  tool root and takes every opt-in, so it answers what gov can ship.
- `cmd_check` reads the registry and its descriptors with `load_registry(root)` and
  `read_descriptors(root, reg, r)` (`tools/govkit/govkit.py:5413-5414`).
- `tools/govkit/entries/kickoff-manifest.kit.toml:17` writes `manifest-check.sh` to
  `{prefix}/manifest-check.sh`; `tools/govkit/entries/check-line-length.kit.toml:21-24` writes
  `check-line-length.sh` to `{prefix}/{relpath}`.

### The join

```text
govkit   = importlib load of <source tool root>/govkit/govkit.py
writes   = { eid: govkit.resolve_entry(root, desc, govkit.canonical_ctx(eid))["writes"] }
for each census row r with ships = true:
    src  = r.enforcer with {prefix} spelled as gov's tool root
    hits = every (eid, dest) whose writes row has src == src
    WRONG unless hits == [(r.kit, r.installed with {prefix} spelled as gov's tool root)]
for each census row r with ships = false:
    WRONG if r carries installed or kit
```

A failed line names the row, the entry and the destination the resolver gave.

### Rollout

Order 7 holds this unit and `TOOL-dGroundRules-22`, and this unit reads that one's fields while
both write `tools/policy/check_policy.py`, so the two are not a parallel group by BUILD-METHOD M6's
first two clauses. The inline author builds `TOOL-dGroundRules-22` first and this unit after it.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `budgets-ships-join` | `CASES` entry, extended | `tools/policy/check_policy.py` |

No function is minted.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/gate-legs.json`

### Alternatives rejected

- **Parse each descriptor's `to` strings inside the case.** A second expander of the rules govkit
  resolves, which `expand_rules`'s own comment (`tools/govkit/govkit.py:435-439`) records as the class
  this repo keeps a record about (§8 F1).
- **Run `govkit.py plan` over a scratch target and read its rows.** It needs a target descriptor and
  a clone per run, to answer a question the resolver answers in process.

## 5. Production-readiness checklist

- security — N/A: a gov-only test case that reads the registry and writes nothing.
- perf / scale — one `govkit.py` import and one resolve per census entry, under `--fixture` only.
- error / empty / loading states — a `govkit.py` that does not import, or a census with no shipped
  row, is the case's `WRONG`, never a pass, because a join over nothing proves nothing.
- observability — each `WRONG` names the row, the entry and the resolved destination.
- risks — a descriptor's `to` changing without the census; this join reds it on gov's tree.
- testing — the extended case under `--fixture`, with AC1 to AC3.
- migration — none.
- user docs — N/A: a gov-only case and a manifest guard.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py` and `caps.toml` under the kit, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python check_policy.py --fixture budgets-ships-join` runs on the built tree, it
  passes; with the `manifest-bytes` row's `installed` staged to a destination under the kickoff
  entry's home in a scratch copy of `caps.toml`, it prints `WRONG` naming `manifest-bytes` and the
  resolver's `manifest-check.sh` destination.
  Red when: a census destination can drift from the descriptor that installs it.
- **AC2** — When the `line-length` row's `kit` is staged to `memory-tree`, the same case prints
  `WRONG` naming `line-length` and `check-line-length`; with `installed` staged onto a
  `ships = false` row, it prints `WRONG` naming that row.
  Red when: a row names the wrong entry, or an unshipped row claims a destination.
- **AC3** — When `python tools/check-spec-tokens.py --legs-for tools/govkit/govkit.py
  tools/govkit/entries/check-line-length.kit.toml` runs on the built tree, it names
  `policy fixtures` for each path.
  Red when: an edit to the resolver or a descriptor alone skips the leg the join runs in.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the case; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture budgets-ships-join`) · covers AC1 AC2 · one shipped row's `installed` staged off its resolved destination, then one row's `kit` staged to another entry · none

## 8. Open questions

- **F1 — How does the join learn where an entry installs an enforcer?** (a) govkit's own
  `resolve_entry` under `canonical_ctx`, loaded from the source repository. (b) The case parses each
  descriptor's `[[files]]` rules itself. (c) `govkit.py plan` over a scratch target. (b) is a second
  expander, which fails the charter's `[reuse]` rule; (c) meets every criterion and costs a target
  and a subprocess per run. (a) meets every criterion with the one resolver `apply` itself uses.
  Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 38 (HIGH, item H1) of the round-1 spec
  audit of units 13 to 21, from the skeptic's corrected fix and govkit's resolver and the two entry
  descriptors read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-32 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 22 to 25 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-4 · 2026-10-23 · §8 · F1's resolved mark rejoined onto one line, its RESOLVED beside
  `widens: none · relaxes: none`, because the departures report reads a mark per line. The mark's
  meaning is unchanged.
- rev-5 · 2026-10-23 · §1 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling, the id a landed dSafePassage ask holds; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-17`'s `budgets-ships-join`, which gains the destination
and entry half beside its `[[exempt]]` half, and govkit's `resolve_entry` with `canonical_ctx`, the
resolver `plan` and `apply` share. `python tools/codebase-map/reuse_lookup.py "install a kit into a
scratch target with the deployer and read its receipt"` ranked `read`, `read_text`, `scratch`,
`kit_rel` and `resolve_kit_dir`, none of which resolves a descriptor's writes, so the resolver was
found by reading `tools/govkit/govkit.py:424-494`. The recall probe returned this audit's H1, which this
unit follows, and `DEPL-aLevelledCopy-2`, an ask about a new engine row's file mode after
`govkit apply`, which does not bear on the join.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture install a kit into a
scratch target with govkit apply" --terms "govkit apply scratch target deploy.toml receipt
install.json fixture requires project-owned withheld"`
