# TOOL-dCalibratedLens-29 — the work-order population read without argv: paths on stdin, one history pass, one policy read per policy revision, timed over the real tree

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 9 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-29-deviation-291.md](../build/2026-11-02-build-TOOL-dCalibratedLens-29-deviation-291.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 52, HIGH, item H11 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Unit 6 S1 defines
`handoff.py reads <path>…` with the paths as argv, and its §5 runs "one `handoff.py reads` call over
every work order". `git ls-files 'memory/builds/*/prompts/*.md'` lists 2,170 paths of 197,728 bytes at
`8bec4cef` (PINNED, the skeptic's measure, 2026-11-02), about six times Windows' 32,767-character
command line, so process creation fails, `gather` raises, and every Loop Review period is blocked.
Unit 6 S2 also runs one `git log` per work order. This unit takes the population off argv, reads its
history in one pass, and proves the step over the real tree within a stated bound. It repairs
`TOOL-dCalibratedLens-6`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 6's text (rev-2, its §4
  "Amendments (round-1 spec audit)", id 52): `python tools/roles/handoff.py reads -` reads the paths
  from stdin, one per line, and refuses a path argument beyond `-`; S2 takes every work order's adding
  commit from ONE `git log --diff-filter=A --name-only --format=%H -- 'memory/builds/*/prompts/*.md'`
  pass; it reads `memory.item-budget` once per distinct blob of `.governance/policy.toml`, each commit
  mapped to its blob by one `git cat-file --batch-check` over `<sha>:.governance/policy.toml` lines, and
  `policy.py get memory.item-budget --rev <one commit of that blob> --json` per blob; the step runs under
  a 120 s bound and a timeout reads `item-budgets: unread · timed out`. §5's perf line states the three
  passes. Observed by AC1.
- **S2** — The proof over the real tree, at this unit's order: `python measure.py --fixture --plant
  item-budget-tree` runs the step over this repository's own tracked work orders, prints one
  `item-budgets` line per role it finds or the `96000 until 30` reading, and prints its wall time,
  which is under the 120 s bound. Observed by AC2.
- **S3** — The argv probe: `git ls-files 'memory/builds/*/prompts/*.md' | python tools/roles/handoff.py
  reads -` exits 0 over the whole population, and `handoff.py reads <path> <path>` exits 2 naming the
  stdin form. Observed by AC3.

## 3. Non-goals (OUT)

- Capping the population to the newest commits that can still feed each role's newest 30, the review's
  third option. The one-pass history makes the full population cheap, and a cap would need a second
  rule for a role that has fewer than 30 recent work orders.
- The newest `loop-review` record's read in S6: id 50 (`TOOL-dCalibratedLens-28`).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-6` — `handoff.py reads`, `derive_role_item_budgets` and the `measure.py --fixture` plants it adds; without them there is no step to time

## 4. Design

### Evidence

- spec-6 S1: "The verb `python tools/roles/handoff.py reads <path>…`"; S2: "its commit the one that
  added it (`git log --diff-filter=A -1 --format=%H -- <path>`)"; §5: "one `handoff.py reads` call over
  every work order, one `git log` per work order".
- 2,170 paths and 197,728 bytes, the skeptic's `git ls-files` measure at `8bec4cef`; about 0.16 s per
  `git` process on this node, so one `git log` per work order costs minutes.
- The refuted id 19 found the SLICED population near zero at base; the argv call is still over every
  work order, sliced or not, because S1 decides slicing by reading each file.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `item-budget-tree` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/measure.py` — S2, the plant

### Alternatives rejected

- **`--from <file>`.** A temporary file for a list stdin already carries.
- **The loop kit listing the work orders itself.** `handoff.py` owns the work-order grammar
  (`MARKER_RE`); a second reader of it in the loop kit is the duplication unit 6 S1 avoids.

## 5. Production-readiness checklist

- security — stdin paths are read as data; `handoff.py` opens only tracked files, as before.
- perf / scale — three subprocess passes plus one policy read per policy blob, bounded at 120 s,
  timed over the real tree by S2.
- error / empty / loading states — a timeout is an `unread` reading; an empty population prints no
  role line.
- observability — the plant prints the wall time.
- risks — a very large history slows the one `git log` pass, which the bound reports as `unread`.
- testing — the plant of S2 and the probe of S3.
- migration — N/A.
- user docs — `tools/roles/README.md` documents `reads -` through unit 6's amended S1.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'reads -' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-6.md`
  runs, it prints the amended S1 and §5 lines.
  Red when: the design still passes the population as argv.
- **AC2** — When `python measure.py --fixture --plant item-budget-tree` runs from the loop kit
  directory, it exits 0 and prints a wall time under 120 s.
  Red when: process creation fails or the bound is exceeded.
  figure: DERIVED, the tree's population at observation time.
- **AC3** — When `git ls-files 'memory/builds/*/prompts/*.md' | python tools/roles/handoff.py reads -`
  runs, it exits 0; `python tools/roles/handoff.py reads a.md b.md` exits 2 naming `reads -`.
  Red when: the verb still takes the population as argv.

## 7. Gates

`policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop measure fixtures` (TOOL-dCalibratedLens-4 S9) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/measure.py · covers AC2 · the `item-budget-tree` plant, staged red by a step that passes the population as argv · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 52 (HIGH, item H11) of the round-1 spec audit;
  unit 6 amended at the disposal (its rev-2).

## 10. Reuse audit

The seam extended is unit 6's own `handoff.py reads` and `derive_role_item_budgets`; the policy read
stays `policy.py get --rev` (`tools/policy/policy.py:1346-1374`, read by unit 6 at base). `python
tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an unread line, never
the walk's exit"`, run once for the set, ranked name stems only; no seam batches per-path history, so
the one-pass log is new over those. The recall probe returned TOOL-cMendedVintage-19, the placement
ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
