# TOOL-aDrainedSluice-4 — V4: the §9 rev high-water stops at §9

**Status:** CLOSED · rev-3 · 2026-08-20 · node a · Tier-2 · base 76fcd09b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-08-review-TOOL-aBatchedTribunal-1-3.md](../../reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md) | diff-review | TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8 |
| [2026-08-08-review-TOOL-aDrainedSluice-2-1.md](../../reviews/2026-08-08-review-TOOL-aDrainedSluice-2-1.md) | spec-audit | TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 |

<!-- /gen:spec-records -->

## 1. Goal

Check 12's rev high-water scan opens at `## 9. Revision log` and never closes. Every `rev-N` after
it — including in §10 and in any prose that follows — raises the high-water, so a header rev is
"logged in §9" whenever a larger number appears anywhere below §9. The backlog row reproduced 99
against a true 1. Close the range at the next `##`.

## 2. Scope (IN)

- **S1** — the scan closes on the next `^## ` heading after §9 opens. Inside §9 the behaviour is
  unchanged: every `rev-N` on every line contributes, and the maximum is the high-water.
- **S2** — this is a VERDICT change and is treated as one. It can only SHRINK the scanned range, so
  it can only produce MORE findings, never fewer. MEASURED BEFORE ANY EDIT, by reimplementing both
  readings over the real corpus: 22 in-scope specs carry a parseable header rev, and the two
  readings differ on ZERO of them. Nobody pays, and the acceptance evidence therefore comes from the
  fixture rather than the corpus — which is exactly why S3 exists.
- **S3** — the fixtures cover BOTH newly-reachable sub-paths of the branch, which has two conditions:
  `!seen` (no `rev-` token anywhere in §9) and `hrev > mx` (§9 logs a smaller rev). One fixture
  exercises `hrev > mx` — header rev-2, §9 logs rev-1, §10 carries rev-99. A SECOND exercises
  `!seen` — a ten-section spec whose §9 body is non-empty but holds no `rev-` token at all, with
  rev-99 in §10. Without the second, an implementation that closes the range for the maximum but
  leaves `seen` set below §9 passes while the masking survives, which is the case §1 names.
- **S3b** — the silent direction is NOT counted as new coverage. The existing corpus already pins it:
  `tFixture-1` and `tFixture-18` are asserted silent, and both would red the instant §9's own entries
  stopped being scanned. Crediting it would justify skipping the `!seen` fixture.
- **S4** — the comment that currently explains why the reset is ABSENT is replaced by one explaining
  why it is present and what it changed. It lives INSIDE a single-quoted awk program, so it may
  contain no apostrophe — the existing "engine s" is that scar, not a typo to correct.
- **S5** — `check-arms` does NOT see this finding. It keys on shell `fail` call sites, and check 12's
  per-spec messages are awk `print` statements funnelled into one `fail 12 "spec files dated >= …"`
  that is already ARMED. So no branch is added, no floor moves, and the harness assertion is the ONLY
  protection this change has. That is stated rather than papered over, and S5b supplies the second
  layer.
- **S5b** — a SOURCE-level assertion joins the three the harness already carries: the reset line is
  present in the engine. The corpus delta is zero, so a deleted fixture assertion would otherwise
  leave the regression invisible to the corpus, to `check-arms` and to both floors at once.

## 3. Non-goals (OUT)

- Widening what counts as a rev mention inside §9. A bare `rev-N` anywhere in the section is
  deliberate: a §9 line may carry two revs, and a strict line grammar would red legitimate entries.
- Changing the header-rev extraction.
- Retro-editing any spec that newly reds. If the measurement finds one, its §9 is fixed as a separate
  visible edit, not smuggled into the engine change.

## 4. Design

### Data model

```
before : in9 opens at `## 9. Revision log` and runs to the end of the body
after  : in9 opens there and CLOSES at the next `^## `
```

Everything else in the loop is untouched: the same `match(L, /rev-[0-9]+/)` walk, the same maximum,
the same `seen` flag driving the "not logged at all" arm.

### Inventory

| Concern | Change |
|---|---|
| `in9` range | gains a close on the next `^## ` |
| the comment above it | rewritten to describe the reset, not its absence |
| the self-test | two fixtures, one per direction |
| the corpus | measured before and after; delta recorded |

### Migration

None, unless the measurement finds a spec that newly reds — in which case that spec's §9 is fixed in
the same commit, visibly.

### Rollout

One commit: the reset, the comment, the two fixtures, and any §9 the measurement exposes.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` and its test, plus `memory/HYGIENE.md` and the
  re-rendered `tools/memory-tree/HYGIENE.template.md`.

### Alternatives rejected

- **Close the range on `## 10.` specifically.** Rejected: it is a spelling of the same idea that
  breaks the moment a spec has a different section after §9, and the canon is date-gated so both
  nine- and ten-section shapes exist in this corpus.
- **Leave it.** Rejected: the row exists because a real spec measured 99 against a true 1, and a
  high-water that any later number can satisfy makes the whole check green-by-accident.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one comparison per body line, inside a loop that already runs.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a spec with no §9 at all is unchanged: `seen` stays 0 and the
  branch fires, which is the existing behaviour.
- observability — the message is unchanged, so an existing reader is not surprised.
- risks — a VERDICT change. Bounded by measurement: the corpus is checked before and after.
- testing + left-shift gates — two fixtures, both directions.
- migration / rollback — one commit.
- user docs — `memory/HYGIENE.md` check 12's wording gains one clause, then
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The render direction is LIVE to
  SHIPPED; editing the template alone reds the parity leg and its printed remedy discards the edit.

## 6. Acceptance criteria

- **AC1** — When a spec's §9 logs its header rev and §10 carries a larger `rev-N`, check 12 is
  silent.
- **AC2** — When a spec's §9 does NOT log its header rev but §10 carries a larger `rev-N`, check 12
  fails naming that spec — the arm that fails before this unit and passes after.
- **AC3** — When a spec has no §9 at all, check 12 fails, unchanged.
- **AC4** — When the corpus is measured before and after, the delta is recorded in the build journal,
  and any spec that newly reds is fixed visibly rather than by widening the rule back.
- **AC5** — When a spec's §9 body is non-empty but holds NO `rev-` token and §10 carries a larger
  one, check 12 fails naming it. This is the `!seen` sub-path, silent before the change and red
  after.
- **AC5b** — When the reset line is deleted from the engine, the harness fails on a SOURCE-level
  assertion even if the fixture arms are also deleted. `check-arms` cannot help here and the spec
  says so: this finding is an awk `print`, not a `fail` branch.
- **AC6** — When `check-memory-hygiene.test.sh` runs, its pass line prints last.

## 7. Gates

`bash tools/run-gates.sh`; the `memory hygiene`, `memory-hygiene self-test` and `harness arms` legs
carry this unit.

## 8. Open questions

none — the fork below is RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork — accept the verdict change, or gate it behind a cutoff.** Options: apply it to every spec,
  or date-gate it the way §10 is. RESOLVED (owner, 2026-08-08): apply it. A cutoff exists to stop a
  NEW rule from redding old work; this is not a new rule but a correction to an existing one that was
  reading the wrong range, and a spec whose §9 does not log its header rev was always non-conforming.
  The measurement decides whether anyone pays, and the answer is recorded either way.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded the pre-edit corpus measurement into S2: 22 in-scope specs, zero
  affected. The change is safe here, and the fixture is the only thing that can prove it works.
- rev-3 · 2026-08-08 · folded review 1: M6 corrects S5/AC5 — `check-arms` does not see awk `print`
  findings, so the old criterion was already true before the unit — and adds a source-level
  assertion as the second layer; M13 adds the `!seen` fixture, without which a partial implementation
  passes; M16 records the no-apostrophe constraint inside the awk program; M12 corrects the doc edit
  direction. The correction also propagates to V2, whose ordering premise cited V4.

## 10. Reuse audit

Three lines inside an existing awk block, two fixtures in an existing harness. The rev extraction,
the message, the `seen` flag and the header parse are all untouched, so the change is exactly the
range and nothing else. No new file, no new key, no new leg.
