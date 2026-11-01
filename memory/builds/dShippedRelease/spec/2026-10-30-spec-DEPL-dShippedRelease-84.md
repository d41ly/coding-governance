# DEPL-dShippedRelease-84 — `disposed` reads one verdict from the closed set, and `BLOCKED` with no finding is forged

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 47 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B3 with ids 29 and 88
(DEPL-dShippedRelease-83, -85). Unit 73 S2 asks only for a `## Verdict` line, so a report reading
`## Verdict: BLOCKED`, or holding two such lines, or a stray `## Verdict` with no member, passes. The
term certifies a conclusion it never read. This unit reads the verdict by the rule hygiene check 22
already grades.

## 2. Scope (IN)

- **S1** — The read. `read_report_verdict(text)` in `tools/loop/deploy_items.py` returns the member of
  the one `## Verdict: <member>` line in the blob, the member one of `REPORT_VERDICTS`, `CLEAN`,
  `CLEAN WITH FIXES` and `BLOCKED`, with trailing space stripped. No such line, two, or any other
  text is `forged · verdict`. Observed by AC1.
- **S2** — `BLOCKED` is a disposal of its findings. Unit 14 S4 files each confirmed finding as a
  patch, so a `BLOCKED` report with `<n>` above 0 passes this term, and `BLOCKED` with `<n>` 0 is
  `forged · verdict`. Observed by AC2.
- **S3** — One fact. `--selftest` compares `REPORT_VERDICTS` with the three literals of
  `tools/memory-tree/check-memory-hygiene.sh`, reached by `resolve_kit_dir("memory-tree", ...)`, and
  prints `not graded · no memory-tree kit` where the kit is absent. Observed by AC3.

## 3. Non-goals (OUT)

- A verdict's relation to its findings beyond S2: the report's own content is the harness's.
- Sharing `tools/runlog/model.py`'s `VERDICT_RE`: a kit imports no sibling, and §4 says what holds
  the copy to the original.

### Edges

- **consumes-from** `DEPL-dShippedRelease-83` — `read_landing_report`, whose blob this unit's term reads
- **consumes-from** `DEPL-dShippedRelease-73` — `check_review_field`, whose S2 this unit narrows
- **hands-off** `DEPL-dShippedRelease-106` — `read_report_verdict`, which the minors batch's report must pass (review id 97)

## 4. Design

### Evidence

- `tools/memory-tree/check-memory-hygiene.sh:1428` grades `CLEAN`, `CLEAN WITH FIXES` and `BLOCKED`, and fails a missing line, a second line and a member outside the set (hygiene check 22).
- `tools/runlog/model.py:167` holds `VERDICT_RE`, the same line shape.
- Unit 14 S4 refuses a report with no `## Verdict` line and files each confirmed finding as a patch, so a landing review that blocks has a disposal and the landing stands.

### The read, as units 83, 84, 85 and 90 leave it

`check_review_field` on a `disposed · <n> finding(s) · <report path>` value, in order, each failure
printing `held · check_landing_review · forged · <term>`:

| Term | Test | Unit |
|---|---|---|
| `path` | the path sits directly under `memory/builds/<slug>/reviews/` and its blob is on the advertised tip | 83 |
| `verdict` | the blob holds exactly one `## Verdict:` line, a member of the closed set | 84 |
| `count` | `<n>` equals `derive_report_count` over the blob | 85 |
| `landing` | the blob's `**Reviewed range:**` line equals this landing's pin | 90 |

### Supersedes

- Unit 73 S2's "that blob holds a `## Verdict` line".

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_report_verdict` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `REPORT_VERDICTS` | module constant, `tools/loop/deploy_items.py` | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — the term reads the tip's tree and the landing's own pin, and a session still writes the field. Unit 73 §5's "outside the reviewed session's reach" is corrected to that: a session able to land a new report naming this landing passes, in the open on the default branch, and unit 73 §8 F1 keeps a signature out.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — check 22 reads records at or after `REVIEW_VERDICT_CUTOFF` and this term reads every report; an older report fails here, and an older report names no landing either.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-forged-verdict` plants a report under this
  build's folder holding `## Verdict: fine`, and again one holding two verdict lines, `--deploy close`
  exits 3 printing `forged · verdict` for each.
  Red when: any line opening `## Verdict` passes.
- **AC2** — When `--case review-forged-blocked` plants `## Verdict: BLOCKED` beside
  `disposed · 0 finding(s) · <that report>`, it exits 3 printing `forged · verdict`.
  Red when: a blocked review passes with nothing filed.
- **AC3** — When `python deploy_items.py --selftest` runs with `CLEAN` respelled in a scratch copy of
  the hygiene script, it exits 1 naming `REPORT_VERDICTS`; on the tree it exits 0.
  Red when: the two sets drift, so the term and the gate grade different verdicts.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · both plants, their failing case the read by prefix · none

New arm: tools/loop/deploy_items.py · covers AC3 · the scratch copy of the hygiene script, its failing case the compare cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 47 (BLOCKER, item B3) of the round-2 spec audit.

## 10. Reuse audit

The seam extended is `check_review_field` (unit 73), and the rule is hygiene check 22's, read at `tools/memory-tree/check-memory-hygiene.sh:1428`.
`python tools/codebase-map/reuse_lookup.py "grade a close term against sources the field does not control"`
ranked name-stem helpers (`note`, `field`, `terms`, `ask_field`) and no verdict reader;
`VERDICT_RE` at `tools/runlog/model.py:167` is one in another kit, so S3 holds the copy to the source.
The recall probe surfaced TOOL-aBlindedTrial-6 and report item B3, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how is a review report tied to the landing it reviewed" --terms "review report Verdict closed set hygiene check disposed forged landing dispose-landing VERDICT_RE"`
