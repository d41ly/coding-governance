# TOOL-aPairedLexer-7 — start of input is a REGEX position

**Status:** SPECCED · rev-3 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`let prev = ''`, and `'})]'.includes('')` returns **`true`** in JavaScript. So at start of input the
guard `!'})]'.includes(prev)` is false, the regex branch never fires, and the first `/` in a script
is read as DIVISION. The comment three lines above lists "or start of input" among the positions
where a regex IS recognised. It is the one position where it never is.

`prev` is also never advanced past a whole-line `//` comment — that branch `break`s without touching
it — so a leading comment does not rescue it.

Round-2 review **D1**. Verified independently before speccing: the empty-string `includes` really
does return `true`, and the review's fixture really does exit `0` at the tip.

## 2. Scope (IN)

- **S1** — `prev` is initialised to a sentinel that is a regex position, in BOTH scanners
  (`renderCodeView` and `blankLiterals`).
- **S2** — arms pinning start-of-input as a regex position STRUCTURALLY, not only by instance.

## 3. Non-goals (OUT)

- Not the previous-token problem — that is `TOOL-aPairedLexer-8`, and the two are independent.
- Not the declined-slash signal — `TOOL-aPairedLexer-6`.
- Not unifying the two scanners (`TOOL-aPairedLexer-5`), though S1 touches both.

## 4. Design

`let prev = ';'`. A semicolon is already in the class of tokens that cannot end an expression, so the
existing predicate needs no new branch and start of input becomes a regex position by falling into
the rule that was always meant to cover it. The review verified that this keeps the suite green with
both copies patched; patching only `tools/hooks/` reds the mirror-drift arm, which is that arm doing
its job.

**Why an instance arm is not enough.** Every regex arm in the suite writes the literal as
`const a = /` … `/` — always after `=`, where `prev` is never empty. The suite exercises the arm the
fix covers and never the arm it does not, which is this project's own "gate the CLASS, not the
instance" broken in the commit that cites it. So AC2 asserts the code view directly.

## 5. Production-readiness checklist

- security — closes a path where the whole hook goes dark: a raw primitive, an unbounded per-item
  fan, a cap of 500 and a `.ref`-keyed join were all admitted at once.
- perf / scale — one character of initialisation.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — denial text unchanged; the denial simply happens.
- risks — none identified: a sentinel that cannot end an expression only ever ADMITS regex
  recognition where it was previously refused, and refusing it was the defect.
- testing + left-shift gates — AC2 is structural and survives a rewrite of the heuristic.
- migration / rollback — one character per copy; revert is trivial.
- user docs — the dossier's ceiling paragraph is refreshed, since it described this as narrower.

## 6. Acceptance criteria

- **AC1** — When the D1 fixture (a leading `//` comment, then a regex holding a backtick, a
  `.ref`-keyed join, `boundedParallel(work, 500)`, and a closing regex) is fed to the hook, it exits
  `2`. At the tip it exits `0`. Independently reproduced before speccing.
- **AC2** — When `node tools/hooks/agent-cap.js --selftest` renders the single line `/x/` through
  the seam `TOOL-aPairedLexer-8` S6 adds, its first output line trims to empty — a structural
  assertion that start of input is a regex position, which no future rewrite of the heuristic can
  quietly lose. Asserted for BOTH scanners, since `-8` S4 makes them share the predicate.
- **AC3** — When the same fixture is prefixed with a bare `;`, it exits `2` both before and after —
  the control the review used to isolate the empty `prev` as the sole cause.
- **AC4** — When `bash tools/hooks/agent-cap.test.sh` runs with the change applied to
  `tools/hooks/agent-cap.js` ALONE, the two-copy mirror-drift arm FAILS; with both copies patched it
  passes. Observed, not assumed.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is
  green after it.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`,
`bash tools/check-kit-versions.sh`.

## 8. Open questions

none — the defect, its control and its fix were all measured before speccing.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D1.
- rev-2 · 2026-08-31 · folded spec-audit finding 4: AC2 called `renderCodeView` directly and the file
  has no seam — no `module.exports`, and `main()` runs unconditionally — so the criterion named no
  runnable command. It now names the `--selftest` seam `TOOL-aPairedLexer-6` S4 adds, and asserts
  both scanners rather than one.
- rev-3 · 2026-08-31 · folded round-2 audit B2: the seam moved from `TOOL-aPairedLexer-6` S4 to
  `TOOL-aPairedLexer-8` S6, because this unit is order 6 and `-6` is order 7 — AC2 named a seam that
  would not exist yet when this unit landed.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **No seam to extend — this is a
one-character initialisation defect**, and the reuse question that matters is the DUPLICATION: the
value is initialised twice because the scanner exists twice. Both sites are patched here and the
underlying duplication stays tracked as `TOOL-aPairedLexer-5`; `TOOL-aPairedLexer-8` introduces the
shared predicate that begins to close it.
