# The lexicon kit — the recommended rebuild

**Serves:** research TOOL-aSurfacedLexicon-1

Synthesis of five measurement lenses, three designs and three adversarial judgements, run 2026-09-04
on `C:/projects/coding-governance/.claude/worktrees/lexicon-tool-rebuild-b95399` at HEAD `d0a18683`.
**Every number in §1 was re-measured by this pass on this worktree**, not inherited from the inputs —
where a lens and my run disagree, my number is the one printed and the disagreement is noted. Nothing
here is estimated except where the row says ESTIMATE. Paths are repo-root-relative, forward-slashed.

---

## 1. MEASURED EVIDENCE

### 1.1 The corpus and what the shipped kit does to it

| Fact | Value | Command / file:line |
|---|---|---|
| Tracked files | 1394 | `git ls-files \| wc -l` |
| Extension census | md 1172 · sh 89 · py 47 · toml 30 · txt 24 · js 11 · json 9 · conf 4 · example 3 · `<none>` 2 · gitattributes 1 · gitignore 1 · tsv 1 | scratchpad `m2.py` over `git ls-files` |
| P1 verb | graded 1047, offenders 461, waived 0 | `python tools/lexicon/lexicon.py --check` |
| P2 suffix | graded 39, offenders 0, waived 0 | same |
| P3 layer | graded 548, offenders 0, waived 0 | same |
| Coverage | armed 58 of 138 definition-carrying files (42.0%) | same |
| The three pins | `VERB_OFFENDER_PIN="461"` · `SUFFIX_OFFENDER_PIN="0"` · `LAYER_OFFENDER_PIN="0"` | `python tools/lexicon/lexicon.py --measure` |
| Function definitions by language | py 925, js 122 (= 1047) | scratchpad `m1.py` via `lexicon.extract` |
| Type definitions by language | py 39, js **0** | same |

### 1.2 The 461 offenders split in two, and the split is 1:10

| Fact | Value | Evidence |
|---|---|---|
| DEBT — leading token is a non-representative spelling of a canon cluster | **43** (all py) | `m1.py`: `v in canon.build_form_index()` |
| UNRULED — leading token in no cluster and no row | **418** (py 373, js 45) | same; 43 + 418 = 461 ✓ |
| Distinct unruled tokens | **258** | same (a lens reported 281; mine is 258 on the 1394-file index) |
| Unruled tokens appearing exactly once | 184 of 258 (71%) | same |
| Top unruled tokens | `a` 18 · `git` 13 · `demand` 10 · `signal` 8 · `bounded` 7 · `kit` 7 · `all` 5 · `carry` 5 · `repo` 4 · `no` 4 · `tree` 4 · `govkit` 4 | same |
| Debt tokens | `is` 7 · `walk` 4 · `make` 3 · `drop`/`require`/`has`/`append`/`find`/`emit`/`dump`/`log`/`apply` 2 each · 11 more at 1 | same |
| **Debt tokens `--suggest` can actually name a replacement for today** | **5 of 23** (`append`, `log`, `compute`, `validate`, `search`) — covering **7 of the 43 definitions** | `python tools/lexicon/lexicon.py --suggest <tok>_thing`, all 23 run |
| Confirmed silent: `--suggest ensure_cache` | ``` `ensure` is not in the declared table``` | direct run |
| Confirmed silent: `--suggest require_adopted_root`, `walk_file_keys` | same shape | direct run |

**This is the single most important measurement in the report.** `run_suggest` reads only the conf's
`VERBS` and the inverted NOT clauses (`tools/lexicon/lexicon.py:796`, `:812`, `build_negatives`), never
`canon.py`. So "DEBT is the class where the kit can name the fix" is **false as shipped for 36 of 43**.
The rebuild must wire `--suggest` to `canon.build_form_index()`; without that graft the debt/unruled
split is a relabelling, not a capability.

### 1.3 The convention predicate — measured cost of the shipped idiomatic defaults

| Cell | Convention | Population | Violations | Evidence |
|---|---|---|---|---|
| py.function | snake | 925 | **0** | `m1.py` |
| py.type | pascal | 39 | **0** | same |
| js.function | camel | 122 | **0** | same |
| js.type | pascal | **0** | — (would red as DEAD CELL) | same |
| py.file | snake | 47 | **7** | `m2.py`, first-dot stem |
| sh.file | kebab | 89 | **4** | same |
| js/json/toml/txt/tsv/`<none>`.file | kebab | 11/9/30/24/1/2 | 0 each | same |
| **All armed file cells** | — | **213** | **11** | same |
| md.file under kebab | — | 1172 | 173 violations **+ 921 that satisfy NO convention at all** | same |

The 7 `py.file` violations: `tools/check-spec-tokens.py`, `tools/gate-lint/ps-hygiene.py`,
`tools/memory-recall/check-recall.py`, `tools/memory-tree/check-arms.py`,
`tools/memory-tree/merge-rows.py`, `tools/pytest-parallel-guardrails/aiosqlite-seam-conftest.py`,
`tools/settings-merge.py`. Each is a module no `import` statement can resolve — a defect class, not a
style preference, and the gate's failing case observed in the tree rather than staged (§7).

The 4 `sh.file` violations: three dated build-repro scripts under `memory/builds/` (frozen records)
plus `tools/run-gates/profile_bar.test.sh`.

| Supporting fact | Value | Evidence |
|---|---|---|
| Names satisfying 2+ conventions (func + type, 1086 names) | 255 (1 two-way, 254 three-way) | `m1.py` — proves the classifier must return a SET, not a value |
| Cross-cell teeth, py.function | camel would red 691 · pascal 925 · screaming 925 · kebab 691 | `m1.py` |
| Cross-cell teeth, js.function | snake would red 102 · pascal 122 | same |
| Cross-cell teeth, py.type | camel/kebab/snake would red 39 · screaming 38 | same |
| First-dot vs last-dot file stem | **64 graded files** disagree | `m2.py` |

### 1.4 The `py.constant` dispute, resolved

Three lenses reported 392, 413 and 419 for the same cell. All three are answers to different
questions. Measured over the 47 tracked `.py` files, **module body only** (not `ast.walk`):

| Population definition | n | screaming | not |
|---|---|---|---|
| All module-body `Name` targets, incl. tuple unpack | 539 | 419 | **120** |
| Simple single-`Name` targets only | 432 | 413 | **19** |
| Public simple targets (no leading `_`) | 331 | 331 | **0** |

Zero is reachable **only** by selecting the population with the property being enforced — the leading
underscore is what correlates with mutable module state (`sys` at `tools/drift-audit/drift_report.py`,
the tuple-unpack `code, out` at `tools/lexicon/selftest.py`). A `py.constant screaming` cell shipping
`0` would be the could-not-fail class of §7, one level up. **It ships DARK.**

### 1.5 P3, and why it goes

| Fact | Value | Evidence |
|---|---|---|
| Declared LAYERS rules | **one**: `tools/lexicon/* -> tools/codebase-map/*` | `.lexicon.conf:215-216` |
| Files matching that FROM glob | 14 | `git ls-files 'tools/lexicon/*' \| wc -l` |
| Imports actually inside it (judgeable) | **44** | own script via `lexicon.extract` |
| Imports the green line claims to grade | 548 | `--check` |
| Commits touching `.lexicon.conf` | 17 | `git log --oneline -- .lexicon.conf \| wc -l` |
| `LAYER_OFFENDER_PIN` values ever written | one: `"0"` | `git log -p --follow -- .lexicon.conf \| grep '^+LAYER'` |
| `SUFFIX_OFFENDER_PIN` values ever written | one: `"0"` | same |
| `VERB_OFFENDER_PIN` values ever written | 384, 412, 415, 417, 450, 452, 455, 458, 460, 461, 463×2 | same |
| P3 engine functions | `_glob_match` 16 · `build_module_index` 17 · `_resolve_relative` 22 · `resolve_import` 48 · `scan_unselective_rules` 26 (+ `_build_glob_rx`, `_check_path_suffix`, `check_layer_violation`) | AST spans over `tools/lexicon/lexicon.py` |

The `graded=548` line overstates the judgeable population by **12x** on every run.

### 1.6 Size, cost and structure

| Fact | Value | Evidence |
|---|---|---|
| Kit line counts | `lexicon.py` 1201 · `selftest.py` 1076 · `adopt-lexicon.sh` 263 · `scaffold_lexicon.py` 231 · `lexicon_conf.py` 185 · `canon.py` 118 · `subtokens.py` 38 | `wc -l tools/lexicon/*` |
| `.lexicon.conf` | 216 lines, **178 of them comments (82%)** | `wc -l`, `grep -cE '^#'` |
| Biggest functions | `run` **278** · `run_brief` 134 · `run_probe` 84 · `run_suggest` 68 | AST spans |
| Selftest arms | 140 `check(` + 48 `run_case(` | `grep -c` |
| Gate legs total | 89 | `tools/gate-legs.json` |
| `lexicon naming predicates` | chunk `declarations`, subject `repo`, guard `["tools/","skills/session-kickoff/",".githooks/",".claude/"]`, ceiling 300 | same |
| `lexicon selftest` | chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, ceiling 880 | same |
| `lexicon wiring` | chunk `wiring`, subject `repo`, **guard `[]`** (runs on every bar), ceiling 330 | same |
| `codebase-map kit selftest` | chunk `selftests`, guard **includes `tools/lexicon/`** | same |
| `drift-audit selftest` | chunk `selftests`, guard `["tools/drift-audit/","tools/lib/"]` — does **not** include the lexicon | same |
| Charter headroom | 48867 / 49152 bytes, **285 free**, already WARNing past its high-water 48378 | `bash tools/check-template-size.sh` |

`AGENTS.md` states `GATE_FULL` does not set `GATE_SELFTESTS` and no boundary sets it. **Anything on a
`chunk = selftests` leg is invisible to the push bar.**

### 1.7 The neighbours

| Fact | Value | Evidence |
|---|---|---|
| `lexicon-verbs` inventory keys | 23 | `memory/map/generated/inventories.json` |
| Populated through the lexicon's own reader | yes | `tools/codebase-map/map_extractors.py:135`, `:139-168` |
| Feature dossiers | 19 (+ `FOUNDATION.md` = **20 claim tables**) | `ls memory/map/features/ \| wc -l` |
| A dossier must carry EXACTLY the inventory id set | **missing keys raise**, not just unknown | `tools/codebase-map/map_lib.py:938-943` |
| codebase-map asserts `lexicon.DEAD_TOKENS == map_lib._STOPWORDS` | yes | `tools/codebase-map/selftest.py:1268-1276` |
| drift-audit fixtures carrying `LAYERS:` blocks | **3** (`selftest.py:734`, `:814`, `:890`) plus 3 `LAYER_OFFENDER_PIN` references | `grep -n LAYERS tools/drift-audit/selftest.py` |
| `lexicon_marginal_offense_rate` overall | 132 of 537 = **24.6%** | `python tools/drift-audit/drift_report.py --json` |
| — fresh-file arm (the kill rule's) | 5 of 138 = **3.6%**, `live: true` | same |
| — pre-declaration files | 127 of 399 = 31.8% | same |
| `lexicon` in `memory/TEMPLATE-SPEC.md` | **0** | `grep -c -i lexicon` |
| `lexicon` in `memory/HYGIENE.md` | **0** | same |
| `govkit update` classifies by iterating the RECEIPT | `for row in rows_all:` | `tools/govkit/govkit.py:5718` |
| `canon.py` role | falls under `include = "**"` / `role = "engine"` — overwritten on upgrade | `tools/lexicon/kit.toml:17-19` |
| Waiver registries role | `seed` — "copied ONCE, then the target owns it" | `tools/lexicon/kit.toml:25-28` |
| Skill placeholders | `VERBS_TABLE, SUGGEST_CLI, BRIEF_CLI, GATE_CLI, CONF, KIT_VERSION` | `tools/lexicon/kit.toml` |
| Hardcoded language axis | `KNOWN_EXTS = {"py":…, "js":…}` and `PATTERN_SETS` (one set, `js-regex`) — both in an `engine`-role file | `tools/lexicon/lexicon.py:102`, `:107-121` |

### 1.8 The anti-mirror closure, verified

`tools/lexicon/scaffold_lexicon.py:143` — `live = {forms[v] for v in counts if v in forms}`. A token in
no cluster **cannot enter a proposal at all**. That line is the structural closure the canon fix
bought, and it is why any `--expand` design that proposes "off-table tokens the canon does not map
elsewhere" is a regression: my measured unruled top-15 contains `git`, `signal`, `bounded`, `kit`,
`all`, `repo`, `no` — **seven of the ten non-verbs the original defect produced** (`canon.py:41-47`).

| Fact | Value | Evidence |
|---|---|---|
| Bare-row refusal (a `VERBS` row with no negative reds) | live | `tools/lexicon/lexicon.py:503-511` |
| Shell function definitions, naive probe | **581** — a FLOOR, from exactly the regex `sh::dark` exists to refuse | own probe over 89 `.sh` files |
| "SHRINK-ONLY" in kit Python source | **zero occurrences**; the only comparison is `> pin` | `grep -n 'shrink\|SHRINK' tools/lexicon/*.py` → none; `lexicon.py:697` |

### 1.9 What I could NOT determine

- **The `lexicon selftest` wall-clock.** I did not run it. The 87 s ledger row cited upstream lives in
  the main tree's git dir at a sha I did not verify against this worktree. Do not quote it.
- **Any adopter's numbers.** `C:/projects/incms/main` was outside this pass's read-only scope. Every
  percentage above is this corpus: 47 py + 11 js files, agent-written under a charter that already
  mandates naming discipline. **0 convention violations across 1086 identifiers is a fact about that**,
  not about software.
- **The cost of the new code.** Nothing comparable ships — no case-style code exists in the kit at all.
  A line count would be the estimate the method rules forbid. The DELETIONS in §2 are measured; the
  additions are not.
- **Whether `.claude/hooks/agent-cap.js` and `tools/hooks/agent-cap.js` being byte-identical tracked
  copies inflates the js counts.** They are duplicates; I did not audit other kits for the same shape,
  so the js unruled figure of 45 may double-count.
- **Review finding D25**, unfiled anywhere: `subtokens.py` is ASCII-only, so an accented identifier
  grades on a truncated leading token and a fully non-ASCII name is skipped with no report. It sits in
  the population-selection path this rebuild keeps. It needs a backlog row before the build starts.

---

## 2. VERDICT ON THE CURRENT KIT, COMPONENT BY COMPONENT

### KEEP UNCHANGED

| Component | Why |
|---|---|
| `subtokens.py` (38 lines) | The splitter every predicate needs. Note it LOWERCASES, so the convention check is its **sibling**, not its consumer — it reads the raw name. |
| `lexicon_conf.py` grammar | `KEY="value"` scalars plus `KEY:` + indented rows. `_SCALAR_RE` accepts any identifier key, so the new stamps need **no reader work at all**. |
| `canon.py` CLUSTERS + the two-deciders rule | 34 code lines carrying the whole load-bearing prior constraint. Stays `role = "engine"` and stays upgradeable — see §5. |
| `load_waivers` + the STALE-waiver refusal | Text-keyed, never `<path>:<line>`. Position keying unpins on any edit above the waived line and was hit for real. |
| `extract` / `extract_text` / `_python_defs` | The one extractor drift-audit consumes against git blobs at two shas. **Signature frozen by contract.** |
| `resolve_self_path` | govkit's apply writes bytes verbatim; a spelled install prefix arrives wrong without it. |
| **The coverage sniffer** | *Reversing a proposal in the input designs.* `lexicon.py:126-131` argues the case itself: "they only run on declared-armed extensions, so a denominator built from them is the numerator." A declaration-derived coverage ratio is one step further from the corpus and is a number the owner moves by typing rows. The honest, uncomfortable `armed 58 of 138 (42.0%)` stays. |
| P2 suffix predicate | 12 lines, prescriptive, safe to inherit, no exemption for a bare `Manager`. |
| `adopt-lexicon.sh`'s render + byte-compare Skill machinery | Runs on the ONE unguarded leg, so any declaration change trips it until re-rendered. The transition's tripwire is already installed. |

### MODIFY

| Component | Change |
|---|---|
| P1 verb | Split the offender count into DEBT and UNRULED, **both pinned** (see §8 Q1), and make DEBT actually name its replacement by wiring the offender line and `--suggest` to `canon.build_form_index()` / `canon.read_gloss()`. Measured: 36 of 43 name nothing today. |
| `run()` (278 lines) | Split the measurement pass from the verdict pass. Not style — the `--measure`/`--check` duality generated three separately-documented armed-but-unreachable defects, each fixed by hoisting code above a `return`, all three confessions still in comments at `lexicon.py:625-670`. |
| `run_suggest` (68 lines) | Takes `--as <cell>`, consults `BANNED_SUFFIXES`, and re-cases to the **declared** convention instead of the caller's. Today `--suggest fetchUserData` returns `loadUserData` — the right verb in a case the new gate reds on the next line. |
| `lexicon_conf.BLOCK_KEYS` | Hardcoded tuple at `:32`; the `VERBS` row-key must be alphabetic at `:104`, so `py.function` is refused. Widen it and make the default block parse generic (`key <rest>`), so the next block key costs nothing. This closes a live G5 violation rather than adding one. |
| `scaffold_lexicon.py` | Gains `--expand` (§5). Its candidate selection at `:143` is **kept verbatim** — that line is the anti-mirror closure. |
| `KNOWN_EXTS` / `PATTERN_SETS` | Become declaration-extensible via a `PATTERNS:` block. This is the one G5 hole that decides whether the kit grades anything at all on a non-py/js adopter (§8 Q4). |
| `graded[(ext, surface)]` keying (`lexicon.py:568-570`) | Already R1's coordinate. The three surface literals become a declared enum: `function`, `type`, `file`. |

### DELETE

| Component | Lines | Why, and what replaces it |
|---|---|---|
| **P3 layer**, whole predicate | ~164 engine + ~223 selftest (21% of that file) + the `LAYERS` block, `LAYER_OFFENDER_PIN`, `lexicon-layer-waivers.txt`, the `lexicon-layers` hole | Architecture wearing a naming kit's badge. In none of G1–G5, in neither ruling. One rule, 44 of 548 imports judgeable, one pin value ever written (`"0"`) across 17 commits, four adversarial review rounds and four blockers. **Compensating check:** a source scan asserting no `tools/lexicon/*.py` imports `codebase-map`, on the `lexicon naming predicates` leg (chunk `declarations`, subject `repo`) — **not** the selftest, which the push bar never runs. |
| `--brief` + `run_brief` + `read_object_state` + `read_object` + `read_token_is_live` + `DEAD_TOKENS` + `MIN_LIVE_TOKEN` | ~163 | "How does this corpus already spell things" is the corpus-as-authority direction the canon closes. Under G1 the prewritten set is the authority and `--suggest` is the delivery. Owed same-commit: delete `tools/codebase-map/selftest.py:1268-1276`. |
| `--probe` / `run_probe` | 84 | Derivable from `--measure` + canon. Its useful half (the debt/unruled split) becomes the permanent shape of the ordinary report. |
| Three of the four duplicated corpus walks | — | `run()`, `run_brief()`, `run_probe()` and `scaffold_lexicon.main()` each re-derive `declared`, re-filter dark, re-call `extract` and swallow errors differently. One `scan_corpus(root, declared)` generator. Pure win. |
| 178 of `.lexicon.conf`'s 216 lines | 178 | Pin archaeology: eleven recorded moves with hand-written name lists. It exists because a one-sided pin carries no machine-readable previous value; a `PINS:` block that `--measure` emits whole is the successor. Git keeps every byte. |

**NOT deleted, against two input designs:** the coverage sniffer (see KEEP) and the UNRULED pin
(see §8 Q1). Both deletions were argued as cleanups and both are enforcement reductions.

---

## 3. THE RECOMMENDED DESIGN

Three predicates over one corpus walk, keyed on a declared (language, surface) cell.

- **P1 vocabulary** — the leading token of a definition must be a `VERBS` row. An offender whose token
  is a canon-cluster alternative is **DEBT** and the report names the replacement; one in no cluster is
  **UNRULED** and is reported with its count. Both pinned, separately, per cell.
- **P2 suffix** — a type name may not end in a `BANNED_SUFFIXES` token. Unchanged.
- **P3 convention** *(new)* — `declared_style ∈ styles(name)`, where `styles()` returns a **set**.
  Six regexes over a core with leading and trailing underscores stripped. Three verdicts, not two:
  SATISFIED, VIOLATION, and AMBIGUOUS (the empty set — the name chose no convention, which is a
  different fact from choosing the wrong one). File stems split at the **first** dot.

Plus four declaration refusals, each one comparison: an extension present in the tree with no `LANGS`
row (shipped); a **cell** with a non-empty population and no `CELLS` row; an **armed cell** with a zero
population (DEAD CELL — the shipped vacuity arm is per-LANGUAGE and cannot see that `js.type` is 0
while `js.function` keeps `.js` green); and a `CANON:` block with no stamp.

**Zero new top-level modules.** `govkit update` iterates the receipt (`govkit.py:5718`), so a file gov
newly ships is outside the classification space — the shape that killed every entry point of the inCMS
adopter for six days when `canon.py` landed with a module-level import at `lexicon.py:84`. Conventions
go in `subtokens.py`; cells and pins in `lexicon_conf.py`; the ratchet and report in `lexicon.py`.
Deletions are safe; additions are the hazard.

### The literal `.lexicon.conf` an owner would write

```
# .lexicon.conf — the naming declaration for this repo. ONE reader: tools/lexicon/lexicon_conf.py.
#
# GRAMMAR: KEY="value" on one line, no trailing comment after a value; or a KEY: header followed by
# INDENTED rows, where the FIRST token is the row key and the remainder is prose.
#
# THE BOUNDARY, stated once because "hardcodes nothing" needs one. Yours: which languages are armed,
# which cells are graded and at what convention, the verb table, the banned tails, the pins, the
# waivers, and whether the canon is frozen. The kit's: what `snake` MEANS (overriding a convention's
# shape can only weaken it), the extractors' code, and the report format. Ratified doctrine — a knob
# is a kit constant, not a conf key (TOOL-cBriefedPilot-2) — is why that line sits where it does.

# ---- provenance -----------------------------------------------------------------------------
# A human curated the table below on this date. An empty value fails the gate.
ratified="2026-08-16 human-curated"

# R2's door, and it is SHUT. Non-empty arms the CANON: block at the foot of this file — the one
# route by which a debt spelling (`get`, `fetch`, `validate`) can become a legal row. The engine
# prints the posture on EVERY run, green as well as red, so an unfrozen canon is never a quiet fact.
# Format: <iso-date> node <tag> — <why>. A block with an empty stamp is a REFUSAL.
canon_unfrozen=""

# G2's one-time expansion stamp. Non-empty makes `adopt-lexicon.sh --expand` refuse. Clearing it is
# a deliberate, tracked, reviewable edit — which is the point: a table you widen on every refusal is
# a synonym list, not a closed vocabulary.
expanded=""

# ---- the vocabulary -------------------------------------------------------------------------
# ONE table for the repo; the CELLS block decides which surfaces it is APPLIED to. Every row carries
# a NEGATIVE, because a row with only a positive gloss cannot tell two verbs apart and the boundary
# is the whole product — the checker refuses a bare row. Spellings come from tools/lexicon/canon.py,
# written without reading this corpus. The corpus decided only WHICH concepts appear here.
VERBS:
  build     create a new value and return it — NOT `create`, which is reserved for side-effecting setup
  load      read a store into memory — NOT `fetch`, which implies a network call
  read      pull bytes or records from a named source — NOT `get`, which says nothing about cost
  write     persist to a store — NOT `save`, which hides whether anything was already there
  parse     turn text into structure, raising on text that is not that structure — NOT `convert`
  render    turn structure into text — NOT `format`, which reads as cosmetic
  resolve   turn a name into the thing it denotes, RUNNING the candidate where that is the only proof — NOT `lookup`, a lookup returns a row; resolve returns the thing
  check     assert a predicate and return a verdict — NOT `validate`, which implies mutation on failure
  scan      walk a population looking for matches — NOT `search`, which implies stopping at the first
  extract   pull a declared shape out of a larger one — NOT `pluck`, pluck names the taking; extract names the declared shape taken
  measure   count a population and report the number, deciding nothing — NOT `count`, count is the arithmetic
  derive    compute a value from a source so it never has to be authored — NOT `compute`, compute says a value was produced, not that it never has to be authored
  seed      write an initial value the tool will not overwrite again — NOT `install`, install claims the tool owns the result after
  init      set up state at construction — NOT `setup`
  run       execute a process to completion and report its outcome — NOT `execute`, the same word twice
  arm       make a dormant check live; its opposite is a check that cannot fail — NOT `enable`, which reads as a feature flag
  add       append to an existing collection — NOT `append`, append claims a position at the end; add claims only membership
  remove    detach without destroying — NOT `delete`, which is irreversible
  set       assign a known value — NOT `update`, which implies a diff against prior state
  print     write to stdout for a human, never a return value in disguise — NOT `log`, log implies a level, a sink and a filter
  main      a module's CLI entry point; reserved, one per module — NOT `start`, which names a lifecycle event
  cmd       a subcommand entry point, dispatched by name; reserved — NOT `do`, which names no role
  test      a test function; reserved for harnesses — NOT `assert`, assert is one statement inside a test

# Type-name suffixes naming a responsibility nobody scoped. Graded on cells declaring `notail`.
BANNED_SUFFIXES="Manager Helper Util Utils Handler Processor Data Info"

# ---- extraction -----------------------------------------------------------------------------
# <ext>:<pattern-set-id>:<mode> — HOW definitions come out of an extension. An extension present in
# the corpus with no row here is a named refusal, never a silent skip. `sh` is DARK deliberately: a
# regex over shell function definitions would look like coverage while silently skipping what it
# forgot. A naive probe finds 581 of them and that number is a FLOOR, which is the whole objection.
# A dark language contributes no definitions and therefore carries no function/type cell — but its
# FILENAMES need no extractor, which is why `sh.file` below is armed.
LANGS="<none>::dark conf::dark example::dark gitattributes::dark gitignore::dark js:js-regex:probe json::dark md::dark py:python-ast:parser sh::dark toml::dark tsv::dark txt::dark"

# Owner-declared probe pattern sets, merged over the kit's shipped ones. This is how a language the
# kit does not ship gets graded without forking an `engine`-role file. Rows are
# <pset-id>.<functions|types>  <python regex with exactly one capturing group>. A declared set whose
# population is empty REDS as a DEAD PROBE, so a regex that matches nothing cannot look like coverage.
# Nothing here today: this repo tracks no language beyond py and js.
# PATTERNS:
#   ts-regex.functions  ^\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)
#   ts-regex.types      ^\s*(?:export\s+)?(?:class|interface|type)\s+([A-Za-z_$][\w$]*)

# ---- R1: the (language, surface) matrix -------------------------------------------------------
# <ext>.<surface>  <convention> [vocab] [notail]
#   surfaces      function · type · file
#   conventions   snake · screaming · camel · pascal · kebab · dark
#                 MEMBERSHIP, not equality: `run` satisfies snake, camel and kebab at once, and a
#                 predicate that picked one answer would red it. 255 of 1086 names here satisfy two
#                 or more. Leading and trailing underscores strip first — `__init__` and `_build` are
#                 privacy markers, not case. A `file` cell grades the basename up to its FIRST dot,
#                 so `map_extractors.template.py` grades on `map_extractors`; the last-dot rule
#                 disagrees on 64 graded files and reds every template the kit itself ships.
#   vocab         arm P1 on the leading token against VERBS
#   notail        arm P2 against BANNED_SUFFIXES
# A cell with a non-empty population and no row REDS as UNDECLARED. An armed row over a population of
# zero REDS as a DEAD CELL. A `dark` row is a legal, visible refusal and the run prints it as one.
CELLS:
  py.function         snake   vocab
  py.type             pascal  notail
  py.file             snake
  js.function         camel   vocab
  js.file             kebab
  sh.file             kebab
  toml.file           kebab
  txt.file            kebab
  json.file           kebab
  tsv.file            kebab
  <none>.file         kebab
  md.file             dark
  conf.file           dark
  example.file        dark
  gitattributes.file  dark
  gitignore.file      dark

# NOT DECLARED, each with the measurement that decided it:
#   js.type       population 0 across all 11 tracked .js files. Declaring it REDS as a DEAD CELL,
#                 which is exactly the arm working: `.js` reports 122 functions and would otherwise
#                 stay green while a class cell graded nothing.
#   py.constant   the population is not mechanically identifiable. Module-body Name targets: 539
#                 total / 419 screaming; simple single-Name targets: 432 / 413; public simple
#                 targets: 331 / 331. Only the third yields a clean cell, and it is clean because
#                 the leading underscore that excludes a name is what correlates with mutable module
#                 state. A cell whose population is defined by its own predicate cannot fail.
#   sh.function   `sh` is dark in LANGS; a definition cell for a dark language is a refusal.

# ---- the pins -------------------------------------------------------------------------------
# MEASURED, never chosen: `python tools/lexicon/lexicon.py --measure` emits this whole block. Paste
# it. Rows are <ext>.<surface>.<predicate>  <count>; a count ABOVE its pin reds, a count BELOW it
# prints the exact replacement row (see §8 Q2 for the fork on whether below should red too).
#
# `debt` is an offender whose leading token is a canon-cluster alternative, so the report names the
# replacement. `unruled` is one in no cluster and no row — the kit has no rename to propose for
# `demand_writable_target` or `git_path`, and 184 of the 258 distinct unruled tokens appear exactly
# once. They are pinned SEPARATELY rather than merged, because one bucket over two populations is
# why the old VERB_OFFENDER_PIN moved eleven times and produced no renames from the second.
PINS:
  py.function.debt        43
  py.function.unruled    373
  py.function.conv         0
  py.type.suffix           0
  py.type.conv             0
  py.file.conv             7
  js.function.debt         0
  js.function.unruled     45
  js.function.conv         0
  js.file.conv             0
  sh.file.conv             4
  toml.file.conv           0
  txt.file.conv            0
  json.file.conv           0
  tsv.file.conv            0
  <none>.file.conv         0

# The seven py.file offenders are hyphenated Python basenames — modules no import can resolve. That
# is a defect class, not a style preference, and it is this gate's failing case observed IN THE TREE
# rather than staged. Draining it is a rename plus the gate-leg argv that names the file; see the
# build record. The four sh.file offenders are three frozen dated build-repro scripts and
# tools/run-gates/profile_bar.test.sh.

# ---- R2: the door, shut ------------------------------------------------------------------------
# Uncomment to override tools/lexicon/canon.py's frozen clusters, and stamp canon_unfrozen above.
# A row REPLACES a cluster's alternatives by representative, ADDS one for a new representative, and
# a leading minus DELETES a shipped cluster. The canon GRADES NOTHING — it decides what a machine may
# propose and how an offender is labelled — so unfreezing it cannot legalise a name by itself; only a
# VERBS row a human wrote can. What it CAN do is make your corpus's own spellings the canon, which is
# the mirror defect this kit was rebuilt to close. That is why the stamp requires a reason.
# CANON:
#   read      get list access obtain consume peek
#   -run      this project does not want `run` claiming `do`, `handle` and `process`
```

---

## 4. THE SURFACE × CONVENTION DEFAULT TABLE

Shipped as a frozen `DEFAULT_CELLS` constant in `canon.py`, read by `scaffold_lexicon.py` **and by
nothing else**. The engine reads only the declaration, so there is no default-fallback at grade time
and therefore no second carrier of a cell's value: an undeclared cell is a refusal, not a silent
default. The table is exogenous by the same argument the clusters are — snake-for-Python and
camel-for-JavaScript are language conventions, written without reading any adopter's tree, with no
ranking step in them to corrupt. **R2 builds no unfreeze machinery for this table**, because it cannot
become a mirror.

| Language | `function` | `type` | `file` | `constant` |
|---|---|---|---|---|
| py | **snake** + vocab | **pascal** + notail | **snake** | *undeclared* — population not identifiable (§1.4) |
| js / ts / jsx / tsx | **camel** + vocab | **pascal** + notail | **kebab** | *undeclared* |
| go | **pascal**/**camel** (exported/unexported — one cell cannot express it; ship `dark` and say so) | **pascal** | **snake** | *undeclared* |
| rs | **snake** + vocab | **pascal** | **snake** | *undeclared* |
| sh | *dark* (a regex probe is a floor, not a population) | — | **kebab** | — |
| md / prose | — | — | **dark** | — |
| data (toml/json/txt/tsv/yaml) | — | — | **kebab** | — |

Measured cost of arming this table on *this* corpus, cell by cell: `py.function` 0 of 925 ·
`py.type` 0 of 39 · `js.function` 0 of 122 · `py.file` **7** of 47 · `js.file` 0 of 11 ·
`sh.file` **4** of 89 · the five data-file cells 0 of 66. **Total 11 violations across 213 graded
files, all of them filenames.**

Three notes the table has to carry, or it is decoration:

1. **A single global `file` cell is measurably wrong.** `file=kebab` reds the 20 snake `.py` stems;
   `file=snake` reds 38 shell scripts. This repo is its own counterexample to the rejected
   one-convention-per-surface design, which is R1's justification in one line.
2. **`md.file` must be dark, not kebab.** Of 1172 `.md` stems, 173 violate kebab and **921 satisfy no
   convention at all** (`DECISIONS.2026-08-10`, `WIRE-INTO-PROJECT`). A naming gate over a record tree
   grades nothing a reader needs, and this tree carries a sixth shape (SCREAMING-KEBAB) the five-value
   vocabulary cannot express. Dark is the honest answer, not a dodge.
3. **The `go` row is why the matrix is not enough on its own.** Go's export rule makes case a function
   of visibility, not of surface, and a `(language, surface)` cell cannot say that. Ship it `dark` and
   record the gap rather than shipping a cell that reds half a correct codebase. The same class is
   waiting in React: PascalCase function bindings are components, and the recorded adopter has 1,072
   of them. A **name-prefix or decorator selector** routing a subset of a cell's population to a
   different convention is the answer, and it is deliberately **out of scope for this rebuild** —
   flagged, unbuilt, and named in §8 Q10 so nobody discovers it at adoption time.

**Every cell above ships with `vocab` OFF except `py.function` and `js.function`.** Measured: a
definition name's leading token lands in the canon 54.8% (py.function) and 63.1% (js.function) of the
time, against 3.6–5.1% for locals, parameters, constants and classes. A verb table over the latter is
noise, and that measurement is the reason the surface set is three and not five.

---

## 5. G2 EXPAND-ONCE AND R2 OWNER-UNFREEZE

### G2 — `bash tools/lexicon/adopt-lexicon.sh --expand`

Today `adopt-lexicon.sh:248` refuses outright when a declaration exists, so the only tool-supported
transition is empty → seeded. `--expand` is the second and last one.

1. **Guard.** Reads `expanded=` from the conf and refuses when non-empty: *"this declaration was
   expanded on `<stamp>`; clearing this key is a deliberate edit."*
2. **Candidates — the closure is inherited verbatim.** `scaffold_lexicon.py:143` is
   `live = {forms[v] for v in counts if v in forms}`, and **that line is not touched**. Expansion
   proposes exactly the canon clusters with a live site that the table does not already declare — a
   set subtraction against the seed logic, nothing more. A token in no cluster **cannot be proposed**.
   This is the single most important property in the design: without it, expansion on this corpus
   would offer `git`, `signal`, `bounded`, `kit`, `all`, `repo` and `no` — seven of the ten non-verbs
   the original defect produced.
3. **Evidence, not proposals.** The unruled tail prints below the proposals under a header that says
   in words: *these are NOT proposals; a row here would be the mirror defect this kit was rebuilt to
   close.* An owner whose project genuinely owns `demand` may still write that row by hand — the canon
   bounds what a machine may propose, never what an owner may declare (`canon.py:44-47`), and this
   repo's own table already carries `seed` and `arm`, which no cluster holds.
4. **The brake is structural, not procedural.** `lexicon.py:503-511` reds any `VERBS` row carrying no
   negative. A hand-written row is therefore **born failing the gate** until a human writes the
   boundary word — which is the scoping question the table exists to force. Only canon-rendered rows
   (which carry a derived NOT clause) parse green unaided.
5. **Stamp.** `--expand --stamp` writes `expanded="<iso-date> <sha>"`, the sha being the tree the
   candidate set was measured against, so the run is reproducible.
6. **Re-measure.** Expansion moves pins; the `PINS:` block must be re-pasted, so an expansion cannot
   land without its cost showing in the diff.

**What makes it visible and recorded:** the stamp is a tracked scalar in the file the owner already
diffs; the proposals arrive in stdout and are pasted by hand; every row an expansion added is derivable
on every run as "rows outside the canon", so provenance is computed rather than authored. **What it
does not do:** stop an owner clearing the stamp. Nothing running under the owner's own uid can. The
stamp makes a second expansion a visible edit rather than an invisible habit — the same standard §9
holds the unattended kit to.

### R2 — the canon door

**Today there is no door.** `canon.py` falls under `kit.toml:17-19`'s `include = "**"` / `role =
"engine"`, so an upgrade overwrites an adopter's edit; `kit.toml` is in the same pool, so the file
cannot even be durably re-roled. That is not "frozen by default", it is welded.

**The door is a `CANON:` block in the declaration plus a stamped `canon_unfrozen=` scalar.**
`canon.py` stays `engine` and keeps upgrading.

*Why not the obvious `role = "seed"` flip.* `kit.toml:25-28` documents seed as "copied ONCE, then the
target owns it" — so flipping canon.py to seed freezes an adopter's clusters at whatever version they
first installed and silently ends canon upgrades. An override bought with an upgrade regression, hidden
in a Python file nobody diffs as a declaration. The conf is the file the owner already curates.

The block merges over `canon.CLUSTERS` inside `build_form_index()`, which is already the one place
every consumer resolves a form: a row naming an existing representative **replaces** its alternatives,
a new representative **adds** a cluster, a leading minus **deletes** one. Full unfreeze — add, replace,
remove — in about thirty lines, in a function that already exists.

**Visible.** `lexicon.py` prints `lexicon: CANON UNFROZEN — <n> owner row(s) · <stamp>` on **every
run, green as well as red**, above the counts. Green output is where a reader stops looking, which is
exactly why the fact sits there. A run that says nothing means the canon is frozen; there is no state
in which it is quietly overridden. The shipped conf carries the commented example block, so the
capability is legible from the file before it has ever been used.

**Recorded.** A `CANON:` block with an empty stamp is a **refusal**, checked by the same CRLF-hardened
grep shape the `ratified` arm already uses (`adopt-lexicon.sh:226-233`), on the `lexicon wiring` leg —
`guard: []`, so it fires on a conf-only diff. The stamp must carry a date, a node **and a reason**; a
date alone records that it happened, not why.

**Structural guard against the mirror returning through the proposal path:** `scaffold_lexicon.py` may
never emit a `CANON:` header. Asserted by `grep -c CANON tools/lexicon/scaffold_lexicon.py` on the
`lexicon naming predicates` leg — chunk `declarations`, subject `repo`, which the push bar runs.
Deliberately **not** on the kit selftest, which it does not.

**The honest limit.** An owner may unfreeze the canon and fill the overlay from their corpus's own
commonest spellings, reinstating precisely the defect `canon.py` closes. No machine check can tell that
overlay from a considered one; the difference is why the rows were chosen, and the tool cannot see why.
What the design buys is that the choice is visible in one tracked line, attributed to a node and a
date, refused without a reason, and printed on every single run. The blast radius is bounded: the canon
**grades nothing** — it decides what a machine may propose and how an offender is labelled — so an
unfrozen canon cannot legalise a name by itself.

---

## 6. G4 — THE INTEGRATION POINTS

### 6a. Codebase map — the correct answer is zero churn, and that is a finding

`VERBS` stays a **flat verb table**; only `CELLS` decides which surfaces it is applied to. Therefore
`map_extractors._read_lexicon_verbs()` (`map_extractors.py:139-168`, which sys.path-inserts the kit and
calls the lexicon's own `load_conf`) returns the same 23 keys, with the same fail-closed-to-empty
contract, and **all 20 claim tables stay untouched**. That is not luck — it is the reason the matrix
went into a new key instead of reshaping `VERBS`.

**Do not mint new inventory ids for the cells.** Two reasons, one measured and one from the source.
Measured: `map_lib.py:938-943` raises on **missing** claim keys, not merely unknown ones, so each new
id costs an edit to 19 dossiers plus `FOUNDATION.md` in the same commit. From the source:
`map_extractors.py:126-134` records that for a hand-authored vocabulary "the ADDITION half is weak …
the DELETION half is the load-bearing one." A cell like `py.function=snake` has no rots-into-fiction
mode the report does not already print. If cells ever need a ratchet, qualify the key **string** inside
the existing id (`py.function:read`) — the in-place rename precedent is recorded at
`memory/map/baseline.toml:6-11`.

**Direction is ratified and must not reverse.** The map may read the lexicon; the lexicon may not read
the map, and `subtokens.py` is a deliberate port rather than an import so the kit ships self-contained.
Deleting P3 removes the `LAYERS` row that encoded this, so the constraint moves to a source scan on the
`lexicon naming predicates` leg — one grep over six files, on a leg the push bar runs.

**One cross-kit edit is owed, in the same commit:** `tools/codebase-map/selftest.py:1268-1276` asserts
`lexicon.DEAD_TOKENS == map_lib._STOPWORDS`, and `DEAD_TOKENS` dies with `--brief`. That leg's guard
already includes `tools/lexicon/`, so it selects itself — but it is `chunk = selftests`, so a miss will
**not** surface at the push that caused it. It goes in the same commit or not at all.

**A second cross-kit edit the input designs missed:** `tools/drift-audit/selftest.py` writes three
fixture `.lexicon.conf` files carrying `LAYERS:` blocks (`:734`, `:814`, `:890`) plus three
`LAYER_OFFENDER_PIN` references. Removing `LAYERS` from `BLOCK_KEYS` makes those a hard `ConfError`,
which `drift_report._load_lexicon` swallows into `None`, degrading every lexicon signal to `not_asked`
and failing the arms that assert `gateable is True`. That leg's guard is
`["tools/drift-audit/","tools/lib/"]` — **it does not include the lexicon**, so a lexicon-only commit
does not even select it, and it is `chunk = selftests`. This break is invisible to the push bar in two
independent ways. Fix the fixtures in the same commit.

**Preserved untouched:** `drift_report.py`'s three lexicon signals. `lexicon_marginal_offense_rate`
derives both operands from one extractor against git blobs at two shas, so `extract`'s signature is
frozen by contract. Putting the matrix in `CELLS` rather than widening the `LANGS` triple also **avoids
making TOOL-dUnstalledConvoy-35 worse**, since that signal fires on any commit touching `LANGS=` and a
per-cell edit never touches that line.

### 6b. Spec templates — one line, deliberately ungated

`memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` both contain **zero** lexicon references, so this half
is greenfield: nothing to honour, nothing to reverse. The hook goes in §4's already-canonical
`### Inventory` sub-head — a spec names each identifier it will mint **with its cell**
(`resolve_profile · py.function`), and cites `--suggest <name> --as <cell>` where a name was refused.

**It is not wired into `check-memory-hygiene.sh`,** and the evidence is the reason rather than taste.
`memory/HYGIENE.md:384-398` sets the governing precedent for exactly this kind of neighbour
integration: hygiene **sanctions** an adjacent kit's files and refuses to enforce that kit's rules —
"The map's coverage/freshness enforcement is its own test file, not this script." And §10's Reuse audit
is the cautionary measurement: the only prose-graded arm this repo has built needed its probe half
truncated at the first terms marker, end-of-line truncation was tried and leaked, and
`TEMPLATE-SPEC.md:145-156` still admits an open hole where one line satisfies both arms. A second
prose-graded arm would be a weaker grader of a question the code predicate already answers on the real
definition site.

**This paragraph is the §7 compensating-check record for that exemption:** the compensating check is
the gate itself — the identifier is graded the day it exists in code, which is a stronger claim than a
spec bullet can make. If the owner wants teeth anyway, the precedented shape is a sixth dated cutoff in
hygiene check 12 beside the five that exist (`check-memory-hygiene.sh:31-34`, `:55`), grading **shape
only** — that a bullet names a cell, never that the cell exists.

### 6c. Gate legs, Skill and charter

Three legs keep their names, argv, guards and ceilings, so `tools/gate-legs.json` and the map's
gate-leg inventory do not churn. The `lexicon wiring` leg byte-compares the rendered Skill and carries
`guard: []`, so a changed placeholder set trips it until re-rendered — the transition's own tripwire is
already installed. `SKILL.template.md` loses `BRIEF_CLI` and gains `--as <cell>` in its routing line;
`kit.toml`'s placeholder list follows.

The charter's §12 kit-conditional block must be **replaced at net zero bytes or smaller**:
`check-template-size.sh` reports 48867 / 49152 with **285 free** and already WARNs past its recorded
high-water. The forbidden-import sentence goes with P3; a (language, surface) sentence and an
unfreeze-stamp sentence take its place. The rows themselves stay out of the charter, exactly as the
existing bullet already insists.

---

## 7. PROPOSED UNIT BREAKDOWN

| # | Unit | Acceptance check |
|---|---|---|
| U1 | Delete P3 and move its one real constraint onto the declarations leg | `lexicon naming predicates` REDS when a `codebase-map` import is staged into any `tools/lexicon/*.py`, and greens when unstaged (break observed per §7). `--check` prints no P3 line. `drift-audit selftest` and `lexicon selftest` green under `GATE_SELFTESTS=1` with the three `LAYERS` fixtures removed. |
| U2 | Delete `--brief`/`--probe`/`DEAD_TOKENS`; collapse four corpus walks into one `scan_corpus`; split `run()` into a measure pass and a verdict pass | `--measure` and `--check` emit byte-identical surviving lines to today's output. `codebase-map kit selftest` green with its `DEAD_TOKENS` arm deleted. A staged refusal reachable only from the measure path is reported by BOTH modes (the class `lexicon.py:625-670` confesses to three times). |
| U3 | `CELLS:` and `PINS:` block grammar; generic `_parse_block` default; widened `BLOCK_KEYS` | A `CELLS` row naming an extension absent from `LANGS` reds. `--print-rows CELLS` prints the matrix for bash without a second parser. A row key containing a dot parses (today `lexicon_conf.py:104` refuses it). |
| U4 | P3-new: the convention predicate in `subtokens.py` — six regexes, set membership, affix strip, first-dot stems | Staged `def loadUserData` reds `py.function`; `__init__` and `_build_index` pass; `FAMILY_of` reds AMBIGUOUS with a message distinct from VIOLATION; `python tools/lexicon/lexicon.py --check` reports `py.file.conv 7` and `sh.file.conv 4` from the tree with nothing staged. |
| U5 | The three cell refusals: UNDECLARED CELL, DEAD CELL, and the per-cell coverage report | Adding `js.type pascal` to the conf REDS as DEAD CELL **today, from the tree, with nothing staged** (population 0). Adding a `class Cap {}` to a tracked `.js` file with no `js.type` row reds as UNDECLARED CELL. Every declared cell, dark ones included, appears in the report. |
| U6 | P1 split into `debt`/`unruled` with canon-backed advice; wire the offender line and `--suggest` to `canon.build_form_index()` | `--suggest ensure_cache` names `check_cache` (today it names nothing — measured, 36 of 43 debt definitions are silent). `--check` prints two rows summing to 461. `--measure` emits the whole `PINS:` block. |
| U7 | `--suggest <name> --as <cell>`: surface-aware, consults `BANNED_SUFFIXES`, re-cases to the declared convention | `--suggest FooManager --as py.type` names `Manager` (today it answers about `foo`). `--suggest fetchUserData --as py.function` returns `load_user_data` (today it returns `loadUserData`, a name the new gate reds). `--as` is required; omitting it is a refusal, not a default. |
| U8 | Owner-declarable `PATTERNS:` block, merged over the shipped `PATTERN_SETS` | A fixture repo declaring `ts:ts-regex:probe` plus two `PATTERNS` rows grades its `.ts` functions and reds a violation. A declared pset matching zero definitions reds DEAD PROBE. `KNOWN_EXTS` no longer gates which languages an adopter may arm. |
| U9 | `--expand` (G2) | Refuses with `expanded=` non-empty. On this corpus it proposes **only canon clusters not already declared** and prints the unruled tail under a not-proposals header. A pasted proposal parses green; a hand-pasted tail row reds as a bare row. A selftest arm asserts the candidate set is a subset of `canon.CLUSTERS` representatives. |
| U10 | The canon overlay + stamp (R2) | A `CANON:` block with an empty `canon_unfrozen` reds on `lexicon wiring` (guard `[]`, so a conf-only diff fires it). A stamped block prints `CANON UNFROZEN …` on every run **including green**. `grep -c CANON tools/lexicon/scaffold_lexicon.py` is 0, asserted on the declarations leg. A CRLF conf cannot launder an empty stamp. |
| U11 | The conf rewrite, the records, and the G4 spec-template line | Hygiene green. `memory/TEMPLATE-SPEC.md` §4 carries the cell line. The decision ids in §8 Q8/Q9 are written. The three stale carriers about the map wiring (dossier says BLOCKED, spec header says CLOSED, backlog says SPECCED) agree. `ratified` re-stamped in the same commit as the `LANGS` edit, or `signal_lexicon_ratified_stale` fires. |

Sequencing note: U1 and U2 are pure deletion and should land first — they shrink the surface every
later unit edits, and both close open rows (TOOL-dUnstalledConvoy-15, TOOL-cSettledDocket-12) for free
if `selftest.py` is rewritten anyway. U8 is independently landable and is the only unit that helps a
non-py/js adopter.

---

## 8. OPEN QUESTIONS FOR THE OWNER

Genuine forks only. Each carries a recommended default the build takes if you say nothing.

**Q1 — Keep the 418 UNRULED offenders pinned, or stop gating them?**
Two of the three input designs dropped the unruled pin entirely, arguing the kit has no rename to
propose for `demand_writable_target` and that eleven pin moves bought no renames from that population.
The counter-argument is that §12 says the table's value is **scoping, not spelling** — "a name that
will not fit is reporting an unclear responsibility" — and a predicate that fires only on canon debt is
a synonym denylist by construction. It also brushes TOOL-dScaffoldedMirror-16, which superseded the
retirement condition on the ground that the enforcement is the point.
**Recommended default: keep both pinned** (`debt 43` + `unruled 373/45`, sum unchanged at 461). The
split then costs no enforcement reach and is purely a reporting and advice improvement. Dropping the
unruled pin later is a one-line edit and an owner ruling; doing it now needs one and does not have one.

**Q2 — Should a pin count that FALLS red, or warn?**
"Shrink-only" appears in the conf and in all three waiver headers and in **no line of Python**; the only
comparison is `> pin`. A two-sided equality assertion makes the ratchet real — but it reds the bar on
correct work until a second commit edits a scalar, and two nodes each draining one name produce a
conflicting single-line edit in a shared mutable scalar that cannot reconcile additively.
**Recommended default: red above, WARN below, printing the exact replacement row.** State plainly that
this is not a full ratchet and name the compensating instrument: `lexicon_marginal_offense_rate` is
per-window rather than a ceiling, so it sees a drain-then-re-add that a ceiling cannot.

**Q3 — The seven hyphenated `.py` filenames: rename them, or waive them?**
They are genuine defects (unimportable modules) and they are this gate's observed failing case. They
are also named in `tools/gate-legs.json` argv and in kit descriptors, so renaming is a cross-kit change.
**Recommended default: ship `py.file` armed with `py.file.conv 7`, and file the renames as their own
unit.** A pin is drainable and visible; seven waiver rows on day one are a pile.

**Q4 — Build the owner-declarable `PATTERNS:` block (U8) now, or defer it?**
Deferring is defensible under YAGNI: the measured adopter population is zero. But `KNOWN_EXTS` and
`PATTERN_SETS` live in an `engine`-role file an upgrade overwrites, so today an adopter in TypeScript,
Go, Rust or C# can only declare their language `dark` — and the whole vocabulary-and-convention
apparatus then grades filenames or nothing.
**Recommended default: build it.** It is the only unit that makes the rebuild worth doing for anyone
but this repo, and it defers the `.ts/.tsx` ruling (TOOL-dScaffoldedMirror-13, still unwritten ten days
on) to the owner who actually has the corpus.

**Q5 — Arm `sh.function`?**
Shell is 79 of the 80 unarmed definition-carrying files, the largest code surface here by file count. A
naive probe finds **581** definitions in 0.04 s. But that probe is exactly the regex `sh::dark` was
written to refuse — 581 is a floor reported as a population, which is the green-by-absence class.
**Recommended default: no. Stays dark, `sh.file` armed.** Re-take this deliberately with a real shell
parser if it is ever wanted; do not inherit it either way.

**Q6 — `py.constant`: arm it on which population, or leave it dark?**
539 module-body targets / 419 screaming, or 432 simple targets / 413, or 331 public / 331. Only the
third is clean, and it is clean because the predicate selects its own population.
**Recommended default: dark, with all three numbers written into the conf comment**, until the
declaration can say what a constant IS (an annotation, a marker, an `__all__`-style list).

**Q7 — What should the AMBIGUOUS verdict DO — red, warn, or count as ungradeable?**
Measured: **0 of 1086** graded identifiers return an empty convention set. The only live instances
(`FAMILY_of`, twice) are in dark shell. So this arm ships exercised only by a staged fixture, and I have
no in-corpus instances to reason from.
**Recommended default: RED, with a message distinct from VIOLATION**, because a name that chose no
convention is a different fact from one that chose the wrong one, and building the distinction now is
cheaper than discovering it at an adopter.

**Q8 — The kill rule's arithmetic disagrees across carriers.**
`drift_report.py:954` and two specs say the condition needs "two FURTHER readings";
`memory/builds/dScaffoldedMirror/README.md:121` says today's is "reading one of two". The fresh-file arm
reads **3.6%** (5 of 138), the second sub-5% reading. Under one carrier this rebuild is building past a
stop rule; under the other the condition is met.
**Recommended default: settle it in `drift_report.py` as the single carrier** and supersede the prose
copies, before today's 3.6% is cited as authority for anything.

**Q9 — Which records get written, with ids?**
Three are owed and none is optional. (a) A **supersession of TOOL-dScaffoldedMirror-18**, live at
`memory/DECISIONS.md:100`, which instructs a reader to build a 459-row grandfather backfill for a
pressure chain this rebuild does not build; the supersession was recorded as owed by its own round-2
review, never written, and the byte ceiling it was parked behind has since been retired. (b) An id
**recording R1's reversal of the "P4 casing refused" ruling**, which today lives only in a build record
and would be a supersession nobody finds — and it is the easy kind to argue, because that refusal
promised a compensating README line telling adopters to wire their own linter and grep finds no such
line, so R1 closes an uncovered gap rather than overriding a covered exemption. (c) An id for **P3's
removal with its compensating check**.
**Recommended default: write all three in this build.**

**Q10 — The visibility/framework axis the matrix cannot express.**
Go's export rule and React components both make case a function of role rather than of surface: the
recorded adopter has 1,072 PascalCase function bindings in `.tsx` that a `js.function=camel` cell would
red in bulk. The answer is a **name-prefix or decorator selector** routing a subset of a cell's
population to a different convention — the same mechanism that would grade the 31 `cmd_*` subcommand
handlers and the 106 `test_*` arms without inventing new surfaces.
**Recommended default: out of scope for this rebuild, flagged not hidden.** Ship the `go` and `tsx`
cells `dark` with the reason written down, and file the selector as its own unit. A cell that reds half
a correct codebase is worse than no cell.

---

*Two things this report deliberately does not do. It does not delete the coverage sniffer, because the
code being deleted argues the case against its own replacement at `lexicon.py:126-131` and a
declaration-derived denominator is a number the owner moves by typing. And it does not claim the debt
class can name its replacement, because I ran all 23 debt tokens and five of them can.*
