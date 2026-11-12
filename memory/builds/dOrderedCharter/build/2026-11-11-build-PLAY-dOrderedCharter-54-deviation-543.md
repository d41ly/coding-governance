# PLAY-dOrderedCharter-54 deviation 543 — a dated transcript's age may pass the staged age by the write's own time

**Serves:** deviation PLAY-dOrderedCharter-54

- **Departs from:** `PLAY-dOrderedCharter-54@rev-3` [Acceptance criteria]
- **Hand-off:** spec-to-code
- **Before:** AC4 expects `s1 · transcript 3600s old` within a second for a transcript dated 3600 seconds back (PINNED by the spec's AC4).
- **After:** the arm accepts an age from 3600 seconds (PINNED by the spec's AC4) up to 3600 plus the seconds between dating the transcript and the write returning, and no more.
- **Cause:** builder discovery
- **Reason:** the age is read at the card write, after the checker derives every startup cell, which took two to three seconds on this host, so a one-second window reds a correct build; the elapsed window still reds a wrong age.
- **Evidence:** the AC4 probe printed `card-file — took over: session s1 · transcript 3602s old`, and a rerun `3603s old`.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-54
