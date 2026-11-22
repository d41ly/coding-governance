# TOOL-dWitnessedBar-13 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-13

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the canonical
`tools/lib/legacy_ledger.py` CLI run over a scratch fixture repo under `%TEMP%` whose `main` sits on a
bare remote it fetched, the row-keyed driver run over planted ledger blobs, the two gate-lint adapters
compared with their own code at `112526471`, and the block cut out of each copy with the parity arm's
`blk` range. Both `New arm:` lines of spec section 7 still owe their RED-first observation, which the
main loop makes at the close, and so does every leg that section names; AC8's own commands are two
gate legs, refused to this role, so the main loop owes them too.

**Evidences:** TOOL-dWitnessedBar-13
- AC1 — `python legacy_ledger.py read <population>` — run by its absolute path with the fixture repo
  as working directory, `read fx-sites` printed both rows and exited 0. With the header's direction
  rewritten to `append-only` it exited 1 naming line 1; with a row keyed `42` it exited 1 naming
  line 4 as a line-number key; with a disposition `done` it exited 1 naming line 4.
- AC2 — `undeclared site` — `compare fx-sites --measured <file>`, the file measuring `b2.sh` and
  omitting `c.sh`, printed one `undeclared site` and one `unmeasured row` and exited 1. Without
  `--measured` it printed neither, and stderr said the both-ways half was not run.
- AC3 — `gained` — a key appended to the `shrink-only` ledger on the branch printed `gained`; the same
  key with disposition `widened:REC-1` printed nothing and exited 0; a key gained by the
  `declared-set` ledger printed nothing; with `refs/remotes/origin/main` deleted, `compare` printed
  `unresolved — no origin/main ref to compare against (never fetched)` and exited 1.
- AC4 — `python legacy_ledger.py carry <population>` — after a staged, uncommitted `git mv a.sh b.sh`,
  `carry fx-sites` printed `carried a.sh -> b.sh`, the home held `b.sh EOF 2 abcdef12 seeded` and no
  `a.sh` row, and `compare --measured` over a file measuring `b.sh` and `c.sh` printed none of
  `gained`, `unmeasured row` and `undeclared site` and exited 0. With the home removed from the index,
  `carry` exited 2 naming `memory/project/fx-sites.txt` and the file's cksum was unchanged.
- AC5 — `ledger-keyed` — `merge-rows.py` over `%O` holding one row and `%A`, `%B` each appending a
  different one exited 0 with all three rows, the header once, and the audit line ending
  `census ledger-keyed, clean`. A generic index's append merge still read `census generic, clean`, and
  identity merges of `memory/DECISIONS.md` and three backlog shards returned their input unchanged.
- AC6 — `merge-rows.sh` — through the driver, `%A` lowering a key to 2 and `%B` to 3 kept 2 with
  `%A`'s sha; `%A` at 3 and `%B` at 2 kept `%B`'s 2 and its sha; a key `%A` removed while `%B` kept it
  as at `%O` was absent, one delete honoured. Equal counts with different shas wrote a row conflict,
  and three disagreeing headers failed closed as a whole-file conflict.
- AC7 — `legacy_ledger_py` — the block cut by `blk` from `tools/memory-tree/legacy_ledger.py` and
  `tools/gate-lint/legacy_ledger.py` equalled the canonical's; a scratch copy of the gate-lint file
  with `KEY_KINDS` changed to `KEY_KINDZ` cut different. The `coverage_join`, `remote_ladder_py` and
  `compare_base_py` blocks of `tools/gate-lint/coverage_join.py` equalled memory-tree's.
- AC8 — `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` — the two
  commands are the gate legs this role may not run, so the main loop owes them at the close. Standing
  in: `read_registry` and `check_registry` of both scanners, new and as at `112526471`, compared over
  6054 inputs (400 generated registries under every key shape, the tracked `memory/project/*.txt`
  registries, and 2000 measured and declared pairs with and without `explained` and `listing`), and
  none differed.
- AC9 — `read_registrations` — `read fx-keys`, registered only in the fixture's
  `tools/govkit/registry.toml`, printed `x:120 1 abcdef12 seeded` and exited 0; `read fx-recall`,
  registered in `scripts/recall/kit.toml`, exited 0 with its row; a table in `tools/fx/kit.toml`
  declaring `fx-keys`' home made `read fx-keys` exit 2 naming both tables.
- AC10 — `verbatim` — `fx-keys`, `key = "key"`, `fields = ["ref"]`, `verbatim = ["ref"]`, read
  `x:120` and exited 0; `fx-sites`, with no `verbatim`, holding a key field `120` exited 1 naming
  line 4; `fx-refs`, `verbatim = ["ref"]` over `fields = ["ref", "note"]`, exited 1 naming line 3 for a
  note `z:9`; `verbatim = ["nope"]` made `read fx-keys` exit 2 naming the `fx-keys` table.
