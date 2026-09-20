# Acceptance ledger — TOOL-dLoggedFlight-10

**Serves:** journal TOOL-dLoggedFlight-10

Tier-2 · node d · 2026-09-14 · the build pass of the schema leg, against spec rev-5. The pass bumped the
spec from rev-4 to rev-5 in its own commit, `809de803`, before any code, and its section 9 line names
each change. Every criterion line is OBSERVED, and what a gate leg observes is written as owed.
`<suite>` is `tools/runlog/selftest.py`, run directly and never through the gate runner. At the closing
bytes it printed `1000 passed, 0 failed (1000 assertions, floor 1000)` in 38.9 s, and three timed runs
before the checklist's fold read 38.5 to 39.1 s. The leg itself was run over this tree as AC5's own
observation. No gate leg ran, per the owner's instruction of 2026-09-13, and no suite that existed
under `tools/unattended/` before this build ran. Every fixture history is a scratch repository built
through one `git fast-import`, and every clean record the leg grades was rendered by `render_record`,
never typed.

## The criteria

**Evidences:** TOOL-dLoggedFlight-10

- AC1 — `check-records` over `render_record`'s output (`test_schema_ac1_render_then_grade`) — the
  record `write_record` rendered from the class model, which carries one value of every shaped class
  and every member of every closed vocabulary a table holds, was staged in a fixture index beside a
  spec for each unit it names. The leg exited 0 printing `1 record`, with nothing refused, and the
  graded record was checked to carry every vocabulary member. Building this arm found the disagreement
  S5 exists for: the `label` class admits a lowercase UUID. The absolute-path and UUID shapes are now
  schema data the renderer withholds by, so a UUID-shaped workflow label is withheld and counted as
  `values withheld: 5`. With the renderer's reading of those shapes removed, the record it wrote was
  refused under `uuid` on the row's line, exit 1. RED seen with the renderer's withholding removed,
  with the leg's spec-defined ids dropped, with the shared spec-unit rule reading the wrong line, and
  with the glob pointed at a name the renderer never writes, which graded no record.
- AC2 — `check-records` (`test_schema_ac2_refusals`) — each refusal of S2, and the three rev-5 adds,
  was staged on a copy of the rendered record, and each exited 1 naming its rule on its line. The
  staged records carried moved headings, a row led by a unit id and a cell outside its vocabulary.
  They carried an absolute path in three spellings, a POSIX home root, a drive letter and a UNC prefix.
  They carried a UUID the label class admits, which is the only rule on its line. Their Data blocks
  were not JSON, carried an undeclared key, carried a JSON escape, or repeated a key. They carried a
  Serves id of another build and one no spec defines, a free-text line, a CR byte, a byte that is not
  UTF-8, and one byte over the cap. A glob-admitted name the renderer never writes was refused under
  `name`. Every rule of `RECORD_RULES` was staged and no refusal named another. Three near misses
  exited 0: a `home` folder mid-path, a Serves range of the build's own ids, and a record of exactly
  the cap. RED seen with each of the eleven rules switched off in turn, each on its own check.
- AC3 — `0 records` and `MEMORY_ROOT=docs/mem` (`test_schema_ac3_liveness`) — with no record tracked
  the leg exited 0 printing `0 records (none committed yet)`. With the declared root naming a folder
  that holds no tracked file it exited 1 under the `root` assertion and printed no GREEN. With
  `MEMORY_ROOT=docs/mem` it graded the record there as `1 record under docs/mem/builds/`, exit 0. With
  the glob pointed at a pattern the renderer does not write, the population emptied and the leg went
  red under its own `glob` assertion. RED seen with each assertion switched off. The glob constant was
  also edited on disk to a pattern the renderer does not write, and the self-test failed in AC1's and
  AC3's arms, as the criterion requires.
- AC4 — `check-records` with `subprocess.Popen` patched (`test_schema_ac4_cost_and_index`) — fixture
  indexes of 1 and of 100 records made the same git calls, and so did 1 and 50 builds carrying
  run-state files. The calls were `ls-files`, `cat-file`, `log`, `log` and `cat-file`, in that order,
  the five S4 and S6 name. A staged violation under a clean working copy exited 1, and a clean staged
  record under a violating working copy exited 0, with the working copy seen to differ from the index.
  `tools/gate-legs.json` declares the leg's ceiling of 60 s, read off the manifest. Whether that
  ceiling clears its evidenced maximum is OWED to the `leg ceilings clear their evidenced maximum` leg
  of the post-build gate run. RED seen with the leg reading the working tree, with a git call added per
  record, and with one added per build.
  MET at the post-build run: `leg ceilings clear their evidenced maximum` is GREEN, so the 60 s
  ceiling this line reads off the manifest does clear its evidenced maximum, and
  `runlog record schema` - the leg itself - is GREEN in 0.7 s, reporting `git_calls=5` over this
  tree.
- AC5 — `check-records` over this tree and `RUN.md` fixtures (`test_schema_ac5_runs`) — over this tree
  it exited 0 in 5 git calls. It reported aBoundedVerdict, aDeclaredBound, aGradedDialect,
  aPacedTurnstile, dTieredTribunal and dUnstalledConvoy with distinct start commits, every window
  ending at or after its start, and disjoint windows; the last two are the builds round-3 H2 named. The
  arm holds the reported set equal to the rotated builds `ls-files` finds. A squashed history, one
  commit adding an archive and `RUN.md`, exited 1 naming the build under `run-start` and `run-window`.
  A LANDED-after-LANDED build rotated the way the driver rotates was graded clean. Its archive's window
  ended at its own terminal write, and its live window ran from the rotation to its own. With the eras
  staged to span the path's whole history, the live window ended at its predecessor's terminal write,
  before its start, and the leg exited 1 naming the build. With the naive key, each archive keyed on its
  own creation commit, it exited 1 under `run-start`. Staged on the shared derivation itself and run
  over this tree, dropping the era bound turned all six rotated builds red under `run-window`, and the
  naive key turned all six red under `run-start` and `run-window`. The closing diff review's round-1
  fold of L3 bumped the spec to rev-7 and widened this criterion. The squashed history's `run-start`
  refusal now names the joint add it saw. The LANDED-after-LANDED build, with its memory root then
  moved to `mem2` in one commit that deletes every path under `memory/` and adds it under `mem2/`,
  as a `git mv` commit records it, with the conf naming the new root, exited 1 refusing the build's
  shared start once, and that refusal names the joint add too. Both of its runs started at the move
  and carried `joint_add`, where before the move they had two starts and neither mark. RED seen in
  place, restored by checksum: the refusal's naming removed, which redded both naming checks, and no
  start marked, which redded those and the mark check.

## What else the pass carried

- **The window derivation moved, unchanged.** `derive_record_commits` and `derive_window` left
  `build_run_model` for functions the leg reads too, and every model and record arm passed after the
  move. `derive_run_starts` takes the index's path set, and `read_blobs` returns bytes on request.
- **One rule for which unit a spec defines.** The checklist's fold moved it into `derive_spec_unit` and
  `build_unit_id_re`, which `read_units` and the leg both read.
- **One path builder.** The renderer names a new record through `derive_record_relpath`, and the leg's
  glob assertion calls it at run time.
- **The leg ships.** It is a `[[gate_leg]]` in the runlog descriptor with `history_depth = "full"`, an
  unguarded manifest row with a 60 s ceiling, and a regenerated subject pin. The dossier claims it, and
  the map was regenerated.
- **The carried-prefix counts did not move.** Every shipped file this pass changed was counted with the
  install-prefix gate's own pattern before and after.
- **The budget row for `runlog selftest`** was re-measured at 40 s rounded up, so x1.5 is exactly the
  file's 60 s floor.

## Staged RED

Twenty-six breaks, each an edit applied to `record.py` or `model.py` on disk by a harness kept outside
the tree. Each ran against the arm it aims at, with the bytecode cache cleared before and after, and
each file was restored byte for byte. Each turned red on the very checks it aims at, matched by the
checks' text and not by the exit status. The whole set was run again against the closing bytes. One
break first crashed the fixture builder instead of failing a check: with the shared spec-unit rule
reading the wrong line, the renderer wrote no record and the builder read a path that was not there.
The builder now fails by a named check and every schema arm stops, and that break turns the check red.
Two further breaks were run against this tree through the leg, report-only; they are AC5's last
sentence.

## The checklist over the build

`gotchas.py --for-diff` over the spec and code commits named eleven classes before the closing commit,
and over the closing commit it named one more, `naming-leg-grades-what-python-named`, which the fold
after it acts on.

- `naming-leg-grades-what-python-named` was violated, and the fold fixes it. Two nested predicates in
  the AC2 arm led with `at`, which the verb table does not carry, and the leg grades nested helpers
  once the map arms them. They are now `check_run_state_line` and `check_workflow_row`. Every other
  definition the unit added, nested ones included, was asked of the lexicon and leads with a declared
  verb, and the map was regenerated in the same commit.

- `two-answers-to-one-question` was violated, and the fold fixes it. The leg carried its own copy of
  which unit a spec defines, beside the model's `read_units`; both now read one function. The dossier
  no longer restates the git-call count, which the self-test pins. The leg's own compilation of the
  schema's classes, beside the renderer's `build_matchers`, is deliberate: it is the spec's second
  enforcement point, and S5's rendered fixture is what holds the two readings together.
- `fixture-passes-by-finding-nothing`: every refusal stands beside a near miss, the vocabulary check
  proves the graded record is rich, and the fixture builder fails by a named check rather than a crash.
- `staged-break-substitutes-a-synthetic-value`: every break edits the subject, which is the leg's
  rules, the shared derivation, or the glob constant AC3's criterion is about.
- `staged-break-runs-stale-bytecode`: the harness clears the cache before and after every break.
- `heredoc-escape-reaches-the-regex`: no source was written through a heredoc; the harness is a file.
- `inline-fence-swallows-the-rest-of-the-file`: the README's one new fence is on lines of its own.
- `amendment-leaves-its-other-half-standing`: rev-5 amended S2, S3, S5, S6, §4 and AC5. The rest of the
  spec, the record README's sentence on the leg, and the dossier were re-read against them.
- `fold-text-is-unreviewed-surface`: rev-5 and this fold are text no review has read. The build's
  closing diff review reads them.
- `one-value-field-records-a-mixed-outcome`: AC4 is part observed and part owed, and its line says owed.
- `suite-invalidated-by-a-commit-under-it`: no commit ran under a timed suite. AC5's arm reads this
  tree through the leg and through `ls-files` a moment apart, so a commit adding a rotated build
  between the two reads would turn it red spuriously. That window is recorded here, not closed.
- `empty-field-collapses-unless-it-is-last`: no shell was written.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `govkit selfcheck`, which the subject-pin regeneration ran in its write mode, and whose verdict is not
  read here;
- `codebase-map coverage + freshness`;
- `leg ceilings clear their evidenced maximum`, which is AC4's ceiling clause;
- `lexicon naming predicates`, though every new name was first asked of the lexicon;
- `memory hygiene`;
- `runlog selftest`, the leg that runs `<suite>`, and `runlog record schema`, the leg this unit adds,
  both first graded on the bar there; and `every held leg is budgeted, every budget row resolves`,
  whose row this pass re-measured.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. Every leg listed above is GREEN: `govkit selfcheck` at 27 of 27 registry entries
with 0 unclaimed, `codebase-map coverage + freshness`,
`leg ceilings clear their evidenced maximum` - AC4's ceiling clause - `lexicon naming predicates`,
`memory hygiene`, `runlog record schema` at `git_calls=5` in 0.7 s, `runlog selftest` printed
`1543 passed, 0 failed (1543 assertions, floor 1543)`, and the budget-population leg. The run's
one RED, `govkit selftest`, is on none of these legs: its 30 failing assertions are the IDENTICAL
set `origin/main` carries, pre-existing, untouched by this build and being fixed in a separate
session. It is not called green here.

## Residue

- **Parked by the fold of L3: a waiver route for a moved memory root.** The closing diff review's
  L3 asked, at minimum, that the leg's list of what it does not check name the moved root, and that
  the refusal have a waiver route. The list names it, and the refusal names the shape. The question
  left is how an adopter whose root moved clears a leg that reds on every bar from then on. The
  options seen were four. Follow the pre-move path, as the review's first option asked: the model
  keys every read on a path under the current root, the run-state history, its blobs, the specs,
  the ledgers and the decision log among them, so following the starts alone would turn a loud
  refusal into windows quietly wrong, and following every read is a redesign of the model, not a
  low's fold. Fall back to the run key a committed record carries: only runs rendered after this
  build have one. Treat a joint add as a relocation and grade it clean: one log cannot tell a move
  from a squash, and AC5 requires the squash to red. Declare the moved build in a waiver registry
  the leg reads: a new surface an adopter authors, which the build method's second veto leaves to
  the owner. None was taken. Until one is, the only route back to green is retiring the moved
  archives from the index, and no run from before the move models correctly under the new root
  with them or without them.
