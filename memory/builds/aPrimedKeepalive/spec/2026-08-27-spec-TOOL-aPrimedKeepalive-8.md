# TOOL-aPrimedKeepalive-8 — the Skill's two halves agree that a resumed keepalive is presumed ALIVE

**Status:** CLOSED · rev-1 · 2026-08-27 · node a · Tier-1 · base b4e1d5be · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-9 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-9-closing-diff.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-9-closing-diff.md) | diff-review | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-9 |

<!-- /gen:spec-records -->

## 1. Goal

`SKILL.template.md:35` told every reader that a resumed session's keepalive is dead before it starts.
`:589` of the same file calls that intuition MEASURED FALSE and cites the measurement. One file, two
answers, 554 lines apart, with the false half in the section every path reads first. Make the halves
agree.

## 2. Scope (IN)

- **S1** — the hoisted keepalive section's `Resume` carve-out states the resumed job is PRESUMED
  ALIVE and points at `## Resume` for the measurement, instead of asserting it dead.
- **S2** — the same claim in this build's own README roster is corrected in the same commit.
- **S3** — the render is regenerated, since the defect shipped through it.

## 3. Non-goals (OUT)

- Any change to `## Resume` itself. Its text is correct; this unit fixes the sites that contradict it.
- A gate. The two sites are prose in one file and no predicate here is cheap and safe; the
  left-shift the audit proposed — a lint over a document's own contradicting claims — is a unit
  nobody has specced.

## 4. Design

PROMOTED from spec-audit round 3 under M4's NON-CONVERGENT exit. It is a `two-answers-to-one-question`
instance, and the interesting part is WHERE it came from: the false half was written by this build's
own round-1 fold, and the true half by its round-2 fold. A fold that corrects a claim in one place and
introduces it in another is the same class one level up, which is why the loop stopped rather than
running a fourth round over the same specs.

`AC9` of `TOOL-aPrimedKeepalive-1` could not catch it: its observation window is the `## Resume`
section, and the contradicting sentence is 554 lines above that heading.

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n · error states · migration — N/A, a prose correction.
- observability — the render is byte-compared by `adopt-unattended.sh --check`.
- risks — none beyond the claim itself, which is what is being removed.
- testing + left-shift gates — no gate; §3 says why and names the unbuilt candidate.
- user docs — the Skill IS the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -c "dead before it starts" .claude/skills/unattended/SKILL.md` runs, it
  returns 0, and the carve-out sentence instead reads that the job is presumed ALIVE.
- **AC2** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it reports in sync.
- **AC3** — When `memory/builds/aPrimedKeepalive/README.md`'s roster is read, no row asserts the
  retired claim, and unit 6's row names check 23 rather than "checks 22 and 23".

## 7. Gates

`unattended skill wiring` · `memory tree hygiene`, and `bash tools/run-gates/run-gates.sh` at the
push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · PROMOTED from spec-audit round 3 by M4's NON-CONVERGENT exit, specced at its
  tier and built rather than parked.

## 10. Reuse audit

No seam and no mechanism — a prose correction across three sites in two files. The reuse is of the
measurement itself: `TOOL-aPromptedMandate-11` in `memory/backlog/TOOL.md`, which records that a run
asserted twice that two keepalives died with their processes and the scheduler's own listing showed
both still firing. `## Resume` already cites it; this unit makes the rest of the file stop
contradicting it.

Recall terms used: `keepalive session-scoped store survives process resume reap read-back orphan
attestation measured false`.
