# TOOL-dDeclaredLoop-8 deviation 83 — what the claim keys' build settles beside its spec

**Serves:** deviation TOOL-dDeclaredLoop-8

- **Departs from:** `TOOL-dDeclaredLoop-8@rev-4` [S6, §4 "### The replay's carry"]
- **Hand-off:** spec-to-code
- **Before:** the carry takes the fresh render whole but for the remote cells, the remote key and `at`, so the written card's header is the fresh one, `by manifest-check.sh --card --replay`; the spec names no remote key for a stored card with no `keys —` cell, no spelling of the `now —` line beyond its toplevel and verdict words, and no `now —` tail for a replay that finds no card.
- **After:** `skills/session-kickoff/manifest-check.sh#print_rekeyed_card` carries the stored header line too, beside the remote cells, the remote key, `at` and the TAIL; a stored card with no `keys —` view key carries `remote k1:? · at ?`; the `now —` line is `now — HEAD <sha> · <branch> · <dirty> · <toplevel> · <keys>`, its keys tail `keys view fresh · remote evidence`, `keys view re-derived · remote evidence`, `keys view moved · not re-derived: over the cap · remote evidence` or `keys skipped: <why>`; a replay that finds no card writes one as before and reads its keys tail off the cell it just wrote.
- **Cause:** builder discovery
- **Reason:** the scratch guard reads a card whose first line names `--card --replay` as a session that started before the writer was wired and admits its commits with a witness (`tools/hooks/scratch-guard.js#checkOriented`), so a re-derived card carrying the fresh header would turn every later commit's tree check into a witness; S6 re-renders the startup CELLS, and the header is not a cell, so carrying it keeps the guard's deny where it was.
- **Surface:** the replay's written header, the `now —` line's spelling
- **Evidence:** the acceptance ledger `2026-11-15-build-TOOL-dDeclaredLoop-8-1-acceptance-ledger.md`, its AC7 line.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-build-TOOL-dDeclaredLoop-8-1-acceptance-ledger
