# aTunedCompass — the acceptance ledger for unit 5

**Serves:** journal TOOL-aTunedCompass-5

*Node `a`, 2026-09-05, written by the unattended run that built the unit, immediately after the
observations were taken rather than reconstructed later.*

Every line below is `OBSERVED` with the command that made it, or `AMENDED` naming the revision that
changed the criterion. There is no third form.

## The staged break, because it is the load-bearing part

Three of the four new self-test arms were observed RED against the SHIPPED behaviour before the fix
was accepted, then GREEN after it. The break was staged by making the directory segment mandatory
again in all three `DURABLE` alternations, reverting the family alternation to the literal
`(DECISIONS|BACKLOG)`, and deleting the diagnosis call — i.e. reconstructing the shipped file
exactly, not a simplified stand-in.

Observed RED under that break:

```
FAIL spine is NON-EMPTY on a FLAT memory root — spine is EMPTY on a flat root
FAIL DURABLE is DERIVED from FAMILIES — the alternation is a literal
FAIL an empty spine beside non-empty records ANNOUNCES itself — the silent empty stayed silent
ok   spine is still NON-EMPTY on a NESTED root — nested root yields 2 spine doc(s)
```

The nested arm is GREEN in both states by design: it is the no-regression arm, and an arm that only
passes after the change would not be testing that the widening kept the old layout working.

**One caveat a later reader needs.** The first attempt at staging this break silently did nothing to
two of the three constructs, and its own report said it had succeeded — it printed a match COUNT
rather than what it had replaced, and the file holds CRLF, so a multi-line replacement never matched.
Under that non-break two arms passed and would have been recorded as "observed red" on the strength
of a message. They were re-run against a verified break instead. The class is this repo's own
`fixture-passes-by-finding-nothing`, one level up: the instrument that stages a break has to be
checked as carefully as the arm it arms.

## Evidences

**Evidences:** TOOL-aTunedCompass-5

- AC1 — `python tools/memory-recall/extract.py . <tmp>` — `spine 755 docs, 378576 indexed chars` and
  `ids anchored 708 (durable home: 633)`, against `spine 0 docs` and `durable home: 0` at BASE.
  Stderr was silent, which is the correct behaviour for a non-empty spine. The spec's §4 predicted
  748 documents; the measured 755 is that figure plus the records this build's own commits added to
  the corpus while it ran, and the difference is reported rather than smoothed.
- AC2 — the candidate predicate was run standalone over `git ls-files -- memory` BEFORE it was
  wired: 9 hits — `memory/DECISIONS.md`, the four `memory/backlog/<FAMILY>.md` shards, and the four
  rotated `memory/archive/` indexes — with **0 near-misses** among index-shaped basenames and 0
  files admitted that are not index-shaped. The shipped pattern scored 0 hits on the same 1325
  files.
- AC3 — `python tools/memory-recall/selftest.py` — the nested-layout arm reports `nested root yields
  2 spine doc(s)`, so the widening did not trade one layout for the other.
- AC4 — same suite — the derivation arm reads `DURABLE.pattern` out of the module under two stub
  confs and asserts the compiled patterns DIFFER, that each declared family appears in its own, and
  that an undeclared family appears in neither. Observed RED against the literal alternation.
- AC5 — same suite, arm `test_empty_spine_is_loud` — it builds a corpus whose records anchor in a
  file no alternation admits, then asserts exit 0, `spine 0`, and `EMPTY SPINE` on stderr naming
  `DURABLE` and the resolved `MEMORY_ROOT`. Observed RED against the shipped extractor, which said
  nothing at all in that state.
- AC6 — `python tools/memory-recall/test_recall_floor.py` — `20/20 arms green`. The empty-graded-set
  arm no longer names `spine`: it empties `records` synthetically through `build_filtered(drop=lambda
  r: True)` and pins the floor over `records`, reaching the same `is EMPTY` refusal in
  `check-recall.py`. That arm previously passed BECAUSE of the defect this unit fixes, so it went red
  on the fix and had to stop depending on a live bug.
- AC7 — `bash tools/check-kit-versions.sh` — exit 0 with `KIT_MEMORY_RECALL_VERSION` at `1.7`.
  **Three carriers, not one:** the constant in `recall_conf.py`, the `gov:kit memory-recall@` marker
  in that same file's header, and the one in `README.md`. The suite caught the second after the first
  and third were moved, which is the recorded "stamps are not one stamp" trap.

## Suites, in full

- `python tools/memory-recall/selftest.py` — **43/43 checks passed**, including the four new arms.
- `python tools/memory-recall/test_recall_floor.py` — **20/20 arms green**.
- `bash tools/check-kit-versions.sh` — exit 0.
- `python tools/codebase-map/gen_map.py --check` — exit 0 after `--write` regenerated
  `memory/map/generated/symbols.json`, which the new module-level function moved.
- `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0.

Both suites are `subject = kit` / `chunk = selftests` and are held off an ordinary bar, so they were
run ON DEMAND, directly, which is what §7 requires the record to state.
