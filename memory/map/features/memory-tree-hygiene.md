# memory-tree hygiene engine — the 21-check gate over the memory tree

```toml
feature = "memory-tree-hygiene"
title = "check-memory-hygiene.sh: the memory tree's structural gate, its per-class size caps, and the epoch that dates its verdicts"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aRelaxedShard-1", "TOOL-aWidenedGuide-1"]

[claims]
gate-legs = ["memory hygiene", "memory-hygiene self-test", "verdict epoch (kit version dates the engine)", "verdict-epoch self-test", "kit version markers", "kit/dogfood doc parity"]
kits = ["memory-tree"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/memory-tree/check-memory-hygiene.sh",
  "tools/memory-tree/check-memory-hygiene.test.sh",
  "tools/memory-tree/check-verdict-epoch.sh",
]
```

## What it is

One shell engine over the tracked contents of `<MEMORY_ROOT>/`, 22 checks, plus the epoch rule that
makes its verdicts datable. Checks 9 and 13-21 delegate to sibling Python modules
(`gen_build_index.py`, `corpus_ids.py`, `gotchas.py`, `row_grammar.py`); this dossier owns the engine,
its self-test and the epoch, not those modules.

The engine is COPY-INSTALLED as a standalone directory, so it carries the python resolver inline and
derives its own prefix. It never reads its identity from a project conf: `KIT_MEMORY_TREE_VERSION` is
set in the file, because a project conf must not be able to spoof which engine graded a tree.

## The size caps — four classes, one line bound

Check 6 is the part that moves most, so it is the part worth writing down.

| class | byte bound | line bound |
|---|---|---|
| `guides/*.md` | 60 KB (hardcoded) | 750 |
| `builds/*/README.md` | 25 KB (hardcoded) | none |
| `<MAP_ROOT>/features/*.md` | `DOSSIER_CAP_BYTES` | none |
| every other row document | `ROW_DOC_CAP_BYTES` | none |

`cl = 0` in the awk means the class has NO line bound, and the comparison is guarded
(`b>cb || (cl>0 && l>cl)`) so a zero can never read as "everything is over". The message splits on the
same variable, printing one bound or two.

**Both byte bounds are DECLARED and neither can be switched off.** They pre-set to the kit default,
the conf is sourced OVER that, and then a helper re-normalises: blank resolves FORWARD to the default
rather than skipping the check, and a non-numeric or zero value refuses with `exit 2` naming the key.
That is deliberately the OPPOSITE of every measured pin in the same conf block, where blank means
skip — because a cap an adopter can disable by emptying a line is a gate that reports green for a tree
nobody is checking, and `project/curation-debt.txt` is already the deliberate per-file exemption.

**The dossier selector is guarded on a non-empty prefix.** `index(f, "")` is 1 for every string, so an
unguarded dossier branch resolves to a bare prefix in a tree with no codebase map and hands the
DOSSIER bound to the whole tree — silently undoing the row cap. Check 7's `ex7` adds its map
alternatives under the same emptiness guard for the same reason.

## Constraints & why

**The row line bound is retired, and that was a decision rather than a tidy-up.** At check 7's
300-char entry budget a 250-line row document may hold 75,000 B, so the byte figure decided every real
case and the line figure needed rows averaging under 82 B — measured on this corpus's backlog rows at
253.7. But it DID bind: over check 6's 29-member row class, 22 sat below the 81.92 B/line break-even
and were line-bound first, every codebase-map dossier among them. `TOOL-aWidenedGuide-1` had refused
to triple the row allowance for exactly that reason. `TOOL-aRelaxedShard-1` reverses that refusal
after the owner was shown the population, and buys the dossier sub-population its own tighter bound so
the relaxation lands on the backlog shards and the decision log that asked for it.

**The byte axis had never been armed.** Every check-6 fixture in the suite was a line-axis
construction, so the bound that actually fires in production had no test behind it. Retiring the row
line bound made fixing that mandatory rather than merely worthwhile, because the one row-class fixture
carried three contracts asserted THROUGH check 6 naming it — that `RUN.md` enters `index_set` at all,
that check 7 exempts it, and the per-class scoping control — and all three would have gone quiet
together while every arm still passed.

**A verdict has an epoch.** The kit version dates what the engine decided, so a diff moving a
non-comment line of the engine must move `KIT_MEMORY_TREE_VERSION` too; `hygiene-parity.test.sh`
derives its baseline floor from that constant, and a stale one put the floor before the change.

## Shared seams

- `.memory-tree.conf` — the one declaration both this engine and the sibling Python modules read.
  The engine's own keys pre-set defaults and the conf is sourced OVER them, which means a blank line
  OVERRIDES a default with blank. Every measured pin uses that as "skip this check"; the two cap keys
  must not be skippable, so they are re-normalised after the source instead. Anything adding a
  non-skippable key to this file needs the same step, and inherits the same trap if it forgets.
- `MAP_SUB` — resolved once, near the top, from `.codebase-map.conf`'s `MAP_ROOT` and only when that
  root is a DIRECT child of the memory root. Both check 6's dossier class and check 7's `ex7`
  exemption key on it, and both guard it for emptiness, because an empty prefix matches every path.
- `--print-index-set` — the engine OWNS the index-set and read-path populations, and `corpus_ids.py`
  asks for them through this print mode rather than re-deriving them. A transcription of either would
  be the drift class the kit exists to remove.
- `KIT_MEMORY_TREE_VERSION` — read by `check-verdict-epoch.sh`, `check-kit-versions.sh` and
  `hygiene-parity.test.sh`, and mirrored as a `gov:kit memory-tree@<v>` marker in every shipped
  template. One constant, four consumers.

## Reuse affordance

seam: the CAPTURE-BEFORE-SOURCE idiom — reuse for any conf key that must NOT be disableable by
blanking its line. `check-memory-hygiene.sh` stashes the shipped value in `_SPEC10_SHIPPED` before the
conf is sourced, and restores it afterwards with `: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"`. Anchored on
those two NAMES rather than on line numbers, which move under any edit above them.
seam: the `cl = 0` sentinel plus the guarded comparison — reuse for adding a size class that bounds
bytes only; extend by adding a branch to the awk after the class it must override, and nothing else:
the message split reads the same variable, so a new class gets the right output for free.
seam: `--print-index-set` — reuse for any sibling that needs this engine's population instead of
guessing it; extend by adding a print mode beside it rather than exporting the variable.

## Gaps

- The `builds/*/README.md` class at 25 KB has no byte-axis arm either — `TOOL-aRelaxedShard-2`. A
  class whose ONLY bound is bytes is currently unarmed.
- Checks 6 and 7 measure RAW working-tree bytes, so an adopter without the `eol=lf` pin gets a
  platform-dependent cap: a CRLF checkout adds one byte per line — `TOOL-aRootedPrefix-3`.
- Check 10 resolves a rotated index's live counterpart by fixed path, so it is blind to every
  `backlog/*.md` shard — `TOOL-cTracedPromise-6`.
