# TOOL-dDeclaredLoop-57 — `update` refuses a claimed kit whose `requires` it leaves unmet, on every admission path

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-deviation-571.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-deviation-571.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 52 at HIGH**, its item **H6**, alone in that item. `TOOL-dDeclaredLoop-36` S2
relies on `update`'s default-gained path to install the loop kit beside a roles kit that now requires
it. That path gains nothing when the receipt records no `gov_commit` (`tools/govkit/govkit.py:987-988`)
or when the registry does not resolve or parse at either vintage (:991-1000), and the only `requires`
check in `cmd_update` (:9247-9259) reads the gained kits alone, never the kits the receipt already
claims. On those paths an adopter's roles kit updates to a version that reads a loop kit the target
lacks, and the update succeeds with one `default-gained: none computed` line. This unit takes the
report's fix. It repairs `TOOL-dDeclaredLoop-36`.

## 2. Scope (IN)

- **S1** — One predicate call after the gained set is final: `cmd_update` passes the claimed kits plus
  the gained ones to `derive_unsatisfied_requires` (`tools/govkit/govkit.py:950`), the one predicate
  `apply` refuses by, through a new function `demand_claimed_requires(claimed, gained, descs, receipt,
  why)`. A non-empty answer raises `Refusal` before any write, read-only runs included, naming each
  `(kit, dependency)` pair and `apply --kits <kit> <dependency>` as the route. Observed by AC1, AC2.
- **S2** — The refusal names why the default-gained path did not cover the pair, carrying the `why`
  string `derive_default_gained` already returns, so "no vintage" and "registry unreadable at a
  vintage" read differently from "the default never held it". Observed by AC1, AC2.
- **S3** — The loop kit's own `requires memory-tree` (`TOOL-dDeclaredLoop-56` S17) is graded by the
  same call: a receipt claiming `loop` without `memory-tree` refuses naming that pair. This corrects
  `TOOL-dDeclaredLoop-36` §5's risk line, which accounted only for roles. Observed by AC3.
- **S4** — The gained-only loop at `tools/govkit/govkit.py:9247-9259` is unchanged and runs first, so a
  gained entry it leaves out is never the subject of S1's refusal, and the ordinary path, a receipt
  with a resolvable `gov_commit` whose default gained `loop`, still installs it. Observed by AC4.

## 3. Non-goals (OUT)

- A `--kits`-scoped update that names roles but not loop: S1 refuses it too, which is the narrower
  statement's own consequence; widening the selection stays the operator's act, as the owner ruled for
  `apply` (`tools/govkit/govkit.py:7553-7555`).
- The default-plan pins `TOOL-dDeclaredLoop-36` does not re-measure: the audit's id 41, batched into
  `TOOL-dDeclaredLoop-67`.
- A selftest arm over every admission path of every verb, the finding's left-shift at full width: the
  arm under §7 covers `update`'s three paths, which are the ones the finding names.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-36` — `loop` in the registry's default set and the default-gained migration it relies on, whose uncovered paths this unit refuses

## 4. Design

### Evidence

- `derive_default_gained` returns `([], why)` for a receipt with no `gov_commit` (:987-988) and for a
  registry that does not resolve or parse at either vintage (:994-1000): read at base `ed497191`.
- `cmd_update` reads the receipt's `kits` at :9234 and checks only that each is still a registry entry
  (:9235-9240); the `requires` loop at :9247 passes `gained`, so a claimed kit's dependency is never
  asked about.
- `apply` refuses through the same predicate with no receipt, so the update and the install answer one
  question one way after this unit.

### The call

```python
def demand_claimed_requires(claimed, gained, descs, receipt, why):
    unmet = derive_unsatisfied_requires(list(claimed) + list(gained), descs, receipt)
    if unmet:
        pairs = ", ".join(f"'{k}' requires '{d}'" for k, d in unmet)
        raise Refusal(f"update would leave {pairs} unmet"
                      + (f"; default-gained did not cover it: {why}" if why else "")
                      + f"; `apply --kits {unmet[0][0]} {unmet[0][1]}` installs both")
```

It is called once, after the gained loop and before `if gained and write:`, so nothing is written on a
refusal.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Pulling the missing dependency in.** It widens the operator's selection, which the owner ruled
  against for `apply`; the refusal names the route instead.
- **A warning line.** The finding's consequence is a broken install that prints one line today; a
  second line is the same defect.

## 5. Production-readiness checklist

- security — a refusal before any write; no new write path.
- perf / scale — one predicate call over the claimed set, a dozen kits.
- error / empty / loading states — an empty claimed set and an empty gained set pass; the refusal
  names every pair, never only the first.
- observability — the refusal text carries the default-gained `why`.
- risks — an adopter that deleted the loop kit by hand while its receipt claims roles is now refused
  on update; that install was already broken, and the route is named.
- testing — AC1 to AC4 as probes; the arm under §7, observed at the close.
- migration — none: a refusal on a path that produced a broken install.
- user docs — none: `help/` holds no page for govkit's update refusals.

## 6. Acceptance criteria

- **AC1** — When a probe applies the default selection at base `ed497191` into a scratch target, deletes
  `gov_commit` from its install receipt, `install.json`, and runs `python tools/govkit/govkit.py update
  --to <this unit's commit>`, it exits with a refusal naming `'roles' requires 'loop'` and the no-vintage
  reason, and `git status --porcelain` in the target prints nothing.
  Red when: the update proceeds and prints `default-gained: none computed`.
  fixture: a scratch target under a short `%TEMP%` path; it runs after this unit's commit, because
  `update` reads `--to` as a commit.
- **AC2** — When a probe imports `govkit` and calls `demand_claimed_requires(["roles"], [], descs,
  {"kits": ["roles"]}, "registry.toml does not resolve at 0000000")` over the live descriptors, it
  raises `Refusal` whose text names `'roles' requires 'loop'` and `does not resolve`.
  Red when: the function returns, so the unreadable-vintage path writes a roles kit without loop.
- **AC3** — When the same probe passes fixture descriptors in which `loop` requires `memory-tree` and a
  receipt claiming `loop` alone, the refusal names `'loop' requires 'memory-tree'`.
  Red when: only roles' dependency is graded.
- **AC4** — When the probe takes a target applied at base and runs `govkit.py update --write --to <this
  unit's commit>` with its receipt intact, it prints `default-gained loop` and no refusal.
  Red when: S1 refuses a gained entry, so the ordinary migration breaks.
  cost: two installs into scratch targets, seconds each.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · a receipt with no gov_commit, an unreadable vintage and a loop claim without memory-tree, each staged against the base update, which writes · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 52 (HIGH, item H6).

## 10. Reuse audit

The seam is govkit's one requires predicate, `derive_unsatisfied_requires`
(`tools/govkit/govkit.py:950`), the function `apply` refuses by; this unit adds one call to it over the
claimed set and no second reader. `python tools/codebase-map/reuse_lookup.py "update refuses a claimed
kit whose requires are unmet"` ranked `claims`, `kit_rel`, `resolve_kit_dir` and two process-monitor
refusal classes, none of which reads `requires`; the predicate was read above and agrees with source.

Recall terms used: govkit update requires claimed gained default-gained gov_commit vintage receipt roles loop refusal
