# TOOL-dQuietDisk-1 leg-tail 38 — loop termination failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** loop termination
- **Hash:** 59556408b2dec27016cbd7b1a4031a7181cd18c8
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg loop termination | exit 1
loop: termination · wait · flow.wait-ceiling 72 hour(s) · 0 live build(s) checked
loop: termination · gov · 7 build state(s) · 52 row(s) · 80 item(s) · 8 program(s)
loop: termination · raise · 0 build(s)
loop: termination · decline · 0 build(s)
loop: termination · pending · 1 wait row(s) · 14 cycle row(s)
loop: termination · wait · cycle item.review.dispose -> item.review.fold -> item.review.dispose · stale: its build dDeclaredLoop has landed; delete the row
loop: termination · wait · cycle item.test.flakes -> item.test.select -> item.test.verdict -> item.test.route -> item.test.flakes · stale: its build dWitnessedBar has landed; delete the row
loop: termination · wait · cycle item.test.flakes -> item.test.verdict -> item.test.route -> item.test.flakes · stale: its build dWitnessedBar has landed; delete the row
loop: termination · wait · cycle item.test.merge -> item.test.select -> item.test.verdict -> item.test.merge · stale: its build dWitnessedBar has landed; delete the row
loop: termination · wait · cycle item.test.route -> item.test.verdict -> item.test.route · stale: its build dWitnessedBar has landed; delete the row
loop: termination · gov · 5 finding(s)
loop: termination · selftest · PASS stage-self-loop · exit 0 · loop: fixture · stage-self-loop · held
loop: termination · selftest · PASS stage-self-loop-drawn · exit 0 · loop: fixture · stage-self-loop-drawn · held
loop: termination · selftest · PASS dead-end · exit 0 · loop: fixture · dead-end · held
loop: termination · selftest · PASS unit-dead-end · exit 0 · loop: fixture · unit-dead-end · held
loop: termination · selftest · PASS orphan-item · exit 0 · loop: fixture · orphan-item · held
loop: termination · selftest · PASS empty-states · exit 0 · loop: fixture · empty-states · held
loop: termination · selftest · PASS wait-no-deadline · exit 0 · loop: fixture · wait-no-deadline · held
loop: termination · selftest · PASS wait-declared · exit 0 · loop: fixture · wait-declared · held
loop: termination · selftest · PASS wait-stale · exit 0 · loop: fixture · wait-stale · held
loop: termination · selftest · FAIL stale-build · exit 2, owed 0 and a line 'loop: fixture · stale-build · held' naming '': loop: fixture · plant stale-build · a pending cycle row over a build's composition whose own rows break the cycle, gov unset
loop: fixture · stale-build · UNARMED · the plant could not be built: C:/projects/coding-governance/.claude/worktrees/disk-churn-fixes-40450b/tools/loop/loop.toml: the item item.plan.research outcome probe has no route 

loop: termination · selftest · PASS raise-unattended · exit 0 · loop: fixture · raise-unattended · held
loop: termination · selftest · PASS raise-released · exit 0 · loop: fixture · raise-released · held
loop: termination · selftest · PASS raise-held · exit 0 · loop: fixture · raise-held · held
loop: termination · selftest · PASS decline · exit 0 · loop: fixture · decline · held
loop: termination · selftest · PASS deadline-patch · exit 0 · loop: fixture · deadline-patch · held
loop: termination · selftest · PASS boundary · exit 0 · loop: fixture · boundary · held
loop: termination · selftest · FAIL · 16 case(s) · 1 failed: stale-build
```
