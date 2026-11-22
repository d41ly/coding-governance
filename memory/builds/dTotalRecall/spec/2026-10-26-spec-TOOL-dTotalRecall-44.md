# TOOL-dTotalRecall-44 — the split census keys on the split's shape, so it lists every id reader whatever its value is named

**Status:** DEFERRED · rev-3 · 2026-11-22 · node d · Tier-2 · base 8b8b1374 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-44-deviation-441.md](../build/2026-10-26-build-TOOL-dTotalRecall-44-deviation-441.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-44-round2-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-44-round2-fix-return.md) | research | — |
| [2026-11-22-build-TOOL-dTotalRecall-44-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-44-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-44-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-44-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-44-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-44-round2-fix-brief.md) | research | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-44-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-44-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-44-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-44-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**. It shares item **H1** with id 35, which `TOOL-dTotalRecall-45`
closes. `TOOL-dTotalRecall-38` S2 lists a hyphen split only where the split value's name holds `id`,
`slug` or `unit`. Two of that unit's own ten readers split a value named `i`:
`tools/memory-recall/check-recall.py#derive_probe_labels` (`i.split("-")[1] != spec["slug"]`,
`tools/memory-recall/check-recall.py@462d20f3:511`) and `tools/memory-tree/gen_build_index.py#cmd_new_build`
(`i.split("-")[1]` in a sort key, `tools/memory-tree/gen_build_index.py@462d20f3:4073`). Unit 38 rev-4
narrowed its AC2 to the eight readers its predicate reaches and greps the two by text (its §8 F2), so its
census still prints clean over any reader whose value bears another name. This unit keys the predicate
on the split's shape and reads no value name. It repairs `TOOL-dTotalRecall-38`.

## 2. Scope (IN)

- **S1** — The Python split shape. `id_grammar.py --readers` lists a line that calls `.split("-")` or
  `.split('-')` with no maxsplit argument, unless the call is indexed `[0]` at once. The family is the
  text before the first hyphen, so a hyphen inside a slug cannot move index 0, while index 1, a later
  index, a slice, an unpacking and a bound list all can. A `.rsplit("-", 1)` indexed `[1]` or `[-1]` is
  not listed, because it reads the sequence after the last hyphen. The predicate reads no value name.
  Observed by AC1 and AC2.
- **S2** — The shell shapes `TOOL-dTotalRecall-38` S2 names (`cut -d-`, `cut -d '-'`, `IFS=-` and the
  four suffix and prefix expansions) are listed by shape too, whatever the variable is named.
  Observed by AC1.
- **S3** — The plants. The `--readers` fixture of unit 38's arm gains five planted lines: three it must
  list (`i.split("-")[1]`, `spec_id.split('-')[1][0]` and `fam, slug, seq = x.split("-")`) and two it
  must not (`x.split("-")[0]` and `x.rsplit("-", 1)[1]`), so the shape can fail both ways. Observed by
  AC1.

## 3. Non-goals (OUT)

- Re-pointing any reader. The ten of unit 38's §1 are unit 38's, and the further id readers the shape
  finds are `TOOL-dTotalRecall-45`'s, `tools/policy/check_policy.py#derive_run_kind` among them (§8 F2).
  Unit 45's rev-2 §1 names three; the fourth is that unit's to take at its own re-ground, and this
  unit's AC3 reads unit 45's §1 as it stands at the pass.
- The parser `parse_id_parts`: `TOOL-dTotalRecall-54`'s, landed in step 8 and rebuilt by
  `TOOL-dTotalRecall-46`.
- The kept-hit marker: the batch `TOOL-dTotalRecall-53` makes `--readers` read it (its S16).
- A data-flow test of whether a split value came from an id regex. The shape is what a reader of an
  id does, and a non-id hit is kept by name.

### Edges

- **consumes-from** `TOOL-dTotalRecall-38` — the widened `--readers` split predicate and its fixture,
  whose name condition this unit replaces with the shape
- **hands-off** `TOOL-dTotalRecall-53` — the shape-keyed split census, whose index-0 and kept splits that unit marks and whose flip case it extends (ids 9, 13 and 23)
- **hands-off** `TOOL-dTotalRecall-60` — the split predicate and AC2's thirteen sites, which that unit widens to maxsplit and rsplit shapes and matches by line text (the round-1 audit of units 44 to 53, ids 20 and 39)

## 4. Design

### The predicate

```text
python  \.split\((["'])-\1\)(?!\[0\])        a split with no maxsplit, not indexed [0]
shell   cut -d ?'?-'? | IFS=- | \$\{[A-Za-z_]+(%%?-\*|##?\*-)\}
```

The predicate replaces the name condition inside `scan_readers`, the census function
`TOOL-dTotalRecall-5` mints and unit 38 widens; its population is unit 5's, every tracked `*.py`, `*.sh`
and `*.js` file under `tools/` and `skills/` and every tracked file under `.githooks/`. The JavaScript
half of the census is unit 5's regex-literal arm and is unchanged. Unit 38 S4's flip-probe census check
runs `--readers` over the clone and over the probe's own tree and fails on a clone-only hit, so it
reads this predicate on both sides and stays a differential.

### The reading at base

`git grep -nE "\.r?split\(['\"]-['\"]" 462d20f3 -- tools` printed 27 lines (PINNED, 2026-10-26).
S1's shape, `git grep -nP` with the Python pattern above, listed 16 of them at that base (PINNED,
2026-11-22). Unit 60 S17 reads the line text `git show 462d20f3:<file>` prints at each base site this
spec and unit 45 cite.

### The reading at HEAD

The same broad command over unit 5's population printed 35 lines at `c2143acf3` (DERIVED 2026-11-22,
`git grep -nE` with the pattern above over the seven pathspecs of unit 5 §4 "The readers"), and the
same 35 at `8b8b1374` (DERIVED). S1's shape lists 17 of them (DERIVED, the `git grep -nP` above over
the same pathspecs, at both commits). The other 18 are a `[0]`, a maxsplit or an `rsplit` sequence
read, for example `tools/memory-tree/gen_build_index.py#cmd_asks` and
`tools/memory-tree/backlog.py#render_family_view`, which take the family at index 0.

| Hit | Disposition |
|---|---|
| the ten readers of unit 38's §1, `derive_probe_labels` and `cmd_new_build` among them | re-pointed by `TOOL-dTotalRecall-38` at order 8 |
| `tools/branch-reconcile/branch_reconcile.py#derive_names`, `tools/memory-tree/gen_build_index.py#render_spec_skeleton`, `tools/memory-tree/row_grammar.py#scan_records` | `TOOL-dTotalRecall-45` rev-2 §1 |
| `tools/policy/check_policy.py#derive_run_kind` (`a.split("-")[1] == build`, an ask id of a build's `BACKLOG.md`) | an id reader landed since base by `TOOL-dLandedOwners-1`; handed to unit 45 (§8 F2) |
| `tools/govkit/selftest.py#check_retired_flags`, `tools/memory-tree/row_grammar.py#cmd_ages`, `tools/run-gates/measure_legs.py#read_turnstile` | kept: a retired flag's name, a date and a queue ticket's file name |

S2's shell shapes list 21 lines at `c2143acf3` (DERIVED 2026-11-22, `git grep -nE` with the shell
pattern above over the same pathspecs). Each reads the head segment, the segment after the last
hyphen, or the text between the first and the last hyphen, or splits no unit id. Among them are unit
38 §4's fourteen name-keyed shell lines, `tools/unattended/unattended.sh#derive_ask_seq`'s sequence and a
comment in `tools/memory-tree/check-memory-hygiene.sh`. No shell hit needs a re-point. The pass
re-runs both predicates before its first edit, and its `Decided:` trailer records those counts and
each kept hit, not these.

### Inventory

Minted: none. The predicate is a pattern inside unit 5's `scan_readers`, and the plants join the
fixture of unit 38's arm.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/memory-recall/selftest.py` (the arm of §7)

`TOOL-dTotalRecall-46` also writes `id_grammar.py` at order 9, so BUILD-METHOD M6 sequences the two
passes.

### Alternatives rejected

- **Add `i` to the name list.** The next reader named `x`, `a` or `rid` escapes the same way, as
  `derive_run_kind`'s `a` does at HEAD.
- **Trace each split's receiver back to an id regex.** It needs a data-flow pass the census does not
  have, and the shape already separates the readers that break from those that do not.

## 5. Production-readiness checklist

- security — no new surface: a read-only census.
- perf / scale — one regex per line over the tool root, as today.
- error / empty / loading states — an empty census prints its count, `0 split reader(s)`.
- observability — each hit prints its path, line and shape.
- risks — a non-id split of the same shape is listed; it is kept by name, so a false hit costs one
  line of record and never a silent pass.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no page covers the census.

## 6. Acceptance criteria

- **AC1** — When `python id_grammar.py --readers <root>` runs over the fixture holding S3's five
  plants, it lists the three positive plants and neither negative one.
  Red when: the predicate still reads the value's name, so `i.split("-")[1]` is not listed, or it lists
  a `[0]` read.
  fixture: a throwaway git tree under the run's scratch directory holding a copy of every memory-tree
  `*.py` and unit 38's split plants beside S3's; the pass makes it.
- **AC2** — When the tip's `id_grammar.py --readers <worktree>` runs over a scratch worktree checked
  out at the parent of `TOOL-dTotalRecall-38`'s pass commit, it lists the thirteen sites: each reader of
  that unit's §1, `derive_probe_labels` and `cmd_new_build` among them, and the three of §4's
  `TOOL-dTotalRecall-45` row. It also lists `derive_run_kind`'s split.
  Red when: any of those fourteen lines is not listed.
  fixture: the scratch worktree under the run's scratch directory; the pass makes it.
- **AC3** — When `python id_grammar.py --readers` runs at the pass tip, every split hit it lists is
  either kept in a pass commit's `Decided:` trailer or a reader `TOOL-dTotalRecall-45`'s §1 re-points.
  Red when: an unkept id reader is listed that no unit re-points.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `build-index selftest` · `memory-recall kit selftest` · `drift-audit selftest` · `playbook render selftest` · `policy fixtures`

New arm: tools/memory-recall/selftest.py · covers AC1 · the five shape plants beside unit 38's `py-split`, `sh-cut` and `sh-expansion`, in `make_repo`'s throwaway tree, staged by restoring the value-name condition · none

The four legs after `build-index selftest` each name `tools/memory-tree/id_grammar.py` in their
`guard` (`tools/gate-legs.json`), and `memory-recall kit selftest` runs the arm: `id_grammar.py` has no
self-test mode and no leg runs it, as `TOOL-dTotalRecall-54` §8 F2 found.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Who re-points `derive_run_kind`, the id reader the shape finds that no unit names?** It landed
  after base (`TOOL-dLandedOwners-1`), splits an ask id named `a`, and under the hyphenated `in-slug`
  flip compares `d2026` against the build slug. Options: (a) this unit re-points it; (b)
  `TOOL-dTotalRecall-45`, whose §1 holds the id readers outside unit 38's table, takes it at its
  re-ground, and AC3 reads that unit's §1 rather than a count of three; (c) the pass keeps it in its
  `Decided:` trailer. (a) breaks §3's non-goal on re-pointing (veto 1). (c) keeps an id reader that
  answers wrong, which §5 admits only for a non-id split, and leaves the defect live. RESOLVED (agent,
  2026-11-22, delegated): (b), the most feature-rich survivor; one follow-up, unit 45's §1 gaining the
  reader. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 1
  (HIGH, item H1 shared with id 35).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-11-22 · §1 · S3 · §3 · §4 · AC1 to AC3 · §7 · §8 · re-grounded per
  `2026-11-22-prompt-TOOL-dTotalRecall-44-reground-brief`: readers cited by symbol, base lines
  blob-pinned at `462d20f3`; §1 states unit 38 rev-4's narrowed AC2; §4 re-derives the census at HEAD
  over unit 5's population (17 Python hits, 21 shell, DERIVED) with each disposition, finding
  `derive_run_kind`, handed to unit 45 (F2), whose split AC2 adds; the arm moves to
  `tools/memory-recall/selftest.py` beside unit 38's plants, Files touched gains it, and §7 names the
  four further legs guarding `id_grammar.py`.

## 10. Reuse audit

The seam extended is `TOOL-dTotalRecall-38` S2's split predicate inside `id_grammar.py --readers`
(`scan_readers`, `TOOL-dTotalRecall-5`'s), its one census; this unit changes its key and adds no
walker. `python tools/codebase-map/reuse_lookup.py "list every hyphen split that reads an id"` ranked
name-stem neighbours (`read_text`, `read_rows`, `read_git`) and no census of split shapes on
2026-11-22, so no existing seam fits beside that predicate.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
