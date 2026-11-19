# TOOL-dTrackedAtlas-1 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-1

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command over the real tree at `9e21ac760`, read through git and never the working tree, or over a scratch
clone at `%TEMP%/ta1fx` (a `--shared` clone checked out at `9e21ac760`, removed after; the real
repository's refs were never written). Each red case was observed on the shape the criterion names: the
schedule as it stood at the unit's start, the clone before its planted landing, or a staged break in a
probe that loads the derivation and swaps one object.

**Evidences:** TOOL-dTrackedAtlas-1
- AC1 — `"$PY" "$SCHED" --ref 9e21ac760` printed `specs done 22, builds landed 6`; the rows of
  dSafePassage and dDeclaredLoop read `done | done`; "runs the owner starts" names 16 runs and neither
  build. The claims line is byte-equal to the pre-change one. Red: the schedule at the unit's start
  printed `builds landed 4`, dDeclaredLoop's build run at `a 0-23` and dSafePassage's at `d 20-29`.
- AC2 — `"$PY" "$STATE" --ref 9e21ac760 --claims none` exited 0. `landed` is dTrueNorth, dGroundRules,
  dSafePassage, dOrderedCharter, dFairHearing, dDeclaredLoop with landings `2511c1181`, `3c0318d95`,
  `3ada42ab1`, `9760fb746`, `0a760477e`, `9e21ac760`. dDeclaredLoop's build-kind run lists `c1f80c002`
  then `9e21ac760`. `startable` and `ready` are both dPlacedRequest, dWitnessedBar. The 27 run records
  read six build-kind runs, one per landed build, and 21 spec-kind ones. Red: over the same document's
  `counts`, `CENSUS_TERMINAL` reads 22 builds landed and candidate (a) reads four, the four the
  pre-change schedule printed.
- AC3 — the same JSON: dSafePassage counts CLOSED 98, DEFERRED 1, WONTDO 1, `landed-carrying`, carrying
  `TOOL-dSafePassage-61` `advances` `TOOL-dSafePassage-14`; dDeclaredLoop 101, 1, 1, carrying
  `TOOL-dDeclaredLoop-34` `advances` `TOOL-dDeclaredLoop-35`; dWitnessedBar DEFERRED 88, dPlacedRequest
  DEFERRED 63, dTrueNorth CLOSED 30. Every build's `deviations` length equals the `ls-tree | grep -c`
  count, 22 of 22, 2211 records in all (PINNED at 9e21ac760). Red: the pre-change schedule counted dSafePassage's and
  dDeclaredLoop's DEFERRED unit as unbuilt (AC1's red); a staged `VERB` that matches nothing read
  dSafePassage's carried unit with `verb` and `ask` null.
- AC4 — in the clone, a branch rotated dWitnessedBar's `RUN.md` to `RUN.LANDED.00000001.md` and wrote a
  `RUN.md` whose `## Run facts` read `phase: LANDING` and `base: 9e21ac760dc0a43d6ed007396922722ccee98d57`,
  merged `--no-ff`. The derivation at HEAD named seven `landed` builds, dWitnessedBar's `landing.sha`
  the merge `1a7a95a05`, and `startable` dPlacedRequest alone; the schedule printed `builds landed 7`.
  Red: the same two commands at the clone's `9e21ac760` before the merge read six landed, `startable`
  dPlacedRequest and dWitnessedBar, and `builds landed 6`.
- AC5 — the clone before the merge, `refs/gov/remote/runs/dPlacedRequest` set to a commit whose message
  reads `status: live`, `node: fx` and a `beat-utc:` of now: dPlacedRequest's `next.state` read
  `running`, it left `startable` and stayed in `ready`, and `running` named it. A `beat-utc:` of
  `2026-01-01T00:00:00Z`, older than `RESUME_STALE_BOUND` 5400, read `stale`. Red: `--claims none` over
  the same clone read it `startable`. The claim ref was deleted after.
- AC6 — `TOOL-dDeclaredLoop-34`'s status flipped to `OPEN` in the clone's working tree and left
  uncommitted: the JSON of `--ref 9e21ac760 --claims none` compared equal under `cmp` to the one taken
  before the edit. Red: a staged swap of the blob reader for a working-tree file read moved
  dDeclaredLoop's `counts` to CLOSED 101, OPEN 1, WONTDO 1.
- AC7 — `tree_state("9e21ac760", {"dDeclaredLoop": [], "dWitnessedBar": []})` on the loaded schedule
  returned exactly `{"dDeclaredLoop": (True, True), "dWitnessedBar": (True, False)}`. Red: a staged
  `tree_state` keyed by every build of the document returned 22 keys and failed the equality.

Also observed: the CLI exits 2 with `build-state: nosuchref resolves to no commit in .` on a ref that does
not resolve, and 1 with the `[chain]` message at v2's first commit `d56c897fc`, whose `[chain]` held 10
builds.

Owed to the close: the plain bar; and `chain-packet self-test` reds CP3, CP4 and CP5 under `GATE_SELFTESTS=1`
until the schedule instrument is re-pinned (section 7 F2, the one ask the main loop files).
Cleared since: spec 1 rev-3's rename to `derive_predecessors` at `8d69e97b7` cleared the `VERB_OFFENDER_PIN` item, since that name leads with the declared verb `derive`, so the lexicon owes nothing for this unit (TOOL-dTrackedAtlas-11).
