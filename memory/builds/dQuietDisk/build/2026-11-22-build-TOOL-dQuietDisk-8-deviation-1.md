# TOOL-dQuietDisk-8 deviation 1 — the aged-gov clone's own checkout pins core.autocrlf=false

**Serves:** deviation TOOL-dQuietDisk-8

- **Departs from:** `TOOL-dQuietDisk-8@rev-5` [S3]
- **Hand-off:** spec-to-code
- **Before:** S3 says that if `tools/govkit/matrix.py`'s aged-gov clone goes sparse, it also takes `--no-checkout` "and checks out its HEAD itself after the sparse set".
- **After:** the clone's own checkout runs `git -C <ga> -c core.autocrlf=false checkout -q HEAD`, and the sparse set and that checkout each run only while the step before them exited 0. `--local` stays beside the new `--shared`.
- **Cause:** builder discovery
- **Reason:** in `tools/govkit/matrix.py#main` the clone's `-c core.autocrlf=false` comes before `clone`, so it applies to the clone process alone and is not written into the clone's config. Today that clone process also makes the checkout. Once the checkout is a second process, a Windows git's system-wide `core.autocrlf=true` would check out CRLF bytes unless the pin moves with it.
- **Evidence:** the acceptance ledger's AC3 line. The matrix probe printed the same 586 lines [PINNED, measured at the pass] on `base`, `full` and `sparse`.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-8
