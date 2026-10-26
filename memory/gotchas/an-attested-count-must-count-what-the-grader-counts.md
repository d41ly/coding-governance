---
name: an-attested-count-must-count-what-the-grader-counts
description: an attestation that carries a count is graded against the record's own population, so an agent that counts only what it thinks of as decisions attests a number the close refuses
kind: class
universal: false
---

# The attested count is the record's count, not yours

## Symptom

`unattended.sh --close` blocks on an agent-attested Definition-of-Done item whose verdict is a
count, though the attestation was made honestly: the agent counted the entries it thinks of as
decisions, and the close counted every entry the record files in the same class.

## Where it bit

dKeptSession's spec run attested `--item parked-decisions-surfaced --value "yes, 1 surfaced"`, its
one parked question about the audit chain's bound. `--close` graded that against the run-state
file's surfaced class in `memory/builds/dKeptSession/RUN.md`, which holds every
`rescope · item defer` row the carry-forward wrote, and read 65; the close blocked, and the count was
re-attested at 65 (PLAY-dClosedLoop-36 asks for the count to be derived).

## The fix

Before attesting a count, read the population the grader counts, not your own list of what
mattered: every surfaced-class row in the run-state file, a spec run's 64 defer rows as much as its
park. Attest after the last act that adds a row of that class, which for a spec run is the
carry-forward, and say in the commit which rows the count covers.

No machine gate catches the miscount before the close: `--close` is its first reader, at the cost
of a close attempt, until PLAY-dClosedLoop-36 derives the count.
