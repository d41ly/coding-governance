---
slug: aLexedStripper
node: a
opened: 2026-08-30
streams: tooling
roster: TOOL
ids: TOOL-aLexedStripper-1 TOOL-aLexedStripper-2
authorized-by: prompt
---

# aLexedStripper — two kit scanners stop reading prose as code

## The problem this build exists to solve
Two shipped kits scan source with regexes that do not know what language they are looking at, and
both mis-read ordinary prose as code structure. Both were found by an adopter (`d41ly/incms`) and
filed there as gov asks, because both files are role `engine` in that tree and a local edit would be
a policy violation.

**`codebase-map`'s `_identifier_tokens`** (`tools/codebase-map/map_lib.py:636`) applies C-family
comment syntax to every language. `_BLOCK_COMMENT_RE = /\*.*?\*/` with `DOTALL` has no language
gate, so a `/*` sequence anywhere opens a comment that runs until the next `*/`. Measured on
inCMS `services/api/app/main.py`: a MIME glob `application/*` inside a docstring opens a span that
closes 674 lines later on an `on*` attribute glob, and the file's identifier count falls
**1616 → 88**, reproducing the reported figure exactly. That is the input to `fan_in`, which is the
ranking behind `reuse_lookup.py` — the probe template §10 and charter §1 make a Definition-of-Ready
item. The audit is not merely degraded on Python; it is blind.

**The damage is far wider than the row that reported it.** `ABL-bCandidLoupe-1` says "24 .py files
affected". Measured across both trees at this build's BASE, counting a file as damaged when it loses
more than half its identifiers: **107 files in gov, 1374 in inCMS**. Per extension, the share of
identifiers that survive: gov `.sh` 16.5%, `.js` 19.9%, `.py` 51.5%; inCMS `.js` 15.4%, `.sh` 19.1%,
`.ts` 21.5%, `.tsx` 30.4%, `.py` 66.7%. `.githooks/gate-env.sh` keeps **0 of 250**. The C-family
languages the regexes were written for are damaged too, because comments are stripped BEFORE
strings, so a `//` inside a URL truncates its line and a `#` inside a string eats the rest of one.
Five distinct over-strip classes, one root: a language-blind regex chain in the wrong order.

**`agent-cap`'s five-lens allowance** (`tools/hooks/agent-cap.js`) proves a lens array bounded by
counting its top-level elements, over a view built by `stripStrings`, which blanks quoted strings
per line and deliberately leaves template literals alone. Lens prompts ARE template literals full of
English, so their punctuation is counted as code structure. Reproduced at gov 1.8 against a correct
five-element fan: a literal `...` in lens prose is read as a spread, the array becomes unmeasurable,
and the harness is DENIED. Unbalanced brackets in prose shift the same count. The refusal talks
about verifier arity and names nothing about prose, so the operator restructures a harness that was
already correct.

## Expected improvements
- The reuse audit charter §1 mandates can actually see Python, TypeScript and shell identifiers.
- A correct five-lens review harness stops being denied for its English, in this repo and in every
  adopter, without either of them hand-fitting prose to a counter.
- Both fixes land UPSTREAM, so adopters take them by re-pull with no role flip and no local delta.
- Each fix reuses a seam that already exists rather than adding a second answer.

## Detriments if this is not built
- Every DoR reuse audit in both trees keeps reading a corpus with most of its identifiers deleted,
  and reports "no existing seam fits" for seams that are there — the exact failure M5 warns is
  indistinguishable from an honest miss.
- Adopters keep writing lens prose around a counter's punctuation bugs, and the gotcha that teaches
  them to do it prescribes U+2019, which fixes nothing the ASCII form actually broke.
- Both rot further with every kit sync: `ABL-bCandidLoupe-1` records that the defect already
  survived one.

## Build-level rules
- **Upstream is the side, and the adopter's blocker does not reach it.** The trap
  `ABL-dPinnedVintage-5` §8 F3 walked for `extract.py` — patch locally, flip the role to `diverged`,
  insert a delta marker, move the blob OID, red kit-sync check 8, and wait on the `install.index`
  regeneration `ABL-dPinnedVintage-3` owns while that row is BLOCKED — is a property of the ADOPTER's
  tree. In gov both files are role `engine` and gov is where they are authored. Nothing here is
  blocked by that row, and the same precedent chose the same side.
- **A stripper is a lexer, not a regex chain.** Comments and strings are mutually exclusive and a
  regex pass over each cannot express that; the order of two such passes decides which one wins, and
  every ordering is wrong for some input. One left-to-right pass with a per-language profile is the
  root-cause shape, and `blankLiterals` in `agent-cap.js` is the in-repo precedent for it.
- **Never widen a guard's blind spot to fix its false positives.** `agent-cap` may not stop seeing a
  real `agent(` call. Interpolations carry real code, so the interpolation-span second view rule 5
  already uses is part of the fix, not an optional extra — blanking template contents alone is a
  fail-open change and would be a defect, not a fix.
- **Both instruments are measured before and after, over the same real corpus**, and the after-figure
  is derived by the same probe. A stripper change asserted rather than measured is how the first one
  shipped.
- **Every fix here is gated by its own failing case, observed RED before it is wired** (§7). A gate
  whose failure has only ever been reasoned about is an assertion about nothing.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aLexedStripper-1` | 2 | `_identifier_tokens` becomes one language-aware pass over a per-suffix comment/string profile |
| 2 | `TOOL-aLexedStripper-2` | 2 | `agent-cap`'s bounded-receiver view becomes `blankLiterals` plus the interpolation spans rule 5 already reads |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 2 unit(s) · node a · opened 2026-08-30 · streams tooling
ids TOOL-aLexedStripper-1 TOOL-aLexedStripper-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aLexedStripper-1 — `_identifier_tokens` becomes one language-aware pass](spec/2026-08-30-spec-TOOL-aLexedStripper-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-08-30 |
| [TOOL-aLexedStripper-2 — `agent-cap`'s lens counter reads a template-aware view](spec/2026-08-30-spec-TOOL-aLexedStripper-2.md) | 2 | 2 | SPECCED | rev-1 | 2026-08-30 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: TOOL-aLexedStripper-2.

Ids no `spec-audit` record has ever named: TOOL-aLexedStripper-1 TOOL-aLexedStripper-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aLexedStripper-1` | no |
| 2 | `TOOL-aLexedStripper-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
