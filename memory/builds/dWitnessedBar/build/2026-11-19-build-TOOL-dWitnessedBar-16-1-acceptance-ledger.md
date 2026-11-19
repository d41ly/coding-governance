# TOOL-dWitnessedBar-16 — acceptance ledger, pass 1

**Serves:** journal TOOL-dWitnessedBar-16

Pass 1 of two: everything but S12, the spec left INPROGRESS as S12 states. This pass ran no merge
bar, no self-test suite and no gate leg except the naming lexicon's `--suggest`. Each criterion below
was checked on node d on 2026-11-19 by `convert_registry.py`'s own CLI, a `python -c` probe of the
changed code, or the changed adopter over a scratch target under `%TEMP%`, in the worktree at base
`7dbe0c8d9d2c`. Owed to the close: every leg spec section 7 names, and the RED-first observations of
its two `New arm:` lines, `tools/drift-audit/selftest.py` (AC7, AC8) and `ratchet selftest`'s
`regrammared` plant (AC12).

**Evidences:** TOOL-dWitnessedBar-16
- AC1 — `legacy_ledger.py read` — the rule over `git ls-files memory/project memory/map tools`, the
  two map names staged as `.txt`, finds 33 paths; less the three §3 leaves to unit 18 and F16's six,
  each is the home of exactly one registration. `tools/lib/legacy_ledger.py read <population>` exits 0
  for all 26 registrations but `readme-contract`, whose worktree home stays legacy until the main
  loop's conversion commit (§8 F15). Each new registration's `seed` is S3's `read-back` argv, and
  `memory/builds/dWitnessedBar/BACKLOG.md` holds TOOL-dWitnessedBar-99, `FIVE REGISTRIES STAY IN THEIR
  GRAMMAR`.
- AC2 — `legacy_ledger.py read` — the conversion record's before and after counts match the factory's
  read of each home; every legacy key appears once with its count (`unarmed-branches` 173 rows (DERIVED) to 166
  keys summing to 173; `readme-contract` 218 lines, its `exempt-pin:` line retired, to 217 rows (DERIVED)), and
  every former reason sits beside its key in the record.
- AC3 — `def read_registry` — `git grep -n "def read_registry" -- tools/gate-lint` prints nothing.
  `check_retirements` over the converted `refusal-retirements.txt` reads 5 rows (DERIVED) with no problem; its
  signature and replay refusals are probed by the function, and the scratch-clone `--check` runs are
  owed to the close, the leg's argv being a gate.
- AC4 — `shell hygiene (a fork spent on builtin work)` — `resolve_declaration` reads the converted
  `spawn-idiom-sites.txt` as 298 keys summing to 2236 with no malformed row, and `check_registry`'s
  both-ways grading is unchanged; the leg's two scratch-clone directions are owed to the close.
- AC5 — `baseline.txt` — `git ls-files memory/map/` lists `baseline.txt` and `affordance-exempt.txt`
  and no `.toml` of either name; `gen_map.py --check` reports only `symbols.json` stale, the map
  generator's output this pass may not write beside its generator (`--dispatch` check 49), so the main
  loop regenerates it. `adopt-codebase-map.sh --scaffold` on a fresh scratch target exited 0, printed
  `unarmed memory/map/affordance-exempt.txt dead probe`, and left the one
  `# unarmed · dead probe · <sha>` line.
- AC6 — `--check-format` — `read_contract_rows` and `check_contract_registry` over today's legacy
  `readme-contract.txt` return 148 bound and 69 exempt paths through S7's transitional read, the
  exempt compare printing `UNGRADED` for the legacy base; over the converted bytes in a scratch root the
  same 148 and 69. The scratch-clone probe with the converted file at `origin/main` is owed to the main
  loop's conversion commit.
- AC7 — `drift_report.py --json` — `shrink_only_lists_not_shrinking` reports `of` 18, the number of
  `shrink-only` registrations, and `git grep -nP "^(SHRINK_ONLY|PINS|BASELINES)\b" -- tools/drift-audit/`
  prints nothing.
- AC8 — `low water` — `derive_low_waters` counts non-`#` lines and every converted home's header is a
  `#` line; `id-orphan-waiver.txt` converts to its header and an unarmed line, zero rows as before. The
  before-and-after run in a scratch clone needs the conversion committed, so it is owed to the close.
- AC9 — `merge: rows` — `git check-attr merge` prints `merge: rows` for
  `memory/project/spawn-idiom-sites.txt`, `tools/playbook-kit-waivers.txt` and
  `memory/map/baseline.txt`; `.gitattributes` carries the line for all 25 converted and drift homes.
- AC10 — `convert_registry.py up` — on a scratch adopter holding `HEAD`'s legacy
  `unarmed-branches.txt`, `up` exited 0 printing 173 reasons and wrote the header `# ledger ·
  unarmed-branches · key site path,check,signature · direction shrink-only · drain hunk`; `witness`
  exited 0; `convert` again exited 0 and wrote nothing (byte-compared); `down` restored the legacy bytes
  (byte-compared).
- AC11 — `owed_rows.py --base HEAD` — exits 0 printing `0 rows owed` over the renamed baseline. The
  `--selftest` run and the leg-removed scratch clone are owed to the close.
- AC12 — `regrammared at` — `check_regrammared_at_base` over gov's tree reads every in-place home
  regrammared and the two map and two drift homes `new at`, as Rollout states; the `--fixture --plant
  regrammared` run is the `New arm:` the close observes RED then GREEN.
- AC13 — `read-back` — `convert_registry.py read-back spawn-idiom-sites` prints 298 lines (DERIVED), each `path`,
  `class` and count TAB-joined; `read-back id-orphan-waiver` prints one `dead probe:` line; F14's four
  homes read `unarmed` through `read_home_state`. The `ratchet.py populated` and `unarmed` legs are owed
  to the close.
- AC14 — `read_legacy_rows` — S12's pass, not this one: the transitional read and its one fixture arm
  stay in `gen_build_index.py` until it.
