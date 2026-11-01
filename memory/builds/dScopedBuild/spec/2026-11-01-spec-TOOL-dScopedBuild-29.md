# TOOL-dScopedBuild-29 — the claim arm and the grace writer launch `map_diff.py` under the running interpreter, and read a non-zero exit as `not-installed`

**Status:** OPEN · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 6 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 17 at HIGH**, report item **H5**. `TOOL-dScopedBuild-9` §4 "The map's check
mode" spells the claim arm's call and the `point.map-writers` adapter's `argv` with a literal
`python3`, and says only that `{prefix}` resolves as gate-leg argvs do. The runner also rewrites
argv[0] `python3` to the resolved interpreter (`tools/run-gates/run-gates.sh:3852`), and the
subprocess launch from `routed_commits.py` leaves that step out. Unit 9 S6 maps only exit 2 to
`not-installed`. Where `python3` is the Microsoft Store stub, which answers `command -v` and exits
9009 with empty stdout, the arm reads zero `would-shrink` lines as clean and the grace shrink
silently does not happen.

This unit gives both launch sites one argv rewrite and one exit reading. It repairs
`TOOL-dScopedBuild-9` and builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — The interpreter. `derive_python_argv(argv)` in `tools/memory-tree/routed_commits.py`
  returns a copy of `argv` whose first word, when it is `python` or `python3`, is `sys.executable`,
  the rewrite `run-gates.sh:3852` applies with `PYBIN`; any other first word is returned unchanged.
  `check_claim_arm`'s `map_diff.py` call (unit 9 S3) and the Build exit's run of the argv
  `read_point_argv` returns (unit 9 S5) both pass through it, after `{prefix}` is resolved. Observed
  by AC1 and AC2.
- **S2** — The exit read. At both launch sites exit 0 is read as lines; exit 2 is unit 9 S6's
  `not-installed: <first stderr line>`; every other exit is
  `not-installed: <argv[0] basename> exited <rc>`, and an `OSError` at the spawn is
  `not-installed: <argv[0] basename> could not start: <why>`. None is a clean line, and at the
  writer none writes. This supersedes unit 9 S6's mapping of exit 2 alone. Observed by AC2 and AC3.
- **S3** — Unit 9 answered. Unit 9's acceptance ledger answers its AC2 with a note naming
  `TOOL-dScopedBuild-29 S2`. Observed by AC2.

## 3. Non-goals (OUT)

- A shared argv rewrite in `tools/lib/`. The two copies in the run-gates kit
  (`tools/run-gates/measure_legs.py:507`, `tools/run-gates/regen.py:273`) belong to a sibling kit,
  which a kit may not import; a third kit-local one is the rule the kits already follow.
- The left-shift lint over Python subprocess launches the report names. No clause of this build
  names it.
- Unit 9's `not-installed` cases for an absent map conf or kit, which stand.

### Edges

- **consumes-from** `TOOL-dScopedBuild-9` — S3's `check_claim_arm` launch, S5's `read_point_argv` argv and S6's exit mapping, which S1 and S2 complete (id 17)
- **hands-off** `TOOL-dScopedBuild-39` — S2's failed-exit line and §3's rationale, which that unit's S1 and S28 correct, naming `derive_leg_argv` the closest seam (ids 1, 21)
- **hands-off** `TOOL-dScopedBuild-41` — the ledger note on §3's first bullet, which this unit's builder writes with the rationale that unit's S19 respells, naming it (id 11)

## 4. Design

### Evidence

- `tools/run-gates/run-gates.sh:3852`: `case "${argv[0]}" in python|python3) argv[0]=$PYBIN ;; esac`,
  commented "the manifest stores the canonical python3; run under the resolved PYBIN".
- `tools/run-gates/regen.py:273-274` makes the same rewrite to `sys.executable` for a Python caller.
- Unit 9 §4 (`memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-9.md:153-161`) spells
  `python3 <codebase-map>/map_diff.py ...` and `["python3", "{prefix}/codebase-map/map_diff.py", ...]`,
  and says the join reads lines and never an exit code.
- The charter's toolchain fact: `tools/lib/resolve-python.sh` RUNS each candidate because the
  MS-Store `python3` stub answers `command -v` and exits 9009.

### The launch, after this unit

```
argv = derive_python_argv(resolve {prefix} in argv)
rc 0           -> read the lines
rc 2           -> not-installed: <first stderr line>                 (unit 9 S6)
rc other       -> not-installed: <argv[0] basename> exited <rc>      (S2)
OSError        -> not-installed: <argv[0] basename> could not start: <why>
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_python_argv` | python function, `routed_commits.py` | `py.function`, OK |

### Migration

None: no stored data changes.

### Rollout

Built at order 6, one step after unit 9 (order 5). It ties with `TOOL-dScopedBuild-27` and
`TOOL-dScopedBuild-8`, which also write `routed_commits.py`, so M6 sequences the three.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write`

### Alternatives rejected

- **Spell `sys.executable` into unit 9's argv rows.** The adapter row is data in `points.toml`, read
  by other callers that do not run Python; the canonical `python3` stays the stored word, as the
  manifest's does.
- **Map only 9009.** Any non-zero exit other than 2 carries no `would-shrink` reading either.

## 5. Production-readiness checklist

- security — no new write path; the writer writes only on exit 0, as before.
- perf / scale — unchanged: one spawn per launch.
- error / empty / loading states — every failed launch prints one `not-installed` line (S2).
- observability — the line names the program and its exit, so a stub host is visible.
- risks — none beyond unit 9's own.
- testing — AC1 by probe, AC2 and AC3 in the routed-commits selftest.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import
  routed_commits as r; print(r.derive_python_argv(['python3', 'x.py'])[0] == sys.executable,
  r.derive_python_argv(['bash', 'x'])[0])"` runs, it prints `True bash`.
  Red when: a `python3` first word passes through, or another first word is rewritten.
- **AC2** — When `check_routed_commits` runs on unit 9 AC3's map-adopting fixture with the resolved
  codebase-map kit's `map_diff.py` a stub that exits 3 printing nothing, standing in for the Store
  stub's 9009, which a POSIX host reads modulo 256, it prints
  `claim · not-installed: map_diff.py exited 3` and no `touched and still graced` line, and the leg's
  exit is unchanged.
  Red when: the arm prints a clean line or nothing, the silent pass the finding names.
  fixture: unit 9 AC3's, with `backlog.resolve_kit_dir` pointed at a stub kit directory.
- **AC3** — When `python routed_commits.py --build tFix --write` runs on the same fixture with the
  adapter's `argv` naming a program that cannot start, it prints `could not start` and the grace
  file's bytes are unchanged.
  Red when: the writer raises a traceback, or writes after a failed launch.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 · the claim arm over a stub writer exiting 3 with empty stdout and the writer over an argv that cannot start, staged by mapping exit 2 alone · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 9's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 17
  (HIGH, item H5).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 1, 21).
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (id 11).

## 10. Reuse audit

The rule is the runner's own argv rewrite (`tools/run-gates/run-gates.sh:3852`), whose Python form
`tools/run-gates/regen.py:273` already writes; the memory-tree kit cannot import the run-gates kit,
so S1 is its kit-local form, used by both of unit 9's launch sites.
`python tools/codebase-map/reuse_lookup.py "replace a python3 first argument with the running
interpreter before a subprocess"` ranked `before`, `resolve_python`, `python_symbols`,
`read_first_commit_date` and `derive_first_seen`; `resolve_python` is the shell launcher resolver,
not an argv rewrite, so no existing seam in the memory-tree kit fits.

Recall terms used: `python tools/memory-recall/query.py "python3 store stub exit 9009 subprocess argv rewrite" --terms "python3 stub 9009 PYBIN argv sys.executable subprocess adapter argv rewrite resolve_python"`
