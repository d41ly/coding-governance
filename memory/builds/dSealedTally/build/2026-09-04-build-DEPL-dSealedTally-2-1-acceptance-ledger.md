# Acceptance ledger — DEPL-dSealedTally-2

**Serves:** journal DEPL-dSealedTally-2

Tier-2 · node d · 2026-09-04

## The headline: the hoist broke the landing, and the existing arms caught it

The unit as specced was one change — move the `rename_dests` fill out of the row walk. Making that
change alone turned a latent bug live and broke the feature the previous build had just shipped.

`rename_dests[eid]` is a kit's FULL source-to-destination map, not a rename-only one. The landing's
`_decided` set took every value in it:

```python
for _m in rename_dests.values():
    for _dl in _m.values():
        _decided.update(_dl)
```

So `_decided` was the entire declared surface of every kit the map held. That was survivable only
because the fill was LAZY: it ran solely for a kit with a rename that reached `resolve_renamed`, and
a run with no renames at all left the map empty. The `[-RS1]` landing arms pass at base for that
reason and no other — the run they exercise adds a file and renames nothing.

Filling eagerly populated the map on every run, `_decided` became everything, and **nothing could
ever land as an unclaimed source again**. Seven `[-RS1]` arms went red. They are arms
`DEPL-dRatifiedSeam-1` wrote three commits earlier, and they did exactly the job they were written
for.

The unit is therefore TWO changes, and the spec is at rev-3 saying so:

- the eager fill, so the map exists for a kit whose renamed row skipped the walk;
- `_decided` narrowed to the destinations of sources gov ACTUALLY renamed, which is what its own
  name and its own comment always claimed it held.

`renames` maps old source to new source, so `_m.get(_new_src)` is the exact narrowing. With no
renames in a run, `_decided` gains nothing from the map and the landing works as before.

## The fixture was wrong twice, and its own liveness arm said so the first time

The first trigger was `role = "gate-leg"`, whose `how` is `report` and which therefore continues
before `classify_row`. It is not INSTALLED — `apply` routes it to an outbox — so the fixture's
install arm redded and the liveness arm redded with it, while two outcome arms sat green on a
target that had never received the file. That is the fixture-passes-by-finding-nothing class, caught
by the assertion written to catch it.

Rebuilt on an engine row carrying `evidence: "unattributed"`, which continues at
`tools/govkit/govkit.py:6112`. That is a real receipt state — `apply` writes it at 7594 for a row it
cannot attribute — and it is the cheapest of the seven pre-`classify_row` continues to construct,
because it is a receipt field rather than a role.

## The criteria

**Evidences:** DEPL-dSealedTally-2

- AC1 — MET, OBSERVED BY STAGED BREAK — `python tools/govkit/selftest.py` runs five `[-ST2]` arms
  over a kit whose renamed row takes the `unattributed` continue: the destination
  `tools/mvkit/moved2.txt` is not landed, the run reports `unclaimed sources: 0 landed`, the kit's
  other file is untouched, and the run exits 0.
- AC2 — MET, OBSERVED — disabling the eager loop in `tools/govkit/govkit.py` and re-running
  turned EXACTLY the two mechanism
  arms red (`the rename DESTINATION is not landed`, `landed no unclaimed source`) while the install
  arm and the LIVENESS arm stayed green. That split is what makes the break discriminating: it
  proves the break is in the mechanism and not in the fixture, which a wholesale red would not.
- AC3 — MET — the `[-11]` and `[-RS1]` arms report the same landing decisions as at base
  `0f19429a`, which is `python tools/govkit/selftest.py` returning to all-green after the narrowing.
  They are the reason the regression was caught rather than shipped.
- AC4 — MET — `fill_rename_dests` is wrapped in `try/except Refusal: continue` in the eager loop,
  and `resolve_renamed` re-raises at the same place it always did for a kit the loop skipped, so a
  kit with an unresolvable descriptor is skipped rather than aborting the run.
- AC5 — NOT MET — the spec asked for a mutation removing `try/except Refusal` and asserting
  that AC4 reds, and no such arm exists. A
  fixture whose descriptor raises during resolution was not built, so AC4 is met by construction
  and reading rather than by an arm, and AC5 has nothing to mutate. Recorded unmet rather than
  faked; see the residue note below.
- AC6 — MET — `python tools/govkit/selftest.py` exits 0 at **1080 arms**, six more than the 1074 at
  base `0f19429a`, and this unit is `order 1` so the base count is the legitimate comparison.

## Residue

AC5 is unmet and AC4 is met by reading. Building the `Refusal` fixture needs a descriptor that
resolves cleanly at `apply` time and raises at `update` time, which is a fixture shape this suite
does not yet have. It is a real gap in this unit's coverage, not a formality: the `try/except` is
the one line that keeps the hoist from moving a refusal onto every kit's path, and nothing observes
it. Recorded here and carried to the build's residue rather than closed silently.
