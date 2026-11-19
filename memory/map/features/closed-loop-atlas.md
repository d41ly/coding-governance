# closed loop atlas — the chain's build state, the page that states it, and the page kept current

```toml
feature = "closed-loop-atlas"
title = "The chain build state the schedule and the Closed Loop Atlas share, the page's stamp and stale check, and its regeneration on node d after main moves"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dTrackedAtlas-1", "TOOL-dTrackedAtlas-2", "TOOL-dTrackedAtlas-3",
  "TOOL-dTrackedAtlas-4"]

stage = ["step.plan", "step.deploy"]

[claims]
gate-legs = []
kits = []
git-hooks = []
harness-hooks = ["PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js"]
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py",
  "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js",
  "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py",
  "memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py",
]
```

## Constraints & why

**One derivation of chain build state, read by both instruments.** The schedule script and the Atlas
generator once answered "what has landed and what can start next" each in its own way, and the two
answers disagreed with the tree. Both now read the one derivation in this build's folder, so the page
and the schedule cannot drift apart on that question.

**The page carries its own stamp and refuses to look current when it is not.** The generator stamps
the commit and a digest of the inputs it read; its `--check --page` recomputes that digest at a ref
and answers current, stale or absent. A page the tree moved past says so instead of looking fresh.

**The page regenerates on node d after `main` moves, with no command typed for it.** A
`PostToolUse` hook runs after every shell call, and its fast path only stats a stamp and starts a
detached runner once per throttle window. The runner reads `refs/remotes/origin/main`, asks the page
check, and only when the page is stale regenerates it in a scratch checkout of that tip, because the
session's own checkout is in general neither at the tip nor clean. A switch, `atlas.regenerate`,
defaults on; a node without the page's folder does nothing and says so on a lander call.

**Everything lives in build folders, not in a kit.** The page is a node-d instrument, so no adopter
receives it; the hook's one row under `tools/` is the loop table's stage claim of its key.

## Shared seams

- The hook follows the process monitor's fail-open fast path and stamp throttle
  (`tools/process-monitor/procmon-hook.js`), and the post-merge bar's environment scrub before its
  first git call (`tools/run-gates/post-merge.sh`).
- The interpreter is resolved by `tools/lib/resolve-python.sh`, the resolver every instrument here uses.
- The switch's interim home is a JSON conf beside the hook; its move into the policy catalogue is a
  hand-off ask, carrying the catalogue row the unit's spec gives.

## Gaps

- The runner trusts this clone's remote-tracking ref and never fetches, so a landing made on another
  node reaches the page only when something on node d next moves that ref.
- A landing made at a console with no agent session running on node d waits for the next shell call
  of any session there.
- Code under `tools/` that the generator reuses is outside the page's input digest, so a tip that
  moves only `tools/` reads current.
- A page edited by hand after a regeneration is not detected.

## Reuse affordance

seam: memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive — reuse for any reader of chain build state; extend via a new field of its result.
