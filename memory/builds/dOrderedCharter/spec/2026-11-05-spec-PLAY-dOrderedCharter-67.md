# PLAY-dOrderedCharter-67 — a suite's guard holds every module it imports, and the bar reads an undefined name

**Status:** CLOSED · rev-1 · 2026-11-05 · node d · Tier-2 · base de8d2d3a1 · streams playbook · order 17 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 |
| [2026-11-05-build-PLAY-dOrderedCharter-67-1-builder-return.md](../build/2026-11-05-build-PLAY-dOrderedCharter-67-1-builder-return.md) | journal | — |
| [2026-11-05-build-PLAY-dOrderedCharter-67-deviation-671.md](../build/2026-11-05-build-PLAY-dOrderedCharter-67-deviation-671.md) | deviation | — |
| [2026-11-05-build-PLAY-dOrderedCharter-67-ledger.md](../build/2026-11-05-build-PLAY-dOrderedCharter-67-ledger.md) | journal | — |
| [2026-11-05-prompt-PLAY-dOrderedCharter-67-1-spec-writer.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-67-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-PLAY-dOrderedCharter-67-build-brief.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-67-build-brief.md) | journal | — |
| [2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief.md) | research | PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes H1 of the closing diff review. PLAY-dOrderedCharter-18 moved the id grammar into
`tools/memory-tree/id_grammar.py`, and no recall guard followed it, so a scoped bar skips the three recall
legs or reuses their green after an edit to that file alone. The guards gain the moved file, and one scanner
gates the two classes behind this: a Python suite importing a module outside its leg's guard, and a Python
name read and never bound. The second class is why unit 18's two undefined names passed every pass
(`memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-38-close-carry.md`).

## 2. Scope (IN)

Every line below was read at `62c5f0c5c`, whose `tools/` and `skills/` equal base `de8d2d3a1`.

- **S1** — H1's guards. `tools/gate-legs.json` gains the exact paths the Design section's guard table lists,
  on the ten legs it names. That table holds the report's four legs (the three recall legs and
  `drift-audit selftest`) and the six more the class arm reds on arrival. Observed by AC1 and AC2.
- **S2** — The guard arm. A new gov-only scanner `tools/run-gates/py_reads.py` walks the import closure of
  each leg whose `guard` is set and whose argv runs a Python file. It reds a walked module the guard does not
  cover. Observed by AC3 and AC4.
- **S3** — The undefined-name arm, in the same file. It reads every tracked `*.py` outside the memory root
  and reds a name loaded and never bound. Observed by AC5 and AC6.
- **S4** — The leg and its rows. `tools/gate-legs.json` gains the one leg the Inventory names, with a
  `[[exempt_leg]]` row, a `project-owned` row for the file in `tools/run-gates/kit.toml`, a pin row and a
  dossier claim. Observed by AC7.
- **S5** — The scanner's `--selftest` plants, run by one new arm of `tools/run-gates/run-gates.gov.test.sh`.
  Observed by AC3, AC4 and AC5, whose probes run the same cases by hand.
- **S6** — The checklist. `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` loses its "No machine gate
  yet" paragraph and gains one that names the leg for Python suites and keeps the record as the checklist
  entry for shell suites. Observed by AC8.

## 3. Non-goals (OUT)

- **Shell suites.** A `*.test.sh` that resolves a sibling kit through `resolve_kit_dir` is not walked. The
  record names `tools/hooks/scratch-guard.test.sh` as one, and a shell walker is a build of its own.
- **The `GATE_SELFTESTS=changed` selection.** It reads the epoch set for an owned leg, and
  `tools/run-gates/run-gates.sh` states that ceiling. The report leaves it standing.
- **Descriptor guards.** `tools/memory-tree/kit.toml` and `tools/codebase-map/kit.toml` carry `{kit}/` guards,
  and no token can name a sibling kit there (TOOL-aCollapsedScan-11). `tools/govkit/govkit.py#selfcheck`
  compares no guard between the manifest and a descriptor, so the manifest moves alone.
- **Frozen records.** The undefined-name arm does not read `memory/`. Three record scripts under
  `memory/builds/dTracedLattice/build/` hit the predicate, and a landed record is not rewritten.
- **A bug-class entry for undefined names.** A gate fits, so the brief's fallback is not owed.

### Edges

none

## 4. Design

### Why the class arm fits this unit

The brief asks whether the report's left-shift arm fits. It does, on two measurements taken by this writer
at `62c5f0c5c` with a scratch copy of the predicate. Over the 26 guarded legs whose argv runs a Python file,
10 show a gap, and every gap closes with an exact-path edit to one file, `tools/gate-legs.json`. The record's
own objection, that a lint reds scratch-guard's leg on arrival, is about a shell suite, which this scope does
not read. The undefined-name predicate hits 0 of the 135 tracked `*.py` outside `memory/`.

Both arms are one mechanism: one AST read of a Python file, on one leg, for what the bar otherwise never reads.
All counts here are PINNED at `62c5f0c5c`, and the leg's own summary line re-derives them.

### The guard table

| Leg | Paths added (each spelled `{prefix}/...`) |
|---|---|
| `memory-recall kit selftest` · `recall floor` · `recall floor arms` | `memory-tree/id_grammar.py`, `memory-tree/tree_lib.py`, `policy/budgets.py`, `policy/policy.py` |
| `drift-audit selftest` | `memory-tree/id_grammar.py`, `memory-tree/tree_lib.py`, `lexicon/canon.py`, `lexicon/lexicon.py`, `lexicon/lexicon_conf.py`, `lexicon/scaffold_lexicon.py`, `lexicon/subtokens.py` |
| `build-index selftest` · `gotchas selftest` | `policy/budgets.py`, `policy/policy.py` |
| `codebase-map kit selftest` · `codebase-map gate coverage` | `memory-tree/coverage_join.py` |
| `process-monitor census selftest` | `process-monitor/classify.py`, `process-monitor/reap.py`, `process-monitor/scope.py` |
| `measure-legs selftest` | `process-monitor/classify.py` |

The arm is the authority: where its first run names a path this table omits, the builder adds it. The report's
fix names `id_grammar.py` alone. `tree_lib.py` and the rest are what the same walk reaches.

### The guard arm

`derive_guard_gaps(legs, tool_root)` reads each row of `tools/gate-legs.json` with a non-empty `guard`,
whose `argv[0]` starts `python`, and whose argv holds a `.py` word. For that entry file:

1. Search directories start at the entry's own directory.
2. `tools/memory-tree/import_walk.py#scan_imports` gives each walked file's `import` and `from` names, and
   each resolves to `<importer dir>/<first name>.py`, then to `<dir>/<first name>.py` for each search directory.
3. A literal `resolve_kit_dir("<home>", ...)` call in a walked file adds `<tool root>/<home>` to the search
   directories, for the whole closure, since `sys.path` is one per process. The walk repeats until no directory
   is added. A `dynamic` row of `scan_imports` is not followed.
4. A module is covered when it equals a guard path or sits under a guard ending `/`, with `{prefix}` expanded.
   Each uncovered module prints `py-reads: RED guard · <leg> · <module> is imported and outside its guard`.

**What it does not read**, printed on every run with its count: a leg whose head is not Python, a module
reached through a subprocess, a `python -c` body, a data file a suite reads, and a kit named by a computed
string. The closing line is `py-reads: guards · <n> suites walked, <m> guarded legs of another head not read`.

### The undefined-name arm

`scan_unbound_names(source)` is the predicate of the scratch script `undef.py`, kept here because the scratch
folder does not outlive the run:

```python
bound = set()
for x in ast.walk(tree):
    if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): bound.add(x.name)
    if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
        a = x.args
        bound.update(y.arg for y in a.posonlyargs + a.args + a.kwonlyargs + [z for z in (a.vararg, a.kwarg) if z])
    if isinstance(x, ast.Name) and isinstance(x.ctx, (ast.Store, ast.Del)): bound.add(x.id)
    if isinstance(x, (ast.Import, ast.ImportFrom)):
        bound.update((al.asname or al.name).split(".")[0] for al in x.names)
    if isinstance(x, ast.ExceptHandler) and x.name: bound.add(x.name)
    if isinstance(x, (ast.Global, ast.Nonlocal)): bound.update(x.names)
    if isinstance(x, (ast.MatchAs, ast.MatchStar)) and x.name: bound.add(x.name)
    if isinstance(x, ast.MatchMapping) and x.rest: bound.add(x.rest)
known = bound | set(dir(builtins)) | {"__file__", "__name__", "__doc__"}
miss = sorted({x.id for x in ast.walk(tree) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)} - known)
```

A file with a star import is skipped and counted, because its names cannot be known. A file that does not parse
is a refusal, exit 2, naming it. Each hit prints `py-reads: RED name · <path> · <name> is read and never bound`.
The population is `git ls-files -z -- '*.py'` minus the memory root, read through `id_grammar.load_conf`, the
shape `tools/gate-lint/encoding_posture.py#scan_tree` uses. An empty population exits 2.

**What it does not read**: the bound set is the whole module, so a name bound in one function and read in another
passes. So does a read before its binding, an attribute, a name in a string or an `eval`, and a Python script
with no `.py` suffix. The closing line is `py-reads: names · <n> files read, <s> star imports skipped`.

### The command

`python tools/run-gates/py_reads.py` runs both arms and exits 0 green, 1 red, 2 refused. `--names <file>` runs
the name arm over one file, `-` being stdin. `--guards <leg>` prints one leg's closure and gaps. `--selftest`
runs the plants. It takes `tools/memory-tree/import_walk.py` and `id_grammar.py` through `resolve_kit_dir`, as
`tools/run-gates/owed_rows.py` takes its kits, which its `project-owned` row permits.

The plants: a file reading an undefined name reds; the same file with the name defined is green; a star import
counts and reds nothing; a fixture leg whose suite imports a sibling module outside its guard reds; the same leg
with the path in its guard is green; a sibling reached only through a literal `resolve_kit_dir` call reds; a file
that does not parse exits 2.

### The probes

Run from the repo root. `pr` reaches the scanner by module, so no bullet spells a path not yet tracked.

```bash
pr() { python -c "import sys; sys.path.insert(0, 'tools/run-gates' ); import py_reads; sys.exit(py_reads.main(sys.argv[1:]))" "$@"; }
scoped() { # one line per named leg: the paths a change to id_grammar.py alone moves under that leg's guard
  w="$(mktemp -d)/w"; git worktree add -q --detach "$w" HEAD
  ( cd "$w"; printf '\n# probe\n' >> tools/memory-tree/id_grammar.py
    python - <<'P'
import json, subprocess
want = ("memory-recall kit selftest", "recall floor", "recall floor arms", "drift-audit selftest")
for leg in json.load(open("tools/gate-legs.json", encoding="utf-8")):
    if leg["name"] in want:
        g = [p.replace("{prefix}", "tools") for p in leg["guard"]]
        d = subprocess.run(["git", "diff", "--name-only", "HEAD", "--", *g], capture_output=True, text=True).stdout
        print(leg["name"], "|", d.strip() or "NOTHING")
P
  ); git worktree remove --force "$w"
}
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/run-gates/py_reads.py` | a gov-only scanner | a file name in the kit's snake-case set |
| `derive_guard_gaps`, `scan_unbound_names` | Python functions | `py.function`, graded at build by `lexicon.py --suggest` |
| `python reads (a name never bound, an import outside its guard)` | a gate leg, `chunk` `declarations`, `subject` `repo`, `ceiling` 120, `enforces` `principle.p16`, no guard | none |

The leg carries no guard because a new import or an undefined name can arrive in any file, and a guard here
would be the hole this unit closes. `tools/playbook/core.py#run_meta_check` refuses a guard beside `enforces`.

### Migration

None. The leg is gov-only, and a guard edit changes which diffs select a leg and nothing it grades.

### Rollout

Live at landing. Each guard edit moves its leg's input key once, so each named leg runs once on the next bar.

### Files touched (estimate)

- `tools/gate-legs.json`: S1, S4
- `tools/run-gates/py_reads.py` (new): S2, S3, S5
- `tools/run-gates/kit.toml`: S4
- `tools/run-gates/run-gates.gov.test.sh`: S5
- `tools/govkit/registry.toml`: S4
- `tools/govkit/subject-pins.tsv`: S4, written by `govkit.py selfcheck --write`, the main loop's where a role refuses
- `memory/map/features/run-gates.md`: S4
- `memory/map/generated/`: S4, written by `gen_map.py --write`
- `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`: S6

No path here overlaps a sibling unit's set: units 68, 69 and 70 touch no file above.

### Alternatives rejected

- **A check inside an existing leg.** `core meta-check` and `every held leg is budgeted, every budget row
  resolves` each name what they check, and neither is a read of Python sources. The name would stop being true.
- **A mode of `tools/gate-lint/encoding_posture.py`.** That file ships to adopters and its class is encoding. The
  guard arm needs `import_walk.py` from a sibling kit, which `gate-lint`'s `requires = []` does not admit.
- **Changed files only**, as the scratch script reads. The whole population costs under five seconds and needs
  no base, and a base is a state a scoped run can get wrong.

## 5. Production-readiness checklist

- security: N/A. The scanner reads tracked files and `tools/gate-legs.json`, runs no scanned code and writes nothing.
- perf / scale: one `ast.parse` per tracked `*.py` and per closure file. The scratch predicate took under five
  seconds over 186 files (PINNED, `62c5f0c5c`). The ceiling of 120 is a first estimate, and the close derives it.
- error / empty / loading states: an unparsable file, an absent manifest and an empty population each exit 2,
  naming what could not be read, so a zero is never a reading of nothing.
- observability: the two closing summary lines, printing what was read and what was not.
- risks: a guard widened to an exact file runs a leg more often, which is the point. `{prefix}/policy/budgets.py`
  lands on five legs, inside `BROAD_LEG_FLOOR` in `tools/check-spec-tokens.py`.
- testing: the plants of S5, and AC1 to AC8 by a pass. The main loop observes the new arm red, then green.
- migration: none (Migration, above).
- user docs: N/A. The leg is gov-only and no page under `help/` lists legs.

## 6. Acceptance criteria

- **AC1** — When `python -c "import json; w=('memory-recall kit selftest','recall floor','recall floor arms','drift-audit selftest'); print(sum('id_grammar.py' in str(l.get('guard')) for l in json.load(open( 'tools/gate-legs.json' , encoding='utf-8')) if l['name'] in w))"`
  runs, it prints `4`.
  Red when: a recall leg or `drift-audit selftest` still lacks the path. At base it prints `0`.
- **AC2** — When `scoped`, the Design section's probe, runs at the tip, each of its four lines ends
  `tools/memory-tree/id_grammar.py`. That diff is the predicate `changed` in the runner evaluates.
  Red when: a line ends `NOTHING`, so an edit to that file alone leaves the leg selected by nothing. Before S1 all four do.
- **AC3** — When `pr --guards "recall floor"` runs at the tip, it prints a closure naming
  `tools/memory-tree/id_grammar.py` and no `RED guard` line, and exits 0.
  Red when: the walk stops at the kit's own directory, so the closure omits the moved file. Or the leg's guard
  lost the path, so a `RED guard` line prints.
- **AC4** — When `pr --guards "recall floor"` runs in a detached scratch worktree of the tip, with
  the path of `tools/memory-tree/id_grammar.py` deleted from that leg's row of `tools/gate-legs.json`, it exits 1 and
  prints `py-reads: RED guard · recall floor · tools/memory-tree/id_grammar.py is imported and outside its guard`.
  Red when: the arm stays green on a real gap.
- **AC5** — When `git cat-file blob deb67afb12b6 | pr --names -` runs, it exits 1 and names `read_relation_gate`.
  When `git cat-file blob 1182b8254440 | pr --names -` runs, it exits 1 and names `test_digest_covers_kit_version`.
  Red when: the arm misses unit 18's two real names. The blobs are `tools/memory-tree/row_grammar.py` and
  `tools/memory-recall/selftest.py` at `2d03321ab`.
  figure: both names are PINNED, and this writer's scratch predicate printed each alone.
- **AC6** — When `pr --names -` reads `print(1)` on stdin, it exits 0. When `pr` runs at the tip with no argument,
  it exits 0, and its last two lines print a files-read count and a suites-walked count, neither zero.
  Red when: a true name reds, the tree carries a hit, or a count reads zero.
  figure: the counts are DERIVED at observation. At `62c5f0c5c` the scratch predicate read 135 files and 26 suites.
  permission: the bare form is the leg's argv through a `python -c` door, so a role agent stops at the first
  sentence and the main loop observes the second.
- **AC7** — When `python tools/run-gates/owed_rows.py --base HEAD` runs before the pass commit, its only `owed`
  row is the `tools/govkit/subject-pins.tsv` pin when the role refuses `selfcheck --write`, and it prints the
  `deferred` line for `tools/run-gates/ceiling-evidence.txt`. When `python tools/govkit/govkit.py shipped` runs, no
  row names the new scanner.
  Red when: a descriptor row or the dossier claim is missing, or the file ships.
- **AC8** — When `grep -c "No machine gate yet" memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` runs, it
  prints `0`, and `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the record still says no gate exists, or the edit breaks the catalogue's checks.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `core meta-check`

The first nine are what the guards join owes the Files-touched paths, derived by this writer from each leg's
`guard` under `BROAD_LEG_FLOOR` 5. `{prefix}/` and `{prefix}/run-gates/` are broad and excluded. The last two are
the rows S4 writes.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC3 AC4 AC5 · runs the scanner's `--selftest`, whose plants stage an undefined name and a suite import outside its guard · `FLOOR_ASSERTIONS` 16 to 17

The new leg is itself a new gate. The main loop observes it red at the close by the plants above, and by AC4's
deleted guard path.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-05 · initial draft, by `2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief`, H1 and the
  undefined-name class of the close carry, each line read at `62c5f0c5c`.

## 10. Reuse audit

The seams extended are `tools/memory-tree/import_walk.py#scan_imports`, the one import walk, and the shape of
`tools/run-gates/owed_rows.py`, a gov-only reader under a `project-owned` row. The population and exit grammar
follow `tools/gate-lint/encoding_posture.py#scan_tree`. No existing seam reads a leg's guard against its imports,
and none reads an undefined name: `git grep` of `tools/gate-legs.json` and `tools/run-gates/` for `pyflakes`, `ruff`
and `undefined` found neither, and neither module is installed here. The probes
`python tools/codebase-map/reuse_lookup.py "a gate that reads a leg's guard against what the suite imports"` and
`python tools/codebase-map/reuse_lookup.py "python scan for a name read and never bound"` ranked generic readers
(`read_text`, `read_conf`, `legs`) and no seam for either. The recall query returned TOOL-aHeardState-6 and
TOOL-aCollapsedScan-11, which this spec follows, and the review itself. Where the record and the source disagree:
the record says a lint reds scratch-guard's leg, and that holds for a shell walker only.

Recall terms used: `python tools/memory-recall/query.py "how is a held suite's leg guard kept in step with the sibling kit modules it imports" --terms "guard gate-legs held suite sibling kit import closure id_grammar resolve_kit_dir input_key changed"`
