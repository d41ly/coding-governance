# aDistilledCharter — the landing, and what it still owes

**Serves:** journal PLAY-aDistilledCharter-1

The build LANDED on 2026-10-11: `origin/main` fast-forwarded `b726385f..f75cffbe`, 41 commits. The
owner ordered it pushed with `git push --no-verify`, so the pre-push bar did not run, and no full bar
ever completed on the landed tree.

## How it got there

- `60bea5e80` reconciled with `origin/main` at `d006cfc5`, 184 commits past BASE `6473ae38`. Of 37
  conflicts, 31 were kit-version markers and took origin's side; the merge message names the rest.
- `3b8100edc` reconciled with `69e0ff0f`, aRoutedQuill's landing. Its v3.6 template added two rules,
  and both moved into v4.1: spec-before-code became the section-1 practice `[spec]`, and the write
  gate became a `kit:agent-cap` line under "Tools to rely on".
- `push-main.sh --prepare` made three landing merges as the tip kept moving; `f75cffbe`, onto
  `b726385f`, is the one pushed. The kickoff manifest was re-stamped after each reconcile and mint.

## The bar, as far as it got

- At `9ab879831`, before either reconcile: 62 of the 63 legs that ran were green. `straggler-guard
  arms` timed out twice on a contended host; run alone it passed 84 assertions in 863 s against a
  300 s ceiling. The 63 self-test legs were held.
- At `bc58ce713`: `codebase-map coverage + freshness` redded because the landing mint moved
  `codebase-map` 1.26 to 1.27 and left the generated map stamping 1.26. The map was regenerated in
  `3b8100edc`. That bar was stopped, since it could not record a green.
- At `f75cffbe`: the bar was stopped when the owner chose to land without it.

## Still owed

- A full bar on `main` at or after `f75cffbe`, which no run has produced.
- The kit self-tests, which the owner runs from the merged tree.
- The remote CI jobs a push to `main` starts, read rather than assumed.
- The rollout to adopters, which is a `govkit update` per repository and was out of this build's scope.
