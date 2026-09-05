# aTunedCompass — the acceptance ledger for unit 6

**Serves:** journal TOOL-aTunedCompass-6

*Node `a`, 2026-09-05, written by the unattended run that built the unit, immediately after the
observations were taken.*

Every line below is `OBSERVED` with the command that made it, or `AMENDED` naming the revision that
changed the criterion. There is no third form.

## The headline result, stated before the evidence because it is not the flattering one

The reorder is proven correct at source: the cap now slices the pool the ranking ordered, and the
ordering key is stated once and read twice. Its MEASURED effect on this corpus, over 140 recorded
probe phrases, is a hit-rate move of 0.579 → 0.600 and **no change at all** to hit@5 (0.371), hit@10
(0.400) or the median rank of the first correct answer (2). So the change fixes a defect that was
real — twelve slots were going to the twelve alphabetically-first names — and buys almost nothing in
the ranks a reader actually reads. That is the unit's own §4 prediction holding: it substitutes one
set of low-value names for another, and the pool it selects from is what unit 10 narrows.

## Evidences

**Evidences:** TOOL-aTunedCompass-6

- AC1 — `python tools/codebase-map/reuse_lookup.py` on this spec's own §10 phrase — the cap is
  applied to `neighbour_ranked` AFTER `neighbour_ranked.sort(key=_shortlist_key)`, and the printed
  neighbours are in descending fan-in.
- AC2 — `python tools/codebase-map/reuse_lookup.py`, run before and after with the fan-in sort
  staged out — the twelve retained neighbours change from a fan-in sum of **8** to **271**, and the
  two sets **do not intersect** (`comm -12` returns 0 names). Those are the figures rev-1 measured
  at base `c4fcf5ad`, reproduced at HEAD.
- AC3 — `diff` over the same two runs, candidates section only and neighbours excluded — the SEED
  half is **byte-identical**, so `_rank` and the seed arm were not disturbed. Worth stating how this was
  nearly mis-read: a first comparison included the `## sources to open` block and reported a
  difference, which is correct behaviour — that block lists the files of the candidates, and the
  neighbours changed. The criterion is about seeds.
- AC4 — `python tools/codebase-map/replay-phrases.py`, run before and after — **140 phrases graded**
  (39 more carried no §10 ground truth and are excluded rather than counted as misses). hit rate
  0.579 → 0.600; hit@5 0.371 → 0.371; hit@10 0.400 → 0.400; median rank of first correct 2 → 2. The
  count is reported rather than pinned, per this criterion's own wording: the parent's 133 is not a
  target and this harness reaches 140 because its invocation pattern joins WRAPPED phrases.
- AC5 — `python tools/codebase-map/reuse_lookup.py "<any phrase>"` — the header now carries two
  lines saying the ranking counts NAME TOKENS and resolves no symbols, so a high rank means "this
  name appears a lot", never "this is the seam you want".
- AC9 — `git ls-files` returns the harness path; running it with no arguments prints the declared
  ceiling; and with `--ceiling 0.001` it **exits 1** naming the breach. The ceiling was observed
  RED, which is the criterion's load-bearing half. It is `60.0` seconds against a measured 2.8s run
  — the first draft declared 600s on reasoning about a subprocess-per-phrase design this harness
  does not have, and a 600s bound over a 3s run is a ceiling that cannot fire.
- AC10 — `python tools/govkit/govkit.py selfcheck` — exit 0 with `replay-phrases.py` claimed
  `project-owned` in `tools/codebase-map/kit.toml`, so `apply` never writes it (`project-owned` is
  absent from `LANDABLE_ROLES`).
- AC11 — `WIRE-INTO-PROJECT.md` §3b step 1 gains the `rm -f` removal line, because a
  `project-owned` role withholds a file from `govkit apply` and from nothing else, and this kit's
  documented install is a plain `cp -r`. The memory-recall kit pays for the same gap the same way.
- AC6 — `python tools/codebase-map/selftest.py` exits 0 (27 executed, 0 skipped) and
  `python tools/codebase-map/test_codebase_map.py` exits 0. Both green.
- AC7 — `bash tools/check-kit-versions.sh` — exit 0 with `KIT_CODEBASE_MAP_VERSION` at `1.5`. TWO
  carriers moved: the constant and the `gov:kit codebase-map@` marker four lines above it. The
  version gate passed while they disagreed, so the marker was caught by reading rather than by a leg.

## The staged break, and what it caught

S4's arm was observed RED against the shipped ordering before it was accepted. The break removes the
fan-in sort so the cap slices the alphabetical pool exactly as shipped, and the arm's failure names
the twelve zero-fan-in filler symbols it kept:

```
FAIL the neighbour cap slices the RANKED pool, not the alphabetical one: the highest-fan-in
neighbour was truncated before it could be ranked: ['aa_pad_00', ... 'aa_pad_11']
```

The fixture derives its filler count from `NEIGHBOUR_CAP` rather than hard-coding twelve, so the arm
cannot rot into vacuity if the cap moves.

**The kit's own selftest caught a real defect in the new harness**, which is worth recording because
it is the arm doing its job on unrelated code: `replay-phrases.py` used `Path(__file__).resolve()`,
and this kit forbids `resolve()` because it follows a junction to the link target and would disagree
with `map_lib.kit_dir()` about the install prefix both stamp into byte-compared artifacts. Changed
to `os.path.abspath`.

## Suites, in full

- `python tools/codebase-map/selftest.py` — **27 executed, 0 skipped, PASS**, including the new arm.
- `python tools/codebase-map/gen_map.py --check` — exit 0 after `--write`.
- `bash tools/check-kit-versions.sh` — exit 0.
- `python tools/govkit/govkit.py selfcheck` — exit 0, 0 unclaimed paths.
- `python tools/check-spec-tokens.py` — exit 0.
- `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0.

`codebase-map kit selftest` and `codebase-map adopter e2e` are `subject = kit` and held off an
ordinary bar, so the suite above was run ON DEMAND, directly.
