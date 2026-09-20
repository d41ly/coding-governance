**Serves:** journal TOOL-dDerivedDocket-4

# TOOL-dDerivedDocket-4 — acceptance ledger

Every observation below was made in the build pass, by a DIRECT check: the driver run over a scratch
fixture repository, the kit gate run over a fixture copy of the kit with a break staged into it, or
a read of the tracked files. No gate leg and no self-test suite ran in this pass. Three criteria
carry a `permission:` line deferring their observation and get no line here.

**Evidences:** TOOL-dDerivedDocket-4

- AC1 — `still held` — a HELD fixture whose `hold-until` is `after 2099-01-01T00:00:00Z` prints it,
  exits 0, and both the run-state file's blob hash and the lease file's are byte-identical after.
- AC2 — `--hold` — on a dirty fixture tree it refuses with the numbered dirty-tree message and the
  run-state file's blob hash is unchanged; the clean check runs before the phase write.
- AC3 — `checkpoint ·` — a hold whose reason carries the words `gates GREEN` prints them ONLY on the
  quoted `reason ·` line; the `checkpoint ·` line's bar field is the path of the newest
  `gate-logs` record placed in the fixture.
- AC4 — `--keepalive-unreachable` — a hold taken from BUILDING with `--keepalive-unreachable nodeX`
  records `· unreachable nodeX` and `held-from: BUILDING`, and the take-over with a new
  `--keepalive-id` returns the record to BUILDING.
- AC5 — `--landed` — on a HELD fixture it, `--close` and `--phase <working phase>` each refuse with a
  numbered message naming HELD, and the run-state file's blob hash is unchanged after all three.
- AC6 — `--resume` — a HELD record under a fresh foreign lease refuses; a working-phase record under
  a fresh lease refuses a different `--keepalive-id` and, with none, prints the `--status` block then
  refuses naming it. Record and lease byte-unchanged on all three.
- AC7 — `presumed-stopped` — `--status` prints it for a working-phase lease older than the bound, and
  `--resume --keepalive-id kC` records kC, takes the lease, and NAMES the staged index it inherited.
- AC8 — `check-unattended.sh` — over a fixture copy of the kit, check 32 reds naming `verb_status()`
  for a direct read, `verb_preflight()` for the rotation test inside a phase WRITER, `verb_resume()`
  for a `recorded_phase` call the allow-list does not name, and `ghostfn()` for a stale allow-list
  row. The shipped driver and allow-list are silent — the control.
- AC9 — `HELD` — deleting it from `PHASES_CORE` in a fixture driver copy reds the leg on the
  `CORE_FLOOR` of `13:12`, and deleting `inherited-red` from `HOLD_CODES_CORE` reds it on
  `HOLD_FLOOR`. On the built driver,
  `sed -n 's/^PHASES_CORE="\(.*\)"/\1/p' tools/unattended/unattended.sh | grep -o 'VERIFYING.*'`
  prints `VERIFYING LANDING LANDED ABORTED`, which is the list `PHASES_ALLOW` spells.
- AC10 — `--preflight` — twice with the same `--keepalive-id` exits 0 with the `keepalive` fact
  unchanged; with a different one it refuses naming `--resume`, the fact is unchanged and the lease
  file's blob hash is identical although the fixture's `WIRING_CHECK` stub ran through `run_bounded`;
  over a HELD record it refuses naming `--resume` and the lease is byte-unchanged.
- AC13 — `verb_phase` — `--phase <slug> HELD --witness <sha>` on a working-phase fixture refuses with
  a numbered message and writes nothing; and over a fixture driver copy whose `verb_phase` no longer
  guards HELD, the kit gate's check 33 reds naming HELD.
- AC14 — `--hold` — refuses on an already-HELD record, on an unpublished tip under
  `ANCHOR_SCOPE=published` with an answering remote, on a `--reaped` id that is not the live
  keepalive, and on both keepalive flags at once. Record byte-unchanged in every case.
- AC15 — `hold-unpushed` — under `ANCHOR_SCOPE=published` against an origin naming a missing path,
  `--code platform-unavailable` holds and records HEAD there while `--code host-degraded` refuses;
  `--status` prints `unpushed <sha8>` on the checkpoint line, and the take-over prints the push as
  its first line of stdout (the reading rev-7 records).
- AC16 — `--code bogus` — refuses, as does `--until 'after tomorrow'`, each writing nothing; a code
  declared in `HOLD_CODES_EXTRA` is accepted and the record reads `phase HELD · code vendor-outage`.
- AC18 — `--resume` — on a HELD fixture whose recorded BASE no longer resolves in this history, the
  take-over refuses through `trusted_base` before the lease is taken; record and lease byte-unchanged.
- AC19 — `presumed-stopped` — a leaseless BUILDING fixture whose newest build-folder commit is dated
  2000 prints it and names that the record had no lease, and `--resume --keepalive-id kC` records kC;
  inside the bound the same resume refuses naming the commit's age.
- AC20 — `--replaces` — `--resume --keepalive-id kB --replaces k1` moves both the lease and the
  `keepalive` fact to kB; `--hold --reaped k1` then refuses and `--hold --reaped kB` is accepted; and
  `--replaces kX` refuses with record and lease byte-unchanged.
- AC21 — `--keepalive-id` — a no-id resume on a met HELD condition and on a stale working-phase lease
  each print the `--status` block and then refuse, numbered, naming it; record and lease unchanged.
- AC22 — `--resume --keepalive-id` — a leaseless working record resumed with the id its `keepalive`
  fact names exits 0 and TAKES the lease; resumed with another id inside the bound it prints the
  `--status` block, refuses naming the commit's age, writes nothing and creates no lease file.
- AC23 — `git cat-file -s` — `memory/guides/UNATTENDED-PROTOCOL.md` is 60324 bytes and 675 lines at
  this unit's parent and 60313 bytes and 674 lines at the build commit, both below the
  `GUIDE_CAP_BYTES` / `GUIDE_CAP_LINES` pair the hygiene gate declares on one line;
  `tools/unattended/PROTOCOL.template.md` reads identically on all four numbers.
  `grep -c 'RESUME is the third case'` counts 1 at the parent and 0 at the build commit, and the
  reap-before-schedule ordering it carried is in `memory/guides/UNATTENDED-STOPS.md` section 9.
  `HOLD_FLOOR`, `LEASE_STALE_AFTER` and `HOLD_CODES_EXTRA` each count 1 in the protocol template's
  section 8 table, 1 in `tools/unattended/.unattended.conf.example` and 1 in gov's own
  `.unattended.conf`. The companion this unit creates is 13183 bytes and 221 lines, under both caps.
- AC24 — `hold-floor` — the discharge command resolved out of `tools/unattended/kit.toml`,
  `grep -qE '^HOLD_FLOOR="?[0-9]+' .unattended.conf`, exits 1 over the shipped example conf with its
  `HOLD_FLOOR` line removed, 0 over that conf as shipped (the QUOTED form, as `HALT_FLOOR` is
  spelled), and 0 over a bare unquoted integer, which the `directives-floor` probe it copies admits.

## Not observed here, and why

- **AC11** and **AC12** carry `permission:` lines deferring them to the build's one post-build bar:
  the first runs two gate legs over the RENDERED tree, the second is the attributed
  `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` run. The orchestrator writes
  both lines after that run.
- **AC17**'s `permission:` line defers the EXECUTION of its arm. The arm is written into
  `tools/unattended/unattended.test.sh` in this commit and its first step is staged RED by dropping
  the refresh from the matching-id row; the suite that executes it sits on no bar leg, so the
  attributed run covers it. The same sequence WAS exercised in this pass against the fixture — the
  preflight take, the matching-id refresh, `--phase`'s refresh, `--hold`'s release and `--abort`'s
  removal all observed — but that is the driver run and not the suite the criterion names.

## Caveats a reader should not have to find

- The two executed-assertion FLOORS in the suites this unit adds arms to were NOT moved. This pass
  runs no suite, so neither new count was measured, and a floor raised above what a suite executes
  reds the bar on the run that raised it. Both pins are shrink-only, so the added arms stay covered.
- `memory/map/features/unattended.md` now sits 23 bytes under its 20480-byte dossier cap. Three
  illustration sentences were trimmed to fund the HELD paragraph and the third guide key. The next
  unit touching this dossier trims before it writes, or splits it.
