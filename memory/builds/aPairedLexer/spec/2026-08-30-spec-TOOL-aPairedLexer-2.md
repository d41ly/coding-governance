# TOOL-aPairedLexer-2 — rule 1 stops reading a lens prompt as a call

**Status:** SPECCED · rev-2 · 2026-08-30 · node a · Tier-2 · base 14e21399 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-build-TOOL-aPairedLexer-1-base-measurements.md](../build/2026-08-30-build-TOOL-aPairedLexer-1-base-measurements.md) | journal | TOOL-aPairedLexer-1 TOOL-aPairedLexer-3 |
| [2026-08-30-review-TOOL-aPairedLexer-1-2-3-spec-audit-round1.md](../reviews/2026-08-30-review-TOOL-aPairedLexer-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-1 TOOL-aPairedLexer-3 |

<!-- /gen:spec-records -->

## 1. Goal

`offendingLines` must stop denying a harness because its PROSE names a primitive. A lens prompt is a
backticked template literal, `stripStrings` leaves backticks alone, so `parallel(` written as English
inside a prompt is read as a call. This is the last member of the class
`TOOL-aLexedStripper-2` removed from rule 2, in the rule next door.

## 2. Scope (IN)

- **S1** — `offendingLines` builds its view with `renderCodeView(script)` instead of the per-line
  `stripStrings(l).split('//')[0]`. Template prose is blanked, `${…}` interpolation bodies are kept
  as code, and the `gov:bounded-fanout` marker check keeps reading the RAW line.
- **S1b** — **and it falls back to the per-line view when the scan ends unterminated**, the same
  branch `TOOL-aLexedStripper-5` landed for rule 2. Rev-1 omitted this and it was a REPRODUCED
  fail-open in the ban rule: `renderCodeView` models no regex literal and no block comment, so one
  stray backtick in either blanks every later line and a genuine raw `parallel(` below it is
  ADMITTED where the shipped hook DENIES. Measured on two spellings, both legal JavaScript.
- **S2** — Fixtures in `tools/hooks/agent-cap.test.sh` in both directions: prose naming a primitive
  inside a prompt ADMITS, a real raw primitive still DENIES, and a primitive written inside a `${…}`
  interpolation still DENIES.
- **S3** — Bump `KIT_AGENT_CAP_VERSION`.

## 3. Non-goals (OUT)

- **The block-comment ceiling STAYS, and is the reason this unit fixes two of three rows rather than
  three.** See §4.
- Not touching rules 2, 3 or 5. Rule 3's blindness is `TOOL-aPairedLexer-1`.
- Not changing `CAP`, `MAX_VERIFIERS` or `MAX_LENSES`.

## 4. Design

### The defect

`offendingLines` (`agent-cap.js:80`) builds `stripStrings(line).split('//')[0]` per line. That blanks
`'…'` and `"…"` and truncates at `//`, and does nothing about a backtick. Measured against the
shipped hook:

| where the prose sits | verdict | correct |
|---|---|---|
| a backticked lens prompt naming `parallel(` | **2 DENY** | 0 |
| a backticked lens prompt naming `pipeline(` | **2 DENY** | 0 |
| a `/* */` block comment | **2 DENY** | 0 |
| a `//` line comment | 0 | 0 |
| control: clean prose | 0 | 0 |
| control: a REAL raw primitive | 2 DENY | 2 |

### Why the block-comment row is NOT fixed here

`renderCodeView` deliberately blanks NO block comment. `TOOL-aLexedStripper-5` deleted that branch
after measuring that it could not tell a real block-opener from one inside a regex literal, and that
blanking on that basis HID a fan-out — a fail-open in the guard. Re-adding block blanking for rule 1
would reintroduce exactly that unsound strip, and rule 1 is the rule where hiding a primitive is
worst.

So this unit fixes the two rows it can fix soundly and leaves the third as the documented
fail-closed ceiling it already is, in `memory/map/features/agent-cap.md` and in this file's header.
That is a smaller claim than "rule 1 stops reading prose as a call", and §6 states it as such.

### Why interpolations must survive

A `parallel(` inside `${…}` is CODE and can execute. `renderCodeView` keeps interpolation bodies
verbatim, which is why it is the right view and a blanket template-blanker is not. AC4 pins it.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — the view in `offendingLines`, and the version constant.
- `tools/hooks/agent-cap.test.sh` — the arms.
- `memory/map/features/agent-cap.md` — the block-comment ceiling line gains the reason it now
  survives deliberately rather than by omission.

### Alternatives rejected

- **Blank block comments for rule 1 too.** Rejected on `TOOL-aLexedStripper-5`'s measurement: the
  strip is unsound and can hide a real primitive.
- **Keep `stripStrings` and special-case backticks in `offendingLines`.** Rejected: a second state
  machine beside `renderCodeView`, which is the two-answers-to-one-question class.

## 5. Production-readiness checklist

- security — rule 1 is the raw-primitive ban. The change makes it see LESS, so the fail-open
  direction is the risk and §6 spends four criteria on it.
- perf / scale — one `renderCodeView` pass, already computed for rule 2 in the same invocation.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a script ending inside a template literal yields a blanked tail;
  rule 1 then sees less. AC5 pins that a real primitive above the opener is still caught.
- observability — unchanged.
- risks — a primitive hidden inside a template literal that is somehow reachable. It is not: a
  template literal is a string, and the executable half is the interpolation, which S1 preserves.
- testing + left-shift gates — arms in both directions, staged first.
- migration / rollback — none; single-file revert.
- user docs — the dossier line named in §4.

## 6. Acceptance criteria

- **AC1** — When a five-lens harness names `parallel(` in a backticked prompt,
  `node tools/hooks/agent-cap.js` exits `0`, against `2` at BASE.
- **AC2** — When it names `pipeline(` the same way, it exits `0`, against `2` at BASE.
- **AC3** — When a script calls a REAL raw `parallel(items.map(...))`, it exits `2`, as at BASE.
- **AC4** — When a raw `parallel(` is written inside a `${…}` interpolation, it exits `2` — the
  interpolation is code and the view must not blank it.
- **AC5** — When a real raw primitive sits ABOVE an unterminated backtick, it exits `2` — the
  blanked tail must not hide a call that precedes it.
- **AC5b** — When a real raw primitive sits BELOW a regex literal containing a backtick, it exits
  `2`. Under rev-1's S1 this exits `0`, measured. This is the criterion rev-1 lacked, and its
  absence is why the fail-open reached the spec: AC5 pinned only the ABOVE case, which is green both
  before and after and therefore observes nothing about the change.
- **AC5c** — When a real raw primitive sits BELOW a block comment containing a backtick, it exits
  `2`, likewise `0` under rev-1.
- **AC6** — When a primitive is named inside a `/* */` block comment, it exits `2`, UNCHANGED from
  BASE. This unit does not fix that row and the arm pins the ceiling rather than the bug.
- **AC7** — When a `gov:bounded-fanout` marked helper line is present, it is still exempt — the
  marker is read from the RAW line and S1 does not move it.
- **AC8** — When each new fixture is staged against the shipped code first,
  `bash tools/hooks/agent-cap.test.sh` reports the BASE verdicts §4's table records.
- **AC9** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm that passes at BASE passes.

## 7. Gates

The legs are read from `tools/gate-legs.json` at emission time. `bash tools/hooks/agent-cap.test.sh`
and `bash tools/check-kit-versions.sh` are the direct invocations §6 names.

## 8. Open questions

- **F1 — is the block-comment ceiling worth its own unit later?** It needs a sound block strip,
  which needs regex-literal awareness, which is the classic JavaScript lexing ambiguity
  `TOOL-aLexedStripper-5` declined. RESOLVED (agent, 2026-08-30, delegated): not now, and not as a
  row either — the dossier already carries it as an accepted blind spot and a backlog row would be a
  second copy of one fact, which is the class this build's own README bans.

## 9. Revision log

- rev-2 · 2026-08-30 · folded the round-1 spec audit's blocker cluster. S1 as written was a
  fail-open in the raw-primitive ban, reproduced on two legal-JavaScript spellings, because it took
  `renderCodeView` without the fallback that makes it safe. S1b adds it and AC5b/AC5c pin the shape
  AC5 could not observe.
- rev-1 · 2026-08-30 · initial draft, from a measured reproduction against the shipped hook at
  `14e21399`.

## 10. Reuse audit

The seam is `renderCodeView`, added by `TOOL-aLexedStripper-2` and corrected by `-5`, in this same
file. This unit adds no mechanism: it points a third consumer at a view that already exists, already
preserves interpolations, and already has the residual that makes it safe stated in the dossier.

The reuse probe for the sibling unit
(`python tools/codebase-map/reuse_lookup.py "decide whether a scan ended inside an unterminated
literal"`) returned `blankLiterals` and `agent-cap.topLevelArgs` but not `renderCodeView`, because
it landed at `7038bc2c` with fan-in 0 and the ranking has nothing to rank it by. That is recorded in
`TOOL-aPairedLexer-1` §10 and is the same answer here: the seam was known from having written it,
and the probe could not have found it.
