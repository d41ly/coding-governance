# The convention predicate, observed RED

**Serves:** research TOOL-aSurfacedLexicon-1

The research pass ASSERTED that the shipped idiomatic convention defaults cost zero on identifiers in
this repo. An assertion about a predicate nobody has run is the shape §7 exists to refuse, so this
record is the run. Prototype only — it lives in the session scratchpad, lands nothing, and is folded
in below so the numbers can be reproduced without it.

Measured 2026-09-04 on node `a`, worktree `lexicon-tool-rebuild-b95399`, at `d0a18683`.

## What was observed

| State | py.function | py.type | py.file | js.function | js.type | sh.file | verdict |
|---|---|---|---|---|---|---|---|
| tree as-is | 0/925 | 0/39 | **7**/47 | 0/100 | 0/**0** | **4**/89 | RED · 11 violations · 1 dead cell |
| `_conv_break.py` staged | **1**/926 | **1**/40 | 7/48 | 0/100 | 0/0 | 4/89 | RED · 13 violations |
| unstaged | 0/925 | 0/39 | 7/47 | 0/100 | 0/0 | 4/89 | RED · 11 violations · back to baseline |

The staged break was two definitions, `def loadUserData` and `class user_record`. Both were caught,
and the message names the convention the name DOES satisfy rather than only the one it misses:

```
VIOLATION  loadUserData  satisfies camel, not snake
VIOLATION  user_record   satisfies snake, not pascal
```

That phrasing is the design's advice half in miniature. The measured defect in the shipped kit is
that it refuses without advising — `--suggest` names a replacement for only 5 of 23 debt tokens — and
a convention violation is the one class where the tool always knows the answer, because the name
already tells it which cell it was written for.

## The three things this run establishes that the research could not

**The predicate has teeth.** Re-grading `py.function` as camel violates 691 of 925. A cell that only
ever passes is an assertion about nothing; this one fails on demand, and the alternate-cell count is
printed on every run rather than being a thing somebody once checked.

**The set-valued classifier is load-bearing, not defensive.** 245 of 1064 graded identifiers satisfy
two or more conventions. A classifier returning a single label would report a violation for every one
of them the moment the declared cell was not the label it happened to pick. This is the difference
between a predicate that ships and one that gets waived in its first week.

**The DEAD CELL refusal fires today, from the tree, with nothing staged.** `js.type` is declared and
armed and its population is 0 — 11 tracked `.js` files, no classes. That is `TOOL-dScaffoldedMirror-2`'s
green-by-absence class caught by construction rather than by a reviewer noticing, and it is U5's
acceptance check already observable before U5 exists.

## Where the prototype is weaker than the design, stated rather than hidden

- **`js.function` graded 100, the research measured 122.** The prototype's JS extraction is two
  regexes over `function <name>` and `class <name>`; it does not see `const f = () =>` or method
  shorthand. The real kit's `js-regex` pattern set does. The zero-violation result for that cell is
  therefore measured over a SUBSET, and the 22 unseen definitions are unproven either way. This is
  the same green-by-absence class the DEAD CELL arm above catches, one level down, and it is why U8's
  owner-declarable `PATTERNS:` block is worth building rather than hand-rolling per language.
- **`py.constant` was not graded.** The research measured three defensible populations for it
  (539/419, 432/413, 331/331) and only the third is clean, because the predicate selects its own
  population. Left dark here rather than shipped on a flattering denominator.
- **Filename stems use the first dot.** `foo.test.sh` stems to `foo`. Last-dot stemming disagrees on
  64 graded files and would report all 49 `*.test.sh` scripts as kebab violations. The rule is pinned
  in the probe rather than left to taste, and a first count of mine using last-dot produced 8 and 49
  instead of 7 and 4 — the rule is not cosmetic.
- **The CRLF warning on the staged fixture is real.** `git add` warned that LF would become CRLF for
  `tools/lexicon/_conv_break.py`. A landed `.py` under this predicate needs its `.gitattributes` pin
  like every other execution-sensitive file here.

## Appendix — the probe

Reproduce with `python conv_probe.py` from the repo root. It reads `git ls-files`, so a staged file is
graded and an unstaged one is not; that is what makes the break above stageable.

The two design decisions worth lifting into U4 verbatim:

```python
# Affixes are stripped BEFORE classification, so `_build_index` and `__init__` are snake
# with an affix rather than violations of it. Largest single source of false positives.
_AFFIX = re.compile(r"^(_*)(.*?)(_*)$", re.DOTALL)

def classify(name):
    """The SET of conventions this name satisfies. `run` is snake AND camel."""
    core = read_core(name)
    if not core:
        return set()
    return {k for k, rx in _FORMS.items() if rx.match(core)}
```

A name violates a cell when the declared convention is **not in its set** — never when it is not the
set's first or only member. The six forms are `snake`, `screaming`, `camel`, `pascal`, `kebab`, `dot`,
each a single anchored regex over the stripped core. Populations come from `ast` for Python, two
regexes for JavaScript, and first-dot basename stems for filenames.
