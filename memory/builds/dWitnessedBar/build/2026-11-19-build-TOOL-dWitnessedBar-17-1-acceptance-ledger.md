# TOOL-dWitnessedBar-17 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-17

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: a scratch clone of
the worktree at `%TEMP%/u17c` with the pass's diff applied and committed, its `origin/main` updated to
that commit; a scratch adopter cloned from it at `%TEMP%/u17a`; a scratch `git init` at `%TEMP%/u17s`
for the scaffold; and a scratch repository at `%TEMP%/u17pfx` holding a copy of `tools/lib/`. The role
hook refused `ratchet.py both-ways` by its argv, the leg `ratchet (both ways)`, and that refusal was read
rather than routed around: every half of a criterion only a `ratchet` leg, `check-memory-hygiene.sh` or a
self-test observes is owed to the close, named on its line below, with the four `New arm:` lines of
spec section 7, each owing its RED-first observation there.

**Evidences:** TOOL-dWitnessedBar-17
- AC1 — `keys-not-scalar` — in the clone the spec's `git grep -nE` over `'.*.conf'` and
  `'tools/*/.*.conf.example'` printed nothing (exit 1); `python ratchet.py keys-not-scalar --measure` in
  `tools/memory-tree/` printed the two `.lexicon.conf` rows alone; `python ratchet.py keys-not-scalar`
  printed both `held` and `pass · 1 populations graded`, exit 0, `conf-scalar-pins.txt` holding those two
  rows.
- AC2 — `--only 20` — owed at the close: the hygiene suite's new check-20 arm runs it. Observed instead
  on `row_grammar.py --check` over a scratch tree: clean with one keyed duplicate; a planted second
  `ARCH-tOne-2` exited 1 naming `memory/DECISIONS.md: ARCH-tOne-2 at lines 5, 6` with no row; with the
  keyed duplicate repaired it exited 1 naming the row `memory/DECISIONS.md ARCH-tOne-1` as stale.
- AC3 — `--only 21` — owed at the close, through the hygiene suite's check-21 fixture, whose second
  unbound record has no row of `unbound-records.txt`. Observed: `legacy_ledger.py seed --population
  unbound-records` printed `armed unbound-records 16` through `corpus_ids.py --list-unbound`.
- AC4 — `dossier-decisions-empty` — `ratchet.py both-ways` is owed at the close. In the clone, with
  `loop.md`'s `decisions` emptied and committed, `map_diff.py --list-empty-decisions` printed `loop	1`
  and `git status --porcelain -- memory/map/generated` printed nothing. With each waiver home its header
  and `# unarmed` line and a backticked dead path committed to `memory/README.md`,
  `python tools/memory-tree/corpus_ids.py` exited 1 naming `check 15: memory/README.md:37 cites
  memory/gone/never-was.md`; with both homes removed it exited 0 naming no check 13 to 15.
  `head -1 memory/project/corpus-path-unresolved.txt` printed `# ledger · corpus-path-unresolved · key site
  path,cited · direction shrink-only · drain hunk`. `adopt-memory-tree.sh --scaffold` over the scaffold
  arm's conf exited 0 and left `memory/project/` holding neither home; the hygiene run there is owed.
- AC5 — `unarmed` — `legacy_ledger.py seed --population severity-unlabelled` and `--population live-rows`
  each printed `unarmed <population> no seed`, exit 0, writing no home; `python ratchet.py unarmed`
  exited 0 naming `unarmed · severity-unlabelled · seed = []` and `unarmed · live-rows · seed = []`.
- AC6 — `never-gains` — owed at the close. `git grep -n "_PIN" -- tools/drift-audit/drift_signals.py`
  prints one narration comment, line 253, and no `RATCHETS` row.
- AC7 — `count rose` — owed at the close, with the `cutoff-later` and `cutoff-blank` plants of
  `ratchet selftest`. Observed on the seed: `ratchet.py measure-cutoffs` printed `SPEC_TIER1_CUTOFF
  99991231` with the key blanked and `20261011` with it a day later.
- AC8 — `measure-cutoffs` — it printed 39 lines, the sum of `git grep -cE "^[A-Z0-9_]+_CUTOFF=" -- (DERIVED from the builder's probe)
  '.*.conf'` (28 and 11), each row equal to `date-cutoffs.txt`'s key and date; the `both-ways` half is
  owed at the close.
- AC9 — `merge: rows` — `git check-attr merge -- date-cutoffs.txt` in `memory/project/` printed it; the
  `--only 3` half is owed at the close.
- AC10 — `upgrade_steps.py list` — in the clone it listed `memory-tree/corpus-path-unresolved-to-ledger`,
  the six `memory-tree/*-pin-to-ledger` rows and `codebase-map/dossier-decisions-empty-pin-to-ledger`. In
  the adopter the `RECORD_UNBOUND_PIN` step's `up` wrote `unbound-records.txt`, removed the key and
  drained its row, `witness` exited 0, and `down` restored the conf's and `conf-scalar-pins.txt`'s bytes
  (`cmp`). The `ORPHAN_ID_PIN` step's `up` over a blank key removed the key and `id-orphan-waiver.txt`,
  and `down` restored both. The `DOSSIER_DECISIONS_EMPTY_PIN` step's `up`, with `test_codebase_map.py` and
  the home removed and the key `"16"`, seeded 14 rows, as many as `--list-empty-decisions` printed, and (DERIVED from the builder's probe)
  removed the key.
- AC11 — `{prefix}` — the spec's `git grep` printed the `conf-scalar-pins` line alone
  (`tools/memory-tree/kit.toml@aa9a8685:727`); in the clone with `row-duplicates.txt` removed, `legacy_ledger.py
  seed --population row-duplicates` printed `armed row-duplicates 3` and `row_grammar.py
  --list-duplicates` printed 3 lines. The new arm's steps, run by hand at `%TEMP%/u17pfx`, printed `armed (DERIVED from the builder's probe)
  fx-pfx 1` with this pass's factory and `unarmed fx-pfx exit 2` with HEAD's, which leaves the token
  literal.
