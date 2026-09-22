# cMendedVintage — the acceptance ledger for unit 9

**Serves:** journal TOOL-cMendedVintage-9

*Node `c`, 2026-09-16, written by the pass that built the unit. Every line below was taken against the
real `skills/session-kickoff/manifest-check.sh` in the unit's own worktree, never a copy with a
simplified read. No merge bar and no `*.test.sh` suite ran in this pass; the two arms S4 adds were
exercised by replaying their exact commands at the shell, which is stated per criterion below.*

## The one thing worth reading twice

The fix was also observed FAILING. The `CARD_SID` term was removed from the real script with `sed`,
the held-open-stdin arm was replayed against the broken file, and it returned 124 at its bound after
ten seconds; the file was then restored from a byte copy taken before the break. A guard nobody has
seen red is an assertion about nothing, and on this unit the red case is the entire point — an arm
that runs the verb with stdin already closed passes today, before any fix.

**Evidences:** TOOL-cMendedVintage-9

- AC1 — `probe-ac1.md` — the spec's command was run verbatim from the repo root. Exit 0, wall 30 s
  (the pipeline waits on its own `sleep`, not on the verb), and stdout was the path ending
  `probe-ac1.md`. The pre-fix behaviour is `timeout` returning 124 at ten seconds.
- AC2 — `probe-ac2.md` — the hook channel with no `--session`: exit 0, stdout the path ending
  `probe-ac2.md`. The new guard does not fire for a caller that passed no flag, so the SessionStart
  hook keeps its reader.
- AC3 — `bash skills/session-kickoff/manifest-check.sh --card --path </dev/null` — exit 2, and the
  message printed was the unchanged two-channel refusal naming both the JSON on stdin and
  `--session <sid>`.
- AC4 — `flagside.md` — both channels supplied at once: stdout was the path ending `flagside.md`, so
  the flag beats the hook's JSON and the implemented precedence is the declared one.
- AC5 — `read_session_id` — the comment block above it now opens on the precedence and says
  `--session` answers first and SUPPRESSES the stdin read, names the never-closing pipe as the case
  `[ -t 0 ]` cannot see, and records the supersession of `KICK-aReplayedCard-1` §S2.
- AC6 — `bash tools/check-testsuite-counts.sh` — exit 0 and silent, which is that leg's documented
  pass shape. The floor moved 174 at base `859daa67` to 176 at the tip, read from the file at both
  ends with `git show`; 176 is 174 plus S4's two arms.

## What this ledger does NOT claim

The two S4 arms have not been observed as part of a suite RUN — `manifest-check.test.sh` is a
`*.test.sh` and no suite ran in this pass. What was observed is their exact command sequence,
replayed at the shell with the same fifo holder, the same `timeout` bounds and the same predicates,
green against the real script and red against the staged break. The suite-level run is owed to the
bar the closing pass executes, and `manifest-check self-test` is the leg that owes it.
