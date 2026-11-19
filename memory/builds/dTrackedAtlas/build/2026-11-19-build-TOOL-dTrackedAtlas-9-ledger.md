# TOOL-dTrackedAtlas-9 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-9

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command, from the worktree root or in `$FX`, a `--shared` clone of the worktree at `%TEMP%/ta9fx` planted
exactly as the spec's section 5 plants it, with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` unset. The plant
made `$P` = `d7c76c2f423f`, the prepared merge, and `$T` = `4de7eee1e00b`, the run tip after it; AC3 made
`$L` = `f37f03d83c69`, parents `9e21ac760` and `$T`. These shas name the removed clone's objects only.
The clone was removed after AC6, and the real repository's refs were never written. Every JSON, stderr
capture and probe sat in the run's scratch directory.

Each red was observed on the shape the criterion names: the derivation as it stood at the pass's start,
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py` at `cb9f7431c`,
run before any edit; or a staged break made by a scratch probe that loads the changed module by path and
swaps one function before calling its `main`, so no tracked file was edited to stage a red.

**Evidences:** TOOL-dTrackedAtlas-9
- AC1 — in `$FX` with `refs/remotes/origin/main` at `9e21ac760`, `--ref "$T" --claims none` exited `0`.
  `landed` named dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter, dFairHearing, dDeclaredLoop
  (PINNED at `9e21ac760`). dWitnessedBar read `not-landed`, `landing` null, its `RUN.md` record's
  `landings` empty; `startable` was dPlacedRequest, dWitnessedBar. `default_ref` read
  `refs/remotes/origin/main` and `default_commit` `9e21ac760dc0a43d6ed007396922722ccee98d57`.
  Red: the module at `cb9f7431c`, same command, read `7` landed (PINNED at `9e21ac760`), dWitnessedBar
  `landed-carrying` with `landing.sha` `$P`.
- AC2 — after `git update-ref refs/remotes/origin/main "$P"`, `--ref "$P" --claims none` read `7` landed
  (PINNED at `$P`), dWitnessedBar's `landing.sha` `$P`, `startable` dPlacedRequest alone, `default_commit`
  `$P`; at `--ref "$T"` dWitnessedBar read landed through `$P` too. The schedule,
  `"$PY" "$WT/$SCHED" --ref "$P"` with no new option, printed `builds landed 7`. Red: the same derivation
  pinned with `--default-ref 9e21ac760` at `--ref "$P"` read `6` landed (PINNED at `9e21ac760`),
  dWitnessedBar `not-landed`.
- AC3 — with `main2` merged and `refs/remotes/origin/main` at `$L`, `--ref "$T" --claims none` read
  dWitnessedBar `not-landed`; at `--ref "$L"` it read `landed-carrying`, `landing.sha` `$L`, and its
  `RUN.md` record's `landings` listed `$L` alone. Red: a probe loading the changed module by path with
  `derive_landings` swapped for the first-parent line of `git merge-base "$T" "$L"`, which printed `$T`
  itself, read dWitnessedBar `landed-carrying` at `--ref "$T"` with `landing.sha` `$P`.
- AC4 — in the worktree, `--ref 5125f93ea --default-ref 9e21ac760 --claims none` read `landed`
  dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter, dFairHearing; dDeclaredLoop `not-landed`,
  `landing` null, `next.state` `startable`; `default_ref` `9e21ac760`, `default_commit`
  `9e21ac760dc0a43d6ed007396922722ccee98d57`. At `--ref b55a6494a` it read `landed` dTrueNorth,
  dGroundRules, dSafePassage, and dFairHearing `not-landed`. Red: the module at `cb9f7431c`,
  `--ref 5125f93ea --claims none`, read dDeclaredLoop `landed-carrying` with landing `67f1ffb18`, and at
  `--ref b55a6494a` read dFairHearing `landed` through `7b42f2c47`.
- AC5 — `--ref 9e21ac760 --default-ref 9e21ac760 --claims none` read the six of unit 1's AC2, with
  `landing.sha` values beginning `2511c1181`, `3c0318d95`, `3ada42ab1`, `9760fb746`, `0a760477e` and
  `9e21ac760`; dDeclaredLoop's build-kind run listed `c1f80c002` then `9e21ac760`; `startable` and
  `ready` both dPlacedRequest, dWitnessedBar. Red: a probe with `derive_landings` swapped to read the
  ref's own first-parent merges inside `<default>..<ref>` read `landed` empty, `[]`.
- AC6 — `--ref 9e21ac760 --default-ref nosuchref --claims none` exited `2`, stdout empty, and stderr the
  one line `build-state: the default-branch ref nosuchref resolves to no commit in .; pass --default-ref <rev>`.
  `--default-ref=-x` exited `2` with the one line `build-state: --default-ref takes a revision, not -x`.
  In `$FX` after `git symbolic-ref --delete refs/remotes/origin/HEAD`, `--ref "$T" --claims none` exited
  `2` with the one line `build-state: the remote ladder names no default branch here; pass --default-ref <rev>`.
  Beyond the criterion, `GOV_REMOTE=nosuch` in `$FX` exited `2` with the ladder's own refusal text
  followed by `Or pass --default-ref <rev>`. Red: a probe with `resolve_default_ref` swapped to fall back
  to `--ref` on a refusal exited `0` in the same clone state, `default_ref` `$T`, dWitnessedBar
  `landed-carrying` through `$P`.
- AC7 — `"$PY" "$ATLAS" --ref 9e21ac760 --claims none --out <scratch>/p9.html` exited `0`; the page's
  `grep -o` printed `"default_ref":"refs/remotes/origin/main"`, and its `default_commit`,
  `9e21ac760dc0a43d6ed007396922722ccee98d57`, equalled `git rev-parse refs/remotes/origin/main` at
  observation time (DERIVED). Red: a probe running the Atlas's `main` with only `derive_actual`'s load of
  the derivation swapped for a wrapper passing the Atlas's own `--ref` as the default ref printed
  `"default_ref":"9e21ac760"`.
- AC8 — over the schedule, `grep -c "first-parent merge of --ref"` printed `0` and
  `grep -c "default branch's first-parent line"` printed `1`; over the derivation,
  `grep -c -- "--default-ref"` printed `8` and `grep -c "has not fetched"` printed `1`, from the module
  docstring. Red: before the edit, at `cb9f7431c`, the four printed `1`, `0`, `0` and `0`.

Owed to the close: the plain bar, whose legs section 6 names; `chain-packet self-test` keeps the
CP3, CP4 and CP5 reds ask `TOOL-dTrackedAtlas-6` already owes under `GATE_SELFTESTS=1`, now at this
pass's schedule blob. No suite arm is added, so no `New arm:` observation is owed.
