# TOOL-aPairedLexer-9 — rule 3 keeps the paren-safe view for join work

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`capFindings` falls back with
`const code = _bl.clean ? _bl.code : lines.map((l) => stripStrings(l).split('//')[0])`.
`stripStrings` blanks `''` and `""` and leaves BACKTICKS alone. So the fallback view retains template
CONTENTS, a `)` inside a lens prompt short-circuits `joinCall`, the second argument disappears, and
the helper's own `cap = 5` default is read as governing — approving a fan the call site wrote as 50.

`blankLiterals`' own docstring calls a `(` inside a prompt unbalancing a forward paren join *"the one
mechanism this rule is built on"*. The fallback `TOOL-aPairedLexer-4` added throws that mechanism
away. Round-2 review **D4**, exit 2 at BOTH 1.9 and 1.10, exit 0 at the tip.

## 2. Scope (IN)

- **S1** — the interface is STATED, because rev-1 left it to the builder and both readings broke a
  shipped arm. The FALLBACK view supplies the scan LINE SET, the call-site and helper DETECTION,
  the `intConsts` bindings, and the `lines[]` used for reporting. The PAREN-SAFE `_bl.code`
  supplies `joinCall` and `topLevelArgs` for an argument on a line already found.
- **S2** — `joinCall` and `topLevelArgs` RE-DERIVE their own match column inside `_bl.code`. They
  may not reuse a column computed against the fallback view: the two strings differ, and a
  fallback-derived column makes `joinCall` walk the wrong text and return null — a denial for
  "never closes its parens", which is green and observes nothing.
- **S2b** — a call site the paren-safe view cannot show AT ALL is a DENY naming the ambiguity,
  never a dropped finding.
- **S3** — a PAIRED arm: the fixture and its control, because the fixture alone would pass under a
  fix that merely stopped setting `dirty`.

## 3. Non-goals (OUT)

- Not the binding-merge rule itself — that is `TOOL-aPairedLexer-10`.
- Not rule 2's copy of the same defect — `TOOL-aPairedLexer-11`.
- Not reverting `TOOL-aPairedLexer-4`'s `dirty` signal: it is correct, and the bug is what the
  fallback then DOES with it.

## 4. Design

A view rule 3 cannot do its job on is not a safer view than a blank page — it is a different
fail-open. The two views answer different questions and the fix is to stop asking one view both:
`_bl.code` is paren-safe and template-blanked, so joins and paren balance come from it; the per-line
view is comment-and-template-dirty but retains bindings a blanked template hid, so `intConsts` comes
from it, filtered by `TOOL-aPairedLexer-10`'s merge.

**The trigger is LIVE in this repo.** The review instrumented `blankLiterals` over the tracked `.js`
files and `tools/workflows/drift-audit-state.js` — a shipped harness — already returns `dirty=true`,
so rules 3 and 5 judge this repo's own drift-audit workflow on the degraded view today.

**Fixture discipline.** The trigger must be an AMBIGUOUS-position slash (`if (a) /won't/.test(s)`),
not a `return`-position one: units 7 and 8 remove the latter, and a fixture whose trigger the sibling
units delete would make this live defect look fixed. The review measured exactly that.

## 5. Production-readiness checklist

- security — restores the cap enforcement on any script whose view is not clean.
- perf / scale — one extra `intConsts` call on the fallback path only.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — the denial names the CALL SITE cap again, which is the message that went missing.
- risks — none beyond the merge rule `-10` governs; joins are computed from the stricter view.
- testing + left-shift gates — S3's paired form is the gate; the fixture alone is not.
- migration / rollback — revert restores the single-view fallback.
- user docs — dossier gap list refreshed.

## 6. Acceptance criteria

- **AC1** — When the D4 fixture (an ambiguous-position declined slash, a `boundedParallel` helper
  with `cap = 5`, and a call site `boundedParallel(pick(` backtick `x)y` backtick `), 50)`) is fed to
  the hook, it exits `2` and the message names the call-site cap of 50. At the tip it exits `0`.
- **AC2** — When the fixture's trigger line is deleted, it still exits `2` — the control the review
  used, and the reason the arm is PAIRED.
- **AC3** — When a script's view IS clean, `capFindings` returns the verdict it returned before
  this unit — the fallback path is the only behaviour that moves.
- **AC4** — When `rule3: an exposed const resolves the cap and the script admits` runs, its verdict
  is whatever `TOOL-aPairedLexer-10` re-baselines it to, and this unit does not change it alone.
- **AC5** — When `rule3: a cap of 500 below an unterminated BLOCK comment denies` runs, it still
  denies AND the message still names the width. Measured: `_bl.code` for that arm is
  `["const c = ","","",""]`, so detection over the paren-safe view finds nothing and the arm
  flips to ADMIT — a fresh fail-open, which is why S1 puts detection on the fallback view.
  Asserting the MESSAGE is what separates a real denial from one that lost the number.
- **AC6** — When `rule3: a cap of 500 below an unterminated backtick denies` runs, it still
  denies. This arm pins the LINE-SET decision: `blankLiterals` emits nothing while in `tmpl`
  mode, so a build resolving S1 the other way turns this arm red instead of shipping.
- **AC7** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is
  green after it, except any this unit's sibling re-baselines by name.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`.

## 8. Open questions

none — the review states two candidate fixes and this spec picks the first, keeping `_bl.code` for
joins. The second, denying when `joinCall` disagrees across views, is strictly more disruptive and
buys nothing AC1 does not.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D4.
- rev-2 · 2026-08-31 · folded spec-audit findings 16 and 6. S1/S2 never said which view DETECTS
  call sites, and `capFindings` runs ONE array for detection, for `joinCall` column offsets and
  for `intConsts`. Read literally, S2 put detection on `_bl.code`, where the block-comment arm's
  call-site line is EMPTY — flipping a shipped DENY to ADMIT. The other reading left `joinCall`
  walking a different string at a fallback column. The interface is now stated, and AC5/AC6 name
  the two shipped arms that pin each half.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **The seam is `blankLiterals`' own
output and this unit stops discarding it** — no new mechanism is introduced, and the fix is to route
two questions to the two views that already answer them. `joinCall` and `topLevelArgs` are the
existing consumers and neither changes signature.
