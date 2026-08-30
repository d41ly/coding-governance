# TOOL-aPairedLexer-8 — decide on the previous TOKEN, in one shared predicate

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`!/[A-Za-z0-9_$]/.test(prev)` cannot distinguish `return` from an identifier. Every keyword that
cannot end an expression — `return typeof case in of instanceof new delete void throw yield await` —
therefore puts the following `/` in a DIVISION position. `return /re/.test(s)` is the commonest regex
position in real JavaScript, and a workflow that parses a markdown report writes it without thinking.

Round-2 review **D2**, a measured DENY→ADMIT against the shipped 1.9.

This is NOT the accepted ceiling restated. The ceiling comment excuses the ambiguity as "after an
identifier, a number, or a closing bracket" — an honest description of a NARROW residual. The
character test makes the residual far wider than the sentence describes.

## 2. Scope (IN)

- **S1** — a shared predicate deciding whether a `/` starts a regex, written ONCE and called from
  both scanners. It keeps a trailing-word buffer beside `prev` and treats `/` as a regex start when
  the preceding WORD is one of the keywords that cannot end an expression.
- **S2** — both `renderCodeView` and `blankLiterals` call it; neither carries its own copy.
- **S3** — a TABLE-DRIVEN arm over the keyword class, not the two instances that happened to be
  found.

## 3. Non-goals (OUT)

- Not full JavaScript lexing. After an identifier, a number or a closing bracket, `/` stays DIVISION
  — that residual is real, is the file's stated ceiling, and `TOOL-aPairedLexer-6` is what makes it
  announce itself.
- Not merging the two scanners wholesale (`TOOL-aPairedLexer-5`). S1 extracts ONE predicate, which is
  the part D2 forces; the rest of the duplication stays tracked.

## 4. Design

The keyword list is CLOSED and is the set of JavaScript tokens that cannot end an expression:
`return typeof case in of instanceof new delete void throw yield await`. A word-boundary match on the
trailing word decides; everything else falls through to the existing character rule.

**Written once, called twice — and that is load-bearing, not tidiness.** The file already carries the
regex block twice, and one view knowing something the other did not caused two of the three prior
fail-opens. The bug-class checklist selected `two-answers-to-one-question` for these paths before a
line was written, which is the same finding arriving from the other direction.

## 5. Production-readiness checklist

- security — closes a wide, ordinary-looking admit path in the fan-out guard.
- perf / scale — one trailing-word buffer per scanner; no change in cost class.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — denial text unchanged.
- risks — a keyword treated as a regex position where a division was meant is possible in principle
  (`a = b in /re/` is not valid JS, so the class is safe); the direction of error is fail-CLOSED,
  since recognising a regex blanks it rather than exposing a call.
- testing + left-shift gates — S3 gates the CLASS, which is the rule this diff broke in the commit
  citing it.
- migration / rollback — revert restores the character test.
- user docs — the dossier's ceiling paragraph is narrowed to what actually remains.

## 6. Acceptance criteria

- **AC1** — When the `return /` backtick `/.test(s)` fixture with a raw `parallel(D.map(...))`
  between two such functions is fed to the hook, it exits `2`. At 1.9 it exits `2`, at the tip `0`.
- **AC2** — When the markdown-fence fixture (a `function isFence(l) { return /^` fence `/.test(l) }`
  around a raw `parallel(...)`) is fed to the hook, it exits `2`; `0` at the tip.
- **AC3** — When the code view is taken of each of `return /re/`, `typeof /re/`, `case /re/:`,
  `throw /re/` and `yield /re/`, the regex is blanked in every one — the table-driven class arm.
- **AC4** — When the predicate is called from both scanners, `grep -c` over `agent-cap.js` for the
  keyword list finds exactly ONE occurrence. A second copy is the defect this unit exists to avoid.
- **AC5** — When a genuine DIVISION follows a closing bracket, it is still division:
  `rule1: after a closing bracket a slash is division, not a regex` stays green.
- **AC6** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is green
  after it.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`,
`bash tools/check-kit-versions.sh`.

## 8. Open questions

*(none.)*

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D2.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **No existing seam fits, and the probe
says why**: `renderCodeView` and `blankLiterals` are both `fan-in 0`, so there is no shared scanner to
wire through — which is the shape of a duplicated grammar rather than a reused one. This unit creates
the first shared predicate between them, so it is the beginning of `TOOL-aPairedLexer-5`'s answer
rather than another copy. `buildCommandView` in `tools/hooks/scratch-guard.js` is the nearest
structural cousin, also `fan-in 0`; it scans shell text, shares no grammar, and folding them would
couple two unrelated guards.
