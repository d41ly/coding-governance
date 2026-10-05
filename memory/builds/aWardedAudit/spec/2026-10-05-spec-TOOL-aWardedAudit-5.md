# TOOL-aWardedAudit-5 — the bar refuses a run commit that writes a spec-audit opt-in

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-2 · base 8cfe5678 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-aWardedAudit-1-runlog-030cb510.md](../build/2026-10-05-build-TOOL-aWardedAudit-1-runlog-030cb510.md) | journal | TOOL-aWardedAudit-1 TOOL-aWardedAudit-2 TOOL-aWardedAudit-3 TOOL-aWardedAudit-6 |
| [2026-10-05-prompt-TOOL-aWardedAudit-5-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aWardedAudit-5-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review, round 1, H1. Units 1 and 2 read the opt-in from the owner's side
of the default branch, but nothing stops a run from LANDING one there: a run commit adding
`spec-audit:` to a slug README, or a dated `SPEC_AUDIT_DEFAULT` to `.unattended.conf`, authorizes
the next run's audit with no owner turn. Check 19 already refuses exactly that shape for `may:`.
This unit makes it refuse the two opt-in keys too, so the protocol's "same reading" claim is true.

## 2. Scope (IN)

- **S1** — `scan_grant_writes` in `tools/unattended/check-unattended.sh` reports a run's own commit
  that writes a `spec-audit:` front-matter line into any build README, by the same two-stage read it
  gives `may:`: present at the commit, and differing from every parent. Observed by AC1.
- **S2** — It also reports a run's own commit that writes a NON-BLANK `SPEC_AUDIT_DEFAULT` into
  `.unattended.conf`, read as the last assignment's raw value with one layer of quotes stripped, and
  differing from every parent's. A blank value is no opt-in and is not reported. Observed by AC2.
- **S3** — Each key fails check 19 with its own message naming the commit, the file and the run;
  the `may:` message is byte-for-byte unchanged. The owner's own commit on the default branch is
  never reported, exactly as for `may:`. Observed by AC1 to AC3.
- **S4** — ONE `diff-tree` pass still serves all three keys, so the bar pays no second walk.
  NOT OBSERVED by an arm: it is a property of the scanner's shape, read in review.

## 3. Non-goals (OUT)

- A key a run writes into a file the driver does not read the opt-in from.
- A conf evaluated the way the shell evaluates it: the scan reads the raw last assignment, and its
  header says so.

### Edges

none

## 4. Design

### Evidence

Read at base `8cfe5678`. `scan_grant_writes` takes commit ids on stdin, runs one
`diff-tree --stdin -r -p --cc` restricted to build READMEs, keeps an added `may:` line whose every
prefix column is `+`, then settles each candidate with `read_may_of` at the commit and at every
parent. Its callers read `<commit> <README>` and fail check 19 per line. Of the tracked history, no
run-state record's own commits write either opt-in key: the three commits that add `spec-audit:` to
a README are `dHashedPrelude`, which keeps no run-state file, and two branches not on the default
branch.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **A second scanner per key.** Two diff walks over one commit list for one question; the existing
  scanner already reads every README hunk.
- **Refuse at the driver.** The driver sees one run; the write that matters is the one the NEXT run
  reads, which only the cross-run arm sees.

## 5. Production-readiness checklist

- perf / scale — the same single `diff-tree` pass, with one more pathspec.
- security — narrows what a run can land; no new write path.
- error / empty / loading states — every skip check 19 announces today still announces.
- observability — each refusal names the key, the commit, the file and the run.
- testing — the arms are observed RED against the base checker first.
- migration — none: no tracked run record's own commits write either key.
- user docs — the protocol already names check 19's reading; unit 6 aligns its wording.
- risks — a branch that wrote the key under an earlier driver reds at its landing, which is the ruling.

## 6. Acceptance criteria

- **AC1** — When a fixture run's own commit adds `spec-audit: 2026-10-05` to a build README, the leg
  prints check 19 naming `spec-audit:` and that commit.
  Red when: the base checker reports nothing for it.
- **AC2** — When a fixture run's own commit sets `SPEC_AUDIT_DEFAULT="2026-10-05"` in `.unattended.conf`,
  the leg prints check 19 naming `SPEC_AUDIT_DEFAULT` and that commit; a commit setting it blank
  prints nothing.
  Red when: the base checker reports nothing, or a blank value reds.
- **AC3** — When the owner's commit on the default branch adds `spec-audit: 2026-10-05` to another
  README, the leg names no commit of it.
  Red when: an owner opt-in reds the run that merely carries it.

## 7. Gates

`unattended kit gate` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · the base checker, which reads `may:` alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the closing review's H1.

## 10. Reuse audit

No new seam: `python tools/codebase-map/reuse_lookup.py` cannot see `.sh` layers, so the seam was
found by reading `check-unattended.sh`. The seam extended is `scan_grant_writes` and check 19's grant-write arm, unchanged in range and
walk. `python tools/memory-recall/query.py` returned `TOOL-dDerivedDocket-19`, the cross-run arm this
unit widens.

Recall terms used: spec-audit SPEC_AUDIT_DEFAULT opt-in owner self-grant second anchor published prompt mode README front matter may grant D12-j
