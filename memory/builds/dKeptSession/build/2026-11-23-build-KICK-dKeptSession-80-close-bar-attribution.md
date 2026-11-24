**Serves:** research KICK-dKeptSession-80

# dKeptSession — the close's first full bar and its reds attributed against origin/main

The full merge bar, `GATE_FULL=1 bash tools/run-gates/run-gates.sh` with no `GATE_SELFTESTS` (held for the owner's opt-in), ran at `0a39514a6` on node d, 2026-11-23.

## The bar's verdict lines (DERIVED, that run's log)

```text
GATE FAIL  lexicon wiring  (exit 1)
---- chunk wiring: RED  (12 ran, 1 failed, 0 skipped, 0 reused, 1 held)
GATE FAIL  lexicon naming predicates  (exit 1)
GATE FAIL  policy check  (exit 1)
GATE FAIL  remote literals (kit code names no remote)  (exit 1)
GATE FAIL  layer dependencies (the core never depends on an expansion)  (exit 1)
GATE FAIL  python reads (a name never bound, an import outside its guard)  (exit 1)
GATE FAIL  ratchet (never gains)  (exit 1)
---- chunk declarations: RED  (71 ran, 6 failed, 0 skipped, 0 reused, 1 held)
GATE FAIL  shell hygiene (a location probe asked from a moved directory)  (exit 1)
GATE FAIL  shell hygiene (a fork spent on builtin work)  (exit 1)
GATE FAIL  shell hygiene (a fixed-name temp renamed into place)  (exit 1)
GATE FAIL  shell hygiene (a stage committed with no staged-diff test)  (exit 1)
GATE FAIL  encoding posture (JavaScript text IO names its encoding)  (exit 1)
GATE FAIL  shell hygiene (a quoting hazard)  (exit 1)
GATE FAIL  portability (shell lines only shrink)  (exit 1)
---- chunk product: RED  (31 ran, 7 failed, 0 skipped, 0 reused, 0 held)
---- chunk selftests: skipped  (0 ran, 0 failed, 0 skipped, 0 reused, 100 held)
GATE FAIL  memory hygiene  (exit 1)
GATE FAIL  memory hygiene (the pass checks)  (exit 1)
---- chunk records: RED  (5 ran, 2 failed, 0 skipped, 0 reused, 0 held)
---- chunk e2e: skipped  (0 ran, 0 failed, 0 skipped, 0 reused, 3 held)
gates RED — 16/119 legs failed (105 held: 105 kit; GATE_SELFTESTS=1 runs the kit ones) (1 retried after timeout) (186 warned)
```

## Each red leg run as-is in this tree and in a worktree at origin/main 525f3ab97 (DERIVED, each leg's manifest argv in both trees)

`lines-only-in-run` counts finding lines this tree prints and origin/main does not, line numbers and shas normalised. Legs 03, 14 and 15 shell out to `bash`, which the probe's Python resolved to WSL, so their two readings compare nothing.

```text
00	lexicon wiring	run=2	main=2	lines-only-in-run=0
01	lexicon naming predicates	run=1	main=0	lines-only-in-run=50
02	policy check	run=1	main=1	lines-only-in-run=20
03	remote literals (kit code names no remote)	run=2	main=2	lines-only-in-run=1
04	layer dependencies (the core never depends on an expansion)	run=1	main=0	lines-only-in-run=12
05	python reads (a name never bound, an import outside its guard)	run=1	main=0	lines-only-in-run=27
06	ratchet (never gains)	run=1	main=0	lines-only-in-run=30
07	shell hygiene (a location probe asked from a moved directory)	run=1	main=0	lines-only-in-run=9
08	shell hygiene (a fork spent on builtin work)	run=1	main=0	lines-only-in-run=18
09	shell hygiene (a fixed-name temp renamed into place)	run=1	main=0	lines-only-in-run=14
10	shell hygiene (a stage committed with no staged-diff test)	run=1	main=0	lines-only-in-run=14
11	encoding posture (JavaScript text IO names its encoding)	run=1	main=0	lines-only-in-run=3
12	shell hygiene (a quoting hazard)	run=1	main=0	lines-only-in-run=28
13	portability (shell lines only shrink)	run=1	main=0	lines-only-in-run=17
14	memory hygiene	run=2	main=2	lines-only-in-run=1
15	memory hygiene (the pass checks)	run=2	main=2	lines-only-in-run=1
```
