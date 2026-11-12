# TOOL-aQueuedIndex-2 — the queued-writers plant fails on each mechanism it claims

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-1 · base 27177490e · streams tooling · order 2 · ratified 2026-11-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aQueuedIndex-1-agent-ledger.md](../build/2026-11-12-build-TOOL-aQueuedIndex-1-agent-ledger.md) | journal | TOOL-aQueuedIndex-1 TOOL-aQueuedIndex-3 |
| [2026-11-12-build-TOOL-aQueuedIndex-2-1-builder-return.md](../build/2026-11-12-build-TOOL-aQueuedIndex-2-1-builder-return.md) | journal | — |
| [2026-11-12-build-TOOL-aQueuedIndex-2-ledger.md](../build/2026-11-12-build-TOOL-aQueuedIndex-2-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-2-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-2-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-2-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-2-build-brief.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-2-spec-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-2-spec-brief.md) | research | — |
| [2026-11-12-review-TOOL-aQueuedIndex-2-diff-review-round2.md](../reviews/2026-11-12-review-TOOL-aQueuedIndex-2-diff-review-round2.md) | diff-review | TOOL-aQueuedIndex-1 |

<!-- /gen:spec-records -->

## 1. Goal

The `queued-writers` plant certifies three mechanisms of TOOL-aQueuedIndex-1 and can go red on only
one of them. After this unit it also goes red when the waiter's re-read under the lock is deleted,
or when any write block of the index module stops opening with `BEGIN IMMEDIATE`. It prints
`both writers green` only once every check has passed. This folds items B1, M1 and L1 of the closing
review `2026-11-12-review-TOOL-aQueuedIndex-1-diff-review-round1`.

## 2. Scope (IN)

- **S1** — B1. The plant grades writer two on its `runs` and `skipped` counters as well as its
  `parsed` count, and requires all three at 0. It prints the three. This restates
  TOOL-aQueuedIndex-1's AC2 through this unit's AC1. Observed by AC1.
- **S2** — M1. Before its race, the plant reads the index module it imported and requires every
  `with con:` block in it to open with `con.execute("BEGIN IMMEDIATE")`. One read covers the
  overlay and the collection blocks, and the tree build's as well. Observed by AC2.
- **S3** — L1. The plant prints `both writers green` only once all its checks pass, as its own
  last line. Observed by AC3.
- **S4** — The plant's row in the tag resolver's plant table of `tools/playbook/adopt-playbook.sh`
  requires `both writers green` in place of the old writer-two line. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `tools/playbook/tag_index.py`. The locking that TOOL-aQueuedIndex-1 shipped stays as
  it is. This unit changes only the arm that observes it.
- No edit to the CLOSED spec of TOOL-aQueuedIndex-1. Its AC2 is restated by this unit's AC1.
- No permanent staged-break case in a selftest leg, the review's left-shift for B1. Section 7 F1
  resolved that choice: such a case is its own unit.
- No change to the plant's slow parse, its lock poll or its writer-one thread.
- No help page change. The plant's output is read by the arm and by a maintainer, never by an
  adopter's user, and `help/` names neither the plant nor its lines (grep, 2026-11-12).

## 4. Design

### What the plant cannot see today

The plant's verdict is `print_equal(...) and a > 0 and b == 0`
(`tools/playbook/gov_tag.py@0fd35bfa:826`), where `b` is writer two's `parsed`. The waiter's
re-read is the two lines after the tree build's `BEGIN IMMEDIATE`
(`tools/playbook/tag_index.py@46bfe37d:669-670`). With them deleted, writer two rebuilds the tree
under the lock. `_write_parsed` then finds every blob already recorded at its current version, counts
each under `skipped` (`tools/playbook/tag_index.py@46bfe37d:595`), and returns before it adds to
`parsed` (`tools/playbook/tag_index.py@46bfe37d:609`). So `b` stays 0 either way.

This writer's probe, run on 2026-11-12 (PINNED), wrapped `load_view` to print each view's counters
and ran the plant in-process over the module at `46bfe37d`:

| module | writer two's parsed | runs | skipped | plant exit |
|---|---|---|---|---|
| as at base | 0 | 0 | 0 | 0 |
| re-read deleted | 0 | 0 | 7 | 0 |

With the re-read in place, `build_index` returns before `_write_parsed`. The overlay that follows
finds a clean worktree and so has no blob to count. Both counters stay empty only on that path.

### S1: grade writer two on its counters

After `a, b = one.result(), state["parsed"]` (`tools/playbook/gov_tag.py@0fd35bfa:824`), the plant
sums `state["runs"]` and `state["skipped"]`, which are `collections.Counter`s. It prints one line
in place of the line at `tools/playbook/gov_tag.py@0fd35bfa:825`:

```
writer one parsed <a> blob(s); writer two parsed <b>, ran <runs> and skipped <skipped>
```

Writer two passes when `b`, `runs` and `skipped` are all 0. The review also offered a second
signal: `tree_built`'s timestamp for H, read before and after writer two. The counters are taken
here because they are already in `state` and need no extra query, and the probe above shows they
move under the break.

### S2: every write block opens with the lock

Before the plant's first `run_verb`, at `tools/playbook/gov_tag.py@0fd35bfa:786`, it parses the
text of `ti.__file__` with the standard `ast` module. It collects every `ast.With` whose first
item's context expression unparses to `con`. Of those, it collects the blocks whose first body
statement does not unparse to `con.execute('BEGIN IMMEDIATE')`. It prints:

```
write blocks: <n - bare> of <n> open with BEGIN IMMEDIATE
write block at line <line> does not open with BEGIN IMMEDIATE
```

The second line prints once for each bare block. The check passes when `n` is at least 1 and no
block is bare. Requiring at least one block means a renamed connection or a moved module reds,
rather than passing over an empty population. The plant goes on to its race either way, so one run
shows every check.

This writer ran that predicate on 2026-11-12 (PINNED) over `tools/playbook/tag_index.py@46bfe37d`.
It found 3 blocks and none bare. Over copies with one line deleted, it named one bare block each
time:

| line deleted | its block | `with con:` line named |
|---|---|---|
| 668 | the tree build | 667 |
| 745 | the overlay | 744 |
| 784 | the collection | 783 |

The `with con:` population of `tools/playbook/tag_index.py` is exactly those three blocks. Its
other writes either go to the temp tables `load_view` fills, or run inside the schema reset of
`load_index`, which opens its own `BEGIN IMMEDIATE` with no `with con:`
(`tools/playbook/tag_index.py@46bfe37d:523`). The other modules that open the index,
`tools/playbook/instruction_units.py` and `tools/playbook/edge_grammar.py`, hold no `with con:` and
no index write (grep, 2026-11-12). The two `with con:` blocks in `tools/playbook/gov_tag.py` are
other plants' state set-up, not writers of the index, and the read does not cover them.

One read covers both of M1's blocks, because the defect is one shape. A block that loses its
`BEGIN IMMEDIATE` runs as statements that commit one at a time, under the autocommit connection
`load_index` opens (`tools/playbook/tag_index.py@46bfe37d:519`). The read names the shape directly.
It also covers a block added later, which a per-block crash plant would not.

What this check does not see: a write outside a `with con:` block, a block over a connection under
another name, a write in another module, and whether a block is atomic at run time. That includes a
connection opened again under implicit transaction control. TOOL-aQueuedIndex-1's AC1 and AC3
observe the run-time behaviour.

### S3: the green line last

The plant computes one verdict: the S2 check, `print_equal(read_dump(root), read_cold_dump())`,
`a > 0`, and S1's three zeros. It prints `both writers green` only when the verdict holds, then
returns 0, and returns 1 otherwise. The early returns for `writer one never took the write lock`
and `writer two refused` stay as they are.

### S4: the row

The row at `tools/playbook/adopt-playbook.sh@320df434:344` becomes:

```
queued-writers|0|both writers green|DIFFER
```

The phrase now prints only on a passing run, so it is enough as the must-print field. The
`writer two parsed 0` text it required before is no longer printed in that form.

### What the race still cannot see

If writer two reaches its unlocked read only after writer one commits, it returns there, and its
counters stay empty whether or not the re-read exists. Then S1 passes without exercising the
re-read, as TOOL-aQueuedIndex-1's own design said. Writer two has the 3 s staged parse to pass that
read, and in the probe above it queued. A staged break that reads green must be run again before it
is recorded.

### Inventory

This unit mints no function, constant, type or file. Its new names are locals inside the plant's
branch: `blocks`, `bare`, `runs`, `skipped` and the verdict. The lexicon grades only the surfaces
`function`, `type`, `file` and `constant` (`tools/lexicon/lexicon_conf.py@1754d838:41`), so no new
name has a cell for `--suggest` to grade.

### Files touched (estimate)

`tools/playbook/gov_tag.py`
`tools/playbook/adopt-playbook.sh`

## 5. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant queued-writers` runs, it exits 0
  and prints `writer two parsed 0, ran 0 and skipped 0` beside a non-zero blob count for writer one.
  This restates TOOL-aQueuedIndex-1's AC2, whose CLOSED spec stays as written.
  Red when: a scratch copy of the tree has the waiter's two re-read lines deleted, the lines §4
  pins. Writer two then prints a non-zero skipped count and the plant exits 1.
  cost: about 10 s a run, as TOOL-aQueuedIndex-1's AC1 measured, PINNED 2026-11-12.
  figure: the skipped count under the break was 7 in this writer's probe, PINNED 2026-11-12.
- **AC2** — When `python tools/playbook/gov_tag.py --fixture --plant queued-writers` runs, it prints
  `write blocks: 3 of 3 open with BEGIN IMMEDIATE` and no `does not open with BEGIN IMMEDIATE` line.
  Red when: a scratch copy has the overlay's `BEGIN IMMEDIATE` deleted, and in a second run the
  collection's. Each run prints one `does not open with BEGIN IMMEDIATE` line and exits 1.
  figure: the 3 is DERIVED: the §4 predicate over the index module re-derives it.
- **AC3** — When `python tools/playbook/gov_tag.py --fixture --plant queued-writers` runs over each
  staged break AC1 and AC2 name, its output holds no `both writers green`.
  Red when: the plant prints the phrase before it grades, as it does at base.
- **AC4** — When `grep -c "^queued-writers|0|both writers green|DIFFER$" tools/playbook/adopt-playbook.sh`
  runs, it prints 1.
  Red when: the row still requires the old writer-two line.

## 6. Gates

`playbook render selftest` · `govkit acceptance matrix` · `tags (the resolver's checks)` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 · the `queued-writers` row run over a scratch copy whose index module lacks the waiter's re-read, the overlay's `BEGIN IMMEDIATE` or the collection's, one break at a time · none

The arm runs in the `playbook render selftest` leg. The parse adds milliseconds to the plant's
10 s, inside that leg's 300 s ceiling. What the arm does not check: S2's blind spots in §4, and a
writer two that passes its unlocked read after writer one commits.

## 7. Open questions

- **F1** — Does the deleted re-read become a permanent staged-break case in a selftest leg, the
  review's left-shift for B1?
  - (a) No. The main loop observes the arm red on each break once, at the close, as the build
    method's M8 owes. The brief scopes this unit to the review's three items.
  - (b) Yes. A case loads the index module with the re-read removed, runs the plant through `runpy`
    and requires exit 1, so every bar re-checks that the arm can go red. That adds about 10 s to
    the leg it lands in, and a second mechanism that the review's item B1 does not ask for.
  - Recommendation: (a). If (b) is chosen, it is its own unit with its own spec, under the build
    method's M2.
  - RESOLVED (agent, 2026-11-12, delegated): no — the review's three items only; a permanent
    staged-break case is its own unit. The main loop took the recommendation under the owner's
    prompt and accepted brief, which delegate forks to recommendations.

## 8. Revision log

- rev-1 · 2026-11-12 · initial draft.
