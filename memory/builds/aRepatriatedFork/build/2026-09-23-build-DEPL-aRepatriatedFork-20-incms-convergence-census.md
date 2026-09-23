# inCMS → gov memory-tree convergence — grounded measurements

**Serves:** research DEPL-aRepatriatedFork-20

Measured READ-ONLY on 2026-09-23.

- **gov:** worktree `arepatriated-fork-build-e42158`, HEAD `f8fdd873`. Line numbers below are gov's at that HEAD.
- **inCMS:** primary tree `C:/projects/incms/main`, branch `main`, HEAD
  **`9a0e5ebbe1832683df74f848aa2d93771aa15e68`**. The tree was clean and equal to `origin/main`.
- **Scratch clones:** three `git clone --local --shared` clones of that HEAD, under
  `C:/Users/DAILY-~1/AppData/Local/Temp/`. Nothing was written to the real inCMS tree or to gov.
  - `icx` is pristine, the baseline.
  - `icw` has gov's four programs, `row_grammar.py`, `check-arms.py` and `check-memory-hygiene.sh` copied over `scripts/`.
  - `icv` has a trial mechanical front-matter migration, followed by gov's `gen_build_index.py --write`.

Scripts used, all in the scratchpad: `fm_stats.py`, `hdr_stats.py`, `migrate_trial.py`.

---

## 1. The five programs

### 1a. Where they live and how big they are

| inCMS file | lines | gov counterpart | gov lines | same bytes? |
|---|---|---|---|---|
| `scripts/gen_build_index.py` | 774 | `tools/memory-tree/gen_build_index.py` | 2787 | no |
| `scripts/corpus_ids.py` | 1837 | `tools/memory-tree/corpus_ids.py` | 1259 | no |
| `scripts/gotchas.py` | 664 | `tools/memory-tree/gotchas.py` | 648 | no |
| `scripts/merge-rows.py` | 303 | `tools/memory-tree/merge-rows.py` | 1141 | no |
| `scripts/check-docs-hygiene.sh` (the adopter's engine) | 1671 | `tools/memory-tree/check-memory-hygiene.sh` | 2512 | n/a |

Several other files matter here:

- gov's `check-memory-hygiene.sh` is ALREADY installed at inCMS as `scripts/check-memory-hygiene.sh`.
  It is byte-identical to gov (blob `92aceced`) and no leg calls it.
- `scripts/row_grammar.py` and `scripts/check-arms.py` differ from gov.
- inCMS's `row_grammar.py` carries a delta, `KIT_MEMORY_TREE_ROW_GRAMMAR_DELTA`, at `row_grammar.py:2-6`: `encoding="utf-8"` on subprocess calls. See §1d.
- The census figure of 518 lines for inCMS `gen_build_index.py` (census lines 149-155) is stale: it is 774 now.

### 1b. CLI flags

**inCMS `gen_build_index.py`**

- Flags: `--check`, `--write`, `--print-bindings`, `--selftest` (`gen_build_index.py:716-730`).
- Usage text is at `:724`.
- An unknown flag exits 2.

**gov `gen_build_index.py`**

- Flags: `--check`, `--write`, `--check-format`, `--print-bindings`, `--survey`, `--report`, `--bump`, `--selftest` (`gen_build_index.py:2752-2784`).
- No argument means `--check`.

**inCMS `corpus_ids.py`**

- `--check <what>`, where `<what>` is one of `ids|orphans|paths|readset|rows|unique|backfill` (`corpus_ids.py:1746-1831`, refusal text at `:1830`).
- `--check readset --dump capped` (`:1798-1805`).
- `--report [paths|--sieve]` (`:1709-1744`).
- `--branch <name>` (`:1695-1706`).
- A bare `--check` exits 2.

**gov `corpus_ids.py`**

- Flags: `--check` (runs checks 13-16 in one call), `--report`, `--measure`, `--print-defined-ids`, `--selftest` (`corpus_ids.py:1223-1256`).
- No argument means `--check`.
- Findings are printed as `HYGIENE <line>`.

**inCMS `gotchas.py`**

- Flags: `--declares`, `--selftest`, `--for-diff <range>`, `--for-paths <p>...`, `--check`, `--write` (`gotchas.py:548-661`).
- `--declares` PRINTS `declares: yes|no` (`:555`).

**gov `gotchas.py`**

- Flags: `--check`, `--write`, `--report`, `--for-diff`, `--for-paths`, `--declares`, `--selftest` (`gotchas.py:610-645`).
- `--declares` sets the exit code only and prints nothing (`:614-615`).

**inCMS `merge-rows.py`**

- Driver argv `%O %A %B` (`merge-rows.py:276`).
- Audit line `merge-rows: written (<n> keyed, 0 hashed)` (`:246`). The hashed term is 0 by construction (`:236-245`).

**gov `merge-rows.py`**

- Same argv (`merge-rows.py:1105`).
- Two-plane model (keyed plus hashed). Audit line printed at `:1078`.

**inCMS `check-docs-hygiene.sh`**

- `--staged` (`.githooks/pre-commit:67`, `.githooks/pre-merge-commit:43`).
- `--print-index-set` (`check-docs-hygiene.sh:206`).
- A full run (`.githooks/pre-push:173`, and the leg `memory-hygiene` at `scripts/gate-legs.json:173-182`).

**gov `check-memory-hygiene.sh`**

- `--staged`, `--print-index-set`, `--print-append-only-ere`, `--print-rotated-archive-ere` (contract table in the spec).

### 1c. Who calls them at inCMS

Enumerated with `git grep` over everything except `memory/builds`, `memory/archive` and `memory/ledger`. The one-shot `scripts/memory-reorg/rekey/step*.py` scripts are listed in the scratch output but are not wired and are ignored here.

**Wired callers of the inCMS copies**

- **`check-docs-hygiene.sh`**
  - Leg `memory-hygiene` (`gate-legs.json:173-182`, argv `bash scripts/check-docs-hygiene.sh`).
  - `.githooks/pre-commit:66-67` (`--staged`).
  - `.githooks/pre-merge-commit:42-43` (`--staged`).
  - `.githooks/pre-push:55,173` (full run).
  - Leg `docs-hygiene-test` runs `scripts/check-docs-hygiene.test.sh` (`gate-legs.json:469-479`, optIn).
- **`gen_build_index.py`**
  - `check-docs-hygiene.sh:1545` (check 23, `--check`, rc only).
  - `check-docs-hygiene.test.sh` (`--selftest`, optIn leg).
  - `.unattended.conf:114` `GENERATED_INDEXES="memory/LIVE.md:scripts/gen_build_index.py memory/ledger:scripts/gen_build_index.py"`.
- **`corpus_ids.py`**
  - `check-docs-hygiene.sh:891` (`--check rows`, check 14).
  - `:930` (`--check unique`, check 15).
  - `:997` (`--check ids`, check 17).
  - `:1007` (`--check paths`, check 18).
  - `:1037` (`--check readset`, check 19).
  - `check-docs-hygiene.test.sh:441` (`--check readset --dump capped`).
  - `check-docs-hygiene.test.sh:470-475`: a smoke over every mode it greps from the `--check takes …` line.
  - **`scripts/recall/selftest.py:522,587,631,835,864,893,1460`** does `import corpus_ids as C`. It is run by `scripts/check_recall.py:409`, which is leg `recall-regression` (`gate-legs.json:302-311`). That leg is NOT optIn and has scope `always`.
- **`gotchas.py`**
  - `check-docs-hygiene.sh:1527` (`--check`, check 24).
  - `check-docs-hygiene.sh:1204-1215` (`--declares`, check 25). This caller greps `^declares: ` as a completion probe.
  - `--for-diff` in `CLAUDE.md`, `scripts/workflows/unattended-build.js:344` and `.claude/skills/unattended/SKILL.md`.
  - `--for-paths` in `.claude/workflows/snidecartographer-specreview.js`.
- **`merge-rows.py`**
  - `.gitattributes:331-332` (`memory/DECISIONS.md merge=rows`, `memory/backlog/*.md merge=rows`).
  - `scripts/check-wiring.sh:480-620` (arm M). Its smoke builds rows from the `FAMILIES` tuple in `scripts/recall/extract.py` (`:547`) and requires `hashed == 0` (`:612-620`).
  - Leg `merge-rows-test` (`gate-legs.json:565-575`, optIn).

**Gov-shipped consumers installed at inCMS but on no leg** (they match the spec's F3)

- `scripts/check-memory-hygiene.sh`.
- `scripts/manifest-check.sh:352-356`. It looks for `corpus_ids.py` only under `tools/memory-tree` or `memory-tree`, so at inCMS it prints the "id citations unchecked" NOTE (`:407`) and never reaches `scripts/`.
- `scripts/marker-contract.test.sh`, `scripts/row_grammar.py`, `scripts/check-arms.py`.

### 1d. What gov's copy must learn: inCMS behaviour that a wired caller depends on

Each item was measured by dropping gov's bytes into clone `icw` or `icv`.

1. **An explicit `encoding="utf-8"` on every text-mode subprocess call.**
   - Leg `encoding-posture` (`gate-legs.json:86-98`) runs `services/api/scripts/check_encoding_posture.py`, whose target globs include `scripts/*.py` (`check_encoding_posture.py:34-39`).
   - Run over gov's copies, it FAILS on 8 calls:
     - `gen_build_index.py:235`
     - `corpus_ids.py:98` and `corpus_ids.py:341`
     - `gotchas.py:67`
     - `row_grammar.py:54`, `:653` and `:776`
     - `check-arms.py:71`
   - inCMS's copies pass (`OK: 4 files`).
   - This is cheap, it belongs to gov, and inCMS has already sent it upstream once (`row_grammar.py:2-6`, "Sent upstream as ABL-aTidalGrommet-7").
2. **`gotchas.py --declares` printing `declares: yes|no`.**
   - inCMS check 25 refuses a run that does not print it (`check-docs-hygiene.sh:1208`).
   - This is already `TOOL-aRepatriatedFork-3`.
3. **Sibling-kit lookup at inCMS's layout.**
   - gov `corpus_ids.py:47` hard-codes `GRAMMAR_DIR = HERE.parent / "memory-recall"`. In `icw` it prints "no id set — the id grammar lives in the memory-recall kit and …\icw\memory-recall/extract.py is not installed".
   - gov `merge-rows.py:168-180` looks only in `tools/memory-recall` and `memory-recall`. inCMS has `scripts/recall/`.
   - This is already `TOOL-aRepatriatedFork-2`.
4. **A recall-kit API the four programs call, which inCMS's recall fork does not have.** This one is new.
   - gov `corpus_ids.py:279-284` requires `extract.grammar_for(root)`.
   - gov `merge-rows.py:201-203` requires `EX.grammar_for` and a two-argument `EX.anchor_at(line, g)`.
   - inCMS `scripts/recall/extract.py` has neither: `anchor_at(line)` takes one argument (`extract.py:219`) and there is no `grammar_for`.
   - So even after item 3 is fixed, gov's `corpus_ids` and `merge-rows` cannot run against inCMS's recall kit.
   - Convergence of the memory-tree four therefore ALSO needs inCMS's `scripts/recall/extract.py` to gain gov's `grammar_for` and `anchor_at` signature, or to converge. That is outside the five and unscoped.

**Behaviour inCMS's copies have that is NOT a gov must-learn**

These are real dependencies, but on schema or on inCMS policy, and they are listed in §5:

- The `[a, b]` list syntax, roster as session slugs, and `ids` as the minted list.
- Grandfathered builds that carry no `status:`.
- The `BEGIN/END GENERATED` wrapper.
- `corpus_ids`'s split `--check <what>` modes and their summary lines. These are only called by `check-docs-hygiene.sh`, which leaves with convergence.
- The ~25 inCMS-only `corpus_ids` internals that `scripts/recall/selftest.py` imports:
  - `check_paths`, `check_waiver`, `check_readset`, `check_backfill`, `sieve`, `glosses`, `definitions`, `duplicate_anchors`
  - `PRESENT`, `ROW`, `SEED_MARKER`, `READ_PATH_TOKEN_ARMS`, `RECORD_HOME`
  - and others, measured by name-probe against gov's `corpus_ids.py`.
  - Those arms test inCMS's own implementation. They retire or migrate with it; gov should not grow them.

**The lexicon leg reds on the swap, and it is not strictly gov's to fix**

- Leg `lexicon` (`gate-legs.json:976-989`) grades against `VERB_OFFENDER_PIN="9816"` (`.lexicon.conf`).
- With gov's copies in `icw` it reports `verb offenders 9831 over pin 9816`: **+15, and the leg is RED**.
- Per file, inCMS → gov: `gen_build_index` 17→30, `corpus_ids` 42→20, `gotchas` 15→16, `merge-rows` 6→29. `row_grammar` and `check-arms` are unchanged at 13 each.
- Remedy: either inCMS raises the pin once, which is an inCMS decision, or gov renames. gov's own lexicon grades these four at 77 offenders, and its VERBS table glosses differ from inCMS's.

### 1e. gov contract clauses inCMS's copies lack

Checked against the spec's contract table, by grep on inCMS files.

- **`gen_build_index.py`**
  - `--check-format`, `--survey`, `--report`, `--bump`: absent.
  - `unfenced_lines`, `STATUS_TOKENS`, `TERMINAL`, `apply_region`, `Problem`, `MARK_OPEN`, `MARK_CLOSE`: all absent. The `apply_region` hit is prose at `:4`. It has `read_unfenced_lines` and `SRC_OPEN`/`SRC_CLOSE` instead (`:84,221`).
  - It HAS `--check`, `--write`, `--selftest` and `--print-bindings`, with gov's A/B/S/N rows ported verbatim (`:188-197,334-362`).
- **`corpus_ids.py`**
  - A bare `--check` exits 2 (`:1830`).
  - `--print-defined-ids`: absent.
  - `parse_conf`: absent. This is why `row_grammar.py` dies on import there, as the spec already says.
- **`gotchas.py`**: meets `--check`, `--for-diff` and `--for-paths`. Its `--declares` goes beyond gov's clause.
- **`merge-rows.py`**: meets the argv and audit-line clause. The hashed term is always 0.
- **`check-docs-hygiene.sh`**: has `--print-index-set`. It lacks `--print-append-only-ere` and `--print-rotated-archive-ere`, which gov's `corpus_ids.py:371,555` calls.

---

## 2. Build README front matter

### 2a. Population and key sets

- **Glob:** `git ls-files 'memory/builds/*/README.md'` filtered to depth 4, i.e. `memory/builds/<slug>/README.md`.
- **Count: 324.** 324 folders, 324 READMEs, and every folder has one.
- **Key sets:**
  - 312 READMEs carry `slug node opened streams roster ids`.
  - 12 carry the same keys plus `authorized-by`, the unattended-kit key.
  - None has a `status:` key. inCMS check 31 bans it (`check-docs-hygiene.sh:1119-1146`).
- **A blind spot in check 31:** its key sed `^[A-Za-z_][A-Za-z0-9_]*:` cannot match `authorized-by`, because of the hyphen. So check 31 never sees that key, and the 12 pass by accident.

**Value syntax at inCMS**

- `streams: [architecture]`, bracketed and comma-separated. 24 carry more than one stream, and 1 is not bracketed.
- `roster: [aBraidedLintel, dLacqueredTransom]`.
- `ids: [BBL-aBraidedLintel-1, …]`.
- The inCMS parser strips the brackets (`gen_build_index.py:147-156`).

**What gov reads** (`gen_build_index.py:174` REQUIRED_KEYS `slug node opened streams roster ids`, plus an optional `status`)

- Keys at column 0.
- `streams` is `+`-joined and graded against `DISCIPLINES` when that is declared (`:783-785`).
- `roster` is `+`-joined, and every value must be a declared FAMILY (`:786-788`).
- `ids` is space-separated.
- `status:` is REQUIRED when no spec under the build carries a parseable header, and FORBIDDEN otherwise (`:635-648`).
- gov's own READMEs follow this: for example `memory/builds/aRepatriatedFork/README.md:2-7` has `streams: tooling+deployer+playbook`, `roster: TOOL+DEPL`, and `ids:` as a space list.

### 2b. roster and ids: the two meanings

**inCMS `roster:`** is the set of SESSION SLUGS whose recording files may live in this folder.

- Its only reader is check 22 (`check-docs-hygiene.sh:1090-1117`): "every recording file's FILENAME slug appears in the `roster:` list". That reader seds `^roster: \[(.*)\]$`.
- Measured distribution:
  - 221 are `[<folder slug>]`.
  - 83 are empty `[]`.
  - 13 hold the folder slug plus other slugs.
  - 7 EXCLUDE the folder slug. These are the non-slug folders `content-promotion`, `gap-closure`, `bOrderlyAtlas-memory-reorg` and `aTracedBlueprint-fd35`, among others.
  - One value is literally `['ARCH ABL']`, in `dMarshalledStorefront`.

**gov `roster:`** is the set of id FAMILIES the build mints under, for example `TOOL+DEPL`. It is validated against FAMILIES and otherwise unused (`:786-788`).

The same key carries two unrelated meanings. No gov check associates a recording file's filename slug with its folder (gov check 5, `HYGIENE.template.md:155-160`, grades the filename grammar only). So check 22's guarantee has no gov home.

**inCMS `ids:`** is the AUTHORED per-family high-water, i.e. what the session minted.

- `CLAUDE.md:136-138`: "Record your per-family high-water in your build's README front matter `ids:` list. That front matter is the ONLY authored input to `scripts/gen_build_index.py`".
- It is read by check 27 (`check-docs-hygiene.sh:1274-1364`): every id there must have a row in DECISIONS, a backlog shard or an archive.
- It is also read by check 28, which shares the parse at `:1311-1321`.
- 79 READMEs have an empty `ids`.
- 12 carry `PKG-*` ids, which are not in the conf FAMILIES.

**gov `ids:`** is an OUTPUT: "`ids` is therefore an OUTPUT, not a source: `--write` overwrites whatever was authored there" (`gen_build_index.py:24-26`).

- It is derived from every tracked file under `memory/` citing `<FAM>-<slug>-<n>` whose slug component matches (`rosters()`, `:664-697`).
- When the derivation is empty, gov falls back to the authored value (`:796`).

**Measured difference.** gov's derivation was replayed over inCMS with inCMS's FAMILIES:

| comparison | READMEs |
|---|---|
| derived set == authored set | 138 |
| derived is a STRICT SUPERSET of authored | 116 |
| derived empty, so gov keeps the authored value | 70 |

The superset rows are ids that are cited but were not in the authored minted list. Example: `aBraidedLintel` gains `BBL-aBraidedLintel-2..5` and `BLOCK-aBraidedLintel-6`, while `PKG-aBraidedLintel-1` is dropped.

So after convergence `ids:` stops meaning "minted", and check 27/28's input disappears.

### 2c. Is the migration mechanical?

**Mostly yes, as syntax.** Trial in clone `icv`, using `scratchpad/migrate_trial.py`:

- Rewrite list syntax.
- Set `roster` to the `+`-joined families of the authored ids.
- Space-join `ids`.
- Add `status:` where needed.

Four programmatic steps and one manual one got gov's `gen_build_index.py --check` from an immediate refusal to `clean (963 artifact(s))`:

1. Create an empty `memory/project/stale-header-waiver.txt`. gov refuses its absence: "The stale-header waiver registry is REQUIRED even when empty".
2. Rewrite the 324 front matters.
3. Delete a stray, empty second `gen:build-index` marker pair in 4 READMEs: `aMendedTurnstile`, `bLimberTransom`, `bNimbleThicket` and `dLimnedTriage`. gov refused with "expected exactly one '<!-- gen:build-index -->' marker pair, found 2 open and 2 close". inCMS's generator partitions on `BEGIN GENERATED` and never noticed.
4. `--write`. It rewrote 963 files: 324 READMEs, `LIVE.md`, 4 ledger shards and 634 spec files, which each gained a `gen:spec-records` region.

Before step 1, gov refused on the first README: `roster value '[aBoundGazetteer]' is outside the FAMILIES set`.

**It needs judgment in four places:**

1. **`status:` on 194 builds.** 194 of 324 builds have no spec with a gov-parseable `**Status:**` header. inCMS's `gen_build_index --check` itself reports "324 builds … 194 grandfathered".
   - The header-parse population is IDENTICAL under both regexes: 634 spec files parse under both, 520 under neither, and 0 differ (`hdr_stats.py`).
   - gov requires `status:` on all 194. That reverses inCMS decision `ARCH-aFerriedToolkit-1`, which is enforced by check 31 and narrated in `memory/builds/aMendedTurnstile/README.md:36-40`.
   - By opening month, 184 of the 194 were opened in June or July 2026, where one owner-ratified default such as CLOSED is plausible. 10 were opened in August or September and each needs a real answer: `aFerriedToolkit`, `aSlackenedPortcullis`, `aSweptDockyard`, `aThriftyTollbooth`, `aTidiedConfluence`, `aWaxedThimble`, `bPacedLantern`, `dMarshalledStorefront`, `dSaltedCatalogue`, `dSurveyedThicket`.
2. **`roster` for builds with no family-bearing id.**
   - 80 READMEs fell back to the stream's first family in the trial.
   - The 7 non-slug folders lose their slug association entirely. For example `content-promotion` becomes `roster: ARCH` and an empty `ids:`, and its `dGildedFerry` and `dPolishedCrucible` sessions are no longer tied to it.
3. **`PKG-*` ids in 12 READMEs.** These are not a declared family. gov drops them from `ids`, and inCMS check 27 already excludes them (`:1293-1296`).
4. **The `<!-- BEGIN GENERATED -->` / `<!-- END GENERATED -->` wrapper and the generator comment line** survive in all 324 READMEs as authored text around gov's region. This is mechanical to delete.
   - `--check-format` was not graded past its first refusal, "memory/project/readme-contract.txt is absent". Whether the wrapper reds the slot contract is therefore NOT measured.

**Three representative examples** (before is the HEAD front matter; after is the trial plus gov `--write` in `icv`)

**`aBoundGazetteer`** is the simple case.

Before:

```
roster: [aBoundGazetteer]
ids: [ABL-aBoundGazetteer-1, ARCH-aBoundGazetteer-1, ARCH-aBoundGazetteer-2, BLOCK-aBoundGazetteer-1]
```

After:

```
roster: ABL+ARCH+BLOCK
ids: ABL-aBoundGazetteer-1 ARCH-aBoundGazetteer-1 ARCH-aBoundGazetteer-2 BLOCK-aBoundGazetteer-1 BLOCK-aBoundGazetteer-2
```

`BLOCK-aBoundGazetteer-2` is derived from `memory/archive/blocks/DECISIONS.2026-07-27.md:252`. The change is mechanical, but `ids` changes meaning.

**`aBraidedLintel`** is the multi-slug case with a PKG id.

Before:

```
roster: [aBraidedLintel, dLacqueredTransom]
ids: [BBL-aBraidedLintel-1, BLOCK-…-1..5, PKG-aBraidedLintel-1]
```

After:

```
roster: BBL+BLOCK
ids: BBL-aBraidedLintel-1..5 BLOCK-aBraidedLintel-1..6
```

The `dLacqueredTransom` association is lost. `PKG-aBraidedLintel-1` is dropped, and 5 cited-but-unminted ids appear. The units table goes from 4 to 6 columns and gains the Records, build-order and build-edges regions.

**`content-promotion`** is a grandfathered non-slug folder.

Before:

```
roster: [dGildedFerry, dPolishedCrucible]
ids: []
```

It has no status header anywhere. After:

```
roster: ARCH
ids:
status: <must be authored>
```

This one needs judgment: the status, and whether the two session slugs are still recorded anywhere.

---

## 3. inCMS `.memory-tree.conf`, as gov's programs would read it

The file says of itself that it is read by only one tool (`.memory-tree.conf:1-6`). It declares three keys:

- **`MEMORY_ROOT=memory`** (`:17`). This agrees with gov.
- **`ARMS_FLOORS="scripts/check-docs-hygiene.sh:46:16 scripts/manifest-check.sh:16:16 scripts/unattended/unattended.sh:168:165"`** (`:22`).
  - gov's `check-arms.py` reads the same format.
  - After the hygiene swap, the `check-docs-hygiene.sh` floor names a gate that no longer exists. By inCMS's own rule (`:12-13`) that is a FAILURE. The VALUE has to be re-measured for `check-memory-hygiene.sh`.
- **`FAMILIES="architecture:ARCH deployment:DEPLOY blocks:BLOCK design:DES performance:PERF architecture:ABL deployment:DPL blocks:BBL design:DBL performance:PBL"`** (`:30`).
  - gov accepts two families per discipline.
  - **It omits `PKG`**, while inCMS's `scripts/recall/extract.py:37` FAMILIES tuple includes it. `memory/DECISIONS.md` holds 8 PKG-anchored lines.
  - The conf's own header claims the two are "that same closed set" (`:25-28`), and they are not.
  - Under gov, `grammar_for` reads the conf. So a PKG row is unkeyed, and it would HASH in gov's `merge-rows`. Meanwhile check-wiring arm M builds its smoke from `extract.py`'s tuple, which includes PKG (`check-wiring.sh:547`), and requires `hashed == 0` (`:612-620`). The predicted result is UNWIRED. This is inferred from the code and was not run.
  - gov's two readers also disagree on a bare `PKG` token:
    - `recall_conf.py:254-259` takes `rpartition(":")`, so a bare `PKG` counts.
    - `gen_build_index.py:782` needs a `:`, so a bare `PKG` is ignored.
  - So PKG can only be declared as `<discipline>:PKG`. inCMS says PKG belongs to the separate nc repo (`check-docs-hygiene.sh:1293-1296`), so it has no discipline to name. That is a gap in how gov's conf can express this, and inCMS has to make a decision about it.

**Keys gov reads that inCMS does not declare, and the value inCMS holds elsewhere today**

- **`CHARTER`.** gov defaults to `AGENTS.md` (`corpus_ids.py:57`). inCMS hard-codes `CLAUDE.md` (`scripts/corpus_ids.py:91`). Declaring it is a value, not a new key.
- **`DISCIPLINES`.** When it is absent, gov skips the streams check silently (`gen_build_index.py:783-785`).
- **`SPEC_FORMAT_CUTOFF`.** inCMS hard-codes `2026-07-15` in check 12 (`check-docs-hygiene.sh:607`). gov with it blank prints "check 25 … is DISARMED".
- **`ORPHAN_ID_PIN` and `DEAD_PATH_PIN`.** inCMS keeps its pins inside its registries: `paths: 66 rows (PIN 66)` and `corpus-id-unresolved.txt` with 29 rows. With both blank, gov checks 13-15 are disabled (the `measured-pins` hole).
- **`RECORD_UNBOUND_PIN`.** Undeclared; gov reds it by name ("RECORD_UNBOUND_PIN is undeclared"). Its population is the 1515 inCMS records that carry no Serves line.
- **`ROW_DUPLICATE_PIN`, `UNIVERSAL_BUDGET`, `ROTATION_MODE`, and the `INDEX_CAP_*` / `ENTRY_CAP_*` / `BUILD_README_*` caps.** inCMS keeps the literals `CAP7=153600` and `CAP_RAW=20480` at `check-docs-hygiene.sh:440-441`.

**Values gov would reject or read differently**

- **`READ_PATH_CEILING`.** inCMS keeps it as a code constant, `148580` (`corpus_ids.py:228`), and check 19 is a summed read budget (`ARCH-aGrittedFlagstone-2`). gov RETIRED the sum in 2.42 and only announces a declared `READ_PATH_CEILING` (`HYGIENE.template.md:256-262`). Converging drops an inCMS gate by gov's design.
- **Registry location and row grammar.** This is layout plus format, not a conf key:
  - inCMS keeps `scripts/legacy-files.txt`, `scripts/curation-debt.txt`, `scripts/corpus-path-unresolved.txt` and `scripts/corpus-id-unresolved.txt`. gov reads `memory/project/*` (`check-memory-hygiene.sh:284-285`).
  - inCMS's dead-path row is `<cited> <absent|removed|repointed> <citing> [dest]`, space-separated, 66 rows. gov's is TAB-separated `<citing> <cited> <occurrences> <absent|moved:DEST>` (header of gov `memory/project/corpus-path-unresolved.txt`). inCMS's `removed` has no gov equivalent.
  - inCMS's orphan waiver carries reasons `grammar|glossed|no-source|backfilled` (`corpus_ids.py:1012-1013`) plus a sieve. gov's `id-orphan-waiver.txt` is a count-pinned list.

---

## 4. `check-docs-hygiene.sh` vs gov's `check-memory-hygiene.sh`

inCMS's checks, from the section headers in `check-docs-hygiene.sh`, are 1-8, 10-19 and 21-32. Its check 9 is retired (`:548`).

**Checks inCMS has that gov LACKS**, where the gov numbers are from `HYGIENE.template.md:140-340`:

| inCMS check | what | nearest gov |
|---|---|---|
| 13 | spec-section canon freshness via `gen-spec-canon.sh` (`:864-875`) | none |
| 16 | the recall fixture resolves into the corpus (`:956-972`) | none in memory-tree |
| 19 | the SUMMED read-path ceiling (`:1017-1045`) | gov 16 without the sum (retired in 2.42) |
| 21 | emission: a memory/ path a commit ADDS must be adopted (`:1551-1602`) | none. gov 21 is a different check: records name their spec |
| 22 | roster coverage: filename slug ∈ `roster:` (`:1090-1117`) | none |
| 25 | a NEW gotcha declares its gate, staged and added only (`:1173-1216`) | gov 18 is corpus-wide, with no grandfather |
| 26 | help/ and infra/ may not point at a retired discipline dir (`:1218-1272`) | none |
| 27 | a minted id in `ids:` owns a recorded row (`:1274-1364`) | none |
| 28 | a build whose ids reached the shipped tree may not read SPECCED (`:1366-1440`) | none |
| 29 | a new memory/ .md carries no NUL byte (`:1442-1520`) | none |
| 30 | the CLAUDE.md micro-format definitions parse under one grammar (`:1047-1085`) | none in memory-tree |
| 31 | front-matter keys nothing reads (`:1119-1146`) | none, and it contradicts gov's required `status:` |
| 32 | no literal-credential fallback in memory scripts (`:1149-1171`) | none |

**Gov checks that red inCMS's current tree**

- **Engine used:** gov's engine with gov's four programs, in clone `icw` (`bash scripts/check-memory-hygiene.sh`, 19 s wall, rc 1).
- **Baseline for comparison:** inCMS's own engine on pristine clone `icx` (`check-docs-hygiene.sh`, about 2.5 min). Its only red is check 18, a single row: a dead citation to `.claude/worktrees/readopt-coding-governance-103a26`, which exists only in the real tree's worktrees. That is a CLONE ARTIFACT, not a tree defect. The baseline run finished at rc 1, and check 18 was its only FAILED line.

| gov check | red lines | what |
|---|---|---|
| 2 link integrity | 10 | 9 broken relative links plus a `….md…` placeholder in `memory/HYGIENE.md`. inCMS's check 2 exemptions differ |
| 3 structure | 3 | `memory/backend-test-harness.md`, `memory/browser-preview.md` and `memory/review-workflow-protocol.md` are at the memory root. They are in inCMS's `IDX_ROOT` at `:126` and not in gov's sanctioned set |
| 4 build-folder shape | 18 | `STATUS.md` in 18 build folders. inCMS admits `STATUS.md` (`:149`) and gov does not |
| 5 recording-file naming | 676, then 155 | 676 with the registries where they are. **155** after copying `scripts/legacy-files.txt` into `memory/project/`, which shows the registry location accounts for 521 of them |
| 6 index caps | 6 | unchanged by relocating `curation-debt.txt` |
| 7 entry budget | 19 | unchanged by relocating `curation-debt.txt` |
| 9 build index | 1 | gov `gen_build_index` refuses the first README's roster. See §2 |
| 21 records name their spec | 1515 + 7 + 53, plus an undeclared pin | 1515 records under build/, prompts/ or reviews/ with no Serves line. 7 Serves lines name undefined ids. 53 filename-vs-Serves mismatches. And `RECORD_UNBOUND_PIN` is undeclared |
| 13-16 (corpus_ids) | not reached | gov `corpus_ids` refuses because `--print-index-set` "answered with findings rather than a set" (check 2 is red), and the recall kit is not found anyway (§1d.3) |
| 17 gotchas index | yes | `INDEX.md` stale. inCMS renders it with `BEGIN/END GENERATED` markers |
| 17-19 front matter | first record refuses | `…re-fires-on-every-scan.md:5: front-matter key is indented`. **223 of 254** `memory/gotchas/*.md` carry a nested `metadata:` block (`node_type: memory`, `type: project`); 27 more are under archive/. inCMS's reader ignores it (`gotchas.py:15-19`), and gov refuses indented keys |
| 17-19, after stripping `metadata` and moving `recurring-bug-classes.md` out | 70 | 1 is check 17 (stale). **68 are check 18** (the record names no gate). 1 is check 19 (`stale-docker-container-owns-port.md`, no anchor). `recurring-bug-classes.md` is not a record: inCMS skips it by name (`gotchas.py:209`), and gov refuses "no front matter" |
| 20 row grammar | 3 | dash-led lines carrying an id the grammar cannot key. Lines include `memory/backlog/DPL.md:12,17` |
| 25 | disarmed | `SPEC_FORMAT_CUTOFF` is blank |

**Converging the generator alone, keeping inCMS's hygiene engine**

Measured in `icv`, which has the migrated front matter and gov's `--write`, with inCMS's own engine run over it. Four reds:

- **Check 22:** 1851 lines. The roster is no longer slugs.
- **Check 31:** 194 lines, the `status:` keys.
- **Check 23:** 329 views. inCMS's generator disagrees with gov's render.
- **Check 18:** the clone artifact.

So the generator cannot converge without the engine converging too, or without checks 22, 23 and 31 being rewritten.

---

## 5. What makes convergence impossible, or forces a gov-side conf key

The build's rule is that a new conf key is justified only for an adopter's DECISION, never for its layout.

**Layout, so no key is justified; inCMS moves or rewrites.** All of it is mechanical or scriptable:

- The registries under `scripts/` go to `memory/project/`. The dead-path rows are rewritten to gov's TAB grammar.
- The 3 root memory files and the 18 `STATUS.md` files are moved or folded.
- `recurring-bug-classes.md` leaves `gotchas/`.
- The front-matter syntax changes, the `BEGIN GENERATED` wrapper is deleted, and the 4 stray marker pairs are deleted.
- The nested `metadata:` block is stripped from 223 or more records.
- The sibling-kit path is gov's side (`TOOL-aRepatriatedFork-2`).

**Decisions: inCMS policy that gov's programs cannot express.** Each needs either the owner to reverse inCMS's decision, or a gov-side conf key:

1. **Grandfathered builds carry no status.** `ARCH-aFerriedToolkit-1`, enforced by check 31, against gov's required `status:` (`gen_build_index.py:635-641`). gov's docstring deliberately refuses a default: "every plausible default for them was wrong, so the fallback is explicit and gated instead" (`:31-35`). Converging means inCMS authors 194 values, 10 of which need real judgment, or gov adds a policy key.
2. **The gotcha-declaration scope is added-only.** inCMS check 25, `ARCH-dQuarriedLedger-1` U10 S7, stated with its measurement "46 of 121 … a corpus-wide arm would red the merge bar on debt the committer did not write" (`:1173-1180`). gov check 18 is corpus-wide with no cutoff or pin: 68 records red. That means either 68 per-record declarations, or a gov `*_CUTOFF` or pin key of the same shape as its other cutoffs.
3. **`roster:` and `ids:` mean different things under the same name** (§2b). inCMS checks 22, 27 and 28 guard properties gov has no check for:
   - check 22: a recording's session is rostered in its folder;
   - check 27: a minted id has a recorded row;
   - check 28: shipped ids are not SPECCED.
   After migration their input is gone. Either inCMS accepts the loss of coverage, or gov gains those checks. That would be new checks, not conf keys, and the owner has to decide.
4. **The summed read-path ceiling.** This is inCMS check 19, and gov retired it deliberately. inCMS has to accept losing it. No key is justified, because gov already refused it.
5. **`PKG`, a family with no discipline.** The conf grammar cannot state it, and gov's two readers disagree on a bare token (§3). This needs an owner decision.

**Hard dependencies outside the five programs.** These are not decisions, but convergence is impossible without them:

- **The recall-kit API.** gov's `corpus_ids` and `merge-rows` need `extract.grammar_for(root)` and a two-argument `anchor_at`. inCMS's forked `scripts/recall/extract.py` has neither (§1d.4).
- **Leg `recall-regression`.** It imports about 25 inCMS-only `corpus_ids` internals through `scripts/recall/selftest.py`. Those arms must retire or migrate in the same change.
- **Leg `lexicon`.** It goes +15 over its pin. That needs an inCMS pin decision or gov renames.
- **Leg `encoding-posture`.** gov must add `encoding="utf-8"` at 8 call sites. This one is cheap and it is gov's to do.

**Nothing found makes convergence strictly impossible.** The blockers are owner decisions (1-5) and one unscoped dependency (the recall kit).

---

## Not measured

- gov `gen_build_index.py --check-format` over inCMS past its first refusal (`readme-contract.txt` absent). Whether the `BEGIN GENERATED` wrapper or inCMS's authored README headings violate the slot contract or heading canon is unknown.
- gov checks 13-16 (`corpus_ids`) against inCMS's corpus. They are blocked by check 2's findings and by the recall-kit path, and I did not stub past either. Orphan-id and dead-path counts under gov's rules are therefore unknown.
- Whether gov's `merge-rows` keys inCMS's DECISIONS and backlog rows. It cannot import inCMS's `extract.py`. The check-wiring arm-M UNWIRED prediction for PKG is inferred, not run.
- Whether the unattended driver's `GENERATED_INDEXES` or dispatch declaration tolerates gov's `--write` also touching 634 spec files and 324 READMEs. Not run.
- The optIn legs `docs-hygiene-test` and `merge-rows-test`, and the `recall-regression` leg, with gov's copies. The recall break is inferred from 25 missing symbols by name-probe; the leg was not executed.
- gov `gotchas.py --for-diff` output parity against inCMS consumers.
- `check-arms.py` and `row_grammar.py` beyond the encoding and lexicon probes. They are outside the five.
- Row counts of inCMS files under gov check 6/7 caps after declaring inCMS's actual cap values. The caps were left undeclared.
- Whether check 2's 9 broken links are also red under inCMS's own check 2. They were not red in the baseline, so inCMS's exemptions cover them.
