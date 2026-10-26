# TOOL-dPlacedRequest-51 — the prepared-merge shape table splits the first-parent walk by `--no-merges`

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 26 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-52 |
| [2026-10-25-build-TOOL-dPlacedRequest-51-deviation-511.md](../build/2026-10-25-build-TOOL-dPlacedRequest-51-deviation-511.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-51-deviation-512.md](../build/2026-10-25-build-TOOL-dPlacedRequest-51-deviation-512.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-52 |
| [2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md`)
confirmed **finding 10 at HIGH**, its item **H2**, which holds no other finding.
`TOOL-dPlacedRequest-45` adds a section "A merge onto the default tip" to
`memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`, and its first row says
`git log --first-parent <base>..HEAD` on that merge reads "no — the default branch's line only".
Without `--no-merges` that walk lists the merge and diffs it against its first parent, so it reads the
whole branch diff. The record's existing row already says so ("`git log --first-parent`: it diffs a
merge against its first parent | yes", `:27`), so the new row contradicts it. B1's vacuous oracle came
from `--first-parent` paired with `--no-merges`, which the row never names, and 45 AC2 runs only the
`--no-merges` form and greps only the `HEAD^1..HEAD^2` row. This unit repairs `TOOL-dPlacedRequest-45`,
at order 25, so it sits at order 26: the row is split by the flag that decides it, and every row of the
section is re-measured by a criterion.

## 2. Scope (IN)

- **S1** — The split rows. The section's table carries three rows: `git log --first-parent
  --no-merges <base>..HEAD` reads "no, the default branch's commits only (the vacuous oracle)";
  `git log --first-parent <base>..HEAD` with `-p` or `--name-status` reads "yes, the whole branch diff,
  attributed to the merge"; `git log --no-merges HEAD^1..HEAD^2` reads "yes, every one". The record is
  edited in place, and 45 S1 and its §4 sketch are rewritten to the same three rows as one rev bump of
  45 with its §9 line. Observed by AC1.
- **S2** — Every row re-measured. 45 AC2 is rewritten in place to name its own fixture by count and to
  run each row's command on it, grepping the record for each row: a base, two branch commits (one
  bumping `KIT_UNATTENDED_VERSION` from 1.110 to 1.111), one default-branch commit, and a `--no-ff`
  merge onto the default branch. Observed by AC2.

## 3. Non-goals (OUT)

- No change to the oracle: `TOOL-dPlacedRequest-44`'s, and finding 17's item of
  `TOOL-dPlacedRequest-52`.
- No change to the record's selection or anchors: 45 S2's.
- No machine gate: the record declares none, and AC2 is the re-measurement.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-45` — the record's "A merge onto the default tip" section, its S1 and AC2, which this unit splits and re-measures in place; without the section there is no row to correct
- **hands-off** `TOOL-dPlacedRequest-56` — S1, S2, §4 Evidence, §5, AC1 and AC2, which that unit's items for findings 4, 5, 10, 12, 20, 21 and 24 amend

## 4. Design

### The section's table, as it stands after this unit

```
| Shape, run on that merge | Reads the branch's commits |
|---|---|
| `git log --first-parent --no-merges <base>..HEAD` | no, the default branch's commits only (the vacuous oracle) |
| `git log --first-parent -p <base>..HEAD`, or `--name-status` | yes, the whole branch diff, attributed to the merge |
| `git log --no-merges HEAD^1..HEAD^2` | yes, every one |
```

The second row agrees with the record's existing `:27` row instead of contradicting it, and the first
names the flag pair that made B1 vacuous.

### Evidence

- Measured 2026-10-25 on node a in a fixture repository under `%TEMP%`, built as S2 states, with the
  merge subject `merge: dPlacedRequest — land onto origin/main at x`:
  `--first-parent --no-merges` listed `m1` only; bare `--first-parent` listed the merge and `m1`;
  with `--name-status` it printed `A b2` and `M tools/unattended/unattended.sh` under the merge; with
  `-p`, `-KIT_UNATTENDED_VERSION=1.110` and `+KIT_UNATTENDED_VERSION=1.111`; `HEAD^1..HEAD^2` listed
  `b2` and `bump`. PINNED at that date.
- The record's shape table, `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md:22-31`.

### Files touched (estimate)

- `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`: the section's rows
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-45.md`: S1, §4, AC2 and its
  §9 line

### Alternatives rejected

- **No first-parent row at all.** The vacuous pairing is the shape the next writer repeats, so the
  record names it rather than leaving it out.
- **Re-measure only the corrected row.** The review's gate is that every row has a command, and a row
  nobody re-runs is the one that drifts.

## 5. Production-readiness checklist

- security — none.
- perf / scale — none: one record.
- error / empty / loading states — N/A — a record, no runtime path.
- observability — the checklist line `gotchas.py` prints for a lander diff now names the vacuous pair.
- risks — none beyond 45 §5's.
- testing — the probes of §6.
- migration — none.
- user docs — the record is the documentation.

## 6. Acceptance criteria

- **AC1** — When `grep -cF` runs over `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`
  once per row command, `--first-parent --no-merges <base>..HEAD`, `--first-parent -p <base>..HEAD`
  and `--no-merges HEAD^1..HEAD^2`, each prints 1, and the row of the `-p` form reads `yes`.
  Red when: the section says a bare first-parent walk reads no branch work, as 45 rev-2 writes it.
- **AC2** — When the S2 fixture repository is built under `%TEMP%` and the three row commands run on
  its merge, the first lists the default-branch commit alone, the second prints both
  `KIT_UNATTENDED_VERSION` lines, and the third lists the two branch commits.
  Red when: a row states a shape its command contradicts on the fixture.
  fixture: built by the probe, not held in the tree.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the record declares no machine gate, and AC2 re-measures every row.

## 8. Open questions

- **F1 — How does the section state the first-parent walk?** (a) Two rows split by `--no-merges`,
  every row re-measured; (b) no row for the bare form; (c) the row kept as 45 rev-2 writes it. (c) is the
  defect; (b) drops the vacuous pairing the record exists to name. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-3 promotions, finding
  10 (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edge to `TOOL-dPlacedRequest-56`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is the class record `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`
and the section `TOOL-dPlacedRequest-45` adds to it, read by `tools/memory-tree/gotchas.py`.
`python tools/codebase-map/reuse_lookup.py "record a shape table row for a first-parent walk over a
prepared merge"` ranked `rows`, `row`, `merge`, `records` (`tools/memory-tree/gotchas.py`) and `walk`,
name stems only; `records` is the reader of the record this unit edits. `python
tools/memory-recall/query.py "what does a first-parent walk read from a merge onto the default tip"`
returned TOOL-dSweptBranches-6, `TOOL-dPlacedRequest-45`, this audit's H2 and TOOL-dDeclaredLoop-44;
none disagrees with source.

Recall terms used: first-parent no-merges prepared merge default tip shape table row name-status whole branch diff
