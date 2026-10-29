# TOOL-dMindYourWords-46 — the kit refuses any added-set argv of its own that drops the rename rule

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 29 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dMindYourWords-43), 16 (TOOL-dMindYourWords-44) and 23
(TOOL-dMindYourWords-45). The finding reproduced the rename bypass on a second spelling of an added-set
read, three orders after the unit that closed it on the first. Units 43 and 44 fix the two spellings
that exist; nothing stops the next one. This unit adds the left-shift the report names for H1 as a
self-check of the kit, beside `check_self_containment`: any argv the kit spells with `--diff-filter=A`
must carry the rename rule, or the kit's own run reds.

## 2. Scope (IN)

- **S1** — The walker, extracted. `read_kit_modules(kit_dir)` in `tools/lexicon/lexicon.py` returns
  `[(path, tree_or_error)]` for every `*.py` beside the engine, the walk `check_self_containment`
  (`tools/lexicon/lexicon.py:2359`) does today, which then calls it. This is the walk's second
  instance, so it becomes one function rather than a copy. Observed by AC3.
- **S2** — The rule. `check_rename_rule(kit_dir)` returns `(problems, judged)`: for every list or tuple
  literal in a module `read_kit_modules` returns, `selftest.py` excluded, that holds the string
  `--diff-filter=A`, the same literal must hold `-M` or an element starting `--find-renames`; each
  literal that does not is a problem naming the file and line. A walk that judges zero literals reds as
  `DEAD PROBE`, the token `check_self_containment` already prints. Observed by AC1 and AC2.
- **S3** — Where it runs. The measurement pass calls `check_rename_rule()` beside
  `check_self_containment()` (`tools/lexicon/lexicon.py:2867`) and extends `problems` with its result,
  so `lexicon naming predicates` reds on a violating spelling. Observed by AC2.

## 3. Non-goals (OUT)

- Fixing the two spellings: TOOL-dMindYourWords-43 and -44.
- An argv assembled at run time from separate pieces, a `-c diff.renames` override, or a shell string:
  S2 reads literals only, and says so in its docstring; the remedy for a refusal is to spell the flags
  in one literal.
- The pin inventory over the same walk: TOOL-dMindYourWords-50, which reads `read_kit_modules`.
- The checklist entry the report names under H1: a checklist is its own artifact (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-44` — the one `diff-tree` builder whose literal S2 judges; without it the check reds on the per-parent spelling unit 43 alone leaves
- **hands-off** `TOOL-dMindYourWords-50` — `read_kit_modules`, the extracted walk that unit's pin inventory reads

## 4. Design

### Evidence

- `check_self_containment` walks `sorted(kit.glob("*.py"))`, parses each, reds an unreadable module as
  UNJUDGED and a zero-import walk as `DEAD PROBE`, and runs in the measurement pass
  (`tools/lexicon/lexicon.py:2359-2410`, `:2867`).
- After units 26, 33, 43 and 44 the kit spells `--diff-filter=A` in `build_added_set_argv`
  (`tools/lexicon/lexicon_conf.py`) and in `read_branch_added_paths`' `git log` (TOOL-dMindYourWords-26
  S1, `tools/lexicon/lexicon.py`), both with `-M`; at base it spells it only in a comment
  (`git grep -n 'diff-filter' -- tools/lexicon` prints `tools/lexicon/selftest.py:5353` alone).
- The report's left-shift for H1: "an idiom-ban arm in the lexicon selftest that refuses any `diff-tree
  ... --diff-filter=A` in `tools/lexicon/*.py` without `-M`".

### The rule

```
for path, tree in read_kit_modules(kit_dir):            # selftest.py excluded
    for node in literals(tree, (ast.List, ast.Tuple)):
        if "--diff-filter=A" in strings(node):
            judged += 1
            if "-M" not in strings(node) and not any(s.startswith("--find-renames") for s in strings(node)):
                problems.append(f"{path.name}:{node.lineno}: an added-set argv without -M ...")
if judged == 0: problems.append("rename rule: DEAD PROBE — no added-set argv judged")
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_kit_modules` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest read_kit_modules --as py.function` answered `OK` at writing |
| `check_rename_rule` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest check_rename_rule --as py.function` answered `OK` at writing |

### Rollout

Live at landing, after TOOL-dMindYourWords-43 and -44 at the same order, which sort first, so the
first run finds both spellings carrying `-M`.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, S3
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **A selftest arm**, the report's wording: it runs only under `GATE_SELFTESTS` and in this repo, while
  the self-check runs on every `lexicon naming predicates` bar and in every adopter's install, where
  the kit's own source is the same.
- **A text grep for `--diff-filter=A` without `-M` on the same line**: argv literals wrap across lines,
  and a comment naming the rule would red; the AST reads the literal whole, as
  `check_self_containment` reads imports.

## 5. Production-readiness checklist

- security — N/A — a read of the kit's own source.
- perf / scale — one more pass over the parse trees the walk already produces.
- error / empty / loading states — an unparseable module is UNJUDGED, as in `check_self_containment`;
  a zero population is `DEAD PROBE`.
- observability — each problem names the file and line of the literal.
- risks — a legitimate added-set read that means to count a rename as an add must spell
  `--no-renames` and be refused; none exists, and unit 33 §4 rejects that reading.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — the kit's self-check, reported like `check_self_containment`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, pathlib, shutil; sys.path.insert(0, 'tools/lexicon'); import
  lexicon; print(lexicon.check_rename_rule(pathlib.Path(sys.argv[1])))" <copy>` runs on a scratch copy of
  `tools/lexicon/*.py` in which one `"-M",` element is deleted from `build_added_set_argv`, it prints a
  problem naming `lexicon_conf.py` and that line.
  Red when: an added-set argv without the rename rule passes the check.
  fixture: the copy under the run's scratch directory.
- **AC2** — When the same call runs on `tools/lexicon` itself after the pass, it prints an empty problem
  list and a judged count of at least 2.
  Red when: a spelling of the kit violates the rule, or the walk judged nothing.
  figure: DERIVED at observation; 2 by §4's inventory, the builder and the branch walk.
- **AC3** — When `check_self_containment()` runs after the pass, it returns the same problems, modules
  and imports it returned before the extraction, and `git grep -n 'kit.glob("\*.py")' --
  tools/lexicon/lexicon.py` prints one line, inside `read_kit_modules`.
  Red when: the walk is copied rather than extracted, or the extraction changed self-containment's
  answer.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · a kit copy with `-M` removed from one added-set literal, its failing case the `-M` test cut from `check_rename_rule`, under which the copy reports no problem · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 29 (HIGH, item H1, shared with ids 1, 16
  and 23) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is `check_self_containment` (`tools/lexicon/lexicon.py:2359`), the kit's AST self-check that
already runs in the measurement pass; its walk becomes `read_kit_modules` at this second instance, as
the charter's reuse rule asks, and the new rule rides it. `python tools/codebase-map/reuse_lookup.py
"refuse a source spelling that drops a required flag from an argv literal"` ranked generic readers and
the repository's idiom-ban arms, which are shell greps in other kits' suites; none reads a Python
literal whole, so no existing seam fits beyond the walk this unit extracts.

Recall terms used: `python tools/memory-recall/query.py "how is a change made in a merge resolution held to the same record rule as an ordinary commit" --terms "idiom ban rename diff-filter added argv literal self-check self-containment walk lexicon kit"`
