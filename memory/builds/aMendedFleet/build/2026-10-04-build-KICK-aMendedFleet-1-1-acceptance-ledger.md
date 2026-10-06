# KICK-aMendedFleet-1 — acceptance ledger

**Serves:** journal KICK-aMendedFleet-1

**Evidences:** KICK-aMendedFleet-1
- AC1 — `drift — last bar` — on a `git clone --local` under `%TEMP%`/km76 with a hand-written two-group history in its common git dir, the card line named the second group, `3 signals · 1 nonzero · 1 dead`, `sigDead DEAD` and `sigLive=2/76`, and sat between the `worktrees —` and `live —` lines
- AC2 — `drift — skipped: no drift-history.tsv in the git common dir` — printed at exit 0 with the history renamed away; with the header's `signal` column renamed the line read `drift — UNKNOWN` naming `signal`; with a truncated line appended to the restored file the line still reported the second group's `3 signals`
- AC3 — `grep -n "drift_report" skills/session-kickoff/manifest-check.sh` — printed nothing
- AC4 — `bash skills/session-kickoff/manifest-check.sh --card --replay --session t76a` — after a third group was appended, the replay printed AC1's `drift —` line byte-identically
- AC5 — `grep -n "drift —" memory/map/features/session-kickoff.md` — hit the dossier's new sentence

## Where the observations come from

Each line restates an observation the unit's build commit `6f2c55785` records in its message, made
when the unit was built as Tier-1. TOOL-aMendedFleet-112 re-graded the unit Tier-2, which owes this
ledger, and wrote it from that record; no observation was re-made in that pass. The commit also
records the new arms, run alone as a slice, at 9 of 9 and 6 red with the `derive_drift_line` call
deleted.
