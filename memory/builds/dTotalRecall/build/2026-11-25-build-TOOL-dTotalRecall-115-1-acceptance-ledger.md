# TOOL-dTotalRecall-115 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-115
**Caused-by:** TOOL-dTotalRecall-115

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`3a1f4ba1d8b4dbed164c6c2dc705d6f1bb1d98be`, 2026-11-25 local, in one commit. The probe of §4 ran in a scratch
repository over the working tree's `tools/lib/gov-feed.sh`, over the block as it stood at that base, and over the
block with the key test turned into `1`. §7's legs and the `New arm:` RED-first observation of
`tools/unattended/unattended.test.sh`'s `rr_` block are owed to the close.

The floors of `tools/unattended/unattended.test.sh`: `FLOOR_ASSERTIONS` from 4223 to 4228 and `FLOOR_SHARD_8` from
1440 to 1445, by the four `same` arms and the `keyless.sh` mutant (DERIVED 2026-11-25, the diff's own lines).

**Evidences:** TOOL-dTotalRecall-115
- AC1 — `check_feed refs/gov/remote/` — exited 0 after each landing of the probe, the feed holding 2, 3, 4 and 4 lines over four distinct keys; over the block at the base the second landing printed `extra` with exit 1 and the third left five lines, and with the key test turned into `1` the third left five lines and printed `duplicate` (DERIVED 2026-11-25, that probe).
- AC2 — `duplicate refs/heads/main` — was printed once, naming the copied line's commit, with no other line and exit 1 (DERIVED 2026-11-25, that probe).
- AC3 — `check_feed` — printed `extra` alone for the off-branch commit and `missing` alone for the commit landed with no append, each with exit 1 (DERIVED 2026-11-25, that probe).
- AC4 — `awk '/^# >>> gov_feed_sh/{f=1} f{print} /^# <<< gov_feed_sh/{exit}' <file>` — gave one sha1, 99708c9590b5049976a843f5b56633e3e112a705, over the canonical file and the four carriers, and `bash -n` passed over each (DERIVED 2026-11-25).
- AC5 — `grep -c 'can list commits the feed holds' tools/lib/gov-feed.sh` — printed 0, and the `SETS` line names `duplicate` for a key a second line holds (DERIVED 2026-11-25).
- AC6 — `grep -c 'keyless.sh' tools/unattended/unattended.test.sh` — printed 5 and `bash -n` passed (DERIVED 2026-11-25); the arms' sequence, run as a probe over the same mutant scripts, gave the expected `3 0`, `0 0 0`, `1` and `1 1 1`, and `0 1 0` and `4 1` over the block at the base. The suite's own run is owed to the close.
- AC7 — `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` — read 421, 1604, 733, 12215, 819 and 17602 for the six paths of S7, each the count its row of `memory/project/shell-role.txt` holds, widened by `2026-11-25-build-TOOL-dTotalRecall-115-widen-28` (DERIVED 2026-11-25).
