# What bash actually does with the two spellings, and a STALE claim the backlog row carried

**Serves:** journal TOOL-aWeldedTribunal-5

Run on node `a`, 2026-09-04, at `711c4c50`. Both probes READ only.

## The reference behaviour, measured rather than assumed

The python half is the copy and bash is the format, so the correct answer is whatever bash gives.
Sourcing a fixture holding all three cases:

```
MEMORY_ROOT=memory   # note      ->  MEMORY_ROOT=[memory]
export FAMILIES="TOOL DEPL"      ->  FAMILIES=[TOOL DEPL]
QUOTED="a # b"                   ->  QUOTED=[a # b]
```

All three confirm the spec's §4 design. The third is the one that matters most, because it is the
case a careless fix breaks: an unconditional `#`-strip would turn `a # b` into `a`, which is a
SILENT WRONG VALUE where the current bug is at least a loud directory miss. The strip must run only
on an unquoted `#`, before the quote peel.

## A STALE CLAIM, carried from the backlog row into the spec

`TOOL-aScouredKit-19` closes with: *"`gotchas.py` already imports `corpus_ids.py`, so routing all
five through one parser costs no new coupling."*

**That is false against this tree.** `grep -n corpus_ids tools/memory-tree/*.py` returns hits only
inside `corpus_ids.py` itself — its own docstring and its own error strings. The complete import
graph among the five readers is ONE edge:

```
row_grammar.py  ->  gen_build_index.py   (from gen_build_index import unfenced_lines)
```

`gotchas.py`, `gen_build_index.py` and `check-arms.py` import nothing from any sibling.

### What survives and what does not

The MECHANISM survives: `row_grammar.py:38-39` demonstrates the `sys.path.insert` plus sibling
import pattern in this kit, so the four new callers need no packaging change and follow an
established local precedent. `corpus_ids.py` is still the right home, because it is the reader that
already holds `load_conf` and the widest defaults set.

The JUSTIFICATION does not survive. The change adds four import edges where the row promised zero,
and unit 5 rev-2 says so rather than repeating a sentence the tree contradicts. Four edges inside
one kit directory, all pointing at the module that already owns the conf, is still the right trade —
but it is a trade, and the row presented it as free.

This is the §10 rule doing its job: a hit can be STALE, so verify any claim about current code
against source before building on it, and say where the two disagreed.
