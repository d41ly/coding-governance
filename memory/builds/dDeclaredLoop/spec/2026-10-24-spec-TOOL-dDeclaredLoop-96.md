# TOOL-dDeclaredLoop-96 — the round-11 spec audit's 13 minors, batched

**Status:** CLOSED · rev-3 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-96-deviation-961.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-96-deviation-961.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-96-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-96-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-96-2-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-96-2-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-96-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-96-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-96-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-96-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-95 |

<!-- /gen:spec-records -->

## 1. Goal

The round-11 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md`)
exited CONVERGED with 14 confirmed findings over units 93 and 94, the round-10 promotions. Its one high,
id 1, is unit 95. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW.
Each finding keeps its report id and its own scope item, including where the report merged ids into one
item. The report's three refuted findings, ids 6, 8 and 11, are not in the disposal population.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M2 | MEDIUM | 4, 12 | S2, S3 |
| M3 | MEDIUM | 9 | S4 |
| M4 | MEDIUM | 10 | S5 |
| M5 | MEDIUM | 13 | S6 |
| M6 | MEDIUM | 14 | S7 |
| L1 | LOW | 3 | S8 |
| L2 | LOW | 5, 15 | S9, S10 |
| L3 | LOW | 7 | S11 |
| L4 | LOW | 16 | S12 |
| L5 | LOW | 17 | S13 |

At rev-3 none of S1 to S13 has anything left to build. Each spec text they amend sits in a spec that is
CLOSED at the branch tip, or in 94's, which is CLOSED at order 48 before this unit builds, so frozen.
Each code half was built by 90 §8 F8 (a), or has nothing to change because `load_tree_lib` takes no
argument under 92 §8 F3 (c). §3 names each with its evidence, and F6 settles S13, the one half that
could still build. The item ids and the criterion ids AC1 to AC13 keep their labels on §3's table, so a
sibling's citation of them still lands.

What this unit still owes is S14, the observation that the skew row of ids 5 and 15 holds after 94 S21
rewrites the refusal of `load_tree_lib` at order 48. The pass writes no file of the tree. It builds at
order 50 and closes on AC14 and AC15.

## 2. Scope (IN)

- **S14** — ids 5 and 15, observed at this unit's pass, after 94 S21 has rewritten `load_tree_lib` in
  `tools/loop/loop_lib.py` at order 48. The `no-own-conf-read` plant of `tools/loop/budget.py` first
  loads the real `tree_lib` in its own process through `load_tree_lib`. It then checks a kit pair whose
  `tree_lib.py` lacks `derive_constant_charges` in a fresh `sys.executable -I` child, and the child's
  refusal still names `derive_constant_charges` and `govkit update --kits memory-tree`, with no
  `Traceback`. No code moves in this pass. Observed by AC14, AC15.

## 3. Non-goals (OUT)

- **S1 to S13, settled at the tip.** Each was read on the branch tip §4 Evidence names. Their criteria,
  AC1 to AC13, leave the scope with them; AC14 and AC15 are new labels.

| Item | Id | Rev-2 ordered | Settled because |
|---|---|---|---|
| S1 | 2 | 94 AC19 and a rev bump of 92, each writing range tokens | 92 is CLOSED at the tip and 94 CLOSED at order 48, so both are frozen; 94 rev-4 holds no AC19 and settles its own S3 to S8 in its §3 |
| S2 | 4 | the exit-claim probe's population and floor, in a rev bump of 93 | spec text alone, in 93, CLOSED at the tip; its probe ran at its own close |
| S3 | 12 | the probe's matcher and staged break in 93, and 94 AC10 re-running 93 AC1's grep | 93 is CLOSED; 94 rev-4 holds no AC10 and is frozen before this unit builds |
| S4 | 9 | 90's loader sketch, 90 S4, 86 S21 and 88 S33 over a `need` argument, and 94 S10 and AC6 | `load_tree_lib` takes no argument, and 94 rev-4 §3 sets `need` out under 92 §8 F3 (c); 86, 88 and 90 are CLOSED; 94 S21 builds the any-exception catch and the every-name refusal at order 48 |
| S5 | 10 | 92's sketch calling the loader with `need=`, and `loop_witness.py` reading `GIT_ENV_LEAKS` through it | `tools/loop/loop_witness.py` carries the shared git-env-leaks block inline and calls no loader, as 92 rev-5 S8 states; 92 is CLOSED |
| S6 | 13 | the loader-result value-flow class in 94's route probe, and 94 AC3's staged helper | 94 rev-4 holds no route probe and no AC3, as 95 rev-3 §4 Evidence also reads |
| S7 | 14 | `need` keyword-only in `load_tree_lib`, and 94's probe grading positional and list forms | no `need` argument exists to make keyword-only, and 94 S21's sketch keeps the signature `load_tree_lib()` |
| S8 | 3 | 94's consumes-from 93 bullet citing ids 4, 11, 13, 20 and 29 | spec text alone, in 94, frozen before this unit builds; the two bullets keep their id sets as record |
| S9 | 5 | the skew row checking its copy in a fresh child process | built by 90 §8 F8 (a): the row runs `loop_lib.load_tree_lib()` in a `sys.executable -I` child with the copy's `loop/` first on its `sys.path`; the spec halves sit in the frozen 92 and 94; S14 observes it after order 48 |
| S10 | 15 | 94 AC18's half, the label printing after an in-process load | the row loads the real `tree_lib` in its own process before it starts the child, so every run of the plant is that observation; 94 rev-4 holds no AC18; S14 observes it after order 48 |
| S11 | 7 | 90's catch line and per-name loop, and 88 S33 naming any exception | as S4: 88 and 90 are CLOSED, and 94 S21 builds the idiom in code |
| S12 | 16 | the copied set as three sibling folders, priced from `du -sk` in 92 §5 and 94 §5 | the row copies two files, `loop_lib.py` and `tree_lib.py`, so no folder set is copied and no `du` price is owed; 92 and 94 are frozen |
| S13 | 17 | a refusal where the temp root sits inside the repository, a `TemporaryDirectory` with `ignore_cleanup_errors`, and a left-copy line | F6 (a): the row has no scratch root of its own, it writes under the `tempfile.mkdtemp` root of `run_budget_plant` that every plant shares, and the memory-tree kit's `remove_tree` already swallows an `OSError`, so a cleanup error ends in no `Traceback` |

- The high's mechanism: unit 95, at rev-3 an observation pass at order 49 that writes no code.
- A temp-root check for the loop kit's fixtures. Every `tools/loop/*.py` that creates a temp directory
  shares the case id 17 names, so a check in one plant gates one instance of the class (F6). The class is
  recorded at the close.
- The report's left-shift gates and checklist entries: each class is recorded at the close.
- A by-path load of `tree_lib`. 90 §8 F8 (a) chose the child process, and 94 rev-4 §4 rejects the
  by-path load because it moves how every caller imports.
- Cleanup after `SIGKILL`. No `finally` block runs then.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-95` — rev-3's observation pass, which writes no code: the two-name `TREE_LIB_SYMBOLS` and no `read_tree_conf`, the state that settles S4, S6 and S7 here (the round-11 spec audit's ids 1, 9, 13, 14)
- **consumes-from** `TOOL-dDeclaredLoop-94` — S21's `load_tree_lib` at order 48, whose refusal S14 observes through the skew row, and rev-4's §3 and §6, which hold no route probe, no `need` argument and no AC10, AC18 or AC19, settling S1, S3, S6, S7, S8 and S10 (the round-11 spec audit's ids 2, 3, 4, 5, 7, 9, 10, 12, 13, 14, 15, 16, 17)
- **consumes-from** `TOOL-dDeclaredLoop-93` — its exit-claim probe, AC1 and AC3, frozen at its close, which settle S2 and S3 (the round-11 spec audit's ids 3, 4, 12)
- **consumes-from** `TOOL-dDeclaredLoop-92` — rev-5's S8 and §8 F3 (c), the inline git-env-leaks block and no `need` argument, which settle S4, S5 and S7, and its frozen S3, S17, AC8, AC16 and §5, which settle S1, S9, S12 and S13's spec halves (the round-11 spec audit's ids 2, 5, 10, 16, 17)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4 and its loader sketch, frozen, which settle S4 and S11, and the skew row of its §8 F8 (a), which S14 observes (the round-11 spec audit's ids 7, 9)
- **consumes-from** `TOOL-dDeclaredLoop-88` — S33, frozen, which settles S4 and S11 (the round-11 spec audit's ids 7, 9)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S21, frozen, which settles S4 (the round-11 spec audit's id 9)
- **hands-off** `TOOL-dDeclaredLoop-100` — rev-3's §3, where S4, S6, S9, S12 and S13 and the route-probe and skew-row sketches that unit restates are settled, and §7, which that unit's re-ground reads (the round-12 spec audit's ids 5, 13, 15, 21, 22, 23, 24)

## 4. Design

### Write set

None under `tools/` and no sibling spec. The pass runs AC14 and AC15. The close's records and the build
README's regions are the main loop's and the generator's. The pass mints no public module-level `def`,
so `memory/map/generated/symbols.json` does not move.

### The skew row, as built (S14)

The pass observes this; it builds none of it.

```
mt   = parent folder of load_tree_lib().__file__        # the real tree_lib, loaded in this process
pair = <run_budget_plant's mkdtemp root>/skew
copy loop/loop_lib.py and memory-tree/tree_lib.py into pair, as siblings
append globals().pop("derive_constant_charges", None) to pair/memory-tree/tree_lib.py
run [sys.executable, "-I", "-c", probe, pair/loop]      # probe: sys.path.insert(0, argv[1]); loop_lib.load_tree_lib()
held where the child exits 1 naming derive_constant_charges and govkit update --kits memory-tree, no Traceback
remove_tree(<the mkdtemp root>) in run_budget_plant's finally
```

### The isolation probe (AC15)

```
import ast
t = ast.parse(open("budget.py", encoding="utf-8").read())
f = next(n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == "run_budget_plant")
calls = [n for n in ast.walk(f) if isinstance(n, ast.Call)]
load = [c.lineno for c in calls if ast.unparse(c.func) == "load_tree_lib"]
kid = [c.lineno for c in calls if ast.unparse(c.func) == "subprocess.run" and c.args
       and isinstance(c.args[0], ast.List)
       and [ast.unparse(e) for e in c.args[0].elts[:2]] == ["sys.executable", "'-I'"]]
print(bool(load and kid and min(load) < min(kid)))
```

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `5031e98fd`, its tree written by `git archive` into the run's
scratch directory, since this worktree is cut from main, which lacks the loop kit. The plant ran in that
extracted tree, and the staged break in a scratch copy of its `tools/loop/`, `tools/lib/` and
`tools/memory-tree/`. 95 rev-3 was read from the run's pending copy, since it is not on the branch yet.

- `tools/loop/loop_lib.py#TREE_LIB_SYMBOLS` holds `derive_docstring_ids` and `derive_constant_charges`.
  `tools/loop/loop_lib.py#load_tree_lib` takes no argument. It catches `LookupError`, then `ImportError`
  and `SyntaxError`, and refuses at the first missing name with `has no <name>` and the update command.
- `tools/loop/budget.py#run_budget_plant`, case `no-own-conf-read`, runs the sketch above. Its root is
  `tempfile.mkdtemp(prefix="loop-budget-")`, handed to `remove_tree` in the function's `finally`. Its
  check owes exit 1, the symbol, `govkit update --kits memory-tree` and no `Traceback`.
- `tools/loop/loop_witness.py#remove_tree` calls `tools/memory-tree/deviation_join.py#remove_tree`, which
  makes a refused path writable, deletes it again, and swallows any `OSError` left.
- 94 rev-4 S21 tests every name of the tuple and raises one refusal naming each missing name, and a
  module lacking one name gets the refusal text it gets at the tip. Its sketch keeps `load_tree_lib()`
  with no argument. Its §6 holds AC14, AC15 and AC16 alone, and its §3 holds no route probe and settles
  its own S24 on the built skew row.
- 95 rev-3 states no `read_tree_conf`, no `need` argument and the two-name tuple, and writes no code.
- The specs of units 86, 88, 90, 92 and 93 are CLOSED at the tip, and 94's is INPROGRESS at order 48.
- `python budget.py --fixture --plant no-own-conf-read` in `tools/loop/` exited 0. It printed the
  child's `exit 1` line naming `derive_constant_charges` and the update command, then `held`, in
  1.0 s PINNED wall time.
- Staged break: in a scratch copy whose `loop_lib.py` refusal reads `has no <name>` without the update
  command, the same plant exited 1 printing `MISSED`.
- §4's isolation probe printed `True` over `budget.py`.
- `grep -lE "tempfile\.(mkdtemp|TemporaryDirectory)" tools/loop/*.py | wc -l` printed 15, DERIVED, and
  `grep -rln gettempdir tools/loop/` printed nothing, so no loop fixture compares its temp root with the
  repository.

### Files touched (estimate)

None under `tools/`.

### Alternatives rejected

- **Rev bumps of the sibling specs, as rev-2 planned.** Each is CLOSED, or CLOSED before this unit builds,
  and a CLOSED spec is frozen.
- **Build S13's refusal in the skew row (F6).** The row holds no scratch root of its own, and the case is
  the class of every loop fixture's temp root.
- **Settle S14 with S1 to S13 and close the unit unbuilt (F7).** 94 S21 rewrites the refusal the row
  reads at order 48, after this re-ground.

## 5. Production-readiness checklist

- security — the skew row checks its copy in a fresh isolated child, so the parent's module state never
  answers for it; a temp root inside the repository is out under F6.
- perf / scale — one plant run and one `ast` probe, about 1.0 s PINNED 2026-11-17.
- error / empty / loading states — a skewed kit refuses by name in the child, which AC14 observes; a
  cleanup error is swallowed by `remove_tree`.
- observability — the plant's `exit 1` line and `held` are 90's; this pass reads them.
- risks — unit 100 restates rev-2's items and sketches, and units 97, 98 and 99 at order 50 write
  `loop_lib.py` and `budget.py`; the sweep below names each.
- testing — AC14 and AC15 as a plant run and a probe.
- migration — none: no stored data.
- user docs — none: no verb, flag or usage row is added. `grep -rln "no-own-conf-read" help/` prints
  `help/loop.md` alone at the tip, whose line names the `breakpoints.py` plant of that name, which this
  pass does not read.

### The sweep

The pass writes no file, so no function, constant or fixture moves. The readers below read this spec's
text, which the re-ground commit lands. Each count is DERIVED by the command beside it, run on the
branch tip.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| this spec's item and criterion ids | 100, DEFERRED, and the CLOSED 93, `grep -c "96 [SA][C0-9]" memory/builds/dDeclaredLoop/spec/*.md` | S1 to S13 and AC1 to AC13 keep their labels on §3's table, so each citation lands; 100 is re-grounded before its builder, and 93's text is frozen record |
| the edges naming this unit | eight bullets, seven hands-off from 86, 88, 90, 92, 93, 94 and 95 and one consumes-from from 100, `grep -n "^- \*\*[a-z-]*\*\* .TOOL-dDeclaredLoop-96. " memory/builds/dDeclaredLoop/spec/*.md` | rev-3 keeps the eight mirrored bullets, verbs, targets and id sets unchanged |
| the title | the units row of `memory/builds/dDeclaredLoop/README.md`, a generated region | the title is unchanged; the dispatcher's index regeneration renders rev-3 |
| this spec's positional rows | `memory/project/positional-refs.txt`, three rows naming this spec, `grep -c "dDeclaredLoop-96.md" memory/project/positional-refs.txt` | rev-3 keeps the `BUILD-METHOD M4` row in §1 and cites code by symbol only, so the two rows citing lines of `tools/check-spec-tokens.py` and `tools/memory-tree/row_grammar.py` go stale; the commit landing rev-3 runs `python tools/playbook/positional.py shrink` |
| the symbol tier | `memory/map/generated/symbols.json` | no def is minted, so no row moves |
| the `loop budget fixtures` leg | `tools/gate-legs.json`, whose argv runs `budget.py --selftest`, every plant, `no-own-conf-read` among them; its row in `tools/run-gates/selftest-budgets.txt` | the pass adds and moves no plant row and no budget |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the tip | no new function or constant name, so no `--suggest` run is owed |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files | the pass writes no shell script; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts, and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | it names no path under `memory/builds/` or `tools/loop/` |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps, help anchors and usage rows | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no shipped file, leg, step, verb or flag |

Order: this unit reads the skew row unit 90 built, CLOSED at the tip, and 94 S21's `load_tree_lib`,
which lands at order 48 as 94 rev-4 states it. Unit 95 at order 49 writes no code. Units 97 and 99 write
`tools/loop/loop_lib.py` and 98 writes `tools/loop/budget.py` at order 50, each re-grounded on its own;
where one lands before this pass, AC14 and AC15 run over its landed code, and a red there is that
unit's. Unit 100 at order 51 reads this rev.

## 6. Acceptance criteria

- **AC14** — When `python budget.py --fixture --plant no-own-conf-read` runs in `tools/loop/`, it exits 0.
  It prints a `tree_lib lacking derive_constant_charges · exit 1` line naming `derive_constant_charges`
  and `govkit update --kits memory-tree`, then `no-own-conf-read · held`, with no `Traceback`.
  Red when: the refusal of `load_tree_lib` loses its update command, staged in a scratch copy of
  `tools/loop/`, `tools/lib/` and `tools/memory-tree/` by cutting that command from its missing-name
  message, where the plant exits 1 printing `MISSED`.
  figure: 1.0 s PINNED wall time at the tip, 2026-11-17.
- **AC15** — When §4's isolation probe runs as `python -I -c` in `tools/loop/`, it prints `True`: inside
  `run_budget_plant`, a `load_tree_lib()` call sits on an earlier line than a `subprocess.run` call whose
  argument list opens with `sys.executable` and `"-I"`.
  Red when: the row checks the copy in the parent process, which already holds the real `tree_lib`, and
  the probe prints `False`.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg this pass keeps green, a leg in `tools/gate-legs.json` on the branch and absent from
main's: `loop budget fixtures`, which runs `budget.py --selftest`, the `no-own-conf-read` plant among its
plants. This pass adds and moves no arm: the skew row is 90's, and AC15 is a probe.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — Isolate the skew row's copy by a child process or by a path-keyed load (ids 5, 15)?** (a) a
  fresh child `python`; (b) `load_tree_lib` loading by path under a key naming the resolved directory.
  (b) changes the import of every caller to serve one row. 90 §8 F8 (a) built (a), which S14 observes.
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none
- **F3 — Keep the scratch copy out of the tree by a `dir=` or by a refusal (id 17)?** (a) a `dir=` under a
  chosen path outside the repository; (b) refuse by name where the temp root sits under the repository;
  (c) neither, as F6 settles. (a) picks a location for every adopter,
  and (b) gates one instance of a class. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F4 — Make `need` keyword-only, or read a positional argument as `need` (id 14)?** (a) keyword-only;
  (b) the probe reads the first positional argument as `need`; (c) neither, since `load_tree_lib` takes
  no argument under 92 §8 F3 (c) and 94 rev-4 holds no probe. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F5 — Which side of the 93 and 94 edge moves (id 3)?** (a) 94's bullet cites ids 4, 11, 13, 20 and 29;
  (b) 93's bullet cites id 11 alone; (c) neither, since 93 is CLOSED and 94 is frozen before this unit
  builds. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F6 — With the row writing under the shared plant root, what does S13 build (id 17)?** (a) nothing: S13
  leaves the scope, and the class, a loop fixture's temp root inside the repository, is recorded at the
  close; (b) a refusal in `run_budget_plant` for every budget plant; (c) one temp-root check in
  `loop_lib.py` that every loop fixture calls. (b) gates one file of the 15 that create a temp directory
  (§4 Evidence). (c) is a second mechanism across the kit, a unit of its own under M2. The report graded
  id 17 LOW, with nothing falsely certified or lost, and its cleanup half holds through `remove_tree`.
  Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none
- **F7 — With S1 to S13 settled at the tip, does the unit still build?** (a) yes, as an observation pass at
  order 50 that writes no file and closes on AC14 and AC15; (b) settle S14 too and close the unit
  unbuilt. 94 S21 rewrites the refusal the skew row reads at order 48, after this re-ground, and the run
  keeps this unit's order and status. Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-11 spec audit's 13 minors batched (7 MEDIUM, 6 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 to S13 S14 AC14 AC15 · re-grounded on the code at
  `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-96-2-spec-writer: S1
  to S13 settled in §3, every sibling spec frozen and no `need` argument; S14 observes the skew row after
  94 S21; AC1 to AC13 leave with their items and AC14 and AC15 are new; the eight Edges bullets kept
  with their payloads re-worded; §5's sweep added; every fork re-marked, F3 to F5 gaining option (c),
  and F6 and F7 added.

## 10. Reuse audit

The seam is the `no-own-conf-read` case of `tools/loop/budget.py#run_budget_plant`, 90's skew row,
observed in place over `tools/loop/loop_lib.py#load_tree_lib`. No row, probe or checker is minted.
`python tools/codebase-map/reuse_lookup.py "check a skewed kit copy in a fresh child process outside the repository"`,
run on the branch tip 2026-11-17, ranked `check`, `resolve_kit_dir`, `kit_rel`, `checks`, `kit_dir` and
`read_policy_kit`. `resolve_kit_dir` is the locator `read_memory_tree` already calls, and none of the
others checks a kit copy in a child, so no existing seam fits a second isolation and the row stays 90's.

Recall terms used: skew row no-own-conf-read load_tree_lib TREE_LIB_SYMBOLS child process scratch root temp root remove_tree observation pass minors batch
