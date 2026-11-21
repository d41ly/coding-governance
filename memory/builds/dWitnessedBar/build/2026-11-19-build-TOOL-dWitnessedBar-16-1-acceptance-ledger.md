# TOOL-dWitnessedBar-16 — acceptance ledger, passes 1 and 2

**Serves:** journal TOOL-dWitnessedBar-16

Two passes. Pass 1 built everything but S12 at base `7dbe0c8d9d2c`; pass 2 built S12, S14, S15 and
rev-13's S10 respelling at base `773daf5611812b8953fbcaba094b4f005c796b3c` and closed the spec. Neither
pass ran a merge bar, a self-test suite or a gate leg; pass 2 ran the naming lexicon's `--offenders`
and `--suggest`, and the generators `leg_factory.py --write` and `gen_map.py --write`. Each criterion
below was checked on node d on 2026-11-19 by `convert_registry.py`'s or `registry_to_ledger.py`'s own
CLI, a `python -c` probe of the changed code, or the changed program over a scratch target under
`%TEMP%`. Owed to the close: every leg section 7 names, and the RED-first observations of its two
`New arm:` lines, `tools/drift-audit/selftest.py` (AC7, AC8) and `ratchet selftest`'s `regrammared`
plant (AC12).

**Evidences:** TOOL-dWitnessedBar-16
- AC1 — `legacy_ledger.py read` — pass 1: the rule over `git ls-files memory/project memory/map
  tools`, less the three §3 leaves to unit 18 and F16's six, finds each path the home of exactly one
  registration, and `memory/builds/dWitnessedBar/BACKLOG.md` holds TOOL-dWitnessedBar-99, `FIVE
  REGISTRIES STAY IN THEIR GRAMMAR`. Pass 2: `read_registrations` over the tree reads 26 registrations
  (DERIVED), S14's four homed in `memory/project/`, each with S3's `read-back` seed.
- AC2 — `legacy_ledger.py read` — pass 1: the conversion record's before and after counts match the
  factory's read of each home and every former reason sits beside its key. Pass 2 moved four homes and
  added 20 carried `dead-path-waivers` rows (DERIVED), which the record lists beside their keys with
  `S5`; `read_rows` over that home reads 44 keys (DERIVED) and no malformed row.
- AC3 — `def read_registry` — pass 1: `git grep -n "def read_registry" -- tools/gate-lint` prints
  nothing; the scratch-clone `check-arms.py --check` runs are owed to the close, the leg's argv being a
  gate. Pass 2 renamed `check-arms.py`'s two `unpinned` closures and its `rrow` fixture helper, the
  messages unchanged.
- AC4 — `shell hygiene (a fork spent on builtin work)` — pass 1: `resolve_declaration` reads the
  converted `spawn-idiom-sites.txt` with no malformed row; the leg's two scratch-clone directions are
  owed to the close.
- AC5 — `baseline.txt` — `git ls-files memory/map/` lists `baseline.txt` and `affordance-exempt.txt`
  and no `.toml` of either name; pass 2 ran `gen_map.py --write`, rewriting `CARDS.md` and
  `symbols.json`. Pass 1's `adopt-codebase-map.sh` scratch target left the one `# unarmed · dead probe`
  line; `gen_map.py --check` and the adopter suite are owed to the close.
- AC6 — `--check-format` — pass 1 read today's legacy file through S7's transitional read; pass 2's
  `read_contract_rows` over the converted file returns 148 bound and 69 exempt paths (DERIVED). The
  scratch-clone probe with the converted file at `origin/main` is owed to the close.
- AC7 — `drift_report.py --json` — pass 2's run reports `shrink_only_lists_not_shrinking` with `of` 18,
  the number of `shrink-only` registrations (DERIVED), and reads `backlog_asks_unlabelled`'s pin 447
  from the moved `memory/project/drift-pins.txt`; `git grep -nP "^(SHRINK_ONLY|PINS|BASELINES)\b" --
  tools/drift-audit/` prints nothing.
- AC8 — `id-orphan-waiver.txt` — `derive_low_waters` counts non-`#` lines and every converted home's
  header is a `#` line, so the low water holds; the before-and-after scratch-clone run of
  `python tools/drift-audit/drift_report.py --json` is owed to the close.
- AC9 — `merge: rows` — `.gitattributes` carries `<home> merge=rows` for every converted home, S14's
  four at `memory/project/` since pass 2; `git check-attr merge` prints `merge: rows` for those four
  and for `memory/project/spawn-idiom-sites.txt`.
- AC10 — `up` — on a scratch adopter under `%TEMP%` holding `7dbe0c8d9d2c`'s legacy
  `unarmed-branches.txt`, `registry_to_ledger.py up` exited 0 printing 173 reasons and wrote the header
  `# ledger · unarmed-branches · key site path,check,signature · direction shrink-only · drain hunk` over
  166 rows whose counts sum to 173 (DERIVED); `witness` exited 1 before and 0 after; `convert_registry.py
  convert` again exited 0 and wrote nothing (byte-compared); `down` restored the legacy bytes
  (byte-compared). `up --home memory/project/drift-pins.txt --from tools/drift-audit/drift_signals.py`
  over that layer's `PINS`, 6 of 10 non-zero (DERIVED), wrote six rows; `--from
  ../u16a/tools/drift-audit/drift_signals.py` exited 1 writing nothing.
- AC11 — `owed_rows.py --base HEAD` — pass 1: exits 0 printing `0 rows owed` over the renamed
  baseline; the `--selftest` run and the leg-removed scratch clone are owed to the close.
- AC12 — `regrammared at` — pass 1: `check_regrammared_at_base` reads every in-place home
  regrammared; the `--fixture --plant regrammared` run is the `New arm:` the close observes RED then
  GREEN.
- AC13 — `read-back` — `convert_registry.py read-back spawn-idiom-sites` prints one line per row, its
  `path`, `class` and count TAB-joined; `read-back id-orphan-waiver` prints one `dead probe:` line; the
  `ratchet.py populated` and `unarmed` legs are owed to the close.
- AC14 — `read_legacy_rows` — pass 2: `git grep -n read_legacy_rows -- tools/memory-tree/gen_build_index.py`
  and `git grep -n "import convert_registry" -- tools` print nothing; a home in the old grammar now
  refuses as a `Problem` naming its missing ledger header, probed over a scratch root.
- AC15 — `memory/project/` — `git ls-files -- memory/project tools` lists the four S14 names under
  `memory/project/` alone, and `legacy_ledger.py read` exits 0 for each; the `{gov}/memory-tree/` and
  `^home = "tools/` grep prints nothing; `"{gov}/govkit/steps/registry_to_ledger.py"` totals 33 over the
  11 `-to-ledger` rows (DERIVED), three each; the `TOOLS / ` grep over `convert_registry.py` prints
  nothing; `upgrade_steps.read_steps` validates all 16 rows (DERIVED) at the working tree.
- AC16 — `done <<<` — the grep over `tools/check-dead-paths.sh` and `tools/gate-lint/fork-count.sh`
  prints nothing, nor does `_self_dir/lib/` in `check-dead-paths.sh`, nor `baseline.toml` in the map
  kit's `selftest.py` and `kit.toml`; each of the 20 `carried:TOOL-dWitnessedBar-51` rows names a line
  `git grep -nF -e <text>` finds at its path, `{prefix}` read as `tools`. The `selftest.py` carrier
  names an unregistered `.txt` rather than `baseline.txt`, deviation 164.
