# TOOL-aUnblockedFleet-2 — the merge bar stops reddening because two builds are live

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-2 · base 117de044 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aUnblockedFleet-1-specs-round1.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-1-specs-round1.md) | spec-audit | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 |

<!-- /gen:spec-records -->

## 1. Goal

Leg check 7 reds the merge bar whenever more than one tracked run-state file is non-terminal. It is
the driver refusal's mirror, it carries the same justification, and it is the half that blocks
LANDING rather than STARTING — the state `TOOL-aFusedCharter-4` measured as unresolvable by any
in-band verb. Replace the refusal with a report, so a bar run over a tree holding concurrent runs is
green and still says what it saw.

## 2. Scope (IN)

- **S1** — check 7 (`tools/unattended/check-unattended.sh:1112`) stops calling `fail 7`. It keeps
  building `$live` and `$nlive`, keeps applying the `LANDING`-witness exclusion, and REPORTS the
  survivors instead of failing on them.
- **S2** — the report names each concurrent run by file and phase, on the DEFAULT channel, for the
  reason this leg's own header at `:23` states about the exclusion notice: a notice routed through
  the `REPORT=1` reporter is invisible on every ordinary bar run, which is a check quietly deleted.
- **S3** — SILENT at `nlive <= 1`, matching unit 1's S3. A line on every green bar is a line nobody
  reads, and this leg already prints nothing when it is happy.
- **S4** — the two existing notices are KEPT verbatim: the `EXCLUDED` line and the `UNAVAILABLE`
  line. The second is the liveness assertion — an exclusion that cannot compute must say so rather
  than silently stop excluding — and it becomes MORE important here, not less, because after this
  unit the exclusion is the only thing that distinguishes a stamped-but-unlanded record in the report.
- **S5** — the check KEEPS ITS NUMBER. Check 7 becomes a reporting check rather than a failing one;
  renumbering would break every arm, every header reference and the leg's own count pins.
- **S6** — the check's header states what it now does NOT check, per template §7's rule that a gate's
  own header names its gaps: it no longer asserts anything about how many runs are live, and an
  abandoned record is now reported forever rather than blocking, with no staleness bound.
- **S7** — the IN-CODE justification at `check-unattended.sh:716-720` is corrected in the same edit.
  It sits in check 4's header and explains that check's existence by reference to "the live-run rule
  below", naming `nlive <= 1` as a live refusal. After S1 that sentence is false, and it is the
  justification for the check that becomes MORE load-bearing here — check 4 is what keeps the
  per-build-folder live count at one once the tree-wide count stops failing. A false rationale on a
  check whose importance just rose is worse than no rationale.

## 3. Non-goals (OUT)

- The DRIVER's refusal 5 — `TOOL-aUnblockedFleet-1`, a separate mechanism and a separate unit.
- Leg check 4, which refuses an ARCHIVED record carrying a non-terminal phase. That check is
  correct, is about rotation rather than concurrency, and becomes MORE load-bearing after this unit:
  it is what keeps the per-build-folder live count at one. Untouched, and unit 4 adds no arm for it
  because it already has one.
- A staleness bound on an abandoned record. Same reasoning as unit 1 §3.
- The three OTHER checks that read run-state files (`:247` review rounds, `:332` halt codes, `:448`
  the population). All three grade per file, all three were measured green under two live records,
  and none is touched.

## 4. Design

### The measurement that decided it

The whole leg was run over a scratch copy of this repository holding two genuinely live records for
unrelated builds, with check 7's `fail` replaced by an echo. It exited **0**, green, and no check
other than the neutered 7 reported anything. That is the discriminating result: if any other check
had depended on singularity, it would have redded there.

### Alternatives rejected

**Leave the leg refusing and fix only the driver.** Rejected because it inverts the wedge rather
than removing it: runs would start freely and then be unable to land, which is exactly
`TOOL-aBoundedVerdict-24` ("a run that CLOSES but cannot LAND blocks every later run's bar") and
`TOOL-aFusedCharter-4` (three builds at `LANDING`, resolvable only by falsifying two records). One
half without the other makes the fleet worse, not better.

**Make check 7 fail only when the records share a node tag.** Rejected for unit 1's reason and one
more: the leg runs on every node, so a node-partitioned rule reds a bar for a state that node cannot
act on, and the operator's only remedy is editing another node's record.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/check-unattended.sh` | check 7's `fail 7` becomes a printed report; the `# ---- 7:` header block rewritten to state the new contract and its gaps; the stranded justification at `:716-720` corrected (S7) |

No test file and no version bump appear here. `check-unattended.test.sh` belongs to
`TOOL-aUnblockedFleet-4` and the `KIT_UNATTENDED_VERSION` bump to `TOOL-aUnblockedFleet-3`; rev-1 of
this spec claimed both, which is two units owning one file twice over.

### Rollout

No record migrates and nothing in this unit is versioned. The kit version bump and every carrier it
touches are `TOOL-aUnblockedFleet-3`'s, which is where the full carrier set is enumerated.

## 5. Production-readiness checklist

- security — as unit 1: this check was never an authorization control.
- perf / scale — unchanged; the loop already ran.
- a11y — N/A, a shell gate leg.
- i18n — N/A.
- error / empty / loading states — S3 is the empty case. The no-anchor case keeps its UNAVAILABLE
  notice, which is the leg's liveness assertion for the exclusion.
- observability — the report is what the refusal's diagnostic value becomes, and after this unit it
  is the ONLY tree-wide surface that names abandoned run records at all. That is why S2 pins the
  channel rather than leaving it to the reporter.
- risks — the class this unit is closest to is `two-guards-one-question-two-answers`, which is the
  gotcha `TOOL-aFusedCharter-4` instantiates. Landing only one half re-creates it, which is why the
  two units land in one commit range and unit 4's arms cover both.
- testing + left-shift gates — unit 4. The failing case is observed for this half before it lands.
- migration / rollback — revert; nothing persists.
- user docs — unit 3.

## 6. Acceptance criteria

- **AC1** — When the leg runs over a tree with two non-terminal run-state files for different builds,
  `bash tools/unattended/check-unattended.sh` exits 0, asserted by the rewritten arm in
  `check-unattended.test.sh` where a `hit` on the old failure text stood.
- **AC2** — When that run happens, its output names both records and their phases, asserted by a
  `hit` arm against the report's own text.
- **AC3** — When exactly one record is live, the output carries no concurrency report, asserted by a
  `miss` arm — the green control that stops the report from being a banner.
- **AC4** — When a `LANDING` record whose witness is an ancestor of the advertised tip is present, the
  `EXCLUDED` notice still prints and that record is absent from the report, asserted by the existing
  arm plus a `miss` on the report naming it.
- **AC5** — When no advertised default-branch tip resolves, the `UNAVAILABLE` notice still prints,
  asserted by the existing arm — the liveness assertion survives the change that made it matter more.
- **AC6** — When the full bar runs over THIS repository at the landing tip, `bash
  tools/run-gates/run-gates.sh` is green with the `unattended kit gate` leg among the legs it names.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. Binding legs: `unattended kit gate`, `drift-audit records`, and
the `check-arms` armed-branch floor for `tools/unattended/check-unattended.test.sh`. Measured headroom
at rev-2: that file is 162 branches against floor 101 and 162 armed against floor 100, so removing one
branch moves no pin.

**The landing order is unit 1 §7's**, and it binds this unit identically: this unit rewrites two
headers inside `PRODUCT_GLOBS` while the `non_terminal_specs_cited_by_product_source` ratchet sits at
2 against pin 2. Read it there rather than here — a second copy is the class this build keeps finding.

## 8. Open questions

none — the mechanism follows unit 1's, which the §4 measurement decided for both halves together.
RESOLVED (agent, 2026-08-31, delegated): report the concurrent runs on the default channel, fail on
none of them, and keep the check's number.

## 9. Revision log

- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate, alongside unit 1.
- rev-2 · 2026-08-31 · spec-audit round 1 fold. Dropped this unit's claims on
  `check-unattended.test.sh` (unit 4's) and on the version bump (unit 3's), both of which rev-1 took
  from other units (H6). Added S7, a third in-code carrier of the removed rule that no unit's
  acceptance could see (H3). §7 gained `drift-audit records` and points at unit 1's landing order
  rather than restating it (B3). Order moved 2 -> 4: unit 6 must land before the carriers.

## 10. Reuse audit

The seam is check 7 itself and the notice pattern immediately above it in the same block — the
`EXCLUDED` and `UNAVAILABLE` printfs added by `TOOL-aPrimedKeepalive-4`. This unit reuses that
notice's channel decision verbatim, including the reason recorded in the leg's header at `:23` for
why it may not go through `report`.

No new seam was sought: `reuse_lookup.py` was run once for the pair (recorded in unit 1 §10) and the
two units share one behaviour phrase, so a second identical query would be a second answer to one
question rather than a second probe.

Recall terms are unit 1's, and the same five records bind both halves. **Verified against source at
writing time**: check 7's line number and its `fail 7` call, the three per-file loops at `:247`,
`:332` and `:448`, the header's channel note at `:23`, and leg check 4's archived-record refusal. No
disagreement between the records and the code.
