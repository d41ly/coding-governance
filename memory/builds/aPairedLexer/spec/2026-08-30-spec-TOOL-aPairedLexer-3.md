# TOOL-aPairedLexer-3 — the definition probe strips comments in one pass

**Status:** SPECCED · rev-2 · 2026-08-30 · node a · Tier-2 · base 14e21399 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-build-TOOL-aPairedLexer-1-base-measurements.md](../build/2026-08-30-build-TOOL-aPairedLexer-1-base-measurements.md) | journal | TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 |
| [2026-08-30-review-TOOL-aPairedLexer-1-2-3-spec-audit-round1.md](../reviews/2026-08-30-review-TOOL-aPairedLexer-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 |

<!-- /gen:spec-records -->

## 1. Goal

`scan_js_definitions` must stop losing definitions to a block-comment opener written inside a line
comment. It strips BLOCK comments before LINE comments, so a bare `/*` in a `//` comment opens a
`DOTALL` span that runs to the next closer and swallows every definition between.

## 2. Scope (IN)

- **S1** — Add `render_comment_free(text)` to `map_lib.py`: ONE left-to-right pass that blanks
  `//` line comments and `/* */` block comments ONLY, emitting a newline for every newline it
  consumes so LINE NUMBERS are preserved. It TRACKS `'…'`, `"…"` and backticked strings so that a
  comment marker inside one does not open a comment, and **emits their contents unchanged**.
  **Rev-1 said to blank string contents and that was a measured loss.** The defect is the comment
  ORDER and nothing about it requires touching strings; blanking them adds a second unsound strip —
  the pass models no regex literal — and the audit measured eight real definitions removed from
  this repo's own tracked JavaScript. Tracking without blanking is what the correctness needs, and
  it cannot delete anything: the only bytes this pass removes are inside a comment.
- **S2** — Both consumers use it: `map_lib.py:461` and the mirror at `:539`. `_BLOCK_COMMENT_RE`
  loses its last consumer and is deleted with them.
- **S3** — A selftest arm per direction: a definition after a line-comment block-opener is FOUND, a
  definition inside a real block comment is NOT, and a `//` inside a string does not truncate.
- **S4** — Regenerate `memory/map/generated/` and verify the diff is definitions RECOVERED and
  nothing removed.

## 3. Non-goals (OUT)

- Not touching `_identifier_tokens`. It already has its own language-aware pass from
  `TOOL-aLexedStripper-1` and does not consume `_BLOCK_COMMENT_RE`.
- Not making the pass language-aware by suffix. Both consumers scan a declared extension set that is
  C-family only, so one profile is the whole requirement and a second parameter would be unused.
- Not changing `JS_DEFINITION_RULES` or what counts as a definition.

## 4. Design

### The defect

`map_lib.py:461` and `:539` run

```python
text = _BLOCK_COMMENT_RE.sub(lambda mm: "\n" * mm.group(0).count("\n"), path.read_text(...))
text = "\n".join(ln.split("//", 1)[0] for ln in text.splitlines())
```

Block first, line second. A `//` comment containing a bare block-opener therefore opens a real span.
Measured on a four-definition fixture with an opener inside a line comment after the first:

```
probe order   finds: alpha
correct order finds: alpha, bravo, charlie
SWALLOWED:           bravo, charlie
```

**Swapping the order is not the fix.** Line-first breaks the mirror case: a `//` inside a block
comment — `/* see http://x */` — truncates at the `//`, the closer is lost, and the span runs on.
Either ordering is wrong for some input, which is the same finding `TOOL-aLexedStripper-1` recorded
for the token scan: comments and strings exclude each other and no sequence of independent passes
expresses that.

### Why line structure must survive

The current code substitutes `"\n" * count`, and the probe reports `file:line`. A pass that collapsed
lines would move every definition's line number and silently corrupt `symbols.json`, which is a
COMMITTED artifact. `render_comment_free` therefore emits one newline per newline consumed, and AC5
pins that the output line count equals the input's.

### Adopter-side scale

Measured during `aLexedStripper` with `map_lib`'s own `JS_DEFINITION_RULES` rather than a retyped
regex: `d41ly/incms` carries 35 files with the shape and loses **14 definitions across 9**, including
an account component pair and a fetch helper. This repo lost 4 until a comment was reworded, which
fixed an instance and not the class — and the reword had to be done TWICE during that build, because
the second fix's own comment reintroduced the trigger.

**Swallow SIZE is not harm and must not be used as a proxy.** One adopter file loses 4368 characters
and zero definitions; another loses 5968 and two real components.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py` — the helper, the two call sites, the deleted regex, the version.
- `tools/codebase-map/selftest.py` — the arms.
- `memory/map/generated/` — regenerated.

### Alternatives rejected

- **Swap the two passes.** Rejected on the mirror case above.
- **Reuse `_identifier_tokens`' scanner.** Rejected: it does not preserve line structure and returns
  a token SET rather than text, and widening it to do both would give one function two jobs.
- **Keep reworiding comments.** Rejected: it is the instance fix this build exists to stop, and it
  has already failed twice in one session.

## 5. Production-readiness checklist

- security — N/A; no new input surface.
- perf / scale — one pass replaces two full-text substitutions per file.
- a11y — N/A. i18n — the pass is byte-agnostic over already-decoded text.
- error / empty / loading states — an UNTERMINATED block comment or string must be abandoned rather
  than swallow the file, the rule `TOOL-aLexedStripper-1` S5 set for the token scan. AC6 pins it.
- observability — N/A.
- risks — a definition newly FOUND that should not be. Bounded by AC2's negative arm and by S4's
  regeneration diff, which must show additions only.
- testing + left-shift gates — arms in both directions, staged RED first.
- migration / rollback — `symbols.json` gains rows. Revert is a single-file revert plus a regen.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a `.js` source carries a bare block-opener inside a `//` comment followed by two
  definitions, `python tools/codebase-map/selftest.py` finds both, against neither at BASE.
- **AC2** — When a definition is written inside a REAL `/* */` block comment, it is NOT found —
  the negative arm that stops the fix becoming "strip nothing".
- **AC3** — When a `//` appears inside a string literal (`"https://x"`), the rest of that line is
  NOT truncated and a definition after it is found.
- **AC4** — When the mirror case is scanned — a `//` inside a `/* */` block — the block still closes
  correctly and a definition after it is found.
- **AC5** — When `render_comment_free` runs over any fixture, its output has the same line count as
  its input, so `file:line` reporting is unmoved.
- **AC6** — When a block comment or a string is left unterminated at EOF, `python
  tools/codebase-map/selftest.py` finds the definitions on later lines — the pass abandons the
  construct rather than swallowing the file.
- **AC7** — When each arm is staged against the code at BASE, `python
  tools/codebase-map/selftest.py` reports it RED, except AC2, AC4 and AC5, which pass at BASE and are
  regression guards rather than defect arms — stated so a green row is not misread as a fix.
- **AC8** — When `python tools/codebase-map/gen_map.py --write` runs, the diff to
  `memory/map/generated/symbols.json` contains ADDED definitions and **no removed ones**. This is
  the criterion that catches rev-1's string-blanking loss, and it is checked by diffing the
  regenerated artifact rather than by reading the pass.
- **AC9** — When `python tools/codebase-map/selftest.py` runs whole, it passes, including the
  `js definition probe ⊇ the lexicon's own set` cross-check that caught this class twice.
- **AC10** — When `bash tools/check-kit-versions.sh` runs, `KIT_CODEBASE_MAP_VERSION` is bumped and
  the generated stamps match.

## 7. Gates

The legs are read from `tools/gate-legs.json` at emission time. `python
tools/codebase-map/selftest.py`, `python tools/codebase-map/gen_map.py --write` and
`bash tools/check-kit-versions.sh` are the direct invocations §6 names.

## 8. Open questions

- **F1 — should the helper also serve `_identifier_tokens`?** Both blank comments and strings, but
  that one needs a per-suffix profile and a token SET, and this one needs preserved line structure
  and text. RESOLVED (agent, 2026-08-30, delegated): two functions. Merging them gives one function
  two return shapes and two contracts, and the seven-field profile has no meaning for a probe whose
  extension set is C-family only.

## 9. Revision log

- rev-2 · 2026-08-30 · folded the round-1 spec audit. S1 blanked string and template CONTENTS,
  which BASE never does and which the comment-ORDER defect does not require; implemented literally
  it removed eight real definitions from this repo's tracked JavaScript, because the pass models no
  regex literal and a stray delimiter blanks a live region. The pass now TRACKS strings and blanks
  only comments, so the only bytes it can remove are inside a comment. Same root as this build's
  `-2` blocker: a blanking argued from one delimiter model that the input does not obey.
- rev-1 · 2026-08-30 · initial draft, from a fixture measured against the shipped code at
  `14e21399` and from the adopter-side count taken during `aLexedStripper`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "strip comments from source while preserving line
numbers"` was run. Its ranked hits are `unfenced_lines` (`gen_build_index.py`), the `run-gates`
and `govkit` shared-seam rows, `id_pattern` and `agent-cap.topLevelArgs`. It did NOT surface
`_identifier_tokens`, which is the one function in this repo doing the nearest thing — the SECOND
probe in this build to miss the seam its unit actually relates to. Both misses are recorded rather
than smoothed, because a reuse probe that cannot find the function you are about to parallel is a
fact about the instrument, and this build ships in the kit that owns it.

The seam it matters most to find is `_identifier_tokens`' own pass, added by `TOOL-aLexedStripper-1` — and F1
records why this unit does NOT extend it: that function returns a token set over a per-suffix
profile, this one returns text with line structure intact over a single C-family profile, and one
function cannot own both contracts without carrying two.

What IS reused is the SHAPE, for the third time in two builds: one left-to-right pass with an
explicit mode, because comments and strings exclude each other and no sequence of independent regex
passes can say so. `TOOL-aLexedStripper-1` §4 records the five over-strip classes that reasoning
came from; this unit is the sixth, in the probe rather than the token scan.
