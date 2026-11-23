# TOOL-dTotalRecall-59 — the merged legacy registration is judged at the run's real compare base, where it is new, and its `shrink-only` is proved on a fixture base that holds it

**Status:** DEFERRED · rev-3 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 29 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md](../build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 13 at HIGH**, its item **H3**, alone in that item. `TOOL-dTotalRecall-52`
(order 28) says the merged home "gains every causes row its base lacked" and is refused `gained`,
and S2 builds an `absorbs` read of the absorbed population's home at the compare base to prevent
that. `compare_to_base` judges at `tools/lib/compare_base.py#resolve_compare_base`
(`TOOL-dWitnessedBar-13` §4), HEAD's merge-base with `origin/main`, `8b8b1374c` at 2026-11-23
(DERIVED by `git merge-base HEAD origin/main`). Neither home exists there: units 1 and 19 mint both
on the unmerged run branch. The ratchet reads a home absent at the base `new at <sha12>` with its row
count, graded no further (`ratchet.py#check_new_at_base`, `TOOL-dWitnessedBar-51` S30; its §8 F7
minted no `first seed` reading), and `compare_to_base` returns no findings, never `gained`. So an
`absorbs` read would read nothing. After the close merge, `legacy-records` never reaches `main`,
because unit 52 S3 deletes its home first, so no base anywhere will ever hold it. It repairs
`TOOL-dTotalRecall-52`. Unit 52 builds no `absorbs` field (`TOOL-dTotalRecall-62`), so this unit
grounds the judgement on the real base and proves `shrink-only` on a fixture base.

## 2. Scope (IN)

- **S1** — The judgement at the run's base. At this run's compare base the merged
  `record-kinds-legacy` home is absent, so `ratchet.py#check_new_at_base` reads it `new at <sha12>`
  (`TOOL-dWitnessedBar-51` §8 F7) and `compare_to_base` names no `gained` key. Nothing is added to make
  that so: it is the S30 rule, observed. Observed by AC1.
- **S2** — `absorbs` is absent. Unit 52 builds no such field, so the registration and the factory
  carry none. Observed by AC2.
- **S3** — `shrink-only` proved where it can bite. A fixture whose base commit holds the merged home
  shows a planted extra `causes` row named `gained`, and an unchanged home naming none. Observed by
  AC3.

## 3. Non-goals (OUT)

- The triple key and the old name's carriers: `TOOL-dTotalRecall-52` S1 and S3, unchanged.
- The factory's absent-home and legacy-grammar rules: `TOOL-dWitnessedBar-51` S30's.
- Re-keying any base that holds `legacy-records`: no such base exists, which is why unit 52 builds
  none.

### Edges

- **consumes-from** `TOOL-dTotalRecall-52` — the merged registration, judged here at the real base
  and on a fixture base
- **hands-off** `TOOL-dTotalRecall-60` — the merged registration with `absorbs` absent, against which
  that unit re-observes unit 52's AC3 grep for ids 6 and 12
- **consumes-from** `TOOL-dTotalRecall-62` — S2 as that unit amends it in step 28, observing `absorbs` absent (the round-1 audit of units 54 to 60, id 2)
- **hands-off** `TOOL-dTotalRecall-66` — the fixture and its plant `merged-home-gained`, which that unit moves into the factory's arm and scrubs of the caller's environment (the round-1 audit of units 54 to 60, ids 6, 19, 31, 34 and 37)

## 4. Design

### The registration

The registration is `TOOL-dTotalRecall-52` §4's block, unchanged by this unit.

### The probe

AC1 and AC3 read one probe, run from `tools/memory-tree/`:

```
python -c "import ratchet, legacy_ledger as LL; root = ratchet.resolve_root('.'); sha, why = LL.resolve_compare_base(root); reg = [r for r in LL.read_registrations(root) if r.population == 'record-kinds-legacy'][0]; print(ratchet.check_new_at_base(root, reg, sha), LL.compare_to_base(root, reg))"
```

At the run's base it prints `True` and `compare_to_base`'s `(None, 'no memory/project/record-kinds-legacy.txt at <sha12> (merge-base of HEAD and origin/main)')`; at a base holding the home it prints `False` and the findings.

### The fixture

A scratch repository under `%TEMP%/<short>`, a short path because a clone under the run's scratch
directory fails with `Filename too long`. Its `origin/main` commit holds a merged home of two rows;
the working branch holds three, the third a `causes` row neither base row carried. `compare_to_base`
run there resolves the merge-base as its base, as it does in this repository.

### Inventory

Minted: the fixture plant `merged-home-gained` in `legacy_ledger.py`'s self-test. Naming cell: none.

### Files touched (estimate)

- `tools/lib/legacy_ledger.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

`TOOL-dTotalRecall-53` builds at order 29 too and writes `legacy_ledger.py` (S6), so BUILD-METHOD M6
sequences the two passes.

### Alternatives rejected

- **Keep `absorbs` for an adopter whose base holds `legacy-records`.** No adopter receives that
  population: it is minted and deleted on this run branch, and kits ship from `main`.
- **Seed the merged home on `main` before the build.** It would need a landing outside this build's
  write rule and changes nothing a correct build needs.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — none: the fixture repository is made once per arm run.
- error / empty / loading states — a home absent at the base reads `new at <sha12>`.
- observability — `ratchet (never gains)` prints `record-kinds-legacy · new at <sha12> · <n> rows`.
- risks — none beyond the window in which a home `new at` its base is graded no further, which the
  batch `TOOL-dTotalRecall-66` bounds.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none: no field is built or removed.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's probe runs from `tools/memory-tree/` at the pass tip, it prints `True` for
  `check_new_at_base`, the `new at` reading, and `compare_to_base` names no `gained` key.
  Red when: it names a `gained` key, `check_new_at_base` prints `False`, or it reads a base home this
  run's merge-base does not hold.
- **AC2** — When `git grep -n "absorbs" -- legacy_ledger.py` runs from `tools/lib/`, and
  `git grep -n "absorbs" -- tools/govkit/registry.toml` from the root, at the pass tip, each prints
  nothing.
  Red when: the field, its read or its refusal survives.
- **AC3** — When the same probe runs in the fixture of §4, it names the planted `causes` key `gained`;
  with the planted row removed, it names none.
  Red when: a row the base home lacked passes `shrink-only`.
  fixture: the scratch repository under `%TEMP%/<short>`; the pass makes it.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/lib/legacy_ledger.py · covers AC3 · the plant `merged-home-gained`, a fixture base holding the merged home, staged by reading the base as absent · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 13
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-62, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-11-23 · title · §1 · S1 S2 · §3 · §4 · §5 · AC1 AC2 · §7 · §10 ·
  amended by TOOL-dTotalRecall-62 (id 2, item H2) per
  `2026-11-22-prompt-TOOL-dTotalRecall-62-build-brief`: unit 52 builds no `absorbs`, so S2 observes it absent and AC2's second grep reads
  `tools/govkit/registry.toml`; S1, AC1 and §5 name the ratchet's `new at` reading through §4's probe
  (`TOOL-dWitnessedBar-51` §8 F7); the title, §4, §5, the New arm and the edges carry no cut; §1 and
  §10 cite `tools/lib/compare_base.py#resolve_compare_base` and the base `8b8b1374c`, and §4 points at
  unit 52's registration block. S3 and AC3, the fixture proof, unchanged.

## 10. Reuse audit

The seam is the ledger factory's own base read, `legacy_ledger.py#compare_to_base` at
`tools/lib/compare_base.py#resolve_compare_base` (`TOOL-dWitnessedBar-13` §4), with the ratchet's
absent-base reading `ratchet.py#check_new_at_base` (`TOOL-dWitnessedBar-51` S30); this unit adds
nothing to either. `python tools/codebase-map/reuse_lookup.py "a shrink-only keyed baseline of counted sites"`
is the lookup the factory's own §10 records, and `git merge-base HEAD origin/main` printed `8b8b1374c`
here (DERIVED 2026-11-23).

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
