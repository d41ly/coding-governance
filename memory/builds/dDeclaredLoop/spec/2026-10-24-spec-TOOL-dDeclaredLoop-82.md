# TOOL-dDeclaredLoop-82 — the round-5 spec audit's 23 minors, batched

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 41 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-82-deviation-821.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-82-deviation-821.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md`)
exited CONVERGED with 25 confirmed findings over units 76 to 79, the round-4 promotions. Its two highs
are units 80 and 81, one per id. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM
and every LOW, each by its report id and each its own scope item, where the report merged ids into one
item too. The minors land on six units, so this unit repairs none in particular and builds after every
unit (order 41). Where a minor is the medium grade of a defect a high unit closes, the item here is what
that grade's fix asks beyond the high unit's mechanism.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1, 11 | S1, S2 |
| M2 | MEDIUM | 3 | S3 |
| M3 | MEDIUM | 4 | S4 |
| M4 | MEDIUM | 5 | S5 |
| M5 | MEDIUM | 6 | S6 |
| M6 | MEDIUM | 13 | S7 |
| M7 | MEDIUM | 17 | S8 |
| M8 | MEDIUM | 29 | S9 |
| M9 | MEDIUM | 30 | S10 |
| L1 | LOW | 2 | S11 |
| L2 | LOW | 7 | S12 |
| L3 | LOW | 8 | S13 |
| L4 | LOW | 9 | S14 |
| L5 | LOW | 10 | S15 |
| L6 | LOW | 12 | S16 |
| L7 | LOW | 15 | S17 |
| L8 | LOW | 16 | S18 |
| L9 | LOW | 18 | S19 |
| L10 | LOW | 19 | S20 |
| L11 | LOW | 22 | S21 |
| L12 | LOW | 24 | S22 |
| L13 | LOW | 27 | S23 |

That is 10 MEDIUM and 13 LOW findings by raw id. The report's five refuted findings, ids 14, 21, 23, 25
and 26, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 1. Outside `TOOL-dDeclaredLoop-80`'s fixture boundary, `derive_conf_reads` also counts a
  `Name` or `Attribute` whose identifier is bound at module level in `tools/loop/loop_lib.py` to a
  string constant naming a conf, reached through `import loop_lib`, `from loop_lib import <name>` or
  either aliased, as kind `conf constant`. Those bindings are read by parsing `loop_lib.py`, never by
  importing it. A read inside the boundary is still passed over. Observed by AC1.
- **S2** — id 11. `TOOL-dDeclaredLoop-76` §4 Evidence lists the conf-writing plants inside the two
  modules, 60 AC2, 64 AC1, 72 S4, 76 AC3, 75 S6, 79 AC20 and AC25, and says they sit inside 80's
  boundary; its rejected alternative names S1's cross-module constant. The edit is a rev bump of 76
  with its §9 line. Observed by AC2.
- **S3** — id 3. `TOOL-dDeclaredLoop-77` AC4's observation reaches the mismatch skip line: the
  `url-forms` plant writes a non-empty `FETCH_HEAD` whose one line names the default branch of
  `https://other.example/r`, under a remote configured as `https://u:SECRET@127.0.0.1:9/r.git`, and
  runs the reading with no fetch. Neither the `skipped — no line for` line nor the `--explain` read-set
  carries `SECRET`. Observed by AC3.
- **S4** — id 4. `TOOL-dDeclaredLoop-75` S27's body is restated, as a rev bump of 75 with its §9 line:
  on exit 1 with the policy path outside the conflicted paths, C is 78's `present` or `absent`, or
  refused by 78 S3, in place of "its blob parses". The plant
  `push-merge-resurrect-deleted-policy-conflict-elsewhere` joins `guard.py --fixture`: main's tip lacks
  the policy file, a run branch that never touched it conflicts with main on another file, and the
  resolution keeps the run branch's policy bytes with no trailer. Observed by AC4.
- **S5** — id 5. `TOOL-dDeclaredLoop-79` S18's population is re-derived at this pass: every leg whose
  guard holds `{prefix}/loop/`, at least `loop breakpoints fixtures` (79 S8) and `loop selftest` (75
  S21). Each spec under this build's `spec/` folder that is not CLOSED or WONTDO and whose Files touched
  trips one names it on its §7 leg line, amended as a rev bump with its §9 line, this unit included; 79
  S18 and AC18 are widened to both legs and 79's own leg line gains both. Observed by AC5.
- **S6** — id 6. The pass-commit probe, 79 S26's route, records `leg absent at pass commit` as its own
  ledger line where `derive_leg_argv` finds no manifest row for the leg at a unit's pass commit, then
  runs that leg at the earliest later pass commit holding the row. 79 AC10's probe at 72's pass commit,
  whose leg 71 mints at the same order with no edge between them, is re-observed this way, and 79 S10
  is amended to say so. Observed by AC6.
- **S7** — id 13. 79's `sed-fails` plant puts its stub first on the bash's own PATH from inside that
  bash: it sets `BASH_ENV` to a scratch file that prepends the stub directory, spelled through
  `cygpath -u` where that resolves. Before the run it asserts that `command -v sed` in the bash
  `resolve_bash` answers names the stub, and exits non-zero naming that bash where it does not.
  Observed by AC7.
- **S8** — id 17. `derive_docstring_ids(tree)` in `tools/memory-tree/tree_lib.py` answers the ids of the
  docstring constants of the module and of every `ClassDef`, `FunctionDef` and `AsyncFunctionDef`.
  `scan_glob_readers` (`tools/memory-tree/gen_build_index.py:5146`) and `derive_conf_reads` both call
  it, and neither builds its own set. Observed by AC8.
- **S9** — id 29. The plant `push-merge-unparseable-parent` joins `guard.py --fixture`: an octopus merge
  one of whose parents holds a policy blob that does not parse, refused as
  `does not parse at parent <sha8>` with no traceback. 78 S4 lists it beside `push-merge-unparseable-c`
  (S13), as a rev bump of 78. Observed by AC9.
- **S10** — id 30. `derive_conf_reads` counts a non-docstring string constant that contains either conf
  name anywhere, not only at its end, and resolves a call's name through the module's `import ... as`
  and `from ... import ... as` aliases, by `derive_import_aliases(tree)`, before matching `parse_conf`
  or `read_driver_conf`. Observed by AC10.
- **S11** — id 2. `TOOL-dDeclaredLoop-72` AC4 is amended in place, as a rev bump of 72 with its §9
  line: its observation is 76 AC1's `no-own-conf-read` plant, and its text holds no substring grep.
  Observed by AC11.
- **S12** — id 7. `TOOL-dDeclaredLoop-78` AC2 is kept as a regression arm: its `Red when` names the break
  it catches, an empty `present` C mapped to `uncomputable`, and 78 §7's arm line records that 69
  already grades the emptied case. The edit is a rev bump of 78. This unit's §7 stages that break.
  Observed by AC12.
- **S13** — id 8. 78 S4's plant list names `push-merge-unparseable-c`, observed by 78 AC4, in the same
  rev bump as S9 and S12. Observed by AC13.
- **S14** — id 9. Step 39's shared write is recorded and observed: 77 §4 names
  `tools/loop/position.py` as written by `TOOL-dDeclaredLoop-75` too, dispatched in sequence (a rev
  bump of 77), and the build README's build-order region, rendered at this pass by
  `TOOL-dDeclaredLoop-66`'s `render_order`, prints step 39's Parallel cell opening `no`.
  Observed by AC14.
- **S15** — id 10. `resolve_memory_root_source` names a source for each of 72 S1's four branches: the
  conf whose branch answered, so `.unattended.conf` where it exists with or without `MEMORY_ROOT`,
  `.memory-tree.conf` where only it exists with or without the key, and `default` only where neither
  exists. 76 AC3's `root-source` plant gains the two unset-key trees. Observed by AC15.
- **S16** — id 12. 76 §4's rule names `ClassDef`, `FunctionDef` and `AsyncFunctionDef`, in S2's rev
  bump of 76, and the `conf-read-forms` plant's docstring-only module holds an `async def` whose
  docstring names `.unattended.conf`. Observed by AC16.
- **S17** — id 15. 77 S2's shim path reaches `GIT_SSH_COMMAND` through `Path.as_posix()`, in
  `position.py` and in 77 S2's text, in S14's rev bump of 77. Observed by AC17.
- **S18** — id 16. 77 §5's risk sentence says a scheme URL whose user part holds `/` or a second `@`
  normalises equal on both sides by git's first-`@` rule, and 77 §4's port-9 sentence is restated to
  S3's no-fetch plant, in S14's rev bump of 77. Observed by AC18.
- **S19** — id 18. 77 §10 weighs `norm_endpoint` (`tools/unattended/unattended.sh:1117`) and the runlog
  `url-userinfo` row (`tools/runlog/redaction.tsv:23`) and says why neither serves, in S14's rev bump of
  77; the `url-forms` table gains `norm_endpoint`'s regression pairs, `github.com:alice/repo` against
  `github.com:bob/repo` unequal and `git@github.com:alice/repo` against `github.com:alice/repo` equal.
  Observed by AC19.
- **S20** — id 19. 79 AC11 observes the held-leg predicate where the FORWARD arm of
  `tools/run-gates/run-selftests.sh` owns it, by extracting that arm's heredoc, and keeps its
  `grep -c "loop breakpoints fixtures"` pin; its typed predicate is no part of the amended text. The
  edit is in S5's rev bump of 79. Observed by AC20.
- **S21** — id 22. 79 §7's sibling-leg paragraph names `loop definition fixtures` and `loop selftest`,
  and 77 §7's names `loop selftest`, in the rev bumps above. The pass-commit probe runs `loop selftest`
  at 77's pass commit, and `loop definition fixtures` at the pass commit of each unit ordered at or
  after 67 whose Files touched names `tools/loop/loop_lib.py`, that population derived from the specs
  at this pass and S6's absent-leg line covering a tie. Observed by AC21.
- **S22** — id 24. 79 S17 names what its trim may not touch, the paragraph ending `in run order:`, the
  paragraph ending `PASS kinds:` and the Definition-of-Done table rows, which
  `tools/unattended/check-unattended.sh` arms D and E read, and 79 §7 names `unattended kit gate` and
  `unattended skill wiring`, in S5's rev bump of 79. Observed by AC22.
- **S23** — id 27. The `url-forms` plant derives one expectation from git itself: it serves a scratch
  bare repository over git's dumb HTTP protocol from `http.server` on `127.0.0.1` at a free port, after
  `git update-server-info`, configures the remote as `http://user:tok@127.0.0.1:<port>/r.git`, fetches,
  and asserts that `normalise_fetch_url` of the configured URL equals the URL git wrote into
  `FETCH_HEAD`. The hand-typed https rows stay as regressions. Observed by AC23.

## 3. Non-goals (OUT)

- The two highs' mechanisms: units 80 and 81, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 14, 21, 23, 25 and 26.
- A TLS endpoint for S23: git's anonymiser is one rule for every scheme (77 S1), and a certificate in a
  fixture is a surface this unit does not price.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-72` — AC4, amended in place to observe through the `no-own-conf-read` plant (id 2)
- **consumes-from** `TOOL-dDeclaredLoop-75` — S27's exit-1 body (id 4), S21's `{prefix}/loop/` guards (ids 5, 22) and its share of `tools/loop/position.py` at step 39 (id 9)
- **consumes-from** `TOOL-dDeclaredLoop-76` — `derive_conf_reads`, `resolve_memory_root_source`, the `root-source` plant and §4 (ids 1, 10, 11, 12, 17, 30)
- **consumes-from** `TOOL-dDeclaredLoop-77` — `normalise_fetch_url`, the `url-forms` plant, the `GIT_SSH_COMMAND` shim and §4, §5, §7 and §10 (ids 3, 9, 15, 16, 18, 22, 27)
- **consumes-from** `TOOL-dDeclaredLoop-78` — S4's plant list, AC2 and S3's refusal (ids 4, 7, 8, 29)
- **consumes-from** `TOOL-dDeclaredLoop-79` — S10's probe, S17's trim, S18's population, the `sed-fails` plant and AC11 (ids 5, 6, 13, 19, 22, 24)
- **consumes-from** `TOOL-dDeclaredLoop-80` — the fixture boundary, outside which S1 counts a conf constant read by name (ids 1, 11)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the clean re-merge's exit table, beside which S4 restates S27's exit-1 body (id 4)

## 4. Design

### Write set

This pass writes the tools below. Inside this build's folder it amends the specs of 72, 75, 76, 77, 78
and 79 as rev bumps, each with its §9 line (S2, S4, S5, S6, S9, S11 to S14, S16 to S22), and its own §7
leg line where S5 finds it tripped; the build README's regions are the generator's render. S6 and S21
observe and record and write no code.

### The conf-read rule, after this unit (S1, S8, S10)

```
derive_conf_reads(path):
    tree    = ast.parse(read(path))
    docs    = tree_lib.derive_docstring_ids(tree)           # Module, ClassDef, FunctionDef, AsyncFunctionDef
    bounded = 80 S1's fixture boundary
    aliases = derive_import_aliases(tree)                   # local name -> imported name
    consts  = module-level str bindings in loop_lib.py naming a conf, read by ast.parse
    for node outside docs and bounded:
        Call whose resolved callee is parse_conf or read_driver_conf    -> (line, "reader call")
        Constant str containing ".memory-tree.conf" or ".unattended.conf" -> (line, "conf name")
        Name or Attribute resolving to a member of consts               -> (line, "conf constant")
```

### Evidence

- `scan_glob_readers` builds its docstring set over `ast.Module`, `FunctionDef`, `AsyncFunctionDef` and
  `ClassDef` (`tools/memory-tree/gen_build_index.py:5146`, the set at :5191-5194); a grep for
  `get_docstring` and `body[0].value` across `tools/` finds that set and one selftest helper (:6313),
  read 2026-10-24. 76 §4's rule names only `ClassDef` and `FunctionDef`.
- `resolve_bash` takes the first `bash.exe` on PATH outside System32 and WindowsApps
  (`tools/govkit/govkit.py:1184-1195`). Probed 2026-10-24 on node `d`: a sed stub placed only in the
  inherited PATH was bypassed by `Git/bin/bash.exe`, which ran `/usr/bin/sed`; a `BASH_ENV` file
  prepending the stub directory, written through `cygpath -u`, reached the stub from both
  `Git/bin/bash.exe` and `Git/usr/bin/bash.exe` when spawned from Python: PINNED, that date.
- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1 and Python 3.14: `git fetch` from
  `http://user:tok@127.0.0.1:<port>/r.git`, served by `python -m http.server` over a bare repository
  after `git update-server-info`, wrote `branch 'main' of http://127.0.0.1:<port>/r` into `FETCH_HEAD`,
  and `http://user@127.0.0.1:<port>/r.git/` wrote the same: PINNED, that date.
- `norm_endpoint` (`tools/unattended/unattended.sh:1117-1140`) drops the scheme and the port and folds
  host case; the runlog row `url-userinfo` (`tools/runlog/redaction.tsv:23`) masks a credential.
- The FORWARD arm of `--check` holds the held-leg predicate in the heredoc opened on its `missing=$(`
  line (`tools/run-gates/run-selftests.sh:826`).
- Arms D and E read the template's paragraph ending `in run order:`
  (`tools/unattended/check-unattended.sh:3724`), the paragraph ending `PASS kinds:` (:3742) and the
  Definition-of-Done rows `| `<item>` |` (:3765).
- `check_guard_trips(path, guard)` takes one guard string (`tools/check-spec-tokens.py:581`).

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `tools/loop/position.py`
- `tools/loop/loop_witness.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the conf-read rule and the rest.** The halves are not disjoint by M6 clause 2: S5's
  probe reads every live spec's §7 and Files touched as an acceptance input, 76's included, which S2
  and S16 write; and both halves write `tools/loop/loop_lib.py` (S1, S10, S15).
- **Extracting the whole of `scan_glob_readers`' walk with a predicate (the fix's wider form).** Its walk
  carries the charge rule's scope tracking, which `derive_conf_reads` has no use for; the docstring set
  is the part both walks share, so S8 extracts that.
- **A `CGIHTTPRequestHandler` behind `git http-backend` for S23.** That handler is deprecated in the
  Python 3.14 this node runs; the dumb protocol over `http.server` needs no CGI and was probed.

## 5. Production-readiness checklist

- security — S1 and S10 widen what the no-own-conf-read rule sees; S3 and S23 keep a planted credential
  off every printed line; S23 binds `127.0.0.1` only, at a free port.
- perf / scale — S23 costs one local HTTP server and one fetch, seconds; S6 and S21 cost one scratch
  worktree per probed commit, once at this pass.
- error / empty / loading states — S6 names an absent leg instead of failing or skipping it; S7 names the
  bash its stub could not reach.
- observability — each probe exit is a ledger line; S1's hits name their kind.
- risks — the amendments land on specs whose units are built, as 79 S18 and S24 amend theirs; each is a
  rev bump with its §9 line, and none moves a built criterion's verdict except 72 AC4's, which 76 S4
  already records against 76 AC1.
- testing — AC1 to AC23 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, its row
  reading `(tree / ll.UNATTENDED_CONF).read_text()` after `import loop_lib as ll`, over a scratch
  `loop_lib.py` binding `UNATTENDED_CONF = ".unattended.conf"`, answers one `conf constant` hit, and the
  same line inside a function named `check_plant_root` answers none.
  Red when: a name bound to a conf in `loop_lib.py` reads as no read outside the boundary.
- **AC2** — When `grep -c "unset-driver-root"` and `grep -c "trailing-slash-agree"` run over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md`, each prints at least 1.
  Red when: 76 §4 Evidence still names only 75's docstrings and printed lines.
- **AC3** — When `python position.py --fixture --plant url-forms` runs, its output holds a line opening
  `skipped — no line for main of` and no line holding `SECRET`; with the skip line staged to print the
  configured URL, a line holding `SECRET` appears.
  Red when: the plant's fetch fails, the reading prints `skipped — empty`, and the URL-printing path is
  never reached.
- **AC4** — When `python guard.py --fixture --plant push-merge-resurrect-deleted-policy-conflict-elsewhere`
  runs, it exits 1 naming each key M holds, and `grep -c "its blob parses"` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md` prints 0.
  Red when: an absent C at exit 1 falls to the parents and the exemption skips the merge.
- **AC5** — When a probe loads `tools/check-spec-tokens.py` by `importlib` and, for each spec under
  this build's `spec/` folder that is not CLOSED or WONTDO, applies `check_guard_trips` to each path of
  its Files touched against the guards of the `loop selftest` and `loop breakpoints fixtures` rows of
  `tools/gate-legs.json`, with `{prefix}` read as `tools`, every spec that trips a leg names it on its §7
  leg line, and 79's leg line names both.
  Red when: a live spec declaring a loop path lacks `loop selftest` on its leg line.
- **AC6** — When the pass-commit probe runs for 72's pass commit, its ledger line names either the exit
  of `loop breakpoints fixtures` there or `leg absent at pass commit` followed by that leg's exit at the
  earliest later pass commit holding its row, and every recorded exit is 0.
  Red when: an absent row is recorded as a failure, or skipped with no line.
  cost: one scratch worktree per probed commit.
- **AC7** — When `python loop_witness.py --fixture --plant sed-fails` runs with Git for Windows'
  launcher bash, the one in its `bin` folder, resolved first on PATH, it exits non-zero printing
  `witness: normaliser unavailable — sed:`, and with `BASH_ENV` unset by a staged break it exits
  non-zero naming the bash whose `command -v sed` missed the stub.
  Red when: the stub sits only in the inherited PATH and the launcher's own sed runs.
  fixture: a node with Git for Windows; elsewhere the resolved bash is the plain one and both halves
  read the stub.
- **AC8** — When a `python -c` probe imports `tree_lib` from `tools/memory-tree/` and calls
  `derive_docstring_ids` on a module whose `async def` opens with a docstring, the answer holds that
  docstring's id, and `awk '/^def scan_glob_readers/,/^def cmd_selftest/' gen_build_index.py` in
  `tools/memory-tree/` piped to `grep -c "body\[0\]"` prints 0.
  Red when: either walk keeps its own docstring set, or the async scope is missing.
- **AC9** — When `python guard.py --fixture --plant push-merge-unparseable-parent` runs, it exits 1
  printing `does not parse at parent ` and no `Traceback`.
  Red when: the uncomputable branch skips the merge or raises on the unparseable parent.
- **AC10** — When `--plant conf-read-forms` runs its rows for a bash `-c` string sourcing
  `"$ROOT/.unattended.conf"` before a `printf`, and for `rdc(tree, ["MEMORY_ROOT"])` after
  `from loop_lib import read_driver_conf as rdc`, each answers one hit, `conf name` and `reader call`.
  Red when: only a trailing conf name counts, or an alias hides the reader.
- **AC11** — When `grep -n '^- \*\*AC4\*\*'` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md`, the line it prints holds
  `no-own-conf-read` and not `grep -c`.
  Red when: 72 AC4 still asks for the substring count, so a literal re-run at the close reads red.
- **AC12** — When `python guard.py --fixture --plant push-merge-resurrect-emptied-policy` runs, it exits 1
  naming each key M holds; with an empty `present` C staged to map to `uncomputable`, it exits 0.
  Red when: the arm stays green under that break, so it adds no evidence for the state split.
- **AC13** — When `awk '/^- \*\*S4\*\*/,/^## 3/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md` is piped to
  `grep -c "push-merge-unparseable-c"`, it prints at least 1.
  Red when: the plant 78 AC4 runs is still introduced by no scope item.
- **AC14** — When `grep -n "^| 39 |"` runs over `memory/builds/dDeclaredLoop/README.md` at this pass,
  the Parallel cell opens `no`, and `grep -c "position.py.*TOOL-dDeclaredLoop-75"` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-77.md` prints 1.
  Red when: step 39 still reads `yes` over two units sharing a file.
- **AC15** — When `python budget.py --fixture --plant root-source` runs, the tree holding
  `.unattended.conf` without `MEMORY_ROOT` answers `(memory, .unattended.conf)` and the tree holding
  `.memory-tree.conf` alone without the key answers `(memory, .memory-tree.conf)`, beside 76 AC3's three.
  Red when: an unset key's source is left to the builder and reads `default` in one tree only.
- **AC16** — When `--plant conf-read-forms` runs its docstring-only module, which holds an `async def`
  whose docstring names `.unattended.conf`, it answers no hit, and `grep -c "AsyncFunctionDef"` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md` prints at least 1.
  Red when: an async docstring reads as a conf name.
- **AC17** — When `grep -n "GIT_SSH_COMMAND" position.py` runs in `tools/loop/`, every line it prints
  holds `as_posix()`.
  Red when: the shim path is written as `str()` of a Windows path and sh eats its backslashes.
- **AC18** — When `grep -c "at once"` and `grep -c "reads skipped, the conservative"` run over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-77.md`, each prints 0.
  Red when: 77 still claims a fallback that does not exist or a cost it does not have.
- **AC19** — When `--plant url-forms` runs, `github.com:alice/repo` against `github.com:bob/repo` reads
  unequal and `git@github.com:alice/repo` against `github.com:alice/repo` reads equal, and
  `grep -c "norm_endpoint"` over the 77 spec prints at least 1.
  Red when: the scp regression pairs `norm_endpoint`'s comment records are absent from the table.
- **AC20** — When `sed -n "/^  missing=\$(/,/^PY$/p" tools/run-gates/run-selftests.sh` is piped through
  `sed '1d;$d'` to `python - tools/run-gates/selftest-budgets.txt tools/gate-legs.json`, it prints no
  line opening `loop `, and the AC11 bullet of
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md` names that heredoc.
  Red when: a held loop leg lacks a budget row, or 79 AC11 still types the predicate.
- **AC21** — When this unit's acceptance ledger is read, it holds a `loop selftest` exit line for 77's
  pass commit and a `loop definition fixtures` exit or absent-leg line for each derived unit, every exit
  0, and `grep -c "loop selftest"` over the 77 spec prints at least 1.
  Red when: a pass broke the kit self-test or the definition fixtures and nothing attributed it.
- **AC22** — When the three extractions of `tools/unattended/check-unattended.sh:3724`, :3742 and :3765
  are applied to `tools/unattended/PROTOCOL.template.md` and to its blob at base `ed497191`, each pair
  of sets is equal and non-empty, and `grep -c "unattended kit gate"` over the 79 spec prints at least 1.
  Red when: the trim took a parsed anchor and only the size row was read.
- **AC23** — When `--plant url-forms` runs, it prints a `git-written` row whose configured URL, carrying
  the user part `user:tok@`, normalises equal to the URL `git fetch` wrote into `FETCH_HEAD`; with
  `normalise_fetch_url` staged to keep the user part, that row reads unequal.
  Red when: the only https oracle is a table typed from the same reading S1 implements.
  cost: one local HTTP server and one fetch, seconds.

## 7. Gates

`recall floor` · `recall floor arms` · `tier2-review self-test` · `build-index selftest` · `unattended kit gate` · `unattended skill wiring` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop position fixtures`, the leg `loop guard fixtures`, the leg
`loop computed witness`, the leg `loop definition fixtures` and the leg `loop selftest`, none of them a
leg at HEAD; S5 puts the last on this line once it resolves.

New arm: tools/loop/budget.py · covers AC1 AC10 AC15 AC16 · the conf-read-forms table and the two unset-key root-source trees, staged against 76's trailing-only, alias-blind rule · none
New arm: tools/loop/guard.py · covers AC4 AC9 AC12 · the conflict-elsewhere deleted-policy and unparseable-parent plants, and the emptied-policy plant staged with an empty present C mapped to uncomputable · none
New arm: tools/loop/position.py · covers AC3 AC19 AC23 · the mismatch-line SECRET row, the scp regression pairs and the git-written http row, each staged as its criterion's Red when · none
New arm: tools/loop/loop_witness.py · covers AC7 · the sed-fails plant under Git's bin/bash.exe launcher, staged with BASH_ENV unset · none
New arm: tools/memory-tree/gen_build_index.py · covers AC8 · the glob-reader arm gains an async docstring holding the pathspec, staged against a docstring set without AsyncFunctionDef · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which source does an unset key name (id 10)?** (a) the conf whose branch answered; (b) `default`
  wherever the value is the driver's default. (b) prints `default` for a tree whose `.unattended.conf`
  exists and decides the root, hiding which file to edit; (a) names that file, and is the skeptic's sound
  fix. RESOLVED (agent, 2026-10-24, delegated): (a), S15. widens: none · relaxes: none
- **F3 — Re-observe 79 AC10 at 72's commit by an absent-leg line, an edge 72 <- 71, or a lower order for
  71 (id 6)?** An edge or an order written now would amend 71 and 72 outside this disposal's mirror
  bullets, and both build before this unit; the absent-leg line is observable at this pass and keeps
  every exit recorded. RESOLVED (agent, 2026-10-24, delegated): the absent-leg line, S6.
  widens: none · relaxes: none
- **F4 — Name the fixture conf through a loop_lib constant only, or count such a constant outside the
  boundary too (id 1)?** Counting it is M1's negative case and the only form that closes the
  `loop_lib.UNATTENDED_CONF` read M1 describes. RESOLVED (agent, 2026-10-24, delegated): count it, S1.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-5 spec audit's 23 minors batched (10 MEDIUM, 13 LOW).

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 76's `derive_conf_reads` and
80's boundary (S1, S10), the memory-tree kit's docstring set lifted out of `scan_glob_readers` into
`tree_lib.py` (S8), 76's `resolve_memory_root_source` (S15), 77's `normalise_fetch_url` and its
`url-forms` table (S3, S19, S23), 78's states and plants (S4, S9, S12, S13), 79's pass-commit probe on
the run-gates kit's `add_scratch_worktree` and `derive_leg_argv` (S6, S21), the run-selftests FORWARD
arm read in place (S20) and `check_guard_trips` (S5).
`python tools/codebase-map/reuse_lookup.py "collect the docstring nodes of a parsed python module"`
ranked `parse`, `parse_conf` and `parse_spec_h1`, none a docstring walk; the grep for docstring-id
walkers found `gen_build_index.py:5191`, the seam S8 extends.
`"resolve import aliases of a parsed python module"` ranked `parse`, `resolve` and `resolve_kit_dir`,
none an alias map, so no existing seam fits `derive_import_aliases`.
`"serve a git repository over http for a fetch fixture"` ranked `git`, `fixture`, `build_fixture` and
`run_git`, none serving a repository, so no existing seam fits S23's server.

Recall terms used: spec-audit minors batch derive_conf_reads docstring AsyncFunctionDef url-forms FETCH_HEAD oracle sed stub pass-commit probe
