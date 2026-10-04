# TOOL-aMendedFleet-10 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-10

**Evidences:** TOOL-aMendedFleet-10
- AC1 — `python tools/memory-tree/gen_build_index.py --asks --json` — on the live tree, 459 rows, every one carrying `pointer` and `summary`; of the 269 rows whose raw line in its `BACKLOG.md` has an arrow tail, none reports an empty `pointer`. The longest `summary` is 159 bytes. Against the base generator no row carried either field
- AC2 — `--selftest` — the arm "a 400-byte text's summary is cut in BYTES" over fixture ask EXMP-aFoo-3, whose text is 155 ASCII bytes then em dashes straddling bytes 157 and 160, reads a `summary` of 158 bytes ending `a…`. RED on a staged break cutting by characters in a scratch copy of the kit: `bytes=164 ends=False`
- AC3 — `gen_build_index.py --asks --json --limit 0` — with `--path` naming `tools/unattended/unattended.sh`: 31 rows; every raw line read at its `file` and `line` names that path or `tools/unattended/` in its text, a `seen` locator or its pointer, or points at the containing directory `tools/` (four rows). Rows ordered newest filing first; all 31 are unlabelled
- AC4 — `--selftest` — the five-ask fixture: `--path` given the fixture file in backslashed form with a line suffix returns exactly EXMP-aFoo-2 (HIGH, pinned `seen`), EXMP-aFoo-1 (MED, directory pointer) and EXMP-aFoo-3 (unlabelled, `seen` matching), in that order, with `paths` normalised to the slashed form and no line; `--path` on the fixture's rooted aFoo build README returns only EXMP-aFoo-4, whose pointer is relative to the memory root. RED on two staged breaks in a scratch copy: severity sort removed gave the order 3, 2, 1; a character prefix instead of a whole-segment one let the near-miss ask EXMP-aFoo-5, under a sibling directory sharing the prefix, through (`matched=4`)
- AC5 — `--asks --json` — with `--path` and no `--limit`: 20 rows, `matched` 31, `cut` 11, 12,213 bytes against 278,541 for the unfiltered call in the same session (4.4%). The unfiltered rows, with `pointer` and `summary` removed, equal the base generator's output row for row, order included (459 rows)
- AC6 — `gen_build_index.py --asks` — `--path` set to ../x, `--path` set to an absolute drive path, `--tsv` beside a `--path`, `--limit 5` alone and `--limit -1` beside a `--path` each exit 2 with nothing on stdout and a stderr line naming the conflict; so do an id pick, `--ready` and `--probe` beside a `--path`
- AC7 — `grep -n -- "--path" tools/memory-tree/README.md` — the Print modes paragraph names `--path`, `--limit`, `pointer` and `summary`, and the refused options

## Owed at the close

- `memory/map/generated/symbols.json` — regenerated in this commit by `gen_map.py --write`; the
  codebase-map coverage and freshness legs are the close's.
- The lexicon leg grades `derive_ask_locators`, `resolve_ask_path` and `check_ask_path`; each was
  answered OK by `lexicon.py --suggest --as py.function`, and the leg itself is the close's.
