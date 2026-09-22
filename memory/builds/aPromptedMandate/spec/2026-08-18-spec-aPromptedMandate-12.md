# TOOL-aPromptedMandate-12 — `build-complete` reads the units table, not the whole region

**Status:** CLOSED · rev-2 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPromptedMandate-12-spec-audit.md](../reviews/2026-08-18-review-TOOL-aPromptedMandate-12-spec-audit.md) | spec-audit | TOOL-aPromptedMandate-13 |
| [2026-08-19-review-TOOL-aPromptedMandate-12-tier2-diff.md](../reviews/2026-08-19-review-TOOL-aPromptedMandate-12-tier2-diff.md) | diff-review | TOOL-aPromptedMandate-13 |

<!-- /gen:spec-records -->

## 1. Goal

Make the `build-complete` Definition-of-Done item satisfiable by a build that follows the method. Its
selector spans the whole generated region, which renders two tables, so every review record the
method mandates is counted as an unfinished unit.

## 2. Scope (IN)

- **S1** — `unit_rows` selects only rows whose link target is under `spec/`, which is where M2 puts a
  unit's spec. The records table links to `build/` and `reviews/` and drops out by construction.
- **S1b** — **`verb_status` is routed through `nonterminal_units` instead of open-coding the same
  pipeline.** It is a SECOND reader of the same region and rev-1 did not know it existed: it inlines
  `region … | grep -E '^| \[' | grep -vE '| (CLOSED|WONTDO) |' | head -1 | sed …` and never calls
  either helper. Narrowing only `unit_rows` would leave `--close` reading the units table while
  `--status` and `--resume` keep reading the records table — two answers to one question, which is
  what the extraction's own comment says it exists to prevent. MEASURED on a landed build:
  `--status aBranchedMandate` reports `next 2026-08-16-build-TOOL-aBranchedMandate-3-repro-c3.sh`,
  offering a record filename as the next unit.
- **S2** — an arm per direction: a build whose specs are all terminal and which carries records
  satisfies the item; one with a genuinely non-terminal spec still fails it.
- **S3** — the anti-vacuity arm. Narrowing a selector can narrow it to NOTHING, and term 3 of
  `build-complete` (`unit_rows` non-empty) is the guard that already exists for exactly that — this
  unit adds the arm proving that guard fires when the selector matches no row.
- **S4** — the backlog row `TOOL-aPromptedMandate-8` closes, naming this unit. (That row is the
  build-complete finding; the id clash with this unit's former number is why it was renumbered.)

## 3. Non-goals (OUT)

- **No change to the other four terms.** Roster presence, `missing_units`, non-emptiness and the
  terminal-status filter are all correct; only the population they read was wrong.
- **No change to `gen_build_index.py`.** Rendering both tables into one region is the generator's
  design and other readers depend on it. The defect is in what the driver SELECTS, not in what the
  generator writes.
- **No retroactive edit of landed builds.** `aBranchedMandate` and `aStandingWrit` carry the same
  shape and are left exactly as they are; the fix changes how they would be READ, not their bytes.

## 4. Design

### The discriminator, measured

The units table links to `spec/`; the records table links to `build/` or `reviews/`. Measured across
three builds in this corpus:

| build | rows matching `^\| \[` | rows linking `spec/` |
|---|---|---|
| `aPromptedMandate` | 12 | 8 |
| `aBranchedMandate` | 13 | 6 |
| `aStandingWrit` | 3 | 1 |

The `spec/` count equals the unit count in all three. **This build's own row is re-measured at rev-2**
and moved as this build wrote records — rev-1 recorded 9/6 and the tree already read 11/8 by the
commit that added the spec. A table of live measurements inside a spec goes stale the moment the
build it measures does anything, which is why the ARM below reads the tree rather than this table. So:

```sh
unit_rows() { region "$1" "$SRC_OPEN" "$SRC_CLOSE" 2>/dev/null | grep -E '^\| \[.*\]\(spec/'; }
```

**`.*`, not `[^]]*`.** A negated class stops at the first `]`, so a unit whose spec title contains one
would be DROPPED from the selection — and a dropped unit row is a false GREEN: `nonterminal_units`
cannot see it, so `build-complete` passes over an unfinished unit. Greedy `.*` matches the last
`](spec/` on the line, which is the link, and a title containing `](spec/` verbatim is not a case
this corpus can produce.

**Why the link target and not the status column.** Filtering rows that merely CONTAIN a status token
would work today and rot the moment a record's kind column holds a word that looks like one. The link
target is what M2 already uses to define a unit's spec, so this selector and that definition move
together or not at all.

### Why this is not the run editing its own judge

Stated because it is the reason this unit was parked rather than folded silently. The run does not
decide whether it is complete — it makes the check able to answer the question it already asks. The
five terms, the roster join and the terminal-status filter are untouched; a genuinely unfinished unit
still fails, and S2 carries the arm that proves it.

### Files touched (estimate)

`tools/unattended/unattended.sh` — `unit_rows` AND `verb_status`'s inline derivation, which is the
second reader rev-1 missed · `tools/unattended/unattended.test.sh` (four arms) · `memory/backlog/TOOL.md`
(close the row).

## 5. Production-readiness checklist

- security — N/A; the item is a completeness verdict, not an authorization one
- perf / scale — N/A, one grep pattern
- a11y / i18n — N/A
- error / empty / loading states — a selector matching nothing is already refused by term 3, and S3
  is the arm that proves it
- observability — `--close` names the unmet item; unchanged
- risks — narrowing to nothing (armed, S3); a build whose generated region predates the two-table
  render (measured: all three sampled builds render both tables)
- testing + left-shift gates — the three arms in S2 and S3; the item itself is the regression gate
- migration / rollback — no stored state changes; landed builds are read differently, not rewritten
- user docs — the driver's own comment at the item, which already explains the five terms

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --close aPromptedMandate` runs over this build,
  `build-complete` is no longer reported unmet, AND no other DoD item newly appears — the criterion
  is that the item is MET, not that a complaint is absent, which a differently-failing term would
  also produce.
- **AC1b** — When `bash tools/unattended/unattended.sh --status aBranchedMandate` runs, the unit it
  names is a spec id and not a record filename; today it prints a `build/` filename.
- **AC2** — When a spec under a build carries a non-terminal status, `bash tools/unattended/unattended.test.sh`
  observes `build-complete` still unmet — the item did not become vacuous.
- **AC3** — When the generated region contains records but no `spec/`-linked row,
  `bash tools/unattended/unattended.test.sh` observes term 3's existing refusal firing rather than a
  silent pass.
- **AC4** — When `bash tools/unattended/unattended.test.sh` runs, its printed assertion count has
  grown and `bash tools/check-testsuite-counts.sh` stays green.
- **AC5** — When `memory/backlog/TOOL.md` is read, `TOOL-aPromptedMandate-8` is closed naming this
  unit, and no id in this build is carried by both a spec and an open backlog row.

## 7. Gates

`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/cross-component.test.sh` · `bash tools/check-testsuite-counts.sh` ·
`bash tools/run-gates.sh`

## 8. Open questions

none — the fork below is RESOLVED.

- **Fix the selector, or override the item** — RESOLVED (owner, 2026-08-18): fix it, as this unit.
  Put to the owner because it is DoD machinery discovered at close, and a run that repairs the check
  judging it should not make that call for itself.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft, after the owner ratified fixing the selector.
- rev-2 · 2026-08-18 · folded the M4 audit. BLOCKER: `unit_rows` is not the single reader —
  `verb_status` open-codes the same pipeline and rev-1's §10 claimed otherwise; S1b added, measured
  live. The `[^]]*` class would drop a unit whose title contains `]`, a false GREEN. The measured
  table was already stale. AC1 could pass on an absent complaint; AC1b added. Renumbered from `-7`,
  which the backlog already held.

## 10. Reuse audit

Satisfied for the SET in unit 1's reuse audit; this unit adds one probe of its own. The seam is
`unit_rows` in `tools/unattended/unattended.sh`, the single reader both `nonterminal_units` and
`build-complete`'s terms 3–5 go through — and rev-1 claimed one function therefore carried the whole
fix. That was FALSE and the audit measured it: `verb_status` open-codes the identical pipeline and
reaches the same region without either helper, so the fix is two sites, not one. The claim is left
here in corrected form rather than deleted, because "I checked the callers" and "I grepped for the
helper's name" are different acts and only the second one happened. Verified against source rather than against prose: the two-table render was confirmed
by reading three builds' generated regions, including two that already LANDED with the condition
present, which is what establishes the defect as pre-existing rather than introduced here.


**The id was reallocated at rev-2.** This unit was first minted as `-7`/`-8`, which the backlog
already held for two different findings this same run had filed. The manifest's id protocol says
collision-grep `memory/` before minting and that step was skipped; the spec audit caught it. Nothing
downstream depended on the old number.
