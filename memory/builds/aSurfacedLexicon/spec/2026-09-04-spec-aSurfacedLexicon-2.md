# TOOL-aSurfacedLexicon-2 — delete P3, keep its one real constraint

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Delete the import-direction predicate P3 from the lexicon kit and replace its single declared rule
with a self-containment refusal that judges the population P3 could actually reach. The predicate
costs 164 engine lines and 29 self-test arms to enforce one rule over 44 of the 548 imports its own
green line claims to grade, and that pin has held the value `"0"` across every commit it has ever
had.

## 2. Scope (IN)

- **S1** — Delete the eight P3 engine functions from `tools/lexicon/lexicon.py`: `_build_glob_rx`,
  `_check_path_suffix`, `_glob_match`, `build_module_index`, `_resolve_relative`, `resolve_import`,
  `check_layer_violation` and `scan_unselective_rules`. Measured at 164 lines by AST spans over the
  file at writing time.
- **S2** — Remove the `layer` third from the predicate machinery in `run()`: the `WAIVER_FILES` and
  `PIN_KEYS` entries, the `offenders` and `graded` keys, the `tally` and `label` rows, the
  `P3 NOT ARMED` refusal, and the `UNSELECTIVE LAYERS RULE` refusal.
- **S3** — Delete `tools/lexicon/lexicon-layer-waivers.txt`, drop it from the `include` array at
  `tools/lexicon/kit.toml:26`, and delete the `lexicon-layers` hole at `tools/lexicon/kit.toml:103`.
- **S4** — Delete the `LAYERS` block from `.lexicon.conf` and the `LAYER_OFFENDER_PIN` scalar at
  `.lexicon.conf:166`.
- **S5** — Remove `LAYERS` from `lexicon_conf.BLOCK_KEYS` at `tools/lexicon/lexicon_conf.py:32` and
  delete the glob-pair branch of `_parse_block` that only `LAYERS` reached.
- **S6** — Add the self-containment refusal described in §4 to the `run()` check path, so the
  `lexicon naming predicates` leg carries it without a change to that leg's argv.
- **S7** — Delete the 29 P3 arms from `tools/lexicon/selftest.py`: the fixture block, the
  `GLOB_CASES` table, the `resolve_import` case table and the `LAYER_SIDES` fixture dict. Add the
  arms for the new refusal named in §6.
- **S8** — Repair the three `LAYERS:` fixtures in `tools/drift-audit/selftest.py` at `:734`, `:814`
  and `:890`, plus the three `LAYER_OFFENDER_PIN` strings beside them.
- **S9** — Repair the prose carriers: `tools/lexicon/README.md:24` and `:26`,
  `tools/lexicon/LEXICON.md:76-85`, the `LAYERS` seed emission at
  `tools/lexicon/scaffold_lexicon.py:171` and `:215` with its module docstring at `:16-18`, and the
  forbidden-import clause in the §12 bullet of both `AGENTS.md:383` and
  `coding-governance-agents.template.md:318`.
- **S10** — Add `tools/dead-path-waivers.txt` rows for the four spellings of the deleted waiver
  filename in `tools/govkit/fixtures/incms-2cff5855.receipt.json`, which is a frozen adopter receipt
  and must not be rewritten to please a gate.

## 3. Non-goals (OUT)

- The convention predicate that takes the name `P3` in the rebuilt kit. That is a separate unit and
  this one leaves the kit at two predicates, not three.
- Widening `BLOCK_KEYS` or making the default block parse generic. This unit only removes a key;
  the generic grammar is its own unit and inherits a `_parse_block` with one branch left.
- Deleting `--brief`, `--probe` or `DEAD_TOKENS`, and collapsing the corpus walks. That is the
  sibling unit at the same build order.
- Rewriting `tools/govkit/fixtures/incms-2cff5855.receipt.json`. A receipt records what a real
  adopter install wrote, so waiving its lines is correct and editing them is falsification.
- Renaming the seven hyphenated `.py` basenames. Ruled to be its own unit.
- Any change to `extract`, `extract_text` or `_python_defs`. Their signatures are frozen by
  contract because `tools/drift-audit/drift_report.py` derives both operands of
  `lexicon_marginal_offense_rate` through them.

## 4. Design

### Inventory

Everything below was measured on this worktree at writing time, not inherited from the research
record.

| What dies | Size | How it was measured |
|---|---|---|
| Eight P3 engine functions | 164 lines | AST spans over `tools/lexicon/lexicon.py` |
| P3 self-test arms | 29 of 140 `check(` arms | `grep -c` over `tools/lexicon/selftest.py` |
| `LAYERS` block and `LAYER_OFFENDER_PIN` | 3 conf lines | `.lexicon.conf:164-166`, `:215-216` |
| `lexicon-layer-waivers.txt` | 1 tracked file, header only | `cat`, no waiver row has ever existed |
| The `lexicon-layers` hole | 1 `[[hole]]` block | `tools/lexicon/kit.toml:102-108` |
| `LAYERS` fixtures in a neighbour kit | 3 | `grep -n LAYERS tools/drift-audit/selftest.py` |

The case for deletion, re-measured rather than quoted. `.lexicon.conf` declares exactly one rule,
`tools/lexicon/* -> tools/codebase-map/*`. `git ls-files 'tools/lexicon/*'` returns 14 files. A
script over `lexicon.extract` counts 548 graded imports repo-wide and 44 of them inside that FROM
glob, so `python tools/lexicon/lexicon.py --check` prints `P3 layer graded=548` for a judgeable
population of 44, overstating its reach by 12.5x on every run.
`git log -p --follow -- .lexicon.conf | grep '^+LAYER'` returns one pin value ever written, `"0"`,
across the 17 commits `git log --oneline -- .lexicon.conf` reports.

### Data model

The surviving constraint is not the deleted rule restated. The deleted rule was a declared,
glob-shaped, repo-relative direction that needed a glob dialect, a module index and an import
resolver to evaluate. The rule the repo actually relies on is narrower and needs none of them: the
lexicon kit ships self-contained, which is why `subtokens.py` is a port of a `codebase-map` function
rather than an import of it.

The replacement predicate reads, in full:

> Every non-relative import in a `.py` file sitting beside `lexicon.py` names either a stdlib
> top-level module or another `.py` file in that same directory.

It is stronger than the deleted rule, because it refuses any foreign kit rather than one named
directory. It carries no hand-kept name list, so there is nothing in it to rot. It resolves nothing
and globs nothing, so the two functions that carried every P3 defect in the kit's history have no
successor. It reads the kit's own directory through `Path(__file__).resolve().parent`, so it is
independent of the install prefix an adopter chose, which is the property `resolve_self_path`
already exists to buy.

It judges IMPORT STATEMENTS through `extract`, never file text. A whole-file text search is the
`memory/gotchas/absence-assertion-over-whole-file-text.md` class, and it would fire here on its own
documentation: the comment explaining why the ban exists must spell `codebase-map` to be readable,
and `tools/codebase-map/selftest.py` spells it while legitimately importing both kits.

Run over the real tree before wiring, as §7 requires. The predicate walks the 6 tracked kit modules,
judges all 44 of their imports, and returns zero offenders today. Staging `import map_lib` into any
of them makes it return one, because `map_lib` is in neither `sys.stdlib_module_names` nor the
sibling set `{canon, lexicon, lexicon_conf, scaffold_lexicon, selftest, subtokens}`. That is the
same 44 imports P3 could reach, now reported as 44 rather than as 548.

### Migration

`.lexicon.conf` loses three lines and one block. `lexicon_conf.load_conf` refuses an unknown block
header rather than ignoring it: with `LAYERS` gone from `BLOCK_KEYS`, the header falls through
`_BLOCK_RE` to `_SCALAR_RE`, matches neither, and raises `ConfError` at that line. That is the
correct behaviour and it is also why S8 is not optional in a later commit. The three
`tools/drift-audit/selftest.py` fixtures write `LAYERS:` into a fixture conf, `_load_lexicon`
swallows the `ConfError` into `None`, and every lexicon signal degrades to `not_asked` while the
arms asserting `gateable is True` fail. That leg's guard is `["tools/drift-audit/","tools/lib/"]`,
which a lexicon-only commit does not select, and its chunk is `selftests`, which the push bar holds.
The break is invisible to the push boundary in two independent ways, so it lands in this commit.

Deleting `lexicon-layer-waivers.txt` makes its basename a dead-path needle on the next run of the
unguarded `dead-path carriers` leg. `grep -rn lexicon-layer-waivers` finds five carriers outside
`memory/`: `tools/lexicon/kit.toml:26` and `tools/lexicon/selftest.py:84` are edited by S3 and S7,
and four spellings live in the frozen govkit receipt fixture, which S10 waives instead of editing.

### Rollout

One commit. There is no flag to hide a deletion behind and nothing to land dark: a predicate that
is gone cannot be half-gone, and the compensating refusal has to arrive in the same commit or the
constraint is unheld between them.

### Files touched (estimate)

`tools/lexicon/lexicon.py`, `tools/lexicon/lexicon_conf.py`, `tools/lexicon/selftest.py`,
`tools/lexicon/scaffold_lexicon.py`, `tools/lexicon/kit.toml`, `tools/lexicon/README.md`,
`tools/lexicon/LEXICON.md`, `tools/lexicon/lexicon-layer-waivers.txt` (deleted), `.lexicon.conf`,
`tools/drift-audit/selftest.py`, `tools/dead-path-waivers.txt`, `AGENTS.md` and
`coding-governance-agents.template.md`. Thirteen files, one of them a deletion.

### Alternatives rejected

**Keep P3 and fix its reach.** Rejected because there is nothing to fix. The rule is correct, the
resolver is correct after four review rounds, and the 12.5x overstatement is in the reporting line
rather than in the verdict. What is wrong is the ratio: 164 engine lines and 29 arms for one rule
whose pin has never moved off `"0"`.

**Move the constraint to a standalone `grep` on a new gate leg.** Rejected on the build README rule
that no new bar leg lands without a wall-clock ceiling and a `memory/project/testsuite-count-waivers.txt`
row, and on the research finding that the three lexicon leg definitions should keep their names,
argv, guards and ceilings so `tools/gate-legs.json` and the map's gate-legs inventory do not churn.
A grep is also the wrong instrument for the reason given under Data model.

**Charge the constraint to the kit self-test.** Rejected because `lexicon selftest` carries
`chunk = selftests`, `.githooks/pre-push` sets `GATE_FULL` and not `GATE_SELFTESTS`, and no boundary
sets the latter. A constraint held only there is not held at the push boundary at all.

## 5. Production-readiness checklist

- security — N/A. No new write path, no untrusted input, no egress. The new predicate reads tracked
  source the checker already reads.
- perf / scale — the deletion removes a repo-wide import resolution pass over 548 imports and adds a
  walk over 6 files. The `lexicon naming predicates` leg keeps its 300 s ceiling with headroom.
- a11y — N/A. A command-line checker with no user interface.
- i18n — N/A. No user-facing strings beyond the checker's own English diagnostics.
- error / empty / loading states — the new refusal must name the file, the line and the offending
  import target, because a refusal that says only "not self-contained" leaves the reader grepping.
- observability — the checker prints two predicate rows instead of three, and prints the
  self-containment population so a green row is a measurement rather than a mood.
- risks (concurrency, data-loss, rollback hazards) — the conf edit and the drift-audit fixture edit
  must ride the same commit or the neighbour kit is broken between them. Rollback is a revert; no
  data is migrated and no state is written.
- testing + left-shift gates — the new refusal gets its own self-test arms and an observed staged
  RED, per the build README rule that a new check is not landed until its failing case is seen.
- migration / rollback — covered under §4 Migration. Reversible by revert.
- user docs — `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` lose their P3 sections, and
  the §12 charter bullet loses its forbidden-import clause in both carriers.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --check` runs on the landed tree, it prints
  `P1 verb` and `P2 suffix` rows and no `P3 layer` row.
- **AC2** — When `import map_lib` is staged into any module under `tools/lexicon/`, the
  `lexicon naming predicates` leg REDS naming that file, that line and `map_lib`; when the file is
  unstaged, the same leg greens. Both states are observed and recorded, per the build README rule
  that a check is not landed until its failing case has been seen.
- **AC3** — When the self-containment refusal reports its population, it names `44` imports over the
  6 kit modules rather than the `548` the deleted `P3 layer graded=` row claimed.
- **AC4** — When `.lexicon.conf` is read after the edit, `grep -c LAYER .lexicon.conf` returns `0`
  and `python tools/lexicon/lexicon.py --measure` emits two pin lines rather than three.
- **AC5** — When `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, both `lexicon selftest`
  and `drift-audit selftest` are green with the three `LAYERS:` fixtures repaired.
- **AC6** — When `bash tools/check-dead-paths.sh` runs after `tools/lexicon/lexicon-layer-waivers.txt`
  is deleted, it exits 0, with the four govkit-receipt spellings covered by rows in
  `tools/dead-path-waivers.txt` and no other carrier left naming the file.
- **AC7** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs, the `lexicon wiring` leg is
  green, which asserts the rendered Skill still byte-compares after the kit descriptor lost its
  `lexicon-layer-waivers.txt` include row and its `lexicon-layers` hole.
- **AC8** — When `bash tools/check-template-size.sh` runs after the §12 bullet edit, it reports a
  byte count no larger than the pre-edit `48867`, because the charter had `285` free bytes and was
  already WARNing past its recorded high-water before this unit touched it.
- **AC9** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary, it is green,
  including the unguarded `dead-path carriers` and `testsuite counts` legs whose populations this
  unit moves.

## 7. Gates

`lexicon naming predicates` (the leg that carries the replacement refusal), `lexicon wiring`,
`lexicon selftest` and `drift-audit selftest` under `GATE_SELFTESTS=1`, `codebase-map kit selftest`
(its guard names `tools/lexicon/`), `dead-path carriers (deleted files still named)`,
`testsuite counts (every bar self-test prints one)`, the memory-tree hygiene leg, and
`bash tools/check-template-size.sh`. This unit adds no new gate leg and no new ceiling; it moves one
refusal into a leg that already exists.

## 8. Open questions

**F1 — does the self-containment refusal ship to adopters, or stay gov-local?**
The `lexicon naming predicates` leg's argv is `["python", "tools/lexicon/lexicon.py"]` with no mode
flag, so a check on that leg necessarily runs inside `run()` and therefore inside every adopter's
copy of the kit. Option A is exactly that: the kit asserts its own self-containment wherever it is
installed, which is true of every adopter and is the property the constraint was always about.
Option B keeps the assertion gov-local by giving the leg a second argv element or a wrapper script,
which changes a leg definition the research pass argued should not churn, and a wrapper script is a
new moving part needing its own declaration.
**Recommendation: option A.** The rule is a property of the kit, not of this repo, and an adopter
whose install has been edited to import a neighbour kit has broken the same thing gov would have.
It also costs no leg churn and no new declaration.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `d0a18683` with every figure re-measured on
  this worktree.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "assert that a kit's own source files do not import
another kit"` ranked `tracked_files` in `tools/lexicon/lexicon.py` as a fan-in 3 SEAM, alongside
`resolve_import` in the same file and the `absence-assertion-over-whole-file-text.md` gotcha key. The
seam this unit extends is therefore `tools/lexicon/lexicon.py`'s own extraction pair, `tracked_files`
plus `extract`: the replacement refusal reads import statements through `extract`, which already
returns the import list as its third element and whose signature is frozen by contract for
`drift_report.py`. Nothing new is built to reach imports. The gotcha key the same probe surfaced is
what rules OUT the obvious alternative, a whole-file text search for `codebase-map`, and is cited in
§4 Data model for that reason.

Recall terms used: `python tools/memory-recall/query.py "why was the lexicon import-direction
predicate P3 armed and what would removing it cost" --terms "lexicon LAYERS P3 import direction
predicate vacuous selector pin waiver codebase-map self-contained port"`. It returned 36 hits; the
load-bearing ones are the review finding that the only armed rule was unmatchable by construction
and its pin therefore unfalsifiable, and the spec record establishing that the forbidden direction
exists because the kit must ship self-contained and is the reason `subtokens.py` was ported rather
than imported.
