# Acceptance ledger — DEPL-aHalvedInstall-4

**Serves:** journal DEPL-aHalvedInstall-4

Built at `7609570d`. The arms run twice in `check_update_safety` in `tools/govkit/selftest.py`, once
for a kit declaring `[check] none` and once for a kit whose check stays green, each over a fixture
with one conflicting row, one clean row and a regenerate. Run as a slice of that function. With the
held set staged never to fill, the restore, decline and order arms went RED and the liveness and
conflict-order controls stayed green.

**Evidences:** DEPL-aHalvedInstall-4
- AC1 — `update` — `[aHI-4 ha AC1/AC3]`: `plain.txt` back to `a\nb\n`, its receipt row's commit back at A, and `HELD BACK demo: 1 row(s) refused`
- AC2 — `DECLINED` — `DECLINED demo: a row of this kit was refused this run` names `conf.sh`, and `docs/out.md` stays `v1`
- AC3 — `[check]` — `[aHI-4 hg AC1/AC3]` passes with a check that exits 0 throughout
- AC4 — `update-rollback-demo.md` — carries `was HELD BACK`, `REFUSED` with the conflicting path, and `restored` with the clean one
- AC5 — `.governance/outbox` — `update-conflict-<slug>.md` and its `candidate` file exist after the held run
- AC6 — `python tools/govkit/govkit.py epoch` — `--base cd90f7fa` prints no `FAILED` line at `1bfa4d01`
- AC7 — `hook.fragment.json` — `[aHI-4 ha|hg|hz AC7]`: named `landed UNWIRED — its kit is HELD BACK` at its old bytes; all three red with the held union staged away of `_fr_skip`. The merge honouring that set is the fragment-wiring arm's `a kit in the skip set is not wired`
- AC8 — `HELD BACK` — the `hz` variant puts the refused row `zz-conf.sh` last; its AC1, AC2 and AC4 arms red with the compare after the write loop staged away, while `ha` and `hg` stay green (`8658fc59`)
