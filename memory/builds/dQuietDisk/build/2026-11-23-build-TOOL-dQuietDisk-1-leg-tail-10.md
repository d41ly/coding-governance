# TOOL-dQuietDisk-1 leg-tail 10 — recall floor arms failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** recall floor arms
- **Hash:** 7ab10c2ad9e2811af5c2e8812a8ea06b77ef0a64
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg recall floor arms | exit 1
ok   baseline is green and prints both verdicts — per-id ok + RECALL_FLOOR ok, exit 0
ok   the FLOOR reds alone (per-id stays green) — floor RED at 0.7500, per-id ok — the directions are independent
ok   PER-ID reds alone (the floor stays green and RISES) — per-id RED naming the id, floor ok at 0.9091 — it rose
ok   one retirement of a HITTING target is free by construction — normalised 0.8182 >= 0.81, floor ok — the headroom the pin is derived from
ok   dropping the whole record file reds BOTH (the plumbing arm) — both RED at 0.0909 — the score responds to the corpus, which is all this arm claims
ok   an ABSENT fixture reds by name and does not skip — REFUSED naming the path
ok   an EMPTY fixture reds at the precondition, never downstream — REFUSED — a question set with no questions cannot grade anything
ok   an ALL-MISS fixture reds on per-id and reports the floor as not evaluated — per-id RED, floor `not evaluated` — no 0/0
ok   an EMPTY graded set refuses (the branch that replaced one that could not fail) — REFUSED — a synthetically emptied set grades nothing, and the floor says so
ok   an ABSENT pin reds naming the key, with no default — REFUSED naming RECALL_FLOOR
ok   a MALFORMED pin reds naming the key — REFUSED — a bare scalar names no cell
ok   an OUT-OF-VOCABULARY pin reds at the pin, not inside bench.load — REFUSED naming the key — no FileNotFoundError
FAIL --audit-fixture is green on the served pin, h and R not below the conf's record — expected 0
  #  expected id                  slice       homes  hits  overlap
  1  TOOL-aUnmannedHelm-5         terms           4   yes    0.444
  2  TOOL-aUnmannedHelm-5         naive_terms     4   yes    0.444
  3  TOOL-aUnmannedHelm-6         terms           4   yes    0.500
  4  TOOL-aUnmannedHelm-6         naive_terms     4   yes    0.500
  5  TOOL-aStandingWrit-2         terms           2   yes    0.500
  6  TOOL-aStandingWrit-2         naive_terms     2   yes    0.500
  7  TOOL-aStandingWrit-4         terms           2   yes    0.375
  8  TOOL-aStandingWrit-4         naive_terms     2   yes    0.375
  9  TOOL-cSteadyMetronome-1      terms           2   yes    0.375
 10  TOOL-cSteadyMetronome-1      naive_terms     2   yes    0.375
 11  TOOL-aWidenedGuide-1         terms           2   yes    0.429
 12  TOOL-aWidenedGuide-1         naive_terms     2   yes    0.429
 13  TOOL-aWrittenMethod-4        terms           4   yes    0.333
 14  TOOL-aWrittenMethod-4        naive_terms     4   yes    0.333
 15  TOOL-aWrittenMethod-6        terms           4   yes    0.167
 16  TOOL-aWrittenMethod-6        naive_terms     4   yes    0.167
 17  TOOL-aUnmannedHelm-10        terms           2   yes    0.125
 18  TOOL-aUnmannedHelm-10        naive_terms     2    no    0.125
 19  TOOL-aMouldedFolio-1         terms           1   yes    0.167
 20  TOOL-aMouldedFolio-1         naive_terms     1    no    0.167
 21  TOOL-aUnmannedHelm-9         terms           3   yes    0.500
 22  TOOL-aUnmannedHelm-9         naive_terms     3   yes    0.500
 23  TOOL-cFinalBerth-1           terms           3   yes    0.429
 24  TOOL-cFinalBerth-1           naive_terms     3   yes    0.429
slice terms: h=12 R=12
slice naive_terms: h=10 R=12

overlap: max 0.500 mean 0.362  over 24/24 measured  (OVERLAP_MAX 0.60)
derivation: h=22 R=24  (h-1)/(R-1) = 0.9130  declared RECALL_FLOOR 0.86
check-recall: AUDIT RED -- question 22 declares hits=False and measures True in slice naive_terms

ok   a TAUTOLOGICAL fixture reds the overlap audit — copied text overlaps ~1.0 and reds — the property is a gate, not a sentence
ok   a fixture whose declared `hits` disagrees with the measurement reds — the hand-kept column is documentation a gate keeps honest, per slice
ok   a served fixture missing a term list, or one outside TERM_BAND, REFUSES naming the question — REFUSED, naming question 4: no naive_terms, short terms
ok   the kit payload WITHHOLDS all three gov-only files — 3 withheld, adopter still shipped (11 files in the ** pool)
ok   the overlap audit reds NOT MEASURED on an unresolvable target, never a passing 0.000 — row 10 NOT MEASURED, red, and excluded from max/mean
ok   the overlap audit MEASURES a chunks pin instead of reading 0.000 across the board — 12/12 measured under a chunks pin — the guard is live for both sets
ok   a failed extraction REFUSES with exit 2, not a traceback at exit 1 — exit 2 and REFUSED — not exit 1, which reads as a floor regression
ok   a question with no `query` REFUSES by index, not KeyError three branches later — REFUSED naming the 1-based index
ok   rm3 is seed-stable (S3 / AC1) — identical across 5 seeds
ok   spec-probes: a root with no section-10 probe prints DEAD PROBE at the harvest — exit 1, DEAD PROBE at the harvest
ok   spec-probes: a question with an apostrophe across a wrap parses whole — question whole through the apostrophe; section-10 id excluded

23/24 arms green
```
