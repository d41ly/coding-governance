# TOOL-dRetiredFork-18 — the gap lines use the wrap helper written for them

**Status:** INPROGRESS · rev-1 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 0

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 |

<!-- /gen:spec-records -->

## 1. Goal

`_render_wrapped_ids` at `tools/memory-tree/gen_build_index.py:822` exists for exactly this, and its
docstring says so: "Hit for real by a thirteen-unit build: the `spec-audit` gap line reached 399
characters against a 350 ceiling and the build could not be committed." It carries selftest arms at
`:1836-1842`. The two emission sites it was written for, at `:773` and `:777`, do not call it. So the
remedy was built, proven and never wired, and a 24-unit build reproduces the original defect at 509
and 531 characters.

## 2. Scope (IN)

- **S1** — Route both gap lines at `:773` and `:777` through `_render_wrapped_ids`.
- **S2** — Keep the `none — …` branch of each line UNWRAPPED and byte-identical. The helper appends
  its own terminator and would render `Ids no record names.` for an empty list, which is a different
  sentence; the empty case is also the common case and must not change.
- **S3** — A selftest arm asserting the EMISSION wraps, not just that the helper can. The existing
  arms grade the helper in isolation, which is why a helper that nothing called still passed them.
- **S4** — Observe the RED first: render `memory/builds/dRetiredFork/README.md` before the change and
  confirm check 7 reports 509 and 531, then after and confirm it reports nothing.

## 3. Non-goals (OUT)

- Raising `BUILD_README_ENTRY_CAP_CHARS`. The helper's own docstring forbids it: "The remedy must
  never be raising that ceiling, because this population grows with every unit a build carries, so a
  raise buys one build and reds the next."
- Exempting generated regions from check 7. It is the wider fix and it would stop grading lines that
  no rule says are exempt; the narrow fix is that these two lines were always meant to wrap.
- `TOOL-dUnstalledConvoy-13` and `DEPL-dCarriedReceipt-16`, the generated record-BINDINGS row. A
  table cell cannot wrap the way a paragraph does, which is why `_render_id_ranges` exists beside
  this helper. Different line, different grammar, both stay open.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/gen_build_index.py --write` renders a build with 24
  units, no emitted line exceeds `BUILD_README_ENTRY_CAP_CHARS`; before the change
  `memory/builds/dRetiredFork/README.md` carried lines of 509 and 531 characters.
- **AC2** — When a build's gap set is empty, both lines render byte-identically to their pre-change
  output, verified by `git diff` over every other build README showing no change.
- **AC3** — When the arm in S3 is run against the pre-change emission, it FAILS; `python3
  tools/memory-tree/gen_build_index.py --selftest` passes after the change.
- **AC4** — `bash tools/memory-tree/check-memory-hygiene.sh` exits `0`, with check 7 and check 9
  both clean.

## 7. Gates

`memory hygiene` · `build README slot contract` · `build-index selftest` · `kit version markers` ·
`verdict epoch (kit version dates the engine)`.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. The helper, its docstring and its unwired call sites were read
  at b0108f13 rather than recalled.
