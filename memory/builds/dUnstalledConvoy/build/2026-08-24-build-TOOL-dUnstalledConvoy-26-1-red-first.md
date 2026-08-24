# TOOL-dUnstalledConvoy-26 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-26

Eleven scope items across three commits and two later ones. The arms live in
`tools/run-gates/run-gates.test.sh` (case 3h2, nine assertions; case 3h4, six),
`tools/govkit/selftest.py` and `tools/govkit/matrix.py`.

## The arms, and the break each one was observed against

| item | how it was observed |
|---|---|
| S1/S1b `subject` on every descriptor leg | the cross-check redded on every leg until each descriptor declared one; the population is read through `read_descriptors`, which loads BOTH roots — a glob over `tools/*/kit.toml` alone misses ten legs |
| S2 held unless asked | 3h2: a kit-subject leg reported `GATE held` with the switch off |
| S2 `GATE_FULL` does not ask | 3h2: the same leg still held under `GATE_FULL=1`. This is the arm the unit rests on — `guard = ["{kit}/"]` failed precisely because `changed()` returns 0 the moment GATE_FULL is set |
| S3 the ask is the switch | 3h2: `GATE ok` under `GATE_SELFTESTS=1`, and nothing held |
| S4 its own verb | 3h2 asserts the held line does NOT carry `skip`'s `(unchanged vs …)` tail, which would be false — the leg is not unchanged, it is out of subject |
| S5 the stamp still writes, and records the switch | 3h2: `selftests\t1` present in `.git/gate-full-green` after a switch-ON green. The first draft of this arm asserted against a file the fixture could not produce — it lacked `gate-fingerprint.sh`, so `FPRINT_START` was empty and no stamp could ever be written. Fixed by copying the helper in |
| S6 the wire format's sixth field | appended AFTER `chunk`, because `chunk` was the last field and anything inserted before it is parsed as chunk by a reader that has not moved in the same commit |
| S7 the guard PRE-PASS | deciding in the dispatch loop leaves an index with no result, which the reporting pass renders as `(no result)` — one per held leg |
| S8 both-directions cross-check | three refusal shapes: no subject, a value outside `kit\|repo`, and descriptor-vs-manifest disagreement |
| S9 emission | AC9 below |
| S10 the adopter is told | AC11 below |

## AC9 and AC10 were not met by this unit's own build

Both were found by reading the spec against the tree at close, not by a gate.

**AC10** — an all-held run printed `gates GREEN — 0/0 legs passed` and exited 0. A repository whose
whole manifest is kit-subject would report a green forever while executing nothing, and stamp a
record saying so. Now exit 2 with a refusal naming the switch. Three of six arms RED; the other
three are the two controls and one that already passed because the held note names the switch
anyway.

**AC9** — the emitted `subject` had no arm in `matrix.py` at all. Added there rather than in the
selftest because a real `apply` into a real target, read back off that target's own manifest, is
the shape that matters. Observed RED with the emission removed — by a stronger route than expected:
the descriptor cross-check refused the apply outright, so no leg reached the manifest at all.

**AC11** — the install-summary arm caught a live defect in the first draft: the receipt row appended
to `emitted` never carried `subject`, so `n_kit` counted zero and the whole block printed nothing.
An `if n_kit:` that is never true is silent, and silence reads as a kit with no self-tests.

## Two defects this unit shipped and later units removed

Recorded here rather than only in the units that fixed them, because a spec's own record should say
what its build got wrong.

- The counter stayed out of `skips` correctly and out of every figure `skips` FEEDS incorrectly —
  the run total and the chunk verdict. `TOOL-dUnstalledConvoy-31` and `-32`.
- `profile_bar.py`'s closed verb set never learned the verb, which S4 names in as many words. 42 of
  gov's 85 legs were dropped from every profile with nothing reporting a gap. Fixed at the closing
  review, and gated as a class: the reader derives the runner's emission set and refuses on any verb
  it does not know.

## The eight stray keys

The descriptor pass placed `subject = "repo"` outside a `[[gate_leg]]` table eight times — six in
`[check]`, one in `[adopt]`, one in `[gate_runner_seed]`. Inert to every reader, and wrong: those
blocks do not declare a subject. Removed under `TOOL-dUnstalledConvoy-30`, with the parsed gate_leg
subjects compared before and after rather than the diff eyeballed.
