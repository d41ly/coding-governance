# TOOL-dWitnessedBar-20 — acceptance ledger, pass 1

**Serves:** journal TOOL-dWitnessedBar-20

One pass, the second builder, at base `abf06676dfb430ec05e00414258f70121fca93a2` over the rev-5 spec. The
pass ran no merge bar, no self-test suite and no gate leg; it ran the naming lexicon's `--suggest`, the
generators `leg_factory.py --write`, `gen_map.py --write` and `gen_build_index.py --write`, the changed
verbs `policy.py lists --check | --derive | --marks` on the tree, the canonical `legacy_ledger.py read`,
and `python` probes of the changed fixture helpers (`build_legacy_repo`, `check_legacy_drain_merge`,
`derive_legacy_home`) over scratch repositories under `%TEMP%`. Each criterion below was checked on
node d on 2026-11-20. Owed to the close: every leg section 7 names, the `--fixture` runs AC4 to AC7 and
AC9 to AC11 name, and the RED-first observation of the `New arm:` line on `tools/policy/check_policy.py`.

**Evidences:** TOOL-dWitnessedBar-20
- AC1 — `legacy-homes.txt` — under `memory/project/`, `grep -v '^#' | awk -F'\t' 'NF!=5 || $3!=1'` prints
  nothing and `grep -c ' owner-policy$'` prints 0 over the 114 converted rows (DERIVED from the builder's probe).
- AC2 — `cut -f1,2` — the converted key set equals the key set of `tools/policy/legacy-homes.txt` at the run's
  base `9e21ac76`, both sorted, by `diff` (DERIVED).
- AC3 — `--derive` — `policy.py lists --derive legacy-homes` on the tree equals `cut -f1-3` of the list line for
  line, by `diff`; `--derive other` and a bare `--marks` exit 2.
- AC4 — `case growth` — over a scratch fixture repository a planted conf key with its row typed `seeded` makes
  `lists --check` exit 1 with the one new-legacy-home report and `lists --write` exit 1 with the list's bytes
  unchanged; with the row typed `widened:TOOL-bPlanted-1` (`case widened`) `lists --check` exits 0. The
  `--fixture legacy-homes` run is owed to the close.
- AC5 — `case planted-row` — a row typed for a key no home holds makes `lists --check` exit 1 with `unmeasured
  row .unattended.conf PLANTED_KEY: no scan of the legacy homes finds it` and its `gained` line, over a scratch
  repository; the fixture run is owed.
- AC6 — `case shrink` — with `KEPT_KEY` deleted from the conf, `lists --write` exits 0 and removes that row
  alone, every other row byte-equal to its line before, then `lists --check` exits 0; the fixture run is owed.
- AC7 — `case unmarked` — `lists --check` exits 1 with the one `has no mark in GATE_ENV_MARKS` report, and
  `lists --marks legacy-homes` prints the row `.githooks/gate-env.sh`, `GATE_PLANTED`, `unmarked`; the
  fixture run is owed.
- AC8 — `legacy_ledger.py read legacy-homes` — run from `tools/lib/` it prints the 114 rows and exits 0 (DERIVED from the builder's probe)
  (DERIVED); the `[[ledger]]` table in `tools/govkit/registry.toml` reads `direction = "shrink-only"`, and `grep
  -c '^\[\[ledger\]\]'` under `tools/policy/kit.toml` prints 0.
- AC9 — `merge: rows` — `git check-attr merge -- legacy-homes.txt` under `memory/project/` prints it; the
  `drain-merge` helper over a scratch repository merged two adjacent drains with exit 0, both rows gone and no
  conflict marker, then `lists --check` green; with `merge.rows.driver` left unset the same merge exited 1
  with a content conflict, observed RED. The fixture run is owed.
- AC10 — `git ls-files tools/policy/legacy-homes.txt` — prints nothing after the move; `grep -n '^home =
  "tools/'` over the registry prints nothing, `grep -c 'legacy-homes' tools/policy/kit.toml` prints 0, and
  `grep -c 'project/legacy-homes'` over `tools/gate-legs.json` prints 1, the `policy fixtures` row; a probe of
  the `legacy-homes-present` logic reads one registration with its home a file and no list in the kit. The
  `--fixture legacy-homes-present` and `legacy-homes-withheld-install` runs are owed.
- AC11 — `census-source-receipt` — over a scratch repository holding gov's registry tracked and an empty file at
  its registration's home, `check_legacy_graded` answers True beside the source-mode receipt and False beside
  the adopter receipt, and False before the home is written; the `--fixture census-source-receipt` run is owed.
