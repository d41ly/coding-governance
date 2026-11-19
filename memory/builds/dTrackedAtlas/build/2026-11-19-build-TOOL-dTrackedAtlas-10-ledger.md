# TOOL-dTrackedAtlas-10 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-10

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command in `$FX`, a `--shared` clone of the worktree at `%TEMP%/ta10fx`, from the clone's root, with
`GOV_REMOTE` and `GOV_DEFAULT_BRANCH` unset. The pass's generator was carried into the clone as one
fixture commit on top of the pass's base `ffcceea59`, so `$T0` = `bb0566e38140` is the run branch's tip
carrying this unit; the section 5 plant then made `$B` = `e65919010b17`. AC1 made `$M` = `0c418816ed34`,
AC3 made `$P` = `d79d1016bbf8`, and AC4 moved the default branch to `f34cf076321e`. These shas name the
removed clone's objects only. Every page, as `$S/<name>.html`, and every probe sat in the run's scratch
directory, and every generation passed `--claims none`. The clone was removed after AC6, and the real
repository's refs were never written: `refs/remotes/origin/main` read `9e21ac760` after.

Each red was observed on the shape the criterion names, by a scratch probe that loads the clone's
generator by path, swaps one function in memory and calls its `check_page`; where the red needs a stamp
of that shape, a second scratch probe copied the page's data with only the stamp's `digest` replaced by
the staged function's value. No tracked file was edited to stage a red.

**Evidences:** TOOL-dTrackedAtlas-10
- AC1 — at `$B`, `--claims none --out "$S/p0.html"` exited `0` and its check exited `0`, reading
  `atlas: current` with inputs `30665d796577`. After the merge, `git diff --name-only "$B" "$M"` printed
  only `memory/builds/dTrackedAtlas/README.md`. `--check --page "$S/p0.html" --ref "$M"` exited `1` with
  `atlas: stale — $S/p0.html: the inputs stamped at e65919010b17 moved by 0c418816ed34… (0c418816ed34)`,
  then `  landings of dWitnessedBar moved: 0c418816ed34`, then `  0c418816ed34 fixture: land`.
  `--ref "$B"` exited `0`, `atlas: current`. `--out "$S/p1.html"` at `$M` then checked `0`, inputs
  `ace45af6ca95`. `p0.html`'s `state.landed` named dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter,
  dFairHearing, dDeclaredLoop; `p1.html`'s named those and dWitnessedBar. Red: a stamp of the tree-only
  digest at `$B`, `cabe84fce94c`, checked by the generator with `derive_input_digest` staged to the tree
  listing alone, `TOOL-dTrackedAtlas-3`'s shape, exited `0` at `--ref "$M"` reading `atlas: current`.
  cost: `32` s for the first generation (PINNED, this pass), under the spec's minutes.
- AC2 — `p1.html`'s stamp read `schema` `2` and `default_ref` `refs/remotes/origin/main`; its `landings`
  keys equalled the page's `state.builds` slugs, `22` of them (DERIVED, from the page's `state`), and
  `landings.dWitnessedBar` equalled the reversed `git log --first-parent --merges --format=%H "$M" -- memory/builds/dWitnessedBar/RUN.md`,
  `9a1845bd4a8c` then `0c418816ed34`. Hashing `git ls-tree -r -z "$M" -- <inputs>`, a NUL byte and the
  compact sorted JSON of `default_ref` and `landings` printed `ace45af6ca951f7f…`, the stamp's `digest`;
  the plain `git ls-tree -r -z "$M" -- <inputs> | sha256sum` printed `cabe84fce94c50468…`, which the
  stamp does not carry. Red: a copy of `p1.html` whose `digest` was the tree-only value, `$S/p1-red.html`,
  matched that `sha256sum` and no longer matched the history-folded recomputation.
- AC3 — at `$P`, with `refs/remotes/origin/main` at `$T0`, `--out "$S/p2.html"` exited `0` and its check
  at `--ref "$P"` exited `0`, `atlas: current`. After `git update-ref refs/remotes/origin/main "$P"` the
  same check exited `1`: `atlas: stale — $S/p2.html: the inputs stamped at d79d1016bbf8 moved by d79d1016bbf8… (d79d1016bbf8)`
  and `  landings of dWitnessedBar moved: d79d1016bbf8`, with no commit line. Red: the generator with
  `read_landings` staged to measure against the stamp-time default commit `$T0` rather than re-resolving
  `default_ref` exited `0` on the same check, `atlas: current`.
- AC4 — after a second `README.md` commit on `fx-main`, `f34cf076321e`, became
  `refs/remotes/origin/main`, `--check --page "$S/p1.html" --ref "$M"` exited `0`, `atlas: current`,
  inputs `ace45af6ca95`. Red: a stamp of `p1.html` whose digest also folds the default branch's commit,
  §7 F3 (a), planted while the default branch was at `$M`, checked `0` before the move and `1`,
  `atlas: stale`, after it, under a generator staged to fold that commit.
- AC5 — copies of `p1.html` made by a `"$PY"` one-liner each exited `1` with `atlas: unstamped`:
  `$S/p1-old.html` naming `the stamp's schema field fails its rule:1`, `$S/p1-bad.html` naming
  `the stamp's landings field fails its rule:…`, and `$S/p1-dash.html` naming
  `the stamp's default_ref field fails its rule:"-x"`. Red: with `read_stamp` staged to drop the three
  rules, `p1-old.html` and `p1-bad.html` each exited `0`, `atlas: current`, and `p1-dash.html` carried
  `-x` past the read boundary to the derivation's resolver, which refused it with
  `atlas: cannot check: --default-ref takes a revision, not -x`, exit `2`; it reached no git call
  because that resolver's own guard stopped it first.
- AC6 — after `git update-ref -d refs/remotes/origin/main`, `--check --page "$S/p1.html" --ref "$M"`
  exited `2`, `0` bytes on stdout (PINNED, this pass), and one stderr line,
  `atlas: cannot check: the default-branch ref refs/remotes/origin/main resolves to no commit in <the clone>; pass --default-ref <rev>`.
  The ref was restored to `$M` after. Red: `read_landings` staged without its `StateError` translation
  ended in a traceback, `atlas_build_state.StateError: the default-branch ref refs/remotes/origin/main …`.
- AC7 — over the pass's generator, `grep -c "spec_from_file_location"` printed `1` and
  `grep -c "TOOL-dTrackedAtlas-10"` printed `6`, one of them the module docstring's sentence of §4
  "The module docstring". Red: the generator at `ffcceea59` printed `2` for the first grep, its two inline
  loaders; a staged copy of the pass's generator whose `read_landings` carries its own inline loader
  printed `2`, so the criterion's `1` refuses it, though not with the `3` the spec's red names, since the
  staged copy keeps `load_build_state` and drops the two old copies.

Probed beside the criteria: the AC6 refusal's text ends `pass --default-ref <rev>`, the derivation's own
wording carried through as §4 "The landing reader" says; the Atlas has no such option, by §3.

Owed to the close: the plain bar, whose legs section 6 names. No suite arm is added, so no `New arm:`
observation is owed.
