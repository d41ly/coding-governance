# TOOL-dQuietDisk-1 leg-tail 39 — upgrade-walk failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** upgrade-walk
- **Hash:** 68fd0644414f69b86bc77712825dfacbd3f9776d
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg upgrade-walk | exit 2
upgrade-walk: grader · order-kind · ok
upgrade-walk: grader · arm-needle · ok
upgrade-walk: grader · tree-clean · ok
upgrade-walk: grader · case-counts · ok
upgrade-walk: grader · fixture-keys · ok
upgrade-walk: grader · release-engine · ok
upgrade-walk: grader · shim-root · ok
upgrade-walk: grader · plant-root · ok
upgrade-walk: release-0 applied by the pinned clone's own apply over the fixture's kits line · exit 0 · receipt schema 3
upgrade-walk: release-0 · the policy adopter's re-run committed .governance/policy.json
upgrade-walk: pin 60d90cb71db51e651aa1c5efe3f6d48ba21a997d · landed ref 4b5054df2ea652d443ff5eda27ec2b0590b870d7 · tip 5163b97a7a9a91f229dcfc155b89dff980fdaabc · 27 step(s)
upgrade-walk: nothing measured: up · the walk to the tip did not return: exit 1 | the upgrade-step walk stopped at memory-tree/row-duplicate-pin-to-ledger: exit 1: conf-pins-to-ledger: up refused · the seed of row-duplicates did not arm it, so the key and its row stay in place: unarmed row-duplicates no directory memory/project. The steps before it stay applied; the next `update  | kit 'policy' passed its own check before this run and fails it after: exit 0 -> 1. Its writes were ROLLED BACK to their pre-run index entries and an order was written under .governance/outbox/
```
