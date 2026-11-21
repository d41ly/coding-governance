# TOOL-dWitnessedBar-1 leg-tail 6 — portability (shell lines only shrink) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** portability (shell lines only shrink)
- **Hash:** 0c98c706322ad92a0e243b41240a4543740477fb
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** 079d8513ce2ba90ffd4755b9b8677ab9b4bba1ee
- **Cause:** run:dWitnessedBar

```
# run-gates | leg portability (shell lines only shrink) | exit 1
sh-hygiene: shell role — 151 tracked shell source(s), 120505 code line(s)
sh-hygiene: 20 shell-role finding(s).
  .githooks/pre-push: 1800 code line(s), above its row's 1799 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  .githooks/pre-push.test.sh: 2459 code line(s), above its row's 2417 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  skills/session-kickoff/card-store.fixture.sh: a shell file of 346 code line(s) with no row — logic belongs in Python, and a shim earns its lines through the ledger's widen route
  skills/session-kickoff/manifest-check.sh: 1933 code line(s), above its row's 1449 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  skills/session-kickoff/manifest-check.test.sh: 1771 code line(s), above its row's 1652 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/hooks/format-guard.test.sh: 598 code line(s), above its row's 593 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/hooks/scratch-guard.test.sh: 1353 code line(s), above its row's 1284 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/lib/gov-feed.sh: a shell file of 296 code line(s) with no row — logic belongs in Python, and a shim earns its lines through the ledger's widen route
  tools/lib/gov-ref.sh: a shell file of 48 code line(s) with no row — logic belongs in Python, and a shim earns its lines through the ledger's widen route
  tools/lib/resolve-python.test.sh: 1557 code line(s), above its row's 1420 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/push-main.sh: 1469 code line(s), above its row's 1089 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/push-main.test.sh: 1685 code line(s), above its row's 1356 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/run-gates/post-merge.sh: 622 code line(s), above its row's 309 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/run-gates/run-gates.evidence.test.sh: 2459 code line(s), above its row's 2452 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/run-gates/run-selftests.sh: 1542 code line(s), above its row's 1480 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/run-gates/run-selftests.test.sh: 1003 code line(s), above its row's 980 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/unattended/lib-unattended.sh: 1331 code line(s), above its row's 1319 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/unattended/unattended.sh: 11453 code line(s), above its row's 9793 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/unattended/unattended.test.sh: 16420 code line(s), above its row's 13973 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
  tools/workflows/check-verifier-fanout.test.sh: 1443 code line(s), above its row's 1442 — shell outside a shim only shrinks; move the logic to Python, or widen the row through the ledger
```
