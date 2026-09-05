# aTunedCompass — what the unattended run of 2026-09-05 built, and what it did not

**Serves:** journal TOOL-aTunedCompass-1

*Node `a`, 2026-09-05. This began as three rules in the build README's `## Build-level rules` slot.
That slot is byte-capped at 1800 B and the run pushed it to 4503 — a run writing its own report into
a capped slot is the "put the fact where it belongs" lesson the cap exists to teach, and the closing
review's round 2 caught it as a live merge-bar red. The content moved here; a pointer stayed there.*

## What was built

**Seven units CLOSED**: 1, 4, 5, 6, 7, 8, 10. Each carries an acceptance ledger under `build/` with
its criteria answered by an observation and a command, or marked `AMENDED` where a criterion was
deferred to a later unit.

**Unit 11 is IMPLEMENTED and committed, and its spec is NOT closed.** See the caveat below.

**Units 2, 3 and 9 are UNBUILT.** 2 and 3 are blocked on 9, and 9 is the largest single piece in the
build: a sampled, agent-judged question set plus engine changes binding the fixture audit's graded
set to each fixture rather than to the pin. Starting it without finishing would have left a
half-authored question set that `TOOL-aTunedCompass-3` is due to pin the merge bar against, which is
worse than none at all.

What the run did instead: unit 9's spec gained a MEASURED candidate pool at rev-5 — 199 query rows,
179 distinct questions, and **165 of them carry a chunk hit in a file with no anchored record**, which
is the population S1 describes. So the next run inherits the sampling frame rather than rediscovering
it. F1's judgement half — which passage answers each question — is untouched and is still the
expensive part.

## The caveat that matters most: unit 11 is unverified

Its reader, its six declaration carriers and its two record corrections are committed. Every leg that
CAN run over it is green: `unattended kit gate` (check 22 was observed RED on the undocumented key
first, then green once all six carriers declared it), `memory hygiene`, `spec tokens`, `dead paths`,
`kit version markers`, `install prefix`, `lexicon` and `check-wiring`.

What did NOT run is the kit's own driver suite, which carries the three new `MAP_CLI` arms and the
eight existing arms this unit re-worded. **Two attempts, each producing ZERO output before being
killed at its bound — one at 50 minutes, one at 90.** A pristine-tree baseline was equally silent for
its first 100 seconds, so the silence is that suite's buffering rather than a hang this build
introduced; that is why the work was committed rather than reverted. But buffering is not evidence of
passing, and the difference is exactly why the spec stays `SPECCED`.

The one live exercise the run did get is its own `--close`, which evaluates `reuse-probed` against
this tree with both CLIs declared and both logs present.

**The owner's call** is whether to run that suite on a quieter node and close the unit, or to treat
the arms as suspect.

## The reviews, and what they cost

| Review | Subjects | Raw | Confirmed | Precision | Verdict |
|---|---|---|---|---|---|
| spec audit round 1 | all 11 specs | 57 | 27 | 0.47 | BLOCKED — 20 defects, 3 blockers |
| spec audit round 2 | units 4, 6, 9 | 45 | 21 | 0.47 | BLOCKED — 16 defects, 2 blockers |
| closing diff round 1 | `22d75b31..HEAD` | 22 | 20 | **0.91** | BLOCKED — 11 defects, 2 blockers |
| closing diff round 2 | the fold | 22 | 20 | **0.91** | BLOCKED — 11 defects, 1 blocker |

**The spec-audit loop exited NON-CONVERGENT.** Round 2's blocker count did not strictly shrink, so M4
stops the loop; both standing blockers were FOLDED and the disposition is recorded on the exiting
round. Fifteen of round 2's sixteen defects were created by round 1's own fold, which is this repo's
`fold-text-is-unreviewed-surface` class measured rather than asserted.

**The closing review earned its keep twice over, and the precision gap says why.** At 0.47 the spec
audits were arguing about documents; at 0.91 the closing review was reading code and reproducing
defects. Both of its round-1 blockers were seam defects that per-unit verification structurally
cannot see: four backlog rows this build FALSIFIED and left OPEN — the exact class unit 1 exists to
close, re-created four times in the file it edited to fix it — and a telemetry field that dropped
every dossier source while three carriers asserted it was "ONE derivation".

Round 2 then caught the fold's own worst defect: the both-directions containment arm added as the
regression gate for that second blocker **could not fail**, because its fixture holds zero dossiers.
The reviewer staged the break and confirmed the arm passes with the defect restored. A gate written
to prevent a recurrence, that could not have caught the original — which is why "observe the failing
case" is a rule and not a nicety.
