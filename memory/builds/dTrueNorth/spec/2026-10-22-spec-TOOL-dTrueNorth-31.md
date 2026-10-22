# TOOL-dTrueNorth-31 — the round-2 closing diff review's minors: a guarded none, ordered stderr, tracked attributes, held environments, whole walks and arms that can red

**Status:** CLOSED · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-31-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-31-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md](../build/2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md) | journal | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 TOOL-dTrueNorth-32 TOOL-dTrueNorth-33 |
| [2026-10-22-build-TOOL-dTrueNorth-31-deviation-33.md](../build/2026-10-22-build-TOOL-dTrueNorth-31-deviation-33.md) | deviation | — |
| [2026-10-22-build-TOOL-dTrueNorth-31-deviation-34.md](../build/2026-10-22-build-TOOL-dTrueNorth-31-deviation-34.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-31-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-31-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-31-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-31-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-31-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-31-spec-brief.md) | research | — |
| [2026-10-22-review-TOOL-dTrueNorth-31-closing-diff-review-round3.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-31-closing-diff-review-round3.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 closing diff review of dTrueNorth
(`memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md`)
exited CLEAN WITH FIXES with 16 confirmed findings in 15 items and no blocker or high. This unit is
the one batch BUILD-METHOD M4 makes of them, one scope item per review item, each built from the fix
the review's skeptic judged sound, and for findings 3, 6 and 8 from the skeptic's corrected fix. It
builds last (order 14), after every unit whose code it amends. Every line cited below was read at the
range's tip, `072d97f5c`, and every red-when reading marked as measured was observed there.

| Review item | Severity | Finding ids | Scope item | Criterion |
|---|---|---|---|---|
| M1 | MEDIUM | 1 | S1 | AC1 |
| M2 | MEDIUM | 2 | S2 | AC2 |
| M3 | MEDIUM | 3 | S3 | AC3 |
| M4 | MEDIUM | 6 | S4 | AC4 |
| M5 | MEDIUM | 14 | S5 | AC5 |
| M6 | MEDIUM | 16 | S6 | AC6 |
| M7 | MEDIUM | 17 | S7 | AC7 |
| M8 | MEDIUM | 19 | S8 | AC8 |
| M9 | MEDIUM | 22 | S9 | AC9 |
| L1 | LOW | 8 | S10 | AC10 |
| L2 | LOW | 10 | S11 | AC11 |
| L3 | LOW | 13 | S12 | AC12 |
| L4 | LOW | 15, 24 | S13 | AC13 |
| L5 | LOW | 21 | S14 | AC14 |
| L6 | LOW | 25 | S15 | AC15 |

S16 is the deviation record §8 F1 owes for S1. Each item's fix is the record's sound fix except where
the item says why its variant is better.

## 2. Scope (IN)

- **S1** — M1, finding 1, `tools/unattended/lib-unattended.sh:354`. `read_consumes_from` admits a
  payload of `none`, bare or backticked, only when no backtick follows it, the record's rule:
  ``t ~ /^none([ \t][^`]*)?$/ || t ~ /^`none`([ \t][^`]*)?$/`` in place of today's two `none` tests,
  the `external` test unchanged. A `none` whose prose holds a backticked token is unreadable, so
  `--scan` prints its `<spec> TAB` row and `--dispatch` refuses with code 49
  (`tools/unattended/unattended.sh:13734-13737`). The comment above the function (`:328-338`) states
  the narrowed rule. This is better than the record's example pattern, which also refuses
  `none until the reader lands`, a form TOOL-dTrueNorth-26 admitted that names no token, and which puts
  multibyte dashes in an awk bracket expression, where TEMPLATE-SPEC's Edges section keeps marker
  bytes ASCII. Its suite arm plants the line `none until`, a backticked `ARCH-tRun-2`, `lands` in
  the S6 block's CLOSED sibling and expects the unreadable refusal naming that spec. Settled at rung 5
  (§8 F1). Observed by AC1.
- **S2** — M2, finding 2, the capture at `tools/memory-tree/check-memory-hygiene.sh:1268-1273`,
  `:1711` and `:1752`, closed in the generator. `print_check_verdicts`
  (`tools/memory-tree/gen_build_index.py:2925-2944`) runs each verb under
  `contextlib.redirect_stderr(said)` beside `redirect_stdout(said)`, and `main` (`:8568-8569`) binds
  `sys.stderr` to `sys.stdout` for the `--with-verdicts` call and restores it after, so every write to
  `sys.stderr` in that process lands inside its verb's section or after `build-index: verdicts end`, in
  order. The hygiene capture is unchanged. Observed by AC2.
- **S3** — M3, finding 3, `tools/memory-tree/asbuilt_view.py:196`, the skeptic's fix.
  `check_view_merge` (`:189-205`) runs `git -c core.attributesFile=/dev/null check-attr merge -- <view>`
  with `GIT_ATTR_NOSYSTEM=1` in its env, through `design_lib.run_git` (`tools/memory-tree/design_lib.py:152-160`),
  which gains the keyword `extra_env`, a dict laid over the stripped env that no other caller passes.
  When that answers `ours`, `read_info_merge(root, view)` reads `git rev-parse --git-path info/attributes`;
  where the file exists it is evaluated alone, as the `core.attributesFile` of an empty scratch
  repository initialised with `--template=`, under the same env, and any answer but `unspecified` is
  the finding naming that file as untracked node state outranking every tracked line. No call uses
  `--cached`. `build_view_fixture`'s `git init` (`:378`) gains `--template=`. That is better than the
  record's `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1` for the fixture: once the call
  carries its own `-c`, the one route left for node state into the fixture's answer is a template
  copied at init, and `--template=` closes it whatever config or `GIT_TEMPLATE_DIR` says, where the
  env pair leaves `GIT_TEMPLATE_DIR` open. Observed by AC3.
- **S4** — M4, finding 6, `tools/memory-tree/deviation_join.py:657`, the skeptic's fix.
  `read_decision_ref` (`:652-661`) calls `row_grammar.resolve_remote(root)` inside
  `set_env_aside(GIT_ENV_LEAKS)`, a `contextlib.contextmanager` in `deviation_join.py` that pops each
  named key present in `os.environ` for its block and restores the popped values in its `finally`.
  `GIT_ENV_LEAKS` joins the `tree_lib` import at `:136`. `row_grammar.resolve_remote`
  (`tools/memory-tree/row_grammar.py:1146-1196`) is untouched, the inline copy its
  `remote_ladder_py` marker gates. Observed by AC4.
- **S5** — M5, finding 14, `tools/memory-tree/gen_build_index.py:5075`. `scan_glob_readers`
  (`:5056-5085`) walks every `FunctionDef` and `AsyncFunctionDef` at any depth, each named
  `<module>.<qualified name>` with its enclosing class and function names joined by dots, and charged
  with the constants of its own body outside nested functions and classes; and every `Assign`,
  `AnnAssign` and `AugAssign` at any depth outside a function, in a class body or an `if`, `try`,
  `with` or loop block, its targets qualified by the enclosing classes. Its docstring says the walk
  reaches every depth and keeps its NOT SEEN list. The planted module of the AC5 plant arm
  (`:6334-6339`) gains a class `Planted` whose method `read_method` returns a pathspec constant, and a
  constant `GUARDED` assigned under `if True:`. Observed by AC5.
- **S6** — M6, finding 16, `tools/check-spec-tokens.test.sh:1578`. The TOOL-dTrueNorth-26 AC1 probe
  records each captured `env` as handed, `k.get("env")`, and prints `inherits` for a runner handed none,
  the rule `_read_runner_env23` (`tools/memory-tree/gen_build_index.py:6283-6298`) applies, so its
  expected line `AC1 design_lib leaks [] routed_commits leaks [] second list False` holds only when both
  runners pass an env holding no leak name. Observed by AC6.
- **S7** — M7, finding 17, `tools/memory-tree/gen_build_index.py:6247-6248`. Each of the two rows calls
  the reader it names. The `deviation_join.read_population` row calls it over a deviation fixture
  `deviation_join.build_fixture` writes with the `audit-pin` plant, its conf from
  `deviation_join.read_fixture_conf` and its commits from `routed_commits.read_routed_commits(root, ["HEAD"])`,
  so both of its pathspecs (`tools/memory-tree/deviation_join.py:543-544`) read a record: the plant's
  pinned review and the base's divergence prompt. The `gen_build_index.derive_audit_writers` row calls
  `derive_audit_writers(t14w, conf14w["MEMORY_ROOT"], {run14}, _resolve_fixture14)` over the
  TOOL-dTrueNorth-14 fixture (`:5984-6023`), whose answer is `[run14]`. The record named `t23`, but
  `t23` holds no harness, so the reader answers an empty set there and the arm's never-empty half would
  red it. The arm's expected `probed=4 empty=[] moved=[]` is unchanged. Observed by AC7.
- **S8** — M8, finding 19, `tools/memory-tree/deviation_join.py:661` and the AC15 arm (`:1521-1537`).
  A `run_plant_arms` arm gives the base fixture a remote, `git remote add origin <fixture root>` then
  `git update-ref refs/remotes/origin/main <the base commit>`, and asserts `measure_fixture` reports
  `ref` `origin/main` with `rows` read. A second fixture, of the `owner-unknown-id` plant with the same
  remote, commits on its run branch a `memory/DECISIONS.md` holding a row `FIX-dClosedLoop-99`, and its
  report render still refuses the citation, naming `FIX-dClosedLoop-99` and `which no row`, since the
  row is on the run branch alone. The ref shape is the instrument's
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:539`).
  Observed by AC8.
- **S9** — M9, finding 22, `tools/memory-tree/deviation_join.py:1263`. `run_fixture` (`:1263-1297`)
  and `run_plant_arms` each run their whole body inside `set_env_aside(("GOV_REMOTE", "GOV_DEFAULT_BRANCH"))`,
  S4's helper; the inline `ladder_env` hold at `:1497` and its restore at `:1610` become that call.
  The AC15 arm keeps setting `GOV_REMOTE` inside the block. Observed by AC9.
- **S10** — L1, finding 8, the skeptic's fix. The code-49 remedy at `tools/unattended/unattended.sh:13735`
  ends `or the word external or none:$_c_bad`, the comment at `:13723` names `none` beside `external`,
  and in the same commit the literals at `tools/unattended/unattended.test.sh:6429` and `:6430` end
  `or the word external or none` and `or the word external or none:` followed by the planted spec's
  path. Observed by AC10.
- **S11** — L2, finding 10, `tools/check-spec-tokens.py:876`. `load_kit_module` (`:846-877`), when the
  slot holds a module from another file, keeps the kit's load in a module-level dict `KIT_LOADS` keyed
  by the resolved path, so every call in one process returns one module and one `DesignRefusal` class;
  `main`'s catch at `:1633` reads that class through `load_design_lib()`. At
  `tools/memory-tree/gen_build_index.py:1973` the catch tests `isinstance` against
  `mod.load_design_lib().DesignRefusal` where it loaded the checker as `mod`, after the
  `ImportError` and `SyntaxError` test, and keeps `sys.modules["design_lib"]` under an injected
  `resolve`, whose stand-in brings its own module. The docstring says a namesake slot reuses the one
  cached load. Observed by AC11.
- **S12** — L3, finding 13, `tools/memory-tree/gen_build_index.py:2938`. `print_check_verdicts` also
  catches `Exception` per verb, after `Problem`, printing `build-index: <type name>: <message>` inside
  that verb's section with rc 2, so `cmd_check` still runs and check 9 reads its own verdict. `main`'s
  catch (`:8571-8573`) is unchanged. Observed by AC12.
- **S13** — L4, findings 15 and 24, `tools/memory-tree/check-verdict-epoch.sh:257`. The closure line
  reads `the delegates' import closure is <k> sibling module(s) and <m> other scanned file(s), every
  sibling in DELEGATES`, `<k>` counting the read paths directly inside the kit directory and `<m>` the
  rest, and the comment at `:206-218` says what each counts. The suite's control arm
  (`tools/memory-tree/check-verdict-epoch.test.sh:264`) writes a non-sibling `check-spec-tokens.py` at
  its fixture's tool root before the base commit, the path DELEGATES folds `../check-spec-tokens.py` to,
  and asserts `2 sibling module(s) and 1 other scanned file(s)`. Observed by AC13.
- **S14** — L5, finding 21, the S6 block at `tools/unattended/unattended.test.sh:6436-6443`. A second
  plant writes the CLOSED sibling's bullet as a bare `none` with dash prose, ``- **consumes-from** none — it builds on nothing``,
  and the dispatch hits `dispatch declared` and misses `from which no unit id is read`. Observed by
  AC14.
- **S15** — L6, finding 25. `tools/check-spec-tokens.test.sh` passes `"$MEMORY_TREE"` in place of
  `"$HERE/memory-tree"` at `:1551` and `:1618`, globs `"$MEMORY_TREE"/*.py` at `:1628-1629`, and does
  the same at `:1502`, the spelling the record notes predates the range. That is better than the
  record's three sites: the suite then spells the kit's directory through `MEMORY_TREE` alone, so AC15
  asserts the class, zero literal spellings, where the narrower fix leaves one a grep must exempt.
  Observed by AC15.
- **S16** — S1's deviation record, `2026-10-22-build-TOOL-dTrueNorth-31-deviation-34`, written by the
  build pass from §4 verbatim in the commit that changes `read_consumes_from`. Observed by AC16.

## 3. Non-goals (OUT)

- The nine refuted findings, round 1's items, and the inherited reds of the flagged bar.
- The left-shift gates the record proposes per item: an install-prefix leg widened to literal kit
  paths (L6), a probe-row naming rule in the class gate (M7), and the checklist entries. Each is a
  gate of its own and so a unit of its own by BUILD-METHOD M2.
- Hygiene check 12's handling of `none`, the alternative M1 names: S1 closes the defect where it
  takes effect, at the dispatch. TEMPLATE-SPEC's Edges payload rule and check 12's empty-payload
  message still name `external` alone; no finding names them.
- `row_grammar.resolve_remote` and its parity-gated copies; a `tree_lib` home for S4's helper, which
  has one module of callers.
- Any other arm of the five suites, any floor, and running any suite or the bar. They are the
  close's.
- Editing the frozen specs of units 1 to 30, or any other build's spec.

### Edges

- **consumes-from** external — the code the CLOSED units of this build landed, which these fixes
  amend: the none admission and its refusal (units 20 and 26), the verdict sections (unit 27), the
  merge guard and the scrubbed runner (unit 26), the decision ref and the fixture hold (unit 27), the
  glob-reader walk and its mode arm (unit 23), the import-closure line (unit 25), and the suite arms
  (units 26 and 27); a frozen spec cannot write the mirroring hands-off line, so they are named here
  in prose

## 4. Design

### One unit

M4 batches every minor into one unit, two only for disjoint write sets that build concurrently.
S1, S10 and S14 write only the unattended kit, a set disjoint from the rest, but order 14 holds this
unit alone and the rescope row names one, so a split buys no concurrency.

### Contract changes a shipped verb takes (brief item 2)

| Item | Verb | What changes | What does not |
|---|---|---|---|
| S1 | `--dispatch`, through `read_consumes_from` | a `none` payload holding a backticked token is unreadable, refused with code 49 | `external`; `none` bare or backticked with token-free prose; every exit code |
| S10 | `--dispatch`'s code-49 remedy | the text names `none` | the exit and when it fires |
| S2 | `gen_build_index.py --check --with-verdicts` | its stderr lines print on stdout, inside the section of the verb that wrote them or after the end marker | every other mode, the markers, the exit |
| S12 | the same | a verb's non-Problem exception is its section's one line with exit 2, and `--check` still runs | `main`'s Problem mapping |
| S3 | `--check-asbuilt`, check 30 | the attribute is read without global, system or repository-config attribute files, and an `info/attributes` setting merge for the view is a finding | the finding for an unguarded view, its text |
| S9 | `deviation_join.py --fixture` | its verdict is read without the caller's `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` | its arguments, plants and exits |
| S13 | `check-verdict-epoch.sh` | the closure line's wording and its second count | every exit |

Each is the narrowest change that closes its defect: S1 refuses only the form that can name a
sibling, S2 reorders only under the flag whose capture is split, S3 reads one more file only when the
first answer is `ours`, and S9 holds only the two keys the ladder reads.

### What each item does not check

- S1: a sibling named in `none`'s prose without backticks still reads as no edge; check 12's
  sibling-in-prose arm reads backticked tokens only (`check-memory-hygiene.sh:2701-2708`), so both
  readers see one population.
- S2: a child process writing to file descriptor 2 is not reordered; every generator spawn goes
  through `run` (`gen_build_index.py:263-268`), which captures its stderr.
- S3: a `.gitattributes` file in the work tree that is untracked still answers, as today, and the
  AC18 arm empties the work-tree file for that reason. `/dev/null` is read as the null device by Git
  for Windows; measured on git 2.54.0.windows.1: a scratch global `core.attributesFile` holding
  `*.md merge=ours` answered `ours` plainly and `unspecified` under the `-c`, and an `info/attributes`
  line evaluated alone in a template-free scratch repository answered `ours` for its path and
  `unspecified` for another.
- S5: the widened walk names the same five readers the table holds today: an `ast` walk with S5's
  rule over `tools/memory-tree/` at `072d97f5c` printed `design_lib.read_spec_revisions`,
  `deviation_join.read_population`, `gen_build_index.cmd_selftest`,
  `gen_build_index.derive_audit_writers` and `row_grammar._build_backlog_pathspecs`. A pathspec
  composed at run time stays unseen.
- S7: the rows prove the readers' answers do not move under the modes; whether a future reader
  routes through the stripped runner is the class gate's question, outside this unit.
- S8: the remote is a path, and nothing is fetched.
- S11: a namesake still holds `sys.modules["design_lib"]`, as TOOL-dTrueNorth-26 S11 chose.
- S12: the traceback is not printed; the line names the type and the message.

### Deviation-34 (S1, S16)

`memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-31-deviation-34.md`, written in the
build pass's commit with the view re-rendered:

```markdown
# TOOL-dTrueNorth-31 deviation 34 — the dispatch reads a consumes-from none that holds a backticked token as unreadable, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-31

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the edge reader `--dispatch` refuses on
- **After:** TOOL-dTrueNorth-31 makes `read_consumes_from` admit a consumes-from payload of `none`, bare or backticked, only when no backtick follows it, so a `none` whose prose holds a backticked token is unreadable and `--dispatch` refuses it with code 49, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The round-2 closing diff review's finding 1 found that TOOL-dTrueNorth-26's `none` admission skips a bullet whatever follows it, so a `none` naming a same-build producer in prose lets `--dispatch` admit its consumer while that producer is open, and hygiene check 12's sibling-in-prose arm runs for `external` alone. Every mechanism that closes it is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md`, item M1 (finding 1); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-31 §8 F1
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-31
- **Caused-by:** 2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, through `read_consumes_from`: a consumes-from payload of none followed by a backticked token reads as unreadable
```

The number 34 is the build's next after this unit's own deviation-33; a record taking it first moves
this one to the next free number, and the §8 mark follows.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `set_env_aside` | context-manager function, `deviation_join.py` | `py.function`, OK |
| `read_info_merge` | function, `asbuilt_view.py` | `py.function`, OK |
| `KIT_LOADS` | module-level dict, `check-spec-tokens.py` | none, `py.constant` is undeclared |
| `extra_env` | keyword of `design_lib.run_git` | none |

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/check-verdict-epoch.test.sh`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited: deviation-34 and the render's code are view inputs)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-31-deviation-34.md` (new)

### Alternatives rejected

- **S3: scan `info/attributes` for any line setting merge, with no pattern match.** It reds a node
  whose file sets merge for another path; git's own matcher in a scratch repository answers for the
  view alone, and only when the file exists.
- **S3: evaluate every check in a scratch git directory over the work tree.** It pays a `git init`
  on every check-30 run, where S3 pays it only on a node holding `info/attributes`.
- **S4 and S9: two inline holds.** The hold is a kind at its third instance here; one helper is the
  factory the charter's reuse rule asks for.
- **S7: an `ast` proof per row in place of a call.** The record's fallback; a call also reads the
  `prompts/**` pathspec no row reads today.
- **S13: the shorter wording `module(s) read`.** It leaves a dropped sibling offset by an added
  outside file invisible in the count.

## 5. Production-readiness checklist

- security — S3 reads the guard from tracked state alone and refuses untracked state that outranks
  it; S4 and S9 keep a caller's environment out of a reader's answer; S1 refuses rather than admits.
- perf / scale — S3 adds one `rev-parse` per check-30 run, and a scratch repository only where
  `info/attributes` exists; S7 adds one deviation fixture to the generator's selftest.
- error / empty / loading states — S12 keeps a verb crash in its own section; S6 reads an absent env
  as inheritance; S7's rows each read a non-empty answer.
- observability — S2 keeps the degraded-render notice in check 9's message; S13 prints both counts;
  S3's finding names the file that answered.
- risks — S1 refuses a `none` with a backticked non-sibling token too, the loud direction, with the
  remedy S10 writes; S2 changes stream routing under one flag.
- testing — AC1 to AC16 as probes and fixtures; the arms under §7.
- migration — none: the two corpus `none` payloads carry no backtick after the word
  (`memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md:106`,
  `memory/builds/aQuenchedHarness/spec/2026-09-08-spec-TOOL-aQuenchedHarness-13.md:44`).
- user docs — no page under `help/` covers these engines; the comments S1, S10 and S13 name are
  their documentation.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch repository sits under the session's temp
root with no hook installed.

- **AC1** — When a probe sources `tools/unattended/lib-unattended.sh` and runs
  `read_consumes_from --scan` over four scratch specs whose Edges bullet payloads are `none until`
  then a backticked `ARCH-tRun-1` then prose, bare `none` with dash prose, backticked `none` with dash
  prose, and `none until the reader lands`, it prints one line, the first spec's path and a tab, and
  nothing for the other three; in ids mode it prints nothing for any.
  Red when: the first spec prints nothing, as measured at `072d97f5c`.
- **AC2** — When a probe loads `tools/memory-tree/gen_build_index.py` by path, patches
  `cmd_check_coverage` to write `n29` to `sys.stderr`, `cmd_check_asbuilt` to return 0, and
  `cmd_check` to write `n9` to `sys.stderr` and `drift` to stdout, and calls
  `main(["x", "--check", "--with-verdicts"])` in a child whose stdout and stderr share one pipe, `n29`
  prints between `build-index: verdict 29 exit 0` and `build-index: verdict 30 exit 0`, and `n9` after
  `build-index: verdicts end`.
  Red when: `n29` and `n9` print ahead of the first marker, as measured at `072d97f5c`.
- **AC3** — When a probe makes a scratch repository whose `.gitattributes` names no merge line for
  `v.md`, sets `GIT_CONFIG_GLOBAL` to a scratch config naming a `core.attributesFile` that holds
  `*.md merge=ours`, and calls `asbuilt_view.check_view_merge(root, "v.md")`, the finding names
  `DESIGN_VIEW`; with that global unset and `v.md merge=ours` written to the repository's
  `info/attributes`, the finding names `info/attributes`; with the line in the tracked `.gitattributes`
  alone, it returns None.
  Red when: the global or the `info/attributes` line answers for the view and the check is clean.
- **AC4** — When a probe makes a remote-less scratch repository, exports `GIT_DIR` naming this
  checkout's git directory, and calls `deviation_join.read_decision_ref(<scratch>)`, it returns
  `('main', '')`, and `os.environ["GIT_DIR"]` holds the exported value after the call.
  Red when: it returns `('origin/main', '')`, as measured at `072d97f5c`.
- **AC5** — When a probe copies the Python modules of `tools/memory-tree/` to a scratch directory beside a module holding
  a class `Planted` whose method returns a pathspec constant and a constant `GUARDED` assigned under
  `if True:`, `gen_build_index.scan_glob_readers` over it names `planted23.GUARDED` and
  `planted23.Planted.read_method`; over `tools/memory-tree/` it names the five readers §4 lists.
  Red when: either planted reader is unnamed.
- **AC6** — When the S6 probe runs with `subprocess.run` stubbed and `env=` taken out of a scratch copy
  of `routed_commits.run_git`, it prints `routed_commits leaks inherits`; over the kit's own runners it
  prints `AC1 design_lib leaks [] routed_commits leaks [] second list False`.
  Red when: a runner handed no env prints `leaks []`, as the line at `:1578` reads it at `072d97f5c`.
- **AC7** — When an `ast` probe reads the `probes23` dict of `tools/memory-tree/gen_build_index.py`,
  the lambda under the key `deviation_join.read_population` calls `read_population`, and the lambda
  under `gen_build_index.derive_audit_writers` calls `derive_audit_writers`; neither calls
  `read_adding_commits` directly.
  Red when: a row runs `read_adding_commits` in place of the reader it names.
- **AC8** — When a probe builds `deviation_join.build_fixture(root, [])`, adds the remote and the ref
  S8 states, and calls `deviation_join.measure_fixture`, its result holds `ref` equal to `origin/main`
  and `rows` not None; and a probe of the `owner-unknown-id` plant with the same remote and a run-branch
  row `FIX-dClosedLoop-99` renders a refused line naming `FIX-dClosedLoop-99`.
  Red when: the remote half answers no rows, or a row on the run branch alone approves.
- **AC9** — When `GOV_DEFAULT_BRANCH=trunk python tools/memory-tree/deviation_join.py --fixture --plant rotated --policy refuse`
  runs, it exits 0 and prints no line holding `unread at trunk`.
  Red when: it exits 1 naming `trunk`, as measured at `072d97f5c`.
- **AC10** — When `grep -c 'or the word external or none:\$_c_bad' tools/unattended/unattended.sh` and
  `grep -c 'or the word external or none' tools/unattended/unattended.test.sh` run, the first prints 1
  and the second at least 2, and `grep -c 'or the word external:' tools/unattended/unattended.sh`
  prints 0.
  Red when: the remedy names `external` alone.
- **AC11** — When a probe puts a namesake `design_lib` from a scratch file in `sys.modules`, loads
  `tools/check-spec-tokens.py` by path, and calls `load_design_lib()` twice, both calls return one
  module, `isinstance` of the first's `DesignRefusal("x")` against the second's class is True, and
  `sys.modules["design_lib"]` is still the namesake.
  Red when: the two loads differ, as measured at `072d97f5c` (`same False caught False`).
- **AC12** — When the AC2 probe patches `cmd_check_asbuilt` to raise `KeyError("planted")`, the section
  under `build-index: verdict 30 exit 2` holds `build-index: KeyError:`, and `n9` and `drift` print
  after `build-index: verdicts end`.
  Red when: the exception escapes and `cmd_check` never runs, as measured at `072d97f5c`.
- **AC13** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over the tree, its closure line
  reads `11 sibling module(s) and 2 other scanned file(s)`, and
  `grep -c '2 sibling module(s) and 1 other scanned file(s)' tools/memory-tree/check-verdict-epoch.test.sh`
  prints 1.
  Red when: the line counts the recall kit's extractor and the checker as siblings.
  figure: 13 files scanned and 11 siblings, PINNED by the review at `072d97f5c`.
- **AC14** — When `grep -c -F -- '- **consumes-from** none — it builds on nothing' tools/unattended/unattended.test.sh`
  runs it prints at least 1, and a scratch preflight fixture whose CLOSED sibling declares that bullet
  dispatches its consumer with `dispatch declared`.
  Red when: the bare form reads as unreadable and no plant names it.
  cost: minutes, for the preflight fixture TOOL-dTrueNorth-26 AC8 builds.
- **AC15** — When `grep -c -E '\$HERE"?/memory-tree' tools/check-spec-tokens.test.sh` runs it prints 0,
  and `grep -c '"\$MEMORY_TREE"' tools/check-spec-tokens.test.sh` prints at least 5.
  Red when: a probe of the suite spells the kit's directory literally.
- **AC16** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs after
  the build pass, under the chain's value (`PLAY-dClosedLoop-4`), no `refused:` or malformed line names
  `2026-10-22-build-TOOL-dTrueNorth-31-deviation-33` or `2026-10-22-build-TOOL-dTrueNorth-31-deviation-34`.
  Red when: the dispatch change is recorded nowhere, or a record falls outside the grammar.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `recall floor` · `recall floor arms` · `routed-commits selftest` · `tier2-review self-test` · `memory hygiene` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `install-prefix (shipped surface)` · `kit/dogfood doc parity` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC10 AC14 · a CLOSED sibling's none bullet naming a backticked sibling, the remedy's two literals, and a bare none plant · none
New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC2 AC5 AC7 AC12 · a child whose verbs write to stderr, a class-method and a guarded-constant reader in the planted module, the two rows over readers spawning their own git, and a verb raising KeyError · none
New arm: tools/memory-tree/asbuilt_view.py (its selftest) · covers AC3 · the fixture view with its tracked line emptied and ours answered by a scratch global attributes file, then by info/attributes · none
New arm: tools/memory-tree/deviation_join.py (its selftest, run by the routed-commits selftest) · covers AC4 AC8 AC9 · an exported GIT_DIR naming the host repository, a fixture with an origin remote and a run-branch row, and GOV_DEFAULT_BRANCH=trunk exported around run_fixture · none
New arm: tools/check-spec-tokens.test.sh · covers AC6 AC11 · a runner with env= taken out, and a namesake design_lib raising through one load and caught through a second · none
New arm: tools/memory-tree/check-verdict-epoch.test.sh · covers AC13 · the control fixture's non-sibling file, red against a label counting every scanned file as a sibling · none

S15 has no arm. Its probes are the suite's own lines, and no fixture of the bar renames a kit's
directory: the foreign-prefix legs move the tool root alone (TOOL-dTrueNorth-29 S1), so the only gate
that could red it is the widened install-prefix leg §3 leaves to its own unit. AC15's grep observes it.
README rule 8 waives the unattended suites' verdict at this landing, so the first arm's red-then-green
readings at the close are AC1's, AC10's and AC14's probes, as `TOOL-dTrueNorth-26` §7 states for its
own. The first six legs are the ones the estimate's guards trip; the rest carry the arms and the
gates the touched files feed. `KIT_MEMORY_TREE_VERSION` is minted by the lander for the kit files this
unit moves.

## 8. Open questions

- **F1 — Which mechanism closes M1?** (a) `read_consumes_from` admits `none` only when no backtick
  follows it, S1. (b) A `none` branch in check 12's external-payload arm refusing prose that names a
  sibling, the record's alternative. (c) No change, failing AC1 (veto 1). (a) and (b) each change a
  governance carrier no dTrueNorth clause names, the dispatch edge reader or check 12's Edges arm,
  so veto 2 holds outside the grant. Rung 5 takes the most capable: (a) refuses at the dispatch, where
  the defect admits a consumer, and meets AC1; (b) leaves the dispatch admitting it on any tree the
  hygiene gate has not graded. RESOLVED (agent, 2026-10-22, delegated): (a), citing ER:388
  (`PLAY-dClosedLoop-6`), recorded as deviation-34. widens: the --dispatch verb of
  tools/unattended/unattended.sh reads a consumes-from none followed by a backticked token as
  unreadable · relaxes: none
- **F2 — Does the build's grant lift veto 2 for every other carrier edit here?** S2, S3, S11 and S12
  change the memory-tree kit's verdict machinery for checks 29 and 30, `cl-dClosedLoop-0003`'s and
  `cl-dClosedLoop-0006`'s, with S3's runner keyword in `cl-dClosedLoop-0001`'s `design_lib` and S11
  the carries join's loader, `cl-dClosedLoop-0002`'s; S4, S8 and S9 are `cl-dClosedLoop-0004`'s join
  and its fixture. S5 and S7 change a walk only the generator's selftest calls, S6, S14 and S15 are
  suite arms, and S10 and S13 change a message and no exit. RESOLVED (agent, 2026-10-22, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3, for S2 to S4, S8, S9, S11 and S12; S5 to S7, S10 and S13 to
  S15 change no carrier's behaviour, as `TOOL-dTrueNorth-27` §8 F6 read its message edit. grants:
  PLAY-dClosedLoop-3 the memory-tree kit and checker edits S2 to S4, S8, S9, S11 and S12 make for
  cl-dClosedLoop-0001 to cl-dClosedLoop-0004 and cl-dClosedLoop-0006 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, batching the round-2 closing diff review's 9 MEDIUM and 6 LOW items, findings 3, 6 and 8 from the skeptic's corrected fix, with deviation-33 and deviation-34's text.

## 10. Reuse audit

Every item extends a seam the build already has, read at `072d97f5c`: the `external` and `none` arm of
`read_consumes_from` (`tools/unattended/lib-unattended.sh:354`); the `ladder_env` hold
(`tools/memory-tree/deviation_join.py:1497`, `:1610`), lifted into `set_env_aside` at its second and
third instance; `tree_lib.GIT_ENV_LEAKS` (`tools/memory-tree/tree_lib.py:262-275`);
`design_lib.run_git`'s stripped env; `_read_runner_env23`'s rule that a spawn handed no env inherits
every name (`gen_build_index.py:6283-6298`); the deviation fixture's `build_fixture` and its
`audit-pin` plant (`deviation_join.py:1131-1135`, `:1197-1222`); the TOOL-dTrueNorth-14 audit-writer
fixture (`gen_build_index.py:5984-6023`); and the template-free `git init` the verdict-epoch suite's
`newrepo` uses (`tools/memory-tree/check-verdict-epoch.test.sh:73`). `python tools/codebase-map/reuse_lookup.py
"hold environment variables out of a call and restore them after, so a fixture reads the same answer
whatever the caller exported"` ranked name-stem neighbours, `read`, `read_text`, `export`, `fixture`
and `build_fixture`, none an environment hold, so the hold seam was found by reading
`deviation_join.py:1497`; no existing seam fits an `info/attributes` evaluation, and S3 builds it on
`design_lib.run_git`.

Recall terms used: `python tools/memory-recall/query.py "how does a closing diff review's round-two
minors batch close each finding against the code the build landed" --terms "closing diff review round
two minors none admission stderr capture attributes GIT_DIR ladder fixture hold glob walk"`
