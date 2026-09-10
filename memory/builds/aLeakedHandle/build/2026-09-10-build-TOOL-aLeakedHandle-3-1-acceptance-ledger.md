# TOOL-aLeakedHandle-3 — acceptance ledger

**Serves:** journal TOOL-aLeakedHandle-3

**Evidences:** TOOL-aLeakedHandle-3
- AC1 — `bash tools/run-gates/run-gates.test.sh` on node `a`, whole suite, both sides of the change.
  The new arm 4h-kill drives a fixture leg `selfkilled` that runs `sleep 2` and then `kill -9 $$`,
  declared with `"ceiling": 600` under the `tbl-loose` profile so `PROF_TIMEOUT` is 0 and the
  declared 600 is the only bound in play. `timeout` returns 128+9 for a command killed by a signal,
  so the runner sees rc=137 from a kill it never ordered. The seconds in the `GATE FAIL  selfkilled`
  tail and field 2 of that leg's row in `$P/.git/gate-ledger.tsv` were compared as strings, not as
  numbers. The fixed run passed the whole suite silently — this file's arms print only on failure —
  so the BYTES were captured from a direct reproduction of the same fixture outside the suite,
  against the same `tools/run-gates/run-gates.sh`: the tail read
  `GATE FAIL  selfkilled  (killed after 2.152s, ceiling 600s)` and the ledger row read
  `selfkilled<TAB>2.152<TAB>fail<TAB>-<TAB>1789043747925512800`. `2.152` on both sides, decimals
  included. The two runs are named separately here because they are two runs, and the suite's own
  green is the one that grades the assertion
- AC2 — the same reproduction's tail read `(killed after 2.152s, ceiling 600s)`, and inside the
  suite the `case` arm found no `timed out` in it — that arm is one of the three that went red
  against the unfixed source and green after, which is the pair that makes the assertion mean
  something
- AC3 — the two rc=124 controls stayed green in the same run and are the boundary section 2's S2
  draws: `run-gates.test.sh:225` still matched `GATE FAIL  slow bounded` with `timed out after 2s`,
  and the arm now at `run-gates.test.sh:1144` still matched
  `GATE FAIL  sleeper  (timed out after 3s)`. Neither emitted a canary line, and both name the
  CEILING, which is what a passing pair proves here: the change did not widen into the 124 branch
- AC4 — OBSERVED RED FIRST, against the unfixed source. `bash tools/run-gates/run-gates.test.sh`
  was run whole at `2489d058` — this build's tip, three commits past the spec's pinned base
  `013b1af9`, with the rc=137 branch byte-unchanged from it — carrying the test-side hunk alone and
  `tools/run-gates/run-gates.sh` untouched: exit 1, three canary lines and no others. The one this
  criterion is about read
  *the failure tail for a killed leg states '600's where gate-ledger.tsv records '2.144's for the
  same leg on the same run* — both numbers named, a factor of 280 apart on one run of one leg.
  The positive artifact that the arm actually RAN, rather than an empty FAIL list from a harness
  that never executed: the same output carries the runner's own block for that leg —
  `gate profile: loose`, `GATE ok    one`, `GATE FAIL  selfkilled  (timed out after 600s, killed)`,
  `gates RED — 1/2 legs failed` — so the leg was dispatched, killed, reported and ledgered
- AC5 — the fixed run's closing line: `PASS (148 assertions)`, exit 0, 802 s of wall clock, against
  the `FLOOR_ASSERTIONS` raised from 143 to 146 in `tools/run-gates/run-gates.test.sh`. 148 rather
  than 146 because this host has a runnable `timeout`, so the arms that count INSIDE a guard
  executed too — the floor is the skipped-host figure by construction, which is what the constant's
  own header says. The gap of 2 was not measured at BASE and is not claimed here. The unfixed run
  emitted no *below the pinned floor* canary either, so the three increments executed on both sides
  of the change. The timeout-less half of this criterion's Red-when is UNOBSERVED and section 6
  already permits it: no host without a runnable `timeout` is reachable from here. The placement is
  verified by reading the source — the three `n=$((n+1))` sit above the `if [ "$HAVE_TIMEOUT" = 1 ]`
  line, beside arm 4h's four, and the `else` arm names both arms in its skip message

## The moved assertion, and why it moved rather than gained a branch

`run-gates.test.sh:1156` at BASE accepted `(timed out after 3s(, killed)?)` for the kill-after
escalation. That path is a genuine ceiling-fired 137, so the new tail reaches it too, and the
assertion now accepts `(timed out after 3s)` when TERM wins or `(killed after <n>s, ceiling 3s)`
when KILL does — which one wins is the host's business, exactly as before. On this host KILL wins,
and that is the ONLY reason the moved assertion went red on the unfixed run: it was the first canary
line of the three, reporting `GATE FAIL  stubborn  (timed out after 3s, killed)`, the old spelling.
The new line is also more honest about that path than the old one was: the leg ran the declared
bound PLUS the five-second `-k` escalation, so the old `3s` was already wrong by 5 s on a branch
nobody was complaining about.

## What this ledger does not evidence

The degraded `?` form is NOT observed and cannot be reached from a test. `report_one` builds a tail
only for a leg whose `$WORK/<i>.rc` holds a numeric code, and only `runleg` writes that file — after
it has written `$WORK/<i>.sec`. So on every path that reaches the rc=137 branch the `.sec` file is
already there, and `${secs:-?}` is a guard against a write that failed rather than a state a fixture
can stage. The whole-run wall guard does not reach it either: `scan_descendants` seeds its kill set
with the `runleg` subshell's own pid, so a wall-killed leg writes neither file and `report_one`
returns `(no result)` before any tail is built.

Nothing here grades `tools/run-gates/README.md`. Section 2's S4 says so up front — the clause it
adds is documentation, no gate reads that file's prose about the tail, and an arm asserting a
sentence would grade the sentence rather than the behaviour.

Nothing here runs at a merge bar. `run-gates canary` is `chunk: selftests` with a `tools/` guard, so
`run-gates.sh` holds it unless `GATE_SELFTESTS=1`, and the charter records that no push boundary
sets that. The compensating check is the direct invocation recorded above, run whole, twice.

Nothing here measures the rc=137 branch on a host where `timeout` is absent. Both runs above had
`HAVE_TIMEOUT=1`, so arm 4h-kill executed rather than announcing its skip; the skip message itself
is unexercised text.

## The bug-class checklist over this commit, and the two it left standing

`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` selected eleven classes over the
build commit. Nine are discharged by the work itself and are not re-argued here — the staged break
was the SHIPPED source rather than a synthetic simplification, the arm was observed RED before
landing, the liveness half sits inside assertion 2, `awk -F'\t'` does not collapse a run of tabs so
an empty seconds field still reports as field 2 and reds rather than shifting, and neither the
`$( )` capture in the arm nor the `cat` in `report_one` can block on a pipe nobody closed. Two are
left standing deliberately, and standing is not the same as unnoticed:

**`two-answers-to-one-question`, one literal, KEPT.** Assertion 3's failure message says *under a
declared ceiling of 600* while the fixture five lines above declares `"ceiling": 600`. That is the
class: change the fixture and the message lies. It is kept because the duplicate lives inside one
twenty-line arm, in a DIAGNOSTIC string no checker reads, and removing it costs a re-observation of
the red side — the message is on the branch that only runs when the arm fires, so an edit to it is
an edit to observed evidence. A three-word improvement priced at a second full 800 s cycle is the
trade this repo's own cost rule says to refuse. Recorded so it is a decision rather than an
oversight, and so the next hand knows the pair moves together.

**`fold-text-is-unreviewed-surface`, live and unclosable here.** The source comments, the
`tools/run-gates/README.md` clause and this record are fresh prose no review round has read, and
none is available to read them: this spec's audit loop recorded CLEAN at round 1, which check 37
treats as terminal. The same gap unit 2 recorded, for the same reason, and it is the owner's rather
than this pass's. What bounds it: no acceptance criterion, scope item or gate in the spec moved, so
the unreviewed surface is explanation and never contract.
