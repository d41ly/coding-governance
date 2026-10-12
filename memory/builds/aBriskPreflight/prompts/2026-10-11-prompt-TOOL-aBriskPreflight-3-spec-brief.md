# Spec brief — TOOL-aBriskPreflight-3: which wiring arms preflight needs, decided by measurement

**Serves:** research TOOL-aBriskPreflight-3

Read first: the build README, the prompt record and the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`), and the specs of units 1 and 2,
which are built before this one.

## The owner's item, verbatim from the prompt

"Decide what preflight needs from the wiring check, measured rather than assumed. It may need the
whole of `check-wiring.sh --check`, or only the arms an unattended run depends on, such as the
stop-guard, gate-guard, stall-recorder and resume-tick wiring. Record each candidate you tested and
what it would stop catching."

## What orientation already established

- Preflight reads the wiring check's EXIT STATUS only (`check_wiring` in
  `tools/unattended/unattended.sh`: `run_bounded $WIRING_CHECK && return 0`); its output reaches the
  operator only on a failure, indented under refusal 4. `.unattended.conf` declares
  `WIRING_CHECK="bash tools/check-wiring.sh --check"`, and the driver refuses any dash-led token
  outside `--check|--dry-run|--verify|-n`.
- Under `--check`, two arms can never move the exit status: `check_eol` prints `note` at worst
  (its own comment says why it stopped gating), and `check_backlog_stragglers` prints `note`, `ok` or
  `skip`. At BASE the straggler inventory alone cost 71 s and hit its own `timeout 60`.
- NO arm grades the unattended kit's own hooks: the stop-guard, gate-guard and stall-recorder
  fragments beside `tools/unattended/`, and the resume tick, are read by no arm, so the third
  candidate in the prompt cannot be selected from the existing arms. Adding arms for them is NOT
  this unit: a new refusal is not a cut, and an arm that could red a working adopter is not
  "strictly beneficial". File it as an ask in this build's `BACKLOG.md` if the spec judges it
  worth having.

## Candidates the spec must measure and record

1. The whole `--check`, after units 1 and 2.
2. The arms whose verdict can move the exit status under `--check` — every arm but `eol` and the
   straggler inventory. Stops catching: nothing preflight reads on success; on a failure the
   indented output loses those two arms' `note` lines.
3. Only the git-hooks arm (`core.hooksPath`, which the unattended kit's commit-msg and pre-push
   depend on). Stops catching: every settings-hook, merge-driver, ssh, routed and skill arm.

The decision is a FACT-QUESTION in M3's sense only if the spec names the probe, the observation that
decides, and a liveness assertion that the probe can come out the other way; otherwise it is a fork
resolved by M3's rule. A candidate that stops catching a verdict preflight reads today fails the
prompt's "weaken no check" and is vetoed.

## Shape of a narrowing, if one wins

- A declared, read-only selector on `check-wiring.sh` (a flag, never an environment knob: this repo
  deleted an env knob that "survived two releases by appearing to work"), announced by a `skip` line
  per arm it leaves out, naming the reason — a skip must announce itself.
- The driver's read-only allow-list gains the flag, and `.unattended.conf`'s `WIRING_CHECK` value
  names it. That changes a VALUE, never adds a key; the protocol's key table is a governance carrier
  this build may not edit.
- A SessionStart run and a bare `--check` print exactly what they print today.

## Acceptance shape

- The measurement record (a `build/` record) carries each candidate's wall and spawn count from the
  build's `trace-spawns` instrument on one host state, and what each stops catching.
- If a selector lands: a skipped arm prints its `skip` line under the selector and its ordinary line
  without it, observed through a sliced arm of `check-wiring.test.sh`; the driver refuses a flag still
  outside its allow-list (observed RED by staging one).
- If the whole check wins, the unit closes on the record alone and says so.
- Witnesses in §6 by basename.

## Conventions

- Tier-2 if a selector lands (the driver's allow-list and a conf value are a shared contract).
- Lexicon verbs; `gen_map.py --write`; kit versions bumped once at the end.
- Order: 3, after units 1 and 2.
