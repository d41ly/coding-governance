# TOOL-dLinkedLibrary-54 — the shipped micro-format gate carries the `region_sh` block inline, so it runs where `<prefix>/lib/` never travels

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 4 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-deviation-541.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-deviation-541.md) | deviation | — |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-1-spec-writer.md) | journal | TOOL-dLinkedLibrary-1 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 3 at HIGH**, report item **H1**. Ids 12 and 17 share the item, and each is its own unit:
id 12 is `TOOL-dLinkedLibrary-55`'s and id 17 is `TOOL-dLinkedLibrary-56`'s.

`TOOL-dLinkedLibrary-43` S3 has `tools/check-microformats.sh` source `tools/lib/region.sh`, on the premise
that it is "a gov-internal tool at the tool root". The premise is false. The govkit entry
`tools/govkit/entries/check-microformats.kit.toml` ships the script as role `engine` to
`{prefix}/{relpath}` (:24-27), and its header states the entry is NOT conditional and sits in the
declared default selection (:6-12). `tools/run-gates/run-gates.test.sh:30-31` states that
`<prefix>/lib/` never travels. Built as 43 writes it, every default adopter's `micro-format definitions`
leg sources a file it never received.

This unit makes the gate carry the factory's `region_sh` block inline, as `TOOL-dLinkedLibrary-18` S6
requires of every shell site, so it reads its definition block with the factory's contract and sources
nothing. It repairs `TOOL-dLinkedLibrary-43` and builds one step after it (order 4).

## 2. Scope (IN)

- **S1** — The inline block. `tools/check-microformats.sh` carries the `region_sh` block of
  `tools/lib/region.sh` (`TOOL-dLinkedLibrary-18` S3) once, byte-identical, between its own `# >>>
  region_sh` and `# <<< region_sh` markers, and reads its definition block with `region "$FILE" "$OPEN"
  "$CLOSE"` where 43's pass wrote a `source` of `tools/lib/region.sh`. No line of the gate names a path
  under `lib/`. Observed by AC1 and AC3.
- **S2** — The parity population. The inline copy is graded by the existing `region_sh` row of
  `PARITY_ROWS`, which `TOOL-dLinkedLibrary-18` S5 adds, through the copy discovery that greps `^#
  >>> <stem>` over tracked shell files (`tools/lib/resolve-python.test.sh:226`); no row is edited. Observed
  by AC2.
- **S3** — The refusals kept. The exactly-one-pair count (`tools/check-microformats.sh:40-46`) still runs
  first and exits 2 as today. Where `region` exits 3 on a pair the count admits, a close above its open,
  the gate exits 2 with one line naming the pair, never grading an empty block. Observed by AC4.
- **S4** — The header. The gate's header says it ships with the charter and carries its region reader
  inline because `<prefix>/lib/` travels to nobody; the "gov-internal" premise is not written anywhere
  in the file. Observed by AC1.

## 3. Non-goals (OUT)

- The standing arm that runs the gate at a lib-less prefix: `TOOL-dLinkedLibrary-55`'s (id 12).
- The run-gates canary's `mempause_sh` slice: `TOOL-dLinkedLibrary-56`'s (id 17).
- The census predicate and its exclusions: `TOOL-dLinkedLibrary-43`'s S1 and S2, unchanged.
- The `region_sh` block's body: `TOOL-dLinkedLibrary-18`'s; this unit copies it.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-18` — `region_sh` in `tools/lib/region.sh`, the block S1 carries inline and S2's row grades (id 3)
- **consumes-from** `TOOL-dLinkedLibrary-43` — S3's re-point of `tools/check-microformats.sh`, whose `source` line S1 replaces with the inline block (id 3)
- **hands-off** `TOOL-dLinkedLibrary-65` — S1's inline `region_sh` block and AC3's staged break, which unit 65 guards and re-stages as the stripped block (id 24 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — AC1, AC3, S3's exit and S4's header, which unit 74 answers AMENDED in this unit's ledger and completes (ids 34, 3, 23, 46 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/govkit/entries/check-microformats.kit.toml:6-12` and :24-27: not conditional, in the default
  selection, `check-microformats.sh` shipped with role `engine` to `{prefix}/{relpath}`.
- `tools/run-gates/run-gates.test.sh:30-31`: "this harness SHIPS with the kit and <prefix>/lib/ never
  travels".
- `tools/lib/resolve-python.test.sh:160-167`: a copy-installed kit "cannot source a shared library and
  must carry the function inline", graded by a `PARITY_ROWS` row.
- `tools/check-microformats.sh:49` reads the block today with its own awk, `$0 == o {f=1; next} $0 == c
  {f=0} f`, the slice `TOOL-dLinkedLibrary-43` re-points.

### The read after S1

```bash
# >>> region_sh
<the block, byte-identical to tools/lib/region.sh's>
# <<< region_sh
block=$(region "$FILE" "$OPEN" "$CLOSE") || {
  echo "check-microformats: the fence pair in $FILE is not one open above one close"; exit 2; }
```

### Rollout

Same order as units 55 and 56, and disjoint from both: this unit writes only `tools/check-microformats.sh`.
Unit 55's arm reads this file at the close, never at either pass.

### Files touched (estimate)

- `tools/check-microformats.sh`: S1, S3, S4

### Alternatives rejected

- **Shipping `tools/lib/region.sh` with the entry.** It adds `lib/` to an adopter install, which the
  charter's Facts line rules out: `tools/lib/` is gov-internal and every copy-installed kit carries its
  contents inline instead.
- **Keeping the gate's own awk slice.** It leaves a region parser outside the factory, the population
  `TOOL-dLinkedLibrary-18` AC8 counts.

## 5. Production-readiness checklist

- security — read-only gate; the inline reader refuses a malformed pair before any line is graded.
- perf / scale — one function call in place of one awk run.
- error / empty / loading states — a reversed pair exits 2 naming it; an absent pair keeps its exit 2.
- observability — each refusal names the file and the pair.
- risks — the inline copy drifts from its canonical; S2's parity row reds it.
- testing — AC1 to AC4 by probe and a scratch install.
- migration — none: an adopter receives the new bytes on update, and the gate reads the same block.
- user docs — none under `help/`: the gate's own header, S4.

## 6. Acceptance criteria

- **AC1** — When `grep -c "lib/" tools/check-microformats.sh` runs at this pass's tip, it prints 0, and
  `grep -c "^# >>> region_sh" tools/check-microformats.sh` prints 1.
  Red when: the gate sources or names a file under `lib/`, or carries no inline block.
- **AC2** — When the `region_sh` block is sliced from the lib canonical `region.sh` (its path in S1)
  and from `tools/check-microformats.sh` with `awk '/^# >>> region_sh/,/^# <<< region_sh/'` and the two
  compared with `diff`, it prints nothing.
  Red when: the inline copy differs from its canonical.
- **AC3** — When `tools/check-microformats.sh` alone is copied into a scratch git repository under
  `%TEMP%/mf54` at the prefix `gov/`, which holds no `lib/`, beside a copy of `AGENTS.md`, and `bash` runs
  that prefix copy of `check-microformats.sh` from the repository's root with `AGENTS.md` as its one
  argument, it exits 0; with the line `. "$(dirname "$0")/lib/region.sh"` inserted after `set -u` in that
  copy, it exits non-zero.
  Red when: the gate needs a file the install does not ship.
- **AC4** — When the same scratch repository's charter has its `<!-- /microformats -->` line moved above
  `<!-- microformats -->`, the same run of the prefix copy over `AGENTS.md` exits 2 naming the pair.
  Red when: a reversed pair grades as an empty block or as a clean set.

## 7. Gates

`micro-format definitions` · `micro-format gate selftest` · `govkit acceptance matrix` · `python resolver (behaviour + inline parity + idiom ban)` · `install-prefix (shipped surface)` · `foreign-prefix parity (every self-test at three prefixes)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the inline copy joins the `region_sh` population that the parity arm of the python
resolver suite, `tools/lib/resolve-python.test.sh`, already grades, and unit 55 adds the lib-less arm.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Inline block, or ship the library with the entry?** Options: (a) the `region_sh` block inline
  under its parity row; (b) `lib/region.sh` added to the entry's `[[files]]`. (b) adds an install
  location the charter rules out (veto 2). RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the one
  survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 3 (HIGH, item
  H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-65, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-18`'s `region_sh` block and the `PARITY_ROWS` copy discovery in
`tools/lib/resolve-python.test.sh:226`, the house mechanism for a shared shell function a copy-installed
kit carries. `python tools/codebase-map/reuse_lookup.py "copy-installed kit carries a shared shell
function inline under a parity row"` ranked `rows`, `row`, `resolve_kit_dir` and `kit_rel`;
`resolve_kit_dir` is the precedent of an inline-carried function and reads no region, so no existing seam
fits beyond the factory block being carried.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
