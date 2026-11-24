# TOOL-dQuietDisk-1 leg-tail 35 — loop splice check failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** loop splice check
- **Hash:** 0a616af2ef64e633b596bab3a0ccb09484c3ad4e
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg loop splice check | exit 1
loop: splice selftest · PASS check · exit 0 · loop: splices composed · 0 splice(s)
loop: splice selftest · PASS between-test-deploy · exit 0 · loop: splice step.adopter.security-review · R2 adopter-security-review → deploying · item.adopter.security-review.exit · recorded
loop: splice selftest · PASS removes · exit 1 · loop: refused · the stage step.adopter.security-review · removes · the gov stage step.test is excluded, and gov's five stages stay whole
loop: splice selftest · PASS reorders · exit 1 · loop: refused · the stage step.adopter.security-review · adjacent · step.deploy and step.test are not adjacent in order: its before is the gov step after its after
loop: splice selftest · PASS replaces · exit 1 · loop: refused · the stage step.test · tag · holds no `adopter` seat of one name of its own: a repository stage is step.adopter.<name>, its name no gov step's
loop: splice selftest · PASS before-plan · exit 1 · loop: refused · the stage step.adopter.security-review · adjacent · its after None is no gov step, so no gov stage precedes it
loop: splice selftest · PASS after-deploy · exit 1 · loop: refused · the stage step.adopter.security-review · adjacent · its before None is no gov step, so no gov stage follows it
loop: splice selftest · PASS non-adjacent · exit 1 · loop: refused · the stage step.adopter.security-review · adjacent · step.build and step.deploy are not adjacent in order: its before is the gov step after its after
loop: splice selftest · PASS two-splices · exit 1 · loop: refused · the stages step.adopter.security-review and step.adopter.second-review · one per pair · each splices between step.test and step.deploy, and at most one stage sits between two gov steps
loop: splice selftest · PASS gov-rename · exit 0 · loop: re-point step.adopter.security-review · after step.verify → step.test
loop: splice selftest · PASS gov-rename R1 · exit 0 · loop: splice step.adopter.security-review · R1 testing → adopter-security-review · item.test.exit · recorded
loop: splice selftest · PASS stale-pin · exit 1 · loop: refused · the stage step.adopter.security-review · pin · cb6301b0 is stale: the split row testing → deploying on item.test.exit pins cb6301be
loop: splice selftest · PASS exit-elsewhere · exit 1 · loop: refused · the stage step.adopter.security-review · exit · item.test.exit is no item of the stage whose outcome recorded routes to transition
loop: splice selftest · PASS exit-unwitnessed · exit 1 · loop: refused · the stage step.adopter.security-review · witness · loop.toml: the item item.adopter.security-review.exit carries no witness, an inline table { class, by }
loop: splice selftest · PASS orphan-item · exit 1 · loop: refused · program · loop.toml: item row 82 tag 'item.adopter.ghost.check' opens no item.adopter.<stage>.<name> of a composed stage: step.adopter.security-review
loop: splice selftest · FAIL factory · exit 1, owed 0 and a line 'loop: fixture · new again' naming 'step.test and step.deploy': e · check · exit 0 · loop: splices composed · 1 splice(s)
loop: fixture · item check · exit 1 · loop: items composed · 81 row(s) · 1 repository
loop: fixture · new again · exit 2 · loop: refused · new step.adopter.demo · HEAD's composition holds the stage step.adopter.demo between step.test and step.deploy already
loop: fixture · FAIL · item check exited 1, owed 0 and a line naming · 1 repository

loop: splice selftest · FAIL · 16 case(s) · 1 failed: factory
```
