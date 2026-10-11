# Run handoff — aRoutedQuill

**Serves:** journal TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7

node a · 2026-10-09 · written by the attended session that specced the build, for the unattended
run that builds it · authorized-by slug

This record carries only what the README, the specs and the method do not. The README is the
authorization and the roster; each spec's §8 holds the owner's rulings, marked in place. Read this
whole after the README and before the first pass.

## Starting the run

- The owner's act is `/unattended aRoutedQuill` in a fresh session. The README is committed on the
  default branch, so the run is in `slug` mode at the default-branch anchor.
- No directive is waived, and no spec audit is owed: the README declares no `spec-audit:`, by the
  owner's ruling of 2026-10-09.
- Every judgement fork is resolved by the owner. The run decides only the two `FACT-QUESTION` forks
  below, by their probe, as the build method allows.

## The order

| Step | Unit | Disposition in this run |
|---|---|---|
| 1 | `TOOL-aRoutedQuill-1` | build |
| 2 | `KICK-aRoutedQuill-1` | build |
| 3 | `TOOL-aRoutedQuill-2` | run the probe first, then build |
| 4 | `TOOL-aRoutedQuill-3`, `TOOL-aRoutedQuill-4` | build, in parallel |
| 5 | `PLAY-aRoutedQuill-1`, `TOOL-aRoutedQuill-5` | build, in parallel |
| 6 | `TOOL-aRoutedQuill-6` | carry forward, never build here |
| 6 | `TOOL-aRoutedQuill-7` | build only once its external precondition holds, else carry forward |

## Before the gate unit: the one probe

`TOOL-aRoutedQuill-2` F1 and `TOOL-aRoutedQuill-4` F1 are `FACT-QUESTION` forks with one probe
between them. Each spec's §8 names the probe, the deciding observation and the liveness assertion.
Run it once, before step 3's pass, in a throwaway clone made with `git clone --local` under a short
`%TEMP%` root, because a clone in the scratchpad hits MAX_PATH. Record the observation in a
`build/` record, then mark both forks `RESOLVED (agent, <date>, delegated)`. A spawn kind with no
logged line is a DEAD PROBE for that kind, never a "no".

## Enforcement starts inside this run

- A settings edit is live on the next tool call (`memory/gotchas/settings-edit-takes-effect-mid-session.md`).
  So the moment step 3's commit wires gov's `.claude/settings.json`, this run's own product writes
  are gated, and so are its builder subagents'.
- From then on, before a unit's first product write, append a `## route` naming that unit to the
  session's card through `manifest-check.sh --card --append`; step 2 builds that path. A Tier-2 unit
  admits writes only at INPROGRESS, so flip the spec's status before the route goes on.
- From step 4's commit, every commit touching `ROUTED_PATHS` names its unit in the subject or the
  `Pass:` trailer. That includes close repairs and version mints, which name the build's last unit
  (`TOOL-aRoutedQuill-3` F3). Check before the close whether the lander writes any commit of its own
  that cannot carry an id; that would red this run's own leg.

## The two units that may not build here

- **`TOOL-aRoutedQuill-6`, the trial.** Its own spec runs it in an attended session and never under
  the unattended driver: it needs four owner asks and an approved budget. Carry it forward under
  `memory/guides/UNATTENDED-STOPS.md` §15. File an ask in this build's `BACKLOG.md`, give the spec
  header an `advances` verb naming that ask, and run `unattended.sh --rescope aRoutedQuill --act defer`.
  No unit consumes from it, so the fifth carry-forward condition holds.
- **`TOOL-aRoutedQuill-7`, the repoint.** It consumes `TOOL-aQuotedBrief-1`, which another unattended
  run is building now on `branch/unattended-build-template-5f7d7d`. At step 6, build it only when
  that spec reads CLOSED on `origin/main`; otherwise carry it forward the same way. It edits
  `tools/unattended/`, so run `git log origin/main --oneline -20 -- tools/unattended/` first.

## Agreed with the session building aQuotedBrief, 2026-10-09

- `KICK-aRoutedQuill-1` owns the one brief shape. `TOOL-aQuotedBrief-1` builds as specced, with its
  five sub-heads fixed, and `TOOL-aRoutedQuill-7` later points its check at `--brief-skeleton`.
- `read_audit_ask_record` keeps reading only `## The prompt`, so nothing under `## The brief` can opt
  a build into the spec audit.
- A new row in `memory/guides/UNATTENDED-PROTOCOL.md` raises its ceiling in
  `tools/template-size-limits.txt` by the row's bytes, rather than trimming the protocol. That is the
  owner's ruling, for both builds' rows.

## Gates and suites

- A pass runs fast, diff-scoped, direct checks only: no merge bar and no self-test suite. Put "fast
  diff-scoped gates only, nothing held" in every unit brief's ground text, because the unit builder
  otherwise runs every suite its criteria name, concurrently.
- The close's bar is `GATE_FULL=1` alone. The owed kit self-test suites are not run at the close; the
  owner runs them later from the merged tree.
- Kit versions bump once per kit, after its last unit. Run `python tools/govkit/govkit.py epoch --base
  <BASE>` before the close, and grep every version carrier after a reconcile.

## Corrections made after the specs were first written

- `TOOL-aRoutedQuill-2` rev-4 and `TOOL-aRoutedQuill-4` rev-3: hooks are re-read on the next tool
  call, not at session start. Both rollouts now say enforcement begins inside the landing session.
- The gate widens the one existing `scratch-guard` fragment's matcher. A second fragment for the same
  script would be silently dropped by `settings-merge.py`, which matches on the script's name.

## Corrections made by the run, 2026-10-09

- The push leg grades the WHOLE pushed range from `ROUTED_COMMIT_CUTOFF`, not only the commits after
  step 4. So from this run's FIRST commit, every commit touching `ROUTED_PATHS` names its unit in the
  subject or the `Pass:` trailer, not only from step 4 on.
- Step 4's `TOOL-aRoutedQuill-3` and `TOOL-aRoutedQuill-4` both write `memory/map/generated/`, so they
  are SEQUENCED, not parallel (`memory/guides/BUILD-METHOD.md` M6 clause 3). The second re-renders
  `memory/map/generated/` with `python tools/codebase-map/gen_map.py --write` rather than reconciling
  it by hand.
