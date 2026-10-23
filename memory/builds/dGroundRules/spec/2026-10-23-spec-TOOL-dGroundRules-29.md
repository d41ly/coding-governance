# TOOL-dGroundRules-29 — a receipt-less target is gov's source tree only when it holds the registry, so the census arm never grades a scratch target as gov

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 8 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-29-deviation-17.md](../build/2026-10-23-build-TOOL-dGroundRules-29-deviation-17.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-27 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with finding **id 17 at HIGH**, item **H2**, which no other id shares. This unit is
id 17's promotion, built from the skeptic's corrected fix, because the finder's was judged unsound.
It repairs `TOOL-dGroundRules-22`, which sits at order 7, so it builds at order 8.

`TOOL-dGroundRules-22` S2 answers `source` whenever `.governance/install.json` is absent, and §4
then grades every census row at its `enforcer`, an absent one a finding. Several callers run the
policy check over a bare `git init` target that holds no receipt, so each would read as gov's own
tree and red about twenty rows on a correct build, while the criteria that expect one specific
refusal would pass for the wrong reason. This unit makes `source` require the registry only gov's
tree holds, and gives a target with neither a receipt nor the registry its own answer, under which
every row is announced and none is graded.

## 2. Scope (IN)

- **S1** — Three answers. `derive_census_tree(repo)` in `tools/policy/check_policy.py` answers
  `adopter` with the parsed receipt when `.governance/install.json` exists, as `TOOL-dGroundRules-22`
  S2 states. With no receipt it answers `source` when exactly one `<d>/govkit/registry.toml` exists
  with `<d>` at depth 0 to 2 below the repository's top level, the search `derive_tool_root` makes;
  it answers `unadopted` when there is none; and two or more is a finding naming each candidate.
  Observed by AC1, AC2, AC4.
- **S2** — The `unadopted` grading. `arm_cap_census` announces a `ships = false` row as
  `<name> · enforcer not shipped` and every other row as `<name> · kit <kit> not installed`, and
  reports no finding, the reading `tools/run-gates/check-receipt.py:38-41` gives a tree that adopted
  nothing. Observed by AC1.
- **S3** — The source tool root. On `source`, `{prefix}` in a row's `enforcer` resolves to `<d>`, the
  directory holding the found `govkit/`. Observed by AC2.
- **S4** — The standing case `census-receiptless-target` in `CASES` of `tools/policy/check_policy.py`.
  Its temporary repository holds no receipt and no registry, and the case asserts announce lines
  only; it then copies `{prefix}/govkit/registry.toml` into the repository and asserts each absent
  enforcer is a finding. Observed by AC3.
- **S5** — The written scope. The `arm_cap_census` row of the kit README's "Each arm in an adopter"
  table (`TOOL-dGroundRules-22` S5) states the three answers and the registry rule. Observed by AC5.

## 3. Non-goals (OUT)

- A receipt whose shape is wrong: finding 25, an item of `TOOL-dGroundRules-32`, which adds an
  `invalid` answer beside these three.
- Planting a receipt in each receipt-less caller's target (§8 F1).
- Any change to the census rows, to `ships`, or to how an `adopter` is graded.

### Edges

- **consumes-from** `TOOL-dGroundRules-22` — `derive_census_tree`, the census arm by tree and its README row, which this unit gives a third answer
- **hands-off** `TOOL-dGroundRules-32` — the three answers of `derive_census_tree`, which that unit's receipt-shape item (finding 25) extends with `invalid`
- **hands-off** `TOOL-dGroundRules-34` — `derive_census_tree`'s three answers and `arm_cap_census` under `unadopted`, which that unit observes at the depth window's edge and keeps joining (ids 5, 14, 28, 37, 24 and 33 of the round-1 spec audit of units 26 to 32)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `derive_tool_root` finds a fixture's tool root as the parent of the one directory holding
  `govkit/registry.toml`, searched at depths 0 to 2, and refuses none or more than one
  (`tools/govkit/govkit.py:153-173`).
- `tools/govkit/registry.toml:294-296` exempts `{prefix}/govkit`, so no adopter install holds the
  registry.
- `tools/run-gates/check-receipt.py:38-41`: a tree with no receipt "never adopted anything", and gov's
  own tree holds none.
- The receipt-less callers `TOOL-dGroundRules-22` names none of: `TOOL-dGroundRules-1` AC9 runs
  `--check` over a fresh `git init` target; `TOOL-dGroundRules-21` S4's `adopt-policy.test.sh`, run
  by `adopter-suite`, plants refusals in scratch targets; `TOOL-dGroundRules-25` S27's
  `arms-empty-target` runs `--check` over a target with no policy file and no tracked code. Each
  holds neither a receipt nor the registry, so each answers `unadopted`.

### The census by tree after this unit

| Receipt | Registry under `<d>` | Answer | Rows |
|---|---|---|---|
| present | any | `adopter` | as `TOOL-dGroundRules-22` §4 states |
| absent | exactly one | `source` | graded at `enforcer`, `{prefix}` as `<d>` |
| absent | none | `unadopted` | announced, no finding |
| absent | two or more | finding | naming each candidate |

A `--fixture` case whose temporary repository stands for gov's own tree copies
`{prefix}/govkit/registry.toml` into it, as S4's second half does.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `unadopted` | an answer of `derive_census_tree` | `tools/policy/check_policy.py` |
| `census-receiptless-target` | `CASES` entry | `tools/policy/check_policy.py` |

No function is minted.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/README.md`

### Alternatives rejected

- **Plant a receipt in every receipt-less caller.** It repairs the four callers named today and
  leaves the fifth, and any hand-copied adopter, graded as gov (§8 F1).
- **A flag on `check_policy.py` saying which tree it reads.** A public flag no clause names.

## 5. Production-readiness checklist

- security — N/A: the arm reads two paths the target holds and writes nothing.
- perf / scale — three globs per run when no receipt exists.
- error / empty / loading states — an ambiguous registry is a finding naming the candidates; an
  unadopted tree announces every row, never silence and never a false red.
- observability — each announce line names the row and the kit; the ambiguity finding names paths.
- risks — a scratch copy of gov's tree that drops the registry reads as `unadopted`; S4's second
  half and the copy rule in §4 keep gov-standing fixtures graded.
- testing — `census-receiptless-target` under `--fixture`, with AC1 to AC5.
- migration — none.
- user docs — the kit README's "Each arm in an adopter" row, S5.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py`, `adopt-policy.sh` and `README.md` under the kit, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `bash adopt-policy.sh --scaffold --target <t>` and then `--check --target <t>` run
  over a fresh `git init` target, as `TOOL-dGroundRules-1` AC9 builds one, `--check` exits 0 and
  `arm_cap_census` prints only `not installed` and `not shipped` lines.
  Red when: a receipt-less scratch target is graded as gov's source tree.
- **AC2** — When `python check_policy.py --repo <t>` runs over a `git init` target holding only a
  copy of the registry at `tools/govkit/registry.toml`, `arm_cap_census` prints a finding for each
  census enforcer the target lacks; and over this repository it prints no `not installed` line.
  Red when: gov's own tree, or a fixture standing for it, stops grading its enforcers.
- **AC3** — When `python check_policy.py --fixture census-receiptless-target` runs, it prints no
  `WRONG`; with `derive_census_tree` staged in a scratch copy to answer `source` for every
  receipt-less tree, it prints `WRONG`.
  Red when: the standing case passes while the arm grades a bare target as gov.
- **AC4** — When a receipt-less `git init` target holds `registry.toml` and
  `registry.toml` and `python check_policy.py --repo <t>` runs, `arm_cap_census` prints a
  finding naming both paths.
  Red when: an ambiguous tree is guessed to be gov's at one of the two roots.
- **AC5** — When `grep -n "registry.toml" README.md` runs under the kit, it prints the
  `arm_cap_census` row of the "Each arm in an adopter" table.
  Red when: the written scope still says a missing receipt means gov's own tree.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the case; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture census-receiptless-target`) · covers AC3 · `derive_census_tree` staged to answer `source` for every receipt-less tree · none

## 8. Open questions

- **F1 — How does a receipt-less scratch target stop reading as gov's source tree?** (a) `source`
  requires the registry only gov's tree holds, and a tree with neither answers `unadopted`. (b) Each
  receipt-less caller plants a receipt in its target. (b) changes four other units' fixtures, leaves
  any later receipt-less caller graded as gov, and leaves `TOOL-dGroundRules-1` AC9's bare target
  red, which fails AC1 (veto 1). (a) meets every criterion with one rule at the reader.
  Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 17 (HIGH, item H2) of the round-1 spec
  audit of units 22 to 25, from the skeptic's corrected fix, its three-way rule, with
  `derive_tool_root`, the registry's exemption and the receipt check read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-22`'s `derive_census_tree`, which gains a third answer
rather than a second arm, and the registry search `derive_tool_root`
(`tools/govkit/govkit.py:153-173`) states, restated as three globs because an adopter has no
`govkit.py` to import. `python tools/codebase-map/reuse_lookup.py "locate an installed kit file in an adopter from its install receipt"`
ranked `adopt`, `kit_rel`, `resolve_kit_dir` and `kit_dir`; none tells gov's tree from an unadopted
one, and `resolve_kit_dir` refuses with no receipt and no sibling, which is the case this unit
answers. The recall probe returned this audit's H2, `TOOL-cMendedVintage-6`'s receipt-sync leg,
which skips a tree with no receipt, and `TOOL-dGroundRules-22`'s own reuse audit; all three agree
with source and with this design.

Recall terms used: `python tools/memory-recall/query.py "how does an arm tell gov's source tree from
an adopter with no install receipt" --terms "install receipt install.json source tree adopter census
registry.toml derive_tool_root receipt-less scratch target"`
