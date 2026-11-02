# TOOL-dFoldedAudit-14 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-14

The acceptance criteria were observed by this unit's builder over the tree of this commit, on fixture T of section 6, by scratch probes of the library, the driver and the leg as CLIs. No gate, suite or bar ran. Each new arm's RED-first observation is the close's, and it is not recorded here.

Fixture T carried two keys section 6 does not name. `HALT_FLOOR` and `HOLD_FLOOR` join its conf because check 2 refuses a conf without them, ahead of any record, and read as `check 2 FAILED` lines that have nothing to do with this unit. The suite's arms declare them the same way.

**Evidences:** TOOL-dFoldedAudit-14

- AC1 — `read_first_commit_date "$B" tenancy` — over H it printed 2026-11-20; with no second argument 2026-10-20; `$A` under `tenancy` printed 2026-10-20.
- AC2 — `tenancy` — with H's last two commits dated 2026-11-20, `$B` printed 2026-11-20 and `$A` printed 2026-10-20, so the first archive took no floor from the second.
- AC3 — `UNATTENDED check 2 FAILED` — `$G` over H printed no such line.
- AC4 — `spec subject(s) S1 record a terminal row with no highs and minors counts or with disposition fold` — `$G` printed this, naming `$A`, with the fold row committed 2026-10-21 in the first run's record.
- AC5 — `check_landed_facts_due "$B" 2026-11-02` — it returned 1, and 0 with a third argument `tenancy`. The grep printed 1 for the driver and 1 for the leg.
- AC6 — `--subject S2` — over a staged rotation the S1 call exited 0 and `$G` printed no check 2 line; after the 2026-11-05 commit the S2 call exited 0 and `$G` still printed none.
- AC7 — `an archive added on or after SPEC_FOLD_CUTOFF that no rotation wrote` — `$G` printed this naming the stub in all three cases: the `deadbeef` name, the true blob over a running record, and the true blob beside a `HELD` record its commit left alone.
- AC8 — `SPEC_FOLD_CUTOFF` — H with `$B` edited 2026-11-26 printed no check 2 line. The stub dated 2026-10-30, and the stub under a blank key, each printed no check 2 or check 37 line naming it.
- AC9 — `grep -cE '^(check_honest_rotation|check_retired_blob|read_blob_fact|is_terminal)\(\) *\{' tools/unattended/lib-unattended.sh tools/unattended/unattended.sh` — it printed 4 and 0.
- AC10 — `grep -c 'never toward a frozen red' tools/unattended/lib-unattended.sh` — it printed 0, and `grep -c tenancy` over the leg printed 10.
- AC11 — `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh` — it printed 318 and 264.
- AC12 — `git ls-files 'memory/builds/*/RUN.*.md'` — S5's two tests with no date test passed all 10 of 10 listed paths.

Beyond the criteria. The three hoisted functions' bodies and the `is_terminal` line were compared by bytes between the driver at the base and the library: each is identical. The leg's four bare CR bytes held across the edit.

Owed at the close: the bar, and the four `New arm:` lines of section 7, each RED on its staged break and GREEN once restored. `FLOOR_ASSERTIONS` moved 1057 to 1074 and 2978 to 2983, `FLOOR_SHARD_2` 83 to 100 and the driver suite's `FLOOR_SHARD_1` 461 to 466, all counted off the blocks' own lines.
