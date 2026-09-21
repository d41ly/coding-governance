# TOOL-aWokenSentinel-27 — unit 21's leg satisfies the three meta-gates that grade a manifest leg: the `PASS` count line, the `gate-legs` dossier claim with the map re-rendered, and the `subject-pins.tsv` row

**Status:** CLOSED · rev-1 · 2026-09-21 · node a · Tier-2 · base 830c46e8 · streams tooling · order 27

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-27-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-27-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-27-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-27-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close audit findings H3, H4 and H5 (round 4, raw ids 18, 29, 20, 30 and 19): `TOOL-aWokenSentinel-21`
adds `unattended-build self-test` to `tools/gate-legs.json` and names none of the three unguarded,
`subject = repo` legs that red on a new leg from the commit that lands it. `testsuite counts (every
bar self-test prints one)` takes every `*.test.sh` string in the manifest as its population
(`tools/check-testsuite-counts.sh:36`) and its `compliant()` at `:66` wants an anchored
`echo "PASS ($n assertions)"` beside the floor, which spec 21 §3 refused; `codebase-map coverage +
freshness` enumerates `gate-legs` as every leg name in the manifest (`map_extractors.py:72`) and
`test_every_inventory_key_is_claimed_or_baselined` at `test_codebase_map.py:93` reds on a key no
dossier claims; `govkit selfcheck` at `govkit.py:1743` reds any manifest leg with no row in
`tools/govkit/subject-pins.tsv`, a GENERATED file spec 21's `[[exempt_leg]]` row does not touch.
`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md` records the class by name. Spec 21
is folded at its rev-2 to drop the `PASS`-line non-goal and to hand these three enrolments here;
this unit is the enrolment, one leg in three registries, each observed by that registry's own
checker at the tip and seen RED at the tip of unit 21's pass. It is one mechanism — putting one
declared name where every reader of the manifest expects to find it — and the three registries are
its three carriers, the way spec 21's four files are one enrolment in the self-test population.

## 2. Scope (IN)

- **S1** — `tools/workflows/unattended-build.test.sh` prints `PASS ($n assertions)` on a green run:
  the line `[ "$st" = 0 ] && echo "PASS ($n assertions)"` between the `--- $n arms, exit $st`
  summary and `exit $st`, the shape of `tools/unattended/gate-guard.test.sh:457`, below the floor
  compare spec 21 rev-2 places above the summary. Observed by AC1.
- **S2** — `memory/map/features/review-harnesses.md` claims `unattended-build self-test` in
  `[claims].gate-legs` beside `tier2-review self-test` and `review-join self-test`, its prose
  refreshed on touch to name the fourth suite and what it exercises, and
  `memory/map/generated/MAP.md` and `memory/map/generated/inventories.json` are re-rendered by
  `python tools/codebase-map/gen_map.py --write` in the same commit. Observed by AC2.
- **S3** — `tools/govkit/subject-pins.tsv` gains the row `unattended-build self-test<TAB>kit<TAB>selftests`,
  written by `python tools/govkit/govkit.py selfcheck --write` and never by hand, in the same
  commit. Observed by AC3.
- **S4** — Each of the three checkers is observed RED at the tip of unit 21's pass — the commit
  whose subject carries `TOOL-aWokenSentinel-21` — naming the leg, before the enrolment is
  committed, and GREEN at this unit's tip. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- **No change to the leg, the budget row or the exemption row.** Those are spec 21's; this unit
  adds nothing to `tools/gate-legs.json`, `selftest-budgets.txt` or `registry.toml`.
- **No change to the floor block or the suite's arms.** The `PASS` line is the one line spec 21
  §3 refused; the compare, the pin and the after-exit self-read are spec 21 rev-2's.
- **No pre-flight over specs for the class.** The gotcha already anchors `tools/gate-legs.json`,
  so `gotchas.py --for-diff` names the class over any diff touching the manifest; the audit's
  spec-time grep is a commission concern outside this build's scope.
- **No dossier for the workflows kit's other suites.** `verifier fan-out self-test` is claimed
  wherever it is claimed today; this unit claims the one key it adds.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-21` — the leg name in the manifest, the floor block
  with its `st` and `n` variables, and the suite's summary line; without the leg there is no key
  to claim, no row to pin and no population membership to satisfy.
- **consumes-from** external — `tools/check-testsuite-counts.sh`'s `compliant()`,
  `tools/codebase-map/gen_map.py`, `tools/codebase-map/test_codebase_map.py`,
  `tools/govkit/govkit.py selfcheck --write`, and the three sibling rows in each registry that
  the new entries copy.
- **hands-off** external — nothing.

## 4. Design

### The line

Directly above `exit $st` in `tools/workflows/unattended-build.test.sh`, after spec 21 rev-2's
block, the tail of the file reads: the floor compare, `echo "--- $n arms, exit $st"`,
`[ "$st" = 0 ] && echo "PASS ($n assertions)"`, `exit $st` — the order of
`gate-guard.test.sh:455` to `:458`. `compliant()` anchors on the emitting line, so the `PASS` line
must be a column-0 statement and not a string inside a fixture generator, which is why it sits in
the file's tail and nowhere else.

### The claim

In `memory/map/features/review-harnesses.md`, `gate-legs` becomes the four names, and the dossier's
prose gains one sentence under its suites paragraph naming `unattended-build.test.sh` as the build
harness's suite, exercising `unattended-build.js` and `unattended-unit.js` with stub hooks and held
on the bar like its siblings. `gen_map.py --write` re-renders `generated/MAP.md` and
`generated/inventories.json`; `generated/symbols.json` moves only if a symbol did, and the pass
commits whatever `--write` wrote.

### The pin

`python tools/govkit/govkit.py selfcheck --write` regenerates every row of `subject-pins.tsv` with
both fields from the manifest; the diff is one added row, `unattended-build self-test`, `kit`,
`selftests`, and no other row moves. A hand-written row would pass the same check today and drift
the next time the file is regenerated, which is the reason the header says GENERATED.

### Why one unit and not three

Each carrier is a different file with a different checker, and BUILD-METHOD M2 makes a separate
generated artifact a separate unit. They are one unit here because the mechanism is one — a name
declared in a manifest is enrolled where the manifest's readers look for it — and a closing diff
of three one-line changes to three registries is attributable line by line: each AC names the
carrier whose checker observes it, so a finding lands on one file by construction.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `unattended-build self-test` | the existing leg name, as a dossier claim and a pin row | no cell; not a function |

No function, key, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/workflows/unattended-build.test.sh` | the `PASS ($n assertions)` line between the summary and `exit $st` |
| `memory/map/features/review-harnesses.md` | one claim in `[claims].gate-legs`; one sentence of prose |
| `memory/map/generated/MAP.md` | re-rendered by `gen_map.py --write` |
| `memory/map/generated/inventories.json` | re-rendered by `gen_map.py --write` |
| `tools/govkit/subject-pins.tsv` | one row, written by `govkit.py selfcheck --write` |

### Alternatives rejected

- **A row in `memory/project/testsuite-count-waivers.txt`.** The file is shrink-only by its own
  header and seeded from a measured population; a waiver is the ratchet reversed, and the line it
  would excuse costs one line.
- **A row in `memory/map/baseline.toml`.** Shrink-only too, and a claim is the unblock: the
  dossier already claims the three siblings.
- **Fold all three into spec 21.** The audit's own fix and the smaller record. Spec 21 is a
  promoted unit at rev-1 whose §3 states the opposite of S1; folding three HIGH findings into it
  is the disposition BUILD-METHOD M4 admits for a MEDIUM, and the closing diff of a seven-file
  unit could not tell which carrier a finding lands on.

## 5. Production-readiness checklist

- security — N/A; a suite line, a dossier claim and a generated row.
- perf / scale — nothing on the bar changes cost; the three checkers already run.
- error / empty / loading states — a red run prints no `PASS` line, which `compliant()` accepts
  because it grades the emitting line's presence, not its execution.
- observability — each checker names the leg in its refusal at the tip of unit 21's pass.
- risks — a future regeneration of the map or the pins from a manifest that lost the leg reds the
  declaration legs, which is the two-direction assertion spec 21 §4 relies on.
- testing — §6; three checkers at two commits.
- migration — additive.
- user docs — the dossier sentence.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-testsuite-counts.sh` runs at the tip it exits 0 and its output
  does not name the harness suite; at the tip of unit 21's pass — the commit whose
  subject carries `TOOL-aWokenSentinel-21` — the same run exits 1 with `pins a floor but does not
  print the agreed count line` naming that suite; and `grep -cE '^\[ "\$st" = 0 \] && echo "PASS
  \(\$n assertions\)"$' tools/workflows/unattended-build.test.sh` prints 1 at the tip, on a line
  above `exit $st`.
  Red when: the line is absent, a string inside a function, or below the exit, which
  `compliant()` refuses or cannot reach; or the checker was not RED at unit 21's tip, which means
  the population never held the suite and this unit enrols nothing.
- **AC2** — When `python3 tools/codebase-map/test_codebase_map.py` runs at the tip it exits 0, and
  `python tools/codebase-map/gen_map.py --check` exits 0; at the tip of unit 21's pass the first
  names `unattended-build self-test` as an unclaimed `gate-legs` key; and
  `grep -c '"unattended-build self-test"' memory/map/features/review-harnesses.md` prints 1 at the
  tip and 0 at this unit's base.
  Red when: the key is unclaimed, which the coverage leg reds at the close; or the generated
  artifacts are stale, which the freshness test reds; or the claim sits in a dossier that does
  not own `tools/workflows/`, which is a claim by a stranger.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs at the tip it exits 0; at the tip
  of unit 21's pass it prints `gate leg 'unattended-build self-test' has no row in
  tools/govkit/subject-pins.tsv`; and `grep -c '^unattended-build self-test	kit	selftests$'
  tools/govkit/subject-pins.tsv` prints 1 at the tip and 0 at this unit's base, with
  `git diff --stat` of the pins file between unit 21's tip and this unit's tip showing one
  insertion and no deletion.
  Red when: the row is absent, which selfcheck reds; or more than one row moved, which is a
  regeneration from a manifest that differs from the one unit 21 committed.
  figure: the diff figures are DERIVED by `git diff --numstat` at observation.

## 7. Gates

`testsuite counts (every bar self-test prints one)` · `codebase-map coverage + freshness` · `govkit selfcheck` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These run once at `--close`. The pass runs none of them as a bar: it verifies with the three
checkers of AC1 to AC3 run directly, each once at the tip of unit 21's pass and once at this unit's
tip, and the greps beside them. Under the first three, the new leg is the member this unit adds to
each population; under `every held leg is budgeted`, nothing moves.

New arm: none — this unit adds no assertion; it makes three existing legs read the suite spec 21 enrolled

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 4 as the
  promotion of H3 (raw ids 18, 29), H4 (raw ids 20, 30) and H5 (raw id 19), one unit because the
  three carriers enrol one name: the dropped non-goal and the hand-off are spec 21's rev-2 fold,
  and the enrolment is this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "enrol a new gate leg in every meta-gate that grades a
manifest leg: the PASS count line, the map dossier claim, the subject pin"` ranked `meta` across
the workflow scripts, `map_root` and `MapError` in `tools/codebase-map/map_lib.py` and `claims` in
`tools/codebase-map/selftest.py`, none an enrolment, and reported `unscanned layers: .sh`; no
Python seam fits, and none is needed — the three registries and their regenerators are the seam,
read at source: `compliant()` at `tools/check-testsuite-counts.sh:66`, the `gate-legs` extractor at
`tools/codebase-map/map_extractors.py:72` with the claim block at
`memory/map/features/review-harnesses.md:11`, and the pin loop at `tools/govkit/govkit.py:1742`
with its `--write` remedy in the refusal sentence. The recall probe returned `TOOL-aScouredKit-21`
(the counts checker hardcodes its manifest path — a portability row, not this class), this build's
own run-state row for this unit, and `TOOL-aTimedTurnstile-2` (which of the meta-gates are
correctly unguarded, confirming all three run on every bar); the gotcha
`a-new-leg-trips-a-growing-set-of-meta-gates` names the class and anchors the manifest, and no
prior record enrols this suite.

Recall terms used: `new leg meta-gates subject-pins dossier claim gate-legs inventory testsuite counts PASS line selfcheck codebase-map`
