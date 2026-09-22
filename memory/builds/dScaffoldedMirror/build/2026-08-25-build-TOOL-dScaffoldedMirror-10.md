# TOOL-dScaffoldedMirror-10 — build record

**Serves:** journal TOOL-dScaffoldedMirror-10

Node `d`, 2026-08-25, base `500a5db6`, unattended run `dScaffoldedMirror`. Spec:
`../spec/2026-08-24-spec-dScaffoldedMirror-10.md`, built at rev-4. Tier-2.

## Result

The table now reaches whoever is writing the name, by three routes with different costs.

```
$ python tools/lexicon/lexicon.py --suggest fetch_remote
use `load_remote` — the declaration says `load`, NOT `fetch`: read a store into memory
```

That full form works only because `TOOL-dScaffoldedMirror-8`'s NOT-clause grammar landed first,
which is the entire reason that split was taken. 84 ms worst of 20, no corpus pass.

`--brief` keys on the OBJECTS a file already names and reports every spelling live for each. It found
something real on its first run against this tree:

```
conf: load x9, budget x1 (off-table), read x1  <-- SPELLED MORE THAN ONE WAY
```

That is the `load_conf`/`read_conf` conflict the research pass measured, surfaced by pointing one
verb at one file — a class P1 calls green, because both spellings are declared.

And the rendered Skill carries the whole 1,787-byte table, byte-compared by its own unguarded leg.

## The charter POINTS, and it is smaller for it

| file | before | after | delta |
|---|---|---|---|
| `AGENTS.md` | 64,394 | 64,292 | **−102** |
| `coding-governance-agents.template.md` | 48,827 | 48,725 | **−102** |

Five bullets became four, and the fourth says the rows are NOT restated there. That is §6's own rule
— point at the source or gate the pair — applied to the document that states it.

## Six defects found by building, and five were already written down

**Three in the render, all documented one kit over.** `KITREL` trimmed `ROOT` off `KIT_DIR`, which on
Windows are spelled `C:/...` and `/c/...`, so the trim silently did nothing and the ABSOLUTE path
rendered into the Skill description — and shipped, briefly, into a registered Skill. `memory-recall`
derives the same value with `git rev-parse --show-prefix` and its comment says the wrong way writes a
drifting diff into a committed artifact silently; that comment had been read twenty minutes earlier.
The render stripped CR from the TEMPLATE but not from substituted VALUES, and Python's `print` emits
CRLF on Windows, so `--check` reported DRIFTED against a file it had just written. And `diff -q -`
reading stdin AND a process substitution returned non-zero on identical content under Git-Bash.

**One in the CLI surface.** `--scaffold` REFUSES on an existing declaration, so a DRIFTED Skill had no
non-destructive remedy. `--render` was added beyond the spec, because a refusal whose only fix is
deleting the declaration is one people learn to bypass.

**Two in this spec's own criteria.** AC3 named `do_check_format` showing both `do` and `cmd`;
`TOOL-dScaffoldedMirror-14` renamed every `do_` away first, so the example is gone and its absence is
the earlier unit having worked. AC9 named byte literals that were wrong three times over — rev-1's,
the review's correction, and the arithmetic behind both — because three other units edited those
files in between. Both are the same class: **a criterion naming a live instance ages with the tree.**

## What was parked rather than fixed

`drift-audit`'s `non_terminal_specs_cited_by_product_source` sat 3 over pin 2 through this unit,
because `-8` and `-10` were both INPROGRESS and both cited by the code implementing them. Raising the
pin is the defect this build exists to remove. `-10` closing here drops it to 2; `-8` closing drops
it to the `aBatchedLintel-1` baseline.

**Evidences:** TOOL-dScaffoldedMirror-10
- AC1 — `python tools/lexicon/lexicon.py --suggest build_index` — prints `OK — build_index leads with 'build'`, exits 0, and reads only the declaration
- AC2 — `python tools/lexicon/lexicon.py --suggest fetch_remote` — names `load_remote` and quotes `NOT 'fetch'`; armed as `--suggest: an off-table token names the REPLACEMENT from the NOT clause`
- AC3 — amended rev-2 — rev-1's `do_check_format` example was deleted by `-14` before this unit built; the arm uses the live `index` object, spelled `build` and `render`, and asserts the more-than-one-way flag (§9 rev-2)
- AC4 — `python tools/lexicon/lexicon.py --brief tools/push-main.sh` — prints `COVERAGE: dark` and exits 2, armed as `--brief: a dark extension is a NAMED refusal, not an empty section`
- AC5 — `python tools/lexicon/selftest.py` — `S6: --suggest never exits 1` and its `--brief` twin, both observed RED when `--suggest` was made to return 1
- AC6 — `bash tools/lexicon/adopt-lexicon.sh --check` — editing a `VERBS` gloss without re-rendering prints `DRIFTED` and exits 1
- AC7 — `bash tools/lexicon/adopt-lexicon.sh --check` — an emptied template prints `the Skill render produced NOTHING` and exits 1 rather than byte-comparing two empty files
- AC8 — `tools/gate-legs.json` — the `lexicon skill wiring` row carries `"guard": []`, matching `memory-recall skill wiring`
- AC9 — amended rev-4 — from byte literals to the PROPERTY, all three predicted figures having gone stale; measured `bash tools/check-template-size.sh AGENTS.md` at 64,292 / 64,512 and the template at 48,725 / 49,152, both green and both smaller than before
- AC10 — `python tools/lexicon/lexicon.py` — no `UNSELECTIVE LAYERS RULE` and no P3 offender; this unit added no `LAYERS` row, so the criterion is satisfied by the existing rule staying armed and obeyed
- AC11 — 20 consecutive `--suggest` invocations, worst 84 ms against a 100 ms bar on node `d`
