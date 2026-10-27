# TOOL-dWellOiledMachine-95 — unit 90 never widens the shared spec token read: its S1 is handed whole to unit 93's caller-side join before unit 90 builds

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 66 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-95-deviation-951.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-95-deviation-951.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-3 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md`),
finding 1, item H1, at HIGH. TOOL-dWellOiledMachine-90 (order 65) S1 still has unit 90 widen
`design_lib.read_spec_writes` to return every `New arm:` suite path. TOOL-dWellOiledMachine-93
(order 66) exists because that widening turns `spec tokens` red, and it removes the widening one step
later; its S5 rev-bumps 90's S1 only at 93's own pass, after 90 has built. So unit 90 either cannot
pass green or builds the break, and `design_lib` ships in the copy-installed memory-tree kit, so a
landing that carries 93 forward ships the wrong reader to adopters. This unit rewrites 90's S1 so that
unit 90 builds no part of it, and deletes 93's revert clause, both before unit 90's pass.

## 2. Scope (IN)

- **S1** — Spec 90 loses S1's build. Spec 90 takes a rev bump, its §9 line naming this unit, finding 1
  of the round-3 promotions audit and finding 25 of the round-2 promotions audit:
  - its S1 reads: "Finding 2 (M1), on TOOL-dWellOiledMachine-68 and -13. NOT BUILT HERE: the suite path
    of each `New arm:` line joins the build-order write set in its one caller, through
    TOOL-dWellOiledMachine-93 S3, and this unit edits no `design_lib` spec reader. Observed by AC1.";
  - its AC1 reads: "When `git log --format=%s <BASE>..HEAD -- tools/memory-tree/design_lib.py` runs at
    this unit's pass, no subject names this unit. Red when: this unit's pass edits a `design_lib` spec
    reader.";
  - its Files touched no longer lists `tools/memory-tree/design_lib.py` or
    `tools/memory-tree/gen_build_index.py`, which only S1 named;
  - its §3 non-goal sentence "S1 is the one exception, because the parallel join is the finding
    itself", its §5 observability and risks lines, its §10 seam list and its hands-off line to
    TOOL-dWellOiledMachine-93 stop naming S1 as built here.
  Observed by AC1, AC3.
- **S2** — Spec 93 loses its revert. Spec 93 takes a rev bump, its §9 line naming this unit and
  finding 1: S3's clause "and any arm read a prior pass put into it is removed" is deleted, so S3 reads
  `read_spec_writes` as at this spec's base; S5's sentence opening "Spec 90 takes a rev bump at this
  unit's pass" is deleted, since S1 here carries that rev bump; and Files touched no longer lists spec
  90's file. 93's consumes-from line to TOOL-dWellOiledMachine-90 names S1 as handed to 93 whole.
  Observed by AC4.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md`, the one spec spelling the deleted clause and sentence. by value: NO VALUE READERS — spec prose no program reads.
- **S3** — The rev bumps land before unit 90's pass. S1's and S2's rev bumps are made by the build
  run's main loop at BUILD-METHOD M2's cross-read, before its first code pass, as one spec pass whose
  commit subject names this unit. At this unit's own pass, at order 66, nothing is written: the pass
  runs AC1 to AC5 and records them. Observed by AC2.

## 3. Non-goals (OUT)

- No change to 93's arm-line reader, its caller-side join, its dispatch sentence or its renders: 93
  S1 to S4 stand, and S5's re-render stands.
- No re-order of unit 90 or unit 93 (§4 Alternatives rejected).
- No lint over specs that rev-bump a lower-order sibling's scope item: the report's left-shift line,
  a separate mechanism (M2).
- 93 AC3's "before and after" wording is finding 2 (L1), and a criterion over 90's S1 paragraph for 94
  S26's rev bump is finding 9 (L3): both are carried by the minors batch TOOL-dWellOiledMachine-97.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-90` — S1, AC1, Files touched and the sentences naming S1 as built here, which this unit rewrites before unit 90 builds, so unit 90 edits no `design_lib` spec reader
- **consumes-from** `TOOL-dWellOiledMachine-93` — S3's caller-side join, which carries 90's S1 whole, and S3's revert clause and S5's rev bump of spec 90, which this unit deletes
- **hands-off** `TOOL-dWellOiledMachine-97` — 90's rewritten S1 paragraph, which the batch's item for finding 9 observes beside 94 S26's Files touched pointer
- **hands-off** `TOOL-dWellOiledMachine-98` — the §6 preamble, which gains the one ordering probe this build loads, before this unit's pass runs AC2 (round-4 promotions audit, finding 1)
- **hands-off** `TOOL-dWellOiledMachine-99` — S3 and §5's observability and risks lines, which state the commit pair the ordering claim compares (round-4 promotions audit, finding 11)
- **hands-off** `TOOL-dWellOiledMachine-100` — AC2's first half, rewritten to check each rev bump by ancestry against unit 90's build commit (round-4 promotions audit, finding 19)
- **hands-off** `TOOL-dWellOiledMachine-101` — §4, §5's testing line and §6, which gain the fixture and AC6 that observe the ordering check red (round-4 promotions audit, finding 29)
- **hands-off** `TOOL-dWellOiledMachine-108` — S1's text for spec 90, S2, AC3 and §4 Evidence, amended before this unit builds (round-4 promotions audit, findings 4, 10, 16 and 18)

## 4. Design

### Evidence

- Spec 90 is order 65 and spec 93 order 66 (each status header, line 3).
- 90 S1 has `read_spec_writes` add every `New arm:` suite path to the write set
  (`spec-90.md:41-45`), its AC1 observes the widened render (`:367-369`), and its Files touched opens
  with `tools/memory-tree/design_lib.py` and `tools/memory-tree/gen_build_index.py` (`:316`). No other
  scope item of spec 90 names either file.
- 93 S3 removes "any arm read a prior pass put into it" (`spec-93.md:46-48`), and 93 S5 rev-bumps 90 S1
  "at this unit's pass" (`:58-59`).
- `read_spec_writes` is "the one token read" of the spec-token checker's `extract_files_touched`
  (`tools/check-spec-tokens.py:577`), the guard-legs join's input, and returns Files touched words only
  at base (`tools/memory-tree/design_lib.py:528-540`).
- `SPEC_GUARD_LEGS_CUTOFF="2026-09-22"` is armed (`.memory-tree.conf:356`).
- The disposal harness checks a promotion's placement as the repaired unit's order plus one
  (`tools/workflows/unattended-build.js:2187-2197`), so this unit sits at 66, after unit 90.
- BUILD-METHOD M2 binds a cross-read of the spec set before the first code pass, on the interface and
  ordering axes, and fixes a disagreement in exactly one document by a rev bump
  (`memory/guides/BUILD-METHOD.md:66-71`). 90 S1 and 93 S3 spell `read_spec_writes`'s contract two
  ways, which is that disagreement.

### Inventory

Nothing is minted: this unit writes spec text only.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-90.md` (S1's rev bump)
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md` (S2's rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since both rev cells move)

### Alternatives rejected

- **The rev bumps at this unit's own pass.** That pass is at order 66, after unit 90's, so unit 90
  builds the widening and 93 reverts it: the finding itself.
- **Order 93 before 90, the report's second option.** It moves 93's whole build, the checker, the
  dispatch sentence and the tree-wide re-render, ahead of order 65, and 90's S1 text must still change
  before 90 builds. It adds a re-order to the same pre-build amendment and buys nothing.
- **This unit at order 65 beside unit 90, with a §3 edge sequencing it first.** The placement rule
  fixes this unit at 66, and a consumes-from from unit 90 to a unit ordered after it is the ordering
  defect M2's cross-read refuses.

## 5. Production-readiness checklist

- security — N/A — no write path, secret or surface; two specs' text changes.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — N/A — no runtime path.
- observability — AC2's history probe shows whether unit 90's pass touched `design_lib`.
- risks — a build run that skips M2's cross-read builds 90 S1 as first written; AC2 is red at this
  unit's pass in that case, and the remedy is 93 S3 as first written, which reverts the widening.
- testing — AC1 to AC5.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec 90>` and `<spec 93>` are the two files under Files touched, and `<BASE>` is the build run's
pinned `base:` fact in `memory/builds/dWellOiledMachine/RUN.md`.

- **AC1** — When `awk '/^- \*\*S1\*\*/{p=1} /^- \*\*S2\*\*/{p=0} p' <spec 90>` runs, its output names
  `TOOL-dWellOiledMachine-93` and `NOT BUILT HERE`, and the same output piped to
  `grep -c read_spec_writes` prints 0.
  Red when: 90's S1 still has unit 90 widen the shared token read.
- **AC2** — When `git log --reverse --format=%s <BASE>..HEAD | grep -E "TOOL-dWellOiledMachine-(90|95)([^0-9]|$)" | head -1`
  runs at this unit's pass, it prints this unit's amendment commit; and
  `git log --format=%s <BASE>..HEAD -- tools/memory-tree/design_lib.py | grep -cE "TOOL-dWellOiledMachine-90([^0-9]|$)"`
  prints 0.
  Red when: the amendment lands after unit 90's pass, or unit 90's pass edits `design_lib`.
- **AC3** — When `awk '/^### Files touched/{p=1;next} /^#/{p=0} p' <spec 90> | grep -c "design_lib.py"`
  runs, it prints 0.
  Red when: unit 90 still declares a write to `design_lib`, and its dispatch records one.
- **AC4** — When `grep -c "prior pass put into it" <spec 93>` and
  `grep -c "Spec 90 takes a rev bump" <spec 93>` run, each prints 0.
  Red when: 93 still reverts a widening nobody builds, or still owns 90's S1 text.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --check` runs after the rev bumps, it
  exits 0.
  Red when: the README's rev cells for specs 90 and 93 are left stale.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: AC2 is a history probe at this unit's pass, and 93's §7 arm stays the
observation of the caller-side join.

## 8. Open questions

- **F1 — When do S1's and S2's rev bumps land, given this unit's order is 66 and unit 90's is 65?**
  (a) at this unit's own pass; (b) at the build run's M2 cross-read, before its first code pass, as a
  spec pass naming this unit; (c) a re-order of 93 below 90. (a) is the finding: unit 90 builds what
  93 then reverts. (c) moves a whole unit's build and still needs the pre-build text change. (b) is the
  one route that reaches 90's text before 90's builder reads it, using the step M2 already binds, and
  leaves every order verb as the placement rule sets it. RESOLVED (agent, 2026-10-27, delegated): (b).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-3 promotions, finding
  1 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-4
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-98, TOOL-dWellOiledMachine-99, TOOL-dWellOiledMachine-100, TOOL-dWellOiledMachine-101, TOOL-dWellOiledMachine-108.

## 10. Reuse audit

The seam reused is BUILD-METHOD M2's pre-code cross-read, the method's one step that amends a spec
before any unit builds, and TOOL-dWellOiledMachine-93 S3's caller-side join, which already builds what
90's S1 asks. The probe `python tools/codebase-map/reuse_lookup.py "amend a lower-order spec before the
build run dispatches it"` ranked `run`, `before`, `build` and `run_git` by name stem, none a spec
amendment, because the act is a record change rather than a symbol. The recall query below ranked
TOOL-dTotalRecall-62, a repair that amends a sibling in its own step ahead of that sibling's pass,
second; that route needs an order equal to the amended unit's, which this unit's placement does not
give, so §4 records it as rejected.

Recall terms used: `python tools/memory-recall/query.py "when does a promoted repair rev-bump a
lower-order sibling spec before it builds" --terms "rev bump lower order sibling spec cross-read before
first code pass ordering axis promoted repair"`
