# TOOL-dTrackedAtlas-12 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-12

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command in a `--shared` clone of the worktree at `%TEMP%/ta12fx`, set up as section 5 sets it, with the
pass's generator committed there as the fixture commit `$T` and `refs/remotes/origin/main` and
`refs/remotes/origin/HEAD` written in the clone alone. The four probes of section 5 sat in the run's scratch
directory, and every page and probe output went there. Each red ran the generator before this unit, the blob
`09b2b8f67` at the pass's base `c6c533e64`, put over the clone's copy with `git show` and restored with
`git checkout`; a staged break edited the clone's copy the same way. The clone was removed after, and the
real repository's refs were never written.

**Evidences:** TOOL-dTrackedAtlas-12
- AC1 — `stamp_readers.py` printed `build_stamp check_stamp=True re.fullmatch=False`,
  `read_stamp check_stamp=True re.fullmatch=False` and `check_stamp check_stamp=False re.fullmatch=False`.
  Red: over the generator before this unit it printed `check_stamp=False re.fullmatch=True` for
  `build_stamp` and `read_stamp`, and `check_stamp absent`.
- AC2 — `--claims none --out "$S/p0.html"` wrote the page in `31` s (PINNED, this pass) and
  `--check --page "$S/p0.html"` exited `0` with `atlas: current`. Red: a staged `check_stamp` looping over
  every row of `STAMP_RULES` whatever `fields` names made `--out` exit `1` with
  `atlas: cannot stamp the page: the stamp's schema field fails its rule:null`, writing no page.
- AC3 — `stamp_rules.py` over `p0.html` printed
  `fields schema commit default_ref landings digest inputs dirty | stamp schema commit default_ref landings digest inputs dirty`,
  then one `<field> True the stamp's <field> field fails its rule:` line per field with the bad value, the
  field count DERIVED from `STAMP_RULES`. Red: with the `dirty` row deleted, the first line read
  `fields schema commit default_ref landings digest inputs | stamp schema commit default_ref landings digest inputs dirty`
  and no `dirty` line printed.
- AC4 — `stamp_writer.py` printed
  `no-default-commit refused: the chain state carries no 40-hex default_commit, but None`,
  `plus-ref refused: the stamp's default_ref field fails its rule:"refs/remotes/origin/release+2"`,
  `no-builds refused: the stamp's landings field fails its rule:{}` and `whole stamped`. Red: the generator
  before this unit printed `plus-ref stamped` and `no-builds stamped`; a staged `build_stamp` whose
  `default_commit` test reads `if False:` printed `no-default-commit stamped`.
- AC5 — with `refs/remotes/origin/release+2` at `$T`, `GOV_DEFAULT_BRANCH=release+2` and `--out "$S/p-plus.html"`
  exited `1` with
  `atlas: cannot stamp the page: the stamp's default_ref field fails its rule:"refs/remotes/origin/release+2"`,
  and `test -e "$S/p-plus.html"` exited `1`. Red: the generator before this unit exited `0` writing the page,
  and `--check --page` on it printed `atlas: unstamped` with that same reason, exit `1`. The ref was then
  deleted and the page removed.
- AC6 — `state_relay.py` in the three states printed
  `the default-branch ref refs/remotes/origin/main resolves to no commit in <the clone>; fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH`,
  `the remote ladder names no default branch here; fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH`,
  and, under `GOV_REMOTE=nosuch`, a line naming `export GOV_REMOTE=<remote>.` and ending
  `Or fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH`; `grep -c -- "--default-ref"`
  over the three printed `0`. With every ref restored it printed `resolved refs/remotes/origin/main` and `$T`.
  Red: a staged `render_state_error` whose suffix test reads `if False:` ended each of the three lines
  `pass --default-ref <rev>`.
- AC7 — with `refs/remotes/origin/main` deleted, `--check --claims none` exited `1` with the one line
  `atlas: chain state: the default-branch ref refs/remotes/origin/main resolves to no commit in <the clone>; fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH`.
  Red: the generator before this unit ended that line `; pass --default-ref <rev>`, exit `1`.
- AC8 — in the same state, `--check --page "$S/p0.html"` exited `2` with `0` bytes on stdout and the one line
  `atlas: cannot check: the default-branch ref refs/remotes/origin/main resolves to no commit in <the clone>; fetch the default branch the stamp names, or regenerate the page`.
  Red: the generator before this unit ended that line `; pass --default-ref <rev>`, exit `2`. The ref was
  then restored to `$T`.
- AC9 — `grep -c "takes a revision"` over the generator printed `0`, and
  `--check --page "$S/p0.html" --ref -x` exited `2` with `0` bytes on stdout and the one line
  `atlas: cannot check: --ref takes a value`. Red: the `grep` over the generator before this unit printed `1`.

S5's pane observations are not this unit's: by the spec's §4 "The pane observations at the close" the main
loop makes them at the close and records them in ledgers 2 and 3. This pass made none, claims none, and did
not edit either ledger.

Owed to the close: the plain bar, whose legs section 6 names, and S5's two pane observations. No suite arm
is added, so no `New arm:` observation is owed.
