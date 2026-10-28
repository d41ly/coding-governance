# TOOL-dRankedPlan-30 — the declared callers of the session-scoped predicate are kit anchors, resolved at run time

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 7 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-30-deviation-301.md](../build/2026-10-27-build-TOOL-dRankedPlan-30-deviation-301.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-30-deviation-302.md](../build/2026-10-27-build-TOOL-dRankedPlan-30-deviation-302.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md) | research | TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-30-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md) | research | TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) | spec-audit | TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-36 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed
**finding 19 at HIGH**, item **H1**. Finding 9 is the same defect at MEDIUM, item M7, and
`TOOL-dRankedPlan-37` closes it. `TOOL-dRankedPlan-22` S1 has `SESSION_PREDICATE_CALLERS` spell the
repository paths of the loop kit's `ratify.py` and the memory-tree kit's `triage.py` as literals, and its
AC2 pins them "as S1 spells them". `tools/check-install-prefix.sh` is a pure ban with zero tolerance
(:24-28), and its rules 2 and 3 count a literal kit path (:44-47), so the `install-prefix (shipped
surface)` leg reds on the kit. At any other prefix, such as an adopter's `scripts/`, the literal set
matches nothing, and `--check-callers` refuses the kit's own module. This unit stores kit-relative
anchors and derives each caller's path at run time, from the module's own location and the kit
resolver. It repairs `TOOL-dRankedPlan-22`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The anchors. `SESSION_PREDICATE_CALLERS` in `tools/loop/ratify.py` holds `(home, anchor)`
  pairs, never a repository path: `("loop", "ratify.py")` for `derive_plan_exit_ratification` at the
  `plan.exit` move, and `("memory-tree", "triage.py")` for the owner-batches write. Each keeps the
  reason comment `TOOL-dRankedPlan-22` S1 gives it. This supersedes unit 22 S1's two literal paths,
  and unit 22 AC2 is restated as AC1 here. Observed by AC1 and AC3.
- **S2** — The derivation. `derive_predicate_callers(root)` in `ratify.py` returns the set of POSIX
  paths, relative to `root`, of the declared callers in this install. The loop entry is the module's
  own file, `pathlib.Path(__file__)`. Every other entry comes from the loop kit's inline
  `resolve_kit_dir(home, anchor, here)` block, whose canonical copy is `tools/lib/resolve_kit_dir.py`.
  An entry whose kit does not resolve (`LookupError`), or whose file lies outside `root`, yields no
  path, so a file of that name anywhere is refused as an undeclared caller. `check_predicate_callers`
  (`TOOL-dRankedPlan-22` S2) compares callers with this set and with no other. Observed by AC1 and
  AC2.
- **S3** — The plants spelled from the anchors. The `caller-guard` plant (`TOOL-dRankedPlan-22` S3)
  lays out its planted kit files by joining a prefix variable with each anchor pair, never a literal
  kit path. A new plant, `caller-guard-prefix`, lays the loop kit and the memory-tree kit's
  `triage.py` out under `scripts/` in its scratch repository and runs `--check-callers` there. The
  kit's own `ratify.py` and the planted `triage.py` caller are admitted, and a planted
  `.githooks/pre-commit` caller is refused. Observed by AC2 and AC3.
- **S4** — The legs. §7 names `install-prefix (shipped surface)` and `foreign-prefix parity (every
  self-test at three prefixes)`, which `TOOL-dRankedPlan-22` §7 left out. NOT OBSERVED by a criterion
  here: both are legs the close's bar runs, and §7 declares them.

## 3. Non-goals (OUT)

- The caller predicate, meaning which statements count as a call: `TOOL-dRankedPlan-32` widens it.
- Where the tree-wide check runs: `TOOL-dRankedPlan-31` moves it onto its own leg.
- The `--offenders` observation the medium face of this defect adds (finding 9):
  `TOOL-dRankedPlan-37`'s.
- A third declared caller. The set is `TOOL-dRankedPlan-22` S1's, and only its spelling changes here.

### Edges

- **consumes-from** `TOOL-dRankedPlan-22` — `SESSION_PREDICATE_CALLERS`, `check_predicate_callers` and the `caller-guard` plant, which S1 to S3 re-spell; without them there is no allowlist to derive
- **hands-off** `TOOL-dRankedPlan-37` — the derived allowlist, over which that unit's item for finding 9 observes `check-install-prefix.sh --offenders` print no key for the loop kit's `ratify.py`
- **hands-off** `TOOL-dRankedPlan-45` — S2's derivation, AC1 and the `caller-guard-prefix` plant, which that unit's items for findings 9, 35 and 4 correct; carry S1's git-normalised paths and S4's order-7 reading of AC1 into this unit's pass (spec audit of units 30 to 37)
- **hands-off** `TOOL-dRankedPlan-61` — S1's render rule, which this unit's function makes owed: carry `memory/map/generated/symbols.json` into this unit's Files touched and `codebase-map coverage + freshness`, `recall floor` and `recall floor arms` onto its leg line, in this unit's pass (spec audit of units 46 to 52, id 22)

## 4. Design

### Evidence

- `tools/check-install-prefix.sh:24-28`: "A PURE BAN ... ONE predicate, ZERO tolerance, and no remedy
  but deriving the path". Its rule 2 counts gov's prefix followed by a kit, and rule 3 counts "a kit
  segment followed by a file ... under ANY literal prefix" (:44-47). Its population is every tracked
  file under the gate's tool root (:34).
- The same file, :55-57: "a path ASSEMBLED FROM TWO VARIABLES ... is exactly how a fixture laid out at
  a foreign prefix names its kits". The plants of S3 take that form.
- `resolve_kit_dir(home, anchor, here)` (`tools/lib/resolve_kit_dir.py`, inlined byte-identically in
  `tools/check-spec-tokens.py:243-279`) resolves a sibling kit through the install receipt first, then
  probes `<here>/<home>` and `<here>/../<home>`, and raises `LookupError` rather than guess.
- `kit_rel` (`tools/memory-tree/tree_lib.py:48-62`) is the kit's precedent for a path "DERIVED and never
  spelled" from `__file__`.
- A `(home, anchor)` tuple outside a `join(` or `Path(` call is not one of the ban's shapes: the inlined
  resolver call `resolve_kit_dir("memory-tree", "design_lib.py", HERE)` passes it at
  `tools/check-spec-tokens.py:425`.

### The derivation

```
derive_predicate_callers(root)
  here = pathlib.Path(__file__).absolute().parent
  for (home, anchor) in SESSION_PREDICATE_CALLERS:
      path = Path(__file__)                      if anchor is this module's own name
             resolve_kit_dir(home, anchor, here) / anchor   otherwise; LookupError -> skip
      keep path.relative_to(root).as_posix()     when the path lies under root
  return the kept set
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_predicate_callers` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest derive_predicate_callers --as py.function` answered OK |
| `caller-guard-prefix` | `ratify.py` fixture plant | none |

### Rollout

Live at landing. At gov's own prefix the derived set equals the two paths unit 22 spelled, so no caller
changes its answer there.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Match callers by basename alone.** A file named `triage.py` in any kit would be admitted, which
  widens the allowlist past the two acts it declares.
- **Read the paths from the install receipt only.** Gov's own tree carries no receipt row for its own
  kits, so the receipt alone answers nothing at gov's prefix; `resolve_kit_dir` reads the receipt first
  and falls back to the probe, which covers both.

## 5. Production-readiness checklist

- security — deny by default holds: an anchor that does not resolve adds no path, so nothing is
  admitted by a failed lookup.
- perf / scale — one `resolve_kit_dir` call per anchor, once per run.
- error / empty / loading states — an unresolved anchor yields no path, so its file reads as an
  undeclared caller and is refused by name.
- observability — the refusal line names the file and line, as unit 22 S2 prints it.
- risks — an adopter that renames the memory-tree kit's directory is found through its receipt row, as
  every inlined resolver finds it.
- testing — the `caller-guard-prefix` plant, red and green, and AC1's probe.
- migration — none.
- user docs — N/A — no user-facing surface; the kit README paragraph of unit 22 S4 names no path.

## 6. Acceptance criteria

- **AC1** — When a probe imports `ratify.py` and calls `derive_predicate_callers` over this
  repository, it returns exactly two paths, and they are the paths `git ls-files` lists for the loop
  kit's `ratify.py` and the memory-tree kit's `triage.py`.
  Red when: the set holds a path git does not track, or misses one of the two.
- **AC2** — When `python ratify.py --fixture --plant caller-guard-prefix` runs, the check in the
  scratch repository admits its own `ratify.py` and the planted `triage.py` under `scripts/`, and
  refuses the planted `.githooks/pre-commit` caller with exit 1, naming that file.
  Red when: at a foreign prefix the kit refuses its own module, or the declared set matches nothing.
- **AC3** — When `grep -cE "tools/(loop|memory-tree)/" ratify.py` runs over the loop kit's module at
  the pass tip, it prints 0.
  Red when: a declared caller or a planted path is spelled as a literal kit path.

## 7. Gates

`install-prefix (shipped surface)` · `foreign-prefix parity (every self-test at three prefixes)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC2 · the `caller-guard-prefix` plant under `--fixture`, staged by an allowlist holding the literal path of the loop kit's `ratify.py` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29, finding 19 (HIGH,
  item H1; finding 9 is its medium face), repairing `TOOL-dRankedPlan-22`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-45`, each the reciprocal of that promoted unit's own edge (spec audit of units 30 to 37, `reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-61`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is the inlined `resolve_kit_dir` block (`tools/lib/resolve_kit_dir.py`, copied in
`tools/check-spec-tokens.py:243`), with `tree_lib.kit_rel` (`tools/memory-tree/tree_lib.py:48`) as the
precedent for deriving a path from `__file__`. `python tools/codebase-map/reuse_lookup.py "derive a kit
file path at run time from the module location"` ranked `resolve_kit_dir` as a SEAM (fan-in 16,
installs 75) and `kit_rel` second, which agree with the source read. No code exists at base 0689e7fa,
where the loop kit is unbuilt. The recall query returned TOOL-aRepatriatedFork-30, which made the
install-prefix gate a pure ban, and this audit's H1 item, and they agree.

Recall terms used: `python tools/memory-recall/query.py "how does a shipped kit name a sibling kit's file without a literal install prefix" --terms "install-prefix pure ban resolve_kit_dir kit_rel foreign prefix literal kit path allowlist anchors derived"`
