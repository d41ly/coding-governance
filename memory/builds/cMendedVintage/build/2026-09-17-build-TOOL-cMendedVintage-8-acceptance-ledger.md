# cMendedVintage — the acceptance ledger for unit 8

**Serves:** journal TOOL-cMendedVintage-8

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken at the shell in the worktree by running the edited
engine, or the edited adopter inside a scratch repo built by hand, and every red was STAGED into a
scratchpad copy and then discarded rather than described.*

## Read this before you read the green arms

**The defect was reproduced at base before anything was edited, and it is exactly what the spec
said.** Against this repo's own conf the engine exited 0; against a conf declaring a real directory
nothing runs under it exited 1; against a conf carrying two roots assignments it also exited 1, with
a different message and the same integer. A caller reading only the status cannot tell those last two
apart, and `govkit update` is such a caller.

**The declared root's quietness is a property of the directory, not of the machine.** The brief is
right that an arm asserting "nothing runs under this path" is the same class of claim this unit
exists to remove from a verdict, so nothing here assumes it. Every fixture root is a directory
created by the fixture itself, moments before the census that grades it, under a name no live
command line on this box carries — in the shipped arm that is a fresh `tempfile.mkdtemp()`, and in
the hand-run adopter fixture it is a directory made in a separate shell invocation from the one that
ran the check. That is stable for a reason a busy machine cannot undo: a path that has existed for
one second and appears in no argv anywhere cannot be prefix-matched by a process that started before
it existed. It is NOT the system temp root, which the adopter refuses outright, and it is not a
shared scratch directory something else might wander into.

**The liveness companion ran in the same session and is what stops a dead census grading this.** A
census that cannot run raises and returns 1, which is a FAILURE for both new arms, so neither can
pass by the probe being unable to move. The shipped conf answering 0 in the same session is the
positive half of that.

**One criterion was found wrong while building and was amended, not worked around.** AC4 asked for a
root that is not a directory. The adopter refuses that in its own root rules, several sections before
it ever calls the engine, so the arm would have stayed green with the whole dispatch deleted — the
fixture-passes-by-finding-nothing class, arriving inside an acceptance criterion instead of inside a
fixture. Both forms were then run and the finding is measured rather than argued.

**Evidences:** TOOL-cMendedVintage-8

- AC1 — `python tools/process-monitor/scope.py --check-conf` — OBSERVED. Against a scratch tree whose
  conf declares one real directory the kit is not under, the run prints a line opening
  `scope: EMPTY`
  and exits 3. At base the same fixture exited 1 with the old `REFUSED` wording, so the change is a
  measured before-and-after and not a read one. Observed RED on a scratchpad copy of the engine with
  the new return lowered back to 1: the arm reports
  `got 1, wanted 3`
  and the copy was discarded.
  Liveness: the same command against this repo's own `.process-monitor.conf` printed
  `scope: conf admits 6 of 159 row(s) from 3 root(s)`
  and exited 0 in the same session, so a census that could not move would have failed that companion
  first.
- AC2 — `PROCMON_ROOTS=` — OBSERVED. Against a conf carrying two roots assignments the same command
  exits 1 and stderr names the duplicate declaration, reporting
  `the conf carries 2 PROCMON_ROOTS assignments`
  An absent conf was run on the same pass and also exits 1, naming the missing file. The shared
  refusal handler was not touched at all, which is why both survived: the diff changes one `return`
  inside the `--check-conf` branch and nothing in the `except` above it.
- AC3 — `bash tools/process-monitor/adopt-process-monitor.sh --check` — OBSERVED, by hand rather than
  through the suite. In a scratch git repo holding the adopter, `scope.py`, `census.py`, a
  both-events `.claude/settings.json` and the AC1 conf, the adopter prints
  `declaration ok`
  then a second line opening `SKIP:` that ends
  `went UNEXERCISED, not passed`
  and names the command to re-run, and the invocation exits 0. With the BASE engine dropped into the
  same repo and the same conf, that identical invocation exits 1 — which is the verdict
  `govkit update` rolls a kit back on, staged and observed rather than asserted.
- AC4 — `PROCMON_ROOTS=` — AMENDED rev-3, then OBSERVED. The criterion now stages two roots
  assignments instead of a non-directory root, because the non-directory form is refused by the
  adopter's own section 3 with no engine call at all: run for the record, it prints
  `is not a directory`
  and never reaches `declaration ok`, so it graded a branch that is not this unit's. The duplicate
  form does reach the dispatch: the adopter prints
  `the engine's reader REFUSES this conf`
  and exits 1. Observed RED on a scratchpad copy of the adopter whose refusal arm was demoted to a
  note without the `exit 1` — the duplicate conf then exits 0, which is the demotion the spec's
  non-goals say must never happen.
- AC5 — `tools/process-monitor/scope.py` — OBSERVED. The module docstring now carries an
  `EXIT CODES` block naming 0, 1 and 3 and what each means, including the sentence that a caller
  which rolls a kit back on a red must not roll back on 3. It carried no exit contract at all before,
  which is how three outcomes came to share one integer without anyone noticing.
- AC6 — `grep -c '^def test_' tools/process-monitor/selftest.py` — OBSERVED for the engine half,
  OWED for the shell half. The grep reads 67 against 66 at base `859daa67`, one higher as the
  criterion asks, and the new arm is collected by the same predicate the suite's own runner uses —
  checked by listing the callables whose name starts with `test_`, which is the scan that would miss
  a helper named anything else. `FLOOR_ASSERTIONS` reads 34, higher than the pinned 31.
  figure: REASONED, NOT MEASURED, and this is the honest half. The floor moved by the three
  assertions the new block adds, all of them unconditional, counted from the source rather than read
  off a run, because the suite that would print the executed total is a `*.test.sh` this pass may not
  run. A floor is a lower bound, so a suite executing more than 34 still passes; what is unverified
  is only that 34 is the tightest true bound.

**OWED, one arm and two legs.** The two arms added to `adopt-process-monitor.test.sh` ship
UNEXECUTED: that suite is banned in this pass and nothing here claims otherwise. What WAS done
instead is the fixture setup by hand — a scratch git repo built with plain shell commands, the
adopter and both engine files copied into it, a wired settings file and each conf written in turn,
and the adopter invoked directly — so the two branches the arms assert over were observed even though
the arms asserting them were not. The gate legs `process-monitor adopter selftest` and
`testsuite counts` are owed to the main loop's bar.

## What did not run, and why

`bash tools/run-gates/run-gates.sh` in every form, and every `*.test.sh` suite, were withheld by this
pass's own mandate. The gate scripts that DO grade this unit's new bytes were run individually:

| run directly | what it says about this unit | result |
|---|---|---|
| the new arm plus its liveness companion, driven through the engine suite's module | the exit code the unit is | exit 0, 2 of 2 ok |
| the same arm over a scratchpad engine with the new return lowered to 1 | the arm has a failing case | RED, as staged |
| the adopter, by hand, in a scratch repo carrying the engine | both new branches | exit 0 skip, exit 1 refusal |
| `python tools/lexicon/lexicon.py` | the new arm leads with the declared verb `test` | exit 0, offender pin unmoved |
| `bash tools/check-install-prefix.sh` | no new prose spells an install prefix | exit 0, 269 shipped files |
| `bash tools/check-line-length.sh` | the new docstring and skip line stay under the limit | exit 0 |
| `bash tools/check-dead-paths.sh` | the rev-3 edits name no deleted file | exit 0, 24 derived needles |
| `python tools/check-spec-tokens.py` | rev-3's backticked citations still resolve | exit 0, 833 tokens graded |
| `python tools/govkit/govkit.py selfcheck` | no descriptor moved, and none needed to | exit 0, 0 unclaimed |
| `bash -n` on both edited shell files | the `case` parses | exit 0 |

`python tools/codebase-map/gen_map.py --write` rewrote exactly one of the three generated artifacts.
The new test function is a symbol key; the inventory and the map prose came back byte-identical, so
no dossier claim is owed.

## Two notes a later reader will want

**The discriminator is in the engine and the adopter only reads it, and that is the whole design.**
A one-line change on the adopter side — lowering its `exit 1` to a note — would have been a smaller
diff and would have demoted the conf-parse refusal with it. The staged red for AC4 is literally that
change, and it lets a duplicate roots declaration pass. The refusal is the one thing in this path
that must not become a skip, and only the engine can tell the two apart.

**The shell fixture copies the engine and nothing else does.** `run_against` deliberately copies the
adopter alone, so every arm that predates this unit never reaches the dispatch at all. A new arm that
simply reused it would have exercised the `NOT CHECKED` fallback and passed by finding nothing. The
copy is therefore opt-in, one line, gated on an environment variable the two new arms set and no
other arm does — which keeps the older arms grading exactly what they graded before.
