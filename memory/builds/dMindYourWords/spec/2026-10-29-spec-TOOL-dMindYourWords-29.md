# TOOL-dMindYourWords-29 — the round-1 spec audit's 49 minors, batched: one stdout for the ledger, every reader of a moved fact, honest failure states, and the observations that read the wrong thing

**Status:** DEFERRED · rev-3 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 19 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md) | research | TOOL-dMindYourWords-22 TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`)
confirmed 56 findings, its seven highs units 22 to 28. This unit is BUILD-METHOD M4's batch of its 33
MEDIUM and 16 LOW by raw id, one scope item per id. They land on every one of units 1 to 17, so it
repairs no unit in particular and builds last (order 19), after every unit it repairs.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M7 | MEDIUM | 8, 19, 32, 33 | S7, S8, S9, S10 |
| M10 | MEDIUM | 15, 46 | S13, S14 |
| M11 | MEDIUM | 16, 35 | S15, S16 |
| M17 and L8 | MEDIUM and LOW | 37 and 22 | S22 and S41, one fix |

Every other item is one id and one scope item in report order: M1 to M6 (ids 2, 3, 4, 5, 6, 7) are S1
to S6, M8 (id 13) is S11, M9 (id 14) S12, M12 to M16 (ids 25, 26, 28, 29, 36) S17 to S21, M18 to M28
(ids 38, 39, 40, 47, 48, 50, 51, 52, 53, 54, 55) S23 to S33, and L1 to L16 less L8 (ids 9, 10, 11, 12,
17, 20, 21, 27, 30, 34, 41, 42, 56, 57, 58) S34 to S49 less S41.

## 2. Scope (IN)

- **S1** — id 2, item M1, landing on units 1, 5 and 10. Under `--measure`, stdout is the ledger file and
  nothing else: the class line (unit 1 S1), the `lexicon: suppressed=` tally (unit 5 S5), the
  `lexicon: drift=` tally (unit 10 S8) and every other `lexicon:` notice print to stderr in that mode,
  and unit 10 AC4's reading of the drift tally comes from `--list`. Observed by AC1.
- **S2** — id 3, item M2, landing on unit 14. `tools/memory-tree/extract_code.py`, the third copy
  TOOL-dTotalRecall-8 adds, carries unit 14 S3's IIFE edit byte-identical to the canonical block in
  `tools/lib/extract_code.py`, held by that block's parity row. Observed by AC2.
- **S3** — id 4, item M3, landing on units 1 and 24. `POLICY_DEFAULTS` holds one row for each catalogue
  key whose `owner` is `dMindYourWords`, at its catalogue default (`tools/policy/catalogue.toml:388`,
  `:394`, `:400`, `:406`, `:412`): `lexicon.pin`, `lexicon.forced`, `lexicon.at-commit`,
  `lexicon.drift` and `lexicon.packs`. Unit 1's parity arm compares the two key sets for equality both
  ways and each default for equality. Observed by AC3.
- **S4** — id 5, item M4, landing on unit 1. With no ledger home and `read_legacy_pin` returning `None`,
  the pin reads an empty ledger: every debt key is an `undeclared site`, which is today's reading of an
  absent scalar as 0 (`tools/lexicon/lexicon.py:3054-3057`), and one line names the state, `lexicon: no
  debt ledger and no legacy pin — every debt offender is undeclared` (§8 F1). Observed by AC4.
- **S5** — id 6, item M5, landing on units 2, 3 and 10. The pin's falls these units produce live in the
  ledger home `.lexicon-debt.txt` (TOOL-dMindYourWords-27), never in `.lexicon.conf`, which they edit
  only for their own blocks, `CONTRACTS:`, `FAMILIES:` and `NOUNS:`; a pin line any of their passes
  wrote into the conf moves into the home. Observed by AC5.
- **S6** — id 7, item M6, landing on unit 16. The signals fixture of unit 16 AC4 declares
  `OUT_OF_SCOPE:` with the row `memory/builds/**  build records`, so the record defining `seed_r` stays
  out of the walk. Observed by AC6.
- **S7** — id 8, item M7, landing on unit 17. Unit 17's carrier sweep is observed by the anchored
  pattern `(?<!un)attended sessions?\b`, which cannot match inside `unattended`. Observed by AC7.
- **S8** — id 19, item M7, landing on unit 17. `tools/unattended/PROTOCOL.template.md:512`, "reads the
  WORKTREE conf only in an attended session (§1)", is a row-A carrier and is reworded to the
  owner-session sense unit 17 settles. Observed by AC8.
- **S9** — id 32, item M7, landing on unit 17. `tools/hooks/format-guard.js:12`, "unattended session
  emitted none", keeps its sense and its words; S7's pattern does not select it. Observed by AC9.
- **S10** — id 33, item M7, landing on unit 17. The render `memory/guides/UNATTENDED-PROTOCOL.md` is
  regenerated from the template, never hand-edited, and stays within its cap of 66,860 bytes
  (`tools/template-size-limits.txt:146`), so S8's rewording adds no byte. Observed by AC10.
- **S11** — id 13, item M8, landing on unit 1. `main`'s stdout reconfigure (`tools/lexicon/lexicon.py:4432`)
  sets `newline="\n"` beside its encoding, so the ledger `--measure` prints is LF on every node.
  Observed by AC11.
- **S12** — id 14, item M9, landing on unit 1. The policy-read paragraph of `tools/lexicon/README.md`
  states that `policy.py get` serves the last valid revision under `policy-file.on-invalid = last-valid`
  (`tools/policy/policy.py:742-748`), and `read_policy_value`'s out-of-catalogue refusal stays as
  defence in depth. Observed by AC12.
- **S13** — id 15, item M10, landing on units 7 and 8. `tools/lexicon/pack.py` and
  `tools/lexicon/stack_census.py` import `tomllib` under a guard; without it the run prints one problem
  line, `packs need Python 3.11+ (running <version>)`, and exits 1, never a traceback. The kit README and
  the lexicon section of `WIRE-INTO-PROJECT.md` state the packs' 3.11 floor. Observed by AC13.
- **S14** — id 46, item M10, landing on units 1 and 24. `read_policy_value` maps an exit of the policy
  subprocess other than 0 or 2 to a refusal naming the interpreter, `policy read failed for <key> under
  <python> <version>: <stderr tail>`. Observed by AC14.
- **S15** — id 16, item M11, landing on unit 11. Steps 3 and 4 of the `govkit:entry lexicon` section of
  `WIRE-INTO-PROJECT.md` (`:681-688`) write the first vocabulary record through the stand-in command
  unit 11 S7 names, and step 4's "the stamp is present" reads "a vocabulary record exists". Observed by
  AC15.
- **S16** — id 35, item M11, landing on unit 11. `memory/map/features/lexicon.md:90-91` and the comment
  at `.gitattributes:223` name the vocabulary record where they name the `ratified` stamp. Observed by
  AC16.
- **S17** — id 25, item M12, landing on units 1 and 9. One move rule for both arms: unit 1's
  `check_debt_pin` runs unit 9's `check_added_keys` cross-file tail match after `carry_renames` and
  before `compare_counts`, so a definition moved between files with no `git mv` reads as moved under
  the pin and under `--compare` alike. Observed by AC17.
- **S18** — id 26, item M13, landing on unit 11. `read_vocabulary_record` reads change records through
  `build_records.py read` by subprocess, located with `resolve_kit_dir("memory-tree", "build_records.py",
  KIT_DIR)`, keeping kind `change` and the `unit.lexicon.*` tags and reading a refused record as no
  record; TOOL-dMindYourWords-28 S3's added set for a root commit carries over. Observed by AC18.
- **S19** — id 28, item M14, landing on units 10 and 13. Unit 10's per-name noun check is factored out
  of `scan_noun_variants` as `check_noun_subtokens(subtokens, form_index)`, and unit 13's
  `check_tag_name` calls it for its `noun` rule with the merged noun form index, overlay rows included.
  Observed by AC19.
- **S20** — id 29, item M15, landing on unit 5. An ask row in `memory/builds/dScaffoldedMirror/BACKLOG.md`,
  in that file's grammar, records that TOOL-dMindYourWords-5 S1 to S3 deliver TOOL-dScaffoldedMirror-4's
  S1 to S3 with the `<path>::<Class>.<name>` refinement, so -4 narrows to its S4 and S6 remainder.
  Observed by AC20.
- **S21** — id 36, item M16, landing on unit 15. `.lexicon.conf` carries one justification comment per
  extension unit 15 S10 takes out of `LANGS`, `html: dark -> absent`, `svg: dark -> absent`, `log: dark
  -> absent` and `out: dark -> absent`, within 14 lines above `LANGS=` (`DEFAULT_RATCHET_LOOKBACK`,
  `tools/drift-audit/drift_report.py:225`), the form `_check_mode_justified` reads (`:340`). Observed by
  AC21.
- **S22** — id 37, item M17, landing on unit 10. `memory/map/FOUNDATION.md`'s `[claims]` gains
  `lexicon-nouns = []`, the inventory id unit 10 S9 adds, since the map loads that file as a dossier
  under the exact-keys rule (`tools/codebase-map/map_lib.py:1063-1068`). Observed by AC22.
- **S23** — id 38, item M18, landing on unit 5. `memory/map/features/lexicon.md:123-125` and its seam row
  `:235` describe the site-keyed, reasoned, provenance-checked suppression registry unit 5 builds, the
  seam named `lexicon.site-keyed-suppressions`, and `memory/map/generated/` is re-rendered. Observed by
  AC23.
- **S24** — id 39, item M19, landing on unit 16. Unit 16 S5's move of drift-audit's lexicon arms takes
  the whole functions `test_lexicon_signals` (`tools/drift-audit/selftest.py:1018`) and
  `test_lexicon_marginal_rate` (`:1151-1332`) with their runner calls (`:4501-4502`) into
  `tools/lexicon/selftest.py`, by function and never by line range, the all-ungradeable, admit-a-verb and
  shallow DEAD PROBE arms (`:1297`, `:1311`, `:1322`) among them, each pointed at
  `tools/lexicon/lexicon_signals.py`. Observed by AC24.
- **S25** — id 40, item M20, landing on unit 16. Step 4 of the `govkit:entry lexicon` section of
  `WIRE-INTO-PROJECT.md` names the four kit legs unit 16 S4 puts in the pack, `lexicon naming
  predicates`, `lexicon wiring`, `lexicon drift signals` and `lexicon offenders by name`. Observed by
  AC25.
- **S26** — id 47, item M21, landing on unit 9. The commit arm's family candidates match the object's
  forms at a subtoken boundary, never as `git grep -l -i` substrings: a form preceded by the start, a
  non-alphanumeric character, an underscore or a lower-to-upper case change, and followed by the end, a
  character that is not a lowercase letter or digit, or an underscore. Each candidate is confirmed by
  extraction, and a block past its `budget-ms` completes and prints `lexicon: commit arm took <ms> ms
  over its <budget> ms budget` (§8 F2). Observed by AC26.
- **S27** — id 48, item M22, landing on unit 10. The drift blame asks `git rev-parse
  --is-shallow-repository` first; `true` prints `lexicon: drift not measured — shallow history` and
  grades no `drift` key, and the kit README states that drift needs full history. Observed by AC27.
- **S28** — id 50, item M23, landing on unit 12. The binding model: an import is module-level when no
  function or class body holds it, conditional blocks included; a name bound more than once keeps the
  set of its targets, any member matching for units 2 and 4; `qualname` is Python's `__qualname__`,
  `f.<locals>.g` for a def nested in a function; `enclosing` is set only when a class body holds the def
  directly. Observed by AC28.
- **S29** — id 51, item M24, landing on unit 8. The requirements reader joins `\` continuations,
  follows `-r`, skips every other line opening `-`, strips an environment marker after `;`, extras in
  `[...]` and a `--hash=` tail, and refuses only a line that is none of these. It reads every tracked
  `requirements*.txt` and `requirements/*.txt` and Poetry's `[tool.poetry.dependencies]` table, and
  names a manifest-like file it does not read, `Pipfile`, by path. Observed by AC29.
- **S30** — id 52, item M25, landing on unit 11. `--check-record` compares, for each changed tag, the
  staged record's `After` with `--print-hash` at the index and its `Before` with the hash at HEAD,
  refusing with both on a mismatch. Observed by AC30.
- **S31** — id 53, item M26, landing on unit 3. `check_contract_record` walks the non-merge commits
  touching `.lexicon.conf` (`git log --full-history --no-merges`) and requires each whose `CONTRACTS:`
  rows differ from its parent's to add a `unit.lexicon.contracts` record; a merge whose rows equal its
  parents' combined rows needs none. Observed by AC31.
- **S32** — id 54, item M27, landing on unit 3. `check_contract_pointers` runs `annotations.py index` with
  a timeout, and a non-zero exit, an unparseable line or a timeout reds `contract pointers unreadable —
  <why>`, never a pass and never `not graded`. Observed by AC32.
- **S33** — id 55, item M28, landing on unit 16. The `lexicon drift signals` leg's `guard` and `doc_reads`
  in `tools/lexicon/kit.toml` carry `{memory_root}/builds/`, so a push touching only the vocabulary
  records runs the leg, re-rendered into `tools/gate-legs.json`. Observed by AC33.
- **S34** — id 9, item L1, landing on unit 1. The upgrade step was built against TOOL-dSafePassage-1, an
  ancestor through dWitnessedBar, dDeclaredLoop and dOrderedCharter, so no ask or deviation record from
  unit 1 §8 F2's fallback branch stands in this build's records. Observed by AC34.
- **S35** — id 10, item L2, landing on units 4 and 6. Their version observation is made relative to each
  pass's base: the pass commit of each, found by its subject naming the unit, changes
  `KIT_LEXICON_VERSION`. Observed by AC35.
- **S36** — id 11, item L3, landing on unit 1. Unit 1 AC3's case is observed with a `widened:<record>` row
  whose record the branch adds and which is no vocabulary record, so it stays red under `shrink-only`
  after unit 11's admission and TOOL-dMindYourWords-26's narrowing, and green under `absorb`. Observed
  by AC36.
- **S37** — id 12, item L4, landing on unit 14. Unit 14 AC2's repeated-header observation counts per
  key, `grep -oE '^(VERBS|CELLS|PATTERNS|CANON):' .lexicon.conf | sort | uniq -d`. Observed by AC37.
- **S38** — id 17, item L5, landing on unit 1. `WIRE-INTO-PROJECT.md:679`, "MEASURES both offender
  pins", reads that the scaffold writes the debt ledger `.lexicon-debt.txt` from the adopter's own
  measurement. Observed by AC38.
- **S39** — id 20, item L6, landing on unit 9. Unit 9 S9's replay boundary is spelled absolutely,
  `--since=2026-08-16T00:00:00`, in its record script and in the figure it pins, re-derived with that
  spelling. Observed by AC39.
- **S40** — id 21, item L7, landing on unit 8. The census keeps only keys that are identifiers or dotted
  identifiers, so the js `require(...)` match in a comment (`tools/policy/policy-mirror.js:4`, key
  `<this kit>`) is no kit, and the packs line on this tree names the third-party names the rule reports.
  Observed by AC40.
- **S41** — id 22, item L8, landing on unit 10. Unit 10 S9's readers include `memory/map/FOUNDATION.md`,
  the one fix S22 makes, observed over that file and every file under `memory/map/features/`. Observed
  by AC41.
- **S42** — id 27, item L9, landing on units 5 and 10. One porcelain blame reader in
  `tools/lexicon/lexicon.py`, `read_blame_lines(root, rel, lines=None, rev=None, contents=None,
  ignore_ws=False) -> {lineno: (commit, author_time, boundary)}`, run with `--root` as
  TOOL-dMindYourWords-28 S2 requires and returning the zero id for an uncommitted line. Unit 5's
  provenance calls it with `ignore_ws=False` and keeps its zero-id index check; unit 10's drift blame
  calls it with `ignore_ws=True` and reads the zero id as latest. Observed by AC42.
- **S43** — id 30, item L10, landing on unit 9. `--compare` imports `resolve_compare_base` from the kit's
  own `tools/lexicon/coverage_join.py`, so the engine carries no second inline copy of the compare base
  or its remote ladder. Observed by AC43.
- **S44** — id 34, item L11, landing on unit 11. `.githooks/pre-commit.test.sh` gains an arm staging
  `.lexicon.conf` with a changed `VERBS` row and no record, asserting the refusal of unit 11 S4's
  `lexicon vocabulary record, staged leg` block; §7 names `branch-guard self-test` and the python
  resolver leg. Observed by AC44.
- **S45** — id 41, item L12, landing on unit 13. Unit 13's Skill template, its render and its
  `load_conf` refusal are observed by the `lexicon wiring` check, which §7 names. Observed by AC45.
- **S46** — id 42, item L13, landing on unit 16. Ask TOOL-aMendedFleet-96 is answered: a closing row in
  `memory/builds/aMendedFleet/BACKLOG.md`, in that file's grammar, `CLOSED · TOOL-aMendedFleet-96 · by
  TOOL-dMindYourWords-16 · answered by ...`, since unit 16 S5 leaves `drift_report.py` with no reader of
  its own. Observed by AC46.
- **S47** — id 56, item L14, landing on units 6 and 8. `--suggest` maps a `PackError` from a malformed
  custom pack declared in `PACKS:` to exit 2, printing the `PackError` line, inside its 0-or-2 contract.
  Observed by AC47.
- **S48** — id 57, item L15, landing on unit 15. `check_out_of_scope` returns the first-matching glob with
  its reason, the walk stores both, `--list` counts per glob, and a row an earlier row shadows prints
  `shadowed by <glob>`. Observed by AC48.
- **S49** — id 58, item L16, landing on unit 5. A suppression row's key runs to the first whitespace after
  its last `::`, so a path holding a space has a legal spelling; both registries' headers state the
  rule. Observed by AC49.

## 3. Non-goals (OUT)

- Any high: units 22 to 28, one per id.
- The left-shift lints and checklist entries the report names: each is a gate, its own unit (BUILD-METHOD
  M2), and no clause of this build names one.
- Re-reviewing or re-wording a repaired unit's spec (M4): each item is built and observed at this pass.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `--measure`, `POLICY_DEFAULTS`, `read_policy_value`, `read_legacy_pin`, `check_debt_pin`, the upgrade step and AC3's case (ids 2, 4, 5, 9, 11, 13, 14, 25, 46)
- **consumes-from** `TOOL-dMindYourWords-2` — its pin falls and Files touched (id 6)
- **consumes-from** `TOOL-dMindYourWords-3` — its pin falls, `check_contract_record` and `check_contract_pointers` (ids 6, 53, 54)
- **consumes-from** `TOOL-dMindYourWords-4` — its pass commit and the version it moves (id 10)
- **consumes-from** `TOOL-dMindYourWords-5` — the suppressed tally, the registry grammar, the provenance blame and the dossier's waiver seam (ids 2, 27, 29, 38, 58)
- **consumes-from** `TOOL-dMindYourWords-6` — its pass commit and `run_suggest` (ids 10, 56)
- **consumes-from** `TOOL-dMindYourWords-7` — `pack.py`'s `tomllib` read (id 15)
- **consumes-from** `TOOL-dMindYourWords-8` — the census, the manifest reader and `stack_census.py` (ids 15, 21, 51, 56)
- **consumes-from** `TOOL-dMindYourWords-9` — `check_added_keys`, the commit arm's candidates, the replay and `--compare`'s base (ids 20, 25, 30, 47)
- **consumes-from** `TOOL-dMindYourWords-10` — the drift tally, the drift blame, `scan_noun_variants`, its pin falls and its noun inventory id (ids 2, 6, 22, 27, 28, 37, 48)
- **consumes-from** `TOOL-dMindYourWords-11` — `read_vocabulary_record`, `--check-record`, the hook block and the retired stamp's readers (ids 16, 26, 34, 35, 52)
- **consumes-from** `TOOL-dMindYourWords-12` — the binding model of `extract_ranges` with `context=True` (id 50)
- **consumes-from** `TOOL-dMindYourWords-13` — `check_tag_name`'s noun rule and its Skill and conf edits (ids 28, 41)
- **consumes-from** `TOOL-dMindYourWords-14` — the IIFE edit and AC2's repeated-header case (ids 3, 12)
- **consumes-from** `TOOL-dMindYourWords-15` — the removed `LANGS` rows and `check_out_of_scope` (ids 36, 57)
- **consumes-from** `TOOL-dMindYourWords-16` — the signals fixture, the moved arms, the pack's legs, the drift-signals guard and the deleted reader (ids 7, 39, 40, 42, 55)
- **consumes-from** `TOOL-dMindYourWords-17` — the carrier sweep, its row A and its AC2 pattern (ids 8, 19, 32, 33)
- **consumes-from** `TOOL-dMindYourWords-23` — `--measure`'s stdout as the ledger file alone (ids 2, 13)
- **consumes-from** `TOOL-dMindYourWords-24` — `read_policy_value` located through the receipt (ids 4, 14, 15, 46)
- **consumes-from** `TOOL-dMindYourWords-26` — the narrowed `widened:<record>` admission (id 11)
- **consumes-from** `TOOL-dMindYourWords-27` — the home `.lexicon-debt.txt` (ids 6, 17)
- **consumes-from** `TOOL-dMindYourWords-28` — the shallow refusal, `--root` and the root-commit added set (ids 26, 27)
- **hands-off** `TOOL-dMindYourWords-31` — S42's `read_blame_lines` and S31's contract walk, which that unit runs under the kit's one history pin (review id 11)
- **hands-off** `TOOL-dMindYourWords-36` — S31's per-commit contract walk, which that unit widens to merges (review id 35)
- **hands-off** `TOOL-dMindYourWords-37` — S1, S11, S18, S19, S20, S24, S27, S29, S33, S42, S46 and their criteria, which the minors batch repairs (review ids 3, 4, 5, 10, 16, 20, 24, 27, 28, 36, 37, 38, 39 and 40)
- **consumes-from** `TOOL-dMindYourWords-42` — `--ignore-revs-file=` on the provenance blame, which S42's `read_blame_lines` keeps when it becomes the kit's one blame reader

## 4. Design

### Why one unit and not two

M4 admits two batches only when the minors split into two disjoint write sets by M6. They nearly do:
S7 to S10, S20 and S46 touch only the unattended protocol, its render and two other builds' backlogs.
Every other item meets `tools/lexicon/lexicon.py`, `WIRE-INTO-PROJECT.md` or `.lexicon.conf`. The rule
permits the split and never requires it, and the batch builds after every other unit, so a second unit
buys no concurrency against the roster and doubles the edges and the audit; the batch stays one unit
(§8 F3).

### Evidence

- `--measure` today prints the scalar pins, the `PINS:` rows and `# NOTE:` lines to stdout
  (`tools/lexicon/lexicon.py:3552-3574`), and `main` reconfigures stdout's encoding only (`:4432`).
- An absent pin scalar reads as 0 (`tools/lexicon/lexicon.py:3054-3057`).
- The five `lexicon.*` catalogue rows, each `owner = "dMindYourWords"`, sit at
  `tools/policy/catalogue.toml:387-415`; `resolve_read` sends a file with problems to
  `read_last_valid_value` (`tools/policy/policy.py:742-748`).
- `lexicon.py` documents a 3.10 floor and carries no `tomllib` import
  (`tools/lexicon/lexicon.py:2383-2387`).
- `tools/unattended/PROTOCOL.template.md:512` holds the session sense, `tools/hooks/format-guard.js:12`
  the kept one; the render measures 66,859 bytes against a cap of 66,860
  (`tools/template-size-limits.txt:146`), PINNED at `a1f119ec6`.
- The anchored pattern `(?<!un)attended sessions?\b` prints 11 lines over `tools`, `skills`,
  `WIRE-INTO-PROJECT.md` and `help` at `a1f119ec6`, none of them `format-guard.js`.
- `WIRE-INTO-PROJECT.md:679` says the scaffold "MEASURES both offender pins", `:681-688` stamps
  `ratified`, and `:686-689` names two lexicon legs.
- drift-audit's LANGS ratchet ranks a removed extension as a weakening unless `<ext>: dark -> absent`
  sits within `DEFAULT_RATCHET_LOOKBACK` (14) lines above `LANGS=`
  (`tools/drift-audit/drift_report.py:225`, `:340`, `:367`, `:4361`).
- `memory/map/FOUNDATION.md:21` ends its `[claims]` at `lexicon-verbs = []`, and the map raises
  `MapError` on a missing claim key (`tools/codebase-map/map_lib.py:1063-1068`).
- `memory/map/features/lexicon.md:123` keys waivers on matched text and `:235` declares `seam:
  lexicon.text-keyed-waivers`.
- In `tools/drift-audit/selftest.py`, `test_lexicon_signals` opens at `:1018`, `test_lexicon_marginal_rate`
  spans `:1151-1332` and `test_backlog_stragglers` opens at `:1334`.
- `tools/lexicon/lexicon.py:2335` splits a waiver row with `s.split(None, 1)`, and `:151`'s js
  `require(...)` regex has no comment exclusion.
- `memory/backlog/TOOL.md:174` lists TOOL-aMendedFleet-96 OPEN; `memory/builds/dScaffoldedMirror/BACKLOG.md:29`
  holds TOOL-dScaffoldedMirror-4 DEFERRED on `path::name`.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S3, S4, S11, S12, S14, S17, S19, S26, S27, S36, S42, S43, S47, S49, `KIT_LEXICON_VERSION`
- `tools/lexicon/lexicon_conf.py`: S18, S30, S48
- `tools/lexicon/pack.py` and `tools/lexicon/stack_census.py`: S13, S29, S40
- `tools/lexicon/selftest.py`: S6, S24 and the arm of §7
- `tools/lexicon/kit.toml` and its render `tools/gate-legs.json`: S33
- `tools/lexicon/README.md`, `tools/lexicon/lexicon-verb-waivers.txt` and `tools/lexicon/lexicon-suffix-waivers.txt`: S12, S13, S27, S49
- `tools/lib/extract_code.py`, `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py` and `tools/memory-tree/extract_code.py`: S2, S28
- `tools/drift-audit/selftest.py`: S24
- `.lexicon.conf`: S5, S21
- `.githooks/pre-commit.test.sh`: S44
- `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`: S8, S10
- `WIRE-INTO-PROJECT.md`: S13, S15, S25, S38
- `memory/map/FOUNDATION.md`, `memory/map/features/lexicon.md` and `memory/map/generated/`: S16, S22, S23
- `.gitattributes`: S16
- `memory/builds/dScaffoldedMirror/BACKLOG.md`: S20
- `memory/builds/aMendedFleet/BACKLOG.md`: S46
- `memory/builds/dMindYourWords/build/`: S39's record script

### Migration

None beyond S5's move of any pin line into the home and S21's comments; every other item edits code,
docs or a fixture.

### Rollout

Live at landing, the last unit of the build, so the merge bar at the close grades the repaired tree
once.

### Alternatives rejected

- **One unit per minor**: M4 forbids it.
- **Folding each fix into the repaired unit's spec**: the audit's exit folds none (M4, owner rulings DIFF
  2026-10-04 and SPEC 2026-10-05).

## 5. Production-readiness checklist

- security — S14 and S32 turn two silent failures into refusals; S18 reads a record only through its
  factory; no new write path beyond two ask rows the build README's outside-write rule admits.
- perf / scale — S26 bounds the commit arm's candidates; every other item is linear in what it reads.
- error / empty / loading states — S4, S13, S14, S27, S32 and S47 each name a state the repaired unit
  left undefined.
- observability — every new refusal names its cause and its file.
- risks — an item whose defect bites while its unit builds, a Files-touched omission (S2, S5, S10) or a
  fixture (S6), is met by that unit's builder through M2's AMEND route at build time; this pass
  re-observes the repaired state rather than assuming it.
- testing — AC1 to AC49 and the arms of §7.
- migration — S5, S21.
- user docs — `tools/lexicon/README.md`, `WIRE-INTO-PROJECT.md` and the lexicon dossier.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --measure 2>/dev/null` runs at the pass, `grep -c
  '^lexicon:'` over its stdout prints 0, and that stdout written over a scratch copy of the home leaves
  `python legacy_ledger.py read lexicon-debt`, the factory's copy in `tools/lexicon/`, exiting 0 there;
  `--list` prints the `drift=` and `suppressed=` tallies.
  Red when: a tally line reaches `--measure`'s stdout, so the drain edit writes it into the ledger.
- **AC2** — When `git grep -c -F '\([^()]*\)' -- '*/extract_code.py'` runs, it prints one equal, nonzero
  count for each copy it lists, the four under `tools/lib/`, `tools/lexicon/`, `tools/codebase-map/` and
  `tools/memory-tree/` among them.
  Red when: the memory-tree copy lacks the IIFE edit.
- **AC3** — When `python -c "import sys; sys.path.insert(0, 'tools/lexicon'); import lexicon;
  print(sorted(lexicon.POLICY_DEFAULTS.items()))"` runs, it prints the five `lexicon.*` keys at their
  catalogue defaults, and `python tools/lexicon/lexicon.py` in a fixture with no policy kit exits by its
  verdict with no `KeyError`.
  Red when: a key owned by this build has no row, so a run without the policy kit raises.
- **AC4** — When `python tools/lexicon/lexicon.py` runs in a fixture with no ledger home and no legacy
  seam, one debt offender makes it exit 1 naming `undeclared site` and the S4 line; with none it exits 0
  printing the line.
  Red when: the state greens with debt present, or raises.
- **AC5** — When `grep -cE '^(VERB|SUFFIX)_OFFENDER_PIN=|^PINS:' .lexicon.conf` runs, it prints 0, and
  `python tools/lexicon/lexicon.py --measure 2>/dev/null` equals `.lexicon-debt.txt`.
  Red when: a fall sits in the conf, or the home disagrees with the measurement.
- **AC6** — When `python lexicon_signals.py` runs over unit 16's signals fixture, it names
  `seed` among the unused verbs.
  Red when: the record's `seed_r` counts as a use.
- **AC7** — When `git grep -n -i -P '(?<!un)attended sessions?\b' -- tools skills help README.md
  WIRE-INTO-PROJECT.md` runs after the pass, it prints nothing.
  Red when: a session-sense carrier survives.
  figure: DERIVED; 11 lines at `a1f119ec6`, before unit 17's pass.
- **AC8** — When `grep -n -i -P '(?<!un)attended session' tools/unattended/PROTOCOL.template.md` runs, it
  prints nothing.
  Red when: the template keeps the session sense at `:512`.
- **AC9** — When `grep -c 'unattended session' tools/hooks/format-guard.js` runs, it prints 1.
  Red when: the kept line was reworded to satisfy an unanchored grep.
- **AC10** — When `wc -c < memory/guides/UNATTENDED-PROTOCOL.md` runs, it prints at most 66860, and
  `grep -n -i -P '(?<!un)attended session' memory/guides/UNATTENDED-PROTOCOL.md` prints nothing.
  Red when: the render is hand-edited, stale or over its cap.
  figure: PINNED 66,859 bytes at `a1f119ec6`.
- **AC11** — When `python tools/lexicon/lexicon.py --measure 2>/dev/null | od -c | grep -c '\\r'` runs on
  a Windows node, it prints 0.
  Red when: a carriage return reaches the ledger the drain edit writes.
- **AC12** — When a fixture commits `.governance/policy.toml` with `lexicon.pin = "absorb"` and then
  `"loose"`, `python tools/lexicon/lexicon.py` grades as `absorb`; with `policy-file.on-invalid =
  "refuse"` committed as well, it exits 1 naming the refused read.
  Red when: the run reads the invalid value as the default, or refuses where `get` falls back.
- **AC13** — When `python -c "import sys, runpy; sys.modules['tomllib'] = None; sys.argv =
  ['lexicon.py']; runpy.run_path('tools/lexicon/lexicon.py', run_name='__main__')"` runs, it prints
  `packs need Python 3.11+` and no `Traceback`.
  Red when: `ModuleNotFoundError` escapes.
- **AC14** — When a fixture's planted `policy.py` exits 1 with an import error on stderr, `python
  <kit>/lexicon.py` exits 1 naming `policy read failed` and the interpreter.
  Red when: the failure reads as a refused value or as a default.
- **AC15** — When `git grep -n -w 'ratified' -- WIRE-INTO-PROJECT.md` runs, it prints nothing.
  Red when: the runbook still stamps a key nothing reads.
- **AC16** — When `git grep -n -w 'ratified' -- memory/map/features/lexicon.md .gitattributes` runs, it
  prints nothing.
  Red when: the dossier or the attribute comment names the stamp.
- **AC17** — When a fixture moves a ledgered definition to another file with no `git mv`, `python
  tools/lexicon/lexicon.py` names no `undeclared site` and `--compare` names it moved; both exit 0.
  Red when: the two arms disagree on the move.
- **AC18** — When a fixture stages a `VERBS` change with a change record missing `After`, `python
  tools/lexicon/lexicon.py --check-record` exits 1 naming the tag.
  Red when: a record the factory refuses admits the change.
- **AC19** — When `git grep -c 'check_noun_subtokens(' -- tools/lexicon/lexicon.py` runs, it prints at
  least 3, and a fixture with an overlay `NOUNS:` row gives a code name and a tag sharing the word the
  same verdict.
  Red when: the word is debt in one and clean in the other.
- **AC20** — When `git grep -n 'TOOL-dMindYourWords-5' -- memory/builds/dScaffoldedMirror/BACKLOG.md`
  runs, it prints the ask row naming TOOL-dScaffoldedMirror-4.
  Red when: -4 stays open on a different key grammar with no record.
- **AC21** — When `grep -B14 '^LANGS=' .lexicon.conf | grep -cE '(html|svg|log|out): dark -> absent'`
  runs, it prints 4.
  Red when: a removed extension reads as an unjustified weakening.
- **AC22** — When `grep -L 'lexicon-nouns' memory/map/FOUNDATION.md memory/map/features/*.md` runs, it
  prints nothing.
  Red when: a dossier the map loads lacks the claim key.
- **AC23** — When `git grep -n -e 'text-keyed-waivers' -e 'key on the matched TEXT' -- memory/map` runs,
  it prints nothing.
  Red when: the dossier steers reuse to the text-keyed model.
- **AC24** — When `grep -c -E 'def test_lexicon_(signals|marginal_rate)' tools/drift-audit/selftest.py`
  runs, it prints 0; and when `python lexicon_signals.py` runs in a `git clone --depth 1` of unit 16's
  signals fixture, it prints the rate's `dead probe:` line, the case the moved shallow arm stages red.
  Red when: an arm is left behind in drift-audit, or the shallow probe the moved arm holds is gone.
- **AC25** — When `grep -c -e 'lexicon drift signals' -e 'lexicon offenders by name' WIRE-INTO-PROJECT.md`
  runs, it prints at least 2, and `grep -n 'emits two gate legs' WIRE-INTO-PROJECT.md` prints nothing.
  Red when: the runbook wires two of four legs.
- **AC26** — When `time python tools/lexicon/lexicon.py --staged` runs in a fixture declaring a family
  whose object is `conf`, over 200 or more files spelling it and one staged definition, it finishes
  under 2 s.
  Red when: the candidate set runs past the hook's `budget-ms`.
  cost: seconds; fixture: a scratch repository under `%TEMP%`.
- **AC27** — When `python <kit>/lexicon.py` runs in a `git clone --depth 1` of unit 10's drift fixture,
  it prints `drift not measured — shallow history` and no `drift` row.
  Red when: boundary times grade a drift key.
  fixture: the clone under `%TEMP%/<short>`.
- **AC28** — When `python -c` calls `extract_ranges(src, "py", context=True)` from the canonical
  `extract_code.py` in `tools/lib/` over a module with the `try`/`except ImportError` `override` import,
  an `if TYPE_CHECKING:` base and a closure `emit` inside a `logging.Handler` method, it prints both `override`
  targets, the base resolved, and the closure's qualname `H.handle.<locals>.emit` with no `enclosing`.
  Red when: the idiom resolves `unresolved`, or the closure takes the class.
- **AC29** — When `python tools/lexicon/lexicon.py --list` runs in a fixture holding a pip-compile file
  with `--hash=` continuations and markers, it reads the pinned versions with no refusal, and a `Pipfile`
  beside it prints `manifest not read: Pipfile`.
  Red when: a real-world manifest refuses the run or is read silently as `unknown`.
- **AC30** — When a fixture stages a vocabulary change whose record's `After` is stale, `python
  tools/lexicon/lexicon.py --check-record` exits 1 printing both hashes.
  Red when: a stale record admits a different change.
- **AC31** — When a fixture merges two branches that each add a `CONTRACTS:` row and its record, `python
  tools/lexicon/lexicon.py` exits 0; a later commit deleting a row with no record exits 1 naming it.
  Red when: the merge reds, or an unrecorded change passes.
- **AC32** — When a fixture's planted `annotations.py` exits 2, `python <kit>/lexicon.py` exits 1 naming
  `contract pointers unreadable`.
  Red when: a failed index grades as no notes.
- **AC33** — When `python -c "import json; l = [x for x in json.load(open('tools/gate-legs.json')) if
  x['name'] == 'lexicon drift signals'][0]; print('{memory_root}/builds/' in l['guard'],
  '{memory_root}/builds/' in l.get('doc_reads', []))"` runs, it prints `True True`.
  Red when: a records-only push skips the leg.
- **AC34** — When `python upgrade_steps.py list`, govkit's step reader, runs, it prints
  `lexicon/pin-to-debt-ledger`, and
  `git grep -n 'pin-to-debt-ledger' -- memory/builds/dMindYourWords/BACKLOG.md` prints nothing.
  Red when: the dead fallback left an ask or the step is missing.
- **AC35** — When `git log --format=%s -G'^KIT_LEXICON_VERSION = ' <BASE>..HEAD --
  tools/lexicon/lexicon.py` runs, it lists a subject naming `TOOL-dMindYourWords-4` and one naming
  `TOOL-dMindYourWords-6`.
  Red when: either pass left the version where it found it.
- **AC36** — When a fixture's branch adds a non-vocabulary file and cites it in a `widened:<record>` row,
  `python tools/lexicon/lexicon.py` exits 1 naming `gained` under `shrink-only` and exits 0 under a
  committed `absorb`.
  Red when: unit 1's case contradicts unit 11's or unit 26's admission.
- **AC37** — When `grep -oE '^(VERBS|CELLS|PATTERNS|CANON):' .lexicon.conf | sort | uniq -d` runs, it
  prints nothing.
  Red when: a header repeats.
- **AC38** — When `git grep -n -i 'offender pin' -- WIRE-INTO-PROJECT.md` runs, it prints nothing.
  Red when: the runbook describes a scaffold output that no longer exists.
- **AC39** — When `git grep -n -e '--since=2026-08-16[^T]' -e '--since=2026-08-16$' --
  memory/builds/dMindYourWords/build tools/lexicon` runs, it prints nothing.
  Red when: the replay's boundary moves with the hour it is run.
- **AC40** — When `python tools/lexicon/lexicon.py --list | grep -c '<this kit>'` runs, it prints 0.
  Red when: a comment's `require(...)` reads as a kit.
- **AC41** — When `grep -c 'lexicon-nouns' memory/map/FOUNDATION.md` runs, it prints 1.
  Red when: the foundation dossier lacks the key the map requires.
- **AC42** — When `git grep -c -e "'--porcelain'" -e '"--porcelain"' -- tools/lexicon/lexicon.py` runs, it
  prints 1.
  Red when: a second porcelain blame parser lives in the engine.
- **AC43** — When `git grep -n 'def resolve_compare_base' -- tools/lexicon` runs, it prints one line, in
  the kit's `coverage_join.py`.
  Red when: the engine carries a second copy of the block.
- **AC44** — When `grep -c 'lexicon vocabulary record' .githooks/pre-commit.test.sh` runs, it prints at
  least 1.
  Red when: the hook's new block has no arm in its own suite.
- **AC45** — When `bash tools/lexicon/adopt-lexicon.sh --check-render` runs after the pass, it exits 0.
  Red when: unit 13's Skill edit left the render stale.
- **AC46** — When `git grep -n 'CLOSED · TOOL-aMendedFleet-96' -- memory/builds/aMendedFleet/BACKLOG.md`
  runs, it prints the closing row, and `git grep -c '_read_defs_at_sha' --
  tools/drift-audit/drift_report.py` prints 0.
  Red when: the ask stays OPEN after its subject is gone.
- **AC47** — When `python tools/lexicon/lexicon.py --suggest fetch_rows --as py.function` runs in a fixture
  declaring a malformed custom pack, it exits 2 printing the `PackError` line and no `Traceback`.
  Red when: the verb leaves its 0-or-2 contract.
- **AC48** — When `python tools/lexicon/lexicon.py --list` runs in a fixture whose `OUT_OF_SCOPE:` holds
  two rows sharing a reason and one shadowed row, it prints a count per glob and `shadowed by`.
  Red when: counts merge by reason, or the shadowed row reads as live.
- **AC49** — When `python tools/lexicon/lexicon.py` runs in a fixture whose registry holds the row `a
  b/x.py::emit  reason` for a live offender there, the site is suppressed and no `MALFORMED
  SUPPRESSION` prints.
  Red when: a path holding a space has no legal spelling.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `policy fixtures` · `policy check` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `straggler-guard arms` · `govkit acceptance matrix` · `govkit runbook parity` · `drift-audit selftest` · `drift-audit records` · `branch-guard self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended protocol size` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `memory hygiene` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC3 AC4 AC11 AC12 AC13 AC14 AC17 AC18 AC19 AC27 AC28 AC29 AC30 AC31 AC32 AC36 AC47 AC48 AC49 · one planted fixture per criterion, its failing case each item's change cut out in turn, AC1's a tally line printed to stdout · none
New arm: tools/lexicon/selftest.py · covers AC24 · the moved `test_lexicon_signals` and `test_lexicon_marginal_rate`, their not-asked and shallow arms staged red against `tools/lexicon/lexicon_signals.py` · none
New arm: .githooks/pre-commit.test.sh · covers AC44 · `.lexicon.conf` staged with a changed `VERBS` row and no record, red while the block admits it · none

## 8. Open questions

- **F1 — What does the pin read with no ledger home and no legacy seam (S4)?** Options: (a) an empty
  ledger, every debt key `undeclared site`; (b) unresolved, printed and never green. Both red on debt;
  (a) keeps today's reading of an absent scalar as 0 (`tools/lexicon/lexicon.py:3054-3057`) and greens a
  debt-free tree, where (b) reds one. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the
  behaviour the code already has. widens: none · relaxes: none
- **F2 — What does the commit arm do past its budget (S26)?** Options: (a) complete and print the
  overrun; (b) stop and pass the rest to the bar; (c) stop and refuse. (b) lets a family split through
  the commit it was meant to catch, and (c) blocks a commit for the machine's speed. RESOLVED (agent,
  2026-10-29, delegated): (a), rung 3, the verdict kept whole and the overrun reported. widens: none ·
  relaxes: none
- **F3 — One batch or two (§4)?** Options: (a) one unit; (b) two, the unattended-protocol and backlog
  items apart. The rule permits (b) and requires neither, and (b) buys no concurrency for a unit ordered
  after every other. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, fewer units for the same
  coverage. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from the round-1 spec audit's 33 MEDIUM and 16 LOW
  findings, one scope item per raw id.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-31, TOOL-dMindYourWords-36, TOOL-dMindYourWords-37); no scope, design or criterion moved.
- rev-3 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-42); no scope, design or criterion moved.

## 10. Reuse audit

Each item extends the seam of the unit it repairs, named in its scope item: `check_debt_pin`,
`read_policy_value` and `--measure` (unit 1), `check_added_keys` (unit 9), `scan_noun_variants` (unit
10), `read_vocabulary_record` (unit 11), `extract_ranges` (unit 12) and `check_out_of_scope` (unit 15).
Three reuse findings are the items themselves: S17 joins unit 9's move rule to unit 1's pin, S18 reads
the change record through its factory `tools/memory-tree/build_records.py` located by `resolve_kit_dir`,
and S43 imports the compare base from `tools/lexicon/coverage_join.py`. `python
tools/codebase-map/reuse_lookup.py "detect a shallow git history before trusting blame"` ranked generic
git wrappers and no shallow predicate, so S27 carries the `rev-parse --is-shallow-repository` call
`tools/drift-audit/drift_report.py:1505` already makes; `_build_blame_dates`
(`tools/drift-audit/drift_report.py:1824`) is the porcelain parse S42's one reader mirrors inside the
kit, which imports no sibling.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure rebaseline tags slice check_debt_pin widened shallow provenance"`
