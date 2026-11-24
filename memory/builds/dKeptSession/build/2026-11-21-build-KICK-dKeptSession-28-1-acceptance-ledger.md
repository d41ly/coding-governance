# KICK-dKeptSession-28 — acceptance ledger

**Serves:** journal KICK-dKeptSession-28

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `1f8ec4d8`,
each by a probe that sources `tools/unattended/unattended.sh` in a fresh bash and calls the two new
functions, `check_mail_recipient` and `check_mail_addressed`, over the tracked
`tools/playbook/fleet.toml`. A second probe, a scratch script holding the new suite block's subshell
verbatim, printed the five lines its five `same` rows compare, each equal to the row's expected text.
Before the first edit the base's cited symbols were probed: `check_fleet_tag` returned 0 for `a` and
`b` and 1 for `z` and the empty tag, naming fleet.toml; `check_slug_shape` 0 for `fx` and 1 for `3x`
and the empty slug; `UNIT_ID_ERE` anchored matched `KICK-fx-3` and `KICK-3x-3`, never `fx` or
`KICK-fx-x`; and neither new function was defined. The exits section 4 names held.

`python tools/lexicon/lexicon.py` exited 1 over the working tree on its verb-offender pin, 1432
offenders over a pin of 1421 (DERIVED, that run), the count earlier units of this build read at their
bases; `--suggest --as sh.function` graded both new names OK, leading with `check`, so the breach is
not this change's and is owed to the close.

Owed to the close: every leg the spec's section 7 names, the unattended suite whole, whose effective
`FLOOR_ASSERTIONS` rises from 4067 to 4072 and `FLOOR_SHARD_8` from 1284 to 1289 (PINNED, the block's
five unconditional `same` rows, all in region eight), and the `New arm:` line's RED-first observation
on the base driver, which has no recipient checker.

## Decisions taken in the build

- The two functions sit directly below `check_fleet_tag`, the membership check S3 asks, so the
  grammar's one external call reads beside its callee.
- `check_mail_recipient` sets `LC_ALL=C` locally, as `check_cadence_segment` does, so the `[A-Z]` of
  `UNIT_ID_ERE` is the ASCII range under any collation.
- A `build:` and a `unit:` refusal name the form's own rule; any other text, the empty one included,
  names the four forms, as S2 says.
- `check_mail_addressed` reads the slug segment of a `unit:` recipient only where the text holds a
  dash after `unit:`, so a malformed `unit:fx` never reads as build `fx`'s; it checks no form beyond
  that, as S4 says.
- The suite block re-sources the tracked driver in one subshell, and the AC3 plant redefines
  `check_fleet_tag` last inside it, so the suite's own shell keeps the definition its prologue sourced.

**Evidences:** KICK-dKeptSession-28
- AC1 — the sourced probe: `check_mail_recipient` on `build:fx`, `unit:KICK-fx-3`, `node:a` and `project` each returned 0; on `build:`, `unit:fx`, `unit:KICK-fx-x`, `unit:KICK-3x-3`, `everyone`, `Project` and the empty text each returned 2 with one `mail — refused · recipient` line on stderr.
  Eleven recipients, four legal and seven refused (DERIVED, that probe). The planted checker, its unit
  branch rewritten to accept any `unit:` text, returned 0 for `unit:fx`, `unit:KICK-fx-x` and
  `unit:KICK-3x-3` (DERIVED, that probe), the red the criterion names.
- AC2 — the sourced probe: `check_mail_recipient node:z` returned 2 with the one line `mail — refused · recipient node:z: 'z' is no tag of fleet.toml`, and `node:b` returned 0.
  (DERIVED, that probe.)
- AC3 — the sourced probe, `check_fleet_tag` redefined to append to a scratch counter, set `LEASE_WHY` to `fleet.toml could not be read: planted` and return 2: `node:a` returned 2 with `mail — refused · recipient node:a: fleet.toml could not be read: planted`, `build:fx` returned 0, and the counter held one line.
  (DERIVED, that probe.)
- AC4 — the sourced probe: `check_mail_addressed` with `build:fx` returned 0 for `build:fx` and `unit:KICK-fx-3` and 1 for `build:fy`, `unit:KICK-fy-3`, `node:a` and `project`; with `node:a` 0 for `node:a` only; with `project` 0 for `project` only.
  Eighteen pairs, three readers over six recipients (DERIVED, that probe).
