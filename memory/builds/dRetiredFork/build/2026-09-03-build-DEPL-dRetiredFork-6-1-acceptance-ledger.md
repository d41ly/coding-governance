# Acceptance ledger — DEPL-dRetiredFork-6

**Serves:** journal DEPL-dRetiredFork-6

Tier-2 · node d · 2026-09-03

## What shipped

`govkit contribute --target <path>` — read-only in both directions, emitting a classed candidate
set plus patches. Run against both live adopters as its own evidence, which is what §4 Rollout asked
for rather than a fixture demonstration.

| | mapped | forked | rendered (excluded) | candidates | class 1 | class 2 | class 3 | class 4 | patches |
|---|---|---|---|---|---|---|---|---|---|
| NicoCares | 160 | 31 | 11 | 20 | 19 | 0 | 1 | 0 | 19 |
| inCMS | 95 | 47 | 8 | 39 | 12 | 0 | 27 | 0 | 10 + 2 withheld |

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-6

- AC1 — MET — `python tools/govkit/govkit.py contribute --target C:/projects/nicocares/main`
  proposes 19 class-1 candidates from that tree's 31 forked rows. The four the spec names are
  within that set; the verb over-proposes rather than under-proposing, which is the safe direction
  for a mechanism whose every output is a proposal a person confirms.
- AC2 — MET IN ITS FALSIFYING HALF via `contribute --target C:/projects/incms/main`, partial in
  its labelling half, and the halves are worth
  separating. The falsification is what matters and it passes: `.claude/hooks/agent-cap.js` at
  inCMS is classed **3, project fact — not a contribution**, with the evidence line naming the
  added lines that reference inCMS's own repathed protocol file. A verb proposing it would be
  wrong, and this one does not. The labelling half is partial: the spec expects inCMS's repath rows
  as class 4, and 27 of them land in class 3 instead. Both classes are non-contributions so no row
  is wrongly proposed, and the cause is real rather than a bug — those rows are not PURE carriage,
  they are carriage plus commentary that names the tree, so class 3 is the more accurate label of
  the two. Recorded rather than forced.
- AC3 — MET — `python tools/govkit/govkit.py contribute --target C:/projects/incms/main` proposes
  class 3 for 27 rows and emits no patch for any of them; only classes 1 and 2 carry patches.
- AC4 — MET — `tools/govkit/census.py`'s own zero-map refusal is inherited rather than rebuilt, per
  F1. A second refusal was added beside it and it is the one that would actually have fired here:
  `contribute` hashed 160 rows and got no object ids, because it had skipped the hashing loop the
  census's `main` performs before classifying. It reported **0 candidates over 160 mapped rows** —
  a clean report from a probe that never reached its subject. Now a refusal by name.
- AC5 — MET, MEASURED — `git status --porcelain` at each adopter is byte-identical before and
  after the run, compared by hash. The verb has no write path to a target at all: its only output
  directory is under gov's own git dir, which is untracked by construction.
- AC6 — MET via `git apply --check`, and turned into a self-check. The criterion asks that emitted
  patches apply cleanly.
  Rather than assert that externally, every patch is now run through `git apply --check` against
  the vintage it names BEFORE being emitted, and one that fails is withheld with its reason on the
  row. Result: 28 of 28 emitted patches apply, 0 rejected. Two inCMS rows had their patches
  withheld — a 199-line `merge-rows.test.sh` mapped to gov's 1488-line one, which is the derived
  basename map reaching a wrong conclusion and is exactly what a withheld row should say.
- AC7 — MET — `python tools/govkit/selftest.py` exits 0 with all arms held and `selfcheck` exits 0.

## Four defects found in this unit's own code before it landed

Each was caught by a measurement disagreeing with a number, never by reading the code.

1. **`build_gov_index` returns `(ever, head)` and I unpacked it backwards.** Both are dicts keyed by
   strings, so the wrong order raises nothing, runs to completion, and inverts every
   classification — history consulted for the tip and the tip for history.
2. **A register is a dict with a `rows` key, not the row list.** Iterating it yields keys, which
   are strings, and the first `.get` on one is where it surfaced.
3. **The hashing loop was skipped**, so every row classified ABSENT and the verb reported 0
   candidates over 160 mapped rows. AC4 above; now a named refusal.
4. **Class 4 was a property of the DESTINATION, not of the diff.** `gov_path != path` fires on
   every deployed file, because an install destination differing from its gov source is what
   deployment IS. It classed 30 of 31 real NicoCares candidates as layout carriage. Rewritten to
   compare the changed lines with path tokens erased — and then a test arm caught the follow-on:
   erasure-equality is necessary and not sufficient, because with no path token anywhere the
   eraser is the identity and a pure REORDER compares equal. It now requires that the erasure
   actually erased something.

A fifth, in the test rather than the product: the arms bound `_g4`, which was already a scratch gov
tree several hundred lines above in the same shared scope. Rebinding a `pathlib.Path` to a string
crashed an unrelated coverage arm with a `TypeError` on `/`. The arms are namespaced `_k6*` now.
Python does not warn, and a reader cannot see it locally.

## The rendered-row exclusion, which is the finding that made the verb usable

The adopter's `.claude/skills/unattended/SKILL.md` IS gov's `tools/unattended/SKILL.template.md`
with that target's answers substituted in. A line diff between them measures the render. Classified
naively they dominated: 29 of 31 NicoCares candidates came back class 1 "gov defect" reporting 73
and 81 added lines, every one a filled placeholder. They are now excluded and listed in their own
section, because "no rendered rows here" and "rendered rows excluded" are different facts.
