# TOOL-aLexedStripper-1 — `_identifier_tokens` becomes one language-aware pass

**Status:** SPECCED · rev-1 · 2026-08-30 · node a · Tier-2 · base 19d9b328 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-prompt-TOOL-aLexedStripper-1-1.md](../prompts/2026-08-30-prompt-TOOL-aLexedStripper-1-1.md) | research | — |

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
  lexical profile: line-comment markers, an optional block-comment pair, the quote characters, and
  whether backtick opens a string.
- **S2** — Give `_identifier_tokens` the file's suffix. Both call sites already hold the path:
  `build_reference_index` (`map_lib.py:675`, has `rel`) and `reference_index_for`
  (`map_lib.py:710`, has `rel`).
- **S3** — Declare profiles for the three families the covered corpora actually contain: C-family
  (`.js .jsx .mjs .cjs .ts .tsx .c .h .cc .cpp .hpp .java .go .rs .cs .swift .kt .scala .php`),
  Python (`.py .pyi`), and hash-comment (`.sh .bash .zsh .toml .yaml .yml .cfg .ini .conf`).
- **S4** — An UNDECLARED suffix strips nothing and returns every identifier token. This is the
  documented fail-open direction for a ranking heuristic, and it is the opposite of the current
  behaviour, which guesses C syntax for everything.
- **S5** — A selftest arm per over-strip class in §4's table, each staged RED against the current
  code before the fix is wired.

## 3. Non-goals (OUT)

- No parser, and no per-language grammar beyond the four profile fields. `fan_in` is documented as a
  heuristic used for ranking and a WARN, never gated, and this unit does not change that.
- Not changing `subtokens`, `stems`, `_STEM_SUFFIXES` or the seam threshold. The tokenizer's OUTPUT
  set changes; nothing downstream of it is touched.
- Not re-seeding any committed artifact. Verified at BASE: no committed file derives from
  `_identifier_tokens`. `build_reference_index` is documented NEVER committed,
  `affordance-exempt.toml` is a dossier-prose grace list, and `--seed-affordances` prints a worklist.
- Not fixing `dead_exports`' false-positive rate (`ABL-bCandidLoupe-10`). Its count will move because
  its input improves; recounting it is that row's job, in the adopter's tree.

## 4. Design

### Data model

A profile is a 5-tuple keyed by suffix: `(line_markers, block_pair_or_None, quote_chars,
triple_quoted, backtick_is_string)`. Three profiles cover the corpora; the table is data, and adding
a language is one dict entry.

| family | line | block | quotes | triple | backtick |
|---|---|---|---|---|---|
| C-family | `//` | `/*` `*/` | `'` `"` | no | yes, multi-line |
| Python | `#` | none | `'` `"` | yes | no |
| hash-comment | `#` | none | `'` `"` | no | no |

### The five over-strip classes this replaces

Each is a distinct defect of the current chain, and a suffix gate on the block regex alone — the
adopter's own proposed fix, `bHonedPlumbline` S1 in `d41ly/incms` — closes only the first two.

| # | class | why the current chain has it |
|---|---|---|
| 1 | `/*` in a non-C file opens a comment | `_BLOCK_COMMENT_RE` has no language gate and uses `DOTALL` |
| 2 | `//` in a non-C file truncates a line | `_LINE_COMMENT_RE` matches `//` in Python and shell, where it is floor division and a path |
| 3 | `#` in a C-family file truncates a line | the same regex matches `#`, which is a private field in JS and a fragment in a URL |
| 4 | a comment marker INSIDE a string over-strips | comments are stripped BEFORE strings, so a `//` in a URL literal eats its line |
| 5 | a backtick in non-JS prose opens a span | `_STRING_RE`'s `` `[^`]*` `` arm crosses newlines and is applied to every language |

Classes 3 and 4 damage the C-family files the regexes were written for, which is why this is not a
Python-only defect.

### The measured failure

`services/api/app/main.py` in `d41ly/incms`, at BASE. A MIME glob `application/*` inside a docstring
opens a class-1 span that closes 674 lines later on an `on*` attribute glob. Raw identifier tokens
1616, kept 88. Against `tokenize` ground truth the file holds 356 real code identifiers and the
current chain keeps 67 — recall 18.8%, which is the 81.2% loss `ABL-bCandidLoupe-1` reports as 81.3%.

### Migration

None. The function is pure, its output is computed on demand, and no committed artifact derives
from it.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py` — the profile table, the scanner, the two call sites, and the
  `KIT_CODEBASE_MAP_VERSION` bump.
- `tools/codebase-map/selftest.py` — the per-class arms.
- `tools/codebase-map/README.md` — the version line, if it carries one.

### Alternatives rejected

- **Gate only `_BLOCK_COMMENT_RE` on a C-family suffix set** (the adopter's `bHonedPlumbline` S1).
  Tested: it closes classes 1 and 2 and leaves 3, 4 and 5 standing, including both classes that
  damage C-family files. Rejected because it fixes the reported instance and not the class (§7).
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
- error / empty / loading states — an unterminated quote must stop at its line, never eat the file;
  an unknown suffix strips nothing. Both are arms in §6.
- observability — N/A. The scan feeds a ranking and a WARN, and prints nothing of its own.
- risks — the ranking output MOVES: precision rises from 39.0% to 99.3%, so tokens that appeared
  only in prose lose their edges and some `fan_in` counts fall. That is the correction, not a
  regression, but it can drop a symbol below `SEAM_FANIN_THRESHOLD`. No gate reads `fan_in`.
- testing + left-shift gates — one selftest arm per class in §4, each observed RED first.
- migration / rollback — none needed; revert is a single-file revert.
- user docs — `tools/codebase-map/README.md` only if it states the stripping behaviour.

## 6. Acceptance criteria

- **AC1** — When `_identifier_tokens` runs over `services/api/app/main.py` from `d41ly/incms`,
  recall against `tokenize` NAME tokens is 100%, against 18.8% at BASE.
- **AC2** — When the whole inCMS Python corpus is measured against `tokenize` ground truth, recall
  is at least 99% and precision at least 99%, against 97.5% and 39.0% at BASE.
- **AC3** — When a Python source whose docstring contains `application/*` and a later `on*/` is
  scanned, every identifier defined after the docstring is still returned — the class-1 arm in
  `tools/codebase-map/selftest.py`.
- **AC4** — When a `.ts` source contains `# ` inside a string literal and a `//` inside a URL
  literal, the identifiers on those lines survive — the class-3 and class-4 arms.
- **AC5** — When a `.sh` source uses `$#`, `${x#y}` and a `#` comment, only the comment is stripped.
- **AC6** — When a file has a suffix no profile declares, `_identifier_tokens` returns exactly
  `set(_IDENT_TOKEN_RE.findall(source))`.
- **AC7** — When each §4 class arm is staged against the code at BASE, `python
  tools/codebase-map/selftest.py` reports it RED, and the observation is recorded in the acceptance
  ledger.
- **AC8** — When `python tools/codebase-map/selftest.py` runs, it passes, including the existing
  `fan_in` assertions at `selftest.py:861-864`.
- **AC9** — When `bash tools/check-kit-versions.sh` runs, `KIT_CODEBASE_MAP_VERSION` is bumped and
  well-formed.

## 7. Gates

`codebase-map selftest` · `kit-versions` · `memory hygiene` · `map coverage` · and the full bar
`bash tools/run-gates/run-gates.sh` at the push boundary. The new gate this unit adds is the set of
per-class arms in `tools/codebase-map/selftest.py`.

## 8. Open questions

- **F1 — should the hash-comment profile treat backtick as a string?** In shell a backtick opens
  command substitution and its CONTENT is code, so stripping it would delete real identifiers; not
  stripping it leaves nothing to strip, since the backticks themselves are not identifiers.
  Recommendation: do not treat it as a string. RESOLVED (agent, 2026-08-30, delegated): backtick is
  not a string in the hash-comment profile. It falls out of the observation rather than a
  preference — the content is code by the language's own semantics, and M3's veto list is not
  reached.
- **F2 — should `.md`, `.json` and other non-code suffixes get a profile?** They are excluded by the
  caller's extension filter, which is derived from the symbol file list, so a profile for them would
  never be consulted. Recommendation: no profile, and let S4's fail-open cover any that slips
  through. RESOLVED (agent, 2026-08-30, delegated): no profile; S4 covers them.

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, written from a measured reproduction at BASE `19d9b328`.

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

Recall terms used, for M7 re-runs: `codebase-map identifier tokens comment strip regex language
suffix fan-in reference index reuse lookup docstring block comment`. The recall pass returned no
prior gov decision on the tokenizer's language blindness; the only prior record is
`TOOL-aRootedPrefix-1`, which is about the install prefix and not the scanner. The finding's own
history lives in the adopter's tree, cited in §4 and in this build's prompt record.

**A hit that was STALE, recorded because M5 requires it:** `ABL-bCandidLoupe-1` says "24 .py files
affected". Re-measured at BASE across the same tree, 34 Python files lose more than 10% of their
real identifiers and 1123 lose more than half their raw tokens. The row's figure was not re-derived
after the corpus grew, and the adopter's row should be updated from this spec's numbers.
