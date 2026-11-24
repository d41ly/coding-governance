# KICK-dKeptSession-45 — acceptance ledger

**Serves:** journal KICK-dKeptSession-45

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `b7b3a791`. AC1 and AC3 ran as a probe that writes the `context-window-sibling`
scenario with the self-test's `build_scenario` under a scratch config directory's `projects/` and
under a scratch home's `.claude/projects`, then runs `python -c "import extract;
print(extract.derive_context_window('fixture-model'))"` in the runlog kit with
`CLAUDE_CODE_MAX_CONTEXT_TOKENS` dropped from the child's environment. The self-test case
`test_extract_context_window_root` itself did not run. `python tools/lexicon/lexicon.py` exited 1 on
its verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED, that run), the same count it printed
with this unit's two files restored to the base (DERIVED, that run), so the unit adds no offender.

Owed to the close: every leg the spec's section 7 names; the runlog self-test, whose new case and
floor are below; and the `New arm:` line's RED-first observation, the case staged red by a copy of
`extract.py` whose default root is the literal profile path (PINNED, the spec's `New arm:` line).

## S3's answers to KICK-dKeptSession-30

`KICK-dKeptSession-30` S1 says "`root` defaults to the harness's projects root, `~/.claude/projects`",
and its S2 derives the window of `derive_context_fill`'s liveness check and of
`KICK-dKeptSession-9`'s per-stage rows "under the default root". This unit's S1 supersedes both: the
default root is whatever `resolve_projects_root` (`tools/runlog/extract.py#resolve_projects_root`)
resolves from the process environment, `CLAUDE_CONFIG_DIR`'s `projects` before the profile's home,
and where no root resolves the window reads the bottom rung with a `no root:` source (S2).
`resolve_projects_root` is the seam unit 30's Reuse audit does not name, and the one every
transcript-reading `runlog.py` verb already calls. Neither unit 30's spec nor its ledger is written (F1).

## Decisions taken in the build

- The resolver is called only when `root` is None, after the harness's variable is read, so an
  explicit root and the `env` source never reach it, and `measure_context_fill`, which passes its
  transcript's own root, is unchanged.
- The `no root:` source carries the resolver's `ValueError` text whole, as the spec's read shows.
- Under the self-test launcher's decoy, `derive_context_window('fixture-model')` read
  `(200000, 'observed 1 on fixture-model')` from the decoy's `CLAUDE_CONFIG_DIR` canary and
  `derive_context_fill` of a 190000-token event read `0.95` (DERIVED, that probe), so the liveness
  check of `test_extract_context_fill` holds under the resolved root as it did under the literal.

**Evidences:** KICK-dKeptSession-45
- AC1 — with `CLAUDE_CONFIG_DIR` at the scratch config directory and `HOME` and `USERPROFILE` at an empty directory, the probe printed `(1000000, 'observed 900000 on fixture-model')`, exit 0 (DERIVED, that probe). The same probe over the base's code printed `(200000, 'no observation')` (DERIVED, that probe), the red the criterion names.
- AC2 — `grep -n "resolve_projects_root()" extract.py` in the runlog kit printed one line, the assignment inside `derive_context_window`, and `grep -n '\.claude' extract.py` printed two lines, the resolver's docstring and its return, both inside `resolve_projects_root` (DERIVED, that probe); at the base it printed four, two of them in `derive_context_window` (DERIVED, that probe).
- AC3 — with `CLAUDE_CONFIG_DIR`, `HOME` and `USERPROFILE` all removed, the probe printed `200000` and the source `no root: runlog: no transcripts root resolves: CLAUDE_CONFIG_DIR and the profile's home are both unset; pass --transcripts`, exit 0 (DERIVED, that probe); Python's repr quotes that source with double quotes, since it holds an apostrophe. Over the base's code the same environment read this node's real profile through `pathlib.Path.home()`'s Windows fallback, `(1000000, 'observed 988875 on fixture-model')` (DERIVED, that probe).
- AC4 — `tr -s ' \r\n' ' '` over this ledger piped into `grep -c "defaults to the harness's projects root"` printed `1`, and into `grep -c "under the default root"` printed `1` (DERIVED, that probe); this pass stages neither unit 30's spec nor its ledger (DERIVED, `git diff --cached --name-only`).
- Beyond the criteria: with `CLAUDE_CONFIG_DIR` removed and `HOME` and `USERPROFILE` at a scratch home holding the scenario under `.claude/projects`, the probe printed `(1000000, 'observed 900000 on fixture-model')` (DERIVED, that probe), the spec's second row of the read and the new case's liveness check.
- `ASSERTION_FLOOR` rises from 1612 to 1618: the new case's 3 checks and its 3 decoy checks (PINNED, the count its `RAISED` comment prices).
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_extract_context_window_root`: the default root is the literal profile path
