# TOOL-aWeldedTribunal-5 — one `.memory-tree.conf` parser, read by all five python readers

**Status:** OPEN · rev-1 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Five python readers in `tools/memory-tree/` each re-implement the `.memory-tree.conf` parse with an
identical naive `v.strip().strip('"').strip("'")`, while the shell gate SOURCES the same file in
bash. A legal spelling bash accepts and the python half mis-reads takes `gotchas.py --check` from
rc=1 to rc=0 over an identical planted violation — coverage removed, not failed closed, gate still
green. Route all five through one parser that agrees with the shell.

## 2. Scope (IN)

- **S1** — One conf parser, exported from `tools/memory-tree/corpus_ids.py`, which already holds
  `load_conf` and is already imported by `gotchas.py`. It becomes the single reader.
- **S2** — It handles the two spellings bash accepts and the current parse does not: an INLINE
  COMMENT after the value (`MEMORY_ROOT=memory   # note`) and an `export ` prefix on the key.
- **S3** — `gotchas.py`, `gen_build_index.py`, `check-arms.py` and `row_grammar.py` call it instead
  of their own copies. Each keeps its OWN defaults dict — the defaults differ per reader and merging
  them would be a scope change nobody asked for — and only the PARSE is shared.
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
- **The drift-audit copy.** `TOOL-aScouredKit-5` already fixed it; a sixth caller is not in this
  unit's population and pulling it in would widen the diff for no defect.

## 4. Design

### Inventory — the five copies

| File | Line | Defaults it carries |
|---|---|---|
| `tools/memory-tree/corpus_ids.py` | 118 | `MEMORY_ROOT` `DISCIPLINES` `FAMILIES` `CHARTER` and four pins |
| `tools/memory-tree/gotchas.py` | 92 | `MEMORY_ROOT` `UNIVERSAL_BUDGET` |
| `tools/memory-tree/gen_build_index.py` | 287 | `MEMORY_ROOT` `DISCIPLINES` `FAMILIES` |
| `tools/memory-tree/check-arms.py` | 82 | `MEMORY_ROOT` `ARMS_FLOORS` |
| `tools/memory-tree/row_grammar.py` | 93 | `MEMORY_ROOT` `FAMILIES` and a pin |

All five hold the identical body: skip blank, skip `#`-leading, skip no-`=`, partition on the first
`=`, strip whitespace then one layer of double quotes then one layer of single quotes.

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

`row_grammar.py` already does `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` and
imports a sibling; `gotchas.py` already imports `corpus_ids`. The pattern exists, is used, and is
what the other three adopt. No packaging change.

### Files touched (estimate)

- `tools/memory-tree/corpus_ids.py` — the shared parser.
- `tools/memory-tree/gotchas.py`, `gen_build_index.py`, `check-arms.py`, `row_grammar.py` — each
  loses its copy and gains the import.
- One fixture and its arm.

### Alternatives rejected

- **A new `conf.py` module.** Rejected: `corpus_ids.py` already holds `load_conf` and is already
  the import target of one of the four. A sixth file to hold twelve lines is scaffolding.
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

- **AC1** — When a fixture conf holding `MEMORY_ROOT=memory   # note` is read by each of the five
  readers, every one returns `memory`. Today four of them return `memory   # note`.
- **AC2** — When a fixture conf holding `export MEMORY_ROOT=memory` is read by each of the five,
  every one returns `memory` under the key `MEMORY_ROOT`. Today the key is `export MEMORY_ROOT`.
- **AC3** — When the planted violation of `TOOL-aScouredKit-19`'s reproduction is staged under a
  conf carrying the inline comment, `python tools/memory-tree/gotchas.py --check` exits `1`. It
  exits `0` today, which is the whole defect: coverage removed rather than failed closed.
- **AC4** — When the new parser is run over every tracked `.memory-tree.conf` in this repo and
  compared against the current parse, the results are identical. The change is a no-op here.
- **AC5** — When a fixture conf is SOURCED in `bash` and read by `corpus_ids.parse_conf`, the two
  agree on every key. This is S5, and it is what makes the arm a cross-language check rather than a
  tautology between two values the same code derives.
- **AC6** — When `grep -c "strip('\"')" tools/memory-tree/*.py` is run, one copy remains.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the memory-tree hygiene legs and the kit self-test legs whose
names are in `tools/gate-legs.json`. Several are guarded on the kit dir this unit writes, so they
run on this diff by construction.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. All five copies confirmed present at the lines §4 tabulates,
  by `grep -c` over each file.

## 10. Reuse audit

The seam is `corpus_ids.load_conf` at `tools/memory-tree/corpus_ids.py:105`, which is already the
kit's conf reader and is already imported by `gotchas.py`; this unit widens it rather than adding a
module. The import mechanism reused is `row_grammar.py`'s existing `sys.path.insert` plus sibling
import at lines 38-39. The fixture is modelled on the one `TOOL-aScouredKit-5` landed for the
drift-audit copy of the same divergence. Found by
`python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for loop shapes and
array literals"`, which surfaced `row_grammar.scan` and `corpus_ids` in the ranked set, and
confirmed by direct grep of the five files.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
