# DEPL-dGaugedVintage-5 — five entries an adopter cannot read a version out of

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 3 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-5-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-5-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`check-wiring`, `kickoff-manifest`, `playbook-render` and `review-harness` carry a version constant
and no `gov:kit <entry-id>@` token an adopter can grep. `tools/check-kit-versions.sh:84` calls the
marker the thing a deployer reads a kit's version from in an adopting tree, so for these four that
read returns nothing. `codebase-map` is a FIFTH case and a different one: it emits its version into
its generated artifacts instead, deliberately.

## 2. Scope (IN)

- **S1** — A `gov:kit <id>@<version>` marker added to one shipped file per affected entry, chosen so
  an adopter who installs that entry always receives the marker.
- **S2** — A `selfcheck` arm asserting that every entry declaring a version constant has at least one
  marker inside its own resolved file set. An entry declaring `version_from.none` is exempt by that
  declaration, not by omission.
- **S3** — CONSUME the exemption that already exists. `tools/govkit/entries/playbook.kit.toml:6`
  already declares `version_from = { ... kind = "marker" }`, and no code path reads `kind` today. S2
  reads it instead of special-casing `playbook`, and a descriptor omitting `kind` is NOT exempted.
- **S4** — `codebase-map`'s generated-artifact carrier is declared the same way, so the exemption set
  is a declaration rather than a list in the checker.

## 3. Non-goals (OUT)

- The stale drift-audit values. That is `DEPL-dGaugedVintage-4`, which owns the derivation this unit
  asserts against and is ordered beside it.
- Adding a constant to any of the ten entries that declare `version_from.none` with a reason. Their
  declaration is the answer and this unit does not overturn it.
- Deciding WHICH file carries the marker for each of the four. That is F1 and it is per-entry.
- Changing `check-kit-versions.sh`'s `need` list. S2 lives in `selfcheck`, where the registry is.

## 4. Design

### Inventory

| Entry | Constant | Markers today | Candidate carrier |
|---|---|---|---|
| `check-wiring` | `tools/check-wiring.sh:20` | none | the same file's header |
| `kickoff-manifest` | `skills/session-kickoff/manifest-check.sh:21` | none | the checker, which lands as `tools/manifest-check.sh` |
| `playbook-render` | `tools/playbook/render_playbook.py:621` | none | the renderer |
| `review-harness` | `tools/workflows/kit.toml:6` names `tier2-review.js` | only `gov:kit tier2-review@`, a NON-registry id | the same file, under its entry id |
| `codebase-map` | `tools/codebase-map/map_lib.py:48` | emits `codebase-map@<v>` into generated artifacts at `:1393`, `:1421`, `:1462` | ALREADY CARRIED — declare the artifact as its carrier |

`codebase-map` is not in the same state as the other four and rev-1 was wrong to group it.
`map_lib.py:46-47` says so in its own words: the version is mirrored "into the generated artifacts as
`codebase-map@<v>` so the deployer can grep the installed version", and `:1393`, `:1421` and `:1462`
write it into `inventories.json`, `symbols.json` and `MAP.md`. The read an adopter needs already
works; what is missing is a DECLARATION that this is its carrier, which is S4.

`review-harness` is the fifth entry and the awkward one: its files carry `gov:kit tier2-review@`,
which is not its registry id, so an entry-id grep finds nothing.

### Rollout

S1 and S2 land together. Arming S2 first would red the bar on all four until S1 lands, and a gate
whose steady state is red gets bypassed.

### Alternatives rejected

Placing every marker in each kit's README was rejected: `memory-recall` already does that and
`DEPL-dGaugedVintage-3`'s adopter shows a README is not guaranteed to be what a fork carries. The
carrier should be a file the entry cannot function without.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — S2 is a grep per entry over an already-resolved file set.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry with a `version_from.none` declaration must be reported
  as exempt-by-declaration, never skipped silently, so the exempt set stays visible.
- observability — `selfcheck` prints the per-entry marker count.
- risks — a marker placed in a file an adopter does not receive would satisfy S2 while failing its
  purpose, which is why S2 asserts membership of the RESOLVED set rather than mere existence.
- testing + left-shift gates — S2 is the gate; AC3 is its failing case.
- migration / rollback — none. Adding a comment marker changes no behaviour.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs after this unit, all four entries
  report a marker count of at least 1 and the command exits 0.
- **AC2** — When a deployer greps `gov:kit check-wiring@` in a tree that installed only that entry,
  the grep returns the entry's current version, observed on a scratch `apply` target.
- **AC3** — When the new marker is deleted from any one of the four, `python
  tools/govkit/govkit.py selfcheck` exits non-zero and names that entry, observed by staging the
  deletion and restoring it.
- **AC4** — When an entry declares `version_from.none`, the same run reports it exempt with its
  declared reason rather than omitting the row.
- **AC5** — AMENDED at build time. The criterion wanted `codebase-map` satisfied by a DECLARED
  generated-artifact carrier. It is instead satisfied the same way the other four are: `map_lib.py`
  already carried a bare `gov:kit codebase-map` pointer comment with no version, and it gained the
  `@1.3`. That is one mechanism for five entries rather than a second declaration read by one, and
  it puts the marker in the file the constant lives in, where check 5c keeps the pair true. S4's
  separate carrier declaration was therefore NOT built.
- **AC6** — A descriptor declaring `version_from` WITHOUT `kind` is not exempted:
  `python tools/govkit/govkit.py selfcheck` reds for it, observed by deleting `kind` from
  `tools/govkit/entries/playbook.kit.toml` on a fixture.
- **AC7** — `review-harness` reports under its own entry id: after this unit,
  `git grep -c 'gov:kit review-harness@'` is non-zero, or §3 names the follow-up that owns it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `kit version markers`.

## 8. Open questions

- **F1 — the carrier file per entry.** The table in §4 proposes one each. `kickoff-manifest` is the
  awkward one: its constant lives under `skills/` and lands at `tools/manifest-check.sh`, so the
  marker must survive that relocation. RESOLVED (agent, 2026-09-01, delegated): the constant's own
  file in every case, on the constant's own line, so the two cannot be bumped apart — and check 5c
  now fails if they are. `prior:` no prior ruling found.
- **F2 — whether `playbook`'s separate convention should be unified.** It uses
  `governance-template: vN.N` and `WIRE-INTO-PROJECT.md:87` documents that. Unifying means two
  markers on one file or a migration of every adopter's grep. RESOLVED (agent, 2026-09-01,
  delegated): the convention is left alone and the exception is DECLARED — check 5c consumes
  `version_from.kind = "marker"`, which `tools/govkit/entries/playbook.kit.toml:6` had already
  declared and nothing read. `prior:` `WIRE-INTO-PROJECT.md:87` documents the separate convention.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit H8, M5, M6. The affected set is five entries, not
  four: `review-harness` declares a version constant whose only marker is the non-registry id
  `tier2-review`. `codebase-map` was wrongly grouped with the unreadable entries — it deliberately
  emits `codebase-map@<v>` into its generated artifacts, so it needs a declared carrier, not a new
  token, and AC5 was rewritten. S3 now CONSUMES the marker-kind key that already exists at
  `tools/govkit/entries/playbook.kit.toml:6` and is read by nothing.

- rev-3 · 2026-09-01 · BUILT and CLOSED. Five entries gained a `gov:kit <entry-id>@` marker on
  their constant's own line, and `playbook` is exempt by the `version_from.kind` it already
  declared. check 5c's zero-marker NOTE became a REFUSAL. AC5 amended: `codebase-map` took the
  same marker as the others rather than a separate generated-artifact declaration, so S4 was not
  built. F1 and F2 resolved.
  Acceptance ledger at `build/2026-09-01-build-DEPL-dGaugedVintage-5-acceptance-ledger.md`.
## 10. Reuse audit

- The seam is the same one `DEPL-dGaugedVintage-4` extends — `read_descriptors` and `selfcheck`
  check 5b in `tools/govkit/govkit.py`, which already walks every entry's declared version file;
  `python tools/codebase-map/reuse_lookup.py "assert every gov kit version marker site against its
  descriptor"` ranks it first. This unit adds an arm to that walk rather than a second walk.
- Recall terms used: `gov:kit marker population derive descriptor kit.toml check-kit-versions
  verdict-epoch remedy carriers bump sites`
