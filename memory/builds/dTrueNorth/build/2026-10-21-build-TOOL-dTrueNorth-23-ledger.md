# TOOL-dTrueNorth-23 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-23

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the one
name the pass mints (`--suggest scan_glob_readers --as py.function`, OK). Every criterion below was
observed by a probe of the changed code at the working tree over `06dec3a42`, in a child process per
environment, and again against the `HEAD` copy of `tools/memory-tree/` extracted by `git archive` into
`%TEMP%/u23base`, so each probe is seen to move. A second probe mirrors the selftest arm's behavioural
half over a fixture repository of its own under `%TEMP%/u23fx`, built by the generator's `_fixture`: a
spec of two commits, a review record and a backlog shard holding `ARCH-tOne-9`. The arm itself, the
`build-index selftest`, `row-grammar selftest` and `memory hygiene` legs, and the `New arm:` line's
RED-first observation are owed to the close.

**Evidences:** TOOL-dTrueNorth-23
- AC1 — `design_lib.read_spec_revisions` — at this repo's root over
  `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-19.md`, unset and with
  `GIT_LITERAL_PATHSPECS=1` in the child's own environment: 5 revisions both times, the same five shas
  from `3ce234bd8` to `700c564a2`. The `HEAD` kit read 5 unset and 0 under the variable, raising
  nothing, the red.
- AC2 — `tree_lib.read_adding_commits` — over `:(glob)memory/builds/*/reviews/**` for
  `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`, beside AC1's
  call, under each of the four variables set to `1` one at a time: every answer equalled the unset
  one, the record keyed to `3ce234bd8`, and AC1's five revisions. The `HEAD` kit answered `{}` and 0
  revisions under `GIT_LITERAL_PATHSPECS` and the unset answers under the other three. Over the
  fixture the four probes read 2 revisions, one adding commit twice and one dated id, and none moved
  under any mode; the `HEAD` kit moved all four under the literal mode.
- AC3 — `tree_lib.read_git_output` — with all four variables set, `subprocess.run` stubbed to
  capture its `env` keyword and return an empty success: neither `tree_lib.read_git_output` nor
  `gen_build_index._build_git_env`, through the generator's `run`, handed any of the four keys, and
  `tree_lib.GIT_ENV_LEAKS` sorts equal to the eight location variables and the four modes. The `HEAD`
  kit handed all four through both runners, and its list is the eight alone.
- AC4 — `row_grammar.derive_first_seen` — over this repo's conf, unset and with
  `GIT_LITERAL_PATHSPECS=1`: 912 dated ids both times, and the answer is identical to the `HEAD` kit's
  unset answer, id for id and date for date. An `ast` walk of the function finds a `read_git_output`
  call and no `subprocess.run`. The `HEAD` kit dated 912 against 0, and its walk finds the
  `subprocess.run` and no `read_git_output`. Over a directory that is no repository the walk raised
  `Problem` naming the `git log` command and `fatal: not a git repository`, exit 128.
- AC5 — `tools/memory-tree/` — `scan_glob_readers` over it returned exactly
  `design_lib.read_spec_revisions`, `deviation_join.read_population`, `gen_build_index.cmd_selftest`,
  `gen_build_index.derive_audit_writers` and `row_grammar._build_backlog_pathspecs`. Over a scratch
  copy of the directory holding one more module, `planted23.py`, whose top-level function returns a
  `:(glob)` string beside a module-level constant holding one and a function naming one in its
  docstring only, it named `planted23.PLANTED` and `planted23.read_planted` as readers the table does
  not hold, and nothing stale.
