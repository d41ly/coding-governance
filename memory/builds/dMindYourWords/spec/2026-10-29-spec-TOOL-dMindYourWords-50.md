# TOOL-dMindYourWords-50 — the kit refuses any git spawn of its own that bypasses the pinned runner

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, item H3. TOOL-dMindYourWords-31 AC3 observes the pin with `git grep -h -c --
'--no-replace-objects'`, which lists only files that match and drops their names: it prints nothing at
base, so "a nonzero count for each file it lists" holds when every flag is gone, and it cannot see one
reader losing its flag while another in the same file keeps it. Its §7 arm covers only the drift
blame. A builder who drops the pin from any other reader passes every criterion. This unit replaces
that observation with a per-call-site self-check of the kit: every git spawn either goes through
`run_git` or belongs to a declared set of reads no graft can change, and anything else reds the kit's
own run.

## 2. Scope (IN)

- **S1** — The inventory. `check_history_pins(kit_dir)` in `tools/lexicon/lexicon.py` walks the modules
  `read_kit_modules` (TOOL-dMindYourWords-46 S1) returns, `selftest.py` excluded, and judges every call
  of `subprocess.run`, `subprocess.check_output` or `subprocess.Popen` whose first argument is a list or
  tuple literal opening with the string `"git"`. A call inside the body of `run_git` is the runner and
  is admitted. Any other call is admitted only when its first subcommand, read past `-C <dir>` and `-c
  <k=v>`, is a literal in the declared set `NON_HISTORY_GIT`: `ls-files`, or `rev-parse` whose other
  elements are all literals among `--show-toplevel`, `--git-dir`, `--is-shallow-repository`. A starred
  or computed subcommand is not admitted. Each refused call is a problem naming its file, line and
  function. Observed by AC1 and AC2.
- **S2** — The carried blocks named, not judged. A call between a `# >>> <name>` and `# <<< <name>`
  marker pair, a byte-identical block carried from `tools/lib/` and graded by its parity row, is not
  judged; the population line names each such block, so the gap is printed rather than silent.
  Observed by AC3.
- **S3** — Where it runs and what it prints. The measurement pass calls `check_history_pins()` beside
  `check_self_containment()` (`tools/lexicon/lexicon.py:2867`), extends `problems` with its refusals,
  and a walk that judges zero spawns reds `history pins: DEAD PROBE`. Observed by AC2.
- **S4** — The residue moved. Any spawn S1 refuses on the tree at this pass, one minted by a unit of
  this build that units 47 to 49 did not name, is moved onto `run_git` in this pass. Observed by AC2.

## 3. Non-goals (OUT)

- The runner and the readers units 47, 48 and 49 move: those units.
- A shell string, `os.system`, an argv assembled at run time and passed by name, and every
  `selftest.py` spawn: S1 reads literals in the shipped modules and says so in its docstring.
- Re-wording unit 31's AC3: a confirmed finding is not folded (BUILD-METHOD M4); this unit is the
  observation that replaces it.
- The per-file population line and the spec-lint rule the report names under H3: the first is review
  id 25 in the minors batch TOOL-dMindYourWords-52, the second a gate of its own (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-46` — `read_kit_modules`, the walk S1 reads
- **consumes-from** `TOOL-dMindYourWords-47` — `run_git`, the one body inside which S1 admits a history spawn
- **consumes-from** `TOOL-dMindYourWords-48` — the merge-loss guard, the signals, the rename map and the index read, moved onto the runner before S3's first run
- **consumes-from** `TOOL-dMindYourWords-49` — the merge walk and the branch walk, moved onto the runner before S3's first run
- **hands-off** `TOOL-dMindYourWords-52` — `check_history_pins`, whose population line the batch names per file (id 25) and over which it observes the spawns it adds (id 9)

## 4. Design

### Evidence

- Unit 31 AC3: `git grep -h -c -- '--no-replace-objects' -- tools/lexicon/lexicon.py
  tools/lexicon/lexicon_conf.py` "prints a nonzero count for each file it lists"; re-run at base by the
  report it printed nothing and exited 1 (`spec/2026-10-29-spec-TOOL-dMindYourWords-31.md` AC3, review
  ids 2 and 25).
- At base the kit spawns git at `tools/lexicon/lexicon.py:411` (`ls-files`), `:4129` (`ls-tree`),
  `:4145` (`cat-file --batch`), `:4197` (a starred lambda), `:4347` (`-C <dir> rev-parse
  --show-toplevel`), `:4406` (`rev-parse --show-toplevel`) and `tools/lexicon/scaffold_lexicon.py:207`
  (`rev-parse --show-toplevel`); S1 admits the first, fifth, sixth and seventh by `NON_HISTORY_GIT` and
  refuses the rest until units 47 and 48 move them.
- `check_self_containment` is the kit's AST self-check in the measurement pass, with the `DEAD PROBE`
  token for a zero population (`tools/lexicon/lexicon.py:2359`, `:2867`).
- Unit 26 reads the compare base through `tools/lexicon/coverage_join.py`'s copy of
  `resolve_compare_base` (`spec/2026-10-29-spec-TOOL-dMindYourWords-26.md` §10), whose canonical is
  `tools/lib/compare_base.py`, and `tools/lib/resolve-python.test.sh` holds every `# >>> compare_base_py`
  carrier to it; where that copy is carried as such a block, S2 names it rather than judging code the
  kit may not edit.

### The rule

```
for path, tree in read_kit_modules(kit_dir):                 # selftest.py excluded
    for call in git_spawns(tree):                            # subprocess.run/check_output/Popen, ["git", ...]
        if inside(call, "run_git") or inside_carried_block(call): continue
        sub = first_subcommand(call)                         # past -C <dir> and -c <k=v>; None if computed
        if sub in NON_HISTORY_GIT and its other elements are admitted: continue
        problems.append(f"{path.name}:{call.lineno} in {func}: a git spawn outside run_git ...")
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_history_pins` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest check_history_pins --as py.function` answered `OK` at writing |
| `NON_HISTORY_GIT` | constant, `tools/lexicon/lexicon.py` | none; `lexicon.py --suggest NON_HISTORY_GIT --as py.constant` answered that `py.constant` is UNDECLARED at writing |
| `history pins: DEAD PROBE` | refusal line | none |

### Rollout

Live at landing, last of the order-21 group by id, so every reader units 47 to 49 move is on the runner
before its first run.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, S3, S4
- `tools/lexicon/lexicon_conf.py` and `tools/lexicon/lexicon_signals.py`: S4, where a residue spawn sits
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **A per-file count of `--no-replace-objects` against a count of spawns**, the report's lighter
  route: it reads text, and a reader whose flag moved into a comment counts as pinned.
- **A selftest arm**: it runs only under `GATE_SELFTESTS`; the self-check runs on every `lexicon naming
  predicates` bar and in every adopter's install.
- **Admitting a spawn by an allow-comment at the call**: a waiver one keystroke from every reader, the
  shape deny-by-default exists to refuse.

## 5. Production-readiness checklist

- security — deny by default over the kit's own spawns: a history read is pinned or the kit's run
  reds.
- perf / scale — one pass over parse trees the walk already produces.
- error / empty / loading states — an unparseable module is UNJUDGED as in `check_self_containment`; a
  zero population is `DEAD PROBE`.
- observability — each refusal names file, line and function; S2 names each block it did not judge.
- risks — a future non-history read (`git config`, `git check-ignore`) reds until `NON_HISTORY_GIT`
  admits it in a commit that says why; that is the cost of deny by default.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — the kit's self-check, reported like `check_self_containment`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, pathlib; sys.path.insert(0, 'tools/lexicon'); import lexicon;
  print(lexicon.check_history_pins(pathlib.Path(sys.argv[1])))" <copy>` runs on a scratch copy of
  `tools/lexicon/*.py` in which `read_defs_at_sha`'s `run_git(root, "ls-tree", …)` is rewritten as
  `subprocess.run(["git", "ls-tree", …])`, it prints a problem naming `lexicon.py`, that line and
  `read_defs_at_sha`.
  Red when: a reader that lost its pin passes the check, the case unit 31 AC3 could not see.
  fixture: the copy under the run's scratch directory.
- **AC2** — When the same call runs on `tools/lexicon` itself after the pass, it prints no problem and
  a judged count of at least 5.
  Red when: a spawn of the kit bypasses the runner, or the walk judged nothing.
  figure: DERIVED at observation; at least the five spawns §4 lists at base, more as units of this build
  add readers.
- **AC3** — When a scratch copy carries a `subprocess.run(["git", "merge-base", …])` between `# >>>
  compare_base_py` and `# <<< compare_base_py` markers, the call returns no problem for it and its
  population line names `compare_base_py`.
  Red when: a carried block is judged as kit code, or skipped without being named.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC3 · a kit copy with one reader's spawn unrouted and one carried block, its failing case the `inside(call, "run_git")` test made always true, under which the unrouted reader passes · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 2 (HIGH, item H3) of the round-1 audit of
  units 30 to 37.

## 10. Reuse audit

The seam is `check_self_containment` (`tools/lexicon/lexicon.py:2359`), the kit's AST self-check in the
measurement pass, through the walk TOOL-dMindYourWords-46 extracts as `read_kit_modules`; the class it
judges is TOOL-dMindYourWords-47's runner. `python tools/codebase-map/reuse_lookup.py "route every git
history read through one pinned spawn helper"` ranked `run_git`, `read_git_output` and `build_git_env`,
and no inventory of git spawns exists in any kit, so this check is minted on the existing walk.

Recall terms used: `python tools/memory-recall/query.py "how does a kit hold every git history read to the replace and graft pin as a class rather than a list" --terms "graft replace no-replace-objects pinned reader run_git build_git_env inventory spawn class history"`
