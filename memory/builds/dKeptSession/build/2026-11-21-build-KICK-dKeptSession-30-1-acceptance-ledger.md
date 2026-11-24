# KICK-dKeptSession-30 — acceptance ledger

**Serves:** journal KICK-dKeptSession-30

No merge bar, no self-test suite and no gate leg ran in this pass. The one leg command tried, the
reference page's `render_playbook.py --reference --check`, was refused by the role hook as the leg
"help reference pages". The criteria were observed on win32 at the pass's base `4bbc644d`. AC1 to AC4
ran as a probe that writes the two new scenarios, and `context-fill`, the way the self-test's
`build_scenario` does, under scratch projects roots, and runs `python tools/runlog/runlog.py context`
over them with `CLAUDE_CODE_MAX_CONTEXT_TOKENS` dropped from the child's environment unless the
criterion sets it. The self-test case `test_extract_context_window` itself did not run.
`python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 offenders over a pin of 1421
(DERIVED, that run), the count KICK-dKeptSession-14 read at its base; no line it printed names
`tools/runlog/`, and `--suggest` graded `derive_context_window` and `test_extract_context_window` OK as
`py.function`.

Owed to the close: every leg the spec's section 7 names; the runlog self-test, whose new case and
floor are below; the `New arm:` line's RED-first observation, the window case staged red by a copy of
`extract.py` dividing by 200000 (PINNED, the spec's `New arm:` line); and AC9's reference-page check
and its `mirror --check`, which read the commit that re-writes the mirror.

## S3's answer to KICK-dKeptSession-14

`KICK-dKeptSession-14` section 4, "The window", says the pinned window `CONTEXT_WINDOW_TOKENS` "is one constant beside the sum" and its section 8 F2 resolves on option (a), the pinned constant "until KICK-dKeptSession-30 derives it".
This unit's S1 supersedes both: the constant is deleted from `tools/runlog/extract.py`, and the window
is `derive_context_window`'s, the harness's variable first, then the node's observed usage per model
rounded up to a rung, then the bottom rung. Neither unit 14's spec nor its ledger is written (F3).

## Decisions taken in the build

- The default root is the profile's `~/.claude/projects`, read through `pathlib.Path.home()` as S1
  spells it; KICK-dKeptSession-45 resolves it through `resolve_projects_root`.
- The harness's variable is a positive integer only when it is ASCII digits and above zero, so `x`,
  `0` and a non-ASCII digit read as unset and the source is the observation's.
- A compaction's integer `pre_tokens` joins every model's observation, as S1 states it; the probe
  below reads `observed 180000 on other-model` over the `context-fill` root (DERIVED, that probe),
  the behaviour KICK-dKeptSession-47 attributes to a model.
- `held` is matched by the absolute, case-normalised path, so a relative transcript path still stands
  in for its own file in the scan.
- `cmd_context` prints the stderr line only beside a share, so `none` prints nothing there, as S2 says.

**Evidences:** KICK-dKeptSession-30
- AC1 — over a scratch root holding `context-window-sibling` alone, the CLI printed `90%` and `context: window 1000000 · observed 900000 on fixture-model` on stderr, exit 0 (DERIVED, that probe).
- AC2 — over a root holding both scenarios, `context-window`'s main file printed `15%`, exit 0 (DERIVED, that probe).
- AC3 — over a root holding `context-window` alone, it printed `75%` and `context: window 200000 · observed 150000 on fixture-model` (DERIVED, that probe).
- AC4 — AC2's read with the variable at `500000` printed `30%` and `context: window 500000 · env`; at `x`, and at `0`, it printed `15%` (DERIVED, that probe).
- AC5 — `grep -n "CONTEXT_WINDOW_TOKENS" tools/runlog/extract.py` printed nothing, and `grep -n "def derive_context_window" tools/runlog/extract.py` printed one line (DERIVED, that probe).
- AC6 — in `help/`, `grep -n "CLAUDE_CODE_MAX_CONTEXT_TOKENS" orientation-card.md` printed one line of the `context —` paragraph, and `grep -c "pinned window" orientation-card.md` printed `0` (DERIVED, that probe).
- AC7 — `tr -s ' \r\n' ' '` over this ledger piped into `grep -c "is one constant beside the sum"` printed `1`, and into `grep -c "until KICK-dKeptSession-30 derives it"` printed `1` (DERIVED, that probe); this pass stages neither unit 14's spec nor its ledger.
- AC8 — the spec's `git grep -n` over the four paths printed nothing, and `git grep -c CLAUDE_CODE_MAX_CONTEXT_TOKENS` printed one row for each of `tools/runlog/README.md`, `tools/policy/catalogue.toml` and `skills/session-kickoff/manifest-check.sh` (DERIVED, that probe).
- AC9 — `python tools/govkit/docs_leg.py --fingerprints` printed `ba7d79dc` on its `policy:context.threshold` row after the summary edit, the fingerprint the key's anchor on `help/orientation-card.md` carries (DERIVED, that probe). After the build's commit `python tools/policy/policy.py mirror --write` printed `catalogue 7607b1a8`, and the mirror's `catalogue_blob` equals the blob `git ls-tree HEAD tools/policy/catalogue.toml` printed there, no longer `4be1f801` (DERIVED, that probe); the mirror is committed in the commit after the build's, since it renders HEAD. Its `--check` and the reference check are the close's.
- Beyond the criteria: the `context-fill` scenario still printed `60%`, with `context: window 200000 · observed 180000 on fixture-model`, and `measure_context_fill` with `until` before its compaction returned `(0.9, 200000, 'observed 180000 on fixture-model')`; a model never observed read `(200000, 'no observation')`; a 1300000-token turn read its own window; a missing root read the bottom rung; and `held` stood in for its own path's parse (DERIVED, that probe). Over this node's real `~/.claude/projects`, `derive_context_window("claude-opus-5-5")` returned `(1000000, 'observed 988875 on claude-opus-5-5')` in 4.24 s (DERIVED, that probe).
- `ASSERTION_FLOOR` rises from 1587 to 1595: the new case's 5 checks and its 3 decoy checks (PINNED, the count its `RAISED` comment prices).
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_extract_context_window`: the share divided by 200000
