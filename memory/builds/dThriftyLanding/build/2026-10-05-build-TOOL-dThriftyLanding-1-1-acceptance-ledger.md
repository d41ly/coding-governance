# Acceptance ledger — TOOL-dThriftyLanding-1

**Serves:** journal TOOL-dThriftyLanding-1

Built on base `58509c21`. The arms are section 3i2 of the canary, plus arm 1a's `doc_reads` control
and arm 1b's widened tracked-path rule. A slice of the canary holding its prologue, section 3's
fixture setup and those arms ran against the new runner (13 assertions, PASS) and against the base
runner swapped in (5 failures named below, FAIL). A mutation reading only the net diff redded AC4.

**Evidences:** TOOL-dThriftyLanding-1
- AC1 — `GATE skip  reads b only  (docs-only: no path it reads moved)` — printed; `reads notes` ran; the summary read `2/2 legs passed (2 skipped)`; the base runner ran all four
- AC2 — `doc_reads: []` — leg `reads none`, a declared empty list printed `GATE skip`; the undeclared leg printed `GATE ok`; the base runner ran both
- AC3 — `GATE ok` — printed by every leg with the full-bar flag beside the docs base; the run read 4/4 passed
- AC4 — `GATE ok    reads b only` — after notes/b.md was changed and restored inside the range; the net-diff-only mutation printed `GATE skip` instead
- AC5 — `gate-full-green` — absent after a docs run in the fixture, written by the plain run that followed; the base runner stamped the docs run
- AC6 — `doc_reads` — arm 1a passes a row carrying it and fails `doc_read`; arm 1b now grades `doc_reads` elements against `git ls-files` as it grades guards
- AC7 — `1.25` — `KIT_RUN_GATES_VERSION=1.25`; the `kit version markers` leg is owed to the close's bar
