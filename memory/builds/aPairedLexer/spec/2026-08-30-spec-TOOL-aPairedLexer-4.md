# TOOL-aPairedLexer-4 — both views model regex literals, and the ceiling retires

**Status:** SPECCED · rev-1 · 2026-08-30 · node a · Tier-2 · base b3d1ecd8 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-build-TOOL-aPairedLexer-4-acceptance.md](../build/2026-08-30-build-TOOL-aPairedLexer-4-acceptance.md) | journal | — |
| [2026-08-30-review-TOOL-aPairedLexer-1-2-3-4-diff-round2.md](../reviews/2026-08-30-review-TOOL-aPairedLexer-1-2-3-4-diff-round2.md) | diff-review | TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3 |

<!-- /gen:spec-records -->

## 1. Goal

Three consecutive revisions of this hook's code views have each shipped a fail-open, and they share
ONE root: neither scanner models a regex literal, so a backtick, a quote or a `/*` inside one is read
as opening a real construct. Every repair so far has been a MITIGATION of that — swap the view, widen
the flag, fall back on an EOF signal — and each was defeated by a different spelling of the same
ambiguity, because an EVEN number of phantom openers closes itself and the signal never fires.

This unit removes the ambiguity instead of compensating for it, in BOTH views, and takes the
consequences: modelling regex literals is what makes block comments safe to model again, so the
ceiling `TOOL-aPairedLexer-2` §3 retained is retired by measurement rather than waived.

It also closes the round-1 diff review's D2, D3, D4 and D5, which are four faces of the same root.

## 2. Scope (IN)

- **S1** — `renderCodeView` models regex literals and consumes them whole. A `/` opens a regex only
  after a token that cannot END an expression; after an identifier, a number or a closing bracket it
  is DIVISION. A character class may hold an unescaped `/`.
- **S2** — `renderCodeView`'s block-comment branch is RESTORED. `TOOL-aLexedStripper-5` deleted it
  because a `/*` inside a regex literal was indistinguishable from a real one; S1 removes exactly
  that indistinguishability, so the reason for the deletion no longer holds.
- **S3** — `blankLiterals` gains the same regex mode, and stops fabricating a closing quote for an
  UNPAIRED one. It reports `dirty` alongside `endMode`, and a derived `clean`.
- **S4** — `capFindings` keys its fallback on `clean` rather than `endMode === 'code'`, and when the
  view is not clean it CROSS-CHECKS integer bindings between the two views: a name both views bind to
  different integers resolves to the LARGER, which for a cap is fail-closed.
- **S5** — `scanJoinFindings` takes the same fallback, which it currently discards.
- **S6** — A VERSION-PARITY arm: every deny-expected fixture in the suite is replayed against the
  last tracked copy carrying a different kit version, and any that denies there and admits here fails
  the suite. It skips LOUDLY when no earlier copy is reachable.
- **S7** — Bump `KIT_AGENT_CAP_VERSION` across its four carriers.

## 3. Non-goals (OUT)

- **The two scanners are NOT unified.** `renderCodeView` preserves interpolation bodies as code and
  `blankLiterals` blanks template contents, so they emit different views of the same scan. They
  should share one scanner with two emitters; doing that mid-build, under an open review, would put
  an untested refactor under every rule at once. Filed as a backlog row instead.
- Not touching rules 2 or 4, `CAP`, `MAX_VERIFIERS` or `MAX_LENSES`.
- Not attempting full JavaScript lexing. The regex/division rule here is deliberately conservative
  and its residual is named in §4.

## 4. Design

### Where a `/` starts a regex

This is the classic JavaScript ambiguity and the reason `TOOL-aLexedStripper-5` declined to model
block comments at all. The rule adopted is the conservative half: a regex is recognised only after a
token that cannot end an expression — an operator, an opening bracket, a comma, a colon, a semicolon,
or start of input. After an identifier, a number, or a closing bracket the `/` is DIVISION.

Guessing the other way would consume live code to the next `/`, which is a WORSE fail-open than the
one being closed: it would blank real calls. The residual is therefore a regex literal in an
ambiguous position, and the `unterminated` / `clean` fallback still covers what this cannot. This is
a ceiling, stated as one, and it is the reason S6 exists.

### Why the cross-check in S4 is not optional

The fallback view strips neither template contents nor block comments, and `intConsts` matches its
pattern anywhere in the text it is given. Later binding wins, so a `const K = 5` written in PROSE
overrode a real `const K = 500` and turned a correct denial of a 500-wide fan into an approval. The
review measured three spellings, all `node --check` clean, all denying at 1.9 and admitting at HEAD.

Taking the LARGER of two disagreeing bindings is fail-closed for a cap. A name only ONE view binds is
not a disagreement — that is the exposed-binding case the fallback exists to serve, and the arm
pinning it stays green.

### What S6 buys, and what it does not

It bounds REGRESSIONS, not novelty: it cannot catch a fail-open shipped in the same version as the
fixture that would expose it. It would have caught all three shipped so far, because each was a
script the previous version denied. It costs one extra hook invocation per deny fixture.

## 5. Production-readiness checklist

- security — this IS the security surface: the unit closes four fail-opens in the only mechanical
  control against an unbounded agent burst. No new surface added; `tools/hooks/agent-cap.js` gains
  no I/O, no network and no filesystem access.
- perf / scale — one extra character-scan branch per line, and the parity arm costs one extra
  `node` invocation per deny fixture (59 today) on `bash tools/hooks/agent-cap.test.sh` only. The
  hook itself is unchanged in cost class.
- a11y — N/A, no user interface.
- i18n — N/A, the scanner is byte-oriented over JavaScript source.
- error / empty / loading states — an empty or unparseable payload still exits 0 by design; the
  suite's payload-builder guard already fails an arm that produces nothing.
- observability — every denial names the FORM it refused, unchanged; the parity arm prints the
  offending fixture and both verdicts rather than a bare count.
- risks — the regex/division ambiguity is the one residual and is stated as a ceiling in §4. The
  duplicated scanner is the rot risk, filed as `TOOL-aPairedLexer-5`.
- testing + left-shift gates — the version-parity arm generalises the CLASS rather than the three
  instances; `test_enumerate_exports_string_borne_punctuation` gates the string-blindness class.
- migration / rollback — reverting the commit restores 1.10 behaviour; no data, no artifact format
  and no committed contract changes shape. `memory/map/generated/` is re-rendered, not migrated.
- user docs — `memory/map/features/agent-cap.md` is the dossier and is updated in the same commit;
  no `help/` page exists for a hook.

## 6. Acceptance criteria

Every criterion below states the verdict at BASE, so a green arm observes the CHANGE rather than a
state that was already true.

- **AC1** — A raw primitive below a regex literal holding a backtick exits `2`. At BASE (1.9's
  per-line view) this already exits `2`; under `TOOL-aPairedLexer-2` rev-1's view it exited `0`.
- **AC2** — A raw primitive between TWO regex literals holding backticks exits `2`. This is the
  even-count case the EOF signal cannot see: measured `0` under the pre-S1 view, `2` here.
- **AC3** — A raw primitive below a regex literal holding a `/*` exits `2`.
- **AC4** — A primitive named inside a `/* */` block comment exits `0`. At BASE it exits `2`. This
  RETIRES `TOOL-aPairedLexer-2` AC6, which pinned the same fixture at `2` as a ceiling.
- **AC5** — After a closing bracket, a `/` is division: a script whose next line opens a genuine
  template prompt naming a primitive still exits `0`.
- **AC6** — Prose inside a template cannot LOWER a real cap: a `const K = 500` fan with a fabricated
  `const K = 5` in prompt prose exits `2`. At BASE this exits `0` — the D2 repro.
- **AC7** — A `const` inside a block comment cannot lower a real cap: same verdicts.
- **AC8** — An EXPOSED `const K = 5` below an unterminated template still resolves the cap and the
  script exits `0` — the removing direction, unchanged.
- **AC9** — A `.ref`-keyed join below an unterminated construct exits `2` (rule 5's D5 fallback).
- **AC10** — A `.ref` string inside a REGEX LITERAL exits `0`, and a genuine `.ref`-keyed join still
  exits `2`. S3 changes rule 5's view, so both directions are pinned.
- **AC11** — The version-parity arm passes, and has been OBSERVED RED against a staged fail-open in
  `offendingLines` — with the staging itself witnessed, not assumed.
- **AC12** — Every arm green at BASE is still green, and `bash tools/check-kit-versions.sh` passes.

## 7. Gates

The legs are read from `tools/gate-legs.json` at emission time. The direct invocations this unit
owns are `bash tools/hooks/agent-cap.test.sh`, `bash tools/check-kit-versions.sh` and
`python tools/codebase-map/selftest.py`.

## 8. Open questions

- **F1 — should the two scanners become one?** Yes, and not here; see §3. The duplicated regex block
  is a real second copy of one fact and it will rot. Backlog row `TOOL-aPairedLexer-5`.
- **F2 — does S3 weaken rule 5?** A regex literal is now blanked, so a ban pattern can no longer
  match text inside one. That REMOVES false positives and cannot hide a real join, because a join
  cannot be written inside a regex literal. AC10 pins both directions. The `scanJoinFindings` S2
  comment claiming "a regex LITERAL survives the blanking" becomes false and is corrected.

## 9. Revision log

- rev-1 · 2026-08-30 · specced after the round-1 diff review's D1 was closed by a regex-aware
  `renderCodeView`, which retired `TOOL-aPairedLexer-2`'s ceiling as a side effect and made D2–D5 one
  unit's worth of work rather than four patches.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py agent-cap regex literal scanner view`, run 2026-08-30
against a corpus of 591 symbols and 19 affordance seams.

**No existing seam fits, and the probe says so precisely.** The three candidates it surfaces inside
this file — `blankLiterals`, `renderCodeView` and `capFindings` — are the functions this unit
EDITS, each reported at `fan-in 0`, so there is no shared scanner to wire through and none of them
is a seam by the kit's own threshold. `buildCommandView` in `tools/hooks/scratch-guard.js` is the
nearest structural cousin, also `fan-in 0`; it scans shell command text rather than JavaScript
source, shares no grammar, and folding them would couple two unrelated guards.

The probe's own output is therefore the evidence for `TOOL-aPairedLexer-5`: the two views that
should share a scanner are both `fan-in 0` in the same file, which is exactly the shape of a
duplicated grammar rather than a reused one. This unit adds the second copy knowingly and files the
row; it does not pretend a seam exists.
