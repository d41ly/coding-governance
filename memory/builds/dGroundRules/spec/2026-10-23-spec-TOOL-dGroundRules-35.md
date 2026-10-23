# TOOL-dGroundRules-35 — the guard trace records a bytecode-cache read as its source file, so a warm load still records `govkit.py`

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-35-deviation-23.md](../build/2026-10-23-build-TOOL-dGroundRules-35-deviation-23.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 22 at HIGH**, which shares item **H1** with id 1
(`TOOL-dGroundRules-37`) and id 7 (`TOOL-dGroundRules-36`). Id 22 is H1 seen from the failure
envelope: when `tools/govkit/__pycache__` holds a cache, the in-process `importlib` load opens only
the `.pyc`, so the trace never records `tools/govkit/govkit.py`, the read the `policy fixtures` guard
exists to hold, and keeps an interpreter-tagged path that git ignores and no guard can hold. This
unit is id 22's promotion: `add_source_read` records a bytecode-cache read as the source file it
was compiled from. It repairs `TOOL-dGroundRules-33`, which sits at order 11, so it builds at
order 12.

## 2. Scope (IN)

- **S1** — The mapping. In `add_source_read` (`TOOL-dGroundRules-33` S2), ahead of its top-level
  test, a path whose parent directory is named `__pycache__` and whose name ends in `.pyc`, or in
  `.pyc` followed by a dot and digits (the importlib atomic-write temporary), first has that digit
  tail cut and then becomes `importlib.util.source_from_cache(path)`. A cache path that
  `source_from_cache` refuses with `ValueError` is kept as spelled, so the trace names it rather than
  hiding it. Observed by AC1, AC2, AC3.
- **S2** — Cold and warm. For `budgets-ships-join`, the trace records `tools/govkit/govkit.py`
  whether or not a cache of it exists, and keeps no path ending in `.pyc` either way.
  Observed by AC1, AC2, AC3.

## 3. Non-goals (OUT)

- Any other path git ignores: `TOOL-dGroundRules-36`. A guard line naming no tracked file:
  `TOOL-dGroundRules-37`. The source's git directory: `TOOL-dGroundRules-38`.
- The `os.open` mode-None reading (finding 20, `TOOL-dGroundRules-43`). The cold load's temporary
  write arrives with mode None, which `TOOL-dGroundRules-33`'s pseudocode reads as a read; S1 maps it
  to `govkit.py`, which the guard already holds, so this unit is green without that item.
- Turning bytecode writing off for the `--fixture` run. A cache another run wrote is still opened
  first (§4 Evidence), so it does not close the warm case.
- A new line label or a printed list of kept paths. The criteria observe the mapping through the
  `guard-trace` lines `TOOL-dGroundRules-33` already prints.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `add_source_read`, the trace's one recorder, which S1 extends ahead of its top-level test; without it there is no kept set to map into
- **hands-off** `TOOL-dGroundRules-52` — the cache mapping, observed directly, its digit-tail cut, taken out once unit 43's filter is built, its `str(path)`, and a refused cache name's own line (ids 4, 16, 34, 35 and 38 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `b9f7b5c4e`, on Python 3.14.6 on this node.

- A scratch probe installed an audit hook recording `open` events and loaded a module with
  `importlib.util.spec_from_file_location` and `exec_module`. With no cache present it recorded
  `kit\__pycache__\m.cpython-314.pyc` with mode `'r'`, then `kit\m.py` with mode `'r'`, then
  `kit\__pycache__\m.cpython-314.pyc.2080703160112` with mode `None`. Run again with the cache
  present, it recorded the `.pyc` alone and never opened `m.py`.
- `importlib.util.source_from_cache` mapped `tools/govkit/__pycache__/govkit.cpython-314.pyc`,
  the same name tagged `cpython-312`, and the `.opt-1` form each to `tools/govkit\govkit.py`, and
  raised `ValueError` for `tools/govkit/govkit.py`.
- `git check-ignore -v` printed `.gitignore:1:__pycache__/` for a path under `tools/govkit/__pycache__/`.
- `TOOL-dGroundRules-23` S1 loads `govkit.py` in process through `importlib`, and the
  `policy fixtures` guard holds `{prefix}/govkit/govkit.py` as an exact path
  (`TOOL-dGroundRules-24` §4, review id 22).

### The mapping

```text
add_source_read(event, args):                  # TOOL-dGroundRules-33 S2, this unit's lines marked +
    (unit 33's event and mode tests)
+   p = str(path)
+   if parent name of p == "__pycache__" and p matches r"\.pyc(\.\d+)?$":
+       p = re.sub(r"(\.pyc)\.\d+$", r"\1", p)
+       try: p = importlib.util.source_from_cache(p)
+       except ValueError: pass                  # kept as spelled; the trace then names it
    (unit 33's resolve, top-level and temporary-directory tests on p)
```

### Inventory

No identifier is minted. The change sits inside `add_source_read`.

### Files touched (estimate)

- `tools/policy/check_policy.py`

### Alternatives rejected

- **The cache path left out of the kept set.** A warm run then records no read of `govkit.py`, so
  an unguarded source loaded from a warm cache goes untraced and AC3 cannot red.
- **Bytecode writing turned off for the run.** The `.pyc` another run wrote is still opened, and
  the source is still never opened, so AC2 and AC3 fail on a warm tree.

## 5. Production-readiness checklist

- security — N/A: a path string is rewritten before a set insert; nothing is written.
- perf / scale — one suffix test per `open` event and one stdlib call per cache path.
- error / empty / loading states — a cache name the stdlib refuses is kept as spelled, so the trace
  names it as a `WRONG` instead of losing it.
- observability — the existing `guard-trace` lines; a warm run's `govkit.py` read is visible when its
  guard line is staged out (AC3).
- risks — a source file compiled under another implementation's cache tag maps to the same `.py`,
  which is the file that was read.
- testing — AC1 to AC3, cold, warm, and warm with the guard line staged out.
- migration — none.
- user docs — N/A: a gov-only leg.

## 6. Acceptance criteria

Every command runs from the repository root, in a scratch copy of the built tree. `check_policy.py`
names the policy kit's file under the kit, as `TOOL-dGroundRules-33` §6 does. A literal argument the
spec-tokens paths join cannot resolve is spelled whole in this block and named by the criteria,
never shortened:

```text
COLD_CACHE = python -c "import shutil; shutil.rmtree('tools/govkit/__pycache__', ignore_errors=True)"
WARM_CACHE = python -c "import py_compile; py_compile.compile('tools/govkit/govkit.py')"
UNGUARD    = in the copy's tools/gate-legs.json, the "{prefix}/govkit/govkit.py" entry of the
             "policy fixtures" row's guard list taken out
```

- **AC1** — When `COLD_CACHE` runs and then `python check_policy.py --fixture budgets-ships-join`
  runs, it prints the `guard-trace` count line with a count above zero and no `guard-trace` `WRONG`.
  Red when: the cold load's cache attempt or its temporary write is kept as a `.pyc` path.
  figure: the count is DERIVED from the run.
- **AC2** — When `WARM_CACHE` runs and then the same `--fixture budgets-ships-join` runs, it prints
  no `guard-trace` `WRONG`.
  Red when: a warm load keeps the interpreter-tagged `.pyc` path.
- **AC3** — When `WARM_CACHE` and `UNGUARD` run and then the same `--fixture budgets-ships-join`
  runs, it prints `guard-trace · WRONG tools/govkit/govkit.py`, and once `UNGUARD` is reverted it
  prints none.
  Red when: a warm load never records the source read the guard exists to hold.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the trace;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture`, the `guard-trace` join) · covers AC3 · a warm cache written and the `govkit.py` guard entry staged out of a scratch copy's `policy fixtures` row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 22 (HIGH, item H1) of the round-1 spec
  audit of units 33 and 34, from the review's sound fix, with the audit hook's cold and warm events
  and `source_from_cache` run on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.

## 10. Reuse audit

The seams extended are `add_source_read`, `TOOL-dGroundRules-33`'s one recorder, and the standard
library's `importlib.util.source_from_cache`, which is the inverse of the cache naming the importer
uses, so the unit spells no tag parser of its own.
`python tools/codebase-map/reuse_lookup.py "map a bytecode cache path back to its python source file"`
ranked `map_root`, `resolve_python` and `build_spec_path_re`, none of which reads a cache name: no
existing seam in the tree fits. The recall probe returned `TOOL-dGroundRules-33`, this audit's H1,
and `TOOL-aQuarriedLantern-1`'s review F5, where a kit's imports wrote `__pycache__` into a
worktree; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how does a file-access trace treat bytecode
caches, ignored paths and the git directory" --terms "audit hook trace pycache bytecode gitignored
guard-trace policy fixtures legs-for git-dir worktree"`
