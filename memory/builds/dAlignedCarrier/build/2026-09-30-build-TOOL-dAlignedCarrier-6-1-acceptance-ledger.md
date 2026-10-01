# TOOL-dAlignedCarrier-6 — acceptance ledger

**Serves:** journal TOOL-dAlignedCarrier-6

The owed flagged-bar notice left `--close`: `print_selftests_owed` reads the run's range from the
pinned `base` fact, `verb_phase` calls it on a move into VERIFYING and `print_resume_orientation`
at VERIFYING, under every `LANDER_MODE`, and the Skill, the protocol row and both conf comments say
the main loop exports the flag into its one `--close`. A 31-check scratch fixture under `%TEMP%`
run against the built driver and the BASE driver from `git archive 87c245b3`, the greps, `cmp`, the
size check, the adopter's `--check` and the manifest's `--staged` check stood in for the `unattended
kit gate`, `unattended skill wiring`, `unattended protocol size` and `kickoff-manifest ratchet` legs.
No suite ran: the new suite arms are written and their run is not observed here, under the build
README's waiver. The rev-4 fold of the closing review's round 1 added AC9 to AC12, observed by a
39-check scratch fixture over the folded driver (39 green) and the driver at 3c45a567 (16 FAIL lines,
each on an arm the fold moves), and by the kit gate scoped to skip check 28, red on a staged break
with no other check red. Over the final tree the scoped leg did not return inside its 590 s bound and
was stopped with no check failed up to check 23, so the tree-side reading of checks 47 and 48 is their
own scanners, extracted from the checker and run alone; the same no-suite rule held. The rev-5 fold
of round 2 added AC13 to AC16, observed by the map's own test and freshness check, a 47-check scratch
fixture over the folded driver (47 green) and the driver at e01f2ad9 (4 FAIL lines, each on an arm
rev-5 adds), a failed-diff probe over the folded driver and a copy with its `pipefail` removed, and
check 47's scanner, extracted verbatim, over a staged break holding each row's widest instance at
every wrap position. They stood in for the `codebase-map coverage + freshness` and `unattended kit
gate` legs. The kit gate itself, scoped to skip check 28 over that staged break, did not return
inside its 590 s bound, was stopped in check 23 with no check failed, and was not re-run, so check
47's reading is its extracted scanner. The two new suite arms are written and not run, under the
waiver; the tab-path arm's reset shape was run alone over a scratch commit and left a clean tree.

**Evidences:** TOOL-dAlignedCarrier-6
- AC1 — `the run's range e7779aa9..HEAD touches a declared self-test surface (kitsurface/)` — the
  move `--phase tRun VERIFYING` over a commit touching `kitsurface/thing.txt` printed that owed line
  ending `export GATE_SELFTESTS=1 into this run's one --close` and exited 0, under `primary` and
  under `in-place`. The BASE driver printed only `phase VERIFYING · witness` over the same fixture.
- AC2 — `no range here can ever owe the flagged bar and no phase move will announce one` — printed
  with `SELFTESTS_OWED_PATHS=""`; a commit touching only `other/` printed no owed line; with the
  `base` line deleted the move printed `the record pins no base`, and with an unresolvable base
  `the record's base 01234567 does not resolve in this clone`. BASE printed none of the three.
- AC3 — `unattended: resume at phase VERIFYING` — the holder's `--resume tRun --keepalive-id k1`,
  run with the session and pid the record names, printed its orientation on lines 3 to 5 and the
  owed line on line 6; a move into BUILDING over the touching range printed no owed line. BASE's
  resume printed the orientation and no owed line.
- AC4 — `4227:  [ "$want" = VERIFYING ] && print_selftests_owed "$rel"` — the grep printed that,
  `6190:` in `print_resume_orientation` and the `7098:` definition; BASE printed `7035:` and the
  `7422:` call in `gates-green`. The `GATE_SELFTESTS=` grep printed nothing on both. The fixture's
  in-place close reached LANDING with no owed line, its bar reading `GATE_SELFTESTS=<unset>` and
  `GATE_SELFTESTS=1` when exported.
- AC5 — `in sync (skill rendered from template + .unattended.conf)` — the adopter's `--check`
  exited 0. The `nowhere earlier|by hand at` count printed 0 against BASE's 2, the Close-section
  `--phase <slug> VERIFYING` count 1 against 0, and the While-it-runs `close ANNOUNCES` count 0
  against 1. In `## Close` the move sits on line 10, `--prepare` on 25 and the one exported close on 48.
- AC6 — `template-size OK — UNATTENDED-PROTOCOL.md: 65288 / 65692 bytes` — the row grep printed
  one row naming `VERIFYING` and `--close`, `cmp` of the template and its render exited 0, and
  `wc -c` read 65171 before the pass and 65288 after, 117 bytes.
- AC7 — `SELFTESTS_OWED_PATHS="tools/"` — both `sed` blocks end on their BASE value lines, name
  the move into VERIFYING and never say the close announces; `manifest-check.sh --staged` exited 0
  over the staged pass carrying the `last-audit` re-stamp.
- AC8 — `4` — `grep -c -E -- '--phase [A-Za-z]+ VERIFYING'` over the suite printed 4 where BASE
  prints 0, and `git diff -U0` over the suite shows no line of the unset-flag or pass-through arms.
  The fixture's MIRROR section ran the new arms' steps in-place and passed 10 of 10.
- AC9 — `UNATTENDED check 48 FAILED` — `bash tools/unattended/check-unattended.sh --skip 28`, run
  with `verb_phase`'s staging moved back between its two writes, printed it naming
  `tools/unattended/unattended.sh:4220 verb_phase` beside the report line `check 48 graded 602
  function(s) in 23 shell file(s)`, and no other check failed; over the final tree check 48's own
  scanner, extracted from the checker and run alone, named no hit where it names `verb_phase` at
  `3c45a567`, and the whole scoped leg did not return inside its bound. In the rev-4 scratch
  fixture, BUILDING, a commit of what it staged, then VERIFYING left `git diff --name-only` empty,
  the staged-only commit left a clean porcelain with the move's own witness committed, and a second
  move with a changed witness left nothing unstaged; the driver at `3c45a567` failed all four
  readings with `memory/builds/tRun/RUN.md` unstaged.
- AC10 — `3c45a567` — the driver at that sha printed an export whose `primary` close left the bar's
  `GATE_FULL` unset and whose `in-place` close was refused by check 62 on the half-staged record; the
  folded driver's notice printed the pair, and applied as printed to `--close` with both names unset
  beforehand it reached the bar stub's recorded environment with both flags at 1 under `primary` and
  under `in-place`, in the fixture's own section and in its mirror of the written suite arm. `wc -c`
  read 65288 before the fold and 65310 after, 22 bytes of the 300.
- AC11 — `git mv kitsurface/thing.txt moved-out.txt` — as the fixture's only commit after the
  preflight, the move into VERIFYING printed the owed line naming `kitsurface/`, where the driver at
  `3c45a567` printed none; a rename into the prefix announced and a rename between undeclared paths
  did not. `python tools/memory-tree/gotchas.py --check` exited 0 with the class record added.
- AC12 — `UNATTENDED check 47 FAILED` — the same staged run, with the line
  `# the in-place close announces the owed bar` appended to the driver, printed the second row's
  message with `matches: tools/unattended/unattended.sh: "in-place close announ"`; over the final
  tree both rows' patterns, through the checker's own scanner run alone, named nothing.
  `grep -c 'in-place close derives' tools/unattended/check-unattended.sh` printed 0, where
  `3c45a567` prints 1. That quoted excerpt was one letter short, round 2's L4; since rev-5 the
  same staged line reports `"in-place close announces"`, through the extracted scanner.
- AC13 — `test_generated_artifacts_are_fresh` — after the `unattended` dossier claimed the
  round-1 class record and `gen_map.py --write` ran, `test_codebase_map.py` printed six `ok` lines
  and `gen_map.py --check` exited 0. Before the fix the same test printed
  `FAIL test_generated_artifacts_are_fresh`, and `--check` exited 1 naming `inventories.json` and
  `MAP.md`.
- AC14 — `this driver never sets GATE_SELFTESTS` — the fixture's move into VERIFYING under
  `primary` printed the owed line ending with it, where the e01f2ad9 driver's ended
  `this driver sets neither`. The retired-claim grep printed 0 in each of the five carriers, where
  e01f2ad9 prints 2 in the driver and 1 in each of the other four. The "While it runs" bullet's
  closing sentence names `GATE_FULL=1 GATE_SELFTESTS=1`, and the adopter's `--check` printed
  `in sync`.
- AC15 — `"in-place p q close r s t announces"` — check 47's scanner and rows, extracted verbatim,
  reported that whole excerpt 7 times over the staged break and row 1's `"no p q verb r s commits"`
  6 times. The scanner at `e01f2ad9` reported row 2 six times, each excerpt ending `t announ"`, one
  letter short. Over the kit's 49 tracked files neither row named anything at seven words, as at six,
  and the near-miss sweeps named only true sentences, the Skill's "The close announces nothing
  itself" among them.
- AC16 — `touches a declared self-test surface (kitsurface/)` — the folded driver's move printed it
  when the fixture's only commit after the preflight added a file under `kitsurface/` whose name
  holds a tab, through `update-index --index-info` with `core.protectNTFS=false`. The e01f2ad9
  driver printed no owed line there, while `-c core.quotepath=off diff --name-only` printed that
  path C-quoted, a leading double quote and a `\t` escape. The same path under `other/` printed
  nothing. A `git` stub failing
  `diff --name-only` made the folded driver print `could not be diffed`, and a copy with its
  `pipefail` removed printed only its phase line. The e01f2ad9 driver printed `could not be diffed`
  too, having no pipe.
