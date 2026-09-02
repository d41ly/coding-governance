# TOOL-dRetiredFork-15 — five memory-tree values a project owns become declared keys

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

Four NicoCares carve-outs exist because a value a project owns is a literal in gov's checker, and a
fifth exists because check 4 does not consult the grandfather registry check 5 already reads. All
five sit in one file, `tools/memory-tree/check-memory-hygiene.sh`, which already presets thirty
values in one block — so the mechanism is present and these five were simply never added to it.

## 2. Scope (IN)

- **S1** — `BUILD_SLUG_RE`, defaulting to gov's current `^[A-Za-z][A-Za-z0-9-]*$`, bound into check
  4's awk as a fifth `-v` and validated: an empty or unanchored value must ABORT, not silently admit
  everything. Retires `nc carve-out 4/20`.
- **S2** — `PROJECT_REGISTRY_EXTRA`, whitespace-split into check 3's `bp` case default, so a project
  may ADD registries under `memory/project/` without editing the whitelist. Retires `nc 2/20`.
- **S3** — `RECORD_SERVES_CUTOFF`, applied as a date filter to check 21 branch A, added to
  `.memory-tree.conf.example` and to the kit's `[config] optional_keys`. Retires `nc 19/20`.
- **S4** — Check 4 consults `LEGACY_SET` the way check 5 already does at its `in_legacy` line, so a
  grandfathered build root is grandfathered in both checks. Retires `nc 7/20` with no new key.
- **S5** — `ENTRY_CAP_UNIT`, one of `chars` or `bytes`, joined to the existing `_capbad` validation
  loop beside `ENTRY_CAP_CHARS`. Retires `nc 1/20` as a DECLARED choice rather than an incidental
  `LC_ALL` export.
- **S6** — Each key's BLANK semantics chosen and STATED in the conf example: blank means gov's
  current behaviour for all five, so an adopter who never edits the file sees no change.
- **S7** — Bump `KIT_MEMORY_TREE_VERSION` and every paired marker.

## 3. Non-goals (OUT)

- Shipping gov's VALUES to adopters. `adopt-memory-tree.sh` scaffolds the conf with rows and gov's
  defaults only where a default is universal; a threshold measured on gov's corpus is vacuous or
  permanently red elsewhere, which is the class `memory/gotchas/pin-copied-from-another-corpus.md`
  records.
- `nc 3/20`. It needs no gov change: `memory/project/legacy-files.txt` already exists, is already
  wired into `LEGACY_SET`, is already whitelisted by check 3, and NicoCares' copy holds one comment
  and zero entries. `DEPL-dRetiredFork-7` tells them; gov builds nothing.
- Any key that can drive a violation count to zero. `PROJECT_REGISTRY_EXTRA` adds to a whitelist and
  is bounded by the tree's own contents; a threshold key is a different animal and none is added here.

## 4. Design

### Data model

All five are shell variables in the existing preset block, read from `.memory-tree.conf`, validated
in the existing `_capbad`-style loop. No new file, no new parser, no new read path.

### Migration

Every key defaults to gov's current behaviour, so gov's own bar is unchanged and every adopter's
first run after the pull is identical to their last run before it. NicoCares then deletes five
carve-outs and writes five conf lines, which is a data edit in its tree.

### Alternatives rejected

A single `PROJECT_OVERRIDES` table. It makes the validation loop generic, which means it cannot
validate: `BUILD_SLUG_RE` must be anchored and `ENTRY_CAP_UNIT` must be one of two words, and a
generic reader can check neither.

## 5. Production-readiness checklist

- security — a conf value reaches an awk `-v` binding. `BUILD_SLUG_RE` is a regex supplied by the
  target and must not be able to leave its argument; validate anchoring and reject a value that is
  not a well-formed ERE, which is also the substrate `TOOL-aSiftedFork-3` names for `FAMILIES`.
- perf / scale — five variable reads at startup.
- a11y — N/A.
- i18n — `ENTRY_CAP_UNIT` IS the i18n item: byte semantics versus character semantics is what
  `nc 1/20` is about, and making it declared is what stops it being an incidental locale export.
- error / empty / loading states — blank means gov's default for every key, stated in the example.
  An INVALID value aborts; the two are different and must not collapse.
- observability — the run prints any key whose value differs from the shipped default, so a
  divergent configuration is visible without reading the conf.
- risks — a mis-anchored `BUILD_SLUG_RE` silently admits everything. Mitigated by S1's validation
  and by an arm that observes the abort.
- testing + left-shift gates — one arm per key for default, valid-override and invalid-override.
- migration / rollback — additive and defaulted; reverting is deleting five reads.
- user docs — `.memory-tree.conf.example` and `tools/memory-tree/README.md`.

## 6. Acceptance criteria

- **AC1** — When no key is set, `bash tools/memory-tree/check-memory-hygiene.sh` output is
  byte-identical to the pre-change run over gov's tree.
- **AC2** — When `BUILD_SLUG_RE="^[A-Za-z]+$"` is set, check 4 rejects a build folder carrying a
  digit, and gov's own folders still pass under the default.
- **AC3** — When `BUILD_SLUG_RE` is unanchored or empty, the checker ABORTS naming the key.
- **AC4** — When `PROJECT_REGISTRY_EXTRA` names a file, check 3 stops reporting it as unexpected.
- **AC5** — When `RECORD_SERVES_CUTOFF` is set, check 21 branch A grades only records dated on or
  after it.
- **AC6** — When a build root carries a `legacy-files.txt` row, check 4 grandfathers it as check 5
  already does.
- **AC7** — When `ENTRY_CAP_UNIT=bytes`, check 7 counts bytes, and the default counts as today.
- **AC8** — `bash tools/check-kit-versions.sh` exits `0` and `bash tools/memory-tree/kit-dogfood-parity.test.sh`
  passes after the bump.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `kit version markers` ·
`verdict epoch (kit version dates the engine)`.

## 8. Open questions

- **F1 — does `ENTRY_CAP_UNIT` belong here at all?** gov's own check-7 comment says it deliberately
  sets no locale, because pinning one "would silently re-decide the cap on any adopter whose awk
  counts characters today". A DECLARED key with a blank default does not re-decide anything, which is
  the difference. Recommendation: build it, and quote that comment in the conf example so the next
  reader sees why the default is blank rather than `chars`.
- **F2 — is `RECORD_SERVES_CUTOFF` a cutoff or a grandfather list?** NicoCares measured 549 landed
  records with no `Serves` line. A cutoff is one value; a list is 549 rows. Recommendation: cutoff,
  matching the five cutoffs already in `.memory-tree.conf`.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from the dRetiredFork classification of `nc carve-out` 1, 2, 4,
  7 and 19.

## 10. Reuse audit

The seam is the preset-and-validate block in `tools/memory-tree/check-memory-hygiene.sh`, which
already holds thirty values and the `_capbad` validation loop — `reuse_lookup.py` reports no separate
config-reading helper in the corpus, and every kit reads its own conf inline by house rule, so this
unit adds rows to a live mechanism rather than building one.

Recall terms used: `memory-tree`, `conf key`, `preset`, `cutoff`, `LEGACY_SET`, `pop_guard`,
`grandfather`, `check 21`, `Serves`, `entry cap`, `adopter`, `carve-out`, `vacuous`, `pin`.
