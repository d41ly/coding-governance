# TOOL-dQuietDisk-1 leg-tail 33 — policy fixtures failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** policy fixtures
- **Hash:** 1d0900f8b6fac3b9eb11bbb5a212b6b7dd9f5608
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
render-playbook: REFUSED — load-set — BUDGET REFUSE · AGENTS.md · 32845 bytes over CODEX_MAX 32768 · Codex's limit for a file it reads whole · largest: gov:playbook 32845
policy-fixture: budgets-cap-codex-instructions · refuse · the outside enforcer ran, 'over CODEX_MAX 32768' in its output · exit 1 · render-playbook: REFUSED — load-set — BUDGET REFUSE · AGENTS.md · 32845 bytes over CODEX_MAX 32768 · Codex's limit for a file it reads whole · largest: gov:playbook 32845
policy-fixture: budgets-cap-codex-instructions · warn and refuse · the same exit and output · identical
policy-fixture: budgets-cap-codex-instructions · reader · budgets.resolve_caps refuses an outside cap · policy: refused · tools/policy/caps.toml@75f4e336:357 · codex-instructions is consumer, outside the switch; its enforcer reads no mode
policy-fixture: budgets-cap-runlog-record · warn · the outside enforcer ran, '24576' in its output · exit 0 · 24576
policy-fixture: budgets-cap-runlog-record · refuse · the outside enforcer ran, '24576' in its output · exit 0 · 24576
policy-fixture: budgets-cap-runlog-record · warn and refuse · the same exit and output · identical
policy-fixture: budgets-cap-runlog-record · reader · budgets.resolve_caps refuses an outside cap · policy: refused · tools/policy/caps.toml@75f4e336:368 · runlog-record is consumer, outside the switch; its enforcer reads no mode
policy-fixture: budgets-cap-feature-card · warn · the outside enforcer ran, '1024' in its output · exit 0 · 1024
policy-fixture: budgets-cap-feature-card · refuse · the outside enforcer ran, '1024' in its output · exit 0 · 1024
policy-fixture: budgets-cap-feature-card · warn and refuse · the same exit and output · identical
policy-fixture: budgets-cap-feature-card · reader · budgets.resolve_caps refuses an outside cap · policy: refused · tools/policy/caps.toml@75f4e336:379 · feature-card is consumer, outside the switch; its enforcer reads no mode
policy-fixture: budgets-cap-hook-context · warn · the outside enforcer ran, 'capped at 10000 characters' in its output · exit 0 · {"hookSpecificOutput":{"hookEventName":"SubagentStart","additionalContext":"The parent session's orientation card, c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-dmy60231/r/.git/orientation/case.md, holds this route:\n## route\n- build: bX\n- unit: TOOL-bX-0 · spec memory/builds/bX/spe
policy-fixture: budgets-cap-hook-context · refuse · the outside enforcer ran, 'capped at 10000 characters' in its output · exit 0 · {"hookSpecificOutput":{"hookEventName":"SubagentStart","additionalContext":"The parent session's orientation card, c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-dmy60231/r/.git/orientation/case.md, holds this route:\n## route\n- build: bX\n- unit: TOOL-bX-0 · spec memory/builds/bX/spe
policy-fixture: budgets-cap-hook-context · warn and refuse · the same exit and output · identical
policy-fixture: budgets-cap-hook-context · reader · budgets.resolve_caps refuses an outside cap · policy: refused · tools/policy/caps.toml@75f4e336:390 · hook-context is consumer, outside the switch; its enforcer reads no mode
pass-and-lane-adopter: installing from snapshot 408bb120 of the working tree over HEAD 87fdd849 · 15270 files · 9.9s
policy-fixture: pass-and-lane-adopter · install · step 1 · before any row carries the field the adapter exits 0 with its empty-list line · exit 0 · 'pass-legs: 0 legs declared, nothing ran'
policy-fixture: pass-and-lane-adopter · on · step 2 · the gate refuses the product write while no red is open · exit 2 · stderr 'BLOCKED by scratch-guard: this Write targets c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/src/app.txt, a product path under ROUTED_PATHS entry `src/` in c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/.memory-tree.conf, and this session has no orientation card at c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/.git/orientation/pa'
policy-fixture: pass-and-lane-adopter · on · step 3 · over the pass commit the adapter exits 1, its run record reads the planted leg `fail` and the gate ledger holds it red · exit 1 · run record fail · ledger fail
policy-fixture: pass-and-lane-adopter · on · step 4 · the gate admits the product write with one witness line naming planted pass leg and Red-fix: · exit 0 · stderr 'scratch-guard: red-fix lane admits this write — open red leg(s): planted pass leg; its commit owes a `Red-fix: <leg>` trailer beside `Pass: none`'
policy-fixture: pass-and-lane-adopter · lane-off · step 5 · with bar.inline-red-fixes off and the red open the gate refuses, its stderr equal to R0 over the same 755 byte(s) · exit 2 · stderr 'BLOCKED by scratch-guard: this Write targets c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/src/app.txt, a product path under ROUTED_PATHS entry `src/` in c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/.memory-tree.conf, and this session has no orientation card at c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/.git/orientation/pa'
policy-fixture: pass-and-lane-adopter · on · step 6 · the limits verb exits 0 over the fix commit, which carries `Red-fix: planted pass leg` beside `Pass: none` and no unit id · exit 0 · routed-commits: red-fix limits · c17cc2f6 is inside all four · bound 3 path(s), 60 line(s)
policy-fixture: pass-and-lane-adopter · on · step 7 · over the fix commit the adapter exits 0 and its run record reads the planted leg `ok` · exit 0 · run record ok · ledger ok
policy-fixture: pass-and-lane-adopter · on · step 8 · the lane closed with the red: the gate refuses, its stderr equal to R0 over the same 755 byte(s) · exit 2 · stderr 'BLOCKED by scratch-guard: this Write targets c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/src/app.txt, a product path under ROUTED_PATHS entry `src/` in c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/.memory-tree.conf, and this session has no orientation card at c:/users/d41ly/appdata/local/temp/gate-work.u2uj4trr/tmp/pol-u0wp2itt/.git/orientation/pa'
policy-fixture: pass-and-lane-adopter · on · step 9 · the record door exits 0 for the fix commit and writes one red-fix record in the build folder · exit 0 · 2026-11-23-build-ARCH-tPassLane-1-red-fix-1.md
policy-fixture: pass-and-lane-adopter · on · step 10 · the join exits 0 with one fix commit and one record above its step 2 reading, and 0 owed · exit 0 · build-records: red-fix join · 1 fix commit(s) · 1 record(s) · 0 owed · 0 path-less · step 2 read 0 fix commit(s) · 0 record(s) · 0 owed
policy-fixture: pass-and-lane-adopter · on · step 11 · over the range pushed since the pass commit the grader's summary holds `1 red-fix` and no violation line names the fix commit · exit 0 · routed-commits: RANGE 664987cc..eee1599c · graded 1 · 0 exempt by the 2001-01-01 cutoff · 0 merge(s) · 3 not routed · 0 waived · 1 red-fix · 1 spec id(s) at HEAD · ROUTED_PATHS src/
policy-fixture: pass-and-lane-adopter · lane-off · step 12 · with bar.inline-red-fixes off the grader lists the fix commit as `names no unit` · exit 1 · c17cc2f6 fix: the product file reads ok again — no unit id — names no unit
policy-fixture: pass-and-lane-adopter · legs-off · step 13 · with pass.fast-legs off the adapter exits 0 and prints nothing, as built, and the run record and the gate ledger each hash as before the call · exit 0 · 0 line(s) printed · run record 237bd78606f7 · ledger 865b3909bfa2, each unchanged
policy-fixture: pass-and-lane-gov · pass-and-lane-gov · the flow · WRONG: RuntimeError: the clone holds no memory/builds/aNimbleMend/, the build folder the record door writes in
policy-fixture: guard-trace · 112 source read(s)
policy-fixture: guard-trace · 0 absent read(s) set aside
policy-fixture: guard-trace · 0 ignored read(s) set aside
policy-fixture: guard-trace · WRONG tools/loop/kit.toml · not under the policy fixtures guard
policy-fixture: guard-trace · 89 guard line(s) checked
policy-fixture: 1085 assertion(s) executed · 3 wrong
```
