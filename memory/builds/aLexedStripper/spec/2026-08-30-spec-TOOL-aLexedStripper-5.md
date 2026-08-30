# TOOL-aLexedStripper-5 — an unterminated scan falls back to the view it replaced

**Status:** CLOSED · rev-3 · 2026-08-30 · node a · Tier-2 · base 19d9b328 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-build-TOOL-aLexedStripper-1-acceptance-ledger.md](../build/2026-08-30-build-TOOL-aLexedStripper-1-acceptance-ledger.md) | journal | TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-6 |
| [2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-7-closing-diff-round2.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-7-closing-diff-round2.md) | diff-review | TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-6 |
| [2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-closing-diff-round1.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-closing-diff-round1.md) | diff-review | TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-6 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aLexedStripper-2`'s S3 fail-closed branch must stop denying legal scripts. A backtick that
sits in a code position `renderCodeView` does not model leaves the scan in template mode, and S3
then denies a harness the guard admits today. The unit that exists to remove a false-positive class
may not add one.

## 2. Scope (IN)

- **S1** — Replace S3's unconditional DENY. When `renderCodeView` reports the scan ended inside a
  template literal, `fanoutFindings` builds its view with the per-line
  `stripStrings(l).split('//')[0]` it read before `TOOL-aLexedStripper-2` — that is, it falls back
  to BASE behaviour for that script and judges it exactly as the shipped guard does.
- **S2** — ADMIT arms in `tools/hooks/agent-cap.test.sh` for every construct that can leave the scan
  in template mode without the script being malformed: a backtick inside a regex literal, inside a
  regex character class, inside a `'…'` and a `"…"` string, inside a `//` line comment, and inside a
  `/* */` block comment. Each asserts exit `0`, and each is checked against BASE first.
- **S3** — A `§4` residual line naming what `renderCodeView` still does not model, in the shape
  `memory/map/features/agent-cap.md` already uses for rule 1's accepted blind spots.

## 3. Non-goals (OUT)

- No regex-literal lexing. Distinguishing a regex literal from division needs previous-token
  context, and this unit reaches the same verdict without it.
- Not changing what `renderCodeView` returns. The `unterminated` flag stays; only what
  `fanoutFindings` does with it changes.
- Not touching rules 1, 3 and 5, per `TOOL-aLexedStripper-2` §3.

## 4. Design

### The defect

`renderCodeView` inherits `blankLiterals`' code-mode branch set (`agent-cap.js:504-541`), which
tests `//`, `/*`, a backtick, `'` and `"` and nothing else. A JavaScript regex literal is none of
those, so a backtick inside one opens template mode and never closes. The scan reaches EOF in
template mode, which is exactly S3's DENY trigger.

Measured against `git show 19d9b328:tools/hooks/agent-cap.js`, a correct five-lens harness prefixed
with one line:

| first line | BASE | S3 as written | this unit |
|---|---|---|---|
| `const re = /` backtick `/` | 0 ADMIT | **2 DENY** | 0 ADMIT |
| `const re = /[` backtick `~]/g` | 0 ADMIT | **2 DENY** | 0 ADMIT |
| none (control) | 0 | 0 | 0 |

### Why the fallback, and not the two fixes the audit named

The round-2 report offered tracking regex context, or narrowing the flag to a shape a legal script
cannot produce. A third option is smaller than both and has a property neither has.

**Narrowing the flag does not work here, and the obvious narrowing is worse than useless.** The
tempting predicate is "deny only when the blanked-away region holds an `agent(`" — but in the
measured case the harness's own lens fan sits below the regex literal, so that predicate still
denies. It reads as a tightening and is not one.

**The fallback is correct by construction.** For any script whose scan ends in template mode, the
view becomes the one the shipped guard uses, so the verdict IS the shipped guard's verdict. The
change cannot move a verdict in either direction for that class: not a DENY to an ADMIT, because
BASE's DENY is what it returns; not an ADMIT to a DENY, for the same reason. That is a stronger
guarantee than a hand-checked predicate, and it needs no model of a construct nobody has enumerated.

The fail-open S3 was written to close stays closed. `TOOL-aLexedStripper-2` §4 shape 1 — an
unbounded fan below an unterminated backtick — is DENIED at BASE, measured, so the fallback denies
it too. S3's purpose was never "fail closed"; it was "do not admit what BASE denies", and the
fallback delivers exactly that.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — the branch in `fanoutFindings`, and the residual line.
- `tools/hooks/agent-cap.test.sh` — the six ADMIT arms.

### Alternatives rejected

- **Track regex/division context in `renderCodeView`.** Rejected: it needs previous-token state,
  it is the classic JavaScript lexing ambiguity, and it buys a verdict the fallback already gets.
- **Deny only when the hidden region holds an `agent(`.** Rejected on measurement — it denies the
  reproduced case, because the harness's fan is below the regex literal.
- **Drop S3 entirely and never fail closed.** Rejected: that is rev-1's design, whose fail-open
  round-1 blocker 1 measured.

## 5. Production-readiness checklist

- security — the guard's fail-open direction is what matters, and the fallback returns BASE's
  verdict, which is the verdict the guard ships today. AC3 pins it.
- perf / scale — one extra per-line map, only for scripts that end in template mode.
- a11y — N/A, no user interface.
- i18n — N/A.
- error / empty / loading states — this unit IS the error state. An empty script ends in code mode
  and is unaffected.
- observability — unchanged; the hook writes its verdict to stderr.
- risks — the residual is that `renderCodeView` still models no regex literal, so such a script gets
  BASE's precision rather than the improved one. That is a smaller, named loss, and S3 records it.
- testing + left-shift gates — six ADMIT arms, the ADMIT half round-1 finding 31 asked for.
- migration / rollback — none; single-file revert.
- user docs — the `agent-cap` dossier's blind-spot list gains the residual.

## 6. Acceptance criteria

- **AC1** — When a five-lens harness is prefixed with a regex literal containing a backtick,
  `node tools/hooks/agent-cap.js` exits `0`, as at BASE. Under `TOOL-aLexedStripper-2` S3 as
  written it exits `2`.
- **AC2** — When the same harness is prefixed with a regex character class containing a backtick,
  it exits `0`, as at BASE.
- **AC3** — When an unbounded fan is written below an unterminated backtick, it exits `2`, as at
  BASE — the fail-open S3 existed to close is still closed.
- **AC4** — When a backtick appears inside a `'…'` string, a `"…"` string, a `//` comment and a
  `/* */` block, each above a correct five-lens fan, `bash tools/hooks/agent-cap.test.sh` reports
  exit `0` for each.
- **AC5** — When the whole `TOOL-aLexedStripper-2` acceptance suite is re-run, all 29 shapes still
  hold, measured by the harness recorded in
  `memory/builds/aLexedStripper/build/2026-08-30-build-TOOL-aLexedStripper-2-base-measurements.md`.
- **AC6** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm that passes at BASE passes.

## 7. Gates

The legs are read from `tools/gate-legs.json` at emission time, not listed here. This unit's
subject is the `agent-cap` kit, so its self-test leg is guarded and runs under `GATE_SELFTESTS=1`;
`bash tools/hooks/agent-cap.test.sh` is the direct invocation and is what AC4 and AC6 name.

## 8. Open questions

- **F1 — should the residual also be recorded as a backlog row?** The dossier line S3 adds is the
  durable record, and a backlog row would be a second copy of one fact.
  RESOLVED (agent, 2026-08-30, delegated): dossier line only. The two-answers-to-one-question class
  is on this diff's own bug-class checklist.

## 9. Revision log

- rev-1 · 2026-08-30 · promoted from the round-2 spec audit's blocker 1+37 at the NON-CONVERGENT
  exit, per `BUILD-METHOD.md` M4. The blocker was reproduced against BASE before this spec was
  written, and the fallback was measured to close it while holding all 29 of
  `TOOL-aLexedStripper-2`'s shapes.
- rev-2 · 2026-08-30 · folded the closing diff review's blocker 1, which found the fallback did not
  fire for every mode that can outlive a scan. `renderCodeView` reported `stack.length > 0`, and
  BLOCK mode pushes nothing onto that stack — so an unterminated block-comment opener ended the scan
  with an empty stack, blanked everything below it, and ADMITTED an unbounded fan the shipped hook
  DENIES. Reproduced, then fixed by reporting `stack.length > 0 || mode !== 'code'`. S1 is unchanged
  in intent and the fallback is now reached from any surviving mode.
  The review's second blocker — an unpaired quote in code position — is REFUTED: four fixtures were
  run and all four DENY at both BASE and HEAD, because this file's quote handling mirrors
  `stripStrings`' own and therefore cannot regress against it.

- rev-3 · 2026-08-30 · folded the closing review's ROUND 2, which found rev-2's repair insufficient
  and a second fail-open beside it. Both were reproduced before folding, and one of them refutes
  this spec's own rev-2 claim.
  **The widened flag was not enough.** Reporting `mode !== 'code'` catches an opener that never
  closes; it does not catch one BORNE IN A REGEX LITERAL and closed by a later ordinary closer,
  which returns the scan to code mode with an empty stack while the span between is already blanked.
  Round 1 said to delete the block branch and rev-2 shipped the smaller repair instead. It is now
  deleted: this view blanks no block comment at all, which is what the view it replaced also did, so
  it cannot regress against it, and un-blanked comment text can only ADD apparent code rather than
  hide it.
  **Rev-2's refutation of round 1's blocker 2 was WRONG, and this spec now says so.** It claimed an
  unpaired quote cannot regress because the handling mirrors `stripStrings`. The handling did not
  mirror it: the loop ran to end of line and then appended a closer the source never had. The
  verdict only moves when the fan sits on the SAME line as the quote, which is the shape rev-2's
  four fixtures did not have — `if (/won't/.test(args.s)) await Promise.all(all.map((f) =>
  agent(f.prompt)))` ADMITTED while its apostrophe-free control DENIED. An unpaired quote is now
  left as ordinary text, which is what `stripStrings` does and what rev-2 wrongly asserted.
  Six regression arms landed with the fix, one per shape, because round 2's HIGH was that none of
  the previous three fixes had one.

## 10. Reuse audit

The seam is `stripStrings` at `agent-cap.js:70` — the view `fanoutFindings` read before
`TOOL-aLexedStripper-2` moved it. This unit does not add a mechanism; it keeps the old one as the
fallback path, which is why it is three lines rather than a lexer. `blankLiterals` and `stripStrings`
were already ranked by `tools/codebase-map/reuse_lookup.py` as the two candidates for this
behaviour, recorded in `TOOL-aLexedStripper-2` §10, and no fresh probe was owed for a unit whose
answer is "keep the function that is already there".

Recall terms carried from that unit, for M7 re-runs: `agent-cap stripStrings blankLiterals template
literal lens array bounded receiver interpolation view fan-out counter prose`.
