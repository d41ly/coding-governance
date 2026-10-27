# TOOL-dLinkedLibrary-56 — `region_nth` becomes a parity-gated block, and the run-gates canary carries it inline for its `mempause_sh` slice

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 4 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-56-deviation-561.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-56-deviation-561.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 17 at HIGH**, report item **H1**. Ids 3 and 12 share the item, and each is its own unit:
id 3 is `TOOL-dLinkedLibrary-54`'s and id 12 is `TOOL-dLinkedLibrary-55`'s.

Id 17 is the blast-radius half of the item. `TOOL-dLinkedLibrary-43` S3 re-points the `mempause_sh` slice
of `tools/run-gates/run-gates.test.sh` (:3600) onto `region_nth` sourced from `tools/lib/region.sh`, and
`TOOL-dLinkedLibrary-18` S3 puts `region_nth` outside every parity block, "which only gov-internal suites
source". The canary is not gov-internal on every path: `tools/run-gates/kit.toml:35-41` withholds it from
`govkit apply` as `project-owned`, and states that the copy-install path in `WIRE-INTO-PROJECT.md` is a
plain `cp -r` of the kit dir that does not read the descriptor. On that path the canary sources a file
`<prefix>/lib/` never carries (`tools/run-gates/run-gates.test.sh:30-31`).

This unit wraps `region_nth` in its own block with a parity row, and has the canary carry that block
inline and read the `mempause_sh` block through it. It repairs `TOOL-dLinkedLibrary-43` and builds one
step after it (order 4).

## 2. Scope (IN)

- **S1** — The block. In `tools/lib/region.sh`, `region_nth <open> <close> <k> <file>`
  (`TOOL-dLinkedLibrary-18` S3) sits between `# >>> region_nth` and `# <<< region_nth`, its body
  unchanged, calling no function defined outside the block. Observed by AC1.
- **S2** — The row. `PARITY_ROWS` (`tools/lib/resolve-python.test.sh:168-187`) gains
  `region_nth|$ROOT/$KIT_REL/region.sh|$KIT_REL/region`, so every inline copy is graded against
  the canonical and the row's empty-population arm (:229) holds. Observed by AC2.
- **S3** — The canary. `tools/run-gates/run-gates.test.sh` carries the `region_nth` block once, above
  its first use, and its `mempause_sh` slice reads `_mpb=$( region_nth '# >>> mempause_sh' '# <<<
  mempause_sh' 1 "$KITDIR/run-gates.sh" | tr -d '\r' )` where 43's pass wrote a `source` of
  `tools/lib/region.sh`; no line of the canary sources a file under `lib/`. Observed by AC3.

## 3. Non-goals (OUT)

- The micro-format gate: `TOOL-dLinkedLibrary-54` (id 3) and `TOOL-dLinkedLibrary-55` (id 12).
- The `mempause_sh` block itself and its own parity row (`tools/lib/resolve-python.test.sh:179`): unchanged.
- Any other suite that sources `tools/lib/region.sh`: a gov-internal suite under `tools/lib/` keeps
  sourcing it, as `TOOL-dLinkedLibrary-18` S3 allows.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-18` — `region_nth` in `tools/lib/region.sh`, which S1 wraps in a block and S2 rows (id 17)
- **consumes-from** `TOOL-dLinkedLibrary-43` — S3's re-point of the `mempause_sh` slice in `tools/run-gates/run-gates.test.sh`, whose `source` line S3 replaces with the inline block (id 17)
- **hands-off** `TOOL-dLinkedLibrary-74` — the inline `region_nth` copy and its `mempause_sh` slice, which unit 74 completes (ids 22, 30, 32, 45 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/run-gates/run-gates.sh:564` opens the block with the LABELLED line `# >>> mempause_sh — canonical
  copy: run-gates.sh in this kit's dir (byte-identical; gated)` and :716 closes it, so an exact-match
  `region` call does not find it and a labelled reader does.
- `tools/run-gates/run-gates.test.sh:3600` slices it today with `awk '/^# >>> mempause_sh/,/^# <<<
  mempause_sh/'`, printing the markers with the body; `bash -c` runs the comment lines as nothing.
- `tools/run-gates/kit.toml:35-41`: the canary is `project-owned` for `govkit apply` only, and "the
  copy-install path ... is a plain `cp -r` of the kit dir and does not read this file".
- `tools/lib/resolve-python.test.sh:221-237`: `blk` extracts every `# >>> <stem>` block by ordinal, and a
  row whose copies all vanished reds as an empty population.

### Rollout

Same order as units 54 and 55, and disjoint from both: this unit writes `tools/lib/region.sh`,
`tools/lib/resolve-python.test.sh` and `tools/run-gates/run-gates.test.sh`, and neither sibling reads them.

### Files touched (estimate)

- `tools/lib/region.sh`: S1
- `tools/lib/resolve-python.test.sh`: S2
- `tools/run-gates/run-gates.test.sh`: S3

### Alternatives rejected

- **Recording why a project-owned suite may source `lib/`.** The `cp -r` path copies the canary into an
  adopter with no `lib/`, so the record would describe a suite that cannot start there; the canary's
  own header (:30-31) already states the opposite rule.
- **The awk range kept.** It leaves a region parser outside the factory, the population
  `TOOL-dLinkedLibrary-43` S3 completes.

## 5. Production-readiness checklist

- security — read-only slice; the block refuses a malformed pair as `TOOL-dLinkedLibrary-18` S1 states.
- perf / scale — one function call in place of one awk run.
- error / empty / loading states — an absent `mempause_sh` block makes `region_nth` exit non-zero, and the
  canary's arm reports it rather than running an empty program.
- observability — the parity arm names a drifted copy and its block ordinal.
- risks — a second shell site that needs `region_nth` must carry the block too; S2's row grades it.
- testing — AC1 to AC3 by probe.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the `region_nth` block alone is sliced from the lib's `region.sh` (S1) with `awk
  '/^# >>> region_nth/,/^# <<< region_nth/'` into a scratch file under `%TEMP%/rn56`, sourced by a fresh
  `bash`, and `region_nth '# >>> mempause_sh' '# <<< mempause_sh' 1 tools/run-gates/run-gates.sh` runs, it
  prints the labelled open line first and the close line last.
  Red when: the block calls a function it does not hold, or misses a labelled open.
- **AC2** — When `grep -n "^region_nth|" tools/lib/resolve-python.test.sh` and `git grep -l "^# >>>
  region_nth" -- '*.sh'` run at this pass's tip, the first prints the row and the second lists two
  files: the lib's `region.sh` and the run-gates canary, the file S3 names.
  Red when: the canary's copy has no row grading it, or the population is empty.
- **AC3** — When `grep -c "lib/region" tools/run-gates/run-gates.test.sh` runs, it prints 0; and the
  canary's slice command, run in a fresh `bash` with the canary's inline block sourced, prints the same
  bytes as `awk '/^# >>> mempause_sh/,/^# <<< mempause_sh/' tools/run-gates/run-gates.sh | tr -d '\r'`.
  Red when: the canary sources `lib/`, or its slice reads other bytes than before.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `marker contracts` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC2 · the `region_nth` parity row, the failing case staged by one byte changed in the canary's inline copy · none
New arm: tools/run-gates/run-gates.test.sh · covers AC3 · the moved `mempause_sh` slice of 11g, read through the inline `region_nth` block, the failing case staged by a canary whose block is absent, so the slice reads nothing and AC14's value check reds · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Inline the reader, or record why the canary may source `lib/`?** Options: (a) `region_nth` as a
  parity-gated block the canary carries; (b) a recorded exemption for a project-owned suite. (b) fails
  the canary's own rule at :30-31 on the `cp -r` path (veto 1). RESOLVED (agent, 2026-10-27, delegated):
  (a), rung 3, the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 17 (HIGH, item
  H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-18`'s `region_nth` and the `PARITY_ROWS` table with its `blk`
extractor (`tools/lib/resolve-python.test.sh:168-237`), the house mechanism for a function a shipped
suite carries inline. `python tools/codebase-map/reuse_lookup.py "copy-installed kit carries a shared
shell function inline under a parity row"` ranked `rows`, `row`, `resolve_kit_dir` and `kit_rel`, none a
region reader, so no existing seam fits beyond the factory function being rowed.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
