# TOOL-aSurfacedLexicon-9 — the owner-declarable PATTERNS block

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

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
- **S4** — Every read site takes the resolved mapping. Measured six of them in
  `tools/lexicon/lexicon.py`: `:244` inside `_probe_defs`, `:557`, `:726`, `:945`, `:999` and `:1081`.
- **S5** — `KNOWN_EXTS` stops deciding which languages an adopter may arm. It survives as the
  no-declaration fallback it already is at `tools/lexicon/lexicon.py:1072`, and the scaffold's language
  proposal keeps reading it (`tools/lexicon/scaffold_lexicon.py:39`, `:72`, `:74`, `:116`, `:126`,
  `:128`), but no armed path consults it to decide whether an extension may be graded.
- **S6** — A DEAD PROBE refusal. A declared pattern set that some `LANGS` row arms in `probe` mode,
  over an extension with at least one tracked file, yielding zero definitions across all of them,
  REDS by name.
- **S7** — An INERT DECLARATION report, distinct from DEAD PROBE, for a `LANGS` row naming an
  extension with zero tracked files. Without it a zero population satisfies the DEAD PROBE arm by
  accident and the refusal certifies nothing.
- **S8** — Regex validation at parse time: each row compiles, and carries exactly one capturing group.
  A row that fails either is a `ConfError` naming the file and line, never a skipped row.
- **S9** — A `tools/lexicon/selftest.py` fixture repo declaring a `ts` triple in `LANGS` plus two
  `PATTERNS` rows, exercising the green case, the offender case, and the DEAD PROBE case.

## 3. Non-goals (OUT)

- **No second shipped pattern set.** The kit keeps `js-regex` alone. `tools/lexicon/selftest.py:274`
  asserts `set(SENTINELS) == set(lex.PATTERN_SETS)`, so a shipped `ts-regex` owes a frozen sentinel
  fixture, and choosing TypeScript regexes on an adopter's behalf is exactly the ruling
  `TOOL-dScaffoldedMirror-13` defers to the owner who has that corpus. This unit ships the block and
  a commented example, not a set.
- **No `CELLS` rows for a newly armed language.** `TOOL-aSurfacedLexicon-4` owns the cell grammar and
  `TOOL-aSurfacedLexicon-6` owns the cell refusals. A language armed here with no cell declared is
  their UNDECLARED CELL refusal, not this unit's problem to pre-empt.
- **No real lexer for anything.** Shell stays dark under owner ruling Q5 and belongs to the shell
  parser unit.
- **No change to `extract` or `extract_text` signatures.** `tools/drift-audit/drift_report.py` derives
  both operands of `lexicon_marginal_offense_rate` through them against git blobs at two shas, so the
  contract is frozen. The resolved mapping reaches `_probe_defs` as an argument, not through a
  reshaped extractor signature.
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

### Inventory

The six `PATTERN_SETS` reads in `tools/lexicon/lexicon.py`, each with what it decides:

| Site | What it decides |
|---|---|
| `:244` | which regexes `_probe_defs` runs |
| `:557` | whether a declared pattern set exists at all, appended to `problems` |
| `:726` | which extensions count as armed for the coverage fraction |
| `:945` | whether `--suggest`'s coverage line reports an extension as gradeable |
| `:999` | the same test inside the second walk |
| `:1081` | the same test inside the third walk |

Three of those six are inside the duplicated corpus walks `TOOL-aSurfacedLexicon-3` collapses into one
`scan_corpus`. This unit is written against whichever count survives that landing; if the collapse has
landed first, the resolved mapping is threaded through `scan_corpus` alone and the inventory above is
smaller. The order verb puts this unit third, so the collapse is expected to be in place.

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
- `tools/lexicon/lexicon.py` — the resolver, the six read sites, the DEAD PROBE and INERT DECLARATION
  refusals.
- `tools/lexicon/scaffold_lexicon.py` — its `KNOWN` reads take the resolved mapping so a scaffold run
  in a repo that already declares patterns proposes against them.
- `tools/lexicon/selftest.py` — the fixture repo case and the three arms.
- `.lexicon.conf` — the commented `PATTERNS:` example and its boundary comment.
- `tools/lexicon/README.md` — the coverage-mode section gains the declared-set half.

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
  with no report. That is the unfiled review finding D25 named in the research record, and the build
  README already owes it a backlog row before the build starts. This unit widens the population it
  applies to and does not fix it.
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
  Skill needs no change: its `--suggest` routing does not name pattern sets. `--brief` is gone by the
  time this unit lands — `TOOL-aSurfacedLexicon-3` deletes it at build order 1 and leaves the Skill
  single-route — so this unit inherits one routing block, not two.

## 6. Acceptance criteria

- **AC1** — When a fixture repo declares `ts:ts-regex:probe` in `LANGS` plus `ts-regex.functions` and
  `ts-regex.types` rows under `PATTERNS:`, `python tools/lexicon/lexicon.py --check` grades its `.ts`
  definitions and reports a non-zero graded count for `ts`.
- **AC2** — When that fixture's `.ts` file gains a definition whose leading token is outside `VERBS`,
  the same command exits non-zero naming the file and line; when the definition is removed it exits 0.
  The RED is observed before the arm is called landed.
- **AC3** — When a `PATTERNS:` row declares a regex matching zero definitions across every tracked file
  of every extension its `LANGS` row arms, `python tools/lexicon/lexicon.py` exits non-zero printing
  `DEAD PROBE` and the pattern-set id; removing the row greens it.
- **AC4** — When a `LANGS` row arms an extension with zero tracked files, the run reports
  `INERT DECLARATION` and NOT `DEAD PROBE`, so an empty population cannot satisfy the DEAD PROBE arm.
- **AC5** — When no `PATTERNS:` block is declared, the resolved mapping compares equal to
  `lexicon.PATTERN_SETS`, asserted by a `tools/lexicon/selftest.py` arm.
- **AC6** — When a `PATTERNS:` row's regex carries zero capturing groups, or two, or fails to compile,
  `python tools/lexicon/lexicon_conf.py --print-rows PATTERNS .lexicon.conf` raises a `ConfError`
  naming the file and the line, rather than dropping the row.
- **AC7** — When a language is armed by adding a `LANGS` triple and its `PATTERNS` rows,
  `git diff --stat tools/lexicon/lexicon.py` for that change is empty, proving `KNOWN_EXTS` no longer
  gates which languages an adopter may arm.
- **AC8** — When `python tools/lexicon/selftest.py` runs against this repo with a `PATTERNS:` block
  declared in `.lexicon.conf`, the shipped-sentinel arm at `tools/lexicon/selftest.py:274` still passes,
  proving the merge did not mutate the shipped constant.
- **AC9** — When two rows name the same `<pset-id>.<part>` key, the reader raises rather than taking the
  last one, observed by staging the duplicate and reading the refusal from
  `python tools/lexicon/lexicon.py`.

## 7. Gates

- `lexicon naming predicates` — chunk `declarations`, subject `repo`, declared ceiling 300 in
  `tools/gate-legs.json`. This is the leg the push bar actually runs for this kit and the one the new
  refusals surface on.
- `lexicon wiring` — guard `[]`, ceiling 330. Fires on a conf-only diff, so the commented `PATTERNS:`
  example trips it until the Skill is re-rendered.
- `lexicon selftest` — chunk `selftests`, subject `kit`, ceiling 880. Reachable only under
  `GATE_SELFTESTS=1`; nothing at the push boundary runs it, which is why the three new arms are named
  in the acceptance criteria as observations rather than left to that leg.
- `codebase-map kit selftest` — its guard includes `tools/lexicon/`, so it selects itself on this diff.
- The memory-tree hygiene leg, for this spec.

No new bar leg, so no new wall-clock ceiling is owed. `tools/check-testsuite-counts.sh:35` derives its
population from the `*.test.sh` argv strings in `tools/gate-legs.json`, and `tools/lexicon/selftest.py`
is not one, so no `memory/project/testsuite-count-waivers.txt` row is owed either.

## 8. Open questions

- **Q4 is not open.** RESOLVED (owner, 2026-09-04): build the owner-declarable `PATTERNS:` block in
  this rebuild rather than deferring it.
- **F1 — does the kit ship a `ts-regex` set alongside the block, or only the block?** Shipping one
  gives the largest measured adopter population a working default on day one: 626 `.ts` and 572 `.tsx`
  files invisible today, armed coverage 1,190 of 6,168 tracked files at 19.3%, measured against
  `incms/main` on 2026-08-24 and recorded at `memory/backlog/TOOL.md:222`. Note that the review of that
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

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against the owner rulings of the same date.
- rev-2 · 2026-09-04 · cross-spec audit. S2 was a Scope (IN) item claiming the dotted and hyphenated
  row-key grammar that `TOOL-aSurfacedLexicon-4` S2 also claims; it is now written as the inherited
  prerequisite S1 already called it. §5 named `--brief` routing, which
  `TOOL-aSurfacedLexicon-3` deletes two build orders earlier.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "owner-declared regex pattern sets merged over shipped
extractor pattern sets"` ranks `extract` (`tools/lexicon/lexicon.py`, fan-in 7, marked SEAM) first,
and that is the seam this unit extends. Everything below it in the ranking is a different kit's
merge or extraction helper — `owners_of` in `tools/codebase-map/map_lib.py` at fan-in 3, `merge` in
`tools/settings-merge.py` at fan-in 2, and the four `extract_*` functions in
`tools/memory-recall/extract.py` — and none of them is reachable from the lexicon without reversing
the ratified map-reads-lexicon direction. `extract` dispatches on mode and reads the pattern set only
under `probe` (`tools/lexicon/lexicon.py:256-276`), so the resolved mapping enters at exactly one
argument and the extractor signature that `tools/drift-audit/drift_report.py` freezes by contract is
reached through a keyword rather than reshaped. The recall probe returned
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-13.md:54`, whose own reuse
audit ran the same lookup against the same seam at fan-in 9 and declined to touch it; this unit is the
ruling that spec was deferred for.

Recall terms used: `python tools/memory-recall/query.py "why are the lexicon extractor pattern sets
hardcoded in an engine-role file rather than declared" --terms "lexicon PATTERN_SETS KNOWN_EXTS LANGS
probe parser dark extension armed coverage adopter engine role kit.toml"`.
