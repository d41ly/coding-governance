# TOOL-dGroundRules-51 — the build-order evidence observed in the build README with its path whole, beside the root-README negative

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-1 · base 3708a705 · streams tooling · order 15

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-51-deviation-39.md](../build/2026-10-23-build-TOOL-dGroundRules-51-deviation-39.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 21 at HIGH**, item **H3**, which no other id shares at that grade.
`TOOL-dGroundRules-43`'s `EVIDENCE` greps the repository-root `README.md` at `f4d31452a`, which holds
no build-order region, while that unit's §4 Evidence cites `memory/builds/dGroundRules/README.md`
for the same lines, so AC3 prints nothing on a correct build and S3's pinned citation is certified by
no criterion that can pass. This unit is id 21's promotion. It changes no code: it observes
`TOOL-dGroundRules-43` S3 with the build README's path whole, and pairs it with the root-README form
as a negative, so the probe is shown able to tell the two apart. It repairs `TOOL-dGroundRules-43`,
which sits at order 14, so it builds at order 15.

## 2. Scope (IN)

- **S1** — The evidence, whole. `EVIDENCE_WHOLE` (§5) greps the build README at `f4d31452a` for the
  region markers, and is the command through which `TOOL-dGroundRules-43` AC3 is observed at this
  unit's close. Observed by AC1.
- **S2** — The negative. `EVIDENCE_ROOT`, the same grep over the root `README.md` at that revision,
  counts no marker, so the stripped spelling the review names is shown to answer differently.
  Observed by AC2.

## 3. Non-goals (OUT)

- The region markers' revisions, `TOOL-dGroundRules-43` §4 Evidence. This unit observes one of them.
- Any other criterion of `TOOL-dGroundRules-43`; its minors are `TOOL-dGroundRules-52`'s.

### Edges

- **consumes-from** `TOOL-dGroundRules-43` — S3's pinned citation of the build-order markers and AC3, which S1 observes with the path whole
- **hands-off** `TOOL-dGroundRules-52` — `EVIDENCE_WHOLE`, through which that unit observes `TOOL-dGroundRules-43` AC3 (ids 3, 12 and 25)
- **hands-off** `TOOL-dGroundRules-64` — `EVIDENCE_WHOLE`, through which that unit observes `TOOL-dGroundRules-34` AC32 (the adopted discovery of the closing diff review, round 1)

## 4. Design

On 2026-10-23, `git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n gen:build-order`
printed `165:<!-- gen:build-order -->` and `179:<!-- /gen:build-order -->`, and the same grep over
`f4d31452a:README.md` printed nothing and exited 1 (PINNED; the revision is fixed, so the figure
cannot drift).

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

## 5. Acceptance criteria

Every command runs from the repository root. The literals are spelled whole here, once:

```text
EVIDENCE_WHOLE = git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n gen:build-order
EVIDENCE_ROOT  = git show f4d31452a:README.md | grep -c gen:build-order
```

- **AC1** — When `EVIDENCE_WHOLE` runs, it prints two lines, numbered `165` and `179`.
  Red when: the evidence cites lines its stated revision does not hold.
  figure: PINNED, the revision being fixed; this is a check on evidence, not on the build.
- **AC2** — When `EVIDENCE_ROOT` runs, it prints `0`.
  Red when: the probe answers alike for the root README and the build README, so it could not tell
  the stripped spelling from the whole one.

## 6. Gates

`memory hygiene`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 21 (HIGH, item H3) of the round-1 spec
  audit of units 35 to 43, from the review's sound fix, with both greps run on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-64`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.

## 9. Reuse audit

No existing seam fits beyond the one observed: the command is `TOOL-dGroundRules-43`'s `EVIDENCE`
with its path whole, and nothing is built. `python tools/codebase-map/reuse_lookup.py "read test
table rows from a suite file to probe two overlap rules"` ranked no seam that reads a README at a
revision. The recall probe returned `TOOL-dGroundRules-42`, whose class this is, and
`TOOL-dGroundRules-43`; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
