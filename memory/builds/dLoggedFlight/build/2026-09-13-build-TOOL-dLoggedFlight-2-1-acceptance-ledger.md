# Acceptance ledger — TOOL-dLoggedFlight-2

**Serves:** journal TOOL-dLoggedFlight-2

Tier-2 · node d · 2026-09-13 · the build pass of the driver's run-log writer, against spec rev-5.
Every line is OBSERVED. `<suite>` is `tools/unattended/runlog-writer.test.sh`, run directly and never
through the kit's gate runner; its final run printed `PASS (154 assertions)` against a floor of 154.
No suite that existed under `tools/unattended/` before this build was run.

## The criteria

**Evidences:** TOOL-dLoggedFlight-2

- AC1 — `bash tools/unattended/runlog-writer.test.sh` (`check_ac1_calls`) — `--park` ended `rc=0
  exit=clean checks=` with `phase_to=BUILDING`; a refused `--park` ended `rc=1 checks=14`; `--phase`
  ended `phase_to=VERIFYING` read back from the file, and a refused one `checks=19` with the file's
  phase, not the one asked for. A refusing `--close` listed every check it printed, in print order.
  Over the whole journal `build_invocations` found no bad line, no orphan END and no verb mismatch.
  RED seen four ways: `fail()` not recording (4 arms), `phase_to` from `rc` (6), a nonce that does not
  pair (10), and END's verb read from the parsed `VERB` (9).
- AC2 — `<suite>` (`check_ac2_exits`) — `exit "$status"`, the inline `--phase` exit and a usage error
  each ended `exit=clean` with `rc` equal to the process status; a conf `trap 'exit 0' EXIT` and a
  conf function named `trap` changed neither. The enumeration over the driver and its library found
  the five exemptions once each above the install and every other exit marked. On the base driver it
  finds exactly the fifteen sites the spec names. Every run stages its own failing cases into copies:
  an unmarked exit in a verb body, one in the library, and a second copy of an exempt text all red,
  and a marked control passes. RED seen five ways: the install moved after the argument loop (35 arms),
  a conf trap taking effect after the install (5), a plain `trap` (7), and the marker removed from
  `--version`'s exit (2) and from `exit "$status"` (3).
- AC3 — `<suite>` (`check_ac3_signals`) — TERM sent once the stub's ready file named a live pid:
  the driver exited while the stub still ran, and END read `exit=unclean`. KILL left a START alone,
  and the only open invocation in the journal was that `--close`. RED seen with `trap 'exit 143' TERM`
  added (the driver outlived the signal until the stub ended) and with the marker set at install.
- AC4 — `<suite>` (`check_ac4_outside_edit`) — no stamp and no `oob` on a first call, none on an
  untouched second, `oob=1` after a plain append, and none on the call after that. RED seen with the
  END stamp removed and with the stamp's existence test removed.
- AC5 — `<suite>` (`check_ac5_session`) — a UUID reached the line, a value with `/` and a 129-byte
  value were written empty with `sess_bad=1`, an unset name wrote nothing, a bad name was flagged
  beside a good one, and ten names gave eight read and `sess_more=2`. RED seen with the raw value
  written.
- AC6 — `<suite>` (`check_ac6_unjournaled`) — `--version`, `--plan <slug>` and two calls under
  `GOV_RUNLOG=0` wrote no line; a conf assigning `GOV_RUNLOG=0` did not turn the log off. RED seen with
  `--version` journaled and with the switch removed.
- AC7 — `bash -x` on `--status dLoggedFlight` in this worktree — with the trace on its own
  descriptor, the pre-unit driver and this unit's both counted 17 external execs over the same RUN.md
  and an existing journal directory, twice each. The suite's arm counted 13 in its sandbox with the
  writer off and on, and exactly one more, a `mkdir`, on a clone's first call. RED seen with a `date`,
  a `git` and an unconditional `mkdir` added.
- AC8 — `<suite>` (`check_ac8_write_failure`) — with the journal directory replaced by a file, `rc`
  and stdout matched the `GOV_RUNLOG=0` call and stderr gained one `unattended: run log` line and
  nothing else. RED seen with the warning sent to stdout.
- AC9 — `bash tools/run-gates/run-selftests.sh --kit tools/unattended/runlog-writer.test.sh` —
  `ok` in 51 s against its 110 s row; `--check` clean at 64 rows; `govkit plan` into a scratch target
  listed the suite as `ORDER [project-owned]`. RED seen with the budget row renamed, with a manifest
  leg added, with the suite dropped from the project-owned list, and with the floor raised to 155.
- AC10 — `bash tools/unattended/adopt-unattended.sh --check` — in sync, and `check-kit-versions.sh`
  exited 0 at 1.20 across 15 carriers; the `unattended kit gate` leg exited 0 with the new key in both
  directions of check 22. The suite's anchored greps found the section 2 paragraph, the section 8 row,
  the example line and the verbs sentence. RED seen with each of the four removed.
- AC11 — `<suite>` (`check_ac11_worktree`) — a linked worktree's line landed in
  `<common-dir>/runlog/driver.log` naming that worktree, beside the primary tree's own lines; nothing
  appeared under its git dir in `.git/worktrees/`, and its out-of-band stamp did. RED seen with the
  journal root taken from the worktree's git dir.
- AC12 — `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh` — selected
  all three new classes. RED seen with one record's anchors removed (check 19, not selected) and with
  another's index row removed (check 17).
- AC13 — `<suite>` (`check_ac13_units`) — `--brief`, `--dispatch`, `--rescope` and `--review` carried
  their unit, `--phase` its slug, a free-text `--park` item reached no line and judged no unit, and a
  malformed unit set `unit_bad=1`. RED seen with `PK_ITEM` read for `--park` and with an unset
  variable in the trap.

## Staged RED

33 breaks, each applied to a MIRROR of the kits in a scratch dir, never to the working tree, and
each run through the mirror's own copy of the suite. All 33 went RED, each on a named arm, and an
unmodified mirror stayed green before and after. AC12's two were made on the working tree's records
and restored from a copy, never with a checkout.

The spec's data model adds one observation no criterion numbers: a line over 2048 bytes is cut as
`render_line` cuts it, compared byte for byte on an ASCII phase and on three-byte characters whose
cut lands inside one. RED seen with the cut removed and with the character repair removed; the second
leaves bytes the reference cannot decode, so its arms fail on an empty comparison.

## Residue

- The spec's section 4 file list was an estimate. The pass also touched the carried-prefix row of the
  budget file, raised 14 to 15 by hand with its reason; the runlog README and dossier sentence that
  said no producer reached the value cut; and the kickoff manifest stamp, since the conf is watched.
- The three gotcha classes are claimed by the runlog dossier: the unattended dossier sits 10 bytes
  under its cap.
