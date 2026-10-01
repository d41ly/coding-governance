# TOOL-dAlignedCarrier-1 — acceptance ledger

**Serves:** journal TOOL-dAlignedCarrier-1

The driver's auto-file header now names `--close` under in-place landing, the records commit under
`primary` and the Skill's Close sequence on a hold as what commits the staged rows, and the kit gate
gains check 47, a case-insensitive, wrap-joined class scan of every tracked file under the kit
directory for the retired premise. The kit gate ran directly, scoped `--skip 28`, on a staged
four-file break and on the restored tree, standing in for the `unattended kit gate` leg; the kit's
own suite, where the new arm lives, was not run, by the build README's waiver.

**Evidences:** TOOL-dAlignedCarrier-1
- AC1 — `grep -n -i -E 'no (driver )?verb (here )?commits' tools/unattended/unattended.sh` —
  printed nothing and exited 1 after the pass; at BASE the same scan named line 6750. The `-B6`
  read of `^read_leg_argv()` shows lines 6750 to 6753 naming `--close`, `LANDER_MODE=in-place` and
  `write_close_commit` as what commits the rows.
- AC2 — `UNATTENDED check 47 FAILED` — with the four instances staged (lowercase in the lib,
  uppercase wrapped across two lines of the kit README, the second alternative wrapped across two
  `#` lines of `kit.toml`, mixed case appended to the checker in bytes), the kit gate run as
  `bash tools/unattended/check-unattended.sh --skip 28` exited 1 after 560 s with that line the
  only `FAILED` line of the run, naming `README.md`, `check-unattended.sh`, `kit.toml` and
  `lib-unattended.sh` and not the brief-record suite. Restored from byte-identical scratchpad
  backups, the same run exited 0 after 521 s with no `FAILED` line and `check 47 graded 49`.
- AC3 — `grep -c 'NOT check'` — over the `awk '/^# ---- check 47 /,/^[^#]/'` range it printed 1,
  and the range's last paragraph names the three limits: spellings outside the two alternatives,
  files outside the kit directory, and string literals counted like prose.
- AC4 — `python tools/memory-tree/check-arms.py --report` — printed check 47 branch 1 at line 5512
  as ARMED by `check-unattended.test.sh`, and the case-insensitive two-alternative `grep -c` over
  that suite printed 0. The arm's RUN was not observed: the suite is waived for this landing.
- AC5 — `check 47 skipped under --only 28` — the kit gate run with the report channel on as
  `bash tools/unattended/check-unattended.sh --only 28` printed that line, derived from the new
  header, and exited 0 after 7 s.
- AC6 — `git diff --numstat -- tools/unattended/check-unattended.sh` — printed `62 0`, no deleted
  line, and the CR count read 4 before the insertion, after it, and after the AC2 restore; the
  insertion was a Python `rb`/`wb` splice that refused to write had the count moved.
