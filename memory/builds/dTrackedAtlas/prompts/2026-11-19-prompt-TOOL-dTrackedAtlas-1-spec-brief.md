**Serves:** research TOOL-dTrackedAtlas-1

# Spec brief — TOOL-dTrackedAtlas-1: one chain build-state derivation, shared by the schedule and the Atlas

You author ONE spec and write no product code. Read first, whole: the build README
`memory/builds/dTrackedAtlas/README.md`, the prompt record
`memory/builds/dTrackedAtlas/prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md` (it quotes the owner and
carries every measurement), `memory/TEMPLATE-SPEC.md`, and `memory/guides/BUILD-METHOD.md` at `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`,
`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m5-recall-and-reuse` and
`doc.build-method#m12-research-test-choose-when-the-solution-is-not-given`.
Units 2, 3 and 4 are specced AFTER this one and read its interface section as their contract, so state the
interface exactly: module path, function names, signatures, the returned shape and every field name.

## The mechanism

One derivation, read from the tree at a git ref, of every dClosedLoop chain build's actual state. Per build:
its spec run (done or not), its build run (landed, not built, or landed with units carried forward), the
first-parent landing merge on the default branch that landed the build run (sha and subject), unit counts by
spec status, open forks (unresolved §8 items), spec revisions, the deviation records it owns, its run claim where
one is cached, and whether its next run can start now under the schedule's Policy J. The schedule script's
`tree_state` (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py#tree_state`) stops being a
second answer: it reads this derivation, so both print the same landed set.

## Facts measured at origin/main `9e21ac760` (re-verify each before you rely on it)

- The schedule prints `specs done 22, builds landed 4`; six build runs have landed: dTrueNorth, dGroundRules,
  dSafePassage (merge `3ada42ab1`), dFairHearing (`0a760477e`), dOrderedCharter (`9760fb746`), dDeclaredLoop
  (`9e21ac760`; an earlier landing merge `c1f80c002` sits below it). The two runs that could start at that tree
  were dWitnessedBar's and dPlacedRequest's build runs. Both hold live claims on the remote now: a claimed run is
  running, not startable, and the state must say which.
- Status counts: dSafePassage 98 CLOSED, 1 DEFERRED (TOOL-dSafePassage-61, `advances TOOL-dSafePassage-14`),
  1 WONTDO; dDeclaredLoop 101 CLOSED, 1 DEFERRED (TOOL-dDeclaredLoop-34, `advances TOOL-dDeclaredLoop-35`),
  1 WONTDO; dWitnessedBar 88 DEFERRED; dPlacedRequest 63 DEFERRED; dTrueNorth 30 CLOSED.
- A chain spec run carries every unit forward as DEFERRED to its build run (PLAY-dClosedLoop-2 in
  `memory/DECISIONS.md`); a build run closes its units and may carry one forward, DEFERRED with `closes` or
  `advances` naming an open ask (`memory/guides/UNATTENDED-VERBS.md`, Close step 9). A DEFERRED spec that
  advances a later ask is not an unbuilt unit. Read the DEFERRED semantics there before you choose the predicate,
  and record in §8 the candidates you weighed and the observation that rejected each (M12).
- Each build folder holds `RUN.md` and retired `RUN.LANDED.<blob8>.md` records with `phase:`, `mode:`,
  `witness:`, `landed-derived:` and `units-at-landing:` facts; the unattended driver already derives a run's
  landing commit (`read_landing_commit` in `tools/unattended/lib-unattended.sh`). Merge subjects
  (`merge: <slug> — land onto origin/main at <sha>`) do not say whether a spec run or a build run landed.
- `tools/memory-tree/tree_lib.py` names `TERMINAL = (CLOSED, WONTDO)` and `CENSUS_TERMINAL` with DEFERRED.
  `tools/policy/check_policy.py` `derive_landed_owners` is a second copy of the miscounting rule; it is out of this
  unit (it is under `tools/`), and the build files it as an ask.
- Claims: `bash tools/unattended/unattended.sh --claims` caches them under `refs/gov/remote/runs/<slug>`; the
  schedule's `claims()` already reads that cache with `RESUME_STALE_BOUND`.
- Deviation records: `tools/memory-tree/deviation_join.py` and `deviations.py`; the as-built view is
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`.

## Constraints

- The derivation lives in ONE new file in THIS build's folder, `memory/builds/dTrackedAtlas/build/`, named by the
  recording grammar (`2026-11-19-build-TOOL-dTrackedAtlas-1-<slug>.py`, first line `# **Serves:** …`), and the
  schedule and the Atlas load it by path. No new file under `memory/builds/dClosedLoop/build/` (dClosedLoop's
  held spec grows a row per file and reds spec tokens), and nothing under `tools/` (it owes a `GATE_SELFTESTS`
  bar this run may not run). Reading `tools/` code, by import or subprocess, is allowed.
- Every read is at a ref (`git show <ref>:<path>`, `git ls-tree`), never the working tree, so a fixture ref can
  plant a landing. Bound every git call.
- Acceptance names direct observations: the schedule script at `9e21ac760` printing `builds landed 6` and
  planning no run for dSafePassage or dDeclaredLoop; the derivation's own JSON at that ref naming the six landed
  build runs with their merges and the two startable runs; and a planted landing on a fixture ref (a scratch
  clone, never the real repository's refs) moving the landed set, the merge and the startable set. Each red case
  is observed red before green. No gate, suite or bar in any criterion.
- Tier: this writes build-folder instruments, not a shipped kit; assign it by `memory/guides/SESSION-KICKOFF.md`.
