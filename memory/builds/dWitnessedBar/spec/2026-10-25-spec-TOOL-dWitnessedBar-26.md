# TOOL-dWitnessedBar-26 — one bash resolver in `tools/lib` with its JavaScript twin

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 1 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0364@2fbc8cf5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-c.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-27 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

Make one bash resolver, extracted from the execution-based pair `profile_bar.resolve_bash` and
govkit's `resolve_bash` and keeping both their contracts, the only way a gov Python or JavaScript
file finds a bash, so that no site can reach WSL's launcher through a bare `bash` or a PATH-only
loop. Today eleven Python resolvers and one
JavaScript spawn each spell their own rule, and three of them fall back to the bare name, which
Windows resolves to System32's WSL launcher (gap-tool-20, AP-33).

## 2. Scope (IN)

- **S1** — The canonical Python block `# >>> resolve_bash_py` in `tools/lib/resolve_bash.py`: one
  function `resolve_bash(script="", host="")` returning `(found, tried, refusal)`, with the candidate
  order and the acceptance rule of §4 "The rule". If TOOL-dGroundRules-25 S28 has landed the file,
  its block is rewritten in place to this rule (§8 F1). Observed by AC1, AC2, AC3 and AC4.
- **S2** — The JavaScript twin, block `// >>> resolve_bash_js` in `tools/lib/resolve_bash.js`: one
  function `resolveBash({script, host})` returning `{found, tried, refusal}` under the same rule.
  Observed by AC5.
- **S3** — Both files run as a CLI, `python resolve_bash.py` and `node resolve_bash.js`, taking
  `--script <path>` and `--host windows|posix`, printing `bash: <path>` and one `tried: <line>` per
  candidate, exit 0, or the refusal line and exit 2. Observed by AC1, AC2, AC3 and AC5.
- **S4** — `tools/lib/resolve-python.test.sh` gains the rows `resolve_bash_py` and `resolve_bash_js`
  in `PARITY_ROWS`; its block extractor `blk` and its population grep read a `// >>> ` marker and
  `*.js` files beside `# >>> ` and `*.sh`, `*.py`; a section `2j` runs both canonicals over one
  truth table. Observed by AC6.
- **S5** — Every site the query of S6 finds carries the `resolve_bash_py` (or `resolve_bash_js`)
  block inline and keeps its own name and failure contract as a thin adapter, per §4 "The sites".
  No adapter returns, spawns or argv-substitutes a bare `bash`. Observed by AC7 and AC8.
- **S6** — The query is the arm: `test_no_bare_bash_argv` in `tools/run-gates/measure_legs.py` is
  widened from its own file to every tracked `*.py` and `*.js`, through a new function
  `scan_bare_bash(root)` it calls, per §4 "The query". Observed by AC7.
- **S7** — `resolve_shell_argv` raises `Refusal` when no bash resolves, instead of returning the argv
  with its bare `bash` unchanged. Observed by AC8.
- **S8** — `memory/gotchas/subprocess-resolves-a-different-shell.md` "The fix" names the one block and
  its twin instead of the three copies it lists today. NOT OBSERVED by a criterion: a prose pointer,
  graded by the memory hygiene leg at the close.

## 3. Non-goals (OUT)

- The wrong-shell refusal at entry points, and the call from these resolvers into its predicate:
  TOOL-dWitnessedBar-27's (shared interface I7).
- A bash resolver for shell scripts. A `.sh` entry point is already running in some bash; which one
  is unit 27's question.
- Cygwin's bash on a Windows host: `uname -s` answering `CYGWIN` is refused, as the clause names only
  MINGW and MSYS (§8 F3). `tools/process-monitor/selftest.py`'s `resolve_launcher` admits it today.
- The resolver's interpreter floor: dSafePassage's (TOOL-dSafePassage-11), per cl-0362.
- Moving govkit's `resolve_bash` into `tools/govkit/upgrade_steps.py`: TOOL-dSafePassage-35 S24's.
  This unit edits the function wherever it sits at the build run's base.
- The deferred ask `TOOL-dSettledRoster-6` ("three resolve_bash copies"): this unit's landing answers
  it, and its disposition is the main loop's to file.
- A row argv that names `bash` as data, such as `tools/run-gates/held_halves.py:129`'s WSL shim leg
  or a fixture manifest row: it is not a launch, and the WSL mirror runs bash in WSL on purpose.

### Edges

- **hands-off** `TOOL-dWitnessedBar-24` — `scan_bare_bash`, the repo-wide query behind
  `test_no_bare_bash_argv` that the portability pack's bare-shell-name leg runs
- **hands-off** `TOOL-dWitnessedBar-27` — the `resolve_bash_py` block and its `resolve_bash_js` twin,
  into which unit 27 adds the wrong-shell predicate's call
- **consumes-from** external — TOOL-dGroundRules-25 S28's `tools/lib/resolve_bash.py` and its inline
  copy in `tools/policy/check_policy.py` where that build has landed them; absent, this unit creates
  the file and the policy copy joins as data when dGroundRules lands
- **hands-off** `TOOL-dWitnessedBar-48` — the `resolve_bash_py` block and `scan_bare_bash`, which unit 48 gives the row-grammar site and a wider shape 2 (id 27)
- **hands-off** `TOOL-dWitnessedBar-49` — the `resolve_bash_py` block and `scan_bare_bash`, which unit 49 gives the memory-recall selftest site and a fourth shape (id 49)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 23, 42 and 43: shape 2's pinned count, and `resolve_shell_argv`'s nine callers once it raises, each a scope item of that unit
- **hands-off** `TOOL-dWitnessedBar-57` — the `resolve_bash_py` block and its parity row, which the resolver and ledger minors batch carries once in `tree_lib.py` and binds regen's lookup to (ids 17, 29)

## 4. Design

### The rule

One function per language, the same truth table. `host` is `windows` when `os.name == "nt"`
(JavaScript: `process.platform === 'win32'`), else `posix`; the argument overrides it for fixtures.

| Step | Candidate | Refused when |
|---|---|---|
| 1 | `GOV_BASH`, when set | it fails the probe below; the refusal names `GOV_BASH` and its value and nothing after it is tried |
| 2 | Git's own `bin/bash.exe`: the third parent of `git --exec-path`, joined with `bin/bash.exe` | the file is absent (a POSIX git yields `/usr/lib/git-core`, so this step is skipped there), or it fails the probe |
| 3 | PATH, each directory's `bash.exe` then `bash` | its forward-slashed lowercased path holds `/system32/` or `/windowsapps/`, or it fails the probe |

The probe runs the candidate once, with a 20 s bound (profile_bar's):

```python
[cand, "-c", 'u=$(uname -s) && printf "%s\\n" "$u" && { [ -z "$1" ] || test -f "$1"; }', "_", script]
```

A candidate passes when the run exits 0 and, on a `windows` host, its first output line starts with
`MINGW` or `MSYS`. A WSL launcher answers `Linux` (measured on node d, 2026-10-25, with a copy of
`C:/Windows/System32/bash.exe` outside System32: `uname -s` printed `Linux` and `pwd` a `/mnt/c/` path),
so the probe refuses it under any name. `script` keeps profile_bar's contract: a bash that cannot
`test -f` the caller's script is refused. No candidate passing is a refusal naming every `tried`
line and the remedy `set GOV_BASH to Git's bash`; the block never returns a bare `bash`.

`tried` is a list of `<candidate>: <why>` strings, `why` one of `runs`, `absent`, `a launcher`,
`did not run`, `answered <uname>`, `cannot see <script>`.

### The sites

The query of S6 found these at `3f2b31b5` (scout C's table), each verified at `cdfbd1cf`:

| Site | Today | Adapter contract kept |
|---|---|---|
| `tools/run-gates/profile_bar.py:282` `resolve_bash(script)` | candidates end in a bare `"bash"` | `(found, tried)`, `""` on refusal |
| `tools/run-gates/regen.py:232` `resolve_bash(probe)` | delegates to profile_bar | unchanged, delegates |
| `tools/govkit/govkit.py:1144` `resolve_bash()`, loop `:1185` | PATH only | memo `_BASH`, `Refusal(refusal)` |
| `tools/govkit/govkit.py:1200` `resolve_shell_argv` | returns the bare argv on `Refusal` | raises `Refusal` (S7) |
| `tools/memory-tree/corpus_ids.py:390`, loop `:421` | PATH only | `Problem(refusal)` |
| `tools/lexicon/selftest.py:49`, loop `:65` | PATH only, `test -f` probe | exit 2 naming the refusal, `script` its own file |
| `tools/branch-reconcile/selftest.py:1037`, loop `:1041` | falls back to `"bash"` | exit 2 naming the refusal |
| `tools/runlog/selftest.py:8092`, loop `:8100` | PATH only | `None`, memoised |
| `tools/roles/handoff.py:225`, loop `:233` | existence only, no run | `None` |
| `tools/settings-merge.py:925`, loop `:932` | nested function, PATH only | `None` |
| `tools/drift-audit/selftest.py:4328` `resolve_bash_shell` | tries a bare `bash` then `sh` | canonical first, then its own `[[ ]]` feature probe on the found bash; `None` |
| `tools/process-monitor/selftest.py:1133` `resolve_launcher` | bare `bash` first, accepts `CYGWIN` | `(found or None, tried)` |
| `tools/unattended/stop-guard.js:111` `spawnSync('bash', …)` | the bare name | `resolveBash()`; a refusal is `ok: false`, the path a spawn error takes today |
| `tools/policy/check_policy.py` (TOOL-dGroundRules-21 S14) | its S28 copy | as that unit writes it |

The seven loops over `bash.exe` and `bash` are the govkit, corpus_ids, lexicon, branch-reconcile,
runlog, handoff and settings-merge rows. A memo stays in the adapter, never in the block, so the
block is a pure function the truth table can call twice.

### The query

`scan_bare_bash(root)` lists, over `git ls-files '*.py' '*.js'` at `root`, every line outside a
`resolve_bash_py` or `resolve_bash_js` block that holds one of:

1. a call whose first argument is a list or tuple literal opening with the constant `bash` or
   `bash.exe`, read by `ast`, unless that call is `resolve_shell_argv` (which now refuses);
2. a tuple or list literal holding both `bash.exe` and `bash`, read by `ast` (the loop shape);
3. in JavaScript, `spawn`, `spawnSync`, `execFile` or `execFileSync` whose first argument is the
   string `bash` or `bash.exe`, read by a regex.

`test_no_bare_bash_argv` asserts the list is empty and that at least one file of each language was
read, so an empty population cannot pass. At `cdfbd1cf` shapes 1 and 3 find `stop-guard.js:111`
only and shape 2 the seven loops (PINNED, measured 2026-10-25 with an `ast` probe over 150 tracked
`*.py`); the arm re-derives them at every run.

### Inventory

Minted: `tools/lib/resolve_bash.py`, `tools/lib/resolve_bash.js`, the blocks `resolve_bash_py` and
`resolve_bash_js`, `resolveBash`, `scan_bare_bash`, the `PARITY_ROWS` rows, section `2j`. Naming
cells: `scan_bare_bash` is asked of the lexicon's `--suggest` under `--as py.function`, and
`resolveBash` under `--as js.function`, at the pass.

### Migration

None. `GOV_BASH` keeps its name and meaning, and every adapter keeps its signature. A node whose
only bash was reached through the bare-name fall-back now refuses, which is the clause.

### Files touched (estimate)

- `tools/lib/resolve_bash.py` (new, or rewritten if TOOL-dGroundRules-25 landed it)
- `tools/lib/resolve_bash.js` (new)
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/profile_bar.py`
- `tools/run-gates/regen.py`
- `tools/run-gates/measure_legs.py`
- `tools/govkit/govkit.py`
- `tools/govkit/upgrade_steps.py` (where TOOL-dSafePassage-35 S24 moved the resolver)
- `tools/memory-tree/corpus_ids.py`
- `tools/lexicon/selftest.py`
- `tools/branch-reconcile/selftest.py`
- `tools/runlog/selftest.py`
- `tools/roles/handoff.py`
- `tools/settings-merge.py`
- `tools/drift-audit/selftest.py`
- `tools/process-monitor/selftest.py`
- `tools/unattended/stop-guard.js`
- `tools/policy/check_policy.py` (where dGroundRules landed it)
- `memory/gotchas/subprocess-resolves-a-different-shell.md`

### Alternatives rejected

- **Import the canonical instead of inlining it.** `tools/lib/` ships nothing, and govkit, the
  memory-tree kit and the unattended kit are copy-installed, so an import breaks at an adopter.
- **Raise a shared exception class from the block.** Each kit has its own (`Refusal`, `Problem`); a
  tuple return lets each adapter raise its own, as `remote_ladder_py` returns a refusal string.
- **Keep PATH first and add the Git candidate last.** The clause orders Git's bash before PATH, and a
  PATH-first order resolves Git's `usr/bin/bash.exe` or a user's own bash ahead of the one git ships.

## 5. Production-readiness checklist

- security — no new write path; the resolver spawns only absolute candidates it was given, and a set
  `GOV_BASH` that fails is refused rather than skipped, so an operator's choice is never overridden.
- perf / scale — at most one probe per candidate, 20 s bound each; adapters memoise as today.
- error / empty / loading states — no candidate is a refusal naming every `tried` line and the
  remedy; an empty scan population is a red, never a pass.
- observability — the CLI prints every candidate with its reason.
- risks — a node whose only working bash was the bare-name fall-back starts refusing; that node was
  running WSL's bash, which is the defect. A Cygwin-only Windows node refuses (§3).
- testing — AC1 to AC8 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — none under `help/`: no page names the resolver; S8 updates the gotcha.

## 6. Acceptance criteria

- **AC1** — When `python resolve_bash.py --host windows` runs from `tools/lib/` on a Windows node
  with `PATH` staged to a scratch directory holding a copy of System32's `bash.exe` first, then
  `C:/Windows/System32`, then Git's `cmd` directory, it prints `bash:` naming Git's own `bash.exe`,
  and `tried:` lines naming the copy as `answered Linux` and System32's as `a launcher`.
  Red when: the staged WSL-first break, the probe's `uname -s` test removed or PATH searched before
  Git's candidate, so the copy is returned.
  fixture: a Windows node with WSL installed, so the copy runs and answers `Linux`; node d has one.
- **AC2** — When the same command runs with Git's `cmd` directory left off `PATH`, it exits 2 with a
  refusal naming every `tried` line and `GOV_BASH`, and prints no `bash:` line.
  Red when: a fall-back returns the bare name `bash`, or the first candidate that merely runs.
- **AC3** — When `python resolve_bash.py --host posix` runs with `PATH` staged to the copy alone, it
  prints `bash:` naming the copy: on a `posix` host a bash that runs is accepted whatever `uname -s`
  answers, which is a Linux node's own bash.
  Red when: the `MINGW`/`MSYS` test applies on a `posix` host, so a Linux node refuses its own bash.
  fixture: the real Linux arm is the remote CI or a Linux node running AC6's section `2j`; this run
  observes the host branch on node d.
- **AC4** — When `GOV_BASH` is set to a file that is not a bash and `python resolve_bash.py` runs, it
  exits 2 naming `GOV_BASH` and the value, with one `tried:` line; set to Git's own `bash.exe`, it
  prints that path.
  Red when: an unusable `GOV_BASH` falls through to step 2.
- **AC5** — When `node resolve_bash.js` runs under each staging of AC1 to AC4, its stdout and exit
  code equal `python resolve_bash.py`'s under the same staging, line for line.
  Red when: the twin orders, refuses or reports differently.
- **AC6** — When the `resolve_bash_py` block is cut from `resolve_bash.py` and from
  `tools/govkit/govkit.py` with the parity arm's `blk` awk range, and the `resolve_bash_js` block
  from `resolve_bash.js` and `tools/unattended/stop-guard.js`, each pair is identical; with one byte
  changed in either copy, the pair differs.
  Red when: the extractor ignores the `// >>> ` marker, so the JavaScript copy is never compared.
- **AC7** — When `scan_bare_bash` is called from `measure_legs.py` (imported with `tools/run-gates`
  on `sys.path`) with the repository root at the pass tip, it returns `[]`; with the root of a fixture
  repo under `%TEMP%` holding one `.py` with `subprocess.run(["bash", "x.sh"])`, one with the loop
  tuple `("bash.exe", "bash")`, and one `.js` with `spawnSync('bash', [])`, it names all three.
  Red when: any shape of §4 "The query" is not read, or the scan reads its own file only.
- **AC8** — When a probe calls `govkit.resolve_shell_argv(["bash", "x.sh"])` with `PATH` staged
  as in AC2 and `GOV_BASH` unset, it raises `Refusal`; with Git's `cmd` on `PATH`, it returns Git's
  own `bash.exe` as argv 0.
  Red when: the argv comes back with the bare `bash` at position 0.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `measure-legs selftest` · `profile-bar selftest` · `corpus-ids selftest` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor` · `recall floor arms` · `lexicon selftest` · `codebase-map kit selftest` · `branch-reconcile selftest` · `runlog selftest` · `run-gates run-log line` · `pre-push run-log line` · `drift-audit selftest` · `process-monitor census selftest` · `settings-merge selftest` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `resolve_bash_py` and `resolve_bash_js` parity rows and section `2j`'s truth table, staged by one byte changed in the stop guard's copy and by the probe's `uname -s` test cut from the canonical · that suite's assertion count, raised by the rows
New arm: tools/run-gates/measure_legs.py · covers AC7 · `test_no_bare_bash_argv` widened through `scan_bare_bash`, staged by a planted `spawnSync('bash', …)` in a tracked `.js` · none
New arm: tools/memory-tree/corpus_ids.py · covers AC4 · the existing `GOV_BASH` arms of `corpus_ids.py` kept green over the adapter, staged by the adapter falling through an unusable override · none
New arm: tools/govkit/selftest.py · covers AC8 · the existing `GOV_BASH` refusal arm kept green, plus `resolve_shell_argv` refusing under a staged PATH, staged by restoring the bare-argv fall-back · none

## 8. Open questions

- **F1 — TOOL-dGroundRules-25 S28 specs `tools/lib/resolve_bash.py` holding profile_bar's rule,
  which ends in a bare `"bash"` candidate; does this unit mint a second block or rewrite that one?**
  Options: (a) rewrite the S28 block in place to the clause's rule, its policy copy following through
  the parity row; (b) a second block beside it. (b) leaves two canonicals for one fact and keeps the
  fall-back the clause refuses. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, the clause's
  "one bash resolver in `tools/lib`" and its "refusal in place of any fall-back". widens: none ·
  relaxes: none
- **F2 — What does the block return, given two contracts to keep?** Options: (a) a
  `(found, tried, refusal)` tuple, each adapter mapping it to its own contract; (b) raise an exception the block defines;
  (c) profile_bar's `(found, tried)` alone. (b) cannot reach a copy-installed kit's own exception
  class, and (c) loses the refusal text govkit names. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3, tie-broken by reuse of `remote_ladder_py`'s refusal-string seam. widens: none · relaxes: none
- **F3 — Which `uname -s` answers pass on a Windows host?** Options: (a) `MINGW` and `MSYS`, the
  clause's; (b) those and `CYGWIN`, as `resolve_launcher` admits today. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 1, the clause text. widens: none · relaxes: none
- **FACT-QUESTION · F4 — Does the third parent of `git --exec-path` hold Git's `bin/bash.exe` on a
  Git for Windows node?** Probe: `git --exec-path` and a stat of `<that>/../../../bin/bash.exe`.
  Observation, node d, 2026-10-25: `C:/Program Files/Git/mingw64/libexec/git-core`, and the file
  exists. Liveness: on a POSIX git the path is `/usr/lib/git-core` and the derived file is absent, so
  the probe yields a negative. RESOLVED (agent, 2026-10-25, delegated): the third parent, rung 2.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 26, the brief's shared interface I6,
  scout C's row for cl-0364, and the sites read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-48, TOOL-dWitnessedBar-49, TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seam extended is the execution-based pair the clause names: `tools/run-gates/profile_bar.py:282`
and `tools/govkit/govkit.py:1144`, plus the Git-derived and `uname -s` precedent at
`tools/process-monitor/selftest.py:1133`, folded into the inline-block mechanism `PARITY_ROWS` of
`tools/lib/resolve-python.test.sh:168-184`, which already holds two-language canonical pairs
(`remote_ladder_py` and `remote_ladder_sh`). The lookup,
`python tools/codebase-map/reuse_lookup.py "resolve a bash executable by running each candidate"`
with the words `and refusing launchers` appended, ranked `resolve_bash` as a SEAM
across eight files (fan-in 4), `resolve_python` and `resolve_kit_dir` as the inline-block carriers,
and did not list `resolve_launcher` or `resolve_bash_shell`, whose names it does not stem to `bash`
resolution; both were found by `git grep` instead. It also did not see `stop-guard.js`. The recall
probe returned scout C's row, the shape audit's appendix (eleven definitions) and
`TOOL-dSettledRoster-6`; none disagreed with source at `cdfbd1cf`.

Recall terms used: `python tools/memory-recall/query.py "how is one bash resolver shared that runs each candidate and refuses the WSL launcher" --terms "resolve_bash GOV_BASH WSL launcher System32 WindowsApps git-bash candidate runs parity inline copy uname"`
