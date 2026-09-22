# TOOL-aWeldedTribunal-5 — one `.memory-tree.conf` parser, read by every python reader

**Status:** CLOSED · rev-3 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aWeldedTribunal-5-1-conf-parse-measurement.md](../build/2026-09-04-build-TOOL-aWeldedTribunal-5-1-conf-parse-measurement.md) | journal | — |
| [2026-09-04-build-TOOL-aWeldedTribunal-5-2-acceptance-ledger.md](../build/2026-09-04-build-TOOL-aWeldedTribunal-5-2-acceptance-ledger.md) | journal | — |
| [2026-09-04-prompt-TOOL-aWeldedTribunal-1.md](../prompts/2026-09-04-prompt-TOOL-aWeldedTribunal-1.md) | research | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md](../reviews/2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round4.md](../reviews/2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round4.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

The python readers in `tools/memory-tree/` each re-implement the `.memory-tree.conf` parse with an
identical naive `v.strip().strip('"').strip("'")`, while the shell gate SOURCES the same file in
bash. A legal spelling bash accepts and the python half mis-reads takes `gotchas.py --check` from
rc=1 to rc=0 over an identical planted violation — coverage removed, not failed closed, gate still
green. Route them all through one parser that agrees with the shell.

## 2. Scope (IN)

- **S1** — One conf parser, exported from `tools/memory-tree/corpus_ids.py`, which already OWNS the
  conf and carries the widest defaults set. It becomes the single reader. It is NOT already imported
  by `gotchas.py` — §4 measures the import graph and prices the four new edges.
- **S2** — It handles the two spellings bash accepts and the current parse does not: an INLINE
  COMMENT after the value (`MEMORY_ROOT=memory   # note`) and an `export ` prefix on the key.
- **S3** — `gotchas.py`, `gen_build_index.py`, `check-arms.py` and `row_grammar.py` call it instead
  of their own copies. Each keeps its OWN defaults dict — the defaults differ per reader and merging
  them would be a scope change nobody asked for — and only the PARSE is shared.
- **S3b** — `corpus_ids.read_declared_keys` is the SIXTH reader and is routed through the same
  parser for its KEYS. It re-partitions the file on `=` at `corpus_ids.py:122-136` and takes
  `line.partition("=")[0].strip()`, so after S2 an `export MEMORY_ROOT=memory` line yields
  `MEMORY_ROOT` from the shared parser and `export MEMORY_ROOT` from this one — the retired-key and
  undeclared-`CHARTER` checks would then disagree with the parser inside a single file. Its own
  docstring says it "cannot drift from it — same file, same rule", which S2 makes false unless this
  item is built.
- **S4** — A fixture covering both spellings, in whichever of the kit's suites owns conf parsing.
  `TOOL-aScouredKit-5` fixed exactly this divergence in the drift-audit copy and its fixture covers
  both spellings; this unit's fixture is modelled on that one.
- **S5** — An arm proving AGREEMENT with the shell half rather than merely proving the python half
  parses: source the fixture conf in bash, read it in python, compare. Two parsers agreeing with
  themselves is `assertion-between-two-derived-values`, which the checklist selects for these files.

## 3. Non-goals (OUT)

- **A general shell parser.** Bash's assignment grammar is larger than this: command substitution,
  parameter expansion, line continuations and quoted whitespace are all legal and none is in scope.
  The two spellings named in S2 are the ones an adopter actually writes and the ones the kit's own
  example neither shows nor forbids. A third spelling discovered later is a backlog row.
- **Changing the conf format or adding keys.**
- **Merging the five readers' DEFAULTS.** They differ deliberately: `corpus_ids` needs the charter
  and the pins, `gotchas` needs the universal budget, `check-arms` needs the arms floors. One
  defaults dict for all five would give every reader keys it has no use for and hide which reader
  actually depends on which key.
- **The drift-audit copy.** `TOOL-aScouredKit-5` already fixed it; that caller is not in this
  unit's population and pulling it in would widen the diff for no defect.

## 4. Design

### Inventory — the copies

| File | Line | Reads | Defaults it carries |
|---|---|---|---|
| `tools/memory-tree/corpus_ids.py` `load_conf` | 118 | values | `MEMORY_ROOT` `DISCIPLINES` `FAMILIES` `CHARTER` and four pins |
| `tools/memory-tree/gotchas.py` | 92 | values | `MEMORY_ROOT` `UNIVERSAL_BUDGET` |
| `tools/memory-tree/gen_build_index.py` | 287 | values | `MEMORY_ROOT` `DISCIPLINES` `FAMILIES` |
| `tools/memory-tree/check-arms.py` | 82 | values | `MEMORY_ROOT` `ARMS_FLOORS` |
| `tools/memory-tree/row_grammar.py` | 93 | values | **none — `conf = {}`, and it RAISES on an absent conf** |
| `tools/memory-tree/corpus_ids.py` `read_declared_keys` | 122-136 | **keys only** | none — it returns a key set |

The value-reading rows hold the identical body: skip blank, skip `#`-leading, skip no-`=`, partition
on the first `=`, strip whitespace then one layer of double quotes then one layer of single quotes.
The key-reading row shares the skip rules and the partition and stops at the key, which is why
rev-1's inventory missed it and why AC6's quote-strip grep cannot see it either.

**`row_grammar.load_conf` IS NOT LIKE THE OTHERS, and rev-2's cell said it was.**
`tools/memory-tree/row_grammar.py:86-94` is `def load_conf(root): conf = {}` with a bare
`read(os.path.join(root, ".memory-tree.conf"))`, and `read` at `:56-58` is a plain `open` — so it
holds NO defaults and RAISES on an absent conf. The other four all open with a populated defaults
dict AND an `os.path.isfile` guard. `MEMORY_ROOT` and `FAMILIES` are keys it READS, not defaults it
carries. This matters because routing it through a shared `load_conf(root, defaults)` carrying the
isfile guard would silently convert today's hard failure on a missing conf into a quiet empty-dict
success — the direction toward silent success, and the opposite of §5's claim that an absent conf
still yields the defaults. AC7 decides it rather than letting the shared parser decide by accident.

**This inventory is the single source for the count.** No criterion in §6 states a number, per the
charter's rule that no count of a derived population is written in prose.

### The shared parser

`corpus_ids.load_conf` grows a `defaults` parameter and the parse moves into a module-level helper
so a caller that wants only the parse can have it without the pins:

```python
def parse_conf(text: str, conf: dict) -> dict:
    """One reader for `.memory-tree.conf`, agreeing with the bash half that SOURCES the same file.

    TOOL-aScouredKit-19. Five readers held this body and none of them handled two spellings bash
    accepts: an `export ` prefix on the key, and an inline `# comment` after the value. Both parsed
    into a VALUE, so `MEMORY_ROOT=memory   # note` walked a directory that does not exist and the
    check went from rc=1 to rc=0 over an identical planted violation. Coverage removed, gate green.
    """
```

### The two spellings, and why an inline comment is stripped only when unquoted

Bash strips an unquoted `#` that begins a word, and does NOT strip a `#` inside quotes: `X="a # b"`
is the three-character-plus value. So the strip runs before the quote peel and only on an unquoted
`#` preceded by whitespace. Stripping it unconditionally would corrupt a legal quoted value, which
is a silent wrong answer where the current bug is at least a loud directory miss.

### Import mechanism

`row_grammar.py:38-39` does `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` and
imports a sibling. The pattern exists, is used, and is what the four value-readers adopt. No
packaging change.

**The backlog row's justification does NOT survive, and the difference is worth stating.**
`TOOL-aScouredKit-19` closes with *"`gotchas.py` already imports `corpus_ids.py`, so routing all
five through one parser costs no new coupling"*. Measured: `grep -n corpus_ids tools/memory-tree/*.py`
hits only inside `corpus_ids.py` itself, and the complete import graph among the readers is the ONE
edge above. So this adds four import edges where the row promised zero. Four edges inside one kit
directory, all pointing at the module that already owns the conf, is still the right trade — but it
is a trade, and the row presented it as free.

### Files touched (estimate)

- `tools/memory-tree/corpus_ids.py` — the shared parser.
- `tools/memory-tree/gotchas.py`, `gen_build_index.py`, `check-arms.py`, `row_grammar.py` — each
  loses its copy and gains the import.
- One fixture and its arm.

### Alternatives rejected

- **A new `conf.py` module.** Rejected: `corpus_ids.py` already owns the conf, and the four import
  edges it needs are priced in §4. Another file to hold twelve lines is scaffolding.
- **Make the shell half match python instead.** Rejected backwards: bash is the reference because
  bash is what the conf format IS. The python half is the copy and the copy is what is wrong.
- **Leave it, since no tracked conf here uses either spelling.** Rejected: this repo ships the kit,
  the trigger is an adopter writing a legal spelling, and a defect latent HERE is live THERE. This
  is the population the kit exists for.

## 5. Production-readiness checklist

- security — N/A — no untrusted input; the conf is a tracked file in the operator's own repo.
- perf / scale — one parse per process, unchanged.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an absent conf still yields the defaults, unchanged.
- observability — the failure this closes was SILENT by construction. The parser cannot announce a
  mis-parse it does not detect, which is why S5's agreement arm is the observability, not a log line.
- risks — the real risk is a behaviour change on a conf that currently parses one way and would
  parse another. No tracked conf in this repo uses either spelling, so the change is a no-op here
  and a fix for adopters; that is asserted by running the new parser over every tracked
  `.memory-tree.conf` and comparing, which AC4 states.
- testing + left-shift gates — S4's fixture and S5's cross-language agreement arm. The class is
  `two-answers-to-one-question`, which the checklist selects for these files.
- migration / rollback — none; no format change, so no adopter has to do anything.
- user docs — the kit README's conf example should show at least one of the two spellings, since
  "the kit's own example neither shows nor forbids it" is half of why this happened.

## 6. Acceptance criteria

- **AC1** — When a fixture conf holding `MEMORY_ROOT=memory   # note` is read by every reader in
  §4's inventory, each returns `memory`. Today every value-reading one of them returns
  `memory   # note`.
- **AC2** — When a fixture conf holding `export MEMORY_ROOT=memory` is read by every reader in §4's
  inventory, each yields the key `MEMORY_ROOT`. Today every one of them yields `export MEMORY_ROOT`,
  `read_declared_keys` included.
- **AC2b** — When that same fixture is read, `corpus_ids.read_declared_keys` and
  `corpus_ids.load_conf` agree on the key set. This is S3b, and it is the one criterion that catches
  a build that routes the four value-readers and leaves the key-reader behind.
- **AC3** — When the planted violation of `TOOL-aScouredKit-19`'s reproduction is staged under a
  conf carrying the inline comment, `python tools/memory-tree/gotchas.py --check` exits `1`. It
  exits `0` today, which is the whole defect: coverage removed rather than failed closed.
- **AC4** — When the new parser is run over every tracked `.memory-tree.conf` in this repo and
  compared against the current parse, the results are identical. The change is a no-op here.
- **AC5** — When a fixture conf is SOURCED in `bash` and read by `corpus_ids.parse_conf`, the two
  agree on every key. This is S5, and it is what makes the arm a cross-language check rather than a
  tautology between two values the same code derives.
- **AC6** — When `grep -c "strip('\"')" tools/memory-tree/*.py` is run, one copy remains. This
  criterion CANNOT see `read_declared_keys`, which carries no quote strip — AC2b is what covers that
  reader, and saying so here is cheaper than a later reader assuming this grep is the whole audit.
- **AC7** — When every reader in §4's inventory is run against a fixture root holding NO
  `.memory-tree.conf`, each behaves as §4 documents: the four guarded readers return their defaults,
  and `row_grammar.load_conf` does whatever this unit decides — it RAISES today, and the shared
  parser must not change that by accident. One arm makes the difference a fact rather than a table
  cell.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the `memory-hygiene self-test` leg, which
is `subject = kit` in `tools/gate-legs.json` and is therefore held as `ondemand` by
`tools/run-gates/run-gates.sh:947` on the plain bar. A leg's GUARD scopes a RUN; the subject and
chunk decide whether the leg runs at all, and rev-1 reasoned from the wrong one. `AGENTS.md` records
that no boundary sets `GATE_SELFTESTS` (owner, 2026-08-27) and that a DoD owes the full pair for KIT
work, which this is. The plain bar still covers the repo-subject memory-tree hygiene legs, which are
what actually grade this repo's own tree.


**The FULL PAIR, not half of it.** `AGENTS.md:488` spells the DoD command for KIT work as
`GATE_FULL=1 GATE_SELFTESTS=1`; `GATE_SELFTESTS=1` alone lifts the `ondemand` hold but leaves every
per-leg GUARD in force, so kit legs outside the touched directory stay held with no `skipped` line
saying which. Rev-2 cited the pair and prescribed one half of it.
## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. All five value-parsing copies confirmed present at the lines
  §4 tabulates, by `grep -c` over each file.
- rev-2 · 2026-09-04 · folded the pre-wiring measurement and spec-audit round 1 (H7, H10, L1).
  **The measurement** confirmed bash's behaviour on all three spellings, including that a quoted
  `#` must survive, and REFUTED the backlog row's claim that `gotchas.py` already imports
  `corpus_ids` — the complete import graph among the readers is one edge, `row_grammar` to
  `gen_build_index`. The mechanism survives; the "costs no new coupling" justification does not, and
  §4 no longer repeats it. Recorded at
  `memory/builds/aWeldedTribunal/build/2026-09-04-build-TOOL-aWeldedTribunal-5-1-conf-parse-measurement.md`.
  **H10, high:** `corpus_ids.read_declared_keys` is a SIXTH reader living in the host module, absent
  from rev-1's inventory and from every non-goal. After S2 it would disagree with the shared parser
  on keys inside one file — a new two-answers-to-one-question created by the unit whose goal is one
  parser. S3b and AC2b close it. **L1:** rev-1's AC1 said "four of them", excluding `corpus_ids`,
  which is equally broken; criteria now name the §4 inventory instead of a number. **H7:** §7 named
  the plain bar for a `subject = kit` leg and reasoned from the leg's GUARD, which is the wrong
  mechanism; corrected to `GATE_SELFTESTS=1`.

- rev-3 · 2026-09-04 · folded spec-audit round 2 (M1, M6, M7, M10). The loop exited NON-CONVERGENT
  at round 2, so this is the disposing fold and there is no round 3. **M1:** §4 credited
  `row_grammar.py` with defaults it does not carry — it is `conf = {}` with no isfile guard and it
  RAISES on an absent conf. The cell mattered more after rev-2 made the table "the single source for
  the count", and routing that reader through a guarded shared parser would silently turn a hard
  failure into an empty-dict success. Cell corrected, §4 explains it, AC7 decides it. **M6:** the
  title, §1 and §4's heading all said FIVE over a six-row table, in the paragraph nominating that
  table as the count's only source; the counts are gone. **M7:** S1 and the Alternatives bullet still
  carried the import claim this document refutes three times elsewhere — the false answer sitting in
  the binding scope section. Both rewritten to what was measured. **M10:** §7 prescribed half the
  pair it cited.

## 10. Reuse audit

The seam is `corpus_ids.load_conf` at `tools/memory-tree/corpus_ids.py:105`, which is already the
kit's conf reader and carries the widest defaults set; this unit widens it rather than adding a
module. The import mechanism reused is `row_grammar.py`'s existing `sys.path.insert` plus sibling
import at lines 38-39 — the only such edge in the kit today. The fixture is modelled on the one
`TOOL-aScouredKit-5` landed for the drift-audit copy of the same divergence. Found by
`python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for loop shapes and
array literals"`, which surfaced `row_grammar.scan` and `corpus_ids` in the ranked set, and
confirmed by direct grep over every reader.

**A STALE HIT, recorded per this section's own rule.** The backlog row asserts `gotchas.py` already
imports `corpus_ids`, and it does not — verified by grep at `711c4c50`. The seam is still the right
one; the row's claim that reusing it is free is where the two disagreed, and §4 says so.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
