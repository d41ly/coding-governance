# TOOL-aSurfacedLexicon-4 — the CELLS and PINS declaration grammar

**Status:** SPECCED · rev-8 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 |
| [2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round2.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 |

<!-- /gen:spec-records -->

## 1. Goal

Widen `.lexicon.conf`'s block grammar so the (language, surface) matrix and the per-cell pins can be
declared at all. Today `tools/lexicon/lexicon_conf.py` accepts exactly two block keys and refuses any
row key carrying a dot, so `py.function` cannot be written down. Every later unit in this build reads
its cell from this grammar, and the owner's Q2 ruling makes the row-shaped pin block load-bearing
rather than convenient.

## 2. Scope (IN)

- **S1** — `BLOCK_KEYS` at `tools/lexicon/lexicon_conf.py:32` gains `CELLS` and `PINS`. The container
  initializer at `:56` is `{k: ({} if k == "VERBS" else []) for k in BLOCK_KEYS}`, a two-way
  conditional over a tuple that will hold four keys; it becomes a per-key mapping so a new block key
  costs one row rather than an edit to a conditional.
- **S2** — `_parse_block` becomes a keyed dispatch with `_parse_rows` as its default. Read against
  source rather than assumed: today the function has exactly ONE keyed arm, `if key == "VERBS"` at
  `tools/lexicon/lexicon_conf.py:100`, whose alphabetic refusal is `:106`; the glob-pair code below
  it at `:110-117` is the unconditional FALL-THROUGH, not a `LAYERS` arm. `grep -n 'key =='
  tools/lexicon/lexicon_conf.py` returns that one line and no other. So there is no `LAYERS` branch
  to preserve, and an implementer told to keep
  one would have to invent it. After `TOOL-aSurfacedLexicon-2` S5, which removes `LAYERS` from
  `BLOCK_KEYS` at `:32` and deletes that fall-through, there is no arrow code either. This unit adds
  `CELLS` and `PINS` arms and makes `_parse_rows` — `<row-key> <rest>` split on the first run of
  whitespace, returning an insertion-ordered `dict` — the default. The generic path applies no
  `.isalpha()` test, which is what admits a dotted row key.
- **S2's ordering, stated with its difference rather than claimed away.** This unit is order 2 and
  `TOOL-aSurfacedLexicon-2` is order 1, so the fall-through is expected to be gone before S2 runs.
  If the orders invert, S2 still lands, because a keyed dispatch with a default subsumes a
  fall-through — but the arrow code then becomes the `LAYERS` arm rather than the default, and
  `TOOL-aSurfacedLexicon-2` S5 deletes an arm instead of a branch. That is the whole delta; it is
  not order-INDEPENDENT and rev-4 said it was.
- **S3** — the `CELLS` row grammar: `<ext>.<surface>  <convention> [vocab] [notail]`. `surface` is
  the closed set `function`, `type`, `file`, `constant`. `convention` is the closed set `snake`,
  `screaming`, `camel`, `pascal`, `kebab`, `dark`. A row naming a surface or a convention outside
  those sets is a refusal naming the file and line, never a skip.
- **S4** — the `PINS` row grammar: `<ext>.<surface>.<predicate>  <count>`, where `predicate` is the
  closed set `debt`, `unruled`, `suffix`, `conv`, and `count` must parse as a non-negative decimal
  integer. A count that does not parse is a refusal.
- **S5** — two cross-block declaration refusals, both owned here because both are answerable from the
  declaration alone with no corpus walk. A `CELLS` row naming an extension absent from `LANGS` reds.
  A `PINS` row naming a cell absent from `CELLS` reds. `check_declaration` is called from the TAIL of
  `load_conf`, not from a verdict path in `lexicon.py`, so every one of the module's four readers
  refuses identically — including `tools/lexicon/adopt-lexicon.sh --check`, which shells out to
  `lexicon_conf.py --print-verbs` at `:218` and sets `fail=1` on a non-zero rc. That placement is
  what puts these refusals on an UNGUARDED leg, and it is the reason §3's guard non-goal costs so
  little. Measured on this worktree: appending an unknown `FOO:` block to `.lexicon.conf` and running
  `bash tools/lexicon/adopt-lexicon.sh --check` exits 1 naming the line, and exits 0 once the block
  is removed — a conf-only edit, refused by the reader, on a leg with an empty guard.
- **S6** — `lexicon_conf._main`'s `--print-rows` takes an optional block key, so
  `tools/lexicon/adopt-lexicon.sh` can read the matrix through the one reader. Today `--print-rows`
  takes only the conf path and hardcodes `VERBS` at `:174-178`. Omitting the key keeps today's
  behaviour, so no existing caller changes.
- **S7** — the concurrency property Q2's ruling depends on: two branches each draining a different
  cell's pin must merge clean. The mechanism is the fork in §8; the property is in scope either way,
  and its regression arm is `AC5`.
- **S8** — STRUCK at rev-5, number retained so no cross-reference dangles. It widened the
  `lexicon naming predicates` guard to include `.lexicon.conf`; that edit reds an unguarded leg on
  every bar and the lexicon kit's own descriptor already refused it in writing. §3 carries the
  ruling, §4 Alternatives carries the measurements. S10 buys the property S8 was reaching for
  without touching a manifest.
- **S9** — the two-sided pin equality itself, at `tools/lexicon/lexicon.py:697`. Q2's ruling is that a
  count which FALLS reds exactly as one that rises does, so `if len(unwaived) > pin:` becomes an
  inequality against the declared count in both directions. The message distinguishes the two
  directions, because they call for opposite actions: a rising count names the new offenders, and a
  falling one prints the exact replacement row to paste. This unit owns the operator because it owns
  the pin rows the operator reads, and because S7's concurrency property is only worth having if a
  falling count is something the bar actually notices.
- **S9's prose carriers, which S9 makes wrong.** Four tracked files state the pin rule one-sidedly
  and all four say the SAME thing, which is the opposite of what rev-4's AC10 asserted. Measured:
  `grep -n 'never rise' .lexicon.conf tools/lexicon/lexicon-*-waivers.txt` returns four lines —
  `.lexicon.conf:29` and `:2` of each of the three `lexicon-*-waivers.txt` files — every one of them
  reading that the count may fall and never rise. S9 makes a fall red too, so all four sentences
  become false on the commit that lands it. This scope item rewrites them to the two-sided wording.
  Three of the four are kit files an adopter receives on the next `govkit update`, which is why they
  cannot be left for a later unit.
- **S10** — the `PINS` row separation ratified as fork F1 becomes a REFUSAL in the reader rather than
  a convention in a selftest fixture. `_parse_pins` receives its rows as `(lineno, body)` pairs —
  `_parse_block`'s caller builds them that way at `tools/lexicon/lexicon_conf.py:80` — so "no two
  `PINS` rows adjacent" is a one-loop test over line numbers already in hand, with no raw-text
  re-read and no new plumbing. Two rows whose line numbers differ by one is a refusal naming both.
  Because it lives inside `load_conf`, it fires for every reader of the tracked declaration, on the
  unguarded leg S5's note names. A comment line between two rows also satisfies it, since the block
  scanner drops `#` rows from `rows` while still advancing the counter — which is why rev-4's
  unballoted option (d) measures identically to (c) here as well.
- **S11** — regenerate `memory/map/generated/` in the same commit. `check_declaration` is a new
  public module-level def in a tracked `.py` file, which `tools/codebase-map/map_lib.py` indexes into
  `memory/map/generated/symbols.json`, and the leg that byte-compares that artifact against a live
  re-derivation carries no `guard` key at all. Measured: appending a two-line `check_declaration` to
  `lexicon_conf.py` and running `python3 tools/codebase-map/test_codebase_map.py` prints
  `FAIL test_generated_artifacts_are_fresh` and `STALE symbols.json`; removing it returns rc 0. The
  regen is `python tools/codebase-map/gen_map.py --write`. The unit's other six minted identifiers do
  not land: `grep -c lexicon_conf.py memory/map/generated/symbols.json` returns 4 today, and reading
  those four rows they are the module's public classes and defs. The module declares no `__all__`, so
  the three `_parse_*` helpers are excluded as leading-underscore and the three constants as plain
  module-body assignments.

## 3. Non-goals (OUT)

- The convention predicate itself. Six regexes, set membership and stemming are
  `TOOL-aSurfacedLexicon-5`. This unit only declares which cell asks for which convention.
- The `UNDECLARED CELL` and `DEAD CELL` refusals, and the per-cell coverage report. Those need a
  corpus walk to know a population size and belong to the cell-refusal unit.
- Draining any pin to its true count. S9 changes what the comparison DECIDES, not what the counts
  are. A cell whose declared count is wrong on the day S9 lands reds until someone edits the row,
  which is the ratchet working rather than a defect in it. The seven Python filename offenders Q3
  pinned are the worked example, and draining them is the rename unit Q3 filed.
- The pin rows' initial VALUES. `TOOL-aSurfacedLexicon-7` emits the whole `PINS` block from a measured
  run once the debt and unruled split exists, so authoring counts here would be a second carrier for a
  number another unit derives.
- The `PATTERNS` block, the `CANON` block and the `expanded` stamp. Each is its own unit and each
  rides the generic `_parse_block` default this unit adds, which is the point of making it generic.
- Renaming the seven hyphenated Python basenames. Q3 ruled they ship pinned as their own unit.
- Any change to the `VERBS` block's parsed shape. `tools/codebase-map/map_extractors.py:139-168`
  reads it through `load_conf` and the `lexicon-verbs` inventory holds 23 keys; both stay untouched.
- **Widening the `lexicon naming predicates` leg guard to cover `.lexicon.conf`.** This was rev-1
  through rev-4's S8 and it is now refused, on prior art this design pass should have read: the
  lexicon kit's own descriptor at `tools/lexicon/kit.toml` already rules it out in prose, directly
  above the `[[gate_leg]]` block it governs. The reasoning, in this spec's words rather than quoted:
  `tools/govkit/govkit.py` partitions every guard pathspec in the manifest into exactly one of five
  declared classes, and a root-level conf is in none of them, so declaring one reds `govkit selfcheck`
  instead of scoping anything. Widening that taxonomy is an edit to a second kit's contract, which is
  not a cost this unit is buying. **The compensating note, because an exemption is not coverage.**
  What the narrow guard loses is an early signal, and the loss is BOUNDED rather than absent — the
  bound is the hook's, not this spec's. Read against source rather than assumed:
  `.githooks/pre-push` DECIDES whether a total run is owed. It exports `GATE_FULL=1` only when no
  recorded full green covers the pushed tip, when that green is not an ancestor of it, when it is
  further behind the tip than the source constant at `.githooks/pre-push:184` allows (`grep -n
  'GATE_FULL_MAX_LAG=' .githooks/pre-push` returns `GATE_FULL_MAX_LAG=10`), when its tree
  fingerprint does not reproduce at the sha it names, when the tip is a merge whose second parent
  the record cannot speak for, when the leg manifest moved, or when the push runs the kit self-tests
  against a green earned with them held. On any other default-branch push it exports `GATE_BASE`
  instead and every guard is evaluated, so a conf-only diff skips `lexicon naming predicates` at the
  push boundary too. Rev-5 wrote the opposite here — that the hook sets `GATE_FULL=1` and the
  authoritative run stays total — and that is the behaviour the hook RETIRED, as its own comment at
  `:163-171` and `tools/run-gates/run-gates.sh:140` both say. What the narrow guard actually costs
  is an early signal for at most that many commits, never a permanent blind spot, and here it costs
  nothing at all: S5 places the declaration refusals inside `load_conf`, where `lexicon wiring`
  reaches them with an empty guard, so a conf-only commit is refused on the bar whichever way the
  hook decides.

## 4. Design

### Data model

`load_conf` returns one flat dict. Two new keys join it, both insertion-ordered so a printed block
round-trips in declaration order.

| Key | Parsed shape | Refusal cases |
|---|---|---|
| `CELLS` | `{"py.function": ("snake", frozenset({"vocab"}))}` | unknown surface, unknown convention, unknown flag, duplicate row key, extension absent from `LANGS` |
| `PINS` | `{"py.file.conv": 7}` | unknown predicate, non-integer count, duplicate row key, cell absent from `CELLS`, two rows on consecutive lines |

The row key is kept verbatim as the dict key rather than exploded into a tuple. A string key is what
lets `--print-rows` emit the block for bash without a second grammar, and it is what lets a pin row
be `grep`-able by the exact text an owner typed. Callers that need the parts split them at the dots
themselves, which is one expression and no new contract.

The two cross-block refusals in S5 run after the whole file is parsed, because `LANGS` may be
declared below `CELLS` and a reader that refuses on line order refuses a legal file.

Row SEPARATION inside the `PINS` block is a merge property rather than a formatting preference. Fork
F1 is ratified as option (c), one blank line between rows. The reader is indifferent to it when
PARSING — blank lines inside a block are skipped rather than treated as terminators, verified at
`lexicon_conf.py:73-75` — which is exactly why the property needs S10's refusal to hold: a reader
that cannot tell a separated block from a dense one cannot notice the day someone tidies the gaps
shut. S10 makes the separation a thing the grammar REQUIRES rather than a thing a fixture remembers.

### Inventory

Identifiers this unit mints, each with the cell that grades it once
`TOOL-aSurfacedLexicon-5` lands.

| Identifier | Cell | Role |
|---|---|---|
| `_parse_rows` | `py.function` | the generic `<row-key> <rest>` default |
| `_parse_cells` | `py.function` | `CELLS` row validation |
| `_parse_pins` | `py.function` | `PINS` row validation |
| `check_declaration` | `py.function` | the two cross-block refusals of S5 |
| `SURFACES` | `py.constant` | the closed surface set |
| `CONVENTIONS` | `py.constant` | the closed convention set |
| `PIN_PREDICATES` | `py.constant` | the closed predicate set |

`check` is the declared verb for "assert a predicate and return a verdict" and `_parse_*` follows the
`parse` row, so no name here needs a `--suggest` consultation. `SURFACES`, `CONVENTIONS` and
`PIN_PREDICATES` are public module-body simple assignments, which is the population Q6 armed
`py.constant` on, so all three are graded rather than excluded.

### Why `dot` is a classifier form and not a declarable convention

`TOOL-aSurfacedLexicon-5` ships six regexes and this unit's `CONVENTIONS` set holds five plus `dark`.
The sixth form, `dot`, exists so that a dotted name is reported as satisfying something rather than
falling into the AMBIGUOUS bucket, and so a violation message can name what the name does satisfy. No
language convention is "identifiers contain dots", so a declarable `dot` cell would be a cell nothing
could sensibly be written for. The two sets are deliberately different sizes and the refusal message
for `dot` says so in words rather than reporting it as an unknown token.

### Migration

`.lexicon.conf` today declares `VERBS`, `LANGS`, `BANNED_SUFFIXES`, three `*_OFFENDER_PIN` scalars and
a `LAYERS` block. This unit adds two blocks and removes nothing, so a declaration that has not been
rewritten yet parses exactly as it does now: the new blocks are absent, and an absent block key
resolves to its empty container. The conf rewrite that pastes the real `CELLS` and `PINS` bodies is a
later unit. That ordering is deliberate. It means the grammar can land, be gated and be reverted
without any predicate depending on the rows yet existing.

`tools/drift-audit/selftest.py` writes three fixture declarations carrying `LAYERS` blocks at `:734`,
`:814` and `:890`. This unit widens `BLOCK_KEYS` and removes nothing from it, so those fixtures keep
parsing. The unit that deletes `LAYERS` owns that breakage, which is why this one does not touch it.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/lexicon/lexicon_conf.py` | `BLOCK_KEYS`, the `:56` initializer, `_parse_block` dispatch plus three row parsers, `check_declaration`, `--print-rows <key>` |
| `tools/lexicon/lexicon.py` | the two-sided pin comparison at `:697` (S9). NOT the call site for `check_declaration` — S5 puts that at the tail of `load_conf`, so every reader inherits the refusal |
| `tools/lexicon/selftest.py` | red and green fixtures per refusal in S3, S4, S5 and S10, plus the merge arm of AC5 |
| `.lexicon.conf` | the one-sided pin sentence at `:29` rewritten two-sided (S9) |
| `tools/lexicon/lexicon-verb-waivers.txt` | the one-sided pin sentence at `:2` rewritten two-sided (S9) |
| `tools/lexicon/lexicon-suffix-waivers.txt` | same sentence, same line (S9) |
| `tools/lexicon/lexicon-layer-waivers.txt` | same sentence, same line (S9) — deleted outright if `TOOL-aSurfacedLexicon-2` has landed first, in which case this row drops |
| `memory/map/generated/` | regenerated by `python tools/codebase-map/gen_map.py --write` in the same commit (S11) |
| `tools/gate-legs.json` | NOT touched — S8 struck, see §3 |
| `.gitattributes` | NOT touched — F1 ratified option (c), which changes nothing outside `.lexicon.conf` |
| `tools/lexicon/README.md` | the block grammar paragraph |

ESTIMATE, and marked as one because nothing comparable ships: no case-style or matrix declaration
exists in the kit to measure against. Reader work is bounded by the shape rather than guessed —
`_SCALAR_RE` at `:34` and `_BLOCK_RE` at `:35` need no change at all, because `_BLOCK_RE` already
accepts any identifier-shaped block header and the gate that rejects `CELLS:` today is the
membership test at `:67`, not the regex.

### Alternatives rejected

- **A second parser in `adopt-lexicon.sh`.** Refused for the reason the file's own docstring gives at
  `:5-7`: two hand-written parsers for one file is this repo's two-answers-to-one-question class, and
  a closing review already found the Skill render carrying its own inline parser that disagreed with
  this one on a gloss containing a colon. S6 is the cheaper half of that lesson.
- **One scalar per cell**, in the shape of today's `VERB_OFFENDER_PIN`. Q2's ruling makes this
  unbuildable: a scalar cannot reconcile additively, and the ruling names the row-shaped block as the
  mitigation. It is also the shape whose pin moved eleven times without producing a rename.
- **Keying `PINS` on the cell with a nested predicate map**, so a row reads `py.function debt=43
  unruled=373`. Rejected because it packs three drains onto one line, which is precisely the adjacent
  edit that conflicts. One drain per line is the whole concurrency property of S7.
- **Reusing `tools/memory-tree/row_grammar.py`.** It is the anchor grammar for markdown index rows and
  its subject is id uniqueness within a file, not a key-value conf block. Nothing in it reads an
  indented conf row.
- **Widening the leg guard to `.lexicon.conf` — rev-4's S8, now refused twice over.** Prior art this
  design pass missed and should not have: the ruling is written in prose in `tools/lexicon/kit.toml`,
  a file this very unit edits, immediately above the `[[gate_leg]]` block for the leg in question.
  Measured on this worktree rather than taken from it — stage the guard entry and run
  `python tools/govkit/govkit.py selfcheck`: it exits 1 with `guard pathspec '.lexicon.conf' … falls
  into 0 declared classes`, and exits 0 with the entry removed. The leg it reds carries no `guard`
  key of its own, so it runs on every bar including the push boundary; §5's rev-4 claim that S8
  "changes when a leg runs and not what runs" was false.
- **The same widening, in the SECOND carrier as well.** A separate reason S8 dies, and it would have
  bitten even if govkit had allowed it. The identical guard array lives in `tools/gate-legs.json` and
  in `tools/lexicon/kit.toml`'s `[[gate_leg]]` block, and no shipped check compares them: govkit's
  descriptor-vs-manifest parity arm compares leg NAME, SUBJECT and CHUNK and never `guard` —
  `grep -c '"guard"' tools/govkit/govkit.py` returns 6, and reading all six they sit in the
  class-partition arm, the emitter and the placeholder-token scan, none in a parity comparison. A
  one-carrier widening therefore diverges in
  silence, gov's bar reading the wide guard while every adopter keeps the narrow one. That is the
  exact failure mode `TOOL-aSurfacedLexicon-2` §8 used to veto its own option B.
- **Routing `.lexicon.conf` through `tools/govkit/registry.toml`'s `[[exempt]]` list** so the guard
  falls into the `exempt` class. This one MEASURES clean and is rejected on meaning, not mechanics:
  with an exempt entry and the widened guard both staged, `python tools/govkit/govkit.py selfcheck`
  exits 0. But that list holds paths gov deliberately does NOT ship, and `.lexicon.conf` is the one
  file every adopter authors for itself. The entry would buy an early signal by writing a false
  sentence into a registry whose whole value is that its sentences are true.

## 5. Production-readiness checklist

- security — N/A. The declaration is a tracked file read by tools already running as the operator, and
  this unit adds no path resolution, no network call and no write.
- perf / scale — the two new blocks are parsed once per run over a file whose current length is 216
  lines. The cross-block refusals of S5 are two set-difference passes over the declared rows, not over
  the corpus, so they cost nothing measurable against the `lexicon naming predicates` ceiling of 300 s.
- a11y — N/A. No user interface.
- i18n — N/A for the grammar. The known adjacent gap is `subtokens.py` being ASCII-only, filed by the
  research record as an unfiled review finding needing its own backlog row; this unit adds no new
  exposure to it because a row key is compared, never tokenized.
- error / empty / loading states — every refusal names the file, the line and the offending text, in
  the shape `ConfError` already uses. An absent block resolves to its empty container and is legal,
  which is what keeps a not-yet-rewritten declaration parsing.
- observability — the parsed cell and pin counts are printed by the engine's declaration line, so a
  block that silently parsed to nothing is visible rather than inferred.
- risks (concurrency, data-loss, rollback hazards) — the concurrency risk is the whole of fork F1 and
  is measured in §8 rather than asserted. Rollback is a revert of the module, the four prose carriers
  S9 rewrites and the regenerated map artifacts, and touches no manifest at all now that S8 is
  struck; no declaration is required to carry the new blocks.
- testing + left-shift gates — every refusal in S3, S4, S5 and S10 gets a red fixture and a green
  fixture in `tools/lexicon/selftest.py`, and each red is observed before the unit is called done. No
  new bar leg is added and no existing leg's guard, argv or ceiling changes, so the build rule about
  ceilings and `memory/project/testsuite-count-waivers.txt` rows is not triggered. What DOES change is
  which legs a conf-only diff reaches, and it changes without a manifest edit: S5 and S10 put their
  refusals inside `load_conf`, which `lexicon wiring` reaches with an empty guard.
- migration / rollback — covered under `### Migration`. Additive in both directions.
- user docs — `tools/lexicon/README.md` gains the block grammar paragraph. The rendered Skill is
  compared byte-for-byte by the `lexicon wiring` leg, whose guard is empty, so a placeholder change
  reds until re-rendered.

## 6. Acceptance criteria

- **AC1** — When a declaration containing `CELLS:` with the row `py.function snake vocab` is parsed,
  `python tools/lexicon/lexicon_conf.py --print-rows CELLS <conf>` prints that row. Measured before
  the change on this worktree, the same file raises `not a KEY=VALUE line, a KEY: block header, or a
  comment: 'CELLS:'`, and a dotted key under `VERBS:` raises `a verb must be alphabetic, got
  'py.function'`.
- **AC2** — When a `CELLS` row naming an extension absent from `LANGS` is staged,
  `python tools/lexicon/lexicon.py --check` REDS naming that extension and that line number; when
  the row is unstaged it greens. The red is observed and recorded before this unit is called done.
  **The observation is the COMMAND, not the leg, and the difference is the one §3 and §7 just
  established.** `lexicon naming predicates` carries a guard of `tools/`, `skills/session-kickoff/`,
  `.githooks/` and `.claude/`, so a conf-only stage SKIPS it and a criterion phrased against that
  leg could never observe its own red — the same shape as the six criteria round 1 found that could
  not fail. On the bar the conf reaches an unguarded leg through `lexicon wiring`, which shells out
  to `adopt-lexicon.sh --check` and therefore to `load_conf`; S10 is what puts this refusal on that
  path.
- **AC3** — When a `PINS` row carries a non-integer count such as `py.file.conv seven`, `load_conf`
  raises `ConfError` naming the line; when it carries `7` it parses to the integer `7`.
- **AC4** — When a block header that is not in `BLOCK_KEYS` appears, for example `FOO:`,
  `load_conf` still raises rather than silently accepting it. This is the regression arm on S1:
  widening the tuple must not make every identifier-shaped header legal.
- **AC5** — When two branches off one base each drain a different pin row and are merged, `git merge`
  exits 0 with no conflict markers in `.lexicon.conf`, including for two ADJACENT cells. This is a
  standing selftest arm that performs the merge, not a one-time observation. **What it does NOT
  observe, stated rather than left to be discovered:** the arm writes its own separated fixture, so
  it merges clean however dense the TRACKED declaration becomes, and it can never red on the
  tidying-edit hazard F1 identified. That hazard is AC11's, and AC11 is the criterion that can
  actually fail on it. **The merge measurement is UNVERIFIABLE against the live declaration and says
  so**: `grep -n "PINS" .lexicon.conf` exits 1 printing nothing, so there is no block in the tree
  today and the arm and every figure behind it run over a SYNTHESIZED block. With that block dense
  and no attribute set, the adjacent case exits 1 with one conflict marker while a four-row
  separation exits 0; under F1 option (c) the adjacent case exits 0.
- **AC5's scope limit, written rather than left implicit.** This criterion covers DRAIN against DRAIN
  only. A drain against an INSERTION after the same row still exits 1 with one conflict marker under
  option (c), measured on the same synthesized block, and insertion is the shape every cell-arming
  commit produces and the shape §3 hands to `TOOL-aSurfacedLexicon-7` when it emits the whole `PINS`
  block. No insert arm is owed here. The obligation this unit hands off instead is that whichever
  unit emits the block emits it blank-separated, so no cell-arming commit ever authors a dense pair.
- **AC6** — When a `PINS` row names a cell with no `CELLS` row, `python tools/lexicon/lexicon.py
  --check` REDS naming that cell; when the `CELLS` row is added it greens.
- **AC7** — REMOVED at rev-5 along with the scope item it observed. It required the
  `lexicon naming predicates` leg to run on a conf-only commit, which is reachable only by the guard
  widening §3 now refuses. The number is retained and struck rather than reused, so nothing that
  cites AC7 lands on a different criterion. Its property is not orphaned: AC11 and AC12 observe a
  conf-only commit reaching the bar through `lexicon wiring`, whose guard is already empty.
- **AC8** — When the widened reader is in place, the neighbour inventory is unchanged and the
  neighbour signals are still live. Two commands, both run at spec time on this worktree, both
  printing something that would differ if the contract broke.
  `python -c "import sys; sys.path.insert(0,'tools/codebase-map'); import map_extractors; print(len(map_extractors.all_inventories()['lexicon-verbs']))"`
  prints `23`. Rev-4 named `python tools/codebase-map/map_extractors.py` here, which is not an
  observation at all: that module has no `__main__` block, so it exits 0 printing nothing whether the
  count is 23, 0 or the dict is empty, and the criterion passed unconditionally. Second half:
  `python tools/drift-audit/drift_report.py --json` still reports its three `lexicon_`-prefixed
  signals with `live` true rather than `not_asked`.
- **AC9** — When `python tools/lexicon/lexicon_conf.py --print-rows <conf>` is run with no block key,
  it prints the `VERBS` rows exactly as it does today, so `bash tools/lexicon/adopt-lexicon.sh
  --check` finds the rendered Skill unchanged.
- **AC10** — When a pin row's declared count is one ABOVE the measured count, `python
  tools/lexicon/lexicon.py --check` REDS naming that cell and printing the exact replacement row;
  when it is one BELOW, it REDS naming the new offenders. Both directions are observed as real reds
  before this unit is called done, and both are standing selftest arms. This is the arm that proves
  Q2 landed, and its premise is now the one the carriers actually state. Measured on this worktree:
  `tools/lexicon/lexicon.py:697` is `if len(unwaived) > pin:`, which IS the one-sided ratchet the
  conf and the three waiver headers describe — the RISE is guarded and implemented. What is
  unguarded is the FALL, and rev-4 asserted the reverse. Staged and observed: editing
  `VERB_OFFENDER_PIN` from `"461"` to `"462"` against a measured 461 leaves
  `python tools/lexicon/lexicon.py --check` at rc 0. S9 makes that case red and S9's carrier item
  rewrites the four sentences that currently promise it will not.
- **AC11** — When two `PINS` rows are written on consecutive lines in the TRACKED `.lexicon.conf`,
  `bash tools/lexicon/adopt-lexicon.sh --check` exits 1 naming both line numbers; when one blank line
  separates them it exits 0. This is the criterion AC5 cannot be: its input is the tracked file, not
  a fixture the arm wrote, so a later tidying edit that closes the gaps reds the bar. The seam is
  observed rather than assumed — staged today by appending an unknown block header to
  `.lexicon.conf`, that command exits 1 with `lexicon-adopt: .lexicon.conf does not parse`, and exits
  0 once the block is removed, which is a conf-only edit refused through `load_conf` on a leg whose
  guard is empty. The red is observed before this unit is called done.
- **AC12** — When `check_declaration` is added, `python3 tools/codebase-map/test_codebase_map.py`
  exits 0 on the commit that adds it, because `python tools/codebase-map/gen_map.py --write` ran in
  the same commit. The failing case is observed first: with the new def in place and the artifacts
  unregenerated, the same command prints `STALE symbols.json` and exits non-zero, which was staged
  and seen at spec time.

## 7. Gates

- `lexicon naming predicates` — the leg that runs the engine's declaration verdict, chunk
  `declarations`, subject `repo`, ceiling 300 s. Its guard is UNCHANGED by this unit, per §3, and no
  new leg is added anywhere.
- `lexicon wiring` — chunk `wiring`, subject `repo`, guard empty, ceiling 330 s. It byte-compares the
  rendered Skill AND parses the declaration through `lexicon_conf.py`, so it fires on a conf-only
  diff. It is where AC9's regression surfaces and, because S5 and S10 place their refusals inside
  `load_conf`, where AC11 and the cross-block refusals surface too. This is the leg that carries the
  early signal §3's non-goal declines to buy from the manifest.
- `codebase-map coverage + freshness` — chunk `declarations`, subject `repo`, NO guard key at all, so
  it runs on every bar including the push boundary. `check_declaration` is a new public
  module-level def and lands in `memory/map/generated/symbols.json`, which this leg byte-compares
  against a live re-derivation. AC12 is its arm and S11 is the work.
- `lexicon selftest` — chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, ceiling 880 s.
  Carries every red and green fixture above. It is invisible to the push bar, which sets no
  `GATE_SELFTESTS`, so this unit's Definition of Done runs `GATE_SELFTESTS=1 bash
  tools/run-gates/run-gates.sh` explicitly rather than relying on the push boundary.
- `codebase-map kit selftest` and `drift-audit selftest` — both chunk `selftests`. AC8 is the arm that
  makes their neighbour contracts observable from this unit rather than at some later push.
- The memory-tree hygiene leg, for this spec and the records this unit writes.

## 8. Open questions

**F1 — what actually makes two branches draining different cells merge clean?**

Q2's ruling was first written with a merge-driver mitigation named as already present. **That
mitigation was RETRACTED by the owner-rulings record itself, in its own voice, before this spec was
written.** The record's Q2 override paragraph withdraws the claim, states that it was reasoning from
a shape rather than from the attribute, and re-derives the result independently: what buys the
concurrency property is git's ordinary text merge over SEPARATED rows, not a driver. It then routes
the separation options here as this unit's fork. This spec inherits that retraction rather than
discovering it, and what follows is the re-verification, not the finding.

The two source facts the retraction rests on, re-checked here rather than taken on trust.
`git check-attr merge -- .lexicon.conf` reports `unspecified`: the `merge=rows` attribute is declared
only for `memory/DECISIONS.md` and `memory/backlog/*.md`. And the driver's partition predicate is
`_ROW_RE = re.compile(r"^\s*[-*]\s")` at `tools/memory-tree/merge-rows.py:252`, which matches a
markdown bullet, so an indented conf row such as `  py.file.conv 7` is classified as STRUCTURE rather
than as a row and would go to `git merge-file` positionally even with the attribute set. Its key
extractor `_ID_RE` at `:271` wants a decision-id shape a pin row does not carry either.

There is no `PINS:` block in `.lexicon.conf` today — `grep -n "PINS" .lexicon.conf` returns nothing —
so every block measured in this section is SYNTHESIZED, and no figure here can be reproduced against
the live declaration. Measured on this worktree with a ten-row synthesized block and no attribute
set, using the scratchpad script `pinmerge.py`: two branches draining rows four apart merge at exit 0
with zero conflict markers; two branches draining ADJACENT rows merge at exit 1 with one conflict
marker; two branches draining the same row conflict, which is correct and is not the case at issue.

- **(a) Accept plain three-way text merge and weaken AC5 to non-adjacent rows.** Costs nothing and
  ships today. Buys a property that holds for most pairs and fails exactly when two nodes drain
  neighbouring cells, which is the likeliest pair because related cells sit together.
- **(b) Add `.lexicon.conf merge=rows` to `.gitattributes` and make the driver's row predicate
  path-aware.** `merge-rows.sh` already passes `%P` and `merge-rows.py:1105` already ignores it, so
  the path is in hand. Cost: a Tier-2 change to the driver that arbitrates `memory/DECISIONS.md`,
  whose duplicate-introduction failure mode was measured at 147 of 151 historical conflicts under the
  obvious alternative. That is a large blast radius for this unit to take on.
- **(c) Separate pin rows with a single blank line** so git has one line of context between any two
  edits. Blank lines inside a block are skipped rather than terminating it, verified at
  `lexicon_conf.py:72-75`, so the grammar already allows it and no reader changes. **Measured on this
  worktree: with one blank line between every row, two branches draining ADJACENT cells merge at exit
  0 with zero conflict markers**, as does the one-row-apart case. Two blank lines buy nothing further.
  Its cost is that the block roughly doubles in length, and that a merge property is then encoded in
  whitespace that a later tidying edit could silently close.

**Recommendation: (c).** It needs no attribute, no driver change and no reader change, and it is the
only option measured to deliver the property Q2's ruling assumes.

**Correction to rev-3's recommendation, and to rev-4's repair of it.** Rev-3 said the whitespace
hazard is "gated rather than remembered" because an edit closing the gaps reds AC5's merge arm. It
does not, and rev-4 diagnosed only half of why. The half rev-4 got right: that arm lives on the
`lexicon selftest` leg, chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, and
`tools/run-gates/run-gates.sh` holds every `selftests` leg unless `GATE_SELFTESTS` is set BEFORE
guards are evaluated — which no boundary does, and the guard would exclude a conf-only diff even if
one did. **The half it missed, which is the load-bearing one: the arm's INPUT is a block the arm
writes.** It synthesizes a separated `PINS` fixture and merges that, so it merges clean however dense
the tracked declaration becomes. Reaching it changes nothing, which makes rev-4's compensating
`GATE_SELFTESTS=1` run inert against this hazard — a criterion whose input is synthesized cannot
observe a property of a tracked file, whichever leg it is reached from. **The real compensating
check is S10 and AC11**, which move the separation into `load_conf` as a refusal over the tracked
file, on the `lexicon wiring` leg whose guard is empty. Under (c) plus S10 the whitespace hazard is
gated after all — just not by the arm rev-3 named. The explicit `GATE_SELFTESTS=1 bash
tools/run-gates/run-gates.sh` run stays in the Definition of Done for the fixtures' own sake, not as
cover for this.

Option (b) is a change to a shared merge driver bought for one conf file, which is a trade this
build's own rules call out. What is NOT open is whether the pin block is row-shaped; Q2's ruling
makes that a requirement of this unit and S4 delivers it. Only the reconciliation mechanism was open,
and the mark below closes it.

**RESOLVED (agent, 2026-09-04, delegated): F1 — option (c), separate the `PINS:` rows with a single
blank line.**

Option (a) falls to veto 1: it is DEFINED as weakening AC5, a criterion already written in §6
("including for two ADJACENT cells"). An option whose own text is "delete the clause" is the purest
case of the first rung, and adjacent cells are the likeliest concurrent pair, because related cells
sit together — so (a) fails exactly where the property is worth having.

Option (b) falls to veto 2, on either half. `.gitattributes` is a governance carrier named in the
AGENTS.md layout, and its only two `merge=` declarations govern the append-only decision log and the
backlogs. `tools/memory-tree/merge-rows.py` is the driver ARBITRATING those two, and (b) changes its
row predicate — the arbitration behaviour of a governance carrier — and promotes `%P` / `argv[4]`
from read-by-nothing to load-bearing. Corroborating rather than deciding: the attribute half is
measurably INERT on its own. With `.lexicon.conf merge=rows` wired to the shipped driver, it printed
its own verdict — `rows O/A/B 0/0/0 -> 0 written (0 keyed, 0 hashed), … 1 structure conflicts,
CONFLICT` — because `_ROW_RE = re.compile(r"^\s*[-*]\s")` cannot match an indented pin row, so the
lines go to `git merge-file` positionally, the same geometry as no attribute at all. §5's rollback
claim ("one module plus one manifest entry") is false under (b) as well.

(c) is the sole survivor and would also win the feature-richness test outright: it is the only
option measured to deliver AC5's adjacent clause, and it does so touching nothing outside
`.lexicon.conf`'s own whitespace. The reader is indifferent — `lexicon_conf.py` skips blank lines
inside a block at `if not nxt.strip(): i += 1; continue` and terminates only on the dedent test
below it — so no parser changes. Two blank lines buy nothing further; same-row divergent drains
still conflict, which is correct.

One residual survives rev-5 and one is closed. Still open: (c) does NOT survive drain-vs-INSERT — a
drain against an insertion after the same row still exits 1 with one marker, and that is the edit
shape §3 hands to `TOOL-aSurfacedLexicon-7` and to every cell-arming commit, while AC5 is written
only about two drains. Closed: rev-4 recorded that AC5's regression arm cannot see the commit class
it exists to catch, and left it at that. S10 and AC11 now catch that class, in the reader rather than
in a fixture and on a leg with no guard, so the whitespace hazard under (c) is gated rather than
remembered. The gating just does not come from AC5, and AC5 now says so in its own text.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Grammar, refusals and the guard widening specced from the
  rebuild research record and the owner rulings record. `lexicon_conf.py`, `merge-rows.py`,
  `tools/gate-legs.json` and `.gitattributes` re-verified against source at writing time; the Q2
  mitigation was found not to exist as shipped and became fork F1, whose three options were then
  measured against real merges rather than reasoned about.
- rev-2 · 2026-09-04 · cross-spec audit. §3's pin-comparison non-goal routed the Q2 two-sided equality
  to "another unit already splitting `run()`", and that unit — `TOOL-aSurfacedLexicon-3` — disowns it
  by name in its own §3. The operator at `tools/lexicon/lexicon.py:697` is owned by no spec in this
  build; the non-goal now says so instead of pointing at a unit that refuses it. The
  `testsuite-count-waivers.txt` path in §5 was corrected to `memory/project/`.
- rev-3 · 2026-09-04 · the Q2 operator ASSIGNED to this unit rather than left unowned. The audit was
  right to escalate rather than self-assign, but the owner had already ruled the behaviour and only
  the routing was open, so routing it is composition and not a second decision. S9 takes
  `tools/lexicon/lexicon.py:697`, AC10 requires both directions observed RED, and §3's two new
  non-goals keep the counts themselves out: their values are emitted by `TOOL-aSurfacedLexicon-7`
  and draining them is Q3's rename unit.
- rev-4 · 2026-09-04 · F1 ratified as option (c), one blank line between pin rows, measured at exit 0
  with zero markers for adjacent drains where the dense block exits 1. The status base is RE-PINNED
  from `d0a18683` to `6c670b02`, because every figure this revision writes was measured there.
  Recorded that (c) covers drain-vs-drain only — a drain against an insertion still conflicts, which
  is the edit shape `TOOL-aSurfacedLexicon-7` and every cell-arming commit produce — and AC5 now
  carries that scope limit explicitly plus the hand-off that whichever unit emits the block emits it
  blank-separated, rather than leaving either implicit. Recorded that AC5's arm is unreachable from a
  conf-only commit because `lexicon selftest` is held behind `GATE_SELFTESTS` and guarded to
  `tools/lexicon/`; rev-3's claim that the hazard is "gated rather than remembered" is struck as
  false and the compensating explicit run is written in its place. AC5 is also marked UNVERIFIABLE
  against the live declaration: `grep -n "PINS" .lexicon.conf` returns nothing, so the arm and every
  merge figure behind it run over a synthesized block. §8's opening paragraph rewritten to report the
  owner-rulings retraction, which that record already made in its own voice, rather than to
  re-discover it against the ruling; the same falsified merge-driver claim still stands in the
  sibling conf-rewrite spec and is flagged there for the same correction. §4's separation sentence
  and the `.gitattributes` row of the files-touched table updated to the ratified option. Option (d),
  a comment line as the separator, is recorded as an unballoted refinement measuring identically to
  (c) without the whitespace hazard.
- rev-5 · 2026-09-04 · spec audit round 1 folded, and it removes scope rather than annotating it. S8,
  the guard widening, is STRUCK: staged and run here, it reds `govkit selfcheck` — an unguarded leg
  on every bar — and the lexicon kit's own descriptor had already refused it in prose, in a file this
  unit edits. The ruling moves to §3 with its compensating note, and §4 Alternatives records it as
  prior art the design pass missed, alongside the second reason it dies (the guard has two carriers
  and no shipped check compares them) and the registry-exempt route, which measures clean and is
  rejected on meaning. AC7 is struck in place with its number retained. AC5's two halves no longer
  contradict: it now states that its fixture is synthesized and therefore cannot observe the tracked
  file, and the ratified F1 separation becomes S10, a refusal inside `load_conf` over line numbers
  the parser already carries, observed by the new AC11 on the empty-guard `lexicon wiring` leg. AC8's
  first half replaced — the module it named has no `__main__` and printed nothing whatever the count
  was; the replacement prints the number and was run. AC10's premise reversed to match its four
  carriers: the RISE is implemented at the engine's pin comparison and the FALL is what is unguarded,
  and S9 now carries the four one-sided sentences it makes wrong. S2 rewritten against source — the
  module has one keyed arm and an unconditional fall-through, not a `LAYERS` arm — and its
  order-independence claim replaced with the stated difference and the sibling's id. S11 and AC12 add
  the map regeneration the unguarded freshness leg requires.
- rev-6 · 2026-09-04 · round-1 audit fold verification. AC2 asserted a red on `lexicon naming predicates`, a leg whose guard makes a conf-only stage skip it — the exact could-not-fail shape this rev removed elsewhere. It now observes the command, and names the unguarded path the conf actually reaches on the bar.
- rev-7 · 2026-09-04 · round-2 fold. §3's compensating note leaned on a retired hook behaviour: it
  said `.githooks/pre-push` sets `GATE_FULL=1` so the authoritative run stays total, which the hook
  stopped doing when the force became a bounded recorded obligation. The note now states what the
  hook guarantees — the forcing predicates, the ten-commit lag constant read at
  `.githooks/pre-push:184`, and that a scoped push evaluates every guard — so the exemption is
  priced against a bounded early signal rather than against a total run that no longer happens. §4
  Migration is deliberately UNCHANGED. An earlier revision of `TOOL-aSurfacedLexicon-6` S5 said this section must be
  amended to except its order-4 `py.constant` arming, and it was read here rather than taken on
  trust — Migration says the conf rewrite that pastes the real `CELLS` and `PINS` BODIES is a later
  unit, which one armed row at order 4 does not contradict, and it nowhere carries the sentence
  about no cell being armed that the sibling attributes to it.
- rev-8 · 2026-09-05 · the claim about `TOOL-aSurfacedLexicon-6` marked HISTORICAL — that spec withdrew it,
  and stating a withdrawn sibling claim in the present tense is the class three rounds have now been
  dominated by.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "parse an indented block of rows out of the naming
declaration and key them by a dotted cell name"` returns `key` in `tools/memory-tree/merge-rows.py`
at fan-in 27 and `parse` in `tools/memory-recall/query.py` at fan-in 10 as its two top seams, plus the
`row-grammar` affordance seam `id_pattern(conf)`. **The seam this unit extends is
`tools/lexicon/lexicon_conf.py`'s `load_conf` and `_parse_block`, which the lookup surfaces only
indirectly** because the module's functions carry fan-in through `sys.path` inserts rather than
through import edges the map can see. It is the right seam by contract rather than by rank: the
module docstring at `:3-9` names its four consumers and the reason there may be only one parser, and
`tools/codebase-map/map_extractors.py:139-168` reaches it by inserting the kit on `sys.path`. The two
ranked seams are both rejected in `§4 Alternatives rejected` — `merge-rows.key` keys markdown rows by
decision id, and `row_grammar` grades id uniqueness in index documents, neither of which reads a conf
block.

Recall terms used, verbatim: `python tools/memory-recall/query.py "why does the lexicon declaration
grammar refuse a dotted row key and what decided the block-key list" --terms "lexicon declaration conf
block keys VERBS LAYERS row key alphabetic refusal pins ratchet shrink-only"`. It returned 38 hits;
the load-bearing ones are the original grammar decision in this build family's first spec, which
records why the sibling `KEY=VALUE` form could not carry a prose verb table, and the map dossier
`memory/map/features/lexicon.md:137`, which enumerates the four readers this unit must not add a
fifth to.
