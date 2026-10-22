**Serves:** research TOOL-dTrueNorth-30

# Spec brief — TOOL-dTrueNorth-30, the check 21 writer arm that has never been green

## The prompt

> After TOOL-dTrueNorth-29, `tools/memory-tree/check-memory-hygiene.test.sh` at `92a0dcb96` reds one arm this build owns: `check 21: a record an older harness wrote, merged after the pinning harness landed, fails check 21`. A debug copy of the suite dumped the gate's output at that arm: check 21 fails on `memory/builds/tOne/build/result.json — no Serves line in the first 12 unfenced lines`, an undated artifact an earlier arm of the suite plants in the shared fixture and leaves for later arms, while the audit-pin line beside it reads `graded 1 spec-audit record(s) … 1 written by a harness before renderAuditBinding`. TOOL-dTrueNorth-14 added the arm; its writer test never ran in a suite before the close, so the arm has never been green.

## The brief

### Goal
Author TOOL-dTrueNorth-30, one Tier-2 unit whose pass turns that arm green by its cause, the fixture's leftover artifact, without loosening what the arm asserts. Author only: no product code, no commit, no gate.

### Items
1. The arm's conf (the `write_pk_conf` call inside the TOOL-dTrueNorth-14 AC4 block, after `WF_KIT` resolves) declares `RECORD_UNDATED_ARTIFACTS="exempt"` beside its two keys, as the TOOL-aRepatriatedFork-32 arms over the same fixture already do, so check 21 grades the records the arm is about and not the earlier arm's `result.json`. If the spec finds a cleaner cause-level fix (the earlier arm removing its own artifact without breaking the arms that read it), it may take that instead and say why.
2. Neither arm of the block changes what it asserts: the first still requires the four-field Q row's exempt count, the second still reds on `HYGIENE check 21 FAILED`.
3. The spec carries `**Derived:** PLAY-dClosedLoop-2`, `order 13`, Tier-2, status OPEN, path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-30.md`, a micro-spec's length, and an AC a pass can observe without running the suite, for example the arm's conf line by grep and a probe replaying the arm's fixture commits with the gate called once.
4. Write `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-30-deviation-32.md` for the unit itself: Departs from `dTrueNorth [roster]`, design-to-spec, builder discovery, additive, spec writer under author-recorded, `new unit TOOL-dTrueNorth-30`, Caused-by `PLAY-dClosedLoop-2`.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the spec; the AC is a probe a pass can run; the record reads with no malformed field under `python tools/memory-tree/deviation_join.py`.

### Gates
No gate runs in this pass; the spec's §7 names the `memory-hygiene self-test` leg.

### Non-goals
Any other spec; product code; any other arm; the inherited check 26 `cache hits` half of the partition arm; inside §6, an untracked file named by full path inside a backticked token.
