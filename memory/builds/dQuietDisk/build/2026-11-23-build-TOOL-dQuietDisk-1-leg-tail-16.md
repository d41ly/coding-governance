# TOOL-dQuietDisk-1 leg-tail 16 — run-gates gov canary failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** run-gates gov canary
- **Hash:** adfc34f94cd7b167523bf02799d216219c0ed91b
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg run-gates gov canary | exit 1
gov-canary: SKIP the recorded-green lag arm — no gate-full-green in this git dir yet, so there is no record to measure. The boundary forces a total run in exactly this state.
gov-canary: map/features/gate-lint.md claims leg 'portability (the interpreter floor, run for real)', whose tests does not name feature.gate-lint
gov-canary: leg 'portability (a bare shell name launched)' carries tests feature.run-gates, and map/features/run-gates.md does not claim it
gov-canary: map/features/gate-lint.md claims leg 'portability (a bare shell name launched)', whose tests does not name feature.gate-lint
py-reads: selftest · 12 of 12 plants held
gov-canary: bar-scrub parity read BAR_SCRUBBED_KNOBS 6 · BAR_CLEARED_KNOBS 8 · PM_SCRUB 30 (GIT_DIR … GATE_REUSE_DAY) · _gknobs 14
gov-canary: FAIL (81 assertions)
```
