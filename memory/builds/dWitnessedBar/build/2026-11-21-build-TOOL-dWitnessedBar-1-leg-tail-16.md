# TOOL-dWitnessedBar-1 leg-tail 16 — core meta-check failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** core meta-check
- **Hash:** c5269dcccea2378bb19df645af01f912b4defe3f
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg core meta-check | exit 1
core: registry · 42 rows against 42 principles of memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
core: pending · principle 20 · practice 27 · leg 70 · kind 4
core: red · pending practice row practice.verify is stale: it is enforced now, so delete the row (armed by dWitnessedBar)
core: red · pending leg row shell hygiene (a stage committed with no staged-diff test) is stale: it is enforced now, so delete the row (armed by dWitnessedBar)
core: meta-check · red · 42 principles, 224 legs, 17 kinds · core.bypass with-hooks-report
```
