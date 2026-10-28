# TOOL-dSafePassage-52 — the spec audit of units 47 to 50, its seven minors on TOOL-50: a misplaced arm that aborts the suite, one scan line, the arm's place read by content, the template repaired through its render, and the readings that cite them

**Status:** CLOSED · rev-3 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-52-deviation-98.md](../build/2026-10-23-build-TOOL-dSafePassage-52-deviation-98.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-52-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-52-ledger.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-52-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-52-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-51 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 47 to 50
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md`)
exited CONVERGED with 22 minors, which split into two disjoint write sets by BUILD-METHOD M6's
clauses. `TOOL-dSafePassage-51` batches the 15 whose writes are the step module. This unit batches the
other seven, all LOW. Each is named by its report id and is its own scope item, including where the
report merged ids into one item.

All seven land on TOOL-dSafePassage-50, so this unit repairs that unit and builds one above it, at
order 13. Where a minor would bite TOOL-dSafePassage-50's pass, that unit's own §3 hands-off bullet to
this unit names it, so that pass may build it.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-7 | LOW | 6, 20 | S6, S7 |
| D-8 | LOW | 7 | S1 |
| D-11 | LOW | 11 | S2 |
| D-14 | LOW | 15 | S4 |
| D-15 | LOW | 16 | S3 |
| D-16 | LOW | 17 | S5 |

The report refuted none of these seven and left none unverified, and the skeptic re-graded none of
them.

## 2. Scope (IN)

### The arm's failure mode and its place (D-8, D-11, D-15)

- **S1** — id 7. TOOL-dSafePassage-50 S1 is read with the failure mode the suite actually has.
  `tools/push-main.test.sh` runs under `set -u` (`:12`). An arm placed above the scan reads `_mt_rc`
  unbound, so the suite aborts with `unbound variable` and runs nothing after it. It does not take its
  `skip —` branch, and the misplacement is loud. This unit reproduced it on node d, 2026-10-23: under
  `set -u`, `if [ -n "$_mt_rc" ] ...` printed `_mt_rc: unbound variable`, exited 127 and printed
  neither branch. The placement rule stands. TOOL-dSafePassage-50 §7's staged break is read as that
  abort, not as "the `ok` line goes missing". In gov's own tree the arm's guard takes its `ok` branch,
  which AC1 observes; the printed `ok` line is TOOL-dSafePassage-50's `New arm:`, observed by the main
  loop at the close. TOOL-dSafePassage-50's §3 hands-off bullet to this unit names the reading.
  Observed by AC1.
- **S2** — id 11. TOOL-dSafePassage-50 §4 "The arm's place" is read by content. The suite's last arm
  ends at the `fi` that closes the 28-32 block, after its `skip — 28-32` else-branch. That `fi` was
  line 1047 at 2828457d and at the base, and line 1046 is the else-branch (PINNED, read on node d,
  2026-10-23). TOOL-dSafePassage-50's arm sits after that `fi` and before the suite's final
  `[ "$fail" = 0 ]` line. Its sentence that "the probe of AC1 re-derives both" is read as void: AC2
  here reads both lines. Observed by AC2.
- **S3** — id 16. `tools/push-main.test.sh` carries exactly one top-level `_mt_rc=` scan line, and the
  arm's `check-arms.py` load follows it. A second scan line pasted from TOOL-dSafePassage-46's arm
  skeleton is the second locator TOOL-dSafePassage-50 §4 "Alternatives rejected" refuses.
  TOOL-dSafePassage-50 AC1 is read with this clause. Observed by AC2.

### The template's one route (D-14)

- **S4** — id 15. TOOL-dSafePassage-50 S5 and its owner-table row are read with one route. A
  duplicate or a gap that TOOL-dSafePassage-50 AC2 finds in the `SPEC_AC_ORDER_CUTOFF` paragraph is
  repaired in `tools/memory-tree/SPEC-TEMPLATE.template.md` alone. The render of
  `tools/memory-tree/kit-dogfood-parity.test.sh`, run with `--render`, then writes
  `memory/TEMPLATE-SPEC.md` (`:30-32`: "never hand-edit the live copy"). `memory/TEMPLATE-SPEC.md`
  stays in Files touched as a render output only. A gap in
  `tools/memory-tree/.memory-tree.conf.example`, which the render does not write, is filled by hand.
  TOOL-dSafePassage-50's §3 hands-off bullet to this unit names the route. Observed by AC3.

### Readings of a description and a claim (D-7, D-16)

- **S5** — id 17. TOOL-dSafePassage-50 S4 is read as follows. `resolve_kit_dir` is the shared
  primitive `tools/lib/resolve_kit_dir.py`. `tools/push-main.sh:670-710` carries it inline as a
  byte-identical, gated copy, marked at `:673`. The suite only stubs it inside arm 27
  (`tools/push-main.test.sh:916`). A change to it is made in the canonical file under `tools/lib/`.
  NOT OBSERVED: a reading of a description, which no code carries.
- **S6** — id 6. TOOL-dSafePassage-50 §4 Rollout's "so the three passes at order 12 are disjoint
  (M6)" is read as follows. TOOL-dSafePassage-50's pass is disjoint from each of TOOL-dSafePassage-47
  and TOOL-dSafePassage-48. Those two share `tools/govkit/upgrade_steps.py`,
  `tools/govkit/selftest.py` and `help/upgrade-steps.md`, and they stay sequenced with each other by
  M6's first clause, as their own Rollouts state. NOT OBSERVED: a reading of a Rollout sentence, and
  dispatch is strictly sequential today (`tools/workflows/unattended-build.js:76`).
- **S7** — id 20. The same reading binds whoever re-opens parallel dispatch, the open
  `TOOL-cBriefedPilot-28`. At order 12 it may run TOOL-dSafePassage-50's pass beside one of the other
  two, never all three at once. NOT OBSERVED: no dispatch runs in parallel while that unit is open.

## 3. Non-goals (OUT)

- Every step-module minor: `TOOL-dSafePassage-51`.
- Rewriting a built spec. An item that corrects a spec's text states the reading here.
- The report's left-shift gates and checklist entries.
- A second arm. TOOL-dSafePassage-50's arm is the one this unit's readings place.

### Edges

- **consumes-from** `TOOL-dSafePassage-50` — S1's failure mode, §4's arm place, AC1, S4's owner table, S5's route and the Rollout sentence, which S1 to S7 read; without the arm's placement there is nothing to bound
- **hands-off** `TOOL-dSafePassage-57` — AC1 read as a probe of the arm itself: its guard line taken from `tools/push-main.test.sh` by content, evaluated after the scan and alone under `set -u`, and red at the base, finding 3 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-58` — AC1 staged over a wrong-file guard and an exported `_mt_rc`, the arm's skip line named apart, AC2 anchored on the 28-32 block's `fi` and loud on an absent anchor, S1's abort exiting 1 as a file, the `--render` route's four outputs with the other three left unchanged or restored, and a conditional `New arm:` line, findings 9, 14, 27, 15, 28, 10, 11, 20, 26 and 21 of the spec audit of units 51 and 52

## 4. Design

### The arm's place, by content

| Line in `tools/push-main.test.sh` | Content | Where TOOL-dSafePassage-46 S2's arm may sit |
|---|---|---|
| 12 | `set -u` | not here: it makes an unbound read abort the suite |
| 873 | the scan, `_mt_rc=$(cd "$HERE" && for d in */; ...`, the only one | after this line |
| 1046 | `echo "  skip — 28-32 ..."`, the 28-32 block's else-branch | not inside the 28-32 block |
| 1047 | `fi`, closing the 28-32 block | after this line |
| 1049 | `[ "$fail" = 0 ] && { echo "push-main.test: all cases ok"; ...` | before this line |

Line numbers are PINNED, read on node d, 2026-10-23, at the base. AC2 reads each line by its content,
so the numbers may move without the criterion moving.

### Inventory

Minted: none. No function, constant, conf key, gate leg, plant or policy key.

### Migration

None.

### Rollout

Live at landing. It builds at order 13, one above TOOL-dSafePassage-50 (order 12), whose arm place and
template route it repairs. Its write set is `tools/push-main.test.sh`, the template and its rendered
copy, and the example conf. That set does not meet `TOOL-dSafePassage-49`'s, also at order 13, which
is the step module, its self-test and its help page. Neither writes a file the other reads as a
contract or an acceptance input, and neither writes a shared mutable record, so the two passes at
order 13 are disjoint (M6).

### Files touched (estimate)

- `tools/push-main.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md`
- `tools/memory-tree/.memory-tree.conf.example`

### Alternatives rejected

- **Guarding the arm with `${_mt_rc:-}` (S1).** The arm would then skip silently when misplaced, the
  quiet failure TOOL-dSafePassage-50 S1 wrongly described. The abort is the louder signal and the
  placement rule already keeps it unreachable.
- **Pinning the arm's place to line 1047 alone (S2).** A line number goes stale at the next arm; the
  content of the `fi` and the final line do not.
- **Hand-editing `memory/TEMPLATE-SPEC.md` beside the template (S4).** The parity suite forbids it,
  and two hand edits can drift where one render cannot.

## 5. Production-readiness checklist

- security: N/A — a test arm's place, a render route and citations.
- perf / scale: unchanged.
- error / empty / loading states: a misplaced arm aborts the suite with `unbound variable` (S1); the
  arm's `skip —` line stays the honest outcome where no memory-tree kit sits beside the lander.
- observability: the suite prints the arm's `ok` line in gov's own tree.
- risks: none beyond TOOL-dSafePassage-50's.
- testing: AC1's guard probe, AC2's line reads and AC3's commit pairing.
- migration: none.
- user docs: N/A — `memory/TEMPLATE-SPEC.md` is the documentation S4 routes, and no `help/` page
  covers the lander's suite.

## 6. Acceptance criteria

- **AC1** — When `bash -c 'set -u; HERE=tools; eval "$(grep "^_mt_rc=" "tools/push-main.test.sh")"; [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ] && echo ok-branch'`
  runs from the repository root, it prints `ok-branch`. When
  `bash -c 'set -u; [ -n "$_mt_rc" ]; echo after'` runs, it prints `unbound variable`, exits 127 and
  prints no `after`.
  Red when: the arm's guard would take its `skip —` branch in gov's own tree, or an unbound read
  under `set -u` does not abort.
- **AC2** — When `grep -c '^_mt_rc=' tools/push-main.test.sh` runs, it prints `1`. When
  `grep -n -e '^_mt_rc=' -e 'check-arms.py' -e 'skip — 28-32' -e '^\[ "\$fail" = 0 \]' tools/push-main.test.sh`
  runs, the first line spelling `check-arms.py` has a greater number than the `_mt_rc=` line and the
  `skip — 28-32` line, and a smaller one than the final `[ "$fail" = 0 ]` line.
  Red when: the suite carries a second scan, or the arm sits above the scan, inside the 28-32 block or
  after the final line.
- **AC3** — When `git log --format='%H %(trailers:key=Pass,valueonly)' <BASE>..HEAD -- memory/TEMPLATE-SPEC.md`
  runs, `<BASE>` being the build run's pinned base, every commit it lists whose `Pass` trailer is
  `TOOL-dSafePassage-52` is also listed by the same command over
  `tools/memory-tree/SPEC-TEMPLATE.template.md`. The probe prints how many commits it paired, and
  prints `no edit` when it paired none.
  Red when: this unit's pass edits the live copy without the template.
  figure: the paired count is DERIVED; zero is the honest outcome where TOOL-dSafePassage-50 AC2
  found no gap, and it is printed as `no edit`, never as coverage.

## 7. Gates

`push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

This unit adds no arm and moves none. TOOL-dSafePassage-50's arm line is read with S1's abort as its
staged failing case.

What the check does not cover: an arm that reads a variable set by any line other than the scan, and
a live-copy edit that lands in a commit no `Pass: TOOL-dSafePassage-52` trailer names, which the
`kit/dogfood doc parity` leg grades instead.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 47 to 50's 7 LOW findings
  on TOOL-dSafePassage-50, one scope item per raw id.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions `TOOL-dSafePassage-57` and `TOOL-dSafePassage-58` of the spec audit of units 51 and 52, written by the disposal stage; no other section moved.
- rev-3 · 2026-10-26 · AC1 · AC1's grep operand is quoted, per the spec-tokens repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.

## 10. Reuse audit

The seams extended are the lander suite's top-level kit scan and its `set -u` posture in
`tools/push-main.test.sh`, and the dogfood render `render` in
`tools/memory-tree/kit-dogfood-parity.test.sh`, which
`python tools/codebase-map/reuse_lookup.py "render a kit template into its dogfood live copy"`
ranked among its seams, beside `live`, `kit_rel` and `resolve_kit_dir`. S4 routes the repair through
that render rather than a hand edit. `"count that a shell suite assigns a variable exactly once"`
ranked `counts`, `measure_typed_counts` and `parse_shell_defs`, name-token matches, none counting a
shell assignment, so AC2's `grep -c` is the observation and no existing seam fits beyond the suite's
own scan.

Recall terms used: `python tools/memory-recall/query.py "how a lander suite arm is placed after the scan it reads and a template repaired through its render" --terms "lander suite arm placement scan set-u unbound render template dogfood parity minors"`
