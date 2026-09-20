# Acceptance ledger — TOOL-dLoggedFlight-14

**Serves:** journal TOOL-dLoggedFlight-14

Tier-2 · node d · 2026-09-16 · the build pass of source order, against spec rev-4. Nothing in the
spec's design moved, so the pass flips its status and bumps no rev. No suite and no gate leg ran, per
the owner's instruction of 2026-09-13: `tools/runlog/selftest.py` was not run, imported or copied.
The change was observed instead by one throwaway Python script kept outside the repository. It
imported `extract`, `model` and `record` from the kit, built its own git-only and journal-backed
fixture runs, transcripts and stores, all synthetic, and called `build_run_model`,
`resolve_run_sessions` and `render_record` over them. Every staged break below was applied to an
in-memory copy of the model's source, never to the file, and the parent commit's model, e89add11, was
loaded the same way to see the defect itself read red. Twenty observations held. The suite's three
new arms are written and its floor is raised from 1317 to 1338; each arm's verdict is owed to the
post-build run, with the break that stages it RED named beside it.

## The criteria

**Evidences:** TOOL-dLoggedFlight-14

- AC1 — `build_run_model` — over a run whose driver journal names one session, with a twenty-minute
  driver silence from minute 4 to minute 24, an owner turn at minute 20 and a store extract cut at
  minute 4 whose `extracted_at` covers the window, the model read the local transcript: the
  transcripts read `present`, no idle row lay within `IDLE_OWNER_GUARD_S` of the turn, the in-window
  owner count was 1, and the idle block read judged, 0 gaps, 1 kept out beside an owner turn. The
  same store with no transcript local read 0 owner turns and one idle row ending 4 minutes after the
  turn. Staged in memory, a named session read from its store extract whenever one exists gave that
  idle row and the count 0, and so did the parent commit's model. Owed:
  `test_source_ac1_transcript_first`, staged RED by reading the store extract before the transcript
  on the named path.
  MET at the post-build run: `test_source_ac1_transcript_first` is GREEN, inside
  `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC3 — `build_run_model` — over a git-only run no journal names a session of, the discovered session
  with a stale store extract cut before its owner turn and its transcript local read `present`, one
  extract, 1 owner turn and 4 calls, the transcript's; with no transcript local it read `stale` and 0
  owner turns. A stale extract of the whole session, with no transcript local, read `stale`, and its
  record rendered `judged no` for idle gaps and `-` for every owner-turn, usage and attributed-call
  count, while the model held 1 owner turn and calls; the same extract stamped fresh read `present`,
  `judged yes` and integers. Staged in memory, a discovered path that never resolves a local tree read
  `stale` over the local transcript, and the freshness test applied to named sessions only rendered
  the stale shape `present`, `judged yes` and integers. Owed: `test_source_ac3_discovered_order`,
  staged RED by either break.
  MET at the post-build run: `test_source_ac3_discovered_order` is GREEN, inside
  `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC6 — `python tools/memory-tree/gotchas.py --for-paths tools/runlog/model.py` — run directly, it
  selected `withheld-value-recovered-from-a-derived-one` among its anchored classes. The record names
  the instance as a cache preferred over its source with its freshness key never read, R2-B1 of the
  closing review's round 2, and adds no path anchor, so the catalogue index's anchor count for it is
  unchanged. The `memory hygiene` leg's index-freshness verdict is owed to the post-build run.
  MET at the post-build run: `memory hygiene` is GREEN in 29.1 s, so the catalogue index is fresh.
- AC7 — `build_run_model` — the discovered run's store held its own session, fresh, and an earlier
  session of the same slug whose every event and `extracted_at` precede the window's start. With no
  transcript local the Coverage `sessions` fact read `1 extracted` and the state `present`, the state
  the run's own session gives alone; over a window opening two hours earlier `resolve_run_sessions`
  read both sessions and `stale`, so the store holds what the window keeps out. With the earlier
  session's transcript local and `extract_session` wrapped to count its calls, a file last modified a
  minute before the window's start was extracted 0 times, and one modified at the start was extracted
  once and still counted out, `1 extracted` and `present` both times. Staged in memory: the store
  extract kept without an in-window event moved the count and the state; the modification-time test
  removed extracted the older file once; the in-window test skipped after extraction rendered
  `2 extracted`. The parent commit's model rendered `2 extracted` and `stale`. Owed:
  `test_source_ac7_discovered_reach`, staged RED by any of the three.
  MET at the post-build run: `test_source_ac7_discovered_reach` is GREEN, inside
  `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`.

## What else the pass carried

- A local main transcript that will not open falls back to the store, as spec section 5 names; this
  was not staged, because no file on this node refuses its owner a read.
- A discovered session extracted in memory is attributed `heuristic`. A session the journal names is
  never dropped by the reach test, which S4 scopes to the discovered path.
- The model's `method` entry for `sessions` names the reach test and the source order.
- `build_session_events` in the suite takes an optional projects root, and `build_model` passes
  `projects` through. AC3 and AC7 build their own git-only run with a dispatch row, because
  `render_record` refuses a run that dispatched or closed no unit, which the gaps fixture is.
- The kit README gains the source-order bullet in the run model section and the discovered path's
  residue among what the kit does not check. The Skill is not re-rendered: its Stale transcript
  bullet stays true, since a render reads `stale` now only where no transcript is local.
- The runlog dossier lists `TOOL-dLoggedFlight-14` among its decisions. It sat 2 bytes under check 6's
  cap, so one filler clause in its redact() bullet went; it now sits 5 bytes under.

## Owed to the post-build gate run

- `runlog selftest` — the three new arms and every arm whose model now reads through the reach test,
  at a floor of 1338, and its budget row, which the new arms' model builds move.
- `lexicon naming predicates`, `codebase-map coverage + freshness` and `memory hygiene`, the gates the
  spec names. Each new function name was answered `OK` by `lexicon.py --suggest`, which is not the leg.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so all three new arms are GREEN; this unit's floor of 1338 has risen with the units after it. The
run settles the hand-derived chain that carried it there: executed equals floor exactly, so no
step in it ever put the floor above the true total. The suite cost 80 s run directly, under the 93
s its budget row declares, so `tools/run-gates/selftest-budgets.txt` does not move; inside the
bar's 8-wide pool the same leg recorded 93.9 s, a contention reading that file's own header says
to re-read on a quiet box. `lexicon naming predicates`, `codebase-map coverage + freshness` and
`memory hygiene` are GREEN too. The run's one RED, `govkit selftest`, is on none of these legs:
its 30 failing assertions are the IDENTICAL set `origin/main` carries, pre-existing, untouched by
this build and being fixed in a separate session. It is not called green here.
