# TOOL-dTotalRecall-118 — the memory re-measure counts a search of the whole root, and its suite runs its plants again

**Status:** CLOSED · rev-1 · 2026-11-25 · node d · Tier-2 · base acbb74bb · streams tooling · order 46

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-118-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-118-1-acceptance-ledger.md) | log | — |
| [2026-11-25-build-TOOL-dTotalRecall-118-1-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-118-1-builder-return.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-118-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-118-build-brief.md) | journal | — |
| [2026-11-25-review-TOOL-dTotalRecall-115-closing-diff-review-round2.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-115-closing-diff-review-round2.md) | diff-review | TOOL-dTotalRecall-115 TOOL-dTotalRecall-116 TOOL-dTotalRecall-117 TOOL-dTotalRecall-119 TOOL-dTotalRecall-120 TOOL-dTotalRecall-121 TOOL-dTotalRecall-21 |

<!-- /gen:spec-records -->

## 1. Goal

H4 of the closing review (finding 9): a search of the whole memory root is the widest memory read and counts zero
bytes, so the acceptance median is understated. Its plants cannot guard it either: the reconcile `ffa0dcf2d` dropped
every memory arm of `tools/runlog/selftest.py`. This unit counts the root and restores the arms.

## 2. Scope (IN)

- **S1** — `tools/runlog/memory_measure.py#check_memory_word` counts a word that resolves to the root itself, in both
  absolute branches: the main worktree's root and a linked worktree's (§4). Its docstring says so. Observed by AC1.
- **S2** — Five plants of `FIXTURE_PLANTS`, `root-grep`, `root-shell`, `root-absolute`, `root-worktree` and `root-sibling`
  (§4), and their `FIXTURE_CASES` names. Observed by AC2.
- **S3** — `tools/runlog/selftest.py` regains the block of `run_memory_plant`, `read_memory_rows`, `read_memory_cell`,
  `MEMORY_COLUMNS` and the nine `test_memory_` arms (DERIVED, `ffa0dcf2d^1`) that the merge lost, byte for byte from
  `ffa0dcf2d^1`, in the place they held. Observed by AC3.
- **S4** — A tenth arm, `test_memory_dtr118_root`, over S2's plants, and `ASSERTION_FLOOR` raised with its comment line
  in the form `parse_floor_raise` reads (§4). Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- A search of a directory above the root, the repository's top among them: the report scopes the root, and such a read
  is of more than memory.
- A `Grep` with no `path`, which searches the working directory.
- Any other file the reconcile touched: a scan of its Python, shell and JavaScript definitions found no other dropped
  arm (DERIVED 2026-11-25, the two parents against `ffa0dcf2d`, over `tools/`).

### Edges

- **consumes-from** external — the closing review's report and the landed units whose code it read
- **consumes-from** `TOOL-dTotalRecall-115` — its bytes of the symbol map, edited after it
- **consumes-from** `TOOL-dTotalRecall-116` — its bytes of the symbol map, edited after it
- **consumes-from** `TOOL-dTotalRecall-117` — its bytes of the symbol map, edited after it
- **hands-off** `TOOL-dTotalRecall-119` — this unit's bytes of the symbol map
- **hands-off** `TOOL-dTotalRecall-120` — this unit's bytes of the symbol map
- **hands-off** `TOOL-dTotalRecall-121` — this unit's bytes of the symbol map
- **hands-off** external — the close's next bar, the held suites and the landing, each the main loop's

## 4. Design

Read at `acbb74bb` on 2026-11-25. The report holds: with a recorded working directory, `derive_read_channel` gave None
for a Grep of path `memory`, for `rg x memory/`, for the absolute root and for `rg x memory` in a linked worktree, and
`shell` for `rg x memory/` with no working directory (DERIVED 2026-11-25, those calls).

**The report names "runlog-selftest plants" as the gate, and at HEAD the suite runs none.** `git grep` finds
`read-memory` outside `memory_measure.py` in one comment of the suite, `ffa0dcf2d^1` carries the nine arms, and the
floor's comment and value for them stayed, so the suite is under its own floor today.

### The word

```python
main = mdl.derive_path_key(str(main_worktree))
home = f"{main}/{root}"
if folded == home or folded.startswith(home + "/"):
    return True
...
return bool(name) and (rest == root or rest.startswith(root + "/"))
```

`posixpath.normpath` has already cut a trailing slash and a trailing `.` segment, so `memory/` and `.` from inside the
root compare equal too. `memories` and `memory-notes` compare unequal.

### The plants

| Plant | Call | Working directory | Counts |
|---|---|---|---|
| `root-grep` | Grep, path `memory` | `FIXTURE_MAIN` | 400 on read (PINNED, the plant's result) |
| `root-shell` | `rg x memory/` | `FIXTURE_MAIN` | 350 on shell (PINNED, the plant's result) |
| `root-absolute` | Grep, path the absolute root | none | 300 on read (PINNED, the plant's result) |
| `root-worktree` | `rg x memory` | a `.claude/worktrees/side` of `FIXTURE_MAIN` | 250 on shell (PINNED, the plant's result) |
| `root-sibling` | Grep, path `memories` | `FIXTURE_MAIN` | 0 on read (PINNED, the plant's rule) |

On today's code the first four count zero.

### The floor

The new arm makes two checks per plant, and the suite's decoy adds three per arm (DERIVED, `selftest.py`'s loop over its
tests), so the newest raise line reads `# RAISED 1711 -> 1724 by TOOL-dTotalRecall-118: …` (DERIVED, that sum) and its
block closes on `# 10 + 3 = 13` (DERIVED, the two figures above). The restored arms are what the 1711 already counts.

### Inventory

Minted: `test_memory_dtr118_root` (python-function, the suite's `test_` prefix); five plant names.

### Files touched (estimate)

- `tools/runlog/memory_measure.py`
- `tools/runlog/selftest.py`
- `memory/map/generated/`
- `memory/builds/dTotalRecall/build/` (this unit's ledger)

### Alternatives rejected

- **A trailing slash added to both sides before the compare.** It moves every caller's spelling; an equality is one
  clause.
- **The arms rewritten over the plants.** The merge dropped reviewed arms whole, and their bytes are in the history.

## 5. Production-readiness checklist

- security — N/A, a local read measure.
- perf / scale — one string compare per word.
- error / empty / loading states — unchanged.
- observability — the report's columns stand.
- risks — a plant counts what the rule counts, so a wider rule moves the recorded median of past windows; it is measured
  at the report's run and stored nowhere.
- testing — AC1 to AC4 by the pass; §7's arms by the main loop.
- migration — none.
- user docs — N/A, the re-measure's page states channels, not spellings.

## 6. Acceptance criteria

- **AC1** — When a probe calls `memory_measure.derive_read_channel` for the five calls of §4, it answers `read`, `shell`,
  `read`, `shell` and None in order, and None for `C:/fx/other-tree/memory`.
  Red when: either equality is cut. Today the first four answer None.
- **AC2** — When `python tools/runlog/runlog.py memory --fixture --plant <case>` runs for each plant of §4, the pooled row
  carries the figure of its table, and for `root-sibling` zero.
  Red when: a plant is declared and reads no root, or the sibling counts.
- **AC3** — When `grep -c '^def test_memory_' tools/runlog/selftest.py` runs, it prints 10 (DERIVED, S3 and S4), and the
  restored block, cut by its first and last definition, equals `ffa0dcf2d^1`'s byte for byte.
  Red when: an arm is left out or re-typed.
- **AC4** — When `grep -nE '^ASSERTION_FLOOR|RAISED 1711' tools/runlog/selftest.py` runs, it prints the raise line and a
  floor equal to the raise's upper figure (DERIVED, §4), and a probe importing the suite's `test_memory_dtr118_root`
  alone, its `check` calls collected, reports no failure.
  Red when: the figures disagree, or an arm fails over the corrected measure.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `runlog selftest` · `recall floor` · `recall floor arms`

New arm: tools/runlog/selftest.py · covers AC2 AC3 AC4 · `test_memory_dtr118_root` over the five plants, red on today's `check_memory_word`, beside the nine restored arms · `ASSERTION_FLOOR`

## 8. Open questions

- **F1 — Which binding line does a unit the closing review added carry?** The carries join reds a chain spec carrying
  nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the ruling that a chain run
  carries the units it adds, as `TOOL-dTotalRecall-114` §8 F1; (b) a part of another unit's clause, which the parts join
  reds. RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none
- **F2 — Does this unit restore the dropped arms?** Options: (a) yes, S3; (b) the new plants alone, run by nothing, or
  an ask. The left-shift gate the report names needs the arms, and (b) leaves the suite under its floor.
  RESOLVED (agent, 2026-11-25, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the closing review's H4, and the dropped arms found reading it.

## 10. Reuse audit

The seams, each read at `acbb74bb`: `memory_measure.py#check_memory_word` and its plant table; `model.py`'s
`derive_path_key`, the one fold; the suite's arms at `ffa0dcf2d^1` and `selftest.py#parse_floor_raise`.
`python tools/codebase-map/reuse_lookup.py "whether a path word lies under the memory root"` ranked root resolvers, none a
containment test: no existing seam fits beyond these. The task's build-folder walks and
`id_grammar.py#read_kept_reason` read no transcript.

Recall terms used: `python tools/memory-recall/query.py "memory re-measure counts which path words" --terms "memory_measure check_memory_word cwd worktree root grep runlog selftest"`
