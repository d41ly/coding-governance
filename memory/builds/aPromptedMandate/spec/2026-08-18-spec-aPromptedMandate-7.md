# TOOL-aPromptedMandate-7 — `build-complete` reads the units table, not the whole region

**Status:** SPECCED · rev-1 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Make the `build-complete` Definition-of-Done item satisfiable by a build that follows the method. Its
selector spans the whole generated region, which renders two tables, so every review record the
method mandates is counted as an unfinished unit.

## 2. Scope (IN)

- **S1** — `unit_rows` selects only rows whose link target is under `spec/`, which is where M2 puts a
  unit's spec. The records table links to `build/` and `reviews/` and drops out by construction.
- **S2** — an arm per direction: a build whose specs are all terminal and which carries records
  satisfies the item; one with a genuinely non-terminal spec still fails it.
- **S3** — the anti-vacuity arm. Narrowing a selector can narrow it to NOTHING, and term 3 of
  `build-complete` (`unit_rows` non-empty) is the guard that already exists for exactly that — this
  unit adds the arm proving that guard fires when the selector matches no row.
- **S4** — the backlog row `TOOL-aPromptedMandate-8` closes, naming this unit.

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
| `aPromptedMandate` | 9 | 6 |
| `aBranchedMandate` | 13 | 6 |
| `aStandingWrit` | 3 | 1 |

The `spec/` count equals the unit count in all three. So:

```sh
unit_rows() { region "$1" "$SRC_OPEN" "$SRC_CLOSE" 2>/dev/null | grep -E '^\| \[[^]]*\]\(spec/'; }
```

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

`tools/unattended/unattended.sh` (one function) · `tools/unattended/unattended.test.sh` (three arms) ·
`memory/backlog/TOOL.md` (close the row).

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
  `build-complete` is no longer reported unmet.
- **AC2** — When a spec under a build carries a non-terminal status, `bash tools/unattended/unattended.test.sh`
  observes `build-complete` still unmet — the item did not become vacuous.
- **AC3** — When the generated region contains records but no `spec/`-linked row,
  `bash tools/unattended/unattended.test.sh` observes term 3's existing refusal firing rather than a
  silent pass.
- **AC4** — When `bash tools/unattended/unattended.test.sh` runs, its printed assertion count has
  grown and `bash tools/check-testsuite-counts.sh` stays green.
- **AC5** — When `memory/backlog/TOOL.md` is read, `TOOL-aPromptedMandate-8` is closed naming this
  unit.

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

## 10. Reuse audit

Satisfied for the SET in unit 1's reuse audit; this unit adds one probe of its own. The seam is
`unit_rows` in `tools/unattended/unattended.sh`, the single reader both `nonterminal_units` and
`build-complete`'s terms 3–5 go through — so one function carries the whole fix and no consumer
needs to know. Verified against source rather than against prose: the two-table render was confirmed
by reading three builds' generated regions, including two that already LANDED with the condition
present, which is what establishes the defect as pre-existing rather than introduced here.
