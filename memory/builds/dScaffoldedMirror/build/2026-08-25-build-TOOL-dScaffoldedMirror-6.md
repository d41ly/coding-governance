# TOOL-dScaffoldedMirror-6 — build record

**Serves:** journal TOOL-dScaffoldedMirror-6

Node `d`, 2026-08-25, base `500a5db6`, unattended run `dScaffoldedMirror`. Spec:
`../spec/2026-08-24-spec-dScaffoldedMirror-6.md`, built at rev-4.

## Result

The one-string edit that empties a graded population is now visible twice — as a number that moves,
and as a finding that names the move.

```
lexicon: coverage — armed 54 of 128 definition-carrying file(s) (42.2%)
```

Flip `py` from `parser` to `dark` and that reads `10 of 128 (7.8%)`; rev-1 predicted 7.9% from a
different measurement. With no marker beside the `LANGS` line, `drift-audit` reports:

```
.lexicon.conf: LANGS .py moved parser -> dark, which WEAKENS coverage, with no justification beside it.
```

With `# py: parser -> dark, <reason>` above that line, it is silent.

## What the floor's removal cost, and what replaced it

rev-2 cut `COVERAGE_FLOOR` on the owner's ruling: a conf scalar in a build whose thesis is that the
raisable ceiling is the defect. The NUMBER survived and the VERDICT built on it did not. What now
catches a weakening is S5, which is DERIVED from two committed trees rather than compared against an
authored integer — the same distinction that decided `TOOL-dScaffoldedMirror-7`.

**One case is genuinely ungated as a result, and the spec says so rather than implying otherwise.**
An extension declared `dark` from its first appearance rises from absent to 0, so S5 correctly sees
no weakening — yet it lowers coverage exactly as a flip does. rev-1 gave that case to the floor. It
is now visible in the printed fraction and gated by nothing.

## Three defects found by building, two of them mine

**`DEAD SNIFFER` could not fire.** It appended to `problems`, a list already printed and already
folded into `exit_code` forty lines earlier, so blinding the sniffer left the run at exit 0. Found by
staging the break; the code reads correctly.

**S6's liveness asserted the wrong thing.** rev-1 wanted "some dark extension carries a definition",
which reds an honest adopter whose dark extensions are all data files — the same defect
`TOOL-dScaffoldedMirror-2` had to fix in `DEAD PREDICATE`, met a second time in one build. It now
asserts AGREEMENT between two independent readings: every file an armed extractor found a definition
in must also sniff positive.

**The sniffer counted documentation.** Fenced code blocks put 82 `.md` files into the denominator and
reported 25.7% against a true 42.2%. A coverage number that moves when somebody writes a tutorial is
not measuring coverage.

## Recorded because it changes how the result reads

`lexicon_verbs_declared_but_unused` already fired INDIRECTLY on a dark flip — 0 → 14 over pin 3 —
so the move was not wholly unguarded before this unit. That signal reports unused VERBS rather than
lost coverage, and it would stay quiet on a small table where few verbs go unused. S5 names the move
itself, which is the difference between a symptom and the thing.

**Evidences:** TOOL-dScaffoldedMirror-6
- AC1 — `python tools/lexicon/lexicon.py` — prints `coverage — armed 54 of 128 definition-carrying file(s) (42.2%)` and exits 0, against rev-1's predicted 54 of 126 (42.9%)
- AC2 — `python tools/lexicon/lexicon.py` — with `py:python-ast:dark` staged, the same line reads `armed 10 of 128 (7.8%)`, proving the fraction is derived; exit code unchanged, the move being S5's to catch
- AC4 — `python tools/drift-audit/drift_report.py --check` — reports `LANGS .py moved parser -> dark` with no marker and is silent with `# py: parser -> dark` above the line; both directions armed in `tools/drift-audit/selftest.py` as `test_lang_mode_ratchet`
- AC6 — `python tools/lexicon/selftest.py` — `S6: a BLIND sniffer reds as DEAD SNIFFER rather than reporting perfect coverage`, staged by blinding the sniffer inside a fixture copy of the kit; observed rc=1 on the live tree before the arm was written
- AC7 — amended rev-4 — rev-1 named `run-gates.sh`; the five legs it cares about were run directly, the full bar being a push-boundary run in this repo's own model rather than a per-unit cost (§9 rev-4)
