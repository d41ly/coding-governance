# TOOL-aPairedLexer-4 — acceptance, with the RED observations that back it

**Status:** BUILT · rev-1 · 2026-08-30 · node a · Tier-2 · streams tooling · order 4

<!-- gen:spec-records -->
<!-- /gen:spec-records -->

## Why this record exists

`TOOL-aPairedLexer-2` shipped a fail-open TWICE, and both times the suite was green when it shipped.
A third revision would have been the third repair passing every arm that existed. So this record
states, per criterion, what was RUN and what came back — and for every gate added here, what was
staged to make it fail and what failure text appeared. A claim of "observed RED" with no witness is
the thing this build exists to stop.

## The root, restated once

Neither code view modelled a regex literal. A backtick, a quote or a `/*` inside one was read as
opening a real construct. Every prior repair mitigated the CONSEQUENCE — swap the view, widen the
flag, key off an EOF signal — and an EVEN number of phantom openers closes itself, so no EOF-based
signal could ever fire on the two-literal case. Modelling regex literals removes the ambiguity, and
that is also what made block comments safe to model again.

## Acceptance ledger

| AC | Verdict | Evidence |
|---|---|---|
| AC1 raw primitive below a regex holding a backtick denies | PASS | `rule1: a raw primitive below a regex literal holding a backtick still denies` |
| AC2 primitive between TWO regex literals denies | PASS | `rule1: a raw primitive between TWO regex literals holding backticks still denies` — measured `0` under the pre-S1 view, `2` here |
| AC3 primitive below a regex holding `/*` denies | PASS | `rule1: a raw primitive below a regex holding a block opener still denies` |
| AC4 primitive named in a block comment ADMITS | PASS | `rule1: a primitive named in a block comment now ADMITS (ceiling retired by the regex mode)`; the same fixture exits `2` at 1.10 |
| AC5 after a closing bracket a `/` is division | PASS | `rule1: after a closing bracket a slash is division, not a regex` |
| AC6 prose cannot lower a real cap | PASS | `rule3: prose inside a template cannot lower a real cap` |
| AC7 a const in a block comment cannot lower a cap | PASS | `rule3: a const inside a block comment cannot lower a real cap` |
| AC8 an EXPOSED const still resolves the cap | PASS | `rule3: an exposed const resolves the cap and the script admits`, unchanged from `TOOL-aPairedLexer-1` |
| AC9 rule 5 denies below an unterminated construct | PASS | two arms, backtick and block-comment |
| AC10 rule 5, regex literal admits / real join denies | PASS | `rule5: a .ref-shaped pattern inside a regex literal admits` + its control |
| AC11 the parity arm observed RED | PASS | witnessed, below |
| AC12 every BASE-green arm still green, kit versions pass | PASS | `125 passed, 0 failed`; `bash tools/check-kit-versions.sh` exit 0 |

## The RED observations, with witnesses

**The version-parity arm.** Staged break: an early `return []` inserted at the top of
`offendingLines`, so rule 1 finds nothing and every raw primitive admits.

- Staging witness: the patcher printed `break staged`, and `grep -c 'STAGED BREAK'` returned `1`.
- The arm went RED and named six fixtures, each as `DENY→ADMIT: 1.9 exits 2, 1.10 exits 0, on …`.
- Restore witness: `md5sum` matched the pre-break hash and the marker count returned to `0`.

**The `enumerate_exports` arm.** Staged break: the quote-tracking branch in `_has_top_level_comma`
replaced by `if False:`, restoring the string-blind walk.

- Staging witness: `break staged`, marker count `1`.
- RED text was the exact `MapError` the review predicted, on the exact fixture:
  `web-ts: m.ts: unmodelled multi-declarator export … 'export const LINK = "https://x.com/?a=1,b=2";'`
- Restore witness: hash matched, marker count `0`.

## Two failures of my own instrumentation, recorded because they nearly passed

Both are now catalogued classes.

**A staged break that never applied.** The first attempt at the parity RED used a `python - "$H"`
heredoc. On this node `python` handed the script to **node**, which parsed `import sys, io` as an ES
module and died. The bash driver ignored that and ran the suite against the UNTOUCHED hook, printing
`ok version parity … 125 passed, 0 failed`. Read through a grep for the parity line, that is
indistinguishable from a gate that survived a real break. Caught only because the node traceback
happened to be in the same captured output. → [[staged-break-never-applied]]

**A RED that fired for the wrong reason.** The first `enumerate_exports` arm omitted `root=base`, so
it raised `ValueError: … is not in the subpath of …` from a path computation and never reached its
own assertion. It was red, it was red under the staged break, and it proved nothing about string
blindness. Same family as [[fixture-passes-by-finding-nothing]], wearing the opposite mask.

The general shape both share, and the one this build keeps meeting: **an artifact whose validity
depends on a condition it does not record.**

## What the parity arm does and does not buy

It replays every deny-expected fixture against the last tracked copy with a different kit version and
fails on any that denies there and admits here. It captures those fixtures from `check()` as the
suite runs, so a fixture added later is covered by the fact of being added.

It bounds REGRESSIONS, not novelty — it cannot catch a fail-open shipped in the same version as the
fixture that would expose it. It would have caught all three shipped in this file's history. It
skips LOUDLY when no earlier tracked copy is reachable, naming the number of fixtures left
uncompared, because a skip that reads as a pass is this build's subject.

At the time of writing it compares 59 deny fixtures, 1.11 against 1.10.

## Deliberate ceilings

- **The regex/division ambiguity.** A `/` is treated as a regex only after a token that cannot end an
  expression. After an identifier, a number or a closing bracket it is division. The other guess
  would consume live code to the next `/` — a worse fail-open than the one closed. A regex literal in
  an ambiguous position is therefore still mis-modelled, and the unterminated fallback covers it at
  the per-line view's precision.
- **Two scanners, one grammar.** `renderCodeView` and `blankLiterals` now carry the same regex block
  twice. This is a real second copy of one fact and it will rot; it was not unified here because that
  refactor sits under every rule at once and this file has already shipped three fail-opens from
  exactly one view knowing something the other did not. Filed as `TOOL-aPairedLexer-5`.
