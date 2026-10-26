# dPlacedRequest — asks

## Asks

- TOOL-dPlacedRequest-22 · filed 2026-10-21 · build every roster unit of this build from its spec, filed by the opening so the spec run closes by carry-forward with each unit's spec header advancing this ask (README rule 1) · accept every unit of the README's `roster:units` pair is built from its spec and CLOSED, the last one's header carrying `closes` for this ask
- TOOL-dPlacedRequest-65 · filed 2026-10-26 · THE RESUME OVERRIDE READS THE IMPORT LINE, NOT THE FIXTURE. TOOL-dPlacedRequest-2 S7 reads `always-resume` as `fresh-when-idle` while `CLAUDE.md` carries no card import line, a stand-in for the card-import fixture's verdict that cl-dClosedLoop-0150 names, and a later edit to `CLAUDE.md` breaks the equivalence silently (KICK-dKeptSession-12 §8 F3) · accept TOOL-dPlacedRequest-2 S7 and its AC7 name the card-import fixture's recorded verdict, read by `read_card_fixture_verdict`, as the switch that reads `always-resume` as `fresh-when-idle`, the import line no longer consulted
- TOOL-dPlacedRequest-66 · filed 2026-10-26 · THE FEED CENSUS SEES ONLY LEASE-SHAPED PUSHES. TOOL-dPlacedRequest-13 S9's `scan_feed_writers` inspects `--force-with-lease` lines alone, so a plain push of a `refs/gov/` ref skips the census KICK-dKeptSession-23 relies on (KICK-dKeptSession-23 §8 F1) · accept `scan_feed_writers` also flags a line pushing a `refs/gov/` ref without `--force-with-lease`, seen red on a planted plain push of `refs/gov/mail/fx/a/s1`
- TOOL-dPlacedRequest-67 · filed 2026-10-26 · A DECLARED WAIT DOES NOT RENEW ITS LEASE. Under `leases.renewal: progress` TOOL-dPlacedRequest-1 S8 renews only on a transition witness, so a build waiting on an open `question` inside `flow.wait-ceiling` writes no transition and its lease lapses at `leases.expiry-hours`, the red case cl-dClosedLoop-0504 states (KICK-dKeptSession-25 §8 F4) · accept under `leases.renewal: progress` a renew whose `--witness` is the commit of a mail message of kind `question` addressed to the lease's build, `open` on this node and inside its declared deadline by `check_mail_deadline`, writes `renews: yes` even when it equals the record's `witness`, seen on a lease kept live past a 24-hour `leases.expiry-hours` by a 30-hour wait, and red on that witness once the question reads `expired`

## Dispositions

- SEV · TOOL-dPlacedRequest-22 · MED · the build's units stay unbuilt and its owned gaps open
- DEFERRED · TOOL-dPlacedRequest-22 · until TOOL-dPlacedRequest-64 · the spec run carries every unit forward DEFERRED against this ask, each spec header advancing it; the build run builds them, and its last unit in build order, TOOL-dPlacedRequest-64 at order 36 today, closes it (README rule 1)
- SEV · TOOL-dPlacedRequest-65 · MED · a session resumes an idle build whose card import was never proven
- SEV · TOOL-dPlacedRequest-66 · LOW · a mail write by a plain push escapes the feed and the census both
- SEV · TOOL-dPlacedRequest-67 · HIGH · KICK-dKeptSession-25's AC4 stays red: a waiting unattended build loses its lease
