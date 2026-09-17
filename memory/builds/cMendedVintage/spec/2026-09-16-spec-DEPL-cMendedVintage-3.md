# DEPL-cMendedVintage-3 — the coverage tail joins each open gap to its own refusal reason

**Status:** CLOSED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-DEPL-cMendedVintage-3-acceptance-ledger.md](../build/2026-09-16-build-DEPL-cMendedVintage-3-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-DEPL-cMendedVintage-3-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-3-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

`update --write` prints its open coverage gaps and, separately, the unclaimed sources it refused to
land — two lists about the same destinations, joined by nobody, under a closing clause claiming that
landing them "is a verb that does not exist yet" when the landing block sits 400 lines above it. Join
the two and delete the claim.

## 2. Scope (IN)

*No line numbers, in this section or below. Two units landed in this same function after rev-1 was
written and every citation in it had already drifted; the text is the address.*

- **S1** The false clause in the `coverage:` tally — "landing them is a verb that does not exist
  yet" — is deleted, and the gap-set header paragraph beginning "IT REPORTS, IT DOES NOT LAND",
  which says this verb has evidence for none of the fields a landed row needs, is deleted with it.
  Observed by AC3.
- **S2** Each open gap prints with the refusal reason recorded for its destination, joined from
  `dict(_refused_new)` on `dest`. Observed by AC1.
- **S3** A gap whose destination is not in `_refused_new` prints that no refusal reason was recorded
  for it in this run and points at `plan --coverage --emit-declines`, and never a claim that it was
  resolved. Observed by AC2.
- **S4** The whole addition stays inside the existing bare `try`/`except` wrapping the coverage
  block, which is the liveness guard: a join that raises must degrade to the UNAVAILABLE line, never
  to a reassuring zero. Observed by AC4.

## 3. Non-goals (OUT)

- This unit lands nothing and refuses nothing. It changes what the report SAYS about destinations the
  run already decided; every decision is made above it and none moves.
- No new refusal, no change to any of the eight `_refused_new` messages, no change to the
  unclaimed-source landing block that builds them.
- No change to `coverage_rows` or to the decline contract. The gap population and the decline
  registry are read exactly as today.
- No second copy of the reason. The join reads the string `_refused_new` already carries rather than
  re-deriving one at print time.

### Edges

- **consumes-from** external — the unclaimed-source landing block and its `_landed_new` and
  `_refused_new` lists, landed by `DEPL-dPolishedVitrine-3` and present at this build's BASE. Without
  them there is no reason to join to, and the deleted sentence would be true.
- **hands-off** external — nothing in this build consumes this unit's output.

## 4. Design

### Why the clause is false at BASE

The closing clause was written when `update` could not land a source gov had started shipping. The
unclaimed-source landing block writes the blob, `git add`s it, and appends the destination to
`_landed_new` after minting the receipt row — the role, the commit and the oid the "IT REPORTS, IT
DOES NOT LAND" paragraph says the verb has evidence for none of. Both passages therefore describe a
version of the verb that no longer exists, and the second one sits in the header of the very block
whose code contradicts it. Deleting them is the whole of S1.

### The join

```
_refused = dict(_refused_new)
for _g in _gaps:
    _why = _refused.get(_g["dest"])
    print(... f"{_g['dest']}   <- {_g['src']}   " +
          (f"refused: {_why}" if _why else "no refusal reason was recorded …"))
```

`_refused_new` is a `list[tuple[str, str]]` keyed on the same `_dest` string the gap row carries as
`dest`, so the join key needs no normalisation. Both the landing loop and every other refusal this
verb makes run before the coverage `try` opens, so the dict is complete when the join reads it.

`_landed_new` is NOT consulted, which is where this diverges from rev-1's S3. A landed destination
was `git add`ed, and `coverage_rows` filters on `dest not in tracked(target)` — so it cannot be
returned as a gap, and a membership test against it could never be true. A rolled-back landing is
removed from `_landed_new` during the pass and is not in it either. The test would have been the
could-not-fail shape §7 bans, dressed as thoroughness.

### Which gaps can carry a reason, enumerated rather than assumed

This matters because a join whose population is empty by construction is a gate that cannot fail.
`coverage_rows` returns rows where `kind == "write"`, `not missing`, and `dest not in tracked(target)`.
Against the eight `_refused_new` sites, each named by its own message text:

| Refusal site | Leaves the dest untracked? | Reaches the join? |
|---|---|---|
| "carries unresolved token(s)" | the row is dropped by `planned_writes` first | no |
| "resolves outside the target repository" | not a coverage row | no |
| "resolves inside the target's .git directory" | not a coverage row | no |
| "the index could not be read before landing" | yes | yes, not manufacturable in a fixture |
| "the target already holds this path" | it holds it, so it may be tracked | only when untracked |
| "which does not resolve" | the row is `missing` | no |
| "writing it failed" | yes | yes, not manufacturable in a fixture |
| "git refused to stage it" | yes | yes, and manufacturable |

So the join's reliably reachable arm is the staging refusal, staged by a `.gitignore` in the target that covers
the destination: the file is written, `git add` refuses it, the destination stays untracked, and it
is still a gap when the coverage block runs. That is the fixture AC1 is observed on, and the table is
the reason the arm is written against that site rather than against whichever site is convenient.

The rest of `_gap_open` — a destination for a kit the landing loop's selection never reached, or one
a rename decided — carries no entry in either list. S3's residue line is what those print, and it
says nothing about whether the gap was resolved, because a rename-decided destination is in neither
set and is not a refusal.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `_refused` | local dict in `_cmd_update`'s coverage block | `tools/govkit/govkit.py`, inside the existing `try` |

One local. No flag, file, config key or public surface; the print strings are the only other change.

### Files touched (estimate)

`tools/govkit/govkit.py` — about 20 lines: two deletions, one dict, one changed print, one residue
branch. `tools/govkit/selftest.py` — one fixture and three arms.

### Alternatives rejected

- **Re-derive the reason at print time.** A second copy of eight refusal strings, which is the
  prose-beside-its-source class the charter names; the string already exists and is already the one
  the operator sees on the refusal line.
- **Suppress a gap that has a reason.** That is the exclusion-list shape the decline contract's own
  header refuses: a gap that vanishes without saying why is worse than a gap printed twice.
- **Move the join outside the `try`.** It would then be able to fail the verb after bytes landed,
  which the block's own header records as a corrected defect.

### Migration

None. Output only; no receipt field, descriptor key or on-disk artifact changes.

### Rollout

Lands directly. The changed text is a report line, and the deleted sentences describe behaviour the
verb no longer has.

## 5. Production-readiness checklist

- **security** — no write path, no new subprocess, no new file. The unit only prints.
- **perf / scale** — one dict built from a list the run already holds; the loop is the one that
  already prints each gap.
- **error / empty / loading states** — an empty `_refused_new` makes every gap take the residue line;
  an empty `_gap_open` prints the existing `coverage: 0 undeclined gap(s)` line unchanged.
- **observability** — this unit IS the observability item: it turns two disjoint lists into one
  answer, and the count line above it still prints its zero.
- **risks** — the join key. If `_refused_new` ever holds a source path where the gap holds a
  destination, every lookup misses and every gap silently takes the residue line, which reads as a
  clean report. AC1 is the arm that would catch it, and the residue line's wording is deliberately
  not reassuring for the same reason.
- **testing** — three direct selftest arms over one fixture staged with a target `.gitignore`.
- **migration** — N/A, output only.
- **user docs** — none owed, and rev-1 was wrong to say otherwise. It claimed
  `WIRE-INTO-PROJECT.md`'s coverage paragraph repeats the deleted sentence; a repo-wide grep for the
  clause and for its paraphrases returns the engine line and nothing else. The runbook's coverage
  paragraph is about `plan --coverage`, which genuinely does not land anything, and is true as it
  stands.

## 6. Acceptance criteria

- **AC1** — When a fixture target's `.gitignore` covers a destination gov ships and claims,
  `python tools/govkit/govkit.py update --target <fixture> --write` prints that destination on a GAP
  line carrying the staging refusal's own recorded reason.
  Red when: the join keys on something the two lists do not share, so the gap prints with the residue
  wording while a reason for it exists three lines further down the same output.
  fixture: the `-ST2` mvkit fixture, EXTENDED rather than a new one — see AC2 for why that fixture
  and not another.
- **AC2** — When a gap's destination does not appear in `_refused_new`, its line says no refusal
  reason was recorded for it in this run and points at `plan --coverage --emit-declines`.
  Red when: the residue branch prints a resolution claim, or reuses the refused wording with an empty
  reason, either of which asserts something the run did not observe.
  fixture: the same one. `-ST2` already ends holding `tools/mvkit/moved2.txt` — a destination the
  rename machinery DECIDED about without refusing, so it is in neither list and is the residue itself.
  That is why this unit extends that fixture instead of building one.
- **AC3** — When `grep -n 'does not exist yet' tools/govkit/govkit.py` runs, it returns nothing, and
  the gap-set header no longer claims the verb cannot invent a receipt row.
  Red when: the clause is deleted from the print and left standing in the comment, so the file keeps
  the copy a reader reaches first. The arm therefore reads the FILE, not the printed output.
- **AC4** — The join is inside the existing bare `try`/`except`, so a coverage failure still degrades
  to the UNAVAILABLE line rather than failing the verb after bytes landed.
  Red when: the join is added outside the `try`.
  NOT OBSERVED BY AN ARM, and named rather than implied: no fixture in the suite forces
  `coverage_rows` to raise, and rev-1's claim that the `-11` escape fixture "already forces this
  path" is false — the block's own header records that the first cut raised on it and that the
  CURRENT placement is the correction. Graded structurally, by reading the diff.
- **AC5** — When a run has open gaps and refused destinations, the counts on the existing
  `coverage:` and `unclaimed sources:` lines are unchanged by this unit.
  Red when: the join filters the gap list instead of annotating it, which would turn a report into a
  silent exclusion list.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · a target `.gitignore` covering a claimed destination, so the
staging refusal fires and the destination is still an open gap when the coverage block runs · none

Seven arms, extending the `-ST2` mvkit fixture. Two of them are LIVENESS and run before any grading:
one asserts the refusal that fired is the STAGING one by its own text rather than any non-zero exit,
the other asserts the GAP row exists at all, so no later arm can pass over an absent line.

`govkit refusal join` is named because this unit adds no refusal branch and deletes none: its pin and
anchor set must be unchanged by this commit.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · S1 · S3 · S4 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC4 · §7 · §10 · the build pass
  staged the failing case against the real engine before writing the fix, and it corrected four of
  this spec's claims. (a) S3's `_landed_new` membership test is NOT written: a landed destination is
  staged and therefore tracked, so `coverage_rows`' own filter already excludes it, and the test could
  never have been true — the could-not-fail shape §7 bans. The join reads `_refused_new` alone.
  (b) The residue wording is "no REFUSAL reason was recorded", plus a pointer to
  `plan --coverage --emit-declines`. Rev-1's bare "no reason was recorded" overclaims: a rolled-back
  landing is removed from `_landed_new` during the pass and did have a reason, just not a refusal.
  (c) §5's user-docs item is void — `WIRE-INTO-PROJECT.md` does not carry the deleted claim; a
  repo-wide grep returns the engine line and nothing else. (d) AC4 is not observed by an arm and now
  says so instead of citing the `-11` escape fixture, which the block's own header shows does NOT
  force this path under the current placement. Also: every `tools/govkit/govkit.py` line number is
  deleted, as `-2` deleted its own, because two units landed in this function after rev-1 and every
  citation had drifted. The fixture is the `-ST2` mvkit one EXTENDED, not a new one — it already ends
  holding the rename-decided residue row AC2 needs.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "update verb rolls a kit back after declining its render
step"` and the recall probe both return the deployer's own `registry.toml` affordance seam and no
join helper, which is the answer to record: there is no existing "annotate a report row from a
sibling list" seam in this file, and none is needed — `_refused_new` is already a list of pairs and
the extension is `dict()` over it. The seam this unit extends is the gap printing loop itself, which
already distinguishes a declined row from an open one and prints both rather than hiding either; this
adds a third case to that same discrimination. Verified against source rather than against the record:
`TOOL-aFlaggedScaffold-3` states that `update` cannot land a source gov started shipping, and that row
is stale — the unclaimed-source landing block does exactly that, which is why the comment repeating it
is deleted here. That backlog row is NOT touched by this unit; it is a separate record with its own
lifecycle, and rewriting it was never in scope.

Recall terms used: `coverage gap decline refusal reason unclaimed source landing unattributed
evidence remedy re-adopt pin allow-ungraded stamp`
