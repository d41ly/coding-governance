# TOOL-aSurfacedLexicon-9 — the owner-declarable PATTERNS block

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 |

<!-- /gen:spec-records -->

## 1. Goal

Let an adopter arm a language the kit does not ship, by declaring its extraction regexes in
`.lexicon.conf` instead of editing an `engine`-role file an upgrade overwrites. Today `KNOWN_EXTS`
(`tools/lexicon/lexicon.py:102`) and `PATTERN_SETS` (`:108`) are both inside `tools/lexicon/lexicon.py`,
which `tools/lexicon/kit.toml:17-19` ships under `include = "**"` with `role = "engine"`, so a
TypeScript, Go, Rust or C# adopter can only write their language `dark` and the whole
vocabulary-and-convention apparatus then grades filenames or nothing. Owner ruling Q4 builds it now.

## 2. Scope (IN)

- **S1** — A `PATTERNS:` block key in `tools/lexicon/lexicon_conf.py`. Rows are
  `<pset-id>.<functions|types|imports>` followed by one Python regex. `BLOCK_KEYS` at
  `tools/lexicon/lexicon_conf.py:32` is the two-tuple `("VERBS", "LAYERS")` today, and `_parse_block`
  at `:99` has one arm per key with no generic default, so the widened tuple and the generic default
  parse from `TOOL-aSurfacedLexicon-4` are a hard prerequisite of this unit.
- **S2** — INHERITED, not built here: the row-key grammar that admits a dot and a hyphen is
  `TOOL-aSurfacedLexicon-4`'s generic `_parse_block` default, which applies no `.isalpha()` test. This
  unit only asserts the property it depends on. The `VERBS` arm refuses a non-alphabetic key at
  `tools/lexicon/lexicon_conf.py:105`, and every shipped pattern-set id is hyphenated (`js-regex`), so
  `js-regex.functions` is refused today by the reader that has to accept it. If that unit's default has
  not landed, this one does not land either — see S1.
- **S3** — One resolver returning the RESOLVED pattern-set mapping: the shipped `PATTERN_SETS` with
  declared rows merged over it, per pattern-set id and per part. It returns a new mapping and never
  mutates the module constant.
- **S4** — Every read site takes the resolved mapping, and the site set is DERIVED rather than
  assumed. `grep -rn 'PATTERN_SETS' --include='*.py' .` over this worktree returns eight decision
  sites in two files, plus the constant's own definition and one self-test assertion. Five of the
  eight survive build order 1 and are this unit's work. In `tools/lexicon/lexicon.py`: `:244` inside
  `_probe_defs` (which regexes run), `:557` inside `run` (whether a declared set exists at all) and
  `:726` inside `run` (which extensions count as armed for the coverage fraction) — or whatever
  `scan_corpus` holds in their place, since `TOOL-aSurfacedLexicon-3` S4 routes the surviving walks
  through it. In `tools/drift-audit/drift_report.py`: `:827` inside `signal_lexicon_verbs_unused`
  and `:890` inside `_build_armed_exts`, which feeds `lexicon_marginal_offense_rate`. Both of those
  test `pset not in lex.PATTERN_SETS` and `continue`, so a language armed only through `PATTERNS:`
  is skipped file by file while each signal reports a clean number with `live` still true from the
  Python half. That is green-by-absence on a GATED signal, and it is the same "both operands from
  one extractor" property §3 freezes the extractor contract to protect — defeated by the change that
  cites it, unless these two move with the rest.
- **S4a** — The three sites rev-2 also listed — `:945`, `:999` and `:1081` — are DELETED, not
  collapsed, and this unit threads nothing through them. An `ast` walk over
  `tools/lexicon/lexicon.py` puts `:945` and `:999` inside `run_brief` (`:916-1049`) and `:1081`
  inside `run_probe` (`:1053-1136`), and `TOOL-aSurfacedLexicon-3` S1 and S2 delete both functions
  outright at build order 1, two orders before this unit lands. Rev-2 called their fate a collapse,
  which tells an implementer to expect fewer sites rather than none of these three; a collapsed site
  still needs the mapping threaded through it and a deleted one needs nothing.
- **S5** — `KNOWN_EXTS` stops deciding which languages an adopter may arm. It survives as the
  no-declaration fallback it already is at `tools/lexicon/lexicon.py:1072`, and the scaffold's language
  proposal keeps reading it (`tools/lexicon/scaffold_lexicon.py:39`, `:72`, `:74`, `:116`, `:126`,
  `:128`), but no armed path consults it to decide whether an extension may be graded.
- **S6** — The DEAD PROBE arm's POPULATION widens to declared sets. The refusal itself already
  ships and this unit builds none of it: `tools/lexicon/lexicon.py:604-615` loops
  `sorted(declared.items())`, skips `mode == "dark"`, requires
  `any(ext_of(f) == ext for f in files)`, and appends `DEAD PROBE — .<ext> is declared <mode>` with
  the pattern-set id in parentheses. Read directly at this spec's base. What this unit adds is that
  a pattern set reachable ONLY through a declared `PATTERNS` row is inside that arm's population at
  all: today `:557` refuses such an extension before the arm can see it, with
  `LANGS declares pattern set … which this kit does not ship`, so the arm has never graded a
  declared set. Rev-2 wrote S6 as new work, which made its criterion satisfiable by unmodified
  engine code.
- **S7** — An `INERT DECLARATION` report, distinct from DEAD PROBE, for a `LANGS` row naming an
  extension with zero tracked files. Rev-2 justified it by a hole that does not exist — the shipped
  `any(ext_of(f) == ext for f in files)` guard ALREADY excludes a zero population from DEAD PROBE,
  so nothing satisfies that arm by accident. What it actually buys is the report that guard omits:
  an extension with no tracked files is skipped SILENTLY today, so a declaration arming a language
  the repo does not carry is indistinguishable from one grading it. That is the real gap and it is
  worth closing on its own terms.
- **S8** — Regex validation at parse time: each row compiles, and carries exactly one capturing group.
  A row that fails either is a `ConfError` naming the file and line, never a skipped row.
- **S9** — A `tools/lexicon/selftest.py` fixture repo declaring a `ts` triple in `LANGS` plus two
  `PATTERNS` rows, exercising the green case, the offender case, and the DEAD PROBE case. The
  fixture also declares its own `ts` `CELLS` rows, which costs nothing and makes it
  order-independent — see §3, and AC2.
- **S10** — Re-render the codebase map's generated artifacts in this same commit with
  `python tools/codebase-map/gen_map.py --write`. This unit adds one public module-level def to
  `tools/lexicon/lexicon.py` (§4 Identifiers minted), and a `json` read of
  `memory/map/generated/symbols.json` at this spec's base finds 34 rows for `tools/lexicon/`, 21 of
  them for `lexicon.py`, indexing every public def in it. The leg that re-derives that artifact,
  `codebase-map coverage + freshness`, carries NO `guard` key in `tools/gate-legs.json` — chunk
  `declarations`, subject `repo` — so it runs on every bar including the push boundary and a miss
  reds the push rather than waiting for a later run. Observed in §6 AC13. Copied from
  `TOOL-aSurfacedLexicon-3` S10 and `TOOL-aSurfacedLexicon-4` S11, which carry the identical
  obligation for the identical situation; this spec was the outlier.

## 3. Non-goals (OUT)

- **No second shipped pattern set.** The kit keeps `js-regex` alone. `tools/lexicon/selftest.py:274`
  asserts `set(SENTINELS) == set(lex.PATTERN_SETS)`, so a shipped `ts-regex` owes a frozen sentinel
  fixture, and choosing TypeScript regexes on an adopter's behalf is exactly the ruling
  `TOOL-dScaffoldedMirror-13` defers to the owner who has that corpus. This unit ships the block and
  a commented example, not a set.
- **No `CELLS` rows in THIS repo's declaration.** `TOOL-aSurfacedLexicon-4` owns the cell grammar
  and `TOOL-aSurfacedLexicon-6` owns the cell refusals, and this unit adds no cell to
  `.lexicon.conf`. The S9 fixture is the deliberate exception and declares its own `ts` cells.
  Rev-2 routed that case to a sibling that never mentions this fixture, and rev-3 then dated the
  harm wrongly. Read out of `TOOL-aSurfacedLexicon-6` rev-2 itself: its S1 makes an
  (extension, surface) pair with a non-empty population and no `CELLS` row `UNDECLARED CELL`, but
  its `### Rollout` lands that arm REPORT-ONLY at build order 4 behind a default-OFF constant,
  because three real pairs would otherwise red the commit that lands it. The promotion to a refusal
  is a later flip. So the fixture's `ts.function` population, non-empty by construction, is merely
  PRINTED at order 4 and reds only once the arm is promoted — later, not never. The rows are still
  owed and still cost one line each, the grammar is in place from build order 2, and they make the
  fixture independent of the promotion's order as well as of unit 6's. The cells declare the `snake`
  convention, matching the fixture's own definitions, so the arming moves no verdict whichever order
  `TOOL-aSurfacedLexicon-5` lands in. WHICH commit promotes the arm is NOT relied on here, because
  the two specs disagree: `TOOL-aSurfacedLexicon-6`'s Rollout hands the flip to
  `TOOL-aSurfacedLexicon-12` at order 7, and that spec at rev-4 carries no flip and no mention of
  `UNDECLARED CELL` — `grep -n 'flip\|promot\|default-OFF\|CELL'` over it returns nothing. That
  hand-off is those two units' to reconcile; it is reported, not patched from here.
- **No real lexer for anything.** Shell stays dark under owner ruling Q5 and belongs to the shell
  parser unit.
- **No RESHAPING of `extract` or `extract_text`.** `tools/drift-audit/drift_report.py` derives both
  operands of `lexicon_marginal_offense_rate` through them against git blobs at two shas and calls
  them POSITIONALLY, so the positional contract is frozen. The resolved mapping arrives as an
  optional keyword-only parameter defaulting to `None` and falling back to the shipped constant,
  which is what lets every existing positional call keep working unchanged while S4's two out-of-kit
  sites pass the resolution through. An adopter who never edits `drift_report.py` is on exactly
  today's behaviour by that default. Rev-2 said "no change to signatures" and then required the
  mapping to reach `_probe_defs` as an argument, which cannot both hold.
- **No prefix or decorator selector.** Owner ruling Q10 puts that in its own unit.

## 4. Design

### Data model

The block is rows of two fields. The first is `<pset-id>.<part>` where `<pset-id>` matches
`[A-Za-z0-9_-]+` and `<part>` is one of `functions`, `types`, `imports`. The rest of the row is one
Python regex, taken verbatim to end of line, and compiled with `re.M` exactly as the shipped sets are.
Two rows naming the same key are a refusal rather than a last-wins merge, because a duplicated key in
a hand-edited declaration is a typo far more often than an intent.

Merge is per key, not per set: a declared `js-regex.types` row replaces the shipped `types` list for
`js-regex` and leaves its `functions` and `imports` untouched. Replacement rather than append is the
choice that lets an adopter FIX a shipped regex, which is the case that motivates the block at all.
Every run PRINTS the replaced keys, per F2's own mitigation, so a set weakened rather than emptied is
visible rather than inferred. AC12 observes the merge and that line together, because a per-key merge
and a per-set replacement are indistinguishable on a declaration that only ever adds a NEW set.

### Inventory

The eight `PATTERN_SETS` decision sites, derived by
`grep -rn 'PATTERN_SETS' --include='*.py' .` over this worktree and each resolved to its enclosing
function by an `ast` walk. The constant's own definition at `tools/lexicon/lexicon.py:108`, the
docstring mention at `:132` and the sentinel assertion at `tools/lexicon/selftest.py:275` are not
decision sites and are excluded.

| Site | Enclosing function | What it decides | Fate at build order 1 |
|---|---|---|---|
| `lexicon.py:244` | `_probe_defs` | which regexes run | survives |
| `lexicon.py:557` | `run` | whether a declared set exists at all, appended to `problems` | survives |
| `lexicon.py:726` | `run` | which extensions count as armed for the coverage fraction | survives |
| `lexicon.py:945` | `run_brief` | the same membership test inside the `--brief` walk | DELETED |
| `lexicon.py:999` | `run_brief` | the same test inside its second walk | DELETED |
| `lexicon.py:1081` | `run_probe` | the same test inside the `--probe` walk | DELETED |
| `drift_report.py:827` | `signal_lexicon_verbs_unused` | the verb-usage population | survives |
| `drift_report.py:890` | `_build_armed_exts` | which extensions the offense rate spans | survives |

The three DELETED rows go with their functions: `TOOL-aSurfacedLexicon-3` S1 and S2 delete
`run_brief` (`:916-1049`) and `run_probe` (`:1053-1136`) outright at build order 1. Rev-2 described
them as collapsing into `scan_corpus` and hedged that "the inventory above is smaller"; they are not
smaller, they are absent, and the build's house style is to name the deletion — units 10 and 11 each
write it out. The three surviving lexicon-side sites may sit inside `scan_corpus` by the time this
unit lands, per `TOOL-aSurfacedLexicon-3` S4; this unit is written against the BEHAVIOUR each decides
rather than against a line number, so either shape satisfies it.

`tools/drift-audit/drift_report.py` was missing from rev-2 entirely, which is why S4 now derives its
site set repo-wide rather than reading one file.

### Identifiers minted

One public module-level def, run through the gate before it was written down, on
`TOOL-aSurfacedLexicon-3`'s practice.

| Identifier | Leading token | `python tools/lexicon/lexicon.py --suggest <name>` |
|---|---|---|
| `resolve_pattern_sets` | `resolve` | OK — the declaration carries it |

`build_pattern_sets` resolves too and the choice between them is taste; `resolve` was taken because
the function answers "what does this declaration resolve to", not "what new object does it make".
Because the verb is declared, the name adds no row to the verb offender count and does not move
`VERB_OFFENDER_PIN`, which has zero headroom at this base. The `PATTERNS` parse arm in
`tools/lexicon/lexicon_conf.py` is underscore-private and is neither graded by that pin nor indexed
by `symbols.json`.

### Migration

Nothing to migrate. This repo's `.lexicon.conf` declares no `PATTERNS:` block and gains only the
commented example that documents the capability, so the resolved mapping equals the shipped constant
and every count is unchanged. An adopter with no block is in the same position.

### Rollout

Purely additive and behind the declaration, so there is no flag to flip and nothing to land dark. The
capability is inert until an owner writes a row.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py` — `BLOCK_KEYS`, the generic default parse, the `PATTERNS` arm, the
  row-key grammar, the regex validation.
- `tools/lexicon/lexicon.py` — `resolve_pattern_sets`, the three surviving read sites, the widened
  DEAD PROBE population and the INERT DECLARATION report.
- `tools/drift-audit/drift_report.py` — the two membership tests at `:827` and `:890`, and the
  `lex.extract` / `lex.extract_text` calls beside them, which pass the resolved mapping by keyword.
- `tools/lexicon/scaffold_lexicon.py` — its corpus walk takes the resolved mapping so a scaffold run
  in a repo that already declares patterns measures against them. Its LANGUAGE PROPOSAL keeps
  reading `KNOWN_EXTS` (`:39`, `:116`), per S5: `KNOWN_EXTS` maps extension to pattern set and mode
  and is not the mapping being resolved. Rev-2 conflated the two.
- `tools/lexicon/selftest.py` — the fixture repo case and the three arms.
- `.lexicon.conf` — the commented `PATTERNS:` example and its boundary comment.
- `tools/lexicon/README.md` — the coverage-mode section gains the declared-set half.
- `memory/map/generated/` — regenerated by `python tools/codebase-map/gen_map.py --write` in the same
  commit, per S10, because one public def enters `symbols.json` and the leg that re-derives it is
  unguarded.

### Alternatives rejected

**Flipping `tools/lexicon/lexicon.py` to `role = "seed"`.** `tools/lexicon/kit.toml:25-28` documents
seed as copied once and thereafter owned by the target, so the flip would freeze an adopter's whole
engine at install and end kit upgrades. That is the same argument `TOOL-aSurfacedLexicon-11` makes
against the seed flip for `canon.py`, one file larger.

**Mutating `PATTERN_SETS` in place at load.** It reads as the smaller diff and it breaks the kit's own
liveness assertion: `tools/lexicon/selftest.py:274` compares `SENTINELS` against `lex.PATTERN_SETS` to
prove every SHIPPED set has a frozen fixture, and a declared set merged into that constant would red
that arm on any repo whose conf declares one. Shipped and resolved stay two names.

**Deriving the pattern set from the extension.** A one-to-one extension-to-regex mapping cannot express
two extensions sharing a set, which is the `.ts`/`.tsx` case the adopter measurement is about.

## 5. Production-readiness checklist

- security — an owner-authored regex runs over the owner's own tracked text under the owner's own uid,
  the same trust level the rest of `.lexicon.conf` already carries. The honest bound on a pathological
  pattern is the `lexicon naming predicates` leg's declared 300 s ceiling in `tools/gate-legs.json`,
  which reds rather than hanging. No regex-complexity analyser is built.
- perf / scale — one resolve per run, then the same walk. UNVERIFIED whether a second armed probe
  language measurably moves that leg; this repo tracks no third language to measure it with.
- a11y — N/A, no user interface.
- i18n — real and inherited. `tools/lexicon/subtokens.py` is ASCII-only, so a declared pattern set for a
  language with non-ASCII identifiers grades a truncated leading token and skips a fully non-ASCII name
  with no report. That gap is filed and OPEN as `TOOL-aSurfacedLexicon-16`, which names this unit by
  id as the one that measurably WIDENS the population it applies to. Rev-2 called it "the unfiled
  review finding" and directed a build-start filing that was already on disk when rev-2 was written;
  the row is the carrier and this bullet only points at it. This unit widens the population and does
  not fix it.
- error / empty / loading states — the two zero-population cases are the whole point of S6 and S7, and
  they are reported differently on purpose.
- observability — every declared pattern set appears in the per-run report with its resolved definition
  count, so a set that goes inert after landing is visible on the next run rather than at the next audit.
- risks (concurrency, data-loss, rollback hazards) — none beyond the shared-scalar hazard owner ruling
  Q2 already routed into the row-shaped `PINS:` block. Arming a new language moves pins, which is a
  visible diff by construction.
- testing + left-shift gates — the three new arms in `tools/lexicon/selftest.py`, each with its failing
  case observed before the arm is called landed.
- migration / rollback — deleting the block restores the shipped behaviour exactly, because the merge is
  a pure function of the declaration.
- user docs — the kit README's coverage-mode section and the conf's own commented example. The rendered
  Skill needs no change, and this is MEASURED rather than assumed: `render_skill()` in
  `tools/lexicon/adopt-lexicon.sh:95-123` substitutes `{{VERBS_TABLE}}` (from
  `lexicon_conf.py --print-rows`, which emits VERBS rows and nothing else), the three CLI tokens,
  `{{CONF}}` and `{{KIT_VERSION}}` — none of them moved by a pattern-set row. Appending the commented
  `PATTERNS:` example to a copy of this repo's conf and re-running `--print-rows` gives output
  byte-identical to the unmodified conf, 23 rows both times, so the byte-compare in `check_skill`
  stays green. §7 carried the opposite prediction and it was wrong. `--brief` is gone by the
  time this unit lands — `TOOL-aSurfacedLexicon-3` deletes it at build order 1 and leaves the Skill
  single-route — so this unit inherits one routing block, not two.

## 6. Acceptance criteria

- **AC1** — When a fixture repo declares `ts:ts-regex:probe` in `LANGS` plus `ts-regex.functions` and
  `ts-regex.types` rows under `PATTERNS:`, `python tools/lexicon/lexicon.py --check` grades its `.ts`
  definitions and reports a non-zero graded count for `ts`.
- **AC2** — When that fixture's `.ts` file gains a definition whose leading token is outside `VERBS`,
  the same command exits non-zero naming the file and line; when the definition is removed it exits 0.
  The RED is observed before the arm is called landed. The green half is asserted to hold with the
  fixture's `ts` `CELLS` rows declared (S9), which is what keeps it standing once
  `TOOL-aSurfacedLexicon-6`'s `UNDECLARED CELL` becomes a refusal. Read at that unit's rev-2, the
  refusal is NOT its own order-4 landing: its `### Rollout` lands S1 report-only behind a
  default-OFF constant and the promotion is a later flip, so an undeclared fixture cell is printed
  at order 4 and inverts this criterion only on the promoting commit. §3 carries that promotion's
  unsettled ownership.
- **AC3** — When a `PATTERNS:` row declares a regex matching zero definitions across every tracked
  file of every extension its `LANGS` row arms, `python tools/lexicon/lexicon.py` exits non-zero
  printing `DEAD PROBE` and the pattern-set id; removing the row greens it. The failing case
  observed here is the one this unit creates, and it is stated as such because the arm is shipped
  code: at this spec's base the same declaration cannot reach the arm at all — `:557` refuses the
  extension first with `LANGS declares pattern set … which this kit does not ship` — so a RED
  before and after would prove nothing. What is observed is that the exit is non-zero for the DEAD
  PROBE reason and NOT the unshipped-set reason, by the text of the refusal, and that the same
  declaration with a matching regex is green.
- **AC4** — When a `LANGS` row arms an extension with zero tracked files, the run reports
  `INERT DECLARATION` and NOT `DEAD PROBE`, so an empty population cannot satisfy the DEAD PROBE arm.
- **AC5** — When no `PATTERNS:` block is declared, the resolved mapping compares equal to
  `lexicon.PATTERN_SETS`, asserted by a `tools/lexicon/selftest.py` arm.
- **AC6** — When a `PATTERNS:` row's regex carries zero capturing groups, or two, or fails to compile,
  `python tools/lexicon/lexicon_conf.py --print-rows PATTERNS .lexicon.conf` raises a `ConfError`
  naming the file and the line, rather than dropping the row.
- **AC7** — When the fixture repo declares only the `LANGS` triple `ts:ts-regex:probe` and no
  `PATTERNS` rows, `python tools/lexicon/lexicon.py --check` exits non-zero with the shipped refusal
  naming the unshipped pattern set (`tools/lexicon/lexicon.py:557-558`). When the two `PATTERNS`
  rows are added and NOTHING ELSE changes, the same command grades the fixture's `.ts` definitions
  and counts its `.ts` files in the `coverage — armed N of M` line, which is site `:726`. Both states
  are observed. `git diff --stat tools/lexicon/lexicon.py` being empty across that change is a
  SUPPORTING clause, not the criterion: rev-2 asserted only the empty diff, which is true by
  construction of the edit whether or not `KNOWN_EXTS` still gates arming, so it observed nothing.
- **AC8** — When `python tools/lexicon/selftest.py` runs against this repo with a `PATTERNS:` block
  declared in `.lexicon.conf`, the shipped-sentinel arm at `tools/lexicon/selftest.py:274` still passes,
  proving the merge did not mutate the shipped constant.
- **AC9** — When two rows name the same `<pset-id>.<part>` key, the reader raises rather than taking the
  last one, observed by staging the duplicate and reading the refusal from
  `python tools/lexicon/lexicon.py`.
- **AC10** — When `python tools/drift-audit/drift_report.py` runs against a fixture declaring a
  `PATTERNS`-only language, that language's files are SEEN rather than skipped: the fixture's
  `ts` definitions contribute to `signal_lexicon_verbs_unused`'s used-verb set, and
  `_build_armed_exts` returns the `ts` extension so both operands of
  `lexicon_marginal_offense_rate` span it. Observed as a difference against the same fixture run
  with the `PATTERNS` rows removed, because a signal that reports the same clean number either way
  is the green-by-absence this criterion exists to catch. At this spec's base both sites test
  `pset not in lex.PATTERN_SETS` and `continue`, so the pre-change run is the failing case and it is
  free to stage.
- **AC11** — When `python tools/lexicon/scaffold_lexicon.py <dest-outside-the-repo>` runs against the
  same fixture, its measured pins are derived over the resolved mapping — the `ts` files are counted,
  not silently skipped — while `python tools/lexicon/lexicon.py --suggest <name>` answers
  byte-identically with the `PATTERNS` rows present and absent. The second half is asserted, not
  assumed: `run_suggest` reads the declaration and walks no corpus
  (`tools/lexicon/lexicon.py:785-852`), so it holds no pattern-set read after
  `TOOL-aSurfacedLexicon-3` deletes `run_brief` and `run_probe`, and a change in its output means an
  implementer wired a corpus read into the one subcommand whose whole value is not having one. Two
  subcommands, two claims: "the engine resolves it" and "every surface reads the resolution" are not
  the same statement.
- **AC12** — When this repo's own `.lexicon.conf` declares a `js-regex.types` row over the SHIPPED
  set, `python tools/lexicon/lexicon.py --check` shows the `.js` type population move off zero while
  the `.js` function population does not, and the run prints the replaced key. Measured at this
  spec's base by the shipped extractor over the 8 tracked `.js` files — `lex.extract(f, "probe",
  "js-regex")` summed across `lex.tracked_files(root)` gives 69 functions and 0 types, and the run
  itself prints `armed but grading nothing (reported, not a refusal): .js suffix=0` — so a per-key
  merge leaves 69 standing and a per-set replacement takes it to 0. That is the difference the
  criterion detects, and it is why the criterion declares over `js-regex` rather than over a new set
  the way AC1 does. Whichever way F2 resolves, it ships with this observation.
- **AC13** — The two artifacts the push bar re-derives without a guard are fresh on the landing
  commit. `python tools/codebase-map/test_codebase_map.py` is green and `memory/map/generated/` was
  rewritten by `python tools/codebase-map/gen_map.py --write` in that SAME commit, per S10; the STALE
  failure is observed FIRST, by staging `resolve_pattern_sets` without the regen, which prints
  `STALE symbols.json — regen: …` from `test_generated_artifacts_are_fresh`
  (`tools/codebase-map/test_codebase_map.py:128-147`). And `bash tools/lexicon/adopt-lexicon.sh
  --check` is green with the commented `PATTERNS:` example in place, which is the `lexicon wiring`
  leg's actual assertion on this diff — that the VERBS render is unaffected. §7 predicted a red
  there; the prediction was wrong and §5 records the measurement that settles it.

## 7. Gates

- `lexicon naming predicates` — chunk `declarations`, subject `repo`, declared ceiling 300 in
  `tools/gate-legs.json`. This is the leg the push bar actually runs for this kit and the one the new
  refusals surface on.
- `lexicon wiring` — chunk `wiring`, subject `repo`, guard `[]`, ceiling 330. Fires on a conf-only
  diff and is therefore the only leg that does. It asserts the rendered Skill byte-compares against a
  fresh render, and the commented `PATTERNS:` example moves nothing that render reads, so it stays
  GREEN and no Skill re-render is owed. Rev-2 predicted a red here; §5's measurement refutes it and
  AC13 observes the green.
- `lexicon selftest` — chunk `selftests`, subject `kit`, guard `['tools/lexicon/']`, ceiling 880.
  Reachable only under `GATE_SELFTESTS=1`; nothing at the push boundary runs it, which is why the new
  arms are named in the acceptance criteria as observations rather than left to that leg.
- `codebase-map kit selftest` — chunk `selftests`, subject `kit`, guard
  `['tools/codebase-map/', 'tools/lib/', 'tools/lexicon/']`, ceiling 300. Selects itself on this
  diff, and like the leg above is reachable only under `GATE_SELFTESTS=1`.
- `codebase-map coverage + freshness` — chunk `declarations`, subject `repo`, NO `guard` key, ceiling
  300. This is the one on the list that reds without a self-test flag and has no guard to scope it
  away: it byte-compares `memory/map/generated/` against a live re-derivation, and this unit adds a
  row to `symbols.json`. S10 regenerates in the same commit and AC13 observes it.
- `drift-audit selftest` — chunk `selftests`, subject `kit`, guard
  `['tools/drift-audit/', 'tools/lib/']`, ceiling 2300. S4's two out-of-kit sites select it, and it
  too is `GATE_SELFTESTS=1`-only.
- The memory-tree hygiene leg, for this spec.

This unit's DoD therefore runs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, because every
`chunk = selftests` leg above is invisible to the push bar and a green push would otherwise certify
arms it never ran.

No new bar leg, so no new wall-clock ceiling is owed. `tools/check-testsuite-counts.sh:35` derives its
population from the `*.test.sh` argv strings in `tools/gate-legs.json`, and `tools/lexicon/selftest.py`
is not one, so no `memory/project/testsuite-count-waivers.txt` row is owed either.

## 8. Open questions

- **Q4 is not open.** RESOLVED (owner, 2026-09-04): build the owner-declarable `PATTERNS:` block in
  this rebuild rather than deferring it.
- **F1 — does the kit ship a `ts-regex` set alongside the block, or only the block?** Shipping one
  gives the largest measured adopter population a working default on day one: 626 `.ts` and 572 `.tsx`
  files invisible today, armed coverage 1,190 of 6,168 tracked files at 19.3%, measured against
  `incms/main` and recorded in the backlog row `TOOL-dScaffoldedMirror-13`, cited by id because a
  line-keyed cite into a mutable shard unpins itself on the next insertion above it — the class
  `TOOL-aLoosenedCeiling-5` and `TOOL-dSpentCeiling-6` both ratified. Rev-2's line cite had already
  drifted onto a different record. Note that the review of that
  build corrected the denominator once already, so 19.3% is a tracked-file figure and not a
  definition-carrying one. Not shipping one keeps the kit honest about a language nobody here can
  measure, and keeps `tools/lexicon/selftest.py:274` from needing a sentinel whose regexes were guessed.
  Recommendation: ship the block only, and let the adopter with the corpus write the rows, which is what
  `TOOL-dScaffoldedMirror-13` was deferred for.
- **F2 — should a declared row be allowed to replace a SHIPPED set's part, or only add a new set?**
  Replacement is what lets an adopter fix a wrong shipped regex without waiting for a kit release. It
  also lets an adopter silently weaken `js-regex` into matching nothing, which the DEAD PROBE arm
  catches only when the result is zero and not when it is merely smaller. Recommendation: allow
  replacement, and print the replaced key on every run so the weakening is visible rather than
  inferred, on the same argument that makes the canon posture print in `TOOL-aSurfacedLexicon-11`.
  Whichever way this resolves, it ships with AC12, which declares over the SHIPPED `js-regex` set and
  observes both halves of the merge plus the replaced-key line. Rev-2 left this fork with no
  criterion at all, so per-key merge and per-set replacement were indistinguishable on every
  criterion the spec carried — a fork ratified and landed ungated.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against the owner rulings of the same date.
- rev-2 · 2026-09-04 · cross-spec audit. S2 was a Scope (IN) item claiming the dotted and hyphenated
  row-key grammar that `TOOL-aSurfacedLexicon-4` S2 also claims; it is now written as the inherited
  prerequisite S1 already called it. §5 named `--brief` routing, which
  `TOOL-aSurfacedLexicon-3` deletes two build orders earlier.
- rev-3 · 2026-09-04 · spec-audit round 1 folded, eleven findings. S4 is rewritten against what the
  tree will hold when this unit runs: three of the six read sites rev-2 named are DELETED with
  `run_brief` and `run_probe` at build order 1, not collapsed, and two sites in
  `tools/drift-audit/drift_report.py` were missed entirely — a language armed only through
  `PATTERNS:` was skipped there file by file while two gated signals reported clean numbers, which
  is the green-by-absence the frozen extractor contract exists to prevent. The §4 Inventory becomes
  an eight-row table with each site's enclosing function and its fate, and the extractor non-goal is
  restated as a frozen POSITIONAL contract with an optional keyword-only parameter, since rev-2
  forbade a signature change and then required an argument. S6 no longer claims to build the DEAD
  PROBE refusal, which ships with its pattern-set id and its zero-file guard, and S7 no longer rests
  on a hole that guard already closes; AC3 follows both. AC7 stops asserting an empty diff, true by
  construction of the edit, and observes the behaviour change instead. New S10 and AC13 regenerate
  `memory/map/generated/` in the same commit, matching the two siblings that already carry that
  obligation, and AC13 also gates the `lexicon wiring` green that §7 wrongly predicted as a red —
  measured through `render_skill`, which reads only VERBS rows. New AC10 covers the drift-audit
  sites, AC11 covers the scaffold and `--suggest` surfaces, and AC12 gates F2's per-key merge over
  the shipped `js-regex` set. AC2 and §3 make the S9 fixture declare its own `ts` cells so
  `TOOL-aSurfacedLexicon-6`'s `UNDECLARED CELL` cannot invert it at build order 4. §5's i18n bullet
  cites `TOOL-aSurfacedLexicon-16` instead of calling a filed OPEN row unfiled, §8 F1 cites
  `TOOL-dScaffoldedMirror-13` by id instead of by line, and §10 names the shipped refusal it
  extends. Header base re-pinned to the commit every figure in this rev was measured at.
- rev-4 · 2026-09-04 · round-2 fold, one defect: the fold text itself was unreviewed surface. §3 and
  AC2 justified the S9 fixture's own `ts` `CELLS` rows on a sibling mechanism that changed under
  them. Rev-3 read `TOOL-aSurfacedLexicon-6` S1 as a refusal at build order 4; that unit's rev-2
  `### Rollout` lands it REPORT-ONLY behind a default-OFF constant and promotes it to a refusal only
  by a later flip, so the stated mechanism was false. The rows survive on the corrected one — a
  refusal that arrives later still arrives, and the fixture cell is merely printed until it does —
  and both places now name the promotion instead of the landing. Neither place relies on WHICH
  commit promotes the arm, because the two siblings disagree: `TOOL-aSurfacedLexicon-6` hands the
  flip to `TOOL-aSurfacedLexicon-12` at order 7 and that spec at rev-4 carries no such scope item.
  That mismatch is reported to those two units rather than patched from a spec that owns neither
  file. Every other cross-unit claim was re-checked by opening the sibling at its current rev rather
  than by trusting this spec's summary of it: units 3, 4, 5 and 11, the `TOOL-aSurfacedLexicon-16`
  backlog row, and both `TOOL-dScaffoldedMirror-13` cites all hold as written. §10's "the same
  lookup" is corrected to the same tool onto the same seam, that spec's query string being a keyword
  list rather than this one's sentence.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "owner-declared regex pattern sets merged over shipped
extractor pattern sets"` ranks `extract` (`tools/lexicon/lexicon.py`, fan-in 7, marked SEAM) first,
and that is the seam this unit extends. Everything below it in the ranking is a different kit's
merge or extraction helper — `owners_of` in `tools/codebase-map/map_lib.py` at fan-in 3, `merge` in
`tools/settings-merge.py` at fan-in 2, and the four `extract_*` functions in
`tools/memory-recall/extract.py` — and none of them is reachable from the lexicon without reversing
the ratified map-reads-lexicon direction. The refusals already in the target file were enumerated
before any new one was designed, which is what S6 and S7 now rest on: `tools/lexicon/lexicon.py`
ships `UNDECLARED EXTENSIONS`, `STALE WAIVERS`, `DEAD PROBE` (with the pattern-set id and the
`any(ext_of(f) == ext for f in files)` guard, at `:604-615`) and `UNSELECTIVE RULE`, and its module
docstring names the last as the narrowest of the three vacuity checks. This unit adds ONE refusal
that does not exist there, `INERT DECLARATION`, and widens the population of one that does.
`extract` dispatches on mode and reads the pattern set only
under `probe` (`tools/lexicon/lexicon.py:256-276`), so the resolved mapping enters at exactly one
argument and the extractor signature that `tools/drift-audit/drift_report.py` freezes by contract is
reached through a keyword rather than reshaped. The recall probe returned
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-13.md:54`, whose own reuse
audit ran the same tool onto the same seam — `extract`, at fan-in 9 then — and declined to touch it;
this unit is the ruling that spec was deferred for. Its query string was a keyword list rather than
this one's sentence, which is why that clause reads "the same tool" and not "the same lookup".

Recall terms used: `python tools/memory-recall/query.py "why are the lexicon extractor pattern sets
hardcoded in an engine-role file rather than declared" --terms "lexicon PATTERN_SETS KNOWN_EXTS LANGS
probe parser dark extension armed coverage adopter engine role kit.toml"`.
