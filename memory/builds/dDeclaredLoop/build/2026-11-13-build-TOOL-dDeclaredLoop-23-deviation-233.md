# TOOL-dDeclaredLoop-23 deviation 233 — what the shell readers do around the trailer CLI that the spec does not state

**Serves:** deviation TOOL-dDeclaredLoop-23

- **Departs from:** `TOOL-dDeclaredLoop-23@rev-3` [§4 "### The consumers"]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-23`'s spec at rev-3 re-points `read_attribution_tokens` to the kit's `commit_trailers.py tokens "$@"`, `pass_commit` to that function's lines in its scratch file and `check_commit_message` to the `message` verb, and states one refusal: no launcher is a named stderr line and status 2 from `read_attribution_tokens`.
- **After:** the pass also has `read_attribution_tokens` drop the CR a Windows interpreter ends each line with, set `GIT_NO_REPLACE_OBJECTS` on the call so the reader's git keeps the replace-ref pin the library's `GIT` wrapper carried, leave the reader's stderr unsuppressed and return the reader's own status; `pass_commit` returns status 2 where that function fails; `check_commit_message` strips the CR and returns status 2 with a named line where no launcher resolves or the reader fails.
- **Cause:** builder discovery
- **Reason:** on this node `python` ends a printed line CR LF, and every consumer matches an id as a whole token of the line, so the id a `Pass:` trailer ends its line with would match nothing and every trailered pass would read as uncommitted until `TOOL-dDeclaredLoop-38` lands; the replace-ref pin would be shed until `TOOL-dDeclaredLoop-39` lands; and a reader that cannot answer, read as an empty answer, is the failure AC8 names red.
- **Evidence:** `tools/unattended/lib-unattended.sh#read_attribution_tokens`, `tools/unattended/lib-unattended.sh#pass_commit` and `tools/unattended/unattended.sh#check_commit_message` at the pass commit of `TOOL-dDeclaredLoop-23`; the acceptance ledger's AC3 line, where the working tree's raw output held no CR byte and compared identical to the parent commit's.
- **Risk:** stricter
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** `TOOL-dDeclaredLoop-38` and `TOOL-dDeclaredLoop-39` may each remove its guard from the shell side when the CLI carries it
- **Caused-by:** TOOL-dDeclaredLoop-23
