# TOOL-dGroundRules-39 — the census registry window held at both edges by a standing case, its fixture paths spelled whole

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-39-deviation-27.md](../build/2026-10-23-build-TOOL-dGroundRules-39-deviation-27.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-39-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-39-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 2 at HIGH**, which shares item **H3** with ids 17
(`TOOL-dGroundRules-40`), 21 (`TOOL-dGroundRules-41`) and 25 (`TOOL-dGroundRules-42`). Id 2 is H3
on the registry window: `TOOL-dGroundRules-34` AC11 plants a bare top-level `registry.toml` where
S11 names `vendor/gov/govkit/registry.toml`, so a correct `arm_cap_census` finds one candidate and
AC11 is red; AC12 lists one file twice and plants nothing at depth 3, so it passes without probing
the edge S12 certifies; and AC14 checks S11's paths, not AC11's, so it misses the corruption. This
unit is id 2's promotion. The window's two edges become a standing case in `CASES`, so they are
observed on every run of the leg rather than once by a criterion whose inputs a respelling can
shorten, and the one-off observation of AC11 is restated here with its paths spelled whole. It
repairs `TOOL-dGroundRules-34`, which sits at order 12, so it builds at order 13.

## 2. Scope (IN)

- **S1** — The case. `census-window-edge` in `CASES` of `tools/policy/check_policy.py` plants, in a
  receipt-less temporary repository, `tools/govkit/registry.toml`, a `registry.toml` at depth 3
  under `a/b/c/govkit/`, and a `registry.toml` at the top level. Unplanted, it asserts that
  `derive_census_tree` answers `source` at the `tools/govkit/` candidate alone. Planted, it adds a
  `registry.toml` under `vendor/gov/govkit/`, at depth 2, and asserts the ambiguity finding naming
  exactly the depth-1 and depth-2 candidates. Observed by AC1, AC2, AC3.
- **S2** — AC11 restated whole. A receipt-less repository holding `tools/govkit/registry.toml` and
  the `vendor/gov/govkit/` one makes `arm_cap_census` print one finding naming both paths, the
  observation `TOOL-dGroundRules-34` S11 states. Observed by AC4.
- **S3** — The inputs held distinct. The case's four paths are four distinct paths whose
  `<d>` sits at depths 1, 3 and 2, with the fourth not under any `govkit/` directory, so no
  restatement of them can repeat one path or put the in-window pair outside the window.
  Observed by AC5.

## 3. Non-goals (OUT)

- The window rule itself, `TOOL-dGroundRules-29` S1, which follows `derive_tool_root`'s search
  (`tools/govkit/govkit.py:154-175`). This unit observes it; it does not move it.
- `census-ambiguous-registry` (`TOOL-dGroundRules-34` S13), which keeps its two-candidate plant.
  This case is the window's edges, which that one does not reach.
- The other corrupted criteria of item H3: `TOOL-dGroundRules-40`, `TOOL-dGroundRules-41` and
  `TOOL-dGroundRules-42`.

### Edges

- **consumes-from** `TOOL-dGroundRules-34` — `census-ambiguous-registry` and the census-window scope of S11 and S12, which S1 extends to the window's two edges and S2 observes with its paths whole
- **hands-off** `TOOL-dGroundRules-52` — AC2 and AC3, which that unit observes in a git clone, each requiring the `census-window-edge` `WRONG` (id 26 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read on 2026-10-23 at `b9f7b5c4e`.

- `tools/govkit/govkit.py:168-169` searches `govkit/registry.toml` under the patterns `""`, `*/` and
  `*/*/`, so `<d>` sits at depth 0, 1 or 2 and depth 3 is outside; a `registry.toml` with no
  `govkit/` parent matches none of them.
- `TOOL-dGroundRules-34` AC11 (:479-482) plants `tools/govkit/registry.toml` and a bare
  `registry.toml`; AC12 (:483-487) names `registry.toml` and then "a top-level `registry.toml`";
  AC14 (:492-496) builds its check from S11, not from AC11 (review ids 2 and 25).
- `TOOL-dGroundRules-1` S7 states the `--fixture` contract: each case is red as planted and green
  without the plant.

### The case

```text
census-window-edge:                            # CASES, tools/policy/check_policy.py
    t = receipt-less temporary repository
    write t/tools/govkit/registry.toml, t/a/b/c/govkit/registry.toml, t/registry.toml
    unplanted: derive_census_tree(t) == source at tools/govkit/   else WRONG naming the answer
    plant:     write t/vendor/gov/govkit/registry.toml
    planted:   derive_census_tree(t) is the ambiguity finding naming exactly
               tools/govkit/registry.toml and vendor/gov/govkit/registry.toml   else WRONG
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `census-window-edge` | `CASES` entry | `tools/policy/check_policy.py` |

The lexicon declares no cell for a `CASES` key, so the name is graded by none.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **AC11 and AC12 restated as one-off criteria only.** That is the form a respelling shortened
  twice; a standing case keeps the inputs in code that runs on every leg run.
- **The edges added to `census-ambiguous-registry`.** Its red is the two in-window candidates; a
  depth-3 or top-level file planted there changes nothing it asserts, so it cannot see the edge.

## 5. Production-readiness checklist

- security — N/A: a temporary repository the case owns.
- perf / scale — one more case of four file writes per `--fixture` run.
- error / empty / loading states — an unexpected answer is a `WRONG` naming the answer it got.
- observability — the case's `RED as planted` line and its `WRONG` lines.
- risks — none beyond the case's own repository.
- testing — AC1 to AC5.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: a gov-only leg.

## 6. Acceptance criteria

Every command runs from the repository root. `check_policy.py` names the policy kit's file under the
kit, as `TOOL-dGroundRules-34` §6 does. A fixture repository is a `git init` repository under
`%TEMP%/<short name>`. The literal inputs are spelled whole here, once, and the criteria name them:

```text
TREE_AMBIG  = a receipt-less fixture repository holding tools/govkit/registry.toml and
              vendor/gov/govkit/registry.toml, each a copy of this repository's registry
DEPTH3_LIVE = in a scratch copy, derive_census_tree's search staged to add the pattern */*/*/
TOPLEVEL    = in a scratch copy, derive_census_tree's search staged to count any registry.toml
CASE_PATHS  = python -c probe that imports check_policy from the kit directory and prints the four
              paths census-window-edge writes, one per line
```

- **AC1** — When `python check_policy.py --fixture census-window-edge` runs, it prints
  `RED as planted` and no `WRONG`.
  Red when: either edge of the window moves, or the depth-2 candidate stops counting.
- **AC2** — When `DEPTH3_LIVE` runs and then the AC1 command runs in that copy, it prints `WRONG`.
  Red when: a candidate at depth 3 decides the answer with the leg green.
- **AC3** — When `TOPLEVEL` runs and then the AC1 command runs in that copy, it prints `WRONG`.
  Red when: a top-level `registry.toml` with no `govkit/` parent is counted as a candidate.
- **AC4** — When `python check_policy.py --repo <t>` runs over `TREE_AMBIG`, `arm_cap_census` prints
  exactly one finding, and it names both of that repository's `registry.toml` paths.
  Red when: an ambiguous tree is guessed to be gov's at one of its candidates.
- **AC5** — When `CASE_PATHS` runs, it prints four distinct paths, three of them under a `govkit/`
  directory whose parent has one, three and two segments, and one at the top level.
  Red when: a restated input repeats a path or loses a prefix that places it in or out of the window.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the case;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture census-window-edge`) · covers AC1 AC2 AC3 · the census search staged to reach depth 3, then to count a top-level `registry.toml`, each in a scratch copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 2 (HIGH, item H3) of the round-1 spec
  audit of units 33 and 34, from the skeptic's corrected AC11 and AC12 inputs held in a standing
  case, with `derive_tool_root`'s search read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.

## 10. Reuse audit

The seams extended are `CASES` in `tools/policy/check_policy.py`, the `--fixture` home
`TOOL-dGroundRules-1` S7 builds, and `derive_census_tree` (`TOOL-dGroundRules-29` S1), observed and
not copied; `census-ambiguous-registry` (`TOOL-dGroundRules-34` S13) is the sibling case whose plant
pattern this one follows. `python tools/codebase-map/reuse_lookup.py "install a kit into a scratch target with the deployer and read its receipt"`
ranked `read`, `scratch` and `resolve_kit_dir` among name-stem hits, none of which plants a census
tree; the seams above were found by reading the specs the review cites. The recall probe returned
this audit's H3 and `TOOL-aKeyedAnnotation-9`, the open ask on the spec-tokens paths join that drove
the respelling; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion's path respelled to pass
the spec-tokens paths join" --terms "acceptance criterion path stripped prefix paths join basename
respelled spec-tokens literal fixture"`
