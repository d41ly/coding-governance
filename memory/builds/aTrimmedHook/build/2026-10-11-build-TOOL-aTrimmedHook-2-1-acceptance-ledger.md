# TOOL-aTrimmedHook-2 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-2

No merge bar and no self-test suite ran in this pass. The new arms were observed through slices of
`tools/memory-tree/check-memory-hygiene.test.sh` kept inside the kit directory and deleted after
each run. A slice of the whole suite up to the existing `--staged` block plus the new block, run
against this pass's gate, printed `PASS (209 assertions)`. A second slice of the fixture prologue and
the new block ran it three times. Against the pre-unit gate the six negative halves failed, so each
can see the whole-tree grading this unit removes. Against a copy with each guard inverted, the four
positive halves failed. Against this pass's gate all ten held. The first draft of the new-name arm
passed against the inverted copy because check 9's own reason names a staged added file. It now
reads check 5's message, and that is how its RED was observed. The pass also changes one fixture
literal in `tools/memory-tree/gen_build_index.py`: the install-prefix ban refused a kit path spelled
in TOOL-aTrimmedHook-1's arm, and the arm still holds. The close owes the whole
`memory-hygiene self-test` leg.

**Evidences:** TOOL-aTrimmedHook-2
- AC1 — `check-memory-hygiene.sh --staged` — with one tracked `RUN.md` line staged it printed the
  narrowing line, `--staged grades the staged files and their own build folders`.
- AC2 — `check-memory-hygiene.sh --staged` — staging a NEW `badly-named.md` under a spec folder
  reported check 5 for it; an edit-only stage printed the S3 line and no check 1, 3, 4 or 5 finding,
  and the pre-unit gate reported a committed name there, observed RED.
- AC3 — `check-memory-hygiene.sh --staged` — a staged relative link to a missing `.md` target reported check 2;
  with the staged selection emptied it was missed, observed RED.
- AC4 — `check-memory-hygiene.sh --staged` — the five existing staged arms, run against this pass's
  gate through a slice, still saw check 7 on a staged
  over-cap index file and none on a staged spec, through the S5 guard.
- AC5 — `check-memory-hygiene.sh --staged` — a staged edit to an unreferenced archive reported it
  under check 10 over the whole listing; with nothing of that kind staged the HELD line printed and
  the archive went unreported, and the pre-unit gate reported it there, observed RED.
- AC6 — `check-memory-hygiene.sh --staged` — a staged `legacy-files.txt` naming
  `memory/project/gone-forever.md` reported the stale-line guard; unstaged, the HELD line printed.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` — run with no argument on the base tree, the
  pre-unit gate and this pass's gate printed identical output, 26 lines each, before and after the
  empty-input guards on the check 6 and check 7 selections were added.
- AC8 — `bash -x` — the base profile instrument, one staged `RUN.md` line, 14.6 s traced at 30 to 33
  host bash processes: no line of S2, S3, S5, S6, S7, S8 or S9 cost a process. A first profile still
  built the index set, because the index-kind pattern matched the LIVE `RUN.md`; it now matches only
  a retired run-state record, as `index_set` does.
