# DEPL-cMendedVintage-3 — the coverage tail joins each open gap to its own refusal reason

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

`update --write` prints its open coverage gaps and, separately, the unclaimed sources it refused to
land — two lists about the same destinations, joined by nobody, under a closing clause claiming that
landing them "is a verb that does not exist yet" when the landing block sits 400 lines above it. Join
the two and delete the claim.

## 2. Scope (IN)

- **S1** The false clause at `tools/govkit/govkit.py:7797` — "landing them is a verb that does not
  exist yet" — is deleted, and the stale paragraph at `:7739` that says this verb reports and does
  not land is deleted with it. Observed by AC3.
- **S2** Each open gap prints with the refusal reason recorded for its destination, joined from
  `dict(_refused_new)` on `dest`. Observed by AC1.
- **S3** A gap whose destination is in neither `_landed_new` nor `_refused_new` prints that no reason
  was recorded for it in this run, and never a claim that it was resolved. Observed by AC2.
- **S4** The whole addition stays inside the existing bare `try`/`except` at
  `tools/govkit/govkit.py:7726`, which is the liveness guard: a join that raises must degrade to the
  UNAVAILABLE line, never to a reassuring zero. Observed by AC4.

## 3. Non-goals (OUT)

- This unit lands nothing and refuses nothing. It changes what the report SAYS about destinations the
  run already decided; every decision is made above it and none moves.
- No new refusal, no change to any of the eight `_refused_new` messages, no change to the landing
  block at `tools/govkit/govkit.py:7143-7340`.
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
landing block now at `tools/govkit/govkit.py:7143-7340` writes the blob, `git add`s it, and appends
the destination to `_landed_new` after minting the receipt row — the role, the commit and the oid the
comment at `:7739` says the verb has evidence for none of. Both passages therefore describe a version
of the verb that no longer exists, and the second one sits directly above the code that contradicts
it. Deleting them is the whole of S1.

### The join

```
_refused = dict(_refused_new)
for _g in _gap_open:
    _why = _refused.get(_g["dest"])
    print(... f"{_g['dest']}   <- {_g['src']}   " +
          (f"refused: {_why}" if _why else "no reason was recorded for this destination in this run"))
```

`_refused_new` is a `list[tuple[str, str]]` keyed on the same `_dest` string the gap row carries as
`dest`, so the join key needs no normalisation. It is built before the coverage block runs — the
landing loop ends at `tools/govkit/govkit.py:7340` and the coverage `try` opens at `:7726` — so the
dict is complete when the join reads it.

### Which gaps can carry a reason, enumerated rather than assumed

This matters because a join whose population is empty by construction is a gate that cannot fail.
`coverage_rows` returns rows where `kind == "write"`, `not missing`, and `dest not in tracked(target)`
(`tools/govkit/govkit.py:2477`). Against the eight refusal sites:

| Refusal site | Leaves the dest untracked? | Reaches the join? |
|---|---|---|
| `:7187` unresolved token in the source | the row is dropped by `planned_writes` first | no |
| `:7219` resolves outside the target | not a coverage row | no |
| `:7229` resolves inside `.git` | not a coverage row | no |
| `:7248` the index could not be read | yes | yes, not manufacturable in a fixture |
| `:7256` the target already holds the path | it holds it, so it may be tracked | only when untracked |
| `:7264` gov's source does not resolve | the row is `missing` | no |
| `:7279` writing it failed | yes | yes, not manufacturable in a fixture |
| `:7328` git refused to stage it | yes | yes, and manufacturable |

So the join's reliably reachable arm is `:7328`, staged by a `.gitignore` in the target that covers
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
- **user docs** — `WIRE-INTO-PROJECT.md`'s coverage paragraph repeats the deleted claim that landing
  an unclaimed source is not a verb that exists; it is corrected in the same commit or it becomes the
  surviving copy of a sentence this unit deleted for being false.

## 6. Acceptance criteria

- **AC1** — When a fixture target's `.gitignore` covers a destination gov ships and claims,
  `python tools/govkit/govkit.py update --target <fixture> --write` prints that destination on a GAP
  line carrying the refusal reason recorded at `tools/govkit/govkit.py:7328`.
  Red when: the join keys on something the two lists do not share, so the gap prints with the residue
  wording while a reason for it exists three lines further down the same output.
  fixture: built by this unit; no shipped fixture stages a refused-but-still-a-gap destination today.
- **AC2** — When a gap's destination appears in neither `_landed_new` nor `_refused_new`, its line
  says no reason was recorded for it in this run.
  Red when: the residue branch prints a resolution claim, or reuses the refused wording with an empty
  reason, either of which asserts something the run did not observe.
- **AC3** — When `grep -n 'does not exist yet' tools/govkit/govkit.py` runs, it returns nothing, and
  the paragraph at `tools/govkit/govkit.py:7739` no longer claims the verb cannot invent a receipt row.
  Red when: the clause is deleted from the print and left standing in the comment, so the file keeps
  the copy a reader reaches first.
- **AC4** — When the coverage block is made to raise — a fixture whose descriptor forces
  `coverage_rows` to fail — the run still prints the UNAVAILABLE line and still exits on its own
  merits.
  Red when: the join is added outside the `try`, so a report failure becomes a verb failure after the
  bytes have already landed.
  fixture: the `-11` escape fixture named in the block's own header already forces this path.
- **AC5** — When a run has open gaps and refused destinations, the counts on the existing
  `coverage:` and `unclaimed sources:` lines are unchanged by this unit.
  Red when: the join filters the gap list instead of annotating it, which would turn a report into a
  silent exclusion list.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · a target `.gitignore` covering a claimed destination, so the
staging refusal fires and the destination is still an open gap when the coverage block runs · none

`govkit refusal join` is named because this unit adds no refusal branch and deletes none: its pin and
anchor set must be unchanged by this commit.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "update verb rolls a kit back after declining its render
step"` and the recall probe both return the deployer's own `registry.toml` affordance seam and no
join helper, which is the answer to record: there is no existing "annotate a report row from a
sibling list" seam in this file, and none is needed — `_refused_new` is already a list of pairs and
the extension is `dict()` over it. The seam this unit extends is the printing loop itself at
`tools/govkit/govkit.py:7789`, which already distinguishes a declined row from an open one and prints
both rather than hiding either; this adds a third case to that same discrimination. Verified against
source rather than against the record: `TOOL-aFlaggedScaffold-3` states that `update` cannot land a
source gov started shipping, and that row is stale — the landing block at
`tools/govkit/govkit.py:7143` does exactly that, which is why the comment repeating it is deleted here.

Recall terms used: `coverage gap decline refusal reason unclaimed source landing unattributed
evidence remedy re-adopt pin allow-ungraded stamp`
