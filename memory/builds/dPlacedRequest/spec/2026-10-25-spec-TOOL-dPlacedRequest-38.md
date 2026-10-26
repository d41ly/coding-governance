# TOOL-dPlacedRequest-38 — the parity leg runs every inline `gov_feed_sh` copy under `set -u` with nothing from its carrier

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-38-deviation-381.md](../build/2026-10-25-build-TOOL-dPlacedRequest-38-deviation-381.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-38-deviation-382.md](../build/2026-10-25-build-TOOL-dPlacedRequest-38-deviation-382.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 24 at HIGH**. It shares item **H1**, "the node-lock factory is not self-contained
in the `gov_feed_sh` block", with findings 2, 13 and 32, which `TOOL-dPlacedRequest-36`,
`TOOL-dPlacedRequest-37` and `TOOL-dPlacedRequest-39` close. The finding's blast radius is that every
check `TOOL-dPlacedRequest-24` writes stays green while the block aborts in a carrier: AC6 only `cmp`s
the copies and AC5 runs the factory inside the driver, which defines every name the bodies read. A
byte-identical copy is still a copy that dies where its host lacks a name. This unit repairs
`TOOL-dPlacedRequest-24` at order 5 with the gate the item names: the parity leg executes every inline
copy of the block in an empty environment under `set -u`, so a block reading a carrier's name reds.

## 2. Scope (IN)

- **S1** — The arm. A new section of `tools/lib/resolve-python.test.sh`, after the `PARITY_ROWS` loop:
  for every file `git grep -l '^# >>> gov_feed_sh'` lists, the canonical included, it cuts that file's
  `gov_feed_sh` block and the canonical `health_log_sh` block, and runs them in
  `env -i PATH="$PATH" bash -c 'set -u; …'` inside a scratch repository: take `gov-feed.lock` fresh,
  release it, break a planted stale `gov-feed.lock`, release that, and call `add_feed_event` once.
  Each call must exit 0 with no `unbound variable` and no `command not found` on stderr, and no lock
  directory may remain. A failing copy prints `<file>: <first stderr line>`. Observed by AC1 and AC2.
- **S2** — The population is never empty. A run that finds no copy reds naming the stem, as the
  parity loop's own non-empty arm does (`resolve-python.test.sh:221`). Observed by AC3.

## 3. Non-goals (OUT)

- No fix to the block: findings 2, 13 and 32 change it, and this arm reads green on the real tree only
  once those three units are built; the close observes it then.
- No check that a carrier holds `health_log_sh` itself: the arm sources the canonical appender, whose
  copies the `health_log_sh` row holds equal, and `TOOL-dPlacedRequest-36` AC3 observes the carriage.
- No arm over other inline blocks: each other row's block is a pure function of its arguments today.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-24` — `write_node_lock`, `remove_node_lock` and the `gov_feed_sh` block's lock, which this arm executes per copy; without the factory the arm has nothing to exercise
- **hands-off** `TOOL-dPlacedRequest-49` — the carrier arm and §5, which that unit's items for findings 10, 18, 27, 29, 35 and 39 commit, time, sequence, scope and fix
- **hands-off** `TOOL-dPlacedRequest-52` — the carrier arm's population and §3's carriage non-goal, which that unit's items for findings 6 and 18 make the one carriage check

## 4. Design

### The arm

```
for f in $(git grep -l '^# >>> gov_feed_sh'):
  blk gov_feed_sh "$f" > feed.cut ; blk health_log_sh health-log.sh > health.cut
  env -i PATH="$PATH" HOME="$HOME" bash -c 'set -u; . health.cut; . feed.cut
      write_node_lock "$c/gov-feed.lock" t1 && remove_node_lock "$c/gov-feed.lock" t1
      plant "$c/gov-feed.lock" with until = EPOCHSECONDS - 1
      write_node_lock "$c/gov-feed.lock" t2 && remove_node_lock "$c/gov-feed.lock" t2
      add_feed_event refs/gov/bar-red <commit>' 2> err
  rc != 0, or err holds "unbound variable" or "command not found", or $c/gov-feed.lock exists
      -> bad "$f: <first line of err>"
```

`blk` is the file's own extractor (`resolve-python.test.sh:213`), so the cut is exactly the one the
byte arm compares.

### What it does not check

It runs each copy on bash's own `set -u`; a name the block reads only on a path the five calls do not
take, such as the guard-cleared branch, escapes it, and the guard-cleared path is observed by
`TOOL-dPlacedRequest-36` AC2 alone. It reads no carrier code outside the block.

### Files touched (estimate)

- `tools/lib/resolve-python.test.sh`: the carrier arm

### Alternatives rejected

- **A static scan for names the block reads and does not define.** It needs a shell parser to tell a
  local from a global; executing the copy under `set -u` asks bash.
- **Run each carrier whole.** `post-merge.sh` needs a bar verdict and `push-main.sh` a remote; the
  block is the unit under test.

## 5. Production-readiness checklist

- security — none: a scratch repository under the suite's temp dir.
- perf / scale — five calls and one `git init` per copy, four copies at most: well under a second.
- error / empty / loading states — an empty population reds (S2).
- observability — a red names the file and bash's first error line.
- risks — the arm is red on the tree until `TOOL-dPlacedRequest-36` and `TOOL-dPlacedRequest-37` land;
  both sit at this order and the close reads it after them.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: a suite arm.

## 6. Acceptance criteria

The fixture is a scratch directory holding hand-written carrier files, each a copy of the canonical
`gov_feed_sh` block with the edit named, and the probe is S1's loop body run over them.

- **AC1** — When the probe runs over a scratch carrier whose `write_node_lock` carries the verbatim
  claim-push body (`tools/unattended/unattended.sh:2331-2354`), it prints that file and
  `REMOTE_BOUND: unbound variable`, and exits 1.
  Red when: a copy that aborts under `set -u` passes, the staged case being this very plant.
- **AC2** — When the probe runs over a scratch carrier whose block reads only its own names, it prints
  nothing, exits 0, and no `gov-feed.lock` remains in the scratch common dir.
  Red when: the arm reds a self-contained copy.
- **AC3** — When the probe's file list is empty, it prints `no inline copy of 'gov_feed_sh'` and exits 1.
  Red when: an empty population reads as a pass.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 · every inline `gov_feed_sh` copy run under `set -u` in an empty environment, staged by a scratch copy holding the verbatim claim-push body · none

## 8. Open questions

- **F1 — Which gate observes a copy that aborts in its carrier?** (a) An executing arm in the parity
  leg, per copy; (b) a static scan of free names; (c) per-carrier criteria in each unit. (b) cannot
  tell a local from a global without a parser; (c) leaves the next carrier ungraded. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the item's gate. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  24 (HIGH, item H1, shared with findings 2, 13 and 32).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `tools/lib/resolve-python.test.sh`: its `PARITY_ROWS` loop and `blk` extractor
(`:168-233`) already find every inline copy by `git grep` and cut it, and this arm executes the cut it
compares. `python tools/codebase-map/reuse_lookup.py "source every inline copy of a shared block under
set -u and exercise it"` ranked `resolve_pattern_sets`, `scan_shared_index_overlaps` and
`render_charter_blocks`, name stems only, none executing a block. `python
tools/memory-recall/query.py "how is every inline copy of a shared block graded"` returned
TOOL-aLevelledCopy-5, TOOL-aRepatriatedFork-47's audit naming the same table, and
TOOL-aDrainedSluice-6; none disagrees with source.

Recall terms used: parity row inline copy byte-identical resolve-python.test.sh set -u unbound variable gov_feed_sh carrier
