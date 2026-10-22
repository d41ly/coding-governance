**Serves:** journal TOOL-dTrueNorth-29

# TOOL-dTrueNorth-29 — the flagged bar at e583a7f42, its red legs excerpted

The bar `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` ran at e583a7f42 in the run's worktree on node d, rc 1: 133 legs ok, 9 failed. Below, each failed leg's FAIL lines, cut from the 450 KB log; the classification against the base is the brief's.

## Verdicts

```
GATE FAIL  memory-hygiene self-test  (exit 1)
GATE retry  routed-commits selftest  (timed out after 300s beside 2 neighbours; retried in the pool's tail, and alone after it drains unless that passes)
GATE FAIL  row-grammar selftest  (exit 1)
GATE FAIL  pre-push self-test  (exit 1)
GATE retry  push-main self-test  (timed out after 580s beside 4 neighbours; retried in the pool's tail, and alone after it drains unless that passes)
GATE FAIL  tier2-review self-test  (exit 1)
GATE FAIL  unattended-build self-test  (exit 1)
GATE FAIL  foreign-prefix parity (every self-test at three prefixes)  (exit 1)
GATE FAIL  measure-legs selftest  (exit 1)
GATE FAIL  govkit selftest  (exit 1)
GATE FAIL  spec-tokens self-test  (exit 1)
```

## Failed legs

### memory-hygiene self-test  (exit 1)

```
    FAIL the scoped runs do not partition the unscoped run's lines:
    < memory-hygiene: check 29: coverage off — SPEC_CARRIES_CUTOFF is blank
    < memory-hygiene: check 30: as-built view: off — DESIGN_RECORD, DESIGN_BASELINE, DESIGN_VIEW, DESIGN_NODES are blank in .memory-tree.conf, so nothing is read and no view is rendered
    FAIL <tree>/tools/memory-tree/.memory-tree.conf.example does not declare DESIGN_BASELINE, which a module in <tree>/tools/memory-tree reads out of a dict, so an adopter cannot discover it
    FAIL <tree>/tools/memory-tree/.memory-tree.conf.example does not declare DESIGN_NODES, which a module in <tree>/tools/memory-tree reads out of a dict, so an adopter cannot discover it
    FAIL <tree>/tools/memory-tree/.memory-tree.conf.example does not declare DESIGN_RECORD, which a module in <tree>/tools/memory-tree reads out of a dict, so an adopter cannot discover it
    FAIL <tree>/tools/memory-tree/.memory-tree.conf.example does not declare DESIGN_VIEW, which a module in <tree>/tools/memory-tree reads out of a dict, so an adopter cannot discover it
    FAIL check 21: the audit-pin arm did not count the record an older harness wrote as exempt
    FAIL check 21: a record an older harness wrote, merged after the pinning harness landed, fails check 21
```

### row-grammar selftest  (exit 1)

```
    arm FAIL  no sibling engine in this kit imports corpus_ids or gen_build_index — expected to see: hits=[]
          got: hits=[('deviation_join.py', 473, 'gen_build_index')] graded=14
    FAIL — 1 arm(s) failed
```

### pre-push self-test  (exit 1)

```
      FAIL — TOOL-aSparedSpawn-33 AC1 expected the scoped push to reuse pr from the direct bar's entry, got rc=0: pre-push: the merge-loss check did NOT run over refs/heads/main — the lexicon kit is installed neither under '%TEMP%/gate-work.GLi49YuO/tmp/tmp.6k5YDtC1OY/dg/work' nor beside this hook, so no merge in this push was graded.
```

### tier2-review self-test  (exit 1)

```
    FAIL spec-audit: a spec that is also a subject is refused
    FAIL executed 342 assertions against a floor of 343 — arms are UNREACHABLE rather than absent; look for a block stranded past an early exit or a die()
```

### unattended-build self-test  (exit 1)

```
    FAIL TN5-AC3 a caller subject with no id is refused naming the field -- output lacked 'THROW unattended-build: subject 0's `id` is not a unit id'
```

### foreign-prefix parity (every self-test at three prefixes)  (exit 1)

```
    FAIL  [scripts] row-grammar selftest: exit 1
            FAIL — 1 arm(s) failed
    FAIL  [scripts] tier2-review self-test: exit 1
            FAIL executed 342 assertions against a floor of 343 — arms are UNREACHABLE rather than absent; look for a block stranded past an early exit or a die()
    FAIL  [scripts] measure-legs selftest: exit 1
            FAIL (98 assertions)
    FAIL  [scripts] unattended gate selftest shard 8/8: exit 1
            FAIL a helper is defined inside a shard region, stranded for any shard that does not run it: /tmp/gate-work.GLi49YuO/tmp/tmp.3xNDXTQGKM/g/scripts/unattended/check-unattended.test.sh:3805: seed_spc() { # the authored pair's body, or `absent` for no pair at all
            FAIL (5 assertions)
    FAIL — 4 check(s) failed
```

### measure-legs selftest  (exit 1)

```
      FAIL AC2 memio  ((227053568, {'read_ops': 78, 'write_ops': 202, 'other_ops': 3715, 'read_bytes': 705289, 'write_bytes': 209715226, 'other_bytes': 122070}))
      FAIL AC15 the leg's own bar waited  ((0, 0.0, 13.649, 13.649))
    FAIL (98 assertions)
```

### govkit selftest  (exit 1)

```
    ok   and names what it expected and what it found
    FAIL ...and the playbook file previews as a seed WRITE, not as an order — {'write|engine': 109, 'KEEP|seed': 14, 'ORDER|engine': 1, 'ORDER|attributes': 18, 'ORDER|project-owned': 49, 'SIDE|rendered': 6, 'BLOCK|merged': 1, 'COVER|project-owned': 1, 'ORDER|hole': 7}
    FAIL OC8 AC4 the target's adopter --check reads its render fresh — roles: KIT_DIR derived empty — no .git above the kit at /tmp/gate-work.GLi49YuO/tmp/tmp0hqcsxwt/roles-default/target
    FAIL OC8 AC4 a default apply into a scratch target exits 0 — ked path in this target
    FAIL OC8 AC4 the target's adopter --check reads its render fresh — roles: KIT_DIR derived empty — no .git above the kit at /tmp/gate-work.GLi49YuO/tmp/tmp0hqcsxwt/roles-runner/target
    FAIL OC13 AC4 ...and the adopter's --check exits 0 over the seed's optional lexicon grant — roles: KIT_DIR derived empty — no .git above the kit at /tmp/gate-work.GLi49YuO/tmp/tmp0hqcsxwt/roles-runner/target
    FAIL [-5] D1 every function that runs a shell command is DECLARED in SHELL_EXEC_SITES — undeclared spawn in: run_target_argv
    FAIL [-5] D1 ...and every declared row still names a function that spawns — both directions, so a stale row cannot widen the surface it was written to narrow — declared but no longer spawning: _cmd_apply, _cmd_update
```

### spec-tokens self-test  (exit 1)

```
    arm FAIL  parity: a manifest suite invocation BAR does not match:
    arm FAIL  parity: graded 53 + exempt 14 != the manifest's 68 selftests legs — a leg was skipped without being printed
    arm FAIL  AC6 active arm break — expected a CLAIM_CANARY refusal and no claims line
    arm FAIL  AC6 passive arm break — expected a CLAIM_CANARY refusal and no claims line
    arm FAIL  AC6 noun arm break — expected a CLAIM_CANARY refusal and no claims line
    arm FAIL  AC6 fronted arm break — expected a CLAIM_CANARY refusal and no claims line
    arm FAIL  AC6 case-fold break — expected a CLAIM_CANARY refusal and no claims line
    arm FAIL  AC6 space-clause break — expected a CLAIM_CANARY refusal and no claims line
```
