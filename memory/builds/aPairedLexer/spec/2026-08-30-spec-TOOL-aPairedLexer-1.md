# TOOL-aPairedLexer-1 — rule 3 stops being blind below an unterminated template

**Status:** SPECCED · rev-1 · 2026-08-30 · node a · Tier-2 · base 14e21399 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-build-TOOL-aPairedLexer-1-base-measurements.md](../build/2026-08-30-build-TOOL-aPairedLexer-1-base-measurements.md) | journal | TOOL-aPairedLexer-2 TOOL-aPairedLexer-3 |

<!-- /gen:spec-records -->

## 1. Goal

`capFindings` must see a cap argument that sits below an unterminated template literal. It reads
`blankLiterals`, whose mode is carried across lines, so one unmatched backtick blanks every later
line and the rule that exists to refuse an unresolvable or oversized cap sees nothing at all.

## 2. Scope (IN)

- **S1** — `capFindings` detects that the scan ended inside a template literal and, when it did,
  builds its view with the per-line `stripStrings(l).split('//')[0]` instead of `blankLiterals`.
  The signal is `renderCodeView(script).unterminated`, which this file already computes for rule 2.
- **S2** — Fixtures in `tools/hooks/agent-cap.test.sh` for both directions: the two ADMIT-today
  shapes must DENY, and a bounded fan with a resolvable cap below an unterminated template must
  still ADMIT.
- **S3** — Bump `KIT_AGENT_CAP_VERSION`.

## 3. Non-goals (OUT)

- Not changing what `blankLiterals` returns. Rules 3 and 5 keep reading it in the ordinary case, so
  their existing arms are not re-baselined — the constraint `TOOL-aLexedStripper-2` S4 set.
- Not moving rule 3 onto `renderCodeView` wholesale. That would change its view for every script
  rather than for the malformed ones, and the arms it already carries are the reason not to.
- Not touching rules 1, 2 or 5.

## 4. Design

### The defect

`blankLiterals` (`agent-cap.js:504`) declares `let mode` outside its per-line loop. In `tmpl` mode it
appends nothing, so from an unmatched backtick to EOF every output line is `''`. `capFindings` reads
that view, finds no `boundedParallel(` call site and no marker line, and returns empty.

Isolated by classifying the deny message, because an unbounded receiver makes rule 2 deny first and
mask rule 3 entirely. The isolation is a BOUNDED receiver plus an unresolvable or oversized cap:

| script | template terminated | below an unterminated backtick |
|---|---|---|
| bounded receiver, cap `args.width` | **2** — rule3 CAP | **0 ADMIT** |
| bounded receiver, cap `500` | **2** — rule3 CAP | **0 ADMIT** |

### Why the fallback, and why it cannot regress

Identical in shape to `TOOL-aLexedStripper-5`'s fix for rule 2, and it has the same property. The
per-line view sees MORE than the blanked one — it never blanks a line to nothing — so switching to
it on the unterminated path can only ADD findings, never remove them. A rule whose findings are
denials cannot fail open by seeing more.

The direction that could hurt is a false positive: a cap-shaped token inside a template literal now
reaching the counter. That is bounded to scripts that END inside a template literal, which are not
valid JavaScript, and AC3 pins the one legal-looking shape that matters.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — the branch in `capFindings`, and the version constant.
- `tools/hooks/agent-cap.test.sh` — the arms.

### Alternatives rejected

- **Make `blankLiterals` reset its mode per line.** Rejected: rules 3 and 5 depend on the carry for
  a template that legitimately spans lines, and this would re-baseline both.
- **Move rule 3 onto `renderCodeView`.** Rejected: it changes the view for every script to fix the
  malformed ones, and re-baselines arms `TOOL-aLexedStripper-2` S4 exists to protect.
- **Fail closed when the scan ends unterminated.** Rejected on this file's own measured history:
  `TOOL-aLexedStripper-5` found that exact branch denying a legal script carrying a regex literal.

## 5. Production-readiness checklist

- security — this IS the security surface, and the unit closes a measured fail-open in it: a cap of
  500 currently admits.
- perf / scale — one extra `renderCodeView` pass, only computed where rule 3 already runs.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the unterminated template IS the error state and is what this
  unit is about. An empty script yields no findings, unchanged.
- observability — the hook writes its verdict to stderr; unchanged.
- risks — a false positive on a script that ends inside a template literal. Bounded and pinned by
  AC3.
- testing + left-shift gates — arms in both directions, staged against the shipped code first.
- migration / rollback — none; single-file revert.
- user docs — the `agent-cap` dossier gains a line only if the residual changes; it does not.

## 6. Acceptance criteria

- **AC1** — When a bounded receiver is fanned with an unresolvable cap BELOW an unterminated
  backtick, `node tools/hooks/agent-cap.js` exits `2`, against `0` at BASE.
- **AC2** — When the same shape carries a literal cap of `500`, it exits `2`, against `0` at BASE.
- **AC3** — When a bounded receiver is fanned with a RESOLVABLE cap of `5` below an unterminated
  backtick, it exits `0` — the fallback adds no false positive on the shape most likely to be legal.
- **AC4** — When both shapes are written with the template TERMINATED, they exit `2` as at BASE, and
  the deny message still names the cap rule rather than another.
- **AC5** — When each new fixture is staged against the shipped code first,
  `bash tools/hooks/agent-cap.test.sh` reports the BASE verdicts §4's table records.
- **AC6** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm that passes at BASE passes.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, `KIT_AGENT_CAP_VERSION` is bumped and all
  four carriers agree.

## 7. Gates

The legs are read from `tools/gate-legs.json` at emission time. `bash tools/hooks/agent-cap.test.sh`
is the direct invocation AC5, AC6 name; `bash tools/check-kit-versions.sh` is AC7's.

## 8. Open questions

- **F1 — should rule 5 take the same fallback?** It reads `blankLiterals` too and is blind in the
  same shape. Against: rule 5's finding is a wrong-verdict class rather than a burst, its own header
  records the reach it accepts, and widening two rules in one unit makes neither reviewable.
  RESOLVED (agent, 2026-08-30, delegated): rule 3 only; rule 5 is filed as a row if the closing
  review confirms it is blind. M3's tie-break prefers the option leaving fewer open questions inside
  this unit's diff.

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft. The defect was isolated by deny-message classification after a
  first fixture of four scripts returned all-DENY and proved nothing, an unbounded receiver having
  masked the rule under test.

## 10. Reuse audit

The seam is `TOOL-aLexedStripper-5`'s fallback, in this same file: when a scan ends inside a template
literal, judge the script on the per-line view rather than the blanked one. This unit applies the
existing pattern to a second consumer and adds no mechanism. `renderCodeView` already returns the
`unterminated` signal, so the detection is a read rather than a new computation.

`python tools/codebase-map/reuse_lookup.py "decide whether a scan ended inside an unterminated
literal"` was run and its ranked hits are `scan` (`row_grammar.py`), `scan_js_definitions`
(`map_lib.py`), `agent-cap.topLevelArgs` and `blankLiterals`. It did NOT surface
`renderCodeView`, which is the seam this unit actually uses — it landed at `7038bc2c` and carries
fan-in 0, so the ranking has nothing to rank it by. Recorded rather than smoothed: the probe was
right about the corpus and wrong about the answer, and the seam was known from having written it
rather than from the probe.

The one hit worth keeping is `scan_js_definitions`, which is `TOOL-aPairedLexer-3`'s subject —
the probe found this build's third unit while being asked about its first.
