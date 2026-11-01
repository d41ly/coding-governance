# TOOL-dTendedCadence-42 — the adopter instructions follow `PRODUCT_GLOBS` to `tools/loop/flow_layer.py`, from a Readers list built over the whole tree

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling+deployer · order 7 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-42-deviation-421.md](../build/2026-11-01-build-TOOL-dTendedCadence-42-deviation-421.md) | deviation | — |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 31 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H7. Unit 18 S4 moves `PRODUCT_GLOBS`, `EVIDENCE_GLOBS` and the `TRACE_*` declarations from
`tools/drift-audit/drift_signals.py` to `tools/loop/flow_layer.py` (spec-18 :102-110). Its Readers
list claims to be found "by git grep for the names at base" (:111-120) but omits two instructions that
tell an adopter to fill `PRODUCT_GLOBS` in `drift_signals.py`: `WIRE-INTO-PROJECT.md:439` and the
`Next:` heredoc of `tools/drift-audit/adopt-drift-audit.sh:261`. An adopter following either fills a
declaration the flow signals no longer read, and the adopter's own `--check` passes because it tests
existence only (`WIRE-INTO-PROJECT.md:439-442`). This unit redirects both and pins the whole-tree
grep as the criterion.

## 2. Scope (IN)

- **S1** — `WIRE-INTO-PROJECT.md`, the drift-audit steps (`:437-442`): step 3 names
  `<prefix>/loop/flow_layer.py` as the home of `PRODUCT_GLOBS`, filled at minimum, and keeps
  `drift_signals.py` for the declarations that stay there (`SHRINK_ONLY`, `HANDKEPT`, `PINS`), with
  the existence-only caveat unchanged. Observed by AC1.
- **S2** — `tools/drift-audit/adopt-drift-audit.sh`, the `Next:` heredoc (`:259-265`): its first step
  names the loop kit's `flow_layer.py` beside `$KIT_REL` for `PRODUCT_GLOBS`, and `$KIT_REL/drift_signals.py`
  for `PINS`, which step 3 already seeds. Observed by AC1 and AC2.
- **S3** — The two remaining readers the finding names spell `EVIDENCE_GLOBS` with no home:
  `tools/memory-tree/.memory-tree.conf.example:461` and `tools/memory-tree/gen_build_index.py:1962`
  each name the declaration in a refusal and no file, so both stay; S3 records that they were read.
  NOT OBSERVED by a criterion beyond AC1's grep, which they do not match.

## 3. Non-goals (OUT)

- The move itself, its other Readers and the loop kit's adopter seeding `flow_layer.py`: unit 18 S4.
- A checklist entry for moved declarations: the report's left-shift gate is a bug-class entry under
  `memory/gotchas/`, outside this build's write set.

### Edges

- **consumes-from** `TOOL-dTendedCadence-18` — the move of `PRODUCT_GLOBS` to `tools/loop/flow_layer.py`, whose two missed readers this unit redirects
- **hands-off** `TOOL-dTendedCadence-59` — AC1's single-line grep, which the minors batch observes per numbered step (review id 52)

## 4. Design

### Evidence

`git grep -n "PRODUCT_GLOBS\|EVIDENCE_GLOBS" -- ':!memory/builds'` at base, outside
`tools/drift-audit/drift_signals.py`, prints the readers unit 18 S4 lists plus
`WIRE-INTO-PROJECT.md:439`, `tools/drift-audit/adopt-drift-audit.sh:261`,
`tools/memory-tree/.memory-tree.conf.example:461` and `tools/memory-tree/gen_build_index.py:1962`.
Only the first two name `drift_signals.py` as the home.

### Inventory

Minted: nothing.

### Files touched (estimate)

- `WIRE-INTO-PROJECT.md`: S1
- `tools/drift-audit/adopt-drift-audit.sh`: S2
- `tools/drift-audit/selftest.py`: AC2's case

### Alternatives rejected

- **Leave the instructions and re-export `PRODUCT_GLOBS` from `drift_signals.py`.** Two homes for one
  declaration, the defect unit 18 S4 moves it to end.

## 5. Production-readiness checklist

- security — N/A — prose and a heredoc.
- perf / scale — N/A.
- error / empty / loading states — N/A — no code path changes.
- observability — N/A.
- risks — an adopter who installed drift-audit without the loop kit reads a step naming a kit they
  lack; unit 18 S4 makes the loop kit the declaration's owner, so the step names it plainly.
- testing — AC1's grep and AC2's heredoc capture.
- migration — N/A — instructions only.
- user docs — `WIRE-INTO-PROJECT.md` is the adopter's page.

## 6. Acceptance criteria

- **AC1** — When `git grep -n "drift_signals.py.*PRODUCT_GLOBS\|PRODUCT_GLOBS.*drift_signals.py" --
  ':!memory/builds'` runs after the build, it prints nothing, and `git grep -n "flow_layer.py" --
  WIRE-INTO-PROJECT.md tools/drift-audit/adopt-drift-audit.sh` prints one line in each.
  Red when: a shipped instruction still names `drift_signals.py` as the home of `PRODUCT_GLOBS`.
- **AC2** — When `bash adopt-drift-audit.sh` runs in a scratch repository, its `Next:` block names
  `flow_layer.py` on its first step.
  Red when: the printed step names `drift_signals.py` for `PRODUCT_GLOBS`.

## 7. Gates

`drift-audit selftest` · `kit/dogfood doc parity` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC2 · the adopter's `Next:` block captured in a scratch repository, staged against the heredoc at base · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 31 (HIGH, item H7) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (unit 59); no scope, design or criterion moved.

## 10. Reuse audit

No code seam is extended: the change is two instructions unit 18 S4's move leaves stale, found by the
whole-tree `git grep` in §4. `python tools/codebase-map/reuse_lookup.py "launch a python hook from a
settings fragment through a bash shim"` and the other set probes are about mechanisms and name no
instruction text, so no existing seam fits; the grep is the tool, and AC1 re-runs it.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
