# TOOL-dSafePassage-55 — the roster hand-out refuses on TOOL-49 AC2's whole order predicate, written once as one probe

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-55-deviation-101.md](../build/2026-10-23-build-TOOL-dSafePassage-55-deviation-101.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-55-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-55-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
confirmed finding **id 1** at HIGH, its item **H1**. TOOL-dSafePassage-51 S1 holds the roster back
only while TOOL-dSafePassage-4's order is not above both TOOL-dSafePassage-43's and
TOOL-dSafePassage-7's. TOOL-dSafePassage-49's §3 hands-off bullet to TOOL-dSafePassage-51 carries the
same narrow wording. TOOL-dSafePassage-49 AC2 and TOOL-dSafePassage-51 AC1 also require
TOOL-dSafePassage-18 and TOOL-dSafePassage-19 above TOOL-dSafePassage-4, and moving them is a
separate header edit (TOOL-dSafePassage-49 §4 "The order move").

Within one order the driver breaks ties by string id (`tools/workflows/unattended-build.js:608-613`),
and `TOOL-dSafePassage-18` sorts before `TOOL-dSafePassage-4`. So a sweep that moves TOOL-4 to order 3
and leaves 18 and 19 there passes S1's refusal, and both consumers build before the unit they consume
from.

This unit is id 1's promotion. The refusal tests TOOL-dSafePassage-49 AC2's whole predicate, and the
predicate is written once, as §4's probe, which the hand-out step runs. It builds at order 15, one
above TOOL-dSafePassage-51 (order 14), whose S1 it repairs. The probe runs at the hand-out, before
any pass, so the §3 hands-off bullets of TOOL-dSafePassage-49 and TOOL-dSafePassage-51 to this unit
name it for the sweep that TOOL-dSafePassage-49 §8 F1(a) gives the build run.

## 2. Scope (IN)

- **S1** — The probe. §4 "The order probe" reads the status header of every spec under
  `memory/builds/dSafePassage/spec/` through `_parse_order` of `tools/memory-tree/gen_build_index.py`.
  It checks four relations: TOOL-dSafePassage-43 above TOOL-dSafePassage-3; TOOL-dSafePassage-4 above
  TOOL-dSafePassage-43 and above TOOL-dSafePassage-7; TOOL-dSafePassage-18 above TOOL-dSafePassage-4;
  and TOOL-dSafePassage-19 above TOOL-dSafePassage-4. Each failed relation prints one line naming both
  units and their orders, and the probe exits 1. With none failed it prints `order ok` and exits 0.
  Observed by AC1, AC2 and AC3.
- **S2** — The refusal. TOOL-dSafePassage-51 S1's refusal is read as "the build run hands out no
  roster while §4's probe exits non-zero", in place of its two-relation condition.
  TOOL-dSafePassage-49 AC2 is read as that probe's exit 0. TOOL-dSafePassage-49's §3 hands-off bullet
  to TOOL-dSafePassage-51 is read with the same four relations. Observed by AC1 and AC2.
- **S3** — One source. The probe's text lives in this spec's §4 alone. TOOL-dSafePassage-51 S1 and
  TOOL-dSafePassage-49 AC2 cite it, and the build run copies it into its scratchpad and runs it from
  there, never retyping a subset of it. Observed by AC3.

## 3. Non-goals (OUT)

- Moving the headers. TOOL-dSafePassage-49 §8 F1(a) gives the sweep that move, and this unit only
  refuses the hand-out until it is whole.
- A change to `tools/workflows/unattended-build.js`. TOOL-dSafePassage-49 F1(c) refused it.
- An order inversion between units no relation here names, which TOOL-dSafePassage-49 §7 already
  leaves out.
- The attribution of TOOL-dSafePassage-51 AC1 and AC2 to the sweep: finding 2, batched in
  `TOOL-dSafePassage-59`.

### Edges

- **consumes-from** `TOOL-dSafePassage-49` — AC2's four relations and F1(a)'s sweep, which S1 writes as one probe and S2 makes the hand-out's refusal; without them there is no predicate to run
- **consumes-from** `TOOL-dSafePassage-51` — S1's hand-out refusal, which S2 widens to the whole predicate
- **hands-off** `TOOL-dSafePassage-59` — TOOL-dSafePassage-51 AC1 and AC2 recorded as checks of the sweep, whose staged refusal is this unit's AC3, finding 2 of the spec audit of units 51 and 52

## 4. Design

### The order probe

```python
import sys, glob, os
sys.path.insert(0, "tools/memory-tree")
import gen_build_index as g
d = sys.argv[1]
o = {}
for p in glob.glob(os.path.join(d, "*-spec-TOOL-dSafePassage-*.md")):
    head = next(l for l in open(p, encoding="utf-8") if l.startswith("**Status:**"))
    o[int(p.rsplit("-", 1)[1][:-3])] = g._parse_order(head, p)
need = [(43, [3]), (4, [43, 7]), (18, [4]), (19, [4])]
bad = [f"TOOL-dSafePassage-{a} at order {o[a]} is not above TOOL-dSafePassage-{b} at order {o[b]}"
       for a, bs in need for b in bs if not o[a] > o[b]]
print("\n".join(bad) or "order ok")
sys.exit(1 if bad else 0)
```

It runs from the repository root as `python <scratchpad>/order_probe.py <spec directory>`.
`_parse_order` is the parser that renders the README's build-order region, so the probe and the
region read one grammar. This unit ran it on node d, Python 3.14.5, 2026-10-23, over three trees:

| Tree | TOOL-4 | TOOL-18, TOOL-19 | Output | Exit |
|---|---|---|---|---|
| the spec directory at this spec's commit | order 2 | order 3 | two lines naming TOOL-43 and TOOL-7 | 1 |
| a scratch copy, TOOL-4 moved to order 3 | order 3 | order 3 | two lines naming TOOL-18 and TOOL-19 | 1 |
| the same copy, 18 and 19 moved to order 4 | order 3 | order 4 | `order ok` | 0 |

### Inventory

Minted: none in the tree. The probe is a scratch file the build run writes from §4. No function,
constant, conf key, gate leg or policy key.

### Migration

None.

### Rollout

Live at the next hand-out. The unit sits at order 15, one above TOOL-dSafePassage-51. Its probe
runs at the sweep, before the roster is handed out, and its own pass writes no file in the tree.

### Files touched (estimate)

None in the tree: the probe is a scratch file, and the sweep's header edits are TOOL-dSafePassage-49
F1(a)'s.

### Alternatives rejected

- **Widening S1's sentence to four relations and leaving the check to whoever reads it.** The report
  names the predicate's second copy as the defect's cause; a sentence is a third copy.
- **A probe that reads the README's build-order region.** The region is rendered from the headers
  after the sweep, so a probe over it would grade a render step rather than the move.

## 5. Production-readiness checklist

- security: N/A — a read-only probe over spec headers.
- perf / scale: one header read per spec.
- error / empty / loading states: a malformed `order` verb raises `_parse_order`'s `Problem`, which
  stops the hand-out as a non-zero exit does.
- observability: each failed relation names both units and both orders.
- risks: a unit without an `order` verb reads `None`, and the comparison raises, which also stops
  the hand-out.
- testing: the three trees of §4 and the criteria of §6.
- migration: none.
- user docs: N/A — a build-run step with no `help/` page.

## 6. Acceptance criteria

- **AC1** — When §4's probe runs over a scratch copy of `memory/builds/dSafePassage/spec/` in which
  TOOL-dSafePassage-4's header reads `order 3` and TOOL-dSafePassage-18's and TOOL-dSafePassage-19's
  still read `order 3`, it prints lines naming `TOOL-dSafePassage-18` and `TOOL-dSafePassage-19` and
  exits 1.
  Red when: the probe tests TOOL-dSafePassage-4 only against TOOL-dSafePassage-43 and
  TOOL-dSafePassage-7, so the half-done sweep passes.
- **AC2** — When the build run's sweep ends, §4's probe over `memory/builds/dSafePassage/spec/` prints
  `order ok` and exits 0, before the roster is handed out.
  Red when: the sweep left any of the four relations unmet and the roster went out.
- **AC3** — When §4's probe runs over a scratch copy in which TOOL-dSafePassage-4's header still reads
  `order 2`, it prints lines naming `TOOL-dSafePassage-43` and `TOOL-dSafePassage-7` and exits 1.
  Red when: the probe cannot produce a negative on the unswept tree.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory-hygiene self-test`

This unit adds no arm and moves none. Its criteria are observed by the build run at the sweep, and
the main loop records them in this unit's acceptance ledger under a `Pass: none` commit.

What the check does not cover: a README build-order region left stale after the sweep, which the
index generator's own check owns, and the commit order TOOL-dSafePassage-51 AC1 reads afterwards.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 51 and 52's id 1
  (HIGH, item H1).

## 10. Reuse audit

The seam extended is `_parse_order` with `ORDER_RE` in `tools/memory-tree/gen_build_index.py`
(`:212`, `:455`), the order-verb parser the build-order region is rendered from, read at source on
2026-10-23. `python tools/codebase-map/reuse_lookup.py "check build order verbs of specs before handing out a roster"`
ranked `check`, `before`, `build` and `roster`, name-token matches; none compares two units' orders,
so the relations are new and the parse is reused.

Recall terms used: `python tools/memory-recall/query.py "how the build run refuses to hand out a roster whose order verbs invert a consumes-from edge" --terms "spec audit promoted order verb hand-out roster sweep tie-break consumes-from header probe"`
