# TOOL-dWitnessedBar-49 — the bash query sees a PATH lookup of `bash`, and the recall selftest resolves its bash through the block

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 2 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 49 at HIGH**, its item **H10**, alone in that item. `tools/memory-recall/selftest.py`
calls `shutil.which("bash")` at lines 466, 541, 1355, 1441 and 1659 and passes the result straight into
`subprocess.run` (`:1355-1361`). `shutil.which` walks PATH with no System32 or WindowsApps filter. The
file is in neither `TOOL-dWitnessedBar-26`'s site table nor any of its query's three shapes, so
`test_no_bare_bash_argv`, and `TOOL-dWitnessedBar-24`'s bare-shell-name leg that reuses the scan, read
`[]` while that selftest launches whatever bash PATH yields, WSL's launcher included on node d. This unit
takes the report's fix. It repairs `TOOL-dWitnessedBar-26`.

## 2. Scope (IN)

- **S1** — The fourth shape. `scan_bare_bash` gains shape 4: a call to `shutil.which` whose first
  argument is the constant `bash` or `bash.exe`, and in JavaScript a `which(` call with the string
  `bash` or an `execSync`/`execFileSync` running `where bash` or `which bash`, each outside a
  `resolve_bash_py` or `resolve_bash_js` block. Observed by AC1.
- **S2** — The site. `tools/memory-recall/selftest.py` carries the `resolve_bash_py` block inline and
  one adapter, `resolve_selftest_bash()`, which returns the block's `found` and raises `_Skip` with the
  block's refusal where each of the five sites raises `_Skip("no bash on PATH")` today. The five sites
  call it, so the file is one more row of unit 26's site table, its adapter contract `_Skip(refusal)`.
  Observed by AC2.

## 3. Non-goals (OUT)

- The block, its rule and the other sites: `TOOL-dWitnessedBar-26`'s.
- Candidate lists holding a bare `bash`: `TOOL-dWitnessedBar-48`'s shape 2.
- `profile_bar.py:290` and `tools/process-monitor/selftest.py:1146`, which call `shutil.which("bash")`
  today: both are unit 26 sites whose call moves inside the block's adapter, so shape 4 exempts them by
  the block rule.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-26` — the `resolve_bash_py` block, its parity row and `scan_bare_bash`, which this unit gives a fourth shape and one more site
- **hands-off** `TOOL-dWitnessedBar-57` — shape 4 of `scan_bare_bash`, which the resolver and ledger minors batch widens to a variable lookup of `bash` (id 17)

## 4. Design

### Evidence

- The five sites: `bash = shutil.which("bash")` then `if not bash: raise _Skip(...)` at
  `tools/memory-recall/selftest.py:466`, `:541`, `:1355`, `:1441` and `:1659`; `adopt()` runs
  `[bash, str(kitdir / "adopt-memory-recall.sh"), *args]` (`:1354-1361`).
- Two other tracked calls of `shutil.which("bash")`, `tools/run-gates/profile_bar.py:290` and
  `tools/process-monitor/selftest.py:1146`, sit in functions unit 26 rewrites as adapters.
- The leg running this selftest is `memory-recall kit selftest`.

### The shape

```
shape 4 (py) := Call(func=Attribute(Name("shutil"), "which"), args[0]=Constant("bash"|"bash.exe"))
shape 4 (js) := /\bwhich\(\s*['"]bash(\.exe)?['"]/  or  /exec(File)?Sync\(\s*['"](where|which) bash/
                outside a resolve_bash_py or resolve_bash_js block
```

### Inventory

Minted: `resolve_selftest_bash`; shape 4. Naming cells: `resolve_selftest_bash` is asked of `python
tools/lexicon/lexicon.py --suggest resolve_selftest_bash --as py.function` at the pass.

### Migration

None: the selftest skips where it skipped, now naming the block's refusal.

### Rollout

Live at landing. This unit, `TOOL-dWitnessedBar-48` and `TOOL-dWitnessedBar-27` share order 2; this
unit and `TOOL-dWitnessedBar-48` both write `tools/run-gates/measure_legs.py`, so the main loop
sequences those two within the group (BUILD-METHOD M6, clause 1). The new inline copy follows the
canonical block through its parity row whichever of this unit and `TOOL-dWitnessedBar-27` lands first.

### Files touched (estimate)

- `tools/memory-recall/selftest.py`
- `tools/run-gates/measure_legs.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **Filter System32 and WindowsApps out of `shutil.which`'s answer at each site.** Five copies of a
  partial rule; the block already refuses those and also runs the candidate.

## 5. Production-readiness checklist

- security — removes a path to WSL's launcher on a Windows node.
- perf / scale — one probe per selftest run instead of a PATH walk; the block's 20 s bound applies.
- error / empty / loading states — no bash: the selftest's existing skip, naming the refusal.
- observability — the skip line carries the block's `tried` lines.
- risks — a node whose only bash is a launcher now skips those five checks, which is the clause.
- testing — AC1 and AC2 by fixture and probe; the arm of §7 at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python measure_legs.py --selftest` runs in `tools/run-gates/` with a fixture `.py`
  holding `bash = shutil.which("bash")`, the `test_no_bare_bash_argv` arm reds naming it, and the same
  line inside a fixture's `resolve_bash_py` block stays green.
  Red when: shape 4 is missing, so a PATH lookup of bash reads `[]`.
- **AC2** — When `git grep -n 'shutil.which("bash")' -- tools/memory-recall/selftest.py` runs, it prints
  nothing, and `grep -c '^# >>> resolve_bash_py' tools/memory-recall/selftest.py` prints 1.
  Red when: any of the five sites keeps its PATH lookup.

## 7. Gates

`measure-legs selftest` · `memory-recall kit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene`

New arm: tools/run-gates/measure_legs.py · covers AC1 · `test_no_bare_bash_argv` over a fixture `shutil.which("bash")` line inside and outside a block, staged red by planting the line in a tracked `.py` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-26`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 49 (HIGH, item H10).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams are unit 26's `resolve_bash_py` block, carried to one more site under its parity row, and
`scan_bare_bash`, given a fourth shape. `python tools/codebase-map/reuse_lookup.py "find a bash looked up
on PATH by shutil.which"` ranked `resolve_bash` (the sites unit 26 names), `build_spec_path_re`,
`resolve_charter_path`, `attribute_paths`, `deriveSidecarPath` and `log_path`; none is the memory-recall
selftest's lookup, which the report's grep found.

Recall terms used: `python tools/memory-recall/query.py "which selftests look up bash on PATH with shutil.which" --terms "shutil.which bash selftest memory-recall PATH WSL launcher scan_bare_bash shape refusal adapter"`
