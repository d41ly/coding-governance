# TOOL-dLinkedLibrary-95 — the CI census plants a GitLab alias in every node-start position its alias search admits

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 36 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-95-deviation-951.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-95-deviation-951.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 87 to 91
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md`) confirmed
finding **id 23 at HIGH**, report item **H4**. No other id shares the item.

`TOOL-dLinkedLibrary-91` S11 narrows 83 S1's alias search to node-start positions: the start of a value,
or after `[`, `{`, `,` or `- `. Every existing alias plant, in 76, 83, 84 and 91, puts the alias straight
after `key: `, and 91 §5's risks line says existing trees hold "a real alias in each position", which is
false. A build keeping only the post-colon position passes 91 AC11 and every 76, 83 and 84 tree, while
the common form `default:` over `  before_script:` over `    - *setup` grades `importable` with an alias
injecting the script. Before S11 a substring search caught it, so S11 opens the hole.

This unit plants one tree per position S11 admits, with the reason each must read, and widens 91 S6's
flow `<child>` rule so a token inside a flow sequence names the key that holds the sequence. It repairs
`TOOL-dLinkedLibrary-91` and builds one step after it (order 36).

## 2. Scope (IN)

- **S1** — The flow `<child>`. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, 91 S6's flow-style
  `<child>` is the nearest key before the token at the token's own flow depth, or, where that depth holds
  none, at the nearest enclosing depth holding one; it is empty when that key is the block's own. Block
  style is unchanged. Observed by AC2 and AC4.
- **S2** — The block positions, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch
  tree of its own holding a hidden `.setup_cmd: &setup npm publish` and two plain jobs, `test` running
  `npm test` and `lint` running `npm run lint`: one whose `default:` holds `  before_script:` over `    -
  *setup`, the list-item position; and one whose `default:` holds `  before_script:` over `    *setup`
  alone on its line, the value-start position on a continuation line. Observed by AC1.
- **S3** — The flow positions, cases of the same plant, each its own tree with the same hidden key and
  two plain jobs: `default: { before_script: [*setup] }`, the position after `[`; `default: {
  before_script: [echo, *setup] }`, the position after `,`; and `default: { cache: {*setup : x} }`, an
  alias as a flow mapping key, the position after `{`. Observed by AC2.
- **S4** — The staged reds. A scratch copy of `adopt_program.py` whose alias search counts a `*` only
  after `: ` turns every tree of S2 and S3 `importable`; a copy whose flow `<child>` reads the token's own
  depth alone, as 91 S6 is written, gives S3's two sequence trees a reason other than `default:before_script`.
  Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- A bug-class checklist entry that a narrowed match plants one tree per position: the report's
  left-shift, a separate record this unit does not write.
- The glob plants of 91 S11, which 91 AC11 keeps: unchanged.
- Re-wording 91 §5's risks line: 91's own §3 hands-off edge to this unit names the claim as false and
  points here; S2 and S3 are the plants that line said existed.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-91` — S11's node-start alias positions and S6's `<child>` rule, which S2 and S3 plant one position each and S1 widens for a token inside a flow sequence (id 23)

## 4. Design

### Evidence

- Every alias plant in units 76 to 91 follows `key: `: 83 `default: *base`
  (`2026-10-27-spec-TOOL-dLinkedLibrary-83.md`, S4), 84 `variables: *creds`, 76 `<<: *publish`, and 91's
  `before_script: *base`, `image: *img` and `cache: *c`
  (`2026-10-27-spec-TOOL-dLinkedLibrary-91.md:84` and `:92-93`).
- 91 S11 (`2026-10-27-spec-TOOL-dLinkedLibrary-91.md:86-90`) lists the positions; 91 §5
  (`:274-275`) claims a plant in each.
- 91 S6 (`:66-70`) gives the flow `<child>` as the nearest key before the token at the token's own flow
  depth. In `default: { before_script: [*setup] }` the token sits inside `[`, where no key exists, so the
  rule as written names nothing; S1's enclosing-depth step names `before_script`.

### The reasons, by position

| Tree | Position | Reason each plain job reads |
|---|---|---|
| `    - *setup` under `before_script:` | after `- ` | `refused: opaque step alias default:before_script` |
| `    *setup` under `before_script:` | value start | `refused: opaque step alias default:before_script` |
| `[*setup]` | after `[` | `refused: opaque step alias default:before_script` |
| `[echo, *setup]` | after `,` | `refused: opaque step alias default:before_script` |
| `{*setup : x}` under `cache:` | after `{` | `refused: opaque step alias default:cache` |

The two block trees take `<child>` from 91 S6's block rule: the line holds no key, so the nearest key
above at a shallower indentation, `before_script`. 91 AC7's tree, whose token sits at a depth holding
`key`, reads as before under S1.

### Rollout

Order 36, one step after `TOOL-dLinkedLibrary-91`. If the pass adds a function, it re-renders the
generated map with `python tools/codebase-map/gen_map.py --write` where its `--check` exits 1, in the
pass commit.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **Going back to the substring alias search.** It refuses a file for a glob in a plain scalar, the
  defect 91 S11 closes.
- **Expecting `default:` with an empty `<child>` on the sequence trees.** It contradicts the block twins,
  which name `before_script`, so one nesting would read two reasons by style, the defect 91 AC7 guards.

## 5. Production-readiness checklist

- security — closes the import of jobs whose global script arrives by an alias in a list item, on a
  continuation line or inside a flow collection; deny by default.
- perf / scale — five scratch trees more in the plant.
- error / empty / loading states — unchanged from 91 S6 and S11.
- observability — each refusal names `default:` and the key holding the alias.
- risks — 91 §5's claim that existing trees hold every position is false; S2 and S3 are the trees.
- testing — S2 and S3 under `adopt_program.py --fixture`, S4's scratch copies.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: no reason changes.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both plain jobs
  of each of S2's two block trees read `refused: opaque step alias default:before_script`.
  Red when: an alias after `- ` or alone on a continuation line is not counted and the jobs read
  `importable`.
- **AC2** — When the same plant runs, both plain jobs of S3's `[*setup]` and `[echo, *setup]` trees read
  `refused: opaque step alias default:before_script`, and both of its `{*setup : x}` tree read `refused:
  opaque step alias default:cache`.
  Red when: an alias after `[`, `,` or `{` is missed, or a sequence token names no key.
- **AC3** — When the scratch copy of S4 that counts a `*` only after `: ` runs the same plant by `python
  -I`, both plain jobs of every S2 and S3 tree print `importable`.
  Red when: the staged break leaves a tree refused, so its position is not discriminated.
- **AC4** — When the scratch copy of S4 whose flow `<child>` reads the token's own depth alone runs the
  same plant, S3's two sequence trees print a reason other than `refused: opaque step alias
  default:before_script`.
  Red when: the plant cannot tell S1's enclosing-depth step from 91 S6 as written.

## 7. Gates

`codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 · the `ci-census` plant's five alias-position trees, the failing case staged by an alias search that counts a `*` only after `: ` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 87 to 91, id 23 (HIGH, item
  H4), on the skeptic's corrected fix.

## 10. Reuse audit

The seam extended is 83 S1's alias search as 91 S11 narrows it, and 91 S6's `<child>` rule, inside
`TOOL-dLinkedLibrary-8`'s `ci-job` class in `tools/memory-tree/adopt_program.py`, with the `ci-census`
plant of unit 8's `--fixture` mode. `python tools/codebase-map/reuse_lookup.py "find a yaml alias token
at the start of a node"` ranked `resolve_prefix_token`, `derive_run_starts`, `read_attribution_tokens`
and `scan_landing_nodes`, none a YAML reader, so no existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "where may a yaml alias token sit in a gitlab block the census reads" --terms "census gitlab alias node-start position list item flow sequence default before_script plant"`
