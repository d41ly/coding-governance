# KICK-dKeptSession-47 — acceptance ledger

**Serves:** journal KICK-dKeptSession-47

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `4605d479` by one probe under the session scratchpad, which plants each criterion's
scenarios from `tools/runlog/fixtures/transcripts.json` itself, without importing the self-test or
running any arm: a scratch projects root holding unit 30's `context-window` transcript and one of
S2's scenarios, read by `runlog.py context` with `CLAUDE_CODE_MAX_CONTEXT_TOKENS` removed and the
config and home roots aimed at an empty scratch. The same probe read a copy of the kit whose
`extract.py` is the base's, folding every compaction, and a copy folding none. `python
tools/lexicon/lexicon.py` exited non-zero on its verb-offender pin, 1432 offenders over a pin of 1421
(DERIVED, that run), the count unit 46's ledger read before this pass; no offender it named is in
`tools/runlog/`, and `--suggest` graded `test_extract_context_window_compact` OK as `py.function`.

Owed to the close: every leg the spec's section 7 names; the runlog self-test, whose new case and
floor are below; and the `New arm:` line's RED-first observation, the new case staged against a copy
of `extract.py` folding every compaction.

## Decisions taken in the build

- The walk keeps one flag per transcript, whether its newest main usage so far is on `model`, rather
  than the newest usage's model itself: a compaction with no main usage before it then joins no
  model even when `model` is `None`, which a comparison of two `None`s would let through.
- The `context` paragraph of `tools/runlog/README.md` names this unit beside the rewritten clause.

## Unit 30's superseded wording (S3)

Unit 30 is CLOSED, so its spec and ledger stay as they are and the answer is here (F1).

- Unit 30 S1 step 2 gives each transcript's observation as its largest main usage sum on `model`
  "and the largest integer `pre_tokens` of its `compact` events". Read it as S1 of this unit: only a
  compaction whose newest earlier main usage in the same transcript is on `model` joins that model's
  observation, and one with no main usage before it joins no model.
- Unit 30's Evidence bullet, that `extract_session` already yields `model` on every usage event and
  `pre_tokens` on every compact event, "so the scan needs no new parser field", stands: the
  attribution is a fold over the sorted events `extract_session` yields, and adds no field to them.

**Evidences:** KICK-dKeptSession-47
- AC1 — from a root holding `context-window` and `context-window-compact-other`, `runlog.py context` exited 0 printing `75%`, with `context: window 200000 · observed 150000 on fixture-model` on stderr (DERIVED, that probe). The base's `extract.py` printed `15%` with `observed 900000 on fixture-model` from the same root, the red the criterion names (DERIVED, that probe).
- AC2 — from a root holding `context-window` and `context-window-compact-own`, it exited 0 printing `15%`, with `context: window 1000000 · observed 900000 on fixture-model` on stderr (DERIVED, that probe). A copy folding no compaction printed `75%` from the same root, the red the criterion names (DERIVED, that probe).
- AC3 — both passages are quoted above; `git diff --name-only` from the pass's base over unit 30's spec and its acceptance ledger prints nothing, since this commit writes neither (DERIVED, that probe at the commit).
- AC4 — over `tools/runlog/README.md` the new clause counts 1 and `largest compaction` 0, and over `tools/runlog/extract.py` the new docstring clause counts 1 and `largest integer compaction` 0 (DERIVED, `tr` and `grep` at the commit).
- Beyond the criteria, a direct read of `derive_context_window` over `held` events read `no observation` for a compaction timed before the transcript's only usage, and the 1000000 rung for one timed after it (DERIVED, a `python -c` probe).
- `ASSERTION_FLOOR` rises from 1624 to 1629: the new case's 2 checks and its 3 decoy checks (PINNED, the count its `RAISED` comment prices).
