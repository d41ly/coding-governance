# TOOL-dDeclaredLoop-88 — the round-7 spec audit's 36 minors, batched

**Status:** DEFERRED · rev-5 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 44 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-88-deviation-881.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-88-deviation-881.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-87-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-87-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-87 |

<!-- /gen:spec-records -->

## 1. Goal

The round-7 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md`)
exited CONVERGED with 37 confirmed findings over units 83 to 86, the round-6 promotions. Its one high,
id 29, is unit 87. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW,
each by its report id and each its own scope item, where the report merged ids into one item too. The
minors land on 83, 84, 85 and 86, so this unit repairs none in particular and builds after every unit
(order 44, above 87's 43).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1 | S1 |
| M2 | MEDIUM | 2, 20 | S2, S3 |
| M3 | MEDIUM | 3, 21 | S4, S5 |
| M4 | MEDIUM | 4, 31 | S6, S7 |
| M5 | MEDIUM | 5 | S8 |
| M6 | MEDIUM | 7 | S9 |
| M7 | MEDIUM | 8 | S10 |
| M8 | MEDIUM | 11 | S11 |
| M9 | MEDIUM | 16 | S12 |
| M10 | MEDIUM | 17 | S13 |
| M11 | MEDIUM | 23 | S14 |
| M12 | MEDIUM | 25 | S15 |
| M13 | MEDIUM | 30 | S16 |
| M14 | MEDIUM | 32 | S17 |
| M15 | MEDIUM | 33 | S18 |
| M16 | MEDIUM | 34 | S19 |
| L1 | LOW | 6, 19 | S20, S21 |
| L2 | LOW | 9 | S22 |
| L3 | LOW | 10, 18, 28, 37 | S23, S24, S25, S26 |
| L4 | LOW | 12, 26 | S27, S28 |
| L5 | LOW | 13 | S29 |
| L6 | LOW | 14 | S30 |
| L7 | LOW | 15 | S31 |
| L8 | LOW | 22, 36 | S32, S33 |
| L9 | LOW | 24 | S34 |
| L10 | LOW | 27 | S35 |
| L11 | LOW | 35 | S36 |

That is 19 MEDIUM and 17 LOW findings by raw id. Four defects span two grades, and each is fixed once
across its items: M3 with L4 (S4, S5, S27, S28), M12 with L1 (S15, S20, S21), M6 with L11 (S9, S36), and
M11 with L9 (S14, S34). The report refuted no finding.

## 2. Scope (IN)

- **S1** — id 1. `TOOL-dDeclaredLoop-75` S27's sentence that 83 S1 writes, "Only 81's `uncomputable` C,
  an octopus merge or a probed absence of the feature, grades against the parents", is narrowed: an exit
  other than 0 and 1 never grades against the parents, and an octopus merge, a probed absence of the
  feature and an exit 1 whose conflicted paths hold the policy path do, as 69 S2 grades them. 83 S1 says
  the same, and 83 §4's "S27 after this unit" table gains that third parent row. The edits are rev bumps
  of 75 and 83, each with its §9 line. Observed by AC1.
- **S2** — id 2. 78 S1's opening "C has three states" names the five states, `present`, `absent`,
  `conflicted`, `uncomputable` and `failed`, as a rev bump of 78 with its §9 line. Observed by AC2.
- **S3** — id 20. 78 §4's grade block dispatches on all five states in S2's rev bump: `present` or
  `absent` to the C branch; `uncomputable`, or `conflicted` with the policy path among the conflicted
  paths, to 69 S2's parent branch; `failed` to 81 S3's every-parent rule. The two-way
  `if C is not uncomputable:` test gives way to that dispatch. Observed by AC3.
- **S4** — id 3. `TOOL-dDeclaredLoop-81` S1 names `check_write_tree_usage(rc, text)`, answering
  `supported`, `unsupported` or `probe failed` by 85 S2's rule, and `resolve_write_tree_support()`,
  answering that answer with its detail. The one-argument, two-valued sentence gives way to it. The edit
  is a rev bump of 81 with its §9 line. Observed by AC4.
- **S5** — id 21. 81 AC5 calls `check_write_tree_usage` on `(129, <usage line>)` pairs and expects
  `supported` and `unsupported`, and `resolve_write_tree_support()` answering `supported` on the node, in
  S4's rev bump of 81. Observed by AC5.
- **S6** — id 4. The memo of `resolve_write_tree_support` in `tools/loop/guard.py` is keyed to the probe
  it called: it holds the `run_merge_tree_usage` object beside the answer and its detail, and answers from
  the memo only while the module's `run_merge_tree_usage` is that same object. A plant installing a probe
  twin then probes once through the twin, and restoring the real probe probes once more. A process that
  never swaps the probe probes once, as 85 S3 states, and 81 S4's plant that replaces
  `resolve_write_tree_support` itself never reads the memo. 85 S1 and S3 say so, as a rev bump of 85 with
  its §9 line. Observed by AC6.
- **S7** — id 31. `guard.py --fixture` with no `--plant` runs every case in one process, and each probe
  plant and each re-merge plant meets its outcome there as it does alone. Observed by AC7.
- **S8** — id 5. 78 §4's grade block gains the line
  `probe failed -> failed("probe failed", detail), re-merge not run (85 S4)`, in S2's rev bump of 78.
  Observed by AC8.
- **S9** — id 7. `TOOL-dDeclaredLoop-80` S4's sentence "75 S6's plant and 79 AC20's and AC25's plants are
  written inside the boundary" names every later plant of either module too:
  `TOOL-dDeclaredLoop-82`'s `conf-read-forms` rows and AC15's root-source trees, and the
  `conf-read-forms` rows of `TOOL-dDeclaredLoop-86` and `TOOL-dDeclaredLoop-87`. The edit is a rev bump of
  80 with its §9 line. Observed by AC9.
- **S10** — id 8. `TOOL-dDeclaredLoop-86` AC12's last half carries its command, the AC5 range of 82
  piped to `grep -c "both exist\|at least one"`, at least 1, as a rev bump of 86 with its §9 line. 82 AC5
  holds that floor as 86 S12 writes it; where it does not, this unit's rev bump of 82 writes it.
  Observed by AC10.
- **S11** — id 11. 86 AC9 reads the credential store as `cmdkey //list`, the spelling Git Bash passes
  through unchanged, in 86's rev bump. The before-read must hold at least one `Target:` line before "no
  new target" counts, and the staged break must read a new target naming `127.0.0.1`, which the build
  then clears from the credential store by its target name. This pass re-observes the `url-forms` plant that way.
  Observed by AC11.
- **S12** — id 16. 82 S6's pass-commit probe reads each pass commit's manifest through
  `read_profile_legs` (`tools/run-gates/measure_legs.py:473`), which wraps `load_manifest` and refuses a
  duplicate name, an argv that is not a list of strings and an unresolved `{` token. Its `ProfileRefused`
  is recorded as `manifest refused at pass commit: <message>`, never as an absent leg, and a row matched
  by name then goes to `derive_leg_argv`. 82 §10 names `read_profile_legs`, and 86 S8 is restated to the
  same route. The edits are in this unit's rev bumps of 82 and 86. Observed by AC12.
- **S13** — id 17. `derive_constant_charges(tree, module, is_needle)` in `tools/memory-tree/tree_lib.py`
  is the charge walk of `scan_glob_readers` (`tools/memory-tree/gen_build_index.py:5146`), its four
  rules unchanged, lifted with the needle as a predicate over a str constant's value. It answers each
  charged owner with the number of the rule that charged it, over the docstring set
  `derive_docstring_ids` answers (82 S8). `scan_glob_readers` calls it with its `:(glob)` needle and keeps
  no walk of its own. `derive_conf_constants` (87 S1) is the slice whose rule is 2 and whose owner is
  qualified by the module alone, its needle the two conf names, and it reaches `tree_lib` through 86
  S21's in-function route. 86 §10's "No existing seam fits" sentence for `derive_conf_constants` names
  this seam, in 86's rev bump. Observed by AC13.
- **S14** — id 23. 85 §4 Files touched names `memory/map/generated/symbols.json`, with the sentence that
  85's pass regenerates it and that `TOOL-dDeclaredLoop-25` regenerates it at step 21 too, dispatched in
  sequence with 25 first, as 86 S3 records step 38's shared write. The edit is in this unit's rev bump of
  85. This pass regenerates the render once and observes it fresh. Observed by AC14.
- **S15** — id 25. 85 S2 is restated to 86 S2's rule, in 85's rev bump: `supported` and `unsupported`
  each require `rc` 0 or 129 and a line opening `usage: git merge-tree` on either stream, `supported`
  where the text names `--write-tree` and `unsupported` where it does not, and any other outcome is
  `probe failed`. Observed by AC15.
- **S16** — id 30. `run_merge_tree_usage` reaches git through `subprocess.run` with `LC_ALL=C` and an
  empty `LANGUAGE` in that call's environment alone, a copy of the process environment, and decodes both
  streams from bytes with `errors="replace"`. 85 S1 and 86 S2's narrowing say so, in their rev bumps.
  Observed by AC16.
- **S17** — id 32. The plant `push-merge-probe-failed-trailered` joins `guard.py --fixture`: the merge of
  `push-merge-probe-failed`, carrying a `Gov-Policy:` trailer naming each key whose value differs from the
  main parent's. 85 S4's trailer sentence points at it, in 85's rev bump. Observed by AC17.
- **S18** — id 33. 82 AC4 gains the class-level half, as a rev bump of 82 with its §9 line: over the S27
  range of the 75 spec, `grep -c "never a fall to the parents"` prints at least 1, and at 82's pass
  `guard.py --fixture --plant push-merge-tree-fatal` exits 1 printing `the clean re-merge failed: 128`.
  This pass runs both. Observed by AC18.
- **S19** — id 34. Two plants join `guard.py --fixture`. `push-merge-conflicted-unparseable-parent`:
  `run_merge_tree` answering 1 with the policy path among the conflicted paths, one parent's policy blob
  unparseable. `push-merge-probe-failed-unparseable-parent`: the probe twin raising `OSError`, one
  parent's policy blob unparseable. Each refuses with 78 S3's `does not parse at parent <sha8>` line.
  Observed by AC19.
- **S20** — id 6. 81 S1 states S15's rule, `rc` 0 or 129 with a `usage: git merge-tree` line for both
  `supported` and `unsupported`, in S4's rev bump of 81. Observed by AC20.
- **S21** — id 19. No spec of this build keeps the wider predicate in its own words: 85 S2's sentence
  that `supported` is "the text names `--write-tree`" at any exit code, and 81 S1's "true when the text
  names", each give way to S15's rule in the rev bumps above. Observed by AC21.
- **S22** — id 9. The passages 86 S5, S6, S9, S10 and S21 amend carry their amendments at this pass, one
  observation each: 81 S3 names `conflicted` and `failed`; 79 AC10 names 80's pass commit; 82 §5 names
  the credential store; 82 S8 names `govkit update --kits memory-tree`; and with 82 AC15's root-source
  trees in `budget.py`, the `no-own-conf-read` plant exits 0. A passage found without its amendment is
  amended in this unit's rev bump of that spec. Observed by AC22.
- **S23** — id 10. 85 S3's probe detail gains `signal <n>`, n the positive signal number, for a probe
  that dies by a signal and answers a negative `rc`, in 85's rev bump. Observed by AC23.
- **S24** — id 18. One detail builder, `build_failure_detail(outcome, text, empty_label)` in
  `tools/loop/guard.py`, spells every detail under `the clean re-merge failed:`. An `OSError` reads
  `start failed: <strerror>`, a negative `rc` reads `signal <n>`, and any other `rc` reads `<rc>`; each
  but the first is followed by the first non-blank line of `text`, or by `empty_label` where it has none.
  The probe passes stdout and stderr joined with `(no output)`, and the re-merge passes stderr alone with
  `(no stderr)`. 85 S3 and 85 AC2 read that spelling, `probe failed: 129`, in 85's rev bump.
  Observed by AC24.
- **S25** — id 28. 86 S22 is restated to name S24's builder as the one spelling of a re-merge failure,
  in 86's rev bump. Observed by AC25.
- **S26** — id 37. The `push-merge-tree-fatal` plant gains a row whose `run_merge_tree` twin answers
  `rc` -9, and the plant `push-merge-probe-signal` joins `guard.py --fixture`, its probe twin answering
  `rc` -9. Observed by AC26.
- **S27** — id 12. 81 §4's grade opens `support, detail = resolve_write_tree_support()` and carries 85
  S4's three branches, in S4's rev bump of 81. Observed by AC27.
- **S28** — id 26. 85 AC5's grep over the 81 spec is widened to
  `answering false\|not supported\|answers True\|answers False\|check_write_tree_usage(text)\|true when`,
  printing 0, in 85's rev bump. Observed by AC28.
- **S29** — id 13. 86 AC16 counts occurrences, `grep -o "grep -c" | wc -l` over 80's AC4 range, at least
  3, in 86's rev bump. This pass runs it. Observed by AC29.
- **S30** — id 14. 86 AC18's positive half is `grep -c ":3769"` over the 82 spec, at least 2, matching
  82's short citation form, in 86's rev bump. Observed by AC30.
- **S31** — id 15. 83 §4 Evidence cites 75 by anchor, 75 §6 AC27 and 75 §7's
  `New arm: tools/loop/guard.py` line, never by line number, in S1's rev bump of 83. Observed by AC31.
- **S32** — id 22. 86 §4's conf-constant sketch reads the kit directory from
  `resolve_kit_dir("memory-tree", "tree_lib.py", here)` and loads `tree_lib` from that directory as 75
  S35 states, in 86's rev bump. Observed by AC32.
- **S33** — id 36. `derive_conf_reads` in `tools/loop/loop_lib.py` refuses by name where
  `resolve_kit_dir` raises `LookupError` and where loading `tree_lib.py` raises `ImportError` or
  `SyntaxError`, as 86 S21 refuses a `tree_lib` lacking `derive_docstring_ids`: the run exits non-zero
  printing the places looked and `govkit update --kits memory-tree`, never a traceback. The
  `no-own-conf-read` plant of `tools/loop/budget.py` gains a row for each case beside 86 AC21's. 86 S21
  says so, in 86's rev bump. Observed by AC33.
- **S34** — id 24. 86 §4 Files touched and its Write set name `memory/map/generated/symbols.json`, which
  86's pass regenerates, in 86's rev bump. Observed by AC34.
- **S35** — id 27. The Files touched of 83, 84 and 85 each name `memory/builds/dDeclaredLoop/README.md`,
  with the sentence that the build README's regions are the generator's render, in their rev bumps.
  Observed by AC35.
- **S36** — id 35. 86 AC10's third clause greps 80's S4 range for
  `TOOL-dDeclaredLoop-82\|TOOL-dDeclaredLoop-86`, at least 1, in 86's rev bump. Observed by AC36.

## 3. Non-goals (OUT)

- The high's mechanism, the conf-constant class: unit 87.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Following a member name inside a binding's value: 87 §8 F2 keeps the class to charge rule 2's
  predicate, and S13's slice inherits that.
- Pinning the locale of the re-merge call, `run_merge_tree`: its first stderr line is printed and never
  parsed, so a translated line changes no verdict.
- Clearing the credential-store entries the round-6 skeptic's probe left on node `d`: a write to the
  owner's environment outside the repository, as 86 §3 records.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-75` — S27's parent rows, which S1 completes with the conflicted-policy case, and AC27 (id 1)
- **consumes-from** `TOOL-dDeclaredLoop-78` — S1's state count and §4's grade block, which S2, S3 and S8 restate to five states and a failed-probe line (ids 2, 5, 20)
- **consumes-from** `TOOL-dDeclaredLoop-79` — AC10, whose re-observation at 80's pass commit S22 reads (id 9)
- **consumes-from** `TOOL-dDeclaredLoop-80` — S4's plant population, which S9 widens to 82's, 86's and 87's plants (id 7)
- **consumes-from** `TOOL-dDeclaredLoop-81` — S1's probe signature and rule, S3's state names, §4's grade and AC5 (ids 3, 6, 9, 12, 19, 21)
- **consumes-from** `TOOL-dDeclaredLoop-82` — S6's pass-commit probe, S8, AC4, AC5, §5 and §10, and the `scan_glob_readers` docstring set of S8 that S13's lifted walk reads (ids 8, 9, 16, 17, 33)
- **consumes-from** `TOOL-dDeclaredLoop-83` — S1's parent rows, §4's S27 table, its Evidence pins and Files touched (ids 1, 15, 27)
- **consumes-from** `TOOL-dDeclaredLoop-84` — the restatement of 78's grade, whose dispatch S3 completes, and Files touched (ids 2, 20, 27)
- **consumes-from** `TOOL-dDeclaredLoop-85` — `run_merge_tree_usage`, the memoised resolver, the probe detail, S2's predicate, the probe plants, AC2, AC5 and Files touched (ids 4, 10, 18, 19, 23, 25, 26, 27, 30, 31, 32)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S2's narrowing, S8, S21, S22, the conf-constant sketch, §4 Files touched, §10, AC9, AC10, AC12, AC16 and AC18, and the `failed` plants of S6 and S22 (ids 5, 7, 8, 9, 11, 13, 14, 16, 17, 22, 24, 28, 30, 34, 35, 36, 37)
- **consumes-from** `TOOL-dDeclaredLoop-87` — `derive_conf_constants` as the class S1 states, which S13 re-implements as the module-level slice of the lifted walk, AC2's answer unchanged (id 17)
- **consumes-from** `TOOL-dDeclaredLoop-89` — `derive_conf_rebinds`, which S13's `derive_conf_constants` unites with its rule-2 slice where this unit builds after 89 (the round-8 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-90` — S2, S13, S24, S33, the lifted-walk sketch, §4 Evidence and Write set, and AC1, AC2, AC6, AC9, AC12, AC13, AC16 and AC22, which that unit restates, with `derive_constant_charges`, `build_failure_detail` and the `tree_lib` route this unit mints (the round-8 spec audit's ids 2, 3, 5, 6, 7, 11, 13, 15, 16, 21, 22, 25, 26)
- **hands-off** `TOOL-dDeclaredLoop-92` — §3's consumes-from 87 bullet, S13, S24, the lifted-walk sketch and AC1, AC6, AC12, AC13 and AC16, which that unit restates (the round-9 spec audit's ids 1, 5, 6, 22)
- **hands-off** `TOOL-dDeclaredLoop-94` — S18 and AC18, which that unit cites in 92 S17, S24, whose range it greps, and AC24, whose `OSError` spelling it restates (the round-10 spec audit's ids 4, 11, 20)
- **hands-off** `TOOL-dDeclaredLoop-96` — S33, which that unit restates over the caller's `need` and any exception the import raises (the round-11 spec audit's ids 7, 9)

## 4. Design

### Write set

This pass writes `tools/loop/guard.py` (S6, S16, S17, S19, S24, S26), `tools/loop/loop_lib.py` (S13,
S33), `tools/loop/budget.py` (S33's rows), `tools/memory-tree/tree_lib.py` and
`tools/memory-tree/gen_build_index.py` (S13), and `memory/map/generated/symbols.json`, regenerated once
for the symbols S13 and S24 mint. Inside this build's folder it amends the specs of 75, 78, 80, 81, 82,
83, 84, 85 and 86 as rev bumps, one per spec, each with its §9 line, and 79 only where S22 finds its
amendment absent. The build README's regions are the generator's render. S7, S11, S14, S18, S22 and S29
also observe and record.

### The probe memo, after this unit (S6)

```
resolve_write_tree_support():
    probe = run_merge_tree_usage                      # the module attribute a plant may swap
    if memo and memo.probe is probe: return memo.answer, memo.detail
    answer, detail = probe once: OSError -> "probe failed", build_failure_detail(exc, "", "(no output)")
                                 else check_write_tree_usage(rc, out + err), build_failure_detail(rc, out + err, "(no output)")
    memo = (probe, answer, detail)                    # a failed probe included, as 85 S3 states
    return answer, detail
```

### The lifted charge walk (S13)

```
tree_lib.derive_constant_charges(tree, module, is_needle) -> [(owner, rule)]
    docs = derive_docstring_ids(tree)                                     # 82 S8
    scan_glob_readers' scan_scope, verbatim, with `magic in value` read as is_needle(value),
    answering (owner, 1 | 2 | 3 | 4) per charge
gen_build_index.scan_glob_readers(kit_dir):  owners of derive_constant_charges(tree, name, lambda s: ":(glob)" in s)
loop_lib.derive_conf_constants(path):        names n where (f"{module}.{n}", 2) is answered for a conf-name needle
```

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- `cmdkey /list` from Git Bash printed its syntax help and 0 `Target:` lines; `cmdkey //list` printed
  17, counted with `grep -c "Target:"` and never printed.
- `awk '/^- \*\*S4\*\*/,/^## 3/'` over the 80 spec piped to
  `grep -c "TOOL-dDeclaredLoop-82\|TOOL-dDeclaredLoop-86"` printed 0, so S9's and S36's token
  discriminates.
- `read_profile_legs` refuses a duplicate name ("appears a second time") and an argv-less row by index,
  and `load_manifest` refuses only a non-list or a nameless row (`tools/run-gates/measure_legs.py:473-500`,
  `tools/run-gates/held_halves.py:80-95`).
- `resolve_kit_dir` answers a directory, and raises `LookupError` naming the receipt and both probes when
  neither finds the anchor (`tools/lib/resolve_kit_dir.py:15-50`).
- The `codebase-map coverage + freshness` leg carries no guard, and its symbol tier compares
  `symbols.json` byte for byte with `render_symbols_json(all_symbols())`
  (`tools/gate-legs.json`, the leg's row; `tools/codebase-map/test_codebase_map.py:291-332`).
- `C:/Program Files/Git/mingw64/share/locale` does not exist, so git 2.54.0.windows.1 here prints no
  translated usage; git prints its usage header through gettext: UNVERIFIED here, from the report's
  reading of git's parse-options.
- 81 S1 reads `check_write_tree_usage(text)` "true when the text names `--write-tree`", and 81 AC5
  expects "answers True" and "answers False"; 85 S2 reads "`supported`: the text names `--write-tree`";
  78 S1 opens "C has three states" and its §4 dispatches on `if C is not uncomputable:`; 83 §4 Evidence
  pins 75 at lines 389-392 and 430, where AC27 opens at line 390 and the guard arm sits at 431
  (`memory/builds/dDeclaredLoop/spec/`, each spec named).

### Files touched (estimate)

- `tools/loop/guard.py`
- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `memory/map/generated/symbols.json`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the guard items and the rest.** Not disjoint by M6: every half rev-bumps sibling
  specs, so each re-renders the build README's units region, a generated index written with its
  generator (clause 3); and the 85 spec is written by guard items (S6, S16, S17, S23, S24) and by text
  items (S14, S15, S28, S35) alike (clause 1).
- **A second detail builder per caller (S24).** Two builders under one refusal prefix is the defect; the
  `<rc>` spelling is the re-merge's because 81 AC1, 81 AC3, 83 S2 and 82 AC4 grep
  `the clean re-merge failed: 128`, and only 85 AC2 spells `rc 129`.
- **`MSYS_NO_PATHCONV=1` for S11.** It reaches the same store; `//list` was the spelling measured, and an
  environment variable read by the shell is one more thing a criterion's reader must know is set.

## 5. Production-readiness checklist

- security — S6, S7 and S17 keep a failed probe refusing untrailered whatever the plant order; S16 keeps a
  capable git on a translated locale from reading as a failed probe; S11 makes the credential-store read
  observe the store.
- perf / scale — S6 probes once more per probe swap, in fixtures only; S13 replaces one walk with one walk.
- error / empty / loading states — S24 names a start failure, a signal and an empty stream in one
  spelling; S33 names an unlocatable or unloadable `tree_lib`; S12 names a refused manifest.
- observability — each refusal names its case; the probe lines keep 86 S19's key.
- risks — the amendments land on specs whose units are built, as 86 amends its siblings; each is a rev
  bump with its §9 line. S24 moves 85 AC2's expected line from `rc 129` to `129`, a printed-text change
  the rev bump of 85 carries. S13 edits a governance kit's engine, observed by its four-rule probe.
- testing — AC1 to AC36 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `awk '/^- \*\*S27\*\*/,/^- \*\*S28\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md` is piped to
  `grep -c "conflicted paths hold the policy path"`, it prints at least 1, `grep -c "Only 81's"` over the
  same file prints 0, and `awk '/^### S27 after this unit/,/^### Files touched/'` over the 83 spec piped
  to `grep -c "policy path"` prints at least 2.
  Red when: S27 still says only `uncomputable` reaches the parents beside 69 S2's conflicted case.
- **AC2** — When `grep -c "C has three states"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md`, it prints 0, and
  `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over it piped to `grep -c "five states"` prints at least 1.
  Red when: 78 S1 still counts three states.
- **AC3** — When `grep -c "if C is not uncomputable"` runs over the 78 spec, it prints 0, and
  `awk '/^### The grade, restated/,/^### Files touched/'` over it piped to `grep -c "81 S3"` prints at
  least 1.
  Red when: the dispatch still sends `failed` to the branch that compares M with C.
- **AC4** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md` is piped to
  `grep -c "check_write_tree_usage(rc, text)"`, it prints at least 1, and
  `grep -c "check_write_tree_usage(text)\|true when"` over the same file prints 0.
  Red when: 81 S1 still names a one-argument boolean beside two-argument code.
- **AC5** — When `grep -c "answers True\|answers False"` runs over the 81 spec, it prints 0, and
  `awk '/^- \*\*AC5\*\*/,/^## 7/'` over it piped to `grep -c "unsupported"` prints at least 1.
  Red when: re-observing 81 AC5 as written calls the predicate with one argument.
- **AC6** — When a `python -c` probe imports `guard` from `tools/loop/`, installs a counting probe twin
  as `run_merge_tree_usage` and calls `resolve_write_tree_support()` twice, then installs a second twin
  and calls it twice, each twin counts 1 call; and with no twin installed, two calls run the real probe
  once.
  Red when: the memo answers the first twin's answer after a swap, or the real path probes twice.
- **AC7** — When `python guard.py --fixture` runs in `tools/loop/` with no `--plant`, it exits 0, and
  its lines for `push-merge-probe-failed`, `push-merge-probe-silent`, `push-merge-old-git-usage` and
  `push-merge-tree-fatal` hold `probe failed: start failed`, `probe failed: 129`,
  `graded against its parents only` and `the clean re-merge failed: 128`, with `merge-tree runs: 0` for
  each probe plant.
  Red when: a memo set by an earlier case decides what a later plant sees, staged by keying the memo to
  nothing.
- **AC8** — When `grep -c "probe failed"` runs over the 78 spec, it prints at least 1.
  Red when: 78's grade and 81's give two answers for a failed probe.
- **AC9** — When `awk '/^- \*\*S4\*\*/,/^## 3/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-80.md` is piped to
  `grep -c "TOOL-dDeclaredLoop-82\|TOOL-dDeclaredLoop-86"`, it prints at least 1, and at this pass the
  `no-own-conf-read` plant of `budget.py --fixture` and of `breakpoints.py --fixture` each exits 0.
  Red when: 80 S4 still names only 75's and 79's plants.
  figure: the 0 at HEAD is PINNED, 2026-10-24.
- **AC10** — When `awk '/^- \*\*AC5\*\*/,/^- \*\*AC6\*\*/'` over the 82 spec is piped to
  `grep -c "both exist\|at least one"`, it prints at least 1, and
  `awk '/^- \*\*AC12\*\*/,/^- \*\*AC13\*\*/'` over the 86 spec piped to `grep -c 'grep -c "both exist'`
  prints at least 1.
  Red when: 86 AC12's half is judged on 82 AC5's existing mention with no command.
- **AC11** — When `cmdkey //list` piped to `grep -c "Target:"` is read before and after
  `python position.py --fixture --plant url-forms` in `tools/loop/`, the before-read prints at least 1,
  and a `diff` of the two reads' `Target:` lines, run without printing them, finds none added; and
  `grep -c "cmdkey /list"` over the 86 spec prints 0.
  Red when: the read is the syntax help, so "no new target" holds without reading the store.
  permission: this pass reads the OS credential store's target names, never a secret; the staged break
  of 86 AC9 that writes an entry is the build's, and a reviewer does not run it.
  fixture: a Windows node; elsewhere `cmdkey` is absent and the criterion is not observable.
- **AC12** — When `awk '/^- \*\*S6\*\*/,/^- \*\*S7\*\*/'` over the 82 spec and
  `awk '/^- \*\*S8\*\*/,/^- \*\*S9\*\*/'` over the 86 spec are each piped to
  `grep -c "read_profile_legs"`, each prints at least 1; and a `python -c` probe over a scratch copy of
  `tools/gate-legs.json` with its `memory hygiene` row appended a second time finds `load_manifest` answering both
  rows and `read_profile_legs` raising `ProfileRefused` naming `appears a second time`.
  Red when: the probe route still reads the raw loader, which grades a duplicated row by its first match.
- **AC13** — When `grep -c "def scan_scope"` runs over `tools/memory-tree/gen_build_index.py`, it prints
  0, and `grep -c "def derive_constant_charges"` over `tools/memory-tree/tree_lib.py` prints 1; a
  `python -c` probe calling `scan_glob_readers` on a scratch directory holding `m.py`, with a `:(glob)`
  constant inside function `f`, bound to module name `X`, appended at class level in class `K` and
  appended at module level, answers `['m', 'm.K', 'm.X', 'm.f']`; and 87 AC2's probe answers its set
  unchanged.
  Red when: the lift moves an owner, or a second walk remains beside the lifted one.
- **AC14** — When `awk '/^### Files touched/,/^### Alternatives/'` over the 85 spec is piped to
  `grep -c "symbols.json"`, it prints at least 1; and in `tools/codebase-map/`,
  `python -c "import map_extractors as ext, map_lib as m; p = m.map_root() / 'generated' / 'symbols.json'; print(m.lf(p.read_text(encoding='utf-8')) == m.render_symbols_json(ext.all_symbols()))"`
  prints `True` after this pass's one regeneration.
  Red when: a pass adds a symbol and the render is left stale, or two parallel units regenerate it with
  neither declaring it.
- **AC15** — When `awk '/^- \*\*S2\*\*/,/^- \*\*S3\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-85.md` is piped to
  `grep -c "0 or 129"`, it prints at least 1.
  Red when: 85 S2 still answers `supported` at any exit code.
- **AC16** — When a `python -c` probe imports `guard`, replaces `subprocess.run` with a recorder for one
  call and calls `run_merge_tree_usage` on the worktree, the environment it recorded holds `LC_ALL=C`
  and an empty `LANGUAGE`, and `os.environ` is unchanged after; and with `LC_ALL=de_DE.UTF-8` exported,
  `resolve_write_tree_support()` answers `supported` on this node.
  Red when: the probe inherits the caller's locale, so a translated usage header reads `probe failed`.
  fixture: this node ships no git catalogs, so the second half cannot show a translation; the first half
  is the discriminating one.
- **AC17** — When `python guard.py --fixture --plant push-merge-probe-failed-trailered` runs, it exits 0
  printing `merge-tree runs: 0`.
  Red when: `probe failed` refuses whatever the trailer names, staged by routing it to an unconditional
  refusal.
- **AC18** — When `awk '/^- \*\*AC4\*\*/,/^- \*\*AC5\*\*/'` over the 82 spec is piped to
  `grep -c "never a fall to the parents"` and to `grep -c "push-merge-tree-fatal"`, each prints at least
  1; `awk '/^- \*\*S27\*\*/,/^- \*\*S28\*\*/'` over the 75 spec piped to
  `grep -c "never a fall to the parents"` prints at least 1; and `guard.py --fixture --plant push-merge-tree-fatal`
  exits 1 printing `the clean re-merge failed: 128`.
  Red when: 82's pass rewords S27's fallback and only a grep-0 of one old spelling guards it.
- **AC19** — When `python guard.py --fixture --plant push-merge-conflicted-unparseable-parent` and
  `--plant push-merge-probe-failed-unparseable-parent` run, each exits 1 printing
  `does not parse at parent ` and no `Traceback`.
  Red when: the conflicted or the probe-failed branch reads the parent with no parse guard.
- **AC20** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over the 81 spec is piped to
  `grep -c "0 or 129"`, it prints at least 1.
  Red when: a reader of 81 meets the wider predicate with no warning.
- **AC21** — When `grep -c "supported.: the text names\|true when the text names"` runs over the 81 spec
  and over the 85 spec, each prints 0.
  Red when: one spec keeps the predicate the code no longer answers by.
- **AC22** — When `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` over the 81 spec is piped to
  `grep -c "conflicted"` and `grep -c "failed"`, each prints at least 1;
  `awk '/^- \*\*AC10\*\*/,/^- \*\*AC11\*\*/'` over the 79 spec piped to `grep -c "80's pass commit"`
  prints at least 1; `awk '/^## 5/,/^## 6/'` over the 82 spec piped to `grep -c "credential store"` prints
  at least 1; `awk '/^- \*\*S8\*\*/,/^- \*\*S9\*\*/'` over the 82 spec piped to
  `grep -c "govkit update --kits memory-tree"` prints at least 1; and `python budget.py --fixture --plant no-own-conf-read`
  exits 0 with the `root-source` plant's trees present.
  Red when: one of 86's sibling amendments was skipped and every criterion of 86 still passed.
- **AC23** — When a `python -c` probe installs a probe twin answering `(-9, "", "")` and calls
  `resolve_write_tree_support()`, it answers `probe failed` with a detail opening `signal 9`, and
  `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` over the 85 spec piped to `grep -c "signal <n>"` prints at
  least 1.
  Red when: a killed probe prints `rc -9`.
- **AC24** — When a `python -c` probe calls `build_failure_detail` on an `OSError` with `(no output)`,
  on `128` with text `fatal: x` and label `(no stderr)`, on `-9` with empty text and `(no stderr)`, and on
  `129` with empty text and `(no output)`, it answers `start failed: ` and the strerror, `128 fatal: x`,
  `signal 9 (no stderr)` and `129 (no output)`; and
  `grep -c "rc <n>\|rc 129"` over the 85 spec prints 0.
  Red when: the probe and the re-merge spell one failure two ways.
- **AC25** — When `awk '/^- \*\*S22\*\*/,/^## 3/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-86.md` is piped to
  `grep -c "build_failure_detail"`, it prints at least 1.
  Red when: 86 S22 still specifies a builder of its own.
- **AC26** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs, its rc -9 row prints
  `the clean re-merge failed: signal 9`, and `--plant push-merge-probe-signal` exits 1 printing
  `probe failed: signal 9`, neither with a `Traceback`.
  Red when: a builder prints `rc -9` and every other row still passes.
- **AC27** — When `grep -c "supported = resolve_write_tree_support()"` runs over the 81 spec, it prints
  0, and `grep -c "support, detail = resolve_write_tree_support()"` prints at least 1.
  Red when: a reader of 81 tests the answer pair for truthiness.
- **AC28** — When `awk '/^- \*\*AC5\*\*/,/^## 7/'` over the 85 spec is piped to `grep -c "answers True"`,
  it prints at least 1.
  Red when: 85 AC5 cannot see the one-argument boolean wording it exists to catch.
- **AC29** — When `awk '/^- \*\*AC16\*\*/,/^- \*\*AC17\*\*/'` over the 86 spec is piped to
  `grep -c "grep -o"`, it prints at least 1, and `awk '/^- \*\*AC4\*\*/,/^## 7/'` over the 80 spec piped to
  `grep -o "grep -c"` and `wc -l` prints at least 3.
  Red when: a criterion keyed to line layout counts three greps on one line as one.
- **AC30** — When `awk '/^- \*\*AC18\*\*/,/^- \*\*AC19\*\*/'` over the 86 spec is piped to
  `grep -c '":3769"'`, it prints at least 1, and `grep -c ":3769"` over the 82 spec prints at least 2.
  Red when: a correct re-pin in 82's short form reads red.
- **AC31** — When `grep -c "lines 389-392\|line 430"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-83.md`, it prints 0.
  Red when: 83 still lands a reader on AC26's tail and the wrong arm.
- **AC32** — When `grep -c "tl.derive_docstring_ids"` runs over the 86 spec, it prints 0, and
  `awk '/^### The conf-constant kind/,/^### Evidence/'` over it piped to `grep -c "75 S35"` prints at
  least 1.
  Red when: the sketch still treats a directory as a module.
- **AC33** — When a scratch copy of `tools/loop/` and `tools/lib/`, made under the run's scratch
  directory with no `memory-tree/` beside them, runs `python budget.py --fixture --plant no-own-conf-read`
  in its `loop/`, it exits non-zero printing `looked in` and `govkit update --kits memory-tree` and no
  `Traceback`; and a second copy that also holds `memory-tree/`, a syntax error planted in its
  `tree_lib.py`, prints `govkit update --kits memory-tree` and no `Traceback`.
  Red when: `LookupError` or an import failure ends the plant in a traceback.
- **AC34** — When `awk '/^### Files touched/,/^### Alternatives/'` over the 86 spec is piped to
  `grep -c "symbols.json"`, it prints at least 1.
  Red when: 86's pass regenerates a render outside its declared set.
- **AC35** — When `awk '/^### Files touched/,/^### Alternatives/'` over each of the 83, 84 and 85 specs is
  piped to `grep -c "dDeclaredLoop/README.md"`, each prints at least 1.
  Red when: three parallel step-21 units re-render one region with disjoint-looking write sets.
- **AC36** — When `awk '/^- \*\*AC10\*\*/,/^- \*\*AC11\*\*/'` over the 86 spec is piped to
  `grep -c "every plant"`, it prints 0, and to `grep -c "TOOL-dDeclaredLoop-82"` it prints at least 1.
  Red when: 86 AC10's spec-text half is green before 80 S4 is widened.

## 7. Gates

`recall floor` · `recall floor arms` · `tier2-review self-test` · `build-index selftest` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop breakpoints fixtures`, `loop position fixtures`, the leg
`loop guard fixtures` and the leg `loop selftest`, none of them a leg at HEAD.

New arm: tools/loop/guard.py · covers AC6 AC7 AC16 AC17 AC19 AC23 AC24 AC26 · the probe-keyed memo, the whole-fixture run, the pinned locale, the trailered probe-failed plant, the two unparseable-parent plants and the one detail builder with its signal rows, each staged as its criterion's Red when · none
New arm: tools/loop/budget.py · covers AC33 · the unlocatable and the unloadable tree_lib, staged with the locator's LookupError left to propagate · none
New arm: tools/memory-tree/gen_build_index.py · covers AC13 · the four charge-rule owners read through the lifted walk, staged with derive_constant_charges charging a module-level binding to the module · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — How does a plant isolate the probe memo (ids 4, 31)?** (a) the plant hook clears the memo before
  and after each plant; (b) the memo is keyed to the probe object it called; (c) every probe plant
  replaces `resolve_write_tree_support` itself, as 81 S4 does. All three pass AC7. (a) adds a reset a
  builder can reach from the production path; (c) leaves 85's three plants unable to observe the
  resolver's own `OSError` and detail handling, which AC1 to AC3 of 85 read. (b) needs no reset and no
  caller discipline. RESOLVED (agent, 2026-10-24, delegated): (b), S6. widens: none · relaxes: none
- **F3 — Which spelling does the one detail builder keep for an exit code (id 18)?** (a) the re-merge's
  `<rc> <line>`; (b) the probe's `rc <rc> <line>`. Both satisfy AC24's one-spelling rule. (a) moves one
  expected line, 85 AC2's; (b) moves 81 AC1, 81 AC3, 83 S2's re-observation and 82 AC4. RESOLVED (agent,
  2026-10-24, delegated): (a), S24. widens: none · relaxes: none
- **F4 — Lift the charge walk, or record in §10 why not (id 17)?** (a) lift `scan_scope` into `tree_lib`
  and slice it; (b) keep 87's own walk and name charge rule 2 in 86 §10 as the rejected seam. The report
  judged (a) sound and admits (b). (b) leaves two walks deciding one question, the defect, and 82 S8
  already lifts the docstring half of that walk into `tree_lib`. 82 §4's rejection of this extraction
  weighed `derive_conf_reads`, which has no use for the scope tracking; `derive_conf_constants` needs
  exactly rule 2's module scope. RESOLVED (agent, 2026-10-24,
  delegated): (a), S13. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-7 spec audit's 36 minors batched (19 MEDIUM, 17 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-89 and TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-92, written by the round-9 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 85's resolver and probe (S6, S16,
S23, S24), 81's `failed` grade and plants (S17, S19, S26), the memory-tree kit's charge walk lifted into
`tree_lib.py` beside 82 S8's docstring set (S13), the run-gates kit's `read_profile_legs` for the
pass-commit probe (S12), the codebase-map kit's own renderer for the freshness probe (S14), and the
loop kit's `resolve_kit_dir` route (S33).
`python tools/codebase-map/reuse_lookup.py "describe a subprocess failure as start failure, signal or exit code with its first line"`
ranked `check_line`, `render_line`, `parse_conf_line` and `derive_run_starts`, none a failure-detail
builder, so no existing seam fits `build_failure_detail` beyond the two spellings it unifies. The
memory-recall query returned the round-7 report's M4, 85's own checklist and a recorded `OSError` launch
failure (`TOOL-aFoldedQuarry-1`'s review, L2), the start-failure case S24 names.

Recall terms used: memo per process probe twin plant isolation subprocess signal negative returncode refusal detail formatter
