# TOOL-dClosedLexicon-1 — a declared naming lexicon, gated, and portable into an unknown repo

**Status:** SPECCED · rev-1 · 2026-08-16 · node d · Tier-2 · base a9bd87d5 · streams playbook+tooling

## 1. Goal

Companion §12 already claims "gate the layout conventions you can (naming, layer boundaries)" and
funds nothing that does it, so the claim is a convention an adopter is asked to remember. This unit
ships `tools/lexicon/`, an OPT-IN kit that gates three naming predicates against a per-repo
DECLARATION, and the companion §12 rules that route to it. The source material is the
`XiaoYouChR/Ghost-Downloader-3` agent charter, whose closed verb table is the only part of that
document that survives translation out of one Python/Qt application.

## 2. Scope (IN)

- **S1** — `tools/lexicon/lexicon.py`, stdlib-only, Python ≥3.11, implementing predicate P1: every
  function or method DEFINED in the corpus has a leading verb drawn from the declared `VERBS` set.
- **S2** — predicate P2: no type DEFINED in the corpus ends with a declared `BANNED_SUFFIXES` entry.
  Definition sites only, never an imported type, a parameter name, or a parameter type.
- **S3** — predicate P3: no module under a declared layer imports from a layer the declared direction
  forbids. With no `LAYERS` declaration the predicate reports `NOT ARMED` and the run reds, never
  passes green over an absent declaration.
- **S4** — per-language extraction declared, not assumed: `.lexicon.conf` maps an extension to a
  pattern set, and the kit ships seed pattern sets for Python, JavaScript/TypeScript, Go, Rust, Java,
  C#, PHP, Ruby and shell. An extension present in the corpus with no mapping reds by name.
- **S5** — one case normalizer per pattern set, so `addTask`, `add_task`, `AddTask` and `add-task` all
  yield the leading token `add`. The normalizer is the portability crux and is unit-fixtured per case
  style, not per language.
- **S6** — vacuity defence: every declared language asserts a NON-EMPTY definition population against
  a corpus that contains files of that extension, and prints `DEAD PROBE` and reds when it finds
  none. Independently, each shipped pattern set carries a frozen SENTINEL fixture inside the kit, so
  a predicate is proven live on every run without depending on the adopter's corpus.
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
- **S11** — `tools/lexicon/selftest.py`, red and green fixtures per predicate, including an explicit
  arm for each vacuity branch of S6 and each case style of S5.
- **S12** — `tools/check-placeholders.sh` plus its self-test: no `{{`-shaped placeholder survives in
  either shipped playbook file, and any placeholder appearing in BOTH carries the same filled value.
  This funds `PLAY-aSealedCaravan-1` mechanically instead of correcting its prose again.
- **S13** — the playbook edits, in lockstep across all three shipped files, per §4 Migration.

## 3. Non-goals (OUT)

- The 33 rows of the source verb table. The kit seeds a table; it does not ship one repo's domain.
- The source document's case conventions, `_`-prefix rule, boolean prefixes, four-phase `__init__`,
  and the "flat is better than nested" preference. The first three are language-specific and the
  fourth contradicts §0's "build tokens, primitives, and factories BEFORE the screens that use them".
- A `--scaffold` proposal for P3. The layer map is hand-declared in this unit; deriving one from the
  import graph is a follow-up, and shipping a machine-proposed layer map is how P3 becomes vacuous.
- A §0 constitution line naming the fallback for uncovered cases. It is worth having and there is no
  template budget for it; see §8 fork F2.
- Consolidating the symbol extractor with `tools/codebase-map/map_extractors.py`; see §8 fork F3.
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

### Data model

`.lexicon.conf` sits at the repo root beside `.memory-tree.conf` and `.codebase-map.conf`.

| Key | Meaning |
|---|---|
| `VERBS` | The closed table. One row per verb, `<verb>: <meaning>`, negative definitions included. |
| `BANNED_SUFFIXES` | Seeded with the source document's eight, editable. |
| `LAYERS` | `<glob> -> <glob>` pairs naming a FORBIDDEN import direction; empty means `NOT ARMED`. |
| `LANGS` | `<ext>:<pattern-set-id>` pairs over the shipped sets. |
| `VERB_OFFENDER_PIN` | Measured at scaffold, shrink-only. |
| `SUFFIX_OFFENDER_PIN` | Measured at scaffold, shrink-only. |
| `LAYER_OFFENDER_PIN` | Measured at scaffold, shrink-only. |
| `ratified` | The date and node that curated the seed. `--check` reds while it is empty. |

### Portability: what makes this land in an unknown repo

Five things, and every one of them is a lesson this repo already paid for.

1. The language surface is DECLARED, so an unseen language is a named refusal rather than a silent
   pass. `.memory-tree.conf`'s `DISCIPLINES` is the same shape.
2. Every pin is MEASURED against the adopting corpus at scaffold. `.memory-tree.conf` states the rule
   in its own words: a pin copied from a larger tree is either vacuous or permanently red.
3. The seed verb table is DERIVED from the adopter's corpus and then frozen by a human. An adopter
   cannot author a closed vocabulary for a domain they have not read yet, and a kit that demands one
   on day one is a kit that gets deleted on day one.
4. Vacuity is armed twice — once against the adopter's corpus and once against a sentinel frozen
   inside the kit — because the adopter-corpus arm is itself defeated by an empty corpus.
5. Waivers key on matched TEXT. `TOOL-aSealedCaravan-1` records what `<path>:<line>` keying cost
   `install-prefix-waivers.txt`: any edit above a waived line unpins it, and the gate reds on a merge
   that touched nothing it guards.

### Adversarial findings that changed the design

**F-A1 — the seed derivation is a mirror at birth.** Companion §7 bans a gate whose vocabulary is a
hand-kept mirror of the codebase's own identifiers, because a rename drifts it silently. A
prescriptive verb table is the inverse and is safe: a rename cannot make the table stale, only make
code violate it. The `--scaffold` seed, however, IS derived from source, so for one moment it is
exactly the banned shape. Resolution: derivation is a one-time scaffolding step whose output is
marked `PROPOSED`, edited, and frozen; the gate never re-derives. S10's `ratified:` key is what makes
"was edited" checkable rather than assumed.

**F-A2 — vacuity, not false positives, is the dominant failure mode.** A definition regex that stops
matching makes the whole predicate pass green forever, which is this repo's own
`vacuous-selector-empty-population` class and is already live in `TOOL-aCandidStub-2`. S6 arms it on
both sides.

**F-A3 — a blanket `context` ban breaks Go on contact.** `ctx context.Context` appears in most Go
function signatures. Scoping P2 to DEFINITION sites is what keeps the seed shippable; without it the
first Go adopter waives the predicate rather than the occurrence.

**F-A4 — adoption cost is the adoption blocker.** A greenfield predicate over a mature repo fires
hundreds of times, and an adopter facing 300 waivers turns the gate off. The measured shrink-only
pin is the repo's established answer, and `ORPHAN_ID_PIN="5"` is the precedent for a pin that is
honestly non-zero on day one.

**F-A5 — the benefit is unmeasurable, so the kit must be optional.** Seam detection cannot be
counted the way `codebase-map` coverage can. `memory-tree` is the only kit `customize.md` marks
non-droppable; this one joins `codebase-map` and `memory-recall` in the conditional list.

**F-A6 — the template has 86 bytes of headroom and this build spends most of them.** Measured:
`parallel-coding-governance.template.md` is 32,682 B against the 32,768 B ceiling
`tools/check-template-size.sh` enforces. The §12 stub edit costs roughly 78 B and the §5 count fix
returns 9 B, leaving about 17 B. `PLAY-aCandidStub-2` already records that the template is
effectively full and names §14 as the externalization candidate; see §8 fork F1.

**F-A7 — the version note is itself a byte cost nobody budgets.** The template header carries exactly
two changelog entries, currently v2.7 and v2.6, and a v2.8 entry runs about 165 B. A builder who
appends one reds the size gate. The convention is drop-oldest-add-newest, and F-A6's ledger only
balances because the v2.6 entry leaves in the same edit.

**F-A8 — the mandatory kit chassis is most of the work, not the three predicates.** See Inventory.

**F-A9 — `memory/project/` cannot hold the waiver registries.** Hygiene check 3 admits exactly six
`*.txt` registries there and carries no catch-all. `tools/install-prefix-waivers.txt` is the
precedent for a kit keeping its own waivers, which is why S8 puts all three under `tools/lexicon/`
and check 3 is untouched.

**F-A10 — two of the three drive-by findings are already tracked.** `PLAY-aSealedCaravan-1` owns the
`{{MEMORY_ROOT}}` disjointness error and the 13-versus-14 miscount, and `PLAY-aCandidStub-2` owns the
byte budget. Neither is new. S12 changes the first from a prose correction into a gate, which is the
only reason to reopen it. The stale check count is not tracked anywhere and is new.

### Inventory

A new `tools/<kit>/` in this repo lands red without all of the following, and this is the bulk of the
unit.

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
| `ARMS_FLOORS` row | `.memory-tree.conf` | `check-arms.py` needs a per-gate branch and armed floor |
| method-carrier row | the kit registry | only if `LEXICON.md` points at the build method |

### Migration

The three shipped files move together or the lockstep marker lies. `parallel-coding-governance.template.md`
gets the §12 stub clause, the §5 count fix, the v2.8 header entry and the v2.6 drop.
`parallel-coding-governance.domain-rules.md` gets the §12 lexicon rules and the marker bump.
`parallel-coding-governance.customize.md` gets the new conditional-section row, the corrected
disjointness sentence, and the placeholder tally `{{LEXICON_CONF}}` moves.

### Rollout

Land the kit first with its predicates OFF for this repo, measure the three pins over this corpus,
ratify the derived table, then arm the legs in a second commit whose message carries the measured
numbers. Arming and measuring in one commit hides which of the two produced the number.

### Files touched (estimate)

Eleven new files under `tools/lexicon/`, one new `tools/check-placeholders.sh` with its self-test,
three edited playbook files, `tools/gate-legs.json`, `tools/check-kit-versions.sh`,
`tools/govkit/registry.toml`, `.memory-tree.conf`, and one codebase-map dossier.

### Alternatives rejected

- **A tree-sitter or ctags extractor.** Correct parsing, external dependency, and every engine here
  is stdlib-only. Rejected on the dependency, and S6's sentinel is the compensating control.
- **Shipping the source document's 33 verbs as the table.** They encode one downloader's domain, and
  `mount`, `supervise`, `patch` and `reveal` mean nothing in a repo with no viewport or binary.
- **Requiring the kit.** Rejected on F-A5. An unmeasurable benefit does not get to be mandatory.
- **Correcting `customize.md`'s prose again.** `PLAY-aSealedCaravan-1` shows the prose has been wrong
  through at least one correction cycle, which is the argument for S12 rather than a third edit.

## 5. Production-readiness checklist

- security — N/A. The kit reads tracked source and writes only its own conf and waiver files.
- perf / scale — one pass over tracked files per predicate; budget under 5 s on this corpus, and
  the leg carries a guard so a records-only commit skips it.
- a11y — N/A — no user interface.
- i18n — identifier extraction is ASCII-anchored; a corpus with non-ASCII identifiers must declare it
  and is out of scope for the shipped pattern sets.
- error / empty / loading states — the empty-corpus and empty-population cases are S6, and both are
  loud.
- observability — every red names the file, the identifier, the predicate and the waiver line that
  would silence it.
- risks — the dominant risk is a silently vacuous predicate, addressed twice by S6. The secondary
  risk is adopter abandonment under waiver load, addressed by S7.
- testing + left-shift gates — S11 plus the S12 self-test; both ride `tools/run-gates.sh` as legs.
- migration / rollback — the kit is opt-in and removing `.lexicon.conf` disarms it; the playbook edits
  revert as one commit.
- user docs — `tools/lexicon/README.md` and `LEXICON.md`, the prose home, matching the
  `HYGIENE.md` pattern.

## 6. Acceptance criteria

- **AC1** — When a function is defined whose leading token is outside `VERBS`, `python tools/lexicon/lexicon.py`
  exits non-zero and names the file, the identifier and the offending token.
- **AC2** — When a type is defined ending in a `BANNED_SUFFIXES` entry, the same run reds; when that
  same suffix appears only on an imported type or a parameter, `lexicon.py` stays green.
- **AC3** — When `LAYERS` is empty, the run prints `NOT ARMED` and exits non-zero rather than green.
- **AC4** — When a declared language's definition pattern matches zero definitions in a corpus that
  contains that extension, the run prints `DEAD PROBE` and reds, proven by a fixture in `selftest.py`.
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
- **AC11** — When the playbook edits are staged, `bash tools/check-template-size.sh` is green and the
  reported size is at or under 32768 bytes.
- **AC12** — When `python tools/govkit/govkit.py selfcheck` runs after the kit lands, it is green,
  proving the new `tools/lexicon/` directory is a declared entry rather than an unclaimed surface path.
- **AC13** — When `bash tools/run-gates.sh` runs on the landing commit, every new leg appears in the
  green line by name and `tools/check-kit-versions.sh` reports the `KIT_LEXICON_VERSION` pair.

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
  headroom, which makes the next playbook rule of any size impossible. `PLAY-aCandidStub-2` already
  names the fix, moving §14 behind a §-stub for about 1.5 KB. RECOMMENDATION: land the §14
  externalization FIRST as its own unit, then this one. Landing this first is not wrong, it just
  means the next author discovers the wall instead of us.
- **F2 — the §0 constitution line.** The source document opens by naming itself the fallback for
  situations no rule covers, and §0 has no such line. It is worth roughly 120 B that do not exist.
  RECOMMENDATION: defer to the unit that resolves F1, and put it in §0 rather than the companion,
  because a fallback rule nobody loads is not a fallback.
- **F3 — symbol extraction overlaps `codebase-map`.** `tools/codebase-map/map_extractors.py` already
  extracts symbols with fan-in across languages, and `reuse_lookup.py` surfaced it. Hard-depending on
  it is wrong because `codebase-map` is optional, and extract-if-present is two code paths.
  RECOMMENDATION: ship the lexicon's own extractor, record the overlap here, and open a follow-up row
  for consolidation once both extractors have a measured corpus. Note `TOOL-aNumeralWarden-4`, which
  records that the map indexes no non-exported JavaScript function — so the map's extractor could not
  serve P1 today even if the dependency were acceptable.
- **F4 — does P1 earn its adoption cost?** Unmeasurable by construction, per F-A5. RECOMMENDATION:
  ship all three predicates behind one opt-in kit, and let P2 and P3 carry the adoption case, since
  both are cheap and checkable. If P1 goes unused across two adopters, retire it rather than defend it.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, folding the adversarial pass F-A1 through F-A10 into §4.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py naming vocabulary gate` ranked `registry.toml` (govkit),
`check-install-prefix.sh`, `id_pattern(conf)` (row-grammar) and `map_lib` as the nearest seams. Three
of those are the reuse this unit takes: the declaration-not-listing pattern from `registry.toml`, the
shipped-surface waiver pattern from `check-install-prefix.sh`, and the conf-driven pattern grammar
from `row_grammar.py`. The fourth, `map_lib`, is the symbol-extraction seam that would be reuse and
is not takeable today; F3 records why and what would change it. No existing seam covers the
per-language case normalizer of S5, which is the one genuinely new mechanism here.
