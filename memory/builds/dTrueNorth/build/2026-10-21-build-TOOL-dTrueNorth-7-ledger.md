# TOOL-dTrueNorth-7 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-7

No merge bar, no self-test suite and no gate leg ran in this pass. Every criterion below was observed
by a targeted probe of the unit's own code: the driver run from this worktree's kit over a scratch
fixture repository under `%TEMP%/tn7` (FX-spec, FX-added, FX-landed, FX-whole) or a clone of this
repository at `ab02d3576` under `%TEMP%/tn7c` (FX-clone, with a bare origin of its own, `GATE_CMD`
`true`, `LANDER` `echo land`, no reaper and no run claims), each fixture built the way the driver
suite builds `tCarry`, with its ask stub as `ASKS_CMD`. The `before` reading is the same fixture under
the kit at base, extracted by `git archive 271aa59d tools/unattended`; each staged break is a copy of
this kit with one replacement, asserted to match exactly once. The `BASELINE_PROBE` is the spec's
section 4 probe: `lib-unattended.sh` sourced, `region` defined as `check-unattended.sh:211-216`, and
`baseline_units <RUN.md> <README> "" <base>`. These probes stand in for the `unattended kit gate`
leg's `check-unattended.sh` verdict on check 24 and for the two suites' new arms, which the close
runs; README rule 8 waives the suites' verdict at this landing.

The two `New arm:` lines' fixtures are in `unattended.test.sh` (the TOOL-dTrueNorth-7 block, shard 8,
and the moved TOOL-dUnstuckLanding-18 AC4 block) and `check-unattended.test.sh` (`seed_spc` and the
three check 24 cases after the empty-baseline arm, whose expected reason now names both regions).
Neither suite ran here; their RED-first observation and green belong to the close, under a
`Pass: none` commit. The moved arm's shape was probed instead: with the authored roster narrowed to
unit 1 the close is unmet with the `:5183` text and "this run is not a spec run"; left naming unit 2
unspecced, the same fixture carries unit 2 as a spec run's added unit, which is why it moved.

**Evidences:** TOOL-dTrueNorth-7
- AC1 — `--close tSpec` over FX-added, add reason "promoted by the closing diff review": printed `carried forward — ARCH-tSpec-3, added by this spec run and carried once, DEFERRED against the open ask EXMP-tSpec-9` and plain lines for ARCH-tSpec-1 and ARCH-tSpec-2, no `blocks: build-complete`. Base kit: unmet, "that roster cannot be read, so ARCH-tSpec-1 cannot be: the baseline roster names no unit". S4's spec-run branch staged out: unmet naming ARCH-tSpec-3 with the `:5183` text, the two roster units passing first.
- AC2 — the same close with the add reason "an adopted discovery": the same added line for ARCH-tSpec-3, met. Base kit and the same staged break: the AC1 refusals.
- AC3 — FX-landed (`RUN.LANDED.8a9fb2bf.md` rotated by the build run's preflight), units 1 and 2 CLOSED, ARCH-tSpec-3 re-deferred: unmet, "a DEFERRED unit was added and carried forward by an earlier landed run of this build, and a unit a spec run adds is carried once, so this run must build it: ARCH-tSpec-3 in memory/builds/tSpec/RUN.LANDED.8a9fb2bf.md". Base kit and `scan_landed_carry` staged to print nothing: `carried forward — ARCH-tSpec-3`.
- AC4 — the build run of FX-landed closes units 1 to 3, adds and defers ARCH-tSpec-4: unmet with the `:5183` text naming ARCH-tSpec-4, then "; this run is not a spec run, so it carries no unit it added: every unit the authored roster:units pair names at the pinned base 9c6318e5… is specced there". S3's roster half staged out: carried with the added line. Base kit: refused with the `:5183` text alone.
- AC5 — FX-clone: eleven DEFERRED specs advancing TOOL-dGroundRules-12, a defer row each, `--close dGroundRules`: eleven `carried forward — TOOL-dGroundRules-<n>, DEFERRED against the open ask TOOL-dGroundRules-12` lines and no `blocks: build-complete` (closing-review-recorded, reuse-probed, asks-disposed and two attestations stay unmet, none of them this unit's). `BASELINE_PROBE` over the record: exit 0, the same eleven ids. Base kit: term 2 "that roster cannot be read … the baseline roster names no unit"; S2's fallback removed: the same, and the probe exits 1 with "the baseline roster names no unit in its generated region". Check 24's own verdict over it is owed to the close.
- AC6 — the build run of FX-landed closes no unit (ARCH-tSpec-3 WONTDO, 1 and 2 re-deferred), adds and defers ARCH-tSpec-4: the AC4 message. S3's roster half staged to read "this run closed no unit": ARCH-tSpec-4 carried. Base kit: refused.
- AC7 — the build run of FX-landed closes no unit and re-defers all three: unmet with the once refusal naming ARCH-tSpec-3 in `RUN.LANDED.862e6f39.md`, no refusal naming a roster unit. Base kit: all three carried. The scan staged to match a defer row alone: the refusal names ARCH-tSpec-1.
- AC8 — FX-whole: the run files EXMP-tSpec-9 itself, adds and defers ARCH-tSpec-3: unmet, the `:5183` text, "this run is not a spec run", and "the build's BACKLOG.md at the pinned base 2a4738fa… files no ask under tSpec, and an ask this run filed after it does not count". The ask half staged to read HEAD's BACKLOG.md: all three carried. Base kit: "cannot be read".
- AC9 — FX-added's record ABORTED and rotated to `RUN.ABORTED.1c5e2f75.md`; the second run re-adds ARCH-tSpec-3 ("LATE record") and defers all three: met, the added line for ARCH-tSpec-3 and plain lines for 1 and 2. The scan staged over every rotated `RUN.*.md`: refused naming `RUN.ABORTED.1c5e2f75.md`. Base kit: "cannot be read".
- AC10 — FX-clone adds missing:TOOL-dGroundRules-13 beside the eleven (an id with no record anywhere but the scratch clone): `--close` printed the added line for it, `carried forward — <that id>, added by this spec run and carried once, DEFERRED against the open ask TOOL-dGroundRules-12`, and plain lines for the eleven; S4 staged to print the roster line: the added line absent. The spec run set LANDED and merged, the build run rotated `RUN.LANDED.110986df.md`, closed 1 to 11 and re-deferred the added unit: unmet, the once refusal naming it and that archive. The scan staged to print nothing, and the base kit: its plain `carried forward` line.
- AC11 — FX-spec with ARCH-tSpec-3 specced and no add row: `BASELINE_PROBE` exit 0, printing ARCH-tSpec-1 and ARCH-tSpec-2 and not ARCH-tSpec-3. Base kit: exit 1, "the baseline roster names no unit, so every unit this build has would read as added". Check 24's fail 24 line is owed to the close through the checker suite's new arm.
- AC12 — FX-spec with ARCH-tSpec-3's spec in the region: `--rescope tSpec --act add --item ARCH-tSpec-3` printed `LATE record — ARCH-tSpec-3 entered the roster after this run went live and is only being recorded now`, one add row written. Base kit and S2's fallback removed: fail 48 "… cannot be derived …", no row.
- AC13 — the authored pair enclosing no row: `BASELINE_PROBE` exit 1, "the baseline roster names no unit in its generated region, and the authored roster:units pair at the same commit names no unit of this build"; the pair absent: exit 1, "… at the same commit is absent". S1 staged to read an empty pair as an empty success: exit 0 with no id. Base kit: exit 1 naming neither state. The skip line is the checker's, owed to the close.
- AC14 — FX-spec with ARCH-tSpec-1 alone: met, one `carried forward — ARCH-tSpec-1, DEFERRED against the open ask EXMP-tSpec-9`. Base kit, and S2's fallback removed: term 2 "cannot be read" naming ARCH-tSpec-1.
- AC15 — `sed -n '/^## 15\./,$p' memory/guides/UNATTENDED-STOPS.md` prints term 2 naming the **spec run**, the authored `roster:units` pair and `RUN.LANDED.<blob8>.md`; `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` exits 0 after `bash tools/unattended/adopt-unattended.sh`.
- AC16 — `grep -n 'spec run' tools/unattended/VERBS.template.md` prints lines 794-795, the review-exit paragraph ("never DEFERRED to be carried forward, except once by a spec run"), and 900-903, close rule 9; `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` exits 0.
- AC17 — `grep -c '^read_roster_at()'` prints 1 over `lib-unattended.sh` and 0 over `unattended.sh` and `check-unattended.sh`; the non-comment `baseline_units ` counts are 2 in the driver and 1 in the checker, as at base; `grep -n 'spec run' tools/unattended/unattended.sh` prints lines inside the comment above `check_carry_forward`.
