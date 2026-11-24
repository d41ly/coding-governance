# KICK-dKeptSession-46 — acceptance ledger

**Serves:** journal KICK-dKeptSession-46

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `6abb8204` by one probe under the host temp directory, which builds the new case's
fixture itself, without importing the self-test or running any arm: one main transcript under a
scratch `--orient` dir holding the preflight, the `context-window-sibling` request and an Edit in a
record with no `usage`, beside unit 9's two-move fixture repository, every ambient root aimed at an
empty scratch as `tools/runlog/selftest.py#build_arm_env` aims them and the harness's window variable
removed. `python tools/lexicon/lexicon.py` exited non-zero on its verb-offender pin,
1432 offenders over a pin of 1421 (DERIVED, that run), the count unit 9's ledger read before this pass; no offender it named
is a definition this pass added, and `--suggest` graded `test_extract_context_fill_root` OK as
`py.function`.

Owed to the close: every leg the spec's section 7 names; the runlog self-test, whose new case, its
re-spelt context-fill liveness check and its floor are below; and the `New arm:` line's RED-first
observation, the new case staged against a `measure_orient_tree` whose cached window is derived with
no root and a `derive_context_fill` that falls back to the default root.

## Decisions taken in the build

- `derive_context_fill` raises before it reads anything when it holds neither a window nor a root, so
  the refusal costs no scan; with both it takes the window and derives nothing.
- The new case's preflight and Edit records carry no `usage`, so the sibling's request is the only
  usage the transcript holds: both readers take it, and the window's scan observes it alone.
- The `--orient` paragraph is unchanged: the `context` paragraph of `tools/runlog/README.md` now says
  that `--orient` derives each model's window once under the dir it reads.

## The superseded wording of units 30 and 9 (S4)

Units 30 and 9 are CLOSED, so their specs and ledgers stay as they are and the answers are here (F1).

- Unit 30 S2 says `derive_context_fill(ev, window=None)` "takes an explicit window, or derives one from `ev["model"]` under the default root, so `KICK-dKeptSession-9`'s per-stage rows read the same window with no change to their call". Read it as S1 and S2 of this unit: the fill takes `window=` or `root=` by name and raises with neither, and the orient report derives its cached window under its own `root`, the `--orient` dir, and passes it as `window=`.
- Unit 30 S2 says the context-fill case's liveness check "calls `derive_context_fill(usage[-1])` with no window, under the default root the launcher aims at the decoy". Read it as S1's `root=projects`, the case's own root, whose observation of 180000 on `fixture-model` at most derives the 200000 rung, so the agent's 190000 still reads `0.95` (DERIVED, the `context-fill` scenario of `tools/runlog/fixtures/transcripts.json`).
- Unit 9 S2 gives each row's `context` as `derive_context_fill(ev)` "of the last main-source usage event before it". Read the call as S2 of this unit, `derive_context_fill(last, window=<the window cached per model under root>)`, which is the share `root=root` would give.

**Evidences:** KICK-dKeptSession-46
- AC1 — `runlog.py extract --orient <dir> --slug fx --repo <repo>` exited 0 and printed one `orient row` for the main file, `action=edit calls=1 tokens=900010 context=90%` (DERIVED, that probe). With the window derived under no root, the probe's `measure_orient_tree` read `4.5`, the `450%` the criterion's red names (DERIVED, that probe, through a patched `derive_context_window` in that probe's own process).
- AC2 — `runlog.py context <transcript>` on the same file exited 0 printing `90%`, with `context: window 1000000 · observed 900000 on fixture-model` on stderr (DERIVED, that probe).
- AC3 — `extract.derive_context_fill(ev)` with neither argument raised `ValueError` reading `derive_context_fill: pass window= or root=`; with a window by position it raised `TypeError`; over the `context-fill` scenario its last usage, `src` `agent`, read `0.95` with `root=` that scenario's projects dir (DERIVED, that probe).
- AC4 — the three passages are quoted above, each once; `git diff --name-only` from the pass's base over the specs and acceptance ledgers of units 30 and 9 prints nothing, since this commit writes none of them (DERIVED, that probe at the commit).
- AC5 — the `context` paragraph of `tools/runlog/README.md` names `derive_context_fill(ev, *, window=None, root=None)` and no longer holds the phrase its default-root sentence carried (DERIVED, `tr` and `grep` at the commit).
- `ASSERTION_FLOOR` rises from 1618 to 1624: the new case's 3 checks and its 3 decoy checks (PINNED, the count its `RAISED` comment prices).
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_extract_context_fill_root`: `derive_context_fill` falls back to the default root
