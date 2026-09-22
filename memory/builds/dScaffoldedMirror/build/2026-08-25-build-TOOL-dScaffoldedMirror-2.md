# TOOL-dScaffoldedMirror-2 — build record

**Serves:** journal TOOL-dScaffoldedMirror-2

Node `d`, 2026-08-25, base `500a5db6`, unattended run `dScaffoldedMirror`. Spec:
`../spec/2026-08-24-spec-dScaffoldedMirror-2.md`, built at rev-3.

## Result

The gate now says what it measured. Before, a green run printed a file count and the coverage modes
and nothing else:

```
lexicon OK — 896 tracked file(s); coverage: .js=probe, .py=parser, …
```

After:

```
lexicon: P1 verb   graded=832 offenders=463 waived=0
lexicon: P2 suffix graded=37 offenders=0 waived=0
lexicon: P3 layer  graded=509 offenders=0 waived=0
lexicon: armed but grading nothing (reported, not a refusal): .js suffix=0
lexicon OK — 915 tracked file(s); coverage: …
```

`graded` is keyed on (extension, PREDICATE). The fold this replaces summed functions and types into
one number, so `.js` reported a healthy 89 while P2 graded **zero** JavaScript classes and nothing in
the output could say so.

## The refusal that rev-1 wanted, and why it is a report

rev-1 made an armed pair grading nothing a RED. Two measurements killed that, and both are in the
spec's §4. It fires on an honest tree — this repo genuinely writes no JavaScript classes, which is
permanent — and its only reachable discharge was declaring all of `.js` dark, which deletes 45 real
P1 offenders to buy a green bar. Meanwhile the defect it was written for, an extractor gone inert, is
already owned by the frozen SENTINELS fixture, which can tell inert from genuinely-none where a
single tree cannot.

That dissolved the spec-set review's B4 rather than answering it: no pair-level `LANGS` grammar is
needed, so the unit stayed Tier-1 and touched no shared contract.

## `--measure` can fail now

It printed UNDECLARED EXTENSIONS, DEAD PROBE, UNSELECTIVE LAYERS RULE and STALE WAIVERS as `# NOTE:`
comments under an unconditional `return 0`. Three later units use it as a discharge probe, and a
probe that cannot fail discharges nothing.

## Both mechanisms observed RED under a staged break

Removing the empty-pair report reds `armed but empty: the (extension, predicate) pair is NAMED` and
`…the wording says it is not a refusal`, and leaves the third arm of that group green — correctly,
since it asserts the exit code, which the break does not touch. Restoring `--measure`'s unconditional
0 reds `--measure exits NON-ZERO over an undeclared extension`. 90 arms green restored.

**Evidences:** TOOL-dScaffoldedMirror-2
- AC1 — `python tools/lexicon/lexicon.py` — output carries `armed but grading nothing (reported, not a refusal): .js suffix=0`, exit code unchanged at 0
- AC2 — `python tools/lexicon/selftest.py` — `the suffix population is derived: a class makes it non-zero`, a fixture adding `class Widget {}` moving `.js suffix` from 0 to `P2 suffix graded=1`
- AC3 — `python tools/lexicon/lexicon.py` — three `graded=/offenders=/waived=` lines on a GREEN run, armed as `counts on GREEN: every predicate reports graded/offenders/waived`
- AC4 — `python tools/lexicon/lexicon.py --measure` — exit 1 with a staged `.R` file in the corpus, exit 0 with it removed; armed as `--measure exits NON-ZERO over an undeclared extension` and observed RED under a restored unconditional 0
- AC5 — amended rev-3 — the criterion still said "AC1's refusal" after rev-2 made AC1 a report, a spec disagreeing with itself one section apart; the arms cover the report and its derivation, and both were observed RED under a staged break
- AC6 — `bash tools/lexicon/adopt-lexicon.sh --check` — exits 0 with unchanged output; this unit does not touch the adoption path
