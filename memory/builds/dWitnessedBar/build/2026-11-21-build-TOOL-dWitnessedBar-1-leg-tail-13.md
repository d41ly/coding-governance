# TOOL-dWitnessedBar-1 leg-tail 13 — layer dependencies (the core never depends on an expansion) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** layer dependencies (the core never depends on an expansion)
- **Hash:** d7caee92117f5174757d8c9704da2898ca2331ae
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** 079d8513ce2ba90ffd4755b9b8677ab9b4bba1ee
- **Cause:** run:dWitnessedBar

```
# run-gates | leg layer dependencies (the core never depends on an expansion) | exit 1
layers: RED tools/memory-tree/legacy_ledger.py:230 · probe · core kit memory-tree depends on non-core kit govkit, and no optional row of its descriptor names the file as part
layers: RED tools/playbook/instruction_units.py:2152 · probe · core kit playbook-render depends on non-core kit govkit, and no optional row of its descriptor names the file as part
layers: RED tools/playbook/writing_practice.py:491 · probe · core kit playbook-render depends on non-core kit govkit, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/keep_tails.py:109 · probe · core kit run-gates depends on non-core kit runlog, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/keep_tails.py:114 · import · core kit run-gates depends on non-core kit runlog, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/leg_factory.py:74 · probe · core kit run-gates depends on non-core kit govkit, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/leg_factory.py:136 · probe · core kit run-gates depends on non-core kit govkit, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/leg_factory.py:141 · import · core kit run-gates depends on non-core kit govkit, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/product_tests.py:284 · probe · core kit run-gates depends on non-core kit pytest-parallel-guardrails, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/product_tests.py:292 · copy · core kit run-gates depends on non-core kit pytest-parallel-guardrails, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/verdict_flow.py:1186 · probe · core kit run-gates depends on non-core kit drift-audit, and no optional row of its descriptor names the file as part
layers: RED tools/run-gates/verdict_flow.py:1312 · probe · core kit run-gates depends on non-core kit drift-audit, and no optional row of its descriptor names the file as part
layers: not read: a path computed at run time, JavaScript, a file no descriptor claims, a path that names no file the kit ships, and a bare kit name inside a string or a here-document
layers: 12 layer row(s), 30 kit descriptor(s); edges by kind: import 5 · dynamic 0 · probe 48 · copy 6 · shell 0 · requires-if 0; 47 allowed, 12 red; 0 contract red(s)
```
