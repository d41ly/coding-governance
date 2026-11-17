# TOOL-dDeclaredLoop-100 — the round-12 spec audit's 21 minors, batched

**Status:** DEFERRED · rev-2 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 51 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-100-deviation-1001.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-100-deviation-1001.md) | deviation | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-100-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-100-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-100-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-100-reground-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
exited CONVERGED with 24 confirmed findings over units 95 and 96, the round-11 promotions. Its three
highs, ids 1, 11 and 19, share item H1 and are units 97, 98 and 99. This unit is the batch
BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW. Each finding keeps its report id and its
own scope item, including where the report merged ids into one item.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M2 | MEDIUM | 14 | S2 |
| M3 | MEDIUM | 3 | S3 |
| M4 | MEDIUM | 4 | S4 |
| M5 | MEDIUM | 8 | S5 |
| M6 | MEDIUM | 10 | S6 |
| M7 | MEDIUM | 20 | S7 |
| M8 | MEDIUM | 15, 21 | S8, S9 |
| M9 | MEDIUM | 22 | S10 |
| M10 | MEDIUM | 23 | S11 |
| L1 | LOW | 5 | S12 |
| L2 | LOW | 6, 12 | S13, S14 |
| L3 | LOW | 13 | S15 |
| L4 | LOW | 7 | S16 |
| L5 | LOW | 16 | S17 |
| L6 | LOW | 18 | S18 |
| L7 | LOW | 24 | S19 |
| L8 | LOW | 17, 25 | S20, S21 |

The report's one refuted finding, id 9, duplicated id 6 and is not in the disposal population.

At rev-2 none of S1 to S21 has anything left to build. Each spec text they amend sits in a spec that
is CLOSED at the branch tip, or in 96's, which closes at order 50 before this unit builds, so frozen.
Each code half rests on a `read_tree_conf`, a `need` argument, a four-name tuple or a scratch-root
check, none of which exists at the tip, or is built already. §3 names each item with its evidence. The
item ids and the criterion ids AC1 to AC21 keep their labels on §3's table, so a sibling's citation of
them still lands.

What this unit still owes is S22, the observation that the tuple-coverage claim of ids 3, 8 and 25
holds once 97 and 99 have written `tools/loop/loop_lib.py` at order 50. The pass writes no file of the
tree. It builds at order 51, after every other unit, and closes on AC22.

## 2. Scope (IN)

- **S22** — ids 3, 8 and 25, observed at this unit's pass, after 97 and 99 write
  `tools/loop/loop_lib.py` at order 50. `TREE_LIB_SYMBOLS` there still holds `derive_docstring_ids`
  and `derive_constant_charges`. Every attribute `loop_lib.py` reads on a loader result, a
  `load_tree_lib()` call or a name bound from one in the same function body, is a member of that
  tuple, as 90 AC4 collects it and 95 AC8 observed it at order 49. No code moves in this pass.
  Observed by AC22.

## 3. Non-goals (OUT)

- **S1 to S21, settled at the tip.** Each was read on the branch tip §4 Evidence names. Their criteria,
  AC1 to AC21, leave the scope with them; AC22 is a new label.

| Item | Id | Rev-1 ordered | Settled because |
|---|---|---|---|
| S1 | 2 | 41 §5's no-conf and no-kit rule, in a rev bump of 41 | 41 is CLOSED at rev-5, so frozen; 95 rev-3 §3 settles the no-kit clause on the `requires` list of `tools/loop/kit.toml` (its S4) |
| S2 | 14 | 41 S1, 60 S2 and 64 S1 reading `MEMORY_ROOT` through `read_tree_conf` | no `read_tree_conf` exists: the loop kit reads the conf through `read_design_conf` itself, in `read_builds_dir` and `resolve_memory_root_source` (95 rev-3 §3, its S2 and S3); 41, 60 and 64 are CLOSED |
| S3 | 3 | 90 S4's tuple with four members, 94 S10 losing `three-name`, and 94 AC1 naming `parse_conf` | `TREE_LIB_SYMBOLS` holds two names and 95 rev-3 §3 settles `parse_conf` as a member (its S1); 90 and 94 are CLOSED |
| S4 | 4 | 94 AC18 grepping `du -sk`, and 92 §5 and 94 §5 without `3.3 MB` | 92 and 94 are CLOSED; 92 rev-5 holds no `3.3 MB`, 94 rev-4 holds no AC18, and 96 rev-3 §3 settles its S12: the skew row copies two files, so no `du` price is owed |
| S5 | 8 | 95 §4 Evidence saying 90 AC4 matches any receiver, and 95's sketch with no `.read_text` | 90 rev-6 AC4 collects attributes read on a loader result alone, so the `read_text` calls of `derive_conf_constants`, `derive_conf_reads`, `read_actor_rows` and `resolve_kit_dir` on a path are outside it; 95 is CLOSED and holds no conf-read sketch |
| S6 | 10 | `read_tree_conf` decoding the conf as `read_design_conf` does | no `read_tree_conf` exists; every loop read of the conf is `read_design_conf`'s own utf-8 read with replacement and folded line endings |
| S7 | 20 | a named refusal where `read_tree_conf` cannot read an existing conf | no `read_tree_conf` exists; `read_design_conf` tests `is_file`, so a directory of that name reads as `{}`; the permission-denied case on the real readers is F5 |
| S8 | 15 | the skew row's `git rev-parse --show-toplevel` and its `no repository` line | the built row runs no git call: it writes under the `tempfile.mkdtemp` root of `run_budget_plant`, and 96 rev-3 §8 F6 (a) sets the temp-root check out of scope |
| S9 | 21 | `_is_under` for the skew row's scratch-root check | as S8: no scratch-root check exists to define containment for (96 rev-3 §8 F3 (c) and F6 (a)) |
| S10 | 22 | the skew row passing only on a non-zero exit naming the symbol and the command, with no `Traceback` | built by 90 §8 F8 (a): the row's check owes exit 1, `derive_constant_charges` and `govkit update --kits memory-tree` in the child's stdout, and no `Traceback` in either stream; 96 S14 observes it at order 50 |
| S11 | 23 | a nested-scope class in 94's route probe | 94 rev-4 holds no route probe (96 rev-3 §3, its S6) |
| S12 | 5 | 96 S4 spelling a `grep -cF`, and 94 S10 naming three sites | spec text alone, in the CLOSED 94 and in 96 rev-3, whose §3 settles its S4 |
| S13 | 6 | 95 AC4 also running the `confs-disagree` plant of `breakpoints.py` over S6's read | no read moves, since S6 and S7 build nothing; 95 rev-3 holds no AC4; 72 AC3's plants stay in `budget.py` and `breakpoints.py` as 72 built them |
| S14 | 12 | 95 §7 and this unit's §7 naming the breakpoint leg | 95 is CLOSED; this pass writes no file, so it trips no loop leg's guard |
| S15 | 13 | 96 §7 naming the breakpoint and definition legs | 96 rev-3 writes no code, and its §7 names `loop budget fixtures`, the leg that runs the row it observes |
| S16 | 7 | 95 AC5's fixture note on a receipt | 95 is CLOSED and its rev-3 holds no AC5 |
| S17 | 16 | 94 S24, AC18 and its sketch stating `ignore_cleanup_errors=True` | 94 is CLOSED and its rev-4 §3 settles S24 on the built row; the plant's cleanup is `remove_tree` in the `finally` of `run_budget_plant` (96 rev-3 §3, its S13) |
| S18 | 18 | 92's sketch defining `load_tree_lib` with a `need` keyword | `load_tree_lib` takes no argument under 92 §8 F3 (c); 92 is CLOSED |
| S19 | 24 | the skew row taking its loop folder from the loaded `loop_lib` and copying a `lib/` folder where one sits beside it | the row copies `loop_lib.py` from `KIT`, the folder of `budget.py`, and `tree_lib.py` from the folder of the loaded `tree_lib`, and copies no `lib/`: `loop_lib.py` carries `resolve_kit_dir` inline, and the plant prints `held` over that two-file copy (§4 Evidence) |
| S20 | 17 | 92 §5 pricing at most four attributes per call | 92 is CLOSED and its rev-5 holds no `three attributes` line |
| S21 | 25 | 90 AC4 naming `parse_conf` beside the other members | 90 is CLOSED, and `parse_conf` is no member (95 rev-3 §3, its S1) |

- The high's mechanisms: `CONF_READERS` and the rule reading it (97), the `declared readers seen` row of the `conf-read-forms` plant (98)
  and the `conf-readers-declared` plant (99), each at order 50.
- A refusal for an existing conf that cannot be read, on `read_design_conf` or on the driver-conf read
  of `resolve_memory_root_source` (F5). The class is recorded at the close.
- The report's left-shift gates and checklist entries. Each class is recorded at the close.
- Rev bumps of the sibling specs, as rev-1 planned. Every target is CLOSED, or CLOSED before this unit
  builds, and a CLOSED spec is frozen.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-95` — rev-3's §3 and AC8, which settle S2, S3, S5, S6, S13, S16 and S21 on `read_design_conf` and the two-name tuple, and whose collection S22 re-runs (the round-12 spec audit's ids 6, 7, 8, 10, 12, 20)
- **consumes-from** `TOOL-dDeclaredLoop-96` — rev-3's §3, §7 and S14, which settle S4, S8, S9, S10, S11, S12, S15, S17 and S19 on the skew row as built (the round-12 spec audit's ids 5, 13, 15, 21, 22, 23, 24)
- **consumes-from** `TOOL-dDeclaredLoop-94` — rev-4's §3 and §6, which hold no route probe and no AC1 or AC18, settling S3, S4, S11, S12 and S17 (the round-12 spec audit's ids 3, 4, 5, 16, 23)
- **consumes-from** `TOOL-dDeclaredLoop-92` — rev-5's §5 and §8 F3 (c), with no `need` argument, settling S4, S18 and S20 (the round-12 spec audit's ids 4, 17, 18)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4's two-name tuple, AC4's collection over loader results, which S22 re-runs, and the skew row of its §8 F8 (a), settling S3, S5, S10 and S21 (the round-12 spec audit's ids 3, 15, 25)
- **consumes-from** `TOOL-dDeclaredLoop-72` — AC3's `confs-disagree` plants, unchanged, settling S13 (the round-12 spec audit's id 6)
- **consumes-from** `TOOL-dDeclaredLoop-64` — S1's route clause, frozen at its close, settling S2 (the round-12 spec audit's id 14)
- **consumes-from** `TOOL-dDeclaredLoop-60` — S2's route clause, frozen at its close, settling S2 (the round-12 spec audit's id 14)
- **consumes-from** `TOOL-dDeclaredLoop-41` — S1 and §5, frozen at its close, settling S1 and S2 (the round-12 spec audit's ids 2, 14)
- **consumes-from** `TOOL-dDeclaredLoop-99` — its write of `loop_lib.py` at order 50, the file S22's collection reads after it (the round-12 spec audit's ids 10, 19, 20)

## 4. Design

### Write set

None under `tools/` and no sibling spec. The pass runs AC22. The close's records and the build
README's regions are the main loop's and the generator's. The pass mints no public module-level `def`,
so `memory/map/generated/symbols.json` does not move.

### The collection probe (AC22)

The pass observes this; it builds none of it. It is 90 AC4's collection as 95 AC8 ran it, taking the
file to parse and the folder to import `loop_lib` from as its two arguments.

```
import ast, sys
t = ast.parse(open(sys.argv[1], encoding="utf-8").read())
is_load = lambda n: isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "load_tree_lib"
got = set()
for f in ast.walk(t):
    if not isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)):
        continue
    bound = set()
    for n in ast.walk(f):
        if isinstance(n, ast.Assign):
            for tg in n.targets:
                if is_load(n.value) and isinstance(tg, ast.Name):
                    bound.add(tg.id)
                if isinstance(tg, ast.Tuple) and isinstance(n.value, ast.Tuple):
                    bound |= {a.id for a, b in zip(tg.elts, n.value.elts) if is_load(b) and isinstance(a, ast.Name)}
    for n in ast.walk(f):
        if isinstance(n, ast.Attribute) and not n.attr.startswith("__") and (
                is_load(n.value) or (isinstance(n.value, ast.Name) and n.value.id in bound)):
            got.add(n.attr)
sys.path.insert(0, sys.argv[2])
import loop_lib
print(sorted(got), got <= set(loop_lib.TREE_LIB_SYMBOLS), loop_lib.TREE_LIB_SYMBOLS)
```

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `e9e356424`, its tree written by `git archive` into the
run's scratch directory, since this worktree is cut from main, which lacks the loop kit. The plant and
the probe ran in that extracted tree, and the staged break over a scratch copy of its `loop_lib.py`.

- `tools/loop/loop_lib.py#TREE_LIB_SYMBOLS` holds `derive_docstring_ids` and `derive_constant_charges`.
  `tools/loop/loop_lib.py#load_tree_lib` takes no argument, and no `read_tree_conf` and no `_is_under`
  is defined under `tools/loop/`.
- `tools/loop/loop_lib.py#read_builds_dir` and `tools/loop/loop_lib.py#resolve_memory_root_source` each
  call `read_design_conf`, which `tools/memory-tree/design_lib.py#read_design_conf` defines: `{}` where
  `is_file` is false, else `parse_conf` of the bytes decoded utf-8 with replacement, CRLF folded. It
  catches no `OSError`.
- `tools/loop/loop_lib.py#derive_conf_constants`, `#derive_conf_reads`, `#read_actor_rows` and
  `#resolve_kit_dir` call `read_text` on a path, never on a loader result.
- `tools/loop/budget.py#run_budget_plant`, case `no-own-conf-read`, copies `loop_lib.py` from `KIT` and
  `tree_lib.py` from the folder of the loaded `tree_lib` under its `tempfile.mkdtemp` root, runs a
  `sys.executable -I` child, and owes exit 1, `derive_constant_charges` and the update command in the
  child's stdout, and no `Traceback`. Its `finally` hands the root to `remove_tree`. It runs no
  `git rev-parse --show-toplevel`.
- `tools/loop/kit.toml` declares `requires = ["memory-tree", "run-gates"]`.
- `python budget.py --fixture --plant no-own-conf-read` in `tools/loop/` exited 0 and printed the
  child's `exit 1` line naming `derive_constant_charges` and `govkit update --kits memory-tree`, then
  `held`, in 0.95 s PINNED wall time.
- §4's collection probe, run as `python -I` in `tools/loop/` over `loop_lib.py`, printed
  `['derive_constant_charges', 'derive_docstring_ids'] True ('derive_docstring_ids', 'derive_constant_charges')`.
  Over a scratch copy with `def fx_conf(t): return load_tree_lib().parse_conf(t, {})` appended, it
  printed `parse_conf` in the list and `False`.
- The specs of units 41, 60, 64, 72, 90, 92, 94 and 95 are CLOSED at the tip, 96 is INPROGRESS at
  order 50, and 97, 98 and 99 are DEFERRED at order 50.
- `tools/gate-legs.json` names the legs `loop budget fixtures`, `loop breakpoint fixtures` and
  `loop definition fixtures`.

### Files touched (estimate)

None under `tools/`.

### Alternatives rejected

- **Rev bumps of the sibling specs, as rev-1 planned.** Each is CLOSED, or CLOSED before this unit
  builds, and a CLOSED spec is frozen.
- **Build `read_tree_conf` and harden it (S5 to S7).** 95 rev-3 §8 settles the loop kit on
  `read_design_conf`, so a wrapper is a layer no caller needs.
- **Settle S22 with S1 to S21 and close the unit unbuilt (F4).** 97 and 99 rewrite `loop_lib.py` at
  order 50, after 95 AC8's observation, and no leg reads the collection.

## 5. Production-readiness checklist

- security — no grant moves; the tuple keeps an older memory-tree kit refusing by name for every
  `tree_lib` name the loop kit reads, which AC22 observes.
- perf / scale — one `ast` probe, well under a second.
- error / empty / loading states — an unreadable existing conf is F5's class, out of scope; a
  directory named as the conf reads as `{}` through `is_file`.
- observability — the probe prints the collected set, the verdict and the tuple.
- risks — units 97 and 99 write `loop_lib.py` at order 50, and 98 writes `budget.py`; the sweep below
  names each.
- testing — AC22 as a probe with a staged break.
- migration — none: no stored data.
- user docs — none: no verb, flag or usage row is added.

### The sweep

The pass writes no file, so no function, constant or fixture moves. The readers below read this spec's
text, which the re-ground commit lands. Each count is DERIVED by the command beside it, run on the
branch tip.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| this spec's item, criterion and fork ids | the CLOSED 90 and the DEFERRED 99, two lines each, `grep -c "100 [SA][C0-9]\|100 rev-1" memory/builds/dDeclaredLoop/spec/*.md` | S1 to S21, AC1 to AC21 and F1 to F3 keep their labels, on §3's table and in §8, so each citation lands; 90's text is frozen record, and 99's rows describe its own build, which reads none of them |
| the edges naming this unit | ten hands-off bullets from 41, 60, 64, 72, 90, 92, 94, 95, 96 and 99, `grep -n "^- \*\*[a-z-]*\*\* .TOOL-dDeclaredLoop-100. " memory/builds/dDeclaredLoop/spec/*.md` | rev-2 keeps the ten mirrored consumes-from bullets, verbs, targets and id sets unchanged |
| 98's sweep naming this unit's write of `budget.py` | the DEFERRED 98's §5, `grep -n "100 at order 51" memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-98.md` | rev-2 writes no `budget.py` line, so 98 builds with no neighbour in that file at order 51 |
| the title | the units row of `memory/builds/dDeclaredLoop/README.md`, a generated region | the title is unchanged; the dispatcher's index regeneration renders rev-2 |
| this spec's positional rows | `memory/project/positional-refs.txt`, ten rows naming this spec, `grep -c "dDeclaredLoop-100.md" memory/project/positional-refs.txt` | rev-2 keeps the `BUILD-METHOD M2` and `BUILD-METHOD M4` rows and cites code by symbol only, so the eight rows citing code lines go stale; the commit landing rev-2 runs `python tools/playbook/positional.py shrink` |
| the symbol tier | `memory/map/generated/symbols.json` | no def is minted, so no row moves |
| the loop legs | `loop definition fixtures`, `loop budget fixtures` and `loop breakpoint fixtures` in `tools/gate-legs.json` | the pass adds and moves no plant, row or budget |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the tip | no new function or constant name, so no `--suggest` run is owed |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files | the pass writes no shell script; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts, and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md`, `grep "^watch:" memory/guides/SESSION-KICKOFF.md \| grep -c "memory/builds\|tools/loop"` printing 0 | it names no path this pass reads or writes |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps, help anchors and usage rows | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no shipped file, leg, step, verb or flag |

Order: this unit reads `TREE_LIB_SYMBOLS` and `load_tree_lib` as 94 S21 left them at order 48, and 95
rev-3 at order 49 wrote no code. At order 50, 97 rev-2 writes `CONF_READERS` into `loop_lib.py`, 99 rev-2
writes `CONF_ROUTES`, `derive_conf_openers` and its plant there, 98 rev-2 writes `budget.py`, and 96
rev-3 writes nothing. AC22 runs over the `loop_lib.py` they leave; a red there is the order-50 unit's
whose write added the loader-result read.

## 6. Acceptance criteria

- **AC22** — When §4's collection probe runs as `python -I -c` in `tools/loop/` with the arguments
  `loop_lib.py` and `.`, it prints a sorted list, then `True`, then the tuple
  `('derive_docstring_ids', 'derive_constant_charges')`.
  Red when: a loader result is read for a name outside the tuple, staged in a scratch copy of
  `loop_lib.py` with `def fx_conf(t): return load_tree_lib().parse_conf(t, {})` appended, where the
  list holds `parse_conf` and the verdict prints `False`.
  figure: the list is DERIVED at observation time; at the tip it held the two members, PINNED 2026-11-17.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The pass writes no file, so it trips no loop leg's guard. This pass adds and moves no arm: AC22 is a
probe.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — Rewrite 60 S2 and 64 S1, or let their cite resolve to the amended 41 S1 (id 14)?** (a) rev
  bumps of 60 and 64; (b) record that the cite resolves; (c) neither, since 41, 60 and 64 are CLOSED
  and no `read_tree_conf` exists for them to name. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F3 — Fix 90 AC4 against `read_text` by changing the read or by narrowing the probe (id 8)?** (a)
  `loop_lib.py` makes no `.read_text` attribute read; (b) 90 AC4's population narrows to attributes on a
  loader result; (c) neither, since 90 rev-6 AC4 already collects loader results alone and no
  `read_tree_conf` exists. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F4 — With S1 to S21 settled at the tip, does the unit still build?** (a) yes, as an observation pass
  at order 51 that writes no file and closes on AC22; (b) settle S22 too and close the unit unbuilt. 97
  and 99 rewrite `loop_lib.py` at order 50, after 95 AC8's observation, no leg reads the collection,
  and the run keeps this unit's order and status. Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none
- **F5 — With no `read_tree_conf`, where does id 20's unreadable conf land?** (a) nowhere in this unit:
  the class, an existing conf that raises `OSError` on read, is recorded at the close; (b) a named
  refusal in `read_design_conf`; (c) one in `resolve_memory_root_source`. A directory of that name
  already reads as `{}` through `is_file`. (b) changes the memory-tree kit's one reader for every
  caller, a second mechanism under BUILD-METHOD M2, and (c) gates one caller of a class. Recommendation:
  (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-12 spec audit's 21 minors batched (11 MEDIUM, 10 LOW).
- rev-2 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 to S21 S22 AC22 · re-grounded on the code at
  `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-100-1-spec-writer:
  S1 to S21 settled in §3, every sibling spec frozen and no `read_tree_conf`, `need` argument, four-name
  tuple or scratch-root check; S22 observes the tuple's coverage after order 50; AC1 to AC21 leave with
  their items and AC22 is new; the ten Edges bullets kept with their payloads re-worded; §5's sweep
  added; F1 to F3 re-marked, F2 and F3 gaining option (c), and F4 and F5 added.

## 10. Reuse audit

The seam is 90 AC4's collection over `tools/loop/loop_lib.py`, as 95 AC8 ran it, observed in place over
`tools/loop/loop_lib.py#TREE_LIB_SYMBOLS`. No row, probe or checker is minted.
`python tools/codebase-map/reuse_lookup.py "collect the attribute names read on a loaded module result and compare them with a declared tuple"`,
run on the branch tip 2026-11-17, ranked `read_text`, `read`, `read_bytes`, `load`, `load_conf` and
`read_git` first, with `read_memory_tree` and `read_design_conf` below. None collects attributes read on
a loaded module, so no existing seam fits a second collector and the probe stays 90's.

Recall terms used: TREE_LIB_SYMBOLS load_tree_lib loader result attribute collection read_design_conf read_tree_conf skew row observation pass minors batch
