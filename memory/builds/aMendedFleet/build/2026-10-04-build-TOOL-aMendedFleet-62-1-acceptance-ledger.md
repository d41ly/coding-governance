# TOOL-aMendedFleet-62 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-62

**Evidences:** TOOL-aMendedFleet-62
- AC1 — `read_advertised_head` — under `%TEMP%`/af62a1 a bare origin with HEAD on `main`, a seed clone that pushed one commit, and a second clone that sourced `tools/unattended/lib-unattended.sh` and called the reader with the driver's path: rc 0 and `ADVH_SHA` equal to `git ls-remote origin HEAD`; after the seed clone pushed a second commit, the clone fetched and then pinned `refs/remotes/origin/main` back to the old tip, and a fresh call returned the new tip; with the remote removed it returned 1 and `ADVH_WHY` read `this clone declares no remote to observe`. Staged break: a copy of the library whose reader overwrites the advertised sha with `refs/remotes/origin/HEAD` returned the stale tip on the second call, and the fixture reported FAIL there
- AC2 — `tools/unattended/check-pass-order.test.sh` — its prologue and its range block, lines 679 to 748, cut into a slice in the session scratchpad with `HERE` and `KIT` pinned to the kit dir and the fixture root under `%TEMP%`: 13 of 13 assertions passed, including exit 0 with `range <tip8>..` on the summary line and exit 1 naming `ARCH-tRange-3` and not `ARCH-tRange-1`. Staged break: with `$HR_EXCL` removed from the first `build_commit` call in a copied leg, four assertions failed, the first being the pushed unit redding the first run
- AC3 — `tools/unattended/check-brief-recorded.test.sh` — the same slice over lines 703 to 770: 11 of 11 passed, exit 0 with `range ` on the summary line, then exit 1 naming `ARCH-tBR-3` only. Staged break: with `$HR_EXCL` removed from the ranged `build_commit` call in a copied leg, four assertions failed
- AC4 — `range whole (the tip did not resolve: ` — the AC2 slice's unresolved-tip and nothing-unpushed arms passed: the origin HEAD symref on a missing branch printed that field and redded the pushed unit, and HEAD reset to the tip printed `range whole (HEAD carries nothing the tip <tip8> lacks)`. Staged break: a copied library whose unresolved branch set `HR_MODE=range` and `HR_EXCL="^HEAD"` made the unresolved arm exit 0 and never name `ARCH-tRange-1`, two FAILs
- AC5 — `git apply --cached` — a scratch index read from the unit's parent with `GIT_INDEX_FILE`, given `git diff d99cd0328^ f8afa61bc` over the six files and then `git show 83eec3021` over the two suites: all six index blobs equal the committed blobs, and the pass-order suite's blob equals node d's at `83eec3021`
- AC6 — `tools/gate-legs.json` — the unit's diff of that file adds exactly two `impure` lines, one in the `pass-order history` entry and one in the `brief-recorded` entry, and changes nothing else
- AC7 — `memory/guides/SESSION-KICKOFF.md` — the unit's diff moves the `last-audit:` line, and `last-body-change:` beside it

## The suite arms

The arms S5 adds were run only as the two slices above, never as whole suites. Both suites, and the
`pass-order history`, `brief-recorded`, lexicon and kit-epoch legs, are owed at the close.
