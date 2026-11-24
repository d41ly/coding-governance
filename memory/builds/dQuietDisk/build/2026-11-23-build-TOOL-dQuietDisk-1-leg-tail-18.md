# TOOL-dQuietDisk-1 leg-tail 18 — foreign-prefix parity (every self-test at three prefixes) failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** foreign-prefix parity (every self-test at three prefixes)
- **Hash:** 7487c9ea93ab868e0405a799ae8a19b85f9cc312
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
        position: selftest · PASS · 31 case(s) · 0 failed
FAIL  [scripts] loop factories fixtures: exit 1
        
        factories: selftest · PASS workflow-hand · exit 1 · factories: gate · roles: scripts/roles/workflows.toml: R8 — entry 11 (handoff-hand) lists 'gov-nobody', which names no role file
        factories: selftest · PASS factory-restores · exit 1 · factories: fixture · factory-restores · factory exit 1 · porcelain clean
        factories: selftest · PASS factory-restores-create · exit 1 · factories: fixture · factory-restores-create · factory exit 1 · no created file on disk · porcelain clean
        factories: selftest · PASS scenario-new · exit 0 · factories: fixture · scenario-new · factory exit 0 · gate green
        factories: selftest · PASS scenario-hand · exit 1 · factories: gate · loop: refused · scenario.hand · entry step.nowhere is no gov step
        factories: selftest · PASS factory-interrupt · exit 0 · factories: fixture · factory-interrupt · held paths at prior bytes · porcelain clean · leftover named
        factories: selftest · FAIL · 16 case(s) · 1 failed: workflow-new
FAIL  [scripts] policy fixtures: exit 1
        policy-fixture: pass-and-lane-adopter · legs-off · step 13 · with pass.fast-legs off the adapter exits 0 and prints nothing, as built, and the run record and the gate ledger each hash as before the call · exit 0 · 0 line(s) printed · run record a4d4a0b99ba7 · ledger 877a08f571f5, each unchanged
        policy-fixture: pass-and-lane-gov · pass-and-lane-gov · the flow · WRONG: RuntimeError: the clone holds no memory/builds/aNimbleMend/, the build folder the record door writes in
        policy-fixture: guard-trace · 112 source read(s)
        policy-fixture: guard-trace · 0 absent read(s) set aside
        policy-fixture: guard-trace · 0 ignored read(s) set aside
        policy-fixture: guard-trace · WRONG scripts/loop/kit.toml · not under the policy fixtures guard
        policy-fixture: guard-trace · 89 guard line(s) checked
        policy-fixture: 1085 assertion(s) executed · 3 wrong
FAIL  [scripts] check-arms selftest: exit 1
                         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                           rows=render_retirement_row(BG, "beta refusal message here", unit="a-retirement"))
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "C:\Users\d41ly\AppData\Local\Temp\gate-work.U2uJ4tRR\tmp\tmp.6l5gDrirPd\g\scripts\memory-tree\check-arms.py", line 1653, in build_budget_tree
            os.makedirs(t)
            ~~~~~~~~~~~^^^
          File "<frozen os>", line 254, in makedirs
        FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\d41ly\\AppData\\Local\\Temp\\gate-work.U2uJ4tRR\\tmp\\tmp.6l5gDrirPd\\runs\\7\\tmp\\tmpwmpz5dsh\\b12'
FAIL  [scripts] playbook render selftest: exit 1
        instruction-units:   FAILED · a new level-0 gov unit is listed beside the level-0 repository unit, the level-4 one is not · 0 {'lines': [], 'orders': [], 'refuse': False, 'reds': [], 'render': [{'tag': 'repo.ships-charter', 'text': 'MUST ship the charter.'}], 'rows': '0 row kinds registered'}
        pins: fixture · plant unit-class
        instruction-units:   FAILED · the reader returns every gov unit tag · set()
        instruction-units:   ok · the witness returns the tag a record ends
        instruction-units:   FAILED · unit-class ran to its end · ValueError: the unit plant found no gov unit row
        pins: fixture · FAILED · 14 expectation(s) failed
        
        render_playbook.selftest FAILED — 2 of 199 arm(s)
FAIL  [scripts] powershell hygiene selftest: an undeclared whole run: it printed no probe marker, so it ran every arm
        selftest: both scans and the tracked population observed failing and passing
FAIL  [scripts] tags bundle selftest: exit 1
              tags: 45 rows of 45, budget 80 (tags.bundle-rows), 0 groups folded
              tags: plant bundle-rows-values · rows values: 20 -> 9 rows folded, 40 -> 9 rows folded, 80 -> 45 rows
        arm ok    bundle plant bundle-inline
        arm ok    bundle plant bundle-mode-values
        arm ok    bundle plant bundle-unregistered-type
        arm ok    bundle plant bundle-dangling-target
        arm ok    bundle plant bundle-empty-sections
        FAIL — 4 of 9 bundle plant rows failed
FAIL  [scripts] tags positional selftest: an undeclared whole run: it printed no probe marker, so it ran every arm
        arm ok    positional plant positional-bulk-move
        arm ok    positional plant positional-producer-new
        arm ok    positional plant positional-producer-new
        arm ok    positional plant positional-producer-stale
        arm ok    positional plant positional-producer-stale
        arm ok    positional plant positional-no-tree
        arm ok    positional plant positional-absent
        PASS — the positional plants, 43 rows
foreign-prefix: [vendor/gov] not run — scripts was red
foreign-prefix: [root] not run — scripts was red
FAIL — 44 check(s) failed
```
