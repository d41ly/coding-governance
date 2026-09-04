# TOOL-aSurfacedLexicon-4 — the CELLS and PINS declaration grammar

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

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
- **S2** — `_parse_block` gains a generic default. Dispatch stays keyed on the block name: `VERBS`
  keeps its alphabetic refusal at `:105-106`, `LAYERS` keeps its arrow refusal at `:113-117`, and
  every other key parses as `<row-key> <rest>` split on the first run of whitespace, returning an
  insertion-ordered `dict`. The generic path applies no `.isalpha()` test, which is what admits a
  dotted row key. This unit does not touch `LAYERS`, so it lands identically whether or not
  `TOOL-aSurfacedLexicon-2`'s P3 deletion has landed first.
- **S3** — the `CELLS` row grammar: `<ext>.<surface>  <convention> [vocab] [notail]`. `surface` is
  the closed set `function`, `type`, `file`, `constant`. `convention` is the closed set `snake`,
  `screaming`, `camel`, `pascal`, `kebab`, `dark`. A row naming a surface or a convention outside
  those sets is a refusal naming the file and line, never a skip.
- **S4** — the `PINS` row grammar: `<ext>.<surface>.<predicate>  <count>`, where `predicate` is the
  closed set `debt`, `unruled`, `suffix`, `conv`, and `count` must parse as a non-negative decimal
  integer. A count that does not parse is a refusal.
- **S5** — two cross-block declaration refusals, both owned here because both are answerable from the
  declaration alone with no corpus walk. A `CELLS` row naming an extension absent from `LANGS` reds.
  A `PINS` row naming a cell absent from `CELLS` reds.
- **S6** — `lexicon_conf._main`'s `--print-rows` takes an optional block key, so
  `tools/lexicon/adopt-lexicon.sh` can read the matrix through the one reader. Today `--print-rows`
  takes only the conf path and hardcodes `VERBS` at `:174-178`. Omitting the key keeps today's
  behaviour, so no existing caller changes.
- **S7** — the concurrency property Q2's ruling depends on: two branches each draining a different
  cell's pin must merge clean. The mechanism is the fork in §8; the property is in scope either way,
  and its regression arm is `AC5`.
- **S8** — widen the `lexicon naming predicates` leg guard in `tools/gate-legs.json` to include
  `.lexicon.conf`. Measured today the guard is `["tools/","skills/session-kickoff/",".githooks/",".claude/"]`
  and `.lexicon.conf` matches none of those prefixes, so a conf-only commit does not select the leg
  that runs the refusals S5 adds.
- **S9** — the two-sided pin equality itself, at `tools/lexicon/lexicon.py:697`. Q2's ruling is that a
  count which FALLS reds exactly as one that rises does, so `if len(unwaived) > pin:` becomes an
  inequality against the declared count in both directions. The message distinguishes the two
  directions, because they call for opposite actions: a rising count names the new offenders, and a
  falling one prints the exact replacement row to paste. This unit owns the operator because it owns
  the pin rows the operator reads, and because S7's concurrency property is only worth having if a
  falling count is something the bar actually notices.

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

## 4. Design

### Data model

`load_conf` returns one flat dict. Two new keys join it, both insertion-ordered so a printed block
round-trips in declaration order.

| Key | Parsed shape | Refusal cases |
|---|---|---|
| `CELLS` | `{"py.function": ("snake", frozenset({"vocab"}))}` | unknown surface, unknown convention, unknown flag, duplicate row key, extension absent from `LANGS` |
| `PINS` | `{"py.file.conv": 7}` | unknown predicate, non-integer count, duplicate row key, cell absent from `CELLS` |

The row key is kept verbatim as the dict key rather than exploded into a tuple. A string key is what
lets `--print-rows` emit the block for bash without a second grammar, and it is what lets a pin row
be `grep`-able by the exact text an owner typed. Callers that need the parts split them at the dots
themselves, which is one expression and no new contract.

The two cross-block refusals in S5 run after the whole file is parsed, because `LANGS` may be
declared below `CELLS` and a reader that refuses on line order refuses a legal file.

Row SEPARATION inside the `PINS` block is a merge property rather than a formatting preference. Fork
F1 is ratified as option (c), one blank line between rows. The reader is indifferent either way:
blank lines inside a block are skipped rather than treated as terminators, verified at
`lexicon_conf.py:72-75`.

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
| `tools/lexicon/lexicon.py` | call `check_declaration` from the declaration-validation path so S5's refusals reach a verdict |
| `tools/lexicon/selftest.py` | red and green fixtures per refusal in S3, S4 and S5, plus the merge arm of AC5 |
| `tools/gate-legs.json` | one guard entry (S8) |
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
  is measured in §8 rather than asserted. Rollback is a revert of one module plus one manifest entry,
  because no declaration is required to carry the new blocks.
- testing + left-shift gates — every refusal in S3, S4 and S5 gets a red fixture and a green fixture
  in `tools/lexicon/selftest.py`, and each red is observed before the unit is called done. No new bar
  leg is added, so the build rule about ceilings and `memory/project/testsuite-count-waivers.txt` rows is not
  triggered; S8 widens an existing guard, which changes when a leg runs and not what runs.
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
- **AC2** — When a `CELLS` row naming an extension absent from `LANGS` is staged, the
  `lexicon naming predicates` leg REDS naming that extension and that line number; when the row is
  unstaged the leg greens. The red is observed and recorded before this unit is called done.
- **AC3** — When a `PINS` row carries a non-integer count such as `py.file.conv seven`, `load_conf`
  raises `ConfError` naming the line; when it carries `7` it parses to the integer `7`.
- **AC4** — When a block header that is not in `BLOCK_KEYS` appears, for example `FOO:`,
  `load_conf` still raises rather than silently accepting it. This is the regression arm on S1:
  widening the tuple must not make every identifier-shaped header legal.
- **AC5** — When two branches off one base each drain a different pin row and are merged, `git merge`
  exits 0 with no conflict markers in `.lexicon.conf`, including for two ADJACENT cells. This is a
  standing selftest arm that performs the merge, not a one-time observation, so an edit that removes
  the separation F1 chose reds it. **The measurement is UNVERIFIABLE against the live declaration and
  says so**: `grep -n "PINS" .lexicon.conf` returns nothing, so there is no dense block in the tree
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
- **AC7** — When a commit touches only `.lexicon.conf`, `bash tools/run-gates/run-gates.sh` runs the
  `lexicon naming predicates` leg rather than reporting it `skip guarded`. Measured today that guard
  is `["tools/","skills/session-kickoff/",".githooks/",".claude/"]` and matches no conf path.
- **AC8** — When the widened reader is in place, `python tools/codebase-map/map_extractors.py` still
  yields 23 `lexicon-verbs` inventory keys and `python tools/drift-audit/drift_report.py --json`
  still reports its three lexicon signals with `live: true` rather than `not_asked`.
- **AC9** — When `python tools/lexicon/lexicon_conf.py --print-rows <conf>` is run with no block key,
  it prints the `VERBS` rows exactly as it does today, so `bash tools/lexicon/adopt-lexicon.sh
  --check` finds the rendered Skill unchanged.
- **AC10** — When a pin row's declared count is one ABOVE the measured count, `python
  tools/lexicon/lexicon.py --check` REDS naming that cell and printing the exact replacement row;
  when it is one BELOW, it REDS naming the new offenders. Both directions are observed as real reds
  before this unit is called done, and both are standing selftest arms. This is the arm that proves
  Q2 landed: measured today `tools/lexicon/lexicon.py:697` is `if len(unwaived) > pin:`, so the
  falling case currently exits 0 and the ratchet the conf and all three waiver headers claim does not
  exist in any line of Python.

## 7. Gates

- `lexicon naming predicates` — the leg that runs the engine's declaration verdict, chunk
  `declarations`, subject `repo`, ceiling 300 s. S8 widens its guard and this unit adds no new leg.
- `lexicon wiring` — chunk `wiring`, subject `repo`, guard empty, ceiling 330 s. It byte-compares the
  rendered Skill, so it fires on a conf-only diff and is where AC9's regression surfaces.
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

**Correction to rev-3's recommendation, which claimed the opposite of what is true.** Rev-3 said the
whitespace hazard is "gated rather than remembered" because an edit closing the gaps reds AC5's merge
arm. It does not. That arm lives on the `lexicon selftest` leg, chunk `selftests`, subject `kit`,
guard `["tools/lexicon/"]`, and `tools/run-gates/run-gates.sh` holds every `selftests` leg unless
`GATE_SELFTESTS` is set BEFORE guards are evaluated — which no boundary does, and the guard would
exclude a conf-only diff even if one did. A commit that closes the blank lines in `.lexicon.conf`
therefore reaches the arm only under `GATE_SELFTESTS=1 GATE_FULL=1`. Under (c) the whitespace hazard
is REMEMBERED, not gated. The compensating check, since an exemption is not coverage: this unit's
Definition of Done already runs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` explicitly per
§7, and the same explicit run is owed by the conf rewrite that first pastes a real `PINS` block and
by any commit that edits one.

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

Two residuals, neither a veto. (c) does NOT survive drain-vs-INSERT: a drain against an insertion
after the same row still exits 1 with one marker, and that is the edit shape §3 hands to
`TOOL-aSurfacedLexicon-7` and to every cell-arming commit, while AC5 is written only about two
drains. And AC5's regression arm cannot see the commit class it exists to catch: `lexicon selftest`
is chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, and the runner holds every such leg
unless `GATE_SELFTESTS` is set BEFORE guards are evaluated — so a commit closing the blank lines in
`.lexicon.conf` reaches the arm only under `GATE_SELFTESTS=1 GATE_FULL=1`. Under (c) the whitespace
hazard is remembered, not gated, which is the trade §8 claims the recommendation avoids.

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
