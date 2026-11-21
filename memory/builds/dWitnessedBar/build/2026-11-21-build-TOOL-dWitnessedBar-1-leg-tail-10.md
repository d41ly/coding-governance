# TOOL-dWitnessedBar-1 leg-tail 10 — spawn budget (forks per hot entrypoint) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** spawn budget (forks per hot entrypoint)
- **Hash:** ad687a29346eb018db3a287dfefe349a76f84c1d
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** 079d8513ce2ba90ffd4755b9b8677ab9b4bba1ee
- **Cause:** run:dWitnessedBar

```
# run-gates | leg spawn budget (forks per hot entrypoint) | exit 1
fork-count: calibrated — the specimen's 5 fork(s) counted exactly
fork-count: ok unattended-status · measured 45 · ceiling 47 · base 57
fork-count: ok unattended-plan-handover · measured 209 · ceiling 209 · base 1100
fork-count: RED check-unattended · measured 785 · ceiling 782 · delta +3 · base 709 — the sites the most forked subshells first traced at:
    117 tools/unattended/check-unattended.sh@b61aa8d8:5674
    69 tools/unattended/check-unattended.sh@b61aa8d8:6325
    50 tools/unattended/check-unattended.sh@b61aa8d8:6324
    44 tools/unattended/check-unattended.sh@b61aa8d8:5547
    33 tools/unattended/check-unattended.sh@b61aa8d8:5535
    31 tools/unattended/check-unattended.sh@b61aa8d8:5471
    24 tools/unattended/check-unattended.sh@b61aa8d8:5669
    18 _:44
    16 _:21
    11 tools/unattended/check-unattended.sh@b61aa8d8:5641
fork-count:   a site that grew by one can tie below these ten: run --only check-unattended --sites here and at the parent, and diff the two
fork-count: RED run-gates-1leg · measured 58 · ceiling 56 · delta +2 · base 72 — the sites the most forked subshells first traced at:
    4 tools/run-gates/run-gates.sh@db46050c:6336
    3 tools/run-gates/run-gates.sh@db46050c:514
    2 tools/run-gates/run-gates.sh@db46050c:101
    2 tools/run-gates/run-gates.sh@db46050c:515
    2 tools/run-gates/run-gates.sh@db46050c:708
    2 tools/run-gates/run-gates.sh@db46050c:1210
    2 tools/run-gates/run-gates.sh@db46050c:2724
    2 tools/run-gates/run-gates.sh@db46050c:2896
    2 tools/run-gates/run-gates.sh@db46050c:2905
    2 tools/run-gates/run-gates.sh@db46050c:3093
fork-count:   a site that grew by one can tie below these ten: run --only run-gates-1leg --sites here and at the parent, and diff the two
fork-count: RED run-gates-2leg · measured 60 · ceiling 58 · delta +2 · base 97 — the sites the most forked subshells first traced at:
    4 tools/run-gates/run-gates.sh@db46050c:6336
    3 tools/run-gates/run-gates.sh@db46050c:514
    2 tools/run-gates/run-gates.sh@db46050c:101
    2 tools/run-gates/run-gates.sh@db46050c:515
    2 tools/run-gates/run-gates.sh@db46050c:708
    2 tools/run-gates/run-gates.sh@db46050c:1210
    2 tools/run-gates/run-gates.sh@db46050c:2724
    2 tools/run-gates/run-gates.sh@db46050c:2896
    2 tools/run-gates/run-gates.sh@db46050c:2905
    2 tools/run-gates/run-gates.sh@db46050c:3093
fork-count:   a site that grew by one can tie below these ten: run --only run-gates-2leg --sites here and at the parent, and diff the two
fork-count: ok memory-hygiene · measured 192 · ceiling 192 · base 219
fork-count: ok manifest-check · measured 76 · ceiling 76 · base 108
fork-count: ok check-wiring · measured 45 · ceiling 45 · base 55
fork-count: 5 passed · 3 red · 0 skipped — a skipped row is not a pass
```
