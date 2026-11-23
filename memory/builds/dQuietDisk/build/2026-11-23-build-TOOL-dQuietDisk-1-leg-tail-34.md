# TOOL-dQuietDisk-1 leg-tail 34 — loop item kind failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** loop item kind
- **Hash:** 35b581d122d105046acdc4430179536bec392bd2
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
loop: upstream edges · 0 record · 0 measured
loop: refused · the item item.test.flakes returns names record-kind.flake, a typed record kind no [[record-version]] row pins
loop: fixture · new again · exit 2 · loop: refused · new item.test.demo · the definition declares item.test.demo already

loop: item kind selftest · PASS repo-cycle · exit 1 · loop: refused · C:/Users/d41ly/AppData/Local/Temp/gate-work.U2uJ4tRR/tmp/li-xaxnsq93/tools/loop/loop.toml: the item needs form a cycle: item.test.adopter.cycle-a -> item.test.adopter.cycle-b -> item.t
loop: item kind selftest · PASS repo-unresolved-need · exit 1 · loop: refused · C:/Users/d41ly/AppData/Local/Temp/gate-work.U2uJ4tRR/tmp/li-xaxnsq93/tools/loop/loop.toml: the item item.test.adopter.needy needs item.test.adopter.nosuch, which no [[item]] row declar
loop: item kind selftest · PASS repo-input-unproduced · exit 1 · loop: refused · the item item.test.adopter.reader input 'layer.memory:record-kind.acceptance@1' reads record-kind.acceptance@1, which no item in its needs closure returns at that version
loop: item kind selftest · FAIL repo-input-produced · exit 1, owed 0 and a line 'loop: record inputs' naming '1 joined': ion · 1 · 55701546
loop: record-version record-kind.recommendation · 1 · ad896b7b
loop: record-version record-kind.probe-trigger · 1 · 06f96147
loop: record-version record-kind.probe · 1 · fb9eb079
loop: record inputs · 1 joined
loop: upstream edges · 0 record · 0 measured
loop: refused · the item item.test.flakes returns names record-kind.flake, a typed record kind no [[record-version]] row pins

loop: item kind selftest · PASS version-unbumped · exit 1 · loop: refused · record-version record-kind.acceptance fields c24a6acc is not 2f3b42fb, the hash of its row in the record table, while its version stays 1: its meaning changed with no bump · remedy: bu
loop: item kind selftest · FAIL version-bumped · exit 1, owed 0 and a line 'loop: record-version record-kind.acceptance' naming '· 2 ·': ion · 1 · 55701546
loop: record-version record-kind.recommendation · 1 · ad896b7b
loop: record-version record-kind.probe-trigger · 1 · 06f96147
loop: record-version record-kind.probe · 1 · fb9eb079
loop: record inputs · 0 joined
loop: upstream edges · 0 record · 0 measured
loop: refused · the item item.test.flakes returns names record-kind.flake, a typed record kind no [[record-version]] row pins

loop: item kind selftest · PASS version-stale-input · exit 1 · loop: refused · the item item.test.adopter.reader input 'layer.memory:record-kind.acceptance@1' reads record-kind.acceptance@1, which no item in its needs closure returns at that version
loop: item kind selftest · PASS patch-witness · exit 1 · loop: refused · row-checks: red · fixed · item.test.adopter.select-seen amends item.test.select · field witness · fixed by principle=principle.p2 · remedy: drop the field from the row
loop: item kind selftest · PASS patch-outcomes · exit 1 · loop: refused · row-checks: red · fixed · item.test.adopter.select-skips amends item.test.select · field outcomes · fixed by principle=principle.p24 · remedy: drop the field from the row
loop: item kind selftest · PASS supersede-floor · exit 1 · loop: refused · row-checks: red · fixed · item.test.adopter.verdict-own supersedes the fixed row item.test.verdict · fixed by principle=principle.p2 · remedy: drop the row; gov's fixed rows take no ch
loop: item kind selftest · PASS supersede-exit · exit 1 · loop: refused · row-checks: red · fixed · item.test.adopter.build-exit-own supersedes the fixed row item.build.exit · fixed by principle=principle.p20 · remedy: drop the row; gov's fixed rows take no 
loop: item kind selftest · PASS exclude-needed · exit 1 · loop: refused · row-checks: red · exclude · instructions.exclude lists item.test.select, which item.test.verdict still holds in its needs field `needs` · remedy: take item.test.select from that field,
loop: item kind selftest · PASS exclude-breakpoint · exit 1 · loop: refused · row-checks: red · exclude · instructions.exclude lists item.test.flakes, which the policy key review.breakpoints names · remedy: take item.test.flakes from review.breakpoints, or drop 
loop: item kind selftest · FAIL patch-remove-need · exit 1, owed 0 and a line 'loop: patch' naming 'needs remove · widens': ion · 1 · 55701546
loop: record-version record-kind.recommendation · 1 · ad896b7b
loop: record-version record-kind.probe-trigger · 1 · 06f96147
loop: record-version record-kind.probe · 1 · fb9eb079
loop: record inputs · 0 joined
loop: upstream edges · 0 record · 0 measured
loop: refused · the item item.test.flakes returns names record-kind.flake, a typed record kind no [[record-version]] row pins

loop: item kind selftest · FAIL patch-add-need · exit 1, owed 0 and a line 'loop: patch' naming 'needs add · narrows': ion · 1 · 55701546
loop: record-version record-kind.recommendation · 1 · ad896b7b
loop: record-version record-kind.probe-trigger · 1 · 06f96147
loop: record-version record-kind.probe · 1 · fb9eb079
loop: record inputs · 0 joined
loop: upstream edges · 0 record · 0 measured
loop: refused · the item item.test.flakes returns names record-kind.flake, a typed record kind no [[record-version]] row pins

loop: item kind selftest · FAIL patch-routes · exit 1, owed 0 and a line 'loop: patch' naming 'routes add · widens': ion · 1 · 55701546
loop: record-version record-kind.recommendation · 1 · ad896b7b
loop: record-version record-kind.probe-trigger · 1 · 06f96147
loop: record-version record-kind.probe · 1 · fb9eb079
loop: record inputs · 0 joined
loop: upstream edges · 0 record · 0 measured
loop: refused · the item item.test.flakes returns names record-kind.flake, a typed record kind no [[record-version]] row pins

loop: item kind selftest · PASS amended-cycle · exit 1 · loop: refused · C:/Users/d41ly/AppData/Local/Temp/gate-work.U2uJ4tRR/tmp/li-xaxnsq93/tools/loop/loop.toml: the item needs form a cycle: item.test.merge -> item.test.verdict -> item.test.select -> item
loop: item kind selftest · PASS exit-unfixed · exit 1 · loop: refused · the step step.build exit item.build.exit holds no [[fixed-row]] in tools/loop/item-schema.toml
loop: item kind selftest · PASS schema-absent · exit 2 · loop: fixture · compose · exit 2 · overlay-rows: unarmed · kind item · tools/loop/item-schema.toml, its schema, is absent
loop: item kind selftest · PASS definition-uncommitted · exit 2 · loop: fixture · render after the commit · exit 0 · 80 gov:item line(s), 80 [[item]] table(s)
loop: item kind selftest · FAIL · 22 case(s) · 7 failed: check factory repo-input-produced version-bumped patch-remove-need patch-add-need patch-routes
```
