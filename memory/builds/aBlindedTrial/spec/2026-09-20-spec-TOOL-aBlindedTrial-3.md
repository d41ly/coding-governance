# TOOL-aBlindedTrial-3 — the build harness runs its AUDIT stage only when `specAudit` is declared

**Status:** INPROGRESS · rev-1 · 2026-09-20 · node a · Tier-2 · base b7dee206 · streams tooling · order 2 · ratified 2026-09-20

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-build.js` takes a `specAudit` arg; when it is absent the AUDIT stage does
not run, the roster is handed out on SPEC completion with a loud log line, and the return says the
audit was NOT OWED rather than pretending a clean one ran. This is the enforcement point for the
programmatic route, which no tool-call hook can see.

## 2. Scope (IN)

- S1 — the args block accepts an optional `specAudit` (a `<date>` string); any other present
  type or shape is refused by name in the validation block, like `runStateExists` is today
  (`unattended-build.js:101-103`, `:168-182`). Observed by AC1.
- S2 — stage 2 (`phase('Audit')`, `:601-936`) branches: absent → `log('audit stage: OFF by
  declaration — no spec-audit: key on the build README (TOOL-aBlindedTrial-6); the roster is handed
  out on SPEC completion')`, no `workflow()` call, no resolver agent; present → today's path
  unchanged. Observed by AC2, AC3.
- S3 — the OFF path's return carries `audit: { ran: false, verdict: 'NOT-OWED', blockers: null,
  highs: null, unverified: null }` and the note predicate (`template:1293`) exempts `NOT-OWED`, so
  an off run never reads DEGRADED and never reads clean. Observed by AC4.
- S4 — the pairing refusal: `auditIds`, `subjects` or `subjectRound` present beside no `specAudit`
  is a re-invoke after an audit that never ran, refused by name like every other impossible pairing
  in the file. Observed by AC5.
- S5 — the DISPOSAL stage runs over an empty confirmed set on the OFF path and the hand-out follows
  the same code as a CONVERGED round with zero findings, so no second roster path exists. Observed
  by AC3.
- S6 — `unattended-build.template.js` is the source; the render is produced by
  `check-protocol-parity.test.sh --render`; every fixture in `unattended-build.test.sh` that expects
  the audit to run (`UNITS:116` and the eight attended fixtures) gains `"specAudit":"2026-09-20"`, and
  the new OFF arms are observed RED against the pre-edit render first. Version `unattended-build@1.1
  → 1.2` in both carriers. Observed by AC6, AC7.

## 3. Non-goals (OUT)

- `tier2-review.js` is untouched: the spec-audit kind stays available to a declared build.
- No driver verb records the OFF fact; the driver's own preflight line (`TOOL-aBlindedTrial-2`) is
  the record, and the harness's log line and return are the witnesses.
- No project-wide default: `specAudit` is caller-supplied, read from the preflight line.

### Edges

- **consumes-from** `TOOL-aBlindedTrial-2` — the value the caller passes is the driver's pinned
  `spec-audit` fact; without that unit the caller has nothing to read.
- **hands-off** `TOOL-aBlindedTrial-4` — the hook denies a DIRECT `Workflow` call with kind
  `spec-audit`; the nested `workflow()` here is a runtime call the hook cannot see, which is why
  this unit exists.

## 4. Design

### Data model

`specAudit: '<date>' | undefined`. Absent means OFF. The return's `audit` object gains
`ran: boolean` and a `verdict` value `NOT-OWED` beside the existing round verdicts; counts are
`null` (stated absence), never `0`.

### Files touched (estimate)

`tools/workflows/unattended-build.template.js` · `tools/workflows/unattended-build.js` (render) ·
`tools/workflows/unattended-build.test.sh` · `memory/map/features/` dossier prose for the harness.

### Alternatives rejected

- Defaulting `specAudit` to ON when absent: preserves every fixture but makes the opt-in a no-op for
  every caller that does not know the key exists, which is every caller today.
- A new top-level function for the branch: stales `symbols.json` and meets the lexicon pin; the
  branch is `specAudit &&` guards and one ternary in place.

## 5. Production-readiness checklist

- security — N/A
- perf / scale — the OFF path removes ten agents per unit
- error / empty / loading states — a malformed `specAudit` and the pairing hole are both refused by
  name; the OFF path never returns a zero it did not count
- observability — the `audit stage: OFF by declaration` log line and `audit.ran` in the return
- risks — a caller omitting the arg silently gets OFF: the Skill's harness bullet (unit 2) names the
  preflight line to read; the note predicate must exempt `NOT-OWED` or every off run reads DEGRADED
- testing — `unattended-build.test.sh`, run by hand (not on the bar, in no budget row)
- migration — the nine fixture lines gain the key
- user docs — the harness bullet in the Skill render (unit 2)

## 6. Acceptance criteria

- **AC1** — When `run_wf` is given `"specAudit":1`, the trace ends `THROW` with a message naming
  `specAudit` and the date shape.
  Red when: a non-string value reaches stage 2 as truthy.
- **AC2** — When `run_wf` is given `UNITS` without `specAudit` and no `workflow` double, the trace
  carries `log:audit stage: OFF by declaration` and no `workflow:` line.
  Red when: the harness awaits the sub-workflow, or the log line is absent.
- **AC3** — When the same OFF run completes, the trace carries `"roster":[{` and no `HELD AT
  HAND-OUT`, and `phase:Disposal` still appears.
  Red when: the roster is withheld, or DISPOSAL is skipped.
- **AC4** — When the OFF run returns, `RESULT` carries `"verdict":"NOT-OWED"`, `"ran":false` and
  `"blockers":null`, and the note does not contain `DEGRADED`.
  Red when: a `0` blocker count or a clean note appears on a path that reviewed nothing.
- **AC5** — When `run_wf` is given `subjects` and no `specAudit`, the trace ends `THROW` with a
  message naming the pairing.
  Red when: an audit-shaped re-invoke rosters without an audit.
- **AC6** — When `run_wf` is given `UNITS` with `"specAudit":"2026-09-20"`, the trace carries
  `workflow:` and `wargs:` with `"kind":"spec-audit"` exactly as before the change.
  Red when: a declared build loses its audit.
- **AC7** — When `node tools/workflows/check-workflow-syntax.js` and `bash
  tools/workflows/check-verifier-fanout.sh` run over the render, both exit 0; `diff` between
  `unattended-build.template.js` and `unattended-build.js` shows only the six token lines; and both
  carriers read `unattended-build@1.2`.
  Red when: the template and render differ elsewhere, or a marker is left at 1.1.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness`

New arm: `tools/workflows/unattended-build.test.sh` · `UNITS` minus the key against the pre-edit render · none

## 8. Open questions

- **F1 — absent means OFF or absent means ON.** RESOLVED (agent, 2026-09-20, delegated): OFF. The
  owner's ruling is "forbidden unless overridden"; a default that runs the audit when nobody asked is
  the behaviour being retired.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft from the scout of the harness at b7dee206.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "skip a workflow stage when an argument is absent and hand out the roster"` returned no candidate in the layer this
unit edits — it reports `unscanned layers: .sh` and resolves no `.js` symbol either — so the seam below
was found by reading the source, not by the probe. The seam is the harness's own optional-arg pattern (`runStateExists`, `:101-103`) and its impossible-
pairing refusals; the OFF hand-out reuses the CONVERGED-with-zero-findings path rather than adding a
second roster route. Recall terms used: unattended-build harness stage audit roster hand-out
specAudit verdict NOT-OWED degraded null blockers parity render fixture.
