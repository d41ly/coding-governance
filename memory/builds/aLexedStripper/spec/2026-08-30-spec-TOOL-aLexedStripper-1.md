# TOOL-aLexedStripper-1 — `_identifier_tokens` becomes one language-aware pass

**Status:** SPECCED · rev-2 · 2026-08-30 · node a · Tier-2 · base 19d9b328 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-prompt-TOOL-aLexedStripper-1-1.md](../prompts/2026-08-30-prompt-TOOL-aLexedStripper-1-1.md) | research | — |
| [2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round1.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round1.md) | spec-audit | TOOL-aLexedStripper-2 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/codebase-map/map_lib.py`'s `_identifier_tokens` must return the identifiers that appear in a
file's CODE, for every language the map covers, instead of applying C-family comment and string
syntax to all of them. The fan-in index built on it is the ranking behind `reuse_lookup.py`, which
template §10 and charter §1 make a Definition-of-Ready item, so its recall is the property that
matters.

## 2. Scope (IN)

- **S1** — Replace the three module-level regexes `_BLOCK_COMMENT_RE`, `_LINE_COMMENT_RE` and
  `_STRING_RE`, as consumed by `_identifier_tokens`, with ONE left-to-right pass over a per-suffix
  lexical profile. §4's data model is the sole owner of that profile's fields.
- **S2** — Give `_identifier_tokens` the file's suffix. Both call sites already hold the path:
  `build_reference_index` (`map_lib.py:675`, has `rel`) and `reference_index_for`
  (`map_lib.py:710`, has `rel`).
- **S3** — Declare profiles for the three families the covered corpora actually contain: C-family
  (`.js .jsx .mjs .cjs .ts .tsx .c .h .cc .cpp .hpp .java .go .rs .cs .swift .kt .scala .php`),
  Python (`.py .pyi`), and hash-comment (`.sh .bash .zsh .toml .yaml .yml .cfg .ini .conf`).
- **S4** — An UNDECLARED suffix strips nothing and returns every identifier token. This is the
  documented fail-open direction for a ranking heuristic, and it is the opposite of the current
  behaviour, which guesses C syntax for everything.
- **S5** — A multi-line construct left UNTERMINATED at end of file is abandoned rather than allowed
  to swallow the rest of the scan: the pass restarts in code mode at the line after the opener. This
  covers an odd backtick in a `.ts` file and an unbalanced triple quote in a `.py` file, which are
  the two constructs that can reproduce class 1 in a new spelling.
- **S6** — A selftest arm per over-strip class in §4's table, plus the two S5 arms and the corpus
  arm AC1 and AC2 name, each staged RED against the current code before the fix is wired.

## 3. Non-goals (OUT)

- No parser, and no per-language grammar beyond the profile fields §4's data model declares — that
  table is the single owner of the field set, and this bullet names no count of its own. `fan_in` is
  documented as a heuristic used for ranking and a WARN, never gated, and this unit does not change
  that.
- Not changing `subtokens`, `stems`, `_STEM_SUFFIXES` or the seam threshold. The tokenizer's OUTPUT
  set changes; nothing downstream of it is touched.
- Not re-seeding any committed artifact. Verified at BASE: no committed file derives from
  `_identifier_tokens`. `build_reference_index` is documented NEVER committed,
  `affordance-exempt.toml` is a dossier-prose grace list, and `--seed-affordances` prints a worklist.
- Not fixing `dead_exports`' false-positive rate (`ABL-bCandidLoupe-10`). Its count will move because
  its input improves; recounting it is that row's job, in the adopter's tree.

## 4. Design

### Data model

A profile is a 6-field record keyed by suffix. This table is the field set's only declaration.

| field | meaning |
|---|---|
| `line_markers` | tokens that open a comment running to end of line |
| `marker_needs_word_start` | whether a line marker opens a comment ONLY at line start or after whitespace |
| `block_pair` | the block-comment open/close pair, or none |
| `quote_chars` | characters that open a single-line string |
| `triple_quoted` | whether `'''` and `"""` open a multi-line string |
| `backtick_is_string` | whether a backtick opens a string whose content is NOT code |

| family | line | word-start | block | quotes | triple | backtick |
|---|---|---|---|---|---|---|
| C-family | `//` | no | `/*` `*/` | `'` `"` | no | yes, multi-line |
| Python | `#` | no | none | `'` `"` | yes | no |
| hash-comment | `#` | **yes** | none | `'` `"` | no | no |

`marker_needs_word_start` exists for exactly one family and is the field the naive rule cannot
express. In shell, `#` is a comment only at a word boundary: `$#` is the argument count and
`${path#/opt/}` is a prefix strip, and a pass that treats either as a comment deletes the rest of
the line. Python needs no such predicate — outside a string its `#` is always a comment — and the
two rows differ on purpose rather than by omission. Backtick is NOT a string in the hash-comment
family because shell backticks open command substitution, whose content is code.

### The five over-strip classes this replaces

Each row is demonstrated by a fixture in which the current chain loses a named identifier that the
candidate keeps. A suffix gate on the block regex alone — the adopter's own proposed fix,
`bHonedPlumbline` S1 in `d41ly/incms` — closes only rows 1 and 2.

| # | class | fixture | current chain loses |
|---|---|---|---|
| 1 | `/*` in a non-C file opens a comment | `.py` docstring holding `application/*`, later `on*/` | `BRAVO` |
| 2 | `//` in a non-C file truncates a line | `.py` `return DELTA // ECHO` | `ECHO` |
| 2 | same, shell | `.sh` `p=//server/share` and `$(( a // b ))` | `server`, `share`, `b` |
| 3 | `#` in a C-family file truncates a line | `.ts` `const a = "#frag" + bravo`; `class Foo { #priv = 1; bravo() {} }` | `bravo` |
| 4 | a comment marker INSIDE a string over-strips | `.ts` `"https://x.io/" + bravo`; `.js` `'a // b' + bravo`; `.py` `"a # b" + bravo` | `bravo` |
| 5 | a backtick opens a span where it is not a string | `.sh` `alpha=` backtick `date` backtick | `date` |

**An honest bound on rows 3 and 4.** Both are real per fixture, and both are RARE in the measured
corpora: over `d41ly/incms` the `.ts` and `.tsx` populations are within 0.1 percentage points of
each other before and after the change. Rev-1 said these rows mean "this is not a Python-only
defect", which overstates the corpus evidence. The measured damage is concentrated in Python and in
shell; rows 3 and 4 are correctness, not volume.

### The measured failure

`services/api/app/main.py` in `d41ly/incms` at `069f0459`. A MIME glob `application/*` inside a
docstring opens a class-1 span that closes 674 lines later on an `on*` attribute glob. Raw
identifier tokens 1616, kept 88. Against `tokenize` ground truth the file holds 356 real code
identifiers and the current chain keeps 67 — recall 18.8%, which is the 81.2% loss
`ABL-bCandidLoupe-1` reports as 81.3%.

That tree is EVIDENCE, not an acceptance corpus: it is external, this spec pins no revision of it,
and four divergent local checkouts exist. The acceptance corpus is this repo's own, in §6.

### Migration

None. The function is pure, its output is computed on demand, and no committed artifact derives
from it.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py` — the profile table, the scanner, the two call sites, and the
  `KIT_CODEBASE_MAP_VERSION` bump.
- `tools/codebase-map/selftest.py` — the per-class arms, the S5 arms, and the corpus arm.
- `tools/codebase-map/README.md` — the version line, if it carries one.

### Alternatives rejected

- **Gate only `_BLOCK_COMMENT_RE` on a C-family suffix set** (the adopter's `bHonedPlumbline` S1).
  Tested: closes rows 1 and 2, leaves 3, 4 and 5 standing. Rejected because it fixes the reported
  instance and not the class (§7).
- **Strip nothing at all, for every language.** Tested against ground truth: recall rises to 100%
  and precision falls to roughly 14%, because every word of every docstring becomes an identifier.
  The function's own contract says fan-in must be import/identifier-scoped, and that is the half
  this would delete.
- **Use `tokenize` for Python and regexes elsewhere.** Rejected: exact for `.py` and nothing for the
  other two families, so the corpus keeps four of the five classes and gains a second answer to one
  question. It also fails closed on a file that does not parse, and this scan must not.

## 5. Production-readiness checklist

- security — N/A. No new input surface; the function reads tracked files the caller already reads.
- perf / scale — one pass replaces three full-text regex substitutions. Measured no worse; the
  `reuse_lookup` corpus scan is unchanged in shape.
- a11y — N/A, no user interface.
- i18n — the scanner is byte-agnostic and reads text already decoded as UTF-8, unchanged.
- error / empty / loading states — three states, each with its own criterion. An unterminated
  single-line quote stops at its line (AC7 covers the shell case; the rule is in S1's pass). An
  unterminated MULTI-line construct — a `.ts` backtick or a `.py` triple quote — is abandoned per S5
  rather than eating the file (AC8), because those are the two constructs that can reproduce class 1
  in a new spelling. An unknown suffix strips nothing (AC6).
- observability — N/A. The scan feeds a ranking and a WARN, and prints nothing of its own.
- risks — the ranking output MOVES: precision rises from 37.6% to 99.6% on this repo's corpus, so
  tokens that appeared only in prose lose their edges and some `fan_in` counts fall. That is the
  correction, not a regression, but it can drop a symbol below `SEAM_FANIN_THRESHOLD`. No gate reads
  `fan_in`.
- testing + left-shift gates — one arm per §4 class, two S5 arms, one corpus arm, each observed RED
  first.
- migration / rollback — none needed; revert is a single-file revert.
- user docs — `tools/codebase-map/README.md` only if it states the stripping behaviour.

## 6. Acceptance criteria

The acceptance corpus is THIS repo, enumerated as `git ls-files '*.py'` at the commit under test,
with ground truth from stdlib `tokenize` NAME tokens and files that fail to tokenize skipped. It is
re-runnable by anyone with this checkout and needs no external tree.

- **AC1** — When the corpus above is measured by the arm added to
  `python tools/codebase-map/selftest.py`, recall is at least 99%, against 88.6% at BASE.
- **AC2** — When the same arm in `tools/codebase-map/selftest.py` runs, precision is at least 99%,
  against 37.6% at BASE.
- **AC3** — When `tools/lexicon/lexicon.py` is scanned, recall is 100%, against 61.5% at BASE; and
  `tools/codebase-map/selftest.py` likewise, against 57.3% at BASE. These are the two worst files in
  this repo and they fail if the class-1 fix regresses.
- **AC4** — When a Python source whose docstring contains `application/*` and a later `on*/` is
  scanned, every identifier defined after the docstring is still returned — the class-1 arm.
- **AC5** — When a `.ts` source contains `#` inside a string literal and a `//` inside a URL
  literal, the identifiers after those markers on the same line survive — the class-3 and class-4
  arms, each asserting a named identifier the current chain loses.
- **AC6** — When a file has a suffix no profile declares, `_identifier_tokens` returns exactly
  `set(_IDENT_TOKEN_RE.findall(source))`.
- **AC7** — When a `.sh` source uses `$#`, `${x#y}` and a real `#` comment, only the comment is
  stripped and `resolve_target` and `emit_result` after the first two survive — the
  `marker_needs_word_start` arm.
- **AC8** — When a `.ts` source carries one unmatched backtick, and when a `.py` source carries an
  unmatched triple quote, the identifiers on every subsequent line are still returned — the S5 arms,
  which are the class-1 swallow in a new spelling.
- **AC9** — When each arm above is staged against the code at BASE, `python
  tools/codebase-map/selftest.py` reports it RED, and the observation is recorded in the acceptance
  ledger.
- **AC10** — When `python tools/codebase-map/selftest.py` runs whole, it passes, including the
  existing `fan_in` assertions at `selftest.py:861-864`.
- **AC11** — When `bash tools/check-kit-versions.sh` runs, `KIT_CODEBASE_MAP_VERSION` is bumped and
  well-formed.

## 7. Gates

`codebase-map selftest` · `kit-versions` · `memory hygiene` · `map coverage` · and the full bar
`bash tools/run-gates/run-gates.sh` at the push boundary. The new gate this unit adds is the arm set
in `tools/codebase-map/selftest.py`, which carries the per-class arms AND the corpus floors AC1 and
AC2 name, so the class is gated and not only the instances.

## 8. Open questions

- **F1 — should the hash-comment profile treat backtick as a string?** In shell a backtick opens
  command substitution and its CONTENT is code, so stripping it would delete real identifiers; not
  stripping it leaves nothing to strip, since the backticks themselves are not identifiers.
  RESOLVED (agent, 2026-08-30, delegated): backtick is not a string in the hash-comment profile. It
  falls out of the observation — class 5's `.sh` fixture loses `date` under the current chain and
  keeps it under the candidate — rather than from a preference, and M3's veto list is not reached.
- **F2 — should `.md`, `.json` and other non-code suffixes get a profile?** They are excluded by the
  caller's extension filter, which is derived from the symbol file list, so a profile for them would
  never be consulted. RESOLVED (agent, 2026-08-30, delegated): no profile; S4's fail-open covers any
  that slips through.
- **F3 — does `marker_needs_word_start` belong to Python too?** Python's `#` outside a string is
  always a comment, so the predicate would change no verdict there, and setting it would make the
  two `#` rows look identical when they are not. RESOLVED (agent, 2026-08-30, delegated): no — the
  hash-comment family alone. The observation decides it: no Python fixture changes under either
  setting, so the tie-break is the row that stays visibly different on purpose.

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, written from a measured reproduction at BASE `19d9b328`.
- rev-2 · 2026-08-30 · folded the round-1 spec audit
  (`2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round1.md`). Finding 28: the profile gains
  `marker_needs_word_start`, without which AC7's shell case is unimplementable. Finding 16: §3's
  non-goal no longer states a field count and points at §4 as the owner. Finding 5: S5 and AC8 added
  for the unterminated multi-line constructs §5 claimed and §6 did not check. Finding 27: the
  acceptance corpus moved from an unpinned external inCMS checkout to this repo's own tracked
  Python files, with the inCMS figures demoted to §4 evidence and its sha pinned. §4's class table
  gained the fixture that demonstrates each row, after the rev-1 fixtures for rows 3 and 4 were
  found to prove nothing — they placed the identifier BEFORE the marker, which is this repo's own
  `fixture-passes-by-finding-nothing` class.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "strip comments and string literals from source before
counting identifier tokens"` returned `stripStrings` and `blankLiterals`
(`tools/hooks/agent-cap.js`) and `agent-cap.topLevelArgs` as its top same-shape candidates. The
seam this unit extends is therefore NOT in `codebase-map` at all: it is `blankLiterals`, the
single-pass, mode-tracking lexer that `agent-cap.js` already ships for exactly this problem in
JavaScript. That file is the in-repo precedent for the shape, and its header states the reason
directly — a per-line strip "cannot see a template literal".

It is a precedent and not a dependency. `map_lib.py` is stdlib-only Python and `blankLiterals` is
JavaScript, so no code is shared and none should be: this unit copies the SHAPE — one left-to-right
pass with an explicit mode — and not the bytes. The two remain separate implementations of one idea
in two languages, which is what the charter's shared-core rule permits when the languages differ.

**And the precedent carries a warning this unit inherits.** `TOOL-aLexedStripper-2`'s round-1 audit
measured two fail-open shapes in `blankLiterals` when it is used as a sole view: its mode is carried
across lines, so an unterminated construct blanks everything after it. S5 exists because the same
hazard reaches this scanner — an odd backtick in a `.ts` file would reproduce the 674-line swallow
this unit is removing. Copying a shape means copying its failure modes unless they are named.

Recall terms used, for M7 re-runs: `codebase-map identifier tokens comment strip regex language
suffix fan-in reference index reuse lookup docstring block comment`. The recall pass returned no
prior gov decision on the tokenizer's language blindness; the only prior record is
`TOOL-aRootedPrefix-1`, which is about the install prefix and not the scanner.

**A hit that was STALE, recorded because M5 requires it:** `ABL-bCandidLoupe-1` says "24 .py files
affected". Re-measured over `d41ly/incms` at `069f0459`, 34 Python files lose more than 10% of their
real identifiers. This repo is affected too and the row does not say so: 12 gov files lose more than
10%, worst `tools/lexicon/lexicon_conf.py` at 55.6% recall. The adopter's row should be updated from
this spec's numbers.
