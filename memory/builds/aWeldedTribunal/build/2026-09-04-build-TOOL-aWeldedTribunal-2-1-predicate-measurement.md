# Candidate-predicate measurement, before any of the three predicates was wired

**Serves:** journal TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-4

The charter's §7 rule: run a candidate gate predicate over the real tree before wiring it, and print
hits AND near-misses. Run on node `a`, 2026-09-04, at `4fc4aeb3`, over the 8 tracked `*.js` files.
All three probes READ only; nothing was built.

## Unit 1 — the widened loop-header predicate

Candidate: `/\b(?:for(?:\s+await)?|while)\s*\(|\bdo\s*\{/` against today's `/\b(for|while)\s*\(/`.

**Lines the new predicate matches and the old one does not: ZERO, across all 8 files.**

That is the strongest evidence a widening can have. Nothing currently admitted becomes denied,
because nothing in the tracked corpus is written in either new shape. The widening reaches only the
two evasion spellings, which is what it was written for.

## Unit 2 — the growth vocabulary, and a REAL defect in the spec it was drafted from

Unit 2 rev-1 proposed reusing the file's existing right-hand-side growth vocabulary —
`concat`, `push`, `flat`, `flatMap`, `fill`, `repeat` — as the RECEIVER mutation vocabulary, on the
stated ground that two growth vocabularies in one file is the `two-answers-to-one-question` class.
The measurement refutes that:

| Vocabulary | Hits | Distinct receiver names |
|---|---|---|
| the RHS list applied to a receiver | 44 | 10, including `ALL_LENSES.concat` and `lexed.concat` |
| methods that actually GROW a receiver (`push`, `unshift`, `splice`) | 42 | 8, neither of those two |

`concat`, `flat` and `flatMap` are NON-MUTATING: they return a new array and leave the receiver
exactly as long as it was. Applying the RHS list to a receiver would therefore take the bound back
from `ALL_LENSES` — a shipped lens array — on the strength of a `.concat` that changes nothing.
That is the false-denial class this very rule exists to catch, and it caught it before a line was
written.

**The two vocabularies are DIFFERENT because they answer different questions.** The RHS one asks
"can this expression PRODUCE something bigger", where `concat` qualifies. The receiver one asks
"does this statement GROW the array named", where it does not. Unit 2's §4 claim that they should
share one source is wrong and is folded at rev-2; what they may share is the note explaining why
they differ.

### The one receiver at risk, and why no harness reds

`tools/workflows/drift-audit-code.js:275` binds `const indexed = []` and grows it at `:277`. Under
the corrected sweep `indexed` loses its bound. Nothing fans over `indexed`: the fan at `:341` is over
`batches`, bound at `:338` from `indexed.length ? chunk(indexed, Math.ceil(indexed.length / MAX_VERIFIERS)) : []`,
whose two branches are a bounded split resolved through `boundedK` and an empty literal. Neither
branch depends on `indexed` being in the bounded set, so the harness is unaffected.

### Baseline, so the build pass has something to compare against

Every tracked harness piped to the SHIPPED hook, before any change:

```
check-workflow-syntax.js  exit=0
drift-audit-code.js       exit=0
drift-audit-state.js      exit=0
tier2-review.js           exit=0
unattended-build.js       exit=0
```

All five must still exit 0 after units 1, 2 and 3 land. This is unit 2's AC4 and unit 1's AC4, and
the baseline is recorded here so "it still passes" is a comparison rather than a recollection.

## Unit 4 — the criterion's population

Predicate: a harness BINDS a liveness counter (`lensesDead` or `skepticsDead`) and is asserted to
carry the literal `RUN INTEGRITY`.

```
tools/workflows/drift-audit-code.js    binds-counter=yes  RUN-INTEGRITY=yes
tools/workflows/drift-audit-state.js   binds-counter=yes  RUN-INTEGRITY=yes
tools/workflows/tier2-review.js        binds-counter=yes  RUN-INTEGRITY=NO
```

Three of eight tracked `*.js` are in the population and exactly one is red — the file unit 4 names.
The five outside it are the negative arm's real population, so unit 4's AC4 is measurable rather
than hypothetical.
