# TOOL-aWeldedTribunal-5 — acceptance ledger

**Serves:** journal TOOL-aWeldedTribunal-5

## What changed

`corpus_ids.py` gained `parse_conf_line` and `parse_conf`. All SIX readers route through them:
`load_conf` and `read_declared_keys` in that module, plus `gotchas.py`, `gen_build_index.py`,
`check-arms.py` and `row_grammar.py`, each keeping its OWN defaults dict.

## Each criterion, answered

The fixture declares all three cases: `MEMORY_ROOT=memory   # note`, `export FAMILIES="TOOL DEPL"`,
and `QUOTED="a # b"`.

- **AC1** — every value reader returns `memory` for the commented line. All five agree.
- **AC2** — every value reader yields key `FAMILIES` with value `TOOL DEPL` for the exported line.
- **AC2b** — `read_declared_keys` returns exactly the declared key set and agrees with `load_conf`.
- **AC3** — the mechanism, measured directly rather than through an end-to-end rc flip: under the
  OLD parse `MEMORY_ROOT` is `'memory   # note'` and `os.path.isdir` is **False**, so the checker
  walks nothing and every check passes by absence; under the NEW parse it is `'memory'` and
  `isdir` is **True**. That is the defect and its closure. The end-to-end rc flip on a planted
  violation was NOT re-run here — the mechanism is what changed, and this line says which was
  observed rather than implying both.
- **AC4** — over this repo's real `.memory-tree.conf`, 28 declared keys, **zero** differences
  between the old and new parse. The change is a no-op here and a fix for adopters.
- **AC5** — bash is the reference and all five readers match it on all three cases, including the
  quoted `#` surviving as data. A `#`-strip that ignored quoting would have turned `a # b` into `a`,
  a silent wrong value where the original bug was at least a loud directory miss.
- **AC6** — one quote-strip copy remains, in `parse_conf_line`. Stated in the spec and repeated here
  because this grep CANNOT see `read_declared_keys`, which carries no quote strip; AC2b covers it.
- **AC7** — the absent-conf disposition, per reader: `corpus_ids`, `gotchas`, `gen_build_index` and
  `check-arms` return their defaults; **`row_grammar` RAISES `FileNotFoundError`**, exactly as it did
  before. That difference is preserved on purpose and its function now carries a docstring saying so:
  bolting the isfile guard on would have converted a hard failure into a quiet empty-dict success,
  which is the very class this unit closes, reintroduced by the unit closing it.

## Gates run

`gotchas.py --check` rc 0, `corpus_ids.py --check` rc 0, `corpus_ids.py --selftest` PASS,
`row_grammar.py --check` rc 0, `check-arms.py` rc 0, `gen_build_index.py --check-format` clean.

## Two things found while building, neither caused by this unit

`gotchas.py --check` reported `memory/gotchas/INDEX.md` stale — a consequence of unit 4's record
refresh, regenerated with `gotchas.py --write`.

`gen_build_index.py --check-format` refused because `memory/project/readme-contract.txt` named no row
for this build's README, so a new build would escape the contract by existing. Confirmed pre-existing
by running the HEAD version of the generator, which reports it identically. The README is now
registered **BOUND** — and the slots were MEASURED against their ceilings first, then trimmed to fit.
Two builds already in that registry were bound without measuring and have reddened the leg ever
since; their rows say so. Trimming was the right fix rather than a wider ceiling: the material cut
was duplicated from the specs and the review records, which is where it still lives.

## Evidence

**Evidences:** TOOL-aWeldedTribunal-5
- AC1 — `python tools/memory-tree/corpus_ids.py --selftest` — every reader returns the intended value for an inline-commented line; the arm grades against a bash source of the same fixture
- AC2 — `python tools/memory-tree/corpus_ids.py --selftest` — every reader yields the bare key for an `export`-prefixed line
- AC2b — `python tools/memory-tree/corpus_ids.py --selftest` — `read_declared_keys` and `load_conf` agree on the key set
- AC3 — `python tools/memory-tree/gotchas.py --check` — under the old parse the memory root resolved to no directory and the checker walked nothing; under the new one it resolves and walks the tree
- AC4 — `python tools/memory-tree/corpus_ids.py --check` — 28 declared keys on this repo's real conf, zero differences old-versus-new
- AC5 — `python tools/memory-tree/corpus_ids.py --selftest` — six spellings graded against bash, including a quoted comment character surviving as data
- AC6 — `tools/memory-tree/corpus_ids.py` — one quote-strip copy remains, in `parse_conf_line`
- AC7 — `python tools/memory-tree/corpus_ids.py --selftest` — four readers return defaults on an absent conf and `row_grammar.load_conf` still RAISES, the documented difference
