# TOOL-dQuietDisk-1 leg-tail 37 — loop budget fixtures failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** loop budget fixtures
- **Hash:** 074584e7e1a32800e0f0170a8e8996c0cea9ac43
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg loop budget fixtures | exit 1
loop: budget selftest · PASS mint-each-lap · exit 0 · loop: fixture · mint-each-lap · held
loop: budget selftest · PASS before-freeze · exit 0 · loop: fixture · before-freeze · held
loop: budget selftest · PASS stale-verdict · exit 0 · loop: fixture · stale-verdict · held
loop: budget selftest · PASS patch-draw · exit 0 · loop: fixture · patch-draw · held
loop: budget selftest · PASS route-backs · exit 0 · loop: fixture · route-backs · held
loop: budget selftest · PASS value · exit 0 · loop: fixture · value · held
loop: budget selftest · PASS unknown-cause · exit 0 · loop: fixture · unknown-cause · held
loop: budget selftest · PASS driver-draws · exit 0 · loop: fixture · driver-draws · held
loop: budget selftest · PASS spent-spec-round · exit 0 · loop: fixture · spent-spec-round · held
loop: budget selftest · PASS re-entry · exit 0 · loop: fixture · re-entry · held
loop: budget selftest · PASS pre-spec · exit 0 · loop: fixture · pre-spec · held
loop: budget selftest · PASS unrecorded · exit 0 · loop: fixture · unrecorded · held
loop: budget selftest · PASS trailer-only · exit 0 · loop: fixture · trailer-only · held
loop: budget selftest · PASS patch-trailer-only · exit 0 · loop: fixture · patch-trailer-only · held
loop: budget selftest · PASS log-dropped · exit 0 · loop: fixture · log-dropped · held
loop: budget selftest · PASS parallel-append · exit 0 · loop: fixture · parallel-append · held
loop: budget selftest · PASS parallel-append-uneven · exit 0 · loop: fixture · parallel-append-uneven · held
loop: budget selftest · PASS draw-id-rows · exit 0 · loop: fixture · draw-id-rows · held
loop: budget selftest · PASS draws-survive-rotation · exit 0 · loop: fixture · draws-survive-rotation · held
loop: budget selftest · PASS patch-archived · exit 0 · loop: fixture · patch-archived · held
loop: budget selftest · PASS ending · exit 0 · loop: fixture · ending · held
loop: budget selftest · PASS driver-exhausted · exit 0 · loop: fixture · driver-exhausted · held
loop: budget selftest · PASS unattended-root · exit 0 · loop: fixture · unattended-root · held
loop: budget selftest · PASS confs-disagree · exit 0 · loop: fixture · confs-disagree · held
loop: budget selftest · PASS no-own-conf-read · exit 0 · loop: fixture · no-own-conf-read · held
loop: budget selftest · PASS root-source · exit 0 · loop: fixture · root-source · held
loop: budget selftest · PASS attr-missing · exit 0 · loop: fixture · attr-missing · held
loop: budget selftest · PASS patch-concurrent · exit 0 · loop: fixture · patch-concurrent · held
loop: budget selftest · PASS unset-driver-root · exit 0 · loop: fixture · unset-driver-root · held
loop: budget selftest · PASS patch-claims-unread · exit 0 · loop: fixture · patch-claims-unread · held
loop: budget selftest · PASS trailing-slash-agree · exit 0 · loop: fixture · trailing-slash-agree · held
loop: budget selftest · PASS no-confs · exit 0 · loop: fixture · no-confs · held
loop: budget selftest · PASS driver-root-readers · exit 0 · loop: fixture · driver-root-readers · held
loop: budget selftest · PASS conf-read-forms · exit 0 · loop: fixture · conf-read-forms · held
loop: budget selftest · PASS placement-loop · exit 0 · loop: fixture · placement-loop · held
loop: budget selftest · PASS no-intake · exit 0 · loop: fixture · no-intake · held
loop: budget selftest · PASS rows-on-ref · exit 0 · loop: fixture · rows-on-ref · held
loop: budget selftest · FAIL two-nodes · exit 1, owed 0 and a line 'loop: fixture · two-nodes · held' naming '': 365581 · exit 0 · draw · route-back · item.entry.place · 2/4
loop: fixture · second clone · exit 0 · draw · route-back · item.entry.place · 1/4
loop: fixture · two-nodes · MISSED the second clone's draw never reached its push; the first clone drew 'draw · route-back · item.entry.place · 2/4', not 1/4; the second clone did not re-read once and draw 2/4: 'draw · route-back · item.entry.place · 1/4'

loop: budget selftest · PASS unreachable · exit 0 · loop: fixture · unreachable · held
loop: budget selftest · PASS slug-retry · exit 0 · loop: fixture · slug-retry · held
loop: budget selftest · PASS owner-after-exhausted · exit 0 · loop: fixture · owner-after-exhausted · held
loop: budget selftest · FAIL · 41 case(s) · 1 failed: two-nodes
```
