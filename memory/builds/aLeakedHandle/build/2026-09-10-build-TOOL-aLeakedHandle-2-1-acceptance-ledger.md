# TOOL-aLeakedHandle-2 — acceptance ledger

**Serves:** journal TOOL-aLeakedHandle-2

**Evidences:** TOOL-aLeakedHandle-2
- AC1 — the copied `derive-ceilings.py --report` over a fixture `gate-run` holding three `fail` rows on three legs that all declare `ceiling` 100 — `at-ceiling` at 100.4 s, `below-ceiling` at 40.0 s, `way-over` at 400.0 s — printed a table row for `at-ceiling` alone and named the other two on its UNBACKED line. Four assertions rather than three: the fourth is the control that stops the two exclusions passing by an empty report, and it earned its place, because with the `ok`-only predicate restored the report has no admitted row at all and exits DEAD PROBE with no UNBACKED line to read. The `way-over` leg is the class the closed window refuses and is not the 900.240 s instance this unit was written from
- AC2 — with an `ok` row of 20.0 s appended for the same leg, the reported row is `at-ceiling` at 100.4 s over 2 readings, so the admitted failing row reached `max_s` rather than merely entering the population. The assertion grades the count as well as the maximum, so a run that dropped the `ok` row entirely would not satisfy it
- AC3 — the copied `derive-ceilings.py --check` against a hand-written evidence row of 100.4 s for a leg whose ceiling is 100 exited 1 and printed `ceiling 100s was REACHED in a recorded run at 100.4s — that reading is a LOWER BOUND on the work and not its duration`. A second assertion proves the headroom sentence is absent for that row, and a third is its control: a row at 40.0 s under the same ceiling still reports `does not clear its evidenced maximum`, so the absence above is a verdict and not a gate that stopped saying anything. The evidence file for this arm is written by hand rather than chained off AC6's `--write`, so a defect there cannot red this criterion for a reason that is not its own
- AC4 — see *How the six failing cases were observed* below. Every one of the six was staged into `tools/run-gates/derive-ceilings.py` in place, observed, and restored, and the restored file was proven byte-identical to a pristine copy taken before the break. Break 1 was observed through the whole named invocation, `bash tools/run-gates/run-gates.evidence.test.sh` — 63 assertions executed, exactly the four expected `FAIL` lines and no others, `FAIL (run-gates evidence durability, 63 assertions)`, exit 1, 551 s. The criterion was AMENDED to admit the new section alone for the other five, and rev-4 in section 9 states the amendment and the grep it is gated on
- AC5 — `python tools/run-gates/derive-ceilings.py --report` on node `a` in this worktree, both sides of the change. BEFORE: no row for `memory-hygiene self-test` on stdout and `# 1 leg(s) UNBACKED — declared a ceiling, measured nothing: memory-hygiene self-test` on stderr, that leg being the only one named. AFTER: `memory-hygiene self-test	900.5	2	900	-0	900	UNDER` on stdout and an EMPTY stderr, the UNBACKED line gone entirely because no leg is left without a reading. The before side was measured by running the BASE copy of the script out of the same directory, so `HERE` resolved to the same margin and evidence files
- AC6 — the copied `tools/run-gates/derive-ceilings.py --write` over the fixture AC1 builds wrote a row for `at-ceiling` at 100.4 s and no row for either excluded leg. The criterion's own named failure mode was staged and observed: with `read_runs`'s ceilings map given a DEFAULT and `cmd_write`'s `read_legs` call dropped, this is the ONLY arm that reds — AC1's four report assertions, AC3's three and AC7's two all stay green, which is verbatim the silent-regression shape section 4 predicts
- AC7 — the arm extracts `read_runs`'s docstring from the copied file by `ast`, not by grepping the whole module, so a sentence sitting anywhere else cannot satisfy it. It asserts `ceiling`, `slow`, `contended` and `hung` in one assertion and `--reset` in a second, because section 5 rests the whole mitigation of the monotone-floor hazard on the escape and a single assertion would let the two halves cover for each other. Both were staged red separately: cutting the rule and its three causes reds the first alone, cutting only the `--write --reset <leg>` clause reds the second alone

## How the six failing cases were observed

Every new arm's failing case was staged into `tools/run-gates/derive-ceilings.py`, observed RED, and
unstaged. Break 1 ran the whole named invocation; the other five ran the file's own new section from
its own prologue, which rev-4 admits and gates on a grep. That grep is the equivalence and it was
run: over every one of the fifty-one arms preceding the new section, neither `derive-ceilings` nor
the word `ceiling` appears once, so none of them can observe a break confined to that file. The
full-suite run of break 1 is the direct confirmation — 63 arms executed, four `FAIL` lines, and the
other fifty-nine green.

The six breaks and the arms each one reds:

| break | staged | arms that went RED |
|---|---|---|
| 1 | the bare `ok`-only predicate restored in `read_runs` | AC1's admission, AC1's UNBACKED control, AC6, AC2 |
| 2 | the window reopened at the top to `secs >= ceiling` | AC1's four-times-the-ceiling assertion, AC1's UNBACKED control |
| 3 | the headroom sentence restored in `cmd_check` | both AC3 assertions |
| 4a | `cmd_write`'s `read_legs` call dropped, shipped code otherwise unchanged | AC6 alone |
| 4b | that call dropped AND the ceilings map given a DEFAULT | AC6 alone |
| 5 | the rule and its three causes cut from `read_runs`'s docstring | AC7's first assertion alone |
| 6 | only the `--reset` clause cut from that docstring | AC7's second assertion alone |

Two properties of that table are the point of it. Breaks 4a, 4b, 5 and 6 red exactly ONE arm each,
which is what makes those arms separable rather than four spellings of one assertion. And break 1
reds AC1's UNBACKED control for a reason worth stating: with nothing admitted, `cmd_report` refuses
as a DEAD PROBE and prints no UNBACKED line at all, so the control fails by absence rather than by
naming the wrong legs.

**Why 4a exists beside 4b.** The bug-class checklist selected
`staged-break-substitutes-a-synthetic-value` over this diff and it was live. 4b ADDS a default that
the shipped signature does not have, so on its own it proves AC6 catches a write path under a
signature nobody ships — the failure mode section 4 names, and a synthetic one. 4a is the shipped
bytes minus one call and nothing else: `read_runs`'s ceilings map is a REQUIRED parameter, so
dropping `cmd_write`'s call raises rather than silently reverting, `--write` produces no file, and
AC6 reds. Both were observed. 4a is the one that grades what ships.

**The observation harness itself carried a defect first, and it is recorded because it is the class
this repository keeps re-filing.** The first driver reported all six breaks as UNOBSERVED. Nothing
had gone red because nothing had RUN: a Windows path handed through a POSIX-emulation layer arrived
at `bash` mangled, every invocation exited 127, and an empty FAIL list read exactly like a clean
one. The driver now refuses any run that does not execute all twelve arms, and it runs the unbroken
tree first as a control. Charter section 7's liveness rule, met by a probe that could not move and
said so instead of reporting a reassuring zero.

**The suite's own cost, because a check nobody can afford is a check nobody runs.** Unbroken, on
node `a` 2026-09-10: `PASS (63 assertions)` in 559 s, against a declared budget of 2250 s in
`tools/run-gates/selftest-budgets.txt` and a recorded maximum of 1385.1 s in
`tools/run-gates/ceiling-evidence.txt`. Twelve new arms added roughly nothing to it: they build one
`mktemp -d` copy of two files and run five short python invocations against it, where the arms
already there drive the real runner through dozens of scratch repositories.

## What this ledger does not evidence

Nothing here measures the changed predicate at a merge bar. `run-gates evidence` is
`chunk: selftests` and `subject: kit`, which `run-gates.sh` holds unless `GATE_SELFTESTS=1`, and the
charter records that no boundary sets it. The one leg in section 7 that touches this unit's own file
at a boundary is `leg ceilings clear their evidenced maximum`, and it runs `--check`, which reads
the two tracked files and no run file at all. A green bar over this diff is therefore NOT coverage
of the admission rule, and the compensating check is the direct invocation recorded above.

Nothing here refreshes `tools/run-gates/ceiling-evidence.txt`. Section 3 forbids it, and the first
consequence of doing it would be a red on a ceiling the owner has parked. The artifact is untouched
by this unit, which is why AC5's new row is visible to `--report` and to nothing else.

Nothing here reviews the rev-4 amendment's own prose. `fold-text-is-unreviewed-surface` was
selected over this diff and it is live: the section 9 line and the amended AC4 are fresh text no
review round has read, and no round is available to read them — this spec's loop recorded CONVERGED
at round 1, which check 37 reads as terminal. That is the same gap this run already parked as a
decision in `RUN.md`, and it is the owner's, not this pass's. What bounds it here is that the
amendment relaxes an OBSERVATION method and nothing else: every criterion, every scope item and
every gate is byte-unchanged, and break 1 was observed through the unrelaxed invocation anyway.

Nothing here says WHY `memory-hygiene self-test` reaches its ceiling. Slow, contended and hung have
one signature in the record, `read_runs`'s docstring says so, and this unit deliberately invents no
discriminator for them.
