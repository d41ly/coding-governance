# TOOL-dClosedLexicon-1 — a declared naming lexicon, gated, and portable into an unknown repo

**Status:** DEFERRED · rev-4 · 2026-08-16 · node d · Tier-2 · base a9bd87d5 · streams playbook+tooling · ratified 2026-08-16

## 1. Goal

Companion §12 already claims "gate the layout conventions you can (naming, layer boundaries)" and
funds nothing that does it, so the claim is a convention an adopter is asked to remember. This unit
ships `tools/lexicon/`, an OPT-IN kit that gates three naming predicates against a per-repo
DECLARATION, and the companion §12 rules that route to it. The source material is the
`XiaoYouChR/Ghost-Downloader-3` agent charter, whose closed verb table is the only part of that
document that survives translation out of one Python/Qt application.

This unit is the KIT and the playbook edits. Wiring the verb table into the `codebase-map` ratchet
and the `drift-audit` signal set is `TOOL-dClosedLexicon-2`, split out at rev-3 because §1 does not
let one unit carry a cross-stream contract change. Unit 2 depends on this one; this one stands alone.

## 2. Scope (IN)

- **S1** — `tools/lexicon/lexicon.py`, stdlib-only, Python ≥3.11, implementing predicate P1: every
  function or method DEFINED in the corpus has a leading verb drawn from the declared `VERBS` set.
- **S2** — predicate P2: no type DEFINED in the corpus ends with a declared `BANNED_SUFFIXES` entry.
  Definition sites only, never an imported type, a parameter name, or a parameter type.
- **S3** — predicate P3: no module under a declared layer imports from a layer the declared direction
  forbids. With no `LAYERS` declaration the predicate reports `NOT ARMED` and the run reds, never
  passes green over an absent declaration.
- **S4** — per-language extraction declared with a COVERAGE MODE, one of `parser`, `probe` or `dark`,
  per §4 Coverage modes. Python ships `parser` on `ast`; the regex pattern sets ship `probe`; an
  extension present in the corpus with no declaration reds by name. The mode is DECLARED and REPORTED
  every run; the guard that would refuse a bad pin movement is not in this unit, per §4 F-A14.
- **S5** — `tools/lexicon/subtokens.py` owns the leading-token splitter, ported from
  `map_lib.subtokens()`. The lexicon is the source of truth for its own copy and ships
  self-contained, so an adopter taking this kit without `codebase-map` gets a working kit. A
  gov-internal parity leg asserts the two copies agree IN THIS REPO ONLY and is not shipped, the way
  `tools/lib/` is gov-internal and ships nothing.
- **S6** — a live non-empty assertion inside `lexicon.py`: a declared language whose definition
  population is EMPTY against a corpus containing that extension prints `DEAD PROBE` and reds. This
  is HYGIENE rule 5 applied to this gate, not a record-versus-reality question, and it stays here
  rather than moving to `drift-audit` with the signals that are.
- **S7** — three shrink-only offender pins in `.lexicon.conf`, MEASURED from the adopter's own corpus
  at scaffold and never inherited: `VERB_OFFENDER_PIN`, `SUFFIX_OFFENDER_PIN`, `LAYER_OFFENDER_PIN`.
- **S8** — waiver registries at `tools/lexicon/lexicon-verb-waivers.txt`,
  `tools/lexicon/lexicon-suffix-waivers.txt` and `tools/lexicon/lexicon-layer-waivers.txt`, keyed on
  matched TEXT rather than `<path>:<line>`, and a waiver whose hit is gone reds as stale.
- **S9** — `tools/lexicon/adopt-lexicon.sh` with `--scaffold` and `--check`. `--scaffold` DERIVES a
  proposed verb table from the adopter's corpus by leading-token frequency, writes it marked
  `PROPOSED`, and measures the three pins. `--check` is the drift mode every kit here carries.
- **S10** — a `ratified:` key in `.lexicon.conf` that `--check` asserts is present and non-empty, so
  an unedited `PROPOSED` seed cannot reach the merge bar disguised as a curated vocabulary.
- **S11** — `tools/lexicon/selftest.py`, red and green fixtures per predicate, per case style, and a
  frozen SENTINEL fixture per shipped pattern set, so a pattern set going inert fails here.
- **S12** — `tools/check-placeholders.sh` plus its self-test, asserting three things over the shipped
  playbook files: no `{{`-shaped placeholder survives, any placeholder appearing in BOTH carries the
  same filled value, and the three `governance-template: vN.N` markers agree. This funds
  `PLAY-aSealedCaravan-1` mechanically instead of correcting its prose again.
- **S13** — the playbook edits, in lockstep across all three shipped files, per §4 Migration.
  `{{LEXICON_CONF}}` is hosted in the COMPANION, which carries no byte gate, and the template's §12
  stub only routes to it.

## 3. Non-goals (OUT)

- The 33 rows of the source verb table. The kit seeds a table; it does not ship one repo's domain.
- The source document's case conventions, `_`-prefix rule, boolean prefixes, four-phase `__init__`,
  and the "flat is better than nested" preference. The first three are language-specific and the
  fourth contradicts §0's "build tokens, primitives, and factories BEFORE the screens that use them".
- A `--scaffold` proposal for P3. The layer map is hand-declared in this unit.
- The `codebase-map` inventory declaration and the `drift-audit` signals. Both are
  `TOOL-dClosedLexicon-2`.
- A pin-direction guard. Cut at rev-3 per review R3 and R4; it needs a baseline the conf does not
  carry, and it would serve `drift-audit` and `memory-tree` too, so it is a shared follow-up rather
  than this kit's private mechanism. Consequence stated in §4 F-A14.
- A new `memory/gotchas/` class for naming violations. Companion §7 requires a failing case OBSERVED
  before a gate lands. The first confirmed P1 or P2 finding becomes one, per §7's left-shift rule.
- A §0 constitution line naming the fallback for uncovered cases. Ratified to the §14 externalization
  unit instead, which is the only landing that can afford its ~120 B; see §8 fork F2.
- Any claim that this kit catches defects. Its value is seam detection, which is not measurable, and
  that is exactly why S13 lands it as OPT-IN rather than required.

## 4. Design

### Predicates

P1 is the load-bearing one, and its value is not typo-catching. A closed verb table makes the
question "which verb is this" answerable only when the function has one responsibility, so a name
that will not fit the table is reporting an unclear responsibility or a seam in the wrong place. The
rows that matter are the ones pinned by what they are NOT — `build` not `create`, `remove` not
`delete`, `set` not `update`, `update` not `refresh`, `load` not `fetch`. A table without those
negative definitions is decoration and the kit's seed writer says so.

P2 is the cheapest predicate and aims at the same target from the other side. A type named
`...Manager` is a type nobody scoped, and the ban is what forces companion §12's "one shared core,
thin adapters" to be true rather than aspirational.

P3 states §12's core-and-adapter rule as a DIRECTION, which is the form a machine can check.

### Coverage modes

`map_extractors.py:134` refuses to ship a regex extractor for shell and declares
`RECALL_DARK_LAYERS="bash"` instead, because a regex over shell definitions would look like coverage
while silently skipping what it forgot. That law binds here. Each declared language carries a mode.

| Mode | Extractor | Standing |
|---|---|---|
| `parser` | a real parse, Python `ast` today | complete over its extension |
| `probe` | a regex pattern set | incomplete by construction, reported as such every run |
| `dark` | none, declared explicitly | named every run, never silently absent |

### Data model

`.lexicon.conf` sits at the repo root beside `.memory-tree.conf` and `.codebase-map.conf`.

| Key | Meaning |
|---|---|
| `VERBS` | The closed table. One row per verb, `<verb>: <meaning>`, negative definitions included. |
| `BANNED_SUFFIXES` | Seeded with the source document's eight, editable. |
| `LAYERS` | `<glob> -> <glob>` pairs naming a FORBIDDEN import direction; empty means `NOT ARMED`. |
| `LANGS` | `<ext>:<pattern-set-id>:<mode>` triples over the shipped sets. |
| `VERB_OFFENDER_PIN` | Measured at scaffold, shrink-only. |
| `SUFFIX_OFFENDER_PIN` | Measured at scaffold, shrink-only. |
| `LAYER_OFFENDER_PIN` | Measured at scaffold, shrink-only. |
| `ratified` | The date and node that curated the seed. `--check` reds while it is empty. |

### Portability: what makes this land in an unknown repo

1. The language surface is DECLARED with a mode, so an unseen language is a named refusal and a
   partially-read one says so on every run.
2. Every pin is MEASURED against the adopting corpus at scaffold. `.memory-tree.conf` states the rule
   in its own words: a pin copied from a larger tree is either vacuous or permanently red.
3. The seed verb table is DERIVED from the adopter's corpus and then frozen by a human. An adopter
   cannot author a closed vocabulary for a domain they have not read yet.
4. Vacuity is armed on both sides — S6 against the adopter's corpus, S11's sentinels against the
   kit's own pattern sets — because the corpus-side arm is itself defeated by an empty corpus.
5. The kit ships SELF-CONTAINED. S5 is the rule that keeps it that way, and it is the rule an
   integration is most likely to break.
6. Waivers key on matched TEXT. `TOOL-aSealedCaravan-1` records what `<path>:<line>` keying cost
   `install-prefix-waivers.txt`: any edit above a waived line unpins it.

### Adversarial findings that changed the design

**F-A1 — the seed derivation is a mirror at birth.** Companion §7 bans a gate whose vocabulary is a
hand-kept mirror of the codebase's own identifiers. A prescriptive verb table is the inverse and is
safe. The `--scaffold` seed IS derived from source, so for one moment it is exactly the banned shape.
Resolution: derive once, mark `PROPOSED`, freeze, and make "was edited" checkable through S10.

**F-A2 — vacuity, not false positives, is the dominant failure mode.** This repo's own
`vacuous-selector-empty-population` class, live in `TOOL-aCandidStub-2`.

**F-A3 — a blanket `context` ban breaks Go on contact.** P2 scopes to DEFINITION sites only.

**F-A4 — adoption cost is the adoption blocker.** `ORPHAN_ID_PIN="5"` is the precedent for a pin that
is honestly non-zero on day one.

**F-A5 — the benefit is unmeasurable, so the kit must be optional.**

**F-A6 — the template has 86 bytes of headroom and this build spends most of them.** Measured 32,682 B
against the 32,768 B ceiling. The §12 stub edit costs roughly 78 B and the §5 count fix returns 9 B.
`{{LEXICON_CONF}}` is hosted in the companion (S13), so it costs the ledger nothing.

**F-A7 — the version note is itself a byte cost nobody budgets.** The template header carries exactly
two changelog entries, and the convention is drop-oldest-add-newest.

**F-A8 — the mandatory kit chassis is most of the work, not the three predicates.** See Inventory.

**F-A9 — `memory/project/` cannot hold the waiver registries.** Hygiene check 3 admits exactly six
`*.txt` registries there with no catch-all; `tools/install-prefix-waivers.txt` is the precedent.

**F-A10 — two of the three drive-by findings are already tracked.** `PLAY-aSealedCaravan-1` and
`PLAY-aCandidStub-2`. The stale `19-check` count is new.

**F-A11 — rev-1's §10 was wrong about its own novelty.** It called the case normalizer "the one
genuinely new mechanism here" while `map_lib.subtokens()` had shipped at `map_lib.py:528`.

**F-A12 — rev-1's nine-language regex set contradicted a law this repo already wrote down.**

**F-A13 — a gotcha class authored ahead of its first instance is the gate-discipline error.**

**F-A14 — cutting the pin-direction guard downgrades the coverage modes, and the spec says so rather
than hiding it.** Review R4 found the guard as specced would refuse a LEGITIMATE pin drop: fixing ten
real violations under a `probe` extractor could never be banked, which inverts the shrink-only
doctrine. Review R3 found it also needs a previous-value baseline the conf does not carry, and
`TOOL-aNumeralWarden-3` is an OPEN row saying no gate here can see a pin movement. Two independent
defects in one sentence of scope is a mechanism that has not been designed. Cut. What survives is
weaker and honest: a `probe` mode is declared and reported, an operator reading a lowered pin can see
which languages are incomplete, and nothing refuses the lower automatically. The guard is filed as a
shared follow-up because `drift-audit` and `memory-tree` need the same baseline read.

**F-A15 — rev-2 over-assigned S6 to `drift-audit`.** Three questions were bundled: an empty definition
population, a stale waiver, and a verb never used. The first is HYGIENE rule 5 — a check must not
select an empty population — and belongs INSIDE the gate that would otherwise pass green. The third
is genuinely record-versus-reality and belongs to `drift-audit`. Splitting them is what lets this
unit land alone without an unarmed vacuity check.

### Inventory

A new `tools/<kit>/` in this repo lands red without all of the following.

| Integration | Where | Why it reds otherwise |
|---|---|---|
| `KIT_LEXICON_VERSION` constant | `tools/lexicon/lexicon.py` | `tools/check-kit-versions.sh` needs a `need()` row |
| `gov:kit lexicon@X.Y` marker | same file | the version pair gate compares marker to constant |
| registry entry | `tools/govkit/registry.toml` | the `tools/*` surface glob makes an unregistered dir a `selfcheck` failure |
| gate legs | `tools/gate-legs.json` | the run-gates canary asserts legs are single-sourced there |
| leg guards | same | a records-only commit must skip the kit's self-tests |
| `--check` wiring mode | `adopt-lexicon.sh` | every adopter kit here carries one |
| install-prefix compliance | all shipped strings | `tools/check-install-prefix.sh` refuses a root-install kit path |
| codebase-map claim | `memory/map/` | the `kits` inventory reds on an unclaimed new key |
| gov-internal splitter parity | `tools/lexicon/subtokens.py` | S5; the leg is dogfood-only and must not ship |
| `ARMS_FLOORS` row | `.memory-tree.conf` | `check-arms.py` needs a per-gate branch and armed floor |

### Migration

The three shipped files move together or the lockstep marker lies.
`parallel-coding-governance.template.md` gets the §12 stub clause, the §5 count fix, the v2.8 header
entry and the v2.6 drop. `parallel-coding-governance.domain-rules.md` gets the §12 lexicon rules,
`{{LEXICON_CONF}}`, and the marker bump. `parallel-coding-governance.customize.md` gets the new
conditional-section row, the corrected disjointness sentence, and the placeholder tally.

### Rollout

Land the kit with its predicates OFF for this repo, measure the three pins over this corpus, ratify
the derived table, then arm the legs in a second commit whose message carries the measured numbers.
Arming and measuring in one commit hides which of the two produced the number.

### Files touched (estimate)

Twelve new files under `tools/lexicon/`, one new `tools/check-placeholders.sh` with its self-test,
three edited playbook files, `tools/gate-legs.json`, `tools/check-kit-versions.sh`,
`tools/govkit/registry.toml`, `.memory-tree.conf`, and one codebase-map dossier.

### Alternatives rejected

- **A tree-sitter or ctags extractor.** External dependency; every engine here is stdlib-only.
- **Vendoring the splitter FROM `codebase-map` with a shipped parity gate.** Review R5: the parity
  leg would compare against a file an adopter taking only this kit does not have, so it reds forever
  or is silently skipped. The lexicon owns its copy instead and the parity leg stays gov-internal.
- **Shipping the source document's 33 verbs as the table.** They encode one downloader's domain.
- **Requiring the kit.** Rejected on F-A5.
- **Correcting `customize.md`'s prose again.** `PLAY-aSealedCaravan-1` shows the prose has been wrong
  through at least one correction cycle, which is the argument for S12.

## 5. Production-readiness checklist

- security — N/A. The kit reads tracked source and writes only its own conf and waiver files.
- perf / scale — one pass over tracked files per predicate; budget under 5 s on this corpus, and the
  leg carries a guard so a records-only commit skips it.
- a11y — N/A — no user interface.
- i18n — identifier extraction is ASCII-anchored; a corpus with non-ASCII identifiers declares `dark`.
- error / empty / loading states — the empty-corpus and empty-population cases are S6 and S11.
- observability — every red names the file, the identifier, the predicate and the waiver line that
  would silence it.
- risks — the dominant risk is a silently vacuous predicate, armed by S6 and S11. The secondary risk
  is adopter abandonment under waiver load, addressed by S7 and re-examined in fork F4. A third,
  new at rev-3: with the pin-direction guard cut, a `probe`-mode pin can be lowered on incomplete
  evidence and only a reader will notice.
- testing + left-shift gates — S11 and the S12 self-test.
- migration / rollback — the kit is opt-in and removing `.lexicon.conf` disarms it; the playbook edits
  revert as one commit.
- user docs — `tools/lexicon/README.md` and `LEXICON.md`, matching the `HYGIENE.md` pattern.

## 6. Acceptance criteria

- **AC1** — When a function is defined whose leading token is outside `VERBS`, `python tools/lexicon/lexicon.py`
  exits non-zero and names the file, the identifier and the offending token.
- **AC2** — When a type is defined ending in a `BANNED_SUFFIXES` entry, the same run reds; when that
  same suffix appears only on an imported type or a parameter, `lexicon.py` stays green.
- **AC3** — When `LAYERS` is empty, the run prints `NOT ARMED` and exits non-zero rather than green.
- **AC4** — When a declared language's definition population is empty against a corpus containing that
  extension, `python tools/lexicon/lexicon.py` prints `DEAD PROBE` and reds, fixtured in `selftest.py`.
- **AC5** — When every shipped pattern set runs against its frozen sentinel fixture, each reports a
  non-zero definition count, so `python tools/lexicon/selftest.py` fails if any pattern set goes inert.
- **AC6** — When `addTask`, `add_task`, `AddTask` and `add-task` are each extracted, all four yield
  `add`, asserted per case style in `selftest.py`.
- **AC7** — When `.lexicon.conf` carries an empty `ratified` key, `bash tools/lexicon/adopt-lexicon.sh --check`
  exits non-zero naming the unratified seed.
- **AC8** — When a waiver's matched text no longer appears in the corpus, the run reds as stale, and
  an edit ABOVE a waived occurrence does NOT unpin it, both fixtured in `selftest.py`.
- **AC9** — When `{{MEMORY_ROOT}}` is filled with different values in the two shipped files,
  `bash tools/check-placeholders.sh` exits non-zero naming the placeholder and both values.
- **AC10** — When any `{{`-shaped placeholder survives in either shipped file, `tools/check-placeholders.sh` reds.
- **AC11** — When the three shipped files carry disagreeing `governance-template` markers,
  `bash tools/check-placeholders.sh` reds naming each file and its version.
- **AC12** — When the playbook edits are staged, `bash tools/check-template-size.sh` is green and the
  reported size is at or under 32768 bytes.
- **AC13** — When `python tools/govkit/govkit.py selfcheck` runs after the kit lands, it is green,
  proving `tools/lexicon/` is a declared entry rather than an unclaimed surface path.
- **AC14** — When `bash tools/run-gates.sh` runs on the landing commit, every new leg appears in the
  green line by name and `tools/check-kit-versions.sh` reports the `KIT_LEXICON_VERSION` pair.
- **AC15** — When `tools/lexicon/subtokens.py` diverges from `map_lib.subtokens()`, the gov-internal
  parity leg reds; when the kit is installed into a tree with no `codebase-map`,
  `python tools/lexicon/lexicon.py` still runs green, proving the kit is self-contained.

## 7. Gates

Existing legs that must stay green: `tools/check-template-size.sh`, `tools/check-kit-versions.sh`,
`tools/check-install-prefix.sh`, `python tools/govkit/govkit.py selfcheck`,
`tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-arms.py`, and
`python tools/codebase-map/test_codebase_map.py`.

New legs this unit adds: `python tools/lexicon/lexicon.py`, `python tools/lexicon/selftest.py`,
`bash tools/lexicon/adopt-lexicon.sh --check`, `bash tools/check-placeholders.sh`, and
`bash tools/check-placeholders.test.sh`.

## 8. Open questions

- **F1 — sequencing against the template budget.** This unit leaves roughly 17 B of template
  headroom. `PLAY-aCandidStub-2` names the fix, moving §14 behind a §-stub for about 1.5 KB.
  RESOLVED (owner, 2026-08-16): the §14 externalization lands FIRST as its own unit, then this one.
  That unit is not yet specced and has no id; this spec is DEFERRED — approved, parked on a
  predecessor — rather than INPROGRESS, and the token is what a resuming session reads.
- **F2 — the §0 constitution line.** The source document opens by naming itself the fallback for
  situations no rule covers, and §0 has no such line. It is worth roughly 120 B that do not exist.
  RESOLVED (owner, 2026-08-16): add it, in §0 rather than the companion, carried by the §14 unit F1
  ratified. It is a §3 non-goal HERE, and that unit's scope is now two items, not one.
- **F3 — symbol extraction overlaps `codebase-map`, narrowly.** RESOLVED (agent, 2026-08-16,
  delegated): the splitter is ported and lexicon-owned per S5, and the parser is not reusable because
  `map_lib.python_symbols` indexes only public symbols. Whether `codebase-map` should later CONSUME a
  lexicon-owned definition census, which would also close `TOOL-aNumeralWarden-4`, moves to
  `TOOL-dClosedLexicon-2` §8.
- **F4 — does P1 earn its adoption cost?** Unmeasurable by construction. RESOLVED (owner,
  2026-08-16): ship all three predicates behind one opt-in kit, and retire P1 if it goes unused
  across two adopters. The retirement condition is the record, not an intention — a later session
  reading this is entitled to close P1 on that evidence without reopening the argument.
- **F5 — has rev-2 made the unit too big to land as one?** RESOLVED (owner, 2026-08-16): split. The
  integration is `TOOL-dClosedLexicon-2`; the pin-direction guard is cut to a shared follow-up rather
  than moved, per F-A14.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, folding the adversarial pass F-A1 through F-A10 into §4.
- rev-2 · 2026-08-16 · folded the kit-integration pass: coverage modes replace the flat regex set
  (S4), the case splitter becomes vendored reuse (S5), vacuity moves to `drift-audit` signals (S6),
  the verb table joins the map ratchet (S14), a pin-direction guard lands (S15), and §10 is
  rewritten after F-A11 found it wrong about its own novelty.
- rev-3 · 2026-08-16 · folded review-dClosedLexicon-1. F5 resolved by split: S14 and the drift
  signals leave for `TOOL-dClosedLexicon-2` (R7). S15 and its AC are CUT, not moved, on two
  independent defects (R3, R4), and F-A14 records the downgrade that buys. S5 inverts to
  lexicon-owned with a gov-internal parity leg (R5). S6 is re-scoped to the live rule-5 assertion
  after F-A15 found rev-2 had over-assigned it. S12 gains the marker-lockstep assertion (R8) and S13
  names the companion as `{{LEXICON_CONF}}`'s host (R9).
- rev-4 · 2026-08-16 · owner ratified the scope menu. F1, F2 and F4 resolved in place, so §8 is now
  fully resolved and the header carries `ratified`. Status moves SPECCED to DEFERRED: scope approval
  happened, so "awaiting owner scope approval" is no longer true, and the §14 externalization is a
  predecessor this unit is parked on rather than an external prereq.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py naming vocabulary gate` ranked `registry.toml` (govkit),
`check-install-prefix.sh`, `id_pattern(conf)` (row-grammar) and `map_lib` as the nearest seams. Three
are reuse in this unit. From `check-install-prefix.sh`, the shipped-surface waiver pattern for S8.
From `row_grammar.py`, the conf-driven grammar compilation. From `map_lib`, `subtokens()` at line 528,
ported rather than imported per S5 — the S5 mechanism rev-1 wrongly called new. The fourth,
`registry.toml`'s declaration-not-listing pattern, is reuse in `TOOL-dClosedLexicon-2`, not here.

One seam the query did not surface: `tools/lib/resolve-python.sh` is the precedent for a
gov-internal-only parity gate over a copy that ships, which is the shape S5 settled on after review
R5 showed the shipped-parity version was un-runnable in an adopter tree. No existing seam covers the
three predicates themselves, which is the whole of what this kit owns.
