# TOOL-aClassedKnob-2 — push-main arm 2d holds its lock until the lander has reached it

**Status:** SPECCED · rev-1 · 2026-10-07 · node a · Tier-1 · base c83ef509 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `tools/push-main.test.sh` arm 2d load-independent. It plants a claim-push lock due in three
seconds and expects the lander to wait; a loaded host reaches the lock after it has expired, and the
lander correctly passes it.

## 2. Scope (IN)

- S1. Arm 2d plants the lock with a deadline well beyond any load, and a background releaser removes
  it a fixed interval after the lander's marker appears. The lander touches that marker immediately
  before it waits, so the lock is always still held when the lander first looks. Observed by AC1.
- S2. The verdict reads the lander's own announcements: it waited, it did not pass the lock as
  expired, and it landed. Observed by AC1 and AC2.
- S3. Arm 2e re-creates the lock directory the releaser removed. Observed by AC3.

## 3. Non-goals (OUT)

No change to `tools/push-main.sh` or `CLAIM_WAIT_CEILING`.

### Edges

none

## 4. Design

`push-main.sh` touches `$marker` and then calls `check_claim_push_clear` on both paths. The marker
is the only observable the test has that the lander has reached the lock, so the releaser keys on it.
It polls for the marker under its own bound, sleeps three seconds, and removes the lock. The deadline
is 100 seconds out, under the 120-second ceiling, so a releaser that never fires still ends the wait
and reds the arm by name.

### Files touched (estimate)

- `tools/push-main.test.sh`

## 5. Production-readiness checklist

- risks — a releaser left running would remove a later arm's lock; the arm waits for it.
- testing — AC1 to AC3.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the push-main suite runs while a second copy runs beside it, its arm `2d` passes in
  both. Red when: the verdict depends on the lander reaching the lock inside a fixed wall-clock window.
- **AC2** — When the wait in `check_claim_push_clear` is cut, arm 2d reds. Red when: the arm passes
  on a lander that never waited.
- **AC3** — When arm `2e` runs after `2d`, it still observes the expired-lock announcement.
  Red when: 2e writes into a directory 2d's releaser removed.

## 7. Gates

`push-main self-test`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-07 · initial draft.
