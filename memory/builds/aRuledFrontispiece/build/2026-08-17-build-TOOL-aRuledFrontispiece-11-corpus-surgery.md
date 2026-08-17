# aRuledFrontispiece-11 — the corpus surgery, file by file

**Serves:** journal TOOL-aRuledFrontispiece-11

A 6-file authored diff is not reviewable from the diff alone, so this is the record spec 11's S6
requires. It states what moved, what did not, and how conservation was proved.

## The population, derived not chosen

`python tools/memory-tree/gen_build_index.py --check-format` named the files. Six of 39 tracked build
READMEs violated the slot contract. That is fewer than the 14 an earlier hand estimate produced,
because that estimate used a heuristic — authored headings between a roster heading and the generated
open — which is not the predicate the contract actually states. The predicate has two triggers and
only those two files count.

## What moved

| File | Lines moved from after the regions | Lines moved from between the plan pair and the regions |
|---|---|---|
| `aRuledFrontispiece/README.md` | 180 | 0 |
| `aSiftedPlaybook/README.md` | 120 | 0 |
| `aStandingWrit/README.md` | 0 | 74 |
| `aTimedTurnstile/README.md` | 10 | 0 |
| `cKeyedLaunchpad/README.md` | 11 | 0 |
| `cTracedPromise/README.md` | 23 | 0 |

`aStandingWrit` is the only file exercising the second trigger, and it is the file that made the
trigger necessary: it carries the corpus's one landed `roster:units` pair, and 74 lines of authored
prose sat between that pair's close and the generated open. A predicate with only the first trigger
would have passed it, and the slot contract would have shipped with a hole in exactly the shape of
the one file that already used the feature.

## What did NOT move

No authored text was rewritten. Sections moved as blocks and kept their relative order. No generated
byte changed: `--check` reports the same clean verdict and the same artifact count at this unit's tip
as at its parent, so the regions were relocated intact rather than re-rendered into a new shape.

Prose that sat between the plan pair and the regions moved ABOVE the plan pair, not below the
regions. The plan stays adjacent to the generated surface, which is what makes the slot order read as
one authored block followed by one machine-owned block rather than as an alternation.

No `roster:units` pair was ADDED. Spec 11 S2 anticipated wrapping authored plans across the corpus,
and the derived population for that operation is empty: `--check-format` cannot identify an authored
plan that is not already wrapped, and an unwrapped plan is legal under unit 1 S5. Inventing the
boundary per file is the judgement S4 refuses to make, so the twelve candidate rosters keep their
no-pair branch. **This is a scope item that did not fire, recorded rather than quietly dropped**, and
it is the open half of P6 in the build README.

## How conservation was proved

Per file, the multiset of non-blank lines before and after is byte-identical:

```
git show HEAD:<file> | grep -v '^$' | sort | md5sum
grep -v '^$' <file>  | sort | md5sum
```

All six matched. A diffstat cannot show this — a move reads as balanced additions and deletions
whether or not a line was altered in transit — so the hash over the sorted multiset is the arm that
actually distinguishes a relocation from a rewrite.
