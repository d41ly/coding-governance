# TOOL-dCalibratedLens-29 — the work-order population read without argv: paths on stdin, one history pass, one policy read per policy revision, timed over the real tree

**Status:** DEFERRED · rev-3 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 9 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-29-deviation-291.md](../build/2026-11-02-build-TOOL-dCalibratedLens-29-deviation-291.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-30 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 |

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
  "Amendments (round-1 spec audit)", id 52, and rev-3, round-2 ids 19, 34 and 35):
  `python tools/roles/handoff.py reads -` reads the paths from stdin, one per line, and refuses a path
  argument beyond `-`. S2 takes every sliced work order's adding commit from
  `tree_lib.read_adding_commits(root, "memory/builds/*/prompts/*.md", wanted, newest=True,
  timeout=120)` (`tools/memory-tree/tree_lib.py:302-325`), the one adding-commit reader, whose single
  `git log --no-renames --diff-filter=A --reverse` with `newest=True` keeps a re-added work order's
  newest add, the add that wrote its bytes at `HEAD` (round-2 id 19 and round-3 ids 15 and 20,
  `TOOL-dCalibratedLens-38`). A tracked work order the reader leaves unanswered, a merge-added one
  say, is counted into one stderr line `item-budgets — <n> work order(s) with no adding commit` and
  left out of the population, never raised (round-2 id 34). Each adding commit's
  `.governance/policy.toml` text comes from ONE `tree_lib.read_blobs_at` call; commits are grouped by
  that text, every commit whose answer is `None` (no policy file) joining one absent group (round-2
  id 35), and `policy.py get memory.item-budget --rev <one commit of the group> --json` runs once per
  group, the absent group's answer being the catalogue default. `tree_lib` is reached through
  `resolve_kit_dir`, as `load_tree_lib` in `tools/policy/check_policy.py` reaches it. The step runs
  under a 120 s bound, passed to both shared readers as their `timeout` keyword, and a timeout reads
  `item-budgets: unread · timed out` (round-3 id 20). §5's perf line states the
  passes. Observed by AC2.
- **S2** — The proof over the real tree, at this unit's order: `python measure.py --fixture --plant
  item-budget-tree` runs the step over this repository's own tracked work orders, prints one
  `item-budgets` line per role it finds or the `96000 until 30` reading, and prints its wall time,
  which is under the 120 s bound. It also asserts that the step's unmapped count equals the number of
  tracked work orders a per-path `git log --diff-filter=A -1` answers with nothing (round-2 id 34),
  and the measure fixture's planted history carries one pre-policy commit whose work order is read
  under the absent group (round-2 id 35). Observed by AC2.
- **S3** — The argv probe: `git ls-files 'memory/builds/*/prompts/*.md' | python tools/roles/handoff.py
  reads -` exits 0 over the whole population, and `handoff.py reads <path> <path>` exits 2 naming the
  stdin form. Observed by AC3.

## 3. Non-goals (OUT)

- Capping the population to the newest commits that can still feed each role's newest 30, the review's
  third option. The one-pass history makes the full population cheap, and a cap would need a second
  rule for a role that has fewer than 30 recent work orders.
- The newest `loop-review` record's read in S6: id 50 (`TOOL-dCalibratedLens-28`).
- The re-added and renamed work-order plant: `TOOL-dCalibratedLens-38` (round-2 id 19). The leg's
  guard reaching `handoff.py`, `tree_lib.py` and `policy.py`: `TOOL-dCalibratedLens-41` (round-2 id 13).
- AC1 observes only the disposal's text in unit 6's spec and is green at writing; it is a
  precondition, not an observation of this unit's build (the round-2 audit's ids 4, 18 and 29).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-6` — `handoff.py reads`, `derive_role_item_budgets` and the `measure.py --fixture` plants it adds; without them there is no step to time
- **hands-off** `TOOL-dCalibratedLens-38` — the one-pass step and the `measure.py --fixture` frame, which that unit's `item-budget-history` plant runs over a re-added and a renamed work order (round-2 id 19)

## 4. Design

### Evidence

- spec-6 S1: "The verb `python tools/roles/handoff.py reads <path>…`"; S2: "its commit the one that
  added it (`git log --diff-filter=A -1 --format=%H -- <path>`)"; §5: "one `handoff.py reads` call over
  every work order, one `git log` per work order".
- 2,170 paths and 197,728 bytes, the skeptic's `git ls-files` measure at `8bec4cef`; about 0.16 s per
  `git` process on this node, so one `git log` per work order costs minutes.
- `tools/memory-tree/tree_lib.py:302-340` at base: `read_adding_commits`, "THE one adding-commit
  reader", and `read_blobs_at`, one `git cat-file --batch` answering `None` for a missing object.
- The round-2 review's probes (PINNED, 2026-11-02): with `--no-renames`, 2 of 2,172 tracked work
  orders have no adding commit (`dGroundRules-86-3-spec-writer.md` and `-86-merge-brief.md`,
  merge-added at `f53cd3fcb`); of the 849 adding commits, 629 hold no `.governance/policy.toml` and
  220 hold one blob, `43fa1bb1`.
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
- perf / scale — one `handoff.py reads -` call, one `git log` pass, one `git cat-file --batch` and one
  policy read per distinct policy text, the absent group included, bounded at 120 s and timed over the
  real tree by S2.
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
  A precondition read at writing: it greps the disposal's text.
- **AC2** — When `python measure.py --fixture --plant item-budget-tree` runs from the loop kit
  directory, it exits 0, prints a wall time under 120 s, prints the unmapped count equal to the
  per-path answer, and reads the planted pre-policy work order under the absent group.
  Red when: process creation fails, the bound is exceeded, an unmapped path raises or vanishes
  uncounted, or a commit with no policy file is left unread.
  figure: DERIVED, the tree's population at observation time.
- **AC3** — When `git ls-files 'memory/builds/*/prompts/*.md' | python tools/roles/handoff.py reads -`
  runs, it exits 0; `python tools/roles/handoff.py reads a.md b.md` exits 2 naming `reads -`.
  Red when: the verb still takes the population as argv.

## 7. Gates

`policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop measure fixtures` (TOOL-dCalibratedLens-4 S9) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/measure.py · covers AC2 · the `item-budget-tree` plant, staged red by a step that refuses when the argv it would pass exceeds 32,767 bytes, so the red holds on every host (round-2 id 41) · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 52 (HIGH, item H11) of the round-1 spec audit;
  unit 6 amended at the disposal (its rev-2).
- rev-2 · 2026-11-02 · §3 §4 §5 §7 §10 S1 S2 AC1 AC2 · amended at the disposal of the round-2 spec
  audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: S1's history read through
  `tree_lib.read_adding_commits` and `read_blobs_at` (id 19, `TOOL-dCalibratedLens-38`); the
  unmapped-path line (id 34), the absent policy group (id 35), the host-independent staged break (id
  41), the guard pointer (id 13) and AC1 stated a precondition (ids 4, 18, 29), all
  `TOOL-dCalibratedLens-41`; §3 gains the hands-off to unit 38.
- rev-3 · 2026-11-03 · S1 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from `TOOL-dCalibratedLens-48`: S1's reader
  call keeps the newest add (id 15) and carries the 120 s bound through the readers' `timeout`
  keyword (id 20), both `TOOL-dCalibratedLens-38` S3.

## 10. Reuse audit

The seams extended are unit 6's own `handoff.py reads` and `derive_role_item_budgets`, and the two
shared history readers `tree_lib.read_adding_commits` and `tree_lib.read_blobs_at`
(`tools/memory-tree/tree_lib.py:302-340`); the policy read stays `policy.py get --rev`
(`tools/policy/policy.py:1346-1374`, read by unit 6 at base). `python
tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an unread line, never
the walk's exit"`, run once for the set, ranked name stems only. Rev-1 said no seam batches per-path
history; the round-2 audit (id 19) found `read_adding_commits`, and the source decides. The recall probe returned TOOL-cMendedVintage-19, the placement
ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
