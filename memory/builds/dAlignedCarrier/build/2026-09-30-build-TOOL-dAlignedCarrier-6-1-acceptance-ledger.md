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
own scanners, extracted from the checker and run alone; the same no-suite rule held.

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
  `3c45a567` prints 1.
