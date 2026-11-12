# PLAY-dOrderedCharter-8 deviation 83 — the card file's writer prints only when it skips

**Serves:** deviation PLAY-dOrderedCharter-8

- **Departs from:** `PLAY-dOrderedCharter-8@rev-3` [Production-readiness checklist]
- **Hand-off:** spec-to-code
- **Before:** the observability row reads that the `card-file —` line names where the file was written or why not.
- **After:** `write_card_file` is silent when the file is written and prints one `card-file — skipped: <why>` line when it is not; the design's own text, that a failure prints that one line, is unchanged.
- **Cause:** builder discovery
- **Reason:** the startup writer's stdout is the stored card byte for byte, an existing criterion of the card engine's suite that a line on every write would break, and that output is injected into every session's context; the path is fixed, so a written line would carry nothing a reader lacks.
- **Evidence:** in a scratch clone, `--card --write` with a SessionStart payload printed bytes `cmp` found equal to the stored card, while the card file landed in the payload's worktree; with the file's path made a directory, each verb printed one `card-file — skipped:` line naming the path.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-8
