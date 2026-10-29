# TOOL-dMindYourWords-25 — the unattended suites' missed readers of `landed-by attended`, re-pointed so their `miss` arms can fail

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 31 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, item
H3. TOOL-dMindYourWords-17 S4 moves the persisted value `landed-by attended` and the display
`LANDED (attended)` to `owner`, and its Readers name only part of the two suites that spell the old
literals. After the rename, the unnamed `miss` arms test for a string the code no longer prints, so they
can never fail, and the unnamed positive arms red. This unit moves every remaining suite reader of the
old literals to the new spelling and has each `miss` arm seen red on a staged break.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.test.sh`, the settle case's lines unit 17 S4 does not name: the
  positive arm `:10702` reads `phase LANDED (owner)`, the leg count `:10717` reads `owner LANDED 1`, the
  HELD case's `miss` arm `:10765` reads `LANDED (owner)`, and the comments `:10697`, `:10699` and
  `:10735` name the `owner` population. Observed by AC1 and AC3.
- **S2** — `tools/unattended/check-unattended.test.sh`, the leg's lines unit 17 S4 does not name: the
  empty-population count `:6100` reads `owner LANDED 0`, `:6175` reads `owner LANDED 1`, the `miss` arm
  `:6176` reads `population owner, missing`, and `:6180` reads `population owner, missing
  [units-at-landing]`. The planted record's `landed-by: attended` at `:6172` stays as written, the
  legacy record unit 17 S4 reads as `owner`, so the arm grades the legacy reading too. Observed by AC2
  and AC4.
- **S3** — Each of the two `miss` arms, `:10765` and `:6176`, is staged red once at the close: a HELD
  record forced to display `LANDED (owner)`, and a planted `owner`-population record missing
  `units-at-landing` before the `:6175` run. Declared on §7's `New arm:` lines, observed by the main
  loop (BUILD-METHOD M8). Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- The rename itself, its writer, its display and its other readers: TOOL-dMindYourWords-17 S4.
- The spec-lint rule the report names as H3's left-shift gate, requiring a rename spec to list every
  `git grep` hit of the old literal: a gate is its own unit (BUILD-METHOD M2), and no clause of this
  build names it.
- Rewriting the eight landed run-state records that carry `landed-by: attended`: a landed record is
  never rewritten (unit 17 S4).

### Edges

- **consumes-from** `TOOL-dMindYourWords-17` — S4's rename of `landed-by attended` and `LANDED (attended)` to `owner`, and its reading of a legacy `attended` as `owner`; without it the new spelling is never printed and every re-pointed arm reds
- **hands-off** `TOOL-dMindYourWords-37` — the re-pointed settle-case lines and the `check-unattended.test.sh` settle block, whose opening comment and kept legacy record the minors batch settles (review ids 8, 26 and 41)

## 4. Design

### Evidence

Read at `a1f119ec6`, no product file differing from base `ccd1292e`:

| File | Line | Text at HEAD | Kind |
|---|---|---|---|
| `tools/unattended/unattended.test.sh` | 10697, 10699, 10735 | comments naming `LANDED (attended)` and the `attended` population | prose |
| `tools/unattended/unattended.test.sh` | 10702 | `hit ... "phase LANDED (attended)"` | positive |
| `tools/unattended/unattended.test.sh` | 10717 | `hit "$out" "attended LANDED 1"` | positive |
| `tools/unattended/unattended.test.sh` | 10765 | `miss "$out" "LANDED (attended)"`, on a HELD record | negative |
| `tools/unattended/check-unattended.test.sh` | 6100 | `... · attended LANDED 0 - a count of 0, ...` | positive |
| `tools/unattended/check-unattended.test.sh` | 6175 | `hit "$out" "committed LANDING 0 · attended LANDED 1"` | positive |
| `tools/unattended/check-unattended.test.sh` | 6176 | `miss "$out" "population attended, missing"` | negative |
| `tools/unattended/check-unattended.test.sh` | 6180 | `hit "$out" "population attended, missing [units-at-landing] in ..."` | positive |

Unit 17 S4's Readers name `unattended.test.sh` `:10708`, `:10711`, `:10750` and
`check-unattended.test.sh` `:6169-6172` (`spec/2026-10-29-spec-TOOL-dMindYourWords-17.md:58-59`). The
report lists `:10697`, `:10702`, `:10765`, `:6100`, `:6175`, `:6176` and `:6180`; `git grep -n attended`
over the two suites adds `:10699`, `:10717` and `:10735`, which this unit covers too.

### The staged breaks

| Arm | Break staged at the close | Red observed |
|---|---|---|
| `:10765` `miss "LANDED (owner)"` | the `--status` display in `tools/unattended/unattended.sh` (unit 17 S4's `:8190`) printing `LANDED (owner)` for a HELD record | the `miss` fires |
| `:6176` `miss "population owner, missing"` | the fixture record at `:6172` written without `units-at-landing` before the `:6175` run | the `miss` fires |

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: S1
- `tools/unattended/check-unattended.test.sh`: S2

### Alternatives rejected

- **Folding the lines into unit 17's Readers**: the audit's exit promotes every finding to its own unit
  and folds none (BUILD-METHOD M4).
- **Deleting the two `miss` arms**: each guards a distinct wrong-green, a HELD record shown landed and a
  missing fact passed, and an arm seen red is worth keeping.

## 5. Production-readiness checklist

- security — N/A — test-suite text only, no write path or surface.
- perf / scale — N/A — no arm added to a suite's runtime beyond the two staged observations at the close.
- error / empty / loading states — the empty-population line `:6100` keeps its "a count of 0" wording,
  so a zero population still says it graded nothing.
- observability — each re-pointed arm prints its own failure through the suites' `hit`/`miss` helpers.
- risks — a line unit 17 moves by its own edits shifts these line numbers; the arms are found by their
  text, which §4's table quotes.
- testing — AC1 to AC4; the two `New arm:` lines of §7.
- migration — N/A — no data.
- user docs — N/A — suites only.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'LANDED (attended)' tools/unattended/unattended.test.sh` runs after the pass,
  it prints 0, and `grep -c 'LANDED (owner)'` over the same file prints at least 2.
  Red when: a reader of the old display survives, or the HELD case's `miss` still names it.
- **AC2** — When `grep -cE 'attended LANDED|population attended' tools/unattended/check-unattended.test.sh`
  runs after the pass, it prints 0, and `grep -c 'population owner, missing'` prints 2.
  Red when: a count line or the missing-fact arms keep the old population name.
- **AC3** — When the main loop stages the HELD-display break of §4 and runs the arm, `:10765`'s `miss`
  reports a failure; restored, it passes.
  Red when: the arm passes with the break staged, which is the vacuity this unit removes.
  permission: the suite run is the main loop's at the close, never this pass's.
- **AC4** — When the main loop plants the record of §4 without `units-at-landing` before the `:6175`
  run, `:6176`'s `miss` reports a failure; restored, it passes.
  Red when: the arm passes with the fact missing.
  permission: the suite run is the main loop's at the close, never this pass's.

## 7. Gates

`unattended kit gate`

New arm: tools/unattended/unattended.test.sh · covers AC3 · the `--status` display printing `LANDED (owner)` for a HELD record, under which `:10765`'s `miss` fires · none
New arm: tools/unattended/check-unattended.test.sh · covers AC4 · the `:6172` fixture record planted without `units-at-landing` before the `:6175` run, under which `:6176`'s `miss` fires · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 31 (HIGH, item H3) of the round-1 spec
  audit, with `:10699`, `:10717` and `:10735` added from a `git grep` the report did not list.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

No existing seam fits: the work is re-pointing assertions in two suites to a renamed literal, and the
suites' own `hit` and `miss` helpers are the seam they already use. `python
tools/codebase-map/reuse_lookup.py "re-point a suite's assertions after a persisted literal is renamed"`
ranked only name-stem regex builders (`build_spec_path_re`, `build_unit_id_re`), none of which reads a
suite, so the evidence is the `git grep -n attended` table of §4, read against both suites at HEAD.
The recall probe surfaced TOOL-dUnstuckLanding-14, the unit that wrote the `attended` population arms,
which agrees with §4's reading of `:6168-6180`.

Recall terms used: `python tools/memory-recall/query.py "which suite assertions read the landed-by attended value and the LANDED attended display" --terms "landed-by attended owner LANDED settle population miss hit check-unattended unattended.test vacuous rename"`
