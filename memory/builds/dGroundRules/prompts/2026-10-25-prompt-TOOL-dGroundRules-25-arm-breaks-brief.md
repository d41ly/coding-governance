**Serves:** research TOOL-dGroundRules-25 TOOL-dGroundRules-10 TOOL-dGroundRules-21

# Research brief — staged breaks for the close's hard suite arms

## The prompt

> The close observes each `New arm:` line RED on a staged break and GREEN once restored (BUILD-METHOD M8). For most arms the break is the unit's product change rolled back; for the arms below the unit changed only the suite, or the arm tests pre-existing behaviour, so a rollback cannot red them and a break has to be designed.

## The brief

### Goal
For each arm below, read the suite arm and the product code it exercises at HEAD, and return ONE minimal staged break per arm: the exact file, the exact old text and the exact new text (a literal substring replacement, applied in a scratch clone), chosen so that arm goes RED naming its own assertion while the product still runs; plus the arm's assertion line(s) that should FAIL, and how to run the suite (its argv from `tools/gate-legs.json`, or the `--shard <i>/<n>` that holds the arm). Read only; write nothing; run no suite.
1. TOOL-dGroundRules-10 AC12, `tools/govkit/selftest.py`: its fixture renderer arm, re-pointed from the print mode to the policy reader.
2. TOOL-dGroundRules-10 AC12, `tools/workflows/unattended-build.test.sh`: its renderer arm, re-pointed to the policy reader.
3. TOOL-dGroundRules-21 AC33, `tools/workflows/check-review-join.test.sh`: the D7 arm re-planted with a stub predicate exiting 2 before any rule.
4. TOOL-dGroundRules-25 AC2-AC4, `tools/push-main.test.sh`: a policy-file change on `feat` landed through the real `--prepare`, then the lander staged to a stub.
5. TOOL-dGroundRules-25 AC35, `tools/check-template-size.test.sh`: a `PATH` holding no Python launcher over an over-cap subject, the `fail 5` line asserted.
6. TOOL-dGroundRules-25, `tools/memory-tree/check-memory-hygiene.test.sh`: a `PATH` holding no Python launcher, exit 2 and the line `HYGIENE · no usable python`.
7. TOOL-dGroundRules-66 AC1-AC3, `tools/unattended/unattended.test.sh` region 4: confirm that rolling `tools/unattended/unattended.sh` back to `cfdee9fd0^` reds those arms, and give the shard argv that runs region 4 alone.
Each unit's spec §6/§7 `New arm:` line and its acceptance ledger under `memory/builds/dGroundRules/build/` describe the arm and how its builder observed it.

### Non-goals
Any write; any change to a tracked file; running a suite.

### Acceptance
One entry per arm: file · old text · new text · the FAIL line(s) expected · the suite argv.

### Gates
No gate runs in this pass.

### Limitations
HEAD is 7e80dee4d; TOOL-dGroundRules-67 is building meanwhile and touches none of these files.

### Reuse
The close's own break script shape: literal substring replacement in a scratch clone.
