# TOOL-dFurnishedOrders-38 — the per-pass line's absence arms graded on their content: a named `miss` helper, and a probe whose red pattern reads each arm's text, never git grep's prefixed line

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 08e30fef · streams tooling · order 24 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-38-deviation-381.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-38-deviation-381.md) | deviation | — |
| [2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md) | research | TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md) | research | TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |
| [2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`)
confirmed finding **id 29 at HIGH**, report item **H1**. Id 1 reports the same defect at MEDIUM as
item M1 and takes `TOOL-dFurnishedOrders-42`, which counts the converted arms this unit names.

`TOOL-dFurnishedOrders-37` AC3 requires the lines of `git grep -n "for-diff HEAD~1" --
tools/unattended/adopt-unattended.test.sh` to be "none opening `hit `". `git grep -n` prefixes every
line with `<path>:<line>:`, so no printed line ever opens with `hit `. At `08e30fef` the probe prints
three lines, `:257`, `:605` and `:627`, and each is a presence `hit` assertion of the per-pass line
(read at `08e30fef`). The clause already passes on the unconverted tree. Unit 37 S4 has unit 30
answer its own AC3 in that amended form, and the unattended kit's suites are WAIVED for this landing
by the build README's rule, so this probe is the only guard on those arms, and it certifies nothing.

This unit gives the absence assertion a name in the suite and grades the arms by their own text. It
repairs `TOOL-dFurnishedOrders-37` and builds one step after it (order 24).

## 2. Scope (IN)

- **S1** — The absence helper. `tools/unattended/adopt-unattended.test.sh` gains `miss()` beside
  `hit()` (`:141`): it counts one assertion and fails, printing `FAIL present: <needle>`, when the
  needle IS found in the haystack, as `hit` fails when it is not. Observed by AC2.
- **S2** — The three arms on the per-pass line open with `miss `. The arms at `:257`, `:605` and
  `:627` (read at `08e30fef`; unit 30 S4 converts them to absence assertions) are written as `miss`
  calls with the same haystack and needle. Where unit 30's pass landed them in another absence
  form, this pass re-expresses that form through `miss`, so the suite carries one absence spelling.
  Observed by AC1.
- **S3** — The criterion graded on content. The red pattern is the arm's own text:
  `git grep -h -e "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh` prints the matching
  lines with no path or line prefix, and `grep -c` over that stream counts the lines opening
  `hit `. A count is taken with `grep -c` on git grep's own stdout, never by `printf '%s\n' "$x" | wc
  -l` over a captured variable, which counts one line for an empty capture. Unit 37's ledger answers
  the adopt-unattended half of its AC3, and unit 30's ledger the same half of its AC3, in the
  AMENDED form, naming this unit's AC1. Observed by AC1.

## 3. Non-goals (OUT)

- The floor on the converted arms, that at least three `miss` lines carry the per-pass line: the
  minors batch `TOOL-dFurnishedOrders-42`, for id 1.
- Unit 37 AC3's second arm, over `tools/workflows/unattended-build.test.sh`: it reads
  `dispatch.args.checklist` lines and its clause `none spelling --for-diff HEAD~1` grades their text
  already.
- Running the adopter suite: it stays WAIVED at landing by the build README's rule, and its clean
  reading is owed with PLAY-dClosedLoop-18.
- The report's left-shift gate, a spec-lint over criteria that grep with `-n` and grade a line's
  opening: no clause of this build names it.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-30` — S4's conversion of the three arms on the per-pass line to absence assertions, which S2 writes through `miss` (id 29)
- **consumes-from** `TOOL-dFurnishedOrders-37` — AC3's adopt-unattended arm and S4's amended answer for unit 30, which S3 grades on content (id 29)
- **hands-off** `TOOL-dFurnishedOrders-42` — the `miss` helper and the three arms written with it, whose floor unit 42 counts (id 1)
- **hands-off** `TOOL-dFurnishedOrders-46` — the `miss` helper, its failure text, its three arms and the offender key it mints, which unit 46 S7, S14 and S16 settle (ids 20, 19, 28 of the fourth audit)

## 4. Design

### The helper

```bash
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }   # :141, unchanged
miss() { n=$((n+1)); ! grep -qF -- "$2" <<<"$1" || { echo "FAIL present: $2"; st=1; }; }
```

### The probe, before and after

```
git grep -h -e "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh | grep -c "^[[:space:]]*hit "
  at 08e30fef        -> 3   (the three presence arms; red)
  after this unit    -> 0   (green)
```

The `-h` flag is what makes the line's own text the subject. Without it the first field is the path,
and any pattern anchored at the line start grades the path.

### Inventory

Minted: the shell function `miss` in `tools/unattended/adopt-unattended.test.sh` and its failure text
`FAIL present:`. No flag, key or file.

### Migration

None: a suite's assertion helper stores nothing.

### Rollout

Live at landing, at order 24. The unattended kit's version moves where the kit epoch leg reads the
suite as shipped bytes.

### Files touched (estimate)

- `tools/unattended/adopt-unattended.test.sh`

### Alternatives rejected

- **Keep `git grep -n` and strip `^[^:]*:[0-9]+:` before grading.** It grades the same text through a
  pattern a Windows drive-letter path breaks; `-h` never prints the prefix.
- **Grade "none opening `hit `" with no named helper.** The converted arms could then take any
  shape, including a comment, and no reader could tell an absence assertion from a deleted one.
- **Re-point the arms in unit 30's spec text.** An audited spec is not rewritten from outside it;
  the ledger's AMENDED form is the route unit 37 S4 already uses.

## 5. Production-readiness checklist

- security — N/A: a suite helper and a read-only probe, no write path.
- perf / scale — one `grep` per arm, as `hit` costs.
- error / empty / loading states — an empty probe stream counts 0 under `grep -c`, which S3 states
  is the only counting form.
- observability — `miss` prints `FAIL present: <needle>` naming what survived.
- risks — the suite is WAIVED at landing, so the probe of AC1 is the observation until
  PLAY-dClosedLoop-18's clean reading.
- testing — AC1 and AC2 by a probe and a helper fixture; the arm of §7 at the close.
- migration — none.
- user docs — none: a suite helper.

## 6. Acceptance criteria

- **AC1** — When `git grep -h -e "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh`
  runs piped to `grep -c "^[[:space:]]*hit "`, it prints 0.
  Red when: a presence `hit` arm of the per-pass line survives, which the three arms at `08e30fef` do.
  figure: the count is 3 at `08e30fef` (PINNED, measured 2026-10-27), so the criterion is red before
  the unit is built.
- **AC2** — When `bash -c` evaluates the `hit()` and `miss()` lines that
  `grep -E "^(hit|miss)\(\)" tools/unattended/adopt-unattended.test.sh` prints, with `n=0 st=0`, then
  calls `miss "abc" "b"`, it prints `FAIL present: b` and leaves `st` at 1; calling `miss "abc" "z"`
  instead prints nothing and leaves `st` at 0.
  Red when: `miss` passes on a present needle, so a converted arm certifies nothing.
  fixture: none beyond the suite file; the helper lines are evaluated alone.

## 7. Gates

`unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/adopt-unattended.test.sh · covers AC1 · the three arms on the per-pass line written with `miss`, staged by restoring one `hit` arm; the suite stays WAIVED at landing by the build README's rule, its arm owed with PLAY-dClosedLoop-18 · none

## 8. Open questions

- **F1 — How is an absence assertion spelled in the suite?** Options: (a) a named `miss` helper
  beside `hit`; (b) an inline `! grep -qF` per arm; (c) whatever unit 30's pass writes. (b) and (c)
  leave the converted arms without a spelling a probe can count, so id 1's floor has nothing to
  count. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged fix of id 1
  ("name the absence-assertion helper"), which this unit's grading needs too. widens: none ·
  relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one repairs are unbuilt.** `TOOL-dFurnishedOrders-30` and `-37` are specced
  and unbuilt at `08e30fef`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on
  each at the pass and stops this unit if unit 30 S4 is still absent then, rung 1, the brief's rule
  for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-2 promotions, id 29
  (HIGH, item H1, related to id 1 at MEDIUM).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-46, promoted from the spec audit of the round-3 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seam extended: the suite's own assertion helpers, `hit`, `same`, `absent` and `present`
(`tools/unattended/adopt-unattended.test.sh:141-144`), of which `absent` already names a negative
for a path and none for a string; `miss` is their string twin. `python
tools/codebase-map/reuse_lookup.py "assert a string is absent from a rendered file in a shell suite"`
ranked `absent` in this same suite first (a SEAM, fan-in 30), then `corpus_files` and the
`ask_filed_in` pair, none a string-absence assertion, so the suite's own helpers are the seam and no
wider one fits. The recall probe returned the audit's M1 text and unit 4's reuse scout on the
per-pass line's readers, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "how does a suite assert the per-pass line is
absent from the rendered unattended Skill" --terms "per-pass line for-diff absence assertion hit miss
adopt-unattended suite git grep prefix content"`
