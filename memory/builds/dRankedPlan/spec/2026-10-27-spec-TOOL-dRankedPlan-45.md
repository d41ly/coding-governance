# TOOL-dRankedPlan-45 — the spec audit of units 30 to 37: its 32 medium and low findings, closed in one batch

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 20 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-38-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-38-promoted-fix-return.md) | research | TOOL-dRankedPlan-38 TOOL-dRankedPlan-41 |
| [2026-10-27-build-TOOL-dRankedPlan-45-deviation-451.md](../build/2026-10-27-build-TOOL-dRankedPlan-45-deviation-451.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-38-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-38-promoted-fix-brief.md) | research | TOOL-dRankedPlan-38 TOOL-dRankedPlan-41 |
| [2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) | spec-audit | TOOL-dRankedPlan-43 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-44 TOOL-dRankedPlan-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed 23
MEDIUM and 9 LOW findings. BUILD-METHOD M4 promotes them all into one unit, and this is that unit. Each
finding is named by its report id and given its own §2 item. Where the report merged ids into one item,
each id still takes its own item, and the item it shares is named beside it. Two mediums are the medium
face of a high that has its own unit. Each of those items adds the observation the medium's fix names,
over the high's mechanism, and never repeats the mechanism.

| Item | Ids | Grade | High face | §2 |
|---|---|---|---|---|
| M1 | 9, 35 | MEDIUM | none | S1, S2 |
| M2 | 3 | MEDIUM | none | S3 |
| M3 | 4 | MEDIUM | none | S4 |
| M4 | 5 | MEDIUM | none | S5 |
| M5 | 6, 24 | MEDIUM | none | S6, S7 |
| M6 | 11 | MEDIUM | none | S8 |
| M7 | 13 | MEDIUM | `TOOL-dRankedPlan-41` (H3) | S9 |
| M8 | 14 | MEDIUM | none | S10 |
| M9 | 15, 29 | MEDIUM | none | S11, S12 |
| M10 | 16, 25, 41 | MEDIUM | none | S13, S14, S15 |
| M11 | 20 | MEDIUM | none | S16 |
| M12 | 27 | MEDIUM | none | S17 |
| M13 | 28 | MEDIUM | none | S18 |
| M14 | 30 | MEDIUM | none | S19 |
| M15 | 36 | MEDIUM | `TOOL-dRankedPlan-43` (H5) | S20 |
| M16 | 37 | MEDIUM | none | S21 |
| M17 | 39 | MEDIUM | none | S22 |
| M18 | 40 | MEDIUM | none | S23 |
| L1 | 7 | LOW | none | S24 |
| L2 | 12 | LOW | none | S25 |
| L3 | 17 | LOW | none | S26 |
| L4 | 18 | LOW | none | S27 |
| L5 | 21 | LOW | none | S28 |
| L6 | 23 | LOW | none | S29 |
| L7 | 31 | LOW | none | S30 |
| L8 | 32 | LOW | none | S31 |
| L9 | 42 | LOW | none | S32 |

The minors land on units 30 to 37, so this unit repairs none in particular and is ordered after every
unit of the build. Many items correct a spec whose unit builds earlier, and the correction must reach
that unit's builder before its pass. Each such unit's §3 carries a hands-off edge to this unit naming
the items, so its builder carries the correction out in its own pass. This unit builds the rest and
observes every item at its tip.

## 2. Scope (IN)

- **S1** — Id 9, item M1 (with id 35). `derive_predicate_callers(root)` (`TOOL-dRankedPlan-30` S2) takes
  each derived path's repository-relative form from git, `git -C <root> ls-files --full-name --
  <path>`, and keeps the entry only when that prints exactly one line. Git normalises an 8.3 or a long
  spelling itself. `root` is the directory `--root` names, or the git toplevel of the working directory
  otherwise. This supersedes the lexical `relative_to(root)` step of unit 30 §4 "The derivation".
  Observed by AC1.
- **S2** — Id 35, item M1 (with id 9). The `caller-guard-prefix` plant (`TOOL-dRankedPlan-30` S3) runs
  a second time with `--root` spelled another way: its 8.3 short form on Windows, or a symlink to the
  scratch repository elsewhere. The kit's own `ratify.py` is admitted in both runs. Observed by AC1.
- **S3** — Id 3, item M2. `read_python_callers` (`TOOL-dRankedPlan-32` S1) resolves an argv element that
  is a `Name` or `Attribute`, or a call wrapping one such as `str(CLI)`, through the file's module-level
  and function-local assignments. The element names `ratify.py` when an assignment to that name holds a
  `str` constant ending `ratify.py`. The plant `caller-argv-bound` plants `CLI = HERE / "ratify.py"` and
  `subprocess.run([sys.executable, str(CLI), slug])`, and it is refused. Observed by AC2.
- **S4** — Id 4, item M3. `TOOL-dRankedPlan-30` AC1 reads, at its own order 7: the set holds exactly the
  tracked path of the loop kit's `ratify.py`, and the `triage.py` anchor raises `LookupError` and adds
  nothing. The two-path reading moves here, at order 20, after `TOOL-dRankedPlan-3` has created
  `tools/memory-tree/triage.py` at order 10. Unit 30's builder takes the order-7 reading through its
  hands-off edge. Observed by AC3.
- **S5** — Id 5, item M4. `TOOL-dRankedPlan-33` S2 reads: every plant is seeded by S1, and the three
  `plan-record-*` plants then set their own state over the seed. `plan-record-absent` commits a tree
  with no plan record for `tFix`, `plan-record-unread` commits a tree with no copied memory-tree kit,
  and `plan-record-open-probe` commits its eleven-field record over the seeded one. Unit 33 §4's table
  is read from this sentence. Unit 33's builder takes it through its hands-off edge. Observed by AC4.
- **S6** — Id 6, item M5 (with id 24). The row of `session-predicate callers (asked only at the act)` in
  `tools/gate-legs.json`, and its `[[gate_leg]]` in `tools/loop/kit.toml`, each carry `ceiling = 300`,
  the value `review-join ban (no ref-keyed join)` carries (`tools/gate-legs.json:717-724`). Its
  `tools/run-gates/ceiling-evidence.txt` row is written by `derive-ceilings.py --write` from the
  close's measured run. `TOOL-dRankedPlan-31`'s Files touched gains that file through its hands-off
  edge. Observed by AC5.
- **S7** — Id 24, item M5 (with id 6). `TOOL-dRankedPlan-31` §7 names `govkit selfcheck`,
  `codebase-map coverage + freshness` and `leg ceilings clear their evidenced maximum`, the unguarded
  meta-gates that grade a new leg. The close runs the bar with `GATE_FULL=1`. Observed by AC5.
- **S8** — Id 11, item M6. `seed_plan_witness` (`TOOL-dRankedPlan-33` S1) writes the scratch
  `.memory-tree.conf` from the example conf with one key set, `FAMILIES`, to the example's value with
  `tooling:TOOL` appended, so the `TOOL-<slug>-1` it mints binds. It sets no other key. Observed by AC6.
- **S9** — Id 13, item M7 (high face `TOOL-dRankedPlan-41`). A shell file is tokenized only when its
  text names `ratify.py` or `read_plan_ratification`, the textual prefilter unit 32 S1 applies to
  Python. The plant `caller-shell-unbalanced-elsewhere` plants a `.githooks/pre-push` with an
  unterminated quote that names neither, beside a well-formed caller-free `.githooks/pre-commit`. The
  check exits 0. A second run adds `ratify.py` to the broken hook's text, and the check exits 2 through
  `TOOL-dRankedPlan-41` S4. Observed by AC7.
- **S10** — Id 14, item M8. A heredoc body is read. In separators mode,
  `scan_shell_tokens` (`TOOL-dRankedPlan-41` S1) emits each heredoc body as one `heredoc` token at its
  first line, carrying the word that opened it. When that command's word is an interpreter, the body is
  read by `read_python_callers` for `python`, `python3` or `py`, and by `read_shell_callers` for `bash`
  or `sh`. Any other body is read only by `TOOL-dRankedPlan-38`'s textual rule. The plant
  `caller-heredoc-argv` feeds `"$py" - <<'EOF'` a body running `subprocess.run([sys.executable,
  "ratify.py", slug])`, and it is refused. The table in §4 "File kinds and readers" supersedes the
  error-state and risk lines of unit 32 §4 and §5 that say a heredoc line fails closed. Observed by AC8.
- **S11** — Id 15, item M9 (with id 29). `TOOL-dRankedPlan-37` S19 and S20 cite unit 16's lines by
  content, "the population line" and "the perf line", and S19's correction also covers unit 16's §3
  hands-off line to unit 37, respelled "whose population figure that unit corrects", with no figure.
  Unit 37's builder carries it out through its hands-off edge. Observed by AC9.
- **S12** — Id 29, item M9 (with id 15). The §9 line unit 37 S19 asks for in unit 16's spec is spelled
  "corrects the population figure to 695", naming no old figure, so `TOOL-dRankedPlan-37` AC16's count
  of `697` over the whole file reaches 0. Observed by AC9.
- **S13** — Id 16, item M10 (with ids 25, 41). `TOOL-dRankedPlan-31` §4 Rollout's red window reads: the
  leg reds on `plan_revision.py` from order 13, through `TOOL-dRankedPlan-15` S6's stubs, stays red
  through order 17, where `TOOL-dRankedPlan-29` S32 adds one more stub, and reads green from order 18.
  Observed by AC10.
- **S14** — Id 25, item M10. The Rollout records why building unit 15's plants with explicit
  `ratification=` values would not keep the leg green at order 13: unit 15 S5's own call in `show` is
  already a caller there. NOT OBSERVED by a criterion: it is a recorded reason, and AC10 observes the
  window it explains.
- **S15** — Id 41, item M10. The Rollout cites `TOOL-dRankedPlan-37` S9 as the owner of the green
  observation, after S3 to S5 there de-stub every plant. Observed by AC10.
- **S16** — Id 20, item M11. `read_js_callers` (`TOOL-dRankedPlan-32` S3) reads array literals from
  `scan_ts_tokens` in the loop kit's `extract_code.py` copy (`TOOL-dRankedPlan-41` S2), which already
  emits `[`, `]` and `,`, in place of its own scanner. A `SyntaxError` there exits 2 as
  `TOOL-dRankedPlan-41` S4 states for shell. The plant `caller-js-argv` plants a `.js` file whose
  array literal names `ratify.py` across two lines, and it is refused. Observed by AC11.
- **S17** — Id 27, item M12. Once dDeclaredLoop's loop legs are in `tools/gate-legs.json`, the §7 leg
  line of every spec of this build whose Files touched names a file under `tools/loop/` names `loop
  selftest` and every other leg whose guard is `{prefix}/loop/`. Each unit does it in its own pass,
  through its hands-off edge, and until the leg is in the manifest its §7 says so in prose. Observed by
  AC12.
- **S18** — Id 28, item M13. Two guards widen in `tools/gate-legs.json` and in their kits' `[[gate_leg]]`
  entries: `build-index selftest` gains `{prefix}/loop/`, and `loop selftest` gains
  `{prefix}/memory-tree/`. `TOOL-dRankedPlan-37` AC11 reads: the manifest guard holds the added entries,
  and the descriptor guard holds the same added entries beside its `{kit}/`. Observed by AC13.
- **S19** — Id 30, item M14. `derive_step_scenarios(build, move_fields=None)` is the signature
  `TOOL-dRankedPlan-36` S2 needs. Its one call site, in `tools/loop/loop_transition.py` before
  `write_transition` writes, passes the pending move's fields. `TOOL-dRankedPlan-36`'s Files touched and
  edges gain that file and TOOL-dDeclaredLoop-27's caller, through its hands-off edge. Observed by AC14.
- **S20** — Id 36, item M15 (high face `TOOL-dRankedPlan-43`). A stale record taken out of the tree
  and a similar fresh record added in one commit after T is reported by git as a rename, so
  `TOOL-dRankedPlan-43`'s walk dates it by the stale add and does not keep it. Git records no rename, so
  this history is the same as a `git mv`. The held line of Plan's exit gate (`TOOL-dRankedPlan-10` S4)
  names the stale record and says `add the fresh record in a commit that keeps the stale one`.
  `reader-bound` gains `replaced-in-one-commit`, pinned "not kept". Observed by AC15.
- **S21** — Id 37, item M16. `ratify.py --fixture --seed <dir>` exits 2 unless `<dir>`, resolved with
  `os.path.realpath`, lies under `tempfile.gettempdir()`, resolved the same way, and is not the toplevel
  of the repository holding the running `ratify.py`. It exits 2 naming the path when `<dir>` already
  holds a `.memory-tree.conf`, a memory-tree kit copy or a plan record for the slug. So a fixture that
  writes its own conf lines appends them after the seed. The plant `seed-refused` points `--seed` at a
  non-fixture repository and at a seeded one. Observed by AC16.
- **S22** — Id 39, item M17. A build's first move whose `scenario` field is absent or empty is refused
  with exit 1, `scenario — first move of <slug> carries no scenario= field`, never exit 2. The plant
  `plan-first-no-field` joins `scenario.py --fixture`. Observed by AC17.
- **S23** — Id 40, item M18. `check_repo_relative_path(value)` (`TOOL-dRankedPlan-37` S23) folds `\` to
  `/` itself, before its four shapes, and refuses an empty value. A `\`-led value folds to `/` and a UNC
  value to `//`, and both are refused as absolute. Observed by AC18.
- **S24** — Id 7, item L1. `TOOL-dRankedPlan-35` S3's `merged-sides` branch records carry different
  words, `defer` on one branch and `continue` on the other, and its third record carries `continue`.
  Unit 35's builder takes it through its hands-off edge. Observed by AC19.
- **S25** — Id 12, item L2. `TOOL-dRankedPlan-35` S1's unranked clause reads proper ancestry, `a != b`
  and `git merge-base --is-ancestor a b`, so records sharing one adding commit are mutually unranked.
  Observed by AC19.
- **S26** — Id 17, item L3. `TOOL-dRankedPlan-32` AC4's evidence is two greps over
  `tools/unattended/unattended.sh`, one for `resolve_kit_dir .* loop ratify.py` and one for `ratify.py"
  .*--exit`, each at least 1. Observed by AC20.
- **S27** — Id 18, item L4. In `TOOL-dRankedPlan-37` S25, "not committed" means absent from `git
  ls-files`, or present with no adding commit at HEAD, and both print `disposition <path> not
  committed`. Its `untracked` plant runs one staged-only and one untracked record. Observed by AC21.
- **S28** — Id 21, item L5. `TOOL-dRankedPlan-32` §10 reads: the unit supersedes the
  `tools/workflows/check-review-join.sh` code-line rule that unit 22 S2 cited, and the seam it extends is
  `scan_shell_tokens` through `TOOL-dRankedPlan-41`. NOT OBSERVED by a criterion: a record correction
  with no behaviour.
- **S29** — Id 23, item L6. `TOOL-dRankedPlan-31` §7 says in prose that its leg and `loop selftest` are
  owed and graded at the build, and its leg line names both in the pass that adds their rows to
  `tools/gate-legs.json`. Observed by AC12.
- **S30** — Id 31, item L7. Each unit of this build that mints a function re-renders
  `memory/map/generated/symbols.json` with `gen_map.py --write` in its pass and names
  `codebase-map coverage + freshness` on its §7. `TOOL-dRankedPlan-37`'s pass re-renders
  `memory/gotchas/INDEX.md` with `gotchas.py --write` for its S24 gotcha. This unit re-renders
  `symbols.json` once more at its tip. Observed by AC22.
- **S31** — Id 32, item L8. The seed copies the memory-tree kit once per fixture run into a template
  repository, and each plant clones the template rather than copying the kit, so the per-plant cost is
  one clone. `TOOL-dRankedPlan-33` §5's perf line states the measured cost of one kit copy, 5.1 s, and
  the close re-measures and re-declares the `loop selftest` row of
  `tools/run-gates/selftest-budgets.txt`. Observed by AC23.
- **S32** — Id 42, item L9. The reader is chosen by extension first: `*.py` to `read_python_callers`,
  `*.js` to `read_js_callers`, `*.sh` to `read_shell_callers`. An extensionless file under `.githooks/`
  goes to the shell reader. So `.githooks/pre_push_bar_selftest.py` is read as Python. The plant
  `caller-heredoc-argv` runs a second time over a `.py` hook whose one mention of the predicate's name
  is in its docstring. Observed by AC8.

## 3. Non-goals (OUT)

- Any HIGH of the same audit: units 38 to 44.
- Rewriting a landed spec. Every correction here supersedes a sentence it names, and the earlier unit's
  builder carries it out in its own pass.
- Two batch units. The ratify.py half and the rest do not split by BUILD-METHOD M6: S6's ceiling is
  measured from the leg that runs S1, S3 and S9's reader, an acceptance input of the other half, and
  S30's `symbols.json` is a generated index both halves' mints write.
- A wrapper outside `TOOL-dRankedPlan-40`'s prefix set, and a call assembled at run time: unread, as
  those units state.

### Edges

- **consumes-from** `TOOL-dRankedPlan-30` — `derive_predicate_callers`, AC1 and the `caller-guard-prefix` plant, which S1, S2 and S4 correct and re-run
- **consumes-from** `TOOL-dRankedPlan-31` — the leg's row, Files touched, §7 and Rollout, which S6, S7, S13 to S15 and S29 complete
- **consumes-from** `TOOL-dRankedPlan-32` — `read_python_callers`, `read_js_callers`, the dispatch of S5, AC4 and §10, which S3, S10, S16, S26, S28 and S32 extend or correct
- **consumes-from** `TOOL-dRankedPlan-33` — `seed_plan_witness`, `--seed`, S2's plants and §5, which S5, S8, S21 and S31 correct
- **consumes-from** `TOOL-dRankedPlan-34` — `reader-bound`'s rename cases, beside which S20 plants the replace-in-one-commit case
- **consumes-from** `TOOL-dRankedPlan-35` — S1's unranked clause and S3's `merged-sides` plant, which S24 and S25 make exact
- **consumes-from** `TOOL-dRankedPlan-36` — S2's pin on the first move, whose signature S19 spells and whose absent field S22 refuses
- **consumes-from** `TOOL-dRankedPlan-37` — S13's guards, S19's correction, S23's helper, S25's hold line and its forced render, which S11, S12, S18, S23, S27 and S30 correct
- **consumes-from** `TOOL-dRankedPlan-16` — §3's hands-off line to unit 37, whose figure S11 respells away
- **consumes-from** `TOOL-dRankedPlan-41` — the separators mode and its exit 2, over which S9 adds the prefilter, S10 the heredoc token and S16 the JavaScript tokenizer
- **consumes-from** `TOOL-dRankedPlan-43` — the rename walk, over which S20 states and plants the replace-in-one-commit case
- **hands-off** `TOOL-dRankedPlan-46` — S10's `heredoc` token and its routing table, whose shell arm that unit restates as its own command-word test (spec audit of units 38 to 45, id 1)
- **hands-off** `TOOL-dRankedPlan-47` — S10's `heredoc` token, its routing table and the `caller-heredoc-argv` plant, whose Python arm that unit restates over unit 32's interpreter class (spec audit of units 38 to 45, id 30)
- **hands-off** `TOOL-dRankedPlan-48` — S16's `read_js_callers` reading and the `caller-js-argv` plant, whose element text that unit takes from the tokenizer's new string mode (spec audit of units 38 to 45, id 8)
- **hands-off** `TOOL-dRankedPlan-49` — S3's bound-name rule for Python, whose shell twin that unit adds (spec audit of units 38 to 45, id 33)
- **hands-off** `TOOL-dRankedPlan-52` — S10's heredoc token, S21's seed check, S31's seed, AC8, AC10, AC12, AC22, AC23, §4 and §5, which that unit's items for findings 3, 4, 16, 18, 21, 24, 26, 29, 31 and 36 correct or extend; carry S9, S12, S18 and S19 into this unit's pass (spec audit of units 38 to 45)

## 4. Design

### Evidence

- M1: `resolve_kit_dir.py:28` uses `.absolute()` and never `resolve()`. On this machine `%TEMP%` is
  `C:\Users\DAILY-~1\…` and `git rev-parse --show-toplevel` prints the long form, so a lexical
  `relative_to` raises (the audit's appendix rows for ids 9 and 35).
- M2: `tools/branch-reconcile/selftest.py:28` binds `CLI = HERE / "branch_reconcile.py"` and :121 runs
  `[sys.executable, str(CLI), "--root", …]`.
- M5: `tools/gate-legs.json:717-724` gives `review-join ban (no ref-keyed join)` `"ceiling": 300`, and
  `tools/roles/kit.toml:97-102` shows a descriptor `ceiling` on an unguarded repo leg.
- M6: `.memory-tree.conf.example:20` reads `FAMILIES="architecture:ARCH deployment:DEPL design:DES"`,
  and `tree_lib._id_alternation` (`tools/memory-tree/tree_lib.py:414-416`) builds the id alternation
  from `FAMILIES` alone.
- M8 and L9: `git ls-files .githooks` lists `.githooks/pre_push_bar_selftest.py` beside the
  extensionless hooks and `*.sh` files.
- M13: `tools/memory-tree/kit.toml:277-280` gives `build-index selftest` the guard `["{kit}/"]`, while
  `tools/gate-legs.json:482-486` holds three entries, and `tools/govkit/govkit.py:2604-2605` says
  nothing compares the two.
- M16: `tools/unattended/unattended.test.sh:2537` and :6521 write their own `.memory-tree.conf`.
- M18: `tools/memory-tree/routed_commits.py:155` and `tools/memory-tree/gen_build_index.py:3339` fold
  `\` at the caller, before the shape test.
- L7: `tools/memory-tree/gotchas.py:529-531` reds a missing or stale `gotchas/INDEX.md`.
- L8: `tools/run-gates/selftest-budgets.txt:55` holds `build-index selftest 140`, and the audit measured
  one memory-tree kit copy at 5.10 s.

### File kinds and readers (S10, S32)

| File | Reader |
|---|---|
| `*.py`, `.githooks/` included | `read_python_callers` |
| `*.js` | `read_js_callers` |
| `*.sh`, and an extensionless `.githooks/` file | `read_shell_callers`, with `TOOL-dRankedPlan-38`'s textual rule |
| a heredoc body fed to `python`, `python3` or `py` | `read_python_callers` |
| a heredoc body fed to `bash` or `sh` | `read_shell_callers` |
| any other heredoc body | `TOOL-dRankedPlan-38`'s textual rule only |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-argv-bound`, `caller-shell-unbalanced-elsewhere`, `caller-heredoc-argv`, `caller-js-argv`, `seed-refused` | `ratify.py` fixture plants | none |
| `replaced-in-one-commit` | `reader-bound` case | none |
| `plan-first-no-field` | `scenario.py` fixture plant | none |
| `heredoc` | token kind of `scan_shell_tokens` in separators mode | none |

### Rollout

This unit lands last, at order 20. Its corrections to earlier specs reach their builders through those
units' hands-off edges, so each lands in its own unit's pass and is observed here.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3, S9, S10, S16, S20, S21, S31, S32
- `tools/lib/extract_code.py`, `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`,
  `tools/loop/extract_code.py`: S10's `heredoc` token
- `tools/gate-legs.json`, `tools/loop/kit.toml`, `tools/memory-tree/kit.toml`: S6, S18
- `tools/run-gates/ceiling-evidence.txt`: S6
- `tools/loop/scenario.py`, `tools/loop/loop_transition.py`: S22
- `tools/memory-tree/tree_lib.py`: S23
- `tools/run-gates/selftest-budgets.txt`: S31
- `memory/map/generated/symbols.json`: S30

### Alternatives rejected

- **Name the heredoc forms unread (S10).** It is the cheaper fix the audit offers, but it leaves a
  `ratify.py` call in a heredoc'd Python body outside a deny-by-default ban. BUILD-METHOD M3 takes the
  option that satisfies more, and the tokenizer already finds the bodies.
- **Keep an existing `.memory-tree.conf` under `--seed` (S21).** The seed would then mint an id the kept
  conf may not declare, which is finding 11's defect again. Refusing is deny by default.

## 5. Production-readiness checklist

- security — S3, S9, S10 and S32 close reading gaps in a deny-by-default ban. S21 validates the one
  fixture write path at its boundary. S23 refuses backslash and UNC forms.
- perf / scale — S9's prefilter skips the tokenizer on most shell files, and S31 makes the seed one
  copy per fixture run.
- error / empty / loading states — S16's and S10's tokenizer errors exit 2 as unit 41 states, S21 and
  S22 name their refusals.
- observability — each plant prints its answer, and S20's held line names the stale record.
- risks — S17 and S29 depend on dDeclaredLoop's loop legs being in the manifest at the build run, as
  the build's parents are.
- testing — the plants of S2, S3, S9, S10, S20, S21 and S22, the probes of S1, S4, S6, S8, S18 and S23,
  and the greps of S11, S12, S17, S26, S29 and S30.
- migration — none.
- user docs — N/A — no user-facing surface moves.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-guard-prefix` runs, the kit's own
  `ratify.py` is admitted with `--root` in each of its two spellings.
  Red when: a differing spelling of the root refuses the kit's own module.
  fixture: a scratch repository under a short `%TEMP%` path.
- **AC2** — When the plant `caller-argv-bound` runs, the check exits 1 naming the `subprocess.run` line.
  Red when: an argv list naming the script through a bound name passes.
- **AC3** — When a probe calls `derive_predicate_callers` over this repository at this unit's tip, it
  returns exactly the two paths `git ls-files` lists for the loop kit's `ratify.py` and the memory-tree
  kit's `triage.py`.
  Red when: either declared caller is missing once both exist.
- **AC4** — When the plants `plan-record-absent`, `plan-record-unread` and `plan-record-open-probe` run,
  their moves print `unwitnessed`, `unread`, and a refusal then an admission once the probe returns.
  Red when: a plant's state disagrees with S5's sentence.
- **AC5** — When a probe reads `tools/gate-legs.json` and `tools/run-gates/ceiling-evidence.txt`, the
  row `session-predicate callers (asked only at the act)` carries `ceiling` 300 and has an evidence row,
  and `grep -c "govkit selfcheck"` over unit 31's spec prints at least 1.
  Red when: the new leg has no ceiling or its meta-gates are unnamed.
- **AC6** — When `python ratify.py --fixture --seed <dir> --build tFix` runs over a fresh scratch
  repository, its `.memory-tree.conf` declares `tooling:TOOL` and the seeded record's `**Serves:**` line
  binds.
  Red when: the seed mints an id its conf does not declare.
- **AC7** — When the plant `caller-shell-unbalanced-elsewhere` runs, the check exits 0, and with
  `ratify.py` named in the broken hook it exits 2 naming that hook.
  Red when: an untokenizable file that names neither name reds the leg, or one that does is skipped.
- **AC8** — When the plant `caller-heredoc-argv` runs, the check exits 1 naming the body's line. When
  its second run plants, under the scratch repository's `.githooks/`, only a `.py` file whose one
  mention of `read_plan_ratification` sits in its docstring, the check exits 0, where the shell
  reader's textual rule (`TOOL-dRankedPlan-38` S1) would refuse that line.
  Red when: a heredoc'd argv call passes, or a `.py` hook is read as shell.
- **AC9** — When `grep -c "697"` runs over `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md`
  at this unit's tip, it prints 0.
  Red when: unit 16's hands-off line or a §9 line still states the old figure.
- **AC10** — When `python ratify.py --check-callers` runs over this repository at this unit's tip, it
  exits 0, and `grep -c "order 17"` over unit 31's spec prints at least 1.
  Red when: the leg is red after order 18, or the Rollout still states a window ending at order 14.
- **AC11** — When `python ratify.py --fixture --plant caller-js-argv` runs, its planted `.js` file
  holding `["python3", "ratify.py", slug]` across two lines is refused with exit 1.
  Red when: the JavaScript reader misses an array literal that `scan_ts_tokens` reads.
- **AC12** — When `grep -l "loop selftest"` runs over the specs of units 30 to 45 at this unit's tip, it
  lists every one whose Files touched names a file under `tools/loop/`.
  Red when: a unit touching the loop kit leaves the loop kit's suite unnamed.
- **AC13** — When a probe reads `tools/gate-legs.json`, `tools/memory-tree/kit.toml` and the loop
  kit's `kit.toml`, `build-index selftest`'s guards hold `{prefix}/loop/` and `loop selftest`'s
  hold `{prefix}/memory-tree/`, each spelled with its own placeholder in the descriptor.
  Red when: a suite reads a sibling kit its guard does not name.
- **AC14** — When `grep -n "derive_step_scenarios("` runs over the loop kit's `loop_transition.py` at
  this unit's tip, the call passes the pending move's fields.
  Red when: the first move's `scenario` field never reaches the check.
- **AC15** — When the plant `reader-bound` runs `replaced-in-one-commit`, the fresh record is not kept
  and the held line names the stale record.
  Red when: the case is kept silently, or held with no reason.
- **AC16** — When the plant `seed-refused` runs, `--seed` at a non-fixture repository and at a seeded
  one each exits 2 naming the path, and writes nothing.
  Red when: the seed writes outside a fixture or over existing state.
- **AC17** — When `python scenario.py --fixture --plant plan-first-no-field` runs, the first move exits
  1 printing `carries no scenario= field`.
  Red when: an absent field brings back exit 2.
- **AC18** — When a probe calls `check_repo_relative_path` with `\abs`, `a\..\b`, `\\srv\x` and an empty
  string, each raises.
  Red when: a backslash form passes the helper.
- **AC19** — When the `merged-sides` and `one-commit` cases of `reader-bound` run, `merged-sides`
  returns `None` with `disposition conflict` before its third record, and two different words added in
  one commit return `None`.
  Red when: the plant's words agree, or a shared commit ranks its own records.
- **AC20** — When `grep -c "resolve_kit_dir .* loop ratify.py"` and `grep -c 'ratify.py" .*--exit'` run
  over `tools/unattended/unattended.sh`, each prints at least 1.
  Red when: one shape is missing and a whole-file count hides it.
- **AC21** — When the `untracked` case of `reader-bound` runs its staged-only and its untracked record,
  each `why` reads `not committed`.
  Red when: a staged-only record prints another line.
- **AC22** — When `grep -c "read_kept_dispositions"` runs over `memory/map/generated/symbols.json` at
  this unit's tip, it prints at least 1, and `gotchas.py --check` exits 0.
  Red when: a minted function or gotcha is missing from its render.
- **AC23** — When `grep -c "loop selftest" tools/run-gates/selftest-budgets.txt` runs at this unit's
  tip, it prints at least 1, and the seed copies the kit once per fixture run.
  Red when: the seed's per-plant copy is back, or no budget row covers the suite.
  figure: 5.1 s per kit copy is PINNED, measured by the audit's skeptic on 2026-10-27.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck` · `codebase-map coverage + freshness` · `leg ceilings clear their evidenced maximum` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, by S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC7 AC8 AC11 AC15 AC16 AC19 AC21 · `caller-argv-bound`, `caller-shell-unbalanced-elsewhere`, `caller-heredoc-argv`, `caller-js-argv`, `seed-refused`, `replaced-in-one-commit` and the corrected `merged-sides`, staged by a reader that skips bound names and heredoc bodies and reads a `.py` hook as shell · none

New arm: tools/loop/scenario.py · covers AC17 · `plan-first-no-field`, staged by a check that passes `pin=None` on an absent field · none

New arm: tools/memory-tree/tree_lib.py · covers AC18 · the backslash and UNC cases of `check_repo_relative_path`, staged by a helper that does not fold `\` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37: its 23 MEDIUM and
  9 LOW findings, ids 3 4 5 6 7 9 11 12 13 14 15 16 17 18 20 21 23 24 25 27 28 29 30 31 32 35 36 37 39
  40 41 42, batched under BUILD-METHOD M4.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-46`, the hands-off edge to `TOOL-dRankedPlan-47`, the hands-off edge to `TOOL-dRankedPlan-48`, the hands-off edge to `TOOL-dRankedPlan-49`, the hands-off edge to `TOOL-dRankedPlan-52`, each the reciprocal of that promoted unit's own edge (spec audit of units 38 to 45, `reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`); no other section moves.

## 10. Reuse audit

Each item extends the seam its finding names rather than minting one. S1 takes git's own path
normalisation. S10 and S16 extend `TOOL-dRankedPlan-41`'s use of `scan_shell_tokens` and reuse
`scan_ts_tokens` from the same copied block. S20 sits on `TOOL-dRankedPlan-43`'s walk, and S23 on
`TOOL-dRankedPlan-37`'s helper. `python tools/codebase-map/reuse_lookup.py "tokenize shell source into
commands and words with quotes and command substitution"` ranked `parse_shell_defs`, the tokenizer's
own caller, so no seam fits beyond the block TOOL-dTotalRecall-13 moves into `tools/lib`. The recall
query returned that unit's move and this audit's items, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader find a script invocation behind if exec or a case arm" --terms "shell tokenizer scan_shell_tokens invocation reserved word exec case pattern heredoc shlex caller predicate"`
