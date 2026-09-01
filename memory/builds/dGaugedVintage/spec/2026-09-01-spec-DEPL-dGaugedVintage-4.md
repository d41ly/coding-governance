# DEPL-dGaugedVintage-4 — derive each kit's marker population, and assert every site in it

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 3 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-4-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-4-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-kit-versions.sh` asserts three of drift-audit's eight `gov:kit` marker sites, so five
shipped files carry `@1.2` and `@1.4` against a `1.8` constant and the bar stays green. Derive the
marker population per kit and assert every member of it.

## 2. Scope (IN)

- **S1** — A derivation naming its BASIS explicitly: `entry_members` (`tools/govkit/govkit.py:356`),
  which claims an entry's non-landable and carved sources too, plus a DECLARED cross-entry allowance
  (see §4). Not `resolve_entry`'s `writes`, which reaches neither.
- **S2** — The forward assertion: every `gov:kit <id>@` marker inside the derived set equals that
  entry's version constant.
- **S3** — The reverse assertion over a DECLARED population, stated in §4 rather than left implicit:
  a file in that population carrying a marker for an entry that neither claims it nor is allowed to
  reds.
- **S4** — The five stale drift-audit markers repaired to `1.8` in the same change that arms S2.
- **S5** — The remedy message names the DERIVED list, closing the half of `TOOL-aBoundedVerdict-29`
  this unit reaches.

## 3. Non-goals (OUT)

- The four entries carrying no marker at all. That is `DEPL-dGaugedVintage-5`, ordered beside this.
- `tools/workflows/tier2-review.js`'s bare presence check. `TOOL-dTieredTribunal-6` owns it.
- Changing any kit's version CONSTANT. This unit makes markers agree with constants that exist.
- Closing `TOOL-aScouredKit-26`, the missing cross-entry destination token. The allowance in S1 is a
  DECLARATION that works around its absence, and §4 names it as the row that would retire it.
- The `check-verdict-epoch.sh` remedy for memory-tree. `TOOL-dSettledRoster-4` owns it.

## 4. Design

### The cross-entry problem, which rev-1 did not see

`tools/drift-audit/kit.toml` declares `home = "tools/drift-audit"` (`:4`) with `include = "**"`
(`:10`). So NO resolution of the drift-audit entry can contain
`tools/workflows/drift-audit-code.js` or `-state.js`: `tools/workflows/kit.toml` is entry id
`review-harness` and claims both through its own `**`. Yet both carry `// gov:kit drift-audit@1.8`
at `:15`, and `check-kit-versions.sh:211` asserts them today.

A naive per-entry basis therefore reds two CORRECTLY-valued markers while AC1 requires exit 0. Both
cannot hold, which is why S1 carries an explicit allowance: a descriptor may declare that another
entry's files carry its marker. That is a workaround for `TOOL-aScouredKit-26` — no cross-entry
destination token exists — and it is declared rather than inferred so the exception is visible.

`drift_signals.py` is NOT in this class. It is `project-owned` (`tools/drift-audit/kit.toml:14-15`),
and `resolve_entry` keeps project-owned rows in `survivors` (`:304-306`), so the basis reaches it and
S4 can name all five stale files.

### The reverse population, declared

A bare `git grep -lE 'gov:kit [a-z0-9-]+@[0-9]'` outside `tools/` and `skills/` returns 36 files at
this base, and 30 of them are spec and review PROSE under `memory/builds/**` — including this build's
own round-1 review record and an earlier revision of this very spec. That set is self-referential and
cannot be the population.

The declared population for S3 is: the union of every entry's `entry_members`, plus every declared
rendered destination, MINUS `memory/builds/**`. The rendered carriers outside `tools/` and `skills/`
are nine files: `.claude/hooks/agent-cap.js`, `.claude/hooks/scratch-guard.js`,
`.claude/skills/lexicon/SKILL.md`, `.claude/skills/unattended/SKILL.md`, `memory/HYGIENE.md`,
`memory/TEMPLATE-SPEC.md`, and the three `memory/guides/` documents.

### Inventory

The eight drift-audit marker sites and the constant, measured at `d65da7ab`:

| Site | Value | Asserted today | In a per-entry basis |
|---|---|---|---|
| `tools/drift-audit/drift_report.py:51` (the constant) | `1.8` | yes | yes |
| `tools/drift-audit/README.md:3` | `@1.8` | yes | yes |
| `tools/workflows/drift-audit-code.js:15` | `@1.8` | yes | **no — `review-harness` claims it** |
| `tools/workflows/drift-audit-state.js:15` | `@1.8` | yes | **no — same** |
| `tools/drift-audit/adopt-drift-audit.sh:4` | `@1.2` | no | yes |
| `tools/drift-audit/drift_report.py:4` | `@1.4` | no | yes |
| `tools/drift-audit/drift_signals.py:3` | `@1.4` | no | yes, via `survivors` |
| `tools/drift-audit/drift_signals.template.py:3` | `@1.4` | no | yes |
| `tools/drift-audit/selftest.py:4` | `@1.4` | no | yes |

### Migration

S4 is a value repair across five files, not a version bump: the constant does not move, so no
adopter's pin changes meaning.

### Alternatives rejected

Enumerating the sites in the checker: it is the shape that failed, and `TOOL-aBoundedVerdict-29`
already names derivation as the remedy.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one grep per entry over that entry's derived set.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry whose derived marker set is EMPTY must announce that,
  not pass silently.
- observability — the checker prints the derived count per entry and the allowance rows it honoured.
- risks — arming S2 before S4 reds the bar for every session in between, so they ship together.
- testing + left-shift gates — the assertion IS the gate; AC4 is its failing case.
- migration / rollback — none.
- user docs — none; the checker's header states what it now covers, including its BASIS by name.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-kit-versions.sh` runs at `HEAD` after this unit, all eight
  drift-audit marker sites read `1.8` and the leg exits 0.
- **AC2** — When one of the five previously-unasserted markers is edited to a wrong value,
  `bash tools/check-kit-versions.sh` exits non-zero and names that file, observed by staging the
  break and restoring it.
- **AC3** — When a file in the DECLARED reverse population carries a marker for an entry that neither
  claims it nor declares an allowance, `bash tools/check-kit-versions.sh` reds, observed on a fixture.
- **AC4** — The assertion is observed RED before S4's repair: arm S2 alone against current bytes and
  confirm `bash tools/check-kit-versions.sh` names all five stale files.
- **AC5** — When an entry declares a version constant and its derived marker set is empty,
  `bash tools/check-kit-versions.sh` prints that entry with a zero count rather than omitting it.
- **AC6** — AMENDED at build time, because the criterion as written would have passed for the wrong
  reason. Rendered DESTINATIONS are not in check 5c's population at all: `entry_members` returns an
  entry's claimed SOURCES, and a probe of `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`,
  `.claude/skills/unattended/SKILL.md` and `.claude/hooks/agent-cap.js` returns False for every one.
  So they never red — not because an exclusion is gated, but because they are never examined. That is
  green-by-absence and is recorded as a KNOWN GAP rather than reported as a pass: a rendered artifact
  carrying a stale marker is caught today only by `check-verdict-epoch.sh` and
  `tools/check-kit-versions.sh`, which cover memory-tree's rendered docs and nothing wider.
- **AC7** — The two `tools/workflows/drift-audit-*.js` markers pass under the declared allowance and
  red without it, observed by removing the allowance row.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `kit version markers` leg is the one this unit changes;
`govkit selfcheck` check 5b already reports registry-vs-checker disagreement in both directions.

## 8. Open questions

- **F1 — where the derivation lives.** `check-kit-versions.sh` is shell and the descriptors are TOML.
  Recommendation: `selfcheck`, which already holds check 5b and reads the registry.
  RESOLVED (agent, 2026-09-01, delegated): `selfcheck`, as check 5c beside 5b — it already parses
  every descriptor, and the shell checker cannot read TOML without help.
  `prior:` `TOOL-aBoundedVerdict-29` says the remedy should be DERIVED from `kit.toml`, not
  enumerated in prose; it does not say by which program.
- **F2 — whether a test fixture's marker counts.** `tools/memory-tree/check-verdict-epoch.test.sh:89`
  carries `gov:kit memory-tree@1.5` inside a `sed` mutating a scratch fixture. Recommendation:
  RESOLVED (agent, 2026-09-01, delegated): excluded from the derived set, and check 5c's own comment
  says so. `prior:` no prior ruling found.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit B2 and H7. The per-entry basis rev-1 specified
  structurally cannot reach two of the eight sites its own table lists, because `review-harness`
  claims `tools/workflows/**`; S1 now names `entry_members` as the basis and adds a declared
  cross-entry allowance, and §4 carries the whole problem. S3's reverse direction now declares its
  population — rev-1 named none, and the obvious grep is self-referential, returning this spec and
  its own review. AC6 and AC7 added.

- rev-3 · 2026-09-01 · BUILT and CLOSED as check 5c in `selfcheck`. F1 and F2 resolved. AC6
  AMENDED: rendered destinations are not in the population, so the criterion would have passed by
  absence; the gap is recorded rather than reported as coverage. The zero-marker note found SIX
  entries with no marker, not the five §1 predicted — `playbook` and `codebase-map` carry their
  version by other declared routes, so `DEPL-dGaugedVintage-5`'s real target is four.
  Acceptance ledger at `build/2026-09-01-build-DEPL-dGaugedVintage-4-acceptance-ledger.md`.
## 10. Reuse audit

- The seam is `entry_members` (`tools/govkit/govkit.py:356`) beside `resolve_entry` (`:282`), which
  `selfcheck` check 5b already uses to walk each entry's declared file set; this unit asserts over
  that walk rather than adding one. `python tools/codebase-map/reuse_lookup.py "assert every gov kit
  version marker site against its descriptor"` ranks `read_descriptors` first among descriptor-aware
  symbols in the same file.
- Recall terms used: `gov:kit marker population derive descriptor kit.toml check-kit-versions
  verdict-epoch remedy carriers bump sites`
