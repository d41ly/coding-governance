# TOOL-aRepatriatedFork-21 — a build README is `builds/<slug>/README.md`, at exactly that depth

**Status:** SPECCED · rev-1 · 2026-09-24 · node a · Tier-1 · base 41d2802b · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-prompt-TOOL-aRepatriatedFork-21-build-brief.md](../prompts/2026-09-24-prompt-TOOL-aRepatriatedFork-21-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`gen_build_index.py`'s slot-contract verb and its survey verb both take every tracked path under
`<MEMORY_ROOT>/builds/` that ends in `/README.md` as a build README, at any depth. The render path
already keys on `builds/<slug>/`. `DEPL-aRepatriatedFork-20` measured the difference at inCMS: 41
folder-shaped legacy records carry a `README.md` two levels down, and each one fails the slot
contract, so its AC3 cannot pass. This unit makes both verbs read the same population the render
reads.

## 2. Scope (IN)

- **S1** — One function, `extract_build_readmes`, keeps exactly the paths shaped
  `<MEMORY_ROOT>/builds/<slug>/README.md`. The slot-contract verb and the survey verb both call it
  in place of their own `endswith("/README.md")` filters. Observed by AC1, AC2.
- **S2** — A `--selftest` arm pins both halves: a nested `README.md` is dropped and a build-level one
  is kept. Observed by AC1.
  **Readers:** by name: `cmd_check_format` and `cmd_survey` in `gen_build_index.py` are the two
  readers of the population, and both now call `extract_build_readmes`. by value:
  `check_contract_registry` grades the list those verbs pass it, so a dropped nested README is
  no longer a row it demands.
- **S3** — memory-tree takes its version bump in every carrier. Observed by AC3.

## 3. Non-goals (OUT)

- Renaming inCMS's 41 records. That is `DEPL-aRepatriatedFork-20`'s migration, which this unit
  makes unnecessary.
- The render path, which already selects by `builds/<slug>/` and is unchanged.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the build-README population its AC3 grades at inCMS.

## 4. Design

### Evidence

`gen_build_index.py:1734` and `:1837` filter `git ls-files -- <m>/builds/` by `endswith("/README.md")`.
`DEPL-aRepatriatedFork-20`'s pass ran gov HEAD's `--check-format` over a migrated inCMS clone:
`--check` was clean over 971 artifacts and `--check-format` failed on the 41 nested READMEs alone.
Gov's own tree holds 128 tracked build READMEs and none nested, measured with `git ls-files`.

### Inventory

`extract_build_readmes(paths, memory_root)` — `py.function`, snake, verb `extract`.

### Rollout

Additive for gov: the population is unchanged on a tree with no nested README, which AC2 observes.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` plus the memory-tree version carriers.

### Alternatives rejected

- A depth check inline at each site. Two copies of one predicate are two answers to one question.

## 5. Production-readiness checklist

- security — none; a read-only filter over tracked paths.
- perf / scale — one pass over the listing both verbs already take.
- error / empty / loading states — an empty listing returns an empty list, as before.
- observability — unchanged output on gov's tree.
- risks — a build whose README sits deeper is dropped from the contract. The render path already
  ignores such a file, so the two now agree.
- testing — the S2 arm.
- migration — none.
- user docs — none; the verb's contract does not change for a conforming tree.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, the new arm passes,
  and it fails when `extract_build_readmes` is replaced by the `endswith("/README.md")` filter.
  Red when: a nested README survives the filter.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --check-format` runs on gov's tree, it
  exits 0 with the same bound and unbound counts as before the change.
  Red when: the filter drops a real build README.
- **AC3** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch --base
  f8fdd873` names no kit.
  Red when: a memory-tree carrier was missed.

## 7. Gates

`build-index selftest` · `build README slot contract` · `memory hygiene` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates`

New arm: `tools/memory-tree/gen_build_index.py` · a nested and a build-level README in `--selftest` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-24 · §2 opened as a discovery adopted under the mandate (protocol §11), from
  `DEPL-aRepatriatedFork-20`'s measurement at inCMS.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "select build readmes at one depth"` ranked
`build_reference_index`, `build_index` and `build`, none of which selects build READMEs by depth; the render's `builds/<slug>/` split at `gen_build_index.py:704` is a
set of slugs, not of README paths, so no existing seam fits and one function now serves both verbs.

Recall terms used: `build README population check-format survey nested depth slot contract
gen_build_index`.
