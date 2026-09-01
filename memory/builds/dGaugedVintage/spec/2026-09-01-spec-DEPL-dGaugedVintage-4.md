# DEPL-dGaugedVintage-4 — derive each kit's marker population, and assert every site in it

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-kit-versions.sh` asserts three of drift-audit's eight `gov:kit` marker sites, so five
shipped files carry `@1.2` and `@1.4` against a `1.8` constant and the bar stays green. Derive the
marker population from each kit's descriptor and assert every member of it.

## 2. Scope (IN)

- **S1** — A derivation that answers, for one entry, "which shipped files carry a `gov:kit <id>@`
  marker" — computed from the entry's own resolved file set, never from a list typed into a checker.
- **S2** — An assertion in both directions over that derived set: every marker in it equals the
  entry's version constant, and a file carrying a marker for an entry that does not claim it reds.
- **S3** — The five stale drift-audit markers repaired to `1.8` in the same change that arms S2, so
  the assertion lands green rather than landing red and being waived.
- **S4** — The remedy message names the DERIVED list, closing the half of
  `TOOL-aBoundedVerdict-29` this unit reaches: a remedy naming three files when the kit has eight is
  the defect that produced this state.

## 3. Non-goals (OUT)

- The four entries carrying no marker at all. That is `DEPL-dGaugedVintage-5`, which shares this
  unit's derivation and is ordered beside it.
- `tools/workflows/tier2-review.js`'s bare presence check. `TOOL-dTieredTribunal-6` owns that
  question and it is explicitly still the owner's.
- Changing any kit's version CONSTANT or bumping any kit. This unit makes the markers agree with the
  constants that already exist.
- The `check-verdict-epoch.sh` remedy for memory-tree. `TOOL-dSettledRoster-4` owns it; the same
  derivation should serve it, and this unit does not do that work.

## 4. Design

### Inventory

The eight drift-audit sites and what each says today, measured at `d65da7ab`:

| Site | Value | Asserted today |
|---|---|---|
| `tools/drift-audit/drift_report.py:51` (the constant) | `1.8` | yes |
| `tools/drift-audit/README.md:3` | `@1.8` | yes |
| `tools/workflows/drift-audit-code.js:15` | `@1.8` | yes |
| `tools/workflows/drift-audit-state.js:15` | `@1.8` | yes |
| `tools/drift-audit/adopt-drift-audit.sh:4` | `@1.2` | **no** |
| `tools/drift-audit/drift_report.py:4` | `@1.4` | **no** |
| `tools/drift-audit/drift_signals.py:3` | `@1.4` | **no** |
| `tools/drift-audit/drift_signals.template.py:3` | `@1.4` | **no** |
| `tools/drift-audit/selftest.py:4` | `@1.4` | **no** |

That is nine rows for eight marker sites plus the constant; `drift_report.py` appears twice because
it carries both the constant and a stale marker four lines above it.

### Migration

S3 is a value repair across five files. It is not a version bump: the constant does not move, so no
adopter's pin changes meaning.

### Alternatives rejected

Enumerating the eight sites in the checker was rejected because it is the shape that failed: a
hand-kept list is what let five files drift, and `TOOL-aBoundedVerdict-29` already names derivation
as the remedy.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one grep per entry over that entry's resolved file set; the sets are small.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry whose derived marker set is EMPTY must announce that,
  not pass silently; an empty population that reports clean is the vacuous-selector class.
- observability — the checker prints the derived count per entry so a reader can see it moved.
- risks — arming S2 before S3 would red the bar for every session until the repair lands, so the two
  ship together and the spec says so.
- testing + left-shift gates — the assertion IS the gate; its failing case is AC4.
- migration / rollback — none.
- user docs — none; the checker's own header states what it now covers.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-kit-versions.sh` runs at `HEAD` after this unit, all eight
  drift-audit marker sites read `1.8` and the leg exits 0.
- **AC2** — When one of the five previously-unasserted markers is edited to a wrong value,
  `bash tools/check-kit-versions.sh` exits non-zero and names that file, observed by staging the
  break and restoring it.
- **AC3** — When a file carries a `gov:kit` marker for an entry whose resolved file set does not
  include it, the checker reds, observed on a fixture.
- **AC4** — The assertion is observed RED before S3's repair lands: arm S2 alone against current
  bytes and confirm `bash tools/check-kit-versions.sh` names all five stale files.
- **AC5** — When an entry declares a version constant and its derived marker set is empty,
  `bash tools/check-kit-versions.sh` prints that entry with a zero count rather than omitting it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `kit version markers` leg is the one this unit changes, and
`govkit selfcheck` check 5b already reports registry-vs-checker disagreement in both directions.

## 8. Open questions

- **F1 — where the derivation lives.** `check-kit-versions.sh` is shell and the descriptors are TOML,
  which shell cannot read without help; `govkit.py` already parses them. Options: move the assertion
  into `selfcheck`, or have the shell call a small python helper. Recommendation: `selfcheck`, since
  it already holds check 5b and the registry is its subject. Unresolved.
- **F2 — whether a test fixture's marker counts.** `tools/memory-tree/check-verdict-epoch.test.sh:89`
  carries `gov:kit memory-tree@1.5` inside a `sed` that mutates a scratch fixture. It is noise in a
  deployer's grep, not a wrong claim. Recommendation: exclude `*.test.sh` from the derived set and
  say so in the checker's header. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- The seam is `read_descriptors` in `tools/govkit/govkit.py`, which already resolves every entry's
  descriptor and is what `selfcheck` check 5b reads;
  `python tools/codebase-map/reuse_lookup.py "assert every gov kit version marker site against its
  descriptor"` ranks it first among descriptor-aware symbols. No new seam is needed.
- Recall terms used: `gov:kit marker population derive descriptor kit.toml check-kit-versions
  verdict-epoch remedy carriers bump sites`
