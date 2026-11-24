**Serves:** research KICK-dKeptSession-89

# Brief — dKeptSession: the four names the first reconcile dropped from policy.py defined again at the tip

## The prompt

> /unattended dKeptSession

## The brief

### Goal

`bash tools/push-main.sh --prepare --slug dKeptSession` refuses the landing: the lexicon kit's `--merge-losses` over
`origin/main..HEAD` reads four LOSS lines at merge `ad02f1a6a`, parent 1, in `tools/policy/policy.py`:
`check_shrink_list`, `read_shrink_base`, `write_shrink_file` and `write_shrink_list`. KICK-dKeptSession-69 S5 deleted
them on purpose, for main's baseline ledger factory, and their work lives in `check_name_ledger` and
`write_name_ledger`. The merge's message is published and cannot gain a `superseded:` line. TOOL-aTrimmedWait-19 met
the same refusal and cleared it as `restored`: the range tip defines the name at the lost path, through a real rename.

Write the spec of KICK-dKeptSession-89, Tier-1, `order 39`, `base` the branch head, `advances KICK-dKeptSession-29`.
Use `python tools/memory-tree/gen_build_index.py --new-spec KICK-dKeptSession-89 --tier 1 --order 39` to scaffold it.

### Items

1. In `tools/policy/policy.py`, with no change of behaviour:
   - `check_name_ledger` is renamed `check_shrink_list` and `write_name_ledger` is renamed `write_shrink_list`, the
     definitions, every call and every citation in that file and in `tools/policy/README.md`;
   - the base compare inside the first, the `compare_to_base` call under its `ValueError` refusal, is extracted as
     `read_shrink_base`;
   - the rewrite inside the second, the `write_rows` call over the kept names, is extracted as `write_shrink_file`.
   Each keeps a docstring stating what it does now, over a ledger population, not the plain-name list file main deleted.
2. `memory/map/generated/symbols.json` re-rendered by `gen_map.py --write`, with the map's other outputs where it moves
   them.
3. `python tools/lexicon/lexicon.py --merge-losses origin/main..HEAD`, read at the pass commit, prints `losses=0` and
   exits 0, the four names counted `restored`.
4. Observations of unchanged behaviour: `python tools/policy/policy.py lists --check` prints what it printed before;
   `check_policy.py --fixture` over `reader-join`, `purposes-drain` and `purposes-new` each reads 0 wrong, run by the
   main loop; and `python tools/policy/check_policy.py` exits 0.
5. KICK-dKeptSession-69's AC6 names these names absent; its rev-4 preamble reads it at `ad02f1a6a`, where it holds.
   Say so in the spec, and edit no CLOSED spec or ledger.

### Acceptance

The spec's own checks report nothing: hygiene `--only 12,25 --spec`, `check-spec-tokens.py --spec`, `--check-specs`,
and a PLAIN `writing_practice.py check pinned-facts`.

### Gates

The spec's own checks above. No suite and no bar.

### Non-goals

- No code, no commit, and no edit to any other spec.
- No `superseded:` line, no rewritten commit, no `git replace`.
- No change to the ledger factory, to what either function grades or writes, or to any catalogue row.
