# TOOL-dDerivedDocket-48 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-48

The bounded runner's capture, split into two streams, plus the two helpers that read them. No merge
bar, no gate leg and no `*.test.sh` suite was run in this pass. Every arm below was exercised by
hand against a scratch copy of the driver or a scratch fixture repository, and each was observed RED
against a staged break before it was allowed to pass. AC8 carries a `permission:` line deferring its
suite run to the bar the main loop runs after the last unit is terminal, and AC3 carries one
deferring the two halves that need the driver's own verb fixture; the orchestrator writes those
lines after that run.

Five criteria moved in rev-2, which was written before the code, as the brief requires. The lines
below say which form each one takes and why.

**Evidences:** TOOL-dDerivedDocket-48
- AC1 — `run_bounded` — the function extracted from the shipped driver and sourced. A stub writing
  `ROWLINE` to stdout and `NOTICELINE` to stderr leaves `RB_STDOUT` holding the first alone,
  `RB_ERR` the second alone, and `RB_OUT` both with stdout first. With `mktemp` shadowed to fail,
  the call returns 1, keeps `run_bounded: cannot create a capture file` verbatim in `RB_OUT`,
  empties the two new values and zeroes an `RB_TOOK` seeded to 99 immediately before it. Staged
  RED, three ways: the merged redirect restored in the unbounded branch puts the stderr line in the
  row stream; the refusal branch emptying `RB_OUT` leaves a failed capture with no diagnostic; and
  the refusal branch not zeroing `RB_TOOK` leaves the seeded 99 standing.
- AC2 — `GATE_BOUND` — the two bound properties re-observed against the two-file form on node d.
  Against a 2s bound a 30s sleeper returned in 2s at status 124, and a command that backgrounds a
  30s grandchild and exits returned in 0s while the command-substitution CONTROL blocked the full
  30s — so this host reproduces the class and the arm graded something rather than nothing. The
  file form the bound rests on is unchanged; only the number of files moved.
- AC3 — `RB_OUT` — the half that does not need the driver's verb fixture. The two lines that derive
  the `--dispatch` refusal's tail are extracted from the shipped driver rather than retyped, and run
  over a stub that writes NOTHING to stdout and one line to stderr: the refusal names that stderr
  line through its `head -1` clause, not an empty string. Staged RED both ways the criterion names —
  `RB_OUT` built from stdout alone, and `RB_OUT` built by joining the two values with a separator so
  it opens on a blank line while every byte is still present. The `$WIRING_CHECK` and `$GATE_CMD`
  halves have arms and are deferred by rev-2's `permission:` line.
- AC4 — `--asks --tsv` — the real declared producer run through the extracted `run_bounded` over a
  builds-mode fixture rebuilt from unit 15's own renderers, with three asks. `RB_STDOUT` is exactly
  three `ask` lines and one `examined` line naming 3, every line leading with one of those two
  words, and
  the count read off it is 3 rather than a DEAD PROBE; the waiver line is on `RB_ERR` and never in
  the row stream. Staged RED by restoring the merged redirect in one branch: the row stream then
  carries two notice lines and the parse this build wrote would refuse a healthy producer.
- AC5 — `derive_stream_verdict` — extracted and called directly, because the helper is dark at this
  order and no caller's output can grade it. After a stub that wrote only to stderr it returns the
  wrote-only-to-stderr string carrying `read_stderr_tail`'s output; after a silent stub the DEAD
  PROBE string; on status 124 with the bound live the never-answered string. The three differ from
  each other. A fourth call made while the row stream HOLDS rows returns 1 and prints nothing.
  Staged RED by conflating the talking and dead branches, which collapses two of the three strings
  into one. The never-answered wording is drawn rather than copied, per rev-2.
- AC6 — `read_stderr_tail` — extracted and called directly. 500 stderr lines come back as 20 lines
  plus one line reading `read_stderr_tail: 480 of 500 stderr line(s) not shown`, inside 2000 bytes;
  twenty 501-byte lines, which the line pin cannot touch, come back inside 2000 bytes too; an empty
  `RB_ERR` yields nothing at all. Staged RED four ways: both cuts removed, which gives 7944 and
  10071 bytes and a drop count of 0 on a stream that dropped 480; the driver's line pin moved to 50,
  which the arms catch because they source the pins from the driver rather than retyping them; and
  one pin deleted from the driver, which the extraction arm names rather than silently falling back
  to this file's own copy.
- AC7 — `git cat-file -s` — `memory/map/features/unattended.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` are byte-equal
  and line-equal at this commit and at its parent, because this unit opens none of them. The
  criterion's pinned figure was AMENDED in rev-2 rather than re-cited: the dossier's headroom fell
  from 93 B at `fb07ca25` to 13 B at this parent, which changes no verdict here and would have
  changed one for any unit that wrote a dossier byte.
- AC8 — amended rev-2 — the criterion demanded the `ARMS_FLOORS` pair move, and it does not. The
  harness meta-gate counts `fail <n> "` call sites and this unit adds none: the capture refusal is
  an existing branch and neither new helper refuses through `fail`. Measured at 256 sites in
  `tools/unattended/unattended.sh` at this commit and 256 at its parent, so the one-sided floor
  holds unchanged and `.memory-tree.conf` left the write set. Rev-2's §9 entry logs it. The suite
  run this criterion's other half asks for is deferred by its own `permission:` line.
