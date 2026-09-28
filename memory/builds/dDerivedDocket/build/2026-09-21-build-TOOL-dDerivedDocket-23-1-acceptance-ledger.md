# TOOL-dDerivedDocket-23 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-23

A red bar leg is now attributed, report-only: `GATE_ATTRIBUTE=<R>` re-runs each red leg alone at R
from a detached worktree and prints a `GATE attr` line per red leg plus an `attribution` record, and
no exit code moves. The normaliser and the worktree runner are one sourced kit file both runners
load only on the path that attributes; the pre-push hook exports the remote sha it reads; the four
signature legs gained an `--offenders` mode each. No merge bar, no gate leg and no `*.test.sh` suite
ran in this pass. What ran instead, from the scratch root outside the tree:

- the runner over a two-commit fixture carrying a leg per classifier branch: every verdict read as
  the spec's rules say, the exit stayed 1, the R worktree was gone afterwards, and the record held
  one six-column row per red leg with the full R sha; the same fixture read every red OWN under a
  touch to its runner, every red DEAD PROBE against a rev that does not resolve, and MIXED 0/2 once L
  fixed R's offender and added two. A second fixture under an 8 s wall read its R run DEAD PROBE
  `cut by the wall` and returned near the wall rather than after the 60 s R sleep.
- the canary's new section 7, extracted with the canary's own variables set and its signature loop
  pointed at a scratch manifest: 37 assertions, green, over the final runner. The AC12 block as it
  landed, with the shipped staged break the checklist fold added, driven alone over three staged
  signatures: green on a well-shaped one, RED on a `--list` sibling that prints keys, and RED on a
  signature that prints a line locator.
- the edited pre-push hook driven directly with a hand-fed stdin line: the runner saw the remote sha,
  the hook exited the runner's 3, and an all-zero remote sha exported nothing.
- the lifted normaliser against the inline one it replaced, extracted from HEAD: the same sed program
  byte for byte, over a Windows root with a space and a POSIX root.
- each `--offenders` mode over its own suite's fixture: the exact key set, the ordinal on a repeat,
  keys unmoved by an unrelated insertion, no cut past 40, and the default mode's output and exit
  byte-identical to the pre-change checker's over the same fixture (lexicon against BASE, hygiene
  and install-prefix against HEAD's copy). The drift report's default and `--check` runs match
  HEAD's copy in exit and in every line but one: `source_cited_ids_resolving_to_no_record`, a
  report-only signal, counts 23 cited ids where HEAD's copy counts 22, because the fixture carries
  the kit's own source and the new function's docstring cites this unit's id.

Every criterion carries a `permission:` line deferring its observation to the build's post-build
bar, `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, so none gets a line here; the
orchestrator writes each after that run. The owed legs are `run-gates canary`, `run-gates gov
canary`, `pre-push self-test`, `run-selftests self-test`, `lexicon selftest`, `install-prefix
self-test`, `drift-audit selftest` and `memory-hygiene self-test`, plus the plain legs the section 7
list names.

**Evidences:** TOOL-dDerivedDocket-23
- AC1 — `GATE_ATTRIBUTE` — at 364278a8 `run-gates canary` exited 0 with `PASS (266 assertions)`
  and no SKIP line. Its section 7 drives the real runner under `GATE_ATTRIBUTE=HEAD` over a
  two-commit fixture and asserts leg `sig off` reads `MIXED · inherited 1 · own 1`, then
  `MIXED · inherited 0 · own 2` once L fixed R's offender and added two others.
- AC2 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no SKIP line. Section 7 asserts
  leg `cmpself`, red at R as at L and with its checker `fx14/c.sh` edited on the branch, reads
  `OWN · the diff against R touches its comparator: fx14/c.sh`.
- AC3 — `<git-dir>/gate-run/<id>/attribution` — at 364278a8 `run-gates canary` exited 0 with
  `PASS (266 assertions)` and no SKIP line. Section 7 asserts leg `absent` reads
  `DEAD PROBE · R's argv file`, leg `empty`, empty at L with exit 1, reads `DEAD PROBE`, a one-leg
  manifest whose argv file R lacks prints `attributed 0 of 1 red legs`, and the `attribution` file
  holds one nine-column TAB row per red leg, each with a known verdict and the full R sha in
  column five.
- AC4 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no SKIP line. Section 7 asserts
  signature-less leg `same`, byte-identical at R and L, reads `INHERITED · offenders 1`, and leg
  `gained`, whose L output adds one line under an unchanged `FAIL x`, reads `MIXED`.
- AC5 — `tools/run-gates/run-gates.sh` — at 364278a8 `run-gates canary` exited 0 with
  `PASS (266 assertions)` and no SKIP line. Section 7 appends a comment to the fixture's copy of
  the runner and asserts leg `same`, identical at both ends, then reads `OWN · KF3`.
- AC6 — `tools/gate-legs.json` — at 364278a8 it declares `signature` on 4 of its 122 rows, the
  four S3 legs: `drift-audit records`, `install-prefix (shipped surface)`,
  `lexicon naming predicates` and `memory hygiene`. `run-gates canary` (exit 0,
  `PASS (266 assertions)`) holds the key-set control that passes a `signature` row and reds a
  `signatur` near-miss, and `run-gates gov canary` (exit 0, `PASS (17 assertions)`) holds G1b,
  the four-leg pin.
- AC7 — `pre-push self-test` — at 364278a8 the leg exited 0, `pre-push.test: all cases ok`, with
  `9 the runner is handed GATE_ATTRIBUTE = the remote sha fed on stdin`,
  `9 the hook's exit is the runner's (3)` and
  `9b an all-zero remote sha exports no GATE_ATTRIBUTE` each `ok`.
- AC8 — `run-selftests self-test` — at 364278a8 the leg exited 0 with `PASS (139 arms, width 1)`,
  every arm `ok`, the 27 of its `--attribute` block among them. `git show 53a7a067` shows this
  unit's one change to `tools/run-gates/run-selftests.test.sh` is four lines in `build_repo`
  copying `lib-attribute.sh`, no arm edited. At 364278a8 `run-selftests.sh` defines no
  normaliser: it makes one `write_normaliser` call, and that function is defined in
  `lib-attribute.sh`.
- AC9 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no SKIP line. Section 7 replays
  a `lexicon naming predicates` leg from measured pairs: `TOOL-aStagedLane-6`'s landing pair, R at
  461/1045 and green, L at 467/1059, reads `OWN · green at R`; the branch point, 463 at both ends,
  reads `INHERITED`; dCarriedReceipt's R at 382 under a pin of 384 and green, L at 429, reads
  `OWN · green at R`.
- AC10 — `signature` — at 364278a8 `run-gates canary` exited 0 with `PASS (266 assertions)` and
  no SKIP line. Section 7 asserts legs `sig c` and `sig f`, whose L manifest points `signature` at
  a constant line and at a filtering wrapper, both read `MIXED · inherited 1 · own 1`; leg
  `lonelysig`, whose `signature` only L declares, reads `INHERITED · offenders 2` by the byte
  rule; and leg `argvd` reads `OWN · its argv differs`.
- AC11 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no SKIP line. Section 7 asserts
  leg `cmp`, whose helper `fx8/helper.txt` the branch edited, and leg `rootconf`, whose root conf
  `rootconf.txt` its checker names, each read
  `OWN · the diff against R touches its comparator:` naming that file.
- AC12 — `signature` — at 364278a8 `run-gates canary` exited 0 with `PASS (266 assertions)` and
  no SKIP line. Section 7 ran each of the 4 declared `signature` argvs on that tree through its
  shape predicate (a TAB on every line, no `:<digits>:` locator, no bare count, colon-ended header
  or `… and` line) with no red, and ran a declared signature's own `--list` sibling there, whose
  real output the same predicate reded.
- AC13 — `lexicon.py --offenders` — read at 53a7a067 against its parent 37ef8940, from scratch
  copies of each commit's checker, over the fixtures each checker's own suite builds: lexicon's
  `OFF_FILES` under `BASE_CONF`, and install-prefix's README line carrying two root spellings plus
  its ROSE carried-prefix repo. At 53a7a067 `--offenders` printed exactly the known sets, four
  lexicon keys, `frobnicate_a#2` among them, and two install-prefix keys, one ending `#2`, and
  printed them unchanged after an unrelated function or line and an unrelated tracked file landed
  above. Each checker's default run over the same fixtures gave stdout, stderr and exit
  byte-identical by `cmp` at the build commit and its parent: lexicon 1525 and 1526 bytes,
  install-prefix 606, 606 and 1210, every exit 1. The parent's lexicon.py answers `--offenders`
  with its usage and exit 2, so it is the pre-change checker. Lexicon's default output also matched
  BASE fb07ca25's, and `check-install-prefix.sh` is one blob at BASE and the parent. The runner
  half is the `run-gates canary` leg record of bar run 20260928T034330Z at 364278a8: exit 0,
  `PASS (266 assertions)`, no `canary:` failure line, so its `siginh` arm held, which wants
  `INHERITED · offenders 1` after an unrelated line and an unrelated tracked file.
- AC14 — `GATE_ATTRIBUTE` — at 364278a8 `run-gates canary` exited 0 with `PASS (266 assertions)`
  and no SKIP line, so its `timeout -k` arms ran. Section 7 asserts `timed` (rc 124, bound 2)
  reads `CONTENDED · timed out after 2s; not re-run at R`, `stubborn` (rc 137 under bound 1 after
  an ignored TERM) `CONTENDED · killed after`, `kill0` (rc 137, bound 0) `INHERITED`, `argvd`
  `OWN · its argv differs`, `newrow` `OWN · no row in R's manifest`, `greenr` `OWN · green at R`,
  `rslow` `DEAD PROBE · R's run hit its 3s ceiling` and `siginh` `INHERITED · offenders 1`. Under
  `GATE_ATTRIBUTE=no-such-rev`, leg `same` reads `DEAD PROBE · R 'no-such-rev' does not resolve`
  and the summary names that R.
- AC15 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no SKIP line. Section 7 runs an
  R copy that sleeps 120 s under `GATE_WALL=8` and asserts leg `walled` reads
  `DEAD PROBE · cut by the wall`, the summary reads `attributed 0 of 1 red legs` with
  `DEAD PROBE 1`, and the runner exits 1 in under 100 s, the margin it grades against the sleep.
