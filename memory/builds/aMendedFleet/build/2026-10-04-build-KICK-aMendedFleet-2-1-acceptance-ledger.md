# KICK-aMendedFleet-2 — acceptance ledger

**Serves:** journal KICK-aMendedFleet-2

**Evidences:** KICK-aMendedFleet-2
- AC1 — `overlaps — unattended: overlap probe` — under `%TEMP%`/km77, with a bare clone of the unit's tip, a second clone pushing a branch editing `tools/runlog/runlog.py` and a third clone editing it too, the card printed the cell and the pushed branch's row with that path tagged `diff`, both above `live —`; with the `derive_overlaps_line` call removed no cell printed
- AC2 — `bash tools/unattended/unattended.sh --overlaps` — a `SPECCED` fixture spec declaring the path was announced, and flipped to `WONTDO` the summary read no shared path; with the empty-slug branch removed the declared path read no shared path
- AC3 — `overlap probe UNAVAILABLE` — an unset origin HEAD printed that one line at exit 0, and with the remote URL naming an absent path the verb still answered from the local refs; with `observe_anchor` called from `print_overlaps` the verb refused on the remote
- AC4 — `overlaps — skipped: no .unattended.conf in this tree` — printed with the conf deleted from the working tree, and `grep -n "tools/unattended" skills/session-kickoff/manifest-check.sh` printed nothing
- AC5 — `overlaps — skipped: --overlaps did not answer within 1s` — a sleeping stub under `CARD_OVERLAP_BOUND=1` was skipped at exit 0; the write took 5.1 s wall against the criterion's "about four", the card's own base being 2.7 s on node a, and the bound itself fired at 1.15 s
- AC6 — `grep -n -- "--overlaps" tools/unattended/README.md` — hit the new text, and `grep -n "overlaps —" memory/map/features/session-kickoff.md` hit the dossier's

## Where the observations come from

Each line restates an observation the unit's build commit `481eb9f39` records in its message, made
when the unit was built as Tier-1; its follow-up `b2762c788` dropped `.unattended.conf` from the
card suite's clone fixture and was checked by a stub-driver fixture under `%TEMP%`/km77s.
TOOL-aMendedFleet-112 re-graded the unit Tier-2, which owes this ledger, and wrote it from that
record; no observation was re-made in that pass. AC5's wall clock is the one figure the record
states outside the criterion's wording, and it is carried here as recorded.
