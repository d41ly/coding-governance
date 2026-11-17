# TOOL-aPiecewiseGrade-6 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-6

No merge bar, no self-test suite and no gate ran in this pass. The probe criteria were observed by
the spec's pass probe, `pg6.sh` in the run's scratch, removed after the pass, run over the built
driver with the fixture repository at `%TEMP%/pg6`. The same probe over the base driver from
`55f371908`, held under `%TEMP%/pg6b`, printed `overlap second-busy 0 next 0 inputs 1 named-first 0`
and `busy said 0 admitted 1 key 0 kept 0 held 1`, and stopped at the `pids` step, where the base has
no `write_dir_lock_pid`: the probe tells the two drivers apart.

Where the probe is narrower than section 4 describes, none moving a criterion:
- The fixture's `.memory-tree.conf` is written after the seed commit and left untracked. Committed,
  the checker refused `SPEC_DIRECT_CUTOFF` as not past the day it was committed, which is the
  fixture's date and not the driver.
- The `pids` step removes `K` first, as every call step does; left in place, the start half skips
  and starts no checker, so there is no `pid.checker` to read.
- The `killed` step's stub lives under the fixture's git dir, because `SPEC_TOKENS_CLI` is
  repo-relative.

One build choice the section 4 snippet does not spell: the start half's tree read keeps its
column inside the new `if [ "$ST_STATE" != busy ]` block, so its line, which carries a command
substitution, is not an added line and AC7 holds as written. Its behaviour is the snippet's.

**Evidences:** TOOL-aPiecewiseGrade-6
- AC1 — `overlap second-busy 1 next 1 inputs 1 named-first 1` — printed as written.
- AC2 — `busy said 1 admitted 1 key 0 kept 1 held 1` and `busyred refused 1 held 1` — both printed as written.
- AC3 — `stale said 0 key 1 named 1 lock 0 event 1` — printed as written.
- AC4 — `release skip 1 refused 1 moved 1 window 1 cacheoff 1` — printed as written.
- AC5 — `git diff -U0 fccef94ef -- tools/unattended/unattended.sh | grep -cE '^-.*(echo "unattended: dispatch|fail 49 |WC_WHY=)'`
  printed 0, and the same with `^\+` printed 1, the busy line.
- AC6 — `grep -c 'claim_push_lock' tools/unattended/unattended.sh tools/unattended/unattended.test.sh`
  printed 0 for both, and `grep -n 'write_dir_lock "' tools/unattended/unattended.sh` named two call
  sites, `write_claim`'s passing `"$(( REMOTE_BOUND + 10 ))" claim-push` and the start half's
  passing the stem `spec-tokens`.
- AC7 — the `git diff -U0 fccef94ef -- tools/unattended/unattended.sh | grep -E '^\+'` pipeline the
  criterion spells printed 0.
- AC8 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` printed nothing,
  `grep -c 'One dispatch of a build at a time holds that cache' memory/guides/UNATTENDED-VERBS.md`
  printed 1, and `grep -c 'spec-tokens-lock-broken' tools/unattended/README.md` printed 1.
- AC9 — `python tools/codebase-map/gen_map.py --check` exited 0 after `--write`, and
  `grep -c '"id": "write_dir_lock"' memory/map/generated/symbols.json` printed 1.
- AC10 — `pids driver 1 checker 1 end 1` — printed as written.
- AC11 — `killed during 1 after 0 key 1 event 1` — printed as written.
- AC12 — `planted-dead stamped 0 consumed 0 skipped 0 event 3` — printed as written.
- AC13 — `planted-live driver 1 checker 1 stampless 1 pending 1 held 4` — printed as written.
- AC14 — `claim live 1 passed 0 young 1 aged 0` — printed as written.
- AC15 — the `git diff -U0 fccef94ef -- tools/unattended/unattended.test.sh | grep -E '^-[^-]'`
  pipeline the criterion spells printed 0.

Owed to the main loop at the close. These were written and not run:
- New arm, the `TOOL-aPiecewiseGrade-6 AC1 AC2 AC3 AC4` assertions after TOOL-aPiecewiseGrade-2's
  block in `tools/unattended/unattended.test.sh`: RED on ignoring the take's status, on dropping
  the busy branch's `ST_STATE`, on making `check_dir_lock_stale` answer busy, and on cutting the
  skip return's release; GREEN once each is restored.
- New arm, the `TOOL-aPiecewiseGrade-6 AC10 AC11 AC12 AC13 AC14` assertions after it: RED on
  dropping the pid loop from `check_dir_lock_stale`, on dropping its end-file clause, on reading a
  non-digit first field as gone, on reading an empty population as gone, and on skipping the start
  half's real `pid.checker` write; GREEN once each is restored.
- New arm, the GH37 block on the factory's names: its existing staged breaks re-run unchanged, and
  it is staged RED by passing a hold of 0, which reds `GH37 AC3 ...its until is a deadline in the
  future`. The unchanged GH36 AC14 arm is staged RED by reading an empty pid population as gone.
- The driver suite's `FLOOR_ASSERTIONS` rises 3348 -> 3377 (DERIVED from the arms' text, 29 `hit`,
  `miss` and `same` lines); the close confirms the executed count.
- The legs section 7 names.
