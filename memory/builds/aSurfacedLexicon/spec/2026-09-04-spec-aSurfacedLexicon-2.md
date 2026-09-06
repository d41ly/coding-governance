# TOOL-aSurfacedLexicon-2 — delete P3, keep its one real constraint

**Status:** CLOSED · rev-9 · 2026-09-06 · node a · Tier-2 · base 6c670b02 · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aSurfacedLexicon-2-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aSurfacedLexicon-2-acceptance-ledger.md) | journal | TOOL-aSurfacedLexicon-3 |
| [2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 |
| [2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round2.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 |
| [2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round1.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round1.md) | diff-review | TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 |
| [2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round2.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round2.md) | diff-review | TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 |

<!-- /gen:spec-records -->

## 1. Goal

Delete the import-direction predicate P3 from the lexicon kit and replace its single declared rule
with a self-containment refusal that judges the population P3 could actually reach. The predicate
costs 164 engine lines and 29 self-test arms to enforce one rule over 44 of the 557 imports its own
green line claims to grade — `python tools/lexicon/lexicon.py --check` prints
`lexicon: P3 layer  graded=557 offenders=0 waived=0` at this rev's base — and that pin has held the
value `"0"` across every commit it has ever had.

## 2. Scope (IN)

- **S1** — Delete the eight P3 engine functions from `tools/lexicon/lexicon.py`: `_build_glob_rx`,
  `_check_path_suffix`, `_glob_match`, `build_module_index`, `_resolve_relative`, `resolve_import`,
  `check_layer_violation` and `scan_unselective_rules`. Measured at 164 lines by AST spans over the
  file at writing time.

  **FOUR OF THESE MOVED RATHER THAN DIED, and a reader of this deletion is entitled to know it.**
  `build_module_index`, `_resolve_relative`, `_check_path_suffix` and `resolve_import` — this tree's
  only AST import resolver — were copied into `tools/codebase-map/map_imports.py` by
  `TOOL-dTracedLattice-6`, which the owner ratified on 2026-09-05 and which was built to land BEFORE
  this unit precisely so the capability would survive. It did not: this unit landed first, so the
  copy arrived into a tree where the original was already gone, and the rescue's parity arm now
  SKIPS with a named reason instead of comparing the two — which is its designed end state, one
  landing earlier than planned. `ext_of` is not on the list above and stays here; the codebase-map
  copy carries its own, spelled `derive_ext` because that directory is an armed layer for the naming
  gate and this one is not. So this deletion removed a capability that had already been carried
  elsewhere, and the arms covering those four are in `tools/codebase-map/selftest.py`. Nothing about
  this unit's decision changes.
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
- **S11** — Refresh `memory/map/features/lexicon.md`, the codebase map's own dossier for this
  feature, which describes P3 as a live predicate in five places this unit falsifies. `grep -nE
  'LAYERS|resolve_import|_glob_match|P3' memory/map/features/lexicon.md` returns eleven lines at
  this rev's base, covering four of the five. The fifth is the front-matter `title` field, which
  counts the kit's predicates in WORDS and so is reached by no such grep — one reason a criterion
  over this file has to be read rather than exit-coded. The other four are the third vacuity arm at
  `:90`; the reachability paragraph at `:92-100`, whose subject is the deleted resolver; the
  unarmed-predicate paragraph at `:109-111`, whose only example is the empty `LAYERS` block; and the
  two Gaps bullets at `:171-187` on the resolver's limits and on the two helper functions that
  carried every P3 defect. The title and the two present-tense paragraphs are rewritten to the
  two-predicate kit. The reachability and helper-function material is history the kit paid four
  blockers for, so it is kept and moved to the past tense naming P3 as deleted, rather than dropped
  — but no line may leave the dossier asserting a predicate, a rule shape or a resolver that no
  longer exists. The dossier's `claims` block is untouched: `armed-but-unreachable-rule.md` names a
  gotcha file this unit does not delete, so the claimed key stays live.
- **S12** — Run `python tools/codebase-map/gen_map.py --write` and commit the refreshed
  `memory/map/generated/symbols.json` in the SAME commit as S1. The map's symbol tier indexes every
  public module-level def, and four of S1's eight deletions are in that index today:
  `build_module_index`, `check_layer_violation`, `resolve_import` and `scan_unselective_rules`, all
  four carried with `file: tools/lexicon/lexicon.py` among the 21 rows the artifact holds for that
  file (counted by a `json` read of `memory/map/generated/symbols.json`). The artifact moves in both
  directions, because S6 adds one public def, `check_self_containment`, and one added row is as
  stale as four removed ones. `symbols.json` is the only generated artifact this unit moves: the
  same run renders `inventories.json` and `MAP.md` from the claim and inventory sets, which S1's
  deletions do not touch, and neither of those two carries a symbol row.

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
script over `lexicon.extract` counts 44 graded imports inside that FROM glob, while
`python tools/lexicon/lexicon.py --check` prints `P3 layer` with `graded=557` — a judgeable
population of 44 reported as 557, overstating its reach by 12.66x on every run. The `548` and
`12.5x` this spec carried at rev-1 were WRONG at this rev's base, not merely stale: the same
`--check` command produced both the old and the new figure, at `d0a18683` and at `6c670b02`.
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
same 44 imports P3 could reach, now reported as 44 rather than as 557.

**Four conditions bind the implementation.** The first three were ratified with the fork in §8 and
are repeated here because this is where the implementer reads; the fourth was added at rev-3 and is
not part of that ratification. First, the refusal is emitted as a refusal line and a population
line, never as a third `P<n> … graded=` row: a third row would contradict the §3 non-goal that
leaves the kit at two predicates and the observability line in §5. Second, it sits BELOW the NOT
ADOPTED return at `tools/lexicon/lexicon.py:478-480`, which keeps the inert-without-a-declaration
contract intact. Third, it dedupes on the top-level module name, because `_python_defs` emits both
`map_lib` and `map_lib._STOPWORDS` for `from map_lib import _STOPWORDS` and the population AC2 names
would otherwise read doubled.

Fourth, and this one pins a placement rather than a shape: the refusal is appended to the shared
`problems` list ABOVE the `measure_mode` return at `tools/lexicon/lexicon.py:669`, beside `DEAD
PROBE` at `:612` and `DEAD SNIFFER` at `:665`. Conditions two and four together fix the insertion
window to the span between `:480` and `:669`, and S6's "the `run()` check path" is not that window —
it reads equally as the `--check` branch below `:680`, where a refusal is reachable from `--check`
and unreachable from `--measure`. That is the armed-but-unreachable defect this file has now earned
three times, and its own comments confess to each one at `:624-632`, `:654-663` and `:738-745`:
every one of them was a refusal written below this return that a later review had to hoist above it.
No new exit plumbing is needed on the `--measure` side, because `:680` already returns `1` when
`problems` is non-empty; the whole cost of getting this right is which side of `:669` one
`problems.append` sits on. AC10 observes it differentially rather than by reading the diff.

**The refusal carries its own liveness assertion, because the thing it replaces existed to buy
one.** The `P3 NOT ARMED` refusal S2 deletes was the kit's written answer to a predicate that is
satisfied and a predicate that was never asked returning the same exit code. Its successor walks a
population it derives, and every derivation can come back empty for reasons that have nothing to do
with self-containment: an install layout where the tracked-file walk selects nothing beside
`lexicon.py`, or an extractor that stops returning imports. Zero offenders over zero imports is
exactly the clean green a broken probe prints. So the walk REDS when it judges zero imports, in the
`DEAD PROBE` token the engine already spells at `:612` and the neighbouring kits already read,
rather than in a second spelling invented here. That refusal joins `problems` under the same fourth
condition as the self-containment refusal itself, so `--measure` sees it too.

For that arm to be observable the population source has to be injectable, and this is the one place
the design constrains the code shape. `check_self_containment` takes the directory it walks as a
parameter defaulting to `Path(__file__).resolve().parent`, so a self-test arm can point it at an
empty temporary directory and watch it RED. A predicate that can only ever read its own installed
directory has a liveness arm nobody can stage, which is the same unfalsifiable shape one level up.
The name was checked before it was written: `python tools/lexicon/lexicon.py --suggest
check_self_containment` answers `OK — check_self_containment leads with 'check', which the
declaration carries`.

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
unguarded `dead-path carriers` leg. Re-derived at this rev's base rather than carried: `git grep -n
lexicon-layer-waivers -- . ':!memory/'` returns SEVEN lines across FOUR files, not the five carriers
rev-2 claimed under a command that produces no such number. Three of the seven are engine carriers
this unit edits — `tools/lexicon/kit.toml:26` (S3), `tools/lexicon/selftest.py:84` (S7), and
`tools/lexicon/lexicon.py:93`, the `WAIVER_FILES["layer"]` row, which S2 removes and which the rev-2
sentence never named. The remaining four are the receipt spellings at
`tools/govkit/fixtures/incms-2cff5855.receipt.json:128`, `:129`, `:597` and `:600`, which S10 waives
instead of editing. The plain `grep -rn` form rev-2 wrote reports an eighth match inside an
untracked `__pycache__` blob, which is why the tracked-only form is the one written here: the leg
reads tracked files, so an untracked hit is noise in the implementer's checklist.

### Rollout

One commit. There is no flag to hide a deletion behind and nothing to land dark: a predicate that
is gone cannot be half-gone, and the compensating refusal has to arrive in the same commit or the
constraint is unheld between them.

### Files touched (estimate)

`tools/lexicon/lexicon.py`, `tools/lexicon/lexicon_conf.py`, `tools/lexicon/selftest.py`,
`tools/lexicon/scaffold_lexicon.py`, `tools/lexicon/kit.toml`, `tools/lexicon/README.md`,
`tools/lexicon/LEXICON.md`, `tools/lexicon/lexicon-layer-waivers.txt` (deleted), `.lexicon.conf`,
`tools/drift-audit/selftest.py`, `tools/dead-path-waivers.txt`, `AGENTS.md`,
`coding-governance-agents.template.md`, `memory/map/features/lexicon.md` (S11, the dossier) and
`memory/map/generated/symbols.json` (S12, regenerated, never hand-edited). Fifteen files, one of
them a deletion and one of them generated.

### Alternatives rejected

**Keep P3 and fix its reach.** Rejected because there is nothing to fix. The rule is correct, the
resolver is correct after four review rounds, and the 12.66x overstatement is in the reporting line
rather than in the verdict. What is wrong is the ratio: 164 engine lines and 29 arms for one rule
whose pin has never moved off `"0"`.

**Move the constraint to a standalone `grep` on a new gate leg.** Rejected on the build README rule
that no new bar leg lands without a wall-clock ceiling and a `memory/project/testsuite-count-waivers.txt`
row, and on the research finding that the three lexicon leg definitions should keep their names,
argv, guards and ceilings so `tools/gate-legs.json` and the map's gate-legs inventory do not churn.
A grep is also the wrong instrument for the reason given under Data model.

**Charge the constraint to the kit self-test.** Rejected because `lexicon selftest` carries
`chunk = selftests` and no boundary sets `GATE_SELFTESTS`. The hook DECIDES whether to force
`GATE_FULL` and does not set it unconditionally, but that half does not matter here: `GATE_FULL`
bypasses GUARDS and never unlocks a `selftests` chunk, so the conclusion holds under either
reading and the conditional is stated only so the sentence is not reused as a fact about the hook. A constraint held only there is not held at the push boundary at all.

## 5. Production-readiness checklist

- security — N/A. No new write path, no untrusted input, no egress. The new predicate reads tracked
  source the checker already reads.
- perf / scale — the deletion removes a repo-wide import resolution pass over the 557 imports
  `python tools/lexicon/lexicon.py --check` reports at this rev's base, and adds a walk over 6
  files. The `lexicon naming predicates` leg keeps its 300 s ceiling with headroom.
- a11y — N/A. A command-line checker with no user interface.
- i18n — N/A. No user-facing strings beyond the checker's own English diagnostics.
- error / empty / loading states — the new refusal must name the file, the line and the offending
  import target, because a refusal that says only "not self-contained" leaves the reader grepping.
- observability — the checker prints two predicate rows instead of three, and prints the
  self-containment population so a green row is a measurement rather than a mood. PRINTING the
  population is not enough on its own: a printed zero is still a green, so the zero-population case
  REDS as `DEAD PROBE` per §4 Data model, and AC11 is the arm that observes it.
- risks (concurrency, data-loss, rollback hazards) — the conf edit and the drift-audit fixture edit
  must ride the same commit or the neighbour kit is broken between them. Rollback is a revert; no
  data is migrated and no state is written. The standing residual the §8 ratification surfaced lives
  here because no other section owns it: the replacement refusal is the kit's only UNWAIVABLE
  predicate. P1 and P2 both route through `load_waivers` against registries that ship with
  `role = "seed"`, and S3 deletes the third registry outright, so an adopter with a legitimate
  cross-kit import has no waiver route and must edit an engine file the next `govkit update`
  overwrites. No unit in this build owns that route, and this spec records it rather than resolving
  it.
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
- **AC3** — When the self-containment refusal reports its population ON THIS REPO, it names `44`
  imports over the 6 kit modules rather than the `557` the deleted `P3 layer graded=` row claimed.
  Both figures are GOV-SCOPED and this criterion is checkable here only: `44` comes from a
  `lexicon.extract` walk over the 14 files `git ls-files 'tools/lexicon/*'` returns on this tree, and
  `557` from `python tools/lexicon/lexicon.py --check` at this rev's base. An adopter's run
  reproduces neither number, so what travels with the kit is the SHAPE — a population line naming the
  imports and modules it actually judged — and not these two values.
- **AC4** — When `.lexicon.conf` is read after the edit, `grep -c LAYER .lexicon.conf` returns `0`
  and `python tools/lexicon/lexicon.py --measure` emits two pin lines rather than three.
- **AC5** — When `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, both `lexicon selftest`
  and `drift-audit selftest` are green with the three `LAYERS:` fixtures repaired.
- **AC6** — When `bash tools/check-dead-paths.sh` runs after the layer-waiver registry
  `lexicon-layer-waivers.txt` under `tools/lexicon/` is deleted, it exits 0, with the four
  govkit-receipt spellings covered by rows in `tools/dead-path-waivers.txt` and no other
  carrier left naming the file. The filename is spelled without its directory ON PURPOSE:
  `tools/check-spec-tokens.py` grades every backticked path-shaped token in this section
  against `git ls-files`, and this criterion's own subject is a path the unit DELETES, so the
  full spelling reds the unguarded `spec tokens` leg on the landing commit. A waiver row was
  the alternative and is worse: that registry's rows go stale when the spec citing them goes
  terminal, so it would red the moment this unit is marked done.
- **AC7** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs, the `lexicon wiring` leg is
  green, which asserts the rendered Skill still byte-compares after the kit descriptor lost its
  `lexicon-layer-waivers.txt` include row and its `lexicon-layers` hole.
- **AC8** — When `bash tools/check-template-size.sh` runs after the §12 bullet edit, it reports a
  byte count no larger than the pre-edit one AND still under the 48 KiB ceiling. The rev-1 pair
  `48867` / `285` free bytes was measured at `d0a18683` and is dead at this rev's base: the same
  command at `6c670b02` reports `49144 / 49152 bytes (8 under, 100.0%)`, and `wc -c <
  coding-governance-agents.template.md` agrees. So the headroom is EIGHT bytes, not 285, and this
  criterion is not a formality — the §12 edit must be net-neutral or net-negative in bytes or the
  `template size` leg REDS. **AND THE RENDERED HALF IS TIGHTER, which this criterion missed:** the
  charter is a rendered PAIR, and `bash tools/check-template-size.sh AGENTS.md` reports
  `64506 / 64512 bytes (6 under, 100.0%)`. Six is the binding margin, not eight, because a §12 edit
  lands in both carriers. This criterion covers BOTH. Re-read both figures from the command at build
  time; do not trust either number typed here. The leg also WARNs past its recorded high-water independently of the ceiling,
  and that warning is advisory and does not satisfy or fail this criterion.
- **AC9** — When this unit's pass is complete, the three UNGUARDED legs whose populations it moves
  are green ON THIS COMMIT, run directly: `dead-path carriers`, `testsuite counts` and
  `codebase-map coverage + freshness`. All three carry `chunk: declarations` and `subject: repo`
  with no `guard` key in `tools/gate-legs.json`, so nothing scopes them off this commit.
  **The WHOLE bar is deliberately NOT this criterion, and rev-7 removed that claim.** The full bar
  runs ONCE, at the push boundary, over the cumulative diff of every unit — so a per-unit criterion
  asserting it would be the same fact stated thirteen times, none of the thirteen observable when
  its own pass ends, and all thirteen satisfied or failed together by a run none of them controls.
  The run's Definition of Done already carries the whole-bar item and is where it belongs; this
  criterion carries only what this pass can actually observe.
- **AC10** — When `import map_lib` is staged into any module under `tools/lexicon/`, `python
  tools/lexicon/lexicon.py --check` and `python tools/lexicon/lexicon.py --measure` BOTH exit `1`
  and both name that file, that line and `map_lib`; when it is unstaged both exit `0`. The two
  refusal sets are compared as sets, not spot-checked: a refusal visible to one mode and not the
  other fails this criterion even when the leg is green, which is the only way to observe the fourth
  binding condition without reading the diff. Baseline for the unstaged half, measured at this rev's
  base: both modes exit `0` today, `--measure` printing three pin lines and `--check` printing its
  predicate rows.
- **AC11** — When `check_self_containment` is pointed at a directory holding no `.py` files, or at
  one whose modules yield no imports, the run REDS with a `DEAD PROBE` refusal naming the empty
  population, and the same refusal is present in `--measure` output. The failing case is STAGED and
  OBSERVED before the arm lands, per the build README rule. A run that prints a zero and exits `0`
  on an empty population fails this criterion: that outcome is indistinguishable from a satisfied
  predicate, which is the distinction the deleted `P3 NOT ARMED` refusal was bought to keep.
- **AC12** — When `grep -nE 'LAYERS|resolve_import|_glob_match|P3' memory/map/features/lexicon.md`
  runs on the landed tree, every surviving hit is in a past-tense sentence naming P3 as DELETED, and
  the front-matter `title` no longer counts three predicates. A hit that reads as a description of a
  live predicate, a live rule shape or a live resolver fails this criterion. Nothing on the bar
  catches this — the freshness leg grades claimed KEYS and not dossier prose — so this criterion is
  the only observation there is, and it is checked by reading the command's output rather than by
  its exit code.
- **AC13** — When `python tools/codebase-map/gen_map.py --write` has run in the landing commit,
  `python tools/codebase-map/test_codebase_map.py` passes `test_generated_artifacts_are_fresh` at
  that commit, and `memory/map/generated/symbols.json` contains no row for `build_module_index`,
  `check_layer_violation`, `resolve_import` or `scan_unselective_rules` while carrying one for
  `check_self_containment`. Both halves are needed: the freshness assert alone passes on a
  hand-edited artifact, and the row check alone passes on an artifact stale in some other feature.
  The baseline is measured: at this rev's base that command reports all five of its checks `ok` in
  about two seconds, so a RED on the landing commit is attributable to this unit and not inherited.

## 7. Gates

`lexicon naming predicates` (the leg that carries the replacement refusal), `lexicon wiring`,
`lexicon selftest` and `drift-audit selftest` under `GATE_SELFTESTS=1`, `codebase-map kit selftest`
(its guard names `tools/lexicon/`), `dead-path carriers (deleted files still named)`,
`testsuite counts (every bar self-test prints one)`, `codebase-map coverage + freshness` (unguarded,
and S1's four public deletions plus S6's one addition move the artifact it byte-compares), the
memory-tree hygiene leg, and `bash tools/check-template-size.sh`. This unit adds no new gate leg and
no new ceiling; it moves one refusal into a leg that already exists.

## 8. Open questions

### F1 — does the self-containment refusal ship to adopters, or stay gov-local?
The `lexicon naming predicates` leg's argv is `["python", "tools/lexicon/lexicon.py"]` with no mode
flag, so a check on that leg necessarily runs inside `run()` and therefore inside every adopter's
copy of the kit. Option A is exactly that: the kit asserts its own self-containment wherever it is
installed, which is true of every adopter and is the property the constraint was always about.
Option B keeps the assertion gov-local by giving the leg a second argv element or a wrapper script.
The case against B is NOT leg churn, which is what rev-1 rested it on and is wrong: a flagged leg is
already precedented, since `lexicon wiring` carries
`["bash", "tools/lexicon/adopt-lexicon.sh", "--check"]` in both `tools/gate-legs.json` and
`tools/lexicon/kit.toml`. B falls on the governance-carrier edit instead. The flag has to land in
`tools/gate-legs.json`, which is the merge bar's leg manifest, and the kit descriptor cannot follow
it, because adopters read the descriptor's argv while gov's bar reads the manifest. A wrapper script
is a new tracked `tools/` path that the govkit surface registry reds until a declaration claims it.
**Recommendation: option A.** The rule is a property of the kit, not of this repo, and an adopter
whose install has been edited to import a neighbour kit has broken the same thing gov would have.

**RESOLVED (agent, 2026-09-04, delegated): F1 — option A, the self-containment refusal runs inside
`run()`, on the existing `lexicon naming predicates` leg, and ships with the kit.**

Both forms of option B fall to veto 2, a change to a governance carrier. B-flag needs a second argv
element in `tools/gate-legs.json`, the merge bar's leg manifest, and the kit descriptor cannot
follow: adopters receive the DESCRIPTOR's argv while gov's bar reads `gate-legs.json`, and the
descriptor-vs-manifest parity check compares leg NAME and SUBJECT and nothing else, so the
divergence would survive precisely in the field no guard reads. B-wrapper adds a depth-1 `tools/`
path that `tools/govkit/registry.toml` reds until an `[[exempt]]` row or a descriptor claim lands,
and a wrapper moved inside `tools/lexicon/` dodges that glob only by being auto-claimed by
`include = "**"`, shipping to adopters and defeating the gov-local intent that was its only reason
to exist. Independently, a standalone wrapper must re-implement extraction or import the kit from
outside it.

A is the sole survivor and is not itself vetoed, so this is a ratification and not a park. It trips
no rung: no new dependency, no new tracked path, no new install location, no new public surface (an
existing mode's verdict, not a new flag), no carrier edit, and it is read-only. It is also the
richest survivor. It satisfies AC2 as measured — the predicate names file, line and target, and
`run(root, False, False)` is the leg's default dispatch — plus AC3 on gov's tree (44 imports over 6
kit modules; a staged `import map_lib` returns exactly one offender), AC7 and AC9. Deliverability is
the argument the spec did not make and it is the strongest: `TOOL-aFlaggedScaffold-3` records that
`govkit update` cannot land a source gov newly ships, measured on the one real adopter whose kit
died with `ModuleNotFoundError` for six days under a green bar. A rides inside `lexicon.py`, which
already has a receipt row, so it reaches adopters through the normal upgrade path.

Three conditions bind the pick. The refusal is emitted as a refusal/population line and never as a
third `P<n> … graded=` row, or it breaks the §3 non-goal that leaves the kit at two predicates and
contradicts §5's observability line. It sits BELOW the NOT ADOPTED return at `lexicon.py:478-480`,
keeping the inert-without-a-conf contract intact. It dedupes on the top-level module name, because
`_python_defs` emits both `map_lib` and `map_lib._STOPWORDS` for `from map_lib import _STOPWORDS`
and AC2's wording would otherwise read doubled.

Residual, not a veto: A ships the kit's only UNWAIVABLE predicate. P1 and P2 route through
`load_waivers` against registries that ship `role = "seed"`, and S3 deletes the third, so an adopter
with a legitimate cross-kit import has no waiver route and must edit an engine the next `govkit
update` clobbers. That route is unowned by any unit in this build.

## 9. Revision log

- rev-9 · 2026-09-06 · S1 gains the pointer `TOOL-dTracedLattice-6` S4 requires and its AC4 grades:
  four of the eight functions are now in `tools/codebase-map/map_imports.py`, so a reader of this
  deletion is not told a capability was removed. Added at the merge that brought that build in,
  which landed AFTER this one rather than before — the ordering the rescue was specced to guarantee
  did not hold, and the note says so rather than implying it did. Nothing else in this spec changed
  and this unit's decision is untouched.

- rev-1 · 2026-09-04 · initial draft, written against `d0a18683` with every figure re-measured on
  this worktree.
- rev-2 · 2026-09-04 · F1 ratified as option A (the refusal runs inside `run()` on the existing
  leg and ships with the kit), with three binding conditions: a population line rather than a third
  `P<n>` row, placement below the NOT ADOPTED return, and a dedupe on the top-level module name.
  Those three now sit in §4 Data model as well as in the §8 mark, because that is where the
  implementer reads. §8's case against B corrected — a flagged leg is not unprecedented
  (`lexicon wiring` already carries `["bash", "tools/lexicon/adopt-lexicon.sh", "--check"]` in both
  carriers), so B falls on the governance-carrier edit, not on leg churn. The `548` / `12.5x` pair
  was WRONG, not merely stale: `python tools/lexicon/lexicon.py --check` prints `graded=557` at this
  rev's base, a 12.66x overstatement of the judgeable 44, and §1, §4, §5 and AC3 now carry that.
  AC3's `44` and `6` recorded as gov-scoped figures an adopter's run does not reproduce. The adopter
  waiver route for the new refusal recorded in §5 as unowned by this build. Header base re-pinned
  from `d0a18683` to `6c670b02`, the commit every figure in this rev was measured at.
- rev-3 · 2026-09-04 · spec-audit fold, four findings. Two scope items added: S11 refreshes the
  codebase map's own dossier for this feature, which described the deleted predicate in five places
  no gate reads, and S12 regenerates `memory/map/generated/symbols.json` in the landing commit,
  because four of S1's eight deletions and S6's one addition move rows in an artifact the unguarded
  `codebase-map coverage + freshness` leg byte-compares. Both files added to §4 Files touched, which
  is now fifteen rather than thirteen, and that leg named in §7 and in AC9. A FOURTH binding
  condition added to §4 Data model, pinning the refusal above the `measure_mode` return rather than
  merely below the NOT ADOPTED one, since S6's "the `run()` check path" also reads as the branch
  below it — the placement this file's own comments confess to getting wrong three times — with AC10
  observing `--check` and `--measure` refusal sets as equal. The replacement refusal given the
  liveness assertion the deleted `P3 NOT ARMED` refusal used to buy: a zero-import population REDS
  in the engine's existing `DEAD PROBE` token, the walk root becomes a parameter so the arm can be
  staged, and AC11 observes it. §4 Migration's dead-path count re-derived: the tracked-only grep
  returns seven lines across four files, not five carriers, and `lexicon.py:93` joins the two engine
  carriers the paragraph already named. New criteria AC10 through AC13.
- rev-4 · 2026-09-04 · the pre-push hook DECIDES whether to force a total run rather than setting `GATE_FULL=1`
  unconditionally, so the alternatives note no longer states it as a fact about the hook. The
  conclusion it supported is unchanged: `GATE_FULL` bypasses guards and never unlocks a
  `selftests` chunk.
- rev-5 · 2026-09-05 · AC8 extended to the RENDERED charter. The pair is byte-capped on both sides and the
  rendered one is TIGHTER — `bash tools/check-template-size.sh AGENTS.md` reports six free bytes
  against the template's eight — so a §12 edit measured only on the template can still red the bar.
- rev-6 · 2026-09-05 · §8’s fork became a `###` sub-head. Both machine readers count a fork as a bullet or a
  `###` sub-head, and this section led its fork with a bold run-in, so the section scored ZERO items —
  which routes to the empty-section branch and reads FORKED however conforming the resolution mark is.
  The mark was always there; nothing could see it.

- rev-7 · 2026-09-05 · AC6's path token de-backticked to a bare basename plus a separate directory
  token, and the reason written into the criterion. No other change: the criterion's subject,
  witness command and exit condition are byte-identical in meaning. Found by running the
  unguarded `spec tokens` leg during the build pass, which was green at this rev's base and
  red on the unit's own tree — the leg §7 of this spec does not name.
- rev-8 · 2026-09-05 · AC9 narrowed from the whole bar to the three unguarded legs this unit's own
  commit moves. The full bar runs once, at the push boundary, over every unit's cumulative diff, so
  a per-unit criterion claiming it is one fact restated once per unit and observable by none of
  them when their pass ends; the run's Definition of Done already owns it. Written during this
  unit's build pass, which is when the criterion turned out to be unobservable by the pass it
  belongs to.

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
