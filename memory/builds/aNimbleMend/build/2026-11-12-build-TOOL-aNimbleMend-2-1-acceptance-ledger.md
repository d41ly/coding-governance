# Acceptance ledger — TOOL-aNimbleMend-2

**Serves:** journal TOOL-aNimbleMend-2

Built against spec rev-2 in the pass commit `d4eb74047`. Each line is a probe the builder made in the pass and returned; the main loop wrote this record from that return. The fixture repositories F and B sat under `%TEMP%` and are not tracked. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, and the new canary arm of AC8 observed RED with `pass_leg` out of the `KNOWN` literal and GREEN restored.

**Evidences:** TOOL-aNimbleMend-2
- AC1 — `GOV_NODE=f python <kit>/pass_legs.py --write` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC2 — `pass_legs.py --report` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC3 — `pass_legs.py --check` — the builder's fixture probe ran the criterion's commands in fixture B and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC4 — `pass_legs.py --check` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC5 — `pass_legs.py --apply` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC6 — `DEAD PROBE` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC7 — `GOV_NODE` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC8 — `KNOWN` — the criterion's grep printed 2; the arm itself is owed RED-first at the close. (PINNED, 2026-11-12)
- AC9 — `not derived, no evidence file` — the builder's fixture probe ran the criterion's commands in fixture F and returned that it observed the criterion as the spec states it; the return quotes no output for it.
- AC10 — `python tools/run-gates/regen.py --list` — named `pass_legs.py --apply` at stage 2 with its `--check`, and the `kit.toml` grep printed 2. (PINNED, 2026-11-12)
- AC11 — `GOV_NODE=a python tools/run-gates/pass_legs.py --write` — in this repository it read 202 bars, 117 of them red, and wrote 78 evidence rows; `--check` exited 0 with 26 legs declared at 412.8s of the 600s budget, none a self-test, an e2e leg or the unattended gate. (PINNED, 2026-11-12)
- AC12 — `tools/run-gates/README.md` — the criterion's two greps printed 8 and 2. (PINNED, 2026-11-12)
