# TOOL-aBlindedTrial-5 — M4 becomes the procedure for a declared audit, and the ruling is recorded

**Status:** INPROGRESS · rev-2 · 2026-09-20 · node a · Tier-2 · base b7dee206 · streams tooling+playbook · order 2 · ratified 2026-09-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round1.md](../reviews/2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 |
| [2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round2.md](../reviews/2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 |

<!-- /gen:spec-records -->

## 1. Goal

The method text stops saying every unreviewed spec is audited before its code: `BUILD-METHOD.md` M4
says when the audit is owed and keeps the procedure for that case, the kickoff tier rule stops
equating Tier 2 with "adversarial review before building", and one decision row records that the
`specs-reviewed` directive is the one MUST-by-default member made opt-in, with the trial as its
evidence.

## 2. Scope (IN)

- S1 — `tools/memory-tree/BUILD-METHOD.template.md` M4's opening paragraph ("Which, and this is what
  `specs-reviewed` measures…") is rewritten: owed when the build README declares `spec-audit:
  <date>`; recommended, not owed, for a set of two or more specs or an unresolved §8 fork; the
  procedure below it unchanged. The rewrite is net-negative in bytes, because the render sits 370
  B under its hard ceiling. Observed by AC1, AC2.
- S2 — M2's "a spec you wrote this run is unreviewed by definition" sentence stays, and the M1 loop
  sentence "review every unreviewed spec (M4)" reads "audit the set when declared (M4)". Observed by
  AC1.
- S3 — `memory/guides/BUILD-METHOD.md` is re-rendered by `adopt-memory-tree.sh`, `KIT_MEMORY_TREE
  _VERSION` moves 2.79 → 2.80 in every paired carrier, and the other three renders regenerate
  byte-identical except for the marker. Observed by AC3.
- S4 — `memory/guides/SESSION-KICKOFF.md:153` reads "Tier 2 (a spec before building; the spec audit
  is opt-in, M4) for: …", and the manifest's `last-audit` is re-stamped with a delta line in the
  commit message. Observed by AC4.
- S5 — `memory/DECISIONS.md` gains the row `TOOL-aBlindedTrial-6`: the `specs-reviewed` directive
  and its `specs-audited` term are owed only when a build declares `spec-audit:`, superseding the
  MUST-by-default ruling for that one member, citing the trial report's §5 figures. Observed by AC5.
- S6 — `memory/map/features/` prose for the memory-tree method carrier mentions the declaration.
  Observed by AC3.

## 3. Non-goals (OUT)

- `gen_build_index.py` is not edited: its front-matter parser has no closed key set, so
  `spec-audit:` needs nothing, and its informational "Ids no `spec-audit` record has ever named"
  line stays as it is.
- The product template `coding-governance-agents.template.md` is not edited: its §1 DoR names a
  spec and a menu, not an audit, and its §8 adversarial review is the diff review.
- No change to TEMPLATE-SPEC.md.

### Edges

- **consumes-from** `TOOL-aBlindedTrial-2` — the key name and shape M4 tells the reader to write.
- **hands-off** external — a later unit that adds a project-wide default, if one is ever wanted.

## 4. Design

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` · every
`KIT_MEMORY_TREE_VERSION` carrier (`check-memory-hygiene.sh:20`, the four template markers) and the
four renders · `memory/guides/SESSION-KICKOFF.md` · `memory/DECISIONS.md` · a `memory/map/features/`
dossier.

### Alternatives rejected

- Raising `tools/template-size-limits.txt:86` to fit a longer M4: the budget is a stated constraint
  of a document M7 re-reads at every pass boundary; the rewrite is a swap, not an addition.
- A PLAY-family row: the ruling being superseded is a TOOL row in the unattended driver, and the
  build's roster is `TOOL`; the family follows the carrier.

## 5. Production-readiness checklist

- security — N/A
- perf / scale — N/A
- error / empty / loading states — N/A, prose
- observability — the decision row is where the next session finds the why
- risks — the template's byte budget; a render left stale reds `kit/dogfood doc parity`
- testing — `check-template-size.sh` and `kit-dogfood-parity.test.sh --check`
- migration — none
- user docs — the rendered guide

## 6. Acceptance criteria

- **AC1** — When `grep -n 'spec-audit' memory/guides/BUILD-METHOD.md` runs after the render, it
  names M4's opening paragraph and M1's loop sentence, and `grep -c 'review every unreviewed spec'`
  on the file is 0.
  Red when: the old unconditional sentence survives anywhere in the file.
- **AC2** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs, it prints
  `template-size OK` with a byte figure ≤ 27278.
  Red when: the render grew.
- **AC3** — When `bash tools/check-kit-versions.sh` runs it exits 0, every `memory-tree@` marker
  reads 2.80, and `diff` between `BUILD-METHOD.template.md` and the render shows only the
  substituted tokens.
  Red when: a render or a marker is left behind.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh` runs after the tier-rule edit and
  the re-stamp, it exits 0 and reports no stale `last-audit`.
  Red when: the ratchet reds at the lander.
- **AC5** — When `grep -n 'TOOL-aBlindedTrial-6' memory/DECISIONS.md` runs, it finds one row naming
  `specs-reviewed`, `spec-audit:` and the trial report path.
  Red when: the row is absent or cites no evidence.

## 7. Gates

`build-method size` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `kit version markers` · `kickoff-manifest ratchet` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft from the scout of the method carriers at b7dee206.
- rev-2 · 2026-09-20 · S2 · M6's `passes-harnessed` sentence also moves: the harness runs AUDIT and
  DISPOSAL where `specAudit` is declared and hands out the roster on a terminal verdict or NOT-OWED.
  The builder parked it as outside S1–S6; folded here, render re-measured at 27275 bytes.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "render a kit template into its dogfood copy"` returned no candidate in the layer this
unit edits — it reports `unscanned layers: .sh` and resolves no `.js` symbol either — so the seam below
was found by reading the source, not by the probe. No new seam: the unit edits three existing carriers and appends one row. The renderer and the size
gate are reused as shipped. Recall terms used: BUILD-METHOD M4 spec audit opt-in declared byte
budget render parity tier rule kickoff manifest last-audit decision row supersede.
