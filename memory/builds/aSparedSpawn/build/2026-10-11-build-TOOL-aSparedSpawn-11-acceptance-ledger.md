# Acceptance ledger — TOOL-aSparedSpawn-11

**Serves:** journal TOOL-aSparedSpawn-11

Node `a`, 2026-10-11, bash 5.3 under MSYS, node 22, Python 3.14. The pass ran no bar, no suite, no
held leg and no slice of a suite. Every observation below drove the changed program itself over a
hand-built fixture, through the instrument committed beside this ledger,
`2026-10-11-build-TOOL-aSparedSpawn-11-direct-checks.sh`, whose three steps run the memo in a scratch
repository (`ac7`), the agent-cap runner extracted verbatim from the suite's quoted heredoc (`runner`),
and `read_one_signal` against the report subprocess (`onesignal`). `bash -n` passed on all seven
changed shell files and the instrument; `py_compile` passed on the drift-audit selftest. Every
criterion whose witness is a suite run, or one of the two history checkers over the whole tree, is
owed at VERIFYING and says so.

**Evidences:** TOOL-aSparedSpawn-11
- AC1 — `direct-checks.sh runner` — the property ran in ONE node over the tracked population and four
  hand fixtures: "population 3862 scanned, 73 denied at BASE, 0 denial(s) lost, 2 ratified" in 52 s,
  against round one's 717 s serial for the Python loop. Every one of the 73 BASE-denied payloads was
  then put through the runner's parity mode against real `node`, both hooks each: 148 verdicts, 0
  disagreements, 144 s. The suite's own summary line beside base `22efab65` on one tree is OWED at
  VERIFYING; the Python loop at base is about 3700 spawns.
- AC2 — `direct-checks.sh runner` with the exit stub staged to drop its code in a copy of the runner —
  the parity mode exited 1 with 5 disagreements, the first "DISAGREE BASE hook on ...fix/raw.js:
  in-process exit 0, node exit 2"; unstaged, 28 verdicts over 14 payloads, 5 real denies, 0
  disagreements. The same break in a scratch copy of the suite is OWED at VERIFYING.
- AC3 — `direct-checks.sh runner` with the marker strip staged to a no-op — the property exited 1:
  "73 denied at BASE, 2 denial(s) lost, 0 ratified". The suite-copy form is OWED at VERIFYING.
- AC4 — `direct-checks.sh onesignal` — over a hand-built repository the derived map named 27 signals
  for 27 entries of `SIGNALS`, and all 27 in-process records equalled `report()` over their own
  fields. One `report()` took 14.2 s and the 27 reads 124.9 s, 4.6 s a read. The suite arm
  `test_one_signal_matches_report`, its clean and violating fixtures, and the 72 call sites converted
  to `read_one_signal` are OWED at VERIFYING.
- AC5 — `git grep -nE` for a bracketed run of two signal-shaped names over `selftest.py` — two hits,
  both pre-existing tuples inside arms that assert those signals by name (the lexicon pair at the
  lexicon arm, `_ASK_SIGNALS` at the ask-signal arm); no name map exists, the map is
  `SIGNAL_ORDER`, filled from `report()`'s order. `CHECK_FLOOR` rose 478 to 482, COUNTED off the
  arm; the executed count is OWED at VERIFYING.
- AC6 — `check-hook-destinations.test.sh` — OWED at VERIFYING, with the staged reset removal. Read in
  the diff: one `scratch` builds the tree once and resets it per arm to the recorded fixture commit,
  all nine `d=$(scratch)` calls are bare `scratch`, and no arm deletes the shared tree.
- AC7 — `direct-checks.sh ac7` — "u=WANT,WANT m=WANT,WANT other= capped=WANT walks undeclared=2
  declared=3": two declared calls over one range walked once, the other range and the capped
  newest-first window walked their own, and every answer equalled the undeclared one. With the key
  staged to omit the range in a copy of the library the third call answered from the memo
  (`other=WANT`, `declared=2`) and the step redded. The suite arm in `check-unattended.test.sh`,
  counting through the same PATH stub, is OWED at VERIFYING.
- AC8 — `check-pass-order.sh` and `check-brief-recorded.sh` at base and after — OWED at VERIFYING.
  Each is a whole leg over the tree, 576 s and 490 s in round one, so neither ran in the pass.
- AC9 — `manifest-check.sh --card --write` over a hand-built repository, a logging `claude` stub first
  on PATH — with `AI_AGENT` unset the log stayed absent; with `AI_AGENT=claude-code_2-1-286_agent`
  one write logged one call and its cell read the stub's 2.1.178, which is the leak the prologue's
  unset closes. The suite arm is OWED at VERIFYING, and arms only where the runner set `AI_AGENT`.
- AC10 — each touched suite and the two checkers timed at base and after on a frozen clone — OWED at
  VERIFYING; no figure exists yet. The AC4 arm adds two reports and 54 in-process reads per run.

Checked as well, none of them a bar leg over a suite: `sh_hygiene.py --spawn-idioms` with the changed
files as pathspecs found no count change for any of them, `sh_hygiene.py` over the substitution-fed
loop registry exited 0, and `lexicon.py` exited 0 after `gen_map.py --write`, where a second `GIT`
definition had first moved both of its pins by one (spec rev-3).
