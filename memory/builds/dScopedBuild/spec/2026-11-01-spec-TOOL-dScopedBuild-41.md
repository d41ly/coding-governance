# TOOL-dScopedBuild-41 — the round-1 audit of units 36 to 39, its 22 minors batched: 10 MEDIUM and 12 LOW findings, each its own scope item

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 18 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 |
| [2026-11-01-prompt-TOOL-dScopedBuild-40-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-40-promoted-fix-brief.md) | research | TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 39
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md`)
exited CONVERGED with 23 confirmed findings. One is at HIGH, and `TOOL-dScopedBuild-40` takes it. The
other 22 are minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, and §4 "Why one
unit" says why these stay one. Each finding is named by report id and is its own scope item. That
includes the ids the report merged into one item (M1, L9), each of which takes that item's severity.
The minors land on units 36 to 39, so this unit repairs no one unit and builds after every unit of
the build (order 18).

| Report item | Severity | Report id | Lands on | Scope item | Built by |
|---|---|---|---|---|---|
| M1 | MEDIUM | 1 | unit 39 S22, AC17 | S1 | units 36, 39 |
| M1 | MEDIUM | 21 | unit 39 S22, AC17 | S2 | units 36, 39 |
| M2 | MEDIUM | 2 | unit 39 S27, AC20 | S3 | unit 30's ledger |
| M3 | MEDIUM | 3 | unit 39 S16, AC13 | S6 | observed only |
| M4 | MEDIUM | 10 | unit 39 S12, AC10 | S7 | unit 39 |
| M5 | MEDIUM | 17 | unit 39 AC4, AC5 | S8 | observed only |
| M6 | MEDIUM | 18 | unit 39 S8, S9 | S9 | units 4, 7 |
| M7 | MEDIUM | 19 | unit 36 §4, §7 | S10 | unit 36 |
| M8 | MEDIUM | 25 | unit 37 AC2 | S11 | observed only |
| M9 | MEDIUM | 26 | unit 39 S18, AC14 | S12 | unit 39 |
| L1 | LOW | 4 | unit 38 S1, S3 | S13 | unit 40 |
| L2 | LOW | 5 | unit 38 §3; unit 5 S2 | S14 | unit 5's ledger |
| L3 | LOW | 6 | unit 37 S1, S3, §5 | S15 | unit 37 |
| L4 | LOW | 7 | unit 39 S15, §10 | S16 | text only |
| L5 | LOW | 8 | unit 38 S2, AC1, AC3 | S17 | observed only |
| L6 | LOW | 9 | unit 39 S29, AC21 | S18 | observed only |
| L7 | LOW | 11 | unit 39 S28 | S19 | unit 29's ledger |
| L8 | LOW | 13 | unit 39 §4 Evidence | S20 | text only |
| L9 | LOW | 14 | unit 39 AC20 | S4 | unit 30's ledger |
| L9 | LOW | 23 | unit 39 AC20 | S5 | unit 30's ledger |
| L10 | LOW | 15 | unit 38 §1, §4 | S21 | text only |
| L11 | LOW | 22 | unit 37 §1, §3 | S22 | this unit |

That is 10 MEDIUM and 12 LOW findings by raw id. Every item supersedes or completes a clause of the
unit it lands on by name. That unit's §3 names this unit, and its acceptance ledger answers the
clause with a note naming this unit's scope item.

## 2. Scope (IN)

- **S1** — id 1. One checkout for every `build_fixture` tree a leg writes into.
  `routed_commits.build_fixture` (`tools/memory-tree/routed_commits.py:385`) gains a keyword,
  `checkout=False`. When it is True, the function runs `git reset -q --hard` through `run_git`
  (`:86`) after the fast-import, so the tree's index and working tree hold HEAD. Unit 36's builder
  adds it and calls it for unit 36 S1's two fixtures in place of a reset of their own. Unit 39's
  builder calls it, as `build_fixture(..., checkout=True)`, for S22's two trees, whose commits
  carry unit 36 S1's tracked `tFix` `BACKLOG.md` and the slug README the filer reads (`readme_of`, `tools/unattended/unattended.sh:1348`).
  Unit 39 AC17 reads the staged set by `git diff --cached --name-only`. §8 F2. Observed by AC1 and
  AC2.
- **S2** — id 21. The same checkout closes id 21, the blast-radius lens's statement of the
  index-noise read: `write_ask_rows` runs `GIT add` into whatever index exists (`unattended.sh:9994`).
  Observed by AC2.
- **S3** — id 2. Unit 39 AC20 is superseded by AC3, which reads unit 30's acceptance ledger for the
  note unit 39 S27 rules: its `**Evidences:** TOOL-dScopedBuild-30` block names
  `TOOL-dScopedBuild-39 S27`. The pinned 50 stays S27's evidence and the figure that note records.
  Observed by AC3.
- **S4** — id 14. The same read closes id 14: AC20's command reads the immutable `c891f007` and
  cannot fail. Observed by AC3.
- **S5** — id 23. The same read closes id 23, the blast-radius lens's statement of it. Observed by
  AC3.
- **S6** — id 3. Unit 39 AC13 also asserts presence. Each of `.githooks/pre-commit`,
  `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md` holds `--diff-filter=ACMRD` at least once,
  and each of the two docs holds unit 39 S16's line that a deletion runs the leg so check 32 sees it.
  Observed by AC4.
- **S7** — id 10. Unit 39 AC10's first plant is named by form. On Windows its stub is a `.cmd`
  wrapper, which CreateProcess starts. On POSIX it is a `#!` script. The plant asserts the line the
  dispatch-row spawn's non-zero exit prints, and the absence of the `corpus_ids` line
  `GOV_BASH is set to` (`tools/memory-tree/corpus_ids.py:416`). Unit 39's builder builds the arm in
  this form. Observed by AC5.
- **S8** — id 17. Unit 39 AC4's and AC5's named-reader greps are superseded by a call-site read. An
  `ast` walk counts `Call` nodes named `read_policy_value` whose first argument is the key literal.
  Their `"get"` absence halves stand. Observed by AC6.
- **S9** — id 18. The write sets unit 39 S8 and S9 hand out are declared where they are graded.
  Before building S3's `--unit-commits` mode, unit 4's builder adds
  `tools/memory-tree/routed_commits.py` to unit 4's Files touched by a rev bump. Before building S5's
  `TYPED_RECORD_KINDS` member, unit 7's builder adds `tools/memory-tree/tree_lib.py` to unit 7's
  Files touched and `policy fixtures` to its §7 by a rev bump. `design_lib.read_spec_writes`
  (`tools/memory-tree/design_lib.py:528`) is what unit 3's scope arm and unit 5's lease read.
  Observed by AC7.
- **S10** — id 19. Unit 36's map. Before building `read_backlog_state`, unit 36's builder adds
  `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write`, to unit 36's Files
  touched by a rev bump. Its §7 gains `codebase-map coverage + freshness`,
  `lexicon naming predicates`, `recall floor` and `recall floor arms`. The last two are the legs the
  symbols file's guard trips. Observed by AC8.
- **S11** — id 25. Unit 37 AC2 also asserts that `$hk` is non-empty and holds `GATE_REGEN_CHECK`, so
  a cut of the hook that reads nothing turns it red. Observed by AC9.
- **S12** — id 26. A failed adapter load, stated as the class. In
  `tools/codebase-map/reuse_check.py`, any exception raised while resolving or loading the adapter
  is the CLI's exit 2 with the one line naming `memory-tree/policy_value.py`. So is a loaded module that lacks `read_policy_value`. This
  supersedes unit 39 S18's `LookupError` and `ImportError` pair. Unit 39's builder builds S18 in
  this form. Observed by AC10.
- **S13** — id 4. A path under a nested entry. With `["src/", "src/core/"]`, `src/core/x.py` reduces
  to itself. Unit 40 S1's guard builds it, because `src/core/` equals an entry. Observed by AC11.
- **S14** — id 5. Unit 38 S2's `read_unit_writes(unit, spec_text, run_rows, tracked, entries)`
  supersedes unit 5 S2's four-parameter spelling
  (`memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-5.md:39`) by name. Unit 5's acceptance ledger
  answers AC3, the criterion its S2 names first, with a note naming `TOOL-dScopedBuild-41 S14`.
  Observed by AC3.
- **S15** — id 6. Unit 37 S3's `gates-green` change is observed. Unit 37's builder extends the
  driver suite's TOOL-aFrugalTurnstile-12 AC1/AC2 arm (`tools/unattended/unattended.test.sh:12078-12085`)
  with `GATE_REGEN_CHECK=0` exported, its bar stub recording the knob. S1's required comment is
  grepped. This supersedes unit 37 S3's and §5's "observed by AC1". Observed by AC12.
- **S16** — id 7. Unit 39 S15's and §10's cites are superseded. The `RB_BOUND` sets are at
  `unattended.sh:11263` and `:11276`, and the clears at `:11271` and `:11280`. NOT OBSERVED: a
  corrected citation has no behaviour, §4 Evidence pins the four lines at `62d7511a`, and S15's
  bound is unit 39 AC12's.
- **S17** — id 8. Unit 38 S2's two unobserved halves. The `--kit-dir` CLI exits 2 naming
  `ROUTED_PATHS` when `check_conf` refuses a blank one (`routed_commits.py:142-143`). The touch join
  receives the write set reduced with `entries`. Observed by AC13.
- **S18** — id 9. Unit 39 AC21 is superseded by AC14. AC14 defines BASE as `f4597719`, the header's
  base, and reads every commit that edits `tools/policy/check_policy.py`, not only unit 26's.
  Observed by AC14.
- **S19** — id 11. Unit 39 S28's rationale is respelled. `tools/run-gates/regen.py` resolves
  `{prefix}`: its `TOKENS` (`:48`) are applied by `resolve_argv` (`:125-137`) with the context built
  at `:176` to each row's argv (`:188-190`). It rewrites `python` to `sys.executable` at `:273`. It
  resolves no alias. The conclusion that the three rules differ stands. Unit 29's acceptance ledger
  carries the respelled rationale with a note naming `TOOL-dScopedBuild-41 S19`. Observed by AC3.
- **S20** — id 13. Unit 39 §4's diff-filter Evidence is spelled with AC13's pathspec,
  `-- .githooks tools/memory-tree/README.md WIRE-INTO-PROJECT.md`, which prints the three lines. The
  hygiene gate's own read at `tools/memory-tree/check-memory-hygiene.sh:664` stays ACMR by design
  (unit 39 S23). NOT OBSERVED: an evidence spelling has no behaviour, and AC4 reads the files it
  describes.
- **S21** — id 15. Unit 38 §1's and §4's conf evidence is respelled. The kit's conf example
  documents `ROUTED_PATHS="src/ lib/"` as its sample, a commented line at
  `tools/memory-tree/.memory-tree.conf.example:487`, and `:484-486` say neither key ships assigned.
  NOT OBSERVED: an evidence spelling has no behaviour, and the `src/` rationale rests on
  `set_fixture_conf`'s default (`routed_commits.py:420-424`).
- **S22** — id 22. The landed-sha bar's scrub. `PM_SCRUB` in `tools/run-gates/post-merge.sh`
  (`:35-38`) gains `GATE_REGEN_CHECK`, and its comment (`:28-34`) says why, citing the hook's
  `BAR_SCRUBBED_KNOBS` (`.githooks/pre-push:1838-1842`). An inherited `GATE_REGEN_CHECK=0` would skip
  the generated-output preflight (`tools/run-gates/run-gates.sh:1442`) on the bar that publishes
  GREEN for the landed sha. This completes unit 37 §3. §8 F3. Observed by AC15.

## 3. Non-goals (OUT)

- The report's left-shift gates: spec-lint, spec-audit checklist, bug-class and parity rules, one
  per item. No clause of this build names them.
- The HIGH finding, which `TOOL-dScopedBuild-40` takes.
- Rewording units 4, 5, 7 and 29 to 39 in this pass. Each item supersedes a clause by name, and where
  an earlier builder declares a write, that builder makes the rev bump.
- Moving any unit's order. The disposal adds this unit at order 18 and renumbers nothing.

### Edges

- **consumes-from** `TOOL-dScopedBuild-36` — S1's two checked-out fixtures and §4's write set, which S1 makes one `build_fixture` keyword and S10 widens by the map (ids 1, 21, 19)
- **consumes-from** `TOOL-dScopedBuild-37` — S1's comment, S3's `gates-green` line, AC2's hook cut and §3, which S15, S11 and S22 complete (ids 6, 25, 22)
- **consumes-from** `TOOL-dScopedBuild-38` — S2's CLI refusal, its callers' `entries` and its five-parameter spelling, and §1's and §4's conf evidence, which S17, S14 and S21 complete (ids 8, 5, 15)
- **consumes-from** `TOOL-dScopedBuild-39` — S8, S9, S12, S15, S16, S18, S22, S27 to S29, §4 and AC4, AC5, AC10, AC13, AC14, AC17, AC20 and AC21, which S1 to S9, S12, S16 and S18 to S20 complete (ids 1, 21, 2, 14, 23, 3, 10, 17, 18, 26, 7, 9, 11, 13)
- **consumes-from** `TOOL-dScopedBuild-40` — S1's guard, which closes the nested-entry case S13 observes (id 4)
- **consumes-from** `TOOL-dScopedBuild-4` — S3's `--unit-commits` write, which S9 rules unit 4's builder declares in its Files touched (id 18)
- **consumes-from** `TOOL-dScopedBuild-7` — S5's `TYPED_RECORD_KINDS` member, for which S9 rules unit 7's builder declares `tree_lib.py` and `policy fixtures` (id 18)
- **consumes-from** `TOOL-dScopedBuild-5` — S2's `read_unit_writes` call and the ledger line answering it, which S14 supersedes and AC3 reads (id 5)
- **consumes-from** `TOOL-dScopedBuild-29` — the ledger note on §3's first bullet, which S19 respells and AC3 reads (id 11)
- **consumes-from** `TOOL-dScopedBuild-30` — the ledger note on §4's last Evidence command, which AC3 reads for S3 to S5 (ids 2, 14, 23)

## 4. Design

### Why one unit

M4 admits a second unit only where the minors split into two disjoint write sets by M6. This unit's
own pass writes one file, `tools/run-gates/post-merge.sh` (S22). Every other item is built by the
builder of the unit whose clause it corrects, or is an observation of what that builder built, as
"Rollout" says. One write set cannot split, so the minors are one unit.

### Evidence

- `routed_commits.py:385-415`: `build_fixture` runs `git init -q --template=` and one
  `git fast-import`. Nothing checks out, so the tree has no index (S1, S2).
- A `#!` stub raised `OSError [WinError 193]` under `subprocess.run` on this node. A `.cmd` stub
  returned 0 on `-c :` and 1 on a script argument. PINNED on 2026-11-01 (S7).
- `git grep -c -- '--diff-filter=ACMRD' -- .githooks/pre-commit tools/memory-tree/README.md
  WIRE-INTO-PROJECT.md` prints nothing at `62d7511a`. The deletion line grep prints 0 for each doc
  (S6).
- `read_spec_writes` lists no `tools/memory-tree/` path for unit 4 at `62d7511a`. For unit 7 it lists
  `tools/memory-tree/build_records.py` and no `tree_lib.py`, and unit 7's §7 holds no
  `policy fixtures`. For unit 36 it lists no `symbols.json` (S9, S10).
- `memory/map/generated/symbols.json` lists symbols as `{id, kind, file}` rows. Its guard trips
  `recall floor` and `recall floor arms`, each carried by two legs (S10).
- `unattended.sh:11263`, `:11271`, `:11276` and `:11280` hold the `RB_BOUND` sets and clears at
  `62d7511a`, and `:11274` and `:11278` are comments (S16).
- `regen.py` holds no `alias` token at `62d7511a` (S19).
- Over `.githooks/pre-push`'s six `BAR_SCRUBBED_KNOBS` words, the one `PM_SCRUB` lacks at
  `62d7511a` is `GATE_REGEN_CHECK` (S22).

### Inventory

Minted: the `checkout` keyword of `routed_commits.build_fixture` (S1), a parameter and not a symbol,
which unit 36's builder adds. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 18, after every unit, as the disposal rule places a batch that lands on several
units. Where an item corrects a clause an earlier unit builds, that unit's builder builds the item's
form, and its §3 hands-off line to this unit names it. That covers S1, S7, S9, S10, S12, S13 and
S15. Where an item corrects a criterion, the corrected criterion is this unit's, observed at the
close: S3 to S6, S8, S11, S14 and S17 to S19. This unit's pass writes S22 and observes the rest.

### Files touched (estimate)

- `tools/run-gates/post-merge.sh`: S22's scrub word and comment

### Alternatives rejected

- **Build every correction in this unit's pass, at order 18.** S9's and S10's write sets are graded
  at units 4, 7 and 36's own commits, long before order 18. S1's keyword must exist when unit 36
  builds its fixtures.
- **One unit per minor.** M4 forbids it.
- **Correct the citations of S16, S20 and S21 in the specs they land on.** That is a fold, and M4
  admits none.

## 5. Production-readiness checklist

- security — S22 denies the landed-sha bar one more inherited knob. S12 turns every failed adapter
  load into a refusal. Nothing widens a write path.
- perf / scale — S22 runs the generated-output preflight where an inherited knob had skipped it.
  S1's reset costs under a second per fixture.
- error / empty / loading states — S12's load failures and S17's blank `ROUTED_PATHS` each get a
  named exit 2. AC9, AC14 and AC15 each state what an empty read means.
- observability — S7's plant names its own branch's line. S15's not-honoured line names
  `GATE_REGEN_CHECK`.
- risks — S1, S7, S9, S10, S12 and S15 rest on earlier builders reading their §3 hands-off lines.
  AC1, AC5, AC7, AC8, AC10 and AC12 observe the built form at the close.
- testing — each AC is a probe, a fixture or a ledger read. AC2, AC5, AC10 and AC12 are observed at
  the close.
- migration — none.
- user docs — none under `help/`; no page describes `post-merge.sh`'s scrub.

## 6. Acceptance criteria

- **AC1** — When `python -c` builds a two-commit tree by
  `routed_commits.build_fixture(root, "t", commits, checkout=True)`, `git -C <tree> status
  --porcelain` prints nothing and `git -C <tree> ls-files` lists every path of HEAD's tree. With
  `checkout` left at its default, the same `status` lists HEAD's paths as staged deletions.
  Red when: the keyword leaves the tree without an index.
  permission: observed at the close, after unit 36 is built.
- **AC2** — When the driver suite's unit 39 AC17 arm runs the sliced `check_build_exit` over each of
  its two trees under `warn-and-ask`, `git diff --cached --name-only` in that tree prints at least
  one path, and every path it prints has `BACKLOG.md` as its last segment. A rerun at the same tip leaves that output
  unchanged.
  Red when: a tree is built with `checkout` False, so the cached diff lists HEAD's files as deleted.
  permission: observed at the close, after unit 39 is built.
- **AC3** — When `awk -v U=<unit> '$0 == "**Evidences:** " U {f=1; next}
  /^\*\*Evidences:\*\*|^#/ {f=0} f' memory/builds/dScopedBuild/build/*.md | grep -c '<note>'` runs
  after that unit is built, it prints at least 1 for each of three pairs. Unit
  `TOOL-dScopedBuild-30` with note `TOOL-dScopedBuild-39 S27` answers S3 to S5. Unit
  `TOOL-dScopedBuild-5` with note `TOOL-dScopedBuild-41 S14` answers S14. Unit
  `TOOL-dScopedBuild-29` with note `TOOL-dScopedBuild-41 S19` answers S19.
  Red when: a ledger answers its clause without the note, or the note sits in another unit's block.
  A planted journal holding the S27 note under `**Evidences:** TOOL-dScopedBuild-29` prints 0 for
  unit 30's row.
  figure: DERIVED at observation; each row prints 0 at `62d7511a`.
  permission: observed at the close, after units 5, 29 and 30 are built.
- **AC4** — When `git grep -c -- '--diff-filter=ACMRD' -- .githooks/pre-commit
  tools/memory-tree/README.md WIRE-INTO-PROJECT.md` runs on the built tree, it prints a count of at
  least 1 for each of the three files. `grep -c 'deletion.*check 32\|check 32.*deletion'` prints at
  least 1 for each of `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md`.
  Red when: a snippet is deleted or rewritten to another filter, or the deletion line is absent.
  figure: DERIVED at observation; every count is 0 at `62d7511a`.
- **AC5** — When the routed-commits selftest's unit 39 AC10 arm runs its first plant, a `.cmd` stub
  on Windows or a `#!` script on POSIX that exits 0 on `-c :` and 1 on anything else,
  `check_routed_commits` exits 2. Its output holds the line the spawn's non-zero exit prints and no
  `GOV_BASH is set to` line. With a `#!` stub on Windows in its place, the first plant fails.
  Red when: a first plant that fails at `resolve_bash` passes.
  permission: observed at the close, after unit 39 is built.
- **AC6** — When `python -c "import ast, sys; k = sys.argv[1]; print(sum(1 for f in sys.argv[2:] for
  c in ast.walk(ast.parse(open(f, encoding='utf-8').read())) if isinstance(c, ast.Call) and
  getattr(c.func, 'id', getattr(c.func, 'attr', None)) == 'read_policy_value' and c.args and
  isinstance(c.args[0], ast.Constant) and c.args[0].value == k))"` runs with
  `build.reuse-check.second-pass`, then `flow.route-backs`, over `reuse_check.py`,
  and with `deviation.gate` over `tools/memory-tree/routed_commits.py` and
  `tools/memory-tree/deviation_join.py`, each prints at least 1.
  Red when: a key's only `read_policy_value` mention is a comment or a docstring. A copy of
  `reuse_check.py` whose only such line opens `#` prints 0.
  permission: observed at the close, after units 26 and 30 are built.
- **AC7** — When `python -c` calls `design_lib.read_spec_writes` on unit 4's spec and on unit 7's,
  the first lists `tools/memory-tree/routed_commits.py` and the second
  `tools/memory-tree/tree_lib.py`. Unit 7's §7 leg line holds `policy fixtures`.
  Red when: a unit commits a file its declared write set omits.
  figure: DERIVED at observation; both lists lack the path at `62d7511a`.
  permission: observed at the close, after units 4 and 7 are built.
- **AC8** — When `python -c` reads `memory/map/generated/symbols.json`, a row has `id`
  `read_backlog_state` and `file` `tools/memory-tree/routed_commits.py`.
  `design_lib.read_spec_writes` on unit 36's spec lists `memory/map/generated/symbols.json`, and its
  §7 leg line holds `codebase-map coverage + freshness`, `lexicon naming predicates`,
  `recall floor` and `recall floor arms`.
  Red when: unit 36 adds a mapped symbol and leaves the map stale.
  permission: observed at the close, after unit 36 is built.
- **AC9** — When `hk=$(sed -n 's/^BAR_SCRUBBED_KNOBS="\([^"]*\)"$/\1/p' .githooks/pre-push)` runs,
  `$hk` is non-empty and holds `GATE_REGEN_CHECK`, and unit 37 AC2's other clauses hold.
  Red when: the hook's line yields no words. A copy of the hook whose line reads
  `export BAR_SCRUBBED_KNOBS="..."` yields an empty `$hk`, which fails here.
  figure: DERIVED at observation; `$hk` holds six words at `62d7511a`.
- **AC10** — When `reuse_check.py bound` runs with `resolve_kit_dir` pointed at each of three
  directories, it exits 2 with the line naming `policy_value.py` by its kit-relative path, under
  `memory-tree/`, and
  `git diff --cached --name-only` names no `BACKLOG.md`. The three are one with no
  `policy_value.py`, one whose `policy_value.py` holds a syntax error, and one whose
  `policy_value.py` defines no `read_policy_value`.
  Red when: a load failure exits 1, read as a bound hit.
  fixture: unit 12's `reuse_check.py --fixture` tree.
  permission: observed at the close, after unit 39 is built.
- **AC11** — When `python -c` calls `design_lib.derive_kit_dir("src/core/x.py", ["src/",
  "src/core/"])`, it returns `src/core/x.py`.
  Red when: the first matching entry reduces the path to the declared `src/core/`.
  permission: observed at the close, after unit 40 is built.
- **AC12** — When the driver suite's TOOL-aFrugalTurnstile-12 AC1/AC2 arm runs `--close tRun` with
  `GATE_REGEN_CHECK=0` exported beside its three knobs, its bar stub records `GATE_REGEN_CHECK` unset
  and the output holds `not honoured from the environment by this bar: GATE_LEGS GATE_REUSE
  GATE_DOCS_BASE GATE_REGEN_CHECK`. `grep -B4 '_gknobs="' tools/unattended/unattended.sh | grep
  '^ *#' | grep -c GATE_REGEN_CHECK` prints at least 1.
  Red when: the `gates-green` bar inherits the knob, or S1's comment is absent.
  figure: DERIVED at observation; the grep prints 0 at `62d7511a`.
  permission: observed at the close, after units 32 and 37 are built.
- **AC13** — When `python <repo>/tools/memory-tree/design_lib.py --kit-dir src/a` runs with its
  working directory a `build_fixture` tree whose conf `set_fixture_conf` writes with
  `ROUTED_PATHS=""`, it exits 2 and its output names `ROUTED_PATHS`. When `python -c` replaces
  `routed_commits.check_touch_join` with a function recording its `writes` argument and runs
  `check_routed_commits` on unit 38 AC3's `src/` fixture, the recorded `writes` holds `src/a` and no
  `src/`.
  Red when: the CLI falls back to a default, or the touch join receives a write set reduced without
  `entries`.
  permission: observed at the close, after units 9 and 38 are built.
- **AC14** — When, for each sha `git log --format=%H f4597719..HEAD -- tools/policy/check_policy.py`
  prints at the close, the commit's subject names a unit whose `design_lib.read_spec_writes` lists
  `tools/policy/check_policy.py` and whose §7 leg line holds `policy fixtures`; and for each commit
  whose subject names `TOOL-dScopedBuild-26`, `git diff-tree --no-commit-id --name-only -r <sha>`
  prints no `tools/policy/check_policy.py`.
  Red when: a commit edits the file under a subject naming no such unit. A planted commit in a
  scratch clone, subject `TOOL-dScopedBuild-26`, that edits the file is named.
  figure: DERIVED at the close. The population is empty at `62d7511a`, and an empty population is
  reported as no commit editing the file, never as the first half passing.
- **AC15** — When `hk` is cut as in AC9 and `pm=$(sed -n '/^PM_SCRUB="/,/"$/p'
  tools/run-gates/post-merge.sh | tr -d '"')` runs, `$hk` is non-empty and every word of `$hk` is a
  word of `$pm`.
  Red when: `PM_SCRUB` lacks a knob the hook scrubs.
  figure: DERIVED at observation; at `62d7511a` the one miss is `GATE_REGEN_CHECK`.

## 7. Gates

`run-gates evidence` · `routed-commits selftest` · `unattended kit gate` · `codebase-map kit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC12 · unit 39 AC17's trees read by their cached diff, and the `gates-green` arm with `GATE_REGEN_CHECK=0`, staged by building the trees with `checkout` False and by dropping the knob from the list · none

New arm: tools/memory-tree/routed_commits.py · covers AC5 · unit 39 AC10's first plant as a `.cmd` stub on Windows, staged by a `#!` stub that fails at resolution · none

New arm: tools/codebase-map/reuse_check.py · covers AC10 · the syntax-error and missing-function adapters, staged by catching `ImportError` alone · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause.
  It lands on four units. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the precedent
  `TOOL-dWitnessedBar-91` §8 F1 set. widens: none · relaxes: none
- **F2 — Check out S1's trees by a reset at each caller, or by one keyword on `build_fixture` (ids
  1, 21)?** Options: (a) each caller runs `git reset -q --hard` after `build_fixture`, as unit 36 S1
  writes it; (b) a `checkout=False` keyword that runs the reset, called by unit 36's two fixtures
  and unit 39's two trees. Both satisfy AC1 and AC2. The reset is now needed at a second caller, and
  the charter's reuse rule extracts at a kind's second instance. A default of False leaves every
  other caller as it is, which unit 36 §3 requires. RESOLVED (agent, 2026-11-01, delegated): (b),
  rung 3, the tie-break on reuse of a seam M5 found. widens: none · relaxes: none
- **F3 — Name `PM_SCRUB` out of scope, or add the knob to it (id 22)?** Options: (a) a §3 bullet
  naming `post-merge.sh`'s list as a third carrier outside this build, and an ask against the
  run-gates kit; (b) `PM_SCRUB` gains `GATE_REGEN_CHECK`, observed by AC15. (b) closes the defect and
  leaves no ask open. It trips no veto: `post-merge.sh` is a kit file and not a governance carrier,
  and the change narrows what an inherited environment may choose. RESOLVED (agent, 2026-11-01,
  delegated): (b), rung 3, the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 36 to 39, its 22
  minors: MEDIUM ids 1 2 3 10 17 18 19 21 25 26 and LOW ids 4 5 6 7 8 9 11 13 14 15 22 23.

## 10. Reuse audit

Each item extends the seam of the unit it lands on: `routed_commits.build_fixture`
(`tools/memory-tree/routed_commits.py:385`) gains one keyword for S1, unit 40's guard serves S13,
`design_lib.read_spec_writes` (`tools/memory-tree/design_lib.py:528`) is S9's and S10's read, and
`PM_SCRUB` (`tools/run-gates/post-merge.sh:35`) is held to the hook's `BAR_SCRUBBED_KNOBS` for S22.
`python tools/codebase-map/reuse_lookup.py "check out a fast-import fixture repository so its index
and working tree hold HEAD"` ranked `tree`, `check` and `fixture`, and none checks out a
`build_fixture` tree. `python tools/codebase-map/reuse_lookup.py "the knobs a bar scrubs from its
inherited environment"` ranked `write_bar_green` and `write_inherited_asks`, and neither is a knob
list. So no seam fits beyond those named.

Recall terms used: `python tools/memory-recall/query.py "which bar scrub lists must hold the hook's scrubbed knobs" --terms "PM_SCRUB post-merge BAR_SCRUBBED_KNOBS GATE_REGEN_CHECK scrub list knob bar landed sha"`
